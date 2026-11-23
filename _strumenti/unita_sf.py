"""Percorsi «Alfabetizzazione», «A2» e «B1» sulla traccia degli argomenti di tre volumi Edilingua mandati da Erila il 2026-11-23
(Senza frontiere Alfabetizzazione + Avvio, Nuovo Senza frontiere 2 e 3). I libri sono protetti: Erila ha scelto di rifare tutto
con testi nuovi. Si tengono argomenti, sequenza e TIPI di esercizio dell'unità; dialoghi, frasi, nomi, ascolti (voce del computer)
e immagini (Canva) sono nuovi. Ambientazione: Bari, operatori del SAI (Giovanni, Cristian, Michele, Silvia, Saleah, Eneida…).

Ogni livello ha il suo stile (caratteri, colori, impaginazione):
  alfa = Atkinson Hyperlegible, grande, MAIUSCOLO, una cosa per riga, 🔊 su ogni parola
  a2   = Nunito, minuscolo, tabelle e dialoghi
  b1   = Source Sans 3 + Merriweather per i testi da leggere, pagina più larga
Uso: python3 _strumenti/unita_sf.py   (dalla cartella principale del sito) → slide (index.html) ed esercizi (esercizi.html)"""
import os, sys
sys.path.insert(0, os.path.dirname(__file__))
from genera import eq, has, all_, build as build_es
import slide as SL
from unita_primi import cover, slide, cards, table, nota, dialogo, end
from unita_drive import ILL_CSS, ill, ill2, vf, scegli, menu, scrivi as _scrivi, ordina, completa, parla, libero

def scrivi(items, *a, **kw):
    return _scrivi([(q, (k,) if isinstance(k, str) else k) for q, k in items], *a, **kw)
from teoria import tab, es

# ---------------------------------------------------------------- stile per livello (slide)
FONT = {
    "alfa": "Atkinson+Hyperlegible:wght@400;700",
    "a2": "Nunito:wght@400;700;800",
    "b1": "Source+Sans+3:wght@400;600;700&family=Merriweather:wght@400;700",
}
CSS = {
 "alfa": ILL_CSS + """
  :root{ --blu:#0b7a75; --blu-scuro:#06403d; --teal:#14a39a; --arancio:#f4b400; }
  body{ font-family:"Atkinson Hyperlegible", Verdana, sans-serif !important; letter-spacing:.03em; }
  h2{ font-size:2.6rem; }
  .card b{ font-size:1.7rem; } .card .emoji{ font-size:3.6rem; } .card span{ font-size:1.2rem; }
  .parola{ display:flex; flex-wrap:wrap; gap:18px; justify-content:center; margin:10px 0; }
  .parola div{ background:#fff; border:4px solid var(--teal); border-radius:22px; padding:18px 26px; text-align:center; min-width:180px; }
  .parola b{ display:block; font-size:3rem; color:var(--blu-scuro); letter-spacing:.08em; }
  .parola small{ display:block; font-size:1.6rem; color:#555; text-transform:lowercase; margin-top:4px; }
  .sill{ background:#ffe9a8; border-radius:10px; padding:0 2px; }
  .parola .sill{ letter-spacing:.08em; }
  .lettera{ font-size:9rem; font-weight:bold; color:var(--blu); line-height:1; }
  .lettera small{ font-size:4rem; text-transform:lowercase; margin-left:20px; color:var(--teal); }
  .numeri{ display:grid; grid-template-columns:repeat(6,1fr); gap:12px; }
  .numeri div{ background:#fff; border-radius:16px; border:3px solid #cfe9e6; text-align:center; padding:10px; }
  .numeri b{ display:block; font-size:2.8rem; color:var(--blu); } .numeri span{ font-size:1.1rem; }
  @media (max-width:700px){ .numeri{ grid-template-columns:repeat(3,1fr); } .parola b{ font-size:2.2rem; } .lettera{ font-size:6rem; } }""",
 "a2": ILL_CSS + """
  :root{ --blu:#c2410c; --blu-scuro:#5a1d06; --teal:#0e7490; --arancio:#fbbf24; }
  body, .btn, button{ text-transform:none !important; font-family:Nunito, "Segoe UI", sans-serif !important; }
  h2{ font-size:2rem; } .lead{ font-size:1.4rem; }
  .bubble{ font-size:1.15rem; } table.plur td, table.plur th{ font-size:1.1rem; }""",
 "b1": ILL_CSS + """
  :root{ --blu:#5b3fa3; --blu-scuro:#2b1d55; --teal:#0f766e; --arancio:#f59e0b; }
  body, .btn, button{ text-transform:none !important; font-family:"Source Sans 3", "Segoe UI", sans-serif !important; }
  h1, h2{ font-family:Merriweather, Georgia, serif; } h2{ font-size:1.8rem; }
  .testo{ font-family:Merriweather, Georgia, serif; font-size:1.08rem; line-height:1.8; background:#fff; border-radius:14px;
          border-left:6px solid var(--blu); padding:16px 20px; text-align:left; max-width:900px; margin:0 auto; }
  .testo p{ margin:0 0 10px; }
  .bubble{ font-size:1.05rem; } table.plur td, table.plur th{ font-size:1rem; } .card span{ font-size:1rem; }""",
}

def font_link(liv):
    return '<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=%s&display=swap">' % FONT[liv]

def build_slide(path, unit, topbar, slides, liv):
    SL.build(path, unit, topbar, slides, CSS[liv])
    s = open(path, encoding="utf-8").read().replace("</head>", font_link(liv) + "\n</head>", 1)
    open(path, "w", encoding="utf-8").write(s)

def say(t, label="🔊"):
    return '<button type="button" class="say" data-say="%s" aria-label="ascolta">%s</button>' % (t, label)

def parole(items):
    """riquadri grandi per l'alfabetizzazione: (MAIUSCOLO, minuscolo)"""
    return '    <div class="parola">' + "".join('<div data-say="%s"><b>%s</b><small>%s</small></div>' % (a, a, b) for a, b in items) + "</div>"

def testo(*par):
    return '    <div class="testo">' + "".join("<p>%s</p>" % p for p in par) + "</div>"

def ascolto(d, righe):
    d["audio"] = righe
    return d

# =====================================================================
# ALFABETIZZAZIONE · UNITÀ 1 · CIAO, IO SONO
# =====================================================================
ALFA1_SLIDE = [
    cover("👋", "CIAO, IO SONO…", "MI PRESENTO · LE VOCALI O ED E · I NUMERI DA 0 A 10", "ALFABETIZZAZIONE &bull; UNITÀ 1"),
    slide("CHE COSA IMPARIAMO?", cards([
        ("🙋", "MI PRESENTO", "CIAO, SONO SILVIA"), ("🌍", "DA DOVE VENGO", "VENGO DAL MALI"),
        ("🔤", "O · E", "LE VOCALI O ED E"), ("🔢", "0 → 10", "I NUMERI")])),
    slide("🗣️ LE PAROLE", parole([("CIAO", "ciao"), ("IO", "io"), ("SONO", "sono"), ("PIACERE", "piacere"), ("VENGO", "vengo")]) + "\n" +
          nota("👆 TOCCA LA PAROLA E ASCOLTA.")),
    slide("🏫 IL PRIMO GIORNO DI SCUOLA", ill("alfa1-classe.jpg", "UNA CLASSE DI ADULTI: UNA INSEGNANTE E TRE STUDENTI SI SALUTANO") + "\n" + dialogo([
        ("*SILVIA", "CIAO! IO SONO SILVIA, L'INSEGNANTE."),
        ("BAKARY", "CIAO SILVIA. IO SONO BAKARY."),
        ("*SILVIA", "PIACERE, BAKARY! DA DOVE VIENI?"),
        ("BAKARY", "VENGO DAL MALI.")])),
    slide("🤝 TI PRESENTO…", dialogo([
        ("BAKARY", "CIAO SILVIA, TI PRESENTO NOOR. VIENE DALL'AFGHANISTAN."),
        ("*SILVIA", "PIACERE, NOOR!"),
        ("NOOR", "PIACERE. IO SONO NOOR."),
        ("*SILVIA", "COME STAI?"),
        ("NOOR", "BENE, GRAZIE.")]) + "\n" +
        nota("LUI È BAKARY. 👨 &nbsp;&nbsp; LEI È NOOR. 👩")),
    slide("🔤 LA VOCALE O", '    <div class="lettera" data-say="O">O<small>o</small></div>\n' +
          parole([("<span class='sill'>O</span>TTO", "otto"), ("<span class='sill'>O</span>LIO", "olio"), ("S<span class='sill'>O</span>N<span class='sill'>O</span>", "sono"), ("CIA<span class='sill'>O</span>", "ciao")])),
    slide("🔤 LA VOCALE E", '    <div class="lettera" data-say="E">E<small>e</small></div>\n' +
          parole([("<span class='sill'>E</span>URO", "euro"), ("<span class='sill'>E</span>STAT<span class='sill'>E</span>", "estate"), ("V<span class='sill'>E</span>NGO", "vengo"), ("PIAC<span class='sill'>E</span>R<span class='sill'>E</span>", "piacere")])),
    slide("🧩 LE SILLABE", parole([("CIA + O", "ciao"), ("SO + NO", "sono"), ("VEN + GO", "vengo"), ("PIA + CE + RE", "piacere")]) + "\n" +
          nota("🧩 UNISCO I PEZZI E LEGGO LA PAROLA.")),
    slide("🔢 I NUMERI DA 0 A 10", '    <div class="numeri">' + "".join(
        '<div data-say="%s"><b>%d</b><span>%s</span></div>' % (w, n, w) for n, w in enumerate(
            ["ZERO", "UNO", "DUE", "TRE", "QUATTRO", "CINQUE", "SEI", "SETTE", "OTTO", "NOVE", "DIECI"])) + "</div>"),
    slide("📞 IL MIO NUMERO DI TELEFONO", dialogo([
        ("*SILVIA", "BAKARY, QUAL È IL TUO NUMERO DI TELEFONO?"),
        ("BAKARY", "3 - 2 - 0 - 4 - 5 - 6 - 7 - 1 - 8 - 9.")]) + "\n" +
        nota("📞 320 456 71 89")),
    slide("🎂 LA DATA DI NASCITA", table([["GIORNO", "MESE", "ANNO"], ["<b>7</b>", "<b>3</b>", "<b>1990</b>"]]) + "\n" +
          nota("BAKARY È NATO IL 7 / 3 / 1990.<br>PRIMA IL GIORNO, POI IL MESE, POI L'ANNO.")),
    slide("🪪 IL MIO CARTELLINO", ill("alfa1-cartellino.jpg", "UN CARTELLINO CON NOME E COGNOME SUL BANCO") + "\n" +
          parole([("NOME", "bakary"), ("COGNOME", "keita")]) + "\n" + nota("✍️ SCRIVO IL MIO NOME E COGNOME.")),
    end("ORA SAI DIRE CHI SEI E DA DOVE VIENI!"),
]

def x_parola(n, senti, opzioni):
    return {"q": say(senti) + " %d." % n, "opts": opzioni}

ALFA1 = {
 "title": "👋 Ciao, io sono · Esercizi", "store": "alfa-ciao-io-sono", "upper": True, "livello": "alfa",
 "sub": "🔊 TOCCA E ASCOLTA. ✍️ SCRIVI O 👆 SCEGLI. POI PREMI «CONTROLLA».",
 "sections": [
  {"part": "Ascolto e leggo"},
  {"id": "e1", "title": "1 · 🔊 Ascolta e scegli la parola", "short": "1 · Ascolta e scegli", "type": "choice",
   "cons": "TOCCA 🔊. SCEGLI LA PAROLA CHE SENTI.",
   "items": [x_parola(1, "SONO", ["CIAO", "SONO", "IO"]), x_parola(2, "IO", ["IO", "VENGO", "SONO"]),
             x_parola(3, "PIACERE", ["VENGO", "CIAO", "PIACERE"]), x_parola(4, "CIAO", ["PIACERE", "CIAO", "IO"]),
             x_parola(5, "VENGO", ["SONO", "IO", "VENGO"])],
   "k": [eq(a) for a in ["SONO", "IO", "PIACERE", "CIAO", "VENGO"]]},
  {"id": "e2", "title": "2 · 👀 Cerca la parola uguale", "short": "2 · Uguale", "type": "choice",
   "cons": "GUARDA LA PAROLA. TROVA LA PAROLA UGUALE.",
   "items": [{"q": "<b>CIAO</b>", "opts": ["CIAO", "CASA", "COSA"]}, {"q": "<b>SONO</b>", "opts": ["SOLE", "SONO", "SETE"]},
             {"q": "<b>VENGO</b>", "opts": ["VENGO", "VENDO", "VEDO"]}, {"q": "<b>PIACERE</b>", "opts": ["PIACERE", "PIANO", "PIZZA"]},
             {"q": "<b>IO</b>", "opts": ["IL", "IO", "OI"]}],
   "k": [eq(a) for a in ["CIAO", "SONO", "VENGO", "PIACERE", "IO"]]},
  {"part": "Scrivo"},
  {"id": "e3", "title": "3 · ✍️ Copia la parola", "short": "3 · Copia", "type": "text", "w": "m",
   "cons": "GUARDA E SCRIVI LA STESSA PAROLA.",
   "items": [{"q": "CIAO"}, {"q": "SONO"}, {"q": "IO"}, {"q": "PIACERE"}, {"q": "VENGO"}],
   "k": [eq(a) for a in ["CIAO", "SONO", "IO", "PIACERE", "VENGO"]]},
  {"id": "e4", "title": "4 · 🔊 Ascolta e scrivi la lettera", "short": "4 · La lettera", "type": "text", "w": "s",
   "cons": "TOCCA 🔊. SCRIVI LA LETTERA CHE MANCA.",
   "items": [{"q": say("CIAO") + " CIA _", "w": "s"}, {"q": say("SONO") + " S _ N _"}, {"q": say("IO") + " I _"},
             {"q": say("VENGO") + " V _ NG _"}, {"q": say("PIACERE") + " PIAC _ R _"}],
   "k": [eq("O"), eq("OO", "O O"), eq("O"), eq("EO", "E O"), eq("EE", "E E")]},
  {"id": "e5", "title": "5 · 🧩 Componi la parola", "short": "5 · Le sillabe", "type": "text", "w": "m",
   "cons": "UNISCI I PEZZI. SCRIVI LA PAROLA.",
   "items": [{"q": "<span class='sill'>CIA</span> + <span class='sill'>O</span> ="}, {"q": "<span class='sill'>SO</span> + <span class='sill'>NO</span> ="},
             {"q": "<span class='sill'>VEN</span> + <span class='sill'>GO</span> ="}, {"q": "<span class='sill'>PIA</span> + <span class='sill'>CE</span> + <span class='sill'>RE</span> ="},
             {"q": "<span class='sill'>O</span> + <span class='sill'>LIO</span> ="}],
   "k": [eq(a) for a in ["CIAO", "SONO", "VENGO", "PIACERE", "OLIO"]]},
  {"part": "Le vocali O ed E"},
  {"id": "e6", "title": "6 · 🔊 Comincia con E o con O?", "short": "6 · E o O", "type": "choice",
   "cons": "TOCCA 🔊. LA PAROLA COMINCIA CON <b>E</b> O CON <b>O</b>?", "opts": ["E", "O"],
   "items": [{"q": "<span class='emo'>8️⃣</span> " + say("OTTO")}, {"q": "<span class='emo'>💶</span> " + say("EURO")},
             {"q": "<span class='emo'>☂️</span> " + say("OMBRELLO")}, {"q": "<span class='emo'>🐘</span> " + say("ELEFANTE")},
             {"q": "<span class='emo'>🕐</span> " + say("OROLOGIO")}, {"q": "<span class='emo'>☀️</span> " + say("ESTATE")}],
   "k": [eq(a) for a in ["O", "E", "O", "E", "O", "E"]]},
  {"id": "e7", "title": "7 · ✍️ Completa con E o con O", "short": "7 · Completa", "type": "text", "w": "s",
   "cons": "TOCCA 🔊. SCRIVI <b>E</b> OPPURE <b>O</b>.",
   "items": [{"q": say("OLIO") + " OLI _"}, {"q": say("PANE") + " PAN _"}, {"q": say("AMICO") + " AMIC _"},
             {"q": say("STRADE") + " STRAD _"}, {"q": say("MARE") + " MAR _"}, {"q": say("GATTO") + " GATT _"}],
   "k": [eq(a) for a in ["O", "E", "O", "E", "E", "O"]]},
  {"part": "Mi presento"},
  {"id": "e8", "title": "8 · 🗣️ Completa il dialogo", "short": "8 · Il dialogo", "type": "cloze",
   "cons": "SCRIVI LA PAROLA GIUSTA.", "bank": "SONO · VENGO · PIACERE · CIAO",
   "parts": ["GIOVANNI: ", {}, "! IO SONO GIOVANNI.<br>AWA: CIAO GIOVANNI. IO ", {}, " AWA.<br>GIOVANNI: ", {},
             "! DA DOVE VIENI?<br>AWA: ", {}, " DALLA COSTA D'AVORIO."],
   "k": [eq("ciao"), eq("sono"), eq("piacere"), eq("vengo")]},
  {"id": "e9", "title": "9 · 👀 Lui o lei?", "short": "9 · Lui o lei", "type": "choice", "opts": ["LUI È", "LEI È"],
   "cons": "GUARDA. SCEGLI <b>LUI È</b> 👨 OPPURE <b>LEI È</b> 👩.",
   "items": [{"q": "<span class='emo'>👨🏿</span> … BAKARY."}, {"q": "<span class='emo'>🧕</span> … NOOR."},
             {"q": "<span class='emo'>👩🏾</span> … AWA."}, {"q": "<span class='emo'>👨🏽</span> … GIOVANNI."}],
   "k": [eq(a) for a in ["LUI È", "LEI È", "LEI È", "LUI È"]]},
  {"part": "I numeri"},
  {"id": "e10", "title": "10 · 🔢 Conta e scrivi il numero", "short": "10 · Conta", "type": "text", "w": "s",
   "cons": "CONTA. SCRIVI IL NUMERO: 1, 2, 3…",
   "items": [{"q": "<span class='emo'>✏️✏️✏️</span>"}, {"q": "<span class='emo'>📕📕📕📕📕</span>"}, {"q": "<span class='emo'>🪑🪑</span>"},
             {"q": "<span class='emo'>🎒🎒🎒🎒🎒🎒🎒</span>"}, {"q": "<span class='emo'>📱</span>"}, {"q": "<span class='emo'>🖍️🖍️🖍️🖍️🖍️🖍️🖍️🖍️🖍️</span>"}],
   "k": [eq("3", "TRE"), eq("5", "CINQUE"), eq("2", "DUE"), eq("7", "SETTE"), eq("1", "UNO"), eq("9", "NOVE")]},
  {"id": "e11", "title": "11 · 🔊 Ascolta e scrivi il numero", "short": "11 · Ascolta il numero", "type": "text", "w": "s",
   "cons": "TOCCA 🔊. SCRIVI IL NUMERO CON LE CIFRE: 0, 1, 2…",
   "items": [{"q": say("SEI") + " 1."}, {"q": say("DIECI") + " 2."}, {"q": say("QUATTRO") + " 3."}, {"q": say("OTTO") + " 4."}, {"q": say("ZERO") + " 5."}],
   "k": [eq("6"), eq("10"), eq("4"), eq("8"), eq("0")]},
  {"id": "e12", "title": "12 · 🔊 Il numero di telefono di Silvia", "short": "12 · Il telefono", "type": "text", "w": "m",
   "cons": "TOCCA 🔊 E SCRIVI IL NUMERO.",
   "items": [{"q": say("3 4 7, 2 0 5, 1 6, 9 8")}],
   "k": [eq("3472051698", "347 205 16 98", "347 2051698", "347 205 1698")]},
  {"part": "Il mio modulo"},
  libero("e13", 13, "I miei dati", "SCRIVI IL TUO NOME, IL TUO COGNOME E LA TUA DATA DI NASCITA (GIORNO / MESE / ANNO).",
         ["NOME", "COGNOME", "DATA DI NASCITA", "NUMERO DI TELEFONO"], rows=1),
  parla("e14", 14, "PRESENTATI: «CIAO, IO SONO… VENGO DA…»"),
 ]
}

# =====================================================================
# A2 · UNITÀ 1 · LA SALUTE
# =====================================================================
A2SAL_SLIDE = [
    cover("🩺", "La salute", "Dal medico · In farmacia · I servizi sanitari", "A2 &bull; Modulo 1 &bull; Unità 1"),
    slide("In questa unità impari a…", cards([
        ("🤒", "Dire come stai", "Ho mal di testa, mi fa male la schiena"), ("👨‍⚕️", "Parlare con il medico", "Che sintomi ha? Da quanto tempo?"),
        ("💊", "Chiedere in farmacia", "Le compresse? Le prendo dopo i pasti"), ("🏥", "Scegliere il servizio giusto", "Medico di base, guardia medica, 118, CUP")])),
    slide("🧍 Le parti del corpo", ill("a2-salute-corpo.jpg", "Illustrazione del corpo umano con le parti principali") + "\n" + cards([
        ("🗣️", "la testa, la gola, il collo", ""), ("💪", "il braccio → le braccia", "plurale irregolare"),
        ("🖐️", "la mano → le mani", ""), ("🦵", "il ginocchio → le ginocchia", "plurale irregolare"),
        ("👂", "l'orecchio → le orecchie", ""), ("🦴", "la schiena, la pancia, lo stomaco", "")], "g3")),
    slide("🤒 I sintomi", table([
        ["ho mal di…", "testa, gola, denti, pancia, stomaco, schiena"], ["mi fa male…", "il collo, la gamba, il braccio (una cosa)"],
        ["mi fanno male…", "le gambe, le orecchie, gli occhi (più cose)"], ["ho…", "la febbre, la tosse, il raffreddore, la nausea"],
        ["mi sento…", "stanco/a, debole, indolenzito/a"]], head=["dico", "esempi"])),
    slide("💬 Chiedere e dire come stai", table([
        ["Come stai? Come va?", "Come sta? Come si sente?"], ["Dove ti fa male?", "Dove le fa male?"], ["Che sintomi hai?", "Che sintomi ha?"]],
        head=["informale (tu) 🧑‍🤝‍🧑", "formale (Lei) 🩺"]) + "\n" +
        nota("Non sto tanto bene: ho mal di schiena. · Sto malissimo: mi fanno male le orecchie. · Sto meglio, grazie!")),
    slide("🩺 Lezione A · Dal medico", ill("a2-salute-medico.jpg", "Un medico visita un uomo nell'ambulatorio") + "\n" + dialogo([
        ("*Dottoressa Lorusso", "Buongiorno, signor Haidari. Come si sente oggi?"),
        ("Jawad", "Non molto bene, dottoressa. Ho mal di gola e la febbre a 38."),
        ("*Dottoressa Lorusso", "Da quanto tempo?"),
        ("Jawad", "Da due giorni. E mi fanno male anche le orecchie."),
        ("*Dottoressa Lorusso", "Vediamo… La gola è rossa. Le scrivo uno sciroppo e delle compresse per la febbre."),
        ("Jawad", "Le compresse quando le prendo?"),
        ("*Dottoressa Lorusso", "Le prende dopo i pasti, due volte al giorno. Se tra tre giorni la febbre non passa, torni da me.")])),
    slide("📘 I pronomi diretti: lo, la, li, le", table([
        ["il medico, lo sciroppo", "lo", "Lo sciroppo? <b>Lo</b> prendo la sera."], ["la ricetta, la pomata", "la", "La ricetta? <b>La</b> porto in farmacia."],
        ["i farmaci, gli esami", "li", "Gli esami? <b>Li</b> faccio domani."], ["le compresse, le medicine", "le", "Le compresse? <b>Le</b> prendo dopo pranzo."],
        ["Lei (formale)", "La", "Dottoressa, <b>La</b> chiamo domani."]], head=["chi? che cosa?", "pronome", "esempio"]) + "\n" +
        nota("Il pronome va <b>prima del verbo</b>. Con la negazione: non <b>lo</b> prendo.")),
    slide("💊 Lezione B · In farmacia", dialogo([
        ("Mariam", "Buonasera. Vorrei qualcosa per la tosse, per favore."),
        ("*Farmacista", "Tosse secca o grassa? Ha anche la febbre?"),
        ("Mariam", "Secca, senza febbre. Non dormo la notte."),
        ("*Farmacista", "Allora Le do questo sciroppo. Lo prende tre volte al giorno, lontano dai pasti."),
        ("Mariam", "Serve la ricetta?"),
        ("*Farmacista", "No, è un farmaco da banco. Legga il foglietto illustrativo prima di prenderlo.")])),
    slide("📘 I pronomi diretti: mi, ti, ci, vi", table([
        ["io", "mi", "Il medico <b>mi</b> visita alle 10."], ["tu", "ti", "<b>Ti</b> accompagno io in ospedale."],
        ["noi", "ci", "La guardia medica <b>ci</b> richiama."], ["voi", "vi", "<b>Vi</b> aspetto in farmacia."]],
        head=["soggetto", "pronome diretto", "esempio"])),
    slide("👩‍⚕️ I medici specialisti", cards([
        ("🦷", "il dentista", "i denti"), ("🦴", "l'ortopedico", "le ossa, i muscoli"), ("👂", "l'otorino", "naso, gola, orecchie"),
        ("👁️", "l'oculista", "gli occhi"), ("🧴", "il dermatologo", "la pelle"), ("🧒", "il pediatra", "i bambini"),
        ("🫄", "il ginecologo", "la salute della donna"), ("❤️", "il cardiologo", "il cuore"), ("🍽️", "il gastroenterologo", "lo stomaco, la pancia")], "g3")),
    slide("🏥 Educazione civica · Dove vado?", cards([
        ("👨‍⚕️", "il medico di base", "visite, ricette, impegnative. Lo scegli all'ASL"),
        ("📅", "il CUP", "Centro Unico di Prenotazione: prenoti visite ed esami con l'impegnativa"),
        ("🌙", "la guardia medica", "di notte, nel fine settimana e nei giorni festivi"),
        ("🚑", "il 118 / il 112", "emergenze: un incidente, un dolore fortissimo"),
        ("🏥", "il Pronto Soccorso", "in ospedale, per le cose urgenti"),
        ("👩‍👧", "il consultorio familiare", "donne in gravidanza, mamme e bambini, giovani")], "g2")),
    end("Ora sai parlare della tua salute!"),
]

A2SAL = {
 "title": "🩺 La salute · Esercizi", "store": "a2-la-salute", "livello": "a2",
 "sections": [
  {"part": "Il corpo e i sintomi"},
  menu(["testa", "gola", "denti", "schiena", "pancia", "orecchie"],
       [("1. Ho mangiato troppo: ho mal di …", "pancia"), ("2. Non posso parlare: ho mal di …", "gola"),
        ("3. Devo andare dal dentista: ho mal di …", "denti"), ("4. Ho portato una scatola pesante: ho mal di …", "schiena"),
        ("5. La musica era troppo forte: mi fanno male le …", "orecchie"), ("6. Ho studiato tutta la notte: ho mal di …", "testa")],
       "1 · Dove fa male?", "1 · I sintomi", "e1"),
  menu(["a", "b", "c", "d", "e"],
       [("1. Come stai?", "c"), ("2. Dove ti fa male?", "e"), ("3. Signora Bianchi, come si sente?", "a"),
        ("4. Che sintomi ha?", "b"), ("5. Come va oggi?", "d")],
       "2 · Collega domande e risposte", "2 · Domande e risposte", "e2",
       cons="a. Non molto bene, dottore: mi sento debole.<br>b. Ho la febbre e la tosse.<br>c. Benissimo, grazie! E tu?<br>d. Insomma… ho ancora un po' di mal di testa.<br>e. Mi fa male il ginocchio destro."),
  scegli([("1. Mi … male le gambe.", ["fa", "fanno", "ha"], "fanno"), ("2. Mi … male il collo.", ["fa", "fanno", "sono"], "fa"),
          ("3. Ho mal … denti.", ["di", "ai", "la"], "di"), ("4. Dottore, mi fanno male le …", ["ginocchio", "ginocchia", "ginocchie"], "ginocchia"),
          ("5. Mi fa male il braccio; anzi, mi fanno male tutte e due le …", ["bracci", "braccia", "braccie"], "braccia")],
         "3 · Fa o fanno?", "3 · Fa / fanno", "e3"),
  {"part": "Dal medico"},
  ascolto(vf(["1. Jawad sta bene.", "2. Jawad ha la febbre.", "3. Ha mal di gola da una settimana.",
              "4. Gli fanno male anche le orecchie.", "5. Deve prendere le compresse prima di mangiare.", "6. Se la febbre non passa, torna dalla dottoressa."],
             ["FALSO", "VERO", "FALSO", "VERO", "FALSO", "VERO"], "4 · 🎧 Ascolta il dialogo: vero o falso?", "4 · Dal medico", "e4"),
          [["F", "Buongiorno, signor Haidari. Come si sente oggi?"], ["M", "Non molto bene, dottoressa. Ho mal di gola e la febbre a trentotto."],
           ["F", "Da quanto tempo?"], ["M", "Da due giorni. E mi fanno male anche le orecchie."],
           ["F", "Vediamo. La gola è rossa. Le scrivo uno sciroppo e delle compresse per la febbre."], ["M", "Le compresse quando le prendo?"],
           ["F", "Le prende dopo i pasti, due volte al giorno. Se tra tre giorni la febbre non passa, torni da me."]]),
  {"part": "I pronomi diretti lo, la, li, le", "teoria":
     tab(("il / lo …", "lo"), ("la …", "la"), ("i / gli …", "li"), ("le …", "le"), ("Lei (formale)", "La"), head=("parola", "pronome")) +
     "Il pronome sostituisce una cosa o una persona e va <b>prima del verbo</b>." + es("Lo sciroppo? <b>Lo</b> prendo la sera.", "Le compresse? Non <b>le</b> prendo.")},
  scrivi([("1. Il foglietto illustrativo? Sì, … leggo sempre.", "lo"), ("2. La ricetta? Il medico … scrive adesso.", "la"),
          ("3. I farmaci? … compro in farmacia.", "li"), ("4. Le iniezioni? No, non … faccio.", "le"),
          ("5. Lo sciroppo? … bevo dopo cena.", "lo"), ("6. Signora Rossi, … chiamo domani per i risultati.", "la")],
         "5 · Completa con lo, la, li, le", "5 · lo, la, li, le", "e5", bank="lo · la · li · le", w="s"),
  {"part": "In farmacia"},
  ascolto(scegli([("1. Mariam ha…", ["la tosse e la febbre", "la tosse senza febbre", "mal di stomaco"], "la tosse senza febbre"),
                  ("2. La farmacista le dà…", ["delle compresse", "una pomata", "uno sciroppo"], "uno sciroppo"),
                  ("3. Deve prenderlo…", ["tre volte al giorno", "una volta al giorno", "solo la sera"], "tre volte al giorno"),
                  ("4. Per comprarlo…", ["serve la ricetta", "non serve la ricetta", "serve l'impegnativa"], "non serve la ricetta")],
                 "6 · 🎧 In farmacia: scegli la risposta giusta", "6 · In farmacia", "e6"),
          [["F", "Buonasera. Vorrei qualcosa per la tosse, per favore."], ["F", "Tosse secca o grassa? Ha anche la febbre?"],
           ["F", "Secca, senza febbre. Non dormo la notte."], ["F", "Allora le do questo sciroppo. Lo prende tre volte al giorno, lontano dai pasti."],
           ["F", "Serve la ricetta?"], ["F", "No, è un farmaco da banco. Legga il foglietto illustrativo prima di prenderlo."]]),
  {"id": "e7", "title": "7 · Leggi le scatole: giusto o sbagliato?", "short": "7 · Le scatole", "type": "choice", "opts": ["GIUSTO", "SBAGLIATO"], "full": True,
   "info": "<b>DOLORSTOP</b> · Perché si usa: mal di testa, mal di denti · Come si prende: 1 compressa dopo i pasti, massimo 3 al giorno<br>"
           "<b>TOSSIFEN</b> · sciroppo per la tosse secca · 10 ml 2 volte al giorno, lontano dai pasti<br>"
           "<b>GASTROL</b> · per il mal di stomaco · 2 compresse prima dei pasti",
   "items": [{"q": "1. Per il mal di denti Sami prende Dolorstop dopo pranzo."}, {"q": "2. Lucia prende 5 compresse di Dolorstop al giorno."},
             {"q": "3. Per il mal di stomaco Omar prende Gastrol dopo cena."}, {"q": "4. Per la tosse secca Amina prende Tossifen la mattina e la sera."}],
   "k": [eq(a) for a in ["GIUSTO", "SBAGLIATO", "SBAGLIATO", "GIUSTO"]]},
  {"part": "I pronomi diretti mi, ti, ci, vi", "teoria":
     tab(("io", "mi"), ("tu", "ti"), ("noi", "ci"), ("voi", "vi"), head=("soggetto", "pronome")) + es("Il medico <b>mi</b> visita. · <b>Ti</b> accompagno io.")},
  scrivi([("1. Mi aiuti? Sì, … aiuto.", "ti"), ("2. Ci aspettate? Sì, … aspettiamo.", "vi"), ("3. (io) Silvia … accompagna dal dentista.", "mi"),
          ("4. (noi) Il dottore … chiama quando è il nostro turno.", "ci"), ("5. (voi) … porto in ospedale con la macchina.", "vi")],
         "8 · Completa con mi, ti, ci, vi", "8 · mi, ti, ci, vi", "e8", bank="mi · ti · ci · vi", w="s"),
  menu(["il dentista", "l'oculista", "l'ortopedico", "il pediatra", "il dermatologo", "l'otorino"],
       [("1. Mio figlio ha la febbre: chiamo …", "il pediatra"), ("2. Non vedo bene da lontano: vado da …", "l'oculista"),
        ("3. Mi sono rotto la gamba: mi visita …", "l'ortopedico"), ("4. Ho una macchia rossa sulla pelle: prenoto …", "il dermatologo"),
        ("5. Ho sempre mal di orecchie: vado da …", "l'otorino"), ("6. Mi fa male un dente: telefono a …", "il dentista")],
       "9 · Quale specialista?", "9 · Gli specialisti", "e9"),
  {"part": "Educazione civica"},
  vf(["1. Per una ricetta normale vado al Pronto Soccorso.", "2. Il medico di base scrive l'impegnativa per una visita specialistica.",
      "3. Con il CUP prenoto visite ed esami.", "4. La guardia medica lavora di notte e nei giorni festivi.",
      "5. Il numero per un'emergenza è il 181.", "6. Al consultorio familiare vanno spesso le donne in gravidanza."],
     ["FALSO", "VERO", "VERO", "VERO", "FALSO", "VERO"], "10 · I servizi della salute: vero o falso?", "10 · I servizi", "e10"),
  scegli([("1. È domenica sera e Fatou ha la febbre alta. Chiama…", ["il medico di base", "la guardia medica"], "la guardia medica"),
          ("2. Ali ha avuto un incidente con la bici e perde sangue. Chiama…", ["il 112 / 118", "il CUP"], "il 112 / 118"),
          ("3. Rosa è incinta e vuole fare un controllo. Va…", ["al consultorio familiare", "al Pronto Soccorso"], "al consultorio familiare"),
          ("4. Igor ha l'impegnativa per l'oculista. Telefona…", ["al CUP", "in farmacia"], "al CUP")],
         "11 · Che cosa devono fare?", "11 · Che cosa fare", "e11"),
  libero("e12", 12, "Un dialogo", "Scrivi un piccolo dialogo dal medico o in farmacia (6 battute). Usa: mi fa male / ho mal di / lo, la, li, le.", ["Il mio dialogo"], rows=6),
  parla("e13", 13, "Racconta: quando stai male, che cosa fai? Dove vai? Com'è il servizio sanitario nel tuo Paese?"),
 ]
}

# =====================================================================
# B1 · UNITÀ 1 · LA CITTADINANZA ITALIANA
# =====================================================================
B1CIT_SLIDE = [
    cover("🇮🇹", "La cittadinanza italiana", "Al patronato · Documenti e ricordi · Cittadini italiani ed europei", "B1 &bull; Modulo 1 &bull; Unità 1"),
    slide("In questa unità impari a…", cards([
        ("🗂️", "Descrivere una procedura", "Prima… poi… alla fine"), ("🕰️", "Raccontare il passato", "Passato prossimo e imperfetto"),
        ("🏢", "Usare il registro formale", "Come si chiama? Dov'è nato?"), ("🇪🇺", "Diritti e doveri", "Cittadinanza italiana ed europea")])),
    slide("🗂️ Le parole della burocrazia digitale", cards([
        ("🔑", "lo SPID / la CIE", "le credenziali per entrare nei siti della Pubblica Amministrazione"),
        ("💻", "la procedura telematica", "la domanda si fa online, non allo sportello"),
        ("📄", "l'atto di nascita", "il documento che dice dove e quando sei nato; dall'estero va tradotto e legalizzato"),
        ("⚖️", "il certificato penale", "dice che non hai condanne; serve anche quello del Paese d'origine"),
        ("🎓", "la certificazione B1", "l'esame di italiano: CILS, CELI, PLIDA, Roma Tre"),
        ("🤝", "il patronato", "un ufficio gratuito che aiuta con pratiche e domande")], "g3")),
    slide("🏢 Lezione A · Al patronato", ill("b1-cittadinanza-patronato.jpg", "Un operatore del patronato aiuta un uomo davanti al computer") + "\n" + dialogo([
        ("*Michele (patronato)", "Buongiorno, si accomodi. Come si chiama?"),
        ("Youssef", "Youssef El Amrani. Vorrei informazioni sulla domanda di cittadinanza."),
        ("*Michele (patronato)", "Da quanti anni vive in Italia?"),
        ("Youssef", "Sono arrivato nel 2012, quindi da più di dieci anni. Ho sempre abitato a Bari."),
        ("*Michele (patronato)", "Bene. Ha già fatto l'esame di italiano?"),
        ("Youssef", "Sì, l'ho superato l'anno scorso: ho la certificazione B1."),
        ("*Michele (patronato)", "Perfetto. La domanda si presenta online, sul portale del Ministero dell'Interno, con lo SPID. Le servono l'atto di nascita e il certificato penale del Marocco, tradotti e legalizzati, la ricevuta del contributo e una marca da bollo."),
        ("Youssef", "E se ho problemi con il sito?"),
        ("*Michele (patronato)", "Prenda un appuntamento: la compiliamo insieme qui.")])),
    slide("📘 Il passato prossimo", table([
        ["avere + participio", "verbi con oggetto (che cosa?)", "Ho <b>compilato</b> la domanda. Ho <b>fatto</b> l'esame."],
        ["essere + participio", "movimento, stato, cambiamento, riflessivi", "Sono <b>arrivato</b> nel 2012. Mi sono <b>trasferita</b> a Bari."]],
        head=["ausiliare", "quando", "esempio"]) + "\n" + nota(
        "Con <b>essere</b> il participio si accorda: Youssef è arrivat<b>o</b> · Sara è arrivat<b>a</b> · loro sono arrivat<b>i</b>.<br>"
        "Participi irregolari: fare → <b>fatto</b>, dire → <b>detto</b>, chiedere → <b>chiesto</b>, leggere → <b>letto</b>, "
        "rispondere → <b>risposto</b>, nascere → <b>nato</b>, vivere → <b>vissuto</b>, prendere → <b>preso</b>.")),
    slide("🕰️ Lezione B · Documenti e nostalgia", testo(
        "Quando ero piccolo vivevo a Fès con i miei nonni. La nostra casa <b>aveva</b> un cortile con un albero di arance e ogni venerdì "
        "tutta la famiglia <b>mangiava</b> insieme. Mia nonna <b>raccontava</b> storie e io <b>ascoltavo</b> per ore.",
        "Per preparare i documenti della cittadinanza <b>sono tornato</b> in Marocco a ottobre. <b>Ho chiesto</b> l'atto di nascita in comune "
        "e <b>ho rivisto</b> la mia vecchia scuola. <b>Era</b> uguale, ma più piccola di come la ricordavo.") + "\n" +
        nota("<b>Imperfetto</b> = abitudini, descrizioni, situazioni (vivevo, aveva, mangiava).<br><b>Passato prossimo</b> = fatti finiti, una volta (sono tornato, ho chiesto).")),
    slide("📘 L'imperfetto", table([
        ["io", "abit<b>avo</b>", "viv<b>evo</b>", "dorm<b>ivo</b>", "ero"], ["tu", "abit<b>avi</b>", "viv<b>evi</b>", "dorm<b>ivi</b>", "eri"],
        ["lui / lei", "abit<b>ava</b>", "viv<b>eva</b>", "dorm<b>iva</b>", "era"], ["noi", "abit<b>avamo</b>", "viv<b>evamo</b>", "dorm<b>ivamo</b>", "eravamo"],
        ["voi", "abit<b>avate</b>", "viv<b>evate</b>", "dorm<b>ivate</b>", "eravate"], ["loro", "abit<b>avano</b>", "viv<b>evano</b>", "dorm<b>ivano</b>", "erano"]],
        head=["", "-are", "-ere", "-ire", "essere"]) + "\n" + nota("Irregolari: fare → face<b>vo</b>, dire → dice<b>vo</b>, bere → beve<b>vo</b>.")),
    slide("🎩 Registro formale: il Lei", table([
        ["Come ti chiami?", "Come si chiama?"], ["Dove sei nato?", "Dov'è nato/a?"], ["Quando sei arrivato in Italia?", "Quando è arrivato/a in Italia?"],
        ["Che lavoro fai?", "Che lavoro fa?"], ["Hai portato i documenti?", "Ha portato i documenti?"]], head=["informale (tu)", "formale (Lei)"])),
    slide("🇪🇺 Educazione civica · Cittadini italiani ed europei", cards([
        ("🗳️", "Votare", "alle elezioni comunali, regionali, politiche ed europee"), ("🛂", "Il passaporto italiano", "e la libertà di vivere e lavorare in tutta l'UE"),
        ("🏛️", "Il giuramento", "si giura fedeltà alla Repubblica e alla Costituzione davanti al sindaco"), ("⚖️", "I doveri", "rispettare le leggi, pagare le tasse, difendere la Patria"),
        ("👶", "I figli minorenni", "che vivono con il genitore diventano italiani con lui/lei"), ("🌍", "La doppia cittadinanza", "molti Paesi la permettono: informati per il tuo")], "g3")),
    end("Ora sai raccontare un percorso e parlare della cittadinanza!"),
]

PATRONATO = [["M", "Buongiorno, si accomodi. Come si chiama?"], ["M", "Youssef El Amrani. Vorrei informazioni sulla domanda di cittadinanza."],
             ["M", "Da quanti anni vive in Italia?"], ["M", "Sono arrivato nel duemiladodici, quindi da più di dieci anni. Ho sempre abitato a Bari."],
             ["M", "Bene. Ha già fatto l'esame di italiano?"], ["M", "Sì, l'ho superato l'anno scorso: ho la certificazione B1."],
             ["M", "Perfetto. La domanda si presenta online, sul portale del Ministero dell'Interno, con lo SPID. Le servono l'atto di nascita e il certificato penale del Marocco, tradotti e legalizzati, la ricevuta del contributo e una marca da bollo."],
             ["M", "E se ho problemi con il sito?"], ["M", "Prenda un appuntamento: la compiliamo insieme qui."]]

B1CIT = {
 "title": "🇮🇹 La cittadinanza italiana · Esercizi", "store": "b1-cittadinanza", "livello": "b1",
 "sections": [
  {"part": "Le parole"},
  menu(["lo SPID", "il patronato", "l'atto di nascita", "la procedura telematica", "il certificato penale", "la marca da bollo"],
       [("1. Un ufficio gratuito che aiuta i lavoratori con pratiche e domande.", "il patronato"),
        ("2. Le credenziali per entrare nei siti della Pubblica Amministrazione.", "lo SPID"),
        ("3. Una procedura che si fa su internet.", "la procedura telematica"),
        ("4. Il documento che dice dove e quando sei nato.", "l'atto di nascita"),
        ("5. Il documento che dice se una persona ha avuto condanne.", "il certificato penale"),
        ("6. Un bollo che si compra dal tabaccaio e serve per alcune domande.", "la marca da bollo")],
       "1 · Che cos'è?", "1 · Il lessico", "e1"),
  {"part": "Lezione A · Al patronato"},
  ascolto(vf(["1. Youssef chiede informazioni sul permesso di soggiorno.", "2. Youssef vive in Italia da più di dieci anni.",
              "3. Ha abitato in tre città diverse.", "4. Ha già la certificazione di italiano B1.",
              "5. La domanda si presenta allo sportello della prefettura, su carta.", "6. I documenti del Marocco devono essere tradotti e legalizzati.",
              "7. Il patronato può aiutarlo a compilare la domanda."],
             ["FALSO", "VERO", "FALSO", "VERO", "FALSO", "VERO", "VERO"], "2 · 🎧 Ascolta il dialogo: vero o falso?", "2 · Al patronato", "e2"),
          PATRONATO),
  menu(["a", "b", "c", "d", "e"],
       [("1. Scusi, è qui che posso chiedere informazioni sulla cittadinanza?", "c"), ("2. Quando è arrivato in Italia?", "e"),
        ("3. La domanda si può fare in posta?", "a"), ("4. Quali documenti devo presentare?", "d"), ("5. Ha fatto l'esame di lingua?", "b")],
       "3 · Collega domande e risposte", "3 · Domande e risposte", "e3",
       cons="a. No, si fa solo online, sul portale del Ministero dell'Interno.<br>b. Sì, ho la certificazione B1 da marzo.<br>"
            "c. Sì, certo. Prendiamo un appuntamento?<br>d. L'atto di nascita, il certificato penale, la ricevuta del pagamento…<br>e. Sono arrivato undici anni fa."),
  {"part": "Il passato prossimo", "teoria":
     tab(("avere", "ho compilato, ho fatto, ho letto"), ("essere", "sono arrivato/a, sono nato/a, mi sono trasferito/a"), head=("ausiliare", "esempi")) +
     "Con <b>essere</b> il participio cambia (-o, -a, -i, -e). Attenzione ai participi irregolari: fatto, detto, chiesto, letto, nato, vissuto, preso." +
     es("Sara è nat<b>a</b> a Shiraz. · Abbiamo chiest<b>o</b> un appuntamento.")},
  completa("Karim ___ (nascere) a Casablanca nel 1985. Da bambino ___ (frequentare) la scuola nel suo quartiere. Nel 2009 ___ (partire) per l'Italia "
           "e ___ (arrivare) a Bari. All'inizio ___ (lavorare) come aiuto cuoco, poi ___ (fare) un corso di elettricista. "
           "Nel 2015 ___ (conoscere) Zineb e nel 2017 ___ (sposarsi). L'anno scorso ___ (superare) l'esame B1.",
           ["è nato", "ha frequentato", "è partito", "è arrivato", "ha lavorato", "ha fatto", "ha conosciuto", ("si sono sposati", "si è sposato"), "ha superato"],
           "4 · La storia di Karim: scrivi il passato prossimo", "4 · Passato prossimo", "e4", None, "Scrivi il verbo al passato prossimo."),
  scrivi([("1. Sara (nascere) … a Teheran.", "è nata"), ("2. Noi (chiedere) … l'atto di nascita.", "abbiamo chiesto"),
          ("3. Le mie sorelle (trasferirsi) … a Milano.", "si sono trasferite"), ("4. Tu (leggere) … le istruzioni?", "hai letto"),
          ("5. Mio padre (vivere) … per vent'anni in Germania.", ("ha vissuto", "è vissuto")), ("6. Voi (rispondere) … all'email?", "avete risposto")],
         "5 · Avere o essere? Scrivi il verbo", "5 · Avere o essere", "e5", w="m"),
  {"part": "Il registro formale"},
  scrivi([("1. Come ti chiami? →", "come si chiama"), ("2. Da dove vieni? →", ("da dove viene", "di dov'è", "di dove è")),
          ("3. Dove vivi? →", "dove vive"), ("4. Che lavoro fai? →", "che lavoro fa"), ("5. Quando sei arrivato in Italia? →", ("quando è arrivato in italia", "quando è arrivato"))],
         "6 · Dal tu al Lei", "6 · Il Lei", "e6", cons="Trasforma la domanda informale in formale.", w="w"),
  {"part": "Lezione B · Documenti e nostalgia", "teoria":
     tab(("-are", "abitavo, abitava"), ("-ere", "vivevo, viveva"), ("-ire", "dormivo, dormiva"), ("essere", "ero, era, erano"), head=("verbo", "imperfetto")) +
     "<b>Imperfetto</b> per descrivere e per le abitudini del passato; <b>passato prossimo</b> per un fatto finito." +
     es("Quando <b>ero</b> piccolo <b>vivevo</b> con i nonni. · A ottobre <b>sono tornato</b> in Marocco.")},
  completa("Quando ___ (essere) piccola, ___ (abitare) in un villaggio vicino al mare. Ogni mattina mio padre ___ (andare) a pescare "
           "e mia madre ___ (preparare) il pane. Noi bambini ___ (giocare) sulla spiaggia fino a sera.",
           ["ero", "abitavo", "andava", "preparava", "giocavamo"], "7 · Completa con l'imperfetto", "7 · Imperfetto", "e7", None, "Scrivi il verbo all'imperfetto."),
  scegli([("1. Ieri ___ in comune per il certificato.", ["andavo", "sono andato"], "sono andato"),
          ("2. Da bambino ___ sempre a calcio con i miei cugini.", ["giocavo", "ho giocato"], "giocavo"),
          ("3. La casa dei miei nonni ___ grande e luminosa.", ["era", "è stata"], "era"),
          ("4. Nel 2019 ___ il permesso di lungo periodo.", ["ricevevo", "ho ricevuto"], "ho ricevuto"),
          ("5. Mentre ___ la domanda, è suonato il telefono.", ["compilavo", "ho compilato"], "compilavo")],
         "8 · Imperfetto o passato prossimo?", "8 · Imperfetto o passato", "e8"),
  {"part": "Educazione civica"},
  {"id": "e9", "title": "9 · Leggi il testo e rispondi", "short": "9 · Lettura", "type": "choice", "full": True,
   "info": "<p>La cittadinanza italiana si può chiedere per <b>residenza</b> (in genere dopo 10 anni di residenza legale per chi non è cittadino UE) "
           "oppure per <b>matrimonio</b> con un cittadino o una cittadina italiana. Chi chiede la cittadinanza deve dimostrare di conoscere "
           "l'italiano almeno al livello <b>B1</b>, di avere un reddito sufficiente e di non avere condanne gravi.</p>"
           "<p>La domanda si presenta <b>online</b> sul portale del Ministero dell'Interno. Quando la cittadinanza è concessa, la persona "
           "<b>giura</b> fedeltà alla Repubblica davanti al sindaco del suo Comune. Da quel giorno è cittadina italiana e anche "
           "<b>cittadina dell'Unione europea</b>: può votare e circolare liberamente in tutti i Paesi dell'UE.</p>",
   "items": [{"q": "1. Per chiedere la cittadinanza per residenza servono in genere…", "opts": ["5 anni", "10 anni", "20 anni"]},
             {"q": "2. Il livello minimo di italiano è…", "opts": ["A2", "B1", "C1"]},
             {"q": "3. La domanda si presenta…", "opts": ["in comune", "in questura", "online"]},
             {"q": "4. Il giuramento si fa davanti…", "opts": ["al sindaco", "al prefetto", "al giudice"]},
             {"q": "5. Un nuovo cittadino italiano è anche…", "opts": ["cittadino europeo", "cittadino del Consiglio d'Europa", "residente all'estero"]}],
   "k": [eq(a) for a in ["10 anni", "B1", "online", "al sindaco", "cittadino europeo"]]},
  libero("e10", 10, "Una cartolina dal mio Paese", "Scrivi una breve cartolina (60-80 parole) a un compagno: racconta un ricordo della tua infanzia (imperfetto) "
         "e una cosa che hai fatto l'ultima volta che sei tornato/a nel tuo Paese (passato prossimo).", ["Caro/a …"], rows=6),
  parla("e11", 11, "Che cosa significa per te essere cittadino? Quali diritti e quali doveri sono più importanti? (1-2 minuti)"),
 ]
}

# ---------------------------------------------------------------- elenco
SLIDE_SF = [
    ("alfa-ciao-io-sono/index.html", "CIAO, IO SONO", "ALFABETIZZAZIONE", ALFA1_SLIDE, "alfa"),
    ("a2-la-salute/index.html", "La salute", "A2", A2SAL_SLIDE, "a2"),
    ("b1-cittadinanza/index.html", "La cittadinanza italiana", "B1", B1CIT_SLIDE, "b1"),
]
ESERCIZI_SF = [("alfa-ciao-io-sono", ALFA1), ("a2-la-salute", A2SAL), ("b1-cittadinanza", B1CIT)]

# ---------------------------------------------------------------- giochi (memory, impiccato, quiz a tempo, cerca la parola)
GIOCHI_SF = {
 "alfa-ciao-io-sono": ("alfa-percorso", "ALFABETIZZAZIONE", "👋 GIOCHI: CIAO, IO SONO", [
  ["CIAO", "👋", "SALUTO GLI AMICI"], ["IO", "🙋", "IO SONO…"], ["SONO", "🪪", "IO … BAKARY"], ["PIACERE", "🤝", "DICO QUANDO CONOSCO UNA PERSONA"],
  ["VENGO", "🌍", "… DAL MALI"], ["NOME", "🔤", "BAKARY È IL…"], ["COGNOME", "👪", "IL NOME DELLA FAMIGLIA"], ["TELEFONO", "📞", "IL MIO NUMERO DI…"],
  ["UNO", "1️⃣", "1"], ["DUE", "2️⃣", "2"], ["TRE", "3️⃣", "3"], ["OTTO", "8️⃣", "8"], ["DIECI", "🔟", "10"], ["ZERO", "0️⃣", "0"],
  ["EURO", "💶", "I SOLDI IN ITALIA"], ["OLIO", "🫒", "COMINCIA CON O"], ["ESTATE", "☀️", "FA CALDO"], ["SCUOLA", "🏫", "STUDIO QUI"]]),
 "a2-la-salute": ("a2-vivere-insieme", "A2", "🩺 GIOCHI: LA SALUTE (A2)", [
  ["LA GOLA", "🗣️", "MAL DI… QUANDO NON POSSO PARLARE"], ["LA SCHIENA", "🧍", "DIETRO, DAL COLLO ALLE GAMBE"], ["IL GINOCCHIO", "🦵", "IN MEZZO ALLA GAMBA"],
  ["LO STOMACO", "🍽️", "QUI VA IL CIBO"], ["LA FEBBRE", "🤒", "38 GRADI"], ["LA TOSSE", "😷", "LO SCIROPPO È PER LA…"], ["LA RICETTA", "📝", "LA SCRIVE IL MEDICO PER I FARMACI"],
  ["L'IMPEGNATIVA", "📄", "SERVE PER LA VISITA SPECIALISTICA"], ["LE COMPRESSE", "💊", "LE PRENDO CON UN BICCHIERE D'ACQUA"], ["LA POMATA", "🧴", "LA METTO SULLA PELLE"],
  ["IL DENTISTA", "🦷", "CURA I DENTI"], ["L'OCULISTA", "👁️", "CURA GLI OCCHI"], ["IL PEDIATRA", "🧒", "IL MEDICO DEI BAMBINI"], ["L'ORTOPEDICO", "🦴", "CURA LE OSSA"],
  ["IL CUP", "📅", "QUI PRENOTO LE VISITE"], ["LA GUARDIA MEDICA", "🌙", "DI NOTTE E NEI GIORNI FESTIVI"], ["IL PRONTO SOCCORSO", "🏥", "IN OSPEDALE, PER LE URGENZE"], ["IL CONSULTORIO", "👩‍👧", "PER DONNE, MAMME E BAMBINI"]]),
 "b1-cittadinanza": ("b1-cittadini", "B1", "🇮🇹 GIOCHI: LA CITTADINANZA (B1)", [
  ["LA CITTADINANZA", "🇮🇹", "SI CHIEDE DOPO 10 ANNI DI RESIDENZA"], ["IL PATRONATO", "🤝", "UFFICIO GRATUITO CHE AIUTA CON LE PRATICHE"], ["LO SPID", "🔑", "CREDENZIALI PER I SITI PUBBLICI"],
  ["LA DOMANDA", "💻", "SI PRESENTA ONLINE"], ["LA RESIDENZA", "🏠", "DOVE ABITI PER LEGGE"], ["IL GIURAMENTO", "✋", "SI FA DAVANTI AL SINDACO"], ["IL SINDACO", "🏛️", "IL CAPO DEL COMUNE"],
  ["LA PREFETTURA", "🏢", "UFFICIO DELLO STATO IN OGNI PROVINCIA"], ["IL REDDITO", "💶", "I SOLDI CHE GUADAGNI IN UN ANNO"], ["LA MARCA DA BOLLO", "🧾", "SI COMPRA DAL TABACCAIO"],
  ["L'ATTO DI NASCITA", "👶", "DICE DOVE E QUANDO SEI NATO"], ["LA TRADUZIONE", "🌐", "DA UNA LINGUA ALL'ALTRA"], ["IL PASSAPORTO", "🛂", "DOCUMENTO PER VIAGGIARE"],
  ["IL VOTO", "🗳️", "IL DIRITTO DI SCEGLIERE CHI GOVERNA"], ["LA COSTITUZIONE", "📜", "LA LEGGE PIÙ IMPORTANTE"], ["L'EUROPA", "🇪🇺", "UNIONE DI 27 PAESI"],
  ["IL DIRITTO", "⚖️", "UNA COSA CHE PUOI FARE PER LEGGE"], ["IL DOVERE", "📌", "UNA COSA CHE DEVI FARE PER LEGGE"]]),
}

<<<<<<< HEAD
def build_giochi(giochi=None):
    import json
    from giochi_pagine import PAGINA
    for cartella, (sezione, liv, titolo, parole) in (giochi or GIOCHI_SF).items():
=======
def build_giochi():
    import json
    from giochi_pagine import PAGINA
    for cartella, (sezione, liv, titolo, parole) in GIOCHI_SF.items():
>>>>>>> origin/claude/project-thread-i5fd4r
        dati = json.dumps({"id": cartella, "titolo": titolo, "parole": parole}, ensure_ascii=False)
        html = (PAGINA % {"titolo": titolo, "titolo_breve": titolo.split(" ", 1)[1].title(), "sezione": sezione, "dati": dati}).replace("LIVELLO A1", "LIVELLO " + liv)
        open(cartella + "/giochi.html", "w", encoding="utf-8").write(html)
        print("scritto", cartella + "/giochi.html")

if __name__ == "__main__":
    for path, unit, top, sl, liv in SLIDE_SF:
        build_slide(path, unit, top, sl, liv)
    for cartella, dati in ESERCIZI_SF:
        build_es(cartella + "/esercizi.html", dati)
    build_giochi()
