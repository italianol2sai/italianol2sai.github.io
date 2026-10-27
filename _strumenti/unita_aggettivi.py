from genera import eq, has, all_
from unita_nomi import cl, scegli, scrivi

def frase(soggetto, resto):
    """Accetta la frase con o senza pronome: frase("noi", "siamo stanchi")."""
    return eq(*[r for x in resto.split("|") for r in (x, soggetto + " " + x)])

def frasi(righe):
    """[(frase data, soggetto, risposta|alternativa), ...] -> items e chiavi."""
    return ([{"q": f"{i}. {q}", "w": "w"} for i, (q, _, _) in enumerate(righe, 1)],
            [frase(s, r) if s else eq(*r.split("|")) for _, s, r in righe])

# --- Che cos'è un aggettivo? (Schede di ripasso) ---
PAROLE = [("SCOMODO", 1), ("FORMICA", 0), ("AZZURRO", 1), ("TAVOLO", 0), ("LENTO", 1), ("BASSA", 1),
          ("PENNA", 0), ("SIMPATICO", 1), ("MAMMA", 0), ("ALTO", 1), ("BRAVA", 1), ("MACCHINA", 0),
          ("CORTO", 1), ("PRATO", 0), ("ENORME", 1), ("NUVOLA", 0), ("BRUTTO", 1), ("COMODO", 1)]
TIPI = ["ARTICOLO", "NOME", "VERBO", "AGGETTIVO"]
ANALISI = [("I NONNI GUARDANO LA TELEVISIONE SU UN DIVANO COMODO.",
            [("I", 0), ("NONNI", 1), ("GUARDANO", 2), ("LA", 0), ("TELEVISIONE", 1), ("UN", 0), ("DIVANO", 1), ("COMODO", 3)]),
           ("IO MANGIO UN MORBIDO PANINO.", [("MANGIO", 2), ("UN", 0), ("MORBIDO", 3), ("PANINO", 1)]),
           ("IL VENTO SPAZZA LE NUVOLE SCURE.",
            [("IL", 0), ("VENTO", 1), ("SPAZZA", 2), ("LE", 0), ("NUVOLE", 1), ("SCURE", 3)])]
E3_I = [{"q": f"<small>{f}</small><br><b>{p}</b>"} for f, ps in ANALISI for p, _ in ps]
E3_K = [eq(TIPI[t]) for _, ps in ANALISI for _, t in ps]
E4_P, E4_K = cl("SILVESTRO È UN BEL GATTO DAL LUNGO PELO (NERO) [nero], (LISCIO) [liscio] E (LUCIDO) [lucido].<br>"
    "HA UN MUSO (SIMPATICO) [simpatico], DUE OCCHI (SVEGLIO) [svegli] E (LUNGO) [lunghi] BAFFI.<br>"
    "HA UN CORPO (MAGRO) [magro] E (SNELLO) [snello] E QUATTRO ZAMPE (BIANCO) [bianche].<br>"
    "LA CODA, INVECE, È (FOLTO) [folta] E (NERO) [nera] E TERMINA CON UN CIUFFO (BIANCO) [bianco].<br>"
    "SILVESTRO È UN GATTO (VIVACE) [vivace] E UN PO' (DISPETTOSO) [dispettoso].")

# --- Concordanza (Esercizi aggettivi qualificativi) ---
def concorda(righe):
    t = "<br><br>".join(f"<b>{agg.upper()}</b>: " + " · ".join(f"{n} [{f}]" for n, f in coppie) for agg, coppie in righe)
    return cl(t)
E5_P, E5_K = concorda([
    ("facile", [("IL COMPITO", "facile"), ("IL PROBLEMA", "facile"), ("LE SALITE", "facili"), ("GLI ESERCIZI", "facili")]),
    ("noioso", [("IL LIBRO", "noioso"), ("LA PRESENTAZIONE", "noiosa"), ("LE LEZIONI", "noiose"), ("GLI ARGOMENTI", "noiosi")]),
    ("silenzioso", [("LA GENTE", "silenziosa"), ("IL LUOGO", "silenzioso"), ("L'AMBIENTE", "silenzioso"), ("I SIGNORI", "silenziosi")]),
    ("azzurro", [("IL CIELO", "azzurro"), ("GLI OCCHI", "azzurri"), ("LA CAMICIA", "azzurra"), ("LE GONNE", "azzurre")]),
    ("freddo", [("IL PAESE", "freddo"), ("IL CAFFÈ", "freddo"), ("LA MANO", "fredda"), ("LE CARNI", "fredde")])])
E6_P, E6_K = concorda([
    ("importante", [("L'UOMO", "importante"), ("LA DONNA", "importante"), ("LE NOTIZIE", "importanti"), ("LE DECISIONI", "importanti")]),
    ("dolce", [("IL MIELE", "dolce"), ("IL BACIO", "dolce"), ("LA VOCE", "dolce"), ("LE CAREZZE", "dolci")]),
    ("pesante", [("IL LAVORO", "pesante"), ("LE GAMBE", "pesanti"), ("LE BORSE", "pesanti"), ("LA SCATOLA", "pesante")]),
    ("pulito", [("IL VESTITO", "pulito"), ("LA STANZA", "pulita"), ("LE SCARPE", "pulite"), ("I PAVIMENTI", "puliti")]),
    ("brillante", [("L'IDEA", "brillante"), ("LA STELLA", "brillante"), ("LE SOLUZIONI", "brillanti"), ("I GIOIELLI", "brillanti")])])

# --- Frasi al plurale (Esercizi integrativi pag. 5, 12-14) ---
E7_I, E7_K = frasi([("LA PIZZA È CALDA", "", "le pizze sono calde"), ("IL PESCE È CRUDO", "", "i pesci sono crudi"),
    ("LA MAESTRA È GENTILE", "", "le maestre sono gentili"), ("IL POSTO È OCCUPATO", "", "i posti sono occupati"),
    ("LA MACCHINA È NUOVA", "", "le macchine sono nuove"), ("IL BAMBINO È BELLO", "", "i bambini sono belli"),
    ("IL CAFFÈ È DOLCE", "", "i caffè sono dolci"), ("L'ARANCIA È FRESCA", "", "le arance sono fresche"),
    ("LA CASA È PICCOLA", "", "le case sono piccole"), ("IL FIORE È GIALLO", "", "i fiori sono gialli"),
    ("LA BISTECCA È FREDDA", "", "le bistecche sono fredde"), ("IL NEGOZIO È CHIUSO", "", "i negozi sono chiusi"),
    ("IL TAVOLO È SPORCO", "", "i tavoli sono sporchi")])
E8_I, E8_K = frasi([("IL FILM È NOIOSO", "", "i film sono noiosi"), ("IL TAXI È GIALLO", "", "i taxi sono gialli"),
    ("L'ALBERO È GRANDE", "", "gli alberi sono grandi"), ("LA PIAZZA È DESERTA", "", "le piazze sono deserte"),
    ("IL MERCATO È AFFOLLATO", "", "i mercati sono affollati"), ("IL RISTORANTE È CARO", "", "i ristoranti sono cari"),
    ("LA CITTÀ È GRANDE", "", "le città sono grandi"), ("IL BAR È APERTO", "", "i bar sono aperti"),
    ("LA PIZZA È CARA", "", "le pizze sono care"), ("IL LIBRO È PESANTE", "", "i libri sono pesanti"),
    ("LA BORSA È LEGGERA", "", "le borse sono leggere"), ("IL CARRELLO È PIENO", "", "i carrelli sono pieni")])
E9_I, E9_K = frasi([("IO SONO STANCO", "noi", "siamo stanchi"), ("TU HAI POCHI SOLDI", "voi", "avete pochi soldi"),
    ("LUI È BUONO", "loro", "sono buoni"), ("TU SEI ALTO", "voi", "siete alti"),
    ("LUI HA LA MACCHINA", "loro", "hanno la macchina|hanno le macchine"), ("IO HO LA FEBBRE", "noi", "abbiamo la febbre"),
    ("TU SEI SPAGNOLO", "voi", "siete spagnoli"), ("LUI È TRISTE", "loro", "sono tristi"),
    ("TU SEI ALLEGRO", "voi", "siete allegri"), ("LUI HA I DOCUMENTI", "loro", "hanno i documenti"),
    ("IO HO LA BICICLETTA", "noi", "abbiamo la bicicletta|abbiamo le biciclette"), ("TU SEI SIMPATICO", "voi", "siete simpatici"),
    ("IO SONO OPERAIO", "noi", "siamo operai"), ("LUI È CUOCO", "loro", "sono cuochi"), ("TU HAI FREDDO", "voi", "avete freddo"),
    ("IO HO FAME", "noi", "abbiamo fame"), ("LUI È STRANIERO", "loro", "sono stranieri"),
    ("IO HO LA GIACCA", "noi", "abbiamo la giacca|abbiamo le giacche")])
E10_I, E10_K = frasi([("TU … ITALIANO", "tu", "non sei italiano"), ("NOI … A CASA", "noi", "non siamo a casa"),
    ("VOI … I SOLDI", "voi", "non avete i soldi"), ("LUI … L'OMBRELLO", "lui", "non ha l'ombrello"),
    ("VOI … LE SCARPE NUOVE", "voi", "non avete le scarpe nuove"), ("LORO … CINESI", "loro", "non sono cinesi"),
    ("IO … MALATO", "io", "non sono malato"), ("LEI … IN RITARDO", "lei", "non è in ritardo"),
    ("L'AUTOBUS … SPORCO", "l'autobus", "non è sporco"), ("I FIORI … BELLI", "i fiori", "non sono belli"),
    ("MIO FRATELLO … LA MOTO", "mio fratello", "non ha la moto"), ("VOI … FREDDO", "voi", "non avete freddo"),
    ("NOI … CALDO", "noi", "non abbiamo caldo"), ("VOI … AMICI", "voi", "non siete amici"),
    ("NOI … MOLTI AMICI", "noi", "non abbiamo molti amici"), ("LUI … TUO FRATELLO", "lui", "non è tuo fratello"),
    ("LEI … TUA SORELLA?", "lei", "non è tua sorella"), ("LE PENNE … ROSSE", "le penne", "non sono rosse"),
    ("IL PASSAPORTO … SCADUTO", "il passaporto", "non è scaduto")])

# --- I contrari (Loescher, Esercizi integrativi pag. 17) ---
E11_I = [{"q": f"{i}. {q}", "opts": o} for i, (q, o) in enumerate([
    ("☀️ OGGI È UNA … GIORNATA.", ["BELLA", "BUONA"]), ("👕 QUESTA CAMICIA È … (NON È STRETTA)", ["LUNGA", "LARGA"]),
    ("😄 MARCO È UN RAGAZZO …", ["ANTIPATICO", "ALLEGRO"]), ("💻💡 IL COMPUTER È … (NON È SPENTO)", ["ACCESO", "APERTO"]),
    ("👜✨ LA BORSA DI MARTA È … (NON È VECCHIA)", ["SPORCA", "NUOVA"]), ("👟 QUESTA SCARPA È … (NON È PICCOLA)", ["GRANDE", "PIENA"]),
    ("🥶 OGGI FA …", ["BRUTTO", "FREDDO"]), ("💐 TUO MARITO È MOLTO …", ["INTROVERSO", "GENTILE"]),
    ("🏛️🔒 IL LUNEDÌ IL MUSEO È …", ["CHIUSO", "FINITO"]), ("🧍‍♀️ FRANCESCA È … (NON È BASSA)", ["LUNGA", "ALTA"])], 1)]
E11_K = [eq(a) for a in ["BELLA", "LARGA", "ALLEGRO", "ACCESO", "NUOVA", "GRANDE", "FREDDO", "GENTILE", "CHIUSO", "ALTA"]]
CONTRARI = sorted(["BASSO", "ESTROVERSO", "VUOTO", "PULITO", "MALEDUCATO", "INIZIATO", "DIFFICILE", "PICCOLO", "SPENTO",
    "BRUTTO", "CORTO", "CATTIVO", "CHIUSO", "SFORTUNATO", "TRISTE", "VECCHIO", "SIMPATICO", "STRETTO", "CALDO"])
E12_I, E12_K = scegli([("FACILE", "DIFFICILE"), ("BELLO", "BRUTTO"), ("BUONO", "CATTIVO"), ("LUNGO", "CORTO"),
    ("LARGO", "STRETTO"), ("ANTIPATICO", "SIMPATICO"), ("ALLEGRO", "TRISTE"), ("ACCESO", "SPENTO"), ("APERTO", "CHIUSO"),
    ("SPORCO", "PULITO"), ("NUOVO", "VECCHIO"), ("GRANDE", "PICCOLO"), ("PIENO", "VUOTO"), ("FREDDO", "CALDO"),
    ("INTROVERSO", "ESTROVERSO"), ("GENTILE", "MALEDUCATO"), ("FINITO", "INIZIATO"), ("ALTO", "BASSO")])
E13_I, E13_K = scrivi([("AMARO ↔", "dolce"), ("GRASSO ↔", "magro"), ("LEGGERO ↔", "pesante"), ("VELOCE ↔", "lento"),
    ("DURO ↔", "morbido"), ("CRUDO ↔", "cotto"), ("LONTANO ↔", "vicino"), ("CALDO ↔", "freddo"), ("PIENO ↔", "vuoto"),
    ("BUONO ↔", "cattivo"), ("ALTO ↔", "basso"), ("NUOVO ↔", "vecchio|usato")])

# --- Le nazionalità (Paese e nazionalità) ---
E14_I, E14_K = scrivi([("🇮🇹 ITALIA", "italiano"), ("🇨🇳 CINA", "cinese"), ("🇫🇷 FRANCIA", "francese"),
    ("🇧🇷 BRASILE", "brasiliano"), ("🇪🇬 EGITTO", "egiziano"), ("🇹🇳 TUNISIA", "tunisino"), ("🇩🇿 ALGERIA", "algerino"),
    ("🇵🇰 PAKISTAN", "pakistano"), ("🇦🇫 AFGHANISTAN", "afghano|afgano"), ("🇧🇩 BANGLADESH", "bengalese|bangladese"),
    ("🇬🇷 GRECIA", "greco"), ("🇷🇺 RUSSIA", "russo"), ("🇹🇷 TURCHIA", "turco"), ("🇲🇽 MESSICO", "messicano"),
    ("🇵🇹 PORTOGALLO", "portoghese"), ("🇨🇱 CILE", "cileno"), ("🇮🇶 IRAQ", "iracheno"),
    ("🇺🇸 STATI UNITI", "statunitense|americano"), ("🇵🇱 POLONIA", "polacco"), ("🇻🇳 VIETNAM", "vietnamita")])
SUFF = ["-ANO", "-ESE", "-INO", "-ENO", "-O", "-ACCO", "-ITA"]
E15_I, E15_K = scegli([("ALBANIA → ALBAN…", "-ESE"), ("MAROCCO → MAROCCH…", "-INO"), ("NIGERIA → NIGERI…", "-ANO"),
    ("SENEGAL → SENEGAL…", "-ESE"), ("UCRAINA → UCRAIN…", "-O"), ("SIRIA → SIRI…", "-ANO"), ("CILE → CIL…", "-ENO"),
    ("GHANA → GHAN…", "-ESE"), ("SLOVACCHIA → SLOV…", "-ACCO"), ("VIETNAM → VIETNAM…", "-ITA"), ("ARGENTINA → ARGENT…", "-INO"),
    ("GIAPPONE → GIAPPON…", "-ESE")])
E16_P, E16_K = cl("1. AHMED È DEL MAROCCO. È [marocchino].<br>"
    "2. FATIMA È DEL MAROCCO. È [marocchina].<br>"
    "3. OMAR E ALI SONO DEL PAKISTAN. SONO [pakistani].<br>"
    "4. MEI È DELLA CINA. È [cinese].<br>"
    "5. LI E CHEN SONO DELLA CINA. SONO [cinesi].<br>"
    "6. AMINATA E FATOU SONO DEL SENEGAL. SONO [senegalesi].<br>"
    "7. OLENA È DELL'UCRAINA. È [ucraina].<br>"
    "8. JOHN È DELLA NIGERIA. È [nigeriano].<br>"
    "9. AMIRA E SARA SONO DELLA TUNISIA. SONO [tunisine].<br>"
    "10. KLEA E ARTA SONO DELL'ALBANIA. SONO [albanesi].<br>"
    "11. LUCIANA È DELL'ITALIA. È [italiana].<br>"
    "12. HASSAN E KARIM SONO DELL'EGITTO. SONO [egiziani].")

AGGETTIVI = {
 "title": "🎨 Gli aggettivi · Esercizi",
 "store": "aggettivi",
 "upper": True,
 "sections": [
  {"part": "Che cos'è un aggettivo?"},
  {"id": "e1", "title": "1 · Trova gli aggettivi", "short": "1 · Trova gli aggettivi", "type": "multi",
   "cons": "L'aggettivo dice COM'È una persona o una cosa. Tocca solo gli aggettivi.",
   "items": [p for p, _ in PAROLE], "k": [eq("X" if a else "-") for _, a in PAROLE]},
  {"id": "e2", "title": "2 · Articolo, nome, verbo o aggettivo?", "short": "2 · Che parola è", "type": "choice",
   "opts": TIPI, "full": True, "cons": "Leggi la frase. Che parola è?", "items": E3_I, "k": E3_K},
  {"id": "e3", "title": "3 · Com'è Silvestro?", "short": "3 · Silvestro", "type": "cloze",
   "cons": "🐈 Scrivi l'aggettivo nella forma giusta: maschile o femminile, singolare o plurale. Esempio: DUE OCCHI (GRANDE) → GRANDI.",
   "parts": E4_P, "k": E4_K},

  {"part": "Maschile, femminile, singolare, plurale"},
  {"id": "e4", "title": "4 · Scrivi l'aggettivo giusto (1)", "short": "4 · Concordanza 1", "type": "cloze",
   "cons": "Scrivi l'aggettivo accanto a ogni nome. Attenzione: maschile o femminile? Singolare o plurale?",
   "parts": E5_P, "k": E5_K},
  {"id": "e5", "title": "5 · Scrivi l'aggettivo giusto (2)", "short": "5 · Concordanza 2", "type": "cloze",
   "cons": "Gli aggettivi in -E hanno solo due forme: GRANDE, GRANDI.", "parts": E6_P, "k": E6_K},
  {"id": "e6", "title": "6 · Fai il plurale delle frasi (1)", "short": "6 · Frasi al plurale 1", "type": "text",
   "cons": "Esempio: IL GATTO È NERO → I GATTI SONO NERI.", "items": E7_I, "k": E7_K},
  {"id": "e7", "title": "7 · Fai il plurale delle frasi (2)", "short": "7 · Frasi al plurale 2", "type": "text",
   "cons": "Attenzione: alcuni nomi non cambiano al plurale (IL FILM → I FILM).", "items": E8_I, "k": E8_K},
  {"id": "e8", "title": "8 · Io → noi, tu → voi, lui → loro", "short": "8 · Persone al plurale", "type": "text",
   "cons": "Fai il plurale. Esempio: IO SONO CONTENTO → NOI SIAMO CONTENTI.", "items": E9_I, "k": E9_K},
  {"id": "e9", "title": "9 · ESSERE o AVERE? Fai la frase negativa", "short": "9 · Frase negativa", "type": "text",
   "cons": "Scrivi la frase con NON e il verbo ESSERE o AVERE. Esempio: ANNA … DUE BAMBINI → ANNA NON HA DUE BAMBINI.",
   "items": E10_I, "k": E10_K},

  {"part": "I contrari"},
  {"id": "e10", "title": "10 · Scegli l'aggettivo giusto", "short": "10 · Scegli l'aggettivo", "type": "choice",
   "full": True, "cons": "Guarda il disegno e scegli.", "items": E11_I, "k": E11_K},
  {"id": "e11", "title": "11 · Trova il contrario", "short": "11 · I contrari (scegli)", "type": "select", "opts": CONTRARI,
   "cons": "Attenzione: c'è un aggettivo in più!", "items": E12_I, "k": E12_K},
  {"id": "e12", "title": "12 · Scrivi il contrario", "short": "12 · I contrari (scrivi)", "type": "text", "w": "m",
   "items": E13_I, "k": E13_K},

  {"part": "Le nazionalità"},
  {"id": "e13", "title": "13 · Paese e nazionalità", "short": "13 · Paese e nazionalità", "type": "text", "w": "m",
   "cons": "Scrivi la nazionalità al maschile. Esempio: SPAGNA → SPAGNOLO.", "items": E14_I, "k": E14_K},
  {"id": "e14", "title": "14 · Che finale?", "short": "14 · Il finale", "type": "select", "opts": SUFF,
   "cons": "Scegli il finale giusto della nazionalità (al maschile).", "items": E15_I, "k": E15_K},
  {"id": "e15", "title": "15 · Di dove sono?", "short": "15 · Di dove sono", "type": "cloze",
   "cons": "Scrivi la nazionalità nella forma giusta: maschile o femminile, singolare o plurale.",
   "parts": E16_P, "k": E16_K},
  {"id": "e16", "title": "16 ✎ · E tu? Di dove sei? Com'è la tua città?", "type": "free", "rows": 5,
   "items": ["Scrivi 3 o 4 frasi. Esempio: SONO MAROCCHINO. LA MIA CITTÀ È GRANDE E BELLA. BARI È UNA CITTÀ SIMPATICA."]},
 ]
}
