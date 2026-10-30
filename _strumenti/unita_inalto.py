"""Percorso A1-A2 in 13 unità (2026-10-30): Erila ha mandato lo specimen di «In alto! A1-A2» (Ornimi Editions).
Il libro è protetto da copyright: qui si riprendono solo gli ARGOMENTI dell'indice (comunicazione + grammatica);
tutte le frasi e gli esercizi sono scritti per il sito. Unità 0-5 = A1 (STAMPATELLO MAIUSCOLO),
unità 6-12 = A2 (minuscolo, come le altre pagine A2). Pagine in percorso-a1-a2/unita-NN.html."""
from unita_drive import vf, scegli, menu, scrivi, ordina, completa, parla, libero

def unita(n, titolo, livello, sections):
    return {"title": "🧗 Unità %d · %s" % (n, titolo), "store": "percorso-%02d" % n, "upper": livello == "A1",
            "sub": ("PERCORSO A1-A2 · UNITÀ %d · LIVELLO A1" if livello == "A1" else "Percorso A1-A2 · unità %d · livello A2") % n,
            "sections": sections}

U = []

# ---------------------------------------------------------------- A1
U.append(("A1", unita(0, "Cominciamo!", "A1", [
  {"part": "L'alfabeto"},
  menu(["CA", "CHE", "CI", "CO", "CHI"],
       [("1. CASA → ___", "CA"), ("2. PERCHÉ → ___", "CHE"), ("3. CIAO → ___", "CI"), ("4. COSA → ___", "CO"), ("5. CHIAVE → ___", "CHI")],
       "1 · Che suono senti all'inizio o alla fine?", "1 · I suoni", "e1"),
  scrivi([("1. B - A - R - I", ["bari"]), ("2. R - O - M - A", ["roma"]), ("3. L - E - C - C - E", ["lecce"]), ("4. N - A - P - O - L - I", ["napoli"])],
         "2 · Scrivi la parola", "2 · Lettera per lettera", "e2", cons="LEGGI LE LETTERE E SCRIVI LA PAROLA."),
  {"part": "In classe"},
  menu(["PUOI RIPETERE, PER FAVORE?", "COME SI SCRIVE?", "COME SI DICE IN ITALIANO?", "NON HO CAPITO."],
       [("1. L'INSEGNANTE PARLA VELOCE.", "PUOI RIPETERE, PER FAVORE?"), ("2. NON SAI LE LETTERE DI UNA PAROLA.", "COME SI SCRIVE?"),
        ("3. CONOSCI LA PAROLA SOLO NELLA TUA LINGUA.", "COME SI DICE IN ITALIANO?"), ("4. LA SPIEGAZIONE NON È CHIARA.", "NON HO CAPITO.")],
       "3 · Che cosa dici?", "3 · Le frasi utili", "e3"),
  parla("e4", 4, "DI' IL TUO NOME LETTERA PER LETTERA."),
])))

U.append(("A1", unita(1, "Buongiorno, come ti chiami?", "A1", [
  {"part": "Presentarsi"},
  menu(["IO", "TU", "LUI", "LEI", "NOI", "LORO"],
       [("1. ___ SONO INGRID.", "IO"), ("2. ___ SIAMO STUDENTI.", "NOI"), ("3. ___ SEI DI BARI?", "TU"), ("4. ___ È UN RAGAZZO.", "LUI"),
        ("5. ___ È UNA RAGAZZA.", "LEI"), ("6. ___ SONO AMICI.", "LORO")], "1 · Il pronome giusto", "1 · I pronomi", "e1"),
  scegli([("1. SONO DEL BRASILE. SONO ___.", ["BRASILIANA", "BRASILE", "BRASILIANI"], "BRASILIANA"),
          ("2. LUI È DELLA CINA. È ___.", ["CINESE", "CINA", "CINESO"], "CINESE"),
          ("3. LORO SONO DELLA FRANCIA. SONO ___.", ["FRANCESI", "FRANCESE", "FRANCIA"], "FRANCESI"),
          ("4. LEI È DELL'UCRAINA. È ___.", ["UCRAINA", "UCRAINO", "UCRAINESE"], "UCRAINA")], "2 · La nazionalità", "2 · Le nazionalità", "e2"),
  {"part": "Domande e negazioni"},
  scrivi([("1. SEI ITALIANO? NO, NON ___ ITALIANO.", ["sono"]), ("2. HAI UNA PENNA? NO, NON ___ UNA PENNA.", ["ho"]),
          ("3. LUI È DI ROMA? NO, NON ___ DI ROMA.", ["e"]), ("4. AVETE UN DIZIONARIO? NO, NON ___ UN DIZIONARIO.", ["abbiamo"])],
         "3 · Rispondi di no", "3 · No", "e3", w="s"),
  scrivi([("1. 11", ["undici"]), ("2. 14", ["quattordici"]), ("3. 16", ["sedici"]), ("4. 19", ["diciannove"]), ("5. 20", ["venti"])],
         "4 · I numeri 0-20", "4 · I numeri", "e4"),
  parla("e5", 5, "SALUTA, DI' COME TI CHIAMI, DI DOVE SEI E CHIEDI IL NOME A UN COMPAGNO."),
])))

U.append(("A1", unita(2, "Nuovi amici", "A1", [
  {"part": "Come stai?"},
  menu(["STO BENE", "STO MALE", "SONO STANCO", "HO FAME", "HO SONNO"],
       [("1. 😀", "STO BENE"), ("2. 🤒", "STO MALE"), ("3. 😩 HO LAVORATO TANTO.", "SONO STANCO"), ("4. 🍽️", "HO FAME"), ("5. 😴", "HO SONNO")],
       "1 · Come stai?", "1 · Come stai", "e1"),
  {"part": "Verbi in -are e -ere"},
  scrivi([("1. IO (PARLARE) ___ ARABO.", ["parlo"]), ("2. TU (SCRIVERE) ___ UNA LETTERA.", ["scrivi"]), ("3. LEI (ABITARE) ___ A BARI.", ["abita"]),
          ("4. NOI (LEGGERE) ___ IL GIORNALE.", ["leggiamo"]), ("5. VOI (STUDIARE) ___ ITALIANO.", ["studiate"]), ("6. LORO (PRENDERE) ___ IL CAFFÈ.", ["prendono"])],
         "2 · Scrivi il verbo", "2 · Il presente", "e2"),
  menu(["VADO", "VAI", "VA", "STO", "STAI", "STA"],
       [("1. IO ___ AL CORSO IL LUNEDÌ.", "VADO"), ("2. COME ___ TU?", "STAI"), ("3. LEI ___ IN PALESTRA.", "VA"), ("4. IO ___ BENE, GRAZIE.", "STO"),
        ("5. DOVE ___ STASERA?", "VAI"), ("6. TUO FIGLIO COME ___?", "STA")], "3 · Andare o stare?", "3 · Andare e stare", "e3"),
  {"part": "Descrivere un amico"},
  vf(["1. LUCA È ALTO.", "2. HA I CAPELLI BIONDI.", "3. VA SEMPRE AL CINEMA.", "4. LEGGE MOLTO."], ["VERO", "FALSO", "FALSO", "VERO"],
     "4 · Leggi: vero o falso?", "4 · Luca", "e4",
     info="IL MIO AMICO LUCA È ALTO E MAGRO. HA I CAPELLI CORTI E NERI E GLI OCCHI MARRONI. VA QUALCHE VOLTA AL CINEMA, MA LEGGE MOLTO: OGNI SETTIMANA UN LIBRO NUOVO."),
  libero("e5", 5, "Il mio amico", "DESCRIVI UN AMICO O UN'AMICA: COM'È? CHE COSA FA SPESSO?", ["IL MIO AMICO / LA MIA AMICA"], rows=4),
])))

U.append(("A1", unita(3, "Che cosa fai?", "A1", [
  {"part": "Verbi in -ire, fare, dare, venire"},
  scrivi([("1. IO (DORMIRE) ___ 8 ORE.", ["dormo"]), ("2. TU (CAPIRE) ___ L'ITALIANO?", ["capisci"]), ("3. LUI (PARTIRE) ___ DOMANI.", ["parte"]),
          ("4. NOI (FINIRE) ___ ALLE 5.", ["finiamo"]), ("5. LORO (SENTIRE) ___ LA MUSICA.", ["sentono"])], "1 · Verbi in -ire", "1 · -ire", "e1"),
  menu(["FACCIO", "DAI", "VIENE", "VENIAMO", "DANNO", "FATE"],
       [("1. IO ___ L'INFERMIERA.", "FACCIO"), ("2. TU MI ___ IL TUO NUMERO?", "DAI"), ("3. LEI ___ DAL MAROCCO.", "VIENE"),
        ("4. NOI ___ ALLA FESTA.", "VENIAMO"), ("5. I NONNI ___ I REGALI AI BAMBINI.", "DANNO"), ("6. CHE COSA ___ VOI?", "FATE")], "2 · Fare, dare, venire", "2 · Verbi irregolari", "e2"),
  {"part": "Data e ora"},
  scrivi([("1. 10:00 → SONO LE ___", ["dieci"]), ("2. 12:00 → È ___", ["mezzogiorno"]), ("3. 3:30 → SONO LE TRE E ___", ["mezza", "trenta"]),
          ("4. 6:45 → SONO LE SETTE MENO UN ___", ["quarto"])], "3 · Che ore sono?", "3 · L'ora", "e3"),
  ordina(["LUNEDÌ", "MARTEDÌ", "MERCOLEDÌ", "GIOVEDÌ", "VENERDÌ", "SABATO", "DOMENICA"], "4 · Metti in ordine i giorni", "4 · I giorni", "e4"),
  parla("e5", 5, "CHE COSA FAI? LAVORI O STUDI? CHE GIORNI E A CHE ORA?"),
])))

U.append(("A1", unita(4, "Cosa prendiamo?", "A1", [
  {"part": "Al bar"},
  menu(["VORREI UN CAFFÈ.", "QUANTO COSTA?", "IL CONTO, PER FAVORE.", "POSSO SEDERMI QUI?"],
       [("1. VUOI ORDINARE.", "VORREI UN CAFFÈ."), ("2. VUOI SAPERE IL PREZZO.", "QUANTO COSTA?"), ("3. VUOI PAGARE AL TAVOLO.", "IL CONTO, PER FAVORE."),
        ("4. VUOI IL PERMESSO DI USARE UNA SEDIA.", "POSSO SEDERMI QUI?")], "1 · Che cosa dici?", "1 · Al bar", "e1"),
  {"part": "Dire, bere, uscire"},
  menu(["DICO", "DICI", "BEVE", "BEVIAMO", "ESCI", "ESCONO"],
       [("1. IO ___ SEMPRE LA VERITÀ.", "DICO"), ("2. CHE COSA ___ TU?", "DICI"), ("3. LEI ___ UN SUCCO.", "BEVE"), ("4. NOI ___ ACQUA FRIZZANTE.", "BEVIAMO"),
        ("5. TU ___ STASERA?", "ESCI"), ("6. I RAGAZZI ___ ALLE 9.", "ESCONO")], "2 · Dire, bere, uscire", "2 · I verbi", "e2"),
  menu(["MI PIACE", "MI PIACCIONO"], [("1. ___ IL GELATO.", "MI PIACE"), ("2. ___ I CORNETTI.", "MI PIACCIONO"), ("3. NON ___ LE OLIVE.", "MI PIACCIONO"), ("4. ___ BALLARE.", "MI PIACE")],
       "3 · Piace o piacciono?", "3 · Mi piace", "e3"),
  completa("CAMERIERE: BUONGIORNO, CHE COSA ___?<br>CLIENTE: UN CAPPUCCINO E UN CORNETTO, PER FAVORE.<br>CAMERIERE: CON LA CREMA O CON LA ___?<br>"
           "CLIENTE: CON LA CREMA. QUANTO ___?<br>CAMERIERE: 2 EURO E 50.",
           ["prende", "marmellata", "costa"], "4 · Completa il dialogo", "4 · Il dialogo", "e4", "PRENDE · MARMELLATA · COSTA"),
  parla("e5", 5, "INVITA UN AMICO AL BAR. ORDINA E CHIEDI IL CONTO."),
])))

U.append(("A1", unita(5, "In città", "A1", [
  {"part": "Volere, potere, dovere"},
  menu(["VOGLIO", "VUOI", "POSSO", "PUÒ", "DEVO", "DOBBIAMO"],
       [("1. IO ___ VISITARE IL CASTELLO.", "VOGLIO"), ("2. TU ___ UN GELATO?", "VUOI"), ("3. SCUSI, ___ ENTRARE? (IO)", "POSSO"),
        ("4. LEI NON ___ VENIRE: È MALATA.", "PUÒ"), ("5. IO ___ PRENDERE L'AUTOBUS.", "DEVO"), ("6. NOI ___ PAGARE IL BIGLIETTO.", "DOBBIAMO")], "1 · I verbi modali", "1 · I modali", "e1"),
  {"part": "Indicazioni"},
  menu(["SEMPRE DRITTO", "A DESTRA", "A SINISTRA", "DI FRONTE", "VICINO"],
       [("1. ➡️ GIRA ___", "A DESTRA"), ("2. ⬅️ GIRA ___", "A SINISTRA"), ("3. ⬆️ VAI ___", "SEMPRE DRITTO"), ("4. LA FARMACIA È ___ ALLA CHIESA: LA VEDI DALL'ALTRA PARTE DELLA STRADA.", "DI FRONTE"),
        ("5. LA FERMATA È ___ AL BAR: A 20 METRI.", "VICINO")], "2 · Dove?", "2 · Le indicazioni", "e2"),
  menu(["PRIMAVERA", "ESTATE", "AUTUNNO", "INVERNO"], [("1. MARZO", "PRIMAVERA"), ("2. AGOSTO", "ESTATE"), ("3. NOVEMBRE", "AUTUNNO"), ("4. FEBBRAIO", "INVERNO")],
       "3 · Mesi e stagioni", "3 · Le stagioni", "e3"),
  vf(["1. FA FREDDO.", "2. SAMIA VUOLE ANDARE AL MARE.", "3. DEVE LAVORARE DI SABATO.", "4. DOMENICA PUÒ USCIRE."], ["FALSO", "VERO", "VERO", "VERO"],
     "4 · Leggi: vero o falso?", "4 · Il fine settimana", "e4",
     info="OGGI FA CALDO E C'È IL SOLE. SAMIA VUOLE ANDARE AL MARE, MA SABATO DEVE LAVORARE AL SUPERMERCATO. DOMENICA È LIBERA: PUÒ USCIRE CON LE AMICHE."),
  parla("e5", 5, "SPIEGA A UN AMICO COME ARRIVARE DA CASA TUA ALLA SCUOLA."),
])))

# ---------------------------------------------------------------- A2 (minuscolo)
U.append(("A2", unita(6, "Che cosa hai fatto nel fine settimana?", "A2", [
  {"part": "Il passato prossimo"},
  scrivi([("1. Sabato io (lavorare) ___ fino alle 2.", ["ho lavorato"]), ("2. Domenica Fatima (andare) ___ al mare.", ["e andata"]),
          ("3. Noi (mangiare) ___ in pizzeria.", ["abbiamo mangiato"]), ("4. I bambini (giocare) ___ al parco.", ["hanno giocato"]),
          ("5. Tu (uscire) ___ con gli amici? (maschile)", ["sei uscito"])], "1 · Scrivi il passato prossimo", "1 · Il passato", "e1", w="m"),
  {"part": "Già e ancora"},
  scegli([("1. Hai ___ fatto la spesa? Sì, stamattina.", ["già", "ancora", "mai"], "già"), ("2. Non ho ___ finito i compiti.", ["ancora", "già", "sempre"], "ancora"),
          ("3. Il film è ___ cominciato: corri!", ["già", "ancora", "dopo"], "già")], "2 · Già o ancora?", "2 · Già / ancora", "e2"),
  ordina(["Prima ho fatto colazione", "poi sono andato al mercato", "dopo ho cucinato", "infine ho dormito un po'"], "3 · Metti in ordine il racconto", "3 · Prima, poi", "e3"),
  vf(["1. Nadia è rimasta a casa sabato.", "2. Ha visto una mostra.", "3. Domenica ha pranzato dai suoceri.", "4. È tornata a casa tardi."], ["Falso", "Vero", "Vero", "Falso"],
     "4 · Leggi: vero o falso?", "4 · Il fine settimana di Nadia", "e4",
     info="Sabato Nadia è uscita con la sua amica Lina: hanno visto una mostra di fotografia al Teatro Margherita. Domenica ha pranzato dai suoceri e alle 6 è tornata a casa."),
  libero("e5", 5, "Il mio fine settimana", "Racconta che cosa hai fatto lo scorso fine settimana (5 frasi).", ["Il mio fine settimana"], rows=5),
])))

U.append(("A2", unita(7, "Dove abiti?", "A2", [
  {"part": "Stare + gerundio"},
  scrivi([("1. Mio marito (cucinare) ___.", ["sta cucinando"]), ("2. Io (leggere) ___ un annuncio.", ["sto leggendo"]),
          ("3. I bambini (dormire) ___.", ["stanno dormendo"]), ("4. Noi (cercare) ___ casa.", ["stiamo cercando"])], "1 · Che cosa sta facendo?", "1 · Stare + gerundio", "e1", w="m"),
  {"part": "Preposizioni articolate"},
  menu(["nel", "nella", "sul", "sulla", "dal", "alla"],
       [("1. Le chiavi sono ___ cassetto.", "nel"), ("2. Il gatto dorme ___ divano.", "sul"), ("3. Il latte è ___ frigorifero.", "nel"),
        ("4. Abito ___ casa dei miei genitori.", "nella"), ("5. Vado ___ dentista.", "dal"), ("6. La foto è ___ parete.", "sulla")], "2 · La preposizione giusta", "2 · Le preposizioni", "e2"),
  {"part": "La famiglia e i possessivi"},
  scegli([("1. ___ sorella vive a Torino.", ["Mia", "La mia", "Mio"], "Mia"), ("2. ___ genitori sono pensionati.", ["I miei", "Miei", "Le mie"], "I miei"),
          ("3. ___ sorellina va all'asilo.", ["La mia", "Mia", "Il mio"], "La mia"), ("4. Come si chiamano ___ figli?", ["i tuoi", "tuoi", "le tue"], "i tuoi")],
         "3 · Con o senza articolo?", "3 · I possessivi", "e3",
         cons="Attenzione: con i nomi di famiglia al singolare non si usa l'articolo, ma con i diminutivi e al plurale sì."),
  libero("e4", 4, "La mia casa", "Descrivi la casa dove abiti e le persone che ci vivono.", ["La mia casa"], rows=5),
])))

U.append(("A2", unita(8, "Viaggiare", "A2", [
  {"part": "In stazione e in aeroporto"},
  menu(["il binario", "la coincidenza", "il check-in", "il ritardo", "la carta d'imbarco"],
       [("1. Il treno arriva 20 minuti dopo l'orario.", "il ritardo"), ("2. Il posto dove si ferma il treno.", "il binario"),
        ("3. Il secondo treno che prendi durante lo stesso viaggio.", "la coincidenza"), ("4. In aeroporto consegni la valigia e mostri il documento.", "il check-in"),
        ("5. Il documento per salire sull'aereo.", "la carta d'imbarco")], "1 · Che cos'è?", "1 · Il viaggio", "e1"),
  {"part": "I pronomi diretti e ne"},
  menu(["lo", "la", "li", "le", "ne"],
       [("1. Il biglietto? ___ compro online.", "lo"), ("2. La valigia? ___ porto io.", "la"), ("3. Quanti bagagli hai? ___ ho due.", "ne"),
        ("4. I documenti? ___ ho nello zaino.", "li"), ("5. Le chiavi? Non ___ trovo!", "le")], "2 · Il pronome giusto", "2 · I pronomi", "e2"),
  vf(["1. Il treno per Lecce parte dal binario 5.", "2. Il treno è in ritardo.", "3. Il treno ferma a Brindisi.", "4. Si deve convalidare il biglietto."], ["Vero", "Vero", "Vero", "Falso"],
     "3 · Ascolta l'annuncio (leggi): vero o falso?", "3 · L'annuncio", "e3",
     info="Il treno regionale per Lecce delle 10:15 è in partenza dal binario 5 con 10 minuti di ritardo. Ferma a Monopoli, Ostuni e Brindisi. "
          "Il biglietto è digitale: non serve convalidarlo."),
  parla("e4", 4, "Sei a Bari e vuoi andare a Matera. Chiedi a un passante come arrivare alla stazione e quale treno prendere."),
])))

U.append(("A2", unita(9, "Mi ricordo che…", "A2", [
  {"part": "L'imperfetto"},
  scrivi([("1. Da bambino io (abitare) ___ in campagna.", ["abitavo"]), ("2. Mia nonna (fare) ___ il pane.", ["faceva"]),
          ("3. Noi (giocare) ___ per strada.", ["giocavamo"]), ("4. I miei fratelli (essere) ___ piccoli.", ["erano"]),
          ("5. Tu (avere) ___ un cane?", ["avevi"])], "1 · Scrivi l'imperfetto", "1 · L'imperfetto", "e1"),
  scegli([("1. Mentre ___, è arrivato un messaggio.", ["cucinavo", "ho cucinato", "cucino"], "cucinavo"),
          ("2. Ieri ___ alle 7.", ["mi sono svegliato", "mi svegliavo", "mi sveglio"], "mi sono svegliato"),
          ("3. Da piccola ___ sempre al mare d'estate.", ["andavo", "sono andata", "vado"], "andavo"),
          ("4. Quando sono arrivato in Italia, ___ freddo.", ["faceva", "ha fatto", "fa"], "faceva")], "2 · Imperfetto o passato prossimo?", "2 · Imperfetto o passato", "e2"),
  {"part": "Il corpo e il carattere"},
  menu(["timido", "allegro", "testardo", "generoso"],
       [("1. Non parla molto con le persone nuove.", "timido"), ("2. Ride e scherza sempre.", "allegro"), ("3. Non cambia mai idea.", "testardo"), ("4. Regala le sue cose agli altri.", "generoso")],
       "3 · Com'è?", "3 · Il carattere", "e3"),
  libero("e4", 4, "Quando ero piccolo", "Racconta un ricordo di quando eri bambino o bambina: dove abitavi, che cosa facevi?", ["Il mio ricordo"], rows=5),
])))

U.append(("A2", unita(10, "Facciamo la spesa", "A2", [
  {"part": "Pesi e misure"},
  menu(["un chilo di", "un litro di", "un etto di", "una scatola di", "un pacco di"],
       [("1. ___ latte", "un litro di"), ("2. ___ prosciutto", "un etto di"), ("3. ___ patate", "un chilo di"), ("4. ___ biscotti", "un pacco di"), ("5. ___ tonno", "una scatola di")],
       "1 · Quanto?", "1 · Le quantità", "e1"),
  {"part": "I pronomi indiretti"},
  menu(["mi", "ti", "gli", "le", "ci", "vi"],
       [("1. Signora, ___ do un sacchetto? (a Lei)", "le"), ("2. Il fruttivendolo ___ ha dato due mele in più. (a me)", "mi"),
        ("3. A Marco ___ piacciono le arance.", "gli"), ("4. A Sara ___ ho comprato i fiori.", "le"), ("5. Ragazzi, ___ porto un gelato?", "vi"), ("6. Il nonno ___ racconta storie. (a noi)", "ci")],
       "2 · Il pronome indiretto", "2 · I pronomi", "e2"),
  completa("Cliente: Buongiorno, vorrei mezzo ___ di pomodori.<br>Fruttivendolo: Ecco qua. Desidera ___?<br>Cliente: Sì, quanto ___ le fragole?<br>"
           "Fruttivendolo: 4 euro al chilo, ma sono molto buone. Le ___?<br>Cliente: Secondo me sono un po' care. No, grazie.",
           ["chilo", "altro", "costano", "vuole"], "3 · Completa il dialogo", "3 · Al mercato", "e3", "chilo · altro · costano · vuole"),
  parla("e4", 4, "Sei al mercato. Chiedi il prezzo di due prodotti, di' la tua opinione e compra qualcosa."),
])))

U.append(("A2", unita(11, "Se son rose fioriranno!", "A2", [
  {"part": "Futuro e condizionale"},
  scrivi([("1. L'anno prossimo io (cambiare) ___ casa.", ["cambiero"]), ("2. Domani (piovere) ___.", ["piovera"]), ("3. Noi (andare) ___ in vacanza a luglio.", ["andremo"]),
          ("4. Io (volere) ___ un caffè, per favore.", ["vorrei"]), ("5. Tu (dovere) ___ riposare di più.", ["dovresti"])], "1 · Futuro o condizionale", "1 · I verbi", "e1"),
  menu(["un consiglio", "una richiesta gentile", "un desiderio", "un programma"],
       [("1. Dovresti andare dal medico.", "un consiglio"), ("2. Potrebbe aprire la finestra?", "una richiesta gentile"), ("3. Mi piacerebbe vivere al mare.", "un desiderio"),
        ("4. Sabato andrò da mia sorella.", "un programma")], "2 · Che cos'è?", "2 · A che cosa serve", "e2"),
  completa("Se domani ___ bel tempo, andremo al mare. Se il negozio ___ lo sconto, comprerò la giacca di pelle. Se ___ tempo, ti aiuterò.",
           ["farà", "farà", "avrò"], "3 · Se…", "3 · Il periodo ipotetico", "e3", "farà · farà · avrò"),
  menu(["di lana", "di cotone", "di pelle", "di seta"],
       [("1. Una sciarpa calda per l'inverno", "di lana"), ("2. Una maglietta leggera per l'estate", "di cotone"), ("3. Una cintura o una borsa", "di pelle"),
        ("4. Una camicia elegante e lucida", "di seta")], "4 · Di che materiale?", "4 · I materiali", "e4"),
  libero("e5", 5, "Il mio futuro", "Che cosa farai l'anno prossimo? Che cosa ti piacerebbe fare?", ["I miei progetti"], rows=4),
])))

U.append(("A2", unita(12, "E dopo la scuola?", "A2", [
  {"part": "L'imperativo"},
  scegli([("1. (tu) ___ il modulo!", ["Compila", "Compili", "Compilate"], "Compila"), ("2. (Lei) ___, signora!", ["Entri", "Entra", "Entrate"], "Entri"),
          ("3. (voi) ___ attenzione!", ["Fate", "Fa'", "Faccia"], "Fate"), ("4. (tu) Non ___ tardi!", ["arrivare", "arriva", "arrivi"], "arrivare"),
          ("5. (Lei) ___ qui, per favore.", ["Firmi", "Firma", "Firmate"], "Firmi")], "1 · L'imperativo", "1 · L'imperativo", "e1"),
  {"part": "Il lavoro"},
  menu(["si cerca", "si cercano", "si offre", "si richiede"],
       [("1. ___ cameriere con esperienza.", "si cerca"), ("2. ___ due magazzinieri.", "si cercano"), ("3. ___ contratto a tempo indeterminato.", "si offre"),
        ("4. ___ la patente B.", "si richiede")], "2 · L'annuncio di lavoro", "2 · Il si impersonale", "e2"),
  vf(["1. Cercano un cuoco.", "2. Il lavoro è solo la mattina.", "3. Si deve parlare inglese.", "4. Si manda il curriculum per email."], ["Falso", "Falso", "Vero", "Vero"],
     "3 · Leggi l'annuncio: vero o falso?", "3 · L'annuncio", "e3",
     info="Hotel sul lungomare di Bari cerca receptionist per la stagione estiva. Turni di mattina e di pomeriggio. Si richiede buona conoscenza dell'inglese. "
          "Inviare il curriculum all'indirizzo email dell'hotel."),
  libero("e4", 4, "La mia candidatura", "Scrivi una breve email per rispondere a un annuncio di lavoro: chi sei, che esperienza hai, quando sei disponibile.", ["Email"], rows=6),
])))

PERCORSO = [("percorso-a1-a2/unita-%02d.html" % i, d) for i, (_, d) in enumerate(U)]
LIVELLI = [lv for lv, _ in U]

from teoria import aggiungi, TEORIA_PERCORSO
aggiungi([d for _, d in U], TEORIA_PERCORSO)
