"""Eserciziario A1 in 19 schede (2026-10-30): Erila ha chiesto di inserire nel livello A1 l'«eserciziario extra online»
di Ornimi Editions (corso «Italiano anch'io»). Le schede originali sono PDF protetti da copyright: qui si riprendono
solo gli ARGOMENTI di ogni unità (lessico + grammatica); tutte le frasi e gli esercizi sono scritti per il sito.
Pagine in eserciziario-a1/scheda-NN.html, tutto in STAMPATELLO MAIUSCOLO."""
from genera import eq
from unita_drive import vf, scegli, menu, scrivi, ordina, completa, parla, libero

def scheda(n, titolo, store_sfx, sections):
    return {"title": "📒 Scheda %d · %s" % (n, titolo), "store": "eserciziario-%02d" % n, "upper": True,
            "sub": "ESERCIZIARIO A1 · SCHEDA %d DI 19" % n, "sections": sections}

SCHEDE = []

# 1 · saluti, presentarsi, essere/avere, numeri
SCHEDE.append(scheda(1, "Mi presento", "", [
  {"part": "Saluti e presentazioni"},
  menu(["BUONGIORNO!", "BUONANOTTE!", "CIAO!", "ARRIVEDERCI!"],
       [("1. SONO LE 9 DI MATTINA. ENTRI IN UN UFFICIO.", "BUONGIORNO!"), ("2. VAI A DORMIRE.", "BUONANOTTE!"),
        ("3. INCONTRI UN AMICO PER STRADA.", "CIAO!"), ("4. ESCI DAL NEGOZIO.", "ARRIVEDERCI!")], "1 · Che cosa dici?", "1 · I saluti", "e1"),
  vf(["1. KOFI È DEL GHANA.", "2. KOFI HA 30 ANNI.", "3. KOFI LAVORA IN UN RISTORANTE.", "4. KOFI HA DUE FIGLI."],
     ["VERO", "FALSO", "VERO", "FALSO"], "2 · Leggi: vero o falso?", "2 · Kofi", "e2",
     info="CIAO! MI CHIAMO KOFI. SONO DEL GHANA, DI ACCRA. HO 26 ANNI. ABITO A BARI E LAVORO IN UN RISTORANTE. HO UNA FIGLIA, AMA."),
  {"part": "Essere e avere"},
  menu(["SONO", "SEI", "È", "HO", "HAI", "HA"],
       [("1. IO ___ DEL MAROCCO.", "SONO"), ("2. TU ___ 20 ANNI?", "HAI"), ("3. LEI ___ MARIAM.", "È"), ("4. IO ___ DUE FRATELLI.", "HO"),
        ("5. TU ___ ITALIANO?", "SEI"), ("6. LUI ___ UN FIGLIO.", "HA")], "3 · Essere o avere?", "3 · Essere o avere", "e3"),
  menu(["DA", "DAL", "DALLA", "DALL'"],
       [("1. VENGO ___ SENEGAL.", "DAL"), ("2. VENGO ___ NIGERIA.", "DALLA"), ("3. VENGO ___ AFGHANISTAN.", "DALL'"), ("4. VENGO ___ BARI.", "DA")],
       "4 · Da dove vieni?", "4 · Da dove", "e4"),
  {"part": "I numeri"},
  scrivi([("1. 7", ["sette"]), ("2. 12", ["dodici"]), ("3. 18", ["diciotto"]), ("4. 25", ["venticinque"]), ("5. 40", ["quaranta"]),
          ("6. 100", ["cento"])], "5 · Scrivi il numero in lettere", "5 · I numeri", "e5"),
  scrivi([("1. TRENTATRÉ", ["33"]), ("2. SESSANTOTTO", ["68"]), ("3. NOVANTA", ["90"]), ("4. DUECENTO", ["200"]), ("5. MILLE", ["1000", "1.000"])],
         "6 · Scrivi il numero in cifre", "6 · In cifre", "e6", w="s"),
  parla("e7", 7, "PRESENTATI: NOME, PAESE, ETÀ, DOVE ABITI, CHE LAVORO FAI."),
]))

# 2 · descrivere una persona, aggettivi, accordo, negazione
SCHEDE.append(scheda(2, "Com'è?", "", [
  {"part": "Descrivere"},
  menu(["CAPELLI", "OCCHI"], [("1. ___ RICCI", "CAPELLI"), ("2. ___ AZZURRI", "OCCHI"), ("3. ___ BIONDI", "CAPELLI"), ("4. ___ VERDI", "OCCHI"),
                              ("5. ___ LUNGHI", "CAPELLI"), ("6. ___ CASTANI", "OCCHI")], "1 · Capelli o occhi?", "1 · Capelli e occhi", "e1"),
  scegli([("1. LUCIA È ___.", ["ALTA", "ALTO", "ALTI"], "ALTA"), ("2. I BAMBINI SONO ___.", ["SIMPATICI", "SIMPATICO", "SIMPATICHE"], "SIMPATICI"),
          ("3. MARCO HA I CAPELLI ___.", ["NERI", "NERO", "NERA"], "NERI"), ("4. LE RAGAZZE SONO ___.", ["GENTILI", "GENTILE", "GENTILA"], "GENTILI"),
          ("5. AHMED È ___.", ["MAGRO", "MAGRA", "MAGRE"], "MAGRO")], "2 · Scegli l'aggettivo giusto", "2 · L'accordo", "e2"),
  scrivi([("1. UN RAGAZZO ALTO → DUE RAGAZZI ___", ["alti"]), ("2. UNA DONNA BELLA → DUE DONNE ___", ["belle"]),
          ("3. UN AMICO SIMPATICO → DUE AMICI ___", ["simpatici"]), ("4. UNA BAMBINA ALLEGRA → DUE BAMBINE ___", ["allegre"]),
          ("5. UN UOMO GENTILE → DUE UOMINI ___", ["gentili"])], "3 · Scrivi il plurale", "3 · Il plurale", "e3"),
  {"part": "La frase negativa"},
  scrivi([("1. SONO STANCO. → NON ___", ["sono stanco"]), ("2. HO FAME. → NON ___", ["ho fame"]),
          ("3. LUI È ALTO. → LUI NON ___", ["e alto"]), ("4. ABBIAMO LA MACCHINA. → NON ___", ["abbiamo la macchina"])],
         "4 · Scrivi la frase negativa", "4 · Non", "e4", w="l"),
  completa("MIA SORELL___ SI CHIAMA NOOR. È ALT___ E MAGR___. HA I CAPELLI LUNGH___ E GLI OCCHI NER___. È UNA RAGAZZA MOLTO SIMPATIC___.",
           ["a", "a", "a", "i", "i", "a"], "5 · Completa le parole", "5 · Le vocali", "e5", "A · I", cons="SCRIVI LA VOCALE FINALE: A O I."),
  libero("e6", 6, "Una persona", "DESCRIVI UNA PERSONA DELLA TUA FAMIGLIA: COM'È? (4 FRASI)", ["LA PERSONA"], rows=4),
]))

# 3 · la scuola, articoli, c'è / ci sono
SCHEDE.append(scheda(3, "In classe", "", [
  {"part": "Le parole della scuola"},
  scegli([("1. QUAL È L'INTRUSO?", ["LA PENNA", "LA MATITA", "LA GOMMA", "LA BANANA"], "LA BANANA"),
          ("2. QUAL È L'INTRUSO?", ["LUNEDÌ", "MARTEDÌ", "GENNAIO", "VENERDÌ"], "GENNAIO"),
          ("3. QUAL È L'INTRUSO?", ["L'INSEGNANTE", "LO STUDENTE", "LA LAVAGNA", "LA COMPAGNA"], "LA LAVAGNA"),
          ("4. QUAL È L'INTRUSO?", ["IL QUADERNO", "IL LIBRO", "IL DIZIONARIO", "IL LETTO"], "IL LETTO")], "1 · Trova l'intruso", "1 · L'intruso", "e1"),
  {"part": "Gli articoli"},
  menu(["IL", "LO", "LA", "L'", "I", "GLI", "LE"],
       [("1. ___ QUADERNO", "IL"), ("2. ___ ZAINO", "LO"), ("3. ___ SEDIA", "LA"), ("4. ___ ASTUCCIO", "L'"), ("5. ___ LIBRI", "I"),
        ("6. ___ STUDENTI", "GLI"), ("7. ___ PENNE", "LE"), ("8. ___ INSEGNANTE", "L'")], "2 · L'articolo determinativo", "2 · Il, lo, la", "e2"),
  menu(["UN", "UNO", "UNA", "UN'"],
       [("1. ___ BANCO", "UN"), ("2. ___ STUDENTE", "UNO"), ("3. ___ FINESTRA", "UNA"), ("4. ___ AULA", "UN'"), ("5. ___ ARMADIO", "UN"), ("6. ___ GOMMA", "UNA")],
       "3 · L'articolo indeterminativo", "3 · Un, uno, una", "e3"),
  {"part": "C'è / ci sono"},
  menu(["C'È", "CI SONO"], [("1. IN CLASSE ___ UNA LAVAGNA.", "C'È"), ("2. ___ 15 STUDENTI.", "CI SONO"), ("3. SUL BANCO ___ DUE LIBRI.", "CI SONO"),
                             ("4. ___ L'INSEGNANTE?", "C'È"), ("5. NELLO ZAINO ___ LE PENNE.", "CI SONO")], "4 · C'è o ci sono?", "4 · C'è / ci sono", "e4"),
  scrivi([("1. IL LIBRI SONO SUL BANCO.", ["i libri sono sul banco"]), ("2. C'È TRE SEDIE.", ["ci sono tre sedie"]),
          ("3. LA ZAINO È NERO.", ["lo zaino e nero"])], "5 · Correggi l'errore", "5 · Correggi", "e5", cons="C'È UN ERRORE. RISCRIVI LA FRASE GIUSTA.", w="l"),
  libero("e6", 6, "La mia classe", "CHE COSA C'È NELLA TUA CLASSE? SCRIVI 4 FRASI CON C'È E CI SONO.", ["LA MIA CLASSE"], rows=4),
]))

# 4 · lavori, attività quotidiane, fare, presente
SCHEDE.append(scheda(4, "Che lavoro fai?", "", [
  {"part": "I lavori"},
  scrivi([("1. RIA - CA - ME - RE → LA ___", ["cameriera"]), ("2. NI - CO - MEC - CA → IL ___", ["meccanico"]),
          ("3. MIE - RE - FER - IN → L'___", ["infermiere"]), ("4. DI - CUO - CO → IL ___", ["cuoco"])], "1 · Metti in ordine le sillabe", "1 · Le sillabe", "e1"),
  menu(["IL MECCANICO", "L'INFERMIERA", "IL CUOCO", "LA COMMESSA", "IL MURATORE"],
       [("1. LAVORA IN OSPEDALE.", "L'INFERMIERA"), ("2. RIPARA LE MACCHINE.", "IL MECCANICO"), ("3. LAVORA IN CUCINA.", "IL CUOCO"),
        ("4. VENDE I VESTITI IN UN NEGOZIO.", "LA COMMESSA"), ("5. COSTRUISCE LE CASE.", "IL MURATORE")], "2 · Chi è?", "2 · Chi è", "e2"),
  {"part": "Il verbo fare"},
  menu(["FACCIO", "FAI", "FA", "FACCIAMO", "FATE", "FANNO"],
       [("1. IO ___ COLAZIONE ALLE 7.", "FACCIO"), ("2. TU CHE LAVORO ___?", "FAI"), ("3. LEI ___ LA SPESA.", "FA"),
        ("4. NOI ___ SPORT IL SABATO.", "FACCIAMO"), ("5. VOI ___ LE PULIZIE?", "FATE"), ("6. LORO ___ UNA PAUSA.", "FANNO")], "3 · Il verbo fare", "3 · Fare", "e3"),
  scrivi([("1. IO (LAVORARE) ___ IN UN BAR.", ["lavoro"]), ("2. TU (PRENDERE) ___ L'AUTOBUS?", ["prendi"]), ("3. LUI (DORMIRE) ___ POCO.", ["dorme"]),
          ("4. NOI (ANDARE) ___ AL LAVORO.", ["andiamo"]), ("5. LORO (FINIRE) ___ ALLE 6.", ["finiscono"])], "4 · Il presente", "4 · Il presente", "e4"),
  vf(["1. OMAR FA IL CUOCO.", "2. COMINCIA A LAVORARE LA MATTINA PRESTO.", "3. IL LUNEDÌ NON LAVORA.", "4. LA SERA FA SPORT."],
     ["FALSO", "FALSO", "VERO", "FALSO"], "5 · Leggi: vero o falso?", "5 · Omar", "e5",
     info="OMAR FA IL CAMERIERE IN UNA PIZZERIA. COMINCIA A LAVORARE ALLE 6 DI SERA E FINISCE A MEZZANOTTE. IL LUNEDÌ È IL SUO GIORNO LIBERO: "
          "LA MATTINA FA LA SPESA, IL POMERIGGIO GIOCA A CALCIO CON GLI AMICI."),
  parla("e6", 6, "CHE LAVORO FAI O CHE LAVORO VUOI FARE? DOVE? A CHE ORA COMINCI E FINISCI?"),
]))

# 5 · tempo, stagioni, mesi, verbi irregolari, proporre/accettare/rifiutare
SCHEDE.append(scheda(5, "Che tempo fa? Usciamo?", "", [
  {"part": "Stagioni e mesi"},
  menu(["PRIMAVERA", "ESTATE", "AUTUNNO", "INVERNO"],
       [("1. GENNAIO", "INVERNO"), ("2. LUGLIO", "ESTATE"), ("3. APRILE", "PRIMAVERA"), ("4. OTTOBRE", "AUTUNNO"), ("5. AGOSTO", "ESTATE"), ("6. DICEMBRE", "INVERNO")],
       "1 · Che stagione è?", "1 · Le stagioni", "e1"),
  scrivi([("1. O - N - S - E → IL S___ (☀️)", ["sole"]), ("2. G - P - I - A - O - G - I → LA ___ (🌧️)", ["pioggia"]),
          ("3. T - V - E - N - O → IL ___ (💨)", ["vento"]), ("4. E - V - N - E → LA ___ (❄️)", ["neve"])], "2 · Riordina le lettere", "2 · Il tempo", "e2"),
  {"part": "Andare, venire, uscire, stare"},
  scegli([("1. STASERA ___ CON GLI AMICI.", ["ESCO", "USCIO", "ESCI"], "ESCO"), ("2. TU ___ ALLA FESTA?", ["VIENI", "VENI", "VIENE"], "VIENI"),
          ("3. NOI ___ AL MARE.", ["ANDIAMO", "ANDAMO", "VANNO"], "ANDIAMO"), ("4. COME ___ TUA MADRE?", ["STA", "STAI", "STANNO"], "STA"),
          ("5. I RAGAZZI ___ ALLE 8.", ["ESCONO", "USCIANO", "ESCANO"], "ESCONO")], "3 · Scegli il verbo giusto", "3 · I verbi", "e3"),
  {"part": "Proporre"},
  menu(["PROPONGO", "ACCETTO", "RIFIUTO"],
       [("1. TI VA DI ANDARE AL PARCO?", "PROPONGO"), ("2. VOLENTIERI!", "ACCETTO"), ("3. MI DISPIACE, NON POSSO.", "RIFIUTO"),
        ("4. PERCHÉ NON ANDIAMO AL CINEMA?", "PROPONGO"), ("5. VA BENE, A CHE ORA?", "ACCETTO"), ("6. NO, GRAZIE, OGGI SONO STANCO.", "RIFIUTO")],
       "4 · Proponi, accetti o rifiuti?", "4 · Proporre", "e4"),
  completa("SARA: CIAO! CHE ___ OGGI?<br>ALI: FA BEL ___ E C'È IL SOLE.<br>SARA: TI ___ DI ANDARE AL MARE?<br>ALI: SÌ, ___! A CHE ORA?<br>SARA: ALLE 3. VIENI A CASA MIA.",
           ["tempo fa", "tempo", "va", "volentieri"], "5 · Completa il dialogo", "5 · Il dialogo", "e5", "TEMPO FA · TEMPO · VA · VOLENTIERI"),
]))

# 6 · casa, ordinali, preposizioni di luogo, faccende
SCHEDE.append(scheda(6, "La mia casa", "", [
  {"part": "Le stanze e i mobili"},
  menu(["LA CUCINA", "IL BAGNO", "LA CAMERA DA LETTO", "IL SOGGIORNO"],
       [("1. IL LETTO", "LA CAMERA DA LETTO"), ("2. LA DOCCIA", "IL BAGNO"), ("3. IL FORNO", "LA CUCINA"), ("4. IL DIVANO", "IL SOGGIORNO"),
        ("5. L'ARMADIO", "LA CAMERA DA LETTO"), ("6. IL FRIGORIFERO", "LA CUCINA")], "1 · In che stanza?", "1 · Le stanze", "e1"),
  {"part": "I numeri ordinali"},
  scrivi([("1. 1° → IL ___ PIANO", ["primo"]), ("2. 2° → IL ___ PIANO", ["secondo"]), ("3. 3° → IL ___ PIANO", ["terzo"]),
          ("4. 5° → IL ___ PIANO", ["quinto"]), ("5. 10° → IL ___ PIANO", ["decimo"])], "2 · A che piano abiti?", "2 · Gli ordinali", "e2"),
  {"part": "Dov'è?"},
  menu(["SOPRA", "SOTTO", "DAVANTI AL", "DIETRO LA", "ACCANTO AL"],
       [("1. IL GATTO È ___ LETTO: NON SI VEDE!", "SOTTO"), ("2. LA LAMPADA È ___ TAVOLO.", "SOPRA"), ("3. LA TV È ___ DIVANO: LA GUARDO SEDUTO.", "DAVANTI AL"),
        ("4. LA SCOPA È ___ PORTA.", "DIETRO LA"), ("5. IL FRIGORIFERO È ___ FORNO.", "ACCANTO AL")], "3 · Dov'è?", "3 · Le preposizioni", "e3"),
  {"part": "I lavori di casa"},
  scrivi([("1. IO (PULIRE) ___ IL BAGNO.", ["pulisco"]), ("2. MIA MOGLIE (LAVARE) ___ I PIATTI.", ["lava"]), ("3. NOI (FARE) ___ IL LETTO.", ["facciamo"]),
          ("4. I BAMBINI (METTERE) ___ IN ORDINE.", ["mettono"]), ("5. TU (STIRARE) ___ LE CAMICIE?", ["stiri"])], "4 · Chi fa che cosa?", "4 · I lavori", "e4"),
  vf(["1. LA CASA DI ROSA È AL TERZO PIANO.", "2. HA DUE CAMERE DA LETTO.", "3. IL BAGNO È GRANDE.", "4. C'È UN BALCONE."],
     ["FALSO", "VERO", "FALSO", "VERO"], "5 · Leggi: vero o falso?", "5 · La casa di Rosa", "e5",
     info="ROSA ABITA AL QUINTO PIANO. LA SUA CASA HA UNA CUCINA, UN SOGGIORNO, DUE CAMERE DA LETTO E UN BAGNO PICCOLO. DAL SOGGIORNO SI ESCE SU UN BALCONE CON TANTE PIANTE."),
  libero("e6", 6, "La mia casa", "DESCRIVI LA TUA CASA: A CHE PIANO È? QUANTE STANZE CI SONO? CHE COSA C'È IN CUCINA?", ["LA MIA CASA"], rows=4),
]))

# 7 · famiglia, possessivi, quanto
SCHEDE.append(scheda(7, "La mia famiglia", "", [
  {"part": "La famiglia"},
  menu(["LA NONNA", "LO ZIO", "IL NIPOTE", "LA COGNATA", "LA SUOCERA"],
       [("1. LA MADRE DI MIA MADRE", "LA NONNA"), ("2. IL FRATELLO DI MIO PADRE", "LO ZIO"), ("3. IL FIGLIO DI MIO FIGLIO", "IL NIPOTE"),
        ("4. LA SORELLA DI MIO MARITO", "LA COGNATA"), ("5. LA MADRE DI MIA MOGLIE", "LA SUOCERA")], "1 · Chi è?", "1 · La famiglia", "e1"),
  {"part": "I possessivi"},
  scegli([("1. ___ MADRE SI CHIAMA FATIMA.", ["MIA", "LA MIA", "MIO"], "MIA"), ("2. ___ FRATELLI ABITANO IN FRANCIA.", ["I MIEI", "MIEI", "LE MIE"], "I MIEI"),
          ("3. COME SI CHIAMA ___ PADRE?", ["TUO", "IL TUO", "TUA"], "TUO"), ("4. ___ FIGLIE VANNO A SCUOLA.", ["LE SUE", "SUE", "I SUOI"], "LE SUE"),
          ("5. ___ CASA È GRANDE.", ["LA NOSTRA", "NOSTRA", "IL NOSTRO"], "LA NOSTRA")], "2 · Scegli il possessivo", "2 · I possessivi", "e2"),
  scrivi([("1. MIO FRATELLO → I ___", ["miei fratelli"]), ("2. MIA SORELLA → LE ___", ["mie sorelle"]), ("3. TUO CUGINO → I ___", ["tuoi cugini"]),
          ("4. SUA ZIA → LE ___", ["sue zie"])], "3 · Scrivi il plurale", "3 · Il plurale", "e3", w="m"),
  {"part": "Quanto?"},
  menu(["QUANTO", "QUANTA", "QUANTI", "QUANTE"],
       [("1. ___ FRATELLI HAI?", "QUANTI"), ("2. ___ SORELLE HAI?", "QUANTE"), ("3. ___ ACQUA BEVI?", "QUANTA"), ("4. ___ TEMPO HAI?", "QUANTO"), ("5. ___ ANNI HA TUO FIGLIO?", "QUANTI")],
       "4 · Quanto, quanta, quanti, quante?", "4 · Quanto", "e4"),
  libero("e5", 5, "La mia famiglia", "PARLA DELLA TUA FAMIGLIA: QUANTI SIETE? COME SI CHIAMANO? DOVE ABITANO?", ["LA MIA FAMIGLIA"], rows=4),
]))

# 8 · cibi, pasti, negozi, mangiare/bere/preferire, piacere
SCHEDE.append(scheda(8, "A tavola", "", [
  {"part": "I negozi"},
  menu(["DAL PANETTIERE", "DAL MACELLAIO", "DAL PESCIVENDOLO", "DAL FRUTTIVENDOLO"],
       [("1. IL PANE", "DAL PANETTIERE"), ("2. LE COZZE", "DAL PESCIVENDOLO"), ("3. LA CARNE MACINATA", "DAL MACELLAIO"), ("4. LE MELE", "DAL FRUTTIVENDOLO"),
        ("5. LA FOCACCIA", "DAL PANETTIERE"), ("6. L'ORATA", "DAL PESCIVENDOLO")], "1 · Dove lo compro?", "1 · I negozi", "e1"),
  menu(["COLAZIONE", "PRANZO", "CENA"], [("1. ALLE 7 DI MATTINA", "COLAZIONE"), ("2. ALL'UNA", "PRANZO"), ("3. ALLE 8 DI SERA", "CENA"), ("4. CAPPUCCINO E CORNETTO", "COLAZIONE")],
       "2 · Che pasto è?", "2 · I pasti", "e2"),
  {"part": "Mangiare, bere, preferire"},
  scrivi([("1. IO (BERE) ___ IL TÈ.", ["bevo"]), ("2. NOI (MANGIARE) ___ ALLE 8.", ["mangiamo"]), ("3. TU (PREFERIRE) ___ IL CAFFÈ O IL TÈ?", ["preferisci"]),
          ("4. LORO (BERE) ___ ACQUA.", ["bevono"]), ("5. LEI (PREFERIRE) ___ IL PESCE.", ["preferisce"])], "3 · Scrivi il verbo", "3 · I verbi", "e3"),
  menu(["MI PIACE", "MI PIACCIONO"], [("1. ___ LA PIZZA.", "MI PIACE"), ("2. ___ LE ARANCE.", "MI PIACCIONO"), ("3. ___ BERE IL TÈ.", "MI PIACE"),
                                       ("4. ___ GLI SPAGHETTI.", "MI PIACCIONO"), ("5. NON ___ IL PEPERONCINO.", "MI PIACE")], "4 · Piace o piacciono?", "4 · Piacere", "e4"),
  vf(["1. LA MATTINA AMINA BEVE IL CAFFÈ.", "2. A PRANZO MANGIA IL RISO.", "3. LE PIACE LA CARNE.", "4. LA SERA MANGIA IL PESCE."],
     ["FALSO", "VERO", "FALSO", "VERO"], "5 · Leggi: vero o falso?", "5 · I pasti di Amina", "e5",
     info="LA MATTINA AMINA BEVE UN TÈ CON IL LATTE E MANGIA PANE E MARMELLATA. A PRANZO MANGIA RISO CON LE VERDURE: NON LE PIACE LA CARNE. LA SERA PREFERISCE IL PESCE."),
  parla("e6", 6, "CHE COSA MANGI E BEVI DI SOLITO A COLAZIONE, A PRANZO E A CENA? CHE COSA TI PIACE?"),
]))

# 9 · routine, ora, riflessivi, avverbi di frequenza
SCHEDE.append(scheda(9, "La mia giornata", "", [
  {"part": "I verbi riflessivi"},
  menu(["MI", "TI", "SI", "CI", "VI"],
       [("1. IO ___ SVEGLIO ALLE 6.", "MI"), ("2. TU ___ LAVI I DENTI.", "TI"), ("3. LEI ___ TRUCCA.", "SI"), ("4. NOI ___ VESTIAMO.", "CI"),
        ("5. VOI ___ RIPOSATE.", "VI"), ("6. LORO ___ ADDORMENTANO TARDI.", "SI")], "1 · Mi, ti, si…", "1 · I riflessivi", "e1"),
  scrivi([("1. IO (ALZARSI) ___ ALLE 7.", ["mi alzo"]), ("2. LUI (FARSI) ___ LA DOCCIA.", ["si fa"]), ("3. NOI (VESTIRSI) ___ IN FRETTA.", ["ci vestiamo"]),
          ("4. TU (PETTINARSI) ___?", ["ti pettini"])], "2 · Scrivi il verbo", "2 · Coniuga", "e2", w="m"),
  {"part": "L'ora"},
  scrivi([("1. 7:00 → SONO LE ___", ["sette"]), ("2. 8:30 → SONO LE OTTO E ___", ["mezza", "trenta"]), ("3. 1:00 → È ___", ["l'una", "luna"]),
          ("4. 9:15 → SONO LE NOVE E UN ___", ["quarto"])], "3 · Che ore sono?", "3 · L'ora", "e3"),
  {"part": "Sempre, spesso, mai"},
  ordina(["LA DOMENICA", "MI", "ALZO", "SEMPRE", "TARDI"], "4 · Metti in ordine la frase", "4 · La frase", "e4",
         cons="METTI LE PAROLE IN ORDINE: 1, 2, 3… (LA DOMENICA … TARDI)"),
  scegli([("1. QUAL È GIUSTA?", ["NON FACCIO MAI COLAZIONE.", "MAI FACCIO NON COLAZIONE.", "NON MAI FACCIO COLAZIONE."], "NON FACCIO MAI COLAZIONE."),
          ("2. QUAL È GIUSTA?", ["VADO SPESSO IN PALESTRA.", "SPESSO VADO IN SPESSO PALESTRA.", "VADO IN SPESSO PALESTRA."], "VADO SPESSO IN PALESTRA.")],
         "5 · La frase giusta", "5 · Gli avverbi", "e5"),
  libero("e6", 6, "La mia giornata", "RACCONTA LA TUA GIORNATA CON L'ORA: A CHE ORA TI SVEGLI, TI ALZI, MANGI, VAI A DORMIRE?", ["LA MIA GIORNATA"], rows=5),
]))

# 10 · colori e vestiti, accordo, ordine della frase
SCHEDE.append(scheda(10, "Vestiti e colori", "", [
  {"part": "I vestiti"},
  scrivi([("1. GLIA - MA → LA ___", ["maglia"]), ("2. LO - NI - TA - PAN → I ___", ["pantaloni"]), ("3. CIA - CA - MI → LA ___", ["camicia"]),
          ("4. PE - SCAR → LE ___", ["scarpe"])], "1 · Metti in ordine le sillabe", "1 · Le sillabe", "e1"),
  scegli([("1. LA GIACCA ___", ["NERA", "NERO", "NERI"], "NERA"), ("2. I PANTALONI ___", ["BIANCHI", "BIANCO", "BIANCHE"], "BIANCHI"),
          ("3. LE SCARPE ___", ["ROSSE", "ROSSI", "ROSSA"], "ROSSE"), ("4. IL CAPPOTTO ___", ["GRIGIO", "GRIGIA", "GRIGI"], "GRIGIO"),
          ("5. LE GONNE ___", ["VERDI", "VERDE", "VERDA"], "VERDI")], "2 · Il colore giusto", "2 · I colori", "e2"),
  {"part": "La frase"},
  ordina(["OGGI", "MARIA", "PORTA", "UNA", "GONNA", "BLU"], "3 · Metti in ordine la frase", "3 · In ordine", "e3"),
  ordina(["D'INVERNO", "IO", "METTO", "IL", "CAPPOTTO", "PESANTE"], "4 · Metti in ordine la frase", "4 · In ordine", "e4"),
  completa("OGGI FA FREDDO. METTO UN MAGLIONE ROSS___, I PANTALONI NER___, LE SCARPE MARRONI E UNA SCIARPA GIALL___.",
           ["o", "i", "a"], "5 · Completa", "5 · Completa", "e5", "A · I · O", cons="SCRIVI LA VOCALE FINALE."),
  parla("e6", 6, "CHE COSA PORTI OGGI? DESCRIVI I TUOI VESTITI E I COLORI."),
]))

# 11 · città, dovere/andare, preposizioni, ci vuole
SCHEDE.append(scheda(11, "In città", "", [
  {"part": "I luoghi"},
  menu(["ALLA STAZIONE", "IN QUESTURA", "AL DISTRIBUTORE", "ALLA FERMATA", "ALL'AEROPORTO"],
       [("1. DEVO PRENDERE IL TRENO: VADO ___", "ALLA STAZIONE"), ("2. DEVO RINNOVARE IL PERMESSO DI SOGGIORNO: VADO ___", "IN QUESTURA"),
        ("3. LA MACCHINA NON HA BENZINA: VADO ___", "AL DISTRIBUTORE"), ("4. ASPETTO L'AUTOBUS ___", "ALLA FERMATA"),
        ("5. PRENDO L'AEREO: VADO ___", "ALL'AEROPORTO")], "1 · Dove vai?", "1 · I luoghi", "e1"),
  {"part": "Dovere e andare"},
  menu(["DEVO", "DEVI", "DEVE", "DOBBIAMO", "DEVONO"],
       [("1. IO ___ ANDARE IN BANCA.", "DEVO"), ("2. TU ___ STUDIARE.", "DEVI"), ("3. LUI ___ LAVORARE.", "DEVE"), ("4. NOI ___ PARTIRE.", "DOBBIAMO"), ("5. LORO ___ PAGARE.", "DEVONO")],
       "2 · Il verbo dovere", "2 · Dovere", "e2"),
  menu(["A", "IN", "AL", "ALLA", "DAL", "DALLA"],
       [("1. VADO ___ FARMACIA.", "IN"), ("2. VADO ___ BARI.", "A"), ("3. VADO ___ MEDICO.", "DAL"), ("4. VADO ___ SUPERMERCATO.", "AL"),
        ("5. VADO ___ POSTA.", "ALLA"), ("6. VADO ___ PARRUCCHIERA.", "DALLA")], "3 · La preposizione giusta", "3 · Le preposizioni", "e3"),
  {"part": "Ci vuole / ci vogliono"},
  menu(["CI VUOLE", "CI VOGLIONO"], [("1. PER ANDARE IN STAZIONE ___ MEZZ'ORA.", "CI VUOLE"), ("2. DA BARI A ROMA ___ 4 ORE.", "CI VOGLIONO"),
                                     ("3. A PIEDI ___ 10 MINUTI.", "CI VOGLIONO"), ("4. IN AUTOBUS ___ UN'ORA.", "CI VUOLE")], "4 · Quanto tempo ci vuole?", "4 · Ci vuole", "e4"),
  parla("e5", 5, "DESCRIVI IL TUO QUARTIERE: CHE COSA C'È? QUANTO TEMPO CI VUOLE PER ANDARE IN CENTRO?"),
]))

# 12 · trasporti, treno, partire/potere/volere, preposizioni
SCHEDE.append(scheda(12, "In viaggio", "", [
  {"part": "I mezzi"},
  scegli([("1. QUAL È L'INTRUSO?", ["IL TRENO", "L'AUTOBUS", "LA METRO", "IL BINARIO"], "IL BINARIO"),
          ("2. QUAL È L'INTRUSO?", ["IL BIGLIETTO", "L'ABBONAMENTO", "LA VALIGIA", "LA CARTA D'IMBARCO"], "LA VALIGIA"),
          ("3. QUAL È L'INTRUSO?", ["PARTIRE", "ARRIVARE", "DORMIRE", "SCENDERE"], "DORMIRE")], "1 · Trova l'intruso", "1 · L'intruso", "e1"),
  {"part": "Partire, potere, volere"},
  scrivi([("1. IL TRENO (PARTIRE) ___ ALLE 10.", ["parte"]), ("2. IO (VOLERE) ___ UN BIGLIETTO PER LECCE.", ["voglio"]),
          ("3. (POTERE) ___ PAGARE CON LA CARTA? (IO)", ["posso"]), ("4. NOI (VOLERE) ___ VIAGGIARE IN TRENO.", ["vogliamo"]),
          ("5. I TRENI (PARTIRE) ___ DAL BINARIO 2.", ["partono"]), ("6. TU (POTERE) ___ VENIRE?", ["puoi"])], "2 · Scrivi il verbo", "2 · I verbi", "e2"),
  menu(["A", "DA", "IN", "PER"], [("1. IL TRENO ___ FOGGIA PARTE ALLE 9.", "PER"), ("2. ARRIVO ___ MILANO ALLE 18.", "A"), ("3. VIAGGIO ___ TRENO.", "IN"),
                                   ("4. PARTO ___ BARI.", "DA"), ("5. VADO ___ GERMANIA.", "IN")], "3 · A, da, in, per?", "3 · Le preposizioni", "e3"),
  vf(["1. SAMIR VUOLE ANDARE A ROMA.", "2. IL TRENO PARTE ALLE 7:40.", "3. COMPRA UN BIGLIETTO DI ANDATA E RITORNO.", "4. PAGA CON LA CARTA."],
     ["FALSO", "VERO", "FALSO", "VERO"], "4 · Leggi: vero o falso?", "4 · Alla biglietteria", "e4",
     info="SAMIR: BUONGIORNO, VORREI UN BIGLIETTO PER NAPOLI.<br>IMPIEGATA: SOLO ANDATA?<br>SAMIR: SÌ, SOLO ANDATA. A CHE ORA PARTE IL TRENO?<br>"
          "IMPIEGATA: ALLE 7 E 40 DAL BINARIO 3. SONO 35 EURO.<br>SAMIR: POSSO PAGARE CON LA CARTA?<br>IMPIEGATA: CERTO."),
  parla("e5", 5, "SEI ALLA BIGLIETTERIA. CHIEDI UN BIGLIETTO, L'ORARIO, IL BINARIO E IL PREZZO."),
]))

# 13 · salute, fare male
SCHEDE.append(scheda(13, "Dal medico", "", [
  {"part": "Il corpo e i sintomi"},
  menu(["MI FA MALE", "MI FANNO MALE"], [("1. ___ LA TESTA.", "MI FA MALE"), ("2. ___ I DENTI.", "MI FANNO MALE"), ("3. ___ LO STOMACO.", "MI FA MALE"),
                                         ("4. ___ LE GAMBE.", "MI FANNO MALE"), ("5. ___ LA GOLA.", "MI FA MALE"), ("6. ___ GLI OCCHI.", "MI FANNO MALE")],
       "1 · Fa male o fanno male?", "1 · Fare male", "e1"),
  menu(["LA BENDA", "LA POMATA", "IL TERMOMETRO", "LO SCIROPPO", "IL CEROTTO"],
       [("1. HO UN PICCOLO TAGLIO SUL DITO.", "IL CEROTTO"), ("2. VOGLIO SAPERE SE HO LA FEBBRE.", "IL TERMOMETRO"), ("3. HO LA TOSSE.", "LO SCIROPPO"),
        ("4. HO LA PELLE ROSSA E SECCA.", "LA POMATA"), ("5. MI SONO FATTO MALE AL BRACCIO.", "LA BENDA")], "2 · Che cosa serve?", "2 · Le medicine", "e2"),
  completa("MEDICO: BUONGIORNO, CHE COSA SI SENTE?<br>PAZIENTE: HO LA ___ A 38 E MI FA MALE LA ___.<br>MEDICO: HA ANCHE LA TOSSE?<br>"
           "PAZIENTE: SÌ, SOPRATTUTTO LA ___.<br>MEDICO: PRENDA QUESTO ___ TRE VOLTE AL GIORNO E STIA A LETTO.",
           ["febbre", "gola", "notte", "sciroppo"], "3 · Completa il dialogo", "3 · Dal medico", "e3", "FEBBRE · GOLA · NOTTE · SCIROPPO"),
  vf(["1. SE HO UN'EMERGENZA CHIAMO IL 112.", "2. PER LA RICETTA VADO DAL MEDICO DI BASE.", "3. IN FARMACIA SI COMPRANO I VESTITI.", "4. IL PRONTO SOCCORSO È APERTO DI NOTTE."],
     ["VERO", "VERO", "FALSO", "VERO"], "4 · Vero o falso?", "4 · Vero o falso", "e4"),
  parla("e5", 5, "SEI DAL MEDICO. DI' CHE COSA TI FA MALE, DA QUANDO E SE HAI LA FEBBRE."),
]))

# 14 · posta, dimostrativi, ordine della frase
SCHEDE.append(scheda(14, "Alla posta", "", [
  {"part": "Le parole della posta"},
  menu(["IL MITTENTE", "IL DESTINATARIO", "LA RACCOMANDATA", "IL PACCO", "LO SPORTELLO"],
       [("1. LA PERSONA CHE SPEDISCE LA LETTERA", "IL MITTENTE"), ("2. LA PERSONA CHE RICEVE LA LETTERA", "IL DESTINATARIO"),
        ("3. UNA LETTERA IMPORTANTE, CON LA RICEVUTA", "LA RACCOMANDATA"), ("4. UNA SCATOLA DA SPEDIRE", "IL PACCO"), ("5. IL POSTO DOVE C'È L'IMPIEGATO", "LO SPORTELLO")],
       "1 · Che cos'è?", "1 · La posta", "e1"),
  {"part": "Questo e quello"},
  menu(["QUESTO", "QUESTA", "QUESTI", "QUESTE"], [("1. ___ PACCO", "QUESTO"), ("2. ___ LETTERE", "QUESTE"), ("3. ___ BOLLETTA", "QUESTA"), ("4. ___ MODULI", "QUESTI")],
       "2 · Questo, questa…", "2 · Questo", "e2"),
  menu(["QUEL", "QUELLO", "QUELLA", "QUELL'", "QUEI", "QUEGLI", "QUELLE"],
       [("1. ___ SPORTELLO", "QUELLO"), ("2. ___ IMPIEGATO", "QUELL'"), ("3. ___ PACCHI", "QUEI"), ("4. ___ BUSTA", "QUELLA"), ("5. ___ FRANCOBOLLO", "QUEL"),
        ("6. ___ SPORTELLI", "QUEGLI"), ("7. ___ CARTOLINE", "QUELLE")], "3 · Quel, quello, quella…", "3 · Quello", "e3"),
  scrivi([("1. QUESTA LETTERA È PER TE. → QUESTE ___", ["lettere sono per te"]), ("2. QUEL PACCO È PESANTE. → QUEI ___", ["pacchi sono pesanti"])],
         "4 · Scrivi al plurale", "4 · Il plurale", "e4", w="l"),
  ordina(["VORREI", "SPEDIRE", "QUESTA", "RACCOMANDATA", "IN", "FRANCIA"], "5 · Metti in ordine la frase", "5 · In ordine", "e5"),
]))

# 15 · documenti, asilo, stare + gerundio
SCHEDE.append(scheda(15, "I documenti", "", [
  {"part": "I documenti"},
  vf(["1. IL PERMESSO DI SOGGIORNO SI CHIEDE IN QUESTURA.", "2. LA COMMISSIONE TERRITORIALE DECIDE SULLA DOMANDA DI ASILO.",
      "3. IL PERMESSO DI SOGGIORNO NON SCADE MAI.", "4. CON IL CODICE FISCALE POSSO ISCRIVERMI AL SERVIZIO SANITARIO."],
     ["VERO", "VERO", "FALSO", "VERO"], "1 · Vero o falso?", "1 · I documenti", "e1"),
  menu(["PER LAVORO", "PER MOTIVI FAMILIARI", "PER STUDIO", "PER RICHIESTA ASILO"],
       [("1. HO UN CONTRATTO DI LAVORO.", "PER LAVORO"), ("2. SONO VENUTA IN ITALIA DA MIO MARITO.", "PER MOTIVI FAMILIARI"),
        ("3. FREQUENTO L'UNIVERSITÀ A BARI.", "PER STUDIO"), ("4. ASPETTO LA DECISIONE DELLA COMMISSIONE.", "PER RICHIESTA ASILO")],
       "2 · Che permesso di soggiorno?", "2 · Il permesso", "e2"),
  {"part": "Stare + gerundio"},
  menu(["STO", "STAI", "STA", "STIAMO", "STATE", "STANNO"],
       [("1. IO ___ ASPETTANDO IL MIO TURNO.", "STO"), ("2. TU ___ COMPILANDO IL MODULO?", "STAI"), ("3. LUI ___ PARLANDO CON L'AVVOCATO.", "STA"),
        ("4. NOI ___ STUDIANDO.", "STIAMO"), ("5. LORO ___ ARRIVANDO.", "STANNO")], "3 · Il verbo stare", "3 · Stare", "e3"),
  scrivi([("1. PARLARE → ___", ["parlando"]), ("2. SCRIVERE → ___", ["scrivendo"]), ("3. DORMIRE → ___", ["dormendo"]),
          ("4. FARE → ___", ["facendo"]), ("5. BERE → ___", ["bevendo"])], "4 · Scrivi il gerundio", "4 · Il gerundio", "e4"),
  scrivi([("1. QUESTRA", ["questura"]), ("2. PERMESO", ["permesso"]), ("3. DOMANNDA", ["domanda"]), ("4. AVOCATO", ["avvocato"])],
         "5 · Correggi la parola", "5 · Correggi", "e5", cons="LA PAROLA HA UN ERRORE. SCRIVILA GIUSTA."),
]))

# 16 · ufficio, comune, date, passato prossimo
SCHEDE.append(scheda(16, "In ufficio e al Comune", "", [
  {"part": "Il passato prossimo"},
  menu(["HO", "HAI", "HA", "SONO", "SEI", "È"],
       [("1. IERI ___ ANDATO IN COMUNE. (IO)", "SONO"), ("2. ___ COMPILATO IL MODULO? (TU)", "HAI"), ("3. LA SEGRETARIA ___ STAMPATO IL CERTIFICATO.", "HA"),
        ("4. MARIA ___ ARRIVATA IN RITARDO.", "È"), ("5. ___ FIRMATO IL CONTRATTO. (IO)", "HO"), ("6. TU ___ USCITO PRESTO.", "SEI")], "1 · Essere o avere?", "1 · L'ausiliare", "e1"),
  scrivi([("1. FARE → ___", ["fatto"]), ("2. SCRIVERE → ___", ["scritto"]), ("3. PRENDERE → ___", ["preso"]), ("4. VEDERE → ___", ["visto"]),
          ("5. METTERE → ___", ["messo"]), ("6. APRIRE → ___", ["aperto"])], "2 · I participi irregolari", "2 · I participi", "e2"),
  scegli([("1. LE RAGAZZE SONO ___ ALL'ANAGRAFE.", ["ANDATE", "ANDATO", "ANDATI"], "ANDATE"), ("2. MIO FRATELLO È ___ IERI.", ["PARTITO", "PARTITA", "PARTITI"], "PARTITO"),
          ("3. NOI (DONNE) SIAMO ___ ALLE 9.", ["ARRIVATE", "ARRIVATI", "ARRIVATO"], "ARRIVATE")], "3 · L'accordo del participio", "3 · L'accordo", "e3"),
  menu(["IERI", "L'ALTRO IERI", "LA SETTIMANA SCORSA", "UN MESE FA"],
       [("1. OGGI È 15 MARZO. → 14 MARZO", "IERI"), ("2. OGGI È 15 MARZO. → 13 MARZO", "L'ALTRO IERI"), ("3. OGGI È 15 MARZO. → 15 FEBBRAIO", "UN MESE FA"),
        ("4. OGGI È 15 MARZO. → 8 MARZO", "LA SETTIMANA SCORSA")], "4 · Quando?", "4 · Le date", "e4"),
  libero("e5", 5, "Ieri", "CHE COSA HAI FATTO IERI? SCRIVI 4 FRASI AL PASSATO PROSSIMO.", ["IERI"], rows=4),
]))

# 17 · raccolta differenziata, futuro
SCHEDE.append(scheda(17, "La raccolta differenziata", "", [
  {"part": "I rifiuti"},
  menu(["CARTA", "PLASTICA", "VETRO", "ORGANICO"],
       [("1. LA BOTTIGLIA DELL'ACQUA (DI PLASTICA)", "PLASTICA"), ("2. IL GIORNALE", "CARTA"), ("3. IL BARATTOLO DI MARMELLATA (DI VETRO)", "VETRO"),
        ("4. LE BUCCE DI BANANA", "ORGANICO"), ("5. LA SCATOLA DEI BISCOTTI (DI CARTONE)", "CARTA"), ("6. GLI AVANZI DI CIBO", "ORGANICO")], "1 · Dove lo butto?", "1 · I rifiuti", "e1"),
  {"part": "Il futuro"},
  menu(["ANDRÒ", "FARAI", "SARÀ", "AVREMO", "PULIRETE", "VERRANNO"],
       [("1. DOMANI IO ___ AL MERCATO.", "ANDRÒ"), ("2. CHE COSA ___ STASERA, TU?", "FARAI"), ("3. DOMANI ___ UNA BELLA GIORNATA.", "SARÀ"),
        ("4. NOI ___ UNA CASA NUOVA.", "AVREMO"), ("5. VOI ___ LA CUCINA?", "PULIRETE"), ("6. I MIEI CUGINI ___ A NATALE.", "VERRANNO")], "2 · Il futuro", "2 · Il futuro", "e2"),
  scrivi([("1. IO (BUTTARE) ___ LA PLASTICA.", ["buttero"]), ("2. LORO (PORTARE) ___ IL VETRO.", ["porteranno"]), ("3. TU (DIVIDERE) ___ I RIFIUTI.", ["dividerai"]),
          ("4. NOI (USARE) ___ MENO PLASTICA.", ["useremo"])], "3 · Scrivi il futuro", "3 · Scrivi", "e3"),
  completa("SE DOMANI ___ IL SOLE, ANDREMO AL MARE. SE ___ , RESTEREMO A CASA. SE ___ TEMPO, PULIRÒ IL BALCONE.",
           ["ci sarà", "pioverà", "avrò"], "4 · Se… al futuro", "4 · Se", "e4", "CI SARÀ · PIOVERÀ · AVRÒ"),
  libero("e5", 5, "Il fine settimana", "CHE COSA FARAI IL PROSSIMO FINE SETTIMANA? SCRIVI 4 FRASI AL FUTURO.", ["IL MIO FINE SETTIMANA"], rows=4),
]))

# 18 · feste, uffici pubblici, si impersonale
SCHEDE.append(scheda(18, "Feste e servizi", "", [
  {"part": "Le feste"},
  scegli([("1. IL 2 GIUGNO SI FESTEGGIA…", ["LA FESTA DELLA REPUBBLICA", "IL NATALE", "IL CAPODANNO"], "LA FESTA DELLA REPUBBLICA"),
          ("2. DOPO IL RAMADAN SI FESTEGGIA…", ["L'EID AL-FITR", "LA PASQUA", "FERRAGOSTO"], "L'EID AL-FITR"),
          ("3. IL 25 DICEMBRE SI FESTEGGIA…", ["IL NATALE", "LA LIBERAZIONE", "SAN NICOLA"], "IL NATALE")], "1 · Che festa è?", "1 · Le feste", "e1"),
  {"part": "Gli uffici"},
  menu(["IN BANCA", "ALLA POSTA", "IN FARMACIA", "ALL'ANAGRAFE"],
       [("1. SI PRENDONO LE MEDICINE.", "IN FARMACIA"), ("2. SI CHIEDE LA CARTA D'IDENTITÀ.", "ALL'ANAGRAFE"), ("3. SI APRE UN CONTO CORRENTE.", "IN BANCA"),
        ("4. SI SPEDISCE UN PACCO.", "ALLA POSTA"), ("5. SI FA IL CAMBIO DI RESIDENZA.", "ALL'ANAGRAFE")], "2 · Dove si fa?", "2 · Gli uffici", "e2"),
  {"part": "Il si impersonale"},
  scrivi([("1. A BARI (MANGIARE) ___ LE ORECCHIETTE.", ["si mangiano"]), ("2. IN BANCA (ASPETTARE) ___ IL TURNO.", ["si aspetta"]),
          ("3. A NATALE (FARE) ___ I REGALI.", ["si fanno"]), ("4. IN BIBLIOTECA (PARLARE) ___ PIANO.", ["si parla"])],
         "3 · Scrivi con il si", "3 · Si", "e3", w="m", cons="USA SI + VERBO. ATTENZIONE: CON UN NOME PLURALE IL VERBO È PLURALE."),
  libero("e4", 4, "Nel mio paese", "COME SI FESTEGGIA UNA FESTA NEL TUO PAESE? USA IL SI: SI MANGIA…, SI BALLA…", ["LA FESTA"], rows=4),
]))

# 19 · feste popolari, pronomi diretti
SCHEDE.append(scheda(19, "Le feste popolari", "", [
  {"part": "Le feste popolari"},
  vf(["1. IL CORTEO DI SAN NICOLA PASSA PER LE STRADE DI BARI VECCHIA.", "2. A MAGGIO SI FESTEGGIA SAN NICOLA.",
      "3. DURANTE IL CORTEO LE PERSONE PORTANO COSTUMI ANTICHI.", "4. LA FESTA È SOLO PER I BAMBINI."],
     ["VERO", "VERO", "VERO", "FALSO"], "1 · Leggi: vero o falso?", "1 · San Nicola", "e1",
     info="OGNI ANNO A MAGGIO BARI FESTEGGIA SAN NICOLA. LA SERA DEL 7 MAGGIO UN GRANDE CORTEO STORICO, CON CENTINAIA DI PERSONE IN COSTUMI ANTICHI, "
          "PASSA PER LE STRADE DI BARI VECCHIA. ALLA FESTA PARTECIPANO TUTTI: FAMIGLIE, TURISTI E PELLEGRINI DA TANTI PAESI."),
  {"part": "Lo, la, li, le"},
  menu(["LO", "LA", "LI", "LE"],
       [("1. VEDI IL CORTEO? SÌ, ___ VEDO.", "LO"), ("2. CONOSCI LA FESTA? SÌ, ___ CONOSCO.", "LA"), ("3. COMPRI I DOLCI? SÌ, ___ COMPRO.", "LI"),
        ("4. INVITI LE AMICHE? SÌ, ___ INVITO.", "LE"), ("5. PRENDI IL TRENO? SÌ, ___ PRENDO.", "LO")], "2 · Il pronome giusto", "2 · I pronomi", "e2"),
  scegli([("1. HAI VISTO LA PROCESSIONE? SÌ, L'HO ___.", ["VISTA", "VISTO", "VISTI"], "VISTA"), ("2. HAI COMPRATO I BIGLIETTI? SÌ, LI HO ___.", ["COMPRATI", "COMPRATO", "COMPRATE"], "COMPRATI"),
          ("3. HAI FATTO LE FOTO? SÌ, LE HO ___.", ["FATTE", "FATTO", "FATTI"], "FATTE")], "3 · Pronome e participio", "3 · L'accordo", "e3"),
  scrivi([("1. COMPRO IL PANE. → ___ COMPRO.", ["lo"]), ("2. ASPETTO LE MIE SORELLE. → ___ ASPETTO.", ["le"]), ("3. GUARDO I FUOCHI. → ___ GUARDO.", ["li"])],
         "4 · Scrivi il pronome", "4 · Scrivi", "e4", w="s"),
  parla("e5", 5, "RACCONTA UNA FESTA POPOLARE DEL TUO PAESE O DELLA TUA CITTÀ: QUANDO È E CHE COSA SI FA?"),
]))

ESERCIZIARIO = [("eserciziario-a1/scheda-%02d.html" % (i + 1), d) for i, d in enumerate(SCHEDE)]

from teoria import aggiungi, TEORIA_SCHEDE
aggiungi(SCHEDE, TEORIA_SCHEDE)
