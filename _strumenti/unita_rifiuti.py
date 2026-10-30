"""LA RACCOLTA DIFFERENZIATA (la casa + educazione civica, A1), 2026-10-30.
Fonti usate come traccia: «differenziata.pdf» (Università per Stranieri di Siena, Unità 1, A1: lessico, imperativo, simboli),
la scheda di Adgblog «L'italiano con i rifiuti: dove li metti? dove li porti?» (elenco di rifiuti e punti di raccolta),
i colori dei bidoni della raccolta porta a porta di AMIU a Bari (ordinanza del Comune di Bari, 2024).
Testi ed esercizi scritti per il sito, in STAMPATELLO MAIUSCOLO. Il video è quello indicato da Erila.
Uso: python3 _strumenti/slide.py e python3 _strumenti/genera.py"""
from genera import eq, has
from unita_primi import cover, slide, cards, table, nota, dialogo, end
from unita_drive import ILL_CSS, ill2, passi, vf, scegli, menu, scrivi, ordina, completa, parla, libero

TOP = "LA CASA &bull; EDUCAZIONE CIVICA"
VIDEO = "5lJqyDAyXQk"

CSS = ILL_CSS + """
  .bidoni{display:grid; grid-template-columns:repeat(5,1fr); gap:12px;}
  .bidoni div{border-radius:16px; padding:14px 10px; color:#fff; font-weight:bold; font-size:1.25rem; text-align:center;}
  .bidoni .e{display:block; font-size:2.4rem; margin-bottom:6px;}
  .bidoni span{display:block; font-weight:normal; font-size:.95rem; margin-top:6px;}
  .si-no{display:grid; grid-template-columns:1fr 1fr; gap:14px;}
  .si-no > div{border-radius:16px; padding:14px 18px; font-size:1.3rem; background:#fff;}
  .si-no .si{border:4px solid #2e9e5b;} .si-no .no{border:4px solid #d64545;}
  .si-no h3{margin:0 0 8px;} .si-no ul{margin:0; padding-left:22px;} .si-no li{margin:4px 0;}
  .video{position:relative; width:100%; max-width:900px; margin:0 auto; aspect-ratio:16/9; border-radius:18px; overflow:hidden; box-shadow:0 6px 16px rgba(0,0,0,.15); background:#000;}
  .video iframe{position:absolute; inset:0; width:100%; height:100%; border:0;}
  @media (max-width:900px){ .bidoni{grid-template-columns:1fr 1fr;} .bidoni div{font-size:1.05rem;} .si-no > div{font-size:1.05rem;} }
  @media (max-width:520px){ .si-no{grid-template-columns:1fr;} }"""

# colori dei bidoni a Bari (AMIU)
MARRONE, BLU, GIALLO, VERDE, GRIGIO = "#8b5a2b", "#1f6fd1", "#e0a800", "#2e9e5b", "#6b7280"

def bidoni(items):
    return '    <div class="bidoni">\n' + "".join(
        '      <div style="background:%s"><span class="e">%s</span>%s<span>%s</span></div>\n' % c for c in items) + "    </div>"

def si_no(si, no):
    li = lambda xs: "".join("<li>%s</li>" % x for x in xs)
    return ('    <div class="si-no">\n      <div class="si"><h3>✅ SÌ</h3><ul>%s</ul></div>\n'
            '      <div class="no"><h3>❌ NO</h3><ul>%s</ul></div>\n    </div>' % (li(si), li(no)))

SLIDE_RD = [
    cover("♻️", "LA RACCOLTA DIFFERENZIATA", "DOVE BUTTO I RIFIUTI? DOVE LI PORTO?", "LA CASA &bull; EDUCAZIONE CIVICA &bull; A1"),
    slide("CHE COSA IMPARIAMO?", cards([
        ("🗑️", "I RIFIUTI", "CHE COSA SONO E PERCHÉ LI DIVIDIAMO"),
        ("🎨", "I COLORI DEI BIDONI", "A BARI: MARRONE, BLU, GIALLO, VERDE, GRIGIO"),
        ("🔋", "I RIFIUTI SPECIALI", "PILE, MEDICINE, VESTITI, MOBILI VECCHI"),
        ("✏️", "L'IMPERATIVO", "BUTTA! METTETE! NON BUTTARE!")])),
    slide("🗑️ CHE COSA SONO I RIFIUTI?", ill2("rifiuti-cucina.png", "UNA FAMIGLIA IN CUCINA DIVIDE I RIFIUTI IN BIDONI COLORATI",
        nota("I <b>RIFIUTI</b> (O LA <b>SPAZZATURA</b>) SONO LE COSE CHE NON USIAMO PIÙ E BUTTIAMO VIA.<br><br>"
             "IN ITALIA FACCIAMO LA <b>RACCOLTA DIFFERENZIATA</b>: DIVIDIAMO I RIFIUTI. "
             "LA CARTA VA CON LA CARTA, IL VETRO CON IL VETRO, LA PLASTICA CON LA PLASTICA.<br><br>"
             "PERCHÉ? COSÌ POSSIAMO <b>RICICLARE</b>: USARE DI NUOVO I MATERIALI. "
             "È MEGLIO PER L'AMBIENTE E PER LA CITTÀ.", ""))),
    slide("🎨 A BARI: I BIDONI E I COLORI", bidoni([
        (MARRONE, "🍌", "ORGANICO", "AVANZI DI CIBO"), (BLU, "📰", "CARTA E CARTONE", "GIORNALI, SCATOLE"),
        (GIALLO, "🧴", "PLASTICA E METALLI", "BOTTIGLIE, LATTINE"), (VERDE, "🍾", "VETRO", "BOTTIGLIE, VASETTI"),
        (GRIGIO, "🧽", "INDIFFERENZIATO", "QUELLO CHE NON SI RICICLA")]) + "\n" +
        nota("⚠️ I COLORI <b>CAMBIANO DA CITTÀ A CITTÀ</b>. IN UN'ALTRA CITTÀ GUARDA LE ISTRUZIONI DEL TUO COMUNE.")),
    slide("🟤 ORGANICO: IL BIDONE MARRONE", si_no(
        ["GLI AVANZI DI CIBO", "LE BUCCE DELLA FRUTTA E DELLA VERDURA", "I GUSCI D'UOVO", "I FONDI DEL CAFFÈ E LE BUSTINE DEL TÈ",
         "I FIORI E LE FOGLIE SECCHE", "I TOVAGLIOLI DI CARTA SPORCHI"],
        ["LE BUSTE DI PLASTICA", "I PANNOLINI", "LA CENERE DELLE SIGARETTE"]) + "\n" +
        nota("💡 USA I <b>SACCHETTI COMPOSTABILI</b> (QUELLI DEL SUPERMERCATO PER LA FRUTTA).")),
    slide("🔵 CARTA E CARTONE: IL BIDONE BLU", si_no(
        ["I GIORNALI E LE RIVISTE", "I QUADERNI E I FOGLI", "LE SCATOLE DI CARTONE (SCHIACCIATE)", "I SACCHETTI DI CARTA",
         "LE SCATOLE DEI BISCOTTI E DEI CIOCCOLATINI"],
        ["LA CARTA SPORCA DI CIBO O DI OLIO", "I FAZZOLETTI USATI", "GLI SCONTRINI"])),
    slide("🟡 PLASTICA E METALLI: IL BIDONE GIALLO", si_no(
        ["LE BOTTIGLIE DI PLASTICA (SCHIACCIATE)", "I FLACONI DELLO SHAMPOO E DEL DETERSIVO", "LE VASCHETTE DELLA FRUTTA",
         "LE BUSTE DI PLASTICA", "LE LATTINE", "LE SCATOLETTE DEL TONNO E DEI PELATI"],
        ["I GIOCATTOLI", "LE PENNE", "GLI SPAZZOLINI"]) + "\n" +
        nota("💡 PRIMA <b>SVUOTA</b> E <b>SCIACQUA</b> BOTTIGLIE E SCATOLETTE.")),
    slide("🟢 VETRO: IL BIDONE VERDE", si_no(
        ["LE BOTTIGLIE DI VETRO", "I VASETTI DELLA MARMELLATA", "I BARATTOLI DI VETRO"],
        ["I PIATTI E LE TAZZE DI CERAMICA", "GLI SPECCHI", "LE LAMPADINE", "I BICCHIERI DI CRISTALLO"]) + "\n" +
        nota("💡 TOGLI I <b>TAPPI</b>: IL TAPPO DI METALLO O DI PLASTICA VA NEL BIDONE GIALLO.")),
    slide("⚫ INDIFFERENZIATO: IL BIDONE GRIGIO", nota(
        "NEL BIDONE GRIGIO METTO QUELLO CHE <b>NON SI RICICLA</b>.", "") + "\n" + cards([
        ("🧽", "LA SPUGNA VECCHIA", ""), ("🍽️", "IL PIATTO ROTTO", "DI CERAMICA"), ("👶", "I PANNOLINI", ""),
        ("🪥", "LO SPAZZOLINO", ""), ("🖊️", "LE PENNE", ""), ("🧻", "LA CARTA SPORCA", "")], "g3")),
    slide("⚠️ I RIFIUTI SPECIALI: DOVE LI PORTO?", ill2("rifiuti-speciali.png", "PILE, MEDICINE, VESTITI USATI E UN DIVANO VECCHIO",
        cards([("🔋", "LE PILE", "NEL CONTENITORE PER LE PILE (NEI NEGOZI E NEI SUPERMERCATI)"),
               ("💊", "LE MEDICINE SCADUTE", "NEL CONTENITORE DAVANTI ALLA FARMACIA"),
               ("👕", "I VESTITI USATI", "NEL CASSONETTO DEI VESTITI"),
               ("🛋️", "I MOBILI VECCHI (GLI INGOMBRANTI)", "TELEFONA ALL'AMIU E PRENOTA IL RITIRO, OPPURE PORTALI AL CENTRO DI RACCOLTA")]))),
    slide("🚪 IL PORTA A PORTA", passi([
        "IN MOLTI QUARTIERI DI BARI LA RACCOLTA È <b>PORTA A PORTA</b>: OGNI FAMIGLIA HA I SUOI <b>MASTELLI</b> (PICCOLI BIDONI).",
        "GUARDO IL <b>CALENDARIO</b>: OGNI GIORNO PASSANO PER UN RIFIUTO DIVERSO.",
        "LA SERA PRIMA, <b>DOPO LE 21</b>, METTO IL MASTELLO FUORI DAL PORTONE.",
        "LA MATTINA, DOPO LA RACCOLTA, RIPORTO IL MASTELLO A CASA."]) + "\n" +
        nota("☎️ AMIU PUGLIA, NUMERO VERDE (GRATIS): <b>800 011 558</b>.<br>"
             "🚫 NON LASCIARE I RIFIUTI O I MOBILI VECCHI VICINO AI BIDONI: È VIETATO E C'È LA <b>MULTA</b>.")),
    slide("📖 LE PAROLE UTILI", table([
        ["BUTTARE / GETTARE", "METTERE NEL BIDONE"], ["DIVIDERE / SEPARARE", "METTERE LE COSE IN GRUPPI DIVERSI"],
        ["RICICLARE", "USARE DI NUOVO UN MATERIALE"], ["SCHIACCIARE", "FARE PIÙ PICCOLO (LE BOTTIGLIE, LE SCATOLE)"],
        ["SCIACQUARE", "LAVARE CON UN PO' D'ACQUA"], ["IL CASSONETTO", "IL BIDONE GRANDE IN STRADA"],
        ["IL MASTELLO", "IL BIDONE PICCOLO DI CASA"], ["GLI INGOMBRANTI", "I RIFIUTI GRANDI: MOBILI, MATERASSI, FRIGORIFERI"]],
        head=["PAROLA", "CHE COSA VUOL DIRE"])),
    slide("✏️ L'IMPERATIVO: DARE CONSIGLI E ISTRUZIONI", table([
        ["TU", "BUTT<b>A</b>!", "METT<b>I</b>!", "APR<b>I</b>!"],
        ["NOI", "BUTT<b>IAMO</b>!", "METT<b>IAMO</b>!", "APR<b>IAMO</b>!"],
        ["VOI", "BUTT<b>ATE</b>!", "METT<b>ETE</b>!", "APR<b>ITE</b>!"]], head=["", "BUTTARE", "METTERE", "APRIRE"]) + "\n" +
        nota("TU: <b>-ARE → -A</b> &nbsp; (BUTTA, LAVA, SCHIACCIA)<br>TU: <b>-ERE / -IRE → -I</b> &nbsp; (METTI, PRENDI, APRI)<br>"
             "NOI E VOI: COME IL PRESENTE (BUTTIAMO, METTETE).")),
    slide("🚫 L'IMPERATIVO NEGATIVO", table([
        ["TU", "NON + INFINITO", "NON <b>BUTTARE</b> LA CARTA NEL VETRO!"],
        ["NOI", "NON + PRESENTE", "NON <b>BUTTIAMO</b> I RIFIUTI IN STRADA!"],
        ["VOI", "NON + PRESENTE", "NON <b>METTETE</b> LA PLASTICA NELL'ORGANICO!"]], head=["", "COME?", "ESEMPIO"]) + "\n" +
        nota("ATTENZIONE: <b>FARE → FA'/FAI</b> &nbsp; <b>ANDARE → VA'/VAI</b> &nbsp; <b>ESSERE → SII</b> &nbsp; <b>AVERE → ABBI</b>")),
    slide("🔣 SIMBOLI E SIGLE", table([
        ["+", "E, INSIEME", "CARTA + CARTONE"], ["E/O", "E OPPURE O", "PLASTICA E/O ALLUMINIO"],
        ["ES.", "ESEMPIO", "TETRAPAK (ES. IL LATTE)"], ["ECC.", "ECCETERA (E ALTRE COSE)", "BOTTIGLIE, VASETTI, ECC."],
        ["TEL.", "TELEFONO", "TEL. 800 011 558"]], head=["SIMBOLO", "CHE COSA VUOL DIRE", "ESEMPIO"])),
    slide("🗣️ SUL PIANEROTTOLO", dialogo([
        ("AHMED", "BUONASERA SIGNORA ROSA. SCUSI, UNA DOMANDA: DOVE BUTTO LE BOTTIGLIE DI VETRO?"),
        ("*SIG.RA ROSA", "NEL MASTELLO VERDE. MA TOGLI IL TAPPO!"),
        ("AHMED", "E IL TAPPO DOVE LO METTO?"),
        ("*SIG.RA ROSA", "NEL GIALLO, CON LA PLASTICA E I METALLI."),
        ("AHMED", "GRAZIE. E QUANDO PORTO FUORI IL MASTELLO?"),
        ("*SIG.RA ROSA", "GUARDA IL CALENDARIO: IL VETRO È IL GIOVEDÌ. METTILO FUORI MERCOLEDÌ SERA, DOPO LE NOVE."),
        ("AHMED", "PERFETTO. GRAZIE MILLE, SIGNORA!")])),
    slide("🎬 GUARDA IL VIDEO",
        '    <div class="video"><iframe src="https://www.youtube-nocookie.com/embed/%s" title="La raccolta differenziata" '
        'allow="accelerometer; encrypted-media; gyroscope; picture-in-picture" allowfullscreen loading="lazy"></iframe></div>\n' % VIDEO +
        nota('IL VIDEO NON SI VEDE? <a href="https://www.youtube.com/watch?v=%s" target="_blank" rel="noopener">APRILO SU YOUTUBE</a>.' % VIDEO)),
    end("ORA SAI DOVE BUTTARE I RIFIUTI!"),
]

BIDONI = ["ORGANICO (MARRONE)", "CARTA (BLU)", "PLASTICA E METALLI (GIALLO)", "VETRO (VERDE)", "INDIFFERENZIATO (GRIGIO)"]
O, C, P, V, I = BIDONI

LETTURA = ("🏠 <b>LA FAMIGLIA DI AHMED</b><br>AHMED, SUA MOGLIE SAMIRA E I BAMBINI ABITANO A BARI, NEL QUARTIERE LIBERTÀ. "
           "IN CUCINA HANNO QUATTRO SACCHETTI: PER L'ORGANICO, LA CARTA, LA PLASTICA E IL VETRO. "
           "QUELLO CHE NON SI RICICLA VA NEL SACCHETTO GRIGIO.<br>"
           "IL LUNEDÌ SERA AHMED METTE FUORI IL MASTELLO DELLA CARTA. IL MERCOLEDÌ SERA METTE FUORI IL VETRO.<br>"
           "IERI SAMIRA HA TROVATO UNA SCATOLA DI MEDICINE SCADUTE: LE HA PORTATE AL CONTENITORE DAVANTI ALLA FARMACIA.<br>"
           "IL VECCHIO DIVANO È ROTTO. AHMED NON LO LASCIA IN STRADA: TELEFONA AL NUMERO VERDE DELL'AMIU E PRENOTA IL RITIRO.")

RD = {
 "title": "♻️ La raccolta differenziata · Esercizi",
 "store": "raccolta-differenziata",
 "upper": True,
 "sections": [
  {"part": "I bidoni"},
  menu(BIDONI, [("1. LA BUCCIA DELLA BANANA", O), ("2. IL GIORNALE VECCHIO", C), ("3. LA LATTINA DELLA COCA-COLA", P),
                ("4. LA BOTTIGLIA DEL VINO", V), ("5. LA SPUGNA VECCHIA", I), ("6. LA SCATOLA DEI CIOCCOLATINI", C),
                ("7. IL FLACONE DELLO SHAMPOO", P), ("8. GLI AVANZI DEL PRANZO", O)],
       "1 · Dove lo butto?", "1 · Dove lo butto", "e1", cons="SCEGLI IL BIDONE GIUSTO (I COLORI DI BARI)."),
  menu(BIDONI, [("1. IL VASETTO DELLA MARMELLATA", V), ("2. IL PIATTO ROTTO DI CERAMICA", I), ("3. I GUSCI D'UOVO", O),
                ("4. LA SCATOLETTA DEL TONNO", P), ("5. IL SACCHETTO DI CARTA", C), ("6. I FONDI DEL CAFFÈ", O),
                ("7. LA BOTTIGLIA DELL'ACQUA DI PLASTICA", P), ("8. IL PANNOLINO", I)],
       "2 · Dove lo butto? (2)", "2 · Dove lo butto (2)", "e2", cons="SCEGLI IL BIDONE GIUSTO (I COLORI DI BARI)."),
  scegli([("1. DI CHE COLORE È IL BIDONE DEL VETRO A BARI?", ["VERDE", "BLU", "MARRONE"], "VERDE"),
          ("2. DI CHE COLORE È IL BIDONE DELLA CARTA?", ["BLU", "GIALLO", "GRIGIO"], "BLU"),
          ("3. DI CHE COLORE È IL BIDONE DELL'ORGANICO?", ["MARRONE", "VERDE", "GIALLO"], "MARRONE"),
          ("4. DI CHE COLORE È IL BIDONE DI PLASTICA E METALLI?", ["GIALLO", "BLU", "GRIGIO"], "GIALLO"),
          ("5. DI CHE COLORE È IL BIDONE DELL'INDIFFERENZIATO?", ["GRIGIO", "VERDE", "MARRONE"], "GRIGIO")],
         "3 · I colori dei bidoni", "3 · I colori", "e3"),
  menu(["NEL CONTENITORE PER LE PILE", "NEL CONTENITORE DAVANTI ALLA FARMACIA", "NEL CASSONETTO DEI VESTITI", "TELEFONO ALL'AMIU"],
       [("1. LE PILE DEL TELECOMANDO", "NEL CONTENITORE PER LE PILE"),
        ("2. LE ASPIRINE SCADUTE", "NEL CONTENITORE DAVANTI ALLA FARMACIA"),
        ("3. I PANTALONI PICCOLI E IL CAPPOTTO VECCHIO", "NEL CASSONETTO DEI VESTITI"),
        ("4. IL MATERASSO VECCHIO", "TELEFONO ALL'AMIU")],
       "4 · I rifiuti speciali: dove li porto?", "4 · I rifiuti speciali", "e4"),
  {"id": "e5", "title": "5 · Che cosa va nel vetro?", "short": "5 · Il vetro", "type": "multi",
   "cons": "METTI LA SPUNTA VICINO ALLE 3 COSE GIUSTE.",
   "items": ["LA BOTTIGLIA DELL'OLIO DI VETRO", "LO SPECCHIO ROTTO", "IL BARATTOLO DI VETRO DEI CECI", "LA TAZZA DI CERAMICA",
             "IL VASETTO DI VETRO DELLO YOGURT", "LA LAMPADINA"],
   "k": [eq(a) for a in ["X", "-", "X", "-", "X", "-"]]},

  {"part": "Leggi"},
  vf(["1. LA FAMIGLIA DI AHMED ABITA A BARI.", "2. IN CUCINA HANNO DUE SACCHETTI.",
      "3. IL LUNEDÌ SERA AHMED METTE FUORI LA CARTA.", "4. SAMIRA HA BUTTATO LE MEDICINE NEL BIDONE GRIGIO.",
      "5. AHMED LASCIA IL DIVANO VICINO AI BIDONI.", "6. PER IL DIVANO AHMED TELEFONA AL NUMERO VERDE."],
     ["VERO", "FALSO", "VERO", "FALSO", "FALSO", "VERO"], "6 · Leggi: vero o falso?", "6 · Vero o falso", "e6", info=LETTURA),
  scegli([("1. QUANDO METTE FUORI IL VETRO AHMED?", ["IL MERCOLEDÌ SERA", "IL LUNEDÌ MATTINA", "LA DOMENICA"], "IL MERCOLEDÌ SERA"),
          ("2. DOVE HA PORTATO LE MEDICINE SAMIRA?", ["DAVANTI ALLA FARMACIA", "AL COMUNE", "NEL BIDONE BLU"], "DAVANTI ALLA FARMACIA"),
          ("3. PERCHÉ AHMED TELEFONA ALL'AMIU?", ["PER IL RITIRO DEL DIVANO", "PER COMPRARE UN DIVANO", "PER IL CALENDARIO"], "PER IL RITIRO DEL DIVANO"),
          ("4. IL DIVANO È…", ["UN RIFIUTO INGOMBRANTE", "UN RIFIUTO ORGANICO", "VETRO"], "UN RIFIUTO INGOMBRANTE")],
         "7 · Leggi e rispondi", "7 · Rispondi", "e7", info=LETTURA),

  {"part": "Le parole"},
  completa("1. IL BIDONE GRANDE IN STRADA È IL ___.<br>2. IL BIDONE PICCOLO DI CASA È IL ___.<br>"
           "3. I MOBILI VECCHI E I MATERASSI SONO GLI ___.<br>4. USARE DI NUOVO UN MATERIALE VUOL DIRE ___.<br>"
           "5. PRIMA DI BUTTARE LA BOTTIGLIA, LA ___ COSÌ È PIÙ PICCOLA.<br>6. I RESTI DEL CAFFÈ SONO I ___ DEL CAFFÈ.",
           ["cassonetto", "mastello", "ingombranti", "riciclare", "schiaccio", "fondi"],
           "8 · Completa con la parola giusta", "8 · Le parole", "e8",
           bank="MASTELLO · RICICLARE · FONDI · CASSONETTO · SCHIACCIO · INGOMBRANTI"),
  ordina(["SVUOTO LA BOTTIGLIA DI PLASTICA.", "SCHIACCIO LA BOTTIGLIA.", "CHIUDO LA BOTTIGLIA CON IL TAPPO.",
          "LA METTO NEL MASTELLO GIALLO.", "LA SERA METTO FUORI IL MASTELLO."],
         "9 · Metti in ordine: la bottiglia di plastica", "9 · In ordine", "e9"),
  menu(["E, INSIEME", "E OPPURE O", "ESEMPIO", "E ALTRE COSE", "TELEFONO"],
       [("1. +", "E, INSIEME"), ("2. E/O", "E OPPURE O"), ("3. ES.", "ESEMPIO"), ("4. ECC.", "E ALTRE COSE"), ("5. TEL.", "TELEFONO")],
       "10 · Simboli e sigle: che cosa vogliono dire?", "10 · Simboli e sigle", "e10"),

  {"part": "L'imperativo"},
  scrivi([("1. (TU - BUTTARE) ___ LA CARTA NEL BIDONE BLU.", ["butta"]),
          ("2. (TU - METTERE) ___ IL VETRO NEL BIDONE VERDE.", ["metti"]),
          ("3. (VOI - LAVARE) ___ I VASETTI PRIMA DI BUTTARLI.", ["lavate"]),
          ("4. (TU - SCHIACCIARE) ___ LE SCATOLE DI CARTONE.", ["schiaccia"]),
          ("5. (NOI - DIVIDERE) ___ BENE I RIFIUTI!", ["dividiamo"]),
          ("6. (VOI - LEGGERE) ___ IL CALENDARIO DELLA RACCOLTA.", ["leggete"]),
          ("7. (TU - PRENDERE) ___ I SACCHETTI COMPOSTABILI AL SUPERMERCATO.", ["prendi"]),
          ("8. (VOI - USARE) ___ LA BORSA DELLA SPESA DI STOFFA.", ["usate"])],
         "11 · Scrivi l'imperativo", "11 · L'imperativo", "e11", cons="SCRIVI IL VERBO ALL'IMPERATIVO."),
  scegli([("1. TU ___ I RIFIUTI IN STRADA!", ["NON BUTTARE", "NON BUTTA", "NON BUTTI"], "NON BUTTARE"),
          ("2. VOI ___ LA PLASTICA NELL'ORGANICO!", ["NON METTETE", "NON METTERE", "NON METTI"], "NON METTETE"),
          ("3. AHMED, ___ IL TAPPO DALLA BOTTIGLIA!", ["TOGLI", "TOGLIERE", "TOGLIETE"], "TOGLI"),
          ("4. TU ___ ATTENZIONE AL CALENDARIO!", ["FAI", "FARE", "FATE"], "FAI"),
          ("5. TU ___ LE MEDICINE IN FARMACIA!", ["PORTA", "PORTI", "PORTARE"], "PORTA"),
          ("6. TU ___ IL DIVANO VICINO AI BIDONI!", ["NON LASCIARE", "NON LASCIA", "NON LASCI"], "NON LASCIARE")],
         "12 · Scegli la forma giusta", "12 · Scegli", "e12"),

  {"part": "Parlare"},
  completa("AHMED: SCUSI SIGNORA, DOVE ___ LE BOTTIGLIE DI VETRO?<br>SIG.RA ROSA: NEL MASTELLO ___. MA TOGLI IL ___!<br>"
           "AHMED: E QUANDO METTO FUORI IL MASTELLO?<br>SIG.RA ROSA: GUARDA IL ___: IL VETRO È IL GIOVEDÌ.<br>AHMED: GRAZIE ___, SIGNORA!",
           ["butto", "verde", "tappo", "calendario", "mille"],
           "13 · Sul pianerottolo: completa il dialogo", "13 · Il dialogo", "e13",
           bank="TAPPO · MILLE · BUTTO · CALENDARIO · VERDE"),
  parla("e14", 14, "SPIEGA A UN AMICO APPENA ARRIVATO A BARI DOVE BUTTA LA CARTA, LA PLASTICA, IL VETRO, L'ORGANICO E LE PILE. USA L'IMPERATIVO: «BUTTA…», «METTI…», «NON…»."),
  libero("e15", 15, "E nel tuo paese?", "COME BUTTI LA SPAZZATURA NEL TUO PAESE? C'È LA RACCOLTA DIFFERENZIATA? SCRIVI 3 O 4 FRASI.",
         [""], rows=4),
 ]
}

SLIDE_RIFIUTI = [("raccolta-differenziata/index.html", "LA RACCOLTA DIFFERENZIATA", TOP, SLIDE_RD, CSS)]
ESERCIZI_RIFIUTI = [("raccolta-differenziata", RD)]
