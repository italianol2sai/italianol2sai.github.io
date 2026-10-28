"""Letture dai Moduli Google del corso Classroom, rifatte come esercizi del sito.
I testi sono riscritti in parole semplici a partire dai Moduli di Erila."""
from genera import eq, has, all_

VF = ["VERO", "FALSO"]

SOFIA = ("<p><b>MI CHIAMO SOFIA</b></p>"
 "<p>MI CHIAMO SOFIA E HO 35 ANNI. ABITO IN UN PICCOLO PAESE IN CAMPAGNA, IN UNA BELLA CASA CON IL CORTILE. "
 "NELLA MIA FAMIGLIA SIAMO IN CINQUE.</p>"
 "<p>MIO MARITO SI CHIAMA ALESSANDRO E HA 36 ANNI. FA L'OPERAIO IN UNA FABBRICA. È UNA PERSONA MOLTO GENTILE "
 "E GIOCA SPESSO CON I BAMBINI.</p>"
 "<p>ABBIAMO TRE FIGLI: ANDREA VA ALL'ASILO, MARTINA E GIACOMO VANNO ALLA SCUOLA ELEMENTARE. "
 "AI BAMBINI PIACE GIOCARE A TANTI GIOCHI DIVERSI NEL CORTILE.</p>"
 "<p>I GENITORI DI ALESSANDRO ABITANO LONTANO, IN CITTÀ. I MIEI GENITORI INVECE ABITANO VICINO A NOI, NELLO STESSO PAESE: "
 "AMANO I BAMBINI E LI GUARDANO SPESSO.</p>"
 "<p>ANCHE MIA SORELLA GIULIA ABITA VICINO, CON LA SUA FAMIGLIA. SUA FIGLIA MARTA GIOCA SPESSO CON I MIEI FIGLI.</p>"
 "<p>IO SONO CASALINGA, MA LAVORO ANCHE DA CASA: SCRIVO ARTICOLI, SONO UN'ARTICOLISTA. SONO MOLTO FELICE DELLA MIA FAMIGLIA.</p>")

PIRLO = ("<p><b>La mia famiglia</b></p>"
 "<p>Mi chiamo Gennaro Pirlo, ho 37 anni e faccio lo scrittore e il giornalista. "
 "Mia moglie si chiama Antonella Totti, ha 35 anni ed è un'attrice di teatro.</p>"
 "<p>Abbiamo due figli: Manuela, che ha 17 anni, e Marco, che ne ha 15. Tutti e due frequentano il liceo scientifico "
 "e hanno buoni voti. Marco fa il DJ e suona la batteria, Manuela invece dipinge: è una pittrice.</p>"
 "<p>In famiglia c'è anche Tremendo, il nostro cane, che ha 9 anni. Abitiamo in una casa con un grande giardino.</p>")

FAMIGLIA = {
 "title": "👨‍👩‍👧 Letture sulla famiglia · Esercizi",
 "store": "letture-famiglia",
 "sections": [
  {"part": "LIVELLO A1 · MI CHIAMO SOFIA"},
  {"id": "sofia", "title": "📖 LEGGI: MI CHIAMO SOFIA", "type": "info", "info": SOFIA},
  {"id": "e1", "title": "1 · SCEGLI LA RISPOSTA GIUSTA", "short": "1 · Sofia", "type": "choice", "full": True,
   "items": [{"q": "1. QUANTI FIGLI HANNO SOFIA E ALESSANDRO?", "opts": ["HANNO UN FIGLIO", "HANNO DUE FIGLI", "NON HANNO FIGLI", "HANNO TRE FIGLI"]},
             {"q": "2. CHE LAVORO FA SOFIA?", "opts": ["LA COMMESSA", "LA DOTTORESSA", "L'ARTICOLISTA", "L'OPERAIA"]},
             {"q": "3. CHI È MARTA?", "opts": ["LA FIGLIA DI SOFIA E ALESSANDRO", "LA SORELLA DI SOFIA", "LA SORELLA DI ALESSANDRO", "LA NIPOTE DI SOFIA"]},
             {"q": "4. I GENITORI DI SOFIA…", "opts": ["… ABITANO IN CITTÀ", "… ABITANO ALL'ESTERO", "… ABITANO VICINO A LEI, NELLO STESSO PAESE", "… ABITANO CON LEI"]},
             {"q": "5. I FIGLI DI SOFIA E ALESSANDRO…", "opts": ["… GIOCANO SPESSO AI VIDEOGIOCHI", "… GIOCANO A TANTI GIOCHI NEL CORTILE", "… GIOCANO NEL GIARDINO DELLA SCUOLA", "… LITIGANO MOLTO SPESSO"]}],
   "k": [eq("HANNO TRE FIGLI"), eq("L'ARTICOLISTA"), eq("LA NIPOTE DI SOFIA"),
         eq("… ABITANO VICINO A LEI, NELLO STESSO PAESE"), eq("… GIOCANO A TANTI GIOCHI NEL CORTILE")]},
  {"id": "e2", "title": "2 · CHI È? SCRIVI IL NOME", "short": "2 · Chi è", "type": "text",
   "bank": "ALESSANDRO · ANDREA · GIULIA · MARTA · SOFIA",
   "items": [{"q": q} for q in ["1. HA 35 ANNI E SCRIVE ARTICOLI.", "2. È IL MARITO DI SOFIA.", "3. VA ALL'ASILO.",
                                 "4. È LA SORELLA DI SOFIA.", "5. È LA FIGLIA DI GIULIA."]],
   "k": [eq(a) for a in ["sofia", "alessandro", "andrea", "giulia", "marta"]]},

  {"part": "Livello A2 · La mia famiglia"},
  {"id": "pirlo", "title": "📖 Leggi: la famiglia Pirlo", "type": "info", "info": PIRLO},
  {"id": "e3", "title": "3 · Scegli la risposta giusta", "short": "3 · La famiglia Pirlo", "type": "choice", "full": True,
   "items": [{"q": "1. Quanti anni ha il padre, Gennaro Pirlo?", "opts": ["33", "47", "27", "37"]},
             {"q": "2. Quanti anni ha la madre, Antonella Totti?", "opts": ["15", "25", "35", "45"]},
             {"q": "3. Quanti figli hanno Antonella e Gennaro?", "opts": ["3", "17", "2", "15"]},
             {"q": "4. Chi è Tremendo?", "opts": ["Il figlio DJ", "Il cane che ha 9 anni", "Il terzo figlio", "La figlia pittrice"]},
             {"q": "5. Che lavoro fa il padre?", "opts": ["DJ e scrittore", "Batterista e giornalista", "Giornalista e scrittore", "Attore di teatro"]}],
   "k": [eq("37"), eq("35"), eq("2"), eq("Il cane che ha 9 anni"), eq("Giornalista e scrittore")]},
  {"id": "e4", "title": "4 · Vero o falso?", "short": "4 · Vero o falso", "type": "choice", "opts": VF,
   "items": [{"q": q} for q in ["1. Antonella è un'attrice di teatro.", "2. Manuela suona la batteria.",
                                 "3. I figli vanno al liceo scientifico.", "4. La famiglia abita in un appartamento senza giardino."]],
   "k": [eq(a) for a in ["VERO", "FALSO", "VERO", "FALSO"]]},
  {"id": "e5", "title": "5 ✎ · E la tua famiglia?", "type": "free", "rows": 5,
   "items": ["Scrivi 4 o 5 frasi sulla tua famiglia: come si chiamano, quanti anni hanno, che lavoro fanno, dove abitano."]},
 ]
}

CARLO = ("<p><b>LA GIORNATA DI CARLO</b></p>"
 "<p>CIAO, MI CHIAMO CARLO E HO 18 ANNI. LA MATTINA MI SVEGLIO ALLE 7:00. A COLAZIONE BEVO IL TÈ CON I BISCOTTI.</p>"
 "<p>ALLE 7:40 INCONTRO IL MIO AMICO MARCO E PRENDIAMO L'AUTOBUS PER ANDARE A SCUOLA. LA MIA SCUOLA MI PIACE MOLTO "
 "PERCHÉ HA TANTE MATERIE DI INFORMATICA. HO SEI ORE DI LEZIONE OGNI GIORNO, MA IL SABATO NE HO SOLO CINQUE.</p>"
 "<p>IL POMERIGGIO STUDIO, POI GIOCO AL COMPUTER. LA SERA SUONO LA CHITARRA.</p>"
 "<p>ALLE 19:00 CENO CON LA MIA FAMIGLIA: MIO PADRE, MIA MADRE E I MIEI TRE FRATELLI. "
 "DOPO CENA LEGGO UN PO' E VERSO LE 22:30 VADO A LETTO.</p>")

GIORNATA = {
 "title": "☀️ La giornata · Esercizi",
 "store": "letture-giornata",
 "upper": True,
 "sections": [
  {"part": "LA GIORNATA DI CARLO"},
  {"id": "carlo", "title": "📖 LEGGI: LA GIORNATA DI CARLO", "type": "info", "info": CARLO},
  {"id": "e1", "title": "1 · SCEGLI LA RISPOSTA GIUSTA", "short": "1 · Carlo", "type": "choice", "full": True,
   "items": [{"q": "1. QUANTI ANNI HA CARLO?", "opts": ["18 ANNI", "20 ANNI", "16 ANNI", "15 ANNI"]},
             {"q": "2. CHE COSA MANGIA CARLO A COLAZIONE?", "opts": ["UNO YOGURT CON I BISCOTTI", "IL TÈ CON I BISCOTTI", "UN CAFFÈ", "UN FRUTTO"]},
             {"q": "3. A CARLO LA SUA SCUOLA…", "opts": ["PIACE PERCHÉ HA TANTE MATERIE DI ELETTRONICA", "PIACE PERCHÉ HA TANTE MATERIE DI INFORMATICA", "PIACE PERCHÉ HA TANTE LINGUE", "NON PIACE MOLTO"]},
             {"q": "4. CHE COSA SUONA CARLO LA SERA?", "opts": ["LA CHITARRA", "IL PIANOFORTE", "IL BASSO", "IL VIOLINO"]},
             {"q": "5. A CHE ORA CENA CARLO CON LA SUA FAMIGLIA?", "opts": ["ALLE 19:00", "ALLE 20:00", "ALLE 19:30", "ALLE 18:45"]},
             {"q": "6. LE ORE DI SCUOLA DI CARLO…", "opts": ["SONO 6 OGNI GIORNO, TRANNE IL SABATO", "SONO 5 OGNI GIORNO, TRANNE IL SABATO", "SONO 6 OGNI GIORNO", "SONO 5 OGNI GIORNO"]}],
   "k": [eq("18 ANNI"), eq("IL TÈ CON I BISCOTTI"), eq("PIACE PERCHÉ HA TANTE MATERIE DI INFORMATICA"),
         eq("LA CHITARRA"), eq("ALLE 19:00"), eq("SONO 6 OGNI GIORNO, TRANNE IL SABATO")]},
  {"id": "e2", "title": "2 · COMPLETA CON IL VERBO", "short": "2 · I verbi", "type": "cloze",
   "bank": "BEVO · CENO · MI SVEGLIO · PRENDIAMO · SUONO · VADO",
   "parts": ["LA MATTINA ", {}, " ALLE 7:00. A COLAZIONE ", {}, " IL TÈ. CON MARCO ", {}, " L'AUTOBUS. LA SERA ", {},
             " LA CHITARRA. ALLE 19:00 ", {}, " CON LA MIA FAMIGLIA. ALLE 22:30 ", {}, " A LETTO."],
   "k": [eq("mi sveglio"), eq("bevo"), eq("prendiamo"), eq("suono"), eq("ceno"), eq("vado")]},

  {"part": "LA MIA GIORNATA"},
  {"id": "e3", "title": "3 ✎ · DESCRIVI LA TUA GIORNATA", "type": "free", "rows": 8,
   "items": ["USA I VERBI: SVEGLIARSI · ALZARSI · FARE COLAZIONE · FARE LA DOCCIA · VESTIRSI · USCIRE DI CASA · "
             "ANDARE A SCUOLA / ANDARE AL LAVORO · PRANZARE · TORNARE A CASA · CENARE · GUARDARE LA TV · ANDARE A LETTO · ADDORMENTARSI. "
             "ESEMPIO: LA MATTINA MI SVEGLIO ALLE 7…"]},
 ]
}

DOTTORE = ("<p><b>DAL DOTTORE</b></p>"
 "<p><b>EL ASSANI:</b> BUONGIORNO, DOTTORE.<br><b>DOTTORE:</b> BUONGIORNO.<br>"
 "<b>EL ASSANI:</b> SONO IL SIGNOR EL ASSANI. LEI È IL DOTTOR CANNAVALE?<br><b>DOTTORE:</b> SÌ, SONO IO. MI DICA.<br>"
 "<b>EL ASSANI:</b> DA QUALCHE GIORNO NON MI SENTO BENE. HO MAL DI TESTA, MAL DI GOLA E LA TOSSE.<br>"
 "<b>DOTTORE:</b> HA ANCHE LA FEBBRE?<br><b>EL ASSANI:</b> SÌ, 37,8. E IERI SERA HO VOMITATO.<br>"
 "<b>DOTTORE:</b> VEDIAMO… (IL DOTTORE LO VISITA) NON È NIENTE DI GRAVE: HA L'INFLUENZA E UN PO' DI BRONCHITE. LEI FUMA?<br>"
 "<b>EL ASSANI:</b> SÌ, FUMO MOLTO.<br>"
 "<b>DOTTORE:</b> DEVE SMETTERE, IL FUMO FA MALE. IN QUESTI GIORNI DEVE STARE A LETTO E MANGIARE LEGGERO. "
 "PRENDA QUESTE PASTIGLIE: TRE AL GIORNO, DOPO I PASTI, PER UNA SETTIMANA. "
 "E PRENDA ANCHE LO SCIROPPO: DUE CUCCHIAI AL GIORNO, UNO LA MATTINA E UNO LA SERA PRIMA DI DORMIRE. ECCO LA RICETTA.<br>"
 "<b>EL ASSANI:</b> DOVE COMPRO LE MEDICINE?<br>"
 "<b>DOTTORE:</b> IN FARMACIA. IN CITTÀ CI SONO TANTE FARMACIE E OGNI COMUNE HA LA SUA. PER QUESTE MEDICINE SERVE LA RICETTA DEL MEDICO: "
 "IN FARMACIA LEI DÀ LA RICETTA E PAGA IL TICKET.<br>"
 "<b>EL ASSANI:</b> CHE COS'È IL TICKET?<br><b>DOTTORE:</b> È UNA PARTE DEL PREZZO DELLA MEDICINA.<br>"
 "<b>EL ASSANI:</b> GRAZIE, DOTTORE. ARRIVEDERCI.<br><b>DOTTORE:</b> ARRIVEDERCI.</p>")

BERTINE = ("<p><b>AL TELEFONO</b></p>"
 "<p><b>SEGRETARIA:</b> BUONGIORNO, STUDIO MEDICO, MI DICA.<br><b>BERTINE:</b> SALVE, VORREI PRENDERE UN APPUNTAMENTO.<br>"
 "<b>SEGRETARIA:</b> VEDIAMO… VA BENE GIOVEDÌ ALLE 15:00?<br><b>BERTINE:</b> SÌ, PERFETTO! GRAZIE E BUON LAVORO.<br>"
 "<b>SEGRETARIA:</b> GRAZIE A LEI, ARRIVEDERCI.</p>"
 "<p><b>IN AMBULATORIO</b></p>"
 "<p><b>DOTTORESSA:</b> AVANTI IL PROSSIMO!<br><b>BERTINE:</b> BUONGIORNO, DOTTORESSA. POSSO?<br>"
 "<b>DOTTORESSA:</b> PREGO, SIGNORA, SI ACCOMODI. COME STA?<br><b>BERTINE:</b> COSÌ COSÌ… NON MI SENTO BENE.<br>"
 "<b>DOTTORESSA:</b> CHE COSA HA?<br>"
 "<b>BERTINE:</b> LA NOTTE DORMO POCO, MI FA MALE LA SCHIENA, HO SPESSO LA NAUSEA E MI SENTO DEBOLE. CHE COSA DEVO PRENDERE?<br>"
 "<b>DOTTORESSA:</b> PRIMA DEVE FARE LE ANALISI DEL SANGUE E NON DEVE FARE SFORZI. POI FISSIAMO UN ALTRO APPUNTAMENTO.<br>"
 "<b>BERTINE:</b> GRAZIE, DOTTORESSA. ARRIVEDERCI.</p>")

DEF = ["PERSONA MALATA CHE HA BISOGNO DELLE CURE DI UN MEDICO",
       "EDIFICIO, DI SOLITO MOLTO GRANDE, DOVE SI CURANO I MALATI",
       "MEDICO SPECIALIZZATO IN UNA PARTE DELLA MEDICINA",
       "LOCALE DOVE IL MEDICO RICEVE E VISITA I PAZIENTI",
       "NEGOZIO CHE VENDE MEDICINE E ARTICOLI SANITARI",
       "PERSONA LAUREATA IN MEDICINA CHE CURA I MALATI",
       "FOGLIO DEL MEDICO CON LE MEDICINE E LA CURA DA SEGUIRE",
       "MEDICO SPECIALISTA CHE FA LE OPERAZIONI",
       "UNA PARTE DELL'OSPEDALE",
       "PERSONA CHE LAVORA CON I MEDICI E SI OCCUPA DEI MALATI"]

DIAL_DOTTORE = {
 "title": "🩺 Dal dottore · Lettura ed esercizi",
 "store": "letture-dottore",
 "upper": True,
 "sections": [
  {"part": "IL DIALOGO"},
  {"id": "dial", "title": "📖 LEGGI IL DIALOGO", "type": "info", "info": DOTTORE},
  {"id": "e1", "title": "1 · VERO O FALSO?", "short": "1 · Vero o falso", "type": "choice", "opts": VF,
   "items": [{"q": q} for q in ["1. IL DOTTORE SI CHIAMA BIANCHI.", "2. IL SIGNOR EL ASSANI NON SI SENTE BENE.",
                                 "3. HA MAL DI PANCIA E DI STOMACO.", "4. HA ANCHE LA FEBBRE.", "5. IL DOTTORE DICE CHE HA L'INFLUENZA.",
                                 "6. EL ASSANI NON FUMA.", "7. EL ASSANI DEVE STARE A LETTO.", "8. NON DEVE PRENDERE LE PASTIGLIE.",
                                 "9. DEVE PRENDERE CINQUE PASTIGLIE AL GIORNO.", "10. EL ASSANI DEVE COMPRARE LE MEDICINE."]],
   "k": [eq(a) for a in ["FALSO", "VERO", "FALSO", "VERO", "VERO", "FALSO", "VERO", "FALSO", "FALSO", "VERO"]]},
  {"id": "e2", "title": "2 · LA CURA: COMPLETA", "short": "2 · La cura", "type": "cloze",
   "cons": "SCRIVI UN NUMERO O UNA PAROLA DEL DIALOGO.",
   "parts": ["PASTIGLIE: ", {}, " AL GIORNO, DOPO I PASTI, PER UNA ", {}, ".<br>SCIROPPO: ", {},
             " CUCCHIAI AL GIORNO, UNO LA MATTINA E UNO LA ", {}, ".<br>LE MEDICINE SI COMPRANO IN ", {},
             ". SERVE LA ", {}, " DEL MEDICO."],
   "k": [eq("tre", "3"), eq("settimana"), eq("due", "2"), eq("sera"), eq("farmacia"), eq("ricetta")]},
  {"id": "e3", "title": "3 · CHE COSA HA EL ASSANI?", "short": "3 · I sintomi", "type": "multi",
   "cons": "METTI LA SPUNTA VICINO ALLE 5 COSE GIUSTE.",
   "items": ["MAL DI TESTA", "MAL DI DENTI", "MAL DI GOLA", "LA TOSSE", "MAL DI SCHIENA", "LA FEBBRE", "HA VOMITATO"],
   "k": [eq(a) for a in ["X", "-", "X", "X", "-", "X", "X"]]},

  {"part": "DALLA DOTTORESSA"},
  {"id": "bertine", "title": "📖 LEGGI: BERTINE DALLA DOTTORESSA", "type": "info", "info": BERTINE},
  {"id": "e4", "title": "4 · RISPONDI", "short": "4 · Bertine", "type": "text", "w": "w",
   "items": [{"q": q} for q in ["1. DOVE SI INCONTRANO BERTINE E LA DOTTORESSA? (NELL'…)", "2. COME STA BERTINE?",
                                 "3. CHE COSA DEVE FARE BERTINE?", "4. CHE COSA NON DEVE FARE?", "5. QUANDO È L'APPUNTAMENTO? (GIORNO E ORA)"]],
   "k": [has("ambulatorio", "studio"), has("così così", "cosi cosi", "non sta bene", "non si sente bene", "male"),
         has("analisi"), has("sforzi"), all_(["giovedi", "giovedì"], ["15"])]},

  {"part": "L'ITALIANO DAL DOTTORE"},
  {"id": "v1", "title": "5 · CHE COSA SIGNIFICA? SCEGLI", "short": "5 · Le parole", "type": "select",
   "img": "img/dottori.jpg", "alt": "QUATTRO DOTTORI",
   "opts": DEF,
   "items": [{"q": q} for q in ["1. AMBULATORIO", "2. CHIRURGO", "3. FARMACIA", "4. INFERMIERE", "5. MALATO / PAZIENTE",
                                 "6. MEDICO / DOTTORE", "7. OSPEDALE", "8. PRESCRIZIONE / RICETTA", "9. REPARTO"]],
   "k": [eq(DEF[i]) for i in [3, 7, 4, 9, 0, 5, 1, 6, 8]]},
  {"id": "v2", "title": "6 · COMPLETA LE FRASI", "short": "6 · Completa", "type": "cloze",
   "bank": "AMBULATORIO · CHIRURGO · FARMACIA · INFERMIERA · MALATO · MEDICO · OSPEDALE · RICETTA · REPARTO · SPECIALISTA",
   "parts": ["1. IL ", {}, " È STATO RICOVERATO D'URGENZA ALL'", {}, " CON UN DISTURBO ALLE VIE RESPIRATORIE.<br>",
             "2. SONO ANDATO IN ", {}, ", MA NON HO POTUTO COMPRARE LE MEDICINE PERCHÉ NON AVEVO LA ", {}, " MEDICA.<br>",
             "3. L'", {}, " DEL MEDICO SI TROVA IN PIAZZA GARIBALDI.<br>",
             "4. IL ", {}, " È UN MEDICO ", {}, ": SE DEVI OPERARTI, DEVI ANDARE DA LUI.<br>",
             "5. IL ", {}, " LE HA CONSIGLIATO DI PRENDERSI UN PERIODO DI VACANZA.<br>",
             "6. GIOVANNA FA L'", {}, ", LAVORA ALL'OSPEDALE NEL ", {}, " DI CHIRURGIA."],
   "k": [eq("malato", "paziente"), eq("ospedale"), eq("farmacia"), eq("ricetta", "prescrizione"), eq("ambulatorio"),
         eq("chirurgo"), eq("specialista"), eq("medico", "dottore"), eq("infermiera"), eq("reparto")]},
  {"id": "v3", "title": "7 · VISITARE, CURARE, GUARIRE", "short": "7 · I verbi", "type": "cloze",
   "cons": "COMPLETA CON IL VERBO GIUSTO O CON UN NOME (LA CURA, LA VISITA, LA GUARIGIONE).",
   "parts": ["1. LA ", {}, " CHE MI HA DATO IL DOTTORE HA FUNZIONATO: IN POCHI GIORNI SANDRA ", {}, " (GUARIRE).<br>",
             "2. ORARIO DI ", {}, ": DAL LUNEDÌ AL GIOVEDÌ, DALLE 15:00 ALLE 18:00.<br>",
             "3. DOMANI MATTINA IL DOTTORE ", {}, " (VISITARE) I PAZIENTI NEL SUO AMBULATORIO.<br>",
             "4. QUELLE MEDICINE SONO MIRACOLOSE: MI ", {}, " (CURARE) PERFETTAMENTE DALLA MALATTIA.<br>",
             "5. IL PAZIENTE STA MOLTO MEGLIO: È IN VIA DI ", {}, "."],
   "k": [eq("cura", "terapia"), eq("è guarita", "e guarita", "guarisce"), eq("visita", "visite"), eq("visiterà", "visitera", "visita"),
         eq("hanno curato", "hanno curata", "curano"), eq("guarigione")]},
 ]
}

UFFICIO = ("<p><b>Nell'ufficio del datore di lavoro</b></p>"
 "<p><b>Francesco:</b> Permesso?<br><b>Massimo:</b> Oh, Francesco! Vieni, entra. Come va il lavoro? Tutto bene?<br>"
 "<b>Francesco:</b> Molto bene, grazie. Mi trovo bene nella ditta di giardinaggio.<br>"
 "<b>Massimo:</b> Mi fa piacere. Ti ho chiamato perché voglio offrirti un nuovo lavoro.<br><b>Francesco:</b> Di che cosa si tratta?<br>"
 "<b>Massimo:</b> Io curo i giardini dei clienti, tutti a circa 50 km dalla città. La settimana scorsa il mio socio è andato via "
 "e adesso ho tanto lavoro in ufficio: i conti, l'organizzazione e altri impegni a Pistoia. Mi serve un esperto di giardinaggio "
 "per dividere a metà i turni fuori. Mi puoi aiutare?<br>"
 "<b>Francesco:</b> Certo! Credo di essere la persona giusta.<br><b>Massimo:</b> Lo penso anch'io. So che hai già esperienza.<br>"
 "<b>Francesco:</b> Sì, per due anni ho curato i parchi pubblici in Umbria, vicino a Perugia. Il giardinaggio è la mia passione.<br>"
 "<b>Massimo:</b> Allora facciamo così: io lavoro nei giorni dispari, lunedì, mercoledì e venerdì, e tu nei giorni pari, "
 "martedì, giovedì e sabato. Sono mezze giornate, dalle 9:00 alle 14:00. Che ne pensi?<br>"
 "<b>Francesco:</b> Va benissimo, mi interessa molto. Posso cominciare quando vuole.<br>"
 "<b>Massimo:</b> Ci vediamo domani per i dettagli; se serve, possiamo cambiare i turni. Hai la macchina?<br>"
 "<b>Francesco:</b> Sì, un mese fa ho comprato una macchina usata. Non è nuova, ma va bene.<br>"
 "<b>Massimo:</b> Perfetto. Allora domani alle 9:00. E diamoci del tu: chiamami Massimo.<br>"
 "<b>Francesco:</b> Va bene, signor Santinelli… cioè, Massimo! A domani.<br><b>Massimo:</b> A domani, buona giornata!</p>")

TRENO = ("<p><b>Parlare di lavoro</b></p>"
 "<p>Francesco e Marina si incontrano dopo il lavoro.</p>"
 "<p><b>Marina:</b> Ciao Francesco! Prendi il treno delle 14?<br>"
 "<b>Francesco:</b> Sì. Andiamo insieme alla stazione? Sai, il mio capo mi ha offerto un nuovo lavoro: curare i giardini con lui.<br>"
 "<b>Marina:</b> Complimenti! Sei contento?<br>"
 "<b>Francesco:</b> Contentissimo. Ho fatto tanti lavori diversi, ma forse adesso ho trovato quello giusto per me.<br>"
 "<b>Marina:</b> È vero, hai fatto tanti lavori.<br>"
 "<b>Francesco:</b> Dopo il diploma ho lavorato in un call center: telefonavo alle persone per un sondaggio sui prodotti alimentari.<br>"
 "<b>Marina:</b> Anch'io ho lavorato in un call center: vendevo assicurazioni.<br>"
 "<b>Francesco:</b> A me non piaceva: era stressante e la gente non voleva parlare di cibo al telefono. "
 "Poi ho lavorato in un ufficio marketing: non era male, ma stavo troppe ore chiuso dentro.<br>"
 "<b>Marina:</b> E hai lavorato anche in Umbria, vero?<br>"
 "<b>Francesco:</b> Sì, ho curato i parchi con un contratto di due anni, finito due mesi fa. "
 "Un mese fa ho risposto a un annuncio sul giornale di una ditta di giardinaggio, ho telefonato e ho fatto il colloquio.<br>"
 "<b>Marina:</b> E adesso lavori lì?<br>"
 "<b>Francesco:</b> Sì. Il direttore mi è piaciuto subito e dopo una settimana ho cominciato nel reparto spedizioni, "
 "con le piante da giardino e da appartamento. Da domani torno a lavorare all'aperto: non vedo l'ora!<br>"
 "<b>Marina:</b> Anch'io ho fatto tanti lavori: la baby-sitter, la commessa, la cameriera in un bar. "
 "Intanto studiavo lingua e letteratura italiana all'università. Dopo la laurea ho capito che volevo insegnare: "
 "da due anni insegno italiano agli stranieri.<br>"
 "<b>Francesco:</b> Ti piace il tuo lavoro?<br>"
 "<b>Marina:</b> Moltissimo. Conosco persone di paesi e culture diverse e imparo a capire le differenze tra popoli e lingue.<br>"
 "<b>Francesco:</b> Io invece per ora conosco le differenze tra le piante… ma sono contento così!</p>")

LAVORO = {
 "title": "💼 Dialoghi sul lavoro · Esercizi",
 "store": "letture-lavoro",
 "sections": [
  {"part": "Livello A2 · Parlare di lavoro"},
  {"id": "treno", "title": "📖 Leggi: Francesco e Marina", "type": "info", "info": TRENO},
  {"id": "e1", "title": "1 · Vero o falso?", "short": "1 · Francesco e Marina", "type": "choice", "opts": VF,
   "items": [{"q": q} for q in ["1. Francesco e Marina prendono il treno delle 14.", "2. Il capo ha offerto a Francesco un nuovo lavoro.",
                                 "3. A Francesco piaceva molto lavorare nel call center.", "4. In Umbria Francesco ha curato i parchi per due anni.",
                                 "5. Adesso Francesco lavora in un ufficio marketing.", "6. Marina ha studiato lingua e letteratura italiana.",
                                 "7. Marina insegna italiano agli stranieri da cinque anni.", "8. A Marina piace conoscere persone di culture diverse."]],
   "k": [eq(a) for a in ["VERO", "VERO", "FALSO", "VERO", "FALSO", "VERO", "FALSO", "VERO"]]},
  {"id": "e2", "title": "2 · Rispondi", "short": "2 · Domande", "type": "text", "w": "w",
   "items": [{"q": q} for q in ["1. Come ha trovato Francesco la ditta di giardinaggio? (con un annuncio sul…)",
                                 "2. In quale reparto ha cominciato Francesco?",
                                 "3. Scrivi un lavoro che ha fatto Marina quando studiava."]],
   "k": [has("giornale"), has("spedizion"), has("baby", "commess", "cameriera")]},

  {"part": "Livello A2 · Nell'ufficio del datore di lavoro"},
  {"id": "uff", "title": "📖 Leggi: Francesco e Massimo", "type": "info", "info": UFFICIO},
  {"id": "e3", "title": "3 · Scegli la risposta giusta", "short": "3 · In ufficio", "type": "choice", "full": True,
   "items": [{"q": "1. Il dialogo tra Francesco Paolini e il suo datore di lavoro si svolge…", "opts": ["in ufficio", "al bar", "per la strada"]}],
   "k": [eq("in ufficio")]},
  {"id": "e4", "title": "4 · Vero o falso?", "short": "4 · Vero o falso", "type": "choice", "opts": VF,
   "items": [{"q": q} for q in ["1. Il datore di lavoro chiede a Francesco di aiutarlo nel suo lavoro.",
                                 "2. Francesco dovrebbe occuparsi dei giardini pubblici.",
                                 "3. Francesco è un appassionato di giardinaggio.",
                                 "4. Francesco vuole comprare una macchina nuova.",
                                 "5. Francesco e il suo datore di lavoro fissano un incontro per il pomeriggio del giorno dopo."]],
   "k": [eq(a) for a in ["VERO", "FALSO", "VERO", "FALSO", "FALSO"]]},
  {"id": "e5", "title": "5 · I turni: completa", "short": "5 · I turni", "type": "cloze",
   "parts": ["Massimo lavora il lunedì, il mercoledì e il ", {}, ". Francesco lavora il martedì, il giovedì e il ", {},
             ". I turni sono dalle 9:00 alle ", {}, "."],
   "k": [eq("venerdì", "venerdi"), eq("sabato"), eq("14", "14:00", "quattordici")]},
  {"id": "e6", "title": "6 ✎ · E tu?", "type": "free", "rows": 5,
   "items": ["Che lavori hai fatto? Che lavoro fai adesso o vuoi fare? Scrivi 4 o 5 frasi."]},
 ]
}

NEGOZIO_T = ("<p><b>In un negozio di abbigliamento</b></p>"
 "<p><b>Commessa:</b> Buongiorno, posso aiutarla?<br><b>Ragazza:</b> Sì, grazie. Cerco una gonna di velluto, bianca o beige.<br>"
 "<b>Commessa:</b> È per lei?<br><b>Ragazza:</b> Sì.<br><b>Commessa:</b> Che taglia porta?<br><b>Ragazza:</b> La 40 o la 42.<br>"
 "<b>Commessa:</b> Che ne dice di questa?<br><b>Ragazza:</b> Non è male, ma è troppo corta. Non mi piace.<br>"
 "<b>Commessa:</b> E questa?<br><b>Ragazza:</b> Questa è perfetta! Quanto costa?<br><b>Commessa:</b> 169 euro.<br>"
 "<b>Ragazza:</b> È un po' cara. Ha qualcosa di meno caro, dello stesso stile?<br>"
 "<b>Commessa:</b> Sì, questa è in saldo: costa 68 euro.<br>"
 "<b>Ragazza:</b> La prendo. Non la provo, mi sembra la mia taglia. Se non va bene, posso cambiarla?<br>"
 "<b>Commessa:</b> Certo, ma conservi lo scontrino. Come paga?<br><b>Ragazza:</b> In contanti.<br>"
 "<b>Commessa:</b> Ecco il resto e lo scontrino. Arrivederci!<br><b>Ragazza:</b> Grazie, arrivederci!</p>")

NEGOZIO = {
 "title": "🛍️ In un negozio di abbigliamento · Esercizi",
 "store": "letture-negozio",
 "sections": [
  {"part": "Livello A2"},
  {"id": "dial", "title": "📖 Leggi il dialogo", "type": "info", "info": NEGOZIO_T},
  {"id": "e1", "title": "1 · Scegli la risposta giusta", "short": "1 · Scegli", "type": "choice", "full": True,
   "items": [{"q": "1. Che taglia porta la ragazza?", "opts": ["la 40 o la 42", "la 44", "la 46"]},
             {"q": "2. La ragazza può cambiare la gonna se non è la sua taglia?", "opts": ["sì, con lo scontrino", "no, mai"]},
             {"q": "3. Come paga la ragazza?", "opts": ["in contanti", "con il bancomat"]}],
   "k": [eq("la 40 o la 42"), eq("sì, con lo scontrino"), eq("in contanti")]},
  {"id": "e2", "title": "2 · Rispondi", "short": "2 · Domande", "type": "text",
   "items": [{"q": q} for q in ["1. Che cosa cerca la ragazza? (una …)", "2. Quanto costa la gonna perfetta? (euro)",
                                 "3. Quanto costa la gonna in saldo? (euro)", "4. Perché non le piace la prima gonna? È troppo …"]],
   "k": [has("gonna"), has("169"), has("68"), has("corta")]},
  {"id": "e3", "title": "3 · Che cosa dici al negozio?", "short": "3 · Le frasi", "type": "select",
   "opts": ["Che taglia porta?", "Quanto costa?", "Posso provarla?", "Come paga?", "Ha qualcosa di meno caro?"],
   "items": [{"q": q} for q in ["1. Vuoi sapere il prezzo.", "2. La commessa vuole sapere la tua taglia.",
                                 "3. Vuoi andare nel camerino.", "4. Il prezzo è troppo alto per te.", "5. La commessa vuole sapere: contanti o bancomat?"]],
   "k": [eq(a) for a in ["Quanto costa?", "Che taglia porta?", "Posso provarla?", "Ha qualcosa di meno caro?", "Come paga?"]]},
 ]
}

PERSONE = ("<p><b>CHI È?</b></p><ul>"
 "<li><b>MARCO</b> HA 7 ANNI, HA I CAPELLI A SPAZZOLA E SORRIDE SEMPRE. FA SPESSO GLI SCHERZI.</li>"
 "<li><b>ANDREA</b> È UNA PERSONA INTELLIGENTE. È CALVO E PORTA GLI OCCHIALI. LAVORA IN UN'AGENZIA DI PUBBLICITÀ ED È MOLTO BRAVO.</li>"
 "<li><b>ANNAMARIA</b> È UNA SIGNORA MOLTO SIMPATICA. HA I CAPELLI BIANCHI, MA PORTA SPESSO IL CAPPELLO. AMA CURARE I FIORI E STARE ALL'APERTO.</li>"
 "<li><b>VALERIO</b> È UN BALLERINO. È MOLTO MUSCOLOSO E ATLETICO. È UNA PERSONA SERIA E AMA IL SUO LAVORO.</li>"
 "<li><b>CLAUDIA</b> È BIONDA E HA GLI OCCHI AZZURRI. È UNA PERSONA RIFLESSIVA E A VOLTE INDECISA.</li>"
 "<li><b>GIUSEPPE</b> È ANZIANO, HA I CAPELLI BIANCHI ED È UN PO' ROBUSTO. LAVORA TANTO E NON SI STANCA MAI.</li>"
 "<li><b>GABRIELE</b> HA I CAPELLI CASTANI, ABBASTANZA LUNGHI. È UNA PERSONA POSITIVA E GENEROSA.</li>"
 "<li><b>EMMA</b> È UNA RAGAZZA MOLTO VIVACE. HA I CAPELLI RICCI E LA PELLE SCURA, È MAGRA E AMA DIVERTIRSI.</li>"
 "<li><b>ANNA</b> È BIONDA E MAGRA, PORTA GLI OCCHIALI E AMA IL SUO LAVORO.</li>"
 "<li><b>MARIO</b> È MORO E HA LA PELLE SCURA. SPESSO È TRISTE E NON SORRIDE MOLTO.</li>"
 "<li><b>MARIA</b> È MOLTO BELLA, BIONDA E MAGRA, CON LA PELLE CHIARA. È SEMPRE SORRIDENTE E STA ATTENTA ALLA LINEA.</li>"
 "<li><b>CHIARA</b> È UNA BAMBINA MOLTO SIMPATICA. HA I CAPELLI RICCI ED È SPESSO BIRICHINA.</li></ul>")

NOMI = ["MARCO", "ANDREA", "ANNAMARIA", "VALERIO", "CLAUDIA", "GIUSEPPE", "GABRIELE", "EMMA", "ANNA", "MARIO", "MARIA", "CHIARA"]

INDOVINA = {
 "title": "🕵️ Indovina chi · Esercizi",
 "store": "letture-indovina",
 "upper": True,
 "sections": [
  {"part": "DESCRIVERE LE PERSONE"},
  {"id": "pers", "title": "📖 LEGGI LE DESCRIZIONI", "type": "info", "info": PERSONE},
  {"id": "f1", "title": "1 · INDOVINA CHI: GUARDA LE FOTO", "short": "1 · Le foto", "type": "select", "opts": NOMI,
   "cons": "LEGGI LE DESCRIZIONI. CHI C'È NELLA FOTO? SCEGLI IL NOME.",
   "items": [{"q": f'<img src="img/indovina-{i:02d}.png" alt="FOTO {i}" style="width:120px;border-radius:8px;vertical-align:middle"> FOTO {i}'} for i in range(1, 13)],
   "k": [eq(a) for a in ["ANNA", "ANDREA", "CHIARA", "GABRIELE", "CLAUDIA", "GIUSEPPE",
                         "EMMA", "MARIA", "MARIO", "ANNAMARIA", "VALERIO", "MARCO"]]},
  {"id": "e1", "title": "2 · CHI È?", "short": "2 · Chi è", "type": "select", "opts": NOMI,
   "cons": "LEGGI E SCEGLI IL NOME.",
   "items": [{"q": q} for q in ["1. È CALVO E PORTA GLI OCCHIALI.", "2. AMA CURARE I FIORI.", "3. È UN BALLERINO.",
                                 "4. HA GLI OCCHI AZZURRI.", "5. HA 7 ANNI E FA GLI SCHERZI.", "6. È ANZIANO E LAVORA TANTO.",
                                 "7. HA I CAPELLI CASTANI E LUNGHI.", "8. È VIVACE E HA I CAPELLI RICCI E LA PELLE SCURA.",
                                 "9. È BIONDA, MAGRA E PORTA GLI OCCHIALI.", "10. SPESSO È TRISTE.",
                                 "11. È SEMPRE SORRIDENTE E STA ATTENTA ALLA LINEA.", "12. È UNA BAMBINA BIRICHINA."]],
   "k": [eq(a) for a in ["ANDREA", "ANNAMARIA", "VALERIO", "CLAUDIA", "MARCO", "GIUSEPPE",
                         "GABRIELE", "EMMA", "ANNA", "MARIO", "MARIA", "CHIARA"]]},
  {"id": "e2", "title": "3 · IL CONTRARIO", "short": "3 · Il contrario", "type": "select",
   "opts": ["BIONDO", "CHIARA", "CORTI", "GRASSO", "INFELICE", "LISCI", "TRISTE", "GIOVANE"],
   "cons": "SCEGLI L'AGGETTIVO CONTRARIO.",
   "items": [{"q": q} for q in ["1. MORO ↔", "2. PELLE SCURA ↔ PELLE", "3. CAPELLI LUNGHI ↔ CAPELLI", "4. MAGRO ↔",
                                 "5. SORRIDENTE ↔", "6. CAPELLI RICCI ↔ CAPELLI", "7. ANZIANO ↔"]],
   "k": [eq("BIONDO"), eq("CHIARA"), eq("CORTI"), eq("GRASSO"), eq("TRISTE", "INFELICE"), eq("LISCI"), eq("GIOVANE")]},
  {"part": "CHE DIFFERENZA C'È?"},
  {"id": "d1", "title": "4 · CHE DIFFERENZA C'È?", "short": "4 · Che differenza c'è", "type": "cloze",
   "img": "img/che-differenza.png", "alt": "DUE LAMPADE, DUE OMBRELLI, DUE BISTECCHE, DUE VASI",
   "cons": "GUARDA L'IMMAGINE: CI SONO 4 OGGETTI UGUALI MA… DIVERSI! SCRIVI GLI AGGETTIVI CONTRARI.",
   "bank": "ACCESA · APERTO · CHIUSO · COTTA · CRUDA · PIENO · SPENTA · VUOTO",
   "parts": ["1. LA LAMPADA A SINISTRA È ", {}, ", LA LAMPADA A DESTRA È ", {}, ".<br>",
             "2. L'OMBRELLO GRANDE È ", {}, ", L'OMBRELLO PICCOLO È ", {}, ".<br>",
             "3. LA BISTECCA A SINISTRA È ", {}, ", LA BISTECCA A DESTRA È ", {}, ".<br>",
             "4. IL VASO A SINISTRA È ", {}, ", IL VASO A DESTRA È ", {}, " (HA I FIORI)."],
   "k": [eq("spenta"), eq("accesa"), eq("aperto"), eq("chiuso"), eq("cruda"), eq("cotta"), eq("vuoto"), eq("pieno")]},
  {"id": "e3", "title": "5 ✎ · DESCRIVI UNA PERSONA", "type": "free", "rows": 5,
   "items": ["DESCRIVI UNA PERSONA CHE CONOSCI: COME SI CHIAMA, QUANTI ANNI HA, COM'È (CAPELLI, OCCHI, CARATTERE)."]},
 ]
}
