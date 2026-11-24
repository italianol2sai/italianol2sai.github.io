"""Schede da stampare (per l'insegnante, NON per il sito).

Per ogni unità di Nuovo Senza frontiere legge window.DATA da <cartella>/esercizi.html e scrive due pagine HTML:
  <cartella>/_stampa-esercizi.html   scheda per lo studente (senza soluzioni)
  <cartella>/_stampa-soluzioni.html  soluzioni + testi degli ascolti (per l'insegnante)
Poi stampa.js le trasforma in PDF e le cancella. I file _stampa-* non vanno mai pubblicati.
Uso: python3 _strumenti/stampa.py [cartella ...]
"""
import base64, glob, html, json, os, re, sys

LIV = {
    "alfa": ("Alfabetizzazione", "Atkinson+Hyperlegible:wght@400;700", "'Atkinson Hyperlegible'", "15.5pt", "#1f6fb2"),
    "a2": ("Livello A2", "Nunito:wght@400;700;800", "Nunito", "12.5pt", "#2a7f62"),
    "b1": ("Livello B1", "Source+Sans+3:wght@400;600;700&family=Merriweather:wght@400;700", "'Source Sans 3'", "11.5pt", "#5b3ea6"),
}

CSS = """
@page{size:A4;margin:13mm 13mm 15mm}
*{box-sizing:border-box;-webkit-print-color-adjust:exact;print-color-adjust:exact}
body{font-family:%(font)s,'DejaVu Sans',sans-serif;font-size:%(size)s;line-height:1.45;color:#1d1d1d;margin:0}
body.upper{text-transform:uppercase}
header{display:flex;justify-content:space-between;align-items:flex-end;border-bottom:3px solid %(col)s;padding-bottom:6px;margin-bottom:10px}
header h1{margin:0;font-size:1.55em;color:%(col)s} header small{color:#555;font-size:.7em;letter-spacing:.5px}
.nome{margin:4px 0 12px;font-size:.95em} .nome span{display:inline-block;border-bottom:1.5px solid #333;width:12em;margin:0 1.2em 0 .3em}
.part{background:%(col)s;color:#fff;font-weight:700;padding:4px 10px;border-radius:6px;margin:16px 0 8px;break-after:avoid}
.teoria{border:2px solid %(col)s;border-radius:8px;padding:8px 12px;margin:6px 0 10px;break-inside:avoid}
.teoria>b:first-child{display:block;color:%(col)s;margin-bottom:4px}
.teoria table{border-collapse:collapse;margin:6px 0} .teoria td,.teoria th{border:1px solid #999;padding:2px 8px;text-align:left}
.es{margin:10px 0 14px;break-inside:avoid} .es.lungo{break-inside:auto}
h3{font-size:1.05em;margin:0 0 4px;color:%(col)s;break-after:avoid}
.cons{font-style:italic;margin:0 0 6px;color:#333}
.box{border:1.5px dashed #777;border-radius:6px;padding:5px 10px;margin:4px 0 8px}
.ascolta{font-weight:700}
ol.it{list-style:none;padding:0;margin:0} ol.it>li{margin:5px 0;break-inside:avoid}
.opz{display:inline-flex;flex-wrap:wrap;gap:4px 16px;margin-left:8px}
.opz span::before{content:"";display:inline-block;width:.8em;height:.8em;border:1.5px solid #333;border-radius:50%%;margin-right:5px;vertical-align:-1px}
.full .opz{display:flex;margin:2px 0 0 18px}
.riga{display:inline-block;border-bottom:1.5px solid #333;min-width:7em;height:1.1em;vertical-align:baseline;margin:0 3px}
.riga.m{min-width:10em} .riga.l{min-width:16em} .riga.xl{display:block;width:100%%;margin:4px 0 0}
.righe div{border-bottom:1.2px solid #555;height:1.9em}
.quad{display:inline-block;width:1.6em;height:1.4em;border:1.5px solid #333;border-radius:4px;margin-right:8px;vertical-align:middle}
.emo{font-size:1.8em;line-height:1}
.parla{border-left:4px solid %(col)s;padding-left:8px}
img{max-width:100%%;max-height:55mm}
.risp{margin:2px 0 4px;line-height:1.7} .sol .es{margin:6px 0 10px}
.trascr{font-size:.9em;border-left:3px solid #999;padding-left:8px;margin:4px 0}
footer{margin-top:14px;font-size:.7em;color:#777;text-align:center;text-transform:none}
"""


def dec(s):
    return json.loads(base64.b64decode(s).decode("utf-8"))


def say_to_icon(q):
    """🔊 button -> plain icon (the teacher reads the word: it is in the soluzioni)."""
    return re.sub(r'<button[^>]*class="say"[^>]*>.*?</button>', "🔊", q or "", flags=re.S)


def says(q):
    return re.findall(r'data-say="([^"]*)"', q or "")


def riga(w):
    return '<span class="riga %s"></span>' % {"s": "", "m": "m", "l": "l"}.get(w or "s", "m")


def opz(o):
    return '<span class="opz">' + "".join("<span>%s</span>" % x for x in o) + "</span>"


def esercizio(ex):
    t = ex.get("type")
    out = ['<div class="es%s"><h3>%s</h3>' % (" lungo" if len(ex.get("items", [])) > 8 else "", ex["title"])]
    cons = ex.get("cons")
    if cons:
        cons = cons.replace("TOCCA 🔊.", "ASCOLTA L'INSEGNANTE.").replace("Tocca 🔊.", "Ascolta l'insegnante.")
        out.append('<p class="cons">%s</p>' % cons)
    if ex.get("audio"):
        out.append('<p class="ascolta">🎧 ASCOLTA L\'INSEGNANTE.</p>')
    if ex.get("info"):
        out.append('<div class="box">%s</div>' % say_to_icon(ex["info"]))
    if ex.get("bank"):
        out.append('<div class="box">%s</div>' % ex["bank"])
    items = ex.get("items", [])
    if t == "choice":
        out.append('<ol class="it">')
        for it in items:
            o = it.get("opts") or ex.get("opts") or []
            cls = ' class="full"' if ex.get("full") else ""
            out.append("<li%s>%s %s</li>" % (cls, say_to_icon(it.get("q", "")), opz(o)))
        out.append("</ol>")
    elif t == "select":
        out.append('<div class="box">%s</div><ol class="it">' % " · ".join(ex["opts"]))
        for it in items:
            out.append("<li>%s %s</li>" % (say_to_icon(it.get("q", "")), riga("l")))
        out.append("</ol>")
    elif t == "text":
        out.append('<ol class="it">')
        for it in items:
            w = it.get("w") or ex.get("w")
            out.append("<li>%s %s%s%s</li>" % (say_to_icon(it.get("q", "")), it.get("pre", ""), riga(w), it.get("post", "")))
        out.append("</ol>")
    elif t == "cloze":
        s = "".join(riga("m") if isinstance(p, dict) else p for p in ex["parts"])
        out.append('<div style="line-height:2.1">%s</div>' % s)
    elif t == "order":
        out.append('<ol class="it">' + "".join('<li><span class="quad"></span>%s</li>' % x for x in items) + "</ol>")
    elif t == "free":
        for lab in items:
            out.append("<p><b>%s</b></p><div class=\"righe\">%s</div>" % (lab, "<div></div>" * int(ex.get("rows", 4))))
    elif t == "record":
        out.append('<p class="cons">🗣️ Parla con l\'insegnante o con un compagno.</p>')
        out.append("".join('<p class="parla">%s</p>' % x for x in items))
    out.append("</div>")
    return "".join(out)


def soluzione(ex):
    righe = []
    for it in ex.get("items", []):
        if isinstance(it, dict):
            w = says(it.get("q"))
            if w:
                righe.append(w)
    k = dec(ex["k"]) if ex.get("k") else []
    if not k and not ex.get("audio") and not righe and not says(ex.get("info")):
        return ""
    out = ['<div class="es"><h3>%s</h3>' % ex["title"]]
    letti = [w for r in righe for w in r] or says(ex.get("info"))
    if letti:
        out.append('<p class="trascr">L\'insegnante legge: %s</p>' % " · ".join(letti))
    if ex.get("audio"):
        a = dec(ex["audio"])
        a = [["", a]] if isinstance(a, str) else a
        out.append('<div class="trascr"><b>Testo dell\'ascolto</b><br>%s</div>' % "<br>".join(
            "– " + html.escape(x) for s, x in a))
    if k:
        def alt(a):
            v = []
            for x in map(str, a["a"]):
                if x.lower() not in [y.lower() for y in v]:
                    v.append(x)
            return " / ".join(v)
        out.append('<p class="risp">' + " &nbsp;·&nbsp; ".join("<b>%d.</b> %s" % (i + 1, alt(a)) for i, a in enumerate(k)) + "</p>")
    out.append("</div>")
    return "".join(out)


def pagina(d, liv, corpo, titolo, upper, nome=True):
    nl, font_url, font, size, col = LIV[liv]
    css = CSS % {"font": font, "size": size, "col": col}
    testa = ('<header><h1>%s</h1><small>ITALIANO L2 · %s</small></header>' % (titolo, nl.upper()))
    nm = ('<p class="nome">NOME<span></span>DATA<span></span></p>' if nome else "")
    return ("<!doctype html><html lang='it'><head><meta charset='utf-8'><title>%s</title>"
            "<link rel='stylesheet' href='https://fonts.googleapis.com/css2?family=%s&display=swap'>"
            "<style>%s</style></head><body class='%s'>%s%s%s<footer>italianol2sai.github.io · Autoapprendimento Italiano L2 ETNIE</footer></body></html>"
            % (html.escape(titolo), font_url, css, "upper" if upper else "", testa, nm, corpo))


def unita(cartella):
    t = open(os.path.join(cartella, "esercizi.html"), encoding="utf-8").read()
    d = json.loads(re.search(r"window\.DATA = (\{.*?\});?\s*</script>", t, re.S).group(1))
    liv = d.get("livello") or cartella.split("-")[0]
    titolo = d["title"].replace(" · Esercizi", "")
    es, sol = [], []
    for ex in d["sections"]:
        if "part" in ex and "type" not in ex:
            es.append('<div class="part">%s</div>' % ex["part"])
            if ex.get("teoria"):
                es.append('<div class="teoria"><b>📘 %s</b>%s</div>' % ("LA REGOLA" if d.get("upper") else "La regola", ex["teoria"]))
            continue
        es.append(esercizio(ex))
        s = soluzione(ex)
        if s:
            sol.append(s)
    up = bool(d.get("upper"))
    open(os.path.join(cartella, "_stampa-esercizi.html"), "w", encoding="utf-8").write(
        pagina(d, liv, "".join(es), titolo + (" · ESERCIZI" if up else " · Esercizi"), up))
    open(os.path.join(cartella, "_stampa-soluzioni.html"), "w", encoding="utf-8").write(
        pagina(d, liv, "".join(sol), titolo + (" · SOLUZIONI" if up else " · Soluzioni"), up, nome=False))
    return cartella


if __name__ == "__main__":
    cartelle = sys.argv[1:] or sorted(c for c in (os.path.dirname(f) for f in glob.glob("*/esercizi.html"))
                                      if c.startswith(("alfa-", "a2-", "b1-")))
    for c in cartelle:
        print("scritto", unita(c))
