from genera import eq, has, all_

P6 = ["IO", "TU", "LUI/LEI", "NOI", "VOI", "LORO"]

def persone(pairs):
    """[(verbo, persona), ...] -> items e chiavi per un esercizio a scelta IO/TU/..."""
    return [{"q": f"{i}. {v}"} for i, (v, _) in enumerate(pairs, 1)], [eq(p) for _, p in pairs]

def frase(soggetti, resto):
    """Accetta la frase con o senza pronome: frase(["lui", "lei"], "ha due gatti")."""
    return eq(resto, *[s + " " + resto for s in soggetti])

def coniuga(verbi, pers):
    """Cloze: una riga per verbo, un campo per persona."""
    parts, k = [], []
    for v, forme in verbi:
        parts.append(f"<b>{v}</b><br>")
        for p, f in zip(pers, forme):
            parts += [f"{p} ", {}, " "]
            k.append(eq(*f.split("|")))
        parts.append("<br>")
    return parts, k

def verbo(items):
    """[(prima, dopo, risposta), ...] -> esercizio con campo in mezzo alla frase."""
    return ([{"pre": f"{i}. {a}", "post": b} for i, (a, b, _) in enumerate(items, 1)],
            [eq(*r.split("|")) for _, _, r in items])

# --- Verbi regolari (Coniugaverbi pag. 2-3) ---
E2_I, E2_K = persone([("SENTO", "IO"), ("GUARDO", "IO"), ("ABITIAMO", "NOI"), ("VIVE", "LUI/LEI"),
    ("ASCOLTANO", "LORO"), ("COMPRA", "LUI/LEI"), ("SENTE", "LUI/LEI"), ("LEGGE", "LUI/LEI"),
    ("SCRIVIAMO", "NOI"), ("PARLATE", "VOI"), ("GIOCANO", "LORO"), ("DORMONO", "LORO"), ("VEDO", "IO"),
    ("LAVORATE", "VOI"), ("MANGI", "TU"), ("ENTRA", "LUI/LEI"), ("CAPIAMO", "NOI"), ("CAMMINA", "LUI/LEI"),
    ("FINITE", "VOI"), ("APRO", "IO"), ("CHIUDI", "TU")])

GRUPPI = [("MANGIARE", "-ARE"), ("SENTIRE", "-IRE"), ("CAMMINARE", "-ARE"), ("CORRERE", "-ERE"),
          ("LEGGERE", "-ERE"), ("STUDIARE", "-ARE"), ("DORMIRE", "-IRE"), ("SCRIVERE", "-ERE"),
          ("PAGARE", "-ARE"), ("TELEFONARE", "-ARE"), ("PRENDERE", "-ERE"), ("METTERE", "-ERE"),
          ("PULIRE", "-IRE"), ("APRIRE", "-IRE"), ("CHIUDERE", "-ERE"), ("PARTIRE", "-IRE")]

E4_P, E4_K = coniuga([("MANGIARE", ["mangio", "mangi", "mangia"]), ("SENTIRE", ["sento", "senti", "sente"]),
    ("CORRERE", ["corro", "corri", "corre"]), ("STUDIARE", ["studio", "studi", "studia"]),
    ("DORMIRE", ["dormo", "dormi", "dorme"]), ("PAGARE", ["pago", "paghi", "paga"]),
    ("PRENDERE", ["prendo", "prendi", "prende"]), ("CHIAMARE", ["chiamo", "chiami", "chiama"])],
    ["IO", "TU", "LUI/LEI"])
E5_P, E5_K = coniuga([("CAMMINARE", ["camminiamo", "camminate", "camminano"]),
    ("LEGGERE", ["leggiamo", "leggete", "leggono"]), ("APRIRE", ["apriamo", "aprite", "aprono"]),
    ("SCRIVERE", ["scriviamo", "scrivete", "scrivono"]), ("TELEFONARE", ["telefoniamo", "telefonate", "telefonano"]),
    ("METTERE", ["mettiamo", "mettete", "mettono"]), ("ENTRARE", ["entriamo", "entrate", "entrano"]),
    ("CHIUDERE", ["chiudiamo", "chiudete", "chiudono"])], ["NOI", "VOI", "LORO"])

E6_I, E6_K = verbo([("TU (MANGIARE)", "LA PASTA A PRANZO", "mangi"), ("LEI (COMPRARE)", "IL GIORNALE", "compra"),
    ("NOI (LEGGERE)", "IL LIBRO", "leggiamo"), ("IO (APRIRE)", "LA PORTA", "apro"),
    ("VOI (CHIUDERE)", "IL PORTONE", "chiudete"), ("VOI (DORMIRE)", "FINO A TARDI LA DOMENICA", "dormite"),
    ("LEI (PARTIRE)", "DOMANI MATTINA", "parte"), ("NOI (ARRIVARE)", "IN AEREO", "arriviamo"),
    ("VOI (STUDIARE)", "L'ITALIANO DUE VOLTE ALLA SETTIMANA", "studiate"),
    ("IO (PULIRE)", "LA CASA TUTTI I GIORNI", "pulisco"), ("VOI (FINIRE)", "I COMPITI…", "finite"),
    ("… E POI (GUARDARE)", "LA TELEVISIONE", "guardate")])

def cl(testo):
    """Testo con [risposta] -> parts e chiavi per un cloze."""
    import re
    parts, k = [], []
    for i, pezzo in enumerate(re.split(r"\[([^\]]+)\]", testo)):
        if i % 2:
            parts.append({}); k.append(eq(*pezzo.split("|")))
        elif pezzo:
            parts.append(pezzo)
    return parts, k

E7_P, E7_K = cl("1. LO STUDENTE (IMPARARE) [impara] L'ITALIANO, (STUDIARE) [studia] MOLTO, (PARLARE) [parla] POCO.<br><br>"
    "2. LUI (PORTARE) [porta] UN VESTITO NUOVO, (COMPRARE) [compra] UN PAIO DI SCARPE, (GUARDARE) [guarda] LE VETRINE.<br><br>"
    "3. GLI STUDENTI (ASCOLTARE) [ascoltano] L'INSEGNANTE E (PARLARE) [parlano] IN CLASSE.<br><br>"
    "4. NOI (ARRIVARE) [arriviamo] SPESSO IN RITARDO. DOMANI (PARTIRE) [partiamo] PER TOKYO.<br><br>"
    "5. GIOVANNI (LEGGERE) [legge] IL GIORNALE, (SCRIVERE) [scrive] UNA LETTERA, (APRIRE) [apre] LA PORTA.<br><br>"
    "6. LAURA NON (MANGIARE) [mangia] LA CARNE, (CUCINARE) [cucina] LA VERDURA, (FINIRE) [finisce] LA FRUTTA.<br><br>"
    "7. GIOVANNA E LAURA (CHIEDERE) [chiedono] UN'INFORMAZIONE, (CONOSCERE) [conoscono] BENE FIRENZE, (VIVERE) [vivono] A PADOVA.<br><br>"
    "8. IO (SALUTARE) [saluto] GIOVANNI, (VEDERE) [vedo] GIOVANNI, (CHIAMARE) [chiamo] GIOVANNI.<br><br>"
    "9. LAURA E IO (ASCOLTARE) [ascoltiamo] UN CONCERTO E (SUONARE) [suoniamo] IL VIOLINO.<br><br>"
    "10. TU (GUARDARE) [guardi] LA TELEVISIONE, (ACCENDERE) [accendi] LA LUCE, (SPEGNERE) [spegni] LA SIGARETTA.")

# --- Verbi in -ISC (Coniugaverbi pag. 4-6) ---
E9_I, E9_K = persone([("CAPITE", "VOI"), ("FINISCE", "LUI/LEI"), ("FINISCONO", "LORO"), ("FINISCO", "IO"),
    ("CAPISCONO", "LORO"), ("PULITE", "VOI"), ("FINIAMO", "NOI"), ("PULISCE", "LUI/LEI"), ("FINISCI", "TU"),
    ("PULISCONO", "LORO"), ("PREFERISCE", "LUI/LEI"), ("PULISCO", "IO"), ("PULISCI", "TU"), ("CAPIAMO", "NOI"),
    ("PULIAMO", "NOI"), ("CAPISCI", "TU"), ("CAPISCE", "LUI/LEI"), ("FINITE", "VOI")])

def righe(rows):
    """[(persona, [verbi], risposta), ...] -> esercizio a scelta con opzioni diverse per riga."""
    return ([{"q": f"{i}. <b>{p}</b>", "opts": vs} for i, (p, vs, _) in enumerate(rows, 1)],
            [eq(r) for _, _, r in rows])

E10_I, E10_K = righe([("TU", ["ARRIVI", "CAPISCE", "PARTI"], "CAPISCE"),
    ("LUI", ["CREDE", "FINISCE", "CORRI"], "CORRI"), ("VOI", ["SOGNATE", "RIDIAMO", "CUCINATE"], "RIDIAMO"),
    ("LEI", ["PIANGE", "GUARDA", "PULISCO"], "PULISCO"), ("TU", ["COMPRO", "VIVI", "CAPISCI"], "COMPRO")])
E11_I, E11_K = righe([("NOI", ["OFFRITE", "TROVIAMO", "PENSATE"], "TROVIAMO"),
    ("LORO", ["RIPOSANO", "PREFERISCO", "VINCO"], "RIPOSANO"),
    ("IO", ["DIMENTICHIAMO", "PULISCO", "ACCENDI"], "PULISCO"),
    ("NOI", ["LAVORATE", "ASCOLTIAMO", "SENTITE"], "ASCOLTIAMO")])


def img(nome):
    return f'<img src="img/{nome}.jpg" alt="" style="display:block;width:100%;max-width:320px;border-radius:12px;margin:4px 0 6px">'

FOTO_A = ["mangiare", "chiudere", "bere", "camminare", "cercare", "comprare", "pagare", "dormire",
          "entrare", "leggere", "partire", "pulire", "scrivere", "studiare", "uscire", "correre"]
FOTO_B = ["aprire", "dare", "vedere", "prendere", "perdere", "salire", "scendere", "mettere",
          "togliere", "buttare", "cucinare", "cuocere", "aiutare", "giocare"]
FOTO_B_OK = {"vedere": ["vedere", "guardare"], "cuocere": ["cuocere", "cucinare"], "dare": ["dare", "pagare"]}
FRASI_FOTO = [("mangiare", "LEI (MANGIARE)", "L'INSALATA", "mangia"), ("chiudere", "IO (CHIUDERE)", "LA PORTA", "chiudo"),
    ("bere", "LEI (BERE)", "UN BICCHIERE D'ACQUA", "beve"), ("dormire", "LEI (DORMIRE)", "NEL LETTO", "dorme"),
    ("leggere", "NOI (LEGGERE)", "UN LIBRO", "leggiamo"), ("scrivere", "TU (SCRIVERE)", "UNA LETTERA", "scrivi"),
    ("studiare", "GLI STUDENTI (STUDIARE)", "IN CLASSE", "studiano"), ("perdere", "IO (PERDERE)", "LE CHIAVI", "perdo"),
    ("salire", "VOI (SALIRE)", "LE SCALE", "salite"), ("giocare", "I BAMBINI (GIOCARE)", "NEL PARCO", "giocano"),
    ("pulire", "LEI (PULIRE)", "LA CASA", "pulisce"), ("cucinare", "TU (CUCINARE)", "LA PASTA", "cucini")]

FARE_TESTO = cl("OGNI MATTINA, PRIMA DI ANDARE A LAVORO, [faccio ginnastica] NELLA PALESTRA SOTTO CASA. "
    "A VOLTE [faccio la doccia] LÌ E MI VESTO NELLO SPOGLIATOIO, COSÌ SONO GIÀ PRONTO PER ANDARE IN UFFICIO. "
    "QUANDO SONO IN RITARDO [faccio colazione] AL BAR SOLO CON UN CAFFÈ. "
    "SE C'È IL SOLE [faccio due passi] PER ANDARE A LAVORO: MENTRE CAMMINO [faccio una telefonata] A MIA MADRE "
    "PER PARLARE UN PO' E INSIEME [facciamo quattro chiacchiere].")

# --- Essere e avere ---
HO_SONO = [("🚗 LA MACCHINA", "IO HO"), ("👨‍🌾 AGRICOLTORE", "IO SONO"), ("🔑 LA CHIAVE", "IO HO"),
    ("🐕 UN CANE", "IO HO"), ("🎤 CANTANTE", "IO SONO"), ("🎸 LA CHITARRA", "IO HO"),
    ("💼 IMPIEGATO", "IO SONO"), ("🐈 UN GATTO", "IO HO"), ("💇‍♀️ PARRUCCHIERA", "IO SONO"),
    ("👓 GLI OCCHIALI", "IO HO"), ("🎒 STUDENTESSA", "IO SONO"), ("🧊 IL FRIGORIFERO", "IO HO"),
    ("⚽ GIOCATORE", "IO SONO"), ("📕 UN LIBRO", "IO HO"), ("🔧 MECCANICO", "IO SONO"), ("🩺 MEDICO", "IO SONO")]

E13_I, E13_K = verbo([("IO (AVERE)", "30 ANNI", "ho"), ("LEI (ESSERE)", "A CASA", "è"),
    ("NOI (ESSERE)", "STUDENTI", "siamo"), ("LORO (AVERE)", "DUE GATTI", "hanno"),
    ("TU (ESSERE)", "SIMPATICO", "sei"), ("VOI (AVERE)", "FAME?", "avete"), ("IO (ESSERE)", "MAROCCHINO", "sono"),
    ("LUI (AVERE)", "UNA MACCHINA ROSSA", "ha"), ("VOI (ESSERE)", "STANCHI?", "siete"),
    ("NOI (AVERE)", "UNA CASA A BARI", "abbiamo"), ("TU (AVERE)", "FIGLI?", "hai"), ("LORO (ESSERE)", "FELICI", "sono")])

# --- Verbi irregolari (Coniugaverbi pag. 7-10) ---
E14_I, E14_K = persone([("VADO", "IO"), ("DOBBIAMO", "NOI"), ("VENGONO", "LORO"), ("BEVO", "IO"), ("ESCI", "TU"),
    ("RIMANIAMO", "NOI"), ("VOGLIAMO", "NOI"), ("HANNO", "LORO"), ("DAI", "TU"), ("AVETE", "VOI"),
    ("STA", "LUI/LEI"), ("SALI", "TU"), ("FA", "LUI/LEI"), ("POTETE", "VOI"), ("SO", "IO"), ("DICE", "LUI/LEI"),
    ("SIETE", "VOI"), ("VENIAMO", "NOI"), ("HO", "IO"), ("SAPPIAMO", "NOI"), ("VOLETE", "VOI"), ("DEVONO", "LORO")])
E15_I, E15_K = persone([("SAI", "TU"), ("PREFERISCO", "IO"), ("LASCI", "TU"), ("ESCONO", "LORO"),
    ("PERDE", "LUI/LEI"), ("OFFRO", "IO"), ("CAPITE", "VOI"), ("VINCIAMO", "NOI"), ("SANNO", "LORO"),
    ("ENTRA", "LUI/LEI"), ("RIMANETE", "VOI"), ("ARRIVANO", "LORO"), ("PULISCO", "IO"), ("FATE", "VOI"),
    ("VIVE", "LUI/LEI"), ("PRENDI", "TU"), ("DEVO", "IO"), ("VENGO", "IO"), ("ANDIAMO", "NOI"),
    ("ABITI", "TU"), ("STUDIAMO", "NOI")])
E16_I, E16_K = righe([("TU", ["VIENI", "LASCIA", "PARTI"], "LASCIA"),
    ("LUI", ["PREFERISCE", "CAPISCI", "ESCE"], "CAPISCI"), ("LORO", ["PREFERISCONO", "VINCE", "BEVONO"], "VINCE"),
    ("IO", ["ARRIVO", "USCIAMO", "PRENDO"], "USCIAMO"), ("LEI", ["DIMENTICA", "FA", "PARTITE"], "PARTITE"),
    ("TU", ["SCRIVO", "ESCI", "LEGGI"], "SCRIVO"), ("NOI", ["CAMMINATE", "SALIAMO", "PIANGIAMO"], "CAMMINATE")])
E17_I, E17_K = righe([("NOI", ["ARRIVANO", "USCIAMO", "FATE"], "USCIAMO"),
    ("VOI", ["POSSO", "VOLETE", "DOBBIAMO"], "VOLETE"), ("LORO", ["VA", "VAI", "VANNO"], "VANNO"),
    ("IO", ["FACCIO", "FA", "FATE"], "FACCIO"), ("LEI", ["SEI", "È", "SONO"], "È"),
    ("VOI", ["AVETE", "HANNO", "ABBIAMO"], "AVETE")])
E18_I, E18_K = verbo([("IO (ANDARE)", "A ROMA", "vado"), ("NOI (RIMANERE)", "A CASA", "rimaniamo"),
    ("NOI (STARE)", "BENE!", "stiamo"), ("IO (BERE)", "IL TÈ A COLAZIONE", "bevo"),
    ("TU (DIRE)", "TANTE BUGIE", "dici"), ("LUI (FARE)", "IL DOTTORE IN UN OSPEDALE MOLTO GRANDE", "fa"),
    ("NOI (SPEGNERE)", "LA LUCE", "spegniamo"), ("LEI (USCIRE)", "TUTTE LE SERE", "esce"),
    ("LORO (VENIRE)", "DA ROMA", "vengono")])

# --- Andare, venire, fare, dare (FAD verbi irregolari e Presente alfa) ---
E19_I, E19_K = righe([("IO … A SCUOLA", ["VADO", "ANDIAMO"], "VADO"),
    ("LUIGI … COLAZIONE CON IL PAPÀ", ["FATE", "FA"], "FA"), ("NOI … AL PARCO", ["VANNO", "ANDIAMO"], "ANDIAMO"),
    ("ELISA E ANDREA … UNA PARTITA A CARTE", ["FANNO", "FACCIAMO"], "FANNO"),
    ("TU … I COMPITI", ["FATE", "FAI"], "FAI"), ("ANNA … A CASA", ["VANNO", "VA"], "VA"),
    ("I RAGAZZI … MERENDA", ["FANNO", "FATE"], "FANNO")])
E20_I, E20_K = verbo([("TU", "UN DISEGNO", "fai"), ("NOI", "AL MARE", "andiamo"), ("GLI ALUNNI", "IN AUTOBUS", "vanno"),
    ("GLI STUDENTI", "IL PROBLEMA DI MATEMATICA", "fanno"), ("DOMANI VOI", "UNA FESTA", "fate"),
    ("IN ESTATE MARTA E GINO", "IN MONTAGNA", "vanno"), ("IO", "I COMPITI", "faccio")])
E21_I, E21_K = verbo([("NOI (ANDARE)", "A GIOCARE A CALCIO", "andiamo"), ("LEI (ANDARE)", "A FARE LA SPESA", "va"),
    ("VOI (ANDARE)", "ALLA STAZIONE", "andate"), ("TU (ANDARE)", "A LAVORARE IN PIZZERIA", "vai"),
    ("IO (VENIRE)", "DALLA CINA", "vengo"), ("LORO (VENIRE)", "DA ROMA", "vengono"),
    ("VOI (VENIRE)", "CON L'AUTOBUS", "venite"), ("TU (VENIRE)", "A PIEDI?", "vieni"),
    ("LUI (VENIRE)", "DALL'AFRICA", "viene"), ("NOI (VENIRE)", "A SCUOLA PER IMPARARE L'ITALIANO", "veniamo")])
PREP = ["AL", "ALLO", "ALL'", "ALLA", "AI", "AGLI", "ALLE"]
E22 = [("1. VADO … BAR (IL BAR)", "AL"), ("2. VADO … FERMATA DELL'AUTOBUS (LA FERMATA)", "ALLA"),
       ("3. VADO … ESTERO (L'ESTERO)", "ALL'"), ("4. VADO … SPETTACOLO (LO SPETTACOLO)", "ALLO"),
       ("5. VADO … CINEMA (IL CINEMA)", "AL"), ("6. VADO … STAZIONE (LA STAZIONE)", "ALLA"),
       ("7. DO I COMPITI … STUDENTI (GLI STUDENTI)", "AGLI"), ("8. LA NONNA DÀ I SOLDI … NIPOTI (I NIPOTI)", "AI"),
       ("9. DO UN REGALO … AMICHE (LE AMICHE)", "ALLE"), ("10. VADO … OSPEDALE (L'OSPEDALE)", "ALL'")]
E23_I, E23_K = verbo([("IO (FARE)", "COLAZIONE", "faccio"), ("TU (FARE)", "LA DOCCIA", "fai"),
    ("LUI (FARE)", "IL CAMERIERE", "fa"), ("NOI (FARE)", "I COMPITI", "facciamo"), ("VOI (FARE)", "UN VESTITO", "fate"),
    ("LORO (FARE)", "IL LETTO", "fanno"), ("IO (DARE)", "UN BACIO AL NIPOTINO", "do"),
    ("LA NONNA (DARE)", "DEI SOLDI AI NIPOTI", "dà"), ("NOI (DARE)", "IL NUMERO DI CELLULARE ALLA SEGRETERIA", "diamo"),
    ("GLI INSEGNANTI (DARE)", "I COMPITI AGLI STUDENTI", "danno"), ("TU (DARE)", "UNA MANO A MARCO", "dai"),
    ("COSA (DARE)", "VOI DA MANGIARE ALLE VOSTRE FIGLIE?", "date")])
MESTIERI = ["L'INSEGNANTE", "IL CAMERIERE", "LA COMMESSA", "L'ELETTRICISTA", "L'ARCHITETTO",
            "IL MURATORE", "L'INFERMIERA", "L'AGRICOLTORE"]
E25 = [("1. INSEGNA L'ITALIANO A SCUOLA.", "L'INSEGNANTE"), ("2. PORTA IL CAFFÈ AI CLIENTI DEL BAR.", "IL CAMERIERE"),
       ("3. VENDE I VESTITI IN UN NEGOZIO.", "LA COMMESSA"), ("4. RIPARA LA LUCE IN CASA.", "L'ELETTRICISTA"),
       ("5. DISEGNA LE CASE.", "L'ARCHITETTO"), ("6. COSTRUISCE UN MURO.", "IL MURATORE"),
       ("7. AIUTA IL DOTTORE E CURA I PAZIENTI.", "L'INFERMIERA"), ("8. LAVORA LA TERRA.", "L'AGRICOLTORE")]
E26_I, E26_K = verbo([("IO (STARE)", "FACENDO I COMPITI", "sto"), ("TU (STARE)", "BEVENDO LA COCA-COLA", "stai"),
    ("LUI (STARE)", "DICENDO UNA POESIA", "sta"), ("NOI (STARE)", "IMPARANDO L'ITALIANO", "stiamo"),
    ("VOI (STARE)", "ANDANDO A CASA", "state"), ("LORO (STARE)", "STUDIANDO A SCUOLA", "stanno")])

MATTEO = ("ALLE 7 MATTEO SI ALZA E FA LA DOCCIA. ALLE 7.30 FA COLAZIONE E FA IL LETTO, POI ALLE 8 VA AL LAVORO "
          "CON L'AUTOBUS. MATTEO LAVORA TUTTA LA MATTINA, POI ALL'UNA PRANZA AL BAR CON I SUOI COLLEGHI. "
          "DOPO PRANZO TORNA IN UFFICIO FINO ALLE 17.30 E POI VA A CASA. ALLE 20.00 CENA E PIÙ TARDI LAVA I PIATTI. "
          "PRIMA DI ANDARE A LETTO CHATTA CON GLI AMICI, POI ALLE 23.00 VA A DORMIRE.")
VERBI_MATTEO = eq("si alza", "alza", "fa", "va", "lavora", "pranza", "torna", "cena", "lava", "chatta",
                  "andare", "dormire")

PRESENTE = {
 "title": "⏱️ Il presente · Esercizi",
 "store": "presente",
 "upper": True,
 "sections": [
  {"part": "I verbi regolari: -ARE, -ERE, -IRE"},
  {"id": "e1", "title": "1 · Le desinenze", "short": "1 · Le desinenze", "type": "select",
   "cons": "Collega ogni persona alla desinenza giusta. Esempio: IO → -O (IO LAVORO, IO PRENDO, IO SENTO).",
   "opts": ["-O", "-I", "-A", "-E", "-IAMO", "-ATE", "-ETE", "-ITE", "-ANO", "-ONO"],
   "items": [{"q": q} for q in ["IO", "TU", "LUI", "LEI", "NOI", "VOI", "LORO"]],
   "k": [eq("-O"), eq("-I"), eq("-A", "-E"), eq("-A", "-E"), eq("-IAMO"), eq("-ATE", "-ETE", "-ITE"), eq("-ANO", "-ONO")]},
  {"id": "e2", "title": "2 · Chi è? Scegli la persona", "short": "2 · Chi è?", "type": "choice", "opts": P6,
   "cons": "Per ogni verbo scegli la persona giusta. Esempio: SENTI → TU.", "items": E2_I, "k": E2_K},
  {"id": "e3", "title": "3 · -ARE, -ERE o -IRE?", "short": "3 · I tre gruppi", "type": "choice",
   "opts": ["-ARE", "-ERE", "-IRE"], "cons": "Guarda la fine del verbo e scegli il gruppo.",
   "items": [{"q": f"{i}. {v}"} for i, (v, _) in enumerate(GRUPPI, 1)], "k": [eq(g) for _, g in GRUPPI]},
  {"id": "e4", "title": "4 · Coniuga: IO, TU, LUI/LEI", "short": "4 · Coniuga (singolare)", "type": "cloze",
   "cons": "Scrivi il verbo per ogni persona. Esempio: GUARDARE → IO GUARDO, TU GUARDI, LUI GUARDA.",
   "parts": E4_P, "k": E4_K},
  {"id": "e5", "title": "5 · Coniuga: NOI, VOI, LORO", "short": "5 · Coniuga (plurale)", "type": "cloze",
   "cons": "Scrivi il verbo per ogni persona. Esempio: GUARDARE → NOI GUARDIAMO, VOI GUARDATE, LORO GUARDANO.",
   "parts": E5_P, "k": E5_K},
  {"id": "e6", "title": "6 · Metti il verbo giusto", "short": "6 · Metti il verbo", "type": "text", "w": "s",
   "cons": "Scrivi il verbo al presente.", "items": E6_I, "k": E6_K},
  {"id": "e7", "title": "7 · Completa le frasi", "short": "7 · Completa le frasi", "type": "cloze",
   "cons": "Scrivi i verbi tra parentesi al presente.", "parts": E7_P, "k": E7_K},

  {"part": "I verbi in -ISC (finire, capire, pulire, preferire)"},
  {"id": "e8", "title": "8 · Le desinenze in -ISC", "short": "8 · Desinenze -ISC", "type": "select",
   "cons": "Collega ogni persona alla desinenza giusta. Attenzione agli intrusi!",
   "opts": ["-ISCO", "-ISCI", "-ISCE", "-IAMO", "-ITE", "-ISCONO", "-SCITE", "-CO", "-SCIAMO", "-SCI"],
   "items": [{"q": q} for q in ["IO", "TU", "LUI", "LEI", "NOI", "VOI", "LORO"]],
   "k": [eq("-ISCO"), eq("-ISCI"), eq("-ISCE"), eq("-ISCE"), eq("-IAMO"), eq("-ITE"), eq("-ISCONO")]},
  {"id": "e9", "title": "9 · Chi è? Scegli la persona", "short": "9 · Chi è? (-ISC)", "type": "choice", "opts": P6,
   "cons": "Per ogni verbo scegli la persona giusta. Esempio: CAPISCO → IO.", "items": E9_I, "k": E9_K},
  {"id": "e10", "title": "10 · Trova il verbo SBAGLIATO", "short": "10 · Verbo sbagliato", "type": "choice",
   "cons": "In ogni riga c'è un verbo che non va bene con la persona. Toccalo.", "items": E10_I, "k": E10_K},
  {"id": "e11", "title": "11 · Trova il verbo GIUSTO", "short": "11 · Verbo giusto", "type": "choice",
   "cons": "In ogni riga c'è solo un verbo giusto per la persona. Toccalo.", "items": E11_I, "k": E11_K},

  {"part": "I verbi con le immagini"},
  {"id": "f1", "title": "A · Che cosa fa? Scegli il verbo", "short": "A · Verbi e foto (scegli)", "type": "select",
   "cons": "Guarda la foto e scegli il verbo giusto.", "opts": sorted(v.upper() for v in FOTO_A),
   "items": [{"q": f"{i}.<br>" + img(v)} for i, v in enumerate(FOTO_A, 1)], "k": [eq(v.upper()) for v in FOTO_A]},
  {"id": "f2", "title": "B · Che cosa fa? Scrivi il verbo", "short": "B · Verbi e foto (scrivi)", "type": "text",
   "cons": "Guarda la foto e scrivi il verbo all'infinito (come nel dizionario: MANGIARE, BERE, DORMIRE…).",
   "bank": " · ".join(v.upper() for v in sorted(FOTO_B)),
   "items": [{"q": f"{i}.<br>" + img(v)} for i, v in enumerate(FOTO_B, 1)],
   "k": [eq(*FOTO_B_OK.get(v, [v])) for v in FOTO_B]},
  {"id": "f3", "title": "C · Guarda e completa la frase", "short": "C · Foto e frasi", "type": "text", "w": "s",
   "cons": "Guarda la foto e scrivi il verbo al presente.",
   "items": [{"q": img(f), "pre": f"{i}. {a}", "post": b} for i, (f, a, b, _) in enumerate(FRASI_FOTO, 1)],
   "k": [eq(r) for *_, r in FRASI_FOTO]},
  {"part": "Essere e avere"},
  {"id": "e12", "title": "12 · IO HO o IO SONO?", "short": "12 · Ho o sono?", "type": "choice",
   "opts": ["IO HO", "IO SONO"], "cons": "IO HO + una cosa (IO HO LA MACCHINA). IO SONO + chi sono, il mio lavoro (IO SONO MECCANICO).",
   "items": [{"q": f"{i}. {v}"} for i, (v, _) in enumerate(HO_SONO, 1)], "k": [eq(a) for _, a in HO_SONO]},
  {"id": "e13", "title": "13 · ESSERE o AVERE: completa", "short": "13 · Essere e avere", "type": "text", "w": "s",
   "cons": "Scrivi il verbo ESSERE o AVERE al presente.", "items": E13_I, "k": E13_K},

  {"part": "I verbi irregolari"},
  {"id": "e14", "title": "14 · Chi è? Verbi irregolari", "short": "14 · Chi è? (irregolari)", "type": "choice", "opts": P6,
   "cons": "Anche i verbi irregolari finiscono quasi sempre così: IO -O, TU -I, NOI -IAMO, VOI -ATE/-ETE/-ITE, LORO -ANO/-ONO. Scegli la persona.",
   "items": E14_I, "k": E14_K},
  {"id": "e15", "title": "15 · Chi è? Regolari e irregolari", "short": "15 · Chi è? (tutti)", "type": "choice", "opts": P6,
   "cons": "Per ogni verbo scegli la persona giusta. Esempio: SALIAMO → NOI.", "items": E15_I, "k": E15_K},
  {"id": "e16", "title": "16 · Trova il verbo SBAGLIATO", "short": "16 · Verbo sbagliato", "type": "choice",
   "cons": "In ogni riga c'è un verbo che non va bene con la persona. Toccalo.", "items": E16_I, "k": E16_K},
  {"id": "e17", "title": "17 · Trova il verbo GIUSTO", "short": "17 · Verbo giusto", "type": "choice",
   "cons": "In ogni riga c'è solo un verbo giusto per la persona. Toccalo.", "items": E17_I, "k": E17_K},
  {"id": "e18", "title": "18 · Metti il verbo giusto", "short": "18 · Metti il verbo", "type": "text", "w": "s",
   "cons": "Scrivi il verbo irregolare al presente.", "items": E18_I, "k": E18_K},

  {"part": "Andare, venire, fare, dare, stare"},
  {"id": "e19", "title": "19 · ANDARE o FARE? Scegli", "short": "19 · Andare o fare", "type": "choice",
   "cons": "Scegli il verbo giusto.", "items": E19_I, "k": E19_K},
  {"id": "e20", "title": "20 · Scrivi ANDARE o FARE", "short": "20 · Scrivi andare o fare", "type": "text", "w": "s",
   "cons": "Scrivi il verbo ANDARE o FARE al presente.", "items": E20_I, "k": E20_K},
  {"id": "e21", "title": "21 · ANDARE e VENIRE", "short": "21 · Andare e venire", "type": "text", "w": "s",
   "cons": "Scrivi il verbo al presente.", "items": E21_I, "k": E21_K},
  {"id": "e22", "title": "22 · AL, ALLA, ALL'…", "short": "22 · Al, alla, all'", "type": "select", "opts": PREP,
   "cons": "A + IL = AL · A + LO = ALLO · A + L' = ALL' · A + LA = ALLA · A + I = AI · A + GLI = AGLI · A + LE = ALLE",
   "items": [{"q": q} for q, _ in E22], "k": [eq(a) for _, a in E22]},
  {"id": "e23", "title": "23 · FARE e DARE", "short": "23 · Fare e dare", "type": "text", "w": "s",
   "cons": "Scrivi il verbo al presente.", "items": E23_I, "k": E23_K},
  {"id": "e24", "title": "24 · Che lavoro fa?", "short": "24 · Lavoro e plurale", "type": "text", "w": "w",
   "cons": "Scrivi la frase completa con il verbo FARE. Esempio: TU, IMPIEGATA, FABBRICA → TU FAI L'IMPIEGATA IN FABBRICA.",
   "items": [{"q": q} for q in ["1. LEI, BIDELLA, SCUOLA", "2. NOI, MEDICI, OSPEDALE", "3. LUI, MAESTRO, SCUOLA",
                                 "4. Al plurale: TU FAI IL MEDICO → VOI …", "5. Al plurale: LUI FA IL CAMERIERE → LORO …",
                                 "6. Al plurale: IO FACCIO L'IMPIEGATO → NOI …"]],
   "k": [frase(["lei"], "fa la bidella a scuola"), frase(["noi"], "facciamo i medici in ospedale"),
         frase(["lui"], "fa il maestro a scuola"), frase(["voi"], "fate i medici"),
         frase(["loro"], "fanno i camerieri"), frase(["noi"], "facciamo gli impiegati")]},
  {"id": "f4", "title": "D · Facciamo i compiti con FARE", "short": "D · Espressioni con fare", "type": "cloze",
   "cons": "Completa il testo con queste espressioni. Scrivi il verbo FARE al presente (IO … / NOI …).",
   "bank": "FARE COLAZIONE · FARE QUATTRO CHIACCHIERE · FARE GINNASTICA · FARE UNA TELEFONATA · FARE LA DOCCIA · FARE DUE PASSI",
   "parts": FARE_TESTO[0], "k": FARE_TESTO[1]},
  {"id": "f5", "title": "E · Guarda le foto: che cosa fanno?", "short": "E · Fare e foto", "type": "text", "w": "m",
   "cons": "Guarda la foto e completa con il verbo FARE.",
   "items": [{"q": img("fare-spesa"), "pre": "1. IO", "post": "LA SPESA"},
             {"q": img("fare-pulizie"), "pre": "2. IO E MIO FIGLIO", "post": "LE PULIZIE"},
             {"q": img("fare-festa"), "pre": "3. NOI FACCIAMO", "post": ""},
             {"q": img("fare-doccia"), "pre": "4. LUI", "post": ""},
             {"q": img("fare-corsa"), "pre": "5. LUI", "post": ""},
             {"q": img("fare-cucina"), "pre": "6. IO E LA MIA FAMIGLIA", "post": ""}],
   "k": [eq("faccio"), eq("facciamo"), eq("festa", "una festa", "la festa", "festa insieme"),
         eq("fa la doccia"), eq("fa jogging", "fa sport", "fa una corsa", "fa footing", "fa ginnastica", "fa running", "fa due passi"),
         eq("facciamo da mangiare", "facciamo il pranzo", "facciamo la cena", "facciamo colazione",
            "facciamo pranzo", "facciamo merenda", "facciamo la spesa")]},
  {"id": "f6", "title": "F ✎ · E tu quando fai queste cose?", "type": "free", "rows": 5,
   "items": ["Scrivi delle frasi come nell'esempio: IL SABATO POMERIGGIO FACCIO LA SPESA. LA SERA FACCIO LA DOCCIA."]},
  {"id": "e25", "title": "25 · Chi è?", "short": "25 · I mestieri", "type": "select", "opts": MESTIERI,
   "cons": "Che cosa fa? Leggi e scegli il lavoro.", "items": [{"q": q} for q, _ in E25], "k": [eq(a) for _, a in E25]},
  {"id": "e26", "title": "26 · STARE + gerundio", "short": "26 · Stare + gerundio", "type": "text", "w": "s",
   "cons": "Che cosa stai facendo adesso? Scrivi il verbo STARE al presente.", "items": E26_I, "k": E26_K},

  {"part": "Singolare e plurale"},
  {"id": "e27", "title": "27 · Dal singolare al plurale", "short": "27 · Al plurale", "type": "text", "w": "w",
   "cons": "Scrivi la frase al plurale. IO → NOI · TU → VOI · LUI/LEI → LORO.",
   "items": [{"q": q} for q in ["1. IO HO 30 ANNI", "2. LEI È A CASA", "3. TU MANGI L'INSALATA", "4. TU VAI AL PARCO",
                                 "5. TU GUARDI LA TELEVISIONE", "6. LUI È SIMPATICO", "7. TU LEGGI IL LIBRO",
                                 "8. LEI PRENDE L'AUTOBUS", "9. IO COMPRO IL VESTITO PER LA FESTA",
                                 "10. IO PARLO CON MIO FRATELLO"]],
   "k": [eq("noi abbiamo 30 anni", "abbiamo 30 anni", "noi abbiamo trenta anni", "abbiamo trenta anni"),
         frase(["loro"], "sono a casa"), frase(["voi"], "mangiate l'insalata"), frase(["voi"], "andate al parco"),
         frase(["voi"], "guardate la televisione"),
         eq("loro sono simpatici", "sono simpatici", "loro sono simpatiche", "sono simpatiche"),
         eq("voi leggete il libro", "leggete il libro", "voi leggete i libri", "leggete i libri"),
         eq("loro prendono l'autobus", "prendono l'autobus"),
         eq("noi compriamo il vestito per la festa", "compriamo il vestito per la festa",
            "noi compriamo i vestiti per la festa", "compriamo i vestiti per la festa"),
         eq(*[p + "parliamo con " + f for p in ["noi ", ""] for f in
              ["mio fratello", "nostro fratello", "i nostri fratelli", "i miei fratelli"]])]},
  {"id": "e28", "title": "28 · Dal plurale al singolare", "short": "28 · Al singolare", "type": "text", "w": "w",
   "cons": "Scrivi la frase al singolare. NOI → IO · VOI → TU · LORO → LUI/LEI.",
   "items": [{"q": q} for q in ["1. NOI PARLIAMO BENE L'ITALIANO", "2. LORO HANNO DUE GATTI",
                                 "3. VOI GUARDATE LA TELEVISIONE", "4. NOI COMPRIAMO IL PANE",
                                 "5. VOI MANGIATE GLI SPAGHETTI", "6. LORO BEVONO IL TÈ", "7. VOI ANDATE IN PISCINA",
                                 "8. NOI ENTRIAMO A SCUOLA", "9. LORO SONO FELICI", "10. LE MATITE SONO COLORATE"]],
   "k": [frase(["io"], "parlo bene l'italiano"), frase(["lui", "lei"], "ha due gatti"),
         frase(["tu"], "guardi la televisione"), frase(["io"], "compro il pane"),
         frase(["tu"], "mangi gli spaghetti"), frase(["lui", "lei"], "beve il tè"), frase(["tu"], "vai in piscina"),
         frase(["io"], "entro a scuola"), frase(["lui", "lei"], "è felice"), eq("la matita è colorata")]},

  {"part": "La giornata di Matteo"},
  {"id": "e29", "title": "29 · Trova i verbi", "short": "29 · Trova i verbi", "type": "set", "n": 8,
   "cons": "Leggi il testo. Scrivi 8 verbi diversi che trovi nel testo.", "info": MATTEO,
   "k": [VERBI_MATTEO] * 8},
  {"id": "e30", "title": "30 · Rispondi", "short": "30 · Rispondi", "type": "text", "w": "w",
   "cons": "Leggi di nuovo il testo e rispondi.", "info": MATTEO,
   "items": [{"q": q} for q in ["1. A CHE ORA SI ALZA MATTEO?", "2. COME VA AL LAVORO?", "3. DOVE PRANZA?",
                                 "4. CHE COSA FA DOPO CENA?", "5. A CHE ORA VA A DORMIRE?"]],
   "k": [has("7", "sette"), has("autobus"), has("bar"), has("piatti", "chatta"), has("23", "undici")]},
  {"id": "e31", "title": "31 ✎ · E tu? La tua giornata", "type": "free", "rows": 6,
   "items": ["Scrivi la tua giornata come Matteo: ALLE 7 IO MI ALZO, FACCIO COLAZIONE, VADO A SCUOLA…"]},
 ]
}

# numera gli esercizi in ordine (1, 2, 3…)
import re as _re
_n = 0
for _s in PRESENTE["sections"]:
    if "title" in _s:
        _n += 1
        _s["title"] = _re.sub(r"^\S+( ✎)? ·", lambda m: f"{_n}{m.group(1) or ''} ·", _s["title"])
        if "short" in _s:
            _s["short"] = _re.sub(r"^\S+ ·", f"{_n} ·", _s["short"])
