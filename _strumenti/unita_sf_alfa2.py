"""Percorso ALFABETIZZAZIONE, unità 6-14 (stessa struttura di unita_sf_alfa.py, testi nuovi ambientati a Bari).
Ogni unità è descritta da un dizionario U e trasformata da fai(U) in presentazione + esercizi + giochi.
Tutto in STAMPATELLO MAIUSCOLO. Le lettere si indicano col loro segno (P, T, R…), mai col nome.
Uso: python3 _strumenti/unita_sf_alfa2.py"""
import os, sys
sys.path.insert(0, os.path.dirname(__file__))
from unita_primi import cover, slide, cards, table, nota, dialogo, end
from unita_drive import parla, libero
from unita_sf import build_slide, build_giochi, say, parole
from genera import build as build_es
from unita_sf_alfa import (S, E, griglia_numeri, sillabe_tab, es_ascolta, es_copia, es_lettera, es_sillabe, es_inizia,
                           es_numeri, es_conti, es_dialogo, es_scegli, pagina)


def sill(sillabe):
    """tabella di sillabe libere, es. ["CI", "CE"] o ["CHI", "CHE"]"""
    return table([[S(x) for x in sillabe]])


def fai(u):
    n = u["n"]
    sl = [cover(u["emo"], u["titolo"], u["sotto"], "ALFABETIZZAZIONE &bull; UNITÀ %d" % n),
          slide("CHE COSA IMPARIAMO?", cards(u["impariamo"])),
          slide("🗣️ LE PAROLE", parole([(w, w.lower()) for w in u["parole"]]) + "\n" + nota("👆 TOCCA LA PAROLA E ASCOLTA.")),
          slide(u["vocab_titolo"], cards([(e, w, "") for e, w in u["vocab"]], "g3")),
          slide(u["dial_titolo"], dialogo(u["dialogo"]))]
    for titolo, tab_html, esempi in u["lettere"]:
        sl.append(slide("🔤 " + titolo, tab_html + "\n" + parole([(w, w.lower()) for w in esempi])))
    if u.get("extra"):
        sl.append(slide(*u["extra"]))
    sl.append(slide(u["num_titolo"], griglia_numeri(u["numeri"])))
    sl.append(end(u["fine"]))

    p = u["parole"]
    rot = lambda i: [p[(i + j) % len(p)] for j in range(3)]
    opts = lambda i: rot(i)[-(i % 3):] + rot(i)[:-(i % 3)] if i % 3 else rot(i)
    e = 0
    def nid():
        nonlocal e
        e += 1
        return "e%d" % e, e
    sec = [{"part": "Ascolto e leggo"}]
    i_, k_ = nid(); sec.append(es_ascolta(i_, k_, [(w, opts(i)) for i, w in enumerate(p)]))
    i_, k_ = nid(); sec.append(es_scegli(i_, k_, "👀 Che cos'è?", [(E(em), None, w) for em, w in u["vocab"][:4]],
                                         opts=[w for _, w in u["vocab"][:4]], cons="GUARDA. SCEGLI LA PAROLA."))
    i_, k_ = nid(); sec.append(es_scegli(i_, k_, u["dial_titolo"], u["dial_dom"]))
    sec.append({"part": "Scrivo"})
    i_, k_ = nid(); sec.append(es_copia(i_, k_, p))
    i_, k_ = nid(); sec.append(es_sillabe(i_, k_, u["sillabe"]))
    sec.append({"part": "Le lettere " + ", ".join(u["sigle"])})
    i_, k_ = nid(); sec.append(es_inizia(i_, k_, u["inizia_lettere"], u["inizia"]))
    i_, k_ = nid(); sec.append(es_lettera(i_, k_, u["buchi"], cons=u.get("buchi_cons", "TOCCA 🔊. SCRIVI LE LETTERE CHE MANCANO.")))
    sec.append({"part": "Parlo"})
    t, keys, bank = u["cloze"]
    i_, k_ = nid(); sec.append(es_dialogo(i_, k_, t, keys, bank))
    sec.append({"part": "I numeri"})
    i_, k_ = nid(); sec.append(es_numeri(i_, k_, u["ascolta_num"], u.get("num_es_titolo", "Ascolta e scrivi il numero")))
    if u.get("conti"):
        i_, k_ = nid(); sec.append(es_conti(i_, k_, u["conti"], u.get("segno", "+")))
    i_, k_ = nid(); sec.append(libero(i_, k_, u["libero"][0], u["libero"][1], u["libero"][2], rows=1))
    i_, k_ = nid(); sec.append(parla(i_, k_, u["parla"]))
    es = pagina("%s %s · Esercizi" % (u["emo"], u["titolo"].capitalize()), u["dir"], sec)
    return sl, es


# =====================================================================
UNITA = [
 {"n": 6, "dir": "alfa-la-mia-salute", "emo": "🩺", "titolo": "LA MIA SALUTE", "sotto": "IL CORPO · DAL MEDICO · P E T · I NUMERI DA 500 A 1000",
  "impariamo": [("🧍", "IL CORPO", "TESTA, PANCIA, PIEDE"), ("🤒", "DAL MEDICO", "HO MAL DI…"), ("🔤", "P · T", "LE LETTERE NUOVE"), ("🔢", "500 → 1000", "I NUMERI")],
  "parole": ["TESTA", "PANCIA", "PIEDE", "MEDICO", "TOSSE"],
  "vocab_titolo": "🧍 IL CORPO", "vocab": [("🗣️", "TESTA"), ("🦶", "PIEDE"), ("✋", "MANO"), ("👁️", "OCCHIO"), ("🦷", "DENTE"), ("💪", "BRACCIO")],
  "dial_titolo": "🏥 DAL MEDICO", "dialogo": [("MICHELE", "BUONGIORNO DOTTORESSA."), ("*DOTTORESSA", "BUONGIORNO. CHE COSA HA?"),
      ("MICHELE", "HO MAL DI TESTA E HO LA TOSSE."), ("*DOTTORESSA", "HA LA FEBBRE?"), ("MICHELE", "SÌ, 38."),
      ("*DOTTORESSA", "PRENDA QUESTO SCIROPPO TRE VOLTE AL GIORNO. E RIPOSI!")],
  "dial_dom": [("1. MICHELE HA MAL DI…", ["TESTA", "PANCIA"], "TESTA"), ("2. MICHELE HA LA…", ["TOSSE", "MANO ROTTA"], "TOSSE"),
               ("3. LA FEBBRE È…", ["38", "36"], "38"), ("4. MICHELE PRENDE…", ["LO SCIROPPO", "IL CAFFÈ"], "LO SCIROPPO")],
  "lettere": [("LA LETTERA P", sillabe_tab("P"), ["PANE", "PIEDE", "PATATA"]), ("LA LETTERA T", sillabe_tab("T"), ["TESTA", "TOSSE", "TELEFONO"])],
  "extra": ("💬 HO MAL DI…", table([["🗣️", "HO MAL DI TESTA."], ["🤰", "HO MAL DI PANCIA."], ["🦷", "HO MAL DI DENTI."], ["🤒", "HO LA FEBBRE."], ["😷", "HO LA TOSSE."]], head=["", "DICO"])),
  "num_titolo": "🔢 I NUMERI DA 500 A 1000", "numeri": [(500, "CINQUECENTO"), (600, "SEICENTO"), (700, "SETTECENTO"), (800, "OTTOCENTO"), (900, "NOVECENTO"), (1000, "MILLE")],
  "sillabe": ["TE-STA", "PAN-CIA", "PIE-DE", "ME-DI-CO", "TOS-SE"], "sigle": ["P", "T"],
  "inizia_lettere": ["P", "T"], "inizia": [("🍝", "PASTA", "P"), ("🍅", "POMODORO", "P"), ("📱", "TELEFONO", "T"), ("🚂", "TRENO", "T"), ("🍐", "PERA", "P"), ("🐢", "TARTARUGA", "T")],
  "buchi": [("PANE", "_ ANE", "P"), ("TOSSE", "_ OSSE", "T"), ("PATATA", "_ A _ A _ A", "PTT"), ("TOPO", "_ O _ O", "TP")], "buchi_cons": "TOCCA 🔊. SCRIVI <b>P</b> OPPURE <b>T</b>.",
  "cloze": ("DOTTORESSA: CHE COSA ___?<br>MICHELE: HO MAL DI ___.<br>DOTTORESSA: HA LA ___?<br>MICHELE: SÌ, 38.", ["ha", "testa", "febbre"], "HA · TESTA · FEBBRE"),
  "ascolta_num": [("SEICENTO", 600), ("OTTOCENTO", 800), ("MILLE", 1000), ("SETTECENTOCINQUANTA", 750), ("NOVECENTO", 900)],
  "conti": [(500, 100), (600, 300), (750, 250), (400, 400)],
  "libero": ("Come stai?", "SCRIVI: OGGI COME STAI? HAI MALE?", ["OGGI HO… / STO…"]), "parla": "SEI DAL MEDICO. DI' CHE COSA HAI.",
  "fine": "ORA SAI PARLARE CON IL MEDICO!",
  "giochi": [["TESTA", "🗣️", "SOPRA IL COLLO"], ["PANCIA", "🤰", "QUI VA IL CIBO"], ["PIEDE", "🦶", "CAMMINO CON IL…"], ["MANO", "✋", "HA CINQUE DITA"], ["OCCHIO", "👁️", "VEDO CON L'…"],
             ["DENTE", "🦷", "MORDO CON IL…"], ["MEDICO", "🩺", "MI VISITA"], ["TOSSE", "😷", "COF COF"], ["FEBBRE", "🤒", "38 GRADI"], ["SCIROPPO", "🧴", "MEDICINA DOLCE"],
             ["PANE", "🍞", "P + A"], ["PERA", "🍐", "P + E"], ["TRENO", "🚂", "T + R"], ["TOPO", "🐭", "T + O"], ["MILLE", "🔢", "1000"], ["SEICENTO", "🔢", "600"]]},

 {"n": 7, "dir": "alfa-la-mia-casa", "emo": "🏠", "titolo": "LA MIA CASA", "sotto": "LE STANZE · I MOBILI · C E R · PRIMO, SECONDO, TERZO",
  "impariamo": [("🛋️", "LE STANZE", "CUCINA, BAGNO, CAMERA"), ("🪑", "I MOBILI", "LETTO, TAVOLO, SEDIA"), ("🔤", "C · R", "CA, CO, CU · RA, RE…"), ("🏢", "IL PIANO", "PRIMO, SECONDO…")],
  "parole": ["CUCINA", "CAMERA", "BAGNO", "LETTO", "TAVOLO"],
  "vocab_titolo": "🪑 I MOBILI", "vocab": [("🛏️", "LETTO"), ("🪑", "SEDIA"), ("🛋️", "DIVANO"), ("🚿", "DOCCIA"), ("🪟", "FINESTRA"), ("🚪", "PORTA")],
  "dial_titolo": "📞 AL TELEFONO", "dialogo": [("*SILVIA", "CIAO CRISTIAN! DOVE ABITI ADESSO?"), ("CRISTIAN", "ABITO IN VIA CAPRUZZI 12, AL TERZO PIANO."),
      ("*SILVIA", "COM'È LA CASA?"), ("CRISTIAN", "È PICCOLA: C'È UNA CUCINA, UNA CAMERA E UN BAGNO."), ("*SILVIA", "C'È IL BALCONE?"), ("CRISTIAN", "SÌ, C'È UN BALCONE CON I FIORI!")],
  "dial_dom": [("1. CRISTIAN ABITA AL…", ["TERZO PIANO", "PRIMO PIANO"], "TERZO PIANO"), ("2. LA CASA È…", ["PICCOLA", "GRANDE"], "PICCOLA"),
               ("3. QUANTE CAMERE?", ["UNA", "TRE"], "UNA"), ("4. SUL BALCONE CI SONO…", ["I FIORI", "LE BICI"], "I FIORI")],
  "lettere": [("LA LETTERA C: CA · CO · CU", sill(["CA", "CO", "CU"]), ["CASA", "CUCINA", "COLLO"]), ("LA LETTERA R", sillabe_tab("R"), ["RADIO", "REGALO", "ROSA"])],
  "extra": ("🏢 IL PIANO", table([["1°", "PRIMO PIANO"], ["2°", "SECONDO PIANO"], ["3°", "TERZO PIANO"], ["4°", "QUARTO PIANO"], ["5°", "QUINTO PIANO"], ["0", "PIANO TERRA"]], head=["", "SI DICE"])),
  "num_titolo": "🔢 PRIMO, SECONDO, TERZO…", "numeri": [("1°", "PRIMO"), ("2°", "SECONDO"), ("3°", "TERZO"), ("4°", "QUARTO"), ("5°", "QUINTO"), ("6°", "SESTO")],
  "sillabe": ["CU-CI-NA", "CA-ME-RA", "BA-GNO", "LET-TO", "TA-VO-LO"], "sigle": ["C", "R"],
  "inizia_lettere": ["C", "R"], "inizia": [("🏠", "CASA", "C"), ("🌹", "ROSA", "R"), ("🥕", "CAROTA", "C"), ("📻", "RADIO", "R"), ("🎁", "REGALO", "R"), ("☕", "CAFFÈ", "C")],
  "buchi": [("CASA", "_ ASA", "C"), ("ROSA", "_ OSA", "R"), ("CUCINA", "_ U _ INA", "CC"), ("CAMERA", "CAME _ A", "R")],
  "cloze": ("SILVIA: DOVE ___?<br>CRISTIAN: IN VIA CAPRUZZI, AL TERZO ___.<br>SILVIA: COM'È LA ___?<br>CRISTIAN: È ___.", ["abiti", "piano", "casa", "piccola"], "ABITI · PIANO · CASA · PICCOLA"),
  "ascolta_num": [("PRIMO", 1), ("TERZO", 3), ("QUINTO", 5), ("SECONDO", 2), ("QUARTO", 4)], "num_es_titolo": "Ascolta: che piano è? Scrivi il numero",
  "conti": [(1, 2), (3, 2), (2, 2), (4, 1)],
  "libero": ("La mia casa", "SCRIVI: COM'È LA TUA CASA? A CHE PIANO ABITI?", ["LA MIA CASA È… ABITO AL…"]), "parla": "DESCRIVI LA TUA CASA: QUANTE STANZE? CHE MOBILI CI SONO?",
  "fine": "ORA SAI DESCRIVERE LA TUA CASA!",
  "giochi": [["CUCINA", "🍳", "QUI CUCINO"], ["CAMERA", "🛏️", "QUI DORMO"], ["BAGNO", "🛁", "QUI MI LAVO"], ["LETTO", "🛏️", "CI DORMO"], ["TAVOLO", "🍽️", "CI MANGIO"],
             ["SEDIA", "🪑", "CI MI SIEDO"], ["DIVANO", "🛋️", "CI GUARDO LA TV"], ["DOCCIA", "🚿", "ACQUA SULLA TESTA"], ["FINESTRA", "🪟", "VEDO FUORI"], ["PORTA", "🚪", "ENTRO ED ESCO"],
             ["BALCONE", "🌷", "FUORI DALLA CASA, IN ALTO"], ["PIANO", "🏢", "PRIMO, SECONDO…"], ["CASA", "🏠", "C + A"], ["ROSA", "🌹", "R + O"], ["TERZO", "3️⃣", "3°"], ["PRIMO", "1️⃣", "1°"]]},

 {"n": 8, "dir": "alfa-cerco-casa", "emo": "🔑", "titolo": "CERCO CASA", "sotto": "L'ANNUNCIO · L'AFFITTO · N E B · I NUMERI DA 1000 IN SU",
  "impariamo": [("📰", "L'ANNUNCIO", "AFFITTASI, LIBERO, ARREDATO"), ("💶", "L'AFFITTO", "QUANTO COSTA AL MESE?"), ("🔤", "N · B", "LE LETTERE NUOVE"), ("🔢", "1000 →", "I NUMERI GRANDI")],
  "parole": ["AFFITTO", "ANNUNCIO", "BALCONE", "NUMERO", "BOLLETTE"],
  "vocab_titolo": "📰 LE PAROLE DELL'ANNUNCIO", "vocab": [("🏠", "AFFITTASI"), ("🛋️", "ARREDATO"), ("💡", "BOLLETTE"), ("🔑", "CHIAVI"), ("📞", "NUMERO"), ("✍️", "CONTRATTO")],
  "dial_titolo": "📞 CHIAMO PER L'ANNUNCIO", "dialogo": [("SALEAH", "BUONGIORNO, CHIAMO PER L'ANNUNCIO DELLA CASA."), ("*GIOVANNI", "BUONGIORNO! LA CASA È IN VIA NAPOLI."),
      ("SALEAH", "QUANTO È L'AFFITTO?"), ("*GIOVANNI", "500 EURO AL MESE. LE BOLLETTE SONO A PARTE."), ("SALEAH", "È ARREDATA?"), ("*GIOVANNI", "SÌ, CON LETTO, TAVOLO E DIVANO. VUOLE VEDERLA DOMANI?")],
  "dial_dom": [("1. LA CASA È IN VIA…", ["NAPOLI", "ROMA"], "NAPOLI"), ("2. L'AFFITTO È…", ["500 EURO", "300 EURO"], "500 EURO"),
               ("3. LE BOLLETTE SONO…", ["A PARTE", "COMPRESE"], "A PARTE"), ("4. LA CASA È…", ["ARREDATA", "VUOTA"], "ARREDATA")],
  "lettere": [("LA LETTERA N", sillabe_tab("N"), ["NASO", "NONNO", "NUMERO"]), ("LA LETTERA B", sillabe_tab("B"), ["BAGNO", "BANANA", "BOLLETTE"])],
  "extra": ("📰 L'ANNUNCIO", nota("<b>AFFITTASI</b><br>📍 VIA NAPOLI 8, BARI<br>🏠 2 CAMERE, CUCINA, BAGNO<br>🛋️ ARREDATO<br>💶 500 EURO AL MESE<br>📞 333 456 7890", "font-size:1.5rem;text-align:left")),
  "num_titolo": "🔢 I NUMERI GRANDI", "numeri": [(1000, "MILLE"), (1500, "MILLECINQUECENTO"), (2000, "DUEMILA"), (3000, "TREMILA"), (5000, "CINQUEMILA"), (10000, "DIECIMILA")],
  "sillabe": ["AF-FIT-TO", "AN-NUN-CIO", "BAL-CO-NE", "NU-ME-RO", "BOL-LET-TE"], "sigle": ["N", "B"],
  "inizia_lettere": ["N", "B"], "inizia": [("👃", "NASO", "N"), ("🍌", "BANANA", "B"), ("☁️", "NUVOLA", "N"), ("⛵", "BARCA", "B"), ("👶", "BAMBINO", "B"), ("🌙", "NOTTE", "N")],
  "buchi": [("NASO", "_ ASO", "N"), ("BARCA", "_ ARCA", "B"), ("BANANA", "_ A _ A _ A", "BNN"), ("NONNO", "_ O _ _ O", "NNN")],
  "cloze": ("SALEAH: QUANTO È L'___?<br>GIOVANNI: 500 EURO AL ___.<br>SALEAH: È ___?<br>GIOVANNI: SÌ, C'È IL LETTO E IL DIVANO.", ["affitto", "mese", "arredata"], "AFFITTO · MESE · ARREDATA"),
  "ascolta_num": [("MILLE", 1000), ("DUEMILA", 2000), ("MILLECINQUECENTO", 1500), ("TREMILA", 3000), ("CINQUEMILA", 5000)],
  "conti": [(500, 500), (1000, 1000), (1500, 500), (2000, 3000)],
  "libero": ("La casa che cerco", "SCRIVI: CHE CASA CERCHI? QUANTE CAMERE? QUANTO PUOI PAGARE?", ["CERCO UNA CASA CON…"]), "parla": "TELEFONI PER UN ANNUNCIO. CHE DOMANDE FAI?",
  "fine": "ORA SAI CERCARE UNA CASA!",
  "giochi": [["AFFITTO", "💶", "LO PAGO OGNI MESE"], ["ANNUNCIO", "📰", "AFFITTASI…"], ["BOLLETTE", "💡", "LUCE, GAS, ACQUA"], ["CHIAVI", "🔑", "APRONO LA PORTA"], ["CONTRATTO", "✍️", "LO FIRMO"],
             ["ARREDATO", "🛋️", "CON I MOBILI"], ["BALCONE", "🌷", "FUORI DALLA CASA"], ["NUMERO", "📞", "PER TELEFONARE"], ["NASO", "👃", "N + A"], ["NOTTE", "🌙", "N + O"],
             ["BANANA", "🍌", "B + A"], ["BARCA", "⛵", "SUL MARE"], ["BAMBINO", "👶", "PICCOLO"], ["MILLE", "🔢", "1000"], ["DUEMILA", "🔢", "2000"], ["MESE", "📅", "30 GIORNI"]]},

 {"n": 9, "dir": "alfa-mi-scusi-dove", "emo": "🧭", "titolo": "MI SCUSI, DOV'È…?", "sotto": "I NEGOZI · DESTRA E SINISTRA · V E Z · L'ORA",
  "impariamo": [("🏪", "I NEGOZI", "FARMACIA, BANCA, POSTA"), ("↔️", "DOVE?", "A DESTRA, A SINISTRA, DRITTO"), ("🔤", "V · Z", "LE LETTERE NUOVE"), ("🕐", "CHE ORE SONO?", "SONO LE TRE")],
  "parole": ["FARMACIA", "DESTRA", "SINISTRA", "VICINO", "PIAZZA"],
  "vocab_titolo": "🏪 IN CITTÀ", "vocab": [("💊", "FARMACIA"), ("🏦", "BANCA"), ("📮", "POSTA"), ("🏥", "OSPEDALE"), ("⛪", "CHIESA"), ("🛒", "SUPERMERCATO")],
  "dial_titolo": "🧭 PER STRADA", "dialogo": [("ENEIDA", "MI SCUSI, DOV'È LA FARMACIA?"), ("*SIGNORE", "È VICINO. VADA DRITTO E POI GIRI A DESTRA."),
      ("ENEIDA", "DOPO LA PIAZZA?"), ("*SIGNORE", "SÌ, DOPO LA PIAZZA. LA FARMACIA È DI FRONTE ALLA BANCA."), ("ENEIDA", "È APERTA ADESSO?"), ("*SIGNORE", "SÌ, CHIUDE ALLE OTTO. PREGO!")],
  "dial_dom": [("1. ENEIDA CERCA…", ["LA FARMACIA", "LA POSTA"], "LA FARMACIA"), ("2. PRIMA VA…", ["DRITTO", "A SINISTRA"], "DRITTO"),
               ("3. POI GIRA…", ["A DESTRA", "A SINISTRA"], "A DESTRA"), ("4. LA FARMACIA CHIUDE ALLE…", ["OTTO", "DUE"], "OTTO")],
  "lettere": [("LA LETTERA V", sillabe_tab("V"), ["VINO", "VICINO", "VIA"]), ("LA LETTERA Z", sillabe_tab("Z"), ["ZAINO", "PIAZZA", "PIZZA"])],
  "extra": ("↔️ DOVE?", cards([("⬅️", "A SINISTRA", ""), ("➡️", "A DESTRA", ""), ("⬆️", "DRITTO", ""), ("📍", "VICINO", ""), ("🔭", "LONTANO", ""), ("🔄", "DI FRONTE", "")], "g3")),
  "num_titolo": "🕐 CHE ORE SONO?", "numeri": [("1:00", "È L'UNA"), ("2:00", "SONO LE DUE"), ("3:00", "SONO LE TRE"), ("8:00", "SONO LE OTTO"), ("12:00", "È MEZZOGIORNO"), ("8:30", "LE OTTO E MEZZA")],
  "sillabe": ["FAR-MA-CI-A", "DE-STRA", "SI-NI-STRA", "VI-CI-NO", "PIAZ-ZA"], "sigle": ["V", "Z"],
  "inizia_lettere": ["V", "Z"], "inizia": [("🍷", "VINO", "V"), ("🎒", "ZAINO", "Z"), ("🦓", "ZEBRA", "Z"), ("🌋", "VULCANO", "V"), ("🍬", "ZUCCHERO", "Z"), ("👗", "VESTITO", "V")],
  "buchi": [("VINO", "_ INO", "V"), ("ZAINO", "_ AINO", "Z"), ("PIAZZA", "PIA _ _ A", "ZZ"), ("VIA", "_ IA", "V")],
  "cloze": ("ENEIDA: MI SCUSI, DOV'È LA ___?<br>SIGNORE: VADA ___ E POI GIRI A ___.<br>ENEIDA: GRAZIE!", ["farmacia", "dritto", "destra"], "FARMACIA · DRITTO · DESTRA"),
  "ascolta_num": [("SONO LE TRE", 3), ("SONO LE OTTO", 8), ("SONO LE DIECI", 10), ("È L'UNA", 1), ("SONO LE SEI", 6)], "num_es_titolo": "Che ore sono? Scrivi il numero",
  "conti": [(8, 2), (3, 4), (9, 3), (6, 6)],
  "libero": ("Vicino a casa mia", "SCRIVI: CHE COSA C'È VICINO A CASA TUA?", ["VICINO A CASA MIA C'È…"]), "parla": "SPIEGA A UN COMPAGNO COME ARRIVARE DALLA SCUOLA ALLA FARMACIA.",
  "fine": "ORA SAI CHIEDERE LA STRADA!",
  "giochi": [["FARMACIA", "💊", "COMPRO LE MEDICINE"], ["BANCA", "🏦", "CI SONO I SOLDI"], ["POSTA", "📮", "SPEDISCO LE LETTERE"], ["OSPEDALE", "🏥", "CI SONO I MEDICI"], ["CHIESA", "⛪", "SAN NICOLA"],
             ["PIAZZA", "⛲", "GRANDE SPAZIO IN CITTÀ"], ["DESTRA", "➡️", "IL CONTRARIO DI SINISTRA"], ["SINISTRA", "⬅️", "IL CONTRARIO DI DESTRA"], ["DRITTO", "⬆️", "SEMPRE AVANTI"], ["VICINO", "📍", "NON LONTANO"],
             ["VINO", "🍷", "V + I"], ["ZAINO", "🎒", "Z + A"], ["PIZZA", "🍕", "CON LA ZZ"], ["ZEBRA", "🦓", "BIANCA E NERA"], ["ORA", "🕐", "CHE … È?"], ["VIA", "🛣️", "LA STRADA"]]},

 {"n": 10, "dir": "alfa-in-giro-per-la-citta", "emo": "🚌", "titolo": "IN GIRO PER LA CITTÀ", "sotto": "AUTOBUS E TRENO · IL BIGLIETTO · CI CE · GI GE",
  "impariamo": [("🚌", "I MEZZI", "AUTOBUS, TRENO, BICI"), ("🎫", "IL BIGLIETTO", "QUANTO COSTA?"), ("🔤", "CI CE · GI GE", "SUONI DOLCI"), ("💶", "EURO E CENTESIMI", "1,50 EURO")],
  "parole": ["CITTÀ", "BIGLIETTO", "STAZIONE", "AUTOBUS", "GIRO"],
  "vocab_titolo": "🚌 I MEZZI", "vocab": [("🚌", "AUTOBUS"), ("🚆", "TRENO"), ("🚲", "BICI"), ("🚕", "TAXI"), ("🛵", "MOTORINO"), ("🚶", "A PIEDI")],
  "dial_titolo": "🎫 IN TABACCHERIA", "dialogo": [("YUSUF", "BUONGIORNO. UN BIGLIETTO PER L'AUTOBUS, PER FAVORE."), ("*TABACCAIA", "ECCO. COSTA 1 EURO E 50."),
      ("YUSUF", "QUALE AUTOBUS VA ALLA STAZIONE CENTRALE?"), ("*TABACCAIA", "IL NUMERO 12. LA FERMATA È QUI DAVANTI."), ("YUSUF", "GRAZIE. ECCO 2 EURO."), ("*TABACCAIA", "ECCO IL RESTO: 50 CENTESIMI.")],
  "dial_dom": [("1. YUSUF COMPRA UN BIGLIETTO PER…", ["L'AUTOBUS", "IL TRENO"], "L'AUTOBUS"), ("2. IL BIGLIETTO COSTA…", ["1,50 EURO", "3 EURO"], "1,50 EURO"),
               ("3. PER LA STAZIONE PRENDE IL…", ["12", "21"], "12"), ("4. IL RESTO È…", ["50 CENTESIMI", "1 EURO"], "50 CENTESIMI")],
  "lettere": [("CI · CE", sill(["CI", "CE", "CA", "CO", "CU"]), ["CITTÀ", "CENA", "CIPOLLA"]), ("GI · GE", sill(["GI", "GE", "GA", "GO", "GU"]), ["GIRO", "GELATO", "GENTE"])],
  "extra": ("🔊 DOLCE O DURO?", table([["CI · CE", "CITTÀ · CENA", "DOLCE"], ["CA · CO · CU", "CASA · COSA · CUCINA", "DURO"], ["GI · GE", "GIRO · GELATO", "DOLCE"], ["GA · GO · GU", "GATTO · GOMMA · GUANTI", "DURO"]], head=["", "PAROLE", "SUONO"])),
  "num_titolo": "💶 EURO E CENTESIMI", "numeri": [("1,00 €", "UN EURO"), ("1,50 €", "UN EURO E CINQUANTA"), ("2,00 €", "DUE EURO"), ("0,50 €", "CINQUANTA CENTESIMI"), ("0,20 €", "VENTI CENTESIMI"), ("5,00 €", "CINQUE EURO")],
  "sillabe": ["CIT-TÀ", "BI-GLIET-TO", "STA-ZIO-NE", "AU-TO-BUS", "GI-RO"], "sigle": ["CI", "CE", "GI", "GE"],
  "inizia_lettere": ["CI", "GI"], "inizia": [("🧅", "CIPOLLA", "CI"), ("🦒", "GIRAFFA", "GI"), ("🏙️", "CITTÀ", "CI"), ("🧥", "GIACCA", "GI"), ("🍒", "CILIEGIA", "CI"), ("🎮", "GIOCO", "GI")],
  "buchi": [("CENA", "_ _ NA", "CE"), ("GELATO", "_ _ LATO", "GE"), ("CITTÀ", "_ _ TTÀ", "CI"), ("GIRO", "_ _ RO", "GI")], "buchi_cons": "TOCCA 🔊. SCRIVI CI, CE, GI OPPURE GE.",
  "cloze": ("YUSUF: UN ___ PER L'AUTOBUS, PER FAVORE.<br>TABACCAIA: COSTA 1 EURO E 50.<br>YUSUF: QUALE AUTOBUS VA ALLA ___?<br>TABACCAIA: IL NUMERO 12.", ["biglietto", "stazione"], "BIGLIETTO · STAZIONE"),
  "ascolta_num": [("DUE EURO", 2), ("CINQUANTA CENTESIMI", 50), ("VENTI CENTESIMI", 20), ("CINQUE EURO", 5), ("DIECI EURO", 10)], "num_es_titolo": "Ascolta il prezzo e scrivi il numero",
  "conti": [(2, 1), (5, 2), (10, 3), (20, 5)], "segno": "-",
  "libero": ("Come vai al corso?", "SCRIVI: COME VAI AL CORSO? IN AUTOBUS, A PIEDI…?", ["VADO AL CORSO…"]), "parla": "COMPRI UN BIGLIETTO. CHE COSA DICI?",
  "fine": "ORA SAI USARE I MEZZI IN CITTÀ!",
  "giochi": [["AUTOBUS", "🚌", "SI FERMA ALLA FERMATA"], ["TRENO", "🚆", "VA IN STAZIONE"], ["BICI", "🚲", "DUE RUOTE, PEDALI"], ["TAXI", "🚕", "MACCHINA BIANCA A BARI"], ["BIGLIETTO", "🎫", "LO COMPRO PER VIAGGIARE"],
             ["STAZIONE", "🚉", "ARRIVANO I TRENI"], ["FERMATA", "🚏", "ASPETTO L'AUTOBUS"], ["CITTÀ", "🏙️", "BARI È UNA…"], ["CENA", "🍽️", "MANGIO LA SERA"], ["GELATO", "🍦", "FREDDO E DOLCE"],
             ["GIRAFFA", "🦒", "COLLO LUNGO"], ["CIPOLLA", "🧅", "FA PIANGERE"], ["RESTO", "🪙", "I SOLDI CHE TORNANO"], ["EURO", "💶", "I SOLDI"], ["CENTESIMI", "🪙", "PICCOLI SOLDI"], ["GIRO", "🔄", "G + I"]]},

 {"n": 11, "dir": "alfa-faccio-la-spesa", "emo": "🛒", "titolo": "FACCIO LA SPESA", "sotto": "AL MERCATO · CHI CHE · GHI GHE · UN CHILO, MEZZO CHILO",
  "impariamo": [("🍎", "FRUTTA E VERDURA", "MELE, PATATE, ZUCCHINE"), ("⚖️", "QUANTO?", "UN CHILO, MEZZO CHILO"), ("🔤", "CHI CHE · GHI GHE", "SUONI DURI"), ("💶", "QUANTO COSTA?", "COSTA 2 EURO AL CHILO")],
  "parole": ["CHILO", "PESCHE", "FUNGHI", "ZUCCHINE", "SPESA"],
  "vocab_titolo": "🥕 FRUTTA E VERDURA", "vocab": [("🍎", "MELE"), ("🍑", "PESCHE"), ("🍄", "FUNGHI"), ("🥒", "ZUCCHINE"), ("🥔", "PATATE"), ("🍅", "POMODORI")],
  "dial_titolo": "🛒 AL MERCATO", "dialogo": [("*FRUTTIVENDOLO", "BUONGIORNO SIGNORA! CHE COSA DESIDERA?"), ("SALEAH", "UN CHILO DI PESCHE, PER FAVORE."),
      ("*FRUTTIVENDOLO", "ECCO. ALTRO?"), ("SALEAH", "MEZZO CHILO DI FUNGHI. QUANTO COSTANO LE ZUCCHINE?"), ("*FRUTTIVENDOLO", "2 EURO AL CHILO."), ("SALEAH", "ALLORA PRENDO ANCHE UN CHILO DI ZUCCHINE. QUANTO FA?")],
  "dial_dom": [("1. SALEAH COMPRA UN CHILO DI…", ["PESCHE", "MELE"], "PESCHE"), ("2. DI FUNGHI PRENDE…", ["MEZZO CHILO", "DUE CHILI"], "MEZZO CHILO"),
               ("3. LE ZUCCHINE COSTANO…", ["2 EURO AL CHILO", "5 EURO AL CHILO"], "2 EURO AL CHILO")],
  "lettere": [("CHI · CHE", sill(["CHI", "CHE", "CI", "CE"]), ["CHILO", "PESCHE", "CHIAVE"]), ("GHI · GHE", sill(["GHI", "GHE", "GI", "GE"]), ["FUNGHI", "SPAGHETTI", "LAGHI"])],
  "extra": ("⚖️ QUANTO?", table([["🍑🍑🍑🍑", "UN CHILO", "1 KG"], ["🍑🍑", "MEZZO CHILO", "½ KG"], ["🍑🍑🍑🍑🍑🍑🍑🍑", "DUE CHILI", "2 KG"], ["🥚 × 6", "SEI UOVA", ""]], head=["", "DICO", "SCRIVO"])),
  "num_titolo": "💶 QUANTO FA?", "numeri": [("2 €", "DUE EURO"), ("3,50 €", "TRE EURO E CINQUANTA"), ("4 €", "QUATTRO EURO"), ("6 €", "SEI EURO"), ("7,50 €", "SETTE EURO E CINQUANTA"), ("10 €", "DIECI EURO")],
  "sillabe": ["CHI-LO", "PE-SCHE", "FUN-GHI", "ZUC-CHI-NE", "SPE-SA"], "sigle": ["CHI", "CHE", "GHI", "GHE"],
  "inizia_lettere": ["CHI", "CI"], "inizia": [("🔑", "CHIAVE", "CHI"), ("🧅", "CIPOLLA", "CI"), ("⛪", "CHIESA", "CHI"), ("🏙️", "CITTÀ", "CI"), ("🎸", "CHITARRA", "CHI"), ("🍪", "CIBO", "CI")],
  "buchi": [("CHILO", "_ _ _ LO", "CHI"), ("FUNGHI", "FUN _ _ _", "GHI"), ("PESCHE", "PES _ _ _", "CHE"), ("SPAGHETTI", "SPA _ _ _ TTI", "GHE")], "buchi_cons": "TOCCA 🔊. SCRIVI CHI, CHE, GHI OPPURE GHE.",
  "cloze": ("FRUTTIVENDOLO: CHE COSA ___?<br>SALEAH: UN ___ DI PESCHE.<br>FRUTTIVENDOLO: ALTRO?<br>SALEAH: QUANTO ___ LE ZUCCHINE?", ["desidera", "chilo", "costano"], "DESIDERA · CHILO · COSTANO"),
  "ascolta_num": [("TRE EURO", 3), ("SETTE EURO", 7), ("DODICI EURO", 12), ("QUINDICI EURO", 15), ("VENTI EURO", 20)], "num_es_titolo": "Ascolta il prezzo e scrivi il numero",
  "conti": [(2, 3), (4, 4), (5, 7), (10, 5)],
  "libero": ("La mia lista della spesa", "SCRIVI LA TUA LISTA DELLA SPESA.", ["UN CHILO DI… MEZZO CHILO DI…"]), "parla": "SEI AL MERCATO. CHIEDI FRUTTA E VERDURA E IL PREZZO.",
  "fine": "ORA SAI FARE LA SPESA!",
  "giochi": [["MELE", "🍎", "ROSSE O VERDI"], ["PESCHE", "🍑", "FRUTTA D'ESTATE"], ["FUNGHI", "🍄", "NEL BOSCO"], ["ZUCCHINE", "🥒", "VERDURA VERDE"], ["PATATE", "🥔", "PER LE PATATINE"],
             ["POMODORI", "🍅", "PER LA SALSA"], ["CHILO", "⚖️", "1 KG"], ["SPESA", "🛒", "COMPRO IL CIBO"], ["MERCATO", "🏪", "BANCHI DI FRUTTA"], ["CHIAVE", "🔑", "CHI + A"],
             ["CHIESA", "⛪", "CHI + E"], ["SPAGHETTI", "🍝", "PASTA LUNGA"], ["LISTA", "📝", "… DELLA SPESA"], ["UOVA", "🥚", "LE FA LA GALLINA"], ["MEZZO", "½", "LA METÀ"], ["CHITARRA", "🎸", "SUONO LA…"]]},

 {"n": 12, "dir": "alfa-cerco-lavoro", "emo": "🔎", "titolo": "CERCO LAVORO", "sotto": "IL CENTRO PER L'IMPIEGO · I DATI · GLI · GN · IL NUMERO DI TELEFONO",
  "impariamo": [("🏢", "IL CENTRO PER L'IMPIEGO", "AIUTA A TROVARE LAVORO"), ("📝", "I MIEI DATI", "NOME, COGNOME, TELEFONO"), ("🔤", "GLI · GN", "FIGLIO, BAGNO"), ("📞", "IL TELEFONO", "LEGGO I NUMERI")],
  "parole": ["LAVORO", "COGNOME", "FIGLI", "OGNI", "MOGLIE"],
  "vocab_titolo": "📝 IL MODULO", "vocab": [("🪪", "NOME"), ("👪", "COGNOME"), ("📞", "TELEFONO"), ("🏠", "INDIRIZZO"), ("🎂", "DATA DI NASCITA"), ("🌍", "NAZIONALITÀ")],
  "dial_titolo": "🏢 AL CENTRO PER L'IMPIEGO", "dialogo": [("*IMPIEGATA", "BUONGIORNO. COME SI CHIAMA?"), ("GIOVANNI", "MI CHIAMO GIOVANNI. IL COGNOME È OKAFOR."),
      ("*IMPIEGATA", "HA UN NUMERO DI TELEFONO?"), ("GIOVANNI", "SÌ: 347 123 4567."), ("*IMPIEGATA", "CHE LAVORO CERCA?"), ("GIOVANNI", "CERCO LAVORO COME MAGAZZINIERE. HO MOGLIE E DUE FIGLI.")],
  "dial_dom": [("1. IL COGNOME DI GIOVANNI È…", ["OKAFOR", "ROSSI"], "OKAFOR"), ("2. GIOVANNI CERCA LAVORO COME…", ["MAGAZZINIERE", "CUOCO"], "MAGAZZINIERE"),
               ("3. GIOVANNI HA…", ["DUE FIGLI", "TRE FIGLI"], "DUE FIGLI")],
  "lettere": [("GLI", sill(["GLIA", "GLIE", "GLI", "GLIO"]), ["FIGLIO", "MOGLIE", "BIGLIETTO"]), ("GN", sill(["GNA", "GNE", "GNI", "GNO"]), ["BAGNO", "COGNOME", "LAVAGNA"])],
  "num_titolo": "📞 IL NUMERO DI TELEFONO", "numeri": [("3", "TRE"), ("4", "QUATTRO"), ("7", "SETTE"), ("1", "UNO"), ("2", "DUE"), ("0", "ZERO")],
  "sillabe": ["LA-VO-RO", "CO-GNO-ME", "FI-GLI", "O-GNI", "MO-GLIE"], "sigle": ["GLI", "GN"],
  "inizia_lettere": ["GLI", "GN"], "inizia": [("👨‍👦", "FIGLIO", "GLI"), ("🛁", "BAGNO", "GN"), ("🎫", "BIGLIETTO", "GLI"), ("🕷️", "RAGNO", "GN"), ("🍃", "FOGLIA", "GLI"), ("⛰️", "MONTAGNA", "GN")],
  "buchi": [("FIGLIO", "FI _ _ _ O", "GLI"), ("BAGNO", "BA _ _ O", "GN"), ("MOGLIE", "MO _ _ _ E", "GLI"), ("LAVAGNA", "LAVA _ _ A", "GN")], "buchi_cons": "TOCCA 🔊. SCRIVI GLI OPPURE GN.",
  "cloze": ("IMPIEGATA: COME SI ___?<br>GIOVANNI: MI CHIAMO GIOVANNI. IL ___ È OKAFOR.<br>IMPIEGATA: CHE ___ CERCA?", ["chiama", "cognome", "lavoro"], "CHIAMA · COGNOME · LAVORO"),
  "ascolta_num": [("TRE QUATTRO SETTE", 347), ("UNO DUE TRE", 123), ("QUATTRO CINQUE SEI", 456), ("TRE TRE TRE", 333), ("OTTO NOVE ZERO", 890)], "num_es_titolo": "Ascolta il pezzo di numero di telefono",
  "libero": ("I miei dati", "SCRIVI I TUOI DATI: NOME, COGNOME, TELEFONO.", ["NOME", "COGNOME", "TELEFONO"]), "parla": "SEI AL CENTRO PER L'IMPIEGO. DI' COME TI CHIAMI E CHE LAVORO CERCHI.",
  "fine": "ORA SAI DARE I TUOI DATI PER CERCARE LAVORO!",
  "giochi": [["LAVORO", "💼", "LO CERCO"], ["COGNOME", "👪", "IL NOME DELLA FAMIGLIA"], ["NOME", "🪪", "MI CHIAMO…"], ["TELEFONO", "📞", "PER CHIAMARE"], ["INDIRIZZO", "🏠", "VIA E NUMERO"],
             ["MODULO", "📝", "LO COMPILO"], ["FIGLIO", "👦", "GLI"], ["MOGLIE", "👩", "LA SPOSA"], ["BAGNO", "🛁", "GN"], ["RAGNO", "🕷️", "OTTO ZAMPE"],
             ["FOGLIA", "🍃", "SULL'ALBERO"], ["MONTAGNA", "⛰️", "ALTA E GRANDE"], ["LAVAGNA", "🟩", "A SCUOLA"], ["OGNI", "🔁", "OGNI GIORNO"], ["FIRMA", "✍️", "IL MIO NOME A MANO"], ["ZERO", "0️⃣", "0"]]},

 {"n": 13, "dir": "alfa-quale-lavoro", "emo": "👷", "titolo": "QUALE LAVORO?", "sotto": "I MESTIERI · SCI SCE · QU · I MESI",
  "impariamo": [("👷", "I MESTIERI", "CUOCO, MURATORE, BADANTE"), ("🗓️", "QUANDO?", "I MESI DELL'ANNO"), ("🔤", "SCI SCE · QU", "SCIARPA, QUADERNO"), ("💬", "CHE LAVORO FAI?", "FACCIO IL CUOCO")],
  "parole": ["CUOCO", "MURATORE", "PESCE", "QUADERNO", "SCIARPA"],
  "vocab_titolo": "👷 I MESTIERI", "vocab": [("👨‍🍳", "CUOCO"), ("👷", "MURATORE"), ("🧑‍🌾", "CONTADINO"), ("🧹", "COLF"), ("🧑‍🔧", "MECCANICO"), ("🧓", "BADANTE")],
  "dial_titolo": "💬 CHE LAVORO FAI?", "dialogo": [("*SILVIA", "CRISTIAN, CHE LAVORO FAI?"), ("CRISTIAN", "FACCIO IL CUOCO IN UN RISTORANTE DI PESCE."),
      ("*SILVIA", "TI PIACE?"), ("CRISTIAN", "SÌ, MOLTO. E TU?"), ("*SILVIA", "IO FACCIO LA BADANTE. LAVORO CON UNA SIGNORA ANZIANA."), ("CRISTIAN", "QUANDO HAI LE FERIE?"), ("*SILVIA", "AD AGOSTO!")],
  "dial_dom": [("1. CRISTIAN FA IL…", ["CUOCO", "MURATORE"], "CUOCO"), ("2. IL RISTORANTE È DI…", ["PESCE", "CARNE"], "PESCE"),
               ("3. SILVIA FA LA…", ["BADANTE", "CUOCA"], "BADANTE"), ("4. SILVIA HA LE FERIE A…", ["AGOSTO", "MARZO"], "AGOSTO")],
  "lettere": [("SCI · SCE", sill(["SCI", "SCE", "SCA", "SCO"]), ["PESCE", "SCIARPA", "USCITA"]), ("QU", sill(["QUA", "QUE", "QUI", "QUO"]), ["QUADERNO", "QUATTRO", "QUESTO"])],
  "num_titolo": "🗓️ I MESI", "numeri": [(1, "GENNAIO"), (2, "FEBBRAIO"), (3, "MARZO"), (4, "APRILE"), (5, "MAGGIO"), (6, "GIUGNO"), (7, "LUGLIO"), (8, "AGOSTO"),
                                       (9, "SETTEMBRE"), (10, "OTTOBRE"), (11, "NOVEMBRE"), (12, "DICEMBRE")],
  "sillabe": ["CUO-CO", "MU-RA-TO-RE", "PE-SCE", "QUA-DER-NO", "SCIAR-PA"], "sigle": ["SCI", "SCE", "QU"],
  "inizia_lettere": ["SC", "QU"], "inizia": [("🧣", "SCIARPA", "SC"), ("📓", "QUADERNO", "QU"), ("🪜", "SCALA", "SC"), ("4️⃣", "QUATTRO", "QU"), ("👟", "SCARPE", "SC"), ("🖼️", "QUADRO", "QU")],
  "buchi": [("PESCE", "PE _ _ E", "SC"), ("QUATTRO", "_ _ ATTRO", "QU"), ("SCIARPA", "_ _ IARPA", "SC"), ("QUESTO", "_ _ ESTO", "QU")], "buchi_cons": "TOCCA 🔊. SCRIVI SC OPPURE QU.",
  "cloze": ("SILVIA: CHE ___ FAI?<br>CRISTIAN: FACCIO IL ___.<br>SILVIA: TI ___?<br>CRISTIAN: SÌ, MOLTO.", ["lavoro", "cuoco", "piace"], "LAVORO · CUOCO · PIACE"),
  "ascolta_num": [("MARZO", 3), ("AGOSTO", 8), ("DICEMBRE", 12), ("MAGGIO", 5), ("OTTOBRE", 10)], "num_es_titolo": "Ascolta il mese: che numero è?",
  "conti": [(12, 1), (6, 6), (3, 9), (7, 5)],
  "libero": ("Il mio lavoro", "SCRIVI: CHE LAVORO FAI? CHE LAVORO VUOI FARE?", ["FACCIO… / VORREI FARE…"]), "parla": "DI' CHE LAVORO FAI O CHE LAVORO FACEVI NEL TUO PAESE.",
  "fine": "ORA SAI PARLARE DEL TUO LAVORO!",
  "giochi": [["CUOCO", "👨‍🍳", "LAVORA IN CUCINA"], ["MURATORE", "👷", "COSTRUISCE LE CASE"], ["CONTADINO", "🧑‍🌾", "LAVORA IN CAMPAGNA"], ["MECCANICO", "🧑‍🔧", "RIPARA LE MACCHINE"], ["BADANTE", "🧓", "AIUTA GLI ANZIANI"],
             ["PESCE", "🐟", "SCE"], ["SCIARPA", "🧣", "SCI"], ["SCALA", "🪜", "PER SALIRE"], ["QUADERNO", "📓", "QU"], ["QUATTRO", "4️⃣", "4"],
             ["GENNAIO", "❄️", "PRIMO MESE"], ["AGOSTO", "🏖️", "MESE DELLE FERIE"], ["DICEMBRE", "🎄", "ULTIMO MESE"], ["MAGGIO", "🌸", "QUINTO MESE"], ["FERIE", "🏝️", "VACANZE DAL LAVORO"], ["QUADRO", "🖼️", "SUL MURO"]]},

 {"n": 14, "dir": "alfa-cosa-fai-domani", "emo": "📅", "titolo": "COSA FAI DOMANI?", "sotto": "IL TEMPO LIBERO · DOMANI, DOPODOMANI · LA H · LE DATE",
  "impariamo": [("⚽", "IL TEMPO LIBERO", "CALCIO, CINEMA, MARE"), ("📅", "QUANDO?", "DOMANI, SABATO, A LUGLIO"), ("🔤", "LA H", "HO, HAI, HA, HANNO"), ("🗓️", "LE DATE", "IL 25 DICEMBRE")],
  "parole": ["DOMANI", "CINEMA", "MARE", "HO", "FESTA"],
  "vocab_titolo": "⚽ IL TEMPO LIBERO", "vocab": [("⚽", "CALCIO"), ("🎬", "CINEMA"), ("🏖️", "MARE"), ("🚶", "PASSEGGIATA"), ("🎉", "FESTA"), ("📺", "TELEVISIONE")],
  "dial_titolo": "📱 AL TELEFONO", "dialogo": [("MICHELE", "CIAO ENEIDA! COSA FAI DOMANI?"), ("*ENEIDA", "DOMANI HO IL CORSO DI ITALIANO. E TU?"),
      ("MICHELE", "IO VADO AL MARE CON I MIEI FIGLI. VIENI CON NOI DOPODOMANI?"), ("*ENEIDA", "SÌ! A CHE ORA?"), ("MICHELE", "ALLE 10, A PANE E POMODORO."), ("*ENEIDA", "VA BENE. HO ANCHE UN PALLONE!")],
  "dial_dom": [("1. DOMANI ENEIDA HA…", ["IL CORSO", "IL LAVORO"], "IL CORSO"), ("2. MICHELE VA AL MARE CON…", ["I FIGLI", "LA MOGLIE"], "I FIGLI"),
               ("3. VANNO AL MARE ALLE…", ["10", "4"], "10"), ("4. ENEIDA PORTA…", ["UN PALLONE", "UNA TORTA"], "UN PALLONE")],
  "lettere": [("LA H NON SI SENTE", table([["IO", "HO"], ["TU", "HAI"], ["LUI / LEI", "HA"], ["LORO", "HANNO"]], head=["", "AVERE"]), ["HO", "HAI", "HANNO"])],
  "extra": ("📅 QUANDO?", table([["OGGI", "📍"], ["DOMANI", "➡️"], ["DOPODOMANI", "⏩"], ["LA SETTIMANA PROSSIMA", "🗓️"], ["IL MESE PROSSIMO", "📆"]], head=["DICO", ""]) + "\n" + nota("<b>H</b> NON SI SENTE: HO = O. MA <b>HO</b> (AVERE) E <b>O</b> (OPPURE) SONO DIVERSI!")),
  "num_titolo": "🗓️ LE DATE", "numeri": [("1/1", "IL PRIMO GENNAIO"), ("8/3", "L'OTTO MARZO"), ("1/5", "IL PRIMO MAGGIO"), ("2/6", "IL DUE GIUGNO"), ("6/12", "IL SEI DICEMBRE"), ("25/12", "IL VENTICINQUE DICEMBRE")],
  "sillabe": ["DO-MA-NI", "CI-NE-MA", "MA-RE", "FE-STA", "PAS-SEG-GIA-TA"], "sigle": ["H"],
  "inizia_lettere": ["H", "A"], "inizia": [("🫴", "HO", "H"), ("🐝", "APE", "A"), ("🫴", "HANNO", "H"), ("🧑‍🤝‍🧑", "AMICI", "A"), ("🫴", "HAI", "H"), ("🍍", "ANANAS", "A")],
  "buchi": [("HO", "_ O", "H"), ("HAI", "_ AI", "H"), ("HANNO", "_ A _ _ O", "HNN"), ("HA", "_ A", "H")], "buchi_cons": "TOCCA 🔊. SCRIVI LE LETTERE CHE MANCANO. ATTENZIONE ALLA H!",
  "cloze": ("MICHELE: COSA FAI ___?<br>ENEIDA: DOMANI ___ IL CORSO.<br>MICHELE: VIENI AL ___ DOPODOMANI?<br>ENEIDA: SÌ!", ["domani", "ho", "mare"], "DOMANI · HO · MARE"),
  "ascolta_num": [("IL VENTICINQUE DICEMBRE", 25), ("L'OTTO MARZO", 8), ("IL DUE GIUGNO", 2), ("IL SEI DICEMBRE", 6), ("IL QUINDICI AGOSTO", 15)], "num_es_titolo": "Ascolta la data: scrivi il giorno",
  "conti": [(7, 7), (25, 5), (15, 15), (30, 1)],
  "libero": ("Il mio fine settimana", "SCRIVI: COSA FAI DOMANI? E SABATO?", ["DOMANI… SABATO…"]), "parla": "INVITA UN COMPAGNO: «VIENI CON ME…?» DI' QUANDO E DOVE.",
  "fine": "BRAVI! HAI FINITO IL PERCORSO DI ALFABETIZZAZIONE!",
  "giochi": [["DOMANI", "➡️", "IL GIORNO DOPO OGGI"], ["CINEMA", "🎬", "GUARDO UN FILM"], ["MARE", "🏖️", "ACQUA E SABBIA"], ["CALCIO", "⚽", "SPORT CON IL PALLONE"], ["FESTA", "🎉", "MUSICA E AMICI"],
             ["PASSEGGIATA", "🚶", "CAMMINO PER LA CITTÀ"], ["TELEVISIONE", "📺", "LA GUARDO LA SERA"], ["PALLONE", "🏐", "PER GIOCARE"], ["HO", "🫴", "IO …"], ["HAI", "🫴", "TU …"],
             ["HANNO", "🫴", "LORO …"], ["SABATO", "6️⃣", "DOPO VENERDÌ"], ["NATALE", "🎄", "25 DICEMBRE"], ["DATA", "🗓️", "GIORNO E MESE"], ["AMICI", "🧑‍🤝‍🧑", "ESCO CON GLI…"], ["DOPODOMANI", "⏩", "TRA DUE GIORNI"]]},
]

if __name__ == "__main__":
    giochi = {}
    for u in UNITA:
        sl, es = fai(u)
        os.makedirs(u["dir"], exist_ok=True)
        build_slide(u["dir"] + "/index.html", u["titolo"], "ALFABETIZZAZIONE", sl, "alfa")
        build_es(u["dir"] + "/esercizi.html", es)
        giochi[u["dir"]] = ("alfa-percorso", "ALFABETIZZAZIONE", "%s GIOCHI: %s" % (u["emo"], u["titolo"]), u["giochi"])
    build_giochi(giochi)
