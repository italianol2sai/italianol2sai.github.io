"""Unità B1-C2 (2026-10-30): Erila ha chiesto teoria e attività sugli argomenti di Nuovo Espresso 3-6.
I libri sono protetti: si prendono solo gli argomenti (lessico, comunicazione, grammatica) tipici di ogni livello;
testi ed esercizi sono scritti per il sito. Minuscolo normale. Pagine in avanzato/<nome>.html."""
from unita_drive import vf, scegli, menu, scrivi, ordina, completa, libero, parla
from teoria import tab, es

def pagina(icona, titolo, livello, sections):
    return {"title": "%s %s · %s" % (icona, titolo, livello), "store": "avz-" + titolo.lower().replace(" ", "-")[:20], "sections": sections}

P = {}

# ---------------------------------------------------------------- B1
P["b1-ci-ne-relativi"] = ("B1", pagina("🧭", "Ci, ne e i pronomi relativi", "B1", [
  {"part": "Ci e ne", "teoria":
     tab(("ci", "= in quel posto / a quella cosa", "Vai a Roma? Sì, ci vado domani. · Pensi all'esame? Ci penso sempre."),
         ("ne", "= di quella cosa / una quantità", "Quanti figli hai? Ne ho due. · Che ne pensi?")) +
     "Al passato con <b>ne</b> il participio si accorda con la quantità: Quante mele hai comprato? Ne ho comprate tre."},
  menu(["ci", "ne"], [("1. Sei mai stato a Matera? Sì, ___ sono stato l'anno scorso.", "ci"), ("2. Quanto pane vuoi? ___ voglio mezzo chilo.", "ne"),
                      ("3. Credi agli oroscopi? No, non ___ credo.", "ci"), ("4. Hai parlato del problema con il capo? Sì, ___ ho parlato ieri.", "ne"),
                      ("5. Quanti caffè bevi al giorno? ___ bevo tre.", "ne")], "1 · Ci o ne?", "1 · Ci e ne", "e1"),
  {"part": "Che, cui, chi", "teoria":
     tab(("che", "soggetto o oggetto", "La donna che lavora con me. Il libro che leggo."),
         ("preposizione + cui", "dopo di, a, da, in, con, per, su, tra", "La città in cui vivo. L'amico a cui scrivo."),
         ("il cui / la cui", "= di chi (possesso)", "Lo scrittore il cui libro ho letto."),
         ("chi", "= la persona che (sempre singolare)", "Chi studia, impara."))},
  scegli([("1. Il collega ___ mi ha aiutato si chiama Ivan.", ["che", "cui", "chi"], "che"), ("2. Questa è la ragione per ___ sono venuto.", ["cui", "che", "chi"], "cui"),
          ("3. ___ arriva tardi non può entrare.", ["Chi", "Che", "Cui"], "Chi"), ("4. La signora ___ figlio studia con me è ucraina.", ["il cui", "la cui", "che"], "il cui"),
          ("5. Il quartiere in ___ abito è tranquillo.", ["cui", "che", "quale"], "cui")], "2 · Scegli il relativo", "2 · I relativi", "e2"),
  libero("e3", 3, "Il posto in cui vivo", "Descrivi la città in cui vivi usando che, cui, ci e ne (5 frasi).", ["La mia città"], rows=5),
]))

# ---------------------------------------------------------------- B2
P["b2-ipotesi"] = ("B2", pagina("🔮", "Se fossi… Il periodo ipotetico", "B2", [
  {"part": "Il congiuntivo imperfetto", "teoria":
     tab(("io / tu", "parlassi", "prendessi", "partissi", "fossi", "avessi"), ("lui / lei", "parlasse", "prendesse", "partisse", "fosse", "avesse"),
         ("noi", "parlassimo", "prendessimo", "partissimo", "fossimo", "avessimo"), ("voi", "parlaste", "prendeste", "partiste", "foste", "aveste"),
         ("loro", "parlassero", "prendessero", "partissero", "fossero", "avessero"), head=("", "-are", "-ere", "-ire", "essere", "avere")) +
     "irregolari: fare → facessi, dire → dicessi, dare → dessi, stare → stessi, bere → bevessi."},
  scrivi([("1. Se io (avere) ___ più tempo, studierei il cinese.", ["avessi"]), ("2. Se tu (essere) ___ al mio posto, che cosa faresti?", ["fossi"]),
          ("3. Se noi (vincere) ___ la lotteria, compreremmo una casa.", ["vincessimo"]), ("4. Se loro (fare) ___ sport, starebbero meglio.", ["facessero"]),
          ("5. Se lei (dire) ___ la verità, tutto sarebbe più semplice.", ["dicesse"])], "1 · Scrivi il congiuntivo imperfetto", "1 · Congiuntivo imperfetto", "e1"),
  {"part": "I tre tipi di ipotesi", "teoria":
     tab(("reale", "se + presente → presente / futuro", "Se piove, resto a casa."),
         ("possibile", "se + congiuntivo imperfetto → condizionale presente", "Se avessi soldi, viaggerei."),
         ("impossibile (passato)", "se + congiuntivo trapassato → condizionale passato", "Se fossi partito prima, non avrei perso il treno.")) +
     "Mai il condizionale dopo <b>se</b>: <s>se avrei</s> → se avessi."},
  scegli([("1. Se domani fa bel tempo, ___ al mare.", ["andiamo", "andremmo", "saremmo andati"], "andiamo"),
          ("2. Se parlassi bene l'inglese, ___ un lavoro migliore.", ["troverei", "trovo", "avrei trovato"], "troverei"),
          ("3. Se avessi studiato, ___ l'esame.", ["avrei superato", "supererei", "supero"], "avrei superato"),
          ("4. Se ___ in te, accetterei l'offerta.", ["fossi", "sarei", "sono stato"], "fossi"),
          ("5. Se mi ___ prima, ti avrei aiutato.", ["avessi chiamato", "chiameresti", "chiamassi"], "avessi chiamato")], "2 · Che tipo di ipotesi?", "2 · Il periodo ipotetico", "e2"),
  libero("e3", 3, "Se potessi…", "Che cosa faresti se potessi cambiare una cosa nella tua città? E che cosa avresti fatto di diverso nella tua vita? (6 frasi)", ["Le mie ipotesi"], rows=6),
]))

P["b2-discorso-indiretto"] = ("B2", pagina("🗣️", "Ha detto che… Il discorso indiretto", "B2", [
  {"part": "Dal diretto all'indiretto", "teoria":
     "quando il verbo che introduce è al passato (ha detto, disse) i tempi cambiano:" +
     tab(("presente", "imperfetto", "«Sono stanco» → Ha detto che era stanco."), ("passato prossimo", "trapassato prossimo", "«Ho finito» → Ha detto che aveva finito."),
         ("futuro", "condizionale passato", "«Verrò» → Ha detto che sarebbe venuto."), ("imperativo", "di + infinito", "«Aspetta!» → Mi ha detto di aspettare.")) +
     "cambiano anche le parole: io → lui/lei, qui → lì, oggi → quel giorno, domani → il giorno dopo, ieri → il giorno prima."},
  scrivi([("1. «Lavoro in un ospedale.» → Ha detto che ___ in un ospedale.", ["lavorava"]), ("2. «Ho perso le chiavi.» → Ha detto che ___ le chiavi.", ["aveva perso"]),
          ("3. «Arriverò domani.» → Ha detto che ___ il giorno dopo.", ["sarebbe arrivato", "sarebbe arrivata"]), ("4. «Chiudi la porta!» → Mi ha detto ___ la porta.", ["di chiudere"]),
          ("5. «Sono qui.» → Ha detto che era ___.", ["li", "lì"])], "1 · Trasforma", "1 · Indiretto", "e1", w="m"),
  {"part": "Le domande indirette", "teoria":
     "domanda sì/no → <b>se</b>; domanda con chi, dove, quando… → la stessa parola." + es("«Vieni?» → Mi ha chiesto se venivo. «Dove abiti?» → Mi ha chiesto dove abitavo.")},
  scegli([("1. «Hai fame?» → Mi ha chiesto ___ avevo fame.", ["se", "che", "di"], "se"), ("2. «Quando parti?» → Mi ha chiesto ___ partivo.", ["quando", "se", "che"], "quando"),
          ("3. «Puoi aiutarmi?» → Mi ha chiesto se ___ aiutarlo.", ["potevo", "posso", "potrò"], "potevo")], "2 · La domanda indiretta", "2 · Domande", "e2"),
  libero("e3", 3, "Che cosa ti hanno detto?", "Racconta una conversazione importante (al lavoro, in un ufficio, in famiglia) con il discorso indiretto.", ["La conversazione"], rows=5),
]))

P["b2-passivo-ambiente"] = ("B2", pagina("🌍", "L'ambiente e la forma passiva", "B2", [
  {"part": "Le parole dell'ambiente", "teoria":
     "parole utili: <b>l'inquinamento</b>, <b>le emissioni</b>, <b>le energie rinnovabili</b> (solare, eolica), <b>lo spreco</b>, <b>il riciclo</b>, <b>la sostenibilità</b>, <b>il cambiamento climatico</b>."},
  menu(["l'inquinamento", "lo spreco", "il riciclo", "le rinnovabili", "la siccità"],
       [("1. Buttare cibo ancora buono è ___.", "lo spreco"), ("2. Il sole e il vento producono energia: sono ___.", "le rinnovabili"),
        ("3. Lo smog delle auto causa ___ dell'aria.", "l'inquinamento"), ("4. Non piove da mesi: c'è ___.", "la siccità"),
        ("5. Con ___ la plastica diventa un oggetto nuovo.", "il riciclo")], "1 · Che cos'è?", "1 · Il lessico", "e1"),
  {"part": "La forma passiva", "teoria":
     tab(("essere + participio", "Il parco è pulito dai volontari.", "tutti i tempi"), ("venire + participio", "Il parco viene pulito ogni lunedì.", "solo tempi semplici"),
         ("andare + participio", "La plastica va separata dalla carta.", "= deve essere"), ("si passivante", "Si raccolgono le bottiglie.", "senza chi fa l'azione")) +
     "il participio si accorda con il soggetto: Le leggi sono state approvate."},
  scrivi([("1. Il comune organizza la raccolta. → La raccolta ___ dal comune.", ["e organizzata", "viene organizzata"]),
          ("2. Hanno costruito il parco eolico nel 2020. → Il parco eolico ___ nel 2020.", ["e stato costruito"]),
          ("3. Si deve spegnere la luce. → La luce ___ spenta.", ["va"]), ("4. Tutti leggono questo articolo. → Questo articolo ___ da tutti.", ["e letto", "viene letto"])],
         "2 · Trasforma al passivo", "2 · Il passivo", "e2", w="m"),
  libero("e3", 3, "La tua opinione", "Che cosa si dovrebbe fare per l'ambiente nella tua città? Scrivi un breve testo argomentativo (80 parole).", ["Il mio testo"], rows=6),
]))

# ---------------------------------------------------------------- C1
P["c1-passato-remoto"] = ("C1", pagina("📜", "Raccontare la storia: il passato remoto", "C1", [
  {"part": "Il passato remoto", "teoria":
     tab(("io", "parlai", "credei / credetti", "partii"), ("tu", "parlasti", "credesti", "partisti"), ("lui / lei", "parlò", "credé / credette", "partì"),
         ("noi", "parlammo", "credemmo", "partimmo"), ("voi", "parlaste", "credeste", "partiste"), ("loro", "parlarono", "crederono / credettero", "partirono"),
         head=("", "-are", "-ere", "-ire")) +
     "irregolari frequenti: essere → fui, fu, furono · avere → ebbi, ebbe, ebbero · fare → feci, fece, fecero · nascere → nacque · vivere → visse · scrivere → scrisse · venire → venne." +
     "<br>si usa per fatti lontani e chiusi, nella storia e nei racconti, soprattutto allo scritto."},
  scrivi([("1. Garibaldi (nascere) ___ a Nizza nel 1807.", ["nacque"]), ("2. Dante (scrivere) ___ la Divina Commedia.", ["scrisse"]),
          ("3. I Romani (costruire) ___ molte strade.", ["costruirono"]), ("4. La regina (avere) ___ tre figli.", ["ebbe"]),
          ("5. Federico II (vivere) ___ a lungo in Puglia.", ["visse"]), ("6. Gli emigranti (partire) ___ dal porto di Napoli.", ["partirono"])],
         "1 · Scrivi il passato remoto", "1 · Il passato remoto", "e1"),
  vf(["1. Il castello fu costruito da Federico II.", "2. Il castello ha la pianta rotonda.", "3. Oggi è un museo.", "4. Federico II ci abitò a lungo."], ["Vero", "Falso", "Vero", "Falso"],
     "2 · Leggi: vero o falso?", "2 · Castel del Monte", "e2",
     info="Castel del Monte fu fatto costruire da Federico II intorno al 1240, su una collina delle Murge. La sua pianta ottagonale, con otto torri anch'esse ottagonali, "
          "lo rese unico in Europa. Non sappiamo con certezza a che cosa servisse: l'imperatore, infatti, non vi soggiornò mai a lungo. Oggi è patrimonio UNESCO e si può visitare."),
  libero("e3", 3, "Una storia del mio paese", "Racconta un fatto storico o una leggenda del tuo paese al passato remoto (100 parole).", ["Il racconto"], rows=6),
]))

P["c1-concordanza"] = ("C1", pagina("🧷", "La concordanza dei tempi", "C1", [
  {"part": "Congiuntivo e concordanza", "teoria":
     tab(("penso / penserò", "che venga (adesso / dopo)", "che sia venuto (prima)"), ("pensavo / ho pensato / penserei", "che venisse (stesso momento / dopo)", "che fosse venuto (prima)"),
         head=("verbo principale", "contemporaneità / posteriorità", "anteriorità")) +
     "posteriorità nel passato anche con il condizionale passato: Pensavo che sarebbe venuto."},
  scegli([("1. Credo che Marta ___ già partita ieri.", ["sia", "fosse", "sarà"], "sia"), ("2. Speravo che tu ___ alla festa.", ["venissi", "venga", "verrai"], "venissi"),
          ("3. Non sapevo che loro si ___ già sposati.", ["fossero", "siano", "sarebbero"], "fossero"), ("4. Vorrei che voi ___ più attenzione.", ["faceste", "facciate", "fate"], "faceste"),
          ("5. Era convinto che il treno ___ in ritardo il giorno dopo.", ["sarebbe arrivato", "arrivi", "arriva"], "sarebbe arrivato")], "1 · Scegli il tempo", "1 · La concordanza", "e1"),
  {"part": "Le congiunzioni con il congiuntivo", "teoria":
     "<b>benché, sebbene, nonostante</b> (concessione) · <b>affinché, perché</b> (scopo) · <b>purché, a condizione che</b> (condizione) · <b>prima che</b> · <b>senza che</b> + congiuntivo." +
     es("Benché fosse stanco, è venuto. Te lo spiego affinché tu capisca.")},
  scrivi([("1. Benché (piovere) ___, siamo usciti.", ["piovesse"]), ("2. Ti presto la macchina purché tu (guidare) ___ con prudenza.", ["guidi"]),
          ("3. Parlo piano affinché tutti (capire) ___.", ["capiscano"]), ("4. È uscito senza che nessuno lo (vedere) ___.", ["vedesse"])], "2 · Scrivi il congiuntivo", "2 · Le congiunzioni", "e2"),
]))

P["c1-registro-formale"] = ("C1", pagina("🏛️", "Scrivere in modo formale", "C1", [
  {"part": "Il registro formale", "teoria":
     tab(("informale", "formale"), ("ti scrivo per…", "Le scrivo in merito a…"), ("volevo chiederti", "vorrei cortesemente chiederLe"), ("ciao / un abbraccio", "Gentile… / Distinti saluti"),
         ("ti mando il file", "in allegato trasmetto il documento"), ("fammi sapere", "resto in attesa di un Suo cortese riscontro")) +
     "connettivi utili: <b>pertanto</b> (quindi), <b>tuttavia</b> (però), <b>inoltre</b>, <b>qualora</b> + congiuntivo (se), <b>in quanto</b> (perché)."},
  menu(["pertanto", "tuttavia", "inoltre", "qualora", "in quanto"],
       [("1. Il documento è scaduto; ___ deve essere rinnovato.", "pertanto"), ("2. ___ avesse bisogno di chiarimenti, non esiti a contattarci.", "qualora"),
        ("3. La domanda è stata respinta ___ incompleta.", "in quanto"), ("4. Il corso è gratuito; ___ è necessario iscriversi entro venerdì.", "tuttavia"),
        ("5. Allego il curriculum; ___ invio una lettera di presentazione.", "inoltre")], "1 · Il connettivo giusto", "1 · I connettivi", "e1"),
  ordina(["Gentile dottoressa Russo,", "Le scrivo in merito alla mia domanda di iscrizione.", "Vorrei cortesemente sapere se la documentazione è completa.",
          "Resto in attesa di un Suo cortese riscontro.", "Distinti saluti"], "2 · Metti in ordine l'email", "2 · L'email", "e2"),
  libero("e3", 3, "Un reclamo formale", "Scrivi un'email formale a un'azienda per un servizio che non ha funzionato (120 parole).", ["L'email"], rows=8),
]))

# ---------------------------------------------------------------- C2
P["c2-nominalizzazione"] = ("C2", pagina("🧱", "Nominalizzazione e stile", "C2", [
  {"part": "Dal verbo al nome", "teoria":
     "nei testi giornalistici e accademici si usano i nomi al posto dei verbi: più breve, più impersonale." +
     tab(("Il governo ha deciso di aumentare le tasse.", "La decisione del governo di aumentare le tasse…"), ("Quando il treno è arrivato…", "All'arrivo del treno…"),
         ("Poiché i prezzi sono saliti…", "A causa dell'aumento dei prezzi…"), head=("con il verbo", "nominalizzato"))},
  scrivi([("1. arrivare → l'___", ["arrivo"]), ("2. scegliere → la ___", ["scelta"]), ("3. crescere → la ___", ["crescita"]), ("4. ridurre → la ___", ["riduzione"]),
          ("5. chiudere → la ___", ["chiusura"]), ("6. rinunciare → la ___", ["rinuncia"])], "1 · Il nome del verbo", "1 · I nomi", "e1"),
  scegli([("1. «Dopo che la legge è stata approvata» →", ["Dopo l'approvazione della legge", "Dopo approvare la legge", "Dopo la legge approvando"], "Dopo l'approvazione della legge"),
          ("2. «Perché è aumentata la disoccupazione» →", ["Per l'aumento della disoccupazione", "Per aumentare la disoccupazione", "Aumentando disoccupazione"], "Per l'aumento della disoccupazione")],
         "2 · Scegli la versione nominale", "2 · Lo stile", "e2"),
  {"part": "I modi indefiniti", "teoria":
     "per uno stile compatto si usano <b>gerundio</b>, <b>participio</b> e <b>infinito</b> al posto delle frasi con i verbi coniugati." +
     tab(("Poiché era stanco, …", "Essendo stanco, …"), ("Dopo che ebbe finito, …", "Finito il lavoro, …"), ("Dopo che aveva parlato, …", "Dopo aver parlato, …"),
         head=("forma esplicita", "forma implicita"))},
  scrivi([("1. Poiché non avevo tempo, ho rinunciato. → Non ___ tempo, ho rinunciato.", ["avendo"]),
          ("2. Dopo che ebbe firmato il contratto, partì. → ___ il contratto, partì.", ["firmato"]),
          ("3. Dopo che ho mangiato, esco. → Dopo ___ mangiato, esco.", ["aver", "avere"])], "3 · Forma implicita", "3 · Implicita", "e3", w="m"),
]))

P["c2-modi-di-dire"] = ("C2", pagina("🎭", "Modi di dire e figure retoriche", "C2", [
  {"part": "Modi di dire", "teoria":
     tab(("essere al verde", "non avere soldi"), ("prendere due piccioni con una fava", "ottenere due risultati con un'azione"), ("non vedere l'ora", "aspettare con impazienza"),
         ("avere le mani bucate", "spendere troppo"), ("in bocca al lupo! – crepi!", "buona fortuna"), ("costare un occhio della testa", "costare moltissimo"))},
  menu(["è al verde", "ha le mani bucate", "costa un occhio della testa", "non vede l'ora", "ha preso due piccioni con una fava"],
       [("1. Spende tutto lo stipendio in tre giorni: ___.", "ha le mani bucate"), ("2. Questa borsa firmata ___.", "costa un occhio della testa"),
        ("3. Domani arriva sua figlia: ___ di abbracciarla.", "non vede l'ora"), ("4. Ha finito i soldi e aspetta lo stipendio: ___.", "è al verde"),
        ("5. Andando in centro ha pagato la bolletta e visto un'amica: ___.", "ha preso due piccioni con una fava")], "1 · Il modo di dire giusto", "1 · Modi di dire", "e1"),
  {"part": "Le figure retoriche", "teoria":
     tab(("metafora", "un paragone senza «come»", "Sei un leone."), ("similitudine", "un paragone con «come»", "Forte come un leone."),
         ("iperbole", "un'esagerazione", "Te l'ho detto mille volte."), ("ossimoro", "due parole opposte insieme", "un silenzio assordante"),
         ("litote", "dire il contrario negato", "Non è stupido (= è intelligente)."))},
  menu(["metafora", "similitudine", "iperbole", "ossimoro", "litote"],
       [("1. «Ho una fame da lupi, mangerei un elefante.»", "iperbole"), ("2. «Quel ragazzo è una volpe.»", "metafora"), ("3. «Era bianco come la neve.»", "similitudine"),
        ("4. «Una lucida follia.»", "ossimoro"), ("5. «Il film non era malaccio.»", "litote")], "2 · Che figura è?", "2 · Figure retoriche", "e2"),
  libero("e3", 3, "Il tuo paese", "Scrivi tre modi di dire della tua lingua, traducili e spiega che cosa significano. Esiste qualcosa di simile in italiano?", ["I modi di dire"], rows=5),
]))

PAGINE = [("avanzato/%s.html" % k, d) for k, (lv, d) in P.items()]
ELENCO = [(k, lv, d) for k, (lv, d) in P.items()]
