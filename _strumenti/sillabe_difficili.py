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

def slug(t):
    t = unicodedata.normalize("NFD", t.lower())
    t = "".join(c for c in t if unicodedata.category(c) != "Mn")
    return re.sub(r"[^a-z0-9]+", "-", t).strip("-")

def data():
    out = {}
    for k, (first, color, hint, leggi, completa, riordina, frasi) in G.items():
        base = k[1]
        out[k] = {"color": color, "label": k, "first": first,
                  "base": [base + v for v in VOC], "syl": [k + v for v in VOC], "hint": hint,
                  "leggi": leggi, "completa": completa, "riordina": riordina, "frasi": frasi}
    return out

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
  @keyframes pop { 0% { transform: scale(.6); } 70% { transform: scale(1.12); } 100% { transform: scale(1); } }
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
    # pulsanti delle lettere: gruppi di 2 lettere
    os.makedirs("sillabe-difficili/audio", exist_ok=True)
    open("sillabe-difficili/index.html", "w", encoding="utf-8").write(s)
    print("scritto sillabe-difficili/index.html")
    # elenco audio da registrare
    have = {os.path.splitext(f)[0] for f in os.listdir("sillabe/audio")}
    have |= {os.path.splitext(f)[0] for f in os.listdir("sillabe-difficili/audio")}
    groups = [("1. PRIMA DI TUTTO: LE SILLABE DI 3 LETTERE", lambda d: d["syl"]),
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

if __name__ == "__main__":
    build()
