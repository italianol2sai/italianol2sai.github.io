"""Crea sillabe-difficili/index.html (A0, chiesta da Erila il 2026-10-28) partendo da sillabe/index.html.
Sillabe di 3 lettere: prima la sillaba di 2 (RA), poi si aggiunge la lettera davanti (T + RA = TRA).
Audio: prima sillabe-difficili/audio/, poi ../sillabe/audio/ (le registrazioni di Erila), poi la voce del computer.
Scrive anche sillabe-difficili/audio/DA-REGISTRARE.txt con i file che mancano.
Uso: python3 _strumenti/sillabe_difficili.py   (dalla cartella principale del sito)"""
import json, os, re, unicodedata

# gruppo: (lettera da aggiungere, colore, consiglio, leggi, completa, riordina, frasi)
# leggi/completa: la sillaba tra [ ] è quella evidenziata o da completare (sempre una sillaba intera).
G = {
 "TR": ("T", "#3a9c58", "👂 T + RA = TRA. DI' LE DUE LETTERE INSIEME, SENZA VOCALE IN MEZZO: TRA, NON TERA.",
        [["[TRE]NO","🚆"],["[TRA]MONTO","🌇"],["[TRI]ANGOLO","🔺"],["QUAT[TRO]","4️⃣"]],
        [["[TRE]","3️⃣"],["VE[TRO]","🪟"],["[TRI]STE","😢"],["MA[TRI]MONIO","💍"],["[TRA]GHETTO","⛴️"]],
        [["TRE-NO","🚆"],["QUAT-TRO","4️⃣"],["TRA-GHET-TO","⛴️"],["TRI-STE","😢"]],
        ["PRENDO IL TRENO.","HO TRE FIGLI.","IL TRAMONTO È BELLO."]),
 "PR": ("P", "#2c6fb3", "👂 P + RA = PRA. NON PERA: TUTTO INSIEME, PRA.",
        [["[PRA]TO","🌱"],["[PRE]GO","🙂"],["[PRI]MAVERA","🌸"],["[PRO]FUMO","🧴"],["[PRU]GNA","🟣"]],
        [["SO[PRA]","⬆️"],["[PRI]MO","🥇"],["SEM[PRE]","🔁"],["[PRE]MIO","🏆"],["A[PRI]LE","📅"]],
        [["PRI-MA-VE-RA","🌸"],["PRO-FU-MO","🧴"],["SO-PRA","⬆️"],["A-PRI-LE","📅"]],
        ["PRONTO, CHI PARLA?","IN PRIMAVERA CI SONO I FIORI.","GRAZIE! PREGO!"]),
 "BR": ("B", "#d98e04", "👂 B + RA = BRA. ATTENZIONE: BRA E PRA SONO DIVERSE!",
        [["FEB[BRE]","🤒"],["[BRO]DO","🍲"],["[BRU]CO","🐛"],["ZE[BRA]","🦓"],["LI[BRO]","📖"]],
        [["[BRA]VO","👏"],["OTTO[BRE]","📅"],["CO[BRA]","🐍"],["FEB[BRA]IO","❄️"],["[BRI]VIDO","🥶"]],
        [["LI-BRO","📖"],["ZE-BRA","🦓"],["FEB-BRE","🤒"],["OT-TO-BRE","📅"]],
        ["IL LIBRO È SUL TAVOLO.","HO LA FEBBRE.","BRAVO! BRAVA!"]),
 "CR": ("C", "#7b4cb8", "👂 C + RA = CRA. IL SUONO È DURO, COME IN CASA.",
        [["[CRE]MA","🧴"],["[CRO]CE","➕"],["[CRI]CETO","🐹"],["MI[CRO]FONO","🎤"],["[CRU]DO","🥩"]],
        [["[CRA]VATTA","👔"],["[CRO]STATA","🥧"],["SE[CRE]TO","🤫"],["MI[CRO]ONDE","📡"],["[CRI]CETO","🐹"]],
        [["CRA-VAT-TA","👔"],["MI-CRO-FO-NO","🎤"],["CRO-STA-TA","🥧"],["CRE-MA","🧴"]],
        ["METTO LA CREMA.","LA CROSTATA È BUONA.","IL CRICETO MANGIA."]),
 "DR": ("D", "#129e8a", "👂 D + RA = DRA. ATTENZIONE: DRA E TRA SONO DIVERSE!",
        [["[DRA]GO","🐉"],["MA[DRE]","👩"],["[DRI]TTO","⬆️"],["QUA[DRO]","🖼️"]],
        [["PA[DRE]","👨"],["LA[DRO]","🦹"],["QUA[DRA]TO","🟥"],["SQUA[DRA]","⚽"],["[DRA]GO","🐉"]],
        [["MA-DRE","👩"],["PA-DRE","👨"],["QUA-DRA-TO","🟥"],["LA-DRO","🦹"]],
        ["MIA MADRE È AL MERCATO.","IL LADRO SCAPPA.","VAI DRITTO!"]),
 "FR": ("F", "#e3572f", "👂 F + RA = FRA. ATTENZIONE: FRA E VRA SONO DIVERSE!",
        [["[FRA]GOLA","🍓"],["[FRE]SCO","🌬️"],["[FRI]GORIFERO","🧊"],["A[FRI]CA","🌍"]],
        [["[FRA]TELLO","👦"],["[FRE]NO","🛑"],["[FRA]SE","💬"],["[FRI]GORIFERO","🧊"],["[FRA]GOLA","🍓"]],
        [["FRA-GO-LA","🍓"],["FRA-TEL-LO","👦"],["A-FRI-CA","🌍"],["FRI-GO-RI-FE-RO","🧊"]],
        ["MIO FRATELLO È ALTO.","LE FRAGOLE SONO ROSSE.","IL LATTE È NEL FRIGORIFERO."]),
 "GR": ("G", "#1f7a8c", "👂 G + RA = GRA. IL SUONO È DURO, COME IN GATTO.",
        [["[GRA]ZIE","🙏"],["[GRI]GIO","🩶"],["[GRU]","🏗️"],["TI[GRE]","🐅"]],
        [["[GRA]TIS","🆓"],["ALLE[GRO]","😀"],["[GRI]GLIA","🍖"],["MA[GRO]","🦴"],["[GRA]NO","🌾"]],
        [["GRA-ZIE","🙏"],["TI-GRE","🐅"],["AL-LE-GRO","😀"],["GRI-GIO","🩶"]],
        ["GRAZIE MILLE!","LA TIGRE È GRANDE.","IL GATTO È GRIGIO."]),
 "ST": ("S", "#d4485b", "👂 S + TA = STA. NON ESTA: LA S È ATTACCATA, STA.",
        [["[STA]ZIONE","🚉"],["[STI]VALI","👢"],["[STO]MACO","🫃"],["[STU]DENTE","🧑‍🎓"]],
        [["PA[STA]","🍝"],["FE[STA]","🎉"],["RI[STO]RANTE","🍽️"],["QUE[STO]","👉"],["[STU]DIARE","📚"]],
        [["STA-ZIO-NE","🚉"],["STU-DEN-TE","🧑‍🎓"],["RI-STO-RAN-TE","🍽️"],["STI-VA-LI","👢"]],
        ["VADO IN STAZIONE.","LA PASTA È BUONA.","SONO UNO STUDENTE."]),
 "SP": ("S", "#e07a1f", "👂 S + PA = SPA. NON ESPA: LA S È ATTACCATA, SPA.",
        [["[SPA]GHETTI","🍝"],["[SPE]SA","🛒"],["[SPI]NACI","🥬"],["[SPO]SA","👰"],["[SPU]GNA","🧽"]],
        [["O[SPE]DALE","🏥"],["A[SPI]RINA","💊"],["[SPE]RANZA","🙏"],["[SPO]SO","🤵"],["[SPA]GHETTI","🍝"]],
        [["O-SPE-DA-LE","🏥"],["SPO-SA","👰"],["SPU-GNA","🧽"],["SPE-SA","🛒"]],
        ["FACCIO LA SPESA.","VADO ALL'OSPEDALE.","MANGIO GLI SPAGHETTI."]),
}
VOC = "AEIOU"

# Gruppi aggiunti dopo (Erila, 2026-10-28): consonante + L, S + consonante, S + 2 consonanti, GN, GLI, SCE/SCI, SCH, CIA/CIE.
# gruppo: (famiglia, etichetta, lettera da aggiungere, sillabe di partenza, sillabe nuove, colore, consiglio, leggi, completa, riordina, frasi)
G2 = {
 "BL": ("CONSONANTE + L", "BL", "B", ["LA","LE","LI","LO","LU"], ["BLA","BLE","BLI","BLO","BLU"], "#d98e04",
        "👂 B + LU = BLU. TUTTO INSIEME, SENZA VOCALE IN MEZZO: BLU, NON BELU.",
        [["[BLU]","🔵"],["PRO[BLE]MA","🤔"],["PUB[BLI]CO","👥"],["[BLU]SA","👚"]],
        [["PRO[BLE]MA","🤔"],["[BLU]SA","👚"],["PUB[BLI]CO","👥"],["[BLU]","🔵"]],
        [["PRO-BLE-MA","🤔"],["BLU-SA","👚"],["PUB-BLI-CO","👥"]],
        ["IL MARE È BLU.","NESSUN PROBLEMA!","LA BLUSA È BIANCA."]),
 "CL": ("CONSONANTE + L", "CL", "C", ["LA","LE","LI","LO","LU"], ["CLA","CLE","CLI","CLO","CLU"], "#7b4cb8",
        "👂 C + LI = CLI. IL SUONO È DURO, COME IN CASA.",
        [["[CLI]NICA","🏥"],["[CLI]MA","🌡️"],["CI[CLI]STA","🚴"],["RICI[CLA]RE","♻️"]],
        [["[CLI]NICA","🏥"],["CI[CLI]STA","🚴"],["RICI[CLA]RE","♻️"],["[CLA]RINETTO","🎷"],["[CLI]MA","🌡️"]],
        [["CLI-NI-CA","🏥"],["CI-CLI-STA","🚴"],["RI-CI-CLA-RE","♻️"],["CLI-MA","🌡️"]],
        ["VADO IN CLINICA.","IL CICLISTA È VELOCE.","IO RICICLO LA CARTA."]),
 "PL": ("CONSONANTE + L", "PL", "P", ["LA","LE","LI","LO","LU"], ["PLA","PLE","PLI","PLO","PLU"], "#2c6fb3",
        "👂 P + LA = PLA. ATTENZIONE: PLA E BLA SONO DIVERSE!",
        [["[PLA]STICA","♻️"],["COM[PLE]ANNO","🎂"],["DI[PLO]MA","📜"],["SEM[PLI]CE","✅"]],
        [["COM[PLE]ANNO","🎂"],["[PLA]STICA","♻️"],["DI[PLO]MA","📜"],["AERO[PLA]NO","✈️"],["[PLU]RALE","👥"]],
        [["COM-PLE-AN-NO","🎂"],["DI-PLO-MA","📜"],["PLA-STI-CA","♻️"],["SEM-PLI-CE","✅"]],
        ["OGGI È IL MIO COMPLEANNO.","HO UN DIPLOMA.","LA BOTTIGLIA È DI PLASTICA."]),
 "SC": ("S + CONSONANTE", "SC", "S", ["CA","CO","CU"], ["SCA","SCO","SCU"], "#3a9c58",
        "👂 S + CA = SCA. IL SUONO È DURO, COME IN CASA. NON ESCA: LA S È ATTACCATA.",
        [["[SCA]LA","🪜"],["[SCO]PA","🧹"],["BO[SCO]","🌲"],["[SCU]RO","🌑"],["PE[SCA]","🍑"]],
        [["TA[SCA]","👖"],["[SCA]TOLA","📦"],["BO[SCO]","🌲"],["[SCU]RO","🌑"],["PE[SCA]","🍑"]],
        [["SCA-TO-LA","📦"],["SCO-PA","🧹"],["PE-SCA","🍑"],["SCA-LA","🪜"]],
        ["SALGO LE SCALE.","IL BOSCO È VERDE.","LA STANZA È SCURA."]),
 "SF": ("S + CONSONANTE", "SF", "S", ["FA","FE","FI","FO","FU"], ["SFA","SFE","SFI","SFO","SFU"], "#e3572f",
        "👂 S + FI = SFI. NON ESFI: LA S È ATTACCATA.",
        [["[SFI]DA","🏆"],["[SFI]LATA","👗"],["[SFE]RA","🔮"],["[SFO]GLIA","🥟"]],
        [["[SFI]DA","🏆"],["[SFI]LATA","👗"],["[SFE]RA","🔮"],["[SFO]GLIA","🥟"]],
        [["SFI-LA-TA","👗"],["SFI-DA","🏆"],["SFE-RA","🔮"]],
        ["È UNA SFIDA.","GUARDO LA SFILATA."]),
 "STR": ("S + 2 CONSONANTI", "STR", "S", ["TRA","TRE","TRI","TRO","TRU"], ["STRA","STRE","STRI","STRO","STRU"], "#d4485b",
        "👂 PRIMA TRA, POI S + TRA = STRA. TRE LETTERE INSIEME: STRA, NON ESTRA.",
        [["[STRA]DA","🛣️"],["FINE[STRA]","🪟"],["[STRU]MENTO","🎸"],["[STRE]GA","🧙"],["MO[STRO]","👹"]],
        [["MINE[STRA]","🍲"],["[STRA]DA","🛣️"],["FINE[STRA]","🪟"],["[STRU]MENTO","🎸"],["DE[STRA]","➡️"],["SINI[STRA]","⬅️"]],
        [["FI-NE-STRA","🪟"],["MI-NE-STRA","🍲"],["STRU-MEN-TO","🎸"],["SI-NI-STRA","⬅️"]],
        ["APRO LA FINESTRA.","GIRA A DESTRA.","LA STRADA È LUNGA."]),
 "SPR": ("S + 2 CONSONANTI", "SPR", "S", ["PRA","PRE","PRI","PRO","PRU"], ["SPRA","SPRE","SPRI","SPRO","SPRU"], "#e07a1f",
        "👂 PRIMA PRE, POI S + PRE = SPRE. TRE LETTERE INSIEME, SENZA VOCALI IN MEZZO.",
        [["[SPRE]MUTA","🍊"],["[SPRE]CO","🗑️"],["A[SPRO]","🍋"]],
        [["[SPRE]MUTA","🍊"],["[SPRE]CO","🗑️"],["A[SPRO]","🍋"]],
        [["SPRE-MU-TA","🍊"],["SPRE-CO","🗑️"],["A-SPRO","🍋"]],
        ["BEVO UNA SPREMUTA.","IL LIMONE È ASPRO."]),
 "SCR": ("S + 2 CONSONANTI", "SCR", "S", ["CRA","CRE","CRI","CRO","CRU"], ["SCRA","SCRE","SCRI","SCRO","SCRU"], "#129e8a",
        "👂 PRIMA CRI, POI S + CRI = SCRI. IL SUONO È DURO, COME IN CASA.",
        [["[SCRI]VERE","✍️"],["[SCRI]VANIA","🗄️"],["[SCRE]MATO","🥛"],["DE[SCRI]VERE","🗣️"]],
        [["[SCRI]VERE","✍️"],["[SCRI]VANIA","🗄️"],["[SCRE]MATO","🥛"],["DE[SCRI]VERE","🗣️"]],
        [["SCRI-VE-RE","✍️"],["SCRI-VA-NI-A","🗄️"],["SCRE-MA-TO","🥛"]],
        ["SCRIVO IL MIO NOME.","IL LATTE È SCREMATO."]),
 "GN": ("SUONI SPECIALI", "GN", "G", ["NA","NE","NI","NO","NU"], ["GNA","GNE","GNI","GNO","GNU"], "#e07a1f",
        "👂 GN È UN SUONO SOLO: BA-GNO, NON BAG-NO.",
        [["BA[GNO]","🛁"],["MONTA[GNA]","⛰️"],["RA[GNO]","🕷️"],["SO[GNO]","💭"],["LE[GNO]","🪵"]],
        [["GIU[GNO]","📅"],["SPU[GNA]","🧽"],["BA[GNO]","🛁"],["LASA[GNA]","🍝"],["CO[GNO]ME","🪪"]],
        [["MON-TA-GNA","⛰️"],["CO-GNO-ME","🪪"],["LA-SA-GNA","🍝"],["SPU-GNA","🧽"]],
        ["IL BAGNO È QUI.","QUAL È IL TUO COGNOME?","VADO IN MONTAGNA."]),
 "GLI": ("SUONI SPECIALI", "GLI", "G", ["LI","LIA","LIE","LIO"], ["GLI","GLIA","GLIE","GLIO"], "#1f7a8c",
        "👂 GLI È UN SUONO SOLO: FI-GLIO, NON FIG-LIO.",
        [["FI[GLIO]","👦"],["FI[GLIA]","👧"],["MO[GLIE]","👰"],["BOTTI[GLIA]","🍾"],["LU[GLIO]","📅"]],
        [["FO[GLIO]","📄"],["A[GLIO]","🧄"],["MO[GLIE]","👰"],["FAMI[GLIA]","👨‍👩‍👧"],["BOTTI[GLIA]","🍾"]],
        [["BOT-TI-GLIA","🍾"],["FA-MI-GLIA","👨‍👩‍👧"],["MO-GLIE","👰"],["LU-GLIO","📅"]],
        ["HO DUE FIGLI.","MIA MOGLIE LAVORA.","UNA BOTTIGLIA D'ACQUA."]),
 "SCI": ("SUONI SPECIALI", "SCE SCI", "S", ["CE","CI","CIA","CIO","CIU"], ["SCE","SCI","SCIA","SCIO","SCIU"], "#3a9c58",
        "👂 SCE SCI È UN SUONO SOLO, MORBIDO: PE-SCE. NON PES-CE.",
        [["PE[SCE]","🐟"],["[SCI]","⛷️"],["U[SCI]TA","🚪"],["CU[SCI]NO","🛏️"],["A[SCIU]GAMANO","🧺"]],
        [["PE[SCE]","🐟"],["U[SCI]TA","🚪"],["CU[SCI]NO","🛏️"],["A[SCIU]GAMANO","🧺"],["[SCI]","⛷️"]],
        [["U-SCI-TA","🚪"],["CU-SCI-NO","🛏️"],["PE-SCE","🐟"],["A-SCIU-GA-MA-NO","🧺"]],
        ["DOV'È L'USCITA?","MANGIO IL PESCE."]),
 "SCH": ("SUONI SPECIALI", "SCHE SCHI", "S", ["CHE","CHI"], ["SCHE","SCHI"], "#7b4cb8",
        "👂 CON LA H IL SUONO È DURO: SCHE SCHI COME SCA SCO. PESCA → PESCHE.",
        [["PE[SCHE]","🍑"],["TA[SCHE]","👖"],["MO[SCHE]","🪰"],["BO[SCHI]","🌲"],["[SCHE]DA","📇"]],
        [["[SCHE]DA","📇"],["BO[SCHI]","🌲"],["PE[SCHE]","🍑"],["TA[SCHE]","👖"],["MO[SCHE]","🪰"]],
        [["PE-SCHE","🍑"],["TA-SCHE","👖"],["SCHE-DA","📇"],["BO-SCHI","🌲"]],
        ["COMPRO LE PESCHE.","LE TASCHE SONO VUOTE."]),
 "CIA": ("SUONI SPECIALI", "CIA CIE", "C", ["IA","IE","IO","IU"], ["CIA","CIE","CIO","CIU"], "#d98e04",
        "👂 CIA CIO CIU: LA I NON SI SENTE BENE, IL SUONO È DOLCE: CIAO. ATTENZIONE: CIELO SI SCRIVE CON CIE.",
        [["[CIA]O","👋"],["[CIE]LO","☁️"],["BA[CIO]","😘"],["CAMI[CIA]","👔"]],
        [["[CIA]O","👋"],["[CIE]LO","☁️"],["BA[CIO]","😘"],["CAMI[CIA]","👔"],["FARMA[CIE]","💊"]],
        [["CA-MI-CIA","👔"],["FAR-MA-CIE","💊"],["BA-CIO","😘"],["CIE-LO","☁️"]],
        ["CIAO! COME STAI?","IL CIELO È BLU."]),
}

def slug(t):
    t = unicodedata.normalize("NFD", t.lower())
    t = "".join(c for c in t if unicodedata.category(c) != "Mn")
    return re.sub(r"[^a-z0-9]+", "-", t).strip("-")

def data():
    out = {}
    for k, (first, color, hint, leggi, completa, riordina, frasi) in G.items():
        fam = "S + CONSONANTE" if k[0] == "S" else "CONSONANTE + R"
        out[k] = {"fam": fam, "color": color, "label": k, "first": first,
                  "base": [k[1] + v for v in VOC], "syl": [k + v for v in VOC], "hint": hint,
                  "leggi": leggi, "completa": completa, "riordina": riordina, "frasi": frasi}
    for k, v in G2.items():
        fam, label, first, base, syl, color, hint, leggi, completa, riordina, frasi = v
        out[k] = {"fam": fam, "color": color, "label": label, "first": first, "base": base, "syl": syl, "hint": hint,
                  "leggi": leggi, "completa": completa, "riordina": riordina, "frasi": frasi}
    fams = ["CONSONANTE + R", "CONSONANTE + L", "S + CONSONANTE", "S + 2 CONSONANTI", "SUONI SPECIALI"]
    return dict(sorted(out.items(), key=lambda kv: fams.index(kv[1]["fam"])))

def build():
    src = open("sillabe/index.html", encoding="utf-8").read()
    D = data()
    js = "const DATA = " + json.dumps(D, ensure_ascii=False, indent=1) + ";\n"
    s = src.replace("<title>Sillabe facili</title>", "<title>SILLABE DIFFICILI</title>")
    s = s.replace("<h1>Sillabe facili</h1>", "<h1>SILLABE DIFFICILI</h1>")
    s = s.replace('<a href="../">← Italiano L2 ETNIE</a>', '<a href="../">← ITALIANO L2 ETNIE</a>')
    a = s.index("const DATA = {"); b = s.index("const MODES = [")
    s = s[:a] + js + s[b:]
    s = s.replace('''const MODES = [
  ["leggi", "👀 Leggi"], ["ascolta", "👂 Ascolta e scegli"], ["cerchia", "⭕ Cerchia"],
  ["completa", "🧩 Completa"], ["riordina", "🔀 Riordina"],
];''', '''const MODES = [
  ["costruisci", "➕ COSTRUISCI"], ["leggi", "👀 LEGGI"], ["ascolta", "👂 ASCOLTA E SCEGLI"], ["cerchia", "⭕ CERCHIA"],
  ["completa", "🧩 COMPLETA"], ["riordina", "🔀 RIORDINA"],
];''')
    s = s.replace('let letter = "B", mode = "leggi";', 'let letter = "TR", mode = "costruisci";')
    s = s.replace('localStorage.getItem("sillabe")', 'localStorage.getItem("sillabe-difficili")')
    s = s.replace('localStorage.setItem("sillabe",', 'localStorage.setItem("sillabe-difficili",')
    # audio: anche le sillabe facili già registrate da Erila
    s = s.replace("for (const url of [`audio/${s}.wav`, `audio/${s}.mp3`, `audio/${s.toUpperCase()}.mp3`]) {",
                  "for (const url of [`audio/${s}.wav`, `audio/${s}.mp3`, `audio/${s}.m4a`, `../sillabe/audio/${s}.wav`, `../sillabe/audio/${s}.mp3`]) {")
    s = s.replace("/* ===== AUDIO: prima cerca audio/<parola>.mp3, altrimenti voce del computer ===== */",
                  "/* ===== AUDIO: prima audio/<parola>, poi ../sillabe/audio/<parola> (voce di Erila), altrimenti voce del computer ===== */")
    # niente minuscolo nelle schede (A0 in maiuscolo)
    s = s.replace('<div class="s">${s}</div><div class="lo">${s.toLowerCase()}</div>', '<div class="s">${s}</div>')
    s = s.replace('const lo = d.label ? "" : `<small>${letter.toLowerCase()}</small>`;', 'const lo = "";')
    # testi delle modalità in maiuscolo
    for x, y in [("Tocca e ascolta", "TOCCA E ASCOLTA"), ("Ascolta la sillaba e tocca quella giusta", "ASCOLTA LA SILLABA E TOCCA QUELLA GIUSTA"),
                 ("Cerchia la sillaba uguale", "CERCHIA LA SILLABA UGUALE"), ("Completa la parola con la sillaba giusta", "COMPLETA LA PAROLA CON LA SILLABA GIUSTA"),
                 ("Metti le sillabe in ordine", "METTI LE SILLABE IN ORDINE"), ("Bravo! 👏", "BRAVO! 👏"), ("Ancora ↻", "ANCORA ↻"),
                 ("Avanti →", "AVANTI →"), ("Mancano: ", "MANCANO: "), ("→ da sinistra a destra", "→ DA SINISTRA A DESTRA")]:
        s = s.replace(x, y)
    # tutte le attività visibili: i pulsanti vanno a capo invece di scorrere
    s = s.replace(".modes { display: flex; gap: 6px; overflow-x: auto;", ".modes { display: flex; flex-wrap: wrap; justify-content: center; gap: 6px; overflow-x: visible;", 1)
    # nuova modalità COSTRUISCI: RA → T + RA = TRA
    css = '''
  .build { display: grid; gap: 12px; }
  .brow { display: flex; align-items: center; justify-content: center; gap: 10px; background: var(--card); border: 1px solid var(--line);
          border-radius: 18px; padding: 12px; font-size: 30px; font-weight: 900; flex-wrap: wrap; }
  .brow .two, .brow .three { border: 3px solid var(--c); color: var(--c); background: var(--card); border-radius: 14px; padding: 6px 14px;
          font-size: 30px; font-weight: 900; cursor: pointer; }
  .brow .add { border: none; background: var(--c); color: #fff; border-radius: 14px; padding: 8px 14px; font-size: 24px; font-weight: 900; cursor: pointer; }
  .brow .first { color: var(--c); }
  .brow .three { background: var(--c); color: #fff; animation: pop .35s; }
  .brow .hide { visibility: hidden; }
  @media (max-width: 520px) { .brow { gap: 6px; flex-wrap: nowrap; padding: 10px 6px; }
    .brow .two, .brow .three { font-size: 22px; padding: 6px 9px; } .brow .add { font-size: 18px; padding: 8px 9px; } }
  @keyframes pop { 0% { transform: scale(.6); } 70% { transform: scale(1.12); } 100% { transform: scale(1); } }
  .letters .fam { flex-basis: 100%; text-align: center; font-size: 12px; font-weight: 800; letter-spacing: .04em; opacity: .65; margin-top: 4px; }
  .all { margin-top: 12px; border: none; background: var(--ink); color: var(--bg); border-radius: 999px; padding: 10px 20px; font-size: 16px; font-weight: 800; cursor: pointer; }
</style>'''
    s = s.replace("</style>", css, 1)
    view = '''
/* ===== ➕ COSTRUISCI: prima la sillaba di 2 lettere, poi si aggiunge la lettera davanti ===== */
let built = {};
function viewCostruisci() {
  const d = DATA[letter];
  if (built.letter !== letter) built = { letter, on: [] };
  return banner("TOCCA ➕ E COSTRUISCI LA SILLABA") + (d.hint ? `<div class="hint">${d.hint}</div>` : "") +
    `<div class="task"><span class="n">1</span> ASCOLTA ${d.base[0]}. POI TOCCA ➕ ${d.first}.</div>
     <div class="build">${d.base.map((b, i) => {
       const on = built.on.includes(i);
       return `<div class="brow">
         <button class="two" data-say="${b}">${b}</button>
         <button class="add" data-build="${i}">➕ ${d.first}</button>
         <span class="${on ? "" : "hide"}">=</span>
         <button class="three ${on ? "" : "hide"}" data-say="${d.syl[i]}">${d.syl[i]}</button>
       </div>`; }).join("")}</div>
     <div style="text-align:center"><button class="all" data-act="all">🔁 DI NUOVO</button></div>`;
}
'''
    s = s.replace("/* ===== 👀 LEGGI ===== */", view + "\n/* ===== 👀 LEGGI ===== */")
    s = s.replace("const v = { leggi: viewLeggi,", "const v = { costruisci: viewCostruisci, leggi: viewLeggi,")
    s = s.replace('const el = e.target.closest("[data-say],[data-act],', 'const el = e.target.closest("[data-say],[data-build],[data-act],')
    s = s.replace('''  if (ds.act === "replay") return say(game.target);''', '''  if (ds.build !== undefined) {                   // costruisci
    const i = +ds.build, d = DATA[letter];
    if (!built.on.includes(i)) built.on.push(i);
    render(); say(d.syl[i]); return;
  }
  if (ds.act === "all") { built = { letter, on: [] }; return render(); }
  if (ds.act === "replay") return say(game.target);''')
    # pulsanti dei gruppi divisi per famiglia
    s = s.replace('''  $("letters").innerHTML = Object.keys(DATA).map(k =>
    `<button style="--lc:${DATA[k].color}" class="${k === letter ? "on" : ""}" data-l="${k}">${DATA[k].label || k}</button>`).join("");''',
    '''  let fam = "";
  $("letters").innerHTML = Object.keys(DATA).map(k => {
    const h = DATA[k].fam !== fam ? `<div class="fam">${fam = DATA[k].fam}</div>` : "";
    return h + `<button style="--lc:${DATA[k].color}" class="${k === letter ? "on" : ""}" data-l="${k}">${DATA[k].label || k}</button>`; }).join("");''')
    os.makedirs("sillabe-difficili/audio", exist_ok=True)
    open("sillabe-difficili/index.html", "w", encoding="utf-8").write(s)
    print("scritto sillabe-difficili/index.html")
    # elenco audio da registrare
    have = {os.path.splitext(f)[0] for f in os.listdir("sillabe/audio")}
    have |= {os.path.splitext(f)[0] for f in os.listdir("sillabe-difficili/audio")}
    groups = [("1. PRIMA DI TUTTO: LE SILLABE", lambda d: d["syl"] + d["base"]),
              ("2. LE PAROLE", lambda d: [re.sub(r"[\[\]]", "", w) for w, _ in d["leggi"] + d["completa"]] + [w.replace("-", "") for w, _ in d["riordina"]]),
              ("3. LE FRASI", lambda d: d["frasi"]),
              ("4. SE HAI TEMPO: I PEZZI DEL GIOCO «RIORDINA»", lambda d: [p for w, _ in d["riordina"] for p in w.split("-")])]
    need, seen = [], set()
    with open("sillabe-difficili/audio/DA-REGISTRARE.txt", "w", encoding="utf-8") as f:
        f.write("REGISTRAZIONI PER «SILLABE DIFFICILI»\n"
                "Un file per ogni riga, con questo nome (va bene .mp3, .m4a o .wav).\n"
                "Le sillabe di 2 lettere (RA, TA, PA...) e molte parole sono già registrate in sillabe/audio: non servono di nuovo.\n"
                "Se un file manca, la pagina usa la voce del computer.\n")
        for title, get in groups:
            f.write("\n\n=== %s ===\n" % title)
            for k, d in D.items():
                for t in get(d):
                    sl = slug(t)
                    if sl in have or sl in seen: continue
                    seen.add(sl); need.append(sl)
                    f.write("%-30s %s\n" % (sl + ".mp3", t))
    print(len(need), "audio da registrare")
    # pagina per registrare (registra.html): tutto quello che non è già in sillabe/audio
    facili = {os.path.splitext(f)[0] for f in os.listdir("sillabe/audio")}
    rec, seen = [], set()
    for title, get in groups:
        for k, d in D.items():
            for t in get(d):
                sl = slug(t)
                if sl in facili or sl in seen: continue
                seen.add(sl); rec.append([["SILLABE", "PAROLE", "FRASI", "PEZZI"][int(title[0]) - 1], sl, t])
    tpl = open(os.path.join(os.path.dirname(__file__), "registra_modello.html"), encoding="utf-8").read()
    open("sillabe-difficili/registra.html", "w", encoding="utf-8").write(
        tpl.replace("/*LISTA*/[]", json.dumps(rec, ensure_ascii=False)))
    print("scritto sillabe-difficili/registra.html con", len(rec), "voci")

if __name__ == "__main__":
    build()
