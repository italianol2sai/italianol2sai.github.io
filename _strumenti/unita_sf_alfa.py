"""Percorso ALFABETIZZAZIONE, unità 2-5 (vedi unita_sf.py per l'origine e le regole).
Ogni unità: parole obiettivo, una o due consonanti con le vocali, i numeri, un piccolo dialogo.
Tutto in STAMPATELLO MAIUSCOLO, una cosa per riga, 🔊 su ogni parola. Testi nuovi, ambientati a Bari.
Uso: python3 _strumenti/unita_sf_alfa.py"""
import os, sys
sys.path.insert(0, os.path.dirname(__file__))
from genera import eq, build as build_es
from unita_primi import cover, slide, cards, table, nota, dialogo, end
from unita_drive import ill, parla, libero
from unita_sf import build_slide, build_giochi, say, parole, x_parola

NUMERI = ["ZERO", "UNO", "DUE", "TRE", "QUATTRO", "CINQUE", "SEI", "SETTE", "OTTO", "NOVE", "DIECI", "UNDICI", "DODICI", "TREDICI",
          "QUATTORDICI", "QUINDICI", "SEDICI", "DICIASSETTE", "DICIOTTO", "DICIANNOVE", "VENTI", "VENTUNO", "VENTIDUE", "VENTITRÉ"]

def S(t):  # sillaba evidenziata
    return "<span class='sill'>%s</span>" % t

def E(e):
    return "<span class='emo'>%s</span>" % e

def griglia_numeri(coppie):
    return '    <div class="numeri">' + "".join('<div data-say="%s"><b>%s</b><span>%s</span></div>' % (w, n, w) for n, w in coppie) + "</div>"

def lettera(l, parole_):
    return '    <div class="lettera" data-say="%s">%s<small>%s</small></div>\n' % (l, l, l.lower()) + parole(parole_)

def sillabe_tab(cons):
    return table([[S(cons + v) for v in "AEIOU"]], head=["%s + A" % cons, "%s + E" % cons, "%s + I" % cons, "%s + O" % cons, "%s + U" % cons])

# ---------- esercizi tipo (gli stessi in ogni unità, come nel libro) ----------
def es_ascolta(eid, n, items):
    return {"id": eid, "title": "%d · 🔊 Ascolta e scegli la parola" % n, "short": "%d · Ascolta" % n, "type": "choice",
            "cons": "TOCCA 🔊. SCEGLI LA PAROLA CHE SENTI.",
            "items": [x_parola(i + 1, w, o) for i, (w, o) in enumerate(items)], "k": [eq(w) for w, _ in items]}

def es_uguale(eid, n, items):
    return {"id": eid, "title": "%d · 👀 Cerca la parola uguale" % n, "short": "%d · Uguale" % n, "type": "choice",
            "cons": "GUARDA LA PAROLA. TROVA LA PAROLA UGUALE.",
            "items": [{"q": "<b>%s</b>" % w, "opts": o} for w, o in items], "k": [eq(w) for w, _ in items]}

def es_copia(eid, n, words, emoji=None):
    return {"id": eid, "title": "%d · ✍️ Copia la parola" % n, "short": "%d · Copia" % n, "type": "text", "w": "m",
            "cons": "GUARDA E SCRIVI LA STESSA PAROLA.",
            "items": [{"q": (E(emoji[i]) + " " if emoji else "") + w} for i, w in enumerate(words)], "k": [eq(w) for w in words]}

def es_lettera(eid, n, items, cons="TOCCA 🔊. SCRIVI LA LETTERA CHE MANCA."):
    """items: (parola, con buchi, risposta)"""
    return {"id": eid, "title": "%d · 🔊 Ascolta e scrivi la lettera" % n, "short": "%d · La lettera" % n, "type": "text", "w": "s",
            "cons": cons, "items": [{"q": say(w) + " " + b} for w, b, _ in items],
            "k": [eq(k, " ".join(k)) for _, _, k in items]}

def es_sillabe(eid, n, items):
    """items: lista di parole divise con '-' (MA-TI-TA)"""
    return {"id": eid, "title": "%d · 🧩 Componi la parola" % n, "short": "%d · Le sillabe" % n, "type": "text", "w": "m",
            "cons": "UNISCI I PEZZI. SCRIVI LA PAROLA.",
            "items": [{"q": " + ".join(S(x) for x in w.split("-")) + " ="} for w in items], "k": [eq(w.replace("-", "")) for w in items]}

def es_inizia(eid, n, lettere, items):
    """items: (emoji, parola, lettera giusta)"""
    return {"id": eid, "title": "%d · 🔊 Con che lettera comincia?" % n, "short": "%d · Comincia con" % n, "type": "choice",
            "cons": "TOCCA 🔊. LA PAROLA COMINCIA CON " + " O CON ".join("<b>%s</b>" % l for l in lettere) + "?", "opts": lettere,
            "items": [{"q": E(e) + " " + say(w)} for e, w, _ in items], "k": [eq(l) for _, _, l in items]}

def es_conta(eid, n, items):
    return {"id": eid, "title": "%d · 🔢 Conta e scrivi il numero" % n, "short": "%d · Conta" % n, "type": "text", "w": "s",
            "cons": "CONTA. SCRIVI IL NUMERO CON LE CIFRE.", "items": [{"q": E(e * k)} for e, k in items],
            "k": [eq(str(k), NUMERI[k] if k < len(NUMERI) else str(k)) for _, k in items]}

def es_numeri(eid, n, items, title="Ascolta e scrivi il numero"):
    """items: (come si legge, risposta in cifre)"""
    return {"id": eid, "title": "%d · 🔊 %s" % (n, title), "short": "%d · I numeri" % n, "type": "text", "w": "s",
            "cons": "TOCCA 🔊. SCRIVI IL NUMERO CON LE CIFRE: 0, 1, 2…",
            "items": [{"q": say(w) + " %d." % (i + 1)} for i, (w, _) in enumerate(items)], "k": [eq(str(r)) for _, r in items]}

def es_conti(eid, n, items, segno="+"):
    return {"id": eid, "title": "%d · ➕ Fai il conto" % n if segno == "+" else "%d · ➖ Fai il conto" % n, "short": "%d · I conti" % n,
            "type": "text", "w": "s", "cons": "SCRIVI IL RISULTATO.",
            "items": [{"q": "%d %s %d =" % (a, segno, b)} for a, b in items], "k": [eq(str(a + b if segno == "+" else a - b)) for a, b in items]}

def es_dialogo(eid, n, parts, keys, bank):
    out = []
    for i, p in enumerate(parts.split("___")):
        out.append(p)
        if i < parts.count("___"):
            out.append({})
    return {"id": eid, "title": "%d · 🗣️ Completa il dialogo" % n, "short": "%d · Il dialogo" % n, "type": "cloze",
            "cons": "SCRIVI LA PAROLA GIUSTA.", "bank": bank, "parts": out, "k": [eq(k) for k in keys]}

def es_scegli(eid, n, title, items, opts=None, cons=None):
    d = {"id": eid, "title": "%d · %s" % (n, title), "short": "%d · %s" % (n, title.split(" ", 1)[-1][:18]), "type": "choice",
         "items": [{"q": q, "opts": o} if o else {"q": q} for q, o, _ in items], "k": [eq(k) for _, _, k in items]}
    if opts: d["opts"] = opts
    if cons: d["cons"] = cons
    return d

def pagina(title, store, sections):
    return {"title": title, "store": store, "upper": True, "livello": "alfa",
            "sub": "🔊 TOCCA E ASCOLTA. ✍️ SCRIVI O 👆 SCEGLI. POI PREMI «CONTROLLA».", "sections": sections}

# =====================================================================
# UNITÀ 2 · VADO AL CORSO
# =====================================================================
U2_SLIDE = [
    cover("🏫", "VADO AL CORSO", "A SCUOLA · LA VOCALE U · D E M · I NUMERI DA 11 A 23", "ALFABETIZZAZIONE &bull; UNITÀ 2"),
    slide("CHE COSA IMPARIAMO?", cards([("📚", "A SCUOLA", "LEGGIAMO, SCRIVIAMO, PARLIAMO"), ("📅", "IL CORSO", "QUANDO? DOVE? QUANTO COSTA?"),
                                         ("🔤", "U · D · M", "LE LETTERE NUOVE"), ("🔢", "11 → 23", "I NUMERI")])),
    slide("🗣️ LE PAROLE", parole([("SCUOLA", "scuola"), ("STUDENTI", "studenti"), ("LIBRO", "libro"), ("VADO", "vado"), ("DUE", "due")]) + "\n" +
          nota("👆 TOCCA LA PAROLA E ASCOLTA.")),
    slide("✏️ CHE COSA FACCIAMO A SCUOLA?", ill("alfa2-scuola.jpg", "STUDENTI ADULTI IN CLASSE CHE LEGGONO, SCRIVONO E ASCOLTANO") + "\n" + cards([
        ("👂", "ASCOLTIAMO", ""), ("🗣️", "PARLIAMO", ""), ("✍️", "SCRIVIAMO", ""), ("📖", "LEGGIAMO", "")])),
    slide("🗣️ IN SEGRETERIA", dialogo([
        ("IBRAHIM", "BUONGIORNO. VORREI FARE IL CORSO DI ITALIANO."),
        ("*SALEAH", "BUONGIORNO! IL CORSO È IL LUNEDÌ E IL MERCOLEDÌ."),
        ("IBRAHIM", "A CHE ORA?"),
        ("*SALEAH", "DALLE 9 ALLE 11."),
        ("IBRAHIM", "QUANTO COSTA?"),
        ("*SALEAH", "È GRATIS. SERVE UN DOCUMENTO.")])),
    slide("📄 IL VOLANTINO", nota("<b>CORSO DI ITALIANO PER ADULTI</b><br>📍 VIA DIEGO 3, BARI<br>📅 LUNEDÌ E MERCOLEDÌ<br>🕘 ORE 9:00 - 11:00<br>💶 GRATIS<br>🪪 PORTA UN DOCUMENTO",
                                  "font-size:1.6rem;text-align:left") + "\n" + nota("👀 GUARDO IL VOLANTINO: TROVO IL GIORNO, L'ORA E IL PREZZO.")),
    slide("🔤 LA VOCALE U", lettera("U", [(S("U") + "VA", "uva"), (S("U") + "NO", "uno"), ("D" + S("U") + "E", "due"), ("SC" + S("U") + "OLA", "scuola")])),
    slide("🔤 LA LETTERA D", sillabe_tab("D") + "\n" + parole([(S("DO") + "VE", "dove"), (S("DU") + "E", "due"), ("VA" + S("DO"), "vado"), (S("DO") + "DICI", "dodici")])),
    slide("🔤 LA LETTERA M", sillabe_tab("M") + "\n" + parole([(S("MO") + "TO", "moto"), (S("MA") + "NO", "mano"), (S("ME") + "LA", "mela"), (S("MU") + "RO", "muro")])),
    slide("🔢 I NUMERI DA 11 A 23", griglia_numeri([(i, NUMERI[i]) for i in range(11, 24)])),
    end("ORA SAI PARLARE DELLA SCUOLA!"),
]
U2 = pagina("🏫 Vado al corso · Esercizi", "alfa-vado-al-corso", [
    {"part": "Ascolto e leggo"},
    es_ascolta("e1", 1, [("SCUOLA", ["SCUOLA", "LIBRO", "DUE"]), ("LIBRO", ["VADO", "LIBRO", "STUDENTI"]), ("STUDENTI", ["STUDENTI", "SCUOLA", "DUE"]),
                         ("VADO", ["DUE", "LIBRO", "VADO"]), ("DUE", ["DUE", "VADO", "SCUOLA"])]),
    es_scegli("e2", 2, "👀 Che cosa fa Ibrahim?", [(E("✍️"), None, "SCRIVE"), (E("📖"), None, "LEGGE"), (E("👂"), None, "ASCOLTA"), (E("🗣️"), None, "PARLA")],
              opts=["SCRIVE", "LEGGE", "ASCOLTA", "PARLA"], cons="GUARDA IL DISEGNO. SCEGLI."),
    {"part": "Scrivo"},
    es_copia("e3", 3, ["SCUOLA", "LIBRO", "VADO", "DUE", "STUDENTI"]),
    es_sillabe("e4", 4, ["SCUO-LA", "LI-BRO", "VA-DO", "STU-DEN-TI", "MO-TO"]),
    {"part": "Le lettere U, D, M"},
    es_lettera("e5", 5, [("UVA", "_ VA", "U"), ("DUE", "D _ E", "U"), ("UNO", "_ NO", "U"), ("MURO", "M _ RO", "U")]),
    es_inizia("e6", 6, ["D", "M"], [("🍎", "MELA", "M"), ("🎲", "DADO", "D"), ("✋", "MANO", "M"), ("🦷", "DENTE", "D"), ("🏍️", "MOTO", "M"), ("💶", "DENARO", "D")]),
    es_lettera("e7", 7, [("MANO", "_ ANO", "M"), ("DADO", "_ A _ O", "DD"), ("MOTO", "_ OTO", "M"), ("DOVE", "_ OVE", "D")],
               cons="TOCCA 🔊. SCRIVI <b>D</b> OPPURE <b>M</b>."),
    {"part": "Il volantino"},
    es_scegli("e8", 8, "📄 Leggi il volantino", [
        ("1. IL CORSO È…", ["LUNEDÌ E MERCOLEDÌ", "MARTEDÌ E GIOVEDÌ"], "LUNEDÌ E MERCOLEDÌ"),
        ("2. A CHE ORA?", ["9:00 - 11:00", "15:00 - 17:00"], "9:00 - 11:00"),
        ("3. QUANTO COSTA?", ["10 EURO", "GRATIS"], "GRATIS"),
        ("4. CHE COSA PORTO?", ["UN DOCUMENTO", "UNA FOTO"], "UN DOCUMENTO")]),
    es_dialogo("e9", 9, "IBRAHIM: VORREI FARE IL ___ DI ITALIANO.<br>SALEAH: È IL LUNEDÌ. ___ DALLE 9 ALLE 11.<br>IBRAHIM: QUANTO ___?<br>SALEAH: È ___.",
               ["corso", "ore", "costa", "gratis"], "CORSO · ORE · COSTA · GRATIS"),
    {"part": "I numeri"},
    es_conta("e10", 10, [("✏️", 12), ("📕", 15), ("🪑", 11), ("🍎", 20)]),
    es_numeri("e11", 11, [("TREDICI", 13), ("DICIOTTO", 18), ("VENTIDUE", 22), ("SEDICI", 16), ("DICIANNOVE", 19)]),
    libero("e12", 12, "Il mio corso", "SCRIVI: IL GIORNO E L'ORA DEL TUO CORSO.", ["GIORNO", "ORA"], rows=1),
    parla("e13", 13, "DI' CHE COSA FAI A SCUOLA: «A SCUOLA LEGGO, SCRIVO…»"),
])

# =====================================================================
# UNITÀ 3 · LA MIA GIORNATA
# =====================================================================
GIORNI = ["LUNEDÌ", "MARTEDÌ", "MERCOLEDÌ", "GIOVEDÌ", "VENERDÌ", "SABATO", "DOMENICA"]
U3_SLIDE = [
    cover("☀️", "LA MIA GIORNATA", "MATTINA, POMERIGGIO, SERA · A E I · D E M · I NUMERI DA 24 A 60", "ALFABETIZZAZIONE &bull; UNITÀ 3"),
    slide("CHE COSA IMPARIAMO?", cards([("🌅", "LA GIORNATA", "MATTINA, POMERIGGIO, SERA"), ("📅", "LA SETTIMANA", "LUNEDÌ, MARTEDÌ…"),
                                         ("🎂", "IL COMPLEANNO", "QUANTI ANNI HAI?"), ("🔢", "24 → 60", "I NUMERI")])),
    slide("🗣️ LE PAROLE", parole([("OGGI", "oggi"), ("IERI", "ieri"), ("MATTINA", "mattina"), ("POMERIGGIO", "pomeriggio"), ("SERA", "sera")])),
    slide("🕗 LA GIORNATA DI MARIAMA", ill("alfa3-giornata.jpg", "UNA DONNA IN TRE MOMENTI DELLA GIORNATA: MATTINA, POMERIGGIO, SERA") + "\n" + cards([
        ("🌅", "LA MATTINA", "VADO A SCUOLA"), ("🌇", "IL POMERIGGIO", "LAVORO"), ("🌙", "LA SERA", "CUCINO E GUARDO LA TV")], "g3")),
    slide("📅 I GIORNI DELLA SETTIMANA", parole([(g, g.lower()) for g in GIORNI])),
    slide("🗓️ LA MIA SETTIMANA", table([["LUNEDÌ", "SCUOLA 📚"], ["MARTEDÌ", "LAVORO 🧹"], ["MERCOLEDÌ", "SCUOLA 📚"], ["GIOVEDÌ", "MEDICO 🩺"],
                                        ["VENERDÌ", "MOSCHEA / CHIESA 🕌"], ["SABATO", "MERCATO 🛒"], ["DOMENICA", "RIPOSO 😴"]], head=["GIORNO", "MARIAMA"])),
    slide("🎂 IL COMPLEANNO", dialogo([
        ("*CRISTIAN", "MARIAMA, QUANDO È IL TUO COMPLEANNO?"),
        ("MARIAMA", "OGGI! HO 34 ANNI."),
        ("*CRISTIAN", "AUGURI! BUON COMPLEANNO!"),
        ("MARIAMA", "GRAZIE!")])),
    slide("🔤 LE VOCALI A E I", lettera("A", [(S("A") + "MICO", "amico"), ("C" + S("A") + "S" + S("A"), "casa")]) + "\n" +
          lettera("I", [(S("I") + "ERI", "ieri"), ("OGG" + S("I"), "oggi")])),
    slide("🔤 D + I · M + A · M + E", parole([(S("DI") + "ECI", "dieci"), ("LUNE" + S("DI"), "lunedì"), (S("MA") + "TTINA", "mattina"), (S("ME") + "RCATO", "mercato")])),
    slide("🔢 I NUMERI DA 24 A 60", griglia_numeri([(24, "VENTIQUATTRO"), (25, "VENTICINQUE"), (28, "VENTOTTO"), (30, "TRENTA"), (34, "TRENTAQUATTRO"),
                                                     (40, "QUARANTA"), (45, "QUARANTACINQUE"), (50, "CINQUANTA"), (55, "CINQUANTACINQUE"), (60, "SESSANTA")])),
    end("ORA SAI RACCONTARE LA TUA GIORNATA!"),
]
U3 = pagina("☀️ La mia giornata · Esercizi", "alfa-la-mia-giornata", [
    {"part": "Ascolto e leggo"},
    es_ascolta("e1", 1, [("OGGI", ["OGGI", "IERI", "SERA"]), ("MATTINA", ["SERA", "MATTINA", "OGGI"]), ("SERA", ["SERA", "IERI", "MATTINA"]),
                         ("POMERIGGIO", ["MATTINA", "POMERIGGIO", "OGGI"]), ("IERI", ["OGGI", "SERA", "IERI"])]),
    es_scegli("e2", 2, "👀 Mattina, pomeriggio o sera?", [(E("🌅") + " ☕", None, "MATTINA"), (E("🌙") + " 😴", None, "SERA"),
                                                          (E("🌇") + " 🧹", None, "POMERIGGIO"), (E("🌅") + " 🏫", None, "MATTINA")],
              opts=["MATTINA", "POMERIGGIO", "SERA"], cons="GUARDA. SCEGLI."),
    {"part": "I giorni"},
    es_ascolta("e3", 3, [("LUNEDÌ", ["LUNEDÌ", "MARTEDÌ", "SABATO"]), ("GIOVEDÌ", ["VENERDÌ", "GIOVEDÌ", "DOMENICA"]),
                         ("SABATO", ["SABATO", "MERCOLEDÌ", "LUNEDÌ"]), ("DOMENICA", ["MARTEDÌ", "DOMENICA", "GIOVEDÌ"])]),
    {"id": "e4", "title": "4 · 📅 Che giorno viene dopo?", "short": "4 · Dopo", "type": "select", "opts": GIORNI,
     "cons": "SCEGLI IL GIORNO CHE VIENE DOPO.",
     "items": [{"q": "LUNEDÌ → "}, {"q": "MERCOLEDÌ → "}, {"q": "VENERDÌ → "}, {"q": "SABATO → "}],
     "k": [eq("MARTEDÌ"), eq("GIOVEDÌ"), eq("SABATO"), eq("DOMENICA")]},
    es_scegli("e5", 5, "🗓️ La settimana di Mariama", [("1. LUNEDÌ MARIAMA VA…", ["A SCUOLA", "AL MERCATO"], "A SCUOLA"),
                                                     ("2. GIOVEDÌ VA…", ["AL LAVORO", "DAL MEDICO"], "DAL MEDICO"),
                                                     ("3. SABATO VA…", ["AL MERCATO", "A SCUOLA"], "AL MERCATO"),
                                                     ("4. DOMENICA…", ["LAVORA", "RIPOSA"], "RIPOSA")]),
    {"part": "Scrivo"},
    es_copia("e6", 6, ["OGGI", "MATTINA", "SERA", "LUNEDÌ", "SABATO"]),
    es_sillabe("e7", 7, ["MAT-TI-NA", "SE-RA", "PO-ME-RIG-GIO", "DO-ME-NI-CA", "SA-BA-TO"]),
    es_inizia("e8", 8, ["A", "I"], [("🐝", "APE", "A"), ("🏝️", "ISOLA", "I"), ("🍍", "ANANAS", "A"), ("🧑‍🤝‍🧑", "AMICI", "A"), ("💉", "INIEZIONE", "I")]),
    es_lettera("e9", 9, [("DIECI", "D _ ECI", "I"), ("CASA", "C _ S _", "AA"), ("OGGI", "OGG _", "I"), ("MAMMA", "M _ MM _", "AA")]),
    {"part": "Il compleanno e i numeri"},
    es_dialogo("e10", 10, "CRISTIAN: QUANDO È IL TUO ___?<br>MARIAMA: ___! HO 34 ___.<br>CRISTIAN: ___!",
               ["compleanno", "oggi", "anni", "auguri"], "COMPLEANNO · OGGI · ANNI · AUGURI"),
    es_numeri("e11", 11, [("TRENTA", 30), ("QUARANTACINQUE", 45), ("VENTISETTE", 27), ("CINQUANTA", 50), ("SESSANTA", 60)]),
    es_conti("e12", 12, [(20, 10), (25, 5), (30, 30), (40, 12)]),
    libero("e13", 13, "La mia giornata", "SCRIVI CHE COSA FAI: LA MATTINA… IL POMERIGGIO… LA SERA…", ["LA MATTINA", "IL POMERIGGIO", "LA SERA"], rows=1),
    parla("e14", 14, "RACCONTA LA TUA SETTIMANA: «LUNEDÌ VADO A SCUOLA…»"),
])

# =====================================================================
# UNITÀ 4 · MI DESCRIVO
# =====================================================================
U4_SLIDE = [
    cover("🧥", "MI DESCRIVO", "I VESTITI · I CAPELLI · QUANTO COSTA? · L, S, G · I NUMERI DA 60 A 100", "ALFABETIZZAZIONE &bull; UNITÀ 4"),
    slide("CHE COSA IMPARIAMO?", cards([("👕", "I VESTITI", "PANTALONI, GUANTI, BORSA"), ("💇", "COME SONO", "ALTO, BASSO, CAPELLI LUNGHI"),
                                         ("💶", "QUANTO COSTA?", "COSTA 20 EURO"), ("🔢", "60 → 100", "I NUMERI E LE ADDIZIONI")])),
    slide("🗣️ LE PAROLE", parole([("CAPELLI", "capelli"), ("COLORE", "colore"), ("PANTALONI", "pantaloni"), ("GUANTI", "guanti"), ("BORSA", "borsa")])),
    slide("👕 I VESTITI", ill("alfa4-vestiti.jpg", "VESTITI COLORATI: PANTALONI, MAGLIONE, GUANTI, BORSA, SCARPE, GIACCA") + "\n" + cards([
        ("👖", "I PANTALONI", ""), ("🧤", "I GUANTI", ""), ("👜", "LA BORSA", ""), ("🧥", "LA GIACCA", ""), ("👟", "LE SCARPE", ""), ("🧶", "IL MAGLIONE", "")], "g3")),
    slide("🎨 I COLORI", '    <div class="colori4">' + "".join('<div style="background:%s" data-say="%s">%s</div>' % c for c in [
        ("#d63a2f", "ROSSO", "ROSSO"), ("#1f6fd1", "BLU", "BLU"), ("#1e9e5a", "VERDE", "VERDE"), ("#e0a800", "GIALLO", "GIALLO"),
        ("#222", "NERO", "NERO"), ("#888", "GRIGIO", "GRIGIO"), ("#7a4b2a", "MARRONE", "MARRONE"), ("#e66fa4", "ROSA", "ROSA")]) + "</div>"),
    slide("💇 COME SEI?", cards([("🧍", "ALTO / ALTA", ""), ("🧍", "BASSO / BASSA", ""), ("👩‍🦱", "CAPELLI RICCI", ""), ("👱", "CAPELLI LISCI", ""),
                                 ("👩", "CAPELLI LUNGHI", ""), ("👨", "CAPELLI CORTI", "")], "g3") + "\n" +
          nota("IO SONO ALTA. HO I CAPELLI LUNGHI E NERI. OGGI HO I PANTALONI BLU.")),
    slide("🛍️ AL MERCATO", dialogo([
        ("GRACE", "BUONGIORNO. QUANTO COSTANO QUESTI GUANTI?"),
        ("*VENDITORE", "COSTANO 8 EURO."),
        ("GRACE", "E LA BORSA ROSSA?"),
        ("*VENDITORE", "LA BORSA COSTA 20 EURO."),
        ("GRACE", "VA BENE, PRENDO I GUANTI. ECCO 10 EURO."),
        ("*VENDITORE", "ECCO IL RESTO: 2 EURO. GRAZIE!")])),
    slide("🔤 L · S · G", table([[S("LA"), S("LE"), S("LI"), S("LO"), S("LU")], [S("SA"), S("SE"), S("SI"), S("SO"), S("SU")], [S("GU") + "ANTI", "LIN" + S("GU") + "A", "", "", ""]]) + "\n" +
          parole([("CAPE" + S("LLI"), "capelli"), (S("BO") + "R" + S("SA"), "borsa"), (S("GU") + "ANTI", "guanti")])),
    slide("🔢 I NUMERI DA 60 A 100", griglia_numeri([(60, "SESSANTA"), (65, "SESSANTACINQUE"), (70, "SETTANTA"), (75, "SETTANTACINQUE"), (80, "OTTANTA"),
                                                      (85, "OTTANTACINQUE"), (90, "NOVANTA"), (95, "NOVANTACINQUE"), (99, "NOVANTANOVE"), (100, "CENTO")])),
    end("ORA SAI DESCRIVERE TE E I TUOI VESTITI!"),
]
U4 = pagina("🧥 Mi descrivo · Esercizi", "alfa-mi-descrivo", [
    {"part": "Ascolto e leggo"},
    es_ascolta("e1", 1, [("CAPELLI", ["CAPELLI", "COLORE", "BORSA"]), ("GUANTI", ["PANTALONI", "GUANTI", "COLORE"]), ("BORSA", ["BORSA", "CAPELLI", "GUANTI"]),
                         ("PANTALONI", ["COLORE", "BORSA", "PANTALONI"]), ("COLORE", ["COLORE", "GUANTI", "CAPELLI"])]),
    es_scegli("e2", 2, "👀 Che cos'è?", [(E("👖"), None, "PANTALONI"), (E("🧤"), None, "GUANTI"), (E("👜"), None, "BORSA"), (E("🧥"), None, "GIACCA")],
              opts=["PANTALONI", "GUANTI", "BORSA", "GIACCA"], cons="GUARDA. SCEGLI LA PAROLA."),
    es_scegli("e3", 3, "🎨 Che colore è?", [(E("🍅"), None, "ROSSO"), (E("🌿"), None, "VERDE"), (E("🍌"), None, "GIALLO"), (E("🫐"), None, "BLU")],
              opts=["ROSSO", "VERDE", "GIALLO", "BLU"], cons="GUARDA. SCEGLI IL COLORE."),
    {"part": "Scrivo"},
    es_copia("e4", 4, ["CAPELLI", "BORSA", "GUANTI", "PANTALONI", "COLORE"], emoji=["💇", "👜", "🧤", "👖", "🎨"]),
    es_sillabe("e5", 5, ["CA-PEL-LI", "BOR-SA", "GUAN-TI", "PAN-TA-LO-NI", "CO-LO-RE"]),
    es_inizia("e6", 6, ["L", "S"], [("🍋", "LIMONE", "L"), ("☀️", "SOLE", "S"), ("🌙", "LUNA", "L"), ("🪑", "SEDIA", "S"), ("📖", "LIBRO", "L"), ("🧂", "SALE", "S")]),
    es_lettera("e7", 7, [("LUNA", "_ UNA", "L"), ("SOLE", "_ OLE", "S"), ("GUANTI", "G _ ANTI", "U"), ("SALE", "_ A _ E", "SL")]),
    {"part": "Quanto costa?"},
    es_scegli("e8", 8, "🛍️ Al mercato", [("1. I GUANTI COSTANO…", ["8 EURO", "20 EURO"], "8 EURO"), ("2. LA BORSA È…", ["ROSSA", "NERA"], "ROSSA"),
                                         ("3. GRACE PRENDE…", ["LA BORSA", "I GUANTI"], "I GUANTI"), ("4. IL RESTO È…", ["2 EURO", "12 EURO"], "2 EURO")]),
    es_dialogo("e9", 9, "GRACE: QUANTO ___ LA BORSA?<br>VENDITORE: 20 ___.<br>GRACE: E I GUANTI?<br>VENDITORE: ___ 8 EURO.",
               ["costa", "euro", "costano"], "COSTA · COSTANO · EURO"),
    {"part": "I numeri e i conti"},
    es_numeri("e10", 10, [("SETTANTA", 70), ("OTTANTACINQUE", 85), ("NOVANTA", 90), ("SESSANTAQUATTRO", 64), ("CENTO", 100)]),
    es_conti("e11", 11, [(60, 20), (45, 30), (50, 50), (72, 8), (35, 35)]),
    libero("e12", 12, "Come sono", "SCRIVI: COME SEI? CHE VESTITI HAI OGGI?", ["IO SONO… HO I CAPELLI…", "OGGI HO…"], rows=1),
    parla("e13", 13, "DESCRIVI UN COMPAGNO O UNA COMPAGNA: È ALTO? HA I CAPELLI…? CHE VESTITI HA?"),
])

# =====================================================================
# UNITÀ 5 · LE MIE EMOZIONI
# =====================================================================
U5_SLIDE = [
    cover("😊", "LE MIE EMOZIONI", "COME STAI? · LA LETTERA F · I NUMERI DA 100 A 500", "ALFABETIZZAZIONE &bull; UNITÀ 5"),
    slide("CHE COSA IMPARIAMO?", cards([("😊", "COME STAI?", "STO BENE, SONO FELICE"), ("😢", "LE EMOZIONI", "TRISTE, ARRABBIATO, STANCO"),
                                         ("🔤", "LA F", "FELICE, FAMIGLIA, FERMATA"), ("🔢", "100 → 500", "I NUMERI")])),
    slide("🗣️ LE PAROLE", parole([("FELICE", "felice"), ("FAMIGLIA", "famiglia"), ("FERMATA", "fermata"), ("SOFIA", "sofia")])),
    slide("😊 LE EMOZIONI", ill("alfa5-emozioni.jpg", "SEI VOLTI CON EMOZIONI DIVERSE: FELICE, TRISTE, ARRABBIATO, STANCO, PAURA, SORPRESO") + "\n" + cards([
        ("😊", "FELICE", ""), ("😢", "TRISTE", ""), ("😠", "ARRABBIATO / ARRABBIATA", ""), ("😴", "STANCO / STANCA", ""), ("😨", "HO PAURA", ""), ("😮", "SORPRESO / SORPRESA", "")], "g3")),
    slide("🚏 ALLA FERMATA", ill("alfa5-fermata.jpg", "UNA DONNA E UN UOMO ASPETTANO L'AUTOBUS ALLA FERMATA") + "\n" + dialogo([
        ("*SOFIA", "CIAO YUSUF! COME STAI?"),
        ("YUSUF", "NON MOLTO BENE. SONO STANCO E TRISTE."),
        ("*SOFIA", "PERCHÉ?"),
        ("YUSUF", "LA MIA FAMIGLIA È LONTANA."),
        ("*SOFIA", "MI DISPIACE. TELEFONI ALLA TUA FAMIGLIA STASERA?"),
        ("YUSUF", "SÌ! ALLORA SONO FELICE.")])),
    slide("🔤 LA LETTERA F", '    <div class="lettera" data-say="F">F<small>f</small></div>\n' + sillabe_tab("F") + "\n" +
          parole([(S("FE") + "LICE", "felice"), (S("FA") + "MIGLIA", "famiglia"), ("SO" + S("FI") + "A", "sofia")])),
    slide("💬 COME STAI?", table([["😊", "STO BENE!"], ["🙂", "ABBASTANZA BENE."], ["😐", "COSÌ COSÌ."], ["😞", "NON MOLTO BENE."], ["😩", "STO MALE."]], head=["", "RISPONDO"])),
    slide("🔢 I NUMERI DA 100 A 500", griglia_numeri([(100, "CENTO"), (150, "CENTOCINQUANTA"), (200, "DUECENTO"), (250, "DUECENTOCINQUANTA"),
                                                       (300, "TRECENTO"), (350, "TRECENTOCINQUANTA"), (400, "QUATTROCENTO"), (500, "CINQUECENTO")])),
    end("ORA SAI DIRE COME STAI!"),
]
U5 = pagina("😊 Le mie emozioni · Esercizi", "alfa-le-mie-emozioni", [
    {"part": "Ascolto e leggo"},
    es_ascolta("e1", 1, [("FELICE", ["FELICE", "FERMATA", "SOFIA"]), ("FAMIGLIA", ["FERMATA", "FAMIGLIA", "FELICE"]),
                         ("FERMATA", ["SOFIA", "FELICE", "FERMATA"]), ("SOFIA", ["SOFIA", "FAMIGLIA", "FERMATA"])]),
    es_scegli("e2", 2, "😊 Come sta?", [(E("😊"), None, "FELICE"), (E("😢"), None, "TRISTE"), (E("😠"), None, "ARRABBIATO"), (E("😴"), None, "STANCO")],
              opts=["FELICE", "TRISTE", "ARRABBIATO", "STANCO"], cons="GUARDA LA FACCIA. SCEGLI."),
    es_scegli("e3", 3, "🚏 Alla fermata", [("1. YUSUF È…", ["FELICE", "TRISTE"], "TRISTE"), ("2. LA SUA FAMIGLIA È…", ["VICINA", "LONTANA"], "LONTANA"),
                                           ("3. STASERA YUSUF…", ["TELEFONA ALLA FAMIGLIA", "VA AL LAVORO"], "TELEFONA ALLA FAMIGLIA")]),
    {"part": "Scrivo"},
    es_copia("e4", 4, ["FELICE", "FAMIGLIA", "FERMATA", "SOFIA"]),
    es_sillabe("e5", 5, ["FE-LI-CE", "FA-MI-GLIA", "FER-MA-TA", "SO-FI-A", "FA-RI-NA"]),
    es_lettera("e6", 6, [("FELICE", "_ ELICE", "F"), ("FOTO", "_ OTO", "F"), ("CAFFÈ", "CA _ _ È", "FF"), ("FIORE", "_ IORE", "F")]),
    es_scegli("e7", 7, "🔊 C'è la F?", [(say("FIORE"), None, "SÌ"), (say("MELA"), None, "NO"), (say("FUOCO"), None, "SÌ"), (say("LUNA"), None, "NO"), (say("TELEFONO"), None, "SÌ")],
              opts=["SÌ", "NO"], cons="TOCCA 🔊. SENTI LA <b>F</b>?"),
    {"part": "Come stai?"},
    es_dialogo("e8", 8, "SOFIA: CIAO! COME ___?<br>YUSUF: NON MOLTO ___. SONO ___.<br>SOFIA: MI ___.",
               ["stai", "bene", "triste", "dispiace"], "STAI · BENE · TRISTE · DISPIACE"),
    {"part": "I numeri"},
    es_numeri("e9", 9, [("DUECENTO", 200), ("CENTOCINQUANTA", 150), ("QUATTROCENTO", 400), ("TRECENTOVENTI", 320), ("CINQUECENTO", 500)]),
    es_conti("e10", 10, [(100, 100), (200, 50), (300, 200), (150, 150)]),
    libero("e11", 11, "Come stai oggi?", "SCRIVI: COME STAI OGGI? PERCHÉ?", ["OGGI STO… / SONO…"], rows=1),
    parla("e12", 12, "DI' COME STAI OGGI E PERCHÉ."),
])

SLIDE_ALFA = [
    ("alfa-vado-al-corso/index.html", "VADO AL CORSO", "ALFABETIZZAZIONE", U2_SLIDE, "alfa"),
    ("alfa-la-mia-giornata/index.html", "LA MIA GIORNATA", "ALFABETIZZAZIONE", U3_SLIDE, "alfa"),
    ("alfa-mi-descrivo/index.html", "MI DESCRIVO", "ALFABETIZZAZIONE", U4_SLIDE, "alfa"),
    ("alfa-le-mie-emozioni/index.html", "LE MIE EMOZIONI", "ALFABETIZZAZIONE", U5_SLIDE, "alfa"),
]
ES_ALFA = [("alfa-vado-al-corso", U2), ("alfa-la-mia-giornata", U3), ("alfa-mi-descrivo", U4), ("alfa-le-mie-emozioni", U5)]
GIOCHI_ALFA = {
 "alfa-vado-al-corso": ("alfa-percorso", "ALFABETIZZAZIONE", "🏫 GIOCHI: VADO AL CORSO", [
  ["SCUOLA", "🏫", "STUDIO QUI"], ["LIBRO", "📖", "LO LEGGO"], ["QUADERNO", "📓", "CI SCRIVO"], ["PENNA", "🖊️", "PER SCRIVERE"], ["MATITA", "✏️", "SI CANCELLA"],
  ["GOMMA", "🧽", "CANCELLA LA MATITA"], ["STUDENTI", "🧑‍🎓", "IMPARANO"], ["DUE", "2️⃣", "2"], ["DODICI", "🔢", "12"], ["VENTI", "🔢", "20"],
  ["UVA", "🍇", "COMINCIA CON U"], ["MANO", "✋", "M + A"], ["DADO", "🎲", "D + A"], ["MOTO", "🏍️", "M + O"], ["ZAINO", "🎒", "CI METTO I LIBRI"], ["LAVAGNA", "🟩", "L'INSEGNANTE SCRIVE QUI"]]),
 "alfa-la-mia-giornata": ("alfa-percorso", "ALFABETIZZAZIONE", "☀️ GIOCHI: LA MIA GIORNATA", [
  ["OGGI", "📍", "QUESTO GIORNO"], ["IERI", "⏪", "IL GIORNO PRIMA"], ["MATTINA", "🌅", "FACCIO COLAZIONE"], ["SERA", "🌙", "CENO"], ["POMERIGGIO", "🌇", "DOPO PRANZO"],
  ["LUNEDÌ", "1️⃣", "IL PRIMO GIORNO"], ["MARTEDÌ", "2️⃣", "DOPO LUNEDÌ"], ["VENERDÌ", "5️⃣", "PRIMA DI SABATO"], ["SABATO", "6️⃣", "DOPO VENERDÌ"], ["DOMENICA", "7️⃣", "RIPOSO"],
  ["ANNI", "🎂", "QUANTI … HAI?"], ["AUGURI", "🎉", "BUON COMPLEANNO!"], ["TRENTA", "🔢", "30"], ["CINQUANTA", "🔢", "50"], ["CASA", "🏠", "A + A"], ["APE", "🐝", "COMINCIA CON A"]]),
 "alfa-mi-descrivo": ("alfa-percorso", "ALFABETIZZAZIONE", "🧥 GIOCHI: MI DESCRIVO", [
  ["CAPELLI", "💇", "SULLA TESTA"], ["PANTALONI", "👖", "PER LE GAMBE"], ["GUANTI", "🧤", "PER LE MANI"], ["BORSA", "👜", "CI METTO LE COSE"], ["GIACCA", "🧥", "SOPRA IL MAGLIONE"],
  ["SCARPE", "👟", "AI PIEDI"], ["ROSSO", "🔴", "COLORE DEL POMODORO"], ["BLU", "🔵", "COLORE DEL MARE"], ["VERDE", "🟢", "COLORE DELL'ERBA"], ["GIALLO", "🟡", "COLORE DEL SOLE"],
  ["NERO", "⚫", "COLORE DELLA NOTTE"], ["ALTO", "🧍", "IL CONTRARIO DI BASSO"], ["EURO", "💶", "I SOLDI"], ["CENTO", "💯", "100"], ["LUNA", "🌙", "L + U"], ["SOLE", "☀️", "S + O"]]),
 "alfa-le-mie-emozioni": ("alfa-percorso", "ALFABETIZZAZIONE", "😊 GIOCHI: LE MIE EMOZIONI", [
  ["FELICE", "😊", "STO BENISSIMO"], ["TRISTE", "😢", "PIANGO"], ["STANCO", "😴", "VOGLIO DORMIRE"], ["PAURA", "😨", "HO …"], ["ARRABBIATO", "😠", "SONO MOLTO NERVOSO"],
  ["FAMIGLIA", "👨‍👩‍👧", "MAMMA, PAPÀ, FIGLI"], ["FERMATA", "🚏", "ASPETTO L'AUTOBUS"], ["FIORE", "🌸", "F + I"], ["FOTO", "📷", "F + O"], ["CAFFÈ", "☕", "AL BAR"],
  ["TELEFONO", "📱", "CHIAMO LA FAMIGLIA"], ["AMICO", "🧑‍🤝‍🧑", "UNA PERSONA CARA"], ["BENE", "👍", "STO …"], ["MALE", "👎", "STO …"], ["DUECENTO", "🔢", "200"], ["CINQUECENTO", "🔢", "500"]]),
}

if __name__ == "__main__":
    for path, unit, top, sl, liv in SLIDE_ALFA:
        build_slide(path, unit, top, sl, liv)
    for cartella, dati in ES_ALFA:
        build_es(cartella + "/esercizi.html", dati)
    build_giochi(GIOCHI_ALFA)
