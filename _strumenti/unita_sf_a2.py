"""Percorso A2 sulla traccia degli argomenti di «Nuovo Senza frontiere 2» (Edilingua): unità 2-4 del modulo 1.
Testi, dialoghi, nomi e ascolti NUOVI (Erila, 2026-11-23: «rifaccio tutto con testi nuovi»): si tengono argomenti, grammatica e tipi
di esercizio. Ambientazione: Bari. Stile del livello: "a2" (Nunito, minuscolo).
Uso: python3 _strumenti/unita_sf_a2.py   (dalla cartella principale del sito)"""
import os, sys
sys.path.insert(0, os.path.dirname(__file__))
from genera import eq, build as build_es
from unita_primi import cover, slide, cards, table, nota, dialogo, end
from unita_drive import ill, vf, scegli, menu, ordina, parla, libero
from teoria import tab, es
from unita_sf import scrivi, ascolto, build_slide, build_giochi

# =====================================================================
# A2 · UNITÀ 2 · LA CONVIVENZA
# =====================================================================
CONV_DIAL = [("Eneida", "Ciao! Tu sei la nuova vicina del terzo piano, vero? Io sono Eneida."),
             ("Rokia", "Sì, piacere, sono Rokia. Vengo dalla Costa d'Avorio, sono ivoriana. E tu?"),
             ("Eneida", "Io sono albanese, di Durazzo, ma abito a Bari da sei anni."),
             ("Rokia", "Senti, a che ora si porta giù la spazzatura qui?"),
             ("Eneida", "La sera, dopo le otto. Di solito io la porto giù quando torno dal lavoro."),
             ("Rokia", "E il bucato? Posso stenderlo sul balcone?"),
             ("Eneida", "Sì, ma attenta a non bagnare i panni della signora di sotto! Lei è molto gentile, ma su questo è severa."),
             ("Rokia", "Grazie, sei proprio gentile. Se ti serve qualcosa, conta su di me!")]
CONV_SLIDE = [
    cover("🏘️", "La convivenza", "I vicini · Le abitudini · Le regole", "A2 &bull; Modulo 1 &bull; Unità 2"),
    slide("In questa unità impari a…", cards([
        ("🌍", "Dire da dove vieni", "Vengo dal Senegal, sono senegalese"), ("🔁", "Parlare delle abitudini", "di solito, spesso, regolarmente"),
        ("🚫", "Capire le regole", "È vietato fumare · Si prega di…"), ("🪧", "Leggere segnali e cartelli", "in condominio, a scuola, in strada")])),
    slide("🌍 Paesi e nazionalità", table([
        ["il Marocco", "marocchino / marocchina"], ["il Senegal", "senegalese"], ["l'Albania", "albanese"], ["la Nigeria", "nigeriano / nigeriana"],
        ["l'Ucraina", "ucraino / ucraina"], ["la Costa d'Avorio", "ivoriano / ivoriana"], ["il Pakistan", "pakistano / pakistana"],
        ["il Bangladesh", "bengalese"], ["la Tunisia", "tunisino / tunisina"]], head=["vengo da…", "sono…"]) + "\n" +
        nota("Vengo <b>dal</b> Marocco · <b>dalla</b> Tunisia · <b>dall'</b>Albania · <b>dagli</b> Stati Uniti. Sono di Casablanca.")),
    slide("🏢 Lezione A · Le abitudini", dialogo([("*" + a if i % 2 else a, b) for i, (a, b) in enumerate(CONV_DIAL)])),
    slide("📘 Gli avverbi in -mente", table([
        ["tranquillo → tranquilla", "tranquillamente"], ["regolare", "regolarmente"], ["gentile", "gentilmente"],
        ["veloce", "velocemente"], ["facile", "facilmente"], ["raro → rara", "raramente"]], head=["aggettivo", "avverbio"]) + "\n" +
        nota("Aggettivo in <b>-o</b>: prendi il femminile <b>-a</b> + <b>mente</b>. In <b>-le / -re</b>: togli la <b>-e</b> + <b>mente</b>.")),
    slide("📘 I pronomi dopo le preposizioni", table([
        ["io", "me", "Vieni con <b>me</b>?"], ["tu", "te", "Questo è per <b>te</b>."], ["lui / lei", "lui / lei", "Abito vicino a <b>lei</b>."],
        ["Lei (formale)", "Lei", "Signora, conto su di <b>Lei</b>."], ["noi", "noi", "Venite da <b>noi</b> stasera?"],
        ["voi", "voi", "Parlo con <b>voi</b>."], ["loro", "loro", "Non vado senza di <b>loro</b>."]], head=["soggetto", "dopo con, per, da, a…", "esempio"])),
    slide("🚫 Lezione B · Le regole del condominio", '    <div class="testo"><p><b>Regolamento del condominio di via Dalmazia 12</b></p>'
          "<p>È vietato fare rumore dalle 14 alle 16 e dalle 22 alle 8.</p><p>È vietato lasciare biciclette e passeggini nell'androne.</p>"
          "<p>La spazzatura si porta nei bidoni del cortile, divisa per tipo.</p><p>I cani devono stare al guinzaglio nelle scale e nel cortile.</p>"
          "<p>Si prega di chiudere sempre il portone.</p></div>"),
    slide("📘 Le preposizioni articolate", table([
        ["a", "al", "allo", "all'", "alla", "ai", "agli", "alle"], ["di", "del", "dello", "dell'", "della", "dei", "degli", "delle"],
        ["da", "dal", "dallo", "dall'", "dalla", "dai", "dagli", "dalle"], ["in", "nel", "nello", "nell'", "nella", "nei", "negli", "nelle"],
        ["su", "sul", "sullo", "sull'", "sulla", "sui", "sugli", "sulle"]], head=["", "il", "lo", "l'", "la", "i", "gli", "le"]) + "\n" +
        nota("La spazzatura va <b>nei</b> bidoni · Le bici non stanno <b>nell'</b>androne · Il bucato è <b>sul</b> balcone.")),
    slide("🪧 Educazione civica · Segnali e cartelli", cards([
        ("🚭", "Vietato fumare", "in tutti i luoghi pubblici chiusi"), ("🚷", "Vietato l'accesso", "non si può entrare"),
        ("🐕", "Cani al guinzaglio", "nei parchi e nei condomini"), ("🤫", "Silenzio", "ospedali, biblioteche"),
        ("♻️", "Raccolta differenziata", "carta, plastica, vetro, organico"), ("🚸", "Attenzione bambini", "vicino alle scuole")], "g3")),
    end("Ora conosci le regole per vivere bene insieme!"),
]
A2CONV = {
 "title": "🏘️ La convivenza · Esercizi", "store": "a2-la-convivenza", "livello": "a2",
 "sections": [
  {"part": "Paesi e nazionalità"},
  scrivi([("1. Karim viene dal Marocco: è …", ("marocchino",)), ("2. Olena viene dall'Ucraina: è …", ("ucraina",)),
          ("3. Moussa viene dal Senegal: è …", ("senegalese",)), ("4. Blessing viene dalla Nigeria: è …", ("nigeriana",)),
          ("5. Amir viene dal Pakistan: è …", ("pakistano",)), ("6. Ines viene dalla Tunisia: è …", ("tunisina",))],
         "1 · Di che nazionalità è?", "1 · Nazionalità", "e1", w="m"),
  menu(["dal", "dalla", "dall'", "dagli"],
       [("1. Rokia viene … Costa d'Avorio.", "dalla"), ("2. Eneida viene … Albania.", "dall'"), ("3. Jamal viene … Bangladesh.", "dal"),
        ("4. Grace viene … Stati Uniti.", "dagli"), ("5. Yusuf viene … Egitto.", "dall'"), ("6. Mariam viene … Somalia.", "dalla")],
       "2 · Vengo da…", "2 · Vengo da", "e2"),
  {"part": "Lezione A · Le abitudini"},
  ascolto(vf(["1. Rokia abita al terzo piano.", "2. Eneida è di Durazzo.", "3. Eneida abita a Bari da due anni.",
              "4. La spazzatura si porta giù la mattina.", "5. Rokia può stendere il bucato sul balcone.", "6. La vicina di sotto è severa sul bucato."],
             ["VERO", "VERO", "FALSO", "FALSO", "VERO", "VERO"], "3 · 🎧 Ascolta le vicine: vero o falso?", "3 · Le vicine", "e3"),
          [["F", b] for _, b in CONV_DIAL]),
  {"part": "Gli avverbi in -mente", "teoria":
     tab(("tranquillo", "tranquillamente"), ("gentile", "gentilmente"), ("regolare", "regolarmente"), head=("aggettivo", "avverbio")) +
     "Aggettivo in -o → femminile in <b>-a</b> + mente. Aggettivo in -le o -re → togli la <b>-e</b> + mente." + es("Parla <b>lentamente</b>, per favore.")},
  scrivi([("1. (lento) Il signor Russo cammina …", ("lentamente",)), ("2. (regolare) Pago l'affitto …", ("regolarmente",)),
          ("3. (gentile) La portinaia risponde sempre …", ("gentilmente",)), ("4. (veloce) Michele sale le scale …", ("velocemente",)),
          ("5. (raro) Nel nostro palazzo ci sono … problemi: quasi mai.", ("raramente",)), ("6. (facile) Con il navigatore trovo … la strada.", ("facilmente",))],
         "4 · Scrivi l'avverbio", "4 · Avverbi in -mente", "e4", w="m"),
  {"part": "I pronomi dopo le preposizioni", "teoria":
     tab(("io", "me"), ("tu", "te"), ("lui / lei / Lei", "lui / lei / Lei"), ("noi / voi / loro", "noi / voi / loro"), head=("soggetto", "dopo la preposizione")) +
     "Dopo <b>con, per, da, a, di, senza, vicino a…</b> usiamo questi pronomi." + es("Vieni con <b>me</b>? · Questo regalo è per <b>te</b>.")},
  scegli([("1. Rokia, vieni al mercato con …?", ["io", "me", "mi"], "me"), ("2. Eneida, questo dolce è per …!", ["te", "tu", "ti"], "te"),
          ("3. La signora di sotto è gentile: abito vicino a …", ["la", "lei", "le"], "lei"), ("4. Ragazzi, stasera venite da …?", ["noi", "ci", "nostri"], "noi"),
          ("5. Signor Russo, conto su di …", ["La", "Lei", "Le"], "Lei"), ("6. I bambini sono al parco: non parto senza di …", ["li", "gli", "loro"], "loro")],
         "5 · Scegli il pronome", "5 · me, te, lei…", "e5"),
  {"part": "Lezione B · Le regole"},
  vf(["1. Alle 15 posso usare il trapano.", "2. Lascio la bicicletta nell'androne.", "3. La spazzatura va nei bidoni del cortile.",
      "4. Il cane può stare libero sulle scale.", "5. Bisogna chiudere il portone."],
     ["FALSO", "FALSO", "VERO", "FALSO", "VERO"], "6 · Leggi il regolamento: vero o falso?", "6 · Il regolamento", "e6",
     info="<b>Regolamento del condominio</b><br>È vietato fare rumore dalle 14 alle 16 e dalle 22 alle 8. · È vietato lasciare biciclette e passeggini nell'androne. · "
          "La spazzatura si porta nei bidoni del cortile, divisa per tipo. · I cani devono stare al guinzaglio nelle scale e nel cortile. · Si prega di chiudere sempre il portone."),
  {"part": "Le preposizioni articolate", "teoria":
     tab(("a + il", "al"), ("di + la", "della"), ("da + i", "dai"), ("in + l'", "nell'"), ("su + le", "sulle"), head=("preposizione + articolo", "")) +
     "Le preposizioni <b>a, di, da, in, su</b> si uniscono all'articolo." + es("La spazzatura va <b>nei</b> bidoni. · Il bucato è <b>sul</b> balcone.")},
  scrivi([("1. (in + i) La carta va … bidoni blu.", ("nei",)), ("2. (su + il) Non stendere i panni … balcone del vicino.", ("sul",)),
          ("3. (di + il) La riunione … condominio è giovedì.", ("del",)), ("4. (a + la) Porto i rifiuti … isola ecologica il sabato.", ("all'",)),
          ("5. (da + l') Le chiavi sono … amministratore.", ("dall'",)), ("6. (in + la) Il regolamento è … bacheca, all'ingresso.", ("nella",))],
         "7 · Completa con la preposizione articolata", "7 · Preposizioni", "e7", w="s"),
  {"part": "Educazione civica · Segnali e cartelli"},
  menu(["vietato fumare", "cani al guinzaglio", "silenzio", "attenzione bambini", "raccolta differenziata", "vietato l'accesso"],
       [("1. Sei nel corridoio dell'ospedale.", "silenzio"), ("2. Sei vicino a una scuola elementare e guidi.", "attenzione bambini"),
        ("3. Sei in un bar e vuoi accendere una sigaretta.", "vietato fumare"), ("4. Porti Fido al parco.", "cani al guinzaglio"),
        ("5. C'è un cantiere e una porta chiusa.", "vietato l'accesso"), ("6. Hai bottiglie di plastica e giornali vecchi.", "raccolta differenziata")],
       "8 · Quale cartello?", "8 · I cartelli", "e8"),
  ordina(["Buongiorno, sono la nuova vicina del secondo piano.", "Piacere! Io sono Giovanni. Abita qui da tanto?",
          "No, da una settimana. Posso chiederLe una cosa?", "Certo, mi dica.", "Dove si mette la bicicletta?", "Nel cortile, vicino ai bidoni."],
         "9 · Metti in ordine il dialogo", "9 · Il dialogo", "e9"),
  libero("e10", 10, "Per scrivere: le regole per i bambini", "Scrivi 5 regole per i bambini della tua casa o del tuo palazzo. Usa: è vietato… / bisogna… / si deve…", ["Le regole"], rows=5),
  parla("e11", 11, "Racconta: com'è il tuo palazzo? Conosci i vicini? Quali regole ci sono? E nel tuo Paese?"),
 ]
}

# =====================================================================
# A2 · UNITÀ 3 · IL TEMPO
# =====================================================================
METEO = [("M", "Buonasera dalla redazione meteo. Domani al nord il cielo sarà nuvoloso e pioverà in Liguria e in Piemonte."),
         ("M", "Al centro tempo variabile, con vento forte sulla costa."),
         ("M", "Al sud e sulle isole bel tempo: c'è il sole e fa caldo, con temperature fino a ventiquattro gradi a Bari e Palermo."),
         ("M", "Attenzione alla nebbia la mattina presto nella pianura padana.")]
TEMPO_SLIDE = [
    cover("🌦️", "Il tempo", "Il tempo atmosferico · Il tempo libero", "A2 &bull; Modulo 1 &bull; Unità 3"),
    slide("In questa unità impari a…", cards([
        ("☀️", "Parlare del tempo", "Che tempo fa? Piove, fa freddo"), ("🧭", "Capire il meteo", "al nord, al sud, le temperature"),
        ("🎨", "Dire cosa stai facendo", "Sto leggendo, sto cucinando"), ("⚽", "Parlare del tempo libero", "Mi piace il calcio, mi piacciono i film")])),
    slide("☀️ Che tempo fa?", cards([
        ("☀️", "c'è il sole", "è sereno"), ("☁️", "è nuvoloso", "ci sono le nuvole"), ("🌧️", "piove", "la pioggia"), ("❄️", "nevica", "la neve"),
        ("💨", "c'è vento", "tira vento"), ("🌫️", "c'è nebbia", "non si vede niente"), ("🔥", "fa caldo", "30 gradi"), ("🥶", "fa freddo", "2 gradi"),
        ("⛈️", "c'è un temporale", "tuoni e fulmini")], "g3")),
    slide("🧭 Le stagioni e i punti cardinali", table([
        ["la primavera", "marzo, aprile, maggio", "il nord ⬆️"], ["l'estate", "giugno, luglio, agosto", "il sud ⬇️"],
        ["l'autunno", "settembre, ottobre, novembre", "l'est ➡️"], ["l'inverno", "dicembre, gennaio, febbraio", "l'ovest ⬅️"]],
        head=["stagione", "mesi", "punti cardinali"]) + "\n" + nota("Bari è <b>al sud</b>, sul mare Adriatico, a <b>est</b>. Milano è <b>al nord</b>.")),
    slide("📺 Lezione A · Le previsioni del tempo", '    <div class="testo">' + "".join("<p>%s</p>" % t for _, t in METEO) + "</div>"),
    slide("📘 Stare + gerundio", table([
        ["-are", "parlare → parl<b>ando</b>", "Sto parlando al telefono."], ["-ere", "leggere → legg<b>endo</b>", "Saleah sta leggendo il giornale."],
        ["-ire", "dormire → dorm<b>endo</b>", "I bambini stanno dormendo."], ["irregolari", "fare → facendo · bere → bevendo · dire → dicendo", "Cosa stai facendo?"]],
        head=["verbo", "gerundio", "esempio"]) + "\n" + nota("<b>sto, stai, sta, stiamo, state, stanno</b> + gerundio = un'azione <b>adesso</b>, in questo momento.")),
    slide("⚽ Lezione B · Il tempo libero", dialogo([
        ("Cristian", "Silvia, cosa fai il fine settimana?"), ("*Silvia", "Il sabato faccio volontariato in una biblioteca di quartiere. E tu?"),
        ("Cristian", "Io gioco a calcetto con i colleghi. Mi piace molto lo sport."), ("*Silvia", "A me non piace il calcio, ma mi piacciono le passeggiate sul lungomare."),
        ("Cristian", "Allora domenica, se c'è il sole, andiamo tutti a Pane e Pomodoro?"), ("*Silvia", "Che bella idea! Porto un buon dolce.")])),
    slide("📘 Mi piace / mi piacciono", table([
        ["mi piace", "+ una cosa / un verbo", "Mi piace <b>il mare</b>. Mi piace <b>ballare</b>."], ["mi piacciono", "+ più cose", "Mi piacciono <b>i film</b>."],
        ["non mi piace", "", "Non mi piace <b>la pioggia</b>."]], head=["", "", "esempio"]) + "\n" +
        nota("a me = mi · a te = ti · a lui = gli · a lei = le · a noi = ci · a voi = vi · a loro = gli")),
    slide("📘 Bello, buono, grande", table([
        ["bello", "un bel libro · un bello spettacolo · un bell'albero · dei bei film · dei begli occhi"], ["buono", "un buon caffè · una buona idea · un buon amico"],
        ["grande", "un gran lavoro · una grande festa (gran = molto)"]], head=["aggettivo", "prima del nome"])),
    slide("🌍 Educazione civica · I centri interculturali", cards([
        ("🗣️", "corsi di lingua", "italiano e lingue madri"), ("🎉", "feste e incontri", "musica, cucina, cultura"),
        ("📚", "biblioteca", "libri in tante lingue"), ("🤝", "volontariato", "puoi aiutare anche tu")], "g2")),
    end("Ora sai parlare del tempo e del tempo libero!"),
]
A2TEMPO = {
 "title": "🌦️ Il tempo · Esercizi", "store": "a2-il-tempo", "livello": "a2",
 "sections": [
  {"part": "Che tempo fa?"},
  menu(["piove", "nevica", "fa caldo", "fa freddo", "c'è nebbia", "c'è vento"],
       [("1. Prendo l'ombrello perché …", "piove"), ("2. Metto il cappotto e i guanti perché …", "fa freddo"),
        ("3. Non vedo le macchine davanti a me: …", "c'è nebbia"), ("4. I bambini fanno il pupazzo bianco: …", "nevica"),
        ("5. Vado al mare e faccio il bagno: …", "fa caldo"), ("6. Il cappello vola via: …", "c'è vento")],
       "1 · Che tempo fa?", "1 · Il tempo", "e1"),
  menu(["primavera", "estate", "autunno", "inverno"],
       [("1. Agosto è in …", "estate"), ("2. Gennaio è in …", "inverno"), ("3. Aprile è in …", "primavera"),
        ("4. Ottobre è in …", "autunno"), ("5. Natale è in …", "inverno"), ("6. Luglio è in …", "estate")],
       "2 · Le stagioni", "2 · Le stagioni", "e2"),
  {"part": "Lezione A · Le previsioni"},
  ascolto(scegli([("1. Domani al nord…", ["c'è il sole", "è nuvoloso e piove", "nevica"], "è nuvoloso e piove"),
                  ("2. Al centro…", ["c'è vento forte sulla costa", "fa molto freddo", "c'è nebbia"], "c'è vento forte sulla costa"),
                  ("3. A Bari…", ["piove", "fa caldo, 24 gradi", "fa freddo, 4 gradi"], "fa caldo, 24 gradi"),
                  ("4. La nebbia c'è…", ["la sera al sud", "la mattina presto in pianura padana", "tutto il giorno al centro"], "la mattina presto in pianura padana")],
                 "3 · 🎧 Ascolta le previsioni del tempo", "3 · Le previsioni", "e3"), [list(x) for x in METEO]),
  {"part": "Stare + gerundio", "teoria":
     tab(("parlare", "parlando"), ("leggere", "leggendo"), ("dormire", "dormendo"), ("fare / bere / dire", "facendo / bevendo / dicendo"), head=("verbo", "gerundio")) +
     "<b>stare</b> (sto, stai, sta, stiamo, state, stanno) + <b>gerundio</b> = azione in corso, adesso." + es("Che cosa <b>stai facendo</b>? <b>Sto cucinando</b>.")},
  scrivi([("1. (io – cucinare) Adesso non posso, …", ("sto cucinando",)), ("2. (Michele – lavorare) Michele … in magazzino.", ("sta lavorando",)),
          ("3. (noi – guardare) … le previsioni del tempo.", ("stiamo guardando",)), ("4. (i bambini – dormire) Silenzio, …", ("stanno dormendo", "i bambini stanno dormendo")),
          ("5. (tu – fare) Che cosa …?", ("stai facendo",)), ("6. (voi – bere) … un caffè al bar?", ("state bevendo",))],
         "4 · Che cosa stanno facendo?", "4 · Stare + gerundio", "e4", w="m"),
  {"part": "Lezione B · Il tempo libero"},
  vf(["1. Silvia fa volontariato il sabato.", "2. Cristian gioca a calcetto.", "3. A Silvia piace molto il calcio.",
      "4. A Silvia piacciono le passeggiate sul lungomare.", "5. Domenica vanno al mare se piove."],
     ["VERO", "VERO", "FALSO", "VERO", "FALSO"], "5 · Leggi il dialogo delle slide: vero o falso?", "5 · Il fine settimana", "e5",
     info="<b>Cristian:</b> Silvia, cosa fai il fine settimana? · <b>Silvia:</b> Il sabato faccio volontariato in una biblioteca di quartiere. E tu? · "
          "<b>Cristian:</b> Io gioco a calcetto con i colleghi. Mi piace molto lo sport. · <b>Silvia:</b> A me non piace il calcio, ma mi piacciono le passeggiate sul lungomare. · "
          "<b>Cristian:</b> Allora domenica, se c'è il sole, andiamo tutti a Pane e Pomodoro? · <b>Silvia:</b> Che bella idea!"),
  {"part": "Mi piace / mi piacciono", "teoria":
     tab(("una cosa, un verbo", "mi piace"), ("più cose", "mi piacciono"), head=("che cosa?", "")) +
     "a me = <b>mi</b>, a te = <b>ti</b>, a lui = <b>gli</b>, a lei = <b>le</b>, a noi = <b>ci</b>, a voi = <b>vi</b>, a loro = <b>gli</b>." + es("Mi piace il mare. · Ti piacciono i gatti?")},
  scegli([("1. Mi … le canzoni italiane.", ["piace", "piacciono"], "piacciono"), ("2. A Saleah … ballare.", ["piace", "piacciono"], "piace"),
          ("3. Ci … molto il parco di Bari.", ["piace", "piacciono"], "piace"), ("4. Ti … i film d'azione?", ["piace", "piacciono"], "piacciono"),
          ("5. A Giovanni non … la pioggia.", ["piace", "piacciono"], "piace"), ("6. Ai bambini … i giochi in cortile.", ["piace", "piacciono"], "piacciono")],
         "6 · Piace o piacciono?", "6 · Piace / piacciono", "e6"),
  menu(["mi", "ti", "gli", "le", "ci", "vi"],
       [("1. (a lui) Ad Ahmed … piace cucinare.", "gli"), ("2. (a lei) A Eneida … piacciono i fiori.", "le"),
        ("3. (a noi) … piace fare volontariato.", "ci"), ("4. (a te) … piace il calcetto?", "ti"),
        ("5. (a voi) … piacciono le feste del centro?", "vi"), ("6. (a me) … piace molto la primavera.", "mi")],
       "7 · Scegli il pronome", "7 · mi, ti, gli…", "e7"),
  {"part": "Bello, buono, grande", "teoria":
     tab(("bel / bello / bell'", "un bel giorno · un bello spettacolo · un bell'albero"), ("buon / buona", "un buon caffè · una buona idea"), head=("forma", "esempio")) +
     "Prima del nome <b>bello</b> e <b>buono</b> cambiano come l'articolo." + es("Che <b>bel</b> tempo oggi!")},
  scegli([("1. Oggi è una … giornata: c'è il sole.", ["bella", "bel", "bello"], "bella"), ("2. Al centro c'è un … corso di cucina.", ["buono", "buon", "buona"], "buon"),
          ("3. Abbiamo visto un … spettacolo.", ["bel", "bello", "bell'"], "bello"), ("4. Che … idea!", ["buon", "buona", "buono"], "buona"),
          ("5. In piazza c'è un … albero di Natale.", ["bel", "bello", "bell'"], "bell'")],
         "8 · Scegli la forma giusta", "8 · bello, buono", "e8"),
  {"part": "Educazione civica · I centri interculturali"},
  vf(["1. Nei centri interculturali ci sono corsi di lingua.", "2. Sono solo per le persone italiane.", "3. Si organizzano feste e incontri.",
      "4. Anche tu puoi fare volontariato."], ["VERO", "FALSO", "VERO", "VERO"], "9 · I centri interculturali: vero o falso?", "9 · I centri", "e9"),
  libero("e10", 10, "Per parlare: cosa facciamo?", "Scrivi un messaggio a un amico: proponi un'attività per il fine settimana. Pensa al tempo (se piove…, se c'è il sole…).", ["Il messaggio"], rows=4),
  parla("e11", 11, "Che tempo fa oggi? Che cosa ti piace fare nel tempo libero? Com'è il clima nel tuo Paese?"),
 ]
}

# =====================================================================
# A2 · UNITÀ 4 · IL LAVORO
# =====================================================================
COLLOQUIO = [("F", "Buongiorno, signor Diallo. Si accomodi. Mi parla un po' di Lei?"),
             ("M", "Buongiorno. Ho ventinove anni, vengo dalla Guinea e vivo a Bari da tre anni."),
             ("F", "Che esperienza ha nel magazzino?"),
             ("M", "Ho lavorato due anni come magazziniere in un supermercato. Ho anche il patentino per il muletto."),
             ("F", "Bene. Il turno è dalle sei alle quattordici. Le va bene?"),
             ("M", "Sì, nessun problema. Mi sveglio presto."),
             ("F", "Perfetto. Le mando una email con i documenti per il contratto. Le telefono entro venerdì."),
             ("M", "Grazie mille, aspetto la Sua telefonata.")]
LAV_SLIDE = [
    cover("💼", "Il lavoro", "Cercare lavoro · Il curriculum · Il colloquio", "A2 &bull; Modulo 1 &bull; Unità 4"),
    slide("In questa unità impari a…", cards([
        ("🔎", "Leggere un annuncio", "cercasi, requisiti, si offre"), ("📄", "Scrivere un curriculum", "esperienze, competenze, lingue"),
        ("🤝", "Fare un colloquio", "Mi parla di Lei? Le va bene?"), ("🏷️", "Leggere le etichette", "i simboli sui prodotti")])),
    slide("🔎 Le parole del lavoro", table([
        ["disoccupato/a", "non ha lavoro"], ["l'annuncio di lavoro", "Cercasi cameriere…"], ["i requisiti", "che cosa serve: patente, esperienza…"],
        ["il turno", "dalle 6 alle 14"], ["il contratto", "a tempo determinato / indeterminato"], ["lo stipendio", "i soldi del mese"]], head=["parola", "che cosa vuol dire"])),
    slide("📰 Lezione A · L'annuncio", '    <div class="testo"><p><b>CERCASI MAGAZZINIERE</b> · Bari, zona industriale</p>'
          "<p><b>Requisiti:</b> esperienza di almeno 1 anno, patentino per il muletto, disponibilità a turni.</p>"
          "<p><b>Si offre:</b> contratto a tempo determinato di 6 mesi, possibilità di rinnovo.</p>"
          "<p>Inviare il curriculum a lavoro@magazzinilevante.it</p></div>"),
    slide("📄 Il curriculum", cards([
        ("👤", "Dati personali", "nome, indirizzo, telefono, email"), ("💼", "Esperienza lavorativa", "dove, quando, che cosa"),
        ("🎓", "Istruzione e formazione", "scuola, corsi"), ("🗣️", "Lingue", "italiano A2, francese, pular"),
        ("🛠️", "Competenze", "muletto, computer, patente B"), ("✍️", "Autorizzazione", "trattamento dei dati personali")], "g2")),
    slide("📘 I pronomi indiretti: gli, le, Le", table([
        ["a lui", "gli", "Il capo <b>gli</b> telefona domani."], ["a lei", "le", "Silvia <b>le</b> manda il curriculum."],
        ["a Lei (formale)", "Le", "<b>Le</b> mando una email, signor Diallo."], ["a loro", "gli", "<b>Gli</b> spiego il lavoro."]],
        head=["a chi?", "pronome", "esempio"]) + "\n" + nota("Il pronome indiretto risponde alla domanda <b>a chi?</b> e va <b>prima del verbo</b>.")),
    slide("🤝 Lezione B · Il colloquio", dialogo([("*Responsabile" if v == "F" else "Mamadou", t) for v, t in COLLOQUIO])),
    slide("📘 I pronomi indiretti: mi, ti, ci, vi", table([
        ["a me", "mi", "<b>Mi</b> parla un po' di Lei?"], ["a te", "ti", "<b>Ti</b> scrivo dopo il colloquio."],
        ["a noi", "ci", "Il capo <b>ci</b> dà i turni il lunedì."], ["a voi", "vi", "<b>Vi</b> mando il contratto."]], head=["a chi?", "pronome", "esempio"])),
    slide("🏷️ Educazione civica · I simboli sulle etichette", cards([
        ("☠️", "tossico", "pericolo di morte"), ("🔥", "infiammabile", "lontano dal fuoco"), ("🧪", "corrosivo", "brucia la pelle"),
        ("❗", "irritante", "fa male a occhi e pelle"), ("🧤", "usa i guanti", "proteggi le mani"), ("♻️", "riciclabile", "va nella differenziata")], "g3")),
    end("Ora sai cercare lavoro e fare un colloquio!"),
]
A2LAV = {
 "title": "💼 Il lavoro · Esercizi", "store": "a2-il-lavoro", "livello": "a2",
 "sections": [
  {"part": "Le parole del lavoro"},
  menu(["disoccupato", "il turno", "lo stipendio", "il contratto", "i requisiti", "l'annuncio"],
       [("1. Non ha un lavoro: è …", "disoccupato"), ("2. I soldi che ricevo ogni mese: …", "lo stipendio"),
        ("3. Dalle 14 alle 22: è …", "il turno"), ("4. Lo firmo quando comincio a lavorare: …", "il contratto"),
        ("5. «Cercasi cuoco» sul giornale: è …", "l'annuncio"), ("6. Patente B ed esperienza: sono …", "i requisiti")],
       "1 · Le parole del lavoro", "1 · Le parole", "e1"),
  {"part": "Lezione A · L'annuncio"},
  vf(["1. Il lavoro è a Bari.", "2. Non serve esperienza.", "3. Serve il patentino per il muletto.", "4. Il contratto è a tempo indeterminato.",
      "5. Il curriculum si manda per email."], ["VERO", "FALSO", "VERO", "FALSO", "VERO"], "2 · Leggi l'annuncio: vero o falso?", "2 · L'annuncio", "e2",
     info="<b>CERCASI MAGAZZINIERE</b> · Bari, zona industriale<br><b>Requisiti:</b> esperienza di almeno 1 anno, patentino per il muletto, disponibilità a turni.<br>"
          "<b>Si offre:</b> contratto a tempo determinato di 6 mesi, possibilità di rinnovo.<br>Inviare il curriculum a lavoro@magazzinilevante.it"),
  menu(["Dati personali", "Esperienza lavorativa", "Istruzione e formazione", "Lingue", "Competenze"],
       [("1. Francese: ottimo. Italiano: A2.", "Lingue"), ("2. 2022-2024: magazziniere, supermercato Conad, Bari.", "Esperienza lavorativa"),
        ("3. Via Napoli 40, Bari – 333 1234567", "Dati personali"), ("4. Corso di sicurezza sul lavoro, 12 ore (2024).", "Istruzione e formazione"),
        ("5. Uso del muletto, patente B, Excel di base.", "Competenze")],
       "3 · In quale parte del curriculum?", "3 · Il curriculum", "e3"),
  {"part": "I pronomi indiretti gli, le, Le", "teoria":
     tab(("a lui / a loro", "gli"), ("a lei", "le"), ("a Lei (formale)", "Le"), head=("a chi?", "pronome")) +
     "Rispondono alla domanda <b>a chi?</b> e vanno <b>prima del verbo</b>." + es("Telefono a Mamadou → <b>Gli</b> telefono.", "Scrivo a Silvia → <b>Le</b> scrivo.")},
  menu(["gli", "le", "Le"],
       [("1. Scrivo a Saleah → … scrivo.", "le"), ("2. Telefono a Giovanni → … telefono.", "gli"),
        ("3. Signora, … mando il contratto domani.", "Le"), ("4. Do i guanti agli operai → … do i guanti.", "gli"),
        ("5. Spiego i turni a Eneida → … spiego i turni.", "le"), ("6. Signor Diallo, … piace questo lavoro?", "Le")],
       "4 · Gli, le o Le?", "4 · gli, le, Le", "e4"),
  {"part": "Lezione B · Il colloquio"},
  ascolto(scegli([("1. Mamadou vive a Bari da…", ["tre anni", "due anni", "nove anni"], "tre anni"),
                  ("2. Ha lavorato come magazziniere…", ["in una fabbrica", "in un supermercato", "al porto"], "in un supermercato"),
                  ("3. Il turno è…", ["dalle 6 alle 14", "dalle 14 alle 22", "di notte"], "dalle 6 alle 14"),
                  ("4. La responsabile gli telefona…", ["domani", "entro venerdì", "lunedì"], "entro venerdì")],
                 "5 · 🎧 Ascolta il colloquio", "5 · Il colloquio", "e5"), [list(x) for x in COLLOQUIO]),
  {"part": "I pronomi indiretti mi, ti, ci, vi", "teoria":
     tab(("a me", "mi"), ("a te", "ti"), ("a noi", "ci"), ("a voi", "vi"), head=("a chi?", "pronome")) + es("<b>Mi</b> parla di Lei? · <b>Vi</b> mando i turni.")},
  scrivi([("1. (a me) Il responsabile … ha dato il contratto.", ("mi",)), ("2. (a te) … mando il numero dell'agenzia.", ("ti",)),
          ("3. (a noi) La capa … spiega le regole di sicurezza.", ("ci",)), ("4. (a voi) … telefono quando ci sono i turni nuovi.", ("vi",)),
          ("5. (a me) … può ripetere, per favore?", ("mi",))],
         "6 · Completa con mi, ti, ci, vi", "6 · mi, ti, ci, vi", "e6", bank="mi · ti · ci · vi", w="s"),
  ordina(["Buongiorno, ho letto il vostro annuncio.", "Buongiorno. Che esperienza ha?", "Ho lavorato tre anni come aiuto cuoco.",
          "Bene. È disponibile anche la sera?", "Sì, va bene anche la sera.", "Allora Le mando una email per il colloquio."],
         "7 · Metti in ordine la telefonata", "7 · La telefonata", "e7"),
  {"part": "Educazione civica · Le etichette"},
  menu(["tossico", "infiammabile", "corrosivo", "irritante", "riciclabile"],
       [("1. La candeggina può bruciare la pelle: è …", "corrosivo"), ("2. L'alcol va tenuto lontano dal fuoco: è …", "infiammabile"),
        ("3. Il veleno per i topi: è …", "tossico"), ("4. La bottiglia di plastica vuota: è …", "riciclabile"),
        ("5. Il detersivo fa male agli occhi: è …", "irritante")],
       "8 · Che simbolo c'è sull'etichetta?", "8 · Le etichette", "e8"),
  libero("e9", 9, "Per scrivere: rispondi a un annuncio", "Scrivi una email per rispondere all'annuncio del magazzino. Saluta, di' chi sei, la tua esperienza, quando sei disponibile, saluta.", ["La mia email"], rows=7),
  parla("e10", 10, "Che lavoro fai o vuoi fare? Che lavoro facevi nel tuo Paese? Hai mai fatto un colloquio?"),
 ]
}

SLIDE = [("a2-la-convivenza/index.html", "La convivenza", "A2", CONV_SLIDE, "a2"),
         ("a2-il-tempo/index.html", "Il tempo", "A2", TEMPO_SLIDE, "a2"),
         ("a2-il-lavoro/index.html", "Il lavoro", "A2", LAV_SLIDE, "a2")]
ESERCIZI = [("a2-la-convivenza", A2CONV), ("a2-il-tempo", A2TEMPO), ("a2-il-lavoro", A2LAV)]
GIOCHI = {
 "a2-la-convivenza": ("a2-vivere-insieme", "A2", "🏘️ GIOCHI: LA CONVIVENZA (A2)", [
  ["IL VICINO", "🏠", "ABITA NELLA CASA ACCANTO"], ["IL CONDOMINIO", "🏢", "UN PALAZZO CON TANTI APPARTAMENTI"], ["IL REGOLAMENTO", "📜", "LE REGOLE DEL PALAZZO"],
  ["L'ANDRONE", "🚪", "L'INGRESSO DEL PALAZZO"], ["IL CORTILE", "🌳", "SPAZIO APERTO DENTRO IL PALAZZO"], ["IL BUCATO", "👕", "I PANNI LAVATI"],
  ["IL BALCONE", "🪴", "QUI STENDO I PANNI"], ["LA SPAZZATURA", "🗑️", "I RIFIUTI DI CASA"], ["IL PORTONE", "🔑", "SI CHIUDE SEMPRE"],
  ["VIETATO", "🚫", "NON SI PUÒ FARE"], ["IL SILENZIO", "🤫", "NIENTE RUMORE"], ["IL GUINZAGLIO", "🐕", "PER IL CANE"],
  ["MAROCCHINO", "🇲🇦", "VIENE DAL MAROCCO"], ["SENEGALESE", "🇸🇳", "VIENE DAL SENEGAL"], ["ALBANESE", "🇦🇱", "VIENE DALL'ALBANIA"],
  ["UCRAINA", "🇺🇦", "OLENA VIENE DALL'…"], ["GENTILMENTE", "🙂", "IN MODO GENTILE"], ["REGOLARMENTE", "📅", "IN MODO REGOLARE"]]),
 "a2-il-tempo": ("a2-vivere-insieme", "A2", "🌦️ GIOCHI: IL TEMPO (A2)", [
  ["IL SOLE", "☀️", "C'È IL… FA CALDO"], ["LA PIOGGIA", "🌧️", "SERVE L'OMBRELLO"], ["LA NEVE", "❄️", "BIANCA E FREDDA"], ["IL VENTO", "💨", "MUOVE GLI ALBERI"],
  ["LA NEBBIA", "🌫️", "NON SI VEDE NIENTE"], ["LE NUVOLE", "☁️", "GRIGIE NEL CIELO"], ["IL TEMPORALE", "⛈️", "TUONI E FULMINI"], ["LA PRIMAVERA", "🌸", "MARZO, APRILE, MAGGIO"],
  ["L'ESTATE", "🏖️", "GIUGNO, LUGLIO, AGOSTO"], ["L'AUTUNNO", "🍂", "CADONO LE FOGLIE"], ["L'INVERNO", "🧣", "DICEMBRE, GENNAIO, FEBBRAIO"], ["IL NORD", "⬆️", "MILANO È AL…"],
  ["IL SUD", "⬇️", "BARI È AL…"], ["IL CALCETTO", "⚽", "CALCIO CON 5 GIOCATORI"], ["IL VOLONTARIATO", "🤝", "AIUTO GLI ALTRI GRATIS"], ["LA PASSEGGIATA", "🚶", "CAMMINO SUL LUNGOMARE"],
  ["IL CINEMA", "🎬", "QUI VEDO I FILM"], ["LA BIBLIOTECA", "📚", "QUI PRENDO I LIBRI"]]),
 "a2-il-lavoro": ("a2-vivere-insieme", "A2", "💼 GIOCHI: IL LAVORO (A2)", [
  ["L'ANNUNCIO", "📰", "CERCASI CAMERIERE…"], ["IL CURRICULUM", "📄", "LE MIE ESPERIENZE SU UN FOGLIO"], ["IL COLLOQUIO", "🤝", "INCONTRO PER UN LAVORO"],
  ["IL CONTRATTO", "✍️", "LO FIRMO QUANDO COMINCIO"], ["LO STIPENDIO", "💶", "I SOLDI DEL MESE"], ["IL TURNO", "⏰", "DALLE 6 ALLE 14"],
  ["DISOCCUPATO", "🙁", "NON HA LAVORO"], ["I REQUISITI", "✅", "COSA SERVE PER IL LAVORO"], ["L'ESPERIENZA", "🧰", "I LAVORI CHE HO FATTO"],
  ["IL MAGAZZINIERE", "📦", "LAVORA IN MAGAZZINO"], ["IL MULETTO", "🚜", "SOLLEVA I PACCHI PESANTI"], ["IL CUOCO", "👨‍🍳", "LAVORA IN CUCINA"],
  ["IL COLLEGA", "👥", "LAVORA CON ME"], ["IL RESPONSABILE", "👔", "IL CAPO DEL REPARTO"], ["TOSSICO", "☠️", "PERICOLO DI MORTE"],
  ["INFIAMMABILE", "🔥", "LONTANO DAL FUOCO"], ["CORROSIVO", "🧪", "BRUCIA LA PELLE"], ["I GUANTI", "🧤", "PROTEGGONO LE MANI"]]),
}

if __name__ == "__main__":
    for path, unit, top, sl, liv in SLIDE:
        os.makedirs(os.path.dirname(path), exist_ok=True)
        build_slide(path, unit, top, sl, liv)
    for cartella, dati in ESERCIZI:
        build_es(cartella + "/esercizi.html", dati)
    build_giochi(GIOCHI)
