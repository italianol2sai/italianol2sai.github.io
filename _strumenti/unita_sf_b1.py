"""Percorso B1 sulla traccia degli argomenti di «Nuovo Senza frontiere 3» (Edilingua): unità 2-4 del modulo 1.
Testi, dialoghi, nomi e ascolti NUOVI (Erila, 2026-11-23: «rifaccio tutto con testi nuovi»): si tengono argomenti, grammatica e tipi
di esercizio. Ambientazione: Bari. Stile del livello: "b1" (Source Sans 3 + Merriweather, pagina larga).
Uso: python3 _strumenti/unita_sf_b1.py   (dalla cartella principale del sito)"""
import os, sys
sys.path.insert(0, os.path.dirname(__file__))
from genera import eq, build as build_es
from unita_primi import cover, slide, cards, table, nota, dialogo, end
from unita_drive import vf, scegli, menu, ordina, parla, libero
from teoria import tab, es
from unita_sf import scrivi, ascolto, testo, build_slide, build_giochi

# =====================================================================
# B1 · UNITÀ 2 · ESAME B1 PER LA CITTADINANZA
# =====================================================================
ISCR = [("F", "Ente certificatore, buongiorno. Sono Saleah, come posso aiutarLa?"),
        ("F", "Buongiorno. Vorrei iscrivermi all'esame B1 per la cittadinanza. Potrebbe dirmi quando sono le prossime date?"),
        ("F", "Certo. Le prossime sessioni sono a febbraio e ad aprile. Le iscrizioni si chiudono un mese prima."),
        ("F", "E come si fa l'iscrizione? Dovrei venire in sede?"),
        ("F", "No, si compila il modulo online e si paga con PagoPA. Poi deve firmare il consenso al trattamento dei dati."),
        ("F", "Che cosa significa esattamente?"),
        ("F", "Significa che Lei ci autorizza a usare i Suoi dati solo per l'esame. Senza la firma non possiamo accettare l'iscrizione."),
        ("F", "Capito. Le converrebbe fare qualche simulazione prima, secondo Lei?"),
        ("F", "Sì, glielo consiglierei. Sul nostro sito ci sono delle prove d'esame gratuite.")]
ESAME_SLIDE = [
    cover("📝", "Esame B1 per la cittadinanza", "L'iscrizione · La struttura dell'esame · I pagamenti elettronici", "B1 &bull; Modulo 1 &bull; Unità 2"),
    slide("In questa unità impari a…", cards([
        ("☎️", "Chiedere informazioni in modo cortese", "Potrebbe dirmi…? Vorrei sapere…"), ("📋", "Compilare un modulo", "dati personali, consenso, privacy"),
        ("🗓️", "Parlare di progetti", "Il mese prossimo farò l'esame"), ("💳", "Pagare online", "PagoPA, carta, app IO")])),
    slide("🗂️ Le parole dell'esame", cards([
        ("🏫", "l'ente certificatore", "l'università o l'istituto che fa l'esame (CILS, CELI, PLIDA, Roma Tre)"),
        ("🗓️", "il calendario degli esami", "le date delle sessioni"), ("✍️", "il modulo di iscrizione", "si compila online"),
        ("🔒", "la privacy", "la protezione dei dati personali"), ("✅", "il consenso", "l'autorizzazione firmata a usare i dati"),
        ("🏅", "la certificazione", "il diploma che dimostra il tuo livello")], "g3")),
    slide("☎️ Lezione A · L'iscrizione", dialogo([("*Saleah (ente)" if i % 2 == 0 else "Ana", t) for i, (_, t) in enumerate(ISCR)])),
    slide("📘 Il condizionale presente", table([
        ["io", "vorr<b>ei</b>", "potr<b>ei</b>", "parler<b>ei</b>"], ["tu", "vorr<b>esti</b>", "potr<b>esti</b>", "parler<b>esti</b>"],
        ["lui / lei / Lei", "vorr<b>ebbe</b>", "potr<b>ebbe</b>", "parler<b>ebbe</b>"], ["noi", "vorr<b>emmo</b>", "potr<b>emmo</b>", "parler<b>emmo</b>"],
        ["voi", "vorr<b>este</b>", "potr<b>este</b>", "parler<b>este</b>"], ["loro", "vorr<b>ebbero</b>", "potr<b>ebbero</b>", "parler<b>ebbero</b>"]],
        head=["", "volere", "potere", "parlare"]) + "\n" + nota(
        "Si usa per: <b>chiedere con cortesia</b> (Potrebbe ripetere?), <b>desideri</b> (Vorrei la cittadinanza), "
        "<b>consigli</b> (Dovresti studiare), <b>dubbi e possibilità</b> (Potrebbe essere difficile).")),
    slide("🧩 Lezione B · Com'è fatto l'esame", testo(
        "L'esame B1 per la cittadinanza ha <b>quattro prove</b>: ascolto, lettura, scrittura e una prova orale. "
        "Nell'ascolto sentirai brevi testi della vita quotidiana, per esempio un annuncio in stazione o un messaggio in segreteria.",
        "Nella lettura risponderai a domande su un avviso o un articolo. Nella scrittura dovrai scrivere un messaggio o una email. "
        "All'orale parlerai di te e della tua esperienza in Italia. Per superare l'esame dovrai prendere il punteggio minimo in <b>ogni</b> prova.")),
    slide("📘 Il futuro semplice", table([
        ["io", "parler<b>ò</b>", "scriver<b>ò</b>", "sar<b>ò</b>", "avr<b>ò</b>"], ["tu", "parler<b>ai</b>", "scriver<b>ai</b>", "sar<b>ai</b>", "avr<b>ai</b>"],
        ["lui / lei", "parler<b>à</b>", "scriver<b>à</b>", "sar<b>à</b>", "avr<b>à</b>"], ["noi", "parler<b>emo</b>", "scriver<b>emo</b>", "sar<b>emo</b>", "avr<b>emo</b>"],
        ["voi", "parler<b>ete</b>", "scriver<b>ete</b>", "sar<b>ete</b>", "avr<b>ete</b>"], ["loro", "parler<b>anno</b>", "scriver<b>anno</b>", "sar<b>anno</b>", "avr<b>anno</b>"]],
        head=["", "parlare", "scrivere", "essere", "avere"]) + "\n" + nota(
        "Usi: <b>progetti</b> (A febbraio farò l'esame), <b>previsioni</b> (Sarà facile), <b>ipotesi</b> (Saranno le dieci). "
        "Irregolari: andare → andrò, fare → farò, venire → verrò, dovere → dovrò, potere → potrò.")),
    slide("📘 Pronomi e aggettivi indefiniti", table([
        ["qualche", "+ singolare", "Farò <b>qualche</b> simulazione."], ["alcuni / alcune", "+ plurale", "<b>Alcune</b> domande sono difficili."],
        ["ogni", "+ singolare", "Devi superare <b>ogni</b> prova."], ["qualcuno / nessuno", "persone", "<b>Nessuno</b> ha copiato."],
        ["qualcosa / niente", "cose", "Hai <b>qualcosa</b> da chiedere? Non ho capito <b>niente</b>."], ["tutto / tutti", "", "Ho risposto a <b>tutte</b> le domande."]],
        head=["parola", "con", "esempio"])),
    slide("💳 Educazione civica · I pagamenti elettronici", cards([
        ("🧾", "PagoPA", "il sistema per pagare la Pubblica Amministrazione: tasse, multe, iscrizioni"),
        ("📱", "l'app IO", "l'app dei servizi pubblici: avvisi, pagamenti, documenti"),
        ("💳", "carta di debito o prepagata", "i soldi escono subito dal conto o dalla carta"),
        ("🏦", "il bonifico", "trasferimento da un conto all'altro con l'IBAN"),
        ("🔐", "attenzione alle truffe", "nessun ente chiede il PIN o la password per telefono"),
        ("🧾", "la ricevuta", "conservala sempre: è la prova del pagamento")], "g3")),
    end("Ora sai iscriverti all'esame e sai com'è fatto!"),
]
B1ESAME = {
 "title": "📝 Esame B1 per la cittadinanza · Esercizi", "store": "b1-esame-cittadinanza", "livello": "b1",
 "sections": [
  {"part": "Le parole"},
  menu(["l'ente certificatore", "il consenso", "la privacy", "la certificazione", "il calendario", "il modulo"],
       [("1. Il documento che dimostra il tuo livello di italiano.", "la certificazione"), ("2. L'autorizzazione a usare i tuoi dati.", "il consenso"),
        ("3. L'istituto che organizza l'esame.", "l'ente certificatore"), ("4. La protezione dei dati personali.", "la privacy"),
        ("5. Le date delle sessioni d'esame.", "il calendario"), ("6. Lo compili online per iscriverti.", "il modulo")],
       "1 · Che cos'è?", "1 · Le parole", "e1"),
  {"part": "Lezione A · L'iscrizione"},
  ascolto(scegli([("1. Ana telefona per…", ["iscriversi all'esame", "sapere il risultato", "cambiare la data"], "iscriversi all'esame"),
                  ("2. Le prossime sessioni sono…", ["a gennaio e a marzo", "a febbraio e ad aprile", "a maggio"], "a febbraio e ad aprile"),
                  ("3. L'iscrizione si fa…", ["in sede", "online", "per posta"], "online"),
                  ("4. Senza il consenso firmato…", ["si paga di più", "l'iscrizione non è accettata", "si fa solo l'orale"], "l'iscrizione non è accettata"),
                  ("5. Saleah consiglia di…", ["fare delle simulazioni", "comprare un libro", "aspettare un anno"], "fare delle simulazioni")],
                 "2 · 🎧 Ascolta la telefonata", "2 · La telefonata", "e2"), [list(x) for x in ISCR]),
  {"part": "Il condizionale presente", "teoria":
     tab(("io", "-rei"), ("tu", "-resti"), ("lui / lei / Lei", "-rebbe"), ("noi", "-remmo"), ("voi", "-reste"), ("loro", "-rebbero"), head=("persona", "desinenza")) +
     "Per chiedere con cortesia, esprimere desideri, dare consigli." + es("<b>Potrebbe</b> ripetere? · <b>Vorrei</b> iscrivermi. · <b>Dovresti</b> esercitarti.")},
  scrivi([("1. (potere – Lei) … ripetere la data, per favore?", ("potrebbe",)), ("2. (volere – io) … sapere quanto costa l'esame.", ("vorrei",)),
          ("3. (dovere – tu) … fare qualche simulazione.", ("dovresti",)), ("4. (piacere – a noi) Ci … studiare insieme.", ("piacerebbe",)),
          ("5. (essere – voi) … disponibili sabato mattina?", ("sareste",)), ("6. (avere – loro) Secondo me … bisogno di più tempo.", ("avrebbero",))],
         "3 · Completa con il condizionale", "3 · Condizionale", "e3", w="m"),
  menu(["richiesta cortese", "desiderio", "consiglio", "dubbio / possibilità"],
       [("1. Potrebbe mandarmi il modulo per email?", "richiesta cortese"), ("2. Vorrei diventare cittadino italiano.", "desiderio"),
        ("3. Dovresti leggere un giornale ogni giorno.", "consiglio"), ("4. L'orale potrebbe essere difficile per me.", "dubbio / possibilità"),
        ("5. Al posto tuo, mi iscriverei ad aprile.", "consiglio"), ("6. Mi piacerebbe fare l'esame a Bari.", "desiderio")],
       "4 · A che cosa serve il condizionale?", "4 · Usi", "e4"),
  {"part": "Lezione B · La struttura dell'esame"},
  vf(["1. L'esame ha tre prove.", "2. Nell'ascolto ci sono testi della vita quotidiana.", "3. Nella scrittura si scrive un messaggio o una email.",
      "4. All'orale si parla di sé e dell'esperienza in Italia.", "5. Basta un buon punteggio totale, anche con una prova insufficiente."],
     ["FALSO", "VERO", "VERO", "VERO", "FALSO"], "5 · Leggi il testo delle slide: vero o falso?", "5 · L'esame", "e5",
     info="L'esame B1 per la cittadinanza ha quattro prove: ascolto, lettura, scrittura e una prova orale. Nell'ascolto sentirai brevi testi della vita quotidiana. "
          "Nella lettura risponderai a domande su un avviso o un articolo. Nella scrittura dovrai scrivere un messaggio o una email. All'orale parlerai di te e della tua esperienza in Italia. "
          "Per superare l'esame dovrai prendere il punteggio minimo in ogni prova."),
  {"part": "Il futuro semplice", "teoria":
     tab(("parlare", "parlerò, parlerai, parlerà…"), ("scrivere", "scriverò, scriverai, scriverà…"), ("essere / avere", "sarò / avrò"), head=("verbo", "futuro")) +
     "Per progetti, previsioni e ipotesi." + es("A febbraio <b>farò</b> l'esame. · <b>Sarà</b> facile!")},
  scrivi([("1. (fare – io) Il mese prossimo … l'esame.", ("farò",)), ("2. (studiare – noi) Questo fine settimana … in biblioteca.", ("studieremo",)),
          ("3. (arrivare – i risultati) I risultati … dopo due mesi.", ("arriveranno",)), ("4. (essere – tu) Domani … nervoso, ma andrà bene!", ("sarai",)),
          ("5. (venire – voi) … anche voi a fare l'esame?", ("verrete",)), ("6. (potere – Ana) Con la certificazione … fare domanda di cittadinanza.", ("potrà",))],
         "6 · Completa con il futuro", "6 · Futuro", "e6", w="m"),
  {"part": "Pronomi e aggettivi indefiniti", "teoria":
     tab(("qualche / ogni", "+ nome singolare"), ("alcuni / alcune", "+ nome plurale"), ("qualcuno / nessuno", "persone"), ("qualcosa / niente", "cose"), head=("parola", "si usa con")) +
     es("Farò <b>qualche</b> simulazione. · Non ho capito <b>niente</b>.")},
  scegli([("1. Ho fatto … esercizio di ascolto.", ["qualche", "alcuni", "qualcosa"], "qualche"), ("2. … candidati sono arrivati in ritardo.", ["Ogni", "Alcuni", "Qualche"], "Alcuni"),
          ("3. C'è … che ha una penna?", ["qualcosa", "qualcuno", "ogni"], "qualcuno"), ("4. Non ho dimenticato …: ho tutti i documenti.", ["niente", "nessuno", "ogni"], "niente"),
          ("5. … prova dura circa mezz'ora.", ["Ogni", "Tutte", "Alcune"], "Ogni"), ("6. Ho risposto a … le domande.", ["ogni", "tutte", "qualche"], "tutte")],
         "7 · Scegli l'indefinito giusto", "7 · Indefiniti", "e7"),
  {"part": "Educazione civica · I pagamenti elettronici"},
  vf(["1. Con PagoPA si pagano tasse e servizi pubblici.", "2. L'app IO serve solo per mandare messaggi agli amici.", "3. Per un bonifico serve l'IBAN.",
      "4. La banca può chiederti il PIN per telefono.", "5. È meglio conservare la ricevuta del pagamento."],
     ["VERO", "FALSO", "VERO", "FALSO", "VERO"], "8 · Pagare online: vero o falso?", "8 · Pagamenti", "e8"),
  libero("e9", 9, "La nostra classe: consigli per l'esame", "Scrivi 5 consigli per un compagno che deve fare l'esame B1. Usa il condizionale (dovresti, potresti…) e il futuro.", ["I miei consigli"], rows=5),
  parla("e10", 10, "Perché vuoi fare l'esame B1? Quali sono i tuoi progetti per il futuro in Italia?"),
 ]
}

# =====================================================================
# B1 · UNITÀ 3 · IL MONDO DIGITALE
# =====================================================================
BANCA = [("M", "Servizio clienti, sono Cristian. Mi dica."),
         ("F", "Buongiorno. Ieri sera volevo fare un bonifico con l'home banking, ma l'app si è bloccata. E adesso il pagamento risulta in sospeso!"),
         ("M", "Mi dispiace. Che cosa stava facendo quando si è bloccata?"),
         ("F", "Stavo inserendo il codice che mi era arrivato per SMS. Poi è apparso un messaggio di errore."),
         ("M", "Capisco. Il bonifico non è partito: i soldi sono ancora sul Suo conto. Può riprovare tra un'ora."),
         ("F", "Non è la prima volta, però! Anche la settimana scorsa l'app non funzionava."),
         ("M", "Ha ragione, c'erano dei lavori sul sistema. Le apro una segnalazione, così un tecnico La richiama.")]
DIG_SLIDE = [
    cover("💻", "Il mondo digitale", "L'home banking · La videochiamata · Internet e gli italiani", "B1 &bull; Modulo 1 &bull; Unità 3"),
    slide("In questa unità impari a…", cards([
        ("📲", "Seguire istruzioni online", "accedi, inserisci il codice, conferma"), ("😤", "Protestare al telefono", "Non è la prima volta!"),
        ("🎥", "Raccontare una videochiamata", "Quando mi hanno chiamato, avevo già…"), ("🌐", "Parlare di internet", "piattaforme, forum, social")])),
    slide("📲 Le parole del digitale", cards([
        ("🏦", "l'home banking", "la banca sul computer o sul telefono"), ("🔢", "il codice OTP", "un codice usa e getta che arriva per SMS"),
        ("👤", "l'operatore", "la persona del servizio clienti"), ("💻", "la piattaforma", "il sito o l'app per lezioni e riunioni online"),
        ("💬", "il forum", "uno spazio dove le persone scrivono e rispondono"), ("🔗", "il link", "l'indirizzo da cliccare")], "g3")),
    slide("📘 Istruzioni · Fare un bonifico online", testo(
        "1. Apri l'app della banca e <b>accedi</b> con le tue credenziali.", "2. Scegli «Bonifico» e <b>inserisci</b> l'IBAN del destinatario.",
        "3. Scrivi l'importo e la causale (per esempio «affitto novembre»).", "4. <b>Conferma</b> con il codice che ricevi per SMS.",
        "5. Salva o scarica la ricevuta.")),
    slide("☎️ Lezione A · Al servizio clienti", dialogo([("*Cristian (banca)" if v == "M" else "Nadia", t) for v, t in BANCA])),
    slide("📘 Passato prossimo o imperfetto?", table([
        ["fatto concluso, una volta", "passato prossimo", "L'app <b>si è bloccata</b>."], ["azione in corso (sfondo)", "imperfetto", "<b>Stavo inserendo</b> / <b>inserivo</b> il codice…"],
        ["descrizione, stato", "imperfetto", "<b>C'erano</b> dei lavori sul sistema."], ["intenzione non realizzata", "imperfetto", "<b>Volevo</b> fare un bonifico, ma…"]],
        head=["situazione", "tempo", "esempio"]) + "\n" + nota("<b>Mentre</b> + imperfetto · <b>quando</b> / <b>all'improvviso</b> + passato prossimo: Mentre pagavo, è andata via la linea.")),
    slide("🎥 Lezione B · La videochiamata", testo(
        "Domenica scorsa ho fatto una videochiamata con la mia famiglia in Perù. Avevo preparato tutto: <b>avevo caricato</b> il tablet e "
        "<b>avevo scaricato</b> la nuova versione dell'app. Quando mia madre ha risposto, però, mio fratello non era ancora arrivato: "
        "<b>aveva perso</b> l'autobus!",
        "Abbiamo parlato per un'ora. Mia nipote mi ha fatto vedere il disegno che <b>aveva fatto</b> per me a scuola. "
        "Alla fine eravamo tutti commossi.")),
    slide("📘 Il trapassato prossimo", table([
        ["avere all'imperfetto + participio", "avevo caricato · avevi scaricato · aveva fatto"], ["essere all'imperfetto + participio", "ero arrivato/a · era uscito/a · erano partiti/e"]],
        head=["forma", "esempi"]) + "\n" + nota("Il trapassato racconta un fatto <b>prima</b> di un altro fatto passato: "
        "Quando mia madre ha risposto, mio fratello <b>non era ancora arrivato</b>.")),
    slide("🌐 Educazione civica · Internet e gli italiani", cards([
        ("📱", "lo smartphone", "è lo strumento più usato per andare su internet"), ("🧓", "il divario digitale", "molti anziani hanno difficoltà con i servizi online"),
        ("🏛️", "i servizi pubblici online", "SPID, CIE, app IO, fascicolo sanitario"), ("📚", "i corsi gratuiti", "biblioteche e centri offrono corsi di informatica"),
        ("🛡️", "la sicurezza", "password diverse, attenzione ai link strani"), ("🧠", "le fake news", "controlla sempre la fonte di una notizia")], "g3")),
    end("Ora sai muoverti meglio nel mondo digitale!"),
]
B1DIG = {
 "title": "💻 Il mondo digitale · Esercizi", "store": "b1-mondo-digitale", "livello": "b1",
 "sections": [
  {"part": "Le parole del digitale"},
  menu(["l'home banking", "il codice OTP", "la piattaforma", "il forum", "il link", "l'operatore"],
       [("1. Lo clicchi per aprire una pagina.", "il link"), ("2. La banca sul telefono.", "l'home banking"),
        ("3. Ti risponde al servizio clienti.", "l'operatore"), ("4. Arriva per SMS e vale pochi minuti.", "il codice OTP"),
        ("5. Qui le persone fanno domande e rispondono.", "il forum"), ("6. La usi per le lezioni online.", "la piattaforma")],
       "1 · Che cos'è?", "1 · Le parole", "e1"),
  ordina(["Apri l'app e accedi con le credenziali.", "Scegli «Bonifico».", "Inserisci l'IBAN del destinatario.", "Scrivi l'importo e la causale.",
          "Conferma con il codice dell'SMS.", "Salva la ricevuta."], "2 · Metti in ordine le istruzioni", "2 · Le istruzioni", "e2"),
  {"part": "Lezione A · Al servizio clienti"},
  ascolto(vf(["1. Nadia voleva pagare con l'home banking.", "2. L'app si è bloccata stamattina.", "3. Stava inserendo il codice dell'SMS.",
              "4. I soldi sono usciti dal conto.", "5. È la prima volta che ha un problema.", "6. Un tecnico la richiamerà."],
             ["VERO", "FALSO", "VERO", "FALSO", "FALSO", "VERO"], "3 · 🎧 Ascolta la telefonata: vero o falso?", "3 · La telefonata", "e3"), [list(x) for x in BANCA]),
  {"part": "Passato prossimo o imperfetto?", "teoria":
     tab(("fatto concluso", "passato prossimo"), ("azione in corso, descrizione", "imperfetto"), ("intenzione non realizzata", "imperfetto (volevo…)"), head=("situazione", "tempo")) +
     "<b>Mentre</b> + imperfetto; <b>quando, all'improvviso</b> + passato prossimo." + es("<b>Mentre pagavo</b>, <b>è andata via</b> la linea.")},
  scegli([("1. Mentre … la password, è suonato il telefono.", ["scrivevo", "ho scritto"], "scrivevo"), ("2. Ieri … un nuovo account.", ["creavo", "ho creato"], "ho creato"),
          ("3. … comprare i biglietti online, ma il sito non funzionava.", ["Volevo", "Ho voluto"], "Volevo"), ("4. Quando ero piccola, non … il computer.", ["avevo", "ho avuto"], "avevo"),
          ("5. All'improvviso lo schermo … nero.", ["diventava", "è diventato"], "è diventato"), ("6. C'… molte persone collegate alla lezione.", ["erano", "sono state"], "erano")],
         "4 · Scegli il tempo giusto", "4 · Pass. prossimo / imperfetto", "e4"),
  {"id": "e5", "title": "5 · Protestare con cortesia", "short": "5 · Protestare", "type": "choice", "full": True,
   "items": [{"q": "1. Vuoi dire che il problema si ripete.", "opts": ["Non è la prima volta!", "Che bella giornata!", "Va bene così."]},
             {"q": "2. Vuoi una soluzione.", "opts": ["Che cosa potete fare per me?", "Arrivederci.", "Non importa."]},
             {"q": "3. Sei arrabbiato ma vuoi restare cortese.", "opts": ["Capisco, però sono molto deluso.", "Siete tutti incapaci!", "Non mi interessa niente."]},
             {"q": "4. Vuoi parlare con qualcun altro.", "opts": ["Potrei parlare con un responsabile?", "Mi passi chiunque!", "Basta!"]}],
   "k": [eq("Non è la prima volta!"), eq("Che cosa potete fare per me?"), eq("Capisco, però sono molto deluso."), eq("Potrei parlare con un responsabile?")]},
  {"part": "Lezione B · La videochiamata"},
  vf(["1. La videochiamata era con la famiglia in Perù.", "2. Il tablet era scarico.", "3. Il fratello non era ancora arrivato.",
      "4. La nipote aveva fatto un disegno.", "5. Hanno parlato per dieci minuti."], ["VERO", "FALSO", "VERO", "VERO", "FALSO"],
     "6 · Leggi il racconto delle slide: vero o falso?", "6 · Il racconto", "e6",
     info="Domenica scorsa ho fatto una videochiamata con la mia famiglia in Perù. Avevo preparato tutto: avevo caricato il tablet e avevo scaricato la nuova versione dell'app. "
          "Quando mia madre ha risposto, però, mio fratello non era ancora arrivato: aveva perso l'autobus! Abbiamo parlato per un'ora. "
          "Mia nipote mi ha fatto vedere il disegno che aveva fatto per me a scuola."),
  {"part": "Il trapassato prossimo", "teoria":
     tab(("avevo, avevi, aveva…", "+ participio"), ("ero, eri, era…", "+ participio (accordato)"), head=("ausiliare all'imperfetto", "")) +
     "Un fatto <b>prima</b> di un altro fatto passato." + es("Quando sono arrivato, la lezione <b>era già cominciata</b>.")},
  scrivi([("1. (io – scaricare) Non potevo entrare perché non … l'app.", ("avevo scaricato",)), ("2. (la lezione – cominciare) Quando mi sono collegata, la lezione … già …", ("era cominciata", "era già cominciata")),
          ("3. (noi – dimenticare) … la password, così abbiamo chiamato l'assistenza.", ("avevamo dimenticato",)), ("4. (Michele – uscire) Ho telefonato a casa, ma Michele … già …", ("era uscito", "era già uscito")),
          ("5. (loro – ricevere) Non … il link, quindi non sono entrati.", ("avevano ricevuto",))],
         "7 · Completa con il trapassato prossimo", "7 · Trapassato", "e7", w="l"),
  {"part": "Educazione civica · Internet e gli italiani"},
  vf(["1. Lo smartphone è lo strumento più usato per internet.", "2. Tutti gli anziani usano facilmente i servizi online.", "3. Biblioteche e centri offrono corsi di informatica.",
      "4. È meglio usare la stessa password per tutto.", "5. Prima di condividere una notizia, bisogna controllare la fonte."],
     ["VERO", "FALSO", "VERO", "FALSO", "VERO"], "8 · Internet in Italia: vero o falso?", "8 · Internet", "e8"),
  libero("e9", 9, "Racconta un problema digitale", "Racconta un problema che hai avuto con un'app, un sito o il telefono. Usa passato prossimo, imperfetto e trapassato.", ["Il mio racconto"], rows=6),
  parla("e10", 10, "Come usi internet ogni giorno? Quali servizi online usi in Italia? Ti piacciono le videochiamate?"),
 ]
}

# =====================================================================
# B1 · UNITÀ 4 · LA DENUNCIA
# =====================================================================
POLIZIA = [("M", "Buongiorno, si sieda. Che cosa è successo?"),
           ("F", "Mi hanno rubato la borsa ieri sera, verso le nove, in corso Vittorio Emanuele."),
           ("M", "Mi racconti con calma."),
           ("F", "Stavo aspettando l'autobus. All'improvviso un ragazzo in motorino si è avvicinato e mi ha strappato la borsa. Poi è scappato verso il lungomare."),
           ("M", "Che cosa c'era nella borsa?"),
           ("F", "Il portafoglio con cinquanta euro, la carta d'identità e il permesso di soggiorno. Le chiavi di casa no, per fortuna: le avevo in tasca."),
           ("M", "Ha già bloccato la carta del bancomat?"),
           ("F", "Sì, ci ho pensato subito, appena sono tornata a casa."),
           ("M", "Bene. Adesso scriviamo il verbale. Con la copia della denuncia potrà chiedere il duplicato dei documenti.")]
DEN_SLIDE = [
    cover("🚓", "La denuncia", "Alla polizia · Videochiamate ed emoji", "B1 &bull; Modulo 1 &bull; Unità 4"),
    slide("In questa unità impari a…", cards([
        ("🗣️", "Raccontare un fatto improvviso", "Stavo aspettando… all'improvviso…"), ("📝", "Fare una denuncia", "furto, scippo, smarrimento"),
        ("🔗", "Collegare le frasi", "prima, poi, perché, quindi, se, per"), ("😊", "Raccontare emozioni nei messaggi", "emoji e messaggistica")])),
    slide("🚨 Le parole della denuncia", cards([
        ("👜", "lo scippo", "qualcuno ti strappa la borsa e scappa"), ("🏠", "il furto", "qualcuno ruba qualcosa, anche in casa"),
        ("🔎", "lo smarrimento", "hai perso qualcosa"), ("🕵️", "il truffatore", "ti inganna per avere soldi"),
        ("📝", "il verbale", "il documento scritto dalla polizia"), ("🏢", "il commissariato / la caserma", "polizia / carabinieri")], "g3")),
    slide("🚓 Lezione A · Al commissariato", dialogo([("*Agente Michele" if v == "M" else "Eneida", t) for v, t in POLIZIA])),
    slide("📘 Le particelle ci e ne", table([
        ["ci = lì, in quel posto", "Vai in commissariato? Sì, <b>ci</b> vado domani."], ["ci = a questa cosa", "Il bancomat? <b>Ci</b> ho pensato subito."],
        ["ne = di questo, di questa cosa", "Della rapina? Non <b>ne</b> so niente."], ["ne = una quantità", "Documenti? <b>Ne</b> avevo tre nella borsa."]],
        head=["significato", "esempio"])),
    slide("📘 I connettivi", table([
        ["tempo", "prima, poi, dopo, mentre, quando, appena, alla fine"], ["causa", "perché, siccome, dato che"],
        ["conseguenza", "quindi, perciò, così"], ["scopo (finale)", "per + infinito, perché + congiuntivo"],
        ["ipotesi", "se, nel caso in cui"], ["contrasto", "ma, però, invece, anche se"]], head=["tipo", "parole"])),
    slide("💬 Lezione B · Messaggi ed emoji", testo(
        "<b>Eneida:</b> Ragazzi, ieri mi hanno scippato la borsa 😢 Sto bene, solo tanta paura 😰",
        "<b>Silvia:</b> Nooo 😱 Hai fatto la denuncia? Se vuoi, ti accompagno io per rifare i documenti 🤗",
        "<b>Eneida:</b> Sì, l'ho fatta stamattina ✅ Grazie, sei un tesoro ❤️ Per rifare la carta d'identità devo prendere appuntamento in Comune.",
        "<b>Giovanni:</b> Che brutta storia 😔 Siccome domani sono libero, posso darti un passaggio 🚗")),
    slide("📘 I pronomi con l'infinito", table([
        ["accompagnare + ti", "accompagnar<b>ti</b>", "Posso accompagnar<b>ti</b> io."], ["fare + la", "far<b>la</b>", "Devo far<b>la</b> subito."],
        ["rifare + li", "rifar<b>li</b>", "Per rifar<b>li</b> serve la denuncia."], ["darti / ti posso dare", "", "Posso dar<b>ti</b> un passaggio = <b>Ti</b> posso dare un passaggio."]],
        head=["", "forma", "esempio"]) + "\n" + nota("Con l'infinito il pronome si attacca <b>alla fine</b>, senza la <b>-e</b>: accompagnar<b>e</b> → accompagnar<b>ti</b>.")),
    slide("😊 Educazione civica · Gli emoji", cards([
        ("🌍", "un linguaggio quasi universale", "ma alcuni emoji cambiano significato da cultura a cultura"),
        ("👍", "nei messaggi informali", "con amici, colleghi stretti, gruppi"), ("🎩", "nelle email formali", "meglio non usarli: ufficio, scuola, datore di lavoro"),
        ("🙏", "attenzione all'ambiguità", "🙏 può essere «grazie», «per favore» o «preghiera»"),
        ("👥", "nei gruppi", "rispetto e niente messaggi offensivi: alcune offese sono reati"),
        ("🔒", "la privacy", "non condividere foto e dati degli altri senza permesso")], "g3")),
    end("Ora sai fare una denuncia e raccontare quello che ti è successo!"),
]
B1DEN = {
 "title": "🚓 La denuncia · Esercizi", "store": "b1-la-denuncia", "livello": "b1",
 "sections": [
  {"part": "Le parole"},
  menu(["lo scippo", "il furto", "lo smarrimento", "il truffatore", "il verbale", "la caserma"],
       [("1. Ho perso il portafoglio: è uno …", "lo smarrimento"), ("2. Un ragazzo in motorino mi ha strappato la borsa: è uno …", "lo scippo"),
        ("3. Sono entrati in casa e hanno preso la TV: è un …", "il furto"), ("4. Mi ha venduto un telefono falso: è un …", "il truffatore"),
        ("5. Il documento che scrive l'agente: …", "il verbale"), ("6. L'ufficio dei carabinieri: …", "la caserma")],
       "1 · Che cos'è successo?", "1 · Le parole", "e1"),
  {"part": "Lezione A · Al commissariato"},
  ascolto(scegli([("1. Il fatto è successo…", ["stamattina", "ieri sera verso le nove", "una settimana fa"], "ieri sera verso le nove"),
                  ("2. Eneida stava…", ["aspettando l'autobus", "facendo la spesa", "tornando dal lavoro in bici"], "aspettando l'autobus"),
                  ("3. Il ragazzo…", ["era a piedi", "era in motorino", "era in macchina"], "era in motorino"),
                  ("4. Nella borsa non c'erano…", ["i documenti", "le chiavi di casa", "i soldi"], "le chiavi di casa"),
                  ("5. Con la copia della denuncia può…", ["avere i soldi indietro", "chiedere il duplicato dei documenti", "non pagare l'autobus"], "chiedere il duplicato dei documenti")],
                 "2 · 🎧 Ascolta la denuncia", "2 · La denuncia", "e2"), [list(x) for x in POLIZIA]),
  ordina(["Stavo aspettando l'autobus.", "All'improvviso è arrivato un ragazzo in motorino.", "Mi ha strappato la borsa.", "È scappato verso il lungomare.",
          "Sono tornata a casa e ho bloccato il bancomat.", "La mattina dopo sono andata in commissariato."], "3 · Metti in ordine il racconto", "3 · Il racconto", "e3"),
  {"part": "Le particelle ci e ne", "teoria":
     tab(("ci", "in quel posto / a quella cosa"), ("ne", "di quella cosa / una quantità"), head=("particella", "sostituisce")) +
     es("In questura? <b>Ci</b> vado domani.", "Quanti documenti hai perso? <b>Ne</b> ho persi due.")},
  menu(["ci", "ne"],
       [("1. Sei mai stato in commissariato? Sì, … sono stato una volta.", "ci"), ("2. Hai parlato del furto con il padrone di casa? Sì, … ho parlato.", "ne"),
        ("3. Quante chiavi avevi? … avevo due.", "ne"), ("4. Hai pensato a bloccare la carta? Sì, … ho pensato subito.", "ci"),
        ("5. Torni in Comune domani? Sì, … torno alle nove.", "ci"), ("6. Vuoi del caffè? No grazie, non … voglio.", "ne")],
       "4 · Ci o ne?", "4 · ci / ne", "e4"),
  {"part": "I connettivi", "teoria":
     tab(("tempo", "prima, poi, mentre, quando, appena"), ("causa", "perché, siccome"), ("conseguenza", "quindi, perciò"), ("scopo", "per + infinito"), ("ipotesi", "se"), head=("tipo", "esempi")) +
     es("<b>Siccome</b> avevo paura, ho chiamato il 112.")},
  menu(["mentre", "siccome", "quindi", "per", "se", "appena"],
       [("1. … aspettavo l'autobus, è arrivato un motorino.", "mentre"), ("2. … sono tornata a casa, ho bloccato la carta.", "appena"),
        ("3. … era buio, non ho visto bene la faccia.", "siccome"), ("4. Ho perso i documenti, … devo fare la denuncia.", "quindi"),
        ("5. Sono andata in Comune … rifare la carta d'identità.", "per"), ("6. … vedi qualcosa di strano, chiama il 112.", "se")],
       "5 · Scegli il connettivo", "5 · Connettivi", "e5"),
  {"part": "Lezione B · Messaggi ed emoji"},
  vf(["1. Eneida ha avuto paura.", "2. Silvia propone di accompagnarla.", "3. Eneida non ha ancora fatto la denuncia.",
      "4. Per la carta d'identità deve prendere appuntamento in Comune.", "5. Giovanni domani lavora tutto il giorno."], ["VERO", "VERO", "FALSO", "VERO", "FALSO"],
     "6 · Leggi la chat delle slide: vero o falso?", "6 · La chat", "e6",
     info="<b>Eneida:</b> Ragazzi, ieri mi hanno scippato la borsa 😢 Sto bene, solo tanta paura 😰<br><b>Silvia:</b> Nooo 😱 Hai fatto la denuncia? Se vuoi, ti accompagno io per rifare i documenti 🤗<br>"
          "<b>Eneida:</b> Sì, l'ho fatta stamattina ✅ Grazie, sei un tesoro ❤️ Per rifare la carta d'identità devo prendere appuntamento in Comune.<br><b>Giovanni:</b> Che brutta storia 😔 Siccome domani sono libero, posso darti un passaggio 🚗"),
  {"part": "I pronomi con l'infinito", "teoria":
     "Con l'infinito il pronome si attacca alla fine e cade la <b>-e</b>." + es("accompagnare + ti → <b>accompagnarti</b>", "Devo fare la denuncia → Devo <b>farla</b>.")},
  scrivi([("1. Devo fare la denuncia → Devo …", ("farla",)), ("2. Posso aiutare te? → Posso …", ("aiutarti",)),
          ("3. Vado in Comune per rifare i documenti → per …", ("rifarli",)), ("4. Voglio ringraziare Silvia → Voglio …", ("ringraziarla",)),
          ("5. Puoi chiamare noi stasera? → Puoi …", ("chiamarci",))],
         "7 · Riscrivi con il pronome", "7 · Pronomi + infinito", "e7", w="m"),
  {"part": "Educazione civica · Gli emoji"},
  scegli([("1. Scrivi una email al datore di lavoro. Usi gli emoji?", ["Sì, tanti", "Meglio di no"], "Meglio di no"),
          ("2. 🙏 significa sempre «grazie»?", ["Sì, in tutto il mondo", "No, può avere più significati"], "No, può avere più significati"),
          ("3. Puoi condividere nel gruppo la foto di un amico senza chiedere?", ["Sì, se è divertente", "No, serve il suo permesso"], "No, serve il suo permesso"),
          ("4. Un messaggio offensivo in un gruppo può essere…", ["un reato", "sempre uno scherzo"], "un reato")],
         "8 · Emoji e messaggi: che cosa è giusto?", "8 · Gli emoji", "e8"),
  libero("e9", 9, "Il momento più brutto (o più bello) in Italia", "Racconta un fatto improvviso che ti è successo. Usa i connettivi: mentre, all'improvviso, siccome, quindi, alla fine.", ["Il mio racconto"], rows=6),
  parla("e10", 10, "Che cosa fai se perdi i documenti in Italia? E nel tuo Paese, come si fa una denuncia?"),
 ]
}

SLIDE = [("b1-esame-cittadinanza/index.html", "Esame B1 per la cittadinanza", "B1", ESAME_SLIDE, "b1"),
         ("b1-mondo-digitale/index.html", "Il mondo digitale", "B1", DIG_SLIDE, "b1"),
         ("b1-la-denuncia/index.html", "La denuncia", "B1", DEN_SLIDE, "b1")]
ESERCIZI = [("b1-esame-cittadinanza", B1ESAME), ("b1-mondo-digitale", B1DIG), ("b1-la-denuncia", B1DEN)]
GIOCHI = {
 "b1-esame-cittadinanza": ("b1-cittadini", "B1", "📝 GIOCHI: ESAME B1 (B1)", [
  ["L'ISCRIZIONE", "✍️", "SI FA ONLINE PRIMA DELL'ESAME"], ["IL CONSENSO", "✅", "AUTORIZZI A USARE I TUOI DATI"], ["LA PRIVACY", "🔒", "LA PROTEZIONE DEI DATI"],
  ["LA SESSIONE", "🗓️", "LE DATE DI UN ESAME"], ["L'ASCOLTO", "🎧", "PROVA CON TESTI DA SENTIRE"], ["LA LETTURA", "📖", "PROVA CON TESTI DA LEGGERE"],
  ["LA SCRITTURA", "✏️", "PROVA: SCRIVI UNA EMAIL"], ["L'ORALE", "🗣️", "PROVA: PARLI CON L'ESAMINATORE"], ["IL PUNTEGGIO", "💯", "I PUNTI DI OGNI PROVA"],
  ["LA SIMULAZIONE", "🧪", "UNA PROVA D'ESAME PER ALLENARSI"], ["LA CERTIFICAZIONE", "🏅", "DIMOSTRA IL TUO LIVELLO"], ["PAGOPA", "🧾", "SISTEMA PER PAGARE GLI ENTI PUBBLICI"],
  ["IL BONIFICO", "🏦", "SERVE L'IBAN"], ["LA RICEVUTA", "🧾", "PROVA DI PAGAMENTO"], ["LA TRUFFA", "🎣", "INGANNO PER RUBARE SOLDI"],
  ["VORREI", "🙏", "CONDIZIONALE DI VOLERE"], ["POTREBBE", "☎️", "… RIPETERE, PER FAVORE?"], ["FARÒ", "🗓️", "FUTURO DI FARE"]]),
 "b1-mondo-digitale": ("b1-cittadini", "B1", "💻 GIOCHI: IL MONDO DIGITALE (B1)", [
  ["L'HOME BANKING", "🏦", "LA BANCA SUL TELEFONO"], ["IL CODICE", "🔢", "ARRIVA PER SMS"], ["LA PASSWORD", "🔑", "PAROLA SEGRETA"], ["L'OPERATORE", "🎧", "RISPONDE AL SERVIZIO CLIENTI"],
  ["LA PIATTAFORMA", "💻", "SITO PER LEZIONI ONLINE"], ["IL FORUM", "💬", "DOMANDE E RISPOSTE ONLINE"], ["IL LINK", "🔗", "LO CLICCHI"], ["L'APP", "📱", "PROGRAMMA DEL TELEFONO"],
  ["LA VIDEOCHIAMATA", "🎥", "PARLI E TI VEDI"], ["LA SEGNALAZIONE", "📣", "COMUNICHI UN PROBLEMA"], ["L'ACCOUNT", "👤", "IL TUO PROFILO"], ["SCARICARE", "⬇️", "… UN'APP"],
  ["ACCEDERE", "🚪", "ENTRARE CON LE CREDENZIALI"], ["LO SCHERMO", "🖥️", "DOVE VEDI LE IMMAGINI"], ["IL TABLET", "📲", "GRANDE COME UN QUADERNO"], ["LE FAKE NEWS", "🧠", "NOTIZIE FALSE"],
  ["IL WIFI", "📶", "INTERNET SENZA FILI"], ["LA RETE", "🌐", "INTERNET"]]),
 "b1-la-denuncia": ("b1-cittadini", "B1", "🚓 GIOCHI: LA DENUNCIA (B1)", [
  ["LA DENUNCIA", "📝", "SI FA ALLA POLIZIA"], ["LO SCIPPO", "👜", "TI STRAPPANO LA BORSA"], ["IL FURTO", "🏠", "RUBANO QUALCOSA"], ["LO SMARRIMENTO", "🔎", "HAI PERSO QUALCOSA"],
  ["IL TRUFFATORE", "🕵️", "TI INGANNA PER I SOLDI"], ["IL LADRO", "🦹", "CHI RUBA"], ["IL VERBALE", "📄", "LO SCRIVE L'AGENTE"], ["IL COMMISSARIATO", "🚓", "UFFICIO DELLA POLIZIA"],
  ["LA CASERMA", "🏢", "UFFICIO DEI CARABINIERI"], ["IL TESTIMONE", "👀", "HA VISTO IL FATTO"], ["IL DUPLICATO", "🪪", "UNA NUOVA COPIA DEL DOCUMENTO"], ["IL PORTAFOGLIO", "👛", "QUI TENGO I SOLDI"],
  ["IL BANCOMAT", "💳", "SI BLOCCA SUBITO SE LO PERDI"], ["IL MOTORINO", "🛵", "PICCOLA MOTO"], ["SICCOME", "🔗", "CONNETTIVO DI CAUSA"], ["QUINDI", "➡️", "CONNETTIVO DI CONSEGUENZA"],
  ["L'EMOJI", "😊", "FACCINA NEI MESSAGGI"], ["LA CHAT", "💬", "CONVERSAZIONE SCRITTA"]]),
}

if __name__ == "__main__":
    for path, unit, top, sl, liv in SLIDE:
        os.makedirs(os.path.dirname(path), exist_ok=True)
        build_slide(path, unit, top, sl, liv)
    for cartella, dati in ESERCIZI:
        build_es(cartella + "/esercizi.html", dati)
    build_giochi(GIOCHI)
