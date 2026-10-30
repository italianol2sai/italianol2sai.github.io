"""Simulazioni d'esame B2 e C1 (2026-10-30), sulla STRUTTURA delle prove di certificazione (Erila ha mandato
i quaderni B2 e C1 di giugno 2026 come modello): ascolto, comprensione della lettura, analisi delle strutture
di comunicazione, produzione scritta, produzione orale. Dei quaderni si copia solo la forma delle prove:
testi, domande e temi sono tutti nuovi (i materiali ufficiali non si possono usare per la didattica)."""
from genera import eq
from unita_esami import ascolto, lettura, VF
from unita_drive import ordina
from unita_simulazioni import cloze

REGOLE = ("Fai le 5 prove in ordine, come all'esame: ascolto, lettura, analisi delle strutture, produzione scritta, produzione orale. "
          "Ogni prova ha il suo tempo; quando finisce passi alla prova dopo e non puoi tornare indietro. Gli ascolti si possono sentire due volte. "
          "Il punteggio automatico conta ascolto, lettura e strutture; lo scritto e l'orale li valuta l'insegnante "
          "(alla fine premi «Invia le risposte all'insegnante»). Per superare la simulazione serve il 55% "
          "(all'esame vero servono 11 punti su 20 in ogni abilità).")

def scelta(eid, title, items, cons, short=None):
    """items: (domanda con ___, [opzioni], giusta)"""
    return {"id": eid, "title": title, "short": short or title, "type": "choice", "full": True, "cons": cons,
            "items": [{"q": q, "opts": o} for q, o, _ in items], "k": [eq(a) for _, _, a in items]}

def scritto(eid, title, cons, parole):
    return {"id": eid, "title": title, "type": "free", "rows": 10, "cons": cons + " Scrivi da %s parole." % parole,
            "items": ["Il tuo testo"]}

# =====================================================================
# B2
# =====================================================================
B2_1 = {
 "title": "🎓 Simulazione d'esame B2 · n. 1", "store": "sim-b2-1",
 "exam": {"soglia": 55, "regole": REGOLE},
 "sub": "Simulazione di un esame di certificazione di livello B2. Leggi le regole e premi «Inizia l'esame».",
 "sections": [
  {"part": "Prova 1 · Ascolto", "min": 30},
  ascolto("a1", "1 · Brevi testi",
          [("M", "Testo uno. Buongiorno, chiamo per il corso serale di fotografia. Ho visto sul sito che le iscrizioni chiudono venerdì, "
                 "ma vorrei sapere se è possibile frequentare solo il modulo di fotografia digitale, senza la parte sulla pellicola."),
           ("F", "Testo due. Ciao Marta, sono Luisa. Sabato al circolo c'è la presentazione del libro di quella scrittrice che ti piace tanto. "
                 "Io pensavo di andarci, ma prima volevo sapere che cosa ne pensi: secondo te vale la pena, o è meglio aspettare il film?"),
           ("M", "Testo tre. Cari ascoltatori, questa settimana vi chiediamo di raccontarci il vostro primo giorno di lavoro: "
                 "scriveteci un messaggio di non più di cinque righe. I racconti più divertenti saranno letti in diretta venerdì mattina."),
           ("F", "Testo quattro. Allora, facciamo così: tu prenoti il treno per sabato mattina, io intanto chiamo l'agriturismo per chiedere "
                 "se hanno ancora la camera doppia. Se è tutto pieno, ci sentiamo stasera e cerchiamo un'altra soluzione."),
           ("M", "Testo cinque. Prima di un colloquio di lavoro conviene informarsi bene sull'azienda, preparare due o tre domande da fare "
                 "e provare a rispondere ad alta voce alle domande più comuni. E ricordate: arrivare dieci minuti prima è sempre una buona idea.")],
          [("1. L'uomo del testo uno chiede", ["se può seguire solo una parte del corso", "quanto costa il corso di fotografia",
                                               "se le iscrizioni sono già chiuse", "dove si svolgono le lezioni"], "se può seguire solo una parte del corso"),
           ("2. Luisa chiede a Marta", ["un'opinione su un evento", "di accompagnarla al cinema", "di prestarle un libro",
                                        "informazioni sul circolo"], "un'opinione su un evento"),
           ("3. La radio invita gli ascoltatori a", ["raccontare un'esperienza personale", "proporre un tema per la trasmissione",
                                                     "partecipare a un concorso a premi", "telefonare in diretta"], "raccontare un'esperienza personale"),
           ("4. Le due persone del testo quattro", ["si dividono i compiti per organizzare un viaggio", "hanno già prenotato tutto",
                                                    "rinunciano alla vacanza", "decidono di partire in macchina"], "si dividono i compiti per organizzare un viaggio"),
           ("5. Lo scopo del testo cinque è", ["dare consigli per un colloquio di lavoro", "presentare un'azienda",
                                               "raccontare un colloquio andato male", "spiegare come scrivere un curriculum"], "dare consigli per un colloquio di lavoro")],
          cons="Ascolta i cinque testi. Completa le frasi: scegli una delle quattro proposte."),
  ascolto("a2", "2 · L'intervista alla cuoca",
          [("M", "Oggi è con noi Rosaria De Santis, chef di un piccolo ristorante sulla costa barese che ha appena ricevuto un premio nazionale. Rosaria, se lo aspettava?"),
           ("F", "Sinceramente no. Pensi che fino a dieci anni fa facevo l'impiegata in banca. La cucina era solo la passione della domenica, quando cucinavo per tutta la famiglia."),
           ("M", "E poi che cosa è successo?"),
           ("F", "La banca ha chiuso la filiale e io mi sono trovata davanti a una scelta. Ho avuto paura, non lo nascondo, ma mio marito mi ha detto: "
                 "se non lo fai adesso, non lo farai mai. Così ho frequentato una scuola di cucina a Roma, mentre i miei figli restavano con i nonni."),
           ("M", "Che cosa ha imparato in quegli anni?"),
           ("F", "Soprattutto la disciplina. Pensavo che bastasse la fantasia, invece in cucina conta l'organizzazione: i tempi, l'ordine, il rispetto per i colleghi."),
           ("M", "E la sua cucina oggi com'è?"),
           ("F", "Semplice. Uso quasi solo prodotti del territorio, compro il pesce dai pescatori del porto e le verdure da due contadini della zona. "
                 "Non mi interessano i piatti spettacolari: voglio che chi mangia da me riconosca i sapori di casa."),
           ("M", "Un consiglio ai giovani che vogliono fare il suo mestiere?"),
           ("F", "Di non avere fretta. Oggi tutti vogliono diventare famosi in televisione, ma prima bisogna lavare tante pentole e ascoltare chi ne sa di più.")],
          [("1. Prima di diventare cuoca, Rosaria", ["lavorava in banca", "faceva la cameriera", "insegnava in una scuola", "aveva un'azienda agricola"], "lavorava in banca"),
           ("2. Ha cambiato lavoro", ["dopo la chiusura del suo ufficio", "perché era stanca della città", "per seguire i figli", "dopo aver vinto un premio"], "dopo la chiusura del suo ufficio"),
           ("3. Il marito", ["l'ha incoraggiata", "era contrario", "lavorava già in cucina", "le ha trovato una scuola"], "l'ha incoraggiata"),
           ("4. Alla scuola di cucina Rosaria ha capito che", ["l'organizzazione è fondamentale", "la fantasia basta", "i colleghi sono rivali", "i tempi non contano"], "l'organizzazione è fondamentale"),
           ("5. Ai giovani Rosaria consiglia di", ["essere pazienti e imparare dagli altri", "andare in televisione", "aprire subito un ristorante", "studiare all'estero"], "essere pazienti e imparare dagli altri")],
          cons="Ascolta l'intervista. Completa le frasi: scegli una delle quattro proposte."),
  ascolto("a3", "3 · Il servizio del telegiornale",
          [("F", "A Bari è partito questa mattina il progetto «Spiagge per tutti»: tre lidi pubblici, a Pane e Pomodoro, Torre Quetta e San Giorgio, "
                 "sono stati attrezzati con passerelle fino al mare, sedie da spiaggia per persone con disabilità e bagni accessibili. "
                 "Il progetto, finanziato in parte dalla Regione, è nato dalla proposta di un gruppo di associazioni di volontariato, "
                 "che da anni chiedevano al Comune di rendere il mare davvero di tutti. «Non si tratta solo di strutture», spiega Gianni Loiacono, "
                 "uno dei volontari, «ma di persone: ogni giorno ci saranno operatori formati che aiuteranno chi ne ha bisogno a entrare in acqua». "
                 "Il servizio è gratuito e non serve prenotare, ma per i gruppi numerosi è consigliato avvisare. Non mancano però le critiche: "
                 "alcuni residenti lamentano la mancanza di parcheggi vicino ai lidi. L'assessore promette nuovi posti auto entro la fine dell'estate.")],
          [("1. Il progetto riguarda tre spiagge pubbliche.", None, "Vero"),
           ("2. Il progetto è stato finanziato soltanto dal Comune.", None, "Falso"),
           ("3. L'idea è venuta da alcune associazioni di volontariato.", None, "Vero"),
           ("4. Secondo Loiacono le strutture sono la cosa più importante.", None, "Falso"),
           ("5. Ci saranno persone preparate per aiutare in acqua.", None, "Vero"),
           ("6. Il servizio costa poco.", None, "Falso"),
           ("7. Per i gruppi grandi è meglio avvisare prima.", None, "Vero"),
           ("8. Tutti i residenti sono soddisfatti del progetto.", None, "Falso")],
          opts=["Vero", "Falso"], cons="Ascolta il servizio. Le informazioni sono vere o false?"),

  {"part": "Prova 2 · Comprensione della lettura", "min": 50},
  lettura("l1", "1 · Il forno di quartiere",
          "<b>IL FORNO CHE HA SALVATO UN QUARTIERE</b><br>Quando nel 2019 l'ultimo panificio di via Napoli ha chiuso, nel quartiere Libertà "
          "molti pensavano che la strada sarebbe diventata un deserto di serrande abbassate. Invece, due anni dopo, quattro giovani tra i 24 e i 30 anni "
          "hanno deciso di riaprirlo: nessuno di loro era fornaio, ma tutti erano cresciuti in quella strada. «Abbiamo passato mesi a imparare dai "
          "vecchi panettieri della zona», racconta Sara, una delle socie, «e abbiamo fatto tantissimi errori: il primo pane era immangiabile!». "
          "Oggi il forno non vende soltanto pane e focaccia: il pomeriggio, nel retrobottega, si tengono corsi di cucina per mamme e ragazzi "
          "del quartiere, molti dei quali stranieri, e la sera i tavoli diventano un piccolo spazio per i compiti. «Volevamo un luogo dove le persone "
          "si incontrassero, non solo un negozio», spiega Sara. I prezzi sono rimasti bassi, perché la farina arriva direttamente da un mulino "
          "della Murgia. Il forno dà lavoro a sette persone e, intorno, hanno riaperto un fruttivendolo e una piccola libreria.",
          [("1. Quando il panificio ha chiuso, gli abitanti", ["temevano che la strada si svuotasse", "erano contenti", "hanno subito protestato", "hanno cambiato quartiere"], "temevano che la strada si svuotasse"),
           ("2. I quattro giovani", ["conoscevano bene il quartiere", "erano fornai esperti", "venivano da un'altra città", "avevano già un negozio"], "conoscevano bene il quartiere"),
           ("3. All'inizio", ["hanno avuto difficoltà a fare un buon pane", "hanno avuto subito successo", "hanno assunto un fornaio", "hanno venduto solo dolci"], "hanno avuto difficoltà a fare un buon pane"),
           ("4. Oltre a vendere pane, il forno", ["offre spazi e attività per il quartiere", "organizza feste private", "vende libri", "fa consegne a domicilio"], "offre spazi e attività per il quartiere"),
           ("5. Secondo il testo, l'apertura del forno", ["ha favorito altre attività nella strada", "ha fatto chiudere altri negozi", "ha aumentato i prezzi", "non ha cambiato niente"], "ha favorito altre attività nella strada")],
          cons="Leggi il testo e completa le frasi: scegli una delle quattro proposte."),
  lettura("l2", "2 · Il bando",
          "<b>BANDO «IDEE GIOVANI PER LA CITTÀ» · 3ª EDIZIONE</b><br>Il Comune finanzia progetti di giovani tra i 18 e i 32 anni residenti in città "
          "da almeno un anno. I progetti devono riguardare uno di questi ambiti: <b>cultura e tempo libero</b>, <b>ambiente</b>, <b>inclusione sociale</b>. "
          "Si può partecipare da soli o in gruppi di massimo cinque persone; in questo caso almeno la metà dei componenti deve avere i requisiti di età e residenza.<br>"
          "Ogni progetto può ricevere fino a 8.000 euro. La domanda va presentata solo online, sul portale del Comune, entro il 15 marzo, con: "
          "descrizione del progetto (massimo 3 pagine), piano delle spese, curriculum dei partecipanti. Non sono ammessi progetti già finanziati da altri enti.<br>"
          "Una commissione sceglierà i 20 progetti migliori, che saranno presentati in un incontro pubblico; il voto dei cittadini, online, conterà per il 30% "
          "del punteggio finale. I vincitori riceveranno metà del finanziamento all'inizio e il resto alla fine, dopo aver presentato le ricevute.",
          [("1. Il bando è alla prima edizione.", None, "Falso"),
           ("2. Possono partecipare anche persone che non abitano in città.", None, "Falso"),
           ("3. In un gruppo ci possono essere persone con più di 32 anni.", None, "Vero"),
           ("4. Ogni progetto riceve esattamente 8.000 euro.", None, "Falso"),
           ("5. La domanda si può consegnare anche a mano.", None, "Falso"),
           ("6. Un progetto che ha già un finanziamento regionale non può partecipare.", None, "Vero"),
           ("7. Anche i cittadini contribuiscono a scegliere i vincitori.", None, "Vero"),
           ("8. I vincitori ricevono tutto il denaro all'inizio.", None, "Falso")],
          opts=["Vero", "Falso"], cons="Leggi il bando. Le informazioni sono vere o false?"),
  ordina(["La storia della focaccia barese comincia in un'epoca in cui il forno non c'era in ogni casa.",
          "Le famiglie, infatti, preparavano l'impasto la mattina e lo portavano a cuocere nel forno pubblico del quartiere.",
          "Per non perdere tempo, il fornaio cuoceva prima le teglie di focaccia, che erano più veloci, e poi il pane.",
          "Ogni famiglia aveva la sua ricetta: c'era chi aggiungeva la patata lessa all'impasto e chi metteva le olive.",
          "Il condimento, però, era quasi sempre lo stesso: pomodorini schiacciati con le mani, sale, origano e tanto olio.",
          "Con il tempo le teglie sono diventate un simbolo della città, e oggi la focaccia si mangia a ogni ora del giorno.",
          "Ancora adesso, se chiedete a un barese qual è la focaccia migliore, vi risponderà senza dubbi: quella della sua panetteria."],
         "3 · Ricostruisci il testo", "3 · Riordina", "l3",
         cons="Il testo «La focaccia barese» è diviso in 7 parti, in disordine. Scrivi il numero giusto (1-7) accanto a ogni parte."),

  {"part": "Prova 3 · Analisi delle strutture di comunicazione", "min": 60},
  cloze("g1", "1 · Aggettivi e pronomi",
        "Molti pensano che il volontariato sia un'attività per ___ ha tanto tempo libero. In realtà ___ può fare qualcosa, anche un'ora alla settimana. "
        "Io, per esempio, aiuto in una mensa: ___ sabato servo i pasti e parlo con le persone che vengono. All'inizio ___ facevo solo per dovere, "
        "poi ho capito che ricevevo più di quanto davo. Ci sono persone ___ storie ti cambiano la giornata. Con ___ di loro sono diventato amico, "
        "e quando non ___ vedo per un po' ___ telefono per sapere come stanno. Non tutti i volontari restano a lungo: ___ smettono dopo poche settimane, "
        "altri restano per anni. Ma ___ sia la tua scelta, l'importante è cominciare.",
        ["chi", "chiunque|ognuno|ciascuno|ognuno di noi", "ogni", "lo", "le cui", "alcuni|qualcuno", "li", "gli", "alcuni|certi", "qualunque|qualsiasi"],
        cons="Completa il testo con gli aggettivi e i pronomi giusti."),
  cloze("g2", "2 · I verbi",
        "Quando ___ (io, arrivare) a Bari dieci anni fa, non ___ (io, parlare) una parola di italiano. Una vicina mi ___ (consigliare) "
        "di iscrivermi a un corso serale e, anche se ___ (io, essere) stanchissimo dopo il lavoro, ci andavo tre volte alla settimana. "
        "Se non ___ (io, fare) quella scelta, oggi non ___ (io, lavorare) come mediatore culturale. Spero che anche i miei figli ___ (imparare) "
        "a non arrendersi. L'anno prossimo, quando ___ (loro, finire) la scuola, li ___ (io, portare) a visitare il mio paese, perché voglio che "
        "___ (conoscere) anche le loro radici.",
        ["sono arrivato|sono arrivata", "parlavo", "ha consigliato", "ero", "avessi fatto", "lavorerei", "imparino", "avranno finito|finiranno",
         "porterò", "conoscano"], cons="Completa il testo con le forme giuste dei verbi tra parentesi."),
  scelta("g3", "3 · Completa il testo: scegli la parola", [
      ("Dal mese prossimo la biblioteca comunale ___ (1) l'orario di apertura anche la domenica mattina.", ["prolungherà", "allungherà", "aumenterà", "estenderà"], "estenderà"),
      ("La decisione è stata presa per venire ___ (2) alle richieste di molti studenti.", ["incontro", "contro", "verso", "dietro"], "incontro"),
      ("Per accedere alle sale studio sarà necessario ___ (3) un documento all'ingresso.", ["esibire", "esporre", "dimostrare", "mostrarsi"], "esibire"),
      ("Il servizio è ___ (4): non bisogna pagare nessun abbonamento.", ["gratuito", "libero", "economico", "aperto"], "gratuito"),
      ("Secondo l'assessore, la biblioteca deve diventare un ___ (5) di incontro per tutta la città.", ["punto", "posto", "motivo", "modo"], "punto"),
      ("Se l'esperimento darà buoni ___ (6), l'orario sarà confermato anche per l'estate.", ["risultati", "effetti", "frutti", "esiti"], "risultati"),
      ("Gli utenti potranno ___ (7) suggerimenti compilando un modulo online.", ["inviare", "spedire", "mandarsi", "ricevere"], "inviare"),
      ("Molti studenti hanno ___ (8) la loro soddisfazione sui social.", ["espresso", "detto", "parlato", "comunicato a"], "espresso")],
      "Leggi le frasi del testo «La biblioteca apre la domenica» e scegli la parola giusta."),
  scelta("g4", "4 · Le situazioni di comunicazione", [
      ("«Gentile cliente, la informiamo che la sua richiesta è stata presa in carico. Riceverà una risposta entro 48 ore.»",
       ["È un messaggio automatico di un servizio clienti.", "È un messaggio di un amico.", "È un annuncio in stazione.", "È una pubblicità."],
       "È un messaggio automatico di un servizio clienti."),
      ("«Ragazzi, domani la verifica è rimandata a lunedì perché la prof è malata. Passate parola!»",
       ["Un compagno di classe scrive nella chat della classe.", "La preside scrive ai genitori.", "Un insegnante parla in classe.", "È un avviso in bacheca del Comune."],
       "Un compagno di classe scrive nella chat della classe."),
      ("«Cercasi cameriere/a con esperienza per stagione estiva. Richiesta conoscenza dell'inglese. Inviare CV a…»",
       ["Leggi un annuncio di lavoro.", "Leggi una recensione.", "Ricevi una lettera di licenziamento.", "Leggi un articolo di giornale."],
       "Leggi un annuncio di lavoro."),
      ("«Mi scusi, potrebbe abbassare un po' la musica? Domani mi alzo alle cinque.»",
       ["Parli con un vicino di casa.", "Parli con il tuo capo.", "Scrivi al Comune.", "Telefoni alla polizia."], "Parli con un vicino di casa."),
      ("«Si comunica che, per lavori di manutenzione, l'acqua sarà sospesa giovedì dalle 9 alle 13.»",
       ["Leggi un avviso nell'atrio del condominio.", "Ricevi un invito a una festa.", "Ascolti una canzone.", "Leggi un menù."],
       "Leggi un avviso nell'atrio del condominio.")],
      "Per ogni testo scegli la situazione giusta."),

  {"part": "Prova 4 · Produzione scritta", "min": 70},
  scritto("s1", "1 ✎ · Il tuo parere",
          "Sempre più persone lavorano da casa almeno qualche giorno alla settimana. Secondo alcuni si vive meglio, secondo altri si perdono "
          "i rapporti con i colleghi. Esprimi la tua opinione sui vantaggi e sugli svantaggi del lavoro a distanza.", "120 a 140"),
  scritto("s2", "2 ✎ · L'email",
          "Hai comprato online un elettrodomestico che è arrivato rotto. Il venditore non risponde da una settimana. "
          "Scrivi un'email per raccontare il problema, esprimere la tua insoddisfazione e chiedere una soluzione.", "80 a 100"),

  {"part": "Prova 5 · Produzione orale", "min": 10},
  {"id": "p1", "title": "1 🎤 · Gioco di ruolo", "type": "record",
   "items": ["Sei in un'agenzia immobiliare. Spiega che casa cerchi (zona, prezzo, stanze), fai domande sull'appartamento che ti propongono e chiedi di vederlo."]},
  {"id": "p2", "title": "2 🎤 · Monologo", "type": "record",
   "items": ["Secondo te è meglio vivere in una grande città o in un piccolo paese? Parla per 2-3 minuti con esempi della tua esperienza."]},
 ]
}

# =====================================================================
# C1
# =====================================================================
C1_1 = {
 "title": "🎓 Simulazione d'esame C1 · n. 1", "store": "sim-c1-1",
 "exam": {"soglia": 55, "regole": REGOLE},
 "sub": "Simulazione di un esame di certificazione di livello C1. Leggi le regole e premi «Inizia l'esame».",
 "sections": [
  {"part": "Prova 1 · Ascolto", "min": 40},
  ascolto("a1", "1 · Brevi testi",
          [("F", "Testo uno. Gentili clienti, vi ricordiamo che da lunedì la nostra filiale osserverà un nuovo orario: apertura continuata dalle 8:30 "
                 "alle 15:30. Le operazioni di cassa, però, si potranno fare solo su appuntamento, prenotando tramite l'applicazione."),
           ("M", "Testo due. Guarda, non voglio scoraggiarti, ma prima di lasciare un contratto a tempo indeterminato per aprire un'attività tua "
                 "ci penserei due volte. Non dico di rinunciare: dico solo di fare bene i conti e magari cominciare nei fine settimana."),
           ("F", "Testo tre. Nel suo ultimo romanzo l'autrice abbandona i toni leggeri dei libri precedenti e affronta, con una scrittura asciutta, "
                 "il tema della malattia in famiglia. Un libro difficile, a tratti doloroso, ma che merita di essere letto."),
           ("M", "Testo quattro. Per la riunione di giovedì vi chiedo di leggere il documento allegato e di mandarmi entro mercoledì sera eventuali "
                 "osservazioni. Così potremo dedicare l'incontro alle decisioni, invece di perdere tempo a discutere i dettagli."),
           ("F", "Testo cinque. Secondo una recente indagine, oltre la metà degli italiani tra i 18 e i 34 anni vive ancora con i genitori. "
                 "Le ragioni principali indicate dai giovani sono il costo degli affitti e la difficoltà di trovare un lavoro stabile.")],
          [("1. Nel testo uno si comunica che", ["per alcune operazioni bisogna prenotare", "la filiale chiuderà", "la banca apre il sabato", "l'applicazione non funziona"], "per alcune operazioni bisogna prenotare"),
           ("2. L'uomo del testo due", ["invita alla prudenza", "è contrario a ogni cambiamento", "propone di lavorare insieme", "si congratula per la scelta"], "invita alla prudenza"),
           ("3. Il testo tre è", ["una recensione", "un'intervista", "una pubblicità", "un annuncio"], "una recensione"),
           ("4. Lo scopo del testo quattro è", ["rendere più efficiente una riunione", "annullare una riunione", "presentare un nuovo collega", "chiedere un documento"], "rendere più efficiente una riunione"),
           ("5. Secondo il testo cinque, molti giovani restano in famiglia", ["per motivi economici", "per scelta culturale", "per studiare", "per aiutare i genitori"], "per motivi economici")],
          cons="Ascolta i cinque testi. Completa le frasi: scegli una delle quattro proposte."),
  ascolto("a2", "2 · Il dibattito alla radio",
          [("M", "Benvenuti. Oggi parliamo di intelligenza artificiale a scuola con la professoressa Elena Marzano, che insegna lettere in un liceo di Lecce. "
                 "Professoressa, i suoi studenti la usano?"),
           ("F", "Certo, e sarebbe ingenuo far finta del contrario. Il punto non è vietarla, ma insegnare a usarla. Io all'inizio ero spaventata: "
                 "ricevevo temi perfetti, ma senza anima. Poi ho cambiato il modo di lavorare."),
           ("M", "In che senso?"),
           ("F", "Adesso i ragazzi scrivono una parte in classe, a mano, e poi confrontano il loro testo con quello prodotto dalla macchina. "
                 "Devono trovare gli errori, le frasi vuote, le informazioni non verificate. Scoprono così che lo strumento sbaglia, e anche spesso."),
           ("M", "E i colleghi come hanno reagito?"),
           ("F", "In modo diverso. Alcuni sono entusiasti, altri molto critici. Credo che la scuola abbia bisogno di formazione, non di slogan. "
                 "Il rischio vero non è che gli studenti copino: è che smettano di fare fatica, e senza fatica non si impara."),
           ("M", "Un'ultima domanda: tra dieci anni la scuola sarà molto diversa?"),
           ("F", "Gli strumenti cambieranno, ma il cuore resterà lo stesso: una persona che aiuta un'altra persona a pensare con la propria testa.")],
          [("1. Secondo la professoressa, l'intelligenza artificiale a scuola", ["va insegnata, non vietata", "va vietata", "è inutile", "riguarda solo le materie scientifiche"], "va insegnata, non vietata"),
           ("2. All'inizio la professoressa", ["era preoccupata", "era entusiasta", "non se n'era accorta", "la usava per correggere"], "era preoccupata"),
           ("3. Oggi gli studenti", ["confrontano il proprio testo con quello della macchina", "scrivono solo al computer", "non fanno più temi", "lavorano solo a casa"], "confrontano il proprio testo con quello della macchina"),
           ("4. Per la professoressa il rischio maggiore è", ["che gli studenti rinuncino allo sforzo", "che gli studenti copino", "che i docenti perdano il lavoro", "che le macchine costino troppo"], "che gli studenti rinuncino allo sforzo"),
           ("5. Secondo lei, in futuro la scuola", ["conserverà la sua funzione essenziale", "sarà completamente diversa", "non avrà più insegnanti", "sarà solo online"], "conserverà la sua funzione essenziale")],
          cons="Ascolta il dibattito. Completa le frasi: scegli una delle quattro proposte."),
  ascolto("a3", "3 · Il reportage",
          [("M", "Siamo a Craco, in Basilicata, un paese che negli anni Sessanta è stato abbandonato a causa di una frana. Per decenni le case vuote, "
                 "arroccate sulla collina, sono rimaste un luogo silenzioso, visitato solo da qualche fotografo. Oggi invece Craco è diventato "
                 "uno dei set cinematografici più richiesti d'Italia: qui sono stati girati film italiani e stranieri, e ogni anno arrivano migliaia di turisti. "
                 "Le visite si fanno solo con una guida e con il casco, perché alcuni edifici sono ancora pericolanti. Gli abitanti del nuovo paese, "
                 "costruito più a valle, hanno opinioni diverse: c'è chi è orgoglioso di questa rinascita e chi teme che il paese vecchio diventi "
                 "soltanto uno sfondo per le fotografie. Il sindaco vorrebbe usare gli incassi delle visite per mettere in sicurezza la chiesa principale "
                 "e trasformarla in un museo della memoria, con le voci e le fotografie di chi ci viveva.")],
          [("1. Craco è stato abbandonato per una catastrofe naturale.", None, "Vero"),
           ("2. Il paese è stato abbandonato da pochi anni.", None, "Falso"),
           ("3. Per molto tempo pochissime persone hanno visitato Craco.", None, "Vero"),
           ("4. A Craco si girano solo film italiani.", None, "Falso"),
           ("5. I turisti possono visitare il paese liberamente.", None, "Falso"),
           ("6. Tutti gli abitanti sono contenti del turismo.", None, "Falso"),
           ("7. Il nuovo paese si trova più in basso rispetto a quello vecchio.", None, "Vero"),
           ("8. Il sindaco vuole creare un luogo che conservi la memoria degli abitanti.", None, "Vero")],
          opts=["Vero", "Falso"], cons="Ascolta il reportage. Le informazioni sono vere o false?"),

  {"part": "Prova 2 · Comprensione della lettura", "min": 70},
  lettura("l1", "1 · L'articolo",
          "<b>LA LENTEZZA COME SCELTA</b><br>Negli ultimi anni un numero crescente di persone ha deciso di rallentare: c'è chi rinuncia a una parte dello "
          "stipendio per lavorare meno ore, chi lascia la città per un paese di collina, chi semplicemente spegne il telefono dopo cena. "
          "Non si tratta, come spesso si legge, di una moda passeggera o di un capriccio di chi può permetterselo. Secondo la sociologa Laura Fanelli, "
          "autrice di un saggio sul tema, la scelta della lentezza nasce piuttosto da una stanchezza diffusa: «Abbiamo creduto che la velocità "
          "coincidesse con il progresso, e ci siamo accorti che ci lasciava più soli e più ansiosi». Fanelli invita però a non idealizzare: "
          "rallentare richiede condizioni materiali che non tutti hanno, e il rischio è che diventi un privilegio. Per questo, sostiene, "
          "il tema non riguarda soltanto le scelte individuali, ma anche le politiche pubbliche: orari di lavoro più flessibili, servizi nei piccoli "
          "centri, trasporti che permettano di vivere lontano dalle grandi città senza sentirsi esclusi.",
          [("1. Secondo il testo, la scelta di rallentare", ["è più di una moda", "è un capriccio di pochi", "riguarda solo i giovani", "è in diminuzione"], "è più di una moda"),
           ("2. Per Fanelli la lentezza nasce", ["da una stanchezza collettiva", "dal desiderio di guadagnare", "dalla paura del futuro", "dall'amore per la natura"], "da una stanchezza collettiva"),
           ("3. Secondo la sociologa, la velocità", ["ha aumentato solitudine e ansia", "ha reso tutti più felici", "è necessaria al progresso", "riguarda solo il lavoro"], "ha aumentato solitudine e ansia"),
           ("4. Fanelli avverte che rallentare", ["può diventare un privilegio", "è facile per tutti", "è sempre una scelta sbagliata", "fa perdere il lavoro"], "può diventare un privilegio"),
           ("5. La conclusione del testo è che", ["servono anche interventi pubblici", "ognuno deve arrangiarsi", "bisogna tornare in città", "la tecnologia va vietata"], "servono anche interventi pubblici")],
          cons="Leggi il testo e completa le frasi: scegli una delle quattro proposte."),
  lettura("l2", "2 · Il regolamento",
          "<b>RESIDENZA ARTISTICA «MARE APERTO» · REGOLAMENTO</b><br>La residenza, promossa da una fondazione privata con il patrocinio della Regione, "
          "ospita per quattro settimane, a ottobre, sei artisti under 35 (arti visive, scrittura, musica). La partecipazione è gratuita: la fondazione copre "
          "vitto, alloggio e spese di viaggio fino a 300 euro; non è previsto un compenso. Gli artisti selezionati si impegnano a partecipare ad almeno due "
          "incontri pubblici con le scuole del territorio e a lasciare alla fondazione un'opera o un testo realizzato durante la residenza, che potrà essere "
          "esposto o pubblicato citando sempre l'autore.<br>Le candidature si inviano per posta elettronica entro il 31 maggio con portfolio, lettera "
          "di motivazione e una proposta di progetto. Una giuria composta da tre esperti esterni sceglierà i partecipanti; i nomi saranno pubblicati "
          "sul sito il 30 giugno. Chi ha già partecipato a una delle edizioni precedenti non può ricandidarsi.",
          [("1. La residenza è organizzata direttamente dalla Regione.", None, "Falso"),
           ("2. Possono partecipare artisti di diverse discipline.", None, "Vero"),
           ("3. Gli artisti ricevono uno stipendio.", None, "Falso"),
           ("4. Il viaggio è rimborsato solo in parte se costa più di 300 euro.", None, "Vero"),
           ("5. Gli artisti devono incontrare gli studenti della zona.", None, "Vero"),
           ("6. Le opere realizzate possono essere usate senza indicare l'autore.", None, "Falso"),
           ("7. La giuria è formata da persone della fondazione.", None, "Falso"),
           ("8. Chi ha partecipato in passato può ripresentare domanda.", None, "Falso")],
          opts=["Vero", "Falso"], cons="Leggi il regolamento. Le informazioni sono vere o false?"),
  ordina(["Chi visita Matera oggi fatica a credere che, settant'anni fa, i Sassi fossero considerati una vergogna nazionale.",
          "Migliaia di persone vivevano allora in case scavate nella roccia, spesso insieme agli animali e senza acqua corrente.",
          "Dopo la denuncia di scrittori e politici, negli anni Cinquanta lo Stato decise di trasferire gli abitanti in nuovi quartieri.",
          "Per alcuni fu una liberazione; per altri, la perdita di una comunità e di un modo di vivere fondato sulla solidarietà.",
          "Per decenni i Sassi rimasero quasi vuoti, finché un gruppo di giovani materani cominciò a battersi per il loro recupero.",
          "Il riconoscimento dell'UNESCO, nel 1993, segnò la svolta: le case furono restaurate e la città tornò a vivere.",
          "Oggi Matera è una meta turistica internazionale, e la sfida è evitare che diventi soltanto una bella cartolina."],
         "3 · Ricostruisci il testo", "3 · Riordina", "l3",
         cons="Il testo «La rinascita dei Sassi» è diviso in 7 parti, in disordine. Scrivi il numero giusto (1-7) accanto a ogni parte."),

  {"part": "Prova 3 · Analisi delle strutture di comunicazione", "min": 75},
  cloze("g1", "1 · Completa il testo",
        "Si dice spesso che ___ va piano va sano e va lontano. ___ è vero per molte cose, lo è ancora di più per lo studio delle lingue: "
        "nessuno impara una lingua ___ poche settimane, ___ quello che promettono certe pubblicità. Serve costanza, ___ è anche vero che "
        "la motivazione conta moltissimo. ___ abbia vissuto all'estero lo sa bene: si impara di più parlando con le persone ___ studiando "
        "le regole sui libri. ___, senza un po' di grammatica, è difficile esprimersi in modo preciso. Insomma, ___ metodo si scelga, "
        "l'importante è non arrendersi ___ primi errori.",
        ["chi", "se", "in", "nonostante|malgrado|contrariamente a", "ma|però", "chiunque|chi", "che", "tuttavia|eppure|però", "qualunque|qualsiasi",
         "ai|davanti ai|dopo i"], cons="Completa il testo con una parola per ogni spazio."),
  cloze("g2", "2 · I verbi",
        "Il ponte romano, che ___ (costruire) nel II secolo d.C., è rimasto in piedi per quasi duemila anni. Gli studiosi credevano che ___ (crollare) "
        "durante il terremoto del 1980, invece i lavori hanno dimostrato che le fondamenta ___ (resistere) meglio di quanto si ___ (pensare). "
        "Se i restauri ___ (cominciare) prima, oggi non ___ (essere) necessario chiudere il ponte al traffico. Gli abitanti sperano che i lavori ___ "
        "(terminare) entro l'estate, ma il direttore del cantiere ha dichiarato che ___ (servire) almeno un altro anno. «Prima di riaprirlo, "
        "___ (noi, dovere) essere sicuri che sia stabile», ha spiegato, «perché nessuno ___ (volere) correre rischi».",
        ["fu costruito|è stato costruito|venne costruito", "fosse crollato|crollasse", "hanno resistito", "pensasse|pensava",
         "fossero cominciati", "sarebbe", "terminino|vengano terminati", "servirà|servirebbe", "dobbiamo|dovremo", "vuole|vorrebbe"],
        cons="Completa il testo con le forme giuste dei verbi tra parentesi."),
  scelta("g3", "3 · Completa il testo: scegli la parola", [
      ("Il riciclo dei vestiti usati è uno dei ___ (1) più interessanti dell'economia circolare.", ["ambiti", "luoghi", "motivi", "modi"], "ambiti"),
      ("Ogni anno in Europa si ___ (2) milioni di tonnellate di tessuti ancora utilizzabili.", ["gettano", "perdono", "lanciano", "tolgono"], "gettano"),
      ("Molte aziende hanno ___ (3) a raccogliere gli abiti usati nei negozi.", ["iniziato", "deciso", "provato", "pensato"], "iniziato"),
      ("Gli esperti, tuttavia, ___ (4) che riciclare non basta: bisogna comprare di meno.", ["sostengono", "dicono di", "affermano di", "parlano"], "sostengono"),
      ("Il problema principale è la ___ (5) qualità dei tessuti economici.", ["scarsa", "piccola", "corta", "povera di"], "scarsa"),
      ("Questi capi si rovinano in fretta e non possono essere ___ (6) in nuovi prodotti.", ["trasformati", "cambiati", "girati", "convertiti a"], "trasformati"),
      ("Per questo alcune città hanno ___ (7) negozi dove si scambiano gli abiti.", ["promosso", "spinto", "condotto", "proposto di"], "promosso"),
      ("Una scelta che, oltre all'ambiente, fa bene anche al ___ (8) .", ["portafoglio", "portamonete", "conto", "bilancio di"], "portafoglio")],
      "Leggi le frasi del testo «Una seconda vita per i vestiti» e scegli la parola giusta."),
  {"id": "g4", "title": "4 ✎ · Riformula le frasi", "type": "free", "rows": 3,
   "cons": "Riscrivi le frasi cominciando con le parole date e cambiando la struttura. Il significato deve restare lo stesso. (Le corregge l'insegnante.)",
   "items": ["1. Per iscriversi è necessario aver compiuto 18 anni. → «L'aver compiuto…»",
             "2. Gli organizzatori comunicheranno a tutti il programma entro venerdì. → «Il programma…»",
             "3. Benché piovesse, la manifestazione si è svolta regolarmente. → «Nonostante la…»",
             "4. Il corso permette ai partecipanti di migliorare le proprie competenze digitali. → «Grazie al corso…»"]},

  {"part": "Prova 4 · Produzione scritta", "min": 90},
  scritto("s1", "1 ✎ · Il saggio",
          "Scegli uno dei due argomenti. A) Si discute molto della possibilità di ridurre la settimana lavorativa a quattro giorni a parità di stipendio. "
          "Esprimi la tua opinione. B) Molti musei sono gratuiti la prima domenica del mese: secondo te la cultura dovrebbe essere sempre gratuita? "
          "Esprimi la tua opinione.", "160 a 180"),
  scritto("s2", "2 ✎ · L'email formale",
          "Scegli una delle due situazioni. A) Hai frequentato un corso di aggiornamento professionale che non corrispondeva al programma promesso: "
          "scrivi agli organizzatori per lamentarti e chiedere un rimborso parziale. B) Il tuo condominio ha deciso dei lavori molto costosi senza "
          "consultare tutti i proprietari: scrivi all'amministratore per esprimere il tuo disaccordo e proporre una soluzione.", "100 a 120"),

  {"part": "Prova 5 · Produzione orale", "min": 15},
  {"id": "p1", "title": "1 🎤 · Gioco di ruolo", "type": "record",
   "items": ["Sei il rappresentante dei genitori della classe di tuo figlio. Parla con la dirigente scolastica: la scuola vuole eliminare "
             "le gite scolastiche per motivi economici. Spiega il punto di vista dei genitori e proponi delle alternative."]},
  {"id": "p2", "title": "2 🎤 · Monologo", "type": "record",
   "items": ["Parla per 3-4 minuti: «Il turismo di massa è una ricchezza o un pericolo per le città d'arte?» Porta argomenti a favore e contro ed esempi concreti."]},
 ]
}

SIM_B2C1 = [("esami/b2-1.html", B2_1), ("esami/c1-1.html", C1_1)]
