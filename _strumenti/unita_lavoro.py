"""Esercizi interattivi dell'argomento «Il lavoro» (5 unità)."""
from genera import eq, has, all_

VF = ["VERO", "FALSO"]
SINO = ["SÌ 👍", "NO 👎"]

def vf(s):  # "VFVF" -> chiavi
    return [eq("VERO") if c == "V" else eq("FALSO") for c in s]

AUTO = {"id": "auto", "title": "✅ Come va?", "type": "survey", "opts": ["bene", "abbastanza", "ancora poco"]}

# ---------------------------------------------------------------- 1. CHE LAVORO FAI?
AHMED = ("<p>CIAO FATIMA, COME STAI?</p><p>DA UNA SETTIMANA HO UN LAVORO NUOVO E MI TROVO BENE! LAVORO IN UNA FABBRICA DI PASTA VICINO A BARI: "
         "FACCIO L'OPERAIO. HO UN CONTRATTO DI 6 MESI.</p><p>LAVORO SU TURNI: IL PRIMO TURNO COMINCIA ALLE 6 E FINISCE ALLE 14, IL SECONDO TURNO "
         "COMINCIA ALLE 14 E FINISCE ALLE 22. QUANDO FACCIO IL PRIMO TURNO, IL POMERIGGIO VADO A SCUOLA DI ITALIANO. QUANDO FACCIO IL SECONDO "
         "TURNO, LA MATTINA VADO A CORRERE AL MARE.</p><p>I COLLEGHI SONO GENTILI: QUANDO NON CAPISCO, MI AIUTANO. PRIMA DI COMINCIARE HO FATTO "
         "IL CORSO SULLA SICUREZZA. IN FABBRICA METTO SEMPRE LE SCARPE DI SICUREZZA E I GUANTI.</p><p>AL LAVORO NON POSSO USARE IL CELLULARE: "
         "TI CHIAMO STASERA! A PRESTO, AHMED</p>")
ANNUNCI = ("<p class='ann'><b>AMINA</b> · HO 28 ANNI, SONO MAROCCHINA. HO LAVORATO COME CAMERIERA. CERCO LAVORO COME CAMERIERA O CUOCA.</p>"
           "<p class='ann'><b>JOHN</b> · HO 25 ANNI, SONO NIGERIANO. HO LA PATENTE B. CERCO LAVORO COME AUTISTA O MAGAZZINIERE.</p>"
           "<p class='ann'><b>OKSANA</b> · HO 45 ANNI, SONO UCRAINA. IN UCRAINA FACCIO L'INFERMIERA. IN ITALIA CERCO LAVORO COME BADANTE.</p>"
           "<p class='ann'><b>SAID</b> · HO 39 ANNI, SONO TUNISINO. PARLO ARABO, FRANCESE E ITALIANO. CERCO LAVORO COME MEDIATORE CULTURALE.</p>")

CHE_LAVORO = {
 "title": "👷 Che lavoro fai? · Esercizi",
 "store": "che-lavoro-fai",
 "upper": True,
 "sections": [
  {"part": "I lavori"},
  {"id": "e1", "title": "1 · Chi è? Guarda e scegli", "short": "1 · Chi è?", "type": "select",
   "opts": ["IL CUOCO", "IL MEDICO", "IL MURATORE", "L'AUTISTA", "LA SARTA", "IL POSTINO", "L'INSEGNANTE", "IL MECCANICO", "LA PARRUCCHIERA", "IL CAMERIERE"],
   "items": [{"q": q} for q in ["1. 🧑‍🍳", "2. 🩺", "3. 🧱", "4. 🚌", "5. 🧵", "6. ✉️", "7. 👩‍🏫", "8. 🔧", "9. 💇", "10. 🍽️"]],
   "k": [eq(a) for a in ["IL CUOCO", "IL MEDICO", "IL MURATORE", "L'AUTISTA", "LA SARTA", "IL POSTINO", "L'INSEGNANTE", "IL MECCANICO", "LA PARRUCCHIERA", "IL CAMERIERE"]]},
  {"id": "e2", "title": "2 · Che cosa fa?", "short": "2 · Che cosa fa", "type": "select",
   "cons": "Collega il lavoro e l'attività.",
   "opts": ["CURA I MALATI", "RIPARA LA MACCHINA", "GUIDA L'AUTOBUS", "CUCE I VESTITI", "COSTRUISCE LE CASE", "PORTA LA POSTA",
            "RIPARA LE SCARPE", "VENDE I GIORNALI", "INSEGNA AGLI STUDENTI", "CURA GLI ANIMALI", "SCRIVE LE NOTIZIE"],
   "items": [{"q": q} for q in ["1. IL MEDICO", "2. IL MECCANICO", "3. L'AUTISTA", "4. LA SARTA", "5. IL MURATORE", "6. IL POSTINO",
                                 "7. IL CALZOLAIO", "8. LA GIORNALAIA", "9. L'INSEGNANTE", "10. IL VETERINARIO", "11. IL GIORNALISTA"]],
   "k": [eq(a) for a in ["CURA I MALATI", "RIPARA LA MACCHINA", "GUIDA L'AUTOBUS", "CUCE I VESTITI", "COSTRUISCE LE CASE", "PORTA LA POSTA",
                          "RIPARA LE SCARPE", "VENDE I GIORNALI", "INSEGNA AGLI STUDENTI", "CURA GLI ANIMALI", "SCRIVE LE NOTIZIE"]]},
  {"id": "e3", "title": "3 · Dove lavora?", "short": "3 · Dove lavora", "type": "select",
   "opts": ["IN OSPEDALE", "A SCUOLA", "AL RISTORANTE", "IN CANTIERE", "IN FABBRICA", "IN NEGOZIO", "IN UFFICIO", "IN OFFICINA", "IN CAMPAGNA"],
   "items": [{"q": q} for q in ["1. L'INFERMIERA LAVORA…", "2. L'INSEGNANTE LAVORA…", "3. IL CAMERIERE LAVORA…", "4. IL MURATORE LAVORA…",
                                 "5. L'OPERAIO LAVORA…", "6. LA COMMESSA LAVORA…", "7. L'IMPIEGATO LAVORA…", "8. IL MECCANICO LAVORA…", "9. IL BRACCIANTE LAVORA…"]],
   "k": [eq(a) for a in ["IN OSPEDALE", "A SCUOLA", "AL RISTORANTE", "IN CANTIERE", "IN FABBRICA", "IN NEGOZIO", "IN UFFICIO", "IN OFFICINA", "IN CAMPAGNA"]]},

  {"part": "La grammatica"},
  {"id": "e4", "title": "4 · Lui e lei: scrivi il femminile", "short": "4 · Femminile", "type": "text",
   "cons": "Esempio: IL CUOCO → LA CUOCA",
   "items": [{"q": q} for q in ["1. IL CAMERIERE → LA", "2. L'INFERMIERE → L'", "3. IL COMMESSO → LA", "4. L'OPERAIO → L'",
                                 "5. IL MEDIATORE → LA", "6. IL SARTO → LA", "7. L'AUTISTA → L'", "8. L'INSEGNANTE → L'"]],
   "k": [eq("cameriera", "la cameriera"), eq("infermiera", "l'infermiera"), eq("commessa", "la commessa"), eq("operaia", "l'operaia"),
         eq("mediatrice", "la mediatrice"), eq("sarta", "la sarta"), eq("autista", "l'autista"), eq("insegnante", "l'insegnante")]},
  {"id": "e5", "title": "5 · Il verbo FARE", "short": "5 · Fare", "type": "cloze",
   "bank": "FACCIO · FAI · FA · FACCIAMO · FATE · FANNO",
   "parts": ["1. IO ", {}, " IL CUOCO.<br>2. E TU, CHE LAVORO ", {}, "?<br>3. LEI ", {}, " LA COMMESSA.<br>4. NOI ", {},
             " I TURNI.<br>5. VOI CHE COSA ", {}, "?<br>6. LORO ", {}, " GLI OPERAI."],
   "k": [eq(a) for a in ["faccio", "fai", "fa", "facciamo", "fate", "fanno"]]},
  {"id": "e6", "title": "6 · Il verbo LAVORARE", "short": "6 · Lavorare", "type": "text",
   "cons": "Scrivi il verbo. Esempio: IO → LAVORO",
   "items": [{"q": q} for q in ["1. TU", "2. LUI / LEI", "3. NOI", "4. VOI", "5. LORO"]],
   "k": [eq("lavori", "tu lavori"), eq("lavora", "lui lavora", "lei lavora"), eq("lavoriamo", "noi lavoriamo"),
         eq("lavorate", "voi lavorate"), eq("lavorano", "loro lavorano")]},
  {"id": "e7", "title": "7 · Quale frase è giusta?", "short": "7 · Frase giusta", "type": "choice", "full": True,
   "items": [{"q": "1.", "opts": ["SONO IL CUOCO.", "SONO CUOCO."]},
             {"q": "2.", "opts": ["FACCIO IL CAMERIERE.", "FACCIO CAMERIERE."]},
             {"q": "3.", "opts": ["LAVORO DI AUTISTA.", "LAVORO COME AUTISTA."]},
             {"q": "4.", "opts": ["LEI FA LA COMMESSA.", "LEI FA COMMESSA."]},
             {"q": "5.", "opts": ["LAVORO IN OSPEDALE.", "LAVORO A OSPEDALE."]},
             {"q": "6.", "opts": ["SONO DISOCCUPATO: CERCO LAVORO.", "SONO DISOCCUPATO: HO UN LAVORO."]}],
   "k": [eq("SONO CUOCO."), eq("FACCIO IL CAMERIERE."), eq("LAVORO COME AUTISTA."), eq("LEI FA LA COMMESSA."),
         eq("LAVORO IN OSPEDALE."), eq("SONO DISOCCUPATO: CERCO LAVORO.")]},

  {"part": "L'orario di lavoro"},
  {"id": "e8", "title": "8 · Com'è il suo lavoro?", "short": "8 · L'orario", "type": "select",
   "opts": ["È DISOCCUPATO", "È PENSIONATO", "LAVORA A TEMPO PIENO", "LAVORA PART-TIME", "LAVORA SU TURNI"],
   "items": [{"q": q} for q in ["1. MARIO LAVORA 8 ORE AL GIORNO, 40 ORE ALLA SETTIMANA.", "2. ALI LAVORA SOLO 4 ORE AL GIORNO.",
                                 "3. CARLOS NON HA UN LAVORO. CERCA LAVORO.", "4. PIETRO HA 70 ANNI, NON LAVORA PIÙ E RICEVE LA PENSIONE.",
                                 "5. FATIMA UNA SETTIMANA LAVORA LA MATTINA, UNA SETTIMANA IL POMERIGGIO."]],
   "k": [eq(a) for a in ["LAVORA A TEMPO PIENO", "LAVORA PART-TIME", "È DISOCCUPATO", "È PENSIONATO", "LAVORA SU TURNI"]]},

  {"part": "Leggo"},
  {"id": "ahmed", "title": "📧 Leggi l'email di Ahmed", "type": "info", "info": AHMED},
  {"id": "e9", "title": "9 · Ahmed: scegli la risposta giusta", "short": "9 · Il lavoro di Ahmed", "type": "choice", "full": True,
   "items": [{"q": "1. AHMED LAVORA…", "opts": ["IN UN RISTORANTE", "IN UNA FABBRICA", "IN UN NEGOZIO"]},
             {"q": "2. AHMED FA…", "opts": ["IL CUOCO", "IL MAGAZZINIERE", "L'OPERAIO"]},
             {"q": "3. L'ORARIO DI LAVORO È…", "opts": ["SU TURNI", "SEMPRE LA MATTINA"]},
             {"q": "4. IL PRIMO TURNO COMINCIA ALLE…", "opts": ["6", "14", "22"]},
             {"q": "5. QUANDO FA IL SECONDO TURNO, LA MATTINA AHMED…", "opts": ["VA A SCUOLA", "VA A CORRERE AL MARE", "DORME"]},
             {"q": "6. IN FABBRICA AHMED METTE…", "opts": ["LA CRAVATTA", "LE SCARPE DI SICUREZZA E I GUANTI"]},
             {"q": "7. AL LAVORO AHMED…", "opts": ["PUÒ USARE IL CELLULARE", "NON PUÒ USARE IL CELLULARE"]},
             {"q": "8. CON I COLLEGHI AHMED…", "opts": ["SI TROVA BENE", "NON SI TROVA BENE"]}],
   "k": [eq(a) for a in ["IN UNA FABBRICA", "L'OPERAIO", "SU TURNI", "6", "VA A CORRERE AL MARE", "LE SCARPE DI SICUREZZA E I GUANTI",
                          "NON PUÒ USARE IL CELLULARE", "SI TROVA BENE"]]},
  {"id": "ann", "title": "📌 Leggi i 4 annunci «Cerco lavoro»", "type": "info", "info": ANNUNCI},
  {"id": "e10", "title": "10 · Completa con le informazioni degli annunci", "short": "10 · Gli annunci", "type": "text",
   "items": [{"q": q} for q in ["1. AMINA HA … ANNI.", "2. AMINA È … (DI CHE PAESE?)", "3. JOHN CERCA LAVORO COME AUTISTA O …",
                                 "4. JOHN HA LA PATENTE …", "5. IN ITALIA OKSANA CERCA LAVORO COME …", "6. SAID PARLA ARABO, FRANCESE E …", "7. SAID HA … ANNI."]],
   "k": [eq("28", "ventotto"), eq("marocchina", "del marocco"), eq("magazziniere"), eq("b"), eq("badante"), eq("italiano"), eq("39", "trentanove")]},

  {"part": "Scrivo e parlo"},
  {"id": "e11", "title": "11 ✎ · E tu? Presentati", "type": "free", "rows": 5,
   "items": ["Scrivi: come ti chiami, di dove sei, quanti anni hai, che lavoro fai (o che lavoro facevi nel tuo paese), che lavoro cerchi."]},
  {"id": "e12", "title": "12 🎤 · Rispondi a voce", "type": "record",
   "cons": "Premi «Registra», rispondi e poi premi «Stop». Puoi riascoltare.",
   "items": ["CHE LAVORO FAI? (OPPURE: CHE LAVORO CERCHI?)", "DOVE LAVORI? (OPPURE: DOVE LAVORAVI NEL TUO PAESE?)",
             "QUAL È IL TUO ORARIO DI LAVORO? (TEMPO PIENO, PART-TIME, TURNI…)"]},
  {"part": "Adesso so fare…"},
  dict(AUTO, items=["dire i nomi di 10 lavori", "dire che cosa fa una persona nel suo lavoro", "dire dove lavora una persona",
                    "usare FARE e LAVORARE", "dire il mio orario di lavoro", "presentarmi e dire che lavoro faccio"]),
 ]
}

# ---------------------------------------------------------------- 2. CERCO LAVORO
LETTERA_AMARA = ("<p>BUONGIORNO.</p><p>MI CHIAMO AMARA DIALLO. SONO DELLA COSTA D'AVORIO. ABITO A BARI.</p>"
                 "<p>CERCO LAVORO COME CUOCA. SO CUCINARE BENE.</p><p>PARLO ITALIANO E FRANCESE.</p><p>SONO DISPONIBILE SUBITO.</p>"
                 "<p>GRAZIE. CORDIALI SALUTI, AMARA DIALLO</p>")

CERCARE = {
 "title": "🔍 Cerco lavoro · Esercizi",
 "store": "cercare-lavoro",
 "upper": True,
 "sections": [
  {"part": "Le parole del lavoro"},
  {"id": "e1", "title": "1 · Collega la parola e la frase", "short": "1 · Le parole", "type": "select",
   "opts": ["I SOLDI DEL LAVORO", "IL DOCUMENTO CHE FIRMO", "IL FOGLIO CON IL MIO NOME E I MIEI LAVORI", "L'UFFICIO CHE MI AIUTA A CERCARE LAVORO", "PARLO CON IL DATORE DI LAVORO"],
   "items": [{"q": q} for q in ["1. IL CV", "2. LO STIPENDIO", "3. IL COLLOQUIO", "4. IL CONTRATTO", "5. IL CENTRO PER L'IMPIEGO"]],
   "k": [eq(a) for a in ["IL FOGLIO CON IL MIO NOME E I MIEI LAVORI", "I SOLDI DEL LAVORO", "PARLO CON IL DATORE DI LAVORO", "IL DOCUMENTO CHE FIRMO", "L'UFFICIO CHE MI AIUTA A CERCARE LAVORO"]]},
  {"id": "e2", "title": "2 · Scegli la parola giusta", "short": "2 · Parola giusta", "type": "choice", "full": True,
   "items": [{"q": "1. OGNI MESE RICEVO LO …", "opts": ["STIPENDIO", "COLLOQUIO"]},
             {"q": "2. PER CERCARE LAVORO PORTO IL …", "opts": ["PALLONE", "CV"]},
             {"q": "3. PRIMA DI LAVORARE FIRMO IL …", "opts": ["NEGOZIO", "CONTRATTO"]},
             {"q": "4. PARLO CON IL DATORE DI LAVORO: HO UN …", "opts": ["COLLOQUIO", "STIPENDIO"]},
             {"q": "5. IL CENTRO PER L'IMPIEGO È …", "opts": ["A PAGAMENTO", "GRATIS"]}],
   "k": [eq(a) for a in ["STIPENDIO", "CV", "CONTRATTO", "COLLOQUIO", "GRATIS"]]},
  {"id": "e3", "title": "3 · Manca una vocale: scrivi la parola", "short": "3 · Le vocali", "type": "text",
   "cons": "Manca una lettera: A, E, I, O, U. Scrivi tutta la parola.",
   "items": [{"q": q} for q in ["1. LAV _ RO", "2. CONTR _ TTO", "3. STIP _ NDIO", "4. COLLOQ _ IO", "5. UFF _ CIO", "6. GR _ TIS"]],
   "k": [eq(a) for a in ["lavoro", "contratto", "stipendio", "colloquio", "ufficio", "gratis"]]},
  {"id": "e4", "title": "4 · Altre parole: che cosa vuol dire?", "short": "4 · Altre parole", "type": "select",
   "opts": ["MANDO IL CV PER UN LAVORO", "VADO IN UN NEGOZIO E CHIEDO LAVORO, ANCHE SENZA ANNUNCIO", "UN ANNUNCIO: «CERCHIAMO PERSONALE»",
            "UN CORSO PER IMPARARE UN LAVORO", "LAVORO SOLO POCHE ORE AL GIORNO", "IL DOCUMENTO PER STARE IN ITALIA IN REGOLA"],
   "items": [{"q": q} for q in ["1. LA CANDIDATURA", "2. LA CANDIDATURA SPONTANEA", "3. L'OFFERTA DI LAVORO", "4. LA FORMAZIONE", "5. IL PART-TIME", "6. IL PERMESSO DI SOGGIORNO"]],
   "k": [eq(a) for a in ["MANDO IL CV PER UN LAVORO", "VADO IN UN NEGOZIO E CHIEDO LAVORO, ANCHE SENZA ANNUNCIO", "UN ANNUNCIO: «CERCHIAMO PERSONALE»",
                          "UN CORSO PER IMPARARE UN LAVORO", "LAVORO SOLO POCHE ORE AL GIORNO", "IL DOCUMENTO PER STARE IN ITALIA IN REGOLA"]]},

  {"part": "Cosa serve per lavorare"},
  {"id": "e5", "title": "5 · Vero o falso?", "short": "5 · Cosa serve", "type": "choice", "opts": VF, "full": True,
   "items": [{"q": q} for q in ["1. POSSO LAVORARE A 14 ANNI.", "2. A 16 ANNI POSSO LAVORARE SE HO FINITO LA SCUOLA OBBLIGATORIA.",
                                 "3. SE HO CHIESTO PROTEZIONE, POSSO LAVORARE IL GIORNO DOPO LA DOMANDA.",
                                 "4. IL CONTRATTO DI LAVORO È REGISTRATO CON IL MIO CODICE FISCALE.", "5. CON L'IBAN RICEVO LO STIPENDIO SUL CONTO.",
                                 "6. CON IL LAVORO IN NERO HO LE FERIE PAGATE.", "7. SE LAVORO IN NERO E MI FACCIO MALE, NESSUNO MI PAGA."]],
   "k": vf("FVFVVFV")},

  {"part": "Dove cerco lavoro"},
  {"id": "e6", "title": "6 · Vero o falso?", "short": "6 · Dove cerco", "type": "choice", "opts": VF, "full": True,
   "items": [{"q": q} for q in ["1. IL CENTRO PER L'IMPIEGO È GRATIS.", "2. IL CENTRO PER L'IMPIEGO È SOLO A ROMA.", "3. L'APP «LAVORO PER TE PUGLIA» È SUL TELEFONO.",
                                 "4. L'APP COSTA 10 EURO.", "5. CHIEDO LAVORO AGLI AMICI.", "6. NEI NEGOZI CHIEDO: «CERCATE PERSONALE?»",
                                 "7. LE AGENZIE PER IL LAVORO SONO GRATIS PER CHI CERCA LAVORO."]],
   "k": vf("VFVFVVV")},
  {"id": "e7", "title": "7 · Completa con le parole", "short": "7 · Completa", "type": "cloze",
   "bank": "BARI · TELEFONO · GRATIS · AMICI · CV",
   "parts": ["1. IL CENTRO PER L'IMPIEGO È A ", {}, ".<br>2. L'APP È SUL ", {}, ".<br>3. L'APP NON COSTA: È ", {},
             ".<br>4. CHIEDO LAVORO AGLI ", {}, ".<br>5. PORTO SEMPRE IL MIO ", {}, "."],
   "k": [eq(a) for a in ["bari", "telefono", "gratis", "amici", "cv"]]},
  {"id": "e8", "title": "8 · L'app: metti in ordine (da 1 a 5)", "short": "8 · L'app in ordine", "type": "order",
   "items": ["CERCO LE OFFERTE DI LAVORO A BARI.", "SCARICO L'APP SUL TELEFONO.", "TOCCO «CANDIDATI».", "METTO IL MIO CV.", "SCRIVO LA MIA EMAIL E LA PASSWORD."],
   "k": [eq(a) for a in ["4", "1", "5", "3", "2"]]},
  {"id": "e9", "title": "9 · Completa con i verbi", "short": "9 · I verbi", "type": "cloze",
   "bank": "CERCO · TOCCO · SCARICO · SCRIVO",
   "parts": ["1. IO ", {}, " L'APP SUL TELEFONO.<br>2. IO ", {}, " LA MIA EMAIL.<br>3. IO ", {}, " LAVORO A BARI.<br>4. IO ", {}, " «CANDIDATI»."],
   "k": [eq(a) for a in ["scarico", "scrivo", "cerco", "tocco"]]},
  {"id": "e10", "title": "10 · Cosa serve per usare l'app?", "short": "10 · Cosa serve", "type": "multi",
   "cons": "Metti la spunta vicino alle 4 cose giuste.",
   "items": ["📱 IL TELEFONO", "☂️ L'OMBRELLO", "⚽ IL PALLONE", "📧 L'EMAIL", "📄 IL CV", "🍕 LA PIZZA", "🚗 LA MACCHINA", "🔑 IL CODICE FISCALE"],
   "k": [eq(a) for a in ["X", "-", "-", "X", "X", "-", "-", "X"]]},

  {"part": "Mi presento"},
  {"id": "e11", "title": "11 · Metti in ordine le parole", "short": "11 · Le frasi", "type": "text", "w": "w", "full": True,
   "cons": "Scrivi la frase giusta. Esempio: LAVORO CERCO → CERCO LAVORO.",
   "items": [{"q": q} for q in ["1. BARI · CERCO · A · LAVORO", "2. COLLOQUIO · HO · DOMANI · UN", "3. MIO · PORTO · CV · IL",
                                 "4. DISPONIBILE · SUBITO · SONO", "5. COME · LAVORO · CAMERIERE · CERCO",
                                 "6. L'IMPIEGO · PORTO · AL · IL · CENTRO · MIO · PER · CV"]],
   "k": [eq("cerco lavoro a bari", "a bari cerco lavoro"), eq("ho un colloquio domani", "domani ho un colloquio"), eq("porto il mio cv"),
         eq("sono disponibile subito"), eq("cerco lavoro come cameriere"), eq("porto il mio cv al centro per l'impiego", "al centro per l'impiego porto il mio cv")]},
  {"id": "e12", "title": "12 · Amara entra in un ristorante", "short": "12 · Il dialogo", "type": "cloze",
   "bank": "CV · GRAZIE · PERSONALE · SUBITO · BUONGIORNO",
   "parts": ["<b>AMARA:</b> ", {}, "! CERCATE ", {}, "?<br><b>SIGNORA:</b> SÌ, CERCHIAMO UNA CUOCA.<br><b>AMARA:</b> HO IL MIO ", {},
             ". LO POSSO LASCIARE?<br><b>SIGNORA:</b> SÌ. QUANDO PUÒ INIZIARE?<br><b>AMARA:</b> POSSO INIZIARE ", {},
             ".<br><b>SIGNORA:</b> BENE. LA CHIAMO DOMANI.<br><b>AMARA:</b> ", {}, ", ARRIVEDERCI!"],
   "k": [eq(a) for a in ["buongiorno", "personale", "cv", "subito", "grazie"]]},
  {"id": "lett", "title": "✉️ Leggi la lettera di Amara", "type": "info", "info": LETTERA_AMARA},
  {"id": "e13", "title": "13 · La lettera di Amara", "short": "13 · La lettera", "type": "choice", "full": True,
   "items": [{"q": "1. AMARA È…", "opts": ["DEL MAROCCO", "DELLA COSTA D'AVORIO"]},
             {"q": "2. AMARA ABITA A…", "opts": ["NAPOLI", "ROMA", "BARI"]},
             {"q": "3. AMARA CERCA LAVORO COME…", "opts": ["CUOCA", "CAMERIERA", "BADANTE"]},
             {"q": "4. AMARA PARLA…", "opts": ["ITALIANO E ARABO", "ITALIANO E FRANCESE"]},
             {"q": "5. AMARA PUÒ INIZIARE…", "opts": ["SUBITO", "FRA UN MESE", "FRA UN ANNO"]}],
   "k": [eq(a) for a in ["DELLA COSTA D'AVORIO", "BARI", "CUOCA", "ITALIANO E FRANCESE", "SUBITO"]]},
  {"id": "e14", "title": "14 ✎ · Scrivi la tua lettera", "type": "free", "rows": 9,
   "items": ["Usa la lettera di Amara come modello: BUONGIORNO. MI CHIAMO … SONO DI … ABITO A … CERCO LAVORO COME … SO … PARLO … SONO DISPONIBILE … GRAZIE. CORDIALI SALUTI, …"]},
  {"id": "e15", "title": "15 🎤 · Entri in un negozio", "type": "record",
   "cons": "Registra quello che dici. Saluta, chiedi se cercano personale, di' che lavoro cerchi e lascia il CV.",
   "items": ["<b>Situazione 1</b> · Entri in un bar in centro a Bari. Cerchi lavoro come barista o cameriere/a.",
             "<b>Situazione 2</b> · Entri in un supermercato. Cerchi lavoro come magazziniere/a o commesso/a. Di' quando puoi iniziare."]},
  {"part": "Adesso so fare…"},
  dict(AUTO, items=["capire le parole del lavoro (CV, colloquio, contratto…)", "dire cosa serve per lavorare in Italia",
                    "dire dove cerco lavoro a Bari", "usare l'app Lavoro per te Puglia", "chiedere «Cercate personale?»", "scrivere una lettera corta"]),
 ]
}

# ---------------------------------------------------------------- 3. CV
CV = {
 "title": "📄 Il curriculum vitae · Esercizi",
 "store": "curriculum",
 "upper": True,
 "sections": [
  {"part": "Le parole del CV"},
  {"id": "e1", "title": "1 · Collega la parola e la definizione", "short": "1 · Le parole", "type": "select",
   "opts": ["NOME DELLA FAMIGLIA", "COSA FACCIO NEL LAVORO", "CHI MI PAGA E MI DÀ IL LAVORO", "DOVE HO STUDIATO", "DOCUMENTO PER GUIDARE LA MACCHINA", "COSA SO FARE"],
   "items": [{"q": q} for q in ["1. IL COGNOME", "2. LA MANSIONE", "3. IL DATORE DI LAVORO", "4. L'ISTRUZIONE", "5. LA PATENTE", "6. LE COMPETENZE"]],
   "k": [eq(a) for a in ["NOME DELLA FAMIGLIA", "COSA FACCIO NEL LAVORO", "CHI MI PAGA E MI DÀ IL LAVORO", "DOVE HO STUDIATO", "DOCUMENTO PER GUIDARE LA MACCHINA", "COSA SO FARE"]]},
  {"id": "e2", "title": "2 · Vero o falso?", "short": "2 · Vero o falso", "type": "choice", "opts": VF, "full": True,
   "items": [{"q": q} for q in ["1. NEL CV SCRIVO LA MIA ETÀ.", "2. IL CV SI CHIAMA ANCHE CURRICULUM VITAE.", "3. LA MANSIONE È DOVE ABITO.",
                                 "4. LA LINGUA MADRE È LA MIA PRIMA LINGUA.", "5. POSSO USARE SUPERBELLA99@… NEL CV.", "6. NEL CV SCRIVO PRIMA IL LAVORO PIÙ RECENTE."]],
   "k": vf("FVFVFV")},
  {"id": "e3", "title": "3 · Che cosa va bene nel CV?", "short": "3 · Le regole", "type": "choice", "full": True,
   "items": [{"q": "1. L'EMAIL", "opts": ["SUPERMARIO99@…", "MARIO.ROSSI@…"]},
             {"q": "2. LA DATA", "opts": ["HO 30 ANNI", "15/03/1995"]},
             {"q": "3. LA FOTO", "opts": ["UN SELFIE CON GLI OCCHIALI DA SOLE", "UNA FOTO SERIA CON SFONDO BIANCO"]},
             {"q": "4. NON HO ESPERIENZA", "opts": ["LASCIO LO SPAZIO VUOTO", "SCRIVO «NESSUNA ESPERIENZA»"]},
             {"q": "5. L'ORDINE DEI LAVORI", "opts": ["PRIMA IL LAVORO PIÙ VECCHIO", "PRIMA IL LAVORO PIÙ RECENTE"]}],
   "k": [eq(a) for a in ["MARIO.ROSSI@…", "15/03/1995", "UNA FOTO SERIA CON SFONDO BIANCO", "SCRIVO «NESSUNA ESPERIENZA»", "PRIMA IL LAVORO PIÙ RECENTE"]]},
  {"id": "e4", "title": "4 · I livelli delle lingue", "short": "4 · I livelli", "type": "select",
   "opts": ["PRINCIPIANTE", "ELEMENTARE", "INTERMEDIO", "BUONO", "AVANZATO", "COME UN MADRELINGUA"],
   "items": [{"q": q} for q in ["A1", "A2", "B1", "B2", "C1", "C2"]],
   "k": [eq(a) for a in ["PRINCIPIANTE", "ELEMENTARE", "INTERMEDIO", "BUONO", "AVANZATO", "COME UN MADRELINGUA"]]},

  {"part": "Il CV di Amara"},
  {"id": "e5", "title": "5 · Completa il CV di Amara", "short": "5 · Il CV di Amara", "type": "text",
   "bank": "IVORIANA · 21/07/1998 · CUOCA · FRANCESE · B1 · AMARA.DIALLO@ESEMPIO.IT",
   "items": [{"q": q} for q in ["1. LA NAZIONALITÀ DI AMARA È:", "2. LA DATA DI NASCITA È:", "3. LA SUA EMAIL È:",
                                 "4. HA LAVORATO COME:", "5. LA SUA LINGUA MADRE È IL:", "6. PARLA ITALIANO A LIVELLO:"]],
   "k": [eq("ivoriana"), eq("21/07/1998", "21/7/1998", "21-07-1998", "21 07 1998"), eq("amara.diallo@esempio.it"),
         eq("cuoca"), eq("francese"), eq("b1")]},
  {"id": "e6", "title": "6 · Metti in ordine le parole", "short": "6 · Le frasi", "type": "text", "w": "w", "full": True,
   "items": [{"q": q} for q in ["1. CHIAMO · MI · AMARA · DIALLO", "2. COME · LAVORATO · HO · CAMERIERE · A · NAPOLI",
                                 "3. LIVELLO · PARLO · A2 · ITALIANO · A", "4. DIPLOMA · HO · SCUOLA · UN · DI · SUPERIORE · IN · SENEGAL"]],
   "k": [eq("mi chiamo amara diallo"), eq("ho lavorato come cameriere a napoli", "a napoli ho lavorato come cameriere"),
         eq("parlo italiano a livello a2"), eq("ho un diploma di scuola superiore in senegal", "in senegal ho un diploma di scuola superiore")]},

  {"part": "Il mio CV"},
  {"id": "e7", "title": "7 ✎ · Scrivi il tuo CV", "type": "free", "rows": 2,
   "cons": "Scrivi le tue informazioni. Non lasciare spazi vuoti: se non sai una parola, chiedi all'insegnante. Poi premi «Invia» in fondo alla pagina.",
   "items": ["1. NOME E COGNOME", "2. DATA DI NASCITA (GG/MM/AAAA)", "3. NAZIONALITÀ", "4. INDIRIZZO", "5. TELEFONO", "6. EMAIL",
             "7. ESPERIENZA LAVORATIVA: DATE (DA… A…), MANSIONE, DATORE DI LAVORO, CITTÀ E PAESE, COSA FACEVI",
             "8. ISTRUZIONE: DATE, TITOLO DI STUDIO, SCUOLA, PAESE, CORSI", "9. LINGUE: LINGUA MADRE, ITALIANO (LIVELLO), ALTRE LINGUE",
             "10. COMPETENZE: COMPUTER, PATENTE, ALTRE COSE CHE SAI FARE"]},
  {"part": "Adesso so fare…"},
  dict(AUTO, items=["capire le parole del CV", "sapere cosa fare e cosa non fare nel CV", "scrivere i livelli delle mie lingue", "scrivere il mio CV"]),
 ]
}

# ---------------------------------------------------------------- 4. COLLOQUIO E CONTRATTO
COLLOQUIO = {
 "title": "🤝 Il colloquio e il contratto · Esercizi",
 "store": "colloquio-contratti",
 "upper": True,
 "sections": [
  {"part": "Il colloquio"},
  {"id": "e1", "title": "1 · Il giorno del colloquio: sì o no?", "short": "1 · Sì o no", "type": "choice", "opts": SINO, "full": True,
   "cons": "IL GIORNO DEL COLLOQUIO IO…",
   "items": [{"q": q} for q in ["1. PORTO IL MIO CV.", "2. ARRIVO 10 MINUTI PRIMA.", "3. ARRIVO IN RITARDO.", "4. SPENGO IL TELEFONO.",
                                 "5. DICO «BUONGIORNO».", "6. PARLO AL TELEFONO CON UN AMICO.", "7. HO I VESTITI PULITI E ORDINATI.", "8. DICO BUGIE SULLE MIE ESPERIENZE."]],
   "k": [eq(SINO[0]) if c == "S" else eq(SINO[1]) for c in "SSNSSNSN"]},
  {"id": "e2", "title": "2 · Collega la domanda e la risposta", "short": "2 · Domande e risposte", "type": "select",
   "opts": ["CERCO LAVORO COME CUOCA.", "ABITO A BARI.", "MI CHIAMO AMARA DIALLO.", "POSSO INIZIARE SUBITO.", "SONO DELLA COSTA D'AVORIO.", "PARLO FRANCESE E ITALIANO."],
   "items": [{"q": q} for q in ["1. COME SI CHIAMA?", "2. DI DOV'È?", "3. DOVE ABITA?", "4. CHE LAVORO CERCA?", "5. QUANDO PUÒ INIZIARE?", "6. QUALI LINGUE PARLA?"]],
   "k": [eq(a) for a in ["MI CHIAMO AMARA DIALLO.", "SONO DELLA COSTA D'AVORIO.", "ABITO A BARI.", "CERCO LAVORO COME CUOCA.", "POSSO INIZIARE SUBITO.", "PARLO FRANCESE E ITALIANO."]]},
  {"id": "e3", "title": "3 · Chi fa la domanda?", "short": "3 · Chi chiede", "type": "choice", "opts": ["IL DATORE DI LAVORO", "IO"], "full": True,
   "items": [{"q": q} for q in ["1. «MI PARLI DI LEI.»", "2. «CHE TIPO DI CONTRATTO OFFRITE?»", "3. «HA ESPERIENZA?»",
                                 "4. «QUANTE ORE SI LAVORA?»", "5. «QUANDO PUÒ INIZIARE?»", "6. «C'È UN PERIODO DI PROVA?»"]],
   "k": [eq(a) for a in ["IL DATORE DI LAVORO", "IO", "IL DATORE DI LAVORO", "IO", "IL DATORE DI LAVORO", "IO"]]},

  {"part": "Il contratto, i diritti, i doveri"},
  {"id": "e4", "title": "4 · Collega la parola e la definizione", "short": "4 · Le parole", "type": "select",
   "opts": ["SOLDI ACCUMULATI CHE RICEVO A FINE CONTRATTO", "IL CONTRATTO COLLETTIVO DEL MIO SETTORE", "LA RETRIBUZIONE ANNUA LORDA",
            "I PRIMI MESI DI LAVORO", "LAVORARE TRAMITE UN'AGENZIA", "I GIORNI DI AVVISO PRIMA DI LASCIARE IL LAVORO"],
   "items": [{"q": q} for q in ["1. IL TFR", "2. IL CCNL", "3. LA RAL", "4. IL PERIODO DI PROVA", "5. LA SOMMINISTRAZIONE", "6. IL PREAVVISO"]],
   "k": [eq(a) for a in ["SOLDI ACCUMULATI CHE RICEVO A FINE CONTRATTO", "IL CONTRATTO COLLETTIVO DEL MIO SETTORE", "LA RETRIBUZIONE ANNUA LORDA",
                          "I PRIMI MESI DI LAVORO", "LAVORARE TRAMITE UN'AGENZIA", "I GIORNI DI AVVISO PRIMA DI LASCIARE IL LAVORO"]]},
  {"id": "e5", "title": "5 · Vero o falso?", "short": "5 · Vero o falso", "type": "choice", "opts": VF, "full": True,
   "items": [{"q": q} for q in ["1. IL CONTRATTO A TEMPO INDETERMINATO HA UNA DATA DI FINE.", "2. HO DIRITTO AD ALMENO 4 SETTIMANE DI FERIE ALL'ANNO.",
                                 "3. SE SONO MALATO, POSSONO LICENZIARMI SUBITO.", "4. LA TREDICESIMA ARRIVA A DICEMBRE.",
                                 "5. UN LICENZIAMENTO A VOCE È VALIDO.", "6. AL COLLOQUIO DEVO ESSERE PUNTUALE.",
                                 "7. IL TFR È UNO STIPENDIO IN PIÙ CHE RICEVO OGNI MESE.", "8. IL SINDACATO AIUTA I LAVORATORI GRATIS."]],
   "k": vf("FVFVFVFV")},
  {"id": "e6", "title": "6 · Completa le frasi", "short": "6 · Completa", "type": "text",
   "bank": "INDETERMINATO · TFR · PUNTUALE · FERIE · BUSTA PAGA · PROVA",
   "items": [{"q": q} for q in ["1. IL CONTRATTO SENZA DATA DI FINE È A TEMPO …", "2. I SOLDI CHE RICEVO ALLA FINE DEL LAVORO SONO IL …",
                                 "3. AL COLLOQUIO DEVO ESSERE SEMPRE …", "4. HO DIRITTO AD ALMENO 4 SETTIMANE DI …",
                                 "5. IL DOCUMENTO CON LO STIPENDIO DEL MESE È LA …", "6. I PRIMI MESI DI LAVORO SONO IL PERIODO DI …"]],
   "k": [eq(a) for a in ["indeterminato", "tfr", "puntuale", "ferie", "busta paga", "prova"]]},
  {"id": "e7", "title": "7 · Metti in ordine le parole", "short": "7 · Le frasi", "type": "text", "w": "w", "full": True,
   "items": [{"q": q} for q in ["1. IL · CONTRATTO · LEGGO · FIRMARE · DI · PRIMA", "2. DIRITTO · HO · A · 4 · FERIE · DI · SETTIMANE",
                                 "3. SINDACATO · IL · AIUTARMI · PUÒ", "4. PUNTUALE · COLLOQUIO · ESSERE · DEVO · AL"]],
   "k": [eq("prima di firmare leggo il contratto", "leggo il contratto prima di firmare"),
         eq("ho diritto a 4 settimane di ferie", "ho diritto a quattro settimane di ferie"),
         eq("il sindacato può aiutarmi", "il sindacato puo' aiutarmi"),
         eq("devo essere puntuale al colloquio", "al colloquio devo essere puntuale")]},
  {"id": "e8", "title": "8 · Che contratto è?", "short": "8 · I contratti", "type": "select",
   "opts": ["A TEMPO INDETERMINATO", "A TEMPO DETERMINATO", "APPRENDISTATO", "PART-TIME", "A CHIAMATA", "CON L'AGENZIA (SOMMINISTRAZIONE)"],
   "items": [{"q": q} for q in ["1. LAVORO SOLO QUANDO IL RISTORANTE MI CHIAMA.", "2. IL MIO CONTRATTO FINISCE IL 31 DICEMBRE.",
                                 "3. HO 20 ANNI E L'AZIENDA MI INSEGNA IL MESTIERE.", "4. LAVORO 20 ORE ALLA SETTIMANA.",
                                 "5. MI HA ASSUNTO ADECCO, MA LAVORO IN UNA FABBRICA.", "6. IL MIO CONTRATTO NON HA UNA DATA DI FINE."]],
   "k": [eq(a) for a in ["A CHIAMATA", "A TEMPO DETERMINATO", "APPRENDISTATO", "PART-TIME", "CON L'AGENZIA (SOMMINISTRAZIONE)", "A TEMPO INDETERMINATO"]]},

  {"part": "Parlo"},
  {"id": "e9", "title": "9 🎤 · Il tuo colloquio", "type": "record",
   "cons": "Immagina di essere al colloquio. Registra le tue risposte.",
   "items": ["«BUONGIORNO. MI PARLI DI LEI.» (NOME, PAESE, CITTÀ, ESPERIENZE)", "«CHE ESPERIENZA HA? CHE COSA SA FARE?»",
             "«QUALI LINGUE PARLA? QUANDO PUÒ INIZIARE?»", "ADESSO TU FAI 2 DOMANDE AL DATORE DI LAVORO (ORARIO, CONTRATTO, STIPENDIO…)."]},
  {"part": "Adesso so fare…"},
  dict(AUTO, items=["prepararmi per un colloquio", "rispondere alle domande del colloquio", "fare domande sul lavoro e sul contratto",
                    "capire i tipi di contratto", "conoscere i miei diritti", "conoscere i miei doveri"]),
 ]
}

# ---------------------------------------------------------------- 5. BUSTA PAGA
BUSTA_INFO = ("<p><b>RISTORANTE «LA TAVOLA BLU» S.R.L. · BARI</b> (ESEMPIO INVENTATO)</p>"
              "<p>LAVORATORE: DIALLO AMARA · CAMERIERA, 4° LIVELLO</p><p>PERIODO: MAGGIO 2026 · CCNL TURISMO</p>"
              "<p>CONTRATTO: TEMPO INDETERMINATO · TEMPO PIENO · ORE LAVORATE: 168</p>"
              "<table><tr><td>PAGA BASE</td><td>1.412,51 €</td></tr><tr><td>CONTINGENZA</td><td>10,33 €</td></tr>"
              "<tr><td>STRAORDINARIO FESTIVO</td><td>67,80 €</td></tr><tr><th>TOTALE LORDO</th><th>1.490,64 €</th></tr>"
              "<tr><td>CONTRIBUTI INPS (9,19%)</td><td>− 136,99 €</td></tr><tr><td>IRPEF</td><td>− 98,40 €</td></tr>"
              "<tr><td>ADDIZIONALI REGIONALE E COMUNALE</td><td>− 12,50 €</td></tr><tr><th>NETTO DEL MESE</th><th>1.242,75 €</th></tr></table>"
              "<p>PAGAMENTO: BONIFICO BANCARIO</p>")

BUSTA = {
 "title": "💶 La busta paga · Esercizi",
 "store": "busta-paga",
 "upper": True,
 "sections": [
  {"part": "Le parole"},
  {"id": "e1", "title": "1 · Vero o falso?", "short": "1 · Vero o falso", "type": "choice", "opts": VF, "full": True,
   "items": [{"q": q} for q in ["1. LA BUSTA PAGA ARRIVA OGNI ANNO.", "2. LO STIPENDIO LORDO È PIÙ ALTO DELLO STIPENDIO NETTO.",
                                 "3. DOPO AVERLA LETTA, BUTTO LA BUSTA PAGA.", "4. L'INPS SI OCCUPA DI PENSIONI E PROTEZIONE DEI LAVORATORI.",
                                 "5. IL DATORE DI LAVORO PAGA SEMPRE IN CONTANTI, A MANO.", "6. LE TASSE TOLGONO SOLDI DALLO STIPENDIO LORDO.",
                                 "7. ANCHE CHI LAVORA PART-TIME RICEVE LA BUSTA PAGA."]],
   "k": vf("FVFVFVV")},
  {"id": "e2", "title": "2 · Collega la parola e il significato", "short": "2 · Le parole", "type": "select",
   "opts": ["PAGAMENTO CHE VA DA UNA BANCA A UN'ALTRA", "STIPENDIO PRIMA DELLE TASSE", "CHI TI PAGA PER LAVORARE", "STIPENDIO DOPO LE TASSE",
            "DOCUMENTO CON LE REGOLE DEL LAVORO", "ENTE PER PENSIONI E PROTEZIONE DEI LAVORATORI"],
   "items": [{"q": q} for q in ["1. LORDO", "2. NETTO", "3. INPS", "4. BONIFICO", "5. DATORE DI LAVORO", "6. CONTRATTO"]],
   "k": [eq(a) for a in ["STIPENDIO PRIMA DELLE TASSE", "STIPENDIO DOPO LE TASSE", "ENTE PER PENSIONI E PROTEZIONE DEI LAVORATORI",
                          "PAGAMENTO CHE VA DA UNA BANCA A UN'ALTRA", "CHI TI PAGA PER LAVORARE", "DOCUMENTO CON LE REGOLE DEL LAVORO"]]},
  {"id": "e3", "title": "3 · Completa le frasi", "short": "3 · Completa", "type": "text",
   "bank": "LORDO · NETTO · INPS · CONTRATTO · BONIFICO",
   "items": [{"q": q} for q in ["1. LO STIPENDIO PRIMA DELLE TASSE È LO STIPENDIO …", "2. LO STIPENDIO DOPO LE TASSE È LO STIPENDIO …",
                                 "3. L'ENTE CHE SI OCCUPA DELLE PENSIONI È L'…", "4. IL DOCUMENTO CON LE REGOLE DEL LAVORO È IL …",
                                 "5. I SOLDI VANNO DA UN CONTO A UN ALTRO CON UN …"]],
   "k": [eq("lordo"), eq("netto"), eq("inps", "l'inps"), eq("contratto"), eq("bonifico")]},
  {"id": "e4", "title": "4 · Scegli la risposta giusta", "short": "4 · Scegli", "type": "choice", "full": True,
   "items": [{"q": "1. LA BUSTA PAGA ARRIVA…", "opts": ["OGNI MESE", "OGNI ANNO", "UNA SOLA VOLTA"]},
             {"q": "2. LO STIPENDIO NETTO È…", "opts": ["PIÙ ALTO DEL LORDO", "PIÙ BASSO DEL LORDO", "UGUALE AL LORDO"]},
             {"q": "3. L'INPS SI OCCUPA DI…", "opts": ["AFFITTI", "PENSIONI E PROTEZIONE DEI LAVORATORI", "RISTORANTI"]},
             {"q": "4. CONSERVO LA BUSTA PAGA PERCHÉ…", "opts": ["SERVE PER I DOCUMENTI (PERMESSO, CASA…)", "NON SERVE A NIENTE", "È SOLO CARTA"]}],
   "k": [eq(a) for a in ["OGNI MESE", "PIÙ BASSO DEL LORDO", "PENSIONI E PROTEZIONE DEI LAVORATORI", "SERVE PER I DOCUMENTI (PERMESSO, CASA…)"]]},

  {"part": "Leggo una busta paga"},
  {"id": "bp", "title": "📋 La busta paga di Amara", "type": "info",
   "cons": "È un esempio inventato per la lezione. Leggi bene: ti serve per l'esercizio 5.", "info": BUSTA_INFO},
  {"id": "e5", "title": "5 · Osserva la busta paga e rispondi", "short": "5 · Osserva", "type": "text",
   "items": [{"q": q} for q in ["1. COME SI CHIAMA LA LAVORATRICE? (NOME)", "2. CHE LAVORO FA?", "3. QUAL È IL MESE?", "4. QUANTE ORE HA LAVORATO?",
                                 "5. QUANTO È IL TOTALE LORDO? (€)", "6. QUANTO PAGA DI CONTRIBUTI INPS? (€)", "7. QUANTO È IL NETTO? (€)",
                                 "8. COME RICEVE LO STIPENDIO?"]],
   "k": [has("amara"), has("camerier"), has("maggio"), has("168"), has("1490,64", "1.490,64"), has("136,99"), has("1242,75", "1.242,75"), has("bonifico")]},
  {"id": "e6", "title": "6 · Fai il calcolo", "short": "6 · Il calcolo", "type": "text", "w": "s",
   "cons": "Ricorda: NETTO = LORDO − TRATTENUTE (TASSE E CONTRIBUTI). Scrivi solo il numero.",
   "items": [{"q": q, "post": "€"} for q in ["1. LORDO 1.000 € · TRATTENUTE 200 € → NETTO", "2. LORDO 1.500 € · TRATTENUTE 300 € → NETTO",
                                              "3. NETTO 900 € · TRATTENUTE 150 € → LORDO"]],
   "k": [eq("800", "800 €", "800 euro"), eq("1200", "1.200", "1200 €", "1.200 €", "1200 euro"), eq("1050", "1.050", "1050 €", "1.050 €", "1050 euro")]},

  {"part": "Parlo"},
  {"id": "e7", "title": "7 🎤 · Una domanda sulla busta paga", "type": "record",
   "cons": "Guarda il dialogo di Amara nella presentazione. Poi registra le tue domande al datore di lavoro.",
   "items": ["Saluta con educazione e chiedi: «POSSO FARLE UNA DOMANDA SULLA MIA BUSTA PAGA?»",
             "Chiedi perché il netto è più basso del lordo e a che cosa servono i soldi dell'INPS.",
             "Ringrazia e saluta."]},
  {"part": "Adesso so fare…"},
  dict(AUTO, items=["capire le parole della busta paga", "spiegare la differenza tra lordo e netto", "trovare il netto, le ore e il mese in una busta paga",
                    "fare una domanda sulla busta paga al datore di lavoro"]),
 ]
}

# Nei menu le scelte vanno in ordine alfabetico: così l'ordine non suggerisce la risposta.
for _D, _ids in [(CHE_LAVORO, "e1 e2 e3"), (CERCARE, "e4"), (CV, "e1 e4"), (COLLOQUIO, "e4 e8")]:
    for _s in _D["sections"]:
        if _s.get("id") in _ids.split():
            _s["opts"] = sorted(_s["opts"])
