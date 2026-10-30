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
        if "audio" in s:
            s["audio"] = enc(s["audio"])
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
    from unita_classroom2 import CUCINA, CASA as CASA_PAROLE, VESTITI, PRIMI as PRIMI_PAROLE, CULTURA, MISTO
    from unita_classroom import FAMIGLIA, GIORNATA, DIAL_DOTTORE, LAVORO, NEGOZIO, INDOVINA, MACCHINA
    from unita_primi import DATI, ORE, EURO, MERCATO
    from unita_primi2 import ESERCIZI2
    from unita_alimentare import A1 as ALIM_A1, A2 as ALIM_A2
    from unita_civica import ESERCIZI_CIVICA
    from unita_drive import ESERCIZI_DRIVE
    from unita_libri import ESERCIZI_LIBRI
    from unita_esami import ESAMI
    from unita_simulazioni import SIMULAZIONI
    from unita_b2c1 import SIM_B2C1
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
    build("letture/famiglia.html", FAMIGLIA)
    build("letture/giornata.html", GIORNATA)
    build("letture/dottore.html", DIAL_DOTTORE)
    build("letture/lavoro.html", LAVORO)
    build("letture/negozio.html", NEGOZIO)
    build("letture/indovina-chi.html", INDOVINA)
    build("dati-personali/esercizi.html", DATI)
    build("ore-giorni/esercizi.html", ORE)
    build("euro/esercizi.html", EURO)
    build("mercato/esercizi.html", MERCATO)
    for cartella, dati in ESERCIZI2 + ESERCIZI_CIVICA + ESERCIZI_DRIVE + ESERCIZI_LIBRI:
        build(cartella + "/esercizi.html", dati)
    build("parole/cucina.html", CUCINA)
    build("mangiare-sano/esercizi.html", ALIM_A1)
    build("mangiare-sano/letture.html", ALIM_A2)
    build("parole/casa.html", CASA_PAROLE)
    build("parole/vestiti.html", VESTITI)
    build("parole/colori-numeri-emozioni.html", PRIMI_PAROLE)
    build("quiz/cultura.html", CULTURA)
    build("quiz/misto.html", MISTO)
    build("letture/macchina.html", MACCHINA)
    from unita_b1 import UNITA as B1  # le slide B1: python3 _strumenti/unita_b1.py
    for cartella, _, _, dati in B1:
        build(cartella + "/esercizi.html", dati)
    os.makedirs("esami", exist_ok=True)
    for path, dati in ESAMI + SIMULAZIONI + SIM_B2C1:
        build(path, dati)
