"""Crea le pagine di esercizi interattivi a partire dai dati qui sotto.
Uso: python3 _strumenti/genera.py   (dalla cartella principale del sito)
Le risposte vengono codificate in base64 dentro la pagina e non sono mai mostrate.
La cartella _strumenti non viene pubblicata da GitHub Pages."""
import base64, json, os, sys

sys.path.insert(0, os.path.dirname(__file__))

def eq(*a): return {"t": "eq", "a": list(a)}
def has(*a): return {"t": "has", "a": list(a)}
def all_(*groups): return {"t": "all", "a": [list(g) for g in groups]}

def enc(k): return base64.b64encode(json.dumps(k, ensure_ascii=False).encode()).decode()

PAGE = """<!doctype html>
<html lang="it">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<link rel="stylesheet" href="../comune/stile.css">
</head>
<body>
<main id="app"></main>
<script>window.DATA = {data};</script>
<script src="../comune/motore.js"></script>
</body>
</html>
"""

def build(path, data):
    out = dict(data)
    secs = []
    for s in data["sections"]:
        s = dict(s)
        if "k" in s:
            s["k"] = enc(s["k"])
        secs.append(s)
    out["sections"] = secs
    js = json.dumps(out, ensure_ascii=False, indent=1)
    with open(path, "w") as f:
        f.write(PAGE.format(title=data["title"].replace("&", "&amp;"), data=js))
    print("scritto", path)

if __name__ == "__main__":
    from unita_corpo import CORPO
    from unita_casa import CASA
    from unita_saluti import SALUTI
    from unita_presente import PRESENTE
    from unita_nomi import NOMI
    from unita_aggettivi import AGGETTIVI
    from unita_possessivi import POSSESSIVI
    from unita_frase import FRASE
    from unita_cardinali import CARDINALI
    from unita_domande import DOMANDE
    from unita_passato import PASSATO
    from unita_modali import MODALI
    from unita_riflessivi import RIFLESSIVI
    from unita_preposizioni import PREPOSIZIONI
    from unita_pronomi import PRONOMI
    from unita_lavoro import CHE_LAVORO, CERCARE, CV, COLLOQUIO, BUSTA
    build("corpo-dottore/esercizi.html", CORPO)
    build("cercare-casa/esercizi.html", CASA)
    build("saluti/esercizi.html", SALUTI)
    build("presente/esercizi.html", PRESENTE)
    build("nomi-articoli/esercizi.html", NOMI)
    build("aggettivi/esercizi.html", AGGETTIVI)
    build("possessivi/esercizi.html", POSSESSIVI)
    build("frase-minima/esercizi.html", FRASE)
    build("punti-cardinali/esercizi.html", CARDINALI)
    build("domande/esercizi.html", DOMANDE)
    build("passato-prossimo/esercizi.html", PASSATO)
    build("modali/esercizi.html", MODALI)
    build("riflessivi/esercizi.html", RIFLESSIVI)
    build("preposizioni/esercizi.html", PREPOSIZIONI)
    build("pronomi/esercizi.html", PRONOMI)
    build("che-lavoro-fai/esercizi.html", CHE_LAVORO)
    build("cercare-lavoro/esercizi.html", CERCARE)
    build("curriculum/esercizi.html", CV)
    build("colloquio-contratti/esercizi.html", COLLOQUIO)
    build("busta-paga/esercizi.html", BUSTA)
