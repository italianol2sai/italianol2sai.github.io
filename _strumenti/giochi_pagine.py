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
 "salute": ("🩺 GIOCHI: LA SALUTE", [
  ["LA TESTA", "🙆", "SOPRA IL COLLO"], ["LA MANO", "✋", "HA CINQUE DITA"], ["IL PIEDE", "🦶", "LO METTI NELLA SCARPA"], ["L'OCCHIO", "👁️", "CON QUESTO VEDI"],
  ["L'ORECCHIO", "👂", "CON QUESTO SENTI"], ["IL NASO", "👃", "IN MEZZO ALLA FACCIA"], ["LA BOCCA", "👄", "CON QUESTA MANGI E PARLI"], ["IL DENTE", "🦷", "LO LAVI CON LO SPAZZOLINO"],
  ["IL CUORE", "❤️", "BATTE NEL PETTO"], ["LA GAMBA", "🦵", "CON QUESTA CAMMINI"], ["IL MEDICO", "🧑‍⚕️", "TI VISITA"], ["LA FARMACIA", "💊", "CI COMPRI LE MEDICINE"],
  ["LA FEBBRE", "🤒", "HAI CALDO, 38 GRADI"], ["IL TERMOMETRO", "🌡️", "MISURA LA FEBBRE"], ["LO SCIROPPO", "🥄", "MEDICINA PER LA TOSSE"], ["IL CEROTTO", "🩹", "LO METTI SU UN TAGLIO"],
  ["L'AMBULANZA", "🚑", "NUMERO 118"], ["L'OSPEDALE", "🏥", "C'È IL PRONTO SOCCORSO"]]),
 "famiglia": ("👨‍👩‍👧 GIOCHI: LA FAMIGLIA", [
  ["LA MAMMA", "👩", "LA MADRE"], ["IL PAPÀ", "👨", "IL PADRE"], ["IL FIGLIO", "👦", "IL BAMBINO DEI GENITORI"], ["LA FIGLIA", "👧", "LA BAMBINA DEI GENITORI"],
  ["IL FRATELLO", "🧑", "FIGLIO DEI TUOI GENITORI, MASCHIO"], ["LA SORELLA", "👱‍♀️", "FIGLIA DEI TUOI GENITORI, FEMMINA"], ["IL NONNO", "👴", "IL PADRE DEL PAPÀ"], ["LA NONNA", "👵", "LA MADRE DELLA MAMMA"],
  ["IL NEONATO", "👶", "HA POCHI GIORNI"], ["IL MARITO", "🤵", "È SPOSATO CON LA MOGLIE"], ["LA MOGLIE", "👰", "È SPOSATA CON IL MARITO"], ["LO ZIO", "🧔", "IL FRATELLO DEL PAPÀ"],
  ["LA ZIA", "👩‍🦰", "LA SORELLA DELLA MAMMA"], ["IL CUGINO", "🧒", "IL FIGLIO DELLO ZIO"], ["LA FAMIGLIA", "👨‍👩‍👧‍👦", "TUTTI INSIEME"], ["LA CASA", "🏠", "DOVE VIVE LA FAMIGLIA"],
  ["LA TORTA", "🎂", "PER IL COMPLEANNO"], ["IL REGALO", "🎁", "LO DAI PER LA FESTA"]]),
 "vestiti": ("👕 GIOCHI: I VESTITI", [
  ["LA MAGLIETTA", "👕", "LA METTI D'ESTATE"], ["I PANTALONI", "👖", "COPRONO LE GAMBE"], ["LA GONNA", "👗", "LA PORTANO LE DONNE"], ["LA GIACCA", "🧥", "SOPRA LA CAMICIA"],
  ["LA CAMICIA", "👔", "HA I BOTTONI"], ["LE SCARPE", "👞", "LE METTI AI PIEDI"], ["LE SCARPE DA GINNASTICA", "👟", "PER FARE SPORT"], ["IL CAPPELLO", "🎩", "SULLA TESTA"],
  ["LA SCIARPA", "🧣", "INTORNO AL COLLO, D'INVERNO"], ["I GUANTI", "🧤", "PER LE MANI, D'INVERNO"], ["LE CALZE", "🧦", "SOTTO LE SCARPE"], ["LA BORSA", "👜", "CI METTI IL PORTAFOGLIO"],
  ["IL COSTUME", "🩱", "PER IL MARE"], ["GLI OCCHIALI", "👓", "PER VEDERE BENE"], ["LA CRAVATTA", "👔", "CON LA CAMICIA ELEGANTE"], ["L'OMBRELLO", "☂️", "QUANDO PIOVE"],
  ["IL PIGIAMA", "🛌", "PER DORMIRE"], ["GLI STIVALI", "👢", "SCARPE ALTE"]]),
 "citta": ("🏙️ GIOCHI: LA CITTÀ", [
  ["L'AUTOBUS", "🚌", "PRENDI IL BIGLIETTO E SALI"], ["IL TRENO", "🚆", "PARTE DALLA STAZIONE"], ["LA STAZIONE", "🚉", "DOVE ARRIVANO I TRENI"], ["IL TAXI", "🚕", "MACCHINA GIALLA O BIANCA"],
  ["LA BICICLETTA", "🚲", "HA DUE RUOTE E I PEDALI"], ["LA MACCHINA", "🚗", "HA QUATTRO RUOTE"], ["IL SEMAFORO", "🚦", "ROSSO, GIALLO, VERDE"], ["LA STRADA", "🛣️", "CI PASSANO LE MACCHINE"],
  ["LA CHIESA", "⛪", "HA IL CAMPANILE"], ["LA SCUOLA", "🏫", "CI STUDIANO I BAMBINI"], ["LA BANCA", "🏦", "CI SONO I SOLDI"], ["LA POSTA", "📮", "SPEDISCI UNA LETTERA"],
  ["IL PARCO", "🌳", "CI SONO GLI ALBERI"], ["IL MARE", "🌊", "BARI È SUL…"], ["IL PORTO", "⛴️", "ARRIVANO LE NAVI"], ["L'AEREO", "✈️", "VOLA IN CIELO"],
  ["IL SUPERMERCATO", "🛒", "CI FAI LA SPESA"], ["LA FERMATA", "🚏", "ASPETTI L'AUTOBUS"]]),
 "lavoro": ("🧰 GIOCHI: IL LAVORO", [
  ["IL CUOCO", "🧑‍🍳", "LAVORA IN CUCINA"], ["IL MURATORE", "🧱", "LAVORA IN CANTIERE"], ["IL MEDICO", "🩺", "LAVORA IN OSPEDALE"], ["L'INSEGNANTE", "🧑‍🏫", "LAVORA A SCUOLA"],
  ["IL CONTADINO", "🧑‍🌾", "LAVORA IN CAMPAGNA"], ["IL MECCANICO", "🔧", "RIPARA LE MACCHINE"], ["IL CAMERIERE", "🍽️", "PORTA I PIATTI AL TAVOLO"], ["IL PARRUCCHIERE", "💇", "TAGLIA I CAPELLI"],
  ["L'AUTISTA", "🚚", "GUIDA IL CAMION"], ["IL POMPIERE", "🚒", "SPEGNE IL FUOCO"], ["IL POLIZIOTTO", "👮", "CONTROLLA LA STRADA"], ["L'INFERMIERE", "💉", "AIUTA IL MEDICO"],
  ["IL CASCO", "⛑️", "PROTEGGE LA TESTA"], ["IL CONTRATTO", "📝", "LO FIRMI PRIMA DI LAVORARE"], ["LO STIPENDIO", "💶", "LO PRENDI OGNI MESE"], ["IL COLLOQUIO", "🤝", "INCONTRO PRIMA DEL LAVORO"],
  ["IL CURRICULUM", "📄", "CI SCRIVI LE TUE ESPERIENZE"], ["IL COMPUTER", "💻", "LAVORI IN UFFICIO CON QUESTO"]]),
 "civica": ("🇮🇹 GIOCHI: EDUCAZIONE CIVICA", [
  ["LA BANDIERA", "🇮🇹", "VERDE, BIANCA E ROSSA"], ["IL COMUNE", "🏛️", "CI FAI LA RESIDENZA"], ["LA QUESTURA", "👮", "CI FAI IL PERMESSO DI SOGGIORNO"], ["IL PERMESSO", "📄", "PERMESSO DI SOGGIORNO"],
  ["IL PASSAPORTO", "🛂", "DOCUMENTO PER VIAGGIARE"], ["LA FIRMA", "✍️", "SCRIVI IL TUO NOME SOTTO"], ["LA LEGGE", "⚖️", "TUTTI LA DEVONO RISPETTARE"], ["IL VOTO", "🗳️", "SCEGLI CHI GOVERNA"],
  ["LA SCUOLA", "🏫", "È OBBLIGATORIA PER I BAMBINI"], ["LA PACE", "🕊️", "IL CONTRARIO DELLA GUERRA"], ["IL LAVORO", "🧰", "L'ITALIA È FONDATA SUL…"], ["LA SALUTE", "🏥", "LA SANITÀ È PER TUTTI"],
  ["IL RIFIUTO", "🗑️", "VA NEL BIDONE GIUSTO"], ["LA CARTA", "📦", "VA NEL BIDONE BIANCO O BLU"], ["IL VETRO", "🍾", "BOTTIGLIE E BARATTOLI"], ["LA TESSERA", "💳", "TESSERA SANITARIA"],
  ["IL MEDICO", "🩺", "MEDICO DI BASE"], ["LA CINTURA", "🚗", "IN AUTO LA METTI SEMPRE"]]),
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
