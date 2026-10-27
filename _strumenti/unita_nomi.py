from genera import eq, has, all_
import re

def cl(testo):
    """Testo con [risposta] -> parts e chiavi per un cloze (risposte alternative separate da |)."""
    parts, k = [], []
    for i, pezzo in enumerate(re.split(r"\[([^\]]+)\]", testo)):
        if i % 2:
            parts.append({"w": "m"} if len(pezzo) > 6 else {}); k.append(eq(*pezzo.split("|")))
        elif pezzo:
            parts.append(pezzo)
    return parts, k

def scegli(coppie):
    """[(parola, risposta), ...] -> items e chiavi per un esercizio a scelta."""
    return [{"q": f"{i}. {p}"} for i, (p, _) in enumerate(coppie, 1)], [eq(r) for _, r in coppie]

def scrivi(coppie):
    """[(domanda, risposta|alternativa), ...] -> items e chiavi per un esercizio da scrivere."""
    return [{"q": f"{i}. {q}"} for i, (q, _) in enumerate(coppie, 1)], [eq(*r.split("|")) for _, r in coppie]

# --- Maschile o femminile? (Schede nomi maschili e femminili) ---
E1_I, E1_K = scegli([("🐑 PECORA", "F"), ("🫏 ASINO", "M"), ("🦃 TACCHINO", "M"), ("🐄 MUCCA", "F"),
    ("🐈 GATTO", "M"), ("🐎 CAVALLO", "M"), ("🐔 GALLINA", "F"), ("🐐 CAPRA", "F"), ("🦓 ZEBRA", "F"),
    ("🦁 LEONE", "M"), ("🐘 ELEFANTE", "M"), ("GAZZELLA", "F"), ("SCIACALLO", "M"), ("🦒 GIRAFFA", "F"),
    ("🦬 BISONTE", "M"), ("🦍 GORILLA", "M")])
E2_I, E2_K = scegli([("🐌 LUMACA", "F"), ("🐸 RANA", "F"), ("🐒 SCIMMIA", "F"), ("🦉 GUFO", "M"),
    ("🐊 COCCODRILLO", "M"), ("STRUZZO", "M"), ("🐢 TARTARUGA", "F"), ("🐖 MAIALE", "M"),
    ("🦏 RINOCERONTE", "M"), ("🐬 DELFINO", "M"), ("🦋 FARFALLA", "F"), ("🐝 APE", "F")])
E3_I, E3_K = scegli([("CANE", "M"), ("CHIAVE", "F"), ("FIORE", "M"), ("NOTTE", "F"), ("PANE", "M"),
    ("CARNE", "F"), ("MESE", "M"), ("STAZIONE", "F"), ("GIORNALE", "M"), ("MOGLIE", "F"), ("MARE", "M"),
    ("GENTE", "F"), ("PESCE", "M"), ("TELEVISIONE", "F"), ("RISTORANTE", "M"), ("NAVE", "F")])
E4_I, E4_K = scrivi([("🐈 GATTO →", "gatta"), ("🐎 CAVALLO →", "cavalla"), ("🐇 CONIGLIO →", "coniglia"),
    ("🐓 GALLO →", "gallina"), ("🐺 LUPO →", "lupa"), ("🐘 ELEFANTE →", "elefantessa"),
    ("🦁 LEONE →", "leonessa"), ("🐕 CANE →", "cagna")])
FEMM = ["REGINA", "DONNA", "SORELLA", "ATTRICE", "DOTTORESSA", "POETESSA", "VIGILESSA", "MOGLIE", "PITTRICE", "STREGA"]
E5_I, E5_K = scegli([("DOTTORE", "DOTTORESSA"), ("MARITO", "MOGLIE"), ("FRATELLO", "SORELLA"),
    ("POETA", "POETESSA"), ("STREGONE", "STREGA"), ("VIGILE", "VIGILESSA"), ("UOMO", "DONNA"),
    ("ATTORE", "ATTRICE"), ("RE", "REGINA"), ("PITTORE", "PITTRICE")])

# --- Il plurale (Esercizi integrativi pag. 13-16) ---
E6_I, E6_K = scrivi([("L'ABBONAMENTO", "gli abbonamenti"), ("L'ACQUA", "le acque"), ("L'AMICO", "gli amici"),
    ("L'AFFITTO", "gli affitti"), ("L'OCA", "le oche"), ("L'ALBERO", "gli alberi"), ("L'ALUNNO", "gli alunni"),
    ("L'ARANCIA", "le arance"), ("L'AULA", "le aule"), ("L'ARMADIO", "gli armadi"), ("L'OMBRELLO", "gli ombrelli"),
    ("L'OPERAIO", "gli operai"), ("L'OROLOGIO", "gli orologi"), ("L'APE (FEMMINILE)", "le api"),
    ("L'UFFICIO", "gli uffici"), ("L'USCITA", "le uscite"), ("L'ENTRATA", "le entrate"),
    ("L'ESAME (MASCHILE)", "gli esami")])
E7_P, E7_K = cl("<br>".join(f"{i}. [{a}] {n} → [{p}]" for i, (a, n, p) in enumerate([
    ("lo", "SBAGLIO", "gli sbagli"), ("la", "SPESA", "le spese"), ("la", "SCADENZA", "le scadenze"),
    ("lo", "SPICCHIO", "gli spicchi"), ("la", "SCALA", "le scale"), ("la", "SPIAGGIA", "le spiagge"),
    ("la", "SCARPA", "le scarpe"), ("lo", "SPOSO", "gli sposi"), ("lo", "SCHERZO", "gli scherzi"),
    ("la", "SCIARPA", "le sciarpe"), ("lo", "SCONTRINO", "gli scontrini"), ("lo", "STIPENDIO", "gli stipendi"),
    ("la", "STRADA", "le strade"), ("la", "SQUADRA", "le squadre")], 1)))

# --- Gli articoli (Esercizi integrativi pag. 10-11) ---
SING = ["TAVOLO", "PORTA", "PESCE", "CARTA", "DONNA", "CAFFÈ", "GIORNALE", "BANANA", "MOSCA", "LIBRO",
        "PENNA", "SEDIA", "SCUOLA", "FERMATA", "BIGLIETTO", "TRENO", "GOMMA", "CARNE", "PANE", "MAESTRO",
        "BAGNO", "PIEDE", "DITO", "BOCCA"]
SING_F = {"PORTA", "CARTA", "DONNA", "BANANA", "MOSCA", "PENNA", "SEDIA", "SCUOLA", "FERMATA", "GOMMA", "CARNE", "BOCCA"}
PLUR = ["CAPELLI", "GUANTI", "SCARPE", "PATATE", "GELATI", "CASE", "VIGILI", "BAMBINE", "MEDICI", "PIAZZE",
        "MEDICINE", "RAGAZZE", "MACCHINE", "NEGOZI", "SEMAFORI", "PISELLI", "CAROTE", "FRAGOLE", "QUADERNI",
        "BIGLIETTI", "MARITI", "FRATELLI", "SORELLE", "FIGLIE"]
PLUR_F = {"SCARPE", "PATATE", "CASE", "BAMBINE", "PIAZZE", "MEDICINE", "RAGAZZE", "MACCHINE", "CAROTE",
          "FRAGOLE", "SORELLE", "FIGLIE"}
VOC = [("UOMO", "L'", "UN"), ("SPAZZOLINO", "LO", "UNO"), ("STRACCIO", "LO", "UNO"), ("ZAINO", "LO", "UNO"),
       ("ACQUA", "L'", "UN'"), ("ZUCCHERO", "LO", "UNO"), ("ORSO", "L'", "UN"), ("ALBERO", "L'", "UN"),
       ("SCHELETRO", "LO", "UNO"), ("STUDIO", "LO", "UNO"), ("STRANIERO", "LO", "UNO"), ("OMBRA", "L'", "UN'"),
       ("SCONTRINO", "LO", "UNO"), ("OCA", "L'", "UN'"), ("APE", "L'", "UN'"), ("SCHERZO", "LO", "UNO"),
       ("SCONTO", "LO", "UNO"), ("ZERO", "LO", "UNO"), ("SBAGLIO", "LO", "UNO"), ("IMBUTO", "L'", "UN")]

E8_I, E8_K = scegli([(n, "LA" if n in SING_F else "IL") for n in SING])
E9_I, E9_K = scegli([(n, "LE" if n in PLUR_F else "I") for n in PLUR])
E10_I, E10_K = scegli([(n, d) for n, d, _ in VOC])
E11_I, E11_K = scegli([(n, "UNA" if n in SING_F else "UN") for n in SING])
E12_I, E12_K = scegli([(n, "DELLE" if n in PLUR_F else "DEI") for n in PLUR])
E13_I, E13_K = scegli([(n, u) for n, _, u in VOC])

E_ = "è|e'|e"
E14_P, E14_K = cl("<br>".join(f"{i}. [{a}] {n} [{v}] {agg}" for i, (a, n, v, agg) in enumerate([
    ("la", "PORTA", E_, "CHIUSA"), ("la", "FINESTRA", E_, "APERTA"), ("il", "QUADERNO", E_, "CHIUSO"),
    ("i", "BAMBINI", "sono", "GRANDI"), ("le", "SCARPE", "sono", "STRETTE"), ("la", "BAMBINA", E_, "BASSA"),
    ("i", "TAVOLI", "sono", "SPORCHI"), ("le", "BOTTIGLIE", "sono", "VUOTE"), ("la", "MACCHINA", E_, "NUOVA"),
    ("l'", "OMBRELLO", E_, "ROTTO"), ("i", "TRENI", "sono", "PARTITI"), ("lo", "ZAINO", E_, "GRANDE"),
    ("i", "GATTI", "sono", "PICCOLI"), ("il", "CANE", E_, "CATTIVO"), ("la", "PIZZA", E_, "CALDA"),
    ("gli", "STUDENTI", "sono", "BRAVI"), ("la", "SCUOLA", E_, "CHIUSA"), ("le", "PENNE", "sono", "ROSSE"),
    ("l'", "ACQUA", E_, "FREDDA")], 1)))

# --- Uno o tanti? (Esercizi integrativi pag. 16) ---
E15_I, E15_K = scegli([("… L'AUTOBUS?", "C'È"), ("… I RAGAZZI?", "CI SONO"), ("… LA BICICLETTA?", "C'È"),
    ("… I NEGOZI?", "CI SONO"), ("… LE BOTTIGLIE?", "CI SONO"), ("… LA PARTITA?", "C'È"), ("… I TRENI?", "CI SONO"),
    ("… LO SCIOPERO?", "C'È"), ("… GLI AMICI?", "CI SONO"), ("… LA FIGLIA?", "C'È")])
E16_I, E16_K = scegli([("… IL SUPERMERCATO?", "DOV'È"), ("… I QUADERNI?", "DOVE SONO"), ("… I SOLDI?", "DOVE SONO"),
    ("… LE CHIAVI?", "DOVE SONO"), ("… IL PASSAPORTO?", "DOV'È"), ("… LE SCARPE?", "DOVE SONO"),
    ("… LA SCIARPA?", "DOV'È"), ("… L'ENTRATA?", "DOV'È"), ("… IL COMUNE?", "DOV'È"), ("… LA QUESTURA?", "DOV'È")])
E17_I, E17_K = scegli([("… LE CARAMELLE", "MI PIACCIONO"), ("… IL GELATO", "MI PIACE"), ("… IL RISO", "MI PIACE"),
    ("… LA FRUTTA", "MI PIACE"), ("… I POMODORI", "MI PIACCIONO"), ("… I FILM", "MI PIACCIONO"),
    ("… LA MACCHINA", "MI PIACE"), ("… L'ESTATE", "MI PIACE"), ("… LE PATATE", "MI PIACCIONO")])
E18_I, E18_K = scegli([("… I PANTALONI?", "COSTANO"), ("… IL COMPUTER?", "COSTA"), ("… I CALZINI?", "COSTANO"),
    ("… IL GIORNALE?", "COSTA"), ("… LE SCARPE?", "COSTANO"), ("… IL BIGLIETTO?", "COSTA"),
    ("… GLI OCCHIALI?", "COSTANO"), ("… L'OMBRELLO?", "COSTA"), ("… LE BANANE?", "COSTANO"),
    ("… IL CAFFÈ?", "COSTA"), ("… I BISCOTTI?", "COSTANO")])

NOMI = {
 "title": "📦 Nomi e articoli · Esercizi",
 "store": "nomi-articoli",
 "upper": True,
 "sections": [
  {"part": "Maschile o femminile?"},
  {"id": "e1", "title": "1 · Gli animali: M o F?", "short": "1 · Animali M o F", "type": "choice", "opts": ["M", "F"],
   "cons": "M = MASCHILE (IL GATTO). F = FEMMINILE (LA CAPRA). Tocca la lettera giusta.", "items": E1_I, "k": E1_K},
  {"id": "e2", "title": "2 · Guarda i disegni: M o F?", "short": "2 · Disegni M o F", "type": "choice", "opts": ["M", "F"],
   "cons": "Attenzione: alcuni nomi finiscono in -E.", "items": E2_I, "k": E2_K},
  {"id": "e3", "title": "3 · Nomi in -E: M o F?", "short": "3 · Nomi in -E", "type": "choice", "opts": ["M", "F"],
   "cons": "I nomi in -E possono essere maschili o femminili. Pensa: IL … o LA …?", "items": E3_I, "k": E3_K},
  {"id": "e4", "title": "4 · Dal maschile al femminile", "short": "4 · Animali al femminile", "type": "text", "w": "m",
   "cons": "Scrivi il femminile. Esempio: IL GATTO → LA GATTA.", "items": E4_I, "k": E4_K},
  {"id": "e5", "title": "5 · Collega maschile e femminile", "short": "5 · Persone", "type": "select", "opts": FEMM,
   "cons": "Scegli il femminile giusto.", "items": E5_I, "k": E5_K},

  {"part": "Il plurale"},
  {"id": "e6", "title": "6 · L' → GLI o LE: fai il plurale", "short": "6 · Plurale con L'", "type": "text", "w": "m",
   "cons": "Scrivi l'articolo e il nome al plurale. Esempio: L'ABITO → GLI ABITI · L'ALBA → LE ALBE.",
   "items": E6_I, "k": E6_K},
  {"id": "e7", "title": "7 · LO o LA? Poi fai il plurale", "short": "7 · Lo/la → gli/le", "type": "cloze",
   "cons": "Scrivi LO o LA. Poi scrivi il plurale con GLI o LE. Esempio: LO SPORTELLO → GLI SPORTELLI.",
   "parts": E7_P, "k": E7_K},

  {"part": "Gli articoli"},
  {"id": "e8", "title": "8 · IL o LA?", "short": "8 · Il o la", "type": "choice", "opts": ["IL", "LA"],
   "items": E8_I, "k": E8_K},
  {"id": "e9", "title": "9 · I o LE?", "short": "9 · I o le", "type": "choice", "opts": ["I", "LE"],
   "items": E9_I, "k": E9_K},
  {"id": "e10", "title": "10 · L' o LO?", "short": "10 · L' o lo", "type": "choice", "opts": ["L'", "LO"],
   "cons": "L' davanti a vocale (A, E, I, O, U). LO davanti a S + consonante, Z.", "items": E10_I, "k": E10_K},
  {"id": "e11", "title": "11 · UN o UNA?", "short": "11 · Un o una", "type": "choice", "opts": ["UN", "UNA"],
   "items": E11_I, "k": E11_K},
  {"id": "e12", "title": "12 · DEI o DELLE?", "short": "12 · Dei o delle", "type": "choice", "opts": ["DEI", "DELLE"],
   "items": E12_I, "k": E12_K},
  {"id": "e13", "title": "13 · UN, UN' o UNO?", "short": "13 · Un, un', uno", "type": "choice", "opts": ["UN", "UN'", "UNO"],
   "cons": "UN' (con l'apostrofo) solo per i nomi femminili: UN'AMICA, UN AMICO.", "items": E13_I, "k": E13_K},
  {"id": "e14", "title": "14 · Completa: articolo e È / SONO", "short": "14 · Articolo e è/sono", "type": "cloze",
   "cons": "Scrivi l'articolo (IL, L', LA, LO, LE, I, GLI) e poi È (uno) o SONO (tanti).",
   "bank": "IL · L' · LA · LO · LE · I · GLI · È · SONO", "parts": E14_P, "k": E14_K},

  {"part": "Uno o tanti?"},
  {"id": "e15", "title": "15 · C'È o CI SONO?", "short": "15 · C'è o ci sono", "type": "choice", "opts": ["C'È", "CI SONO"],
   "items": E15_I, "k": E15_K},
  {"id": "e16", "title": "16 · DOV'È o DOVE SONO?", "short": "16 · Dov'è o dove sono", "type": "choice",
   "opts": ["DOV'È", "DOVE SONO"], "items": E16_I, "k": E16_K},
  {"id": "e17", "title": "17 · MI PIACE o MI PIACCIONO?", "short": "17 · Mi piace", "type": "choice",
   "opts": ["MI PIACE", "MI PIACCIONO"], "items": E17_I, "k": E17_K},
  {"id": "e18", "title": "18 · QUANTO COSTA o QUANTO COSTANO?", "short": "18 · Quanto costa", "type": "choice",
   "opts": ["COSTA", "COSTANO"], "cons": "QUANTO … ?", "items": E18_I, "k": E18_K},
 ]
}
