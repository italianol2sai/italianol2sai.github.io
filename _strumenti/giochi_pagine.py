"""Pagine «Giochi» per argomento (2026-10-30, Erila: «anche giochi, oltre a escape room»): memory, impiccato, quiz a tempo,
cerca la parola, tutti da comune/giochi.js. Per ogni argomento cambia solo la lista di parole: [PAROLA, emoji, indizio].
Uso: python3 _strumenti/giochi_pagine.py → giochi/<argomento>.html"""
import json, os

RADICE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

ARGOMENTI = {
 "casa": ("🏠 GIOCHI: LA CASA", [
  ["LA CUCINA", "🍳", "QUI CUCINI E MANGI"], ["IL BAGNO", "🛁", "QUI TI LAVI"], ["LA CAMERA", "🛏️", "QUI DORMI"], ["IL SOGGIORNO", "📺", "QUI GUARDI LA TV"],
  ["IL BALCONE", "🌿", "È FUORI, MA È DELLA CASA"], ["IL LETTO", "🛌", "CI DORMI SOPRA"], ["IL DIVANO", "🛋️", "CI SIEDI IN TRE"], ["LA SEDIA", "🪑", "CI SIEDI IN UNO"],
  ["IL TAVOLO", "🍽️", "CI METTI I PIATTI"], ["LA PORTA", "🚪", "LA APRI PER ENTRARE"], ["LA FINESTRA", "🪟", "DA QUI ENTRA LA LUCE"], ["LA CHIAVE", "🔑", "APRE LA PORTA"],
  ["LO SPECCHIO", "🪞", "TI GUARDI"], ["LA DOCCIA", "🚿", "ACQUA DALL'ALTO"], ["IL FRIGORIFERO", "🧊", "TIENE IL CIBO FREDDO"], ["LA LAMPADA", "💡", "FA LUCE"],
  ["L'AFFITTO", "💶", "LO PAGHI OGNI MESE"], ["L'ASCENSORE", "🛗", "SALE AI PIANI"]]),
 "cucina": ("🍝 GIOCHI: IL CIBO", [
  ["IL PANE", "🍞", "LO COMPRI DAL PANETTIERE"], ["IL LATTE", "🥛", "È BIANCO, LO BEVI A COLAZIONE"], ["LA MELA", "🍎", "FRUTTO ROSSO O VERDE"], ["LA BANANA", "🍌", "FRUTTO GIALLO E LUNGO"],
  ["IL POMODORO", "🍅", "ROSSO, PER IL SUGO"], ["LA CAROTA", "🥕", "ARANCIONE, PIACE AI CONIGLI"], ["IL FORMAGGIO", "🧀", "SI FA CON IL LATTE"], ["L'UOVO", "🥚", "LO FA LA GALLINA"],
  ["IL PESCE", "🐟", "VIVE NEL MARE"], ["IL POLLO", "🍗", "CARNE BIANCA"], ["IL RISO", "🍚", "PICCOLO E BIANCO, SI CUOCE IN ACQUA"], ["LA PASTA", "🍝", "SPAGHETTI, ORECCHIETTE…"],
  ["IL CAFFÈ", "☕", "NERO, AL BAR"], ["IL LIMONE", "🍋", "GIALLO E ACIDO"], ["L'UVA", "🍇", "SI FA IL VINO"], ["LA PIZZA", "🍕", "TONDA, CON POMODORO E MOZZARELLA"],
  ["IL GELATO", "🍦", "FREDDO E DOLCE"], ["LA PATATA", "🥔", "SI FA FRITTA O AL FORNO"], ["LA CIPOLLA", "🧅", "TI FA PIANGERE"], ["L'ACQUA", "💧", "LA BEVI SEMPRE"]]),
}

PAGINA = """<!doctype html>
<html lang="it">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>%(titolo_breve)s</title>
<link href="https://fonts.googleapis.com/css2?family=Atkinson+Hyperlegible:wght@400;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="../comune/giochi.css">
</head>
<body>
<div class="g-wrap">
  <a class="back" href="../#%(sezione)s">← TUTTI I MATERIALI</a>
  <h1>%(titolo)s</h1>
  <p class="sub">4 GIOCHI CORTI PER RIPASSARE LE PAROLE · LIVELLO A1</p>
  <main id="giochi"></main>
</div>
<script>window.GIOCHI = %(dati)s;</script>
<script src="../comune/giochi.js"></script>
</body>
</html>
"""
SEZIONE = {"casa": "casa", "cucina": "cucina", "salute": "salute", "famiglia": "famiglia", "vestiti": "vestiti", "citta": "citta", "lavoro": "lavoro", "civica": "educazione-civica"}

if __name__ == "__main__":
    os.makedirs(os.path.join(RADICE, "giochi"), exist_ok=True)
    for nome, (titolo, parole) in ARGOMENTI.items():
        dati = json.dumps({"id": nome, "titolo": titolo, "parole": parole}, ensure_ascii=False)
        open(os.path.join(RADICE, "giochi", nome + ".html"), "w", encoding="utf-8").write(
            PAGINA % {"titolo": titolo, "titolo_breve": titolo.split(" ", 1)[1].title(), "sezione": SEZIONE[nome], "dati": dati})
        print("scritto giochi/%s.html" % nome)
