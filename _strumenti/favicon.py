"""Mette la favicon (e l'immagine di condivisione) in tutte le pagine .html del sito.

Inserisce prima di </head> un blocco tra i commenti <!-- icone --> ... <!-- /icone -->.
Se il blocco c'è già lo aggiorna; si può rilanciare quante volte si vuole.
Su GitHub lo fa da solo l'azione .github/workflows/indice.yml a ogni modifica di un file .html.

Uso:  python3 _strumenti/favicon.py
"""
import os, re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SITE = "https://italianol2sai.github.io"
BLOCCO = f"""<!-- icone -->
<link rel="icon" href="/favicon.ico" sizes="any">
<link rel="icon" href="/icone/favicon.svg" type="image/svg+xml">
<link rel="apple-touch-icon" href="/icone/apple-touch-icon.png">
<link rel="manifest" href="/icone/manifest.webmanifest">
<meta name="theme-color" content="#1f8a4c">
<meta name="apple-mobile-web-app-title" content="Autoapprendimento">
<meta property="og:site_name" content="Autoapprendimento · Italiano L2 ETNIE">
<meta property="og:image" content="{SITE}/icone/condividi.png">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta name="twitter:card" content="summary_large_image">
<!-- /icone -->"""
RE_BLOCCO = re.compile(r"<!-- icone -->.*?<!-- /icone -->\n?", re.S)


def aggiungi(testo):
    testo = RE_BLOCCO.sub("", testo)
    i = testo.lower().find("</head>")
    if i < 0:
        return testo
    return testo[:i] + BLOCCO + "\n" + testo[i:]


def main():
    cambiati = 0
    for cartella, dirs, files in os.walk(ROOT):
        dirs[:] = [d for d in dirs if not d.startswith(".") and d != "_strumenti"]
        for nome in files:
            if not nome.endswith(".html"):
                continue
            p = os.path.join(cartella, nome)
            with open(p, encoding="utf-8") as f:
                vecchio = f.read()
            nuovo = aggiungi(vecchio)
            if nuovo != vecchio:
                with open(p, "w", encoding="utf-8") as f:
                    f.write(nuovo)
                cambiati += 1
    print(f"favicon aggiunta/aggiornata in {cambiati} pagine")


if __name__ == "__main__":
    main()
