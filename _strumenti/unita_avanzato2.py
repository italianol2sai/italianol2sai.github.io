"""Altre unità B2 e C1 (2026-10-30, Erila: «e il c1? ha poche attività rispetto al libro. Anche il b2»).
Argomenti tipici di Nuovo Espresso 4 (B2) e 5 (C1): solo gli argomenti, testi ed esercizi sono scritti per il sito.
Minuscolo normale; ascolti con la voce del computer (campo "audio"). Pagine in avanzato/<nome>.html."""
from unita_drive import vf, scegli, menu, scrivi, ordina, libero, parla
from teoria import tab, es
from unita_avanzato import pagina

P = {}

def ascolto(d, testo):
    d["audio"] = testo
    return d

# ================================================================ B2

P["b2-congiuntivo-opinioni"] = ("B2", pagina("💬", "Secondo me… Dare opinioni sui social", "B2", [
  {"part": "Il congiuntivo presente e passato", "teoria":
     "dopo i verbi di <b>opinione</b> (penso, credo, mi sembra), <b>dubbio</b> (dubito, non sono sicuro), <b>speranza e volontà</b> (spero, voglio) e dopo <b>è importante / è meglio / è possibile che</b> si usa il congiuntivo." +
     tab(("io / tu / lui", "parli", "prenda", "parta", "sia", "abbia"), ("noi", "parliamo", "prendiamo", "partiamo", "siamo", "abbiamo"),
         ("voi", "parliate", "prendiate", "partiate", "siate", "abbiate"), ("loro", "parlino", "prendano", "partano", "siano", "abbiano"),
         head=("", "-are", "-ere", "-ire", "essere", "avere")) +
     "congiuntivo passato = sia / abbia + participio: Penso che <b>abbia</b> ragione. Credo che <b>siano</b> già <b>partiti</b>." +
     es("Secondo me / Per me / A mio parere + indicativo: Secondo me, hai ragione.")},
  scrivi([("1. Penso che i social (essere) ___ utili per tenersi in contatto.", ["siano"]),
          ("2. Non credo che tutti (leggere) ___ le notizie prima di condividerle.", ["leggano"]),
          ("3. È importante che i ragazzi (capire) ___ i rischi della rete.", ["capiscano"]),
          ("4. Spero che tu (avere) ___ cambiato la password.", ["abbia"]),
          ("5. Mi sembra che Luca (passare) ___ troppe ore al telefono.", ["passi"]),
          ("6. Dubito che loro (andare) ___ già a dormire: la luce è accesa.", ["siano andati"])],
         "1 · Scrivi il congiuntivo", "1 · Il congiuntivo", "e1", w="m"),
  scegli([("1. Secondo me, i giovani ___ troppo tempo online.", ["passano", "passino", "passerebbero"], "passano"),
          ("2. Credo che le fake news ___ un problema serio.", ["siano", "sono", "fossero"], "siano"),
          ("3. So che Marta ___ un blog di cucina.", ["ha", "abbia", "avesse"], "ha"),
          ("4. È probabile che domani il sito ___ chiuso per manutenzione.", ["sia", "è", "sarà"], "sia"),
          ("5. Sono sicuro che tu ___ la scelta giusta.", ["hai fatto", "abbia fatto", "facessi"], "hai fatto")],
         "2 · Indicativo o congiuntivo?", "2 · Indicativo o congiuntivo", "e2",
         info="attenzione: con <b>so che</b>, <b>sono sicuro che</b>, <b>è vero che</b> (certezza) si usa l'indicativo."),
  {"part": "Esprimere accordo e disaccordo", "teoria":
     tab(("sono d'accordo", "hai perfettamente ragione · condivido · anch'io la penso così"),
         ("in parte", "sì, però… · dipende · da un lato…, dall'altro…"),
         ("non sono d'accordo", "non la penso così · non sono affatto convinto · al contrario…"), head=("", "espressioni"))},
  ascolto(scegli([("1. Di che cosa parlano Giada e Omar?", ["dei social e dei figli", "di un nuovo telefono", "di un corso di informatica"], "dei social e dei figli"),
                  ("2. Che cosa pensa Giada?", ["che il telefono vada dato tardi", "che i social siano solo positivi", "che la scuola debba vietare internet"], "che il telefono vada dato tardi"),
                  ("3. Omar è…", ["d'accordo solo in parte", "completamente d'accordo", "del tutto contrario"], "d'accordo solo in parte"),
                  ("4. Secondo Omar è importante che i genitori…", ["diano l'esempio", "controllino ogni messaggio", "non usino mai il telefono"], "diano l'esempio")],
                 "3 · 🎧 Ascolta: d'accordo o no?", "3 · Ascolto", "e3"),
          [("F", "Omar, tu a che età hai dato il telefono a tuo figlio? Io penso che sia meglio aspettare almeno i quattordici anni."),
           ("M", "Mah, in parte sono d'accordo. Però credo che vietare tutto non serva: i ragazzi trovano sempre il modo."),
           ("F", "Sì, ma i social possono creare dipendenza. Ho letto che molti ragazzi dormono poco per colpa del telefono."),
           ("M", "È vero. Secondo me, però, è fondamentale che i genitori diano l'esempio. Se io sto sempre al telefono a cena, come posso dire a lui di smettere?"),
           ("F", "Hai ragione, su questo non ci avevo pensato.")]),
  libero("e4", 4, "La mia opinione", "Scrivi un commento per un forum: «I social avvicinano o allontanano le persone?» Usa almeno tre verbi di opinione con il congiuntivo (100 parole).", ["Il commento"], rows=7),
  parla("e5", 5, "Sei d'accordo con questa frase? «Senza smartphone si vive meglio.» Spiega perché in un minuto."),
]))

P["b2-congiuntivo-passato-cinema"] = ("B2", pagina("🎬", "Pensavo che fosse… Raccontare un film", "B2", [
  {"part": "Congiuntivo imperfetto e trapassato", "teoria":
     "se il verbo principale è al <b>passato</b> o al <b>condizionale</b>, il congiuntivo va all'imperfetto o al trapassato." +
     tab(("stesso momento", "Pensavo che il film fosse divertente.", "congiuntivo imperfetto"),
         ("prima", "Pensavo che l'avessi già visto.", "congiuntivo trapassato = avessi / fossi + participio"),
         ("desiderio", "Vorrei che tu venissi al cinema con me.", "condizionale + imperfetto"), head=("", "esempio", "tempo")) +
     "<b>come se</b> + congiuntivo imperfetto o trapassato: Parla come se fosse un regista. Si comporta come se non fosse successo niente."},
  scrivi([("1. Credevo che il film (durare) ___ di meno.", ["durasse"]),
          ("2. Non sapevo che l'attrice (vincere) ___ già un Oscar.", ["avesse vinto"]),
          ("3. Vorrei che il regista (fare) ___ un sequel.", ["facesse"]),
          ("4. Pensavamo che voi (essere) ___ già entrati in sala.", ["foste"]),
          ("5. Il protagonista parla come se (sapere) ___ tutto.", ["sapesse"]),
          ("6. Era strano che nessuno (ridere) ___ alla battuta finale.", ["ridesse"])],
         "1 · Scrivi il congiuntivo", "1 · Congiuntivo imperfetto e trapassato", "e1", w="m"),
  {"part": "Le parole del cinema", "teoria":
     "<b>la trama</b> (la storia), <b>il/la protagonista</b>, <b>il regista</b>, <b>la colonna sonora</b> (la musica), <b>i sottotitoli</b>, <b>la recensione</b>, "
     "<b>il colpo di scena</b> (un fatto inatteso), <b>girare</b> un film (fare le riprese), <b>il finale aperto</b>, <b>lo spoiler</b>."},
  menu(["la trama", "il colpo di scena", "la colonna sonora", "i sottotitoli", "la recensione", "il regista"],
       [("1. Il film è in lingua originale con ___ in italiano.", "i sottotitoli"),
        ("2. Ho letto ___ sul giornale: il critico gli dà quattro stelle.", "la recensione"),
        ("3. A metà film scopriamo che il padre è vivo: che ___!", "il colpo di scena"),
        ("4. Le musiche di Morricone: una ___ indimenticabile.", "la colonna sonora"),
        ("5. Ti racconto ___ in due parole: due fratelli cercano la madre.", "la trama"),
        ("6. ___ ha girato il film in Puglia, a Polignano.", "il regista")], "2 · Il lessico del cinema", "2 · Il lessico", "e2"),
  vf(["1. Il film è ambientato a Bari.", "2. Amina pensava che il film fosse una commedia.", "3. Il finale è chiaro.", "4. Chi scrive consiglia il film."],
     ["Falso", "Vero", "Falso", "Vero"], "3 · Leggi la recensione: vero o falso?", "3 · La recensione", "e3",
     info="<b>«Il mare di mezzo»</b> – Credevo che fosse una commedia leggera: il titolo, il manifesto colorato, tutto lo faceva pensare. "
          "Invece il film, girato tra Lampedusa e Palermo, racconta la storia di Amina, una ragazza che arriva in Sicilia e cerca il fratello. "
          "La regista evita la retorica: la macchina da presa segue Amina come se fosse una di noi. Il finale resta aperto e qualcuno in sala "
          "si è lamentato. Io, invece, sono uscita con la voglia di parlarne. Da vedere, possibilmente in lingua originale."),
  libero("e4", 4, "La mia recensione", "Scrivi la recensione di un film che hai visto: trama, protagonisti, che cosa ti aspettavi e che cosa hai pensato alla fine (120 parole).", ["La recensione"], rows=8),
  parla("e5", 5, "Racconta il film più bello che hai visto. Usa: «pensavo che…», «non sapevo che…», «sembrava che…»."),
]))

P["b2-pronomi-combinati"] = ("B2", pagina("🔗", "Glielo dico io! I pronomi combinati", "B2", [
  {"part": "Pronome indiretto + diretto", "teoria":
     tab(("mi", "me lo", "me la", "me li", "me le", "me ne"), ("ti", "te lo", "te la", "te li", "te le", "te ne"),
         ("gli / le / Le", "glielo", "gliela", "glieli", "gliele", "gliene"), ("ci", "ce lo", "ce la", "ce li", "ce le", "ce ne"),
         ("vi", "ve lo", "ve la", "ve li", "ve le", "ve ne"), ("gli (a loro)", "glielo", "gliela", "glieli", "gliele", "gliene"),
         head=("", "lo", "la", "li", "le", "ne")) +
     "al passato il participio si accorda con lo/la/li/le: Le chiavi? <b>Te le</b> ho dat<b>e</b> ieri." +
     es("con l'infinito e l'imperativo il pronome si attacca: Posso dirtelo? Dammelo! Portaglieli.")},
  scrivi([("1. Mi presti la penna? Sì, ___ presto.", ["te la"]),
          ("2. Hai dato il modulo alla segretaria? Sì, ___ ho dato.", ["glielo"]),
          ("3. Ci mandi le foto? Sì, ___ mando stasera.", ["ve le"]),
          ("4. Hai detto la verità ai tuoi genitori? No, non ___ ho ancora detta.", ["gliel'", "gliela"]),
          ("5. Quanti biglietti ti servono? ___ servono due.", ["me ne"]),
          ("6. Puoi spiegare la regola a me? Certo, posso spiegar___ subito.", ["tela"])],
         "1 · Scrivi i pronomi combinati", "1 · I pronomi combinati", "e1", w="m"),
  scegli([("1. Il certificato? ___ hanno spedito ieri.", ["Ce l'", "Ce la", "Ci lo"], "Ce l'"),
          ("2. I documenti per la signora? ___ porto io.", ["Glieli", "Gli li", "Le li"], "Glieli"),
          ("3. Signor Rossi, la ricevuta ___ mando per email.", ["gliela", "le la", "la le"], "gliela"),
          ("4. Le chiavi! ___ hai lasciate in macchina?", ["Te le", "Ti le", "Le ti"], "Te le"),
          ("5. Del problema, ___ abbiamo già parlato.", ["ce ne", "ci ne", "ne ci"], "ce ne")],
         "2 · Scegli la forma giusta", "2 · Scegli", "e2"),
  {"part": "Favori e richieste", "teoria":
     "per chiedere un favore in modo gentile: <b>Ti dispiacerebbe…?</b> · <b>Potresti…?</b> · <b>Mi faresti un favore?</b> · "
     "per rispondere: <b>Figurati!</b> · <b>Ci mancherebbe!</b> · <b>Te lo faccio volentieri.</b> · <b>Mi dispiace, ma…</b>"},
  ascolto(vf(["1. Silvia chiede a Karim di portare un pacco in posta.", "2. Karim può farlo domani mattina.", "3. Il pacco è per la sorella di Silvia.", "4. Silvia gli dà i soldi per la spedizione."],
             ["Vero", "Falso", "Falso", "Vero"], "3 · 🎧 Ascolta: vero o falso?", "3 · Ascolto", "e3"),
          [("F", "Karim, ti dispiacerebbe farmi un favore? Dovrei spedire questo pacco a mia madre, ma oggi non esco dall'ufficio prima delle sette."),
           ("M", "Figurati! Te lo porto io in posta. Però domani mattina non posso, ho il corso. Glielo spedisco nel pomeriggio, va bene?"),
           ("F", "Perfetto, grazie mille. Ecco i soldi per la spedizione e l'indirizzo. Me lo scrivi tu sul modulo?"),
           ("M", "Certo, te lo compilo io. Ci mancherebbe!")]),
  libero("e4", 4, "Un messaggio", "Scrivi un messaggio a un amico per chiedergli un favore (prestare una cosa, accompagnarti, aiutarti). Usa almeno tre pronomi combinati.", ["Il messaggio"], rows=5),
]))

P["b2-futuro-anteriore"] = ("B2", pagina("🔭", "Avrà perso il treno! Futuro anteriore e condizionale passato", "B2", [
  {"part": "Il futuro anteriore", "teoria":
     "futuro anteriore = <b>avrò / sarò</b> + participio. Si usa:" +
     tab(("azione futura che viene prima di un'altra", "Quando avrò finito il corso, cercherò lavoro."),
         ("ipotesi sul passato", "Marco non risponde: avrà perso il telefono. (= forse ha perso)"),
         head=("uso", "esempio"))},
  scrivi([("1. Appena (arrivare) ___ a casa, ti chiamo.", ["saro arrivato", "saro arrivata"]),
          ("2. Dopo che (trovare) ___ casa, porterò qui la famiglia.", ["avro trovato"]),
          ("3. È in ritardo: (perdere) ___ l'autobus.", ["avra perso"]),
          ("4. Hanno gli occhi stanchi: (dormire) ___ poco.", ["avranno dormito"]),
          ("5. Quando voi (leggere) ___ il contratto, firmerete.", ["avrete letto"])],
         "1 · Scrivi il futuro anteriore", "1 · Futuro anteriore", "e1", w="m"),
  {"part": "Il condizionale passato", "teoria":
     "condizionale passato = <b>avrei / sarei</b> + participio. Si usa:" +
     tab(("desiderio non realizzato", "Sarei venuto volentieri, ma ero malato."),
         ("futuro nel passato", "Ha detto che avrebbe chiamato. (e poi?)"),
         ("notizia non confermata (giornali)", "Il ladro sarebbe fuggito in moto."),
         ("consiglio sul passato", "Avresti dovuto chiedere prima."), head=("uso", "esempio"))},
  scegli([("1. ___ volentieri alla festa, ma dovevo lavorare.", ["Sarei andato", "Andrei", "Andavo"], "Sarei andato"),
          ("2. Mi aveva promesso che ___ puntuale.", ["sarebbe stato", "sarà", "sarebbe"], "sarebbe stato"),
          ("3. Secondo i testimoni, l'incendio ___ alle tre di notte.", ["sarebbe scoppiato", "scoppierebbe", "scoppiava"], "sarebbe scoppiato"),
          ("4. Non hai l'ombrello? ___ guardare le previsioni!", ["Avresti dovuto", "Dovresti", "Dovevi avere"], "Avresti dovuto"),
          ("5. Ieri ___ un caffè, ma il bar era chiuso.", ["avrei preso", "prenderei", "avrò preso"], "avrei preso")],
         "2 · Scegli il tempo giusto", "2 · Condizionale passato", "e2"),
  vf(["1. Il furto è avvenuto di notte.", "2. La polizia ha già arrestato i ladri.", "3. Secondo il giornale, i ladri sarebbero entrati dal tetto.", "4. Il proprietario era in negozio."],
     ["Vero", "Falso", "Vero", "Falso"], "3 · Leggi la notizia: vero o falso?", "3 · La cronaca", "e3",
     info="<b>Bari, furto in una gioielleria del centro</b> – Nella notte tra sabato e domenica ignoti sono entrati nella gioielleria di via Sparano. "
          "Secondo i primi accertamenti, i ladri sarebbero passati dal tetto di un edificio vicino e avrebbero disattivato l'allarme. "
          "Il proprietario, che si trovava fuori città, è stato avvisato all'alba. Le indagini sono in corso: per ora nessun arresto."),
  libero("e4", 4, "Rimpianti", "Pensa a tre cose che avresti fatto in modo diverso negli ultimi anni e a tre cose che farai quando avrai raggiunto un obiettivo.", ["Il mio testo"], rows=6),
  parla("e5", 5, "Immagina: un tuo amico non è venuto all'appuntamento e non risponde al telefono. Fai almeno quattro ipotesi (Sarà…, Avrà…)."),
]))

P["b2-gerundio-participio"] = ("B2", pagina("🧘", "Stare bene: gerundio e participio", "B2", [
  {"part": "Il gerundio", "teoria":
     tab(("presente", "parlando, prendendo, partendo", "Camminando ogni giorno, ti senti meglio."),
         ("passato", "avendo parlato, essendo partito", "Avendo dormito poco, era nervoso."), head=("", "forma", "esempio")) +
     "il gerundio può esprimere <b>modo</b> (come?), <b>causa</b> (perché?), <b>tempo</b> (quando?) e <b>condizione</b> (se). Irregolari: fare → facendo, dire → dicendo, bere → bevendo."},
  scrivi([("1. Se mangi meno zucchero, dimagrisci. → (mangiare) ___ meno zucchero, dimagrisci.", ["mangiando"]),
          ("2. Mentre faceva yoga, ascoltava musica. → (fare) ___ yoga, ascoltava musica.", ["facendo"]),
          ("3. Poiché aveva corso troppo, aveva male alle gambe. → (correre) ___ troppo, aveva male alle gambe.", ["avendo corso"]),
          ("4. Mi rilasso così: (leggere) ___ un buon libro.", ["leggendo"]),
          ("5. Poiché era arrivata tardi, non ha trovato posto. → (arrivare) ___ tardi, non ha trovato posto.", ["essendo arrivata"])],
         "1 · Scrivi il gerundio", "1 · Il gerundio", "e1", w="m"),
  {"part": "Il participio passato da solo", "teoria":
     "il participio passato può sostituire una frase di tempo: <b>Finito il lavoro</b>, vado in palestra (= dopo che ho finito il lavoro). "
     "Si accorda con il nome: <b>Fatte le valigie</b>, siamo partiti. <b>Arrivata a casa</b>, Sara si è riposata."},
  menu(["Finita", "Mangiato", "Arrivati", "Chiusa", "Prese"],
       [("1. ___ la lezione, gli studenti sono usciti.", "Finita"), ("2. ___ il pranzo, faccio una passeggiata.", "Mangiato"),
        ("3. ___ in albergo, ci siamo fatti una doccia.", "Arrivati"), ("4. ___ la porta, è andato a letto.", "Chiusa"),
        ("5. ___ le medicine, mi sono sentito meglio.", "Prese")], "2 · Il participio giusto", "2 · Il participio", "e2"),
  {"part": "Le parole del benessere", "teoria":
     "<b>lo stress</b>, <b>l'ansia</b>, <b>l'insonnia</b> (non riuscire a dormire), <b>rilassarsi</b>, <b>fare movimento</b>, <b>un'alimentazione equilibrata</b>, "
     "<b>i ritmi</b> (della giornata), <b>staccare la spina</b> (riposare, non pensare al lavoro)."},
  ascolto(scegli([("1. Che problema ha l'uomo?", ["dorme male", "ha mal di schiena", "è a dieta"], "dorme male"),
                  ("2. Che cosa gli consiglia la dottoressa prima di tutto?", ["spegnere lo schermo un'ora prima di dormire", "prendere un sonnifero", "lavorare di notte"], "spegnere lo schermo un'ora prima di dormire"),
                  ("3. Secondo la dottoressa, camminando…", ["si riduce lo stress", "si dimagrisce subito", "ci si stanca troppo"], "si riduce lo stress"),
                  ("4. Che cosa deve evitare dopo le cinque?", ["il caffè", "l'acqua", "la frutta"], "il caffè")],
                 "3 · 🎧 Ascolta: dal medico", "3 · Ascolto", "e3"),
          [("M", "Dottoressa, da qualche settimana dormo malissimo. Mi sveglio alle tre e non riesco più a riprendere sonno."),
           ("F", "Capisco. Mi dica, la sera che cosa fa prima di andare a letto?"),
           ("M", "Mah, guardo le serie sul telefono, a volte lavoro al computer…"),
           ("F", "Ecco, prima di tutto spenga gli schermi almeno un'ora prima di dormire. E cerchi di fare movimento: camminando mezz'ora al giorno si riduce molto lo stress."),
           ("M", "E il caffè? Ne bevo quattro o cinque."),
           ("F", "Dopo le cinque del pomeriggio, niente caffè. Proviamo così per due settimane e poi ci rivediamo.")]),
  libero("e4", 4, "Consigli per stare bene", "Scrivi cinque consigli per vivere senza stress. Usa il gerundio (es. «Facendo una passeggiata ogni giorno, …»).", ["I miei consigli"], rows=6),
]))

P["b2-argomentare"] = ("B2", pagina("⚖️", "Pro e contro: argomentare", "B2", [
  {"part": "I connettivi", "teoria":
     tab(("aggiungere", "inoltre, per di più, non solo… ma anche"), ("opporre", "però, tuttavia, invece, mentre"),
         ("concedere", "anche se + indicativo · nonostante / sebbene + congiuntivo"), ("causa", "poiché, dato che, siccome (a inizio frase)"),
         ("conseguenza", "quindi, perciò, di conseguenza"), ("concludere", "insomma, in conclusione, per concludere"), head=("funzione", "connettivi"))},
  menu(["inoltre", "tuttavia", "siccome", "di conseguenza", "in conclusione", "mentre"],
       [("1. Lo smart working fa risparmiare tempo; ___ riduce il traffico.", "inoltre"),
        ("2. ___ abito lontano, lavorare da casa mi aiuta molto.", "siccome"),
        ("3. Si lavora da soli; ___ ci si sente isolati.", "di conseguenza"),
        ("4. Molti sono contenti; ___ alcuni sentono la mancanza dei colleghi.", "tuttavia"),
        ("5. Io preferisco l'ufficio, ___ mia sorella lavora meglio a casa.", "mentre"),
        ("6. ___, la soluzione migliore è un modello misto.", "in conclusione")], "1 · Il connettivo giusto", "1 · I connettivi", "e1"),
  scegli([("1. ___ il lavoro da remoto sia comodo, non è adatto a tutti.", ["Sebbene", "Anche se", "Siccome"], "Sebbene"),
          ("2. ___ è comodo, non è adatto a tutti.", ["Anche se", "Nonostante", "Sebbene"], "Anche se"),
          ("3. Nonostante ___ stanco, ha finito il progetto.", ["fosse", "era", "è"], "fosse"),
          ("4. ___ il treno era in ritardo, sono arrivato tardi.", ["Dato che", "Benché", "Tuttavia"], "Dato che")],
         "2 · Concessione o causa?", "2 · Concessione e causa", "e2"),
  {"part": "Il testo argomentativo", "teoria":
     "1. <b>introduzione</b>: presenta il tema · 2. <b>tesi</b>: la tua opinione · 3. <b>argomenti</b> a favore, con esempi · "
     "4. <b>antitesi</b>: l'opinione contraria (Qualcuno potrebbe obiettare che…) · 5. <b>confutazione</b> (Tuttavia…) · 6. <b>conclusione</b>."},
  ordina(["Negli ultimi anni sempre più aziende permettono di lavorare da casa.", "A mio parere, è una possibilità positiva.",
          "Infatti si risparmiano tempo e soldi per gli spostamenti.", "Qualcuno potrebbe obiettare che a casa ci si distrae di più.",
          "Tuttavia, con una buona organizzazione si lavora anche meglio.", "In conclusione, credo che il futuro sia un modello misto."],
         "3 · Metti in ordine il testo", "3 · Il testo", "e3"),
  libero("e4", 4, "Il tuo testo argomentativo", "«È meglio vivere in una grande città o in un piccolo paese?» Scrivi un testo argomentativo con tesi, antitesi e conclusione (150 parole).", ["Il mio testo"], rows=10),
  parla("e5", 5, "Sei per il lavoro da remoto o per il lavoro in ufficio? Dai due argomenti a favore e uno contro."),
]))

P["b2-lingua-dialetti"] = ("B2", pagina("🗺️", "Lingua e dialetti: le parole nuove", "B2", [
  {"part": "Formare le parole", "teoria":
     tab(("prefissi negativi", "in-, im-, ir-, dis-, s-", "utile → inutile · possibile → impossibile · regolare → irregolare · onesto → disonesto · fortuna → sfortuna"),
         ("ri- (di nuovo)", "ri-", "fare → rifare · leggere → rileggere"),
         ("-mente (avverbi)", "aggettivo femminile + mente", "lento → lentamente · facile → facilmente"),
         ("-zione, -mento (nomi)", "dal verbo", "iscrivere → iscrizione · cambiare → cambiamento"),
         ("-bile (si può)", "dal verbo", "leggere → leggibile · lavare → lavabile"), head=("", "", "esempi"))},
  scrivi([("1. Il contrario di «possibile»: ___", ["impossibile"]), ("2. Il contrario di «onesto»: ___", ["disonesto"]),
          ("3. Il contrario di «responsabile»: ___", ["irresponsabile"]), ("4. Leggere di nuovo = ___", ["rileggere"]),
          ("5. Il nome di «cambiare»: il ___", ["cambiamento"]), ("6. Un'acqua che si può bere è ___", ["potabile"])],
         "1 · Forma la parola", "1 · Formare le parole", "e1"),
  {"part": "Italiano, dialetti e lingue straniere", "teoria":
     "in Italia ci sono molti <b>dialetti</b> (il barese, il napoletano, il veneto…): non sono «italiano sbagliato», ma lingue nate dal latino. "
     "L'italiano usa anche molti <b>prestiti</b> dall'inglese (il weekend, il computer, lo smart working) e alcune parole italiane sono famose nel mondo (pizza, ciao, opera)."},
  vf(["1. Il barese è un italiano scritto male.", "2. I dialetti italiani vengono dal latino.", "3. Oggi molti italiani parlano sia l'italiano sia il dialetto.", "4. Secondo il testo, è meglio non parlare mai il dialetto."],
     ["Falso", "Vero", "Vero", "Falso"], "2 · Leggi: vero o falso?", "2 · I dialetti", "e2",
     info="Quando Ahmed è arrivato a Bari, al mercato non capiva quasi niente: «Ué, che vuè?» gli chiedeva il fruttivendolo. Era barese, il dialetto della città. "
          "Come tutti i dialetti italiani, il barese è nato dal latino, come l'italiano: è una lingua vera, con la sua grammatica. "
          "Oggi quasi tutti gli italiani parlano l'italiano, ma molti usano anche il dialetto in famiglia o con gli amici. "
          "Ahmed adesso conosce qualche parola e, quando la usa, i vicini ridono contenti: il dialetto avvicina le persone."),
  menu(["il weekend", "il computer", "la mail", "lo stage", "il marketing"],
       [("1. Il fine settimana = ___", "il weekend"), ("2. Il tirocinio in un'azienda = ___", "lo stage"),
        ("3. La posta elettronica = ___", "la mail"), ("4. L'elaboratore, il PC = ___", "il computer"),
        ("5. Le tecniche per vendere un prodotto = ___", "il marketing")], "3 · La parola inglese", "3 · I prestiti", "e3"),
  libero("e4", 4, "Le mie lingue", "Quali lingue e dialetti parli? Dove e con chi li usi? Conosci qualche parola del dialetto della città in cui vivi?", ["Le mie lingue"], rows=6),
  parla("e5", 5, "Insegna a un compagno tre parole della tua lingua o del tuo dialetto: che cosa vogliono dire e quando si usano?"),
]))

# ================================================================ C1

P["c1-concessive-condizionali"] = ("C1", pagina("🔐", "Benché, purché, a meno che", "C1", [
  {"part": "Frasi concessive", "teoria":
     tab(("+ congiuntivo", "benché, sebbene, nonostante, malgrado, per quanto", "Per quanto si impegni, non riesce a superare l'esame."),
         ("+ indicativo", "anche se, eppure, tuttavia", "Anche se piove, esco."),
         ("+ gerundio", "pur + gerundio", "Pur conoscendo la regola, sbaglia."),
         ("chiunque, qualunque, dovunque", "+ congiuntivo", "Qualunque cosa tu dica, non cambio idea."), head=("", "connettivi", "esempio"))},
  scrivi([("1. Per quanto (essere) ___ difficile, il corso mi piace.", ["sia"]),
          ("2. Pur (avere) ___ poco tempo, ha accettato l'incarico.", ["avendo"]),
          ("3. Malgrado le difficoltà (aumentare) ___, l'associazione continua a lavorare.", ["aumentino"]),
          ("4. Dovunque tu (andare) ___, troverai qualcuno che parla italiano.", ["vada"]),
          ("5. Sebbene (studiare) ___ molto, non aveva superato la prova.", ["avesse studiato"])],
         "1 · Concessive", "1 · Le concessive", "e1", w="m"),
  {"part": "Frasi condizionali ed eccettuative", "teoria":
     tab(("purché, a patto che, a condizione che", "= solo se", "Ti aiuto purché tu mi dica la verità."),
         ("nel caso in cui, qualora", "= se per caso", "Qualora non ricevesse la mail, ci chiami."),
         ("a meno che (non)", "= tranne se", "Arrivo alle otto, a meno che non ci sia traffico."),
         ("senza che", "", "È uscito senza che nessuno se ne accorgesse."), head=("connettivo", "significato", "esempio")) +
     "tutti vogliono il <b>congiuntivo</b>."},
  scegli([("1. Puoi usare la sala ___ la lasci in ordine.", ["purché", "a meno che", "senza che"], "purché"),
          ("2. Partiamo domani, ___ non nevichi.", ["a meno che", "purché", "affinché"], "a meno che"),
          ("3. ___ il pacco non arrivasse, contatti il servizio clienti.", ["Qualora", "Benché", "Siccome"], "Qualora"),
          ("4. Ti presto i soldi ___ tu me li restituisca entro marzo.", ["a patto che", "anche se", "nonostante"], "a patto che"),
          ("5. Ha preso la decisione ___ nessuno lo sapesse.", ["senza che", "purché", "qualora"], "senza che")],
         "2 · Il connettivo giusto", "2 · Condizionali ed eccettuative", "e2"),
  vf(["1. Il contratto si rinnova automaticamente.", "2. Si può recedere senza pagare penali entro 14 giorni.", "3. Il cliente può cambiare indirizzo solo per raccomandata.", "4. Il servizio è sospeso se le bollette non vengono pagate."],
     ["Vero", "Vero", "Falso", "Vero"], "3 · Leggi il contratto: vero o falso?", "3 · Il contratto", "e3",
     info="Art. 4 – Il presente contratto si rinnova automaticamente ogni anno, a meno che una delle parti non comunichi la disdetta con 30 giorni di preavviso. "
          "Il Cliente può recedere senza penali entro 14 giorni dalla firma, purché la richiesta sia inviata per iscritto, anche tramite posta elettronica. "
          "Qualora il Cliente cambiasse indirizzo, è tenuto a comunicarlo tramite l'area personale del sito. "
          "Nel caso in cui due bollette consecutive risultino non pagate, il servizio potrà essere sospeso."),
  libero("e4", 4, "Le condizioni", "Scrivi il regolamento di una sala studio o di un orto condiviso: almeno sei regole con purché, a meno che, qualora, nonostante.", ["Il regolamento"], rows=7),
]))

P["c1-congiuntivo-indipendente"] = ("C1", pagina("🌠", "Magari! Il congiuntivo da solo", "C1", [
  {"part": "Il congiuntivo nelle frasi principali", "teoria":
     tab(("desiderio realizzabile", "Che + congiuntivo presente", "Che vinca il migliore!"),
         ("desiderio difficile", "Magari / Se + congiuntivo imperfetto", "Magari fosse vero! · Se solo avessi più tempo!"),
         ("rimpianto", "Magari / Se + congiuntivo trapassato", "Magari l'avessi saputo prima!"),
         ("dubbio", "Che + congiuntivo", "Che sia già partito? (= forse è partito)"),
         ("ordine con Lei", "congiuntivo presente", "Si accomodi! Venga pure!"), head=("funzione", "forma", "esempio"))},
  scrivi([("1. Magari (vincere) ___ la lotteria! Comprerei una casa al mare.", ["vincessi"]),
          ("2. Non risponde… che (dormire) ___ ancora?", ["dorma"]),
          ("3. Se solo (ascoltare) ___ i tuoi consigli, ora non sarei in questa situazione!", ["avessi ascoltato"]),
          ("4. Signora, (entrare) ___ pure, il dottore la aspetta.", ["entri"]),
          ("5. Che (andare) ___ tutto bene all'esame!", ["vada"]),
          ("6. Magari (esserci) ___ più parchi in questa città!", ["ci fossero"])],
         "1 · Scrivi il congiuntivo", "1 · Il congiuntivo indipendente", "e1", w="m"),
  {"part": "Come se, quasi che", "teoria":
     "<b>come se</b> / <b>quasi che</b> + congiuntivo imperfetto (stesso momento) o trapassato (prima):" +
     es("Mi guarda come se non mi conoscesse. Parlava come se avesse vissuto in Italia per anni.")},
  scegli([("1. Spende come se ___ milionario.", ["fosse", "è", "sarebbe"], "fosse"),
          ("2. Mi ha salutato come se non ___ niente.", ["fosse successo", "succede", "succederebbe"], "fosse successo"),
          ("3. Magari ___ partire con voi!", ["potessi", "posso", "potrei"], "potessi"),
          ("4. Che ___ il traffico? Sono già le nove.", ["sia", "è", "fosse stato"], "sia")],
         "2 · Scegli la forma", "2 · Come se", "e2"),
  ascolto(vf(["1. Nadia ha trovato lavoro.", "2. Nadia vorrebbe lavorare in un ristorante.", "3. Paolo le dice di non perdere la speranza.", "4. Nadia rimpiange di non aver fatto un corso."],
             ["Falso", "Falso", "Vero", "Vero"], "3 · 🎧 Ascolta: vero o falso?", "3 · Ascolto", "e3"),
          [("F", "Paolo, sono stanca. Ho mandato trenta curriculum e nessuno mi ha risposto. Magari mi chiamassero almeno per un colloquio!"),
           ("M", "Non ti scoraggiare, Nadia. Che cosa cerchi, esattamente?"),
           ("F", "Vorrei lavorare in una farmacia o in un laboratorio. In Marocco ero assistente di farmacia. Se solo avessi fatto il corso di riconoscimento del titolo l'anno scorso!"),
           ("M", "Puoi farlo adesso. E nel frattempo continua a mandare domande: che qualcuno risponda, prima o poi, è sicuro."),
           ("F", "Magari avessi il tuo ottimismo!")]),
  libero("e4", 4, "Desideri e rimpianti", "Scrivi cinque frasi che cominciano con «Magari…» o «Se solo…»: tre desideri per il futuro e due rimpianti sul passato.", ["Le mie frasi"], rows=6),
  parla("e5", 5, "Racconta un desiderio grande per la tua vita. Che cosa faresti se si realizzasse?"),
]))

P["c1-verbi-pronominali"] = ("C1", pagina("🧩", "Farcela, cavarsela, prendersela", "C1", [
  {"part": "I verbi pronominali", "teoria":
     tab(("farcela", "riuscire", "Ce la faccio da solo. Non ce l'ho fatta."),
         ("cavarsela", "superare una difficoltà abbastanza bene", "In italiano me la cavo."),
         ("prendersela", "offendersi, arrabbiarsi", "Non prendertela, scherzavo!"),
         ("andarsene", "andare via", "Me ne vado, è tardi."),
         ("fregarsene", "non interessarsi (informale)", "Se ne frega delle regole."),
         ("metterci", "impiegare tempo", "Quanto ci metti a casa? Ci metto venti minuti."),
         ("volerci", "essere necessario", "Ci vogliono due ore. Ci vuole pazienza."),
         ("smetterla", "finire, basta", "Smettila di urlare!"), head=("verbo", "significato", "esempio")) +
     "al passato: ce l'ho fatt<b>a</b> · me la sono cavat<b>a</b> · se n'è andat<b>o</b> · ci ho mess<b>o</b> un'ora · ci sono volut<b>e</b> due ore."},
  menu(["ce la faccio", "me la cavo", "te la sei presa", "me ne vado", "ci vuole", "ci metto"],
       [("1. Il trasloco è pesante, ma ___ da solo.", "ce la faccio"), ("2. Non parlo benissimo il tedesco, però ___.", "me la cavo"),
        ("3. Perché non mi saluti? ___ per quello che ho detto?", "te la sei presa"), ("4. Sono stanco: ___ a dormire.", "me ne vado"),
        ("5. Per imparare una lingua ___ tanta pazienza.", "ci vuole"), ("6. Per arrivare al lavoro ___ mezz'ora a piedi.", "ci metto")],
       "1 · Il verbo giusto", "1 · I verbi pronominali", "e1"),
  scrivi([("1. All'esame (io, farcela) ___ al primo tentativo! (passato prossimo)", ["ce l'ho fatta"]),
          ("2. Per finire il progetto (volerci) ___ tre mesi. (passato prossimo)", ["ci sono voluti"]),
          ("3. Gli ospiti (andarsene) ___ a mezzanotte. (passato prossimo)", ["se ne sono andati"]),
          ("4. Quanto tempo (tu, metterci) ___ a trovare casa? (passato prossimo)", ["ci hai messo"]),
          ("5. Marta (cavarsela) ___ bene al colloquio. (passato prossimo)", ["se l'e cavata"])],
         "2 · Al passato prossimo", "2 · Il passato", "e2", w="m"),
  vf(["1. Il primo anno l'autore se l'è cavata subito bene.", "2. Ci sono voluti mesi per trovare casa.", "3. Un vicino se l'è presa per la musica.", "4. Alla fine l'autore vuole andarsene da Bari."],
     ["Falso", "Vero", "Vero", "Falso"], "3 · Leggi: vero o falso?", "3 · Il racconto", "e3",
     info="Il primo anno a Bari è stato duro. Non parlavo una parola di italiano e pensavo di non farcela. Per trovare una stanza ci sono voluti quattro mesi: "
          "ogni volta che telefonavo, appena sentivano il mio accento, la stanza «non era più libera». Poi ho trovato un appartamento con due studenti, "
          "ma il vicino del piano di sotto se l'è presa per la musica e ha chiamato l'amministratore. Adesso ridiamo di quella storia, e lui mi porta i taralli a Natale. "
          "Oggi me la cavo con la lingua, ho un lavoro e degli amici: andarmene? Non ci penso proprio."),
  libero("e4", 4, "Ce l'ho fatta!", "Racconta un momento in cui pensavi di non farcela e invece ce l'hai fatta. Usa almeno quattro verbi pronominali.", ["Il racconto"], rows=7),
]))

P["c1-forme-implicite"] = ("C1", pagina("📚", "Lo stile letterario: forme implicite e trapassato remoto", "C1", [
  {"part": "Infinito passato e participio presente", "teoria":
     tab(("infinito passato", "aver / esser + participio", "Dopo aver letto la lettera, pianse. · Mi scuso per essere arrivato tardi."),
         ("participio presente", "-ante / -ente", "i cittadini residenti (= che risiedono) · l'acqua corrente · un film affascinante"),
         ("participio passato assoluto", "participio + nome", "Terminata la guerra, tornò al paese."), head=("forma", "come si fa", "esempio"))},
  scrivi([("1. Dopo che aveva cenato, uscì. → Dopo (cenare) ___, uscì.", ["aver cenato", "avere cenato"]),
          ("2. Ti ringrazio perché mi hai aiutato. → Ti ringrazio per (aiutare) ___.", ["avermi aiutato"]),
          ("3. Le persone che partecipano al corso → le persone (partecipare) ___", ["partecipanti"]),
          ("4. Quando la lettera fu scritta, la spedì. → (scrivere) ___ la lettera, la spedì.", ["scritta"]),
          ("5. Dopo che era partita, si pentì. → Dopo (partire) ___, si pentì.", ["essere partita", "esser partita"])],
         "1 · Trasforma", "1 · Le forme implicite", "e1", w="m"),
  {"part": "Il trapassato remoto", "teoria":
     "trapassato remoto = <b>ebbi / fui</b> + participio. Si usa solo nei testi scritti, dopo <b>quando, dopo che, appena, non appena</b>, se il verbo principale è al passato remoto." +
     es("Appena ebbe finito di parlare, tutti applaudirono. Quando fu uscita, la stanza rimase in silenzio.")},
  scegli([("1. Appena ___ la notizia, corse a casa.", ["ebbe saputo", "aveva saputo", "ha saputo"], "ebbe saputo"),
          ("2. Dopo che gli ospiti ___, spense le luci.", ["furono partiti", "sono partiti", "partivano"], "furono partiti"),
          ("3. Quando ___ di mangiare, si alzarono.", ["ebbero finito", "hanno finito", "finivano"], "ebbero finito"),
          ("4. Non appena la nave ___ nel porto, scesero tutti.", ["fu entrata", "è entrata", "entrava"], "fu entrata")],
         "2 · Il trapassato remoto", "2 · Trapassato remoto", "e2"),
  vf(["1. Il nonno partì giovane.", "2. Lavorò in una miniera in Belgio.", "3. Tornò in Italia appena arrivato.", "4. Al ritorno comprò un uliveto."],
     ["Vero", "Vero", "Falso", "Vero"], "3 · Leggi il racconto: vero o falso?", "3 · Il racconto", "e3",
     info="Mio nonno partì da Altamura nel 1952, avendo appena compiuto diciotto anni. Salito sul treno con una valigia di cartone, non si voltò a guardare la stazione. "
          "In Belgio scese in miniera: il lavoro era durissimo e la polvere entrava dappertutto. Dopo che ebbe messo da parte i soldi necessari, "
          "dopo dodici anni di carbone, tornò al paese. Comprato un piccolo uliveto, vi lavorò fino alla fine dei suoi giorni, senza mai parlare del Belgio."),
  libero("e4", 4, "Un racconto", "Scrivi l'inizio di un racconto (120 parole) al passato remoto. Usa almeno un gerundio, un participio assoluto e un infinito passato.", ["Il racconto"], rows=8),
]))

P["c1-lingua-che-cambia"] = ("C1", pagina("🔤", "L'italiano che cambia: anglicismi e neologismi", "C1", [
  {"part": "Anglicismi, neologismi, prestiti", "teoria":
     tab(("prestito integrale", "la parola entra uguale", "il computer, lo smartphone, il manager"),
         ("prestito adattato", "la parola si «italianizza»", "chattare, postare, scannerizzare"),
         ("calco", "la parola si traduce", "grattacielo (skyscraper), fine settimana (weekend)"),
         ("neologismo", "parola nuova", "apericena, webinar, smart working, petaloso"), head=("tipo", "che cos'è", "esempio")) +
     "i verbi inglesi entrano quasi sempre nella <b>prima coniugazione</b>: to like → laikare, to google → googlare."},
  menu(["prestito integrale", "prestito adattato", "calco", "neologismo"],
       [("1. «Ho postato la foto.»", "prestito adattato"), ("2. «Il meeting è alle tre.»", "prestito integrale"),
        ("3. «Il fine settimana vado al mare.»", "calco"), ("4. «Facciamo un apericena?»", "neologismo"),
        ("5. «Ho scaricato l'app.»", "calco"), ("6. «Mi ha bloccato e io l'ho stalkerato.»", "prestito adattato")], "1 · Che tipo di parola è?", "1 · I tipi", "e1"),
  scrivi([("1. the deadline = la ___ (parola italiana)", ["scadenza"]), ("2. the feedback = il ___ (parola italiana)", ["riscontro", "parere", "commento"]),
          ("3. the meeting = la ___ (parola italiana)", ["riunione"]), ("4. the welfare = lo stato ___", ["sociale"]),
          ("5. the jobs act = la riforma del ___", ["lavoro"])], "2 · Trova la parola italiana", "2 · In italiano", "e2", w="m"),
  {"part": "Argomentare in un dibattito", "teoria":
     "per prendere la parola: <b>Vorrei aggiungere che…</b> · <b>Mi permetta di dissentire…</b> · <b>Non mi trova d'accordo…</b> · "
     "<b>È innegabile che…</b> (+ congiuntivo) · <b>Va detto però che…</b> · <b>Ne consegue che…</b>"},
  ascolto(scegli([("1. Di che cosa si discute?", ["dell'uso dell'inglese nell'italiano", "dell'insegnamento dell'inglese a scuola", "dei dialetti"], "dell'uso dell'inglese nell'italiano"),
                  ("2. Che cosa pensa la professoressa?", ["che molti anglicismi non siano necessari", "che l'inglese vada vietato", "che l'italiano sia una lingua morta"], "che molti anglicismi non siano necessari"),
                  ("3. Il giornalista sostiene che…", ["le lingue cambiano sempre", "bisogna usare solo parole italiane", "l'inglese è più bello"], "le lingue cambiano sempre"),
                  ("4. Su che cosa sono d'accordo?", ["sulla chiarezza nei documenti pubblici", "sull'abolire l'inglese", "su niente"], "sulla chiarezza nei documenti pubblici")],
                 "3 · 🎧 Ascolta il dibattito", "3 · Ascolto", "e3"),
          [("F", "È innegabile che l'italiano stia accogliendo troppe parole inglesi. Perché dire «meeting» se abbiamo «riunione»? Molti anglicismi non sono affatto necessari."),
           ("M", "Mi permetta di dissentire, professoressa. Le lingue sono sempre cambiate: il latino ha preso parole dal greco, l'italiano dal francese e dall'arabo. Non è una minaccia."),
           ("F", "Va detto però che quando un ufficio pubblico scrive «welfare» o «caregiver», molti cittadini, anziani o stranieri, non capiscono."),
           ("M", "Su questo le do ragione: nei documenti pubblici la chiarezza deve venire prima di tutto.")]),
  libero("e4", 4, "La tua opinione", "Gli anglicismi impoveriscono o arricchiscono l'italiano? Scrivi un breve articolo d'opinione (180 parole) con esempi.", ["L'articolo"], rows=10),
  parla("e5", 5, "Nella tua lingua ci sono parole prese dall'inglese, dal francese o dall'arabo? Fai tre esempi e spiega se ti piacciono."),
]))

P["c1-saggio-breve"] = ("C1", pagina("📝", "Il saggio breve: scrivere un testo argomentativo", "C1", [
  {"part": "I connettivi del testo scritto", "teoria":
     tab(("ordinare", "in primo luogo, in secondo luogo, infine"), ("aggiungere", "inoltre, per giunta, peraltro"),
         ("spiegare", "ovvero, vale a dire, in altre parole"), ("esemplificare", "ad esempio, si pensi a, basti pensare a"),
         ("opporre", "ciononostante, d'altra parte, al contrario"), ("concludere", "in definitiva, alla luce di quanto detto, pertanto"),
         head=("funzione", "connettivi"))},
  menu(["in primo luogo", "basti pensare a", "vale a dire", "ciononostante", "in definitiva", "peraltro"],
       [("1. ___, va chiarito che cosa si intende per integrazione.", "in primo luogo"),
        ("2. L'integrazione passa dalla lingua: ___ quanto conta capire un medico o un insegnante.", "basti pensare a"),
        ("3. Servono più corsi serali, ___ corsi compatibili con il lavoro.", "vale a dire"),
        ("4. I fondi sono aumentati; ___, le classi restano sovraffollate.", "ciononostante"),
        ("5. I corsi sono gratuiti e, ___, rilasciano un certificato riconosciuto.", "peraltro"),
        ("6. ___, investire nella lingua significa investire nella convivenza.", "in definitiva")], "1 · Il connettivo giusto", "1 · I connettivi", "e1"),
  {"part": "La struttura del saggio", "teoria":
     "<b>titolo</b> · <b>introduzione</b> (il tema e perché è attuale) · <b>tesi</b> · <b>argomenti</b> con dati ed esempi · "
     "<b>antitesi e confutazione</b> · <b>conclusione</b> (riprende la tesi, apre una prospettiva). Registro: impersonale (si ritiene, è opportuno), niente «secondo me» ripetuto."},
  ordina(["Imparare la lingua del paese in cui si vive è il primo passo verso la cittadinanza piena.",
          "Si ritiene, infatti, che senza la lingua sia impossibile accedere ai servizi e al lavoro.",
          "Basti pensare alle difficoltà di chi deve spiegare un sintomo al medico.",
          "D'altra parte, non va dimenticato che molti adulti lavorano tutto il giorno.",
          "Ne consegue che i corsi debbano adattarsi agli orari di chi studia.",
          "In definitiva, la lingua è un diritto prima ancora che un dovere."],
         "2 · Metti in ordine il saggio", "2 · La struttura", "e2"),
  scegli([("1. In un saggio è meglio scrivere…", ["si ritiene che", "secondo me", "boh, penso che"], "si ritiene che"),
          ("2. «Ci sono un sacco di problemi» in registro formale diventa…", ["Si riscontrano numerose criticità", "Ci sono tanti casini", "Problemi ce ne sono"], "Si riscontrano numerose criticità"),
          ("3. «La gente non lo sa» →", ["Tale aspetto è poco noto all'opinione pubblica", "La gente non lo sa mica", "Nessuno lo sa, figurati"], "Tale aspetto è poco noto all'opinione pubblica"),
          ("4. «Comunque alla fine…» →", ["In definitiva", "Tipo alla fine", "Insomma, dai"], "In definitiva")],
         "3 · Scegli il registro giusto", "3 · Il registro", "e3"),
  libero("e4", 4, "Il tuo saggio breve", "Titolo: «La lingua come chiave dell'integrazione». Scrivi un saggio breve (250 parole) con introduzione, tesi, argomenti, antitesi e conclusione.", ["Il saggio"], rows=14),
]))

P["c1-linguaggio-burocratico"] = ("C1", pagina("🏢", "Capire la burocrazia: il linguaggio degli uffici", "C1", [
  {"part": "Le parole della burocrazia", "teoria":
     tab(("l'istanza", "la domanda"), ("il/la richiedente", "chi fa la domanda"), ("il termine perentorio", "la scadenza da rispettare per forza"),
         ("allegare", "aggiungere un documento"), ("la decorrenza", "la data da cui vale"), ("ai sensi di", "secondo (la legge)"),
         ("pena l'esclusione", "altrimenti si viene esclusi"), ("previa", "dopo, a condizione di (previa prenotazione)"), head=("burocratese", "italiano semplice"))},
  menu(["istanza", "richiedente", "termine perentorio", "previa", "pena l'esclusione", "ai sensi"],
       [("1. Il ___ deve essere maggiorenne.", "richiedente"), ("2. L'___ va presentata in carta semplice.", "istanza"),
        ("3. Il 30 giugno è un ___: dopo non si accettano domande.", "termine perentorio"), ("4. Si riceve ___ prenotazione online.", "previa"),
        ("5. Allegare la copia del documento, ___.", "pena l'esclusione"), ("6. ___ dell'art. 13 del Regolamento UE 2016/679…", "ai sensi")],
       "1 · La parola giusta", "1 · Il lessico", "e1"),
  {"part": "Lo stile burocratico", "teoria":
     "nei testi degli uffici si usano: il <b>passivo</b> e il <b>si</b> impersonale (si comunica che…), il verbo <b>andare</b> + participio (la domanda va presentata = deve essere presentata), "
     "il <b>participio presente</b> (gli aventi diritto), le <b>nominalizzazioni</b> (la presentazione della domanda)." },
  scrivi([("1. «Bisogna consegnare il modulo entro venerdì» → Il modulo ___ consegnato entro venerdì.", ["va", "deve essere"]),
          ("2. «Le persone che hanno diritto» → gli ___ diritto", ["aventi"]),
          ("3. «Quando presenterà la domanda» → all'atto della ___ della domanda", ["presentazione"]),
          ("4. «Vi informiamo che l'ufficio è chiuso» → ___ comunica che l'ufficio è chiuso.", ["si"])],
         "2 · Riscrivi in stile burocratico", "2 · Lo stile", "e2", w="m"),
  vf(["1. Il bando è per un contributo all'affitto.", "2. Si può fare domanda anche dopo il 15 dicembre.", "3. Serve l'ISEE.", "4. La domanda si presenta solo allo sportello."],
     ["Vero", "Falso", "Vero", "Falso"], "3 · Leggi l'avviso: vero o falso?", "3 · L'avviso", "e3",
     info="<b>AVVISO PUBBLICO – Contributo per il sostegno alla locazione</b><br>Si rende noto che i nuclei familiari residenti nel Comune, titolari di un contratto di locazione regolarmente registrato, "
          "possono presentare istanza per l'erogazione di un contributo economico. L'istanza, corredata dall'attestazione ISEE in corso di validità, va presentata "
          "entro il termine perentorio del 15 dicembre, pena l'esclusione, tramite il portale online oppure presso lo Sportello del Cittadino, previo appuntamento."),
  libero("e4", 4, "Riscrivi in italiano semplice", "Riscrivi l'avviso dell'esercizio 3 in italiano semplice, per una persona che sta imparando l'italiano (A2).", ["Il testo semplice"], rows=7),
  parla("e5", 5, "Sei allo Sportello del Cittadino: spiega all'impiegato che vuoi chiedere il contributo per l'affitto e chiedi quali documenti servono."),
]))

# ================================================================ C2

P["c2-ordine-marcato"] = ("C2", pagina("🔀", "L'ordine delle parole: dislocazioni e frasi scisse", "C2", [
  {"part": "Le dislocazioni", "teoria":
     "nel parlato si sposta un elemento all'inizio o alla fine della frase e lo si riprende con un pronome, per metterlo in evidenza." +
     tab(("dislocazione a sinistra", "Il caffè, lo prendo amaro. · A Maria, le ho già scritto. · Di politica, non ne parlo."),
         ("dislocazione a destra", "Lo vuoi, un caffè? · Ce l'hai, la patente?"),
         ("tema sospeso", "Mio fratello, gli italiani gli sembrano tutti simpatici."), head=("costruzione", "esempi")) +
     "il pronome deve concordare: <b>La</b> pizza, <b>la</b> mangio · <b>Le</b> chiavi, <b>le</b> ho perse · <b>Al</b> direttore, <b>gli</b> parlo io."},
  scrivi([("1. Il giornale, ___ compro ogni mattina.", ["lo"]), ("2. Le tue amiche, ___ ho viste ieri al mercato.", ["le"]),
          ("3. A tuo padre, ___ hai detto la verità?", ["gli"]), ("4. Di questa storia, non ___ voglio più sentir parlare.", ["ne"]),
          ("5. A Roma, ___ sono stato tre volte.", ["ci"]), ("6. ___ hai fatti, i compiti?", ["li"])],
         "1 · Il pronome di ripresa", "1 · Le dislocazioni", "e1", w="s"),
  {"part": "Le frasi scisse", "teoria":
     "<b>è / sono … che</b> (o <b>a</b> + infinito) mette in evidenza una sola parte della frase:" +
     tab(("frase normale", "Marco ha rotto il vaso."), ("frase scissa", "È Marco che ha rotto il vaso. · È stato Marco a rompere il vaso."),
         ("con il tempo", "È da tre anni che vivo qui."), ("con la causa", "È per questo che ti ho chiamato."), head=("", "esempio"))},
  scegli([("1. Chi ha chiamato? – ___ ha chiamato.", ["È stata Lucia che", "Lucia è che", "È Lucia ha"], "È stata Lucia che"),
          ("2. ___ abito a Bari.", ["È da dieci anni che", "Sono dieci anni che da", "Da dieci anni è che"], "È da dieci anni che"),
          ("3. Sono i giovani ___ usano di più i social.", ["che", "di", "per"], "che"),
          ("4. È per questo ___ non sono venuto.", ["che", "a", "di"], "che")],
         "2 · Scegli la frase scissa", "2 · Le frasi scisse", "e2"),
  menu(["dislocazione a sinistra", "dislocazione a destra", "frase scissa", "ordine normale"],
       [("1. «La macchina, l'ha presa mia sorella.»", "dislocazione a sinistra"), ("2. «L'hai letto, il libro che ti ho prestato?»", "dislocazione a destra"),
        ("3. «È Giulia che organizza la festa.»", "frase scissa"), ("4. «Giulia organizza la festa.»", "ordine normale"),
        ("5. «Ce l'avete, il biglietto?»", "dislocazione a destra")], "3 · Che costruzione è?", "3 · Riconosci", "e3"),
  libero("e4", 4, "Riscrivi", "Riscrivi queste frasi mettendo in evidenza le parole sottolineate a voce: «Ho comprato il pane stamattina.» «Ho conosciuto mia moglie a Lecce.» «Non mi piace il caffè americano.»", ["Le mie frasi"], rows=4),
  parla("e5", 5, "Rispondi usando una dislocazione: «Il caffè come lo prendi?» «I tuoi genitori li senti spesso?» «Di lavoro, ne parli con gli amici?»"),
]))

P["c2-ipotesi-avanzate"] = ("C2", pagina("🌀", "Ipotesi senza se: il periodo ipotetico misto e implicito", "C2", [
  {"part": "Il periodo ipotetico misto", "teoria":
     tab(("passato → presente", "se + congiuntivo trapassato → condizionale presente", "Se avessi studiato medicina, oggi sarei medico."),
         ("presente → passato", "se + congiuntivo imperfetto → condizionale passato", "Se fossi più prudente, non avresti fatto quell'errore."),
         ("parlato", "se + imperfetto → imperfetto", "Se lo sapevo, venivo. (= se l'avessi saputo, sarei venuto)"), head=("", "forma", "esempio"))},
  scegli([("1. Se non avessi perso il treno, adesso ___ già a casa.", ["sarei", "sarei stato", "ero"], "sarei"),
          ("2. Se fosse una persona seria, ___ ieri.", ["avrebbe chiamato", "chiamerebbe", "chiamasse"], "avrebbe chiamato"),
          ("3. Se mi ___ prima, ti avrei aspettato. (parlato)", ["avvisavi", "avvisi", "avviserai"], "avvisavi"),
          ("4. Se fossi nato in Italia, ora ___ meglio l'italiano.", ["parlerei", "avrei parlato", "parlassi"], "parlerei")],
         "1 · Il periodo ipotetico misto", "1 · Il misto", "e1"),
  {"part": "Ipotesi senza «se»", "teoria":
     tab(("gerundio", "Volendo, possiamo partire domani. (= se vogliamo)"), ("a + infinito", "A saperlo, sarei rimasto. (= se l'avessi saputo)"),
         ("participio", "Usato bene, il web è una risorsa. (= se è usato bene)"),
         ("dovesse + infinito", "Dovesse piovere, rimandiamo. (= se per caso piove)"),
         ("congiuntivo senza se", "Avessi tempo, verrei. (= se avessi tempo)"), head=("forma", "esempio"))},
  scrivi([("1. Se lo avessi saputo, non sarei venuto. → A ___, non sarei venuto.", ["saperlo"]),
          ("2. Se vuoi, ti accompagno. → ___, ti accompagno.", ["volendo"]),
          ("3. Se per caso arrivasse tardi, chiamami. → ___ arrivare tardi, chiamami.", ["dovesse"]),
          ("4. Se avessi più soldi, viaggerei. → ___ più soldi, viaggerei.", ["avessi"]),
          ("5. Se è preso a stomaco vuoto, il farmaco fa male. → ___ a stomaco vuoto, il farmaco fa male.", ["preso"])],
         "2 · Ipotesi implicite", "2 · Senza se", "e2", w="m"),
  ascolto(vf(["1. Elena è diventata avvocata.", "2. Da giovane voleva fare l'attrice.", "3. Elena è pentita della sua scelta.", "4. Consiglia ai giovani di seguire i propri desideri."],
             ["Falso", "Vero", "Falso", "Vero"], "3 · 🎧 Ascolta: vero o falso?", "3 · Ascolto", "e3"),
          [("F", "Se avessi ascoltato i miei genitori, oggi sarei un avvocato con uno studio in centro. Loro volevano questo."),
           ("F", "Io, invece, a diciotto anni sognavo il teatro. A pensarci adesso, è stata una follia: niente soldi, niente certezze."),
           ("F", "Eppure, potendo tornare indietro, rifarei tutto. Faccio l'attrice da trent'anni e non mi sono mai annoiata."),
           ("F", "Ai ragazzi dico sempre: dovessero dirvi che il vostro sogno è impossibile, provateci comunque.")]),
  libero("e4", 4, "Le mie strade", "Pensa a una scelta importante della tua vita. Che cosa sarebbe diverso oggi se avessi scelto diversamente? Usa almeno due ipotesi senza «se».", ["Il mio testo"], rows=7),
]))

P["c2-sfumature-lessico"] = ("C2", pagina("🎨", "La parola precisa: sinonimi e sfumature", "C2", [
  {"part": "I verbi generici e quelli precisi", "teoria":
     "nei testi curati si evitano <b>fare, dire, mettere, dare, avere</b> e si sceglie il verbo preciso:" +
     tab(("fare una domanda", "porre una domanda"), ("fare una legge", "emanare / varare una legge"), ("fare un errore", "commettere un errore"),
         ("dire un'opinione", "esprimere un'opinione"), ("mettere una regola", "stabilire / introdurre una regola"),
         ("dare un premio", "assegnare / conferire un premio"), ("avere un ruolo", "ricoprire un ruolo"), head=("generico", "preciso"))},
  menu(["porre", "commettere", "esprimere", "conferire", "ricoprire", "varare"],
       [("1. Il parlamento ha deciso di ___ una nuova legge sull'immigrazione.", "varare"),
        ("2. Vorrei ___ una domanda al relatore.", "porre"),
        ("3. Chiunque può ___ un errore.", "commettere"),
        ("4. Le hanno chiesto di ___ la sua opinione sulla riforma.", "esprimere"),
        ("5. All'università le vogliono ___ la laurea ad honorem.", "conferire"),
        ("6. Da tre anni ___ il ruolo di coordinatrice.", "ricoprire")], "1 · Il verbo preciso", "1 · I verbi", "e1"),
  {"part": "Le sfumature", "teoria":
     "molti sinonimi non sono uguali: cambia l'<b>intensità</b> o il <b>registro</b>." +
     tab(("arrabbiato < furioso < furibondo", "intensità"), ("casa · abitazione · dimora", "neutro · burocratico · letterario"),
         ("morire · venire a mancare · spegnersi · crepare", "neutro · gentile · letterario · volgare"),
         ("lavoro · impiego · mestiere · professione", "generale · contratto · manuale · intellettuale"), head=("parole", "differenza"))},
  scegli([("1. In un necrologio si scrive: «È ___ il nostro caro nonno.»", ["venuto a mancare", "crepato", "morto stecchito"], "venuto a mancare"),
          ("2. In un modulo: «Indirizzo dell'___».", ["abitazione", "dimora", "casetta"], "abitazione"),
          ("3. «Fa il falegname: è un ___ antico.»", ["mestiere", "impiego", "professione"], "mestiere"),
          ("4. Più forte di «arrabbiato»: …", ["furibondo", "seccato", "infastidito"], "furibondo"),
          ("5. «Vive in una splendida ___ dell'Ottocento.» (testo letterario)", ["dimora", "abitazione", "casa popolare"], "dimora")],
         "2 · La sfumatura giusta", "2 · Le sfumature", "e2"),
  scrivi([("1. Mi ha fatto una domanda difficile. → Mi ha ___ una domanda difficile.", ["posto"]),
          ("2. Hanno dato il premio a una scrittrice. → Hanno ___ il premio a una scrittrice.", ["assegnato", "conferito"]),
          ("3. Ho fatto un errore grave. → Ho ___ un errore grave.", ["commesso"]),
          ("4. Il comune ha messo nuove regole. → Il comune ha ___ nuove regole.", ["stabilito", "introdotto"])],
         "3 · Riscrivi con il verbo preciso", "3 · Riscrivi", "e3", w="m"),
  libero("e4", 4, "Riscrivi il testo", "Riscrivi in registro curato: «Il sindaco ha fatto una riunione e ha detto che mette nuove regole per i rifiuti. Molti hanno fatto domande e qualcuno ha fatto polemica.»", ["Il testo curato"], rows=5),
]))

P["c2-varieta-italiano"] = ("C2", pagina("🗣️", "Le varietà dell'italiano: regionale, giovanile, giornalistico", "C2", [
  {"part": "L'italiano regionale", "teoria":
     "ogni regione ha un suo modo di parlare italiano: suoni, parole e costruzioni diverse." +
     tab(("Nord", "il passato prossimo anche per fatti lontani · la Maria (articolo con i nomi) · «Ciao, bella!»"),
         ("Toscana", "la c aspirata (la hasa) · «Noi si va» (= noi andiamo)"),
         ("Sud", "il passato remoto anche per fatti recenti (Ieri andai) · tenere = avere (Tengo fame) · stare = essere (Sto a casa)"),
         ("Puglia", "«Ué!» · «Mo» (= adesso) · «Accomodatevi» con il voi"), head=("zona", "esempi"))},
  menu(["Nord", "Toscana", "Sud"],
       [("1. «Tengo due figli.»", "Sud"), ("2. «Ho parlato con la Giulia.»", "Nord"), ("3. «Stamattina mi alzai presto.»", "Sud"),
        ("4. «Domani si va al mare.»", "Toscana"), ("5. «Sto stanco morto.»", "Sud")], "1 · Da dove viene?", "1 · Italiano regionale", "e1"),
  {"part": "Il linguaggio giovanile e quello dei giornali", "teoria":
     tab(("giovanile", "che figata! (= bellissimo) · sclerare (= arrabbiarsi) · ci sta (= va bene) · bro · cringe · flexare"),
         ("giornalistico", "titoli senza verbo (Caos treni, pendolari a piedi) · il Colle (= il Presidente) · Palazzo Chigi (= il Governo) · Piazza Affari (= la Borsa) · l'esecutivo"),
         head=("varietà", "esempi"))},
  scegli([("1. «Il Colle firma la legge» =", ["il Presidente della Repubblica firma", "un gruppo di montagna firma", "il sindaco firma"], "il Presidente della Repubblica firma"),
          ("2. «Piazza Affari in rosso» =", ["la Borsa perde", "c'è una manifestazione", "il comune è in crisi"], "la Borsa perde"),
          ("3. «Ci sta!» detto da un ragazzo =", ["va bene, sono d'accordo", "c'è qualcuno", "è lì"], "va bene, sono d'accordo"),
          ("4. «Mia madre ha sclerato» =", ["si è arrabbiata molto", "si è addormentata", "ha cambiato lavoro"], "si è arrabbiata molto"),
          ("5. «Palazzo Chigi apre al dialogo» =", ["il Governo è disponibile a parlare", "un museo apre", "il Parlamento chiude"], "il Governo è disponibile a parlare")],
         "2 · Che cosa vuol dire?", "2 · Giovani e giornali", "e2"),
  scrivi([("1. «Caos treni, pendolari a piedi» → I treni ___ in ritardo e i pendolari hanno dovuto camminare.", ["erano", "sono"]),
          ("2. «Che figata!» in registro neutro → Che cosa ___!", ["bella", "bellissima"]),
          ("3. «Mo vengo» (Puglia) → ___ vengo.", ["adesso", "ora"])], "3 · In italiano standard", "3 · Lo standard", "e3", w="m"),
  libero("e4", 4, "L'italiano intorno a me", "Raccogli cinque parole o espressioni che senti a Bari (al mercato, sull'autobus, dai ragazzi) e spiega che cosa significano in italiano standard.", ["Le mie parole"], rows=6),
  parla("e5", 5, "Leggi ad alta voce un titolo di giornale di oggi e spiegalo con una frase completa, come se lo raccontassi a un amico."),
]))

P["c2-punteggiatura-stile"] = ("C2", pagina("✒️", "Punteggiatura, ironia e stile", "C2", [
  {"part": "La punteggiatura", "teoria":
     tab(("virgola", "pause brevi, elenchi, incisi", "Bari, città di mare, è il mio porto."), ("punto e virgola", "separa due frasi collegate", "Era tardi; nessuno parlava."),
         ("due punti", "spiegazione, elenco, discorso diretto", "Una cosa è certa: torneremo."), ("puntini di sospensione", "frase non finita, allusione, ironia", "Sì, certo, puntuale come sempre…"),
         ("lineette", "inciso forte", "Il sindaco – lo sanno tutti – non risponde."), head=("segno", "uso", "esempio")) +
     "attenzione: mai la virgola tra soggetto e verbo: <s>Il direttore, ha deciso</s> → Il direttore ha deciso."},
  scegli([("1. Quale frase è corretta?", ["Gli studenti del corso serale hanno superato l'esame.", "Gli studenti del corso serale, hanno superato l'esame.", "Gli studenti, del corso serale hanno, superato l'esame."], "Gli studenti del corso serale hanno superato l'esame."),
          ("2. «Una cosa è chiara___ dobbiamo cambiare.»", [":", ";", ","], ":"),
          ("3. «Pioveva da giorni___ le strade erano allagate.»", [";", ":", "…"], ";"),
          ("4. «Mio cugino ___ quello che vive a Torino ___ si sposa.»", ["– … –", "; … ;", ": … :"], "– … –")],
         "1 · La punteggiatura giusta", "1 · La punteggiatura", "e1"),
  {"part": "L'ironia", "teoria":
     "l'ironia dice il contrario di quello che pensa. Si riconosce dal contesto, dal tono e da segnali come <b>proprio</b>, <b>davvero</b>, <b>certo</b>, i <b>puntini</b> e le <b>virgolette</b>." +
     es("Il treno ha due ore di ritardo: «Proprio un servizio impeccabile!» · Bella giornata, eh? (sotto la pioggia)")},
  vf(["1. «Complimenti, sei arrivato presto!» (detto a chi arriva con un'ora di ritardo) è ironico.", "2. «Che bella giornata!» detto sotto il sole di aprile è ironico.",
      "3. «Un'idea davvero geniale: lasciare le chiavi dentro la macchina.» è ironico.", "4. «La riunione è finita alle sei.» è ironico."],
     ["Vero", "Falso", "Vero", "Falso"], "2 · È ironico?", "2 · L'ironia", "e2"),
  vf(["1. L'autore è contento della burocrazia.", "2. Per avere il certificato ci sono volute tre settimane.", "3. L'impiegata era molto gentile.", "4. Il testo è ironico."],
     ["Falso", "Vero", "Falso", "Vero"], "3 · Leggi: vero o falso?", "3 · Il testo ironico", "e3",
     info="Che meraviglia, la nostra burocrazia. Ho chiesto un certificato – uno solo, un foglio – e in appena tre settimane, quattro code e due moduli «sbagliati» ce l'ho fatta. "
          "L'impiegata, di una cortesia commovente, mi ha spiegato senza alzare gli occhi dal telefono che il modulo giusto era «ovviamente» quello blu. "
          "Ovviamente. Torno a casa felice: il prossimo anno, si sa, la procedura sarà tutta digitale… come ci dicono dal 2005."),
  libero("e4", 4, "Il tuo testo ironico", "Scrivi un breve testo ironico (150 parole) su un'esperienza quotidiana: l'autobus, la fila alla posta, la riunione di condominio. Cura la punteggiatura.", ["Il testo"], rows=9),
]))

PAGINE = [("avanzato/%s.html" % k, d) for k, (lv, d) in P.items()]
ELENCO = [(k, lv, d) for k, (lv, d) in P.items()]
