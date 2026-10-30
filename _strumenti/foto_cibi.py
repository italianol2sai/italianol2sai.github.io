"""Foto vere dei cibi (Wikimedia Commons, licenze libere), scelte il 2026-10-30 al posto delle emoji sbagliate.
Le foto stanno in comune/cibi/<nome>.jpg (600 px); autore e licenza di ognuna in _strumenti/crediti-cibi.csv.
CC BY e CC BY-SA chiedono di citare l'autore: ogni unità che usa le foto ha una slide «Le foto» con i crediti,
e negli esercizi il credito è sotto la foto."""
import csv, os

CREDITI = {}
with open(os.path.join(os.path.dirname(__file__), "crediti-cibi.csv"), encoding="utf-8") as fh:
    for r in csv.DictReader(fh, delimiter=";"):
        CREDITI[r["file"][:-4]] = r

FOTO_CSS = """
  .card .emoji img.cibo{display:block; width:100%; max-width:220px; margin:0 auto; height:120px; object-fit:cover; border-radius:12px; margin-bottom:6px;}
  table.plur td img.cibo{display:block; width:110px; height:80px; object-fit:cover; border-radius:10px;}
  .crediti{font-size:.8rem !important; text-transform:none; letter-spacing:0; line-height:1.5; columns:2; column-gap:24px; text-align:left;}
  .crediti a{color:inherit;}
  @media (max-width:900px){ .card .emoji img.cibo{height:90px; max-width:160px;} table.plur td img.cibo{width:70px; height:56px;} .crediti{columns:1;} }"""

def foto(nome, alt=""):
    assert nome in CREDITI, nome
    return '<img class="cibo" src="../comune/cibi/%s.jpg" alt="%s" loading="lazy">' % (nome, alt)

def _lic(r):
    lic = r["licenza"]
    if r["url_licenza"]:
        lic = '<a href="%s" target="_blank" rel="noopener">%s</a>' % (r["url_licenza"], lic)
    return lic

def autore(r):
    """alcuni autori su Commons hanno un testo lunghissimo: teniamo solo il nome"""
    a = r["autore"].split(" (")[0].split(" I'd ")[0].strip()
    return a if len(a) <= 40 else a[:38].rstrip() + "…"

def credito(nome):
    r = CREDITI[nome]
    return ('Foto: <a href="%s" target="_blank" rel="noopener">%s</a>, Wikimedia Commons, %s'
            % (r["pagina_commons"], autore(r), _lic(r)))

def crediti_slide(nomi):
    righe = "".join('<div>%s · <a href="%s" target="_blank" rel="noopener">%s</a> · %s</div>'
                    % (n.replace("-", " "), CREDITI[n]["pagina_commons"], autore(CREDITI[n]), _lic(CREDITI[n])) for n in nomi)
    return '    <div class="nota crediti">%s</div>' % righe

def foto_quiz(eid, title, short, items, opts, cons="GUARDA LA FOTO. CHE COS'È?"):
    """items: (nome della foto, risposta giusta). Esercizio a menu con le foto vere e il credito sotto."""
    from genera import eq
    return {"id": eid, "title": title, "short": short, "type": "select", "opts": opts, "cons": cons,
            "items": [{"q": '<img src="../comune/cibi/%s.jpg" alt="" loading="lazy" style="width:100%%;max-width:200px;height:130px;'
                            'object-fit:cover;border-radius:12px;display:block;margin-bottom:4px">'
                            '<small style="text-transform:none;font-size:.65rem;color:#7a6a5a;display:block;max-width:200px;line-height:1.3">%s</small><br>%d.' % (n, credito(n), i + 1)}
                      for i, (n, _) in enumerate(items)],
            "k": [eq(a) for _, a in items]}
