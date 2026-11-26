"""Mette il pulsante «🖨️ Stampa» (comune/stampa.js) in tutte le pagine di teoria a slide e nelle pagine
fatte a mano elencate sotto (regola di Erila 2026-11-26: «per tutto»). Le schede di esercizi con motore.js
lo caricano da sole. Si può rilanciare: non aggiunge due volte lo script.
    python3 _strumenti/aggiungi_stampa.py"""
import glob, os

# pagine fatte a mano (MAI giochi, escape room, flashcard e pagine a carte: Erila 2026-11-26): percorso -> attributi (data-scheda = riga NOME/DATA in cima; data-maiuscolo = A0/A1)
A_MANO = {
    "abbigliamento/esercizi.html": "data-scheda data-maiuscolo",
    "verifica-a2/index.html": "data-scheda",
    "lettere-ponte/index.html": "data-scheda data-maiuscolo",
    "cercare-casa/index.html": "",
    "sillabe/index.html": "data-maiuscolo",
    "sillabe-difficili/index.html": "data-maiuscolo",
}

def metti(path, attr=""):
    s = open(path, encoding="utf-8").read()
    if "comune/stampa.js" in s or "</body>" not in s:
        return False
    rel = os.path.relpath("comune/stampa.js", os.path.dirname(path) or ".")
    tag = '<script src="%s"%s></script>\n' % (rel, (" " + attr) if attr else "")
    i = s.rindex("</body>")
    open(path, "w", encoding="utf-8").write(s[:i] + tag + s[i:])
    return True

if __name__ == "__main__":
    n = 0
    for f in sorted(glob.glob("*/index.html")):
        if 'class="stage"' in open(f, encoding="utf-8").read():
            n += metti(f)
    for f, a in A_MANO.items():
        n += metti(f, a)
    print("pulsante stampa aggiunto in", n, "pagine")
