"""Pagine di grammatica sugli argomenti della «Videogrammatica in alto!» (Ornimi) che mancavano sul sito (2026-10-30).
I video sono dell'editore e non vanno online: qui ci sono solo regole ed esercizi scritti per il sito.
A1 in STAMPATELLO MAIUSCOLO, A2 in minuscolo. Pagine in grammatica/<nome>.html."""
from unita_drive import vf, scegli, menu, scrivi, ordina, completa, libero
from teoria import tab, es

def pagina(icona, titolo, livello, sections):
    return {"title": "%s %s · Grammatica %s" % (icona, titolo, livello), "store": "gram-" + titolo.lower().replace(" ", "-")[:20],
            "upper": livello == "A1", "sections": sections}

P = {}

# ================================================================ A1
P["nomi-irregolari"] = ("A1", pagina("🧩", "Nomi particolari", "A1", [
  {"part": "Nomi che non cambiano", "teoria":
     "ALCUNI NOMI AL PLURALE <b>NON CAMBIANO</b>:" +
     tab(("CON L'ACCENTO", "IL CAFFÈ → I CAFFÈ · LA CITTÀ → LE CITTÀ"), ("STRANIERI", "IL BAR → I BAR · IL COMPUTER → I COMPUTER"),
         ("CORTI (ABBREVIATI)", "LA FOTO → LE FOTO · LA BICI → LE BICI · L'AUTO → LE AUTO"), ("IN -I", "LA CRISI → LE CRISI"))},
  scrivi([("1. IL CAFFÈ → I ___", ["caffe"]), ("2. LA CITTÀ → LE ___", ["citta"]), ("3. LO SPORT → GLI ___", ["sport"]), ("4. LA FOTO → LE ___", ["foto"]),
          ("5. IL LIBRO → I ___", ["libri"]), ("6. L'UNIVERSITÀ → LE ___", ["universita"])], "1 · Scrivi il plurale", "1 · Il plurale", "e1",
         cons="ATTENZIONE: NON TUTTI SONO PARTICOLARI!"),
  {"part": "I nomi dei lavori", "teoria":
     tab(("-O → -A", "IL CUOCO → LA CUOCA"), ("-IERE → -IERA", "L'INFERMIERE → L'INFERMIERA"), ("-TORE → -TRICE", "L'ATTORE → L'ATTRICE"),
         ("-ISTA, -ANTE, -ENTE: UGUALE", "IL / LA GIORNALISTA · IL / LA CANTANTE · IL / LA DIRIGENTE"),
         ("-E → -ESSA", "LO STUDENTE → LA STUDENTESSA · IL DOTTORE → LA DOTTORESSA"))},
  scrivi([("1. IL CAMERIERE → LA ___", ["cameriera"]), ("2. IL PITTORE → LA ___", ["pittrice"]), ("3. IL FARMACISTA → LA ___", ["farmacista"]),
          ("4. LO STUDENTE → LA ___", ["studentessa"]), ("5. IL COMMESSO → LA ___", ["commessa"]), ("6. IL CANTANTE → LA ___", ["cantante"])],
         "2 · Scrivi il femminile", "2 · Il femminile", "e2"),
  {"part": "Plurali speciali", "teoria":
     "ALCUNI NOMI HANNO UN PLURALE TUTTO DIVERSO:" +
     tab(("L'UOMO", "GLI UOMINI"), ("LA MANO", "LE MANI"), ("IL BRACCIO", "LE BRACCIA"), ("IL DITO", "LE DITA"), ("L'UOVO", "LE UOVA"), ("IL GINOCCHIO", "LE GINOCCHIA"))},
  menu(["GLI UOMINI", "LE MANI", "LE UOVA", "LE BRACCIA", "LE DITA"],
       [("1. COMPRO SEI ___ PER LA TORTA.", "LE UOVA"), ("2. LAVATI ___ PRIMA DI MANGIARE!", "LE MANI"), ("3. IN QUESTA SQUADRA GIOCANO SOLO ___.", "GLI UOMINI"),
        ("4. HO UNA MANO CON CINQUE ___.", "LE DITA"), ("5. ALZA ___ IN ALTO!", "LE BRACCIA")], "3 · Scegli il plurale", "3 · Plurali speciali", "e3"),
]))

P["verbi-care-gare"] = ("A1", pagina("🔤", "Verbi in -care e -gare", "A1", [
  {"part": "Cercare, pagare", "teoria":
     "CON TU E NOI SI AGGIUNGE UNA <b>H</b>, PER TENERE IL SUONO DURO:" +
     tab(("IO", "CERCO", "PAGO"), ("TU", "CERC<b>H</b>I", "PAG<b>H</b>I"), ("LUI / LEI", "CERCA", "PAGA"), ("NOI", "CERC<b>H</b>IAMO", "PAG<b>H</b>IAMO"),
         ("VOI", "CERCATE", "PAGATE"), ("LORO", "CERCANO", "PAGANO"), head=("", "CERCARE", "PAGARE")) +
     "COME CERCARE: GIOCARE, TOCCARE, SPIEGARE, LITIGARE, ASCIUGARE." + es("TU CERCHI LAVORO? NOI PAGHIAMO CON LA CARTA.")},
  scrivi([("1. TU (CERCARE) ___ CASA?", ["cerchi"]), ("2. NOI (PAGARE) ___ L'AFFITTO.", ["paghiamo"]), ("3. IO (GIOCARE) ___ A CALCIO.", ["gioco"]),
          ("4. TU (SPIEGARE) ___ BENE.", ["spieghi"]), ("5. LORO (PAGARE) ___ IN CONTANTI.", ["pagano"]), ("6. NOI (GIOCARE) ___ A CARTE.", ["giochiamo"])],
         "1 · Scrivi il verbo", "1 · Scrivi", "e1"),
  scegli([("1. TU ___ IL BIGLIETTO?", ["PAGHI", "PAGI", "PAGA"], "PAGHI"), ("2. NOI ___ LE CHIAVI.", ["CERCHIAMO", "CERCIAMO", "CERCAMO"], "CERCHIAMO"),
          ("3. L'INSEGNANTE ___ LA REGOLA.", ["SPIEGA", "SPIEGHE", "SPIEGI"], "SPIEGA"), ("4. TU ___ CON I BAMBINI?", ["GIOCHI", "GIOCI", "GIOCA"], "GIOCHI")],
         "2 · Quale forma è giusta?", "2 · Scegli", "e2"),
]))

P["avverbi"] = ("A1", pagina("🧭", "Quando, quanto, dove", "A1", [
  {"part": "Il tempo", "teoria":
     tab(("PRIMA", "ADESSO / ORA", "DOPO / POI"), ("IERI", "OGGI", "DOMANI"), ("LA SETTIMANA SCORSA", "QUESTA SETTIMANA", "LA SETTIMANA PROSSIMA"),
         head=("⏪ PASSATO", "▶️ PRESENTE", "⏩ FUTURO")) + "PRESTO = DI MATTINA PRESTO, IN ANTICIPO · TARDI = IN RITARDO, A NOTTE."},
  menu(["IERI", "OGGI", "DOMANI", "ADESSO", "TARDI"],
       [("1. ___ SONO ANDATO AL MERCATO.", "IERI"), ("2. ___ ANDRÒ DAL MEDICO.", "DOMANI"), ("3. SONO LE 11 DI NOTTE: È ___!", "TARDI"),
        ("4. NON POSSO PARLARE ___: SONO AL LAVORO.", "ADESSO"), ("5. ___ È LUNEDÌ.", "OGGI")], "1 · Quando?", "1 · Il tempo", "e1"),
  {"part": "La quantità e la frequenza", "teoria":
     tab(("TROPPO", "😩 PIÙ DEL NECESSARIO"), ("MOLTO", "😀 TANTO"), ("ABBASTANZA", "🙂 BASTA"), ("POCO", "😐 NON TANTO"), ("PER NIENTE", "🙁 ZERO")) +
     "FREQUENZA: SEMPRE · SPESSO · QUALCHE VOLTA · RARAMENTE · MAI (NON… MAI)." + es("LAVORO MOLTO. NON BEVO MAI ALCOL.")},
  scegli([("1. HO MANGIATO ___: MI FA MALE LA PANCIA!", ["TROPPO", "POCO", "PER NIENTE"], "TROPPO"),
          ("2. NON MI PIACE ___ IL PESCE.", ["PER NIENTE", "MOLTO TROPPO", "ABBASTANZA"], "PER NIENTE"),
          ("3. VADO AL CINEMA UNA VOLTA ALL'ANNO: CI VADO ___.", ["RARAMENTE", "SEMPRE", "SPESSO"], "RARAMENTE"),
          ("4. FACCIO COLAZIONE OGNI GIORNO: LA FACCIO ___.", ["SEMPRE", "MAI", "RARAMENTE"], "SEMPRE")], "2 · Scegli la parola giusta", "2 · Quanto?", "e2"),
  {"part": "Lo spazio", "teoria":
     tab(("QUI / QUA", "VICINO A ME"), ("LÌ / LÀ", "LONTANO"), ("SOPRA ⬆️ / SOTTO ⬇️", ""), ("DENTRO 📦 / FUORI 🌳", ""), ("DAVANTI / DIETRO", ""), ("A DESTRA ➡️ / A SINISTRA ⬅️", ""))},
  menu(["DENTRO", "FUORI", "SOPRA", "SOTTO", "QUI"],
       [("1. PIOVE: RESTIAMO ___ CASA.", "DENTRO"), ("2. C'È IL SOLE: GIOCHIAMO ___!", "FUORI"), ("3. IL GATTO DORME ___ IL TAVOLO.", "SOTTO"),
        ("4. VIENI ___, VICINO A ME!", "QUI"), ("5. IL QUADRO È ___ IL DIVANO.", "SOPRA")], "3 · Dove?", "3 · Lo spazio", "e3"),
]))

P["preposizioni-tempo"] = ("A1", pagina("🕰️", "Le preposizioni di tempo", "A1", [
  {"part": "A, in, da, fra, per", "teoria":
     tab(("A", "ORE, FESTE, MESI", "ALLE 8 · A NATALE · A MAGGIO"), ("IN", "MESI, STAGIONI, ANNI", "IN MAGGIO · IN ESTATE · NEL 2020"),
         ("DA", "INIZIO FINO A ADESSO", "ABITO QUI DA 3 ANNI"), ("FRA / TRA", "NEL FUTURO", "PARTO FRA 2 GIORNI"), ("PER", "QUANTO TEMPO", "HO LAVORATO PER 5 ANNI"),
         ("DA… A…", "INIZIO E FINE", "DALLE 9 ALLE 13 · DA LUNEDÌ A VENERDÌ"), head=("", "QUANDO?", "ESEMPIO")) +
     "IL GIORNO DELLA SETTIMANA SENZA PREPOSIZIONE: LUNEDÌ VADO AL CORSO. IL LUNEDÌ = OGNI LUNEDÌ."},
  menu(["ALLE", "IN", "DA", "FRA", "PER", "A"],
       [("1. IL CORSO COMINCIA ___ 9.", "ALLE"), ("2. ABITO IN ITALIA ___ DUE ANNI.", "DA"), ("3. ___ ESTATE FA CALDO.", "IN"), ("4. IL TRENO PARTE ___ 10 MINUTI.", "FRA"),
        ("5. HO STUDIATO ___ TRE ORE.", "PER"), ("6. ___ NATALE VADO DA MIA SORELLA.", "A")], "1 · La preposizione giusta", "1 · Scegli", "e1"),
  completa("L'UFFICIO È APERTO ___ LUNEDÌ ___ VENERDÌ, ___ 9 ___ 13. IL SABATO È CHIUSO.", ["da", "a", "dalle", "alle"],
           "2 · Completa l'orario", "2 · L'orario", "e2", "DA · A · DALLE · ALLE"),
  libero("e3", 3, "Da quanto tempo?", "DA QUANTO TEMPO ABITI IN ITALIA? DA QUANTO TEMPO STUDI L'ITALIANO? CHE COSA FARAI FRA UN ANNO?", ["LE MIE RISPOSTE"], rows=3),
]))

# ================================================================ A2 (minuscolo)
P["comparativi"] = ("A2", pagina("⚖️", "Comparativi e superlativi", "A2", [
  {"part": "Il comparativo", "teoria":
     tab(("più … di", "Roma è più grande di Bari."), ("meno … di", "Il treno è meno caro dell'aereo."), ("così / tanto … come / quanto", "Luca è (così) alto come Marco."),
         ("più … che", "con due aggettivi, verbi o preposizioni: È più bello che utile. Mi piace più leggere che scrivere.")) +
     "irregolari: buono → <b>migliore</b> · cattivo → <b>peggiore</b> · bene → <b>meglio</b> · male → <b>peggio</b>."},
  scegli([("1. Il caffè è ___ forte del tè.", ["più", "di", "che"], "più"), ("2. L'estate è più calda ___ primavera.", ["della", "che la", "come"], "della"),
          ("3. È più facile parlare ___ scrivere.", ["che", "di", "del"], "che"), ("4. Questa pizza è ___ di quella di ieri: buonissima!", ["migliore", "più buono", "meglio"], "migliore"),
          ("5. Oggi sto ___ di ieri: non ho più la febbre.", ["meglio", "migliore", "più bene"], "meglio")], "1 · Scegli", "1 · Il comparativo", "e1"),
  {"part": "Il superlativo", "teoria":
     "<b>-issimo</b> = molto: bello → bellissimo, caro → carissimo, facile → facilissimo.<br>"
     "<b>il più / il meno … di</b> = il numero 1 di un gruppo." + es("È il ragazzo più alto della classe.") +
     "<br>irregolari: il migliore, il peggiore, ottimo (= buonissimo), pessimo (= cattivissimo)."},
  scrivi([("1. molto bello → ___", ["bellissimo"]), ("2. molto stanca → ___", ["stanchissima"]), ("3. molto buoni → ___", ["buonissimi", "ottimi"]),
          ("4. molto lunghe → ___", ["lunghissime"])], "2 · Scrivi il superlativo in -issimo", "2 · -issimo", "e2",
         cons="Attenzione: stanca → stanch-issima, lunghe → lungh-issime."),
  libero("e3", 3, "Il mio paese e l'Italia", "Confronta il tuo paese e l'Italia: il clima, il cibo, la vita (4 frasi con più, meno, come).", ["Il confronto"], rows=4),
]))

P["buono-bello-indefiniti"] = ("A2", pagina("✨", "Buono, bello e gli indefiniti", "A2", [
  {"part": "Buono e bello", "teoria":
     "davanti al nome <b>bello</b> cambia come l'articolo, <b>buono</b> come «un»:" +
     tab(("il → bel", "un bel ragazzo"), ("lo → bello", "un bello zaino"), ("l' → bell'", "un bell'albero"), ("i → bei", "dei bei fiori"), ("gli → begli", "dei begli occhi"),
         ("la / le → bella / belle", "una bella casa")) + "buono: un buon caffè, un buono stipendio, una buon'idea / buona idea, dei buoni amici."},
  menu(["bel", "bello", "bell'", "bei", "begli", "bella"],
       [("1. Che ___ giornata!", "bella"), ("2. Hai dei ___ occhi.", "begli"), ("3. Abbiamo visto un ___ film.", "bel"), ("4. È un ___ albergo.", "bell'"),
        ("5. Ci sono dei ___ negozi in centro.", "bei"), ("6. Che ___ specchio!", "bello")], "1 · Bello", "1 · Bello", "e1"),
  {"part": "Gli indefiniti", "teoria":
     tab(("ogni + singolare", "ogni giorno, ogni settimana"), ("qualche + singolare", "qualche amico (= alcuni amici)"), ("alcuni / alcune + plurale", "alcune persone"),
         ("tutto / tutti + articolo", "tutto il giorno, tutti i giorni"), ("nessuno / niente + non", "non c'è nessuno · non ho capito niente"),
         ("qualcuno / qualcosa", "c'è qualcuno? vuoi qualcosa?"))},
  scegli([("1. Vado in palestra ___ giorno.", ["ogni", "tutti", "qualche"], "ogni"), ("2. Ho ___ amico a Milano.", ["qualche", "alcuni", "ogni"], "qualche"),
          ("3. Non ho visto ___.", ["nessuno", "qualcuno", "ogni"], "nessuno"), ("4. Lavoro ___ i giorni.", ["tutti", "ogni", "qualche"], "tutti"),
          ("5. Vuoi bere ___?", ["qualcosa", "niente", "ogni"], "qualcosa")], "2 · Scegli l'indefinito", "2 · Gli indefiniti", "e2"),
]))

P["nomi-alterati-avverbi"] = ("A2", pagina("🔎", "Nomi alterati e avverbi di modo", "A2", [
  {"part": "I nomi alterati", "teoria":
     tab(("-ino / -etto", "piccolo, carino", "gattino, casetta"), ("-one", "grande", "librone, portone"), ("-accio", "brutto, cattivo", "tempaccio, parolaccia")) +
     "attenzione: alcune parole sembrano alterate ma non lo sono: il mulino, il bottone, il postino."},
  menu(["un ragazzino", "un ragazzone", "una casetta", "un tempaccio", "una parolaccia"],
       [("1. un ragazzo piccolo", "un ragazzino"), ("2. un ragazzo grande e grosso", "un ragazzone"), ("3. una casa piccola e carina", "una casetta"),
        ("4. un tempo brutto, con pioggia e vento", "un tempaccio"), ("5. una parola brutta e volgare", "una parolaccia")], "1 · Che cos'è?", "1 · Gli alterati", "e1"),
  {"part": "Gli avverbi di modo", "teoria":
     "aggettivo femminile + <b>-mente</b>: lenta → lentamente, sicura → sicuramente.<br>in <b>-le / -re</b> la e cade: facile → facilmente, regolare → regolarmente." +
     "<br>irregolari: buono → <b>bene</b>, cattivo → <b>male</b>." + es("Parla lentamente, per favore.")},
  scrivi([("1. lento → ___", ["lentamente"]), ("2. veloce → ___", ["velocemente"]), ("3. facile → ___", ["facilmente"]), ("4. tranquillo → ___", ["tranquillamente"]),
          ("5. buono → ___", ["bene"]), ("6. speciale → ___", ["specialmente"])], "2 · Scrivi l'avverbio", "2 · -mente", "e2"),
]))

P["imperativo-pronomi"] = ("A2", pagina("👉", "Imperativo con i pronomi", "A2", [
  {"part": "Tu, noi, voi", "teoria":
     "con <b>tu, noi, voi</b> il pronome si attacca alla fine del verbo:" + es("Il pane? Compralo! · La porta? Chiudetela! · Alziamoci!") +
     "<br>con i verbi corti (da', di', fa', sta', va') la consonante raddoppia: <b>dimmi</b>, <b>fallo</b>, <b>dammelo</b> (ma: <b>dagli</b>)." +
     "<br>negativo: non + infinito; il pronome va prima o dopo: non lo comprare / non comprarlo."},
  scrivi([("1. (tu) Comprare il latte → ___!", ["compralo"]), ("2. (voi) Chiudere la finestra → ___!", ["chiudetela"]), ("3. (tu) Dire a me → ___!", ["dimmi"]),
          ("4. (tu) Fare i compiti → ___!", ["falli"]), ("5. (noi) Sedersi → ___!", ["sediamoci"])], "1 · Scrivi l'imperativo con il pronome", "1 · Tu, noi, voi", "e1"),
  {"part": "Lei (formale)", "teoria":
     "con <b>Lei</b> il pronome va <b>prima</b> del verbo:" + es("Si accomodi! · Mi dica! · Lo firmi qui, per favore.")},
  menu(["Si accomodi", "Mi dica", "Lo compili", "Ci scusi", "La chiuda"],
       [("1. Il medico fa entrare il paziente: «___, prego.»", "Si accomodi"), ("2. Il commesso: «Buongiorno, ___.»", "Mi dica"),
        ("3. Il modulo? «___ e lo porti allo sportello.»", "Lo compili"), ("4. «___ per il ritardo, signora.» (noi)", "Ci scusi"),
        ("5. La porta? «___, per favore: fa freddo.»", "La chiuda")], "2 · Che cosa dice?", "2 · Lei", "e2"),
]))

P["futuro-imminente"] = ("A2", pagina("⏳", "Stare per e stare + gerundio", "A2", [
  {"part": "Adesso o fra poco?", "teoria":
     tab(("stare + gerundio", "succede adesso", "Sto mangiando: ti chiamo dopo."), ("stare per + infinito", "succede fra pochissimo", "Il treno sta per partire!")) +
     "sto, stai, sta, stiamo, state, stanno."},
  menu(["sta per", "sta"],
       [("1. Corri, il film ___ cominciare!", "sta per"), ("2. Non disturbare il bambino: ___ dormendo.", "sta"), ("3. Il negozio ___ chiudere: sono le 19:58.", "sta per"),
        ("4. Mamma ___ cucinando la cena.", "sta"), ("5. Il bambino ___ cadere! Prendilo!", "sta per")], "1 · Sta per o sta?", "1 · Scegli", "e1"),
  scrivi([("1. Io (uscire, fra un minuto) → ___ uscire.", ["sto per"]), ("2. Noi (lavorare, adesso) → ___.", ["stiamo lavorando"]),
          ("3. Loro (arrivare, fra un minuto) → ___ arrivare.", ["stanno per"]), ("4. Tu (leggere, adesso) → ___?", ["stai leggendo"])], "2 · Scrivi", "2 · Scrivi", "e2", w="m"),
]))

P["impersonale-reciproci"] = ("A2", pagina("👥", "Si impersonale e verbi reciproci", "A2", [
  {"part": "La forma impersonale", "teoria":
     "<b>si</b> + verbo (3ª persona) = tutti, la gente." + es("In Italia si cena tardi. Si parla italiano.") +
     "<br>con un nome plurale il verbo va al plurale: si vendono case." +
     "<br>espressioni impersonali: <b>bisogna</b>, <b>è necessario</b>, <b>è vietato</b>, <b>è meglio</b> + infinito." + es("Bisogna prenotare. È vietato fumare.")},
  scegli([("1. In questo negozio ___ anche le scarpe.", ["si vendono", "si vende", "vendono si"], "si vendono"), ("2. In biblioteca non ___ parlare ad alta voce.", ["si può", "si possono", "può si"], "si può"),
          ("3. ___ arrivare 10 minuti prima dell'esame.", ["Bisogna", "Bisognano", "Si bisogna"], "Bisogna"), ("4. In treno ___ fumare.", ["è vietato", "si vietano", "vietato è"], "è vietato")],
         "1 · Scegli", "1 · Si e bisogna", "e1"),
  {"part": "I verbi reciproci", "teoria":
     "<b>ci, vi, si</b> + verbo = l'uno con l'altro." + es("Io e Sara ci vediamo domani. Marco e Lia si sposano. Voi vi conoscete?") +
     "<br>al passato con <b>essere</b>: ci siamo conosciuti a Bari."},
  menu(["ci", "vi", "si"],
       [("1. Io e Fatima ___ telefoniamo ogni sera.", "ci"), ("2. Voi ___ scrivete spesso?", "vi"), ("3. Paolo e Anna ___ amano.", "si"),
        ("4. Noi ___ siamo conosciuti al corso.", "ci"), ("5. I bambini ___ abbracciano.", "si")], "2 · Ci, vi o si?", "2 · Reciproci", "e2"),
]))

PAGINE = [("grammatica/%s.html" % k, d) for k, (lv, d) in P.items()]
ELENCO = [(k, lv, d) for k, (lv, d) in P.items()]
