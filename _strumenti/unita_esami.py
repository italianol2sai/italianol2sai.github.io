"""Simulazioni d'esame A1 e A2 (2026-10-30), sul modello delle prove per gli adulti stranieri
(ascolto, lettura, scrittura, parlato). Testi e dialoghi scritti nuovi per il sito; gli ascolti sono letti
dalla voce del computer (campo "audio"). Tutto in STAMPATELLO MAIUSCOLO. Persone e indirizzi inventati."""
from genera import eq

def badge(p): return "%d PUNTI" % p

def ascolto(eid, title, audio, items, opts=None, cons=None, p=None):
    """items: (domanda, [opzioni] o None, giusta)"""
    d = {"id": eid, "title": title, "short": title, "type": "choice", "full": True, "audio": audio,
         "items": [({"q": q, "opts": o} if o else {"q": q}) for q, o, _ in items], "k": [eq(a) for _, _, a in items]}
    if opts: d["opts"] = opts
    if cons: d["cons"] = cons
    if p: d["badge"] = badge(p)
    return d

def lettura(eid, title, info, items, opts=None, cons=None, p=None):
    d = {"id": eid, "title": title, "short": title, "type": "choice", "full": True, "info": info,
         "items": [({"q": q, "opts": o} if o else {"q": q}) for q, o, _ in items], "k": [eq(a) for _, _, a in items]}
    if opts: d["opts"] = opts
    if cons: d["cons"] = cons
    if p: d["badge"] = badge(p)
    return d

def abbina(eid, title, opts, items, info=None, audio=None, cons=None, p=None):
    d = {"id": eid, "title": title, "short": title, "type": "select", "opts": opts,
         "items": [{"q": q} for q, _ in items], "k": [eq(a) for _, a in items]}
    if info: d["info"] = info
    if audio: d["audio"] = audio
    if cons: d["cons"] = cons
    if p: d["badge"] = badge(p)
    return d

VF = ["VERO", "FALSO"]
INTRO = {"part": "Come funziona"}

# =====================================================================
# A1 · SIMULAZIONE 1
# =====================================================================
A1_1 = {
 "title": "📝 Simulazione d'esame A1 · n. 1", "store": "esame-a1-1", "upper": True,
 "sections": [
  {"part": "Prova 1 · Ascolto"},
  ascolto("a1", "A1 · L'annuncio alla stazione",
          [("F", "ATTENZIONE. IL TRENO REGIONALE PER LECCE DELLE ORE NOVE E VENTI PARTIRÀ DAL BINARIO QUATTRO. "
                 "IL TRENO HA DIECI MINUTI DI RITARDO. CI SCUSIAMO PER IL DISAGIO.")],
          [("1. DOVE VA IL TRENO?", ["A LECCE", "A FOGGIA", "A ROMA"], "A LECCE"),
           ("2. A CHE ORA PARTE (SENZA RITARDO)?", ["ALLE 9:20", "ALLE 10:20", "ALLE 9:10"], "ALLE 9:20"),
           ("3. DA QUALE BINARIO?", ["4", "2", "10"], "4"),
           ("4. QUANTI MINUTI DI RITARDO?", ["10", "4", "20"], "10")],
          cons="ASCOLTA L'ANNUNCIO E SCEGLI LA RISPOSTA GIUSTA.", p=4),
  ascolto("a2", "A2 · Il messaggio in segreteria",
          [("F", "CIAO SAMIR, SONO GIULIA DELLA SCUOLA DI ITALIANO. DOMANI LA LEZIONE NON È ALLE NOVE MA ALLE DIECI. "
                 "PORTA IL QUADERNO E UNA FOTOGRAFIA PER LA TESSERA. A DOMANI, CIAO!")],
          [("1. CHI TELEFONA?", ["GIULIA, DELLA SCUOLA", "IL MEDICO", "UN AMICO DI SAMIR"], "GIULIA, DELLA SCUOLA"),
           ("2. A CHE ORA È LA LEZIONE DOMANI?", ["ALLE 10", "ALLE 9", "ALLE 11"], "ALLE 10"),
           ("3. CHE COSA DEVE PORTARE SAMIR?", ["IL QUADERNO E UNA FOTO", "IL PASSAPORTO", "I SOLDI"], "IL QUADERNO E UNA FOTO")],
          cons="ASCOLTA IL MESSAGGIO E SCEGLI LA RISPOSTA GIUSTA.", p=3),
  ascolto("a3", "A3 · Al mercato",
          [("M", "BUONGIORNO SIGNORA, CHE COSA LE DO?"), ("F", "BUONGIORNO. UN CHILO DI POMODORI E MEZZO CHILO DI CIPOLLE."),
           ("M", "ECCO. ALTRO?"), ("F", "SÌ, DUE LIMONI. QUANTO PAGO?"), ("M", "TRE EURO E CINQUANTA."),
           ("F", "ECCO A LEI CINQUE EURO."), ("M", "E UN EURO E CINQUANTA DI RESTO. GRAZIE, BUONA GIORNATA!")],
          [("1. LA SIGNORA COMPRA UN CHILO DI POMODORI.", None, "VERO"), ("2. COMPRA UN CHILO DI CIPOLLE.", None, "FALSO"),
           ("3. COMPRA DUE LIMONI.", None, "VERO"), ("4. PAGA TRE EURO E CINQUANTA.", None, "VERO"),
           ("5. LA SIGNORA DÀ DIECI EURO.", None, "FALSO")],
          opts=VF, cons="ASCOLTA IL DIALOGO. VERO O FALSO?", p=5),
  {"part": "Prova 2 · Lettura"},
  abbina("l1", "L1 · Dove leggi questi cartelli?", ["IN FARMACIA", "ALLA STAZIONE", "IN UN NEGOZIO", "ALL'OSPEDALE", "IN AUTOBUS"],
         [("1. «VIETATO PARLARE CON L'AUTISTA»", "IN AUTOBUS"), ("2. «SALDI -50%»", "IN UN NEGOZIO"),
          ("3. «PRONTO SOCCORSO · AMBULANZE»", "ALL'OSPEDALE"), ("4. «BINARI 1-5 · BIGLIETTERIA»", "ALLA STAZIONE"),
          ("5. «FARMACIA DI TURNO: VIA SPARANO 12»", "IN FARMACIA")],
         cons="SCEGLI IL POSTO GIUSTO.", p=5),
  lettura("l2", "L2 · Leggi l'avviso",
          "<b>CENTRO PER L'IMPIEGO DI BARI</b><br>DAL 3 AL 14 NOVEMBRE L'UFFICIO È APERTO SOLO LA MATTINA, DALLE 8:30 ALLE 12:30.<br>"
          "IL GIOVEDÌ È APERTO ANCHE IL POMERIGGIO, DALLE 15 ALLE 17.<br>PER PARLARE CON UN OPERATORE SERVE L'APPUNTAMENTO.<br>"
          "PORTA UN DOCUMENTO E IL CODICE FISCALE.",
          [("1. IL 5 NOVEMBRE ALLE 16 L'UFFICIO È APERTO.", None, "FALSO"), ("2. IL GIOVEDÌ ALLE 16 L'UFFICIO È APERTO.", None, "VERO"),
           ("3. PER PARLARE CON UN OPERATORE SERVE L'APPUNTAMENTO.", None, "VERO"), ("4. DEVO PORTARE LA TESSERA SANITARIA.", None, "FALSO")],
          opts=VF, cons="LEGGI E SCEGLI: VERO O FALSO?", p=4),
  lettura("l3", "L3 · Leggi il messaggio di Amina",
          "CIAO FATOU! SABATO È IL MIO COMPLEANNO. FACCIO UNA FESTA A CASA MIA, IN VIA CRISANZIO 40, ALLE 19. "
          "C'È ANCHE MIA SORELLA. PORTI TU IL DOLCE? IO PREPARO IL RISO E IL POLLO. RISPONDIMI, PER FAVORE! AMINA",
          [("1. QUANDO È LA FESTA?", ["SABATO ALLE 19", "DOMENICA ALLE 19", "SABATO ALLE 9"], "SABATO ALLE 19"),
           ("2. DOVE È LA FESTA?", ["A CASA DI AMINA", "AL RISTORANTE", "A CASA DI FATOU"], "A CASA DI AMINA"),
           ("3. CHE COSA PORTA FATOU?", ["IL DOLCE", "IL RISO", "IL POLLO"], "IL DOLCE"),
           ("4. CHI C'È ALLA FESTA?", ["ANCHE LA SORELLA DI AMINA", "SOLO AMINA E FATOU", "I COLLEGHI DI LAVORO"], "ANCHE LA SORELLA DI AMINA")],
          cons="LEGGI E SCEGLI LA RISPOSTA GIUSTA.", p=4),
  {"part": "Prova 3 · Scrittura"},
  {"id": "s1", "title": "S1 ✎ · Compila il modulo", "type": "free", "rows": 1,
   "cons": "SEI IN UNA PALESTRA. COMPILA IL MODULO IN STAMPATELLO. PUOI USARE DATI INVENTATI.",
   "items": ["NOME", "COGNOME", "DATA DI NASCITA", "NAZIONALITÀ", "INDIRIZZO", "NUMERO DI TELEFONO", "GIORNI IN CUI VUOI ANDARE IN PALESTRA"]},
  {"id": "s2", "title": "S2 ✎ · Rispondi ad Amina", "type": "free", "rows": 4,
   "cons": "RISPONDI AL MESSAGGIO DI AMINA (PROVA L3). SCRIVI 20-30 PAROLE: VAI ALLA FESTA? CHE DOLCE PORTI? A CHE ORA ARRIVI?",
   "items": ["IL TUO MESSAGGIO"]},
  {"part": "Prova 4 · Parlato"},
  {"id": "p1", "title": "P1 🎤 · Parla di te", "type": "record",
   "items": ["PRESENTATI: COME TI CHIAMI, DI DOVE SEI, QUANTI ANNI HAI, DOVE ABITI, CON CHI ABITI, CHE LAVORO FAI O VUOI FARE."]},
  {"id": "p2", "title": "P2 🎤 · Al bar", "type": "record",
   "items": ["SEI AL BAR. ORDINA UNA COSA DA BERE E UNA DA MANGIARE, CHIEDI QUANTO COSTA E SALUTA."]},
 ]
}

# =====================================================================
# A1 · SIMULAZIONE 2
# =====================================================================
A1_2 = {
 "title": "📝 Simulazione d'esame A1 · n. 2", "store": "esame-a1-2", "upper": True,
 "sections": [
  {"part": "Prova 1 · Ascolto"},
  ascolto("a1", "A1 · Dal medico: l'appuntamento",
          [("F", "STUDIO MEDICO, BUONGIORNO."), ("M", "BUONGIORNO. SONO OMAR DIALLO. VORREI UN APPUNTAMENTO CON IL DOTTOR RANIERI."),
           ("F", "CHE COSA HA?"), ("M", "HO MAL DI SCHIENA DA TRE GIORNI."),
           ("F", "VA BENE MERCOLEDÌ ALLE CINQUE DEL POMERIGGIO?"), ("M", "MERCOLEDÌ LAVORO. È POSSIBILE GIOVEDÌ?"),
           ("F", "GIOVEDÌ ALLE UNDICI. PORTI LA TESSERA SANITARIA."), ("M", "PERFETTO, GRAZIE. ARRIVEDERCI.")],
          [("1. CHE PROBLEMA HA OMAR?", ["MAL DI SCHIENA", "MAL DI DENTI", "LA FEBBRE"], "MAL DI SCHIENA"),
           ("2. DA QUANTI GIORNI?", ["TRE", "DUE", "CINQUE"], "TRE"),
           ("3. QUANDO È L'APPUNTAMENTO?", ["GIOVEDÌ ALLE 11", "MERCOLEDÌ ALLE 17", "GIOVEDÌ ALLE 17"], "GIOVEDÌ ALLE 11"),
           ("4. CHE COSA DEVE PORTARE?", ["LA TESSERA SANITARIA", "IL PASSAPORTO", "LA RICETTA"], "LA TESSERA SANITARIA")],
          cons="ASCOLTA LA TELEFONATA E SCEGLI LA RISPOSTA GIUSTA.", p=4),
  ascolto("a2", "A2 · Al supermercato",
          [("F", "GENTILI CLIENTI, OGGI LA FRUTTA È IN OFFERTA: LE MELE COSTANO UN EURO AL CHILO. "
                 "AL BANCO DEL PESCE CI SONO ORATE FRESCHE. IL SUPERMERCATO CHIUDE ALLE OTTO E MEZZA. GRAZIE.")],
          [("1. LE MELE COSTANO 1 EURO AL CHILO.", None, "VERO"), ("2. LA CARNE È IN OFFERTA.", None, "FALSO"),
           ("3. CI SONO ORATE FRESCHE.", None, "VERO"), ("4. IL SUPERMERCATO CHIUDE ALLE 20:30.", None, "VERO")],
          opts=VF, cons="ASCOLTA L'ANNUNCIO. VERO O FALSO?", p=4),
  abbina("a3", "A3 · Dove sono le persone?", ["IN BANCA", "AL RISTORANTE", "IN UN NEGOZIO DI VESTITI", "IN TAXI"],
         [("DIALOGO 1", "AL RISTORANTE"), ("DIALOGO 2", "IN UN NEGOZIO DI VESTITI"), ("DIALOGO 3", "IN TAXI"), ("DIALOGO 4", "IN BANCA")],
         audio=[("M", "DIALOGO UNO."), ("F", "PER ME UN PIATTO DI ORECCHIETTE E UNA BOTTIGLIA D'ACQUA."), ("M", "SUBITO, SIGNORA."),
                ("M", "DIALOGO DUE."), ("F", "POSSO PROVARE QUESTA GIACCA? HA LA TAGLIA QUARANTADUE?"), ("M", "SÌ, IL CAMERINO È LÀ."),
                ("M", "DIALOGO TRE."), ("F", "ALLA STAZIONE CENTRALE, PER FAVORE. QUANTO COSTA?"), ("M", "CIRCA QUINDICI EURO."),
                ("M", "DIALOGO QUATTRO."), ("F", "VORREI PRELEVARE CENTO EURO DAL MIO CONTO."), ("M", "MI DÀ UN DOCUMENTO, PER FAVORE?")],
         cons="ASCOLTA I 4 DIALOGHI E SCEGLI IL POSTO.", p=4),
  {"part": "Prova 2 · Lettura"},
  lettura("l1", "L1 · L'annuncio di lavoro",
          "<b>PIZZERIA «IL FARO» CERCA AIUTO CUOCO</b><br>LAVORO DAL MARTEDÌ ALLA DOMENICA, DALLE 18 ALLE 24.<br>"
          "NON SERVE ESPERIENZA: IMPARI CON NOI.<br>È IMPORTANTE PARLARE UN PO' L'ITALIANO.<br>"
          "MANDA IL CURRICULUM A: lavoro@ilfaro-bari.it OPPURE VIENI IN PIZZERIA IL LUNEDÌ MATTINA.",
          [("1. LA PIZZERIA CERCA…", ["UN AIUTO CUOCO", "UN CAMERIERE", "UN PIZZAIOLO CON ESPERIENZA"], "UN AIUTO CUOCO"),
           ("2. IL LUNEDÌ…", ["NON SI LAVORA", "SI LAVORA DALLE 18", "SI LAVORA TUTTO IL GIORNO"], "NON SI LAVORA"),
           ("3. L'ORARIO È…", ["LA SERA", "LA MATTINA", "IL POMERIGGIO"], "LA SERA"),
           ("4. PER CHIEDERE IL LAVORO POSSO…", ["MANDARE UN'EMAIL O ANDARE IL LUNEDÌ MATTINA", "SOLO TELEFONARE", "ANDARE LA DOMENICA SERA"],
            "MANDARE UN'EMAIL O ANDARE IL LUNEDÌ MATTINA")],
          cons="LEGGI E SCEGLI LA RISPOSTA GIUSTA.", p=4),
  abbina("l2", "L2 · Chi cerca che cosa?", ["ANNUNCIO A", "ANNUNCIO B", "ANNUNCIO C", "ANNUNCIO D"],
         [("1. KOFI CERCA UNA STANZA VICINO ALLA STAZIONE.", "ANNUNCIO B"), ("2. MARYAM VUOLE IMPARARE A USARE IL COMPUTER.", "ANNUNCIO D"),
          ("3. ALI VUOLE COMPRARE UNA BICICLETTA USATA.", "ANNUNCIO A"), ("4. BINTA CERCA LAVORO COME BABY-SITTER.", "ANNUNCIO C")],
         info="<b>A</b> · VENDO BICI DA UOMO, USATA MA IN BUONO STATO. 60 EURO.<br>"
              "<b>B</b> · AFFITTO CAMERA SINGOLA, 5 MINUTI A PIEDI DA BARI CENTRALE. 300 EURO AL MESE.<br>"
              "<b>C</b> · FAMIGLIA CON DUE BAMBINI CERCA RAGAZZA PER IL POMERIGGIO, DAL LUNEDÌ AL VENERDÌ.<br>"
              "<b>D</b> · CORSO GRATUITO DI INFORMATICA AL CENTRO CIVICO: OGNI MERCOLEDÌ ALLE 17.",
         cons="LEGGI GLI ANNUNCI E SCEGLI QUELLO GIUSTO PER OGNI PERSONA.", p=4),
  {"id": "l3", "title": "L3 · Completa il testo", "short": "L3 · Completa", "type": "cloze", "badge": badge(5),
   "cons": "SCRIVI LA PAROLA GIUSTA.", "bank": "ABITO · LAVORO · SONO · HO · VADO",
   "parts": ["MI CHIAMO HASSAN. ", {}, " EGIZIANO E ", {}, " 28 ANNI. ", {}, " A BARI CON MIO FRATELLO. ",
             {}, " IN UN MAGAZZINO. LA SERA ", {}, " A SCUOLA DI ITALIANO."],
   "k": [eq("sono"), eq("ho"), eq("abito"), eq("lavoro"), eq("vado")]},
  {"part": "Prova 3 · Scrittura"},
  {"id": "s1", "title": "S1 ✎ · Una cartolina", "type": "free", "rows": 4,
   "cons": "SEI IN VACANZA IN UNA CITTÀ ITALIANA. SCRIVI UNA CARTOLINA A UN AMICO (20-30 PAROLE): DOVE SEI, CON CHI, CHE TEMPO FA, CHE COSA FAI.",
   "items": ["LA TUA CARTOLINA"]},
  {"part": "Prova 4 · Parlato"},
  {"id": "p1", "title": "P1 🎤 · La tua giornata", "type": "record",
   "items": ["RACCONTA LA TUA GIORNATA: A CHE ORA TI SVEGLI, CHE COSA FAI LA MATTINA, IL POMERIGGIO E LA SERA."]},
  {"id": "p2", "title": "P2 🎤 · Al telefono", "type": "record",
   "items": ["TELEFONI AL MEDICO. DI' CHI SEI, CHE PROBLEMA HAI E CHIEDI UN APPUNTAMENTO."]},
 ]
}

# =====================================================================
# A2 · SIMULAZIONE 1
# =====================================================================
A2_1 = {
 "title": "📝 Simulazione d'esame A2 · n. 1", "store": "esame-a2-1", "upper": True,
 "sections": [
  {"part": "Prova 1 · Ascolto"},
  ascolto("a1", "A1 · Alla radio: il tempo",
          [("M", "ECCO LE PREVISIONI DEL TEMPO PER DOMANI IN PUGLIA. LA MATTINA IL CIELO SARÀ NUVOLOSO SU TUTTA LA REGIONE, "
                 "CON QUALCHE PIOGGIA A FOGGIA. NEL POMERIGGIO TORNA IL SOLE A BARI E A LECCE. LE TEMPERATURE: MINIME DI DODICI GRADI, "
                 "MASSIME DI VENTI. VENTO FORTE SUL MARE: ATTENZIONE SE VIAGGIATE IN NAVE.")],
          [("1. DOMANI MATTINA PIOVE A FOGGIA.", None, "VERO"), ("2. NEL POMERIGGIO A BARI C'È IL SOLE.", None, "VERO"),
           ("3. LA TEMPERATURA MASSIMA È DI 12 GRADI.", None, "FALSO"), ("4. SUL MARE NON C'È VENTO.", None, "FALSO")],
          opts=VF, cons="ASCOLTA LE PREVISIONI. VERO O FALSO?", p=4),
  ascolto("a2", "A2 · All'agenzia per il lavoro",
          [("F", "BUONGIORNO, SI ACCOMODI. CHE TIPO DI LAVORO CERCA?"),
           ("M", "HO LAVORATO TRE ANNI COME MURATORE IN SENEGAL. QUI IN ITALIA HO FATTO IL BRACCIANTE PER SEI MESI."),
           ("F", "HA LA PATENTE?"), ("M", "NO, MA HO LA BICICLETTA E PRENDO L'AUTOBUS."),
           ("F", "C'È UN'IMPRESA EDILE CHE CERCA UN MANOVALE A MODUGNO. IL CONTRATTO È DI SEI MESI, DALLE SETTE ALLE QUINDICI."),
           ("M", "VA BENE. COME POSSO ARRIVARE?"),
           ("F", "C'È UN AUTOBUS DA BARI CENTRALE. LE MANDO L'INDIRIZZO PER EMAIL. IL COLLOQUIO È LUNEDÌ ALLE NOVE.")],
          [("1. IN SENEGAL L'UOMO HA LAVORATO COME…", ["MURATORE", "BRACCIANTE", "AUTISTA"], "MURATORE"),
           ("2. IN ITALIA HA LAVORATO…", ["SEI MESI COME BRACCIANTE", "TRE ANNI COME MURATORE", "MAI"], "SEI MESI COME BRACCIANTE"),
           ("3. COME VA AL LAVORO?", ["IN BICICLETTA O IN AUTOBUS", "IN MACCHINA", "A PIEDI"], "IN BICICLETTA O IN AUTOBUS"),
           ("4. QUANTO DURA IL CONTRATTO?", ["SEI MESI", "UN ANNO", "TRE MESI"], "SEI MESI"),
           ("5. QUANDO È IL COLLOQUIO?", ["LUNEDÌ ALLE 9", "LUNEDÌ ALLE 7", "MARTEDÌ ALLE 9"], "LUNEDÌ ALLE 9")],
          cons="ASCOLTA IL DIALOGO E SCEGLI LA RISPOSTA GIUSTA.", p=5),
  abbina("a3", "A3 · Che cosa devono fare?", ["CAMBIARE BINARIO", "ANDARE ALLO SPORTELLO 3", "USCIRE DAL NEGOZIO", "PRENOTARE ONLINE"],
         [("ANNUNCIO 1", "CAMBIARE BINARIO"), ("ANNUNCIO 2", "ANDARE ALLO SPORTELLO 3"), ("ANNUNCIO 3", "USCIRE DAL NEGOZIO"), ("ANNUNCIO 4", "PRENOTARE ONLINE")],
         audio=[("F", "ANNUNCIO UNO. IL TRENO PER TARANTO OGGI NON PARTE DAL BINARIO DUE MA DAL BINARIO SEI."),
                ("F", "ANNUNCIO DUE. IL NUMERO C QUARANTADUE È PREGATO DI ANDARE ALLO SPORTELLO TRE."),
                ("M", "ANNUNCIO TRE. GENTILI CLIENTI, IL NEGOZIO CHIUDE TRA CINQUE MINUTI. VI PREGHIAMO DI ANDARE ALLE CASSE E DI USCIRE."),
                ("M", "ANNUNCIO QUATTRO. HAI CHIAMATO L'UFFICIO ANAGRAFE. PER LA CARTA D'IDENTITÀ SERVE L'APPUNTAMENTO: PRENOTA SUL SITO DEL COMUNE.")],
         cons="ASCOLTA I 4 ANNUNCI. CHE COSA DEVONO FARE LE PERSONE?", p=4),
  {"part": "Prova 2 · Lettura"},
  lettura("l1", "L1 · La lettera del condominio",
          "<b>AVVISO A TUTTI GLI INQUILINI</b><br>GENTILI SIGNORI, MARTEDÌ 18 NOVEMBRE DALLE 9 ALLE 13 MANCHERÀ L'ACQUA "
          "PER LAVORI ALLE TUBATURE. VI CONSIGLIAMO DI PREPARARE QUALCHE BOTTIGLIA D'ACQUA.<br>"
          "RICORDIAMO ANCHE CHE LA SPAZZATURA VA MESSA NEI CONTENITORI GIUSTI: LA CARTA IL LUNEDÌ, LA PLASTICA IL MERCOLEDÌ, "
          "L'UMIDO IL MARTEDÌ, IL GIOVEDÌ E IL SABATO.<br>NON SI LASCIANO LE BICICLETTE SULLE SCALE.<br>L'AMMINISTRATORE",
          [("1. PERCHÉ MANCA L'ACQUA?", ["PER DEI LAVORI", "PER UN INCIDENTE", "PERCHÉ NON PAGANO"], "PER DEI LAVORI"),
           ("2. PER QUANTE ORE MANCA L'ACQUA?", ["4 ORE", "9 ORE", "TUTTO IL GIORNO"], "4 ORE"),
           ("3. QUANDO SI BUTTA LA PLASTICA?", ["IL MERCOLEDÌ", "IL LUNEDÌ", "IL SABATO"], "IL MERCOLEDÌ"),
           ("4. DOVE NON SI METTONO LE BICICLETTE?", ["SULLE SCALE", "IN CORTILE", "IN CANTINA"], "SULLE SCALE"),
           ("5. CHI SCRIVE L'AVVISO?", ["L'AMMINISTRATORE", "IL SINDACO", "UN VICINO"], "L'AMMINISTRATORE")],
          cons="LEGGI E SCEGLI LA RISPOSTA GIUSTA.", p=5),
  lettura("l2", "L2 · La storia di Ibrahim",
          "MI CHIAMO IBRAHIM E VENGO DAL MALI. SONO ARRIVATO IN ITALIA TRE ANNI FA. ALL'INIZIO ABITAVO IN UN CENTRO DI ACCOGLIENZA "
          "A BARI E NON PARLAVO ITALIANO. HO FREQUENTATO IL CPIA PER UN ANNO E HO PRESO IL CERTIFICATO A2. "
          "POI HO FATTO UN CORSO DI CUCINA DI SEI MESI. ADESSO LAVORO IN UN RISTORANTE IN CENTRO E ABITO CON DUE COLLEGHI. "
          "IL MIO SOGNO È APRIRE UN PICCOLO RISTORANTE CON I PIATTI DEL MIO PAESE.",
          [("1. IBRAHIM È IN ITALIA DA TRE ANNI.", None, "VERO"), ("2. QUANDO È ARRIVATO PARLAVA GIÀ ITALIANO.", None, "FALSO"),
           ("3. HA STUDIATO AL CPIA PER UN ANNO.", None, "VERO"), ("4. ADESSO ABITA NEL CENTRO DI ACCOGLIENZA.", None, "FALSO"),
           ("5. VUOLE APRIRE UN RISTORANTE.", None, "VERO")],
          opts=VF, cons="LEGGI E SCEGLI: VERO O FALSO?", p=5),
  {"id": "l3", "title": "L3 · Il passato prossimo", "short": "L3 · Completa", "type": "cloze", "badge": badge(5),
   "cons": "SCRIVI IL VERBO AL PASSATO PROSSIMO. ESEMPIO: (ANDARE) → SONO ANDATO.",
   "parts": ["IERI ", {}, " (IO, ALZARSI) ALLE SETTE. ", {}, " (IO, PRENDERE) L'AUTOBUS E ", {}, " (IO, ARRIVARE) AL LAVORO ALLE OTTO. "
             "A PRANZO ", {}, " (IO, MANGIARE) CON I COLLEGHI. LA SERA ", {}, " (IO, TELEFONARE) A MIA MADRE."],
   "k": [eq("mi sono alzato", "mi sono alzata"), eq("ho preso"), eq("sono arrivato", "sono arrivata"), eq("ho mangiato"), eq("ho telefonato")]},
  {"part": "Prova 3 · Scrittura"},
  {"id": "s1", "title": "S1 ✎ · Un'email al padrone di casa", "type": "free", "rows": 6,
   "cons": "IN CUCINA IL RUBINETTO PERDE ACQUA. SCRIVI UN'EMAIL AL PADRONE DI CASA (40-50 PAROLE): SALUTA, SPIEGA IL PROBLEMA, "
           "DI' DA QUANDO C'È, CHIEDI QUANDO PUÒ VENIRE UN IDRAULICO, SALUTA.",
   "items": ["LA TUA EMAIL"]},
  {"id": "s2", "title": "S2 ✎ · Il tuo fine settimana", "type": "free", "rows": 5,
   "cons": "RACCONTA CHE COSA HAI FATTO LO SCORSO FINE SETTIMANA (40-50 PAROLE). USA IL PASSATO PROSSIMO.",
   "items": ["IL TUO TESTO"]},
  {"part": "Prova 4 · Parlato"},
  {"id": "p1", "title": "P1 🎤 · Il tuo lavoro", "type": "record",
   "items": ["PARLA DEL LAVORO CHE FACEVI NEL TUO PAESE E DEL LAVORO CHE VUOI FARE IN ITALIA. PERCHÉ?"]},
  {"id": "p2", "title": "P2 🎤 · Un problema", "type": "record",
   "items": ["SEI IN UN NEGOZIO. HAI COMPRATO UN TELEFONO E NON FUNZIONA. SPIEGA IL PROBLEMA E CHIEDI DI CAMBIARLO."]},
 ]
}

# =====================================================================
# A2 · SIMULAZIONE 2
# =====================================================================
A2_2 = {
 "title": "📝 Simulazione d'esame A2 · n. 2", "store": "esame-a2-2", "upper": True,
 "sections": [
  {"part": "Prova 1 · Ascolto"},
  ascolto("a1", "A1 · In farmacia",
          [("F", "BUONASERA, MI DICA."), ("M", "BUONASERA. MIO FIGLIO HA LA TOSSE E UN PO' DI FEBBRE, TRENTOTTO."),
           ("F", "QUANTI ANNI HA?"), ("M", "SEI ANNI."),
           ("F", "ALLORA LE DO QUESTO SCIROPPO PER BAMBINI. CINQUE MILLILITRI DUE VOLTE AL GIORNO, DOPO MANGIATO. "
                 "SE LA FEBBRE SALE SOPRA I TRENTANOVE, CHIAMI IL PEDIATRA."),
           ("M", "E SE IL PEDIATRA È CHIUSO?"), ("F", "DI SERA E NEL FINE SETTIMANA C'È LA GUARDIA MEDICA.")],
          [("1. IL BAMBINO HA…", ["TOSSE E FEBBRE", "MAL DI PANCIA", "MAL D'ORECCHIO"], "TOSSE E FEBBRE"),
           ("2. QUANTI ANNI HA?", ["SEI", "TRE", "OTTO"], "SEI"),
           ("3. QUANTE VOLTE AL GIORNO PRENDE LO SCIROPPO?", ["DUE", "TRE", "UNA"], "DUE"),
           ("4. QUANDO DEVE CHIAMARE IL PEDIATRA?", ["SE LA FEBBRE VA SOPRA 39", "SUBITO", "TRA UNA SETTIMANA"], "SE LA FEBBRE VA SOPRA 39"),
           ("5. LA SERA, SE IL PEDIATRA È CHIUSO, CHIAMA…", ["LA GUARDIA MEDICA", "LA FARMACIA", "LA SCUOLA"], "LA GUARDIA MEDICA")],
          cons="ASCOLTA IL DIALOGO E SCEGLI LA RISPOSTA GIUSTA.", p=5),
  ascolto("a2", "A2 · Il messaggio della scuola",
          [("F", "BUONGIORNO, SONO LA MAESTRA ROSSI DELLA SCUOLA ELEMENTARE «DE AMICIS». VI RICORDO CHE GIOVEDÌ I BAMBINI VANNO "
                 "IN GITA AL MUSEO. DEVONO ARRIVARE A SCUOLA ALLE OTTO, CON IL PRANZO AL SACCO E UNA BOTTIGLIA D'ACQUA. "
                 "IL COSTO DELLA GITA È DI DIECI EURO. DOVETE FIRMARE IL MODULO ENTRO MARTEDÌ. GRAZIE E A PRESTO.")],
          [("1. LA GITA È GIOVEDÌ.", None, "VERO"), ("2. I BAMBINI VANNO AL MARE.", None, "FALSO"),
           ("3. DEVONO PORTARE IL PRANZO.", None, "VERO"), ("4. LA GITA È GRATIS.", None, "FALSO"),
           ("5. I GENITORI FIRMANO IL MODULO ENTRO MARTEDÌ.", None, "VERO")],
          opts=VF, cons="ASCOLTA IL MESSAGGIO. VERO O FALSO?", p=5),
  {"part": "Prova 2 · Lettura"},
  abbina("l1", "L1 · Che servizio ti serve?", ["CAF", "PATRONATO", "CENTRO PER L'IMPIEGO", "CONSULTORIO", "ANAGRAFE"],
         [("1. DEVO FARE LA DICHIARAZIONE DEI REDDITI.", "CAF"), ("2. CERCO LAVORO E VOGLIO ISCRIVERMI ALLE LISTE.", "CENTRO PER L'IMPIEGO"),
          ("3. ASPETTO UN BAMBINO E VOGLIO FARE LE VISITE.", "CONSULTORIO"), ("4. MI SERVE IL CERTIFICATO DI RESIDENZA.", "ANAGRAFE"),
          ("5. VOGLIO CHIEDERE L'ASSEGNO PER I FIGLI ALL'INPS.", "PATRONATO")],
         cons="LEGGI E SCEGLI L'UFFICIO GIUSTO.", p=5),
  lettura("l2", "L2 · Il regolamento della biblioteca",
          "<b>BIBLIOTECA DI QUARTIERE · REGOLE</b><br>LA TESSERA È GRATUITA: SERVE UN DOCUMENTO.<br>"
          "PUOI PRENDERE IN PRESTITO 3 LIBRI PER 30 GIORNI.<br>SE VUOI TENERLI DI PIÙ, PUOI RINNOVARE IL PRESTITO UNA VOLTA, ANCHE ONLINE.<br>"
          "IN SALA LETTURA NON SI MANGIA E SI PARLA A BASSA VOCE.<br>IL WI-FI È GRATUITO PER TUTTI GLI ISCRITTI.<br>"
          "ORARIO: DAL LUNEDÌ AL VENERDÌ 9-19, SABATO 9-13.",
          [("1. LA TESSERA COSTA 5 EURO.", None, "FALSO"), ("2. POSSO PRENDERE 3 LIBRI.", None, "VERO"),
           ("3. POSSO RINNOVARE IL PRESTITO ONLINE.", None, "VERO"), ("4. IN SALA LETTURA POSSO MANGIARE UN PANINO.", None, "FALSO"),
           ("5. IL SABATO POMERIGGIO LA BIBLIOTECA È APERTA.", None, "FALSO")],
          opts=VF, cons="LEGGI E SCEGLI: VERO O FALSO?", p=5),
  {"id": "l3", "title": "L3 · Scegli la parola giusta", "short": "L3 · Scegli", "type": "choice", "full": True, "badge": badge(5),
   "items": [{"q": "1. DOMANI ___ AL MARE CON I MIEI AMICI.", "opts": ["ANDRÒ", "SONO ANDATO", "ANDAVO"]},
             {"q": "2. QUANDO ERO PICCOLO ___ IN UN VILLAGGIO.", "opts": ["ABITAVO", "ABITERÒ", "ABITO"]},
             {"q": "3. MARCO È ___ ALTO DI SUO FRATELLO.", "opts": ["PIÙ", "MOLTO", "TANTO"]},
             {"q": "4. HAI VISTO IL MIO TELEFONO? NO, NON ___ HO VISTO.", "opts": ["L'", "GLI", "LE"]},
             {"q": "5. ___ UN CAFFÈ, PER FAVORE.", "opts": ["VORREI", "VOLEVO STATO", "VORRÒ"]}],
   "k": [eq(a) for a in ["ANDRÒ", "ABITAVO", "PIÙ", "L'", "VORREI"]]},
  {"part": "Prova 3 · Scrittura"},
  {"id": "s1", "title": "S1 ✎ · Una richiesta di permesso", "type": "free", "rows": 6,
   "cons": "DEVI ANDARE IN QUESTURA GIOVEDÌ MATTINA. SCRIVI UN MESSAGGIO AL TUO CAPO (40-50 PAROLE): CHIEDI IL PERMESSO, SPIEGA PERCHÉ, "
           "PROPONI DI RECUPERARE LE ORE.",
   "items": ["IL TUO MESSAGGIO"]},
  {"id": "s2", "title": "S2 ✎ · Il tuo paese", "type": "free", "rows": 5,
   "cons": "DESCRIVI UNA FESTA DEL TUO PAESE (40-50 PAROLE): QUANDO È, CHE COSA SI FA, CHE COSA SI MANGIA.",
   "items": ["IL TUO TESTO"]},
  {"part": "Prova 4 · Parlato"},
  {"id": "p1", "title": "P1 🎤 · La tua città", "type": "record",
   "items": ["CONFRONTA BARI CON LA TUA CITTÀ: COM'È LA VITA, IL TEMPO, IL CIBO, LA GENTE. CHE COSA TI PIACE DI PIÙ?"]},
  {"id": "p2", "title": "P2 🎤 · In questura", "type": "record",
   "items": ["SEI IN QUESTURA. HAI PERSO LA RICEVUTA DEL PERMESSO DI SOGGIORNO. SPIEGA CHE COSA È SUCCESSO E CHIEDI CHE COSA DEVI FARE."]},
 ]
}

ESAMI = [("esami/a1-1.html", A1_1), ("esami/a1-2.html", A1_2), ("esami/a2-1.html", A2_1), ("esami/a2-2.html", A2_2)]
