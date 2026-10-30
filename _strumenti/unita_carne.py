"""I TIPI DI CARNE E I NOMI DEI TAGLI (cucina, A1), 2026-10-30.
Traccia: l'unità «Dal macellaio» mandata da Erila (animale → nome della carne, pesi, vorrei, partitivo).
Testi, disegni ed esercizi scritti per il sito, in STAMPATELLO MAIUSCOLO. I disegni dei tagli sono SVG fatti qui;
le foto sono quelle di comune/cibi/ (Wikimedia Commons, crediti nella slide «Le foto»).
Uso: python3 _strumenti/slide.py e python3 _strumenti/genera.py"""
from genera import eq
from unita_primi import cover, slide, cards, table, nota, dialogo, end
from unita_drive import ILL_CSS, vf, scegli, menu, scrivi, completa, parla
from foto_cibi import foto, crediti_slide, foto_quiz, FOTO_CSS
from teoria import tab, es

TOP = "CUCINA &bull; A1"

CSS = ILL_CSS + FOTO_CSS + """
  .taglio{display:grid; grid-template-columns:1.15fr 1fr; gap:18px; align-items:center;}
  .taglio svg{width:100%; height:auto; max-height:50vh; display:block;}
  .taglio table.plur{font-size:1.05rem;}
  .taglio table.plur td{padding:6px 10px; text-align:left;}
  .taglio table.plur td:first-child{text-align:center; width:44px;}
  .n{display:inline-block; width:30px; height:30px; border-radius:50%; line-height:27px; text-align:center; font-weight:bold; border:2px solid #333; color:#222;}
  .card .emoji img.cibo{height:110px;}
  table.plur td img.cibo{width:90px; height:64px;}
  @media (max-width:900px){ .taglio{grid-template-columns:1fr;} .taglio svg{max-height:34vh;} .taglio table.plur{font-size:.95rem;}
    .card .emoji img.cibo{height:80px;} table.plur td img.cibo{width:60px; height:46px;} }"""

COLORI = ["#f4a3a3", "#f7c08a", "#f9e08b", "#c9e59a", "#9fd8cf", "#a9c8f2", "#c9b3ee", "#f2b3d6"]

def _pt(p): return " ".join("%d,%d" % xy for xy in p)

def _marker(n, x, y, r=15):
    return ('<circle cx="%d" cy="%d" r="%d" fill="#fff" stroke="#333" stroke-width="2"/>'
            '<text x="%d" y="%d" text-anchor="middle" font-size="%d" font-weight="bold" font-family="Arial" fill="#222">%d</text>'
            % (x, y, r, x, y + r * 0.38, r * 1.1, n))

def quadrupede(cid, alt, zone, coda, testa, gambe_y, pelle, zoccolo, stinco):
    """zone: [(punti, (x, y) del numero)]; l'ultimo numero (stinco) va sulle zampe"""
    legs = ""
    for x in (160, 215, 440, 495):
        legs += '<rect x="%d" y="240" width="32" height="%d" rx="6" fill="%s" stroke="#fff" stroke-width="2"/>' % (x, gambe_y - 240, COLORI[len(zone)])
        legs += '<rect x="%d" y="%d" width="32" height="16" rx="4" fill="%s"/>' % (x, gambe_y - 16, zoccolo)
    body = "".join('<polygon points="%s" fill="%s" stroke="#fff" stroke-width="3"/>' % (_pt(p), COLORI[i]) for i, (p, _) in enumerate(zone))
    nums = "".join(_marker(i + 1, x, y) for i, (_, (x, y)) in enumerate(zone))
    nums += _marker(len(zone) + 1, 176, 270, 13) if stinco else ""
    return ('<svg viewBox="0 0 590 %d" role="img" aria-label="%s" xmlns="http://www.w3.org/2000/svg">'
            '<defs><clipPath id="c%s"><rect x="125" y="74" width="420" height="186" rx="48"/></clipPath></defs>'
            '%s%s<g clip-path="url(#c%s)">%s</g>'
            '<rect x="125" y="74" width="420" height="186" rx="48" fill="none" stroke="#555" stroke-width="3"/>%s%s</svg>'
            % (gambe_y + 6, alt, cid, coda, legs, cid, body, testa % pelle, nums))

MUCCA = quadrupede("manzo", "IL MANZO: I TAGLI", [
    ([(120, 70), (200, 70), (195, 168), (120, 168)], (160, 120)),             # collo
    ([(200, 70), (280, 70), (275, 175), (195, 168)], (238, 120)),             # spalla
    ([(120, 168), (195, 168), (275, 175), (270, 265), (120, 265)], (200, 222)),  # petto
    ([(280, 70), (360, 70), (360, 165), (275, 175)], (318, 120)),             # costata
    ([(275, 175), (360, 165), (430, 170), (430, 265), (270, 265)], (352, 220)),  # pancia
    ([(360, 70), (440, 70), (430, 170), (360, 165)], (398, 118)),             # lombata e filetto
    ([(440, 70), (550, 70), (550, 265), (430, 265), (430, 170)], (488, 165)),  # coscia
], '<path d="M548,95 Q585,150 568,225" fill="none" stroke="#555" stroke-width="6" stroke-linecap="round"/>'
   '<circle cx="568" cy="230" r="9" fill="#555"/>',
   '<path d="M150,95 L98,78 Q70,76 58,96 L36,142 Q34,166 60,168 L100,166 Q130,160 152,150 Z" fill="%s" stroke="#555" stroke-width="3"/>'
   '<path d="M92,80 Q86,50 104,40" fill="none" stroke="#c9a66b" stroke-width="7" stroke-linecap="round"/>'
   '<ellipse cx="125" cy="90" rx="18" ry="9" fill="#e9d8c4" stroke="#555" stroke-width="2"/>'
   '<circle cx="84" cy="108" r="6" fill="#333"/><ellipse cx="48" cy="152" rx="9" ry="6" fill="#555"/>',
   320, "#e9d8c4", "#555", True)

MAIALE = quadrupede("maiale", "IL MAIALE: I TAGLI", [
    ([(120, 70), (200, 70), (200, 168), (120, 168)], (162, 120)),             # collo
    ([(200, 70), (270, 70), (270, 265), (120, 265), (120, 168), (200, 168)], (222, 215)),  # spalla
    ([(270, 70), (440, 70), (440, 150), (270, 150)], (355, 112)),             # lonza
    ([(270, 150), (360, 150), (360, 265), (270, 265)], (315, 208)),           # costine
    ([(360, 150), (440, 150), (440, 265), (360, 265)], (400, 208)),           # pancetta
    ([(440, 70), (550, 70), (550, 265), (440, 265)], (492, 165)),             # coscia
], '<path d="M548,110 q24,-6 16,12 q-8,16 10,14" fill="none" stroke="#c76b86" stroke-width="5" stroke-linecap="round"/>',
   '<path d="M152,98 Q112,84 78,104 L46,124 Q34,132 36,146 Q40,162 56,162 L84,166 Q118,176 152,164 Z" fill="%s" stroke="#555" stroke-width="3"/>'
   '<polygon points="106,96 124,62 140,100" fill="#f5b8c8" stroke="#555" stroke-width="3"/>'
   '<ellipse cx="38" cy="143" rx="10" ry="17" fill="#e98fa8" stroke="#555" stroke-width="2"/>'
   '<circle cx="36" cy="136" r="2.5" fill="#555"/><circle cx="36" cy="150" r="2.5" fill="#555"/><circle cx="84" cy="118" r="6" fill="#333"/>',
   300, "#f5b8c8", "#8a5a44", True)

POLLO = ('<svg viewBox="0 0 430 330" role="img" aria-label="IL POLLO: I PEZZI" xmlns="http://www.w3.org/2000/svg">'
         '<defs><clipPath id="cpollo"><ellipse cx="215" cy="170" rx="140" ry="92"/></clipPath></defs>'
         # zampe
         '<path d="M240,285 L236,318 M236,318 l-14,6 M236,318 l14,6 M282,285 L284,318 M284,318 l-14,6 M284,318 l14,6" stroke="#e8a53a" stroke-width="6" stroke-linecap="round"/>'
         '<path d="M222,236 Q228,300 246,292 Q262,286 258,236 Z" fill="%s" stroke="#fff" stroke-width="3"/>'
         '<path d="M266,236 Q270,300 288,292 Q304,286 300,236 Z" fill="%s" stroke="#fff" stroke-width="3"/>'
         # coda
         '<path d="M345,140 Q395,80 405,110 Q410,150 350,190 Z" fill="#f3e3c3" stroke="#555" stroke-width="3"/>'
         '<g clip-path="url(#cpollo)">'
         '<rect x="60" y="60" width="320" height="230" fill="#f3e3c3"/>'
         '<polygon points="60,110 200,105 205,270 60,270" fill="%s" stroke="#fff" stroke-width="3"/>'
         '<polygon points="205,192 370,192 370,270 205,270" fill="%s" stroke="#fff" stroke-width="3"/>'
         '</g>'
         '<ellipse cx="215" cy="170" rx="140" ry="92" fill="none" stroke="#555" stroke-width="3"/>'
         # ala
         '<path d="M205,118 Q300,96 338,140 Q318,190 214,186 Q196,150 205,118 Z" fill="%s" stroke="#555" stroke-width="3"/>'
         # testa
         '<path d="M88,150 Q78,110 96,82 L128,88 Q120,120 128,140 Z" fill="#f3e3c3" stroke="#555" stroke-width="3"/>'
         '<circle cx="104" cy="74" r="30" fill="#f3e3c3" stroke="#555" stroke-width="3"/>'
         '<path d="M84,50 q6,-20 14,-4 q8,-20 14,-2 q10,-14 12,6 Z" fill="#e0453a" stroke="#555" stroke-width="2"/>'
         '<polygon points="76,72 52,82 78,88" fill="#e8a53a" stroke="#555" stroke-width="2"/>'
         '<path d="M80,92 q-4,18 8,18 q8,-6 2,-18 Z" fill="#e0453a"/><circle cx="98" cy="68" r="5" fill="#333"/>'
         % (COLORI[3], COLORI[3], COLORI[0], COLORI[2], COLORI[1]) +
         _marker(1, 135, 200) + _marker(2, 272, 148) + _marker(3, 300, 225) + _marker(4, 262, 268, 13) + '</svg>')

def legenda(righe):
    return table([['<span class="n" style="background:%s">%d</span>' % (COLORI[i], i + 1), "<b>%s</b><br>%s" % r]
                  for i, r in enumerate(righe)], head=["", "IL PEZZO · CHE COSA FAI"])

def legenda_pollo(righe):
    col = [COLORI[0], COLORI[1], COLORI[2], COLORI[3]]
    return table([['<span class="n" style="background:%s">%d</span>' % (col[i], i + 1), "<b>%s</b><br>%s" % r]
                  for i, r in enumerate(righe)], head=["", "IL PEZZO · CHE COSA FAI"])

def taglio(svg, leg):
    return '    <div class="taglio">\n    %s\n%s\n    </div>' % (svg, leg)

FOTO = ["pollo", "tacchino", "coniglio", "bistecca-manzo", "macinato", "braciola-maiale", "salsiccia", "prosciutto-crudo", "costolette-agnello"]

PARTITIVO = (tab(("IL POLLO", "<b>DEL</b> POLLO"), ("LO SPEZZATINO", "<b>DELLO</b> SPEZZATINO"), ("LA CARNE", "<b>DELLA</b> CARNE"),
                 ("L'AGNELLO", "<b>DELL'</b>AGNELLO"), ("I PETTI", "<b>DEI</b> PETTI"), ("GLI HAMBURGER", "<b>DEGLI</b> HAMBURGER"),
                 ("LE SALSICCE", "<b>DELLE</b> SALSICCE"), head=("L'ARTICOLO", "DI + ARTICOLO")) +
             "DEL, DELLA, DEI… VUOL DIRE <b>UN PO' DI</b> (UNA QUANTITÀ NON PRECISA).<br>"
             "<b>VORREI</b> = VOGLIO, MA PIÙ GENTILE. <b>NE</b> = DI QUELLA COSA." +
             es("VORREI DELLA CARNE PER IL RAGÙ.", "IL MACINATO? NE PRENDO TRE ETTI."))

TIPI_SLIDE = [
    cover("🥩", "I TIPI DI CARNE", "DALL'ANIMALE AL PIATTO: I NOMI DELLA CARNE E DEI PEZZI", "CIBO &bull; A1"),
    slide("CHE COSA IMPARIAMO?", cards([
        ("🐄", "ANIMALE E CARNE", "LA MUCCA → IL MANZO"), ("🔪", "I PEZZI (I TAGLI)", "IL FILETTO, IL PETTO, LA COSCIA…"),
        ("⚖️", "QUANTO?", "UN ETTO, MEZZO CHILO, UN CHILO"), ("🗣️", "CHIEDERE", "VORREI DEL POLLO, DELLA CARNE…")])),
    slide("🐾 L'ANIMALE E LA CARNE", table([
        ["🐄 🐂", "LA MUCCA, IL BUE", "<b>IL MANZO</b>", "CARNE ROSSA"],
        ["🐄", "IL VITELLO (LA MUCCA PICCOLA)", "<b>IL VITELLO</b>", "CHIARA E TENERA"],
        ["🐖", "IL MAIALE", "<b>IL MAIALE</b> (LA CARNE SUINA)", "SALSICCE, PROSCIUTTO"],
        ["🐑", "L'AGNELLO (LA PECORA PICCOLA)", "<b>L'AGNELLO</b>", "A PASQUA"],
        ["🐐", "IL CAPRETTO (LA CAPRA PICCOLA)", "<b>IL CAPRETTO</b>", "A PASQUA"],
        ["🐔", "LA GALLINA, IL GALLO", "<b>IL POLLO</b>", "CARNE BIANCA"],
        ["🦃", "IL TACCHINO", "<b>IL TACCHINO</b>", "CARNE BIANCA"],
        ["🐇", "IL CONIGLIO", "<b>IL CONIGLIO</b>", "CARNE BIANCA"],
        ["🐎", "IL CAVALLO", "<b>IL CAVALLO</b>", "A BARI SI MANGIA MOLTO"]],
        head=["", "L'ANIMALE", "LA CARNE", "COM'È?"]) + "\n" +
        nota("☝️ <b>IL MANZO</b> È LA CARNE DELLA MUCCA E DEL BUE. AL SUPERMERCATO C'È SCRITTO ANCHE <b>CARNE BOVINA</b>.")),
    slide("🔴 CARNE ROSSA E ⚪ CARNE BIANCA", cards([
        (foto("bistecca-manzo"), "🔴 CARNE ROSSA", "IL MANZO, L'AGNELLO, IL CAVALLO"),
        (foto("pollo"), "⚪ CARNE BIANCA", "IL POLLO, IL TACCHINO, IL CONIGLIO")]) + "\n" +
        nota("IL VITELLO E IL MAIALE SONO PIÙ CHIARI DEL MANZO. I MEDICI DICONO: POCA CARNE ROSSA, POCHI SALUMI.")),
    slide("🐄 IL MANZO E IL VITELLO: I TAGLI", taglio(MUCCA, legenda([
        ("IL COLLO", "BOLLITO, BRODO"), ("LA SPALLA", "SPEZZATINO, ARROSTO"), ("IL PETTO", "BOLLITO"),
        ("LA COSTATA", "BISTECCA CON L'OSSO, ALLA GRIGLIA"), ("LA PANCIA", "MACINATO, BOLLITO"),
        ("LA LOMBATA E IL FILETTO", "BISTECCHE, FILETTO (IL PIÙ TENERO!)"), ("LA COSCIA", "FETTINE, COTOLETTE, ARROSTO"),
        ("LO STINCO", "L'OSSOBUCO")]))),
    slide("🔪 CHE COSA COMPRO DAL MANZO?", cards([
        (foto("bistecca-manzo"), "LA BISTECCA", "UNA FETTA ALTA, IN PADELLA O ALLA GRIGLIA"),
        ("🥓", "LE FETTINE", "FETTE SOTTILI, 2 MINUTI IN PADELLA"),
        ("🍲", "LO SPEZZATINO", "PEZZI PICCOLI, UN'ORA NEL SUGO"),
        (foto("macinato"), "IL MACINATO", "PER IL RAGÙ, LE POLPETTE, GLI HAMBURGER"),
        ("🔥", "L'ARROSTO", "UN PEZZO GRANDE, NEL FORNO"),
        ("🦴", "L'OSSOBUCO", "UNA FETTA DI STINCO CON L'OSSO")], "g3")),
    slide("🐖 IL MAIALE: I TAGLI", taglio(MAIALE, legenda([
        ("IL COLLO (LA COPPA)", "ARROSTO, ALLA GRIGLIA"), ("LA SPALLA", "ARROSTO, SALSICCE"),
        ("LA LONZA", "LE BRACIOLE, L'ARISTA (ARROSTO)"), ("LE COSTINE", "ALLA GRIGLIA"),
        ("LA PANCETTA", "PER LA PASTA (CARBONARA)"), ("LA COSCIA", "IL PROSCIUTTO"), ("LO STINCO", "AL FORNO")])) + "\n" +
        nota("☪️ NON MANGI IL MAIALE? CHIEDI SEMPRE: «C'È IL MAIALE DENTRO?» LE SALSICCE E I SALUMI SONO QUASI SEMPRE DI MAIALE.")),
    slide("🐔 IL POLLO: I PEZZI", taglio(POLLO, legenda_pollo([
        ("IL PETTO", "FETTINE, COTOLETTE, SPIEDINI"), ("LE ALI", "AL FORNO, FRITTE"),
        ("LA SOVRACOSCIA", "AL FORNO, IN UMIDO"), ("IL FUSO", "AL FORNO, ALLA GRIGLIA")])) + "\n" +
        nota("☝️ <b>LA COSCIA</b> = LA SOVRACOSCIA + IL FUSO. IL POLLO <b>INTERO</b> SI CUOCE NEL FORNO (POLLO ARROSTO).")),
    slide("🐑 L'AGNELLO, IL TACCHINO, IL CONIGLIO", cards([
        (foto("costolette-agnello"), "L'AGNELLO", "LE COSTOLETTE, IL COSCIOTTO, LA SPALLA"),
        (foto("tacchino"), "IL TACCHINO", "IL PETTO A FETTINE (LA FESA DI TACCHINO)"),
        (foto("coniglio"), "IL CONIGLIO", "INTERO O A PEZZI, IN UMIDO")], "g3")),
    slide("✂️ COME LA VUOLE?", cards([
        ("🔪", "A FETTE / A FETTINE", "SPESSE O SOTTILI"), ("🧊", "A PEZZI", "PER LO SPEZZATINO"),
        ("🌀", "MACINATA", "LA CARNE TRITATA"), ("🍗", "INTERO", "TUTTO IL POLLO"),
        ("🦴", "CON L'OSSO / SENZA OSSO", "LA COSTATA HA L'OSSO"), ("🍞", "IMPANATA", "CON IL PANE GRATTUGIATO: LA COTOLETTA")], "g3") + "\n" +
        nota("IL MACELLAIO CHIEDE: «<b>COME LA VUOLE?</b>» TU DICI: «A FETTINE SOTTILI, PER FAVORE.»")),
    slide("💙 LA CARNE A BARI", cards([
        ("🍝", "LE BRACIOLE AL RAGÙ", "FETTINE DI CARNE ARROTOLATE CON FORMAGGIO E PREZZEMOLO, COTTE NEL SUGO. LA DOMENICA!"),
        ("🔥", "LE BOMBETTE", "PICCOLI INVOLTINI DI MAIALE CON IL FORMAGGIO, ALLA BRACE"),
        ("🐎", "I PEZZETTI DI CAVALLO", "CARNE DI CAVALLO A PEZZI, COTTA PIANO NEL SUGO"),
        ("🐑", "L'AGNELLO AL FORNO", "CON LE PATATE, A PASQUA")]) + "\n" +
        nota("⚠️ A BARI <b>LA BRACIOLA</b> È L'INVOLTINO DI CARNE AL SUGO. IN ALTRE CITTÀ È UNA FETTA DI MAIALE CON L'OSSO.")),
    slide("⚖️ QUANTO NE VUOLE?", table([
        ["100 GRAMMI", "<b>UN ETTO</b>", "UN ETTO DI PROSCIUTTO"], ["200 / 300 GRAMMI", "<b>DUE ETTI / TRE ETTI</b>", "TRE ETTI DI MACINATO"],
        ["500 GRAMMI", "<b>MEZZO CHILO</b>", "MEZZO CHILO DI SPEZZATINO"], ["1000 GRAMMI", "<b>UN CHILO</b>", "UN CHILO DI SALSICCE"],
        ["1500 GRAMMI", "<b>UN CHILO E MEZZO</b>", "UN POLLO INTERO"]], head=["IL PESO", "COME SI DICE", "ESEMPIO"]) + "\n" +
        nota("1 PERSONA MANGIA CIRCA <b>UN ETTO E MEZZO</b> DI CARNE (150 GRAMMI).")),
    slide("📘 LA REGOLA: VORREI DEL POLLO", table([
        ["IL POLLO", "<b>DEL</b> POLLO"], ["LO SPEZZATINO", "<b>DELLO</b> SPEZZATINO"], ["LA CARNE", "<b>DELLA</b> CARNE"],
        ["L'AGNELLO", "<b>DELL'</b>AGNELLO"], ["I PETTI", "<b>DEI</b> PETTI"], ["GLI HAMBURGER", "<b>DEGLI</b> HAMBURGER"], ["LE SALSICCE", "<b>DELLE</b> SALSICCE"]],
        head=["L'ARTICOLO", "DI + ARTICOLO"]) + "\n" +
        nota("DEL, DELLA, DEI… = <b>UN PO' DI</b>.<br><b>VORREI</b> = VOGLIO, MA PIÙ GENTILE: «VORREI DELLA CARNE PER IL RAGÙ.»<br>"
             "<b>NE</b> = DI QUELLA COSA: «IL MACINATO? NE PRENDO TRE ETTI.»")),
    slide("🗣️ DAL MACELLAIO", dialogo([
        ("*MACELLAIO", "BUONGIORNO, SIGNORA. CHE COSA LE DO?"),
        ("AMINA", "BUONGIORNO. VORREI DEL MANZO PER IL RAGÙ."),
        ("*MACELLAIO", "MACINATO O SPEZZATINO?"),
        ("AMINA", "SPEZZATINO, GRAZIE. MEZZO CHILO."),
        ("*MACELLAIO", "ECCO. DESIDERA ALTRO?"),
        ("AMINA", "SÌ, VORREI ANCHE DEL PETTO DI POLLO."),
        ("*MACELLAIO", "QUANTO NE VUOLE? E COME LO VUOLE?"),
        ("AMINA", "TRE ETTI, A FETTINE SOTTILI."),
        ("*MACELLAIO", "OGGI ABBIAMO DELLE COSTOLETTE D'AGNELLO BUONISSIME."),
        ("AMINA", "NO, GRAZIE. BASTA COSÌ. QUANTO PAGO?"),
        ("*MACELLAIO", "11 EURO E 80.")])),
    slide("📷 LE FOTO", crediti_slide(FOTO) + "\n" + nota("I DISEGNI DEI TAGLI SONO FATTI PER QUESTO SITO.", "margin-top:12px;font-size:.9rem")),
    end("ORA CONOSCI I TIPI DI CARNE E I NOMI DEI PEZZI!"),
]

TIPI = {
 "title": "🥩 I tipi di carne · Esercizi", "store": "tipi-di-carne", "upper": True,
 "sections": [
  {"part": "L'animale e la carne"},
  menu(["IL MANZO", "IL VITELLO", "IL MAIALE", "L'AGNELLO", "IL CAPRETTO", "IL POLLO"],
       [("1. 🐄 LA MUCCA ADULTA E IL BUE: LA CARNE È…", "IL MANZO"), ("2. 🐄 LA MUCCA PICCOLA: LA CARNE È…", "IL VITELLO"),
        ("3. 🐑 LA PECORA PICCOLA: LA CARNE È…", "L'AGNELLO"), ("4. 🐐 LA CAPRA PICCOLA: LA CARNE È…", "IL CAPRETTO"),
        ("5. 🐔 LA GALLINA E IL GALLO: LA CARNE È…", "IL POLLO"), ("6. 🐖 LA CARNE DEL PROSCIUTTO E DELLE SALSICCE È…", "IL MAIALE")],
       "1 · Che carne è?", "1 · Animale e carne", "e1"),
  menu(["CARNE ROSSA", "CARNE BIANCA"],
       [("1. IL MANZO", "CARNE ROSSA"), ("2. IL POLLO", "CARNE BIANCA"), ("3. L'AGNELLO", "CARNE ROSSA"),
        ("4. IL TACCHINO", "CARNE BIANCA"), ("5. IL CONIGLIO", "CARNE BIANCA"), ("6. IL CAVALLO", "CARNE ROSSA")],
       "2 · Rossa o bianca?", "2 · Rossa o bianca", "e2"),
  foto_quiz("f1", "3 · Guarda la foto: che cos'è?", "3 · Le foto",
            [("pollo", "IL POLLO INTERO"), ("bistecca-manzo", "LA BISTECCA"), ("costolette-agnello", "LE COSTOLETTE D'AGNELLO"),
             ("braciola-maiale", "LA BRACIOLA DI MAIALE"), ("macinato", "IL MACINATO"), ("coniglio", "IL CONIGLIO")],
            ["IL MACINATO", "IL CONIGLIO", "IL POLLO INTERO", "LA BISTECCA", "LA BRACIOLA DI MAIALE", "LE COSTOLETTE D'AGNELLO"]),
  {"part": "I pezzi (i tagli)"},
  scegli([("1. PER IL RAGÙ E LE POLPETTE COMPRO…", ["IL MACINATO", "IL FILETTO", "LE ALI"], "IL MACINATO"),
          ("2. FETTE SOTTILI: 2 MINUTI IN PADELLA. SONO…", ["L'ARROSTO", "LE FETTINE", "LO STINCO"], "LE FETTINE"),
          ("3. PEZZI PICCOLI DI CARNE, UN'ORA NEL SUGO. È…", ["LA BISTECCA", "IL PETTO", "LO SPEZZATINO"], "LO SPEZZATINO"),
          ("4. UN PEZZO GRANDE DI CARNE NEL FORNO. È…", ["L'ARROSTO", "IL MACINATO", "LE FETTINE"], "L'ARROSTO"),
          ("5. IL PEZZO DI MANZO PIÙ TENERO (COSTA MOLTO). È…", ["IL COLLO", "IL FILETTO", "LO STINCO"], "IL FILETTO"),
          ("6. UNA FETTA DI STINCO CON L'OSSO. È…", ["L'OSSOBUCO", "LA COTOLETTA", "LA PANCETTA"], "L'OSSOBUCO"),
          ("7. LA CARNE BIANCA DEL POLLO, SENZA OSSO. È…", ["LE ALI", "IL FUSO", "IL PETTO"], "IL PETTO")],
         "4 · Quale pezzo?", "4 · Quale pezzo", "e4"),
  menu(["MANZO", "VITELLO", "MAIALE", "POLLO", "AGNELLO"],
       [("1. LE ALI", "POLLO"), ("2. LA PANCETTA", "MAIALE"), ("3. LA COSTATA PER LA GRIGLIA", "MANZO"), ("4. IL PROSCIUTTO", "MAIALE"),
        ("5. LE COSTOLETTE DI PASQUA", "AGNELLO"), ("6. IL FUSO", "POLLO"), ("7. LA LONZA E LE COSTINE", "MAIALE"), ("8. L'OSSOBUCO", "VITELLO")],
       "5 · Di che animale è?", "5 · Di che animale", "e5"),
  scrivi([("1. LA COSCIA DEL POLLO = LA SOVRACOSCIA + IL …", ["fuso", "il fuso"]),
          ("2. LA CARNE TRITATA PER IL RAGÙ: IL …", ["macinato", "il macinato"]),
          ("3. A BARI: FETTINE ARROTOLATE CON IL FORMAGGIO, NEL SUGO: LE …", ["braciole", "le braciole"]),
          ("4. LA COSCIA DEL MAIALE DIVENTA IL …", ["prosciutto", "il prosciutto"]),
          ("5. LA FETTINA CON IL PANE GRATTUGIATO, FRITTA: LA …", ["cotoletta", "la cotoletta"])],
         "6 · Scrivi la parola", "6 · Le parole", "e6", bank="BRACIOLE · COTOLETTA · FUSO · MACINATO · PROSCIUTTO"),
  {"part": "Quanto?"},
  scrivi([("1. 100 GRAMMI =", ["un etto", "1 etto"]), ("2. 200 GRAMMI =", ["due etti", "2 etti"]), ("3. 300 GRAMMI =", ["tre etti", "3 etti"]),
          ("4. 500 GRAMMI =", ["mezzo chilo", "mezzo kg"]), ("5. 1000 GRAMMI =", ["un chilo", "1 chilo", "un kg", "1 kg"]),
          ("6. 1500 GRAMMI =", ["un chilo e mezzo", "1 chilo e mezzo"])],
         "7 · Scrivi il peso in parole", "7 · I pesi", "e7", bank="UN ETTO · DUE ETTI · TRE ETTI · MEZZO CHILO · UN CHILO · UN CHILO E MEZZO"),
  {"part": "Vorrei del pollo", "teoria": PARTITIVO},
  menu(["DEL", "DELLO", "DELLA", "DELL'", "DEI", "DEGLI", "DELLE"],
       [("1. VORREI ___ POLLO.", "DEL"), ("2. VORREI ___ CARNE MACINATA.", "DELLA"), ("3. VORREI ___ SALSICCE.", "DELLE"),
        ("4. VORREI ___ AGNELLO.", "DELL'"), ("5. VORREI ___ HAMBURGER.", "DEGLI"), ("6. VORREI ___ SPEZZATINO.", "DELLO"),
        ("7. VORREI ___ PETTI DI POLLO.", "DEI"), ("8. VORREI ___ FETTINE DI VITELLO.", "DELLE")],
       "8 · Del, della, dei…?", "8 · Il partitivo", "e8"),
  scegli([("1. AL BANCO, CON GENTILEZZA, DICO:", ["VOGLIO LA CARNE!", "VORREI DELLA CARNE, PER FAVORE.", "DAMMI CARNE."], "VORREI DELLA CARNE, PER FAVORE."),
          ("2. IL MACINATO? ___ PRENDO TRE ETTI.", ["NE", "LO", "CI"], "NE"),
          ("3. IL MACELLAIO CHIEDE IL PESO:", ["COME LA VUOLE?", "QUANTO NE VUOLE?", "DI DOV'È?"], "QUANTO NE VUOLE?")],
         "9 · Scegli la frase giusta", "9 · Vorrei, ne", "e9"),
  {"part": "Dal macellaio"},
  vf(["1. AMINA COMPRA LA CARNE PER IL RAGÙ.", "2. AMINA PRENDE IL MACINATO.", "3. VUOLE IL POLLO A FETTINE SOTTILI.",
      "4. PRENDE UN CHILO DI POLLO.", "5. COMPRA ANCHE LE COSTOLETTE D'AGNELLO."],
     ["VERO", "FALSO", "VERO", "FALSO", "FALSO"], "10 · Leggi: vero o falso?", "10 · Il dialogo", "e10",
     info="MACELLAIO: BUONGIORNO, SIGNORA. CHE COSA LE DO?<br>AMINA: BUONGIORNO. VORREI DEL MANZO PER IL RAGÙ.<br>MACELLAIO: MACINATO O SPEZZATINO?<br>"
          "AMINA: SPEZZATINO, GRAZIE. MEZZO CHILO.<br>MACELLAIO: ECCO. DESIDERA ALTRO?<br>AMINA: SÌ, VORREI ANCHE DEL PETTO DI POLLO.<br>"
          "MACELLAIO: QUANTO NE VUOLE? E COME LO VUOLE?<br>AMINA: TRE ETTI, A FETTINE SOTTILI.<br>"
          "MACELLAIO: OGGI ABBIAMO DELLE COSTOLETTE D'AGNELLO BUONISSIME.<br>AMINA: NO, GRAZIE. BASTA COSÌ. QUANTO PAGO?<br>MACELLAIO: 11 EURO E 80."),
  completa("MACELLAIO: BUONGIORNO! CHE COSA LE ___?<br>KOFI: VORREI ___ SALSICCE DI POLLO.<br>MACELLAIO: QUANTE NE VUOLE?<br>"
           "KOFI: SEI. E POI MEZZO ___ DI MACINATO DI MANZO.<br>MACELLAIO: ECCO. ___ ALTRO?<br>KOFI: NO, BASTA ___. QUANTO PAGO?",
           ["do", "delle", "chilo", "desidera", "così"], "11 · Completa il dialogo", "11 · Completa", "e11",
           "CHILO · COSÌ · DELLE · DESIDERA · DO"),
  parla("e12", 12, "DOMENICA FAI IL RAGÙ E LE COTOLETTE. VAI DAL MACELLAIO: SALUTA, CHIEDI LA CARNE CON «VORREI DEL… / DELLA…», "
                   "DI' QUANTO (UN ETTO, MEZZO CHILO…) E COME LA VUOI (A FETTINE, A PEZZI…), CHIEDI IL PREZZO E SALUTA."),
 ]
}

SLIDE_CARNE = [("tipi-di-carne/index.html", "I TIPI DI CARNE", "CUCINA", TIPI_SLIDE, CSS)]
ESERCIZI_CARNE = [("tipi-di-carne", TIPI)]
