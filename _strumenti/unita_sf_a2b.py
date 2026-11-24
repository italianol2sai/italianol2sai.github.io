"""Percorso A2, modulo 2 («Il passato») sulla traccia di «Nuovo Senza frontiere 2» (Edilingua): unità 5-8.
Testi, dialoghi, nomi e ascolti NUOVI (Erila, 2026-11-23: «rifaccio tutto con testi nuovi»). Stile "a2".
Uso: python3 _strumenti/unita_sf_a2b.py   (dalla cartella principale del sito)"""
import os, sys
sys.path.insert(0, os.path.dirname(__file__))
from genera import eq, build as build_es
from unita_primi import cover, slide, cards, table, nota, dialogo, end
from unita_drive import vf, scegli, menu, ordina, parla, libero
from teoria import tab, es
from unita_sf import scrivi, ascolto, testo, build_slide, build_giochi

# =====================================================================
# A2 · UNITÀ 5 · LA MIA STORIA
# =====================================================================
STORIA = [("F", "Mi chiamo Fatima, ho quarantadue anni e sono nata in Marocco, vicino a Marrakech."),
          ("F", "Per tanti anni ho lavorato in una sartoria: cucivo vestiti da sposa. Ho imparato il mestiere da mia zia."),
          ("F", "Un giorno ho deciso di partire: mio marito lavorava già a Bari da due anni."),
          ("F", "Sono arrivata in Italia nel duemiladiciotto. All'inizio sono rimasta a casa con i bambini."),
          ("F", "Poi ho fatto un corso di qualifica come assistente familiare e sono diventata assistente di una signora anziana."),
          ("F", "Adesso lavoro sei ore al giorno. Sono contenta: la signora Rosa è come una nonna per i miei figli.")]
STORIA_SLIDE = [
    cover("📖", "La mia storia", "Ho lasciato il mio Paese · Sono diventata assistente familiare", "A2 &bull; Modulo 2 &bull; Unità 1"),
    slide("In questa unità impari a…", cards([
        ("🧳", "Raccontare la tua storia", "Sono nato… ho lavorato… sono arrivato…"), ("🛠️", "Parlare dei lavori", "il sarto, il muratore, la badante"),
        ("⏳", "Dire quando", "per tanti anni, un giorno, prima… poi…"), ("🎓", "Conoscere i corsi di qualifica", "OSS, assistente familiare, cuoco")])),
    slide("🛠️ Mestieri e luoghi di lavoro", table([
        ["il sarto / la sarta", "la sartoria"], ["il falegname", "la falegnameria"], ["il muratore", "il cantiere"], ["la lavandaia / l'addetto", "la lavanderia"],
        ["l'assistente familiare", "la casa della persona anziana"], ["il cuoco / la cuoca", "la cucina del ristorante"], ["il bracciante", "i campi"]],
        head=["chi?", "dove?"])),
    slide("🧳 Lezione A · Ho lasciato il mio Paese", testo(*[t for _, t in STORIA[:3]])),
    slide("📘 Il passato prossimo con avere", table([
        ["-are → -ato", "lavorare → lavor<b>ato</b>", "<b>Ho lavorato</b> in una sartoria."], ["-ere → -uto", "ricevere → ricev<b>uto</b>", "<b>Ho ricevuto</b> il permesso."],
        ["-ire → -ito", "finire → fin<b>ito</b>", "<b>Abbiamo finito</b> il corso."]], head=["verbo", "participio", "esempio"]) + "\n" +
        nota("<b>ho, hai, ha, abbiamo, avete, hanno</b> + participio. Con <b>già, mai, ancora, appena</b>: Non ho <b>ancora</b> trovato casa. Ho <b>già</b> mangiato.")),
    slide("⏳ Le espressioni di tempo", cards([
        ("🔁", "per tanti anni", "una cosa lunga nel passato"), ("☝️", "un giorno", "un momento preciso"), ("1️⃣", "prima… poi…", "l'ordine dei fatti"),
        ("🚪", "all'inizio", "nei primi tempi"), ("🏁", "alla fine", "l'ultima cosa"), ("📅", "nel 2018", "l'anno")], "g3")),
    slide("👩‍🦳 Lezione B · Sono diventata assistente familiare", testo(*[t for _, t in STORIA[3:]])),
    slide("📘 Il passato prossimo con essere", table([
        ["io", "sono arrivat<b>o/a</b>"], ["tu", "sei arrivat<b>o/a</b>"], ["lui / lei", "è arrivat<b>o/a</b>"],
        ["noi", "siamo arrivat<b>i/e</b>"], ["voi", "siete arrivat<b>i/e</b>"], ["loro", "sono arrivat<b>i/e</b>"]], head=["", "arrivare"]) + "\n" +
        nota("Con <b>essere</b>: andare, venire, arrivare, partire, tornare, restare, rimanere, nascere, diventare, entrare, uscire. Il participio si accorda: Fatima è arrivat<b>a</b>.")),
    slide("🎓 Educazione civica · I corsi di qualifica professionale", cards([
        ("👩‍⚕️", "OSS", "operatore socio-sanitario: ospedali e RSA"), ("🏠", "assistente familiare", "aiuto agli anziani a casa"),
        ("🍳", "aiuto cuoco", "ristoranti e mense"), ("⚡", "elettricista, idraulico", "impianti nelle case"),
        ("📍", "dove informarsi", "Regione, Centro per l'impiego, enti di formazione"), ("💶", "quanto costa", "molti corsi sono gratuiti con l'attestato finale")], "g3")),
    end("Ora sai raccontare la tua storia!"),
]
A2STORIA = {
 "title": "📖 La mia storia · Esercizi", "store": "a2-la-mia-storia", "livello": "a2",
 "sections": [
  {"part": "Mestieri e luoghi di lavoro"},
  menu(["in sartoria", "in falegnameria", "in cantiere", "in lavanderia", "nei campi", "in cucina"],
       [("1. Il muratore lavora …", "in cantiere"), ("2. Il falegname lavora …", "in falegnameria"), ("3. La sarta lavora …", "in sartoria"),
        ("4. Il bracciante lavora …", "nei campi"), ("5. Il cuoco lavora …", "in cucina"), ("6. Chi lava e stira lavora …", "in lavanderia")],
       "1 · Dove lavorano?", "1 · I mestieri", "e1"),
  {"part": "Lezione A e B · La storia di Fatima"},
  ascolto(vf(["1. Fatima è nata in Marocco.", "2. In Marocco faceva la cuoca.", "3. Ha imparato il mestiere da sua zia.", "4. Il marito è arrivato in Italia dopo di lei.",
              "5. Ha fatto un corso per assistente familiare.", "6. Adesso lavora otto ore al giorno."],
             ["VERO", "FALSO", "VERO", "FALSO", "VERO", "FALSO"], "2 · 🎧 Ascolta la storia di Fatima: vero o falso?", "2 · Fatima", "e2"), [list(x) for x in STORIA]),
  {"part": "Il passato prossimo con avere", "teoria":
     tab(("-are", "-ato"), ("-ere", "-uto"), ("-ire", "-ito"), head=("verbo", "participio")) +
     "<b>avere</b> (ho, hai, ha, abbiamo, avete, hanno) + participio." + es("<b>Ho lavorato</b> per tanti anni. · <b>Abbiamo finito</b> il corso.")},
  scrivi([("1. (lavorare – io) … in una fabbrica di scarpe.", ("ho lavorato",)), ("2. (vendere – Fatima) … la sua macchina prima di partire.", ("ha venduto",)),
          ("3. (finire – noi) … il corso di italiano a giugno.", ("abbiamo finito",)), ("4. (ricevere – tu) … il permesso di soggiorno?", ("hai ricevuto",)),
          ("5. (aiutare – loro) … la signora Rosa con la spesa.", ("hanno aiutato",)), ("6. (dormire – voi) … bene in albergo?", ("avete dormito",))],
         "3 · Completa con il passato prossimo", "3 · Con avere", "e3", w="m"),
  scegli([("1. Non ho … trovato casa.", ["già", "ancora", "mai"], "ancora"), ("2. Hai … mangiato il cuscus?", ["mai", "ancora", "appena"], "mai"),
          ("3. Ho … finito: sono le 18:01!", ["appena", "mai", "ancora"], "appena"), ("4. Sì, ho … fatto i documenti, ieri.", ["già", "mai", "ancora"], "già")],
         "4 · già, mai, ancora, appena", "4 · Gli avverbi", "e4"),
  {"part": "Il passato prossimo con essere", "teoria":
     tab(("io / tu / lui / lei", "sono / sei / è + -o / -a"), ("noi / voi / loro", "siamo / siete / sono + -i / -e"), head=("persona", "")) +
     "Con i verbi di movimento e di cambiamento. Il participio si accorda come un aggettivo." + es("Fatima <b>è arrivata</b>. · I bambini <b>sono nati</b> a Bari.")},
  scrivi([("1. (arrivare – Fatima) … a Bari nel 2018.", ("è arrivata",)), ("2. (partire – i miei fratelli) … per la Germania.", ("sono partiti",)),
          ("3. (nascere – io, Michele) … in Albania.", ("sono nato",)), ("4. (diventare – Saleah) … mediatrice culturale.", ("è diventata",)),
          ("5. (rimanere – noi, Eneida e Silvia) … a casa tutto il giorno.", ("siamo rimaste",)), ("6. (tornare – tu, Cristian) Quando … dal lavoro?", ("sei tornato",))],
         "5 · Completa con essere", "5 · Con essere", "e5", w="m"),
  menu(["ho", "sono"],
       [("1. Ieri … andata dal medico.", "sono"), ("2. … mangiato una pizza.", "ho"), ("3. … nato nel 1990.", "sono"),
        ("4. … lavorato in un ristorante.", "ho"), ("5. … diventata nonna!", "sono"), ("6. … imparato l'italiano al CPIA.", "ho")],
       "6 · Ho o sono?", "6 · Ho / sono", "e6"),
  ordina(["Sono nato in Senegal.", "Per tanti anni ho fatto il pescatore.", "Un giorno ho deciso di partire.", "All'inizio sono rimasto a Roma.",
          "Poi mi sono trasferito a Bari.", "Alla fine ho trovato lavoro in un cantiere."], "7 · Metti in ordine la storia di Moussa", "7 · Moussa", "e7"),
  {"part": "Educazione civica · I corsi di qualifica"},
  vf(["1. L'OSS lavora negli ospedali e nelle RSA.", "2. Tutti i corsi di qualifica sono molto cari.", "3. Alla fine del corso si riceve un attestato.",
      "4. Il Centro per l'impiego dà informazioni sui corsi."], ["VERO", "FALSO", "VERO", "VERO"], "8 · I corsi: vero o falso?", "8 · I corsi", "e8"),
  libero("e9", 9, "La mia storia", "Racconta la tua storia in 6-8 frasi: dove sei nato/a, che lavoro facevi, quando sei partito/a, che cosa hai fatto in Italia.", ["La mia storia"], rows=7),
  parla("e10", 10, "Per parlare: conosci qualcuno che fa l'assistente familiare? Com'è questo lavoro? Ti piacerebbe farlo?"),
 ]
}

# =====================================================================
# A2 · UNITÀ 6 · RACCONTI
# =====================================================================
FURTO = [("F", "Silvia, sai che cosa mi è successo ieri al mercato?"), ("F", "No, che cosa?"),
         ("F", "Stavo pagando la frutta e un ragazzo mi ha preso il portafoglio dalla borsa!"), ("F", "Oh no! E che cosa hai fatto?"),
         ("F", "Ho gridato e un signore l'ha fermato. Poi sono arrivati i carabinieri."), ("F", "Meno male! Hai fatto la denuncia?"),
         ("F", "Sì, l'ho fatta subito. Ho ripreso il portafoglio, ma ho perso mezz'ora!")]
RAC_SLIDE = [
    cover("🗞️", "Racconti", "Che cosa è successo? · Hai saputo?", "A2 &bull; Modulo 2 &bull; Unità 2"),
    slide("In questa unità impari a…", cards([
        ("❓", "Chiedere che cosa è successo", "Che cosa ti è successo?"), ("📰", "Capire una notizia", "furto, scippo, truffa"),
        ("😮", "Reagire alle notizie", "Davvero? Che bello! Mi dispiace!"), ("✉️", "Scrivere biglietti e messaggi", "auguri, congratulazioni")])),
    slide("🦹 Furti, scippi e truffe", table([
        ["il borseggiatore", "ruba il portafoglio dalla borsa o dalla tasca"], ["lo scippatore", "strappa la borsa e scappa"],
        ["il truffatore", "ti inganna per avere soldi"], ["il ladro", "ruba in casa o nei negozi"]], head=["chi?", "che cosa fa?"])),
    slide("🛒 Lezione A · Che cosa è successo?", dialogo([("Eneida" if i % 2 == 0 else "*Silvia", t) for i, (_, t) in enumerate(FURTO)])),
    slide("📘 I participi irregolari", table([
        ["fare", "fatto"], ["prendere", "preso"], ["mettere", "messo"], ["dire", "detto"], ["leggere", "letto"], ["scrivere", "scritto"],
        ["vedere", "visto"], ["aprire", "aperto"], ["perdere", "perso"], ["chiedere", "chiesto"], ["rispondere", "risposto"], ["succedere", "successo"]],
        head=["verbo", "participio"])),
    slide("😮 Lezione B · Hai saputo?", dialogo([
        ("Giovanni", "Hai saputo di Cristian?"), ("*Saleah", "No, che cosa?"), ("Giovanni", "La settimana scorsa è diventato papà! È nata una bambina."),
        ("*Saleah", "Davvero? Che bella notizia! L'hai vista?"), ("Giovanni", "Sì, l'ho vista domenica. È bellissima."),
        ("*Saleah", "E il regalo? L'avete già comprato?"), ("Giovanni", "No, non l'abbiamo ancora comprato. Ci pensiamo insieme?")])),
    slide("📘 Pronomi diretti e passato prossimo", table([
        ["lo / la", "l'", "Il regalo? <b>L'ho</b> comprato. La bambina? <b>L'ho</b> vist<b>a</b>."], ["li", "li", "I documenti? <b>Li</b> ho portat<b>i</b>."],
        ["le", "le", "Le foto? <b>Le</b> ho mandat<b>e</b>."]], head=["pronome", "davanti a ho / hai…", "esempio"]) + "\n" +
        nota("Con lo, la, li, le il participio si accorda con il pronome.")),
    slide("📅 Le espressioni di tempo", cards([
        ("🌙", "ieri sera", ""), ("📆", "cinque giorni fa", ""), ("🗓️", "la settimana scorsa", ""), ("🎆", "l'anno scorso", ""),
        ("🕐", "due ore fa", ""), ("☀️", "stamattina", "")], "g3")),
    slide("👶 Educazione civica · La dichiarazione di nascita", cards([
        ("🏥", "in ospedale", "entro 3 giorni dalla nascita"), ("🏛️", "in Comune", "entro 10 giorni"),
        ("🪪", "chi la fa", "la mamma o il papà, con un documento"), ("📄", "che cosa serve", "l'attestazione di nascita dell'ospedale"),
        ("👨‍⚕️", "il pediatra", "dopo l'iscrizione al Servizio sanitario"), ("🆔", "il codice fiscale", "arriva con la registrazione")], "g3")),
    end("Ora sai raccontare un fatto e reagire alle notizie!"),
]
A2RAC = {
 "title": "🗞️ Racconti · Esercizi", "store": "a2-racconti", "livello": "a2",
 "sections": [
  {"part": "Le parole"},
  menu(["il borseggiatore", "lo scippatore", "il truffatore", "il ladro"],
       [("1. Mi ha strappato la borsa dalla spalla ed è scappato in motorino.", "lo scippatore"), ("2. Sul tram mi ha preso il telefono dalla tasca.", "il borseggiatore"),
        ("3. Mi ha telefonato e ha detto: «Sono della banca, mi dia il PIN».", "il truffatore"), ("4. È entrato in casa dalla finestra e ha preso la TV.", "il ladro")],
       "1 · Chi è?", "1 · Le parole", "e1"),
  {"part": "Lezione A · Che cosa è successo?"},
  ascolto(scegli([("1. Il fatto è successo…", ["al supermercato", "al mercato", "in autobus"], "al mercato"),
                  ("2. Il ragazzo ha preso…", ["la borsa", "il telefono", "il portafoglio"], "il portafoglio"),
                  ("3. Chi l'ha fermato?", ["un signore", "Silvia", "un carabiniere"], "un signore"),
                  ("4. Eneida…", ["non ha fatto la denuncia", "ha fatto la denuncia subito", "farà la denuncia domani"], "ha fatto la denuncia subito")],
                 "2 · 🎧 Ascolta Eneida e Silvia", "2 · Al mercato", "e2"), [list(x) for x in FURTO]),
  {"part": "I participi irregolari", "teoria":
     tab(("fare", "fatto"), ("prendere", "preso"), ("vedere", "visto"), ("perdere", "perso"), ("dire", "detto"), head=("verbo", "participio")) +
     "Molti verbi in <b>-ere</b> hanno il participio irregolare." + es("Ho <b>perso</b> il portafoglio. · Che cosa è <b>successo</b>?")},
  scrivi([("1. (perdere) Ho … le chiavi di casa.", ("perso",)), ("2. (vedere) Hai … il ladro?", ("visto",)), ("3. (fare) Abbiamo … la denuncia.", ("fatto",)),
          ("4. (prendere) Il borseggiatore ha … il telefono.", ("preso",)), ("5. (dire) Che cosa ha … il carabiniere?", ("detto",)),
          ("6. (scrivere) Ho … un messaggio alla polizia locale.", ("scritto",)), ("7. (rispondere) Nessuno ha … al telefono.", ("risposto",))],
         "3 · Scrivi il participio", "3 · Participi", "e3", w="s"),
  {"part": "Lezione B · Hai saputo?"},
  menu(["Che bello!", "Mi dispiace!", "Davvero?", "Meno male!", "Auguri!", "Che paura!"],
       [("1. È nata la mia bambina!", "Auguri!"), ("2. Mi hanno rubato la bici.", "Mi dispiace!"), ("3. Ho vinto 100 euro alla lotteria!", "Davvero?"),
        ("4. Ho perso il portafoglio, ma una signora me l'ha riportato.", "Meno male!"), ("5. Ho trovato un lavoro a tempo indeterminato!", "Che bello!"),
        ("6. Un cane enorme mi ha inseguito per strada!", "Che paura!")],
       "4 · Come reagisci?", "4 · Reagire", "e4"),
  {"part": "Pronomi diretti e passato prossimo", "teoria":
     tab(("lo / la + ho", "l'ho"), ("li + ho", "li ho"), ("le + ho", "le ho"), head=("pronome", "forma")) +
     "Il participio si accorda con il pronome." + es("La bambina? <b>L'ho vista</b>. · I documenti? <b>Li ho portati</b>.")},
  scrivi([("1. Il portafoglio? … ritrovato al bar.", ("l'ho",)), ("2. La notizia? … letta sul giornale.", ("l'ho",)),
          ("3. I biglietti? … comprati ieri.", ("li ho",)), ("4. Le foto della bambina? … mandate a tutti.", ("le ho",)),
          ("5. I carabinieri? … chiamati subito.", ("li ho",))],
         "5 · Completa con l'ho, li ho, le ho", "5 · l'ho, li ho…", "e5", w="s"),
  scegli([("1. La borsa? L'ho … al commissariato.", ["portato", "portata", "portati"], "portata"), ("2. I documenti? Li ho …", ["perso", "persa", "persi"], "persi"),
          ("3. Le chiavi? Le ho … nel cassetto.", ["messo", "messe", "messi"], "messe"), ("4. Il ladro? L'hanno …", ["preso", "presa", "prese"], "preso")],
         "6 · Scegli il participio giusto", "6 · L'accordo", "e6"),
  ordina(["cinque anni fa", "l'anno scorso", "il mese scorso", "la settimana scorsa", "ieri", "stamattina"],
         "7 · Dal più lontano al più vicino", "7 · Il tempo", "e7"),
  {"part": "Educazione civica · La dichiarazione di nascita"},
  vf(["1. La nascita si dichiara in ospedale entro 3 giorni.", "2. In Comune si può dichiarare entro 10 giorni.", "3. Solo il papà può fare la dichiarazione.",
      "4. Serve l'attestazione di nascita dell'ospedale."], ["VERO", "VERO", "FALSO", "VERO"], "8 · La dichiarazione di nascita: vero o falso?", "8 · La nascita", "e8"),
  libero("e9", 9, "Per scrivere: biglietti e messaggi", "Scrivi due brevi messaggi: 1) auguri a Cristian per la nascita della bambina; 2) a un'amica a cui hanno rubato la borsa.", ["Messaggio 1", "Messaggio 2"], rows=3),
  parla("e10", 10, "Ti è mai successo qualcosa di strano o di bello in Italia? Racconta."),
 ]
}

# =====================================================================
# A2 · UNITÀ 7 · COME ERAVAMO
# =====================================================================
RICORDI = [("M", "Quando ero bambino vivevo in un villaggio vicino a Kabul. La nostra casa era piccola, ma aveva un giardino con un albero di albicocche."),
           ("M", "Non avevamo la lavatrice: mia madre lavava i vestiti al fiume con le altre donne."),
           ("M", "Ogni mattina andavo a scuola a piedi con mio cugino. Ci volevano quaranta minuti."),
           ("M", "Il venerdì giocavamo a calcio con un pallone di stracci. Ero un bambino timido, ma in campo ero sempre allegro."),
           ("M", "La sera mio nonno raccontava storie e noi ascoltavamo in silenzio.")]
ERA_SLIDE = [
    cover("🕰️", "Come eravamo", "Mi ricordo · Che cosa facevi da piccolo?", "A2 &bull; Modulo 2 &bull; Unità 3"),
    slide("In questa unità impari a…", cards([
        ("🧠", "Parlare di ricordi", "Quando ero piccolo…"), ("🔁", "Descrivere abitudini del passato", "ogni mattina andavo…"),
        ("🙂", "Descrivere il carattere", "ero timido, allegro, vivace"), ("📅", "Dire le date e i numeri grandi", "il 12 marzo 1998")])),
    slide("🏠 Gli elettrodomestici", cards([
        ("🧊", "il frigorifero", ""), ("🧺", "la lavatrice", ""), ("🍽️", "la lavastoviglie", ""), ("🔥", "il forno", ""),
        ("⚖️", "la bilancia", ""), ("🌀", "l'aspirapolvere", ""), ("♨️", "il ferro da stiro", ""), ("📺", "il televisore", ""), ("❄️", "il condizionatore", "")], "g3")),
    slide("🧠 Lezione A · Mi ricordo", testo(*[t for _, t in RICORDI[:3]])),
    slide("📘 L'imperfetto (verbi regolari)", table([
        ["io", "gioc<b>avo</b>", "viv<b>evo</b>", "dorm<b>ivo</b>"], ["tu", "gioc<b>avi</b>", "viv<b>evi</b>", "dorm<b>ivi</b>"],
        ["lui / lei", "gioc<b>ava</b>", "viv<b>eva</b>", "dorm<b>iva</b>"], ["noi", "gioc<b>avamo</b>", "viv<b>evamo</b>", "dorm<b>ivamo</b>"],
        ["voi", "gioc<b>avate</b>", "viv<b>evate</b>", "dorm<b>ivate</b>"], ["loro", "gioc<b>avano</b>", "viv<b>evano</b>", "dorm<b>ivano</b>"]],
        head=["", "giocare", "vivere", "dormire"]) + "\n" +
        nota("Si usa per le <b>abitudini</b> (ogni giorno, di solito, il venerdì) e per le <b>descrizioni</b> (la casa era piccola, ero timido).")),
    slide("🔢 I numeri dal 100 in poi e le date", table([
        ["100", "cento"], ["200", "duecento"], ["1.000", "mille"], ["2.000", "duemila"], ["1998", "millenovecentonovantotto"], ["2018", "duemiladiciotto"]],
        head=["numero", "si scrive"]) + "\n" + nota("Le date: <b>il</b> 21 marzo 1998 · <b>il primo</b> maggio · Sono nato <b>nel</b> 1998.")),
    slide("⚽ Lezione B · Che cosa facevi da piccolo?", testo(*[t for _, t in RICORDI[3:]])),
    slide("📘 L'imperfetto (verbi irregolari)", table([
        ["essere", "ero, eri, era, eravamo, eravate, erano"], ["fare", "facevo, facevi, faceva, facevamo, facevate, facevano"],
        ["dire", "dicevo, dicevi, diceva…"], ["bere", "bevevo, bevevi, beveva…"]], head=["verbo", "imperfetto"])),
    slide("🌱 Educazione civica · Buone abitudini per un futuro migliore", cards([
        ("💡", "spegnere le luci", "quando esci da una stanza"), ("🚿", "risparmiare acqua", "la doccia invece del bagno"),
        ("♻️", "fare la raccolta differenziata", "carta, plastica, vetro, organico"), ("🛍️", "usare la borsa di stoffa", "meno plastica"),
        ("🚲", "camminare o usare la bici", "meno traffico e smog"), ("🍞", "non sprecare il cibo", "come facevano i nonni")], "g3")),
    end("Ora sai raccontare i tuoi ricordi!"),
]
A2ERA = {
 "title": "🕰️ Come eravamo · Esercizi", "store": "a2-come-eravamo", "livello": "a2",
 "sections": [
  {"part": "Gli elettrodomestici"},
  menu(["il frigorifero", "la lavatrice", "il forno", "la bilancia", "l'aspirapolvere", "il ferro da stiro"],
       [("1. Tiene il cibo al freddo.", "il frigorifero"), ("2. Lava i vestiti.", "la lavatrice"), ("3. Cuoce il pane e la pizza.", "il forno"),
        ("4. Pesa la farina.", "la bilancia"), ("5. Pulisce il pavimento.", "l'aspirapolvere"), ("6. Toglie le pieghe dalla camicia.", "il ferro da stiro")],
       "1 · Che cos'è?", "1 · Elettrodomestici", "e1"),
  {"part": "Lezione A e B · I ricordi di Ahmad"},
  ascolto(vf(["1. Ahmad viveva in una grande città.", "2. Nel giardino c'era un albero di albicocche.", "3. La madre lavava i vestiti con la lavatrice.",
              "4. Andava a scuola a piedi.", "5. Il venerdì giocavano a calcio.", "6. Ahmad era un bambino molto timido anche in campo."],
             ["FALSO", "VERO", "FALSO", "VERO", "VERO", "FALSO"], "2 · 🎧 Ascolta i ricordi di Ahmad: vero o falso?", "2 · Ahmad", "e2"), [list(x) for x in RICORDI]),
  {"part": "L'imperfetto dei verbi regolari", "teoria":
     tab(("-are", "-avo, -avi, -ava, -avamo, -avate, -avano"), ("-ere", "-evo, -evi, -eva…"), ("-ire", "-ivo, -ivi, -iva…"), head=("verbo", "imperfetto")) +
     "Per abitudini e descrizioni del passato." + es("Da bambino <b>giocavo</b> sempre in cortile.")},
  scrivi([("1. (abitare – io) Da piccola … in un villaggio.", ("abitavo",)), ("2. (lavorare – mio padre) … nei campi.", ("lavorava",)),
          ("3. (giocare – noi) … a nascondino.", ("giocavamo",)), ("4. (dormire – i bambini) … tutti nella stessa stanza.", ("dormivano",)),
          ("5. (leggere – tu) … i fumetti?", ("leggevi",)), ("6. (vivere – voi) … vicino al mare?", ("vivevate",))],
         "3 · Completa con l'imperfetto", "3 · Imperfetto regolare", "e3", w="m"),
  {"part": "L'imperfetto dei verbi irregolari", "teoria":
     tab(("essere", "ero, eri, era, eravamo, eravate, erano"), ("fare", "facevo, facevi, faceva…"), ("bere", "bevevo…"), ("dire", "dicevo…"), head=("verbo", "imperfetto")) +
     es("<b>Ero</b> un bambino vivace. · Che cosa <b>facevi</b> il sabato?")},
  scrivi([("1. (essere – io) … molto timida.", ("ero",)), ("2. (fare – mia nonna) … il pane in casa.", ("faceva",)),
          ("3. (bere – noi) … il tè con la menta.", ("bevevamo",)), ("4. (essere – i miei fratelli) … sempre allegri.", ("erano",)),
          ("5. (dire – il maestro) … sempre: «Studiate!»", ("diceva",)), ("6. (fare – voi) Che cosa … il fine settimana?", ("facevate",))],
         "4 · Completa con l'imperfetto irregolare", "4 · Imperfetto irregolare", "e4", w="m"),
  menu(["timido", "allegro", "vivace", "tranquillo", "testardo", "generoso"],
       [("1. Non parlava mai con le persone nuove: era …", "timido"), ("2. Rideva sempre: era …", "allegro"),
        ("3. Non stava mai fermo: era …", "vivace"), ("4. Dava sempre i suoi giochi agli altri: era …", "generoso"),
        ("5. Non cambiava mai idea: era …", "testardo"), ("6. Non si arrabbiava mai: era …", "tranquillo")],
       "5 · Com'era da bambino?", "5 · Il carattere", "e5"),
  scrivi([("1. 300 = …", ("trecento",)), ("2. 1.000 = …", ("mille",)), ("3. 2026 = …", ("duemilaventisei",)),
          ("4. 1990 = …", ("millenovecentonovanta",)), ("5. 450 = …", ("quattrocentocinquanta",))],
         "6 · Scrivi i numeri in lettere", "6 · I numeri", "e6", w="l"),
  {"part": "Educazione civica · Le buone abitudini"},
  vf(["1. È meglio spegnere le luci quando esci da una stanza.", "2. Il bagno nella vasca consuma meno acqua della doccia.", "3. La borsa di stoffa riduce la plastica.",
      "4. Non bisogna sprecare il cibo."], ["VERO", "FALSO", "VERO", "VERO"], "7 · Buone abitudini: vero o falso?", "7 · Abitudini", "e7"),
  libero("e8", 8, "Per parlare: i cibi e i ricordi", "Scrivi un piatto della tua infanzia: chi lo cucinava? Quando lo mangiavate? Com'era?", ["Il mio piatto"], rows=5),
  parla("e9", 9, "Che cosa facevi da piccolo/a? Con chi giocavi? Com'era la tua casa?"),
 ]
}

# =====================================================================
# A2 · UNITÀ 8 · CAMBIARE VITA
# =====================================================================
PARTENZA = [("M", "Volevo partire già a vent'anni, ma non potevo: mio padre era malato e dovevo aiutare la famiglia."),
            ("M", "Nel duemilaventi ho potuto finalmente partire. Sono dovuto passare dalla Libia: è stato il periodo più difficile della mia vita."),
            ("M", "Quando sono arrivato in Sicilia, ero stanchissimo. Non conoscevo nessuno e non parlavo italiano."),
            ("M", "Mi hanno mandato in un centro SAI a Bari. Lì ho conosciuto Michele, l'operatore: mi ha aiutato tanto."),
            ("M", "Adesso faccio il pizzaiolo e ho una casa in affitto. Ho cambiato vita, ma non dimentico da dove vengo.")]
CAMB_SLIDE = [
    cover("🧭", "Cambiare vita", "La partenza · L'arrivo · Una nuova vita", "A2 &bull; Modulo 2 &bull; Unità 4"),
    slide("In questa unità impari a…", cards([
        ("🧳", "Raccontare un viaggio difficile", "Ho dovuto… non potevo…"), ("💭", "Dare la tua opinione", "Secondo me… Per me…"),
        ("🤝", "Essere d'accordo o no", "Sono d'accordo · Non sono d'accordo"), ("✍️", "Scrivere la tua storia", "passato prossimo e imperfetto")])),
    slide("🌍 Le parole della migrazione", table([
        ["emigrare / l'emigrante", "lasciare il proprio Paese"], ["immigrare / l'immigrato", "arrivare in un altro Paese"],
        ["il confine", "la linea tra due Paesi"], ["la richiesta di asilo", "domanda di protezione"], ["l'accoglienza", "il primo aiuto dopo l'arrivo"],
        ["l'integrazione", "diventare parte della nuova società"]], head=["parola", "significato"])),
    slide("🧳 Lezione A · La partenza", testo(*[t for _, t in PARTENZA[:2]])),
    slide("📘 Passato prossimo dei verbi modali", table([
        ["volere, potere, dovere + verbo con avere", "Ho <b>dovuto</b> lavorare. Ho <b>potuto</b> studiare."],
        ["volere, potere, dovere + verbo con essere", "Sono <b>dovuto</b> partire. Sono <b>potuta</b> tornare."]], head=["regola", "esempio"]) + "\n" +
        nota("Il modale prende l'ausiliare del verbo che segue: partire → <b>sono</b> partito → <b>sono</b> dovuto partire.")),
    slide("💭 Opinioni, accordo e disaccordo", cards([
        ("💬", "Secondo me… / Per me…", "dare un'opinione"), ("🤔", "Penso che sia difficile.", "un'opinione più forte"),
        ("👍", "Sono d'accordo. Hai ragione.", "accordo"), ("👎", "Non sono d'accordo. Non è vero.", "disaccordo")], "g2")),
    slide("🏁 Lezione B · L'arrivo", testo(*[t for _, t in PARTENZA[2:]])),
    slide("📘 Passato prossimo o imperfetto?", table([
        ["un fatto, una volta", "passato prossimo", "<b>Sono arrivato</b> in Sicilia."], ["com'era la situazione", "imperfetto", "<b>Ero</b> stanchissimo."],
        ["un'abitudine", "imperfetto", "Ogni sera <b>chiamavo</b> mia madre."], ["un fatto concluso con durata", "passato prossimo", "<b>Ho lavorato</b> due anni in Libia."]],
        head=["quando", "tempo", "esempio"])),
    slide("🏠 Educazione civica · Cominciare una nuova vita", cards([
        ("🏛️", "il SAI", "Sistema di Accoglienza e Integrazione: casa, corsi, orientamento"), ("🧑‍💼", "l'operatore", "aiuta con documenti, lavoro, salute"),
        ("📚", "il CPIA", "corsi di italiano per adulti, con una piccola quota di iscrizione"), ("💼", "il Centro per l'impiego", "offerte di lavoro e corsi"),
        ("🩺", "la tessera sanitaria", "per il medico di base"), ("🤲", "le associazioni", "volontari, sportelli, consulenze")], "g3")),
    end("Ora sai raccontare un cambiamento di vita!"),
]
A2CAMB = {
 "title": "🧭 Cambiare vita · Esercizi", "store": "a2-cambiare-vita", "livello": "a2",
 "sections": [
  {"part": "Le parole"},
  menu(["emigrare", "il confine", "l'accoglienza", "l'integrazione", "la richiesta di asilo"],
       [("1. Lasciare il proprio Paese per vivere in un altro.", "emigrare"), ("2. La linea tra due Stati.", "il confine"),
        ("3. Il primo aiuto quando arrivi: casa, cibo, documenti.", "l'accoglienza"), ("4. La domanda di protezione.", "la richiesta di asilo"),
        ("5. Diventare parte della nuova società.", "l'integrazione")],
       "1 · Che cos'è?", "1 · Le parole", "e1"),
  {"part": "Lezione A e B · La storia di Yaya"},
  ascolto(scegli([("1. A vent'anni Yaya non poteva partire perché…", ["non aveva soldi", "il padre era malato", "studiava"], "il padre era malato"),
                  ("2. È partito nel…", ["2018", "2020", "2022"], "2020"),
                  ("3. In Sicilia…", ["conosceva molte persone", "non conosceva nessuno", "parlava già italiano"], "non conosceva nessuno"),
                  ("4. Michele è…", ["un operatore del SAI", "un pizzaiolo", "suo cugino"], "un operatore del SAI"),
                  ("5. Adesso Yaya fa…", ["il muratore", "il pizzaiolo", "il cameriere"], "il pizzaiolo")],
                 "2 · 🎧 Ascolta la storia di Yaya", "2 · Yaya", "e2"), [list(x) for x in PARTENZA]),
  {"part": "Il passato prossimo dei verbi modali", "teoria":
     tab(("+ verbo con avere", "ho dovuto / potuto / voluto + infinito"), ("+ verbo con essere", "sono dovuto/a / potuto/a / voluto/a + infinito"), head=("", "forma")) +
     "Il modale prende l'ausiliare del verbo che segue." + es("<b>Ho dovuto</b> lavorare. · <b>Sono dovuto</b> partire.")},
  menu(["ho", "sono"],
       [("1. … dovuto lasciare il mio Paese.", "ho"), ("2. … potuto partire solo nel 2020.", "sono"), ("3. … voluto studiare l'italiano.", "ho"),
        ("4. Saleah … dovuta tornare a casa presto.", "è"), ("5. Non … potuto chiamare la mia famiglia.", "ho"), ("6. … voluta restare a Bari.", "sono")],
       "3 · Ho, sono o è?", "3 · I modali", "e3") | {"opts": ["ho", "sono", "è"]},
  {"part": "Passato prossimo o imperfetto?", "teoria":
     tab(("fatto concluso", "passato prossimo"), ("descrizione, stato, abitudine", "imperfetto"), head=("situazione", "tempo")) +
     es("Quando <b>sono arrivato</b>, <b>ero</b> stanchissimo.")},
  scegli([("1. Quando … a Bari, pioveva.", ["arrivavo", "sono arrivato"], "sono arrivato"), ("2. All'inizio non … nessuno.", ["conoscevo", "ho conosciuto"], "conoscevo"),
          ("3. Il primo giorno … Michele.", ["conoscevo", "ho conosciuto"], "ho conosciuto"), ("4. Ogni sera … mia madre.", ["chiamavo", "ho chiamato"], "chiamavo"),
          ("5. … due anni in Libia.", ["Lavoravo", "Ho lavorato"], "Ho lavorato"), ("6. Il centro … grande e pulito.", ["era", "è stato"], "era")],
         "4 · Scegli il tempo giusto", "4 · Pass. prossimo / imperfetto", "e4"),
  menu(["accordo", "disaccordo", "opinione"],
       [("1. Secondo me, imparare la lingua è la cosa più importante.", "opinione"), ("2. Hai ragione, è proprio così.", "accordo"),
        ("3. Non sono d'accordo: il lavoro è più importante.", "disaccordo"), ("4. Per me, Bari è una città accogliente.", "opinione"),
        ("5. Sì, sono d'accordo con te.", "accordo"), ("6. Non è vero, non è facile per niente!", "disaccordo")],
       "5 · Accordo, disaccordo o opinione?", "5 · Opinioni", "e5"),
  {"part": "Educazione civica · Una nuova vita"},
  menu(["il SAI", "il CPIA", "il Centro per l'impiego", "la tessera sanitaria", "le associazioni"],
       [("1. Voglio un corso di italiano per adulti: vado al …", "il CPIA"), ("2. Cerco lavoro e corsi di formazione: vado al …", "il Centro per l'impiego"),
        ("3. Mi serve per scegliere il medico di base: …", "la tessera sanitaria"), ("4. Casa e orientamento per chi ha protezione: …", "il SAI"),
        ("5. Volontari e sportelli gratuiti: …", "le associazioni")],
       "6 · Dove vado?", "6 · I servizi", "e6"),
  libero("e7", 7, "Per scrivere: la mia storia", "Scrivi la tua storia: perché e quando sei partito/a, com'era il viaggio, com'è stato l'arrivo, com'è la tua vita adesso.", ["La mia storia"], rows=8),
  parla("e8", 8, "Secondo te, che cosa è più difficile quando cambi vita? Sei d'accordo con Yaya: «non dimentico da dove vengo»?"),
 ]
}

SLIDE = [("a2-la-mia-storia/index.html", "La mia storia", "A2", STORIA_SLIDE, "a2"),
         ("a2-racconti/index.html", "Racconti", "A2", RAC_SLIDE, "a2"),
         ("a2-come-eravamo/index.html", "Come eravamo", "A2", ERA_SLIDE, "a2"),
         ("a2-cambiare-vita/index.html", "Cambiare vita", "A2", CAMB_SLIDE, "a2")]
ESERCIZI = [("a2-la-mia-storia", A2STORIA), ("a2-racconti", A2RAC), ("a2-come-eravamo", A2ERA), ("a2-cambiare-vita", A2CAMB)]
GIOCHI = {
 "a2-la-mia-storia": ("a2-vivere-insieme", "A2", "📖 GIOCHI: LA MIA STORIA (A2)", [
  ["IL SARTO", "🧵", "CUCE I VESTITI"], ["IL FALEGNAME", "🪚", "LAVORA IL LEGNO"], ["IL MURATORE", "🧱", "LAVORA IN CANTIERE"], ["LA SARTORIA", "👗", "IL NEGOZIO DEL SARTO"],
  ["IL CANTIERE", "🏗️", "QUI SI COSTRUISCONO LE CASE"], ["LA LAVANDERIA", "🧺", "QUI SI LAVANO I VESTITI"], ["IL BRACCIANTE", "🌾", "LAVORA NEI CAMPI"], ["IL CUOCO", "👨‍🍳", "LAVORA IN CUCINA"],
  ["LA BADANTE", "👵", "AIUTA GLI ANZIANI A CASA"], ["IL CORSO", "🎓", "SI FA PER IMPARARE UN MESTIERE"], ["L'ATTESTATO", "📜", "SI RICEVE ALLA FINE DEL CORSO"], ["PARTIRE", "🧳", "LASCIARE UN POSTO"],
  ["ARRIVARE", "🛬", "SONO … IN ITALIA NEL 2018"], ["NASCERE", "👶", "SONO … IN MAROCCO"], ["DIVENTARE", "🦋", "SONO … ASSISTENTE"], ["IL MESTIERE", "🛠️", "IL LAVORO CHE SAI FARE"],
  ["ALL'INIZIO", "🚪", "NEI PRIMI TEMPI"], ["UN GIORNO", "☝️", "UN MOMENTO PRECISO DEL PASSATO"]]),
 "a2-racconti": ("a2-vivere-insieme", "A2", "🗞️ GIOCHI: RACCONTI (A2)", [
  ["IL BORSEGGIATORE", "👛", "RUBA DALLA TASCA"], ["LO SCIPPATORE", "🛵", "STRAPPA LA BORSA E SCAPPA"], ["IL TRUFFATORE", "🎣", "TI INGANNA PER I SOLDI"], ["IL LADRO", "🦹", "RUBA IN CASA"],
  ["LA DENUNCIA", "📝", "SI FA DAI CARABINIERI"], ["IL PORTAFOGLIO", "💳", "QUI TENGO I SOLDI"], ["LA NOTIZIA", "📰", "HAI SAPUTO LA …?"], ["AUGURI", "🎉", "LO DICI PER UNA NASCITA"],
  ["DAVVERO", "😮", "LO DICI QUANDO SEI SORPRESO"], ["MENO MALE", "😅", "LO DICI QUANDO FINISCE BENE"], ["IERI SERA", "🌙", "IL GIORNO PRIMA, DI SERA"], ["L'ANNO SCORSO", "🎆", "DODICI MESI FA"],
  ["FATTO", "✅", "PARTICIPIO DI FARE"], ["PRESO", "✋", "PARTICIPIO DI PRENDERE"], ["VISTO", "👀", "PARTICIPIO DI VEDERE"], ["PERSO", "🔍", "PARTICIPIO DI PERDERE"],
  ["DETTO", "🗣️", "PARTICIPIO DI DIRE"], ["LA NASCITA", "👶", "SI DICHIARA IN COMUNE"]]),
 "a2-come-eravamo": ("a2-vivere-insieme", "A2", "🕰️ GIOCHI: COME ERAVAMO (A2)", [
  ["IL FRIGORIFERO", "🧊", "TIENE IL CIBO FREDDO"], ["LA LAVATRICE", "🧺", "LAVA I VESTITI"], ["IL FORNO", "🔥", "CUOCE IL PANE"], ["LA BILANCIA", "⚖️", "PESA LA FARINA"],
  ["IL FERRO DA STIRO", "♨️", "TOGLIE LE PIEGHE"], ["L'ASPIRAPOLVERE", "🌀", "PULISCE IL PAVIMENTO"], ["IL TELEVISORE", "📺", "QUI GUARDO I FILM"], ["IL RICORDO", "🧠", "UNA COSA CHE NON DIMENTICO"],
  ["DA BAMBINO", "🧒", "QUANDO ERO PICCOLO"], ["OGNI GIORNO", "🔁", "TUTTI I GIORNI"], ["TIMIDO", "🙈", "NON PARLA CON LE PERSONE NUOVE"], ["ALLEGRO", "😄", "RIDE SEMPRE"],
  ["VIVACE", "🤸", "NON STA MAI FERMO"], ["GENEROSO", "🎁", "DÀ AGLI ALTRI"], ["MILLE", "🔢", "1000"], ["CENTO", "💯", "100"],
  ["ERO", "🕰️", "IMPERFETTO DI ESSERE (IO)"], ["FACEVO", "🛠️", "IMPERFETTO DI FARE (IO)"]]),
 "a2-cambiare-vita": ("a2-vivere-insieme", "A2", "🧭 GIOCHI: CAMBIARE VITA (A2)", [
  ["EMIGRARE", "🧳", "LASCIARE IL PROPRIO PAESE"], ["IL CONFINE", "🚧", "LINEA TRA DUE PAESI"], ["L'ACCOGLIENZA", "🤲", "IL PRIMO AIUTO"], ["L'INTEGRAZIONE", "🧩", "DIVENTARE PARTE DELLA SOCIETÀ"],
  ["L'ASILO", "🛡️", "LA PROTEZIONE CHE SI CHIEDE"], ["IL VIAGGIO", "🚢", "DA UN PAESE A UN ALTRO"], ["LA PARTENZA", "🛫", "IL MOMENTO IN CUI PARTI"], ["L'ARRIVO", "🛬", "IL MOMENTO IN CUI ARRIVI"],
  ["IL SAI", "🏛️", "SISTEMA DI ACCOGLIENZA E INTEGRAZIONE"], ["IL CPIA", "📚", "CORSI DI ITALIANO PER ADULTI"], ["L'OPERATORE", "🧑‍💼", "AIUTA NEL CENTRO"], ["LA NOSTALGIA", "💭", "MANCA LA CASA LONTANA"],
  ["IL PIZZAIOLO", "🍕", "FA LE PIZZE"], ["L'AFFITTO", "🏠", "SI PAGA OGNI MESE PER LA CASA"], ["DOVUTO", "📌", "HO … LAVORARE"], ["POTUTO", "✅", "NON HO … PARTIRE"],
  ["D'ACCORDO", "👍", "SONO … CON TE"], ["SECONDO ME", "💬", "PER DARE UN'OPINIONE"]]),
}

if __name__ == "__main__":
    for path, unit, top, sl, liv in SLIDE:
        os.makedirs(os.path.dirname(path), exist_ok=True)
        build_slide(path, unit, top, sl, liv)
    for cartella, dati in ESERCIZI:
        build_es(cartella + "/esercizi.html", dati)
    build_giochi(GIOCHI)
