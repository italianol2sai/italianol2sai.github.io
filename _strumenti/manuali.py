"""Pagina per l'insegnante: «Dal manuale al sito» (Erila, 2026-11-23: «per le copie dei manuali, trova un modo per farmele
trovare rapidamente»). Per ogni manuale mandato da Erila elenca le pagine del sito rifatte sui suoi argomenti, con lezione,
esercizi e giochi. Non è linkata dalla home (si apre da https://italianol2sai.github.io/manuali.html).
Uso: python3 _strumenti/manuali.py   (si rilancia ogni volta che si aggiunge un'unità; i titoli vengono da elenco.html)"""
import glob, html, os, re

RADICE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.chdir(RADICE)

# titoli dalle voci di elenco.html
TITOLI = {}
for href, strong in re.findall(r'<a class="item" href="([^"]+)">.*?<strong>(.*?)</strong>', open("elenco.html", encoding="utf-8").read(), re.S):
    TITOLI.setdefault(href, re.sub(r"<.*?>", "", strong).strip())

def titolo(href):
    if href in TITOLI:
        return TITOLI[href]
    try:
        t = re.search(r"<title>(.*?)</title>", open(href if not href.endswith("/") else href + "index.html", encoding="utf-8").read(), re.S).group(1)
        return re.sub(r"\s*[-·]\s*ITALIANO L2.*$", "", html.unescape(t)).strip()
    except Exception:
        return href

def unita(cartella):
    """una cartella-unità: lezione + esercizi + giochi se ci sono"""
    out = [("📘 Lezione", cartella + "/")] if os.path.exists(cartella + "/index.html") else []
    for f, n in [("esercizi.html", "📱 Esercizi"), ("giochi.html", "🎲 Giochi")]:
        if os.path.exists("%s/%s" % (cartella, f)):
            out.append((n, "%s/%s" % (cartella, f)))
    return out

def pagine(pattern):
    return [(titolo(p), [("📱 Apri", p)]) for p in sorted(glob.glob(pattern))]

# --- Nuovo Senza frontiere: tutte le unità del libro, con la pagina del sito quando c'è ---
SF = {
 "Senza frontiere Alfabetizzazione (Edilingua)": ("Alfa", [
   ("Ciao, io sono", "alfa-ciao-io-sono"), ("Vado al corso", "alfa-vado-al-corso"), ("La mia giornata", "alfa-la-mia-giornata"),
   ("Mi descrivo", "alfa-mi-descrivo"), ("Le mie emozioni", "alfa-le-mie-emozioni"), ("La mia salute", "alfa-la-mia-salute"),
   ("La mia casa", "alfa-la-mia-casa"), ("Cerco casa", "alfa-cerco-casa"), ("Mi scusi, dov'è…?", "alfa-mi-scusi-dove"),
   ("In giro per la città", "alfa-in-giro-per-la-citta"), ("Faccio la spesa", "alfa-faccio-la-spesa"), ("Cerco lavoro", "alfa-cerco-lavoro"),
   ("Quale lavoro?", "alfa-quale-lavoro"), ("Cosa fai domani?", "alfa-cosa-fai-domani")]),
 "Nuovo Senza frontiere 2 · A2 (Edilingua)": ("A2", [
   ("La salute", "a2-la-salute"), ("La convivenza", "a2-la-convivenza"), ("Il tempo", "a2-il-tempo"), ("Il lavoro", "a2-il-lavoro"),
   ("La mia storia", "a2-la-mia-storia"), ("Racconti", "a2-racconti"), ("Come eravamo", "a2-come-eravamo"), ("Cambiare vita", "a2-cambiare-vita"),
   ("I desideri", "a2-i-desideri"), ("I progetti", "a2-i-progetti"), ("La tecnologia", "a2-la-tecnologia"), ("L'ambiente", "a2-l-ambiente")]),
 "Nuovo Senza frontiere 3 · B1 (Edilingua)": ("B1", [
   ("La cittadinanza italiana", "b1-cittadinanza"), ("Esame B1 per la cittadinanza", "b1-esame-cittadinanza"), ("Il mondo digitale", "b1-mondo-digitale"),
   ("La denuncia", "b1-la-denuncia"), ("Sono una mediatrice culturale", "b1-mediatrice"), ("Trasferirsi per lavoro", "b1-trasferirsi"),
   ("Lavoro come elettricista", "b1-elettricista"), ("I diritti sul lavoro", "b1-diritti-lavoro"), ("Studiando si impara", "b1-studiando"),
   ("Scuola e famiglia", "b1-scuola-famiglia"), ("La scuola superiore", "b1-scuola-superiore"), ("Libri e viaggi", "b1-libri-viaggi")]),
}

def sf_righe(liv, elenco):
    righe = []
    for i, (nome, cart) in enumerate(elenco, 1):
        righe.append(("Unità %d · %s" % (i, nome), unita(cart)))
    return righe

ALTRI = [
 ("Italiano anch'io (Ornimi) · eserciziario A1", "A1", pagine("eserciziario-a1/scheda-*.html")),
 ("Italiano anch'io (Ornimi) · pagine «In Italia» ed Educazione civica", "A1/A2",
  [(titolo(c + "/"), unita(c)) for c in ["condominio", "autocertificazione", "piatti-dal-mondo", "volontariato", "in-strada", "cup-specialisti",
                                          "tasse", "centro-periferia", "feste-repubblica", "unione-europea", "stato-italiano", "enti-locali"]]),
 ("In alto! A1-A2 (Ornimi) · percorso in 13 unità", "A1/A2", pagine("percorso-a1-a2/unita-*.html")),
 ("Videogrammatica in alto! (Ornimi) · regole ed esercizi", "A1/A2", pagine("grammatica/*.html")),
 ("Nuovo Espresso 1 e Dieci A1/A2", "A1/A2", [(titolo(c + "/"), unita(c)) for c in ["tempo-libero", "ristorante", "feste", "in-vacanza"]]),
 ("Nuovo Contatto B1", "B1", [(titolo(c + "/"), unita(c)) for c in ["b1-cronaca", "b1-vacanze", "b1-tempo-libero", "b1-lavoro", "b1-problemi"]]),
 ("Nuovo Espresso 3-6", "B1-C2", pagine("avanzato/*.html")),
 ("L'italiano per la cucina", "A2", pagine("cucina-pro/*.html")),
 ("Come si dice…? (Giunti)", "A1/A2", [(titolo(c + "/"), unita(c)) for c in ["bar", "treno", "posta-banca", "farmacia", "comune-questura"]]),
 ("L'ABC dell'edilizia · Meet the Need · dizionario visivo del cibo", "A1/A2",
  [(titolo(c + "/"), unita(c)) for c in ["cantiere", "assistente-familiare", "cucina-lavoro", "carne-pesce"]]),
]

def riga(nome, link):
    if not link:
        return '<li class="todo"><span>%s</span><em>in preparazione</em></li>' % html.escape(nome)
    return '<li><span>%s</span><span class="l">%s</span></li>' % (
        html.escape(nome), " ".join('<a href="%s">%s</a>' % (h, n) for n, h in link))

def blocco(titolo_, liv, righe, aperto=False):
    fatte = sum(1 for _, l in righe if l)
    return ('<details%s><summary><b>%s</b> <span class="liv">%s</span> <span class="n">%d/%d</span></summary><ul>%s</ul></details>'
            % (" open" if aperto else "", html.escape(titolo_), liv, fatte, len(righe), "".join(riga(n, l) for n, l in righe)))

corpo = "".join(blocco(t, liv, sf_righe(liv, el), True) for t, (liv, el) in SF.items())
corpo += "".join(blocco(t, liv, r) for t, liv, r in ALTRI)

PAGINA = """<!doctype html>
<html lang="it"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="robots" content="noindex"><title>Dal manuale al sito</title>
<link rel="icon" href="/favicon.ico">
<style>
:root{--bg:#f6f7fb;--card:#fff;--ink:#1f2933;--muted:#6b7280;--line:#e3e6ee;--accent:#0f766e;--todo:#b45309}
@media (prefers-color-scheme:dark){:root{--bg:#14171c;--card:#1e232a;--ink:#eef1f4;--muted:#9aa3ad;--line:#333a43;--accent:#2dd4bf;--todo:#fbbf24}}
body{margin:0;background:var(--bg);color:var(--ink);font:17px/1.5 system-ui,-apple-system,"Segoe UI",Roboto,sans-serif}
main{max-width:860px;margin:0 auto;padding:20px 16px 60px}
h1{font-size:26px;margin:6px 0} .sub{color:var(--muted);margin:0 0 16px}
input{width:100%%;box-sizing:border-box;font:inherit;padding:10px 14px;border:2px solid var(--line);border-radius:12px;background:var(--card);color:var(--ink);margin-bottom:14px}
details{background:var(--card);border:1px solid var(--line);border-radius:14px;margin-bottom:10px;padding:4px 14px}
summary{cursor:pointer;padding:8px 0} .liv{background:var(--accent);color:#fff;border-radius:8px;padding:1px 8px;font-size:13px;font-weight:700}
.n{color:var(--muted);font-size:14px;float:right}
ul{list-style:none;margin:0;padding:0 0 8px} li{display:flex;flex-wrap:wrap;gap:6px 12px;justify-content:space-between;padding:7px 0;border-top:1px dashed var(--line)}
li .l{display:flex;gap:6px;flex-wrap:wrap} a{color:var(--accent);text-decoration:none;font-weight:600;font-size:15px;border:1px solid var(--line);border-radius:8px;padding:2px 8px}
li.todo span{color:var(--muted)} li.todo em{color:var(--todo);font-size:14px} .nascosto{display:none}
a.back{border:none;padding:0;color:var(--muted);font-weight:400}
</style></head><body><main>
<a class="back" href="./">← Tutti i materiali</a>
<h1>📚 Dal manuale al sito</h1>
<p class="sub">Per l'insegnante: per ogni libro, le pagine del sito rifatte sui suoi argomenti (testi ed esercizi nuovi). Cerca per titolo o argomento.</p>
<input id="q" type="search" placeholder="Cerca: salute, passato prossimo, unità 3…" autocomplete="off">
%s
</main>
<script>
const q=document.getElementById('q');
q.addEventListener('input',()=>{const t=q.value.trim().toLowerCase();
 document.querySelectorAll('details').forEach(d=>{let vis=0;
  d.querySelectorAll('li').forEach(li=>{const ok=!t||li.textContent.toLowerCase().includes(t)||d.querySelector('summary').textContent.toLowerCase().includes(t);
   li.classList.toggle('nascosto',!ok); if(ok) vis++;});
  d.classList.toggle('nascosto',!vis); if(t) d.open=vis>0;});});
</script>
</body></html>
"""
open("manuali.html", "w", encoding="utf-8").write(PAGINA % corpo)
print("scritto manuali.html")
