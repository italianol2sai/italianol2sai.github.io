"""Simulazioni d'esame (2026-10-30), in «modalità esame» del motore (D.exam): prove una dopo l'altra con il tempo,
nessun «Controlla» per esercizio, consegna e punteggio solo alla fine.
- A2 integrazione: sul modello del test di lingua italiana A2 per il permesso UE di lungo periodo
  (comprensione orale, comprensione scritta, interazione scritta; per superarlo serve l'80%).
- B1 cittadinanza: sul modello della certificazione B1 per la cittadinanza (ascolto, lettura, analisi delle
  strutture di comunicazione, produzione scritta, produzione orale).
Testi, dialoghi e domande scritti nuovi per il sito. Persone, indirizzi e numeri inventati."""
from genera import eq
from unita_esami import ascolto, lettura, abbina, VF, minuscolo

REGOLE_A2 = ("FAI LE 3 PROVE IN ORDINE. OGNI PROVA HA UN TEMPO: QUANDO FINISCE PASSI ALLA PROVA DOPO. NON PUOI TORNARE INDIETRO. "
             "GLI ASCOLTI LI PUOI SENTIRE DUE VOLTE. IL RISULTATO LO VEDI SOLO ALLA FINE. PER SUPERARE IL TEST SERVE L'80%.")
REGOLE_B1 = ("Fai le 5 prove in ordine. Ogni prova ha un tempo: quando finisce passi alla prova dopo e non puoi tornare indietro. "
             "Il punteggio automatico conta ascolto, lettura e strutture; la produzione scritta e orale la valuta l'insegnante "
             "(premi «Invia le risposte all'insegnante» alla fine). Per superare la simulazione serve il 60% nelle prove automatiche.")

def cloze(eid, title, parts_text, keys, bank=None, cons="SCRIVI LA PAROLA GIUSTA."):
    pezzi = parts_text.split("___"); parts = []
    for i, p in enumerate(pezzi):
        parts.append(p)
        if i < len(pezzi) - 1: parts.append({})
    d = {"id": eid, "title": title, "short": title, "type": "cloze", "cons": cons, "parts": parts,
         "k": [eq(*k) if isinstance(k, (list, tuple)) else eq(*k.split("|")) for k in keys]}
    if bank: d["bank"] = bank
    return d

def modulo(eid, title, info, campi, cons):
    """campi: (etichetta, [risposte accettate])"""
    return {"id": eid, "title": title, "short": title, "type": "text", "w": "m", "cons": cons, "info": info,
            "items": [{"q": q} for q, _ in campi], "k": [eq(*a) for _, a in campi]}

# =====================================================================
# A2 INTEGRAZIONE · SIMULAZIONE 1
# =====================================================================
A2I_1 = {
 "title": "🎓 Simulazione d'esame A2 integrazione · n. 1", "store": "sim-a2i-1", "upper": True,
 "exam": {"soglia": 80, "regole": REGOLE_A2},
 "sub": "SIMULAZIONE DEL TEST A2 PER IL PERMESSO DI LUNGO PERIODO. LEGGI LE REGOLE E PREMI «INIZIA L'ESAME».",
 "sections": [
  {"part": "Prova 1 · Comprensione orale", "min": 25},
  ascolto("a1", "1 · Il messaggio del medico",
          [("F", "BUONGIORNO SIGNOR KOUASSI, SONO L'INFERMIERA DELLO STUDIO DEL DOTTOR LOSITO. LE ANALISI DEL SANGUE SONO PRONTE. "
                 "IL DOTTORE LA ASPETTA GIOVEDÌ ALLE DIECI E MEZZA PER LEGGERLE INSIEME. SE NON PUÒ VENIRE, CI CHIAMI ALLO ZERO OTTANTA, "
                 "CINQUE CINQUE SEI, DUE TRE, QUATTRO CINQUE. BUONA GIORNATA.")],
          [("1. CHI TELEFONA?", ["L'INFERMIERA", "IL DOTTORE", "IL FARMACISTA"], "L'INFERMIERA"),
           ("2. CHE COSA È PRONTO?", ["LE ANALISI DEL SANGUE", "LA RICETTA", "IL CERTIFICATO"], "LE ANALISI DEL SANGUE"),
           ("3. QUANDO È L'APPUNTAMENTO?", ["GIOVEDÌ ALLE 10:30", "MARTEDÌ ALLE 10:30", "GIOVEDÌ ALLE 12:30"], "GIOVEDÌ ALLE 10:30"),
           ("4. SE NON PUÒ ANDARE, CHE COSA DEVE FARE?", ["TELEFONARE ALLO STUDIO", "ANDARE IN FARMACIA", "MANDARE UN'EMAIL"], "TELEFONARE ALLO STUDIO")],
          cons="ASCOLTA IL MESSAGGIO DUE VOLTE E SCEGLI LA RISPOSTA GIUSTA."),
  ascolto("a2", "2 · All'ufficio postale",
          [("M", "BUONGIORNO. DEVO SPEDIRE QUESTO PACCO IN SENEGAL."), ("F", "QUANTO PESA? LO METTA SULLA BILANCIA."),
           ("M", "ECCO."), ("F", "TRE CHILI E MEZZO. CON IL SERVIZIO NORMALE ARRIVA IN DUE O TRE SETTIMANE E COSTA TRENTADUE EURO."),
           ("M", "C'È UN SERVIZIO PIÙ VELOCE?"), ("F", "SÌ, CON IL CORRIERE ESPRESSO ARRIVA IN CINQUE GIORNI, MA COSTA SETTANTA EURO."),
           ("M", "VA BENE IL SERVIZIO NORMALE. POSSO PAGARE CON IL BANCOMAT?"), ("F", "CERTO. DEVE SOLO COMPILARE QUESTO MODULO CON L'INDIRIZZO.")],
          [("1. IL PACCO VA IN SENEGAL.", None, "VERO"), ("2. IL PACCO PESA CINQUE CHILI.", None, "FALSO"),
           ("3. CON IL SERVIZIO NORMALE COSTA 32 EURO.", None, "VERO"), ("4. L'UOMO SCEGLIE IL CORRIERE ESPRESSO.", None, "FALSO"),
           ("5. PAGA CON IL BANCOMAT.", None, "VERO")],
          opts=VF, cons="ASCOLTA IL DIALOGO. VERO O FALSO?"),
  abbina("a3", "3 · Gli annunci", ["IN UN SUPERMERCATO", "IN STAZIONE", "IN AEROPORTO", "IN OSPEDALE"],
         [("ANNUNCIO 1", "IN STAZIONE"), ("ANNUNCIO 2", "IN UN SUPERMERCATO"), ("ANNUNCIO 3", "IN OSPEDALE"), ("ANNUNCIO 4", "IN AEROPORTO")],
         audio=[("F", "ANNUNCIO UNO. IL TRENO REGIONALE PER BRINDISI È IN ARRIVO AL BINARIO DUE. ALLONTANARSI DALLA LINEA GIALLA."),
                ("M", "ANNUNCIO DUE. GENTILI CLIENTI, AL REPARTO FRUTTA OGGI LE ARANCE SONO IN OFFERTA A UN EURO AL CHILO."),
                ("F", "ANNUNCIO TRE. SI RICORDA AI VISITATORI CHE L'ORARIO DI VISITA AI RICOVERATI TERMINA ALLE VENTI."),
                ("M", "ANNUNCIO QUATTRO. I PASSEGGERI DEL VOLO PER TIRANA SONO PREGATI DI PRESENTARSI ALL'USCITA SEI.")],
         cons="ASCOLTA I 4 ANNUNCI. DOVE SEI?"),
  {"part": "Prova 2 · Comprensione scritta", "min": 25},
  lettura("l1", "1 · L'avviso del Comune",
          "<b>COMUNE DI BARI · SERVIZI DEMOGRAFICI</b><br>DAL 1° DICEMBRE L'UFFICIO ANAGRAFE DI VIA FRATELLI RUGGIERO SI SPOSTA IN "
          "PIAZZA CHIURLIA 27. L'UFFICIO È APERTO DAL LUNEDÌ AL VENERDÌ DALLE 9 ALLE 12; IL MARTEDÌ E IL GIOVEDÌ ANCHE DALLE 15:30 ALLE 17:30. "
          "PER LA CARTA D'IDENTITÀ ELETTRONICA SI PRENOTA ONLINE. I CERTIFICATI SI POSSONO SCARICARE GRATIS DAL SITO ANPR.",
          [("1. DAL 1° DICEMBRE L'UFFICIO…", ["CAMBIA INDIRIZZO", "CHIUDE", "APRE IL SABATO"], "CAMBIA INDIRIZZO"),
           ("2. IL MERCOLEDÌ POMERIGGIO L'UFFICIO È…", ["CHIUSO", "APERTO DALLE 15:30", "APERTO FINO ALLE 20"], "CHIUSO"),
           ("3. PER LA CARTA D'IDENTITÀ BISOGNA…", ["PRENOTARE ONLINE", "TELEFONARE", "ANDARE SENZA APPUNTAMENTO"], "PRENOTARE ONLINE"),
           ("4. I CERTIFICATI SI POSSONO…", ["SCARICARE GRATIS DA INTERNET", "CHIEDERE SOLO IN POSTA", "PAGARE 10 EURO"], "SCARICARE GRATIS DA INTERNET")],
          cons="LEGGI L'AVVISO E SCEGLI LA RISPOSTA GIUSTA."),
  abbina("l2", "2 · Gli annunci di lavoro", ["ANNUNCIO A", "ANNUNCIO B", "ANNUNCIO C", "ANNUNCIO D"],
         [("1. RAHIM HA LA PATENTE C E VUOLE GUIDARE.", "ANNUNCIO C"), ("2. GRACE HA ESPERIENZA CON GLI ANZIANI.", "ANNUNCIO A"),
          ("3. YOUSSEF HA LAVORATO COME CAMERIERE E PARLA INGLESE.", "ANNUNCIO D"), ("4. FATIMA CERCA UN LAVORO DI PULIZIE LA MATTINA PRESTO.", "ANNUNCIO B")],
         info="<b>A</b> · CERCASI ASSISTENTE FAMILIARE PER SIGNORA DI 85 ANNI, CONVIVENTE, CON ESPERIENZA.<br>"
              "<b>B</b> · IMPRESA DI PULIZIE CERCA PERSONALE PER UFFICI, ORARIO 5:30-8:30.<br>"
              "<b>C</b> · DITTA DI TRASPORTI CERCA AUTISTA CON PATENTE C PER CONSEGNE IN PUGLIA.<br>"
              "<b>D</b> · HOTEL A POLIGNANO CERCA CAMERIERE DI SALA, RICHIESTO INGLESE.",
         cons="LEGGI GLI ANNUNCI. QUALE VA BENE PER OGNI PERSONA?"),
  lettura("l3", "3 · La lettera della scuola",
          "GENTILI GENITORI, LUNEDÌ 15 COMINCIA IL SERVIZIO DI MENSA. IL PRANZO COSTA 3 EURO AL GIORNO E SI PAGA CON L'APP DEL COMUNE. "
          "LE FAMIGLIE CON REDDITO BASSO POSSONO CHIEDERE UNO SCONTO PORTANDO L'ISEE IN SEGRETERIA ENTRO IL 30. "
          "SE IL BAMBINO HA ALLERGIE O NON MANGIA ALCUNI CIBI (PER ESEMPIO PER MOTIVI RELIGIOSI), I GENITORI DEVONO COMPILARE IL MODULO "
          "PER LA DIETA SPECIALE. LA DIRIGENTE SCOLASTICA",
          [("1. IL SERVIZIO DI MENSA È GRATIS PER TUTTI.", None, "FALSO"), ("2. SI PAGA CON L'APP DEL COMUNE.", None, "VERO"),
           ("3. PER LO SCONTO SERVE L'ISEE.", None, "VERO"), ("4. IL BAMBINO CHE NON MANGIA LA CARNE DI MAIALE NON PUÒ ANDARE IN MENSA.", None, "FALSO")],
          opts=VF, cons="LEGGI LA LETTERA. VERO O FALSO?"),
  {"part": "Prova 3 · Interazione scritta", "min": 25},
  modulo("s1", "1 · Compila il modulo",
         "LEGGI: <i>MI CHIAMO NADIA BENALI. SONO NATA A ORANO, IN ALGERIA, IL 3 MARZO 1994. ABITO A BARI IN VIA DANTE 120. "
         "IL MIO TELEFONO È 333 4567890. VORREI ISCRIVERMI AL CORSO DI CUCITO DEL MARTEDÌ.</i>",
         [("COGNOME", ["benali"]), ("NOME", ["nadia"]), ("LUOGO DI NASCITA", ["orano", "orano algeria", "orano (algeria)"]),
          ("DATA DI NASCITA", ["3/3/1994", "03/03/1994", "3 marzo 1994", "03-03-1994", "3-3-1994"]),
          ("INDIRIZZO", ["via dante 120", "via dante 120 bari", "via dante, 120"]), ("CORSO", ["cucito", "corso di cucito"]),
          ("GIORNO", ["martedi", "il martedi"])],
         "SEI ALL'ASSOCIAZIONE. COMPILA IL MODULO DI ISCRIZIONE CON I DATI DI NADIA."),
  cloze("s2", "2 · Completa l'email",
        "GENTILE SIGNOR ROSSI,<br>SONO L'INQUILINA DEL SECONDO PIANO. LE ___ PERCHÉ IN CUCINA C'È UN PROBLEMA: IL RUBINETTO ___ ACQUA DA TRE GIORNI. "
        "POTREBBE ___ UN IDRAULICO? IO SONO A CASA TUTTI I GIORNI ___ LE 15. GRAZIE MILLE.<br>CORDIALI ___,<br>AMINA",
        ["scrivo", "perde", ["mandare", "chiamare"], "dopo", "saluti"], bank="SCRIVO · PERDE · MANDARE · DOPO · SALUTI"),
  {"id": "s3", "title": "3 · Scegli la risposta giusta", "short": "3 · Rispondi", "type": "choice", "full": True,
   "items": [{"q": "1. IL TUO COLLEGA SCRIVE: «DOMANI PUOI FARE IL TURNO DI MATTINA AL POSTO MIO?» RISPONDI DI SÌ:",
              "opts": ["SÌ, NESSUN PROBLEMA. A CHE ORA COMINCIO?", "NO, DOMANI È DOMENICA.", "SÌ, IERI HO LAVORATO."]},
             {"q": "2. UN'AMICA SCRIVE: «STO MALE, NON VENGO A SCUOLA». RISPONDI:",
              "opts": ["MI DISPIACE! RIPOSATI. TI MANDO I COMPITI.", "CHE BELLO! A DOMANI.", "SONO LE OTTO."]},
             {"q": "3. IL PROPRIETARIO SCRIVE: «L'AFFITTO DI QUESTO MESE NON È ARRIVATO». RISPONDI:",
              "opts": ["MI SCUSI, HO FATTO IL BONIFICO IERI. LE MANDO LA RICEVUTA.", "VA BENE, ARRIVEDERCI.", "IL MIO NUMERO È 333..."]}],
   "k": [eq("SÌ, NESSUN PROBLEMA. A CHE ORA COMINCIO?"), eq("MI DISPIACE! RIPOSATI. TI MANDO I COMPITI."),
         eq("MI SCUSI, HO FATTO IL BONIFICO IERI. LE MANDO LA RICEVUTA.")]},
 ]
}

# =====================================================================
# A2 INTEGRAZIONE · SIMULAZIONE 2
# =====================================================================
A2I_2 = {
 "title": "🎓 Simulazione d'esame A2 integrazione · n. 2", "store": "sim-a2i-2", "upper": True,
 "exam": {"soglia": 80, "regole": REGOLE_A2},
 "sub": "SIMULAZIONE DEL TEST A2 PER IL PERMESSO DI LUNGO PERIODO. LEGGI LE REGOLE E PREMI «INIZIA L'ESAME».",
 "sections": [
  {"part": "Prova 1 · Comprensione orale", "min": 25},
  ascolto("a1", "1 · Al centro per l'impiego",
          [("F", "BUONGIORNO, SI SIEDA. HA PORTATO I DOCUMENTI?"), ("M", "SÌ, ECCO IL PERMESSO DI SOGGIORNO E IL CODICE FISCALE."),
           ("F", "BENE. CHE LAVORO HA FATTO FINORA?"), ("M", "HO LAVORATO DUE ANNI IN UN MAGAZZINO A MODUGNO, MA IL CONTRATTO È FINITO A SETTEMBRE."),
           ("F", "LE INTERESSA UN CORSO DI FORMAZIONE? C'È UN CORSO GRATUITO PER CARRELLISTI, DI QUATTRO SETTIMANE."),
           ("M", "SÌ, MI INTERESSA MOLTO. QUANDO COMINCIA?"), ("F", "IL DIECI NOVEMBRE. LE LEZIONI SONO DAL LUNEDÌ AL VENERDÌ, DALLE OTTO ALLE DODICI.")],
          [("1. CHE DOCUMENTI HA PORTATO L'UOMO?", ["PERMESSO DI SOGGIORNO E CODICE FISCALE", "PASSAPORTO E PATENTE", "CONTRATTO E BUSTA PAGA"], "PERMESSO DI SOGGIORNO E CODICE FISCALE"),
           ("2. DOVE HA LAVORATO?", ["IN UN MAGAZZINO", "IN UN RISTORANTE", "IN UN CANTIERE"], "IN UN MAGAZZINO"),
           ("3. QUANTO DURA IL CORSO?", ["QUATTRO SETTIMANE", "DUE ANNI", "DIECI GIORNI"], "QUATTRO SETTIMANE"),
           ("4. IL CORSO COSTA…", ["NIENTE", "DIECI EURO", "MOLTO"], "NIENTE"),
           ("5. LE LEZIONI SONO…", ["LA MATTINA", "LA SERA", "IL SABATO"], "LA MATTINA")],
          cons="ASCOLTA IL DIALOGO DUE VOLTE E SCEGLI LA RISPOSTA GIUSTA."),
  ascolto("a2", "2 · La segreteria della ASL",
          [("M", "BUONGIORNO, AVETE CHIAMATO IL CENTRO UNICO DI PRENOTAZIONE. PER PRENOTARE UNA VISITA PREMETE UNO. "
                 "PER DISDIRE UNA PRENOTAZIONE PREMETE DUE. PER INFORMAZIONI SUGLI ORARI PREMETE TRE. "
                 "RICORDATE DI AVERE VICINO LA TESSERA SANITARIA E LA RICETTA DEL MEDICO.")],
          [("1. PER PRENOTARE UNA VISITA PREMI…", ["1", "2", "3"], "1"),
           ("2. NON PUOI ANDARE ALLA VISITA: PREMI…", ["2", "1", "3"], "2"),
           ("3. CHE COSA DEVI AVERE VICINO?", ["TESSERA SANITARIA E RICETTA", "PASSAPORTO E SOLDI", "IL CONTRATTO DI LAVORO"], "TESSERA SANITARIA E RICETTA")],
          cons="ASCOLTA IL MESSAGGIO E SCEGLI."),
  abbina("a3", "3 · Che cosa chiedono?", ["UN'INFORMAZIONE STRADALE", "UN PREZZO", "UN ORARIO", "UN AIUTO"],
         [("DOMANDA 1", "UN'INFORMAZIONE STRADALE"), ("DOMANDA 2", "UN ORARIO"), ("DOMANDA 3", "UN PREZZO"), ("DOMANDA 4", "UN AIUTO")],
         audio=[("F", "DOMANDA UNO. SCUSI, PER ANDARE ALLA QUESTURA DEVO GIRARE A DESTRA O A SINISTRA?"),
                ("M", "DOMANDA DUE. A CHE ORA PARTE L'ULTIMO AUTOBUS PER IL QUARTIERE SAN PAOLO?"),
                ("F", "DOMANDA TRE. QUANTO COSTA L'ABBONAMENTO MENSILE DELL'AUTOBUS?"),
                ("M", "DOMANDA QUATTRO. MI SCUSI, MI PUÒ AIUTARE A PORTARE QUESTA VALIGIA SULLE SCALE?")],
         cons="ASCOLTA LE 4 DOMANDE. CHE COSA CHIEDE LA PERSONA?"),
  {"part": "Prova 2 · Comprensione scritta", "min": 25},
  lettura("l1", "1 · Il regolamento del condominio",
          "<b>REGOLE DEL CONDOMINIO</b><br>1. DALLE 14 ALLE 16 E DALLE 22 ALLE 7 NON SI FA RUMORE.<br>2. LA SPAZZATURA SI METTE NEI CONTENITORI "
          "IN CORTILE, DIVISA: CARTA, PLASTICA, VETRO, UMIDO, INDIFFERENZIATO.<br>3. I PANNI NON SI STENDONO SUL BALCONE CHE DÀ SULLA STRADA PRINCIPALE.<br>"
          "4. LE BICICLETTE SI LASCIANO NEL GARAGE, NON NELL'INGRESSO.<br>5. PER LAVORI IN CASA BISOGNA AVVISARE L'AMMINISTRATORE.",
          [("1. ALLE 15 POSSO USARE IL TRAPANO.", None, "FALSO"), ("2. LA SPAZZATURA VA DIVISA.", None, "VERO"),
           ("3. POSSO STENDERE I PANNI SUL BALCONE SULLA STRADA PRINCIPALE.", None, "FALSO"),
           ("4. LA BICICLETTA VA NEL GARAGE.", None, "VERO"), ("5. PER RIFARE IL BAGNO DEVO AVVISARE L'AMMINISTRATORE.", None, "VERO")],
          opts=VF, cons="LEGGI LE REGOLE. VERO O FALSO?"),
  lettura("l2", "2 · Il volantino",
          "<b>SPORTELLO GRATUITO PER CITTADINI STRANIERI</b><br>AIUTO PER: PERMESSO DI SOGGIORNO, RICONGIUNGIMENTO FAMILIARE, "
          "ISCRIZIONE AL SERVIZIO SANITARIO, CONTRATTI DI LAVORO.<br>DOVE: CASA DEL QUARTIERE, VIA ARCIDIACONO GIOVINE 10.<br>"
          "QUANDO: MERCOLEDÌ 16-19 E SABATO 10-13.<br>NON SERVE L'APPUNTAMENTO. SI PARLA ITALIANO, INGLESE, FRANCESE E ARABO.",
          [("1. LO SPORTELLO COSTA…", ["NIENTE", "5 EURO", "10 EURO"], "NIENTE"),
           ("2. LO SPORTELLO AIUTA ANCHE PER…", ["IL RICONGIUNGIMENTO FAMILIARE", "TROVARE CASA", "LA PATENTE"], "IL RICONGIUNGIMENTO FAMILIARE"),
           ("3. IL SABATO È APERTO…", ["LA MATTINA", "IL POMERIGGIO", "LA SERA"], "LA MATTINA"),
           ("4. PER ANDARE ALLO SPORTELLO…", ["NON SERVE L'APPUNTAMENTO", "BISOGNA TELEFONARE", "BISOGNA PRENOTARE ONLINE"], "NON SERVE L'APPUNTAMENTO")],
          cons="LEGGI IL VOLANTINO E SCEGLI."),
  abbina("l3", "3 · Dove trovi queste frasi?", ["SU UNA BOLLETTA", "SU UNA RICETTA MEDICA", "SU UNO SCONTRINO", "SU UN BIGLIETTO DELL'AUTOBUS"],
         [("1. «IMPORTO DA PAGARE ENTRO IL 16/11: 74,30 €»", "SU UNA BOLLETTA"), ("2. «1 COMPRESSA 2 VOLTE AL GIORNO PER 6 GIORNI»", "SU UNA RICETTA MEDICA"),
          ("3. «TOTALE 12,80 € · CONTANTI 20,00 € · RESTO 7,20 €»", "SU UNO SCONTRINO"), ("4. «VALIDO 90 MINUTI DALLA CONVALIDA»", "SU UN BIGLIETTO DELL'AUTOBUS")],
         cons="SCEGLI IL DOCUMENTO GIUSTO."),
  {"part": "Prova 3 · Interazione scritta", "min": 25},
  modulo("s1", "1 · Il modulo della palestra",
         "LEGGI: <i>SONO OMAR TOURÉ. SONO NATO IL 21 LUGLIO 1999 A BAMAKO, IN MALI. ABITO A BARI IN VIA CALEFATI 45. "
         "VOGLIO FARE L'ABBONAMENTO DI TRE MESI E VORREI ANDARE IN PALESTRA LA SERA.</i>",
         [("COGNOME", ["toure"]), ("NOME", ["omar"]), ("DATA DI NASCITA", ["21/7/1999", "21/07/1999", "21 luglio 1999", "21-07-1999"]),
          ("LUOGO DI NASCITA", ["bamako", "bamako mali", "bamako (mali)"]), ("INDIRIZZO", ["via calefati 45", "via calefati, 45", "via calefati 45 bari"]),
          ("ABBONAMENTO (QUANTI MESI?)", ["3", "tre", "3 mesi", "tre mesi"]), ("ORARIO PREFERITO", ["sera", "la sera"])],
         "COMPILA IL MODULO DELLA PALESTRA CON I DATI DI OMAR."),
  cloze("s2", "2 · Completa il messaggio",
        "CIAO GIULIA, OGGI NON ___ VENIRE AL CORSO PERCHÉ MIO FIGLIO HA LA FEBBRE. ___ DI ANDARE DAL PEDIATRA. "
        "PUOI DIRE ALL'INSEGNANTE CHE SONO ___? MI MANDI LE FOTO DEI COMPITI? GRAZIE, A ___! KHADIJA",
        ["posso", "devo", "malata|assente", "presto|domani"], bank="POSSO · DEVO · ASSENTE · PRESTO"),
 ]
}


# =====================================================================
# B1 CITTADINANZA · SIMULAZIONE 1
# =====================================================================
B1C_1 = {
 "title": "🎓 Simulazione d'esame B1 cittadinanza · n. 1", "store": "sim-b1c-1",
 "exam": {"soglia": 60, "regole": REGOLE_B1},
 "sub": "Simulazione dell'esame B1 per la cittadinanza italiana. Leggi le regole e premi «Inizia l'esame».",
 "sections": [
  {"part": "Prova 1 · Ascolto", "min": 30},
  ascolto("a1", "1 · Brevi notizie",
          [("F", "Notizia uno. Da gennaio il Comune di Bari aprirà tre nuovi asili nido nei quartieri periferici. Le iscrizioni si faranno solo online."),
           ("M", "Notizia due. Domani sciopero dei mezzi pubblici dalle nove alle diciassette. Saranno garantite solo le corse del mattino presto e della sera."),
           ("F", "Notizia tre. L'Agenzia delle Entrate ricorda che la dichiarazione dei redditi precompilata è disponibile online da fine aprile."),
           ("M", "Notizia quattro. Nel fine settimana sono previste forti piogge su tutta la regione: la Protezione civile consiglia di non usare i sottopassaggi.")],
          [("1. Come ci si iscrive ai nuovi asili nido?", ["Solo online", "In Comune", "A scuola"], "Solo online"),
           ("2. Durante lo sciopero gli autobus…", ["passano solo la mattina presto e la sera", "non passano mai", "passano tutto il giorno"], "passano solo la mattina presto e la sera"),
           ("3. La dichiarazione precompilata è disponibile…", ["da fine aprile", "da gennaio", "da settembre"], "da fine aprile"),
           ("4. Che cosa consiglia la Protezione civile?", ["Di non usare i sottopassaggi", "Di restare a casa tutta la settimana", "Di chiamare il 112"], "Di non usare i sottopassaggi")],
          cons="Ascolta le notizie e scegli la risposta giusta."),
  ascolto("a2", "2 · Un'intervista",
          [("F", "Oggi parliamo con Ana, che è arrivata dal Perù quindici anni fa e da poco è diventata cittadina italiana. Ana, che cosa ha significato per te?"),
           ("M", "Per me è stato un momento molto emozionante. Ho giurato sulla Costituzione davanti al sindaco, con i miei figli vicino."),
           ("F", "È stato difficile ottenere la cittadinanza?"),
           ("M", "Ci sono voluti più di due anni. Ho dovuto raccogliere molti documenti, tradurli e fare l'esame di italiano di livello B1."),
           ("F", "Che cosa cambia adesso nella tua vita?"),
           ("M", "Posso votare, finalmente! E posso viaggiare più facilmente. Ma soprattutto mi sento parte di questa comunità, che è anche mia.")],
          [("1. Ana vive in Italia da quindici anni.", None, "VERO"), ("2. Ha giurato davanti al giudice.", None, "FALSO"),
           ("3. Per la cittadinanza ci sono voluti più di due anni.", None, "VERO"), ("4. Non ha dovuto fare l'esame di italiano.", None, "FALSO"),
           ("5. Ora può votare.", None, "VERO")],
          opts=VF, cons="Ascolta l'intervista e scegli: vero o falso?"),
  {"part": "Prova 2 · Comprensione della lettura", "min": 50},
  lettura("l1", "1 · La Costituzione",
          "La Costituzione italiana è entrata in vigore il 1° gennaio 1948, dopo la fine della Seconda guerra mondiale e il referendum "
          "del 1946, con cui gli italiani hanno scelto la Repubblica al posto della monarchia. Per la prima volta hanno votato anche le donne. "
          "La Costituzione afferma che l'Italia è una Repubblica democratica fondata sul lavoro e che tutti i cittadini sono uguali davanti "
          "alla legge, senza distinzione di sesso, razza, lingua, religione e opinioni politiche. Riconosce diritti come la libertà di "
          "parola, il diritto all'istruzione e alla salute, ma anche doveri, come pagare le tasse in proporzione a quello che si guadagna.",
          [("1. La Costituzione è entrata in vigore nel…", ["1948", "1946", "1861"], "1948"),
           ("2. Nel referendum del 1946 gli italiani hanno scelto…", ["la Repubblica", "la monarchia", "un nuovo re"], "la Repubblica"),
           ("3. Che cosa è successo per la prima volta nel 1946?", ["Hanno votato le donne", "Si è votato per il Papa", "È finita la scuola obbligatoria"], "Hanno votato le donne"),
           ("4. Secondo la Costituzione la Repubblica è fondata…", ["sul lavoro", "sulla religione", "sull'esercito"], "sul lavoro"),
           ("5. Quale è un dovere dei cittadini?", ["Pagare le tasse in base al reddito", "Andare in chiesa", "Avere una casa"], "Pagare le tasse in base al reddito")],
          cons="Leggi il testo e scegli la risposta giusta."),
  abbina("l2", "2 · Le istituzioni", ["Il Parlamento", "Il Presidente della Repubblica", "Il Governo", "La Magistratura", "Il Comune"],
         [("1. Fa le leggi; è formato da Camera dei deputati e Senato.", "Il Parlamento"),
          ("2. È il capo dello Stato e rappresenta l'unità nazionale.", "Il Presidente della Repubblica"),
          ("3. È guidato dal Presidente del Consiglio e mette in pratica le leggi.", "Il Governo"),
          ("4. È indipendente e giudica chi non rispetta la legge.", "La Magistratura"),
          ("5. Si occupa dei servizi della città, come anagrafe, asili e trasporti.", "Il Comune")],
         cons="Leggi le descrizioni e scegli l'istituzione giusta."),
  {"part": "Prova 3 · Analisi delle strutture di comunicazione", "min": 40},
  cloze("g1", "1 · Completa con i verbi",
        "Quando sono arrivata in Italia non ___ (io, conoscere) nessuno. Per fortuna una vicina mi ___ (aiutare) a trovare un corso di italiano. "
        "Credo che imparare la lingua ___ (essere) fondamentale. Se non ___ (io, studiare), oggi non potrei lavorare come mediatrice. "
        "L'anno prossimo ___ (io, chiedere) la cittadinanza.",
        ["conoscevo", "ha aiutata|ha aiutato", "sia", "avessi studiato", "chiederò"], cons="Scrivi il verbo al tempo e modo giusto."),
  {"id": "g2", "title": "2 · Scegli la forma giusta", "short": "2 · Scegli", "type": "choice", "full": True,
   "items": [{"q": "1. È necessario che i genitori ___ i figli a scuola fino a 16 anni.", "opts": ["mandino", "mandano", "manderanno"]},
             {"q": "2. Il sindaco, ___ è stato eletto a giugno, ha presentato il programma.", "opts": ["che", "cui", "il quale di"]},
             {"q": "3. ___ fossi cittadino, voterei alle elezioni.", "opts": ["Se", "Quando", "Perché"]},
             {"q": "4. Le tasse ___ pagate entro il 30 novembre.", "opts": ["devono essere", "devono avere", "hanno dovuto"]},
             {"q": "5. Mi ha detto che ___ il giorno dopo.", "opts": ["sarebbe venuto", "viene", "venga"]}],
   "k": [eq(a) for a in ["mandino", "che", "Se", "devono essere", "sarebbe venuto"]]},
  {"part": "Prova 4 · Produzione scritta", "min": 60},
  {"id": "s1", "title": "1 ✎ · Un'email all'ufficio", "type": "free", "rows": 8,
   "cons": "Devi rinnovare la carta d'identità ma online non trovi appuntamenti liberi prima di due mesi. Scrivi un'email all'ufficio anagrafe "
           "(80-100 parole): spiega la situazione, di' perché ti serve presto il documento e chiedi una soluzione.",
   "items": ["La tua email"]},
  {"id": "s2", "title": "2 ✎ · Un testo personale", "type": "free", "rows": 8,
   "cons": "Che cosa significa per te diventare cittadino italiano? Scrivi un testo (80-100 parole) con la tua esperienza e le tue ragioni.",
   "items": ["Il tuo testo"]},
  {"part": "Prova 5 · Produzione orale", "min": 10},
  {"id": "p1", "title": "1 🎤 · Presentati", "type": "record",
   "items": ["Presentati: da quanto tempo vivi in Italia, che cosa fai, com'è la tua vita a Bari, i tuoi progetti per il futuro."]},
  {"id": "p2", "title": "2 🎤 · Esprimi un'opinione", "type": "record",
   "items": ["Secondo te, quali sono i diritti e i doveri più importanti di chi vive in Italia? Spiega con esempi."]},
 ]
}

# =====================================================================
# B1 CITTADINANZA · SIMULAZIONE 2
# =====================================================================
B1C_2 = {
 "title": "🎓 Simulazione d'esame B1 cittadinanza · n. 2", "store": "sim-b1c-2",
 "exam": {"soglia": 60, "regole": REGOLE_B1},
 "sub": "Simulazione dell'esame B1 per la cittadinanza italiana. Leggi le regole e premi «Inizia l'esame».",
 "sections": [
  {"part": "Prova 1 · Ascolto", "min": 30},
  ascolto("a1", "1 · Allo sportello del patronato",
          [("M", "Buongiorno, vorrei chiedere l'assegno unico per i miei figli. Come devo fare?"),
           ("F", "Prima di tutto serve l'ISEE aggiornato. Lo possiamo fare noi qui, gratuitamente. Quanti figli ha?"),
           ("M", "Due: una bambina di sei anni e un ragazzo di quindici."),
           ("F", "Bene. Porti la prossima volta i documenti di tutta la famiglia, i codici fiscali, il contratto d'affitto e l'IBAN del suo conto."),
           ("M", "E quando arrivano i soldi?"),
           ("F", "Di solito l'INPS paga il mese dopo la domanda, direttamente sul conto. Le fisso un appuntamento per martedì alle undici.")],
          [("1. Che cosa vuole chiedere l'uomo?", ["L'assegno unico per i figli", "La pensione", "Il permesso di soggiorno"], "L'assegno unico per i figli"),
           ("2. Che cosa serve prima di tutto?", ["L'ISEE aggiornato", "Il passaporto", "La busta paga"], "L'ISEE aggiornato"),
           ("3. Quanto costa fare l'ISEE al patronato?", ["Niente", "25 euro", "50 euro"], "Niente"),
           ("4. Come arrivano i soldi?", ["Sul conto corrente", "In contanti", "Con un assegno per posta"], "Sul conto corrente"),
           ("5. Quando è l'appuntamento?", ["Martedì alle 11", "Lunedì alle 11", "Martedì alle 15"], "Martedì alle 11")],
          cons="Ascolta il dialogo e scegli la risposta giusta."),
  abbina("a2", "2 · Che cosa fanno?", ["Si informano", "Si lamentano", "Danno un consiglio", "Ringraziano"],
         [("Persona 1", "Ringraziano"), ("Persona 2", "Danno un consiglio"), ("Persona 3", "Si lamentano"), ("Persona 4", "Si informano")],
         audio=[("F", "Persona uno. Volevo dirvi grazie di cuore: senza il vostro aiuto non avrei mai trovato questo lavoro."),
                ("M", "Persona due. Se fossi in te, prima di firmare il contratto lo farei leggere a un sindacato."),
                ("F", "Persona tre. È la terza volta che il treno arriva con un'ora di ritardo e nessuno ci dà spiegazioni. Non è accettabile!"),
                ("M", "Persona quattro. Buongiorno, vorrei sapere quali documenti servono per iscrivere mio figlio all'università.")],
         cons="Ascolta le 4 persone. Che cosa fanno?"),
  {"part": "Prova 2 · Comprensione della lettura", "min": 50},
  lettura("l1", "1 · La scuola in Italia",
          "In Italia l'istruzione è obbligatoria dai 6 ai 16 anni. Il percorso comincia con la scuola primaria, che dura cinque anni, "
          "prosegue con la scuola secondaria di primo grado, di tre anni, e poi con la scuola secondaria di secondo grado: licei, istituti "
          "tecnici e istituti professionali. Dopo i 16 anni i ragazzi possono anche frequentare corsi di formazione professionale. "
          "La scuola pubblica è gratuita, ma le famiglie pagano libri, mensa e materiale. Anche gli adulti possono studiare: nei CPIA, "
          "i Centri provinciali per l'istruzione degli adulti, si possono seguire corsi di italiano e prendere il diploma di terza media.",
          [("1. La scuola è obbligatoria fino a 18 anni.", None, "FALSO"), ("2. La scuola primaria dura cinque anni.", None, "VERO"),
           ("3. Gli istituti tecnici fanno parte della scuola secondaria di secondo grado.", None, "VERO"),
           ("4. Nella scuola pubblica i libri sono sempre gratis.", None, "FALSO"), ("5. Al CPIA un adulto può prendere il diploma di terza media.", None, "VERO")],
          opts=VF, cons="Leggi il testo e scegli: vero o falso?"),
  lettura("l2", "2 · Il servizio sanitario",
          "Il Servizio sanitario nazionale (SSN) è nato nel 1978 per garantire a tutti le cure mediche, indipendentemente dal reddito. "
          "Chi vive regolarmente in Italia si iscrive all'ASL e riceve la tessera sanitaria. Con l'iscrizione si sceglie il medico di base "
          "e, per i bambini fino a 14 anni, il pediatra. Le visite dal medico di base sono gratuite; per esami e visite specialistiche si paga "
          "spesso un contributo, il ticket, ma alcune persone sono esenti, per esempio per reddito o malattie croniche. "
          "Il pronto soccorso è sempre aperto e cura tutti, anche chi non è iscritto.",
          [("1. Il SSN è nato per…", ["garantire le cure a tutti", "aiutare solo i lavoratori", "costruire ospedali privati"], "garantire le cure a tutti"),
           ("2. Con l'iscrizione all'ASL si sceglie…", ["il medico di base", "l'ospedale", "la farmacia"], "il medico di base"),
           ("3. Il ticket è…", ["un contributo per esami e visite specialistiche", "una multa", "un documento"], "un contributo per esami e visite specialistiche"),
           ("4. Il pronto soccorso…", ["cura tutti, anche chi non è iscritto", "è aperto solo di giorno", "è solo per i cittadini italiani"], "cura tutti, anche chi non è iscritto")],
          cons="Leggi il testo e scegli la risposta giusta."),
  {"part": "Prova 3 · Analisi delle strutture di comunicazione", "min": 40},
  cloze("g1", "1 · Completa con le preposizioni",
        "Sono arrivato ___ Italia nel 2015. Prima ho abitato ___ Roma, poi mi sono trasferito ___ Bari. Lavoro ___ un'azienda che produce olio "
        "e ogni giorno vado al lavoro ___ autobus. ___ sabato studio per l'esame.",
        ["in", "a", "a", "in|per", "in", "il"], bank="A · IN · IN · A · IN · IL", cons="Scrivi la preposizione giusta."),
  {"id": "g2", "title": "2 · Trasforma", "short": "2 · Trasforma", "type": "choice", "full": True,
   "items": [{"q": "1. «Vieni domani!» → Mi ha detto ___ il giorno dopo.", "opts": ["di andare", "che vado", "vieni"]},
             {"q": "2. Il Comune ha approvato la legge. → La legge ___ dal Comune.", "opts": ["è stata approvata", "ha approvato", "approvava"]},
             {"q": "3. Non ho la macchina, ___ prendo il treno.", "opts": ["perciò", "benché", "affinché"]},
             {"q": "4. Vorrei che tu mi ___ con i documenti.", "opts": ["aiutassi", "aiuti", "aiuterai"]},
             {"q": "5. ___ in Italia da dieci anni, Lamine parla bene l'italiano.", "opts": ["Vivendo", "Vissuto", "Vivere"]}],
   "k": [eq(a) for a in ["di andare", "è stata approvata", "perciò", "aiutassi", "Vivendo"]]},
  {"part": "Prova 4 · Produzione scritta", "min": 60},
  {"id": "s1", "title": "1 ✎ · Una lettera al giornale", "type": "free", "rows": 8,
   "cons": "Nel tuo quartiere il parco è sporco e non ci sono giochi per i bambini. Scrivi una lettera al giornale della città (80-100 parole): "
           "descrivi il problema e proponi delle soluzioni.",
   "items": ["La tua lettera"]},
  {"id": "s2", "title": "2 ✎ · Racconta", "type": "free", "rows": 8,
   "cons": "Racconta una persona che ti ha aiutato in Italia (80-100 parole): chi è, come vi siete conosciuti, che cosa ha fatto per te.",
   "items": ["Il tuo testo"]},
  {"part": "Prova 5 · Produzione orale", "min": 10},
  {"id": "p1", "title": "1 🎤 · Descrivi", "type": "record",
   "items": ["Descrivi una festa italiana che conosci (per esempio il 25 aprile, il 2 giugno o la festa di San Nicola a Bari): che cosa si festeggia e come."]},
  {"id": "p2", "title": "2 🎤 · Confronta", "type": "record",
   "items": ["Confronta il sistema della scuola o della sanità in Italia e nel tuo paese: che cosa è simile, che cosa è diverso?"]},
 ]
}

# =====================================================================
# A2 STANDARD e B1 STANDARD: sul modello delle certificazioni generali (CILS/CELI):
# ascolto, lettura, analisi delle strutture, produzione scritta, produzione orale.
# =====================================================================
REGOLE_A2S = ("FAI LE 5 PROVE IN ORDINE. OGNI PROVA HA UN TEMPO: QUANDO FINISCE PASSI ALLA PROVA DOPO E NON PUOI TORNARE INDIETRO. "
              "IL PUNTEGGIO AUTOMATICO CONTA ASCOLTO, LETTURA E STRUTTURE; LA SCRITTURA E IL PARLATO LI VALUTA L'INSEGNANTE. "
              "PER SUPERARE LA SIMULAZIONE SERVE IL 60%.")

A2S_1 = {
 "title": "🎓 Simulazione d'esame A2 · n. 1", "store": "sim-a2s-1", "upper": True,
 "exam": {"soglia": 60, "regole": REGOLE_A2S},
 "sub": "SIMULAZIONE DI UN ESAME DI CERTIFICAZIONE A2. LEGGI LE REGOLE E PREMI «INIZIA L'ESAME».",
 "sections": [
  {"part": "Prova 1 · Ascolto", "min": 30},
  ascolto("a1", "1 · In agenzia immobiliare",
          [("F", "BUONGIORNO, HO VISTO L'ANNUNCIO DELL'APPARTAMENTO IN VIA PICCINNI. È ANCORA LIBERO?"),
           ("M", "SÌ, SIGNORA. È AL TERZO PIANO, CON ASCENSORE: DUE CAMERE, CUCINA ABITABILE, BAGNO E UN PICCOLO BALCONE."),
           ("F", "QUANTO COSTA AL MESE?"), ("M", "SEICENTOCINQUANTA EURO, PIÙ SETTANTA EURO DI SPESE CONDOMINIALI."),
           ("F", "È ARREDATO?"), ("M", "SOLO LA CUCINA. LE CAMERE SONO VUOTE. SE VUOLE, POSSIAMO VEDERLO DOMANI POMERIGGIO ALLE CINQUE."),
           ("F", "PERFETTO, VENGO CON MIO MARITO.")],
          [("1. A CHE PIANO È L'APPARTAMENTO?", ["AL TERZO", "AL PRIMO", "AL QUINTO"], "AL TERZO"),
           ("2. QUANTE CAMERE HA?", ["DUE", "UNA", "TRE"], "DUE"),
           ("3. QUANTO COSTA L'AFFITTO SENZA SPESE?", ["650 EURO", "720 EURO", "570 EURO"], "650 EURO"),
           ("4. CHE COSA È ARREDATO?", ["SOLO LA CUCINA", "TUTTA LA CASA", "NIENTE"], "SOLO LA CUCINA"),
           ("5. QUANDO VANNO A VEDERE LA CASA?", ["DOMANI ALLE 17", "OGGI ALLE 17", "DOMANI MATTINA"], "DOMANI ALLE 17")],
          cons="ASCOLTA IL DIALOGO DUE VOLTE E SCEGLI LA RISPOSTA GIUSTA."),
  ascolto("a2", "2 · Il racconto di Lin",
          [("F", "MI CHIAMO LIN E VENGO DALLA CINA. SONO ARRIVATA A BARI TRE ANNI FA PER STUDIARE ARCHITETTURA. ALL'INIZIO È STATO DIFFICILE: "
                 "NON CAPIVO NIENTE E MI MANCAVA LA MIA FAMIGLIA. POI HO CONOSCIUTO DUE RAGAZZE DEL MIO CORSO CHE MI HANNO AIUTATA MOLTO. "
                 "ADESSO LAVORO IL SABATO IN UN NEGOZIO DI SCARPE E LA DOMENICA VADO AL MARE CON LE MIE AMICHE. L'ANNO PROSSIMO MI LAUREO.")],
          [("1. LIN È VENUTA IN ITALIA PER LAVORARE.", None, "FALSO"), ("2. ALL'INIZIO LE MANCAVA LA FAMIGLIA.", None, "VERO"),
           ("3. DUE COMPAGNE DI CORSO L'HANNO AIUTATA.", None, "VERO"), ("4. LAVORA IN UN NEGOZIO TUTTI I GIORNI.", None, "FALSO"),
           ("5. SI LAUREA L'ANNO PROSSIMO.", None, "VERO")],
          opts=VF, cons="ASCOLTA. VERO O FALSO?"),
  {"part": "Prova 2 · Comprensione della lettura", "min": 40},
  lettura("l1", "1 · Una gita a Matera",
          "SABATO SCORSO SIAMO ANDATI A MATERA CON LA SCUOLA DI ITALIANO. SIAMO PARTITI ALLE OTTO CON IL PULLMAN E SIAMO ARRIVATI DOPO "
          "UN'ORA E MEZZA. LA GUIDA CI HA ACCOMPAGNATI NEI SASSI, LE ANTICHE CASE SCAVATE NELLA ROCCIA, DOVE FINO AGLI ANNI CINQUANTA "
          "VIVEVANO FAMIGLIE MOLTO POVERE. OGGI I SASSI SONO PATRIMONIO DELL'UNESCO E CI SONO ALBERGHI, RISTORANTI E MUSEI. "
          "A PRANZO ABBIAMO MANGIATO LE ORECCHIETTE E IL PANE DI MATERA. NEL POMERIGGIO HA PIOVUTO UN PO', MA ERAVAMO TUTTI CONTENTI.",
          [("1. COME SONO ANDATI A MATERA?", ["IN PULLMAN", "IN TRENO", "IN MACCHINA"], "IN PULLMAN"),
           ("2. QUANTO DURA IL VIAGGIO?", ["UN'ORA E MEZZA", "OTTO ORE", "MEZZ'ORA"], "UN'ORA E MEZZA"),
           ("3. CHE COSA SONO I SASSI?", ["ANTICHE CASE NELLA ROCCIA", "MONTAGNE", "CHIESE MODERNE"], "ANTICHE CASE NELLA ROCCIA"),
           ("4. CHI VIVEVA NEI SASSI FINO AGLI ANNI CINQUANTA?", ["FAMIGLIE POVERE", "TURISTI", "STUDENTI"], "FAMIGLIE POVERE"),
           ("5. COM'ERA IL TEMPO NEL POMERIGGIO?", ["HA PIOVUTO UN PO'", "C'ERA IL SOLE", "HA NEVICATO"], "HA PIOVUTO UN PO'")],
          cons="LEGGI IL TESTO E SCEGLI LA RISPOSTA GIUSTA."),
  abbina("l2", "2 · Le persone e i corsi", ["CORSO A", "CORSO B", "CORSO C", "CORSO D"],
         [("1. MARIA VUOLE IMPARARE A USARE IL COMPUTER.", "CORSO B"), ("2. SAID LAVORA DI GIORNO E PUÒ STUDIARE SOLO LA SERA.", "CORSO D"),
          ("3. ELENA VUOLE PREPARARE TORTE E BISCOTTI.", "CORSO A"), ("4. PEDRO VUOLE FARE SPORT CON ALTRE PERSONE.", "CORSO C")],
         info="<b>A</b> · LABORATORIO DI PASTICCERIA, GIOVEDÌ 10-12.<br><b>B</b> · INFORMATICA DI BASE: EMAIL, INTERNET, SPID. LUNEDÌ 15-17.<br>"
              "<b>C</b> · CALCETTO E PALLAVOLO NEL CAMPO DEL QUARTIERE, SABATO MATTINA.<br><b>D</b> · ITALIANO SERALE, MARTEDÌ E VENERDÌ 19-21.",
         cons="LEGGI GLI ANNUNCI. QUALE CORSO VA BENE?"),
  {"part": "Prova 3 · Analisi delle strutture", "min": 30},
  cloze("g1", "1 · Passato prossimo o imperfetto?",
        "QUANDO ___ (IO, ESSERE) PICCOLO, ___ (IO, ABITARE) IN UN VILLAGGIO VICINO AL MARE. OGNI GIORNO ___ (IO, ANDARE) A SCUOLA A PIEDI. "
        "UN GIORNO MIO PADRE ___ (COMPRARE) UNA BICICLETTA E DA QUEL GIORNO ___ (IO, ANDARE) A SCUOLA IN BICI.",
        ["ero", "abitavo", "andavo", "ha comprato", "sono andato|sono andata|andavo"], cons="SCRIVI IL VERBO AL TEMPO GIUSTO."),
  {"id": "g2", "title": "2 · Scegli la parola giusta", "short": "2 · Scegli", "type": "choice", "full": True,
   "items": [{"q": "1. HAI VISTO LE CHIAVI? SÌ, ___ HO VISTE SUL TAVOLO.", "opts": ["LE", "LI", "LA"]},
             {"q": "2. DOMANI ___ AL CINEMA CON I MIEI AMICI.", "opts": ["VADO", "SONO ANDATO", "ANDAVO"]},
             {"q": "3. QUESTO VESTITO È ___ BELLO DI QUELLO.", "opts": ["PIÙ", "MOLTO", "TROPPO"]},
             {"q": "4. A MIA SORELLA ___ PIACCIONO I GATTI.", "opts": ["LE", "GLI", "LA"]},
             {"q": "5. CI VEDIAMO ___ STAZIONE ALLE TRE.", "opts": ["ALLA", "IN LA", "DALLA"]}],
   "k": [eq(a) for a in ["LE", "VADO", "PIÙ", "LE", "ALLA"]]},
  {"part": "Prova 4 · Produzione scritta", "min": 45},
  {"id": "s1", "title": "1 ✎ · Un'email a un amico", "type": "free", "rows": 6,
   "cons": "SEI IN VACANZA. SCRIVI UN'EMAIL A UN AMICO (40-50 PAROLE): DOVE SEI, CON CHI, CHE COSA HAI FATTO, CHE TEMPO FA.",
   "items": ["LA TUA EMAIL"]},
  {"id": "s2", "title": "2 ✎ · Racconta", "type": "free", "rows": 6,
   "cons": "RACCONTA IL TUO PRIMO GIORNO IN ITALIA (50-60 PAROLE).", "items": ["IL TUO TESTO"]},
  {"part": "Prova 5 · Produzione orale", "min": 10},
  {"id": "p1", "title": "1 🎤 · Parla di te", "type": "record", "items": ["PRESENTATI E PARLA DELLA TUA GIORNATA TIPICA."]},
  {"id": "p2", "title": "2 🎤 · Descrivi", "type": "record", "items": ["DESCRIVI LA CASA DOVE ABITI E IL TUO QUARTIERE."]},
 ]
}

REGOLE_B1S = ("Fai le 5 prove in ordine. Ogni prova ha un tempo: quando finisce passi alla prova dopo e non puoi tornare indietro. "
              "Il punteggio automatico conta ascolto, lettura e strutture; la produzione scritta e orale la valuta l'insegnante. "
              "Per superare la simulazione serve il 60%.")

B1S_1 = {
 "title": "🎓 Simulazione d'esame B1 · n. 1", "store": "sim-b1s-1",
 "exam": {"soglia": 60, "regole": REGOLE_B1S},
 "sub": "Simulazione di un esame di certificazione B1. Leggi le regole e premi «Inizia l'esame».",
 "sections": [
  {"part": "Prova 1 · Ascolto", "min": 30},
  ascolto("a1", "1 · Alla radio: lavorare da casa",
          [("F", "Buongiorno a tutti. Oggi parliamo di lavoro da casa con Marco, informatico di Lecce. Marco, da quanto tempo lavori da casa?"),
           ("M", "Da quattro anni. Prima andavo in ufficio a Milano, poi l'azienda mi ha permesso di tornare in Puglia e lavorare a distanza."),
           ("F", "Quali sono i vantaggi?"),
           ("M", "Non perdo tempo nel traffico, spendo meno per l'affitto e posso stare vicino ai miei genitori, che sono anziani."),
           ("F", "E gli svantaggi?"),
           ("M", "A volte mi sento solo e lavoro troppe ore, perché non c'è una separazione chiara tra casa e lavoro. "
                 "Per questo due giorni alla settimana vado in uno spazio di coworking in centro.")],
          [("1. Marco lavora da casa da…", ["quattro anni", "due anni", "un anno"], "quattro anni"),
           ("2. Prima lavorava…", ["in un ufficio a Milano", "a Lecce", "all'estero"], "in un ufficio a Milano"),
           ("3. Un vantaggio per Marco è…", ["stare vicino ai genitori", "guadagnare di più", "viaggiare spesso"], "stare vicino ai genitori"),
           ("4. Uno svantaggio è…", ["lavorare troppe ore", "il traffico", "l'affitto alto"], "lavorare troppe ore"),
           ("5. Perché va al coworking?", ["Per non sentirsi solo e separare casa e lavoro", "Perché a casa non ha internet", "Perché lo chiede l'azienda"], "Per non sentirsi solo e separare casa e lavoro")],
          cons="Ascolta l'intervista e scegli la risposta giusta."),
  abbina("a2", "2 · Messaggi in segreteria", ["Sposta un appuntamento", "Chiede un favore", "Dà una buona notizia", "Fa un reclamo"],
         [("Messaggio 1", "Dà una buona notizia"), ("Messaggio 2", "Sposta un appuntamento"), ("Messaggio 3", "Fa un reclamo"), ("Messaggio 4", "Chiede un favore")],
         audio=[("F", "Messaggio uno. Ciao Sara! Indovina? Mi hanno presa per il lavoro in biblioteca! Comincio lunedì. Ti chiamo stasera!"),
                ("M", "Messaggio due. Buongiorno, sono il dentista Ferri. Purtroppo giovedì non posso riceverla; possiamo vederci venerdì alla stessa ora?"),
                ("F", "Messaggio tre. Salve, ho comprato da voi una lavatrice due settimane fa e già non funziona. Vorrei che qualcuno venisse a ripararla subito."),
                ("M", "Messaggio quattro. Ciao Ahmed, domani parto per tre giorni. Potresti dare da mangiare al mio gatto? Le chiavi sono dalla portiera.")],
         cons="Ascolta i messaggi. Che cosa fa ogni persona?"),
  {"part": "Prova 2 · Comprensione della lettura", "min": 50},
  lettura("l1", "1 · Lo spreco alimentare",
          "Ogni anno in Italia si buttano tonnellate di cibo ancora buono: in media ogni famiglia spreca circa mezzo chilo di alimenti alla "
          "settimana, soprattutto frutta, verdura e pane. Le cause principali sono la spesa fatta senza una lista, la cattiva conservazione "
          "e la confusione tra «da consumarsi entro» (data di scadenza vera) e «da consumarsi preferibilmente entro», che indica solo il "
          "periodo in cui il prodotto è migliore. Per ridurre lo spreco gli esperti consigliano di pianificare i pasti, usare gli avanzi "
          "in nuove ricette e congelare ciò che non si mangia subito. Molti supermercati, inoltre, donano i prodotti vicini alla scadenza alle associazioni.",
          [("1. Quali cibi si buttano di più?", ["Frutta, verdura e pane", "Carne e pesce", "Dolci"], "Frutta, verdura e pane"),
           ("2. Una causa dello spreco è…", ["fare la spesa senza lista", "comprare al mercato", "cucinare troppo poco"], "fare la spesa senza lista"),
           ("3. «Da consumarsi preferibilmente entro» significa che…", ["dopo quella data il prodotto è meno buono ma non pericoloso", "dopo quella data è pericoloso", "il prodotto è surgelato"], "dopo quella data il prodotto è meno buono ma non pericoloso"),
           ("4. Gli esperti consigliano di…", ["congelare quello che non si mangia subito", "fare la spesa ogni giorno", "comprare confezioni grandi"], "congelare quello che non si mangia subito"),
           ("5. I supermercati…", ["donano prodotti alle associazioni", "vendono il cibo scaduto", "chiudono la domenica"], "donano prodotti alle associazioni")],
          cons="Leggi l'articolo e scegli la risposta giusta."),
  lettura("l2", "2 · La lettera di Teresa",
          "Cara Giovanna, scusa se non ti ho scritto prima, ma questi mesi sono stati pieni di cambiamenti. A settembre ho lasciato il lavoro "
          "in banca: non ero più contenta e volevo fare qualcosa di più utile. Ho seguito un corso per diventare educatrice e adesso lavoro in "
          "una cooperativa che aiuta i ragazzi stranieri a fare i compiti. Guadagno meno, è vero, ma torno a casa soddisfatta. "
          "L'unico problema è che lavoro fino a tardi e vedo poco Paolo. A Natale però saremo liberi: perché non vieni a trovarci? Un abbraccio, Teresa",
          [("1. Teresa ha cambiato lavoro.", None, "VERO"), ("2. In banca era molto contenta.", None, "FALSO"),
           ("3. Ora aiuta i ragazzi stranieri con i compiti.", None, "VERO"), ("4. Adesso guadagna di più.", None, "FALSO"),
           ("5. Invita Giovanna per Natale.", None, "VERO")],
          opts=VF, cons="Leggi la lettera: vero o falso?"),
  {"part": "Prova 3 · Analisi delle strutture", "min": 40},
  cloze("g1", "1 · Completa con i verbi",
        "Ieri ___ (io, incontrare) Luca, che non ___ (io, vedere) da anni. Mi ha detto che ___ (lui, sposarsi) l'estate prossima. "
        "Penso che la sua fidanzata ___ (essere) una persona simpatica. Se ___ (io, avere) tempo, andrei al matrimonio.",
        ["ho incontrato", "vedevo", "si sposerà|si sposerebbe|si sposa", "sia", "avessi"], cons="Scrivi il verbo al tempo e modo giusto."),
  {"id": "g2", "title": "2 · Scegli la forma giusta", "short": "2 · Scegli", "type": "choice", "full": True,
   "items": [{"q": "1. Il libro ___ ti ho parlato è finalmente uscito.", "opts": ["di cui", "che", "a cui"]},
             {"q": "2. ___ piovesse, siamo usciti lo stesso.", "opts": ["Benché", "Siccome", "Mentre"]},
             {"q": "3. Se lo sapevo, te lo ___ (registro informale).", "opts": ["dicevo", "dico", "dirò"]},
             {"q": "4. Hai comprato il pane? Sì, ___ ho comprati due chili.", "opts": ["ne", "lo", "li"]},
             {"q": "5. Domani a quest'ora ___ già partiti.", "opts": ["saremo", "siamo stati", "eravamo"]}],
   "k": [eq(a) for a in ["di cui", "Benché", "dicevo", "ne", "saremo"]]},
  {"part": "Prova 4 · Produzione scritta", "min": 60},
  {"id": "s1", "title": "1 ✎ · Esprimi un'opinione", "type": "free", "rows": 8,
   "cons": "Secondo te è meglio vivere in una grande città o in un paese? Scrivi un testo (100-120 parole) con le tue ragioni ed esempi.",
   "items": ["Il tuo testo"]},
  {"id": "s2", "title": "2 ✎ · Un'email formale", "type": "free", "rows": 8,
   "cons": "Hai comprato online un paio di scarpe, ma è arrivata la misura sbagliata. Scrivi un'email al servizio clienti (80-100 parole): "
           "spiega il problema e chiedi di cambiarle o di avere il rimborso.",
   "items": ["La tua email"]},
  {"part": "Prova 5 · Produzione orale", "min": 10},
  {"id": "p1", "title": "1 🎤 · Racconta", "type": "record", "items": ["Racconta un viaggio importante della tua vita: dove, quando, con chi, che cosa è successo."]},
  {"id": "p2", "title": "2 🎤 · Argomenta", "type": "record", "items": ["I social network: sono più utili o più pericolosi? Spiega la tua opinione."]},
 ]
}

A2I_1, A2I_2, A2S_1 = minuscolo(A2I_1), minuscolo(A2I_2), minuscolo(A2S_1)

SIMULAZIONI = [("esami/a2-integrazione-1.html", A2I_1), ("esami/a2-integrazione-2.html", A2I_2),
               ("esami/b1-cittadinanza-1.html", B1C_1), ("esami/b1-cittadinanza-2.html", B1C_2),
               ("esami/a2-standard-1.html", A2S_1), ("esami/b1-standard-1.html", B1S_1)]
