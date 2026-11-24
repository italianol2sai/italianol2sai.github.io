"""Percorso A2, modulo 3 («Il futuro») sulla traccia di «Nuovo Senza frontiere 2» (Edilingua): unità 9-12.
Testi, dialoghi, nomi e ascolti NUOVI (Erila, 2026-11-23: «rifaccio tutto con testi nuovi»). Stile "a2".
Uso: python3 _strumenti/unita_sf_a2c.py   (dalla cartella principale del sito)"""
import os, sys
sys.path.insert(0, os.path.dirname(__file__))
from genera import eq, build as build_es
from unita_primi import cover, slide, cards, table, nota, dialogo, end
from unita_drive import vf, scegli, menu, ordina, parla, libero
from teoria import tab, es
from unita_sf import scrivi, ascolto, testo, build_slide, build_giochi

# =====================================================================
# A2 · UNITÀ 9 · I DESIDERI
# =====================================================================
DES = [("F", "Senti Bilal, tu che cosa faresti con un mese di ferie?"),
       ("M", "Io tornerei in Pakistan a trovare mia madre. E poi mi piacerebbe portare qui mia moglie e i bambini."),
       ("F", "Con il ricongiungimento familiare?"),
       ("M", "Sì. Ho già un contratto e una casa abbastanza grande. Però dovrei chiedere informazioni allo sportello."),
       ("F", "Ti accompagnerei io, ma giovedì lavoro. Potresti chiedere a Michele del SAI: lui conosce bene le procedure."),
       ("M", "Hai ragione, gli scriverei stasera. E tu, Silvia? Che cosa desideri?"),
       ("F", "Io preferirei un lavoro vicino a casa. Passerei più tempo con mio figlio.")]
DES_SLIDE = [
    cover("🌠", "I desideri", "Mi piacerebbe… preferirei… · Le richieste gentili e i consigli", "A2 &bull; Modulo 3 &bull; Unità 1"),
    slide("In questa unità impari a…", cards([
        ("💭", "Esprimere un desiderio", "Mi piacerebbe… Vorrei…"), ("🙏", "Chiedere in modo gentile", "Potrebbe…? Mi darebbe…?"),
        ("💡", "Dare un consiglio", "Dovresti… Al posto tuo…"), ("🎄", "Conoscere le feste italiane", "Natale, Pasqua, 2 giugno")])),
    slide("👨‍👩‍👧 Il ricongiungimento familiare", cards([
        ("💍", "il coniuge", "il marito o la moglie"), ("🧑", "maggiorenne", "ha 18 anni o più"), ("🧒", "minorenne", "ha meno di 18 anni"),
        ("🏠", "l'alloggio idoneo", "una casa abbastanza grande per la famiglia"), ("💶", "il reddito", "i soldi che guadagni in un anno"),
        ("🏛️", "lo Sportello Unico per l'Immigrazione", "in Prefettura: qui si presenta la domanda (online)")], "g3")),
    slide("💭 Lezione A · Mi piacerebbe…", dialogo([("*Silvia" if v == "F" else "Bilal", t) for v, t in DES])),
    slide("📘 Il condizionale presente (verbi regolari)", table([
        ["io", "torn<b>erei</b>", "prend<b>erei</b>", "prefer<b>irei</b>"], ["tu", "torn<b>eresti</b>", "prend<b>eresti</b>", "prefer<b>iresti</b>"],
        ["lui / lei", "torn<b>erebbe</b>", "prend<b>erebbe</b>", "prefer<b>irebbe</b>"], ["noi", "torn<b>eremmo</b>", "prend<b>eremmo</b>", "prefer<b>iremmo</b>"],
        ["voi", "torn<b>ereste</b>", "prend<b>ereste</b>", "prefer<b>ireste</b>"], ["loro", "torn<b>erebbero</b>", "prend<b>erebbero</b>", "prefer<b>irebbero</b>"]],
        head=["", "tornare", "prendere", "preferire"]) + "\n" + nota("Il condizionale serve per <b>desideri</b>, <b>dubbi</b> e <b>opinioni</b>: Tornerei a casa. · Sarebbe bello.")),
    slide("🙏 Lezione B · Le richieste gentili e i consigli", table([
        ["Mi dà il modulo?", "Mi <b>darebbe</b> il modulo, per favore?"], ["Può aspettare?", "<b>Potrebbe</b> aspettare un momento?"],
        ["Voglio un appuntamento.", "<b>Vorrei</b> un appuntamento."], ["Devi chiedere.", "<b>Dovresti</b> chiedere allo sportello."]],
        head=["diretto", "gentile (condizionale)"])),
    slide("📘 Il condizionale presente (verbi irregolari)", table([
        ["essere", "sarei"], ["avere", "avrei"], ["andare", "andrei"], ["fare", "farei"], ["dare", "darei"], ["stare", "starei"],
        ["potere", "potrei"], ["dovere", "dovrei"], ["volere", "vorrei"], ["venire", "verrei"], ["bere", "berrei"], ["vivere", "vivrei"]],
        head=["verbo", "io"])),
    slide("🎄 Educazione civica · Le feste in Italia", table([
        ["1 gennaio", "Capodanno"], ["6 gennaio", "Epifania (la Befana)"], ["marzo o aprile", "Pasqua e Lunedì dell'Angelo (Pasquetta)"],
        ["25 aprile", "Festa della Liberazione"], ["1 maggio", "Festa dei lavoratori"], ["2 giugno", "Festa della Repubblica"],
        ["15 agosto", "Ferragosto"], ["1 novembre", "Ognissanti"], ["8 dicembre", "Immacolata"], ["25 e 26 dicembre", "Natale e Santo Stefano"]],
        head=["quando", "festa"]) + "\n" + nota("A Bari il santo patrono è <b>San Nicola</b>: 6 dicembre e grande festa a maggio (7-9).")),
    end("Ora sai esprimere desideri e chiedere in modo gentile!"),
]
A2DES = {
 "title": "🌠 I desideri · Esercizi", "store": "a2-i-desideri", "livello": "a2",
 "sections": [
  {"part": "Le parole"},
  menu(["il coniuge", "maggiorenne", "minorenne", "il reddito", "l'alloggio idoneo"],
       [("1. Il marito o la moglie.", "il coniuge"), ("2. Una persona di 20 anni è …", "maggiorenne"), ("3. Un bambino di 10 anni è …", "minorenne"),
        ("4. I soldi che guadagni in un anno.", "il reddito"), ("5. Una casa abbastanza grande per la famiglia.", "l'alloggio idoneo")],
       "1 · Le parole del ricongiungimento", "1 · Le parole", "e1"),
  {"part": "Lezione A · Mi piacerebbe…"},
  ascolto(vf(["1. Bilal tornerebbe in Pakistan a trovare la madre.", "2. Bilal vorrebbe portare in Italia la sua famiglia.", "3. Bilal non ha un contratto.",
              "4. Silvia può accompagnarlo giovedì.", "5. Michele conosce bene le procedure.", "6. Silvia preferirebbe un lavoro vicino a casa."],
             ["VERO", "VERO", "FALSO", "FALSO", "VERO", "VERO"], "2 · 🎧 Ascolta Bilal e Silvia: vero o falso?", "2 · I desideri", "e2"), [list(x) for x in DES]),
  {"part": "Il condizionale presente (verbi regolari)", "teoria":
     tab(("-are / -ere", "-erei, -eresti, -erebbe, -eremmo, -ereste, -erebbero"), ("-ire", "-irei, -iresti, -irebbe…"), head=("verbo", "condizionale")) +
     "Per desideri, dubbi, opinioni." + es("<b>Tornerei</b> a casa. · <b>Preferirei</b> un tè.")},
  scrivi([("1. (tornare – io) … in Senegal per un mese.", ("tornerei",)), ("2. (preferire – tu) … il mare o la montagna?", ("preferiresti",)),
          ("3. (comprare – noi) … una casa più grande.", ("compreremmo",)), ("4. (prendere – Silvia) … un giorno di ferie.", ("prenderebbe",)),
          ("5. (dormire – i bambini) … tutto il giorno!", ("dormirebbero",)), ("6. (scrivere – voi) … una lettera al sindaco?", ("scrivereste",))],
         "3 · Completa con il condizionale", "3 · Condizionale regolare", "e3", w="m"),
  {"part": "Lezione B · Richieste gentili e consigli", "teoria":
     tab(("essere / avere", "sarei / avrei"), ("andare / fare / dare", "andrei / farei / darei"), ("potere / dovere / volere", "potrei / dovrei / vorrei"),
         ("venire / bere / vivere", "verrei / berrei / vivrei"), head=("verbo", "io")) + es("<b>Potrebbe</b> ripetere? · <b>Dovresti</b> riposare.")},
  scrivi([("1. (potere – Lei) … aprire la finestra, per favore?", ("potrebbe",)), ("2. (volere – io) … due biglietti per Lecce.", ("vorrei",)),
          ("3. (dovere – tu) Sei stanco: … dormire di più.", ("dovresti",)), ("4. (essere – lui) Mi … utile un dizionario.", ("sarebbe",)),
          ("5. (andare – noi) … volentieri alla festa di San Nicola.", ("andremmo",)), ("6. (venire – voi) … con noi al mercato?", ("verreste",))],
         "4 · Completa con il condizionale irregolare", "4 · Condizionale irregolare", "e4", w="m"),
  menu(["richiesta gentile", "consiglio", "desiderio"],
       [("1. Mi passeresti il sale?", "richiesta gentile"), ("2. Al posto tuo, andrei dal medico.", "consiglio"), ("3. Mi piacerebbe imparare a guidare.", "desiderio"),
        ("4. Potrebbe chiudere la porta?", "richiesta gentile"), ("5. Dovresti chiamare tua madre.", "consiglio"), ("6. Vorrei vivere vicino al mare.", "desiderio")],
       "5 · Che cos'è?", "5 · Richieste e consigli", "e5"),
  {"part": "Educazione civica · Le feste"},
  menu(["Capodanno", "Epifania", "Festa della Liberazione", "Festa dei lavoratori", "Festa della Repubblica", "Ferragosto", "Natale"],
       [("1. 2 giugno", "Festa della Repubblica"), ("2. 25 dicembre", "Natale"), ("3. 1 maggio", "Festa dei lavoratori"), ("4. 15 agosto", "Ferragosto"),
        ("5. 1 gennaio", "Capodanno"), ("6. 25 aprile", "Festa della Liberazione"), ("7. 6 gennaio", "Epifania")],
       "6 · Che festa è?", "6 · Le feste", "e6"),
  libero("e7", 7, "Per parlare: Natale e Capodanno nel mondo", "Come si festeggia il nuovo anno nel tuo Paese? Quando? Che cosa si mangia? Scrivi 5 frasi.", ["Nel mio Paese"], rows=5),
  parla("e8", 8, "Con un mese libero, che cosa faresti? Che cosa desideri per il futuro?"),
 ]
}

# =====================================================================
# A2 · UNITÀ 10 · I PROGETTI
# =====================================================================
PROG = [("M", "Ciao a tutti! Sono Giovanni dell'associazione «Mani aperte»."),
        ("M", "Il mese prossimo apriremo un laboratorio di cucina nel quartiere Libertà. Si chiamerà «Cucina senza frontiere»."),
        ("M", "Ogni sabato una persona cucinerà un piatto del suo Paese e insegnerà la ricetta agli altri."),
        ("M", "Alla fine faremo una grande festa con tutti i piatti. Inviteremo anche le famiglie del quartiere."),
        ("M", "Se volete partecipare, scriveteci entro il quindici. Sarà divertente, ve lo prometto!")]
PROG_SLIDE = [
    cover("🗓️", "I progetti", "Progetti e annunci · Le ipotesi · Il volontariato", "A2 &bull; Modulo 3 &bull; Unità 2"),
    slide("In questa unità impari a…", cards([
        ("🗓️", "Fare progetti", "L'anno prossimo farò un corso"), ("🤞", "Fare promesse e previsioni", "Ti chiamerò · Domani pioverà"),
        ("📢", "Capire un annuncio", "date, luoghi, iscrizioni"), ("🤔", "Fare ipotesi", "Sarà a casa? Avrà trent'anni")])),
    slide("⏳ Le espressioni di tempo", table([
        ["passato", "ieri, la settimana scorsa, l'anno scorso, due mesi fa"], ["presente", "oggi, adesso, quest'anno"],
        ["futuro", "domani, dopodomani, la settimana prossima, fra un anno, tra poco"]], head=["", "espressioni"])),
    slide("📢 Lezione A · L'annuncio di Giovanni", testo(*[t for _, t in PROG])),
    slide("📘 Il futuro semplice (verbi regolari)", table([
        ["io", "apr<b>irò</b>", "cucin<b>erò</b>", "prend<b>erò</b>"], ["tu", "apr<b>irai</b>", "cucin<b>erai</b>", "prend<b>erai</b>"],
        ["lui / lei", "apr<b>irà</b>", "cucin<b>erà</b>", "prend<b>erà</b>"], ["noi", "apr<b>iremo</b>", "cucin<b>eremo</b>", "prend<b>eremo</b>"],
        ["voi", "apr<b>irete</b>", "cucin<b>erete</b>", "prend<b>erete</b>"], ["loro", "apr<b>iranno</b>", "cucin<b>eranno</b>", "prend<b>eranno</b>"]],
        head=["", "aprire", "cucinare", "prendere"]) + "\n" + nota("Verbi in <b>-care / -gare</b>: cerco → cerc<b>h</b>erò, pago → pag<b>h</b>erò. Verbi in <b>-ciare / -giare</b>: comincerò, mangerò.")),
    slide("🤔 Lezione B · Le ipotesi", dialogo([
        ("Eneida", "Chi è quel signore con il grembiule?"), ("*Cristian", "Non lo so… sarà il cuoco del laboratorio."),
        ("Eneida", "E quanti anni avrà?"), ("*Cristian", "Mah, avrà sessant'anni. Guarda, sta preparando le orecchiette: sarà pugliese!"),
        ("Eneida", "Che ore sono? Ho fame."), ("*Cristian", "Saranno le dodici. Tra poco mangeremo!")])),
    slide("📘 Il futuro semplice (verbi irregolari)", table([
        ["essere", "sarò"], ["avere", "avrò"], ["andare", "andrò"], ["fare", "farò"], ["stare", "starò"], ["potere", "potrò"],
        ["dovere", "dovrò"], ["vedere", "vedrò"], ["venire", "verrò"], ["volere", "vorrò"], ["bere", "berrò"], ["rimanere", "rimarrò"]],
        head=["verbo", "io"]) + "\n" + nota("Il futuro serve anche per le <b>ipotesi</b> sul presente: Sarà il cuoco = Forse è il cuoco.")),
    slide("🤝 Educazione civica · Le associazioni di volontariato", cards([
        ("🍲", "mense e banchi alimentari", "cibo per chi ne ha bisogno"), ("📚", "scuole di italiano gratuite", "corsi con volontari"),
        ("🎨", "laboratori", "cucina, teatro, musica, cucito"), ("🧓", "aiuto agli anziani", "compagnia, spesa, medicine"),
        ("🌳", "ambiente", "pulizia di parchi e spiagge"), ("🙋", "anche tu puoi", "il volontariato è gratuito e aperto a tutti")], "g3")),
    end("Ora sai parlare dei tuoi progetti!"),
]
A2PROG = {
 "title": "🗓️ I progetti · Esercizi", "store": "a2-i-progetti", "livello": "a2",
 "sections": [
  {"part": "Le espressioni di tempo"},
  menu(["passato", "presente", "futuro"],
       [("1. fra un anno", "futuro"), ("2. l'anno scorso", "passato"), ("3. adesso", "presente"), ("4. dopodomani", "futuro"),
        ("5. due mesi fa", "passato"), ("6. tra poco", "futuro"), ("7. quest'anno", "presente")],
       "1 · Passato, presente o futuro?", "1 · Il tempo", "e1"),
  {"part": "Lezione A · L'annuncio"},
  ascolto(scegli([("1. Giovanni lavora in…", ["un ristorante", "un'associazione", "una scuola"], "un'associazione"),
                  ("2. Il laboratorio aprirà…", ["domani", "il mese prossimo", "l'anno prossimo"], "il mese prossimo"),
                  ("3. Il laboratorio sarà…", ["ogni sabato", "ogni domenica", "ogni giorno"], "ogni sabato"),
                  ("4. Alla fine ci sarà…", ["un esame", "una festa", "una gita"], "una festa"),
                  ("5. Per partecipare bisogna scrivere…", ["entro il quindici", "entro il cinque", "a dicembre"], "entro il quindici")],
                 "2 · 🎧 Ascolta l'annuncio", "2 · L'annuncio", "e2"), [list(x) for x in PROG]),
  {"part": "Il futuro semplice (verbi regolari)", "teoria":
     tab(("-are / -ere", "-erò, -erai, -erà, -eremo, -erete, -eranno"), ("-ire", "-irò, -irai, -irà…"), head=("verbo", "futuro")) +
     "Per progetti, promesse e previsioni." + es("Domani <b>cucinerò</b> il cuscus. · Ti <b>chiamerò</b> stasera.")},
  scrivi([("1. (cucinare – io) Sabato … il riso jollof.", ("cucinerò",)), ("2. (aprire – l'associazione) … un nuovo laboratorio.", ("aprirà",)),
          ("3. (invitare – noi) … tutto il quartiere.", ("inviteremo",)), ("4. (cercare – tu) … un lavoro a Milano?", ("cercherai",)),
          ("5. (pagare – voi) … voi la cena?", ("pagherete",)), ("6. (partire – loro) … fra una settimana.", ("partiranno",))],
         "3 · Completa con il futuro", "3 · Futuro regolare", "e3", w="m"),
  {"part": "Lezione B · Le ipotesi", "teoria":
     tab(("essere / avere", "sarò / avrò"), ("andare / fare / stare", "andrò / farò / starò"), ("venire / volere / bere", "verrò / vorrò / berrò"), head=("verbo", "io")) +
     "Il futuro serve anche per fare <b>ipotesi</b> sul presente." + es("Che ore sono? <b>Saranno</b> le dodici. (= forse sono le dodici)")},
  scrivi([("1. (essere) Chi è quel signore? … il cuoco.", ("sara",)), ("2. (avere) Quanti anni ha? … sessant'anni.", ("avra",)),
          ("3. (venire – io) Domani … anch'io al laboratorio.", ("verro",)), ("4. (fare – noi) … una grande festa.", ("faremo",)),
          ("5. (andare – tu) … alla festa sabato?", ("andrai",)), ("6. (essere – loro) Dove sono i bambini? … al parco.", ("saranno",))],
         "4 · Completa con il futuro irregolare", "4 · Futuro irregolare", "e4", w="m"),
  menu(["progetto", "promessa", "previsione", "ipotesi"],
       [("1. L'anno prossimo farò un corso di cucina.", "progetto"), ("2. Ti aiuterò con i compiti, te lo giuro!", "promessa"),
        ("3. Domani pioverà su tutta la Puglia.", "previsione"), ("4. Non risponde al telefono: sarà al lavoro.", "ipotesi"),
        ("5. Ti restituirò i soldi lunedì, prometto.", "promessa"), ("6. Fra un anno apriremo un negozio.", "progetto")],
       "5 · Che cos'è?", "5 · Usi del futuro", "e5"),
  {"part": "Educazione civica · Il volontariato"},
  vf(["1. Il volontariato è un lavoro pagato.", "2. Ci sono scuole di italiano con volontari.", "3. Alcune associazioni puliscono parchi e spiagge.",
      "4. Solo gli italiani possono fare volontariato."], ["FALSO", "VERO", "VERO", "FALSO"], "6 · Il volontariato: vero o falso?", "6 · Il volontariato", "e6"),
  libero("e7", 7, "Per scrivere: Cucina senza frontiere", "Scrivi la ricetta di un piatto del tuo Paese per il laboratorio: ingredienti e 5 passaggi. Usa il futuro (prima taglierò… poi metterò…).", ["La mia ricetta"], rows=7),
  parla("e8", 8, "Quali sono i tuoi progetti per il prossimo anno? Ti piacerebbe fare volontariato? Dove?"),
 ]
}

# =====================================================================
# A2 · UNITÀ 11 · LA TECNOLOGIA
# =====================================================================
INFO = [("F", "Buongiorno a tutti! Oggi impariamo a salvare un file sulla chiavetta USB."),
        ("F", "Prima accendete il computer e inserite username e password del vostro account."),
        ("F", "Bene. Michele, stai per chiudere il programma? Aspetta! Prima devi salvare."),
        ("F", "Adesso inserite la chiavetta nella porta USB. Cliccate su «Salva con nome» e scegliete la chiavetta."),
        ("F", "Avete finito di salvare? Perfetto. Continuiamo a lavorare: adesso impariamo a mandare il file per email.")]
TEC_SLIDE = [
    cover("💻", "La tecnologia", "Una lezione di informatica · Internet · Le regole online", "A2 &bull; Modulo 3 &bull; Unità 3"),
    slide("In questa unità impari a…", cards([
        ("🖥️", "Usare le parole del computer", "account, password, chiavetta"), ("▶️", "Dire a che punto è un'azione", "sto per, comincio a, finisco di"),
        ("🌐", "Capire informazioni online", "il sito della Questura, i permessi"), ("🛡️", "Comportarti bene online", "le regole della rete")])),
    slide("🖥️ Le parole dell'informatica", cards([
        ("👤", "l'account", "il tuo profilo su un sito"), ("🔤", "lo username", "il nome per entrare"), ("🔑", "la password", "la parola segreta"),
        ("💾", "la chiavetta USB", "per portare i file"), ("📁", "il file", "un documento, una foto"), ("🖱️", "cliccare", "premere con il mouse")], "g3")),
    slide("🧑‍🏫 Lezione A · Una lezione di informatica", testo(*[t for _, t in INFO])),
    slide("📘 I verbi fraseologici", table([
        ["stare per + infinito", "subito prima", "Sto per uscire."], ["cominciare / iniziare a + infinito", "l'inizio", "Comincio a studiare."],
        ["continuare a + infinito", "durante", "Continuiamo a lavorare."], ["finire / smettere di + infinito", "la fine", "Ho finito di salvare. Smetto di fumare."]],
        head=["verbo", "quando", "esempio"])),
    slide("🌐 Lezione B · Internet: i tipi di permesso", testo(
        "Sul sito della Polizia di Stato trovi informazioni sui permessi di soggiorno per lavoro.",
        "<b>Lavoro subordinato</b>: lavori per un datore di lavoro con un contratto. <b>Lavoro autonomo</b>: lavori in proprio, per esempio con una partita IVA. "
        "<b>Lavoro stagionale</b>: lavori solo in alcuni mesi dell'anno, per esempio nei campi o negli alberghi d'estate.")),
    slide("📘 I suffissi", table([
        ["-ezza", "aggettivo → nome", "bello → bell<b>ezza</b>, sicuro → sicur<b>ezza</b>, gentile → gentil<b>ezza</b>"],
        ["-ario", "nome → nome", "macchina → macchin<b>ario</b>, vocabolo → vocabol<b>ario</b>"],
        ["-evole", "verbo → aggettivo", "piacere → piac<b>evole</b>, ragionare → ragion<b>evole</b>"]], head=["suffisso", "da… a…", "esempi"])),
    slide("🛡️ Educazione civica · Le regole su internet", cards([
        ("🔑", "password sicure", "lunghe, diverse per ogni sito, mai condivise"), ("🤐", "dati personali", "non scrivere indirizzo e documenti in pubblico"),
        ("📷", "foto degli altri", "chiedi sempre il permesso prima di pubblicarle"), ("🗣️", "rispetto", "niente insulti: anche online sono reati"),
        ("🎣", "truffe", "non cliccare su link strani, la banca non chiede il PIN"), ("🔎", "notizie", "controlla la fonte prima di condividere")], "g3")),
    end("Ora sai usare meglio il computer e internet!"),
]
A2TEC = {
 "title": "💻 La tecnologia · Esercizi", "store": "a2-la-tecnologia", "livello": "a2",
 "sections": [
  {"part": "Le parole dell'informatica"},
  menu(["l'account", "lo username", "la password", "la chiavetta USB", "il file", "cliccare"],
       [("1. La parola segreta per entrare.", "la password"), ("2. Il nome che usi per entrare in un sito.", "lo username"),
        ("3. Il tuo profilo su un sito.", "l'account"), ("4. Ci salvi i documenti per portarli via.", "la chiavetta USB"),
        ("5. Premere con il mouse.", "cliccare"), ("6. Un documento o una foto sul computer.", "il file")],
       "1 · Che cos'è?", "1 · Le parole", "e1"),
  {"part": "Lezione A · La lezione di informatica"},
  ascolto(ordina(["Accendere il computer.", "Inserire username e password.", "Inserire la chiavetta nella porta USB.",
                  "Cliccare su «Salva con nome».", "Scegliere la chiavetta.", "Mandare il file per email."],
                 "2 · 🎧 Ascolta l'insegnante e metti in ordine", "2 · La lezione", "e2"), [list(x) for x in INFO]),
  {"part": "I verbi fraseologici", "teoria":
     tab(("stare per", "subito prima"), ("cominciare a / iniziare a", "l'inizio"), ("continuare a", "durante"), ("finire di / smettere di", "la fine"), head=("verbo", "momento")) +
     es("<b>Sto per</b> uscire. · <b>Ho finito di</b> salvare.")},
  menu(["a", "di", "per"],
       [("1. Comincio … studiare informatica.", "a"), ("2. Ho finito … scrivere l'email.", "di"), ("3. Sto … spegnere il computer.", "per"),
        ("4. Continuate … lavorare!", "a"), ("5. Ho smesso … usare i social.", "di"), ("6. Iniziamo … leggere il testo.", "a")],
       "3 · a, di o per?", "3 · Le preposizioni", "e3"),
  scegli([("1. Il treno parte tra un minuto: …", ["sta per partire", "ha finito di partire"], "sta per partire"),
          ("2. Ho cominciato il corso a ottobre e lo faccio ancora: …", ["continuo a studiare", "ho smesso di studiare"], "continuo a studiare"),
          ("3. Prima fumavo, adesso no: …", ["ho smesso di fumare", "comincio a fumare"], "ho smesso di fumare"),
          ("4. L'email è scritta e spedita: …", ["sto per scriverla", "ho finito di scriverla"], "ho finito di scriverla")],
         "4 · Scegli la frase giusta", "4 · A che punto?", "e4"),
  {"part": "Lezione B · Internet e i permessi"},
  menu(["lavoro subordinato", "lavoro autonomo", "lavoro stagionale"],
       [("1. Amadou lavora nei campi da giugno a settembre.", "lavoro stagionale"), ("2. Olena ha un contratto in una pizzeria.", "lavoro subordinato"),
        ("3. Karim ha un negozio suo con la partita IVA.", "lavoro autonomo"), ("4. Grace lavora d'estate in un albergo al mare.", "lavoro stagionale"),
        ("5. Ali fa l'operaio in una fabbrica con contratto.", "lavoro subordinato")],
       "5 · Che tipo di lavoro è?", "5 · I permessi", "e5"),
  {"part": "I suffissi", "teoria":
     tab(("-ezza", "bello → bellezza"), ("-ario", "macchina → macchinario"), ("-evole", "piacere → piacevole"), head=("suffisso", "esempio")) +
     "I suffissi creano parole nuove."},
  scrivi([("1. (sicuro) La … online è importante.", ("sicurezza",)), ("2. (gentile) Grazie per la tua …", ("gentilezza",)),
          ("3. (piacere) È stata una serata …", ("piacevole",)), ("4. (vocabolo) Cerco la parola nel …", ("vocabolario",)),
          ("5. (bello) Che … questo paesaggio!", ("bellezza",))],
         "6 · Scrivi la parola con il suffisso", "6 · I suffissi", "e6", w="m"),
  {"part": "Educazione civica · Le regole su internet"},
  vf(["1. È meglio usare la stessa password per tutti i siti.", "2. Prima di pubblicare la foto di un amico, chiedo il permesso.",
      "3. Un insulto online può essere un reato.", "4. La banca può chiedermi il PIN via SMS.", "5. Controllo la fonte prima di condividere una notizia."],
     ["FALSO", "VERO", "VERO", "FALSO", "VERO"], "7 · Le regole online: vero o falso?", "7 · Online", "e7"),
  libero("e8", 8, "Per parlare: la comunicazione online", "Come comunichi con la tua famiglia lontana? Quali app usi? Quante volte alla settimana?", ["Io e la tecnologia"], rows=4),
  parla("e9", 9, "Che cosa sai fare con il computer? Che cosa vorresti imparare?"),
 ]
}

# =====================================================================
# A2 · UNITÀ 12 · L'AMBIENTE
# =====================================================================
DIFF = [("F", "Scusi, signora Rosa, dove metto queste bottiglie di vetro?"),
        ("F", "Nel bidone verde, cara. La plastica e le lattine vanno nel giallo, la carta nel blu."),
        ("F", "E gli avanzi di cibo?"),
        ("F", "Nell'organico, il bidone marrone. Si porta giù il lunedì, il mercoledì e il sabato."),
        ("F", "E questo vecchio phon rotto?"),
        ("F", "No, quello non va nei bidoni! Se lo porti al centro di raccolta, lo smaltiscono bene. Il bidone del secco è già strapieno!")]
AMB_SLIDE = [
    cover("🌍", "L'ambiente", "La raccolta differenziata · La difesa dell'ambiente", "A2 &bull; Modulo 3 &bull; Unità 4"),
    slide("In questa unità impari a…", cards([
        ("♻️", "Fare la raccolta differenziata", "vetro, carta, plastica, organico"), ("🌱", "Parlare dell'ambiente", "inquinamento, risparmio, stagione"),
        ("🔀", "Fare ipotesi", "Se ricicli, aiuti il pianeta"), ("🍎", "Scegliere frutta e verdura di stagione", "")])),
    slide("♻️ I bidoni", cards([
        ("🟢", "vetro", "bottiglie, barattoli"), ("🟡", "plastica e metalli", "bottiglie di plastica, lattine, vasetti"),
        ("🔵", "carta e cartone", "giornali, scatole"), ("🟤", "organico", "avanzi di cibo, bucce, fondi di caffè"),
        ("⚫", "secco / indifferenziato", "quello che non si ricicla"), ("🏭", "centro di raccolta", "elettrodomestici, mobili, pile")], "g3")),
    slide("🗑️ Lezione A · La raccolta differenziata", dialogo([("*Signora Rosa" if i % 2 else "Mariam", t) for i, (_, t) in enumerate(DIFF)])),
    slide("📘 I prefissi", table([
        ["iper-", "molto grande, troppo", "<b>iper</b>mercato, <b>iper</b>attivo"], ["stra-", "moltissimo", "<b>stra</b>pieno, <b>stra</b>contento"],
        ["super-", "sopra, più del normale", "<b>super</b>mercato, <b>super</b>veloce"], ["ri-", "di nuovo", "<b>ri</b>ciclare, <b>ri</b>usare"],
        ["in- / im-", "il contrario", "<b>in</b>differenziato, <b>im</b>possibile"]], head=["prefisso", "significato", "esempi"])),
    slide("🌱 Lezione B · La difesa dell'ambiente", testo(
        "Se compri frutta e verdura di stagione, risparmi e inquini meno: non viaggiano per migliaia di chilometri.",
        "Se lavi i vestiti a 30 gradi, consumi meno energia. Se usi la borraccia, non compri bottiglie di plastica.",
        "Se andiamo a piedi o in bici, l'aria della città sarà più pulita.")),
    slide("📘 Il periodo ipotetico (1° tipo)", table([
        ["se + presente", "presente", "Se <b>ricicli</b>, <b>aiuti</b> l'ambiente."], ["se + presente", "futuro", "Se <b>piove</b>, <b>resteremo</b> a casa."],
        ["se + presente", "imperativo", "Se <b>hai</b> sete, <b>usa</b> la borraccia!"]], head=["ipotesi", "conseguenza", "esempio"]) + "\n" +
        nota("È un'ipotesi <b>reale</b>, possibile: una cosa che succede davvero o può succedere.")),
    slide("🧤 Educazione civica · Puliamo il mondo", cards([
        ("📅", "quando", "ogni anno a settembre, in tante città italiane"), ("🧹", "che cosa si fa", "volontari puliscono parchi, spiagge, strade"),
        ("🤝", "chi partecipa", "scuole, associazioni, famiglie, tutti"), ("🌊", "a Bari", "pulizia delle spiagge e del lungomare")], "g2")),
    end("Ora sai fare la tua parte per l'ambiente!"),
]
A2AMB = {
 "title": "🌍 L'ambiente · Esercizi", "store": "a2-l-ambiente", "livello": "a2",
 "sections": [
  {"part": "I bidoni"},
  menu(["vetro", "plastica e metalli", "carta e cartone", "organico", "secco", "centro di raccolta"],
       [("1. Una bottiglia di vino vuota.", "vetro"), ("2. Le bucce di banana.", "organico"), ("3. Una scatola di cartone.", "carta e cartone"),
        ("4. Una lattina di cola.", "plastica e metalli"), ("5. Un frigorifero vecchio.", "centro di raccolta"), ("6. Un piatto rotto di ceramica.", "secco"),
        ("7. I fondi del caffè.", "organico"), ("8. Il giornale di ieri.", "carta e cartone")],
       "1 · Dove lo butti?", "1 · I bidoni", "e1"),
  {"part": "Lezione A · La raccolta differenziata"},
  ascolto(vf(["1. Il vetro va nel bidone verde.", "2. La carta va nel bidone giallo.", "3. L'organico si porta giù tre volte alla settimana.",
              "4. Il phon rotto va nel bidone del secco.", "5. Il bidone del secco è strapieno."],
             ["VERO", "FALSO", "VERO", "FALSO", "VERO"], "2 · 🎧 Ascolta Mariam e la signora Rosa", "2 · La differenziata", "e2"), [list(x) for x in DIFF]),
  {"part": "I prefissi", "teoria":
     tab(("iper-", "ipermercato"), ("stra-", "strapieno"), ("super-", "supermercato"), ("ri-", "riciclare"), ("in- / im-", "impossibile"), head=("prefisso", "esempio")) +
     "I prefissi vanno <b>prima</b> della parola e ne cambiano il significato."},
  menu(["iper", "stra", "super", "ri", "in", "im"],
       [("1. Il bidone è …pieno: non c'è più posto.", "stra"), ("2. Faccio la spesa all'…mercato fuori città.", "iper"),
        ("3. Le bottiglie si possono …ciclare.", "ri"), ("4. Il secco è il rifiuto …differenziato.", "in"),
        ("5. Pulire tutta la spiaggia in un'ora è …possibile!", "im"), ("6. Ho preso un treno …veloce.", "super")],
       "3 · Scegli il prefisso", "3 · I prefissi", "e3"),
  {"part": "Lezione B · Il periodo ipotetico", "teoria":
     tab(("se + presente", "presente / futuro / imperativo"), head=("ipotesi", "conseguenza")) +
     "Un'ipotesi reale, possibile." + es("<b>Se ricicli</b>, <b>aiuti</b> l'ambiente. · <b>Se piove</b>, <b>resteremo</b> a casa.")},
  scrivi([("1. (comprare – tu) Se … frutta di stagione, risparmi.", ("compri",)), ("2. (andare – noi) Se … in bici, inquiniamo meno.", ("andiamo",)),
          ("3. (lavare – voi) Se … a 30 gradi, consumate meno energia.", ("lavate",)), ("4. (usare – io) Se … la borraccia, non compro la plastica.", ("uso",)),
          ("5. (fare – loro) Se … la differenziata, la città sarà più pulita.", ("fanno",))],
         "4 · Completa l'ipotesi", "4 · Se…", "e4", w="m"),
  menu(["inquini meno", "risparmi acqua", "aiuti gli animali del mare", "l'aria sarà più pulita", "consumi meno energia"],
       [("1. Se chiudi il rubinetto mentre ti lavi i denti, …", "risparmi acqua"), ("2. Se spegni le luci quando esci, …", "consumi meno energia"),
        ("3. Se non lasci plastica in spiaggia, …", "aiuti gli animali del mare"), ("4. Se tutti usano l'autobus, …", "l'aria sarà più pulita"),
        ("5. Se compri prodotti locali, …", "inquini meno")],
       "5 · Collega l'ipotesi e la conseguenza", "5 · Conseguenze", "e5"),
  {"part": "Frutta e verdura di stagione"},
  menu(["inverno", "primavera", "estate", "autunno"],
       [("1. le arance", "inverno"), ("2. le fragole", "primavera"), ("3. l'anguria", "estate"), ("4. le castagne", "autunno"),
        ("5. i pomodori", "estate"), ("6. i carciofi", "primavera"), ("7. l'uva", "autunno")],
       "6 · Di che stagione è?", "6 · Le stagioni", "e6"),
  {"part": "Educazione civica · Puliamo il mondo"},
  vf(["1. «Puliamo il mondo» si fa ogni anno a settembre.", "2. Possono partecipare solo le scuole.", "3. I volontari puliscono parchi, spiagge e strade."],
     ["VERO", "FALSO", "VERO"], "7 · Puliamo il mondo: vero o falso?", "7 · Puliamo il mondo", "e7"),
  libero("e8", 8, "Per scrivere: frutta e verdura di stagione", "Scrivi un piccolo cartello per il mercato: 4 prodotti di questa stagione e perché è meglio comprarli.", ["Il cartello"], rows=5),
  parla("e9", 9, "Come si fa la raccolta dei rifiuti nel tuo Paese? Che cosa fai tu per l'ambiente?"),
 ]
}

SLIDE = [("a2-i-desideri/index.html", "I desideri", "A2", DES_SLIDE, "a2"),
         ("a2-i-progetti/index.html", "I progetti", "A2", PROG_SLIDE, "a2"),
         ("a2-la-tecnologia/index.html", "La tecnologia", "A2", TEC_SLIDE, "a2"),
         ("a2-l-ambiente/index.html", "L'ambiente", "A2", AMB_SLIDE, "a2")]
ESERCIZI = [("a2-i-desideri", A2DES), ("a2-i-progetti", A2PROG), ("a2-la-tecnologia", A2TEC), ("a2-l-ambiente", A2AMB)]
GIOCHI = {
 "a2-i-desideri": ("a2-vivere-insieme", "A2", "🌠 GIOCHI: I DESIDERI (A2)", [
  ["IL CONIUGE", "💍", "IL MARITO O LA MOGLIE"], ["MAGGIORENNE", "🧑", "HA 18 ANNI O PIÙ"], ["MINORENNE", "🧒", "HA MENO DI 18 ANNI"], ["IL REDDITO", "💶", "I SOLDI DI UN ANNO"],
  ["L'ALLOGGIO", "🏠", "LA CASA"], ["LA PREFETTURA", "🏛️", "QUI C'È LO SPORTELLO UNICO"], ["VORREI", "🙏", "CONDIZIONALE DI VOLERE"], ["POTREBBE", "☎️", "… RIPETERE, PER FAVORE?"],
  ["DOVRESTI", "💡", "PER DARE UN CONSIGLIO"], ["SAREBBE", "✨", "… BELLO!"], ["IL NATALE", "🎄", "25 DICEMBRE"], ["LA PASQUA", "🥚", "IN PRIMAVERA"],
  ["IL CAPODANNO", "🎆", "1 GENNAIO"], ["LA BEFANA", "🧹", "6 GENNAIO"], ["FERRAGOSTO", "🏖️", "15 AGOSTO"], ["SAN NICOLA", "⛪", "IL PATRONO DI BARI"],
  ["LA REPUBBLICA", "🇮🇹", "SI FESTEGGIA IL 2 GIUGNO"], ["IL DESIDERIO", "🌠", "UNA COSA CHE VORREI"]]),
 "a2-i-progetti": ("a2-vivere-insieme", "A2", "🗓️ GIOCHI: I PROGETTI (A2)", [
  ["IL PROGETTO", "🗓️", "UNA COSA CHE FARÒ"], ["LA PROMESSA", "🤞", "TE LO GIURO!"], ["L'ANNUNCIO", "📢", "INFORMAZIONE PER TUTTI"], ["L'IPOTESI", "🤔", "FORSE…"],
  ["DOMANI", "🌅", "IL GIORNO DOPO OGGI"], ["DOPODOMANI", "📆", "FRA DUE GIORNI"], ["FRA UN ANNO", "⏳", "TRA DODICI MESI"], ["L'ASSOCIAZIONE", "🤝", "UN GRUPPO DI VOLONTARI"],
  ["IL VOLONTARIATO", "🙋", "AIUTARE GRATIS"], ["IL LABORATORIO", "🎨", "SI IMPARA FACENDO"], ["LA RICETTA", "📝", "COME SI CUCINA UN PIATTO"], ["LA FESTA", "🎉", "TUTTI INSIEME CON I PIATTI"],
  ["IL QUARTIERE", "🏘️", "LA ZONA DELLA CITTÀ"], ["SARÒ", "🔮", "FUTURO DI ESSERE"], ["AVRÒ", "🎒", "FUTURO DI AVERE"], ["FARÒ", "🛠️", "FUTURO DI FARE"],
  ["ANDRÒ", "🚶", "FUTURO DI ANDARE"], ["VERRÒ", "🚪", "FUTURO DI VENIRE"]]),
 "a2-la-tecnologia": ("a2-vivere-insieme", "A2", "💻 GIOCHI: LA TECNOLOGIA (A2)", [
  ["L'ACCOUNT", "👤", "IL TUO PROFILO"], ["LO USERNAME", "🔤", "IL NOME PER ENTRARE"], ["LA PASSWORD", "🔑", "PAROLA SEGRETA"], ["LA CHIAVETTA", "💾", "PORTA I FILE"],
  ["IL FILE", "📁", "UN DOCUMENTO SUL COMPUTER"], ["IL MOUSE", "🖱️", "SERVE PER CLICCARE"], ["LA TASTIERA", "⌨️", "SERVE PER SCRIVERE"], ["LO SCHERMO", "🖥️", "QUI VEDI TUTTO"],
  ["L'EMAIL", "📧", "POSTA ELETTRONICA"], ["IL SITO", "🌐", "UNA PAGINA DI INTERNET"], ["SALVARE", "💾", "NON PERDERE IL FILE"], ["CLICCARE", "👆", "PREMERE CON IL MOUSE"],
  ["STAGIONALE", "🌾", "LAVORO SOLO IN ALCUNI MESI"], ["AUTONOMO", "🧾", "LAVORO CON PARTITA IVA"], ["SUBORDINATO", "📄", "LAVORO CON CONTRATTO"], ["LA SICUREZZA", "🛡️", "SICURO + EZZA"],
  ["PIACEVOLE", "😊", "PIACERE + EVOLE"], ["LA TRUFFA", "🎣", "INGANNO ONLINE"]]),
 "a2-l-ambiente": ("a2-vivere-insieme", "A2", "🌍 GIOCHI: L'AMBIENTE (A2)", [
  ["IL VETRO", "🟢", "BIDONE VERDE"], ["LA PLASTICA", "🟡", "BIDONE GIALLO"], ["LA CARTA", "🔵", "BIDONE BLU"], ["L'ORGANICO", "🟤", "AVANZI DI CIBO"],
  ["IL SECCO", "⚫", "NON SI RICICLA"], ["RICICLARE", "♻️", "USARE DI NUOVO I MATERIALI"], ["LA LATTINA", "🥫", "VA CON LA PLASTICA"], ["LA BORRACCIA", "🧴", "BOTTIGLIA DA RIEMPIRE"],
  ["L'INQUINAMENTO", "🏭", "ARIA E ACQUA SPORCHE"], ["IL BIDONE", "🗑️", "QUI BUTTO I RIFIUTI"], ["STRAPIENO", "📦", "PIENISSIMO"], ["L'IPERMERCATO", "🏬", "UN SUPERMERCATO ENORME"],
  ["LA STAGIONE", "🍂", "PRIMAVERA, ESTATE…"], ["LE FRAGOLE", "🍓", "FRUTTA DI PRIMAVERA"], ["L'ANGURIA", "🍉", "FRUTTA D'ESTATE"], ["LE CASTAGNE", "🌰", "FRUTTA D'AUTUNNO"],
  ["LE ARANCE", "🍊", "FRUTTA D'INVERNO"], ["LA SPIAGGIA", "🏖️", "SI PULISCE A SETTEMBRE"]]),
}

if __name__ == "__main__":
    for path, unit, top, sl, liv in SLIDE:
        os.makedirs(os.path.dirname(path), exist_ok=True)
        build_slide(path, unit, top, sl, liv)
    for cartella, dati in ESERCIZI:
        build_es(cartella + "/esercizi.html", dati)
    build_giochi(GIOCHI)
