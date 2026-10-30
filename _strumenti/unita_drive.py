"""Unità nuove dal materiale della cartella «drive» di Erila (2026-10-30).
I libri e le schede con copyright sono serviti solo come traccia degli argomenti: tutti i testi sono scritti per il sito.
Nove unità, tutte in STAMPATELLO MAIUSCOLO:
  cantiere/ (lavoro, A1)            · L'ABC dell'edilizia, Meet the Need (edilizia)
  cucina-lavoro/ (cucina, A1)       · dizionario visivo cibo 1-2 (Balboni), VERBI DA USARE in cucina, Meet the Need (ristorazione)
  carne-pesce/ (cucina, A1)         · dizionario visivo cibo 5-7, Scheda 02 Lessico (Loescher), calorie della carne
  bar/ (città, A1)                  · Come si dice…? (al bar)
  treno/ (città, A1)                · Come si dice…? (prendere un treno)
  posta-banca/ (educazione civica, A2) · Come si dice…? (in banca, alla posta)
  farmacia/ (salute, A1/A2)         · Come si dice…? (in farmacia, al pronto soccorso)
  comune-questura/ (educazione civica, A2) · Come si dice…? (in comune, in questura)
  assistente-familiare/ (lavoro, A2) · Meet the Need (assistenza alla persona)
Le immagini in img/ sono generate con Canva. Uso: python3 _strumenti/slide.py e python3 _strumenti/genera.py"""
from genera import eq, has, all_
from unita_primi import cover, slide, cards, table, nota, dialogo, end
from unita_civica import passi, PASSI_CSS
from foto_cibi import foto, crediti_slide, foto_quiz, FOTO_CSS

ILL_CSS = PASSI_CSS + """
  .ill{display:block; margin:0 auto 14px; max-width:100%; max-height:46vh; border-radius:18px; border:3px solid #e3edf8; background:#fff;}
  .twocol2 .ill{max-height:52vh;}
  .colori4{display:grid; grid-template-columns:repeat(4,1fr); gap:12px;}
  .colori4 div{border-radius:14px; padding:14px; color:#fff; font-weight:bold; font-size:1.3rem; text-align:center;}
  .colori4 span{display:block; font-weight:normal; font-size:1rem; margin-top:6px;}
  @media (max-width:900px){ .colori4{grid-template-columns:1fr 1fr;} .colori4 div{font-size:1.05rem;} }"""

def ill(f, alt):
    return '    <img class="ill" src="img/%s" alt="%s" loading="lazy" onerror="this.remove()">' % (f, alt)

def ill2(f, alt, inner):
    return '    <div class="twocol2">\n  ' + ill(f, alt) + "\n" + inner + "\n    </div>"

def colori4(items):
    return '    <div class="colori4">\n' + "".join(
        '      <div style="background:%s">%s<span>%s</span></div>\n' % c for c in items) + "    </div>"

def vf(items, keys, title, short, eid, info=None):
    d = {"id": eid, "title": title, "short": short, "type": "choice", "opts": ["VERO", "FALSO"], "full": True,
         "items": [{"q": q} for q in items], "k": [eq(a) for a in keys]}
    if info: d["info"] = info
    return d

def scegli(items, title, short, eid, info=None, cons=None):
    """items: (domanda, [opzioni], giusta)"""
    d = {"id": eid, "title": title, "short": short, "type": "choice", "full": True,
         "items": [{"q": q, "opts": o} for q, o, _ in items], "k": [eq(a) for _, _, a in items]}
    if info: d["info"] = info
    if cons: d["cons"] = cons
    return d

def menu(opts, items, title, short, eid, cons=None):
    """items: (frase, giusta)"""
    d = {"id": eid, "title": title, "short": short, "type": "select", "opts": opts,
         "items": [{"q": q} for q, _ in items], "k": [eq(a) for _, a in items]}
    if cons: d["cons"] = cons
    return d

def scrivi(items, title, short, eid, cons=None, bank=None, w=None):
    """items: (domanda, [risposte accettate])"""
    d = {"id": eid, "title": title, "short": short, "type": "text",
         "items": [{"q": q} for q, _ in items], "k": [eq(*a) for _, a in items]}
    if cons: d["cons"] = cons
    if bank: d["bank"] = bank
    if w: d["w"] = w
    return d

def ordina(items, title, short, eid, cons="METTI IN ORDINE: 1, 2, 3…"):
    """items nell'ordine giusto; nella pagina compaiono mescolati con una permutazione fissa"""
    n = len(items)
    perm = [(i * 3 + 1) % n for i in range(n)] if n % 3 else [(i * 2 + 1) % n for i in range(n)]
    if sorted(perm) != list(range(n)):
        perm = list(range(1, n)) + [0]
    return {"id": eid, "title": title, "short": short, "type": "order", "cons": cons,
            "items": [items[p] for p in perm], "k": [eq(str(p + 1)) for p in perm]}

def completa(parts_text, keys, title, short, eid, bank, cons="SCRIVI LA PAROLA GIUSTA."):
    """parts_text con ___ al posto delle parole mancanti"""
    pezzi = parts_text.split("___")
    parts = []
    for i, p in enumerate(pezzi):
        parts.append(p)
        if i < len(pezzi) - 1:
            parts.append({})
    return {"id": eid, "title": title, "short": short, "type": "cloze", "cons": cons, "bank": bank,
            "parts": parts, "k": [eq(*k) if isinstance(k, (list, tuple)) else eq(k) for k in keys]}

def parla(eid, n, testo):
    return {"id": eid, "title": "%d 🎤 · Parla tu" % n, "type": "record", "items": [testo]}

def libero(eid, n, title, cons, items, rows=2):
    return {"id": eid, "title": "%d ✎ · %s" % (n, title), "type": "free", "rows": rows, "cons": cons, "items": items}


# =====================================================================
# 1. IN CANTIERE (lavoro, A1)
# =====================================================================
CANTIERE_SLIDE = [
    cover("👷", "IN CANTIERE", "LA SICUREZZA, GLI ATTREZZI, LE PAROLE DEL LAVORO", "EDILIZIA &bull; A1"),
    slide("CHE COSA IMPARIAMO?", cards([
        ("🦺", "LA SICUREZZA", "I DISPOSITIVI DI PROTEZIONE (DPI)"), ("🧰", "GLI ATTREZZI", "DEL MURATORE E DEL CARPENTIERE"),
        ("🏗️", "IL CANTIERE", "LA GRU, IL PONTEGGIO, LA BETONIERA"), ("🗣️", "PARLARE IN CANTIERE", "PASSAMI IL MARTELLO! ATTENZIONE!")])),
    slide("🏗️ CHE COS'È UN CANTIERE?", ill2("cantiere.png", "UN CANTIERE CON GRU, PONTEGGIO, BETONIERA E SCALA",
        nota("IL <b>CANTIERE</b> È IL POSTO DOVE SI COSTRUISCE O SI RIPARA UNA CASA, UNA STRADA, UN PONTE.<br><br>"
             "CHI LAVORA IN CANTIERE: IL <b>MURATORE</b>, IL <b>MANOVALE</b>, IL <b>CARPENTIERE</b>, IL <b>FERRAIOLO</b>, "
             "L'<b>ELETTRICISTA</b>, L'<b>IDRAULICO</b>.<br><br>IL CAPO È IL <b>CAPOCANTIERE</b>.", ""))),
    slide("🦺 I DPI: MI PROTEGGO!", ill2("operaio-dpi.png", "UN OPERAIO CON CASCO, OCCHIALI, CUFFIE, GILET, GUANTI E SCARPE",
        cards([("⛑️", "IL CASCO", "PROTEGGE LA TESTA"), ("🥽", "GLI OCCHIALI", "PROTEGGONO GLI OCCHI"),
               ("🎧", "LE CUFFIE", "PROTEGGONO LE ORECCHIE DAL RUMORE"), ("🧤", "I GUANTI", "PROTEGGONO LE MANI"),
               ("🥾", "LE SCARPE ANTINFORTUNISTICHE", "PROTEGGONO I PIEDI"), ("🦺", "IL GILET ARANCIONE", "TUTTI MI VEDONO")]))),
    slide("🦺 ALTRI DPI", cards([
        ("😷", "LA MASCHERINA", "PROTEGGE DALLA POLVERE"), ("👖", "LA TUTA", "IL VESTITO DA LAVORO"),
        ("🪢", "L'IMBRACATURA", "LA CINTURA DI SICUREZZA PER LAVORARE IN ALTO"), ("🧴", "LA CREMA SOLARE", "D'ESTATE, AL SOLE, TUTTO IL GIORNO")]) + "\n" +
        nota("⚠️ SENZA DPI NON SI ENTRA IN CANTIERE. È LA <b>LEGGE</b>. IL DATORE DI LAVORO DEVE DARE I DPI <b>GRATIS</b>.")),
    slide("🧰 GLI ATTREZZI DEL MURATORE", ill2("attrezzi-muratore.png", "CAZZUOLA, MARTELLO, LIVELLA, METRO, SECCHIO, CARRIOLA, PALA, SCALPELLO",
        table([["🔺", "LA CAZZUOLA", "PER METTERE LA MALTA"], ["🔨", "IL MARTELLO", "PER BATTERE"],
               ["📏", "LA LIVELLA", "È DRITTO? CONTROLLO"], ["📐", "IL METRO", "PER MISURARE"],
               ["🪣", "IL SECCHIO", "PER L'ACQUA E LA MALTA"], ["🛒", "LA CARRIOLA", "PER PORTARE SABBIA E MATTONI"],
               ["⛏️", "LA PALA", "PER PRENDERE LA SABBIA"], ["🪨", "LO SCALPELLO", "PER ROMPERE"]]))),
    slide("🪚 GLI ATTREZZI DEL CARPENTIERE E DEL FERRAIOLO", cards([
        ("🪚", "LA SEGA", "PER TAGLIARE IL LEGNO"), ("📌", "I CHIODI", "SI BATTONO CON IL MARTELLO"),
        ("🔩", "IL TRAPANO", "PER FARE I BUCHI"), ("🔧", "LA TENAGLIA", "PER TOGLIERE I CHIODI E LEGARE IL FERRO"),
        ("🪛", "IL CACCIAVITE", "PER LE VITI"), ("🧱", "IL TONDINO DI FERRO", "IL FERRO DENTRO IL CEMENTO")], "g3")),
    slide("🏗️ LE MACCHINE E LE ATTREZZATURE", cards([
        ("🏗️", "LA GRU", "ALZA I PESI"), ("🪜", "IL PONTEGGIO", "PER LAVORARE IN ALTO, FUORI DAL PALAZZO"),
        ("🌀", "LA BETONIERA", "FA IL CALCESTRUZZO"), ("🪜", "LA SCALA", "PER SALIRE"),
        ("🧱", "I MATTONI", "PER FARE I MURI"), ("⏳", "LA SABBIA E IL CEMENTO", "CON L'ACQUA FANNO LA MALTA")], "g3")),
    slide("🚧 I CARTELLI DEL CANTIERE", ill("cartelli-sicurezza.png", "QUATTRO CARTELLI DI SICUREZZA: OBBLIGO, DIVIETO, PERICOLO, EMERGENZA") + "\n" + colori4([
        ("#1f6fd1", "🔵 OBBLIGO", "DEVI! (ES. È OBBLIGATORIO IL CASCO)"), ("#d63a2f", "🔴 DIVIETO", "NON PUOI! (ES. VIETATO L'ACCESSO)"),
        ("#e0a800", "🟡 PERICOLO", "ATTENZIONE! (ES. CARICHI SOSPESI)"), ("#1e9e5a", "🟢 EMERGENZA", "QUI TROVI AIUTO (ES. USCITA, PRONTO SOCCORSO)")]) + "\n" +
        nota("CARICHI SOSPESI = SOPRA DI TE LA GRU PORTA DEI PESI. NON STARE SOTTO!")),
    slide("🗣️ PARLARE IN CANTIERE", dialogo([
        ("*CAPOCANTIERE", "OMAR, HAI IL CASCO?"),
        ("OMAR", "SÌ, CAPO. CE L'HO."),
        ("*CAPOCANTIERE", "BENE. PRENDI LA CARRIOLA E PORTA I MATTONI AL PRIMO PIANO."),
        ("OMAR", "VA BENE. DOVE LI METTO?"),
        ("*CAPOCANTIERE", "VICINO AL MURO. POI PASSAMI LA LIVELLA, PER FAVORE."),
        ("OMAR", "ECCO LA LIVELLA."),
        ("*CAPOCANTIERE", "ATTENZIONE! LA GRU! FERMATI!"),
        ("OMAR", "OK, ASPETTO.")])),
    slide("📢 PAROLE VELOCI", table([
        ["PASSAMI…", "DAMMI (UN ATTREZZO)", "PASSAMI IL MARTELLO!"], ["PORTA…", "PRENDI E VAI", "PORTA LA SABBIA!"],
        ["METTI…", "METTI (IL CASCO, I GUANTI)", "METTI I GUANTI!"], ["ATTENZIONE!", "C'È UN PERICOLO", "ATTENZIONE, SCALINO!"],
        ["FERMATI!", "STOP", "FERMATI! LA GRU!"], ["NON HO CAPITO", "PUOI RIPETERE?", "SCUSA, NON HO CAPITO. PUOI RIPETERE?"]],
        head=["PAROLA", "SIGNIFICA", "ESEMPIO"])),
    end("ORA SAI LE PAROLE DEL CANTIERE!"),
]

CANTIERE = {
 "title": "👷 In cantiere · Esercizi", "store": "cantiere", "upper": True,
 "sections": [
  {"part": "La sicurezza"},
  menu(["LA TESTA", "GLI OCCHI", "LE ORECCHIE", "LE MANI", "I PIEDI"],
       [("1. IL CASCO PROTEGGE…", "LA TESTA"), ("2. I GUANTI PROTEGGONO…", "LE MANI"), ("3. LE CUFFIE PROTEGGONO…", "LE ORECCHIE"),
        ("4. LE SCARPE ANTINFORTUNISTICHE PROTEGGONO…", "I PIEDI"), ("5. GLI OCCHIALI PROTEGGONO…", "GLI OCCHI")],
       "1 · Che cosa protegge?", "1 · I DPI", "e1"),
  scrivi([("1. ⛑️ IL C _ S C O", ["casco", "il casco"]), ("2. 🧤 I G U A N _ I", ["guanti", "i guanti"]),
          ("3. 🥽 GLI O C C H I A _ I", ["occhiali", "gli occhiali"]), ("4. 😷 LA M A S C H E R _ N A", ["mascherina", "la mascherina"]),
          ("5. 👖 LA T _ T A", ["tuta", "la tuta"]), ("6. 🎧 LE C U F F _ E", ["cuffie", "le cuffie"])],
         "2 · Scrivi la parola", "2 · Le parole", "e2", cons="MANCA UNA LETTERA. SCRIVI TUTTA LA PAROLA."),
  vf(["1. SENZA DPI POSSO ENTRARE IN CANTIERE.", "2. IL DATORE DI LAVORO DEVE DARE I DPI GRATIS.",
      "3. L'IMBRACATURA SERVE PER LAVORARE IN ALTO.", "4. SOTTO I CARICHI SOSPESI POSSO STARE TRANQUILLO.",
      "5. IL GILET ARANCIONE SERVE PER ESSERE VISTO."], ["FALSO", "VERO", "VERO", "FALSO", "VERO"],
     "3 · Vero o falso?", "3 · Vero o falso", "e3"),
  {"part": "Gli attrezzi"},
  menu(["LA CAZZUOLA", "IL MARTELLO", "LA LIVELLA", "IL METRO", "LA CARRIOLA", "LA SEGA", "IL TRAPANO"],
       [("1. PER MISURARE IL MURO USO…", "IL METRO"), ("2. PER FARE UN BUCO NEL MURO USO…", "IL TRAPANO"),
        ("3. PER PORTARE I MATTONI USO…", "LA CARRIOLA"), ("4. PER METTERE LA MALTA USO…", "LA CAZZUOLA"),
        ("5. PER CONTROLLARE SE È DRITTO USO…", "LA LIVELLA"), ("6. PER TAGLIARE IL LEGNO USO…", "LA SEGA"),
        ("7. PER BATTERE I CHIODI USO…", "IL MARTELLO")],
       "4 · Quale attrezzo uso?", "4 · Gli attrezzi", "e4"),
  {"id": "e5", "title": "5 · Guarda l'immagine e scrivi", "short": "5 · L'immagine", "type": "text",
   "img": "img/attrezzi-muratore.png", "alt": "OTTO ATTREZZI DEL MURATORE",
   "cons": "NELL'IMMAGINE CI SONO 8 ATTREZZI. SCRIVI IL NOME CON L'ARTICOLO.",
   "bank": "IL SECCHIO · LA PALA · LA LIVELLA · IL MARTELLO · LA CARRIOLA · IL METRO · LA CAZZUOLA · LO SCALPELLO",
   "items": [{"q": q} for q in ["1. IN ALTO A SINISTRA (È A PUNTA)", "2. IN ALTO, IL SECONDO", "3. IN ALTO, IL TERZO (È GIALLA)", "4. IN ALTO A DESTRA",
                                 "5. IN BASSO A SINISTRA (È BLU)", "6. IN BASSO, IL SECONDO (È ROSSA)", "7. IN BASSO, IL TERZO", "8. IN BASSO A DESTRA"]],
   "k": [eq(*a) for a in [["la cazzuola", "cazzuola"], ["il martello", "martello"], ["la livella", "livella"], ["il metro", "metro"],
                          ["il secchio", "secchio"], ["la carriola", "carriola"], ["la pala", "pala"], ["lo scalpello", "scalpello"]]]},
  {"part": "I cartelli e le parole veloci"},
  menu(["OBBLIGO", "DIVIETO", "PERICOLO", "EMERGENZA"],
       [("1. 🔴 VIETATO L'ACCESSO AI NON ADDETTI", "DIVIETO"), ("2. 🔵 È OBBLIGATORIO USARE IL CASCO", "OBBLIGO"),
        ("3. 🟡 ATTENZIONE: CARICHI SOSPESI", "PERICOLO"), ("4. 🟢 USCITA DI EMERGENZA", "EMERGENZA"),
        ("5. 🔵 USARE I GUANTI", "OBBLIGO"), ("6. 🔴 VIETATO FUMARE", "DIVIETO")],
       "6 · Che cartello è?", "6 · I cartelli", "e6"),
  completa("CAPO: OMAR, ___ IL CASCO!<br>OMAR: SÌ, SUBITO.<br>CAPO: ___ LA CARRIOLA E PORTA I MATTONI.<br>"
           "OMAR: SCUSA, NON HO ___. PUOI RIPETERE?<br>CAPO: PORTA I MATTONI AL PRIMO PIANO. POI ___ IL MARTELLO.<br>"
           "OMAR: ECCO IL MARTELLO.<br>CAPO: ___! LA GRU!",
           ["metti", "prendi", "capito", "passami", ["attenzione", "fermati"]],
           "7 · Completa il dialogo", "7 · Il dialogo", "e7", "METTI · PRENDI · CAPITO · PASSAMI · ATTENZIONE"),
  parla("e8", 8, "SEI IN CANTIERE. CHIEDI AL COLLEGA DI PASSARTI LA CAZZUOLA, DI' CHE NON HAI CAPITO E CHIEDI DI RIPETERE. POI DI' QUALI DPI HAI."),
 ]
}


# =====================================================================
# 2. LAVORO IN CUCINA (cucina, A1)
# =====================================================================
CUCINA_SLIDE = [
    cover("👩‍🍳", "LAVORO IN CUCINA", "GLI OGGETTI, I VERBI, LA TAVOLA", "RISTORANTE &bull; MENSA &bull; A1"),
    slide("CHE COSA IMPARIAMO?", cards([
        ("🍳", "GLI OGGETTI DELLA CUCINA", "PENTOLA, PADELLA, SCOLAPASTA…"), ("🔪", "I VERBI DEL CUOCO", "PELARE, AFFETTARE, SCOLARE…"),
        ("🍽️", "APPARECCHIARE LA TAVOLA", "PIATTI, BICCHIERI, POSATE"), ("🧼", "L'IGIENE", "LE REGOLE DELLA CUCINA")])),
    slide("👩‍🍳 CHI LAVORA IN UN RISTORANTE?", ill("cuoco.png", "UN AIUTO CUOCO CHE TAGLIA LE VERDURE") + "\n" + cards([
        ("👨‍🍳", "IL CUOCO / LA CUOCA", "CUCINA I PIATTI"), ("🧑‍🍳", "L'AIUTO CUOCO", "PREPARA LA VERDURA, AIUTA IL CUOCO"),
        ("🧽", "IL LAVAPIATTI", "LAVA PIATTI, PENTOLE E BICCHIERI"), ("🤵", "IL CAMERIERE / LA CAMERIERA", "PORTA I PIATTI AI TAVOLI"),
        ("🍕", "IL PIZZAIOLO", "FA LA PIZZA"), ("🧾", "IL RESPONSABILE DI SALA", "ACCOGLIE I CLIENTI")], "g3")),
    slide("🍳 GLI OGGETTI DELLA CUCINA", ill2("utensili-cucina.png", "PENTOLA, PADELLA, SCOLAPASTA, GRATTUGIA, MESTOLO, CUCCHIAIO DI LEGNO, TAGLIERE, COLTELLO, FRUSTA, CIOTOLA",
        table([["LA PENTOLA", "PER BOLLIRE L'ACQUA"], ["LA PADELLA", "PER FRIGGERE"], ["LO SCOLAPASTA", "PER TOGLIERE L'ACQUA"],
               ["LA GRATTUGIA", "PER IL FORMAGGIO"], ["IL MESTOLO", "PER IL BRODO"], ["IL CUCCHIAIO DI LEGNO", "PER MESCOLARE"],
               ["IL TAGLIERE", "PER TAGLIARE SOPRA"], ["IL COLTELLO", "PER TAGLIARE"], ["LA FRUSTA", "PER LE UOVA"], ["LA CIOTOLA", "PER METTERE DENTRO"]]))),
    slide("🔥 E ANCORA…", cards([
        ("🔥", "IL FORNELLO", "IL FUOCO PER CUCINARE"), ("♨️", "IL FORNO", "PER LA PIZZA, IL PANE, I DOLCI"),
        ("⚖️", "LA BILANCIA", "PER PESARE: 200 GRAMMI DI FARINA"), ("🧺", "LO STROFINACCIO", "PER ASCIUGARE"),
        ("🫕", "IL COPERCHIO", "SOPRA LA PENTOLA"), ("☕", "LA CAFFETTIERA", "PER IL CAFFÈ")], "g3")),
    slide("🔪 I VERBI DEL CUOCO", table([
        ["🚿", "LAVARE", "LAVO LA FRUTTA SOTTO L'ACQUA"], ["🥔", "PELARE", "TOLGO LA BUCCIA ALLE PATATE"],
        ["🔪", "TAGLIARE", "TAGLIO LA CIPOLLA A PEZZETTI"], ["🍞", "AFFETTARE", "TAGLIO IL PANE A FETTE"],
        ["🧀", "GRATTUGIARE", "GRATTUGIO IL FORMAGGIO"], ["🥄", "MESCOLARE", "GIRO IL SUGO CON IL CUCCHIAIO"]])),
    slide("🔥 ALTRI VERBI", table([
        ["♨️", "BOLLIRE", "L'ACQUA BOLLE A 100 GRADI"], ["🍝", "SCOLARE", "TOLGO L'ACQUA DALLA PASTA"],
        ["🍳", "FRIGGERE", "CUOCIO NELL'OLIO MOLTO CALDO"], ["🫓", "IMPASTARE", "LAVORO FARINA E ACQUA CON LE MANI"],
        ["🥧", "INFORNARE", "METTO NEL FORNO"], ["😋", "ASSAGGIARE", "PROVO UN PO': È BUONO?"]])),
    slide("🍽️ APPARECCHIARE LA TAVOLA", ill2("tavola-apparecchiata.png", "UNA TAVOLA APPARECCHIATA: TOVAGLIA, PIATTI, POSATE, BICCHIERI, TOVAGLIOLO",
        table([["LA TOVAGLIA", "SOPRA IL TAVOLO"], ["IL PIATTO PIANO", "SOTTO"], ["IL PIATTO FONDO", "SOPRA: PER LA PASTA, LA ZUPPA"],
               ["LA FORCHETTA", "A SINISTRA"], ["IL COLTELLO E IL CUCCHIAIO", "A DESTRA"], ["IL BICCHIERE", "IN ALTO A DESTRA"],
               ["IL TOVAGLIOLO", "A SINISTRA"], ["L'OLIERA", "OLIO, ACETO, SALE, PEPE"]]))),
    slide("🧼 LE REGOLE DELLA CUCINA", passi([
        "MI LAVO LE <b>MANI</b> PRIMA DI COMINCIARE E DOPO IL BAGNO.",
        "METTO LA <b>CUFFIA</b> SUI CAPELLI E IL <b>GREMBIULE</b>.",
        "LA CARNE CRUDA E LA VERDURA: <b>DUE TAGLIERI DIVERSI</b>.",
        "IL CIBO VA IN <b>FRIGORIFERO</b> CON LA <b>DATA</b>.",
        "NON TOCCO IL CIBO SE HO UNA <b>FERITA</b> SULLE MANI SENZA GUANTI."]) + "\n" +
        nota("PER LAVORARE IN CUCINA SERVE UN CORSO SULL'IGIENE DEL CIBO: SI CHIAMA <b>HACCP</b>.")),
    slide("🗣️ IN CUCINA", dialogo([
        ("*CUOCA", "AMADOU, LAVA E PELA LE PATATE, PER FAVORE."),
        ("AMADOU", "VA BENE. LE TAGLIO A PEZZETTI?"),
        ("*CUOCA", "NO, AFFETTALE SOTTILI. POI METTI L'ACQUA NELLA PENTOLA."),
        ("AMADOU", "L'ACQUA BOLLE. BUTTO LA PASTA?"),
        ("*CUOCA", "SÌ, E METTI IL SALE. TRA DIECI MINUTI SCOLA LA PASTA."),
        ("AMADOU", "DOV'È LO SCOLAPASTA?"),
        ("*CUOCA", "È SOTTO IL LAVANDINO. BRAVO!")])),
    end("ORA SAI LAVORARE IN CUCINA!"),
]

CUCINA = {
 "title": "👩‍🍳 Lavoro in cucina · Esercizi", "store": "cucina-lavoro", "upper": True,
 "sections": [
  {"part": "Gli oggetti"},
  menu(["LA PENTOLA", "LA PADELLA", "LO SCOLAPASTA", "LA GRATTUGIA", "IL TAGLIERE", "IL MESTOLO", "LA BILANCIA"],
       [("1. PER BOLLIRE L'ACQUA USO…", "LA PENTOLA"), ("2. PER GRATTUGIARE IL FORMAGGIO USO…", "LA GRATTUGIA"),
        ("3. PER SCOLARE LA PASTA USO…", "LO SCOLAPASTA"), ("4. PER FRIGGERE LE PATATE USO…", "LA PADELLA"),
        ("5. PER PESARE LA FARINA USO…", "LA BILANCIA"), ("6. PER PRENDERE IL BRODO USO…", "IL MESTOLO"),
        ("7. PER TAGLIARE LA CIPOLLA SOPRA USO…", "IL TAGLIERE")],
       "1 · Che cosa uso?", "1 · Gli oggetti", "e1"),
  {"id": "e2", "title": "2 · Guarda l'immagine e scrivi", "short": "2 · L'immagine", "type": "text",
   "img": "img/utensili-cucina.png", "alt": "DIECI OGGETTI DELLA CUCINA",
   "cons": "SCRIVI IL NOME CON L'ARTICOLO.",
   "bank": "LA PENTOLA · LA PADELLA · LO SCOLAPASTA · LA GRATTUGIA · IL COLTELLO · IL TAGLIERE",
   "items": [{"q": q} for q in ["1. IN ALTO A SINISTRA (È ROSSA, CON IL COPERCHIO)", "2. IN ALTO, AL CENTRO (È NERA)", "3. IN ALTO A DESTRA (È BLU, CON I BUCHI)",
                                 "4. IN BASSO A SINISTRA", "5. IN BASSO, AL CENTRO (È DI LEGNO, QUADRATO)", "6. IN BASSO, VICINO AL TAGLIERE (TAGLIA)"]],
   "k": [eq(*a) for a in [["la pentola", "pentola"], ["la padella", "padella"], ["lo scolapasta", "scolapasta"],
                          ["la grattugia", "grattugia"], ["il tagliere", "tagliere"], ["il coltello", "coltello"]]]},
  {"part": "I verbi"},
  menu(["LAVARE", "PELARE", "AFFETTARE", "GRATTUGIARE", "MESCOLARE", "BOLLIRE", "SCOLARE", "FRIGGERE", "IMPASTARE", "INFORNARE"],
       [("1. TOLGO LA BUCCIA ALLE CAROTE.", "PELARE"), ("2. METTO LA TORTA NEL FORNO.", "INFORNARE"),
        ("3. TAGLIO IL SALAME A FETTE SOTTILI.", "AFFETTARE"), ("4. L'ACQUA È A 100 GRADI E FA LE BOLLE.", "BOLLIRE"),
        ("5. METTO LA PASTA NELLO SCOLAPASTA.", "SCOLARE"), ("6. LAVORO LA FARINA CON L'ACQUA E IL LIEVITO.", "IMPASTARE"),
        ("7. CUOCIO LE PATATINE NELL'OLIO CALDO.", "FRIGGERE"), ("8. PASSO LA MELA SOTTO L'ACQUA.", "LAVARE"),
        ("9. GIRO IL SUGO CON IL CUCCHIAIO DI LEGNO.", "MESCOLARE"), ("10. METTO IL PARMIGIANO SULLA PASTA CON LA GRATTUGIA.", "GRATTUGIARE")],
       "3 · Che cosa faccio?", "3 · I verbi", "e3"),
  completa("OGGI AMINA PREPARA LA PASTA CON LE ZUCCHINE.<br>PRIMA ___ LE ZUCCHINE SOTTO L'ACQUA. POI LE ___ A FETTE.<br>"
           "METTE L'ACQUA NELLA PENTOLA: QUANDO L'ACQUA ___, BUTTA LA PASTA.<br>NELLA PADELLA ___ LE ZUCCHINE NELL'OLIO.<br>"
           "DOPO DIECI MINUTI ___ LA PASTA E LA METTE NELLA PADELLA. ___ BENE CON IL CUCCHIAIO.<br>ALLA FINE ___ IL FORMAGGIO. BUON APPETITO!",
           ["lava", "affetta", "bolle", "frigge", "scola", "mescola", "grattugia"],
           "4 · La ricetta di Amina", "4 · La ricetta", "e4", "LAVA · AFFETTA · BOLLE · FRIGGE · SCOLA · MESCOLA · GRATTUGIA"),
  {"part": "La tavola e le regole"},
  menu(["A SINISTRA", "A DESTRA", "SOPRA IL PIATTO PIANO", "SOTTO IL PIATTO FONDO"],
       [("1. LA FORCHETTA VA…", "A SINISTRA"), ("2. IL COLTELLO VA…", "A DESTRA"), ("3. IL PIATTO FONDO VA…", "SOPRA IL PIATTO PIANO"),
        ("4. IL CUCCHIAIO VA…", "A DESTRA"), ("5. IL PIATTO PIANO VA…", "SOTTO IL PIATTO FONDO"), ("6. IL TOVAGLIOLO VA…", "A SINISTRA")],
       "5 · Apparecchia la tavola", "5 · La tavola", "e5"),
  vf(["1. MI LAVO LE MANI SOLO A FINE GIORNATA.", "2. IN CUCINA METTO LA CUFFIA SUI CAPELLI.",
      "3. TAGLIO LA CARNE CRUDA E L'INSALATA SULLO STESSO TAGLIERE.", "4. IL CIBO NEL FRIGORIFERO HA LA DATA.",
      "5. PER LAVORARE IN CUCINA SERVE IL CORSO HACCP."], ["FALSO", "VERO", "FALSO", "VERO", "VERO"],
     "6 · Le regole: vero o falso?", "6 · Le regole", "e6"),
  ordina(["LAVO LE PATATE.", "PELO LE PATATE.", "TAGLIO LE PATATE A BASTONCINI.", "FRIGGO LE PATATE NELL'OLIO CALDO.", "METTO IL SALE E SERVO."],
         "7 · Le patatine fritte: metti in ordine", "7 · In ordine", "e7"),
  parla("e8", 8, "SPIEGA COME PREPARI UN PIATTO DEL TUO PAESE. USA I VERBI: LAVO, TAGLIO, METTO, MESCOLO, CUOCIO."),
 ]
}


# =====================================================================
# 3. DAL MACELLAIO E IN PESCHERIA (cucina, A1)
# =====================================================================
CARNE_FOTO = ['pollo', 'tacchino', 'bistecca-manzo', 'costolette-agnello', 'coniglio', 'salsiccia', 'prosciutto-crudo', 'braciola-maiale', 'salame', 'mortadella', 'orata', 'spigola', 'alici', 'salmone', 'tonno', 'pesce-spada', 'polpo', 'calamari', 'cozze', 'vongole', 'gamberi', 'astice', 'spaghetti', 'penne', 'ravioli', 'lasagne', 'gnocchi', 'orecchiette-cime-di-rapa', 'caffe-espresso', 'caffe-macchiato', 'seppie', 'macinato', 'prosciutto-cotto']
CARNE_SLIDE = [
    cover("🥩", "DAL MACELLAIO E IN PESCHERIA", "LA CARNE, IL PESCE, LA PASTA, IL CAFFÈ", "CIBO &bull; A1"),
    slide("CHE COSA IMPARIAMO?", cards([
        ("🥩", "LA CARNE", "POLLO, MANZO, AGNELLO…"), ("🐟", "IL PESCE", "ORATA, ALICI, COZZE…"),
        ("🍝", "LA PASTA", "ORECCHIETTE, SPAGHETTI, PENNE…"), ("☕", "I CAFFÈ", "MACCHIATO, LUNGO, RISTRETTO…")])),
    slide("🥩 LA CARNE", ill("macelleria.png", "IL BANCONE DI UNA MACELLERIA") + "\n" + table([
        [foto("pollo"), "IL POLLO", "IL PETTO, LA COSCIA, LE ALI"], [foto("tacchino"), "IL TACCHINO", ""],
        [foto("bistecca-manzo"), "IL MANZO / IL VITELLO", "LA BISTECCA, IL MACINATO, LO SPEZZATINO"], [foto("costolette-agnello"), "L'AGNELLO", "LE COSTOLETTE"],
        [foto("coniglio"), "IL CONIGLIO", ""], [foto("salsiccia"), "LA SALSICCIA", "DI POLLO, DI MANZO O DI MAIALE"]], head=["", "LA CARNE", "I PEZZI"]) + "\n" +
        nota("☪️ CERCHI LA CARNE <b>HALAL</b>? A BARI CI SONO MACELLERIE HALAL. CHIEDI: «È CARNE HALAL?»")),
    slide("🐖 IL MAIALE E I SALUMI", cards([
        (foto("prosciutto-crudo"), "IL PROSCIUTTO", "CRUDO O COTTO"), (foto("braciola-maiale"), "LA BRACIOLA", "UN PEZZO DI MAIALE CON L'OSSO"),
        (foto("salame"), "IL SALAME", "A FETTE"), (foto("mortadella"), "LA MORTADELLA", "ROSA, CON I PEZZETTI BIANCHI")]) + "\n" +
        nota("⚠️ I SALUMI SONO QUASI SEMPRE DI <b>MAIALE</b>. NON MANGI IL MAIALE? CHIEDI: «C'È IL MAIALE DENTRO?»")),
    slide("🗣️ DAL MACELLAIO", dialogo([
        ("*MACELLAIO", "BUONGIORNO, DICA!"),
        ("FATIMA", "BUONGIORNO. VORREI MEZZO CHILO DI MACINATO DI MANZO."),
        ("*MACELLAIO", "ECCO. ALTRO?"),
        ("FATIMA", "SÌ, QUATTRO COSCE DI POLLO. LA CARNE È HALAL?"),
        ("*MACELLAIO", "IL POLLO SÌ. LO VUOLE PULITO?"),
        ("FATIMA", "SÌ, GRAZIE. QUANTO VIENE?"),
        ("*MACELLAIO", "SONO 12 EURO E 50.")])),
    slide("🐟 IL PESCE", ill("pescheria.png", "IL BANCO DEL PESCE") + "\n" + cards([
        (foto("orata"), "L'ORATA", ""), (foto("spigola"), "LA SPIGOLA (IL BRANZINO)", ""), (foto("alici"), "LE ALICI", "PICCOLE, SI FRIGGONO"),
        (foto("salmone"), "IL SALMONE", "ROSA"), (foto("tonno"), "IL TONNO", "ANCHE IN SCATOLA"), (foto("pesce-spada"), "IL PESCE SPADA", "")], "g3")),
    slide("🦑 I FRUTTI DI MARE", cards([
        (foto("polpo"), "IL POLPO", "A BARI SI MANGIA ANCHE CRUDO!"), (foto("calamari"), "I CALAMARI E LE SEPPIE", ""),
        (foto("cozze"), "LE COZZE", "NERE"), (foto("vongole"), "LE VONGOLE", "PER GLI SPAGHETTI"),
        (foto("gamberi"), "I GAMBERI", ""), (foto("astice"), "L'ASTICE", "COSTA MOLTO")], "g3")),
    slide("🗣️ IN PESCHERIA", dialogo([
        ("*PESCIVENDOLO", "PESCE FRESCO! CHI È IL PROSSIMO?"),
        ("YUSUF", "IO. QUANTO COSTANO LE ORATE?"),
        ("*PESCIVENDOLO", "15 EURO AL CHILO. SONO FRESCHISSIME."),
        ("YUSUF", "NE PRENDO DUE. ME LE PULISCE?"),
        ("*PESCIVENDOLO", "CERTO. LE VUOLE PER IL FORNO?"),
        ("YUSUF", "SÌ. E UN CHILO DI COZZE, PER FAVORE.")])),
    slide("🍝 LA PASTA", ill("pasta.png", "TANTI TIPI DI PASTA") + "\n" + table([
        ["LUNGA", "SPAGHETTI, LINGUINE, TAGLIATELLE"], ["CORTA", "PENNE, FUSILLI, FARFALLE, MACCHERONI, CONCHIGLIE"],
        ["RIPIENA", "RAVIOLI, TORTELLINI (DENTRO C'È CARNE O FORMAGGIO)"], ["AL FORNO", "LASAGNE"],
        ["DI PATATE", "GNOCCHI"], ["DI BARI 💙", "ORECCHIETTE: CON LE CIME DI RAPA!"]], head=["CHE PASTA?", "I NOMI"])),
    slide("🍝 LA PASTA IN FOTO", cards([
        (foto("spaghetti"), "GLI SPAGHETTI", "LUNGA"), (foto("penne"), "LE PENNE", "CORTA"), (foto("ravioli"), "I RAVIOLI", "RIPIENA"),
        (foto("lasagne"), "LE LASAGNE", "AL FORNO"), (foto("gnocchi"), "GLI GNOCCHI", "DI PATATE"), (foto("orecchiette-cime-di-rapa"), "LE ORECCHIETTE", "CON LE CIME DI RAPA")], "g3")),
    slide("⚖️ COM'È? I CONTRARI", table([
        ["CRUDO", "↔", "COTTO"], ["FRESCO", "↔", "SURGELATO"], ["DOLCE", "↔", "AMARO"], ["CALDO", "↔", "FREDDO"],
        ["BUONO", "↔", "CATTIVO"], ["NATURALE (ACQUA)", "↔", "FRIZZANTE"], ["MAGRO", "↔", "GRASSO"]])),
    slide("☕ I CAFFÈ", ill("caffe.png", "SEI TIPI DI CAFFÈ") + "\n" + cards([
        (foto("caffe-espresso"), "IL CAFFÈ (ESPRESSO)", "PICCOLO E FORTE"), (foto("caffe-macchiato"), "IL CAFFÈ MACCHIATO", "CON UN PO' DI LATTE CALDO O FREDDO"),
        ("💧", "IL CAFFÈ LUNGO", "CON PIÙ ACQUA"), ("🔻", "IL CAFFÈ RISTRETTO", "CON MENO ACQUA, PIÙ FORTE"),
        ("☕☕", "IL CAFFÈ DOPPIO", "DUE CAFFÈ IN UNA TAZZA"), ("🚫", "IL DECAFFEINATO (DECA)", "SENZA CAFFEINA")], "g3")),
    slide("📷 LE FOTO", crediti_slide(CARNE_FOTO)),
    end("ORA SAI FARE LA SPESA DAL MACELLAIO E IN PESCHERIA!"),
]

CARNE = {
 "title": "🥩 Dal macellaio e in pescheria · Esercizi", "store": "carne-pesce", "upper": True,
 "sections": [
  {"part": "Carne o pesce?"},
  menu(["CARNE", "PESCE", "FRUTTI DI MARE", "PASTA"],
       [("1. L'ORATA", "PESCE"), ("2. IL TACCHINO", "CARNE"), ("3. LE COZZE", "FRUTTI DI MARE"), ("4. LE ORECCHIETTE", "PASTA"),
        ("5. LA BISTECCA", "CARNE"), ("6. IL POLPO", "FRUTTI DI MARE"), ("7. LE ALICI", "PESCE"), ("8. I FUSILLI", "PASTA"),
        ("9. L'AGNELLO", "CARNE"), ("10. LE VONGOLE", "FRUTTI DI MARE")],
       "1 · Che cos'è?", "1 · Carne o pesce", "e1"),
  scrivi([("1. IL P _ L L O", ["pollo", "il pollo"]), ("2. LA S A L S I C C _ A", ["salsiccia", "la salsiccia"]),
          ("3. IL S A L M _ N E", ["salmone", "il salmone"]), ("4. I G A M B E R _", ["gamberi", "i gamberi"]),
          ("5. IL M A C I N A T _", ["macinato", "il macinato"]), ("6. LE S E P P _ E", ["seppie", "le seppie"])],
         "2 · Scrivi la parola", "2 · Le parole", "e2", cons="MANCA UNA LETTERA. SCRIVI TUTTA LA PAROLA."),
  foto_quiz("f1", "2b · Guarda la foto: che cos'è?", "2b · Le foto",
            [("mortadella", "LA MORTADELLA"), ("orata", "L'ORATA"), ("cozze", "LE COZZE"), ("salsiccia", "LA SALSICCIA"), ("polpo", "IL POLPO"),
             ("salame", "IL SALAME"), ("gamberi", "I GAMBERI"), ("macinato", "IL MACINATO"), ("seppie", "LE SEPPIE"), ("prosciutto-cotto", "IL PROSCIUTTO COTTO")],
            ["IL MACINATO", "IL POLPO", "IL PROSCIUTTO COTTO", "IL SALAME", "I GAMBERI", "L'ORATA", "LA MORTADELLA", "LA SALSICCIA", "LE COZZE", "LE SEPPIE"]),
  {"part": "Al banco"},
  completa("MACELLAIO: BUONGIORNO, ___!<br>FATIMA: BUONGIORNO. ___ MEZZO CHILO DI MACINATO.<br>MACELLAIO: ECCO. ___?<br>"
           "FATIMA: SÌ, DUE PETTI DI POLLO. È CARNE ___?<br>MACELLAIO: SÌ, SIGNORA.<br>FATIMA: QUANTO ___?<br>MACELLAIO: 11 EURO.",
           ["dica", "vorrei", "altro", "halal", "viene"], "3 · Completa il dialogo", "3 · Dal macellaio", "e3",
           "DICA · VORREI · ALTRO · HALAL · VIENE"),
  scegli([("1. QUANTO COSTANO LE ORATE?", ["15 EURO AL CHILO", "2 EURO L'UNA", "NON SI SA"], "15 EURO AL CHILO"),
          ("2. QUANTE ORATE PRENDE YUSUF?", ["DUE", "UNA", "QUATTRO"], "DUE"),
          ("3. CHE COSA CHIEDE YUSUF?", ["DI PULIRE IL PESCE", "UNO SCONTO", "UNA BORSA"], "DI PULIRE IL PESCE"),
          ("4. COME CUCINA LE ORATE?", ["NEL FORNO", "FRITTE", "CRUDE"], "NEL FORNO"),
          ("5. CHE COSA COMPRA ANCHE?", ["UN CHILO DI COZZE", "IL SALMONE", "IL POLPO"], "UN CHILO DI COZZE")],
         "4 · In pescheria: leggi e rispondi", "4 · In pescheria", "e4",
         info="PESCIVENDOLO: PESCE FRESCO! CHI È IL PROSSIMO?<br>YUSUF: IO. QUANTO COSTANO LE ORATE?<br>PESCIVENDOLO: 15 EURO AL CHILO.<br>"
              "YUSUF: NE PRENDO DUE. ME LE PULISCE?<br>PESCIVENDOLO: CERTO. LE VUOLE PER IL FORNO?<br>YUSUF: SÌ. E UN CHILO DI COZZE, PER FAVORE."),
  {"part": "Pasta, contrari e caffè"},
  menu(["LUNGA", "CORTA", "RIPIENA"],
       [("1. GLI SPAGHETTI", "LUNGA"), ("2. I RAVIOLI", "RIPIENA"), ("3. LE PENNE", "CORTA"), ("4. LE TAGLIATELLE", "LUNGA"),
        ("5. I TORTELLINI", "RIPIENA"), ("6. LE FARFALLE", "CORTA"), ("7. LE ORECCHIETTE", "CORTA")],
       "5 · Che pasta è?", "5 · La pasta", "e5"),
  scrivi([("1. CRUDO ↔", ["cotto"]), ("2. FRESCO ↔", ["surgelato"]), ("3. DOLCE ↔", ["amaro"]), ("4. CALDO ↔", ["freddo"]),
          ("5. BUONO ↔", ["cattivo"]), ("6. NATURALE ↔", ["frizzante"])],
         "6 · Scrivi il contrario", "6 · I contrari", "e6", bank="AMARO · CATTIVO · COTTO · FREDDO · FRIZZANTE · SURGELATO"),
  menu(["MACCHIATO", "LUNGO", "RISTRETTO", "DOPPIO", "DECAFFEINATO"],
       [("1. VOGLIO UN CAFFÈ CON UN PO' DI LATTE: UN CAFFÈ…", "MACCHIATO"), ("2. VOGLIO UN CAFFÈ CON PIÙ ACQUA: UN CAFFÈ…", "LUNGO"),
        ("3. NON POSSO PRENDERE LA CAFFEINA: UN CAFFÈ…", "DECAFFEINATO"), ("4. VOGLIO DUE CAFFÈ IN UNA TAZZA: UN CAFFÈ…", "DOPPIO"),
        ("5. VOGLIO UN CAFFÈ MOLTO FORTE, CON POCA ACQUA: UN CAFFÈ…", "RISTRETTO")],
       "7 · Che caffè vuoi?", "7 · I caffè", "e7"),
  parla("e8", 8, "SEI DAL MACELLAIO O IN PESCHERIA. SALUTA, CHIEDI DUE COSE CON LA QUANTITÀ (MEZZO CHILO, UN CHILO…), CHIEDI IL PREZZO E RINGRAZIA."),
 ]
}


# =====================================================================
# 4. AL BAR (città, A1)
# =====================================================================
BAR_FOTO = ['caffe-espresso', 'cappuccino', 'te', 'spremuta-arancia', 'succo-frutta', 'acqua-bottiglia', 'cornetto', 'panino', 'tramezzino', 'panzerotto', 'fetta-torta', 'gelato-cono']
BAR_SLIDE = [
    cover("☕", "AL BAR", "UN CAFFÈ, PER FAVORE!", "ORDINARE &bull; PAGARE &bull; A1"),
    slide("CHE COSA IMPARIAMO?", cards([
        ("☕", "CHE COSA PRENDO?", "CAFFÈ, CAPPUCCINO, SPREMUTA…"), ("🥐", "CHE COSA MANGIO?", "CORNETTO, PANINO, TRAMEZZINO"),
        ("🧾", "COME PAGO?", "ALLA CASSA, LO SCONTRINO"), ("🗣️", "LE FRASI", "VORREI… QUANTO PAGO?")])),
    slide("☕ DA BERE", ill("bancone-bar.png", "IL BANCONE DI UN BAR CON IL BARISTA E UNA CLIENTE") + "\n" + cards([
        (foto("caffe-espresso"), "IL CAFFÈ", ""), (foto("cappuccino"), "IL CAPPUCCINO", "CAFFÈ + LATTE CON LA SCHIUMA"), (foto("te"), "IL TÈ", "CALDO O FREDDO"),
        (foto("spremuta-arancia"), "LA SPREMUTA D'ARANCIA", "ARANCE FRESCHE"), (foto("succo-frutta"), "IL SUCCO DI FRUTTA", "PESCA, PERA, ALBICOCCA"),
        (foto("acqua-bottiglia"), "L'ACQUA", "NATURALE O FRIZZANTE")], "g3")),
    slide("🥐 DA MANGIARE", cards([
        (foto("cornetto"), "IL CORNETTO", "VUOTO, ALLA CREMA, ALLA MARMELLATA"), (foto("panino"), "IL PANINO", "CON FORMAGGIO, CON TONNO…"),
        (foto("tramezzino"), "IL TRAMEZZINO", "PANE MORBIDO A TRIANGOLO"), (foto("panzerotto"), "IL PANZEROTTO", "A BARI! FRITTO, CON POMODORO E MOZZARELLA"),
        (foto("fetta-torta"), "IL DOLCE", "UNA FETTA DI TORTA"), (foto("gelato-cono"), "IL GELATO", "COPPETTA O CONO")], "g3")),
    slide("🧾 COME FUNZIONA?", passi([
        "IN ALCUNI BAR PRIMA VADO ALLA <b>CASSA</b>: DICO CHE COSA PRENDO E PAGO.",
        "LA CASSIERA MI DÀ LO <b>SCONTRINO</b>.",
        "VADO AL <b>BANCONE</b> E DO LO SCONTRINO AL BARISTA.",
        "IL BARISTA PREPARA IL CAFFÈ. LO BEVO IN PIEDI, AL BANCO."]) + "\n" +
        nota("☝️ AL <b>BANCO</b> (IN PIEDI) COSTA MENO. AL <b>TAVOLO</b> (SEDUTO) A VOLTE COSTA DI PIÙ: VIENE IL CAMERIERE.")),
    slide("🗣️ AL BANCO", dialogo([
        ("*BARISTA", "BUONGIORNO! CHE COSA PRENDE?"),
        ("MARYAM", "BUONGIORNO. UN CAPPUCCINO E UN CORNETTO, PER FAVORE."),
        ("*BARISTA", "IL CORNETTO VUOTO O ALLA CREMA?"),
        ("MARYAM", "ALLA CREMA. E UN BICCHIERE D'ACQUA."),
        ("*BARISTA", "NATURALE O FRIZZANTE?"),
        ("MARYAM", "NATURALE, GRAZIE. QUANTO PAGO?"),
        ("*BARISTA", "3 EURO E 20. LO SCONTRINO È QUI.")])),
    slide("🗣️ LE FRASI UTILI", table([
        ["PER ORDINARE", "VORREI UN CAFFÈ. / PRENDO UN TÈ. / MI DÀ UNA SPREMUTA?"],
        ["PER CHIEDERE", "C'È IL CORNETTO VEGANO? / CHE PANINI AVETE?"],
        ["PER PAGARE", "QUANTO PAGO? / QUANT'È? / POSSO PAGARE CON LA CARTA?"],
        ["PER OFFRIRE", "OFFRO IO! / TI OFFRO UN CAFFÈ."], ["PER RINGRAZIARE", "GRAZIE, BUONA GIORNATA!"]])),
    slide("☕ IL CAFFÈ IN ITALIA", cards([
        ("🌅", "LA MATTINA", "CAPPUCCINO E CORNETTO: È LA COLAZIONE AL BAR"), ("🍽️", "DOPO PRANZO", "UN CAFFÈ. IL CAPPUCCINO DI SOLITO NO!"),
        ("🤝", "CON GLI AMICI", "«PRENDIAMO UN CAFFÈ?» = PARLIAMO UN PO'"), ("⏱️", "VELOCE", "IL CAFFÈ AL BANCO SI BEVE IN 2 MINUTI")])),
    slide("📷 LE FOTO", crediti_slide(BAR_FOTO)),
    end("ORA SAI ORDINARE AL BAR!"),
]

BAR = {
 "title": "☕ Al bar · Esercizi", "store": "bar", "upper": True,
 "sections": [
  {"part": "Che cosa prendo?"},
  menu(["DA BERE", "DA MANGIARE"],
       [("1. IL CORNETTO", "DA MANGIARE"), ("2. LA SPREMUTA", "DA BERE"), ("3. IL TRAMEZZINO", "DA MANGIARE"), ("4. IL CAPPUCCINO", "DA BERE"),
        ("5. IL PANZEROTTO", "DA MANGIARE"), ("6. IL TÈ", "DA BERE"), ("7. IL SUCCO DI FRUTTA", "DA BERE"), ("8. IL PANINO", "DA MANGIARE")],
       "1 · Da bere o da mangiare?", "1 · Bere o mangiare", "e1"),
  scrivi([("1. C A P P U C C _ N O", ["cappuccino"]), ("2. C O R N E T T _", ["cornetto"]), ("3. S P R E M U T _", ["spremuta"]),
          ("4. S C O N T R _ N O", ["scontrino"]), ("5. B A R I S T _", ["barista"]), ("6. T R A M E Z Z _ N O", ["tramezzino"])],
         "2 · Scrivi la parola", "2 · Le parole", "e2", cons="MANCA UNA LETTERA. SCRIVI TUTTA LA PAROLA."),
  foto_quiz("f1", "2b · Guarda la foto: che cos'è?", "2b · Le foto",
            [("cappuccino", "IL CAPPUCCINO"), ("cornetto", "IL CORNETTO"), ("panzerotto", "IL PANZEROTTO"), ("spremuta-arancia", "LA SPREMUTA"),
             ("tramezzino", "IL TRAMEZZINO"), ("caffe-espresso", "IL CAFFÈ"), ("gelato-cono", "IL GELATO"), ("te", "IL TÈ")],
            ["IL CAFFÈ", "IL CAPPUCCINO", "IL CORNETTO", "IL GELATO", "IL PANZEROTTO", "IL TÈ", "IL TRAMEZZINO", "LA SPREMUTA"]),
  {"part": "Al banco"},
  ordina(["VADO ALLA CASSA E DICO CHE COSA PRENDO.", "PAGO.", "PRENDO LO SCONTRINO.", "DO LO SCONTRINO AL BARISTA.", "BEVO IL CAFFÈ AL BANCO."],
         "3 · Come funziona? Metti in ordine", "3 · In ordine", "e3"),
  completa("BARISTA: BUONGIORNO! CHE COSA ___?<br>OMAR: BUONGIORNO. ___ UN CAFFÈ E UNA SPREMUTA.<br>BARISTA: ECCO A LEI.<br>"
           "OMAR: ___ PAGO?<br>BARISTA: 4 EURO.<br>OMAR: POSSO PAGARE CON LA ___?<br>BARISTA: CERTO.<br>OMAR: GRAZIE, BUONA ___!",
           ["prende", ["vorrei", "prendo"], "quanto", "carta", "giornata"], "4 · Completa il dialogo", "4 · Il dialogo", "e4",
           "PRENDE · VORREI · QUANTO · CARTA · GIORNATA"),
  scegli([("1. CHE COSA PRENDE MARYAM DA BERE?", ["UN CAPPUCCINO", "UN TÈ", "UNA SPREMUTA"], "UN CAPPUCCINO"),
          ("2. COM'È IL CORNETTO?", ["ALLA CREMA", "VUOTO", "ALLA MARMELLATA"], "ALLA CREMA"),
          ("3. L'ACQUA È…", ["NATURALE", "FRIZZANTE", "CALDA"], "NATURALE"),
          ("4. QUANTO PAGA?", ["3 EURO E 20", "2 EURO", "5 EURO E 50"], "3 EURO E 20")],
         "5 · Leggi e rispondi", "5 · Maryam al bar", "e5",
         info="BARISTA: BUONGIORNO! CHE COSA PRENDE?<br>MARYAM: UN CAPPUCCINO E UN CORNETTO, PER FAVORE.<br>BARISTA: IL CORNETTO VUOTO O ALLA CREMA?<br>"
              "MARYAM: ALLA CREMA. E UN BICCHIERE D'ACQUA.<br>BARISTA: NATURALE O FRIZZANTE?<br>MARYAM: NATURALE, GRAZIE. QUANTO PAGO?<br>BARISTA: 3 EURO E 20."),
  vf(["1. AL BANCO IL CAFFÈ COSTA DI SOLITO MENO CHE AL TAVOLO.", "2. LA MATTINA MOLTI ITALIANI PRENDONO CAPPUCCINO E CORNETTO.",
      "3. «PRENDIAMO UN CAFFÈ?» VUOL DIRE: ANDIAMO A CASA.", "4. LO SCONTRINO SI DÀ AL BARISTA.",
      "5. IL PANZEROTTO È TIPICO DI BARI."], ["VERO", "VERO", "FALSO", "VERO", "VERO"],
     "6 · Vero o falso?", "6 · Vero o falso", "e6"),
  parla("e7", 7, "SEI AL BAR CON UN AMICO. ORDINA DA BERE E DA MANGIARE PER TE E PER IL TUO AMICO, CHIEDI QUANTO PAGHI E SE PUOI PAGARE CON LA CARTA."),
 ]
}


# =====================================================================
# 5. PRENDO IL TRENO (città, A1)
# =====================================================================
TABELLONE = table([["08:15", "LECCE", "3", "IN ORARIO"], ["08:40", "ROMA", "1", "+10'"],
                   ["09:05", "FOGGIA", "5", "IN ORARIO"], ["09:30", "TARANTO", "—", "SOPPRESSO"]],
                  head=["ORA", "PER", "BIN.", "NOTE"])

TRENO_SLIDE = [
    cover("🚆", "PRENDO IL TRENO", "IL BIGLIETTO, IL BINARIO, L'ORARIO", "STAZIONE &bull; A1"),
    slide("CHE COSA IMPARIAMO?", cards([
        ("🎫", "IL BIGLIETTO", "DOVE LO COMPRO? COME LO USO?"), ("🕐", "IL TABELLONE", "PARTENZE, ARRIVI, RITARDI"),
        ("🛤️", "IL BINARIO", "DA DOVE PARTE IL TRENO?"), ("🗣️", "ALLA BIGLIETTERIA", "UN BIGLIETTO PER LECCE…")])),
    slide("🚉 IN STAZIONE", ill("stazione.png", "UNA STAZIONE CON IL TRENO AL BINARIO") + "\n" + cards([
        ("🎫", "LA BIGLIETTERIA", "LO SPORTELLO PER I BIGLIETTI"), ("🤖", "LA BIGLIETTERIA AUTOMATICA", "LA MACCHINETTA"),
        ("📋", "IL TABELLONE", "GLI ORARI DEI TRENI"), ("🛤️", "IL BINARIO", "IL TRENO PARTE DAL BINARIO 3"),
        ("🪑", "LA SALA D'ATTESA", "PER ASPETTARE"), ("ℹ️", "L'UFFICIO INFORMAZIONI", "PER LE DOMANDE")], "g3")),
    slide("🎫 IL BIGLIETTO", ill("convalida.png", "UNA MANO CONVALIDA IL BIGLIETTO NELLA MACCHINETTA VERDE") + "\n" + table([
        ["SOLO ANDATA", "VADO E BASTA: BARI → LECCE"], ["ANDATA E RITORNO", "VADO E TORNO: BARI → LECCE → BARI"],
        ["REGIONALE", "TRENO LENTO, COSTA POCO, CI SONO TANTE FERMATE"], ["FRECCIA / INTERCITY", "TRENO VELOCE, COSTA DI PIÙ, HA IL POSTO"],
        ["ABBONAMENTO", "PER UN MESE: SE PRENDO IL TRENO OGNI GIORNO"]]) + "\n" +
        nota("⚠️ BIGLIETTO DI CARTA SENZA ORARIO? PRIMA DI SALIRE LO DEVI <b>CONVALIDARE</b> NELLA MACCHINETTA VERDE (O GIALLA).<br>"
             "IL <b>CONTROLLORE</b> CONTROLLA. SENZA BIGLIETTO PAGHI LA <b>MULTA</b>.")),
    slide("📋 IL TABELLONE", TABELLONE + "\n" +
        cards([("⏰", "IN ORARIO", "ARRIVA ALL'ORA GIUSTA"), ("🐢", "IN RITARDO (+10')", "ARRIVA 10 MINUTI DOPO"),
               ("❌", "SOPPRESSO", "OGGI NON PARTE"), ("🔀", "CAMBIO BINARIO", "PARTE DA UN ALTRO BINARIO")], "g4")),
    slide("🗣️ ALLA BIGLIETTERIA", dialogo([
        ("SAMIR", "BUONGIORNO. UN BIGLIETTO PER LECCE, PER FAVORE."),
        ("*IMPIEGATA", "SOLO ANDATA O ANDATA E RITORNO?"),
        ("SAMIR", "ANDATA E RITORNO. A CHE ORA PARTE IL PROSSIMO TRENO?"),
        ("*IMPIEGATA", "ALLE 8 E 15, DAL BINARIO 3. È UN REGIONALE."),
        ("SAMIR", "QUANTO COSTA?"),
        ("*IMPIEGATA", "26 EURO. RICORDI DI CONVALIDARE IL BIGLIETTO!"),
        ("SAMIR", "GRAZIE. A CHE ORA ARRIVA A LECCE?"),
        ("*IMPIEGATA", "ALLE 10 E 05.")])),
    slide("🔊 GLI ANNUNCI", cards([
        ("📢", "«IL TRENO REGIONALE PER LECCE È IN PARTENZA DAL BINARIO 3»", "PARTE ADESSO: CORRI!"),
        ("📢", "«IL TRENO VIAGGIA CON 10 MINUTI DI RITARDO»", "ASPETTA 10 MINUTI"),
        ("📢", "«ALLONTANARSI DALLA LINEA GIALLA»", "STAI DIETRO LA LINEA GIALLA: ARRIVA UN TRENO"),
        ("📢", "«IL TRENO PARTIRÀ DAL BINARIO 5 INVECE CHE DAL BINARIO 3»", "CAMBIO BINARIO!")])),
    slide("📱 L'APP E IL SITO", passi([
        "IL BIGLIETTO SI COMPRA ANCHE CON L'<b>APP</b> O SUL <b>SITO</b> DEL TRENO.",
        "SCRIVO LA STAZIONE DI <b>PARTENZA</b> E LA STAZIONE DI <b>ARRIVO</b>.",
        "SCELGO IL <b>GIORNO</b> E L'<b>ORA</b>. PAGO CON LA CARTA.",
        "IL BIGLIETTO È SUL TELEFONO. LO MOSTRO AL CONTROLLORE."]) + "\n" +
        nota("☝️ IL BIGLIETTO REGIONALE COMPRATO CON L'APP DI SOLITO VA <b>ATTIVATO</b> (CHECK-IN) PRIMA DI SALIRE.")),
    end("ORA SAI PRENDERE IL TRENO!"),
]

TRENO = {
 "title": "🚆 Prendo il treno · Esercizi", "store": "treno", "upper": True,
 "sections": [
  {"part": "In stazione"},
  menu(["LA BIGLIETTERIA", "IL TABELLONE", "IL BINARIO", "LA SALA D'ATTESA", "IL CONTROLLORE"],
       [("1. GUARDO GLI ORARI DEI TRENI SUL…", "IL TABELLONE"), ("2. COMPRO IL BIGLIETTO ALLA…", "LA BIGLIETTERIA"),
        ("3. IL TRENO PARTE DAL…", "IL BINARIO"), ("4. SUL TRENO MI CONTROLLA IL BIGLIETTO…", "IL CONTROLLORE"),
        ("5. FA FREDDO: ASPETTO IL TRENO NELLA…", "LA SALA D'ATTESA")],
       "1 · Dove? Chi?", "1 · In stazione", "e1"),
  {"part": "Il tabellone"},
  scegli([("1. A CHE ORA PARTE IL TRENO PER LECCE?", ["ALLE 8:15", "ALLE 8:40", "ALLE 9:05"], "ALLE 8:15"),
          ("2. DA QUALE BINARIO PARTE IL TRENO PER FOGGIA?", ["5", "3", "1"], "5"),
          ("3. QUALE TRENO È IN RITARDO?", ["QUELLO PER ROMA", "QUELLO PER LECCE", "QUELLO PER FOGGIA"], "QUELLO PER ROMA"),
          ("4. DI QUANTI MINUTI?", ["10", "40", "5"], "10"),
          ("5. IL TRENO PER TARANTO…", ["NON PARTE (SOPPRESSO)", "È IN ORARIO", "PARTE DAL BINARIO 1"], "NON PARTE (SOPPRESSO)")],
         "2 · Leggi il tabellone", "2 · Il tabellone", "e2",
         info=TABELLONE),
  {"part": "Il biglietto"},
  menu(["SOLO ANDATA", "ANDATA E RITORNO", "ABBONAMENTO"],
       [("1. LAVORO A MOLFETTA E PRENDO IL TRENO OGNI GIORNO PER UN MESE.", "ABBONAMENTO"),
        ("2. VADO A LECCE DA MIO FRATELLO E LA SERA TORNO A BARI.", "ANDATA E RITORNO"),
        ("3. MI TRASFERISCO A MILANO. NON TORNO.", "SOLO ANDATA"),
        ("4. VADO A FOGGIA PER UN COLLOQUIO E TORNO DOPO.", "ANDATA E RITORNO")],
       "3 · Che biglietto compro?", "3 · Il biglietto", "e3"),
  vf(["1. IL BIGLIETTO DI CARTA SENZA ORARIO VA CONVALIDATO PRIMA DI SALIRE.", "2. IL TRENO REGIONALE È PIÙ VELOCE DEL FRECCIA.",
      "3. SENZA BIGLIETTO PAGO LA MULTA.", "4. «SOPPRESSO» VUOL DIRE CHE IL TRENO OGGI NON PARTE.",
      "5. QUANDO ARRIVA IL TRENO STO DAVANTI ALLA LINEA GIALLA."], ["VERO", "FALSO", "VERO", "VERO", "FALSO"],
     "4 · Vero o falso?", "4 · Vero o falso", "e4"),
  completa("SAMIR: BUONGIORNO. UN ___ PER LECCE, PER FAVORE.<br>IMPIEGATA: SOLO ANDATA O ANDATA E ___?<br>SAMIR: ANDATA E RITORNO. "
           "A CHE ORA ___ IL TRENO?<br>IMPIEGATA: ALLE 8 E 15, DAL ___ 3.<br>SAMIR: QUANTO ___?<br>IMPIEGATA: 26 EURO.",
           ["biglietto", "ritorno", "parte", "binario", "costa"], "5 · Alla biglietteria", "5 · Il dialogo", "e5",
           "BIGLIETTO · RITORNO · PARTE · BINARIO · COSTA"),
  ordina(["APRO L'APP.", "SCRIVO LA STAZIONE DI PARTENZA E DI ARRIVO.", "SCELGO IL GIORNO E L'ORA.", "PAGO CON LA CARTA.", "MOSTRO IL BIGLIETTO AL CONTROLLORE."],
         "6 · Il biglietto con l'app: metti in ordine", "6 · L'app", "e6"),
  parla("e7", 7, "SEI ALLA BIGLIETTERIA DI BARI CENTRALE. CHIEDI UN BIGLIETTO PER UNA CITTÀ, ANDATA E RITORNO. CHIEDI L'ORARIO, IL BINARIO E IL PREZZO."),
 ]
}


# =====================================================================
# 6. ALLA POSTA E IN BANCA (educazione civica, A2)
# =====================================================================
POSTA_SLIDE = [
    cover("🏤", "ALLA POSTA E IN BANCA", "SPEDIRE, PAGARE, APRIRE UN CONTO", "EDUCAZIONE CIVICA &bull; A2"),
    slide("CHE COSA IMPARIAMO?", cards([
        ("✉️", "SPEDIRE", "LETTERA, RACCOMANDATA, PACCO"), ("🧾", "PAGARE", "IL BOLLETTINO, LE BOLLETTE"),
        ("🏦", "IL CONTO", "CONTO CORRENTE, IBAN, CARTA"), ("💳", "IL BANCOMAT", "PRELEVARE, VERSARE, IL PIN")])),
    slide("🏤 ALLA POSTA", ill("ufficio-postale.png", "UN UFFICIO POSTALE CON LE PERSONE IN ATTESA") + "\n" + passi([
        "ENTRO E PRENDO IL <b>NUMERO</b> ALLA MACCHINETTA: SCELGO IL SERVIZIO (SPEDIZIONI, PAGAMENTI, CONTI…).",
        "ASPETTO. GUARDO LO <b>SCHERMO</b>: QUANDO C'È IL MIO NUMERO, VADO ALLO <b>SPORTELLO</b>.",
        "ALLO SPORTELLO DICO CHE COSA VOGLIO FARE."]) + "\n" +
        nota("📱 CON L'APP <b>UFFICIO POSTALE</b> POSSO PRENDERE IL NUMERO ANCHE DA CASA.")),
    slide("✉️ SPEDIRE", cards([
        ("✉️", "LA LETTERA", "CON IL FRANCOBOLLO"), ("📩", "LA RACCOMANDATA", "LA LETTERA IMPORTANTE: HO LA RICEVUTA"),
        ("📮", "LA RACCOMANDATA A/R", "CON RICEVUTA DI RITORNO: SO QUANDO ARRIVA"), ("📦", "IL PACCO", "PER MANDARE OGGETTI")]) + "\n" +
        nota("SULLA BUSTA SCRIVO: IL <b>DESTINATARIO</b> (A CHI MANDO) E IL <b>MITTENTE</b> (IO). NOME, VIA, NUMERO, <b>CAP</b>, CITTÀ.")),
    slide("📬 NON ERO A CASA: L'AVVISO", nota("IL POSTINO PORTA UNA RACCOMANDATA, MA IO NON CI SONO.<br>"
        "LASCIA UN <b>AVVISO DI GIACENZA</b> NELLA CASSETTA DELLA POSTA.<br><br>"
        "VADO ALL'UFFICIO POSTALE SCRITTO SULL'AVVISO CON IL <b>DOCUMENTO</b> E L'AVVISO.<br>"
        "HO <b>30 GIORNI</b> DI TEMPO PER RITIRARLA.<br><br>⚠️ LE RACCOMANDATE SONO SPESSO IMPORTANTI: QUESTURA, TRIBUNALE, MULTE, LAVORO. RITIRALE SEMPRE!", "")),
    slide("🧾 PAGARE ALLA POSTA", cards([
        ("🧾", "IL BOLLETTINO", "UN FOGLIO PER PAGARE: LUCE, GAS, TASSE, SCUOLA"), ("💡", "LE BOLLETTE", "LUCE, GAS, ACQUA, TELEFONO"),
        ("💳", "LA POSTEPAY", "UNA CARTA PREPAGATA: CI METTO I SOLDI E PAGO"), ("🔢", "IL CODICE PAGOPA", "SI PAGA ANCHE IN TABACCHERIA O CON L'APP")])),
    slide("🏦 IL CONTO CORRENTE", '    <div class="twocol2">\n' +
        nota("IL <b>CONTO CORRENTE</b> È IL POSTO DOVE LA BANCA O LA POSTA TIENE I MIEI SOLDI.<br><br>"
             "OGNI CONTO HA UN <b>IBAN</b>: UN CODICE DI 27 LETTERE E NUMERI.<br><br>"
             "IL DATORE DI LAVORO MI MANDA LO <b>STIPENDIO</b> SUL CONTO CON UN <b>BONIFICO</b>.", "") + "\n" +
        cards([("🪪", "UN DOCUMENTO", "PASSAPORTO O CARTA D'IDENTITÀ"), ("🔢", "IL CODICE FISCALE", ""),
               ("📄", "IL PERMESSO DI SOGGIORNO", "O LA RICEVUTA"), ("🏠", "L'INDIRIZZO", "DOVE ABITO")]) + "\n    </div>\n" +
        nota("PER APRIRE UN CONTO SERVONO…", "margin-top:8px; font-size:1rem;")),
    slide("💳 LA CARTA E IL BANCOMAT", ill("bancomat.png", "UN UOMO PRELEVA AL BANCOMAT E COPRE IL PIN") + "\n" + table([
        ["PRELEVARE", "PRENDO I SOLDI DAL BANCOMAT"], ["VERSARE", "METTO I SOLDI SUL CONTO"],
        ["IL SALDO", "QUANTI SOLDI HO SUL CONTO"], ["IL BONIFICO", "MANDO SOLDI A UN ALTRO CONTO"],
        ["IL PIN", "IL CODICE SEGRETO DELLA CARTA"], ["L'ESTRATTO CONTO", "LA LISTA DEI MOVIMENTI"]]) + "\n" +
        nota("🔒 IL PIN NON SI DÀ A NESSUNO. LA BANCA E LA POSTA NON CHIEDONO MAI IL PIN AL TELEFONO O CON UN SMS!")),
    slide("🗣️ ALLO SPORTELLO", dialogo([
        ("*IMPIEGATO", "BUONGIORNO, PREGO."),
        ("BINTA", "BUONGIORNO. DEVO SPEDIRE QUESTA LETTERA CON LA RACCOMANDATA."),
        ("*IMPIEGATO", "CON RICEVUTA DI RITORNO?"),
        ("BINTA", "SÌ, PER FAVORE. E VORREI PAGARE ANCHE QUESTO BOLLETTINO."),
        ("*IMPIEGATO", "VA BENE. IN TUTTO SONO 72 EURO E 40."),
        ("BINTA", "POSSO PAGARE CON LA CARTA?"),
        ("*IMPIEGATO", "CERTO. ECCO LE RICEVUTE: LE CONSERVI!")])),
    end("ORA SAI COME FARE ALLA POSTA E IN BANCA!"),
]

POSTA = {
 "title": "🏤 Alla posta e in banca · Esercizi", "store": "posta-banca", "upper": True,
 "sections": [
  {"part": "Alla posta"},
  ordina(["PRENDO IL NUMERO ALLA MACCHINETTA.", "ASPETTO E GUARDO LO SCHERMO.", "VADO ALLO SPORTELLO.", "DICO CHE COSA VOGLIO FARE.", "PAGO E PRENDO LA RICEVUTA."],
         "1 · Alla posta: metti in ordine", "1 · In ordine", "e1"),
  menu(["LA LETTERA", "LA RACCOMANDATA A/R", "IL PACCO", "IL BOLLETTINO", "LA POSTEPAY"],
       [("1. DEVO MANDARE DEI VESTITI A MIO CUGINO.", "IL PACCO"), ("2. DEVO PAGARE LA BOLLETTA DELLA LUCE.", "IL BOLLETTINO"),
        ("3. MANDO UN DOCUMENTO IMPORTANTE E VOGLIO SAPERE QUANDO ARRIVA.", "LA RACCOMANDATA A/R"),
        ("4. VOGLIO UNA CARTA PER PAGARE ONLINE. CI METTO I SOLDI PRIMA.", "LA POSTEPAY"),
        ("5. SCRIVO AUGURI A UN'AMICA CON IL FRANCOBOLLO.", "LA LETTERA")],
       "2 · Che cosa mi serve?", "2 · Che cosa serve", "e2"),
  scegli([("1. CHE COSA LASCIA IL POSTINO SE NON SONO A CASA?", ["L'AVVISO DI GIACENZA", "IL PACCO DAVANTI ALLA PORTA", "UN SMS"], "L'AVVISO DI GIACENZA"),
          ("2. CHE COSA PORTO ALL'UFFICIO POSTALE?", ["IL DOCUMENTO E L'AVVISO", "SOLO IL CODICE FISCALE", "NIENTE"], "IL DOCUMENTO E L'AVVISO"),
          ("3. QUANTI GIORNI HO PER RITIRARE LA RACCOMANDATA?", ["30", "3", "365"], "30"),
          ("4. LE RACCOMANDATE SONO…", ["SPESSO IMPORTANTI", "SEMPRE PUBBLICITÀ", "SOLO AUGURI"], "SPESSO IMPORTANTI")],
         "3 · L'avviso di giacenza", "3 · L'avviso", "e3"),
  {"part": "In banca"},
  menu(["PRELEVARE", "VERSARE", "IL SALDO", "IL BONIFICO", "IL PIN", "L'IBAN"],
       [("1. PRENDO 50 EURO DAL BANCOMAT.", "PRELEVARE"), ("2. IL CODICE SEGRETO DELLA CARTA.", "IL PIN"),
        ("3. IL CODICE DEL MIO CONTO: 27 LETTERE E NUMERI.", "L'IBAN"), ("4. MANDO 200 EURO SUL CONTO DI MIA SORELLA.", "IL BONIFICO"),
        ("5. VOGLIO SAPERE QUANTI SOLDI HO SUL CONTO.", "IL SALDO"), ("6. METTO 100 EURO SUL MIO CONTO.", "VERSARE")],
       "4 · Le parole della banca", "4 · La banca", "e4"),
  {"id": "e5", "title": "5 · Che cosa serve per aprire un conto?", "short": "5 · Aprire un conto", "type": "multi",
   "cons": "METTI LA SPUNTA VICINO ALLE 4 COSE GIUSTE.",
   "items": ["UN DOCUMENTO", "IL CODICE FISCALE", "LA PATENTE DI GUIDA", "IL PERMESSO DI SOGGIORNO (O LA RICEVUTA)", "L'INDIRIZZO", "LA FOTO DELLA FAMIGLIA"],
   "k": [eq(a) for a in ["X", "X", "-", "X", "X", "-"]]},
  vf(["1. POSSO DARE IL PIN ALLA BANCA SE ME LO CHIEDE CON UN SMS.", "2. LO STIPENDIO ARRIVA SUL CONTO CON UN BONIFICO.",
      "3. LA POSTEPAY È UNA CARTA PREPAGATA.", "4. SULLA BUSTA IL MITTENTE È LA PERSONA CHE RICEVE LA LETTERA.",
      "5. LE RICEVUTE DEI PAGAMENTI SI CONSERVANO."], ["FALSO", "VERO", "VERO", "FALSO", "VERO"],
     "6 · Vero o falso?", "6 · Vero o falso", "e6"),
  completa("IMPIEGATO: BUONGIORNO, PREGO.<br>BINTA: DEVO ___ QUESTA LETTERA CON LA RACCOMANDATA.<br>IMPIEGATO: CON RICEVUTA DI ___?<br>"
           "BINTA: SÌ. E VORREI PAGARE ANCHE QUESTO ___.<br>IMPIEGATO: IN TUTTO SONO 72 EURO.<br>BINTA: POSSO PAGARE CON LA ___?<br>"
           "IMPIEGATO: CERTO. ECCO LE ___.",
           ["spedire", "ritorno", "bollettino", "carta", "ricevute"], "7 · Allo sportello", "7 · Il dialogo", "e7",
           "SPEDIRE · RITORNO · BOLLETTINO · CARTA · RICEVUTE"),
  parla("e8", 8, "SEI ALLO SPORTELLO. DI' CHE VUOI APRIRE UN CONTO, DI' CHE DOCUMENTI HAI E CHIEDI QUANTO COSTA AL MESE E SE C'È LA CARTA."),
 ]
}


# =====================================================================
# 7. IN FARMACIA E AL PRONTO SOCCORSO (salute, A1/A2)
# =====================================================================
FARMACIA_SLIDE = [
    cover("💊", "IN FARMACIA E AL PRONTO SOCCORSO", "LE MEDICINE, LA RICETTA, L'EMERGENZA", "SALUTE &bull; A1/A2"),
    slide("CHE COSA IMPARIAMO?", cards([
        ("💊", "LE MEDICINE", "COMPRESSE, SCIROPPO, POMATA…"), ("📝", "LA RICETTA", "QUANDO SERVE?"),
        ("🕐", "COME SI PRENDONO", "DUE VOLTE AL GIORNO, DOPO I PASTI"), ("🚑", "L'EMERGENZA", "IL 112, IL PRONTO SOCCORSO")])),
    slide("💊 LE MEDICINE", ill("farmacia.png", "LA FARMACISTA AL BANCO") + "\n" + cards([
        ("💊", "LE COMPRESSE", "SI INGOIANO CON L'ACQUA"), ("🧴", "LO SCIROPPO", "PER LA TOSSE"), ("💧", "LE GOCCE", "PER GLI OCCHI, IL NASO, LE ORECCHIE"),
        ("🩹", "LA POMATA / LA CREMA", "SULLA PELLE"), ("🫧", "LA BUSTINA", "SI SCIOGLIE NELL'ACQUA"), ("💉", "LA PUNTURA", "L'INIEZIONE")], "g3")),
    slide("📝 CON O SENZA RICETTA?", '    <div class="twocol2">\n' +
        nota("<b>SENZA RICETTA</b><br>PER UN MAL DI TESTA, UN RAFFREDDORE, UN PO' DI FEBBRE: CHIEDO AL <b>FARMACISTA</b>. MI DÀ UNA MEDICINA SEMPLICE.", "") + "\n" +
        nota("<b>CON LA RICETTA</b><br>PER GLI ANTIBIOTICI E TANTE ALTRE MEDICINE SERVE LA <b>RICETTA DEL MEDICO</b>.<br>"
             "CON LA RICETTA E LA <b>TESSERA SANITARIA</b> LA MEDICINA COSTA POCO.", "") + "\n    </div>\n" +
        nota("🌙 DI NOTTE E LA DOMENICA C'È LA <b>FARMACIA DI TURNO</b>: LA LISTA È SULLA PORTA DI OGNI FARMACIA.")),
    slide("🕐 COME LA PRENDO?", table([
        ["1 VOLTA AL GIORNO", "LA MATTINA"], ["2 VOLTE AL GIORNO", "LA MATTINA E LA SERA"], ["OGNI 8 ORE", "3 VOLTE AL GIORNO"],
        ["PRIMA DEI PASTI", "PRIMA DI MANGIARE"], ["DOPO I PASTI", "DOPO AVER MANGIATO"], ["A STOMACO VUOTO", "SENZA MANGIARE"],
        ["PER 5 GIORNI", "NON SMETTO PRIMA!"]]) + "\n" +
        nota("📄 NELLA SCATOLA C'È IL <b>FOGLIETTO ILLUSTRATIVO</b>. LEGGO ANCHE LA <b>SCADENZA</b>.")),
    slide("🗣️ IN FARMACIA", dialogo([
        ("*FARMACISTA", "BUONASERA. MI DICA."),
        ("ALI", "BUONASERA. HO MAL DI GOLA E UN PO' DI TOSSE."),
        ("*FARMACISTA", "HA LA FEBBRE?"),
        ("ALI", "NO, NON HO LA FEBBRE."),
        ("*FARMACISTA", "ALLORA LE DO QUESTO SCIROPPO. NE PRENDA UN CUCCHIAIO TRE VOLTE AL GIORNO, DOPO I PASTI."),
        ("ALI", "VA BENE. QUANTO COSTA?"),
        ("*FARMACISTA", "8 EURO E 50. SE TRA TRE GIORNI NON STA MEGLIO, VADA DAL MEDICO.")])),
    slide("🚑 L'EMERGENZA: IL 112", '    <div class="twocol2">\n' +
        nota("📞 <b>112</b> È IL NUMERO UNICO PER TUTTE LE EMERGENZE: AMBULANZA, POLIZIA, POMPIERI.<br>È <b>GRATIS</b>, ANCHE SENZA CREDITO.", "") + "\n" +
        passi(["DICO CHE COSA È SUCCESSO.", "DICO DOVE SONO: VIA, NUMERO, CITTÀ.", "RISPONDO ALLE DOMANDE. NON CHIUDO PER PRIMO."]) +
        "\n    </div>\n" + nota("🌙 NON È UN'EMERGENZA MA IL MEDICO È CHIUSO (NOTTE, DOMENICA)? C'È LA <b>GUARDIA MEDICA</b>.")),
    slide("🏥 AL PRONTO SOCCORSO", ill("pronto-soccorso.png", "L'INGRESSO DEL PRONTO SOCCORSO CON L'AMBULANZA") + "\n" + nota("AL PRONTO SOCCORSO <b>NON</b> ENTRA PRIMA CHI ARRIVA PRIMA.<br>"
        "UN INFERMIERE FA IL <b>TRIAGE</b>: CONTROLLA CHI STA PIÙ MALE. CHI STA PIÙ MALE ENTRA PRIMA.", "") + "\n" +
        colori4([("#d63a2f", "ROSSO", "PERICOLO DI VITA: SUBITO"), ("#ef7d00", "ARANCIONE", "MOLTO URGENTE"),
                 ("#1f8fd1", "AZZURRO", "URGENTE, MA SI PUÒ ASPETTARE"), ("#1e9e5a", "VERDE / BIANCO", "POCO URGENTE: SI ASPETTA DI PIÙ")]) + "\n" +
        nota("PORTA SEMPRE: IL <b>DOCUMENTO</b>, LA <b>TESSERA SANITARIA</b> E LA LISTA DELLE MEDICINE CHE PRENDI.")),
    slide("🗣️ AL TELEFONO CON IL 112", dialogo([
        ("*OPERATORE", "112, EMERGENZA. CHE COSA È SUCCESSO?"),
        ("AMINA", "MIO MARITO È CADUTO DALLA SCALA. NON RIESCE A MUOVERE LA GAMBA."),
        ("*OPERATORE", "DOVE SIETE?"),
        ("AMINA", "A BARI, IN VIA CRISANZIO 25, SECONDO PIANO."),
        ("*OPERATORE", "RESPIRA BENE? È SVEGLIO?"),
        ("AMINA", "SÌ, PARLA, MA HA MOLTO DOLORE."),
        ("*OPERATORE", "MANDO L'AMBULANZA. NON LO MUOVA E RESTI AL TELEFONO.")])),
    end("ORA SAI CHE COSA FARE IN FARMACIA E IN EMERGENZA!"),
]

FARMACIA = {
 "title": "💊 In farmacia e al pronto soccorso · Esercizi", "store": "farmacia", "upper": True,
 "sections": [
  {"part": "Le medicine"},
  menu(["LE COMPRESSE", "LO SCIROPPO", "LE GOCCE", "LA POMATA", "LA BUSTINA"],
       [("1. HO LA TOSSE. PRENDO UN CUCCHIAIO DI…", "LO SCIROPPO"), ("2. HO UNA PICCOLA SCOTTATURA SULLA MANO. METTO…", "LA POMATA"),
        ("3. HO GLI OCCHI ROSSI. METTO…", "LE GOCCE"), ("4. LA SCIOLGO IN UN BICCHIERE D'ACQUA:", "LA BUSTINA"),
        ("5. LE INGOIO CON UN PO' D'ACQUA:", "LE COMPRESSE")],
       "1 · Quale medicina?", "1 · Le medicine", "e1"),
  menu(["CON LA RICETTA", "SENZA RICETTA"],
       [("1. UN ANTIBIOTICO", "CON LA RICETTA"), ("2. UNO SCIROPPO PER UN PO' DI TOSSE", "SENZA RICETTA"),
        ("3. UNA COMPRESSA PER IL MAL DI TESTA", "SENZA RICETTA"), ("4. LA MEDICINA PER LA PRESSIONE ALTA, OGNI GIORNO", "CON LA RICETTA")],
       "2 · Con o senza ricetta?", "2 · La ricetta", "e2"),
  scegli([("1. CHE PROBLEMA HA ALI?", ["MAL DI GOLA E TOSSE", "MAL DI PANCIA", "LA FEBBRE ALTA"], "MAL DI GOLA E TOSSE"),
          ("2. CHE COSA GLI DÀ LA FARMACISTA?", ["UNO SCIROPPO", "UNA POMATA", "LE GOCCE"], "UNO SCIROPPO"),
          ("3. QUANTE VOLTE AL GIORNO LO PRENDE?", ["TRE", "UNA", "DUE"], "TRE"),
          ("4. QUANDO LO PRENDE?", ["DOPO I PASTI", "PRIMA DEI PASTI", "DI NOTTE"], "DOPO I PASTI"),
          ("5. SE NON STA MEGLIO TRA TRE GIORNI…", ["VA DAL MEDICO", "CHIAMA IL 112", "PRENDE PIÙ SCIROPPO"], "VA DAL MEDICO")],
         "3 · In farmacia: leggi e rispondi", "3 · In farmacia", "e3",
         info="FARMACISTA: MI DICA.<br>ALI: HO MAL DI GOLA E UN PO' DI TOSSE.<br>FARMACISTA: HA LA FEBBRE?<br>ALI: NO.<br>"
              "FARMACISTA: ALLORA LE DO QUESTO SCIROPPO. NE PRENDA UN CUCCHIAIO TRE VOLTE AL GIORNO, DOPO I PASTI. "
              "SE TRA TRE GIORNI NON STA MEGLIO, VADA DAL MEDICO."),
  scrivi([("1. LA MATTINA E LA SERA = 2 ___ AL GIORNO", ["volte"]), ("2. PRIMA DI MANGIARE = PRIMA DEI ___", ["pasti"]),
          ("3. IL FOGLIO NELLA SCATOLA = IL FOGLIETTO ___", ["illustrativo"]), ("4. DI NOTTE APRE LA FARMACIA DI ___", ["turno"]),
          ("5. IL GIORNO DOPO IL QUALE LA MEDICINA NON VA BENE = LA ___", ["scadenza"])],
         "4 · Scrivi la parola", "4 · Le parole", "e4", bank="VOLTE · PASTI · ILLUSTRATIVO · TURNO · SCADENZA"),
  {"part": "L'emergenza"},
  vf(["1. IL 112 È IL NUMERO PER TUTTE LE EMERGENZE.", "2. PER CHIAMARE IL 112 SERVE IL CREDITO.",
      "3. AL PRONTO SOCCORSO ENTRA PRIMA CHI ARRIVA PRIMA.", "4. IL CODICE ROSSO È IL PIÙ URGENTE.",
      "5. DI NOTTE, SE NON È UN'EMERGENZA, POSSO CHIAMARE LA GUARDIA MEDICA."], ["VERO", "FALSO", "FALSO", "VERO", "VERO"],
     "5 · Vero o falso?", "5 · Vero o falso", "e5"),
  ordina(["CHIAMO IL 112.", "DICO CHE COSA È SUCCESSO.", "DICO L'INDIRIZZO: VIA, NUMERO, CITTÀ.", "RISPONDO ALLE DOMANDE.", "ASPETTO L'AMBULANZA."],
         "6 · Che cosa faccio? Metti in ordine", "6 · In ordine", "e6"),
  parla("e7", 7, "CHIAMA IL 112: DI' CHE UN AMICO STA MALE (CHE COSA HA), DI' L'INDIRIZZO E RISPONDI: È SVEGLIO, RESPIRA."),
 ]
}


# =====================================================================
# 8. AL COMUNE E IN QUESTURA (educazione civica, A2)
# =====================================================================
COMUNE_SLIDE = [
    cover("🏛️", "AL COMUNE E IN QUESTURA", "LA RESIDENZA, LA CARTA D'IDENTITÀ, IL PERMESSO DI SOGGIORNO", "EDUCAZIONE CIVICA &bull; A2"),
    slide("CHE COSA IMPARIAMO?", cards([
        ("🏠", "LA RESIDENZA", "DOVE ABITO, PER LO STATO"), ("🪪", "LA CARTA D'IDENTITÀ", "LA CIE"),
        ("📄", "I CERTIFICATI", "DI RESIDENZA, STATO DI FAMIGLIA"), ("🛂", "IL PERMESSO DI SOGGIORNO", "IL RINNOVO IN QUESTURA")])),
    slide("🏛️ IL COMUNE: L'ANAGRAFE", ill("anagrafe.png", "LO SPORTELLO DELL'ANAGRAFE") + "\n" + '    <div class="twocol2">\n' +
        nota("L'<b>ANAGRAFE</b> È L'UFFICIO DEL COMUNE CON I DATI DI TUTTE LE PERSONE CHE ABITANO IN CITTÀ.<br><br>"
             "A BARI CI SONO TANTI UFFICI NEI <b>MUNICIPI</b>. DI SOLITO SERVE L'<b>APPUNTAMENTO</b> (ONLINE O AL TELEFONO).", "") + "\n" +
        cards([("🏠", "LA RESIDENZA", ""), ("🪪", "LA CARTA D'IDENTITÀ", ""), ("📄", "I CERTIFICATI", ""), ("👶", "LE NASCITE E I MATRIMONI", "")]) +
        "\n    </div>"),
    slide("🏠 LA RESIDENZA", passi([
        "ABITO IN UNA CASA A BARI: FACCIO LA <b>DICHIARAZIONE DI RESIDENZA</b> AL COMUNE (ENTRO 20 GIORNI).",
        "PORTO: <b>DOCUMENTO</b>, <b>CODICE FISCALE</b>, <b>PERMESSO DI SOGGIORNO</b>, IL <b>CONTRATTO D'AFFITTO</b> (O IL PERMESSO DEL PROPRIETARIO).",
        "DOPO QUALCHE GIORNO VIENE UN <b>VIGILE</b> A CASA: CONTROLLA CHE ABITO LÌ. IL MIO NOME DEVE ESSERE SUL CAMPANELLO!",
        "ORA HO LA RESIDENZA. POSSO CHIEDERE LA CARTA D'IDENTITÀ."]) + "\n" +
        nota("LA RESIDENZA SERVE PER: IL MEDICO DI BASE, LA SCUOLA DEI FIGLI, I BONUS, LA CITTADINANZA.")),
    slide("🪪 LA CARTA D'IDENTITÀ (CIE)", cards([
        ("📅", "L'APPUNTAMENTO", "CON IL COMUNE"), ("📸", "UNA FOTO", "RECENTE, A COLORI"),
        ("🛂", "IL DOCUMENTO", "PASSAPORTO E PERMESSO DI SOGGIORNO"), ("💶", "IL COSTO", "CIRCA 22 EURO")]) + "\n" +
        nota("☝️ PER I CITTADINI STRANIERI LA CARTA D'IDENTITÀ <b>NON</b> SERVE PER ANDARE ALL'ESTERO. SERVE IL PASSAPORTO.")),
    slide("📄 I CERTIFICATI", table([
        ["CERTIFICATO DI RESIDENZA", "DICE DOVE ABITO"], ["STATO DI FAMIGLIA", "DICE CHI ABITA CON ME"],
        ["CERTIFICATO DI NASCITA", "PER UN FIGLIO NATO IN ITALIA"]]) + "\n" +
        nota("💻 MOLTI CERTIFICATI SI SCARICANO ONLINE DALL'<b>ANPR</b>, CON LA CIE O LO SPID. SONO GRATIS.")),
    slide("🛂 IN QUESTURA: IL PERMESSO DI SOGGIORNO", ill("questura.png", "LO SPORTELLO DELLA QUESTURA E LE IMPRONTE DIGITALI") + "\n" + '    <div class="twocol2">\n' +
        nota("LA <b>QUESTURA</b> È L'UFFICIO DELLA <b>POLIZIA</b> CHE DÀ E RINNOVA IL <b>PERMESSO DI SOGGIORNO</b>.<br><br>"
             "LA PARTE DELLA QUESTURA PER GLI STRANIERI SI CHIAMA <b>UFFICIO IMMIGRAZIONE</b>.", "") + "\n" +
        cards([("📅", "LA SCADENZA", "GUARDO SEMPRE LA DATA SUL PERMESSO"), ("⏳", "PRIMA DELLA SCADENZA", "CHIEDO IL RINNOVO IN TEMPO (MEGLIO 60 GIORNI PRIMA)"),
               ("🧾", "LA RICEVUTA", "LA CONSERVO: MENTRE ASPETTO, VALE COME IL PERMESSO"), ("☝️", "LE IMPRONTE", "IN QUESTURA LASCIO LE IMPRONTE DIGITALI")]) +
        "\n    </div>"),
    slide("📮 IL RINNOVO: COME SI FA?", passi([
        "PER MOLTI PERMESSI (LAVORO, FAMIGLIA) PRENDO IL <b>KIT</b> ALLA POSTA: UNA BUSTA CON I MODULI.",
        "COMPILO I MODULI (CON L'AIUTO DI UN PATRONATO O DEGLI OPERATORI) E LI SPEDISCO DALLO <b>SPORTELLO AMICO</b> DELLA POSTA.",
        "PAGO: UNA <b>MARCA DA BOLLO</b>, IL SERVIZIO DELLA POSTA E UN <b>CONTRIBUTO</b>. PRENDO LA <b>RICEVUTA</b>.",
        "ARRIVA L'<b>APPUNTAMENTO</b> IN QUESTURA (SULLA RICEVUTA O CON UN SMS): VADO CON LE FOTO E I DOCUMENTI.",
        "QUANDO IL PERMESSO È PRONTO, LO VADO A RITIRARE."]) + "\n" +
        nota("☝️ PER ALTRI PERMESSI (ES. ASILO, PROTEZIONE) SI VA <b>DIRETTAMENTE IN QUESTURA</b>. CHIEDI SEMPRE AGLI OPERATORI DEL SAI.")),
    slide("🗣️ ALL'ANAGRAFE", dialogo([
        ("*IMPIEGATA", "BUONGIORNO. HA L'APPUNTAMENTO?"),
        ("KOFI", "SÌ, ALLE 10. VORREI FARE LA RESIDENZA."),
        ("*IMPIEGATA", "MI DÀ IL PASSAPORTO, IL PERMESSO DI SOGGIORNO E IL CODICE FISCALE?"),
        ("KOFI", "ECCO. HO ANCHE IL CONTRATTO D'AFFITTO."),
        ("*IMPIEGATA", "PERFETTO. NEI PROSSIMI GIORNI PASSA UN VIGILE A CONTROLLARE. METTA IL SUO NOME SUL CAMPANELLO."),
        ("KOFI", "VA BENE. POI POSSO FARE LA CARTA D'IDENTITÀ?"),
        ("*IMPIEGATA", "SÌ, QUANDO LA RESIDENZA È CONFERMATA.")])),
    end("ORA SAI CHE COSA FARE AL COMUNE E IN QUESTURA!"),
]

COMUNE = {
 "title": "🏛️ Al comune e in questura · Esercizi", "store": "comune-questura", "upper": True,
 "sections": [
  {"part": "Dove vado?"},
  menu(["AL COMUNE (ANAGRAFE)", "IN QUESTURA", "ALLA POSTA"],
       [("1. VOGLIO FARE LA CARTA D'IDENTITÀ.", "AL COMUNE (ANAGRAFE)"), ("2. DEVO LASCIARE LE IMPRONTE PER IL PERMESSO DI SOGGIORNO.", "IN QUESTURA"),
        ("3. PRENDO IL KIT PER IL RINNOVO DEL PERMESSO.", "ALLA POSTA"), ("4. HO CAMBIATO CASA: FACCIO LA RESIDENZA.", "AL COMUNE (ANAGRAFE)"),
        ("5. MI SERVE IL CERTIFICATO DI STATO DI FAMIGLIA.", "AL COMUNE (ANAGRAFE)"), ("6. RITIRO IL PERMESSO DI SOGGIORNO NUOVO.", "IN QUESTURA")],
       "1 · Dove vado?", "1 · Dove vado", "e1"),
  {"part": "La residenza"},
  ordina(["PRENDO L'APPUNTAMENTO AL COMUNE.", "VADO ALL'ANAGRAFE CON I DOCUMENTI E IL CONTRATTO.", "METTO IL MIO NOME SUL CAMPANELLO.",
          "UN VIGILE VIENE A CASA A CONTROLLARE.", "HO LA RESIDENZA E CHIEDO LA CARTA D'IDENTITÀ."],
         "2 · La residenza: metti in ordine", "2 · In ordine", "e2"),
  {"id": "e3", "title": "3 · Che cosa porto per la residenza?", "short": "3 · I documenti", "type": "multi",
   "cons": "METTI LA SPUNTA VICINO ALLE 4 COSE GIUSTE.",
   "items": ["IL PASSAPORTO", "IL CODICE FISCALE", "LA PAGELLA DELLA SCUOLA", "IL PERMESSO DI SOGGIORNO", "IL CONTRATTO D'AFFITTO", "LA BOLLETTA DEL TELEFONO"],
   "k": [eq(a) for a in ["X", "X", "-", "X", "X", "-"]]},
  scegli([("1. CHE COSA VUOLE FARE KOFI?", ["LA RESIDENZA", "IL PASSAPORTO", "IL CODICE FISCALE"], "LA RESIDENZA"),
          ("2. A CHE ORA HA L'APPUNTAMENTO?", ["ALLE 10", "ALLE 12", "NON HA L'APPUNTAMENTO"], "ALLE 10"),
          ("3. CHI PASSA A CONTROLLARE?", ["UN VIGILE", "IL PROPRIETARIO", "UN INFERMIERE"], "UN VIGILE"),
          ("4. CHE COSA DEVE METTERE SUL CAMPANELLO?", ["IL SUO NOME", "IL NUMERO DI TELEFONO", "UNA FOTO"], "IL SUO NOME"),
          ("5. QUANDO PUÒ FARE LA CARTA D'IDENTITÀ?", ["QUANDO LA RESIDENZA È CONFERMATA", "SUBITO", "TRA UN ANNO"], "QUANDO LA RESIDENZA È CONFERMATA")],
         "4 · All'anagrafe: leggi e rispondi", "4 · All'anagrafe", "e4",
         info="IMPIEGATA: HA L'APPUNTAMENTO?<br>KOFI: SÌ, ALLE 10. VORREI FARE LA RESIDENZA.<br>IMPIEGATA: MI DÀ IL PASSAPORTO, IL PERMESSO DI SOGGIORNO E IL CODICE FISCALE?<br>"
              "KOFI: ECCO. HO ANCHE IL CONTRATTO D'AFFITTO.<br>IMPIEGATA: PERFETTO. NEI PROSSIMI GIORNI PASSA UN VIGILE A CONTROLLARE. METTA IL SUO NOME SUL CAMPANELLO.<br>"
              "KOFI: POI POSSO FARE LA CARTA D'IDENTITÀ?<br>IMPIEGATA: SÌ, QUANDO LA RESIDENZA È CONFERMATA."),
  {"part": "Il permesso di soggiorno"},
  completa("IL PERMESSO DI SOGGIORNO HA UNA ___: LA GUARDO SEMPRE.<br>CHIEDO IL RINNOVO PRIMA DELLA SCADENZA, MEGLIO 60 ___ PRIMA.<br>"
           "PER MOLTI PERMESSI PRENDO IL ___ ALLA POSTA.<br>DOPO LA SPEDIZIONE HO LA ___: LA CONSERVO BENE.<br>"
           "IN QUESTURA LASCIO LE ___ DIGITALI.",
           ["scadenza", "giorni", "kit", "ricevuta", "impronte"], "5 · Completa", "5 · Il rinnovo", "e5",
           "SCADENZA · GIORNI · KIT · RICEVUTA · IMPRONTE"),
  vf(["1. LA QUESTURA È UN UFFICIO DELLA POLIZIA.", "2. LA CARTA D'IDENTITÀ DI UN CITTADINO STRANIERO SERVE PER VIAGGIARE ALL'ESTERO.",
      "3. MOLTI CERTIFICATI SI SCARICANO ONLINE DALL'ANPR.", "4. PER IL PERMESSO PER ASILO SI VA DIRETTAMENTE IN QUESTURA.",
      "5. LA RESIDENZA SERVE ANCHE PER AVERE IL MEDICO DI BASE."], ["VERO", "FALSO", "VERO", "VERO", "VERO"],
     "6 · Vero o falso?", "6 · Vero o falso", "e6"),
  parla("e7", 7, "SEI ALL'ANAGRAFE. SALUTA, DI' CHE HAI L'APPUNTAMENTO, CHE COSA VUOI FARE E QUALI DOCUMENTI HAI."),
 ]
}


# =====================================================================
# 9. LAVORO COME ASSISTENTE FAMILIARE (lavoro, A2)
# =====================================================================
ASSISTENTE_SLIDE = [
    cover("🤲", "L'ASSISTENTE FAMILIARE", "AIUTARE UNA PERSONA ANZIANA: IL LAVORO, LE PAROLE, LE DOMANDE", "LAVORO &bull; A2"),
    slide("CHE COSA IMPARIAMO?", cards([
        ("🧓", "IL LAVORO", "CHE COSA FA UN'ASSISTENTE FAMILIARE?"), ("📅", "LA GIORNATA", "DALLA MATTINA ALLA SERA"),
        ("🩺", "LA SALUTE", "LE DOMANDE GENTILI"), ("📝", "IL CONTRATTO", "CONVIVENTE O A ORE")])),
    slide("🤲 CHI È L'ASSISTENTE FAMILIARE?", ill("assistente-anziana.png", "UN'ASSISTENTE FAMILIARE AIUTA UNA SIGNORA ANZIANA A CAMMINARE") + "\n" + nota("L'<b>ASSISTENTE FAMILIARE</b> (SI DICE ANCHE <b>BADANTE</b>) AIUTA UNA PERSONA "
        "ANZIANA, MALATA O CON UNA DISABILITÀ, A CASA SUA.<br>LA <b>COLF</b> INVECE PULISCE E TIENE IN ORDINE LA CASA.", "") + "\n" +
        cards([("😊", "GENTILE E PAZIENTE", ""), ("⏰", "PUNTUALE", ""), ("🤝", "AFFIDABILE", "LA FAMIGLIA SI FIDA"),
               ("👀", "ATTENTA", "VEDE SE QUALCOSA NON VA"), ("💪", "IN FORMA", "AIUTA A ALZARSI, A CAMMINARE"), ("🤫", "RISERVATA", "NON RACCONTA I FATTI DELLA FAMIGLIA")], "g3")),
    slide("📅 LA GIORNATA DELLA SIGNORA ROSA", table([
        ["8:00", "LA SVEGLIO E LA AIUTO AD ALZARSI"], ["8:15", "LA AIUTO A LAVARSI E A VESTIRSI"],
        ["8:45", "PREPARO LA COLAZIONE. LE DO LE MEDICINE"], ["10:00", "FACCIAMO UNA PASSEGGIATA. FACCIO LA SPESA"],
        ["12:30", "CUCINO IL PRANZO. MANGIAMO INSIEME"], ["15:00", "RIPOSA. IO METTO IN ORDINE LA CASA"],
        ["17:00", "LA ACCOMPAGNO DAL MEDICO"], ["20:00", "CENA, POI LA AIUTO AD ANDARE A LETTO"]], head=["ORA", "CHE COSA FACCIO?"])),
    slide("💊 LE MEDICINE: ATTENZIONE!", ill("portapillole.png", "UN PORTAPILLOLE DELLA SETTIMANA E UN QUADERNO") + "\n" + passi([
        "LE MEDICINE LE DECIDE <b>IL MEDICO</b>. IO NON CAMBIO NIENTE.",
        "SCRIVO IN UN <b>QUADERNO</b>: CHE MEDICINA, A CHE ORA, QUANTE.",
        "USO IL <b>PORTAPILLOLE</b> DELLA SETTIMANA: LUNEDÌ, MARTEDÌ…",
        "SE LA SIGNORA STA MALE O CADE, CHIAMO LA <b>FAMIGLIA</b>, IL <b>MEDICO</b> O IL <b>112</b>."])),
    slide("🩺 LE DOMANDE GENTILI (CON IL LEI)", table([
        ["COME SI SENTE OGGI?", "STO BENE / NON MOLTO BENE"], ["HA DORMITO BENE?", "SÌ / NO, MI SONO SVEGLIATA SPESSO"],
        ["LE FA MALE QUALCOSA?", "SÌ, MI FA MALE LA SCHIENA"], ["HA PRESO LA PASTIGLIA?", "SÌ, DOPO COLAZIONE"],
        ["HA FAME? HA SETE?", "UN PO' D'ACQUA, GRAZIE"], ["VUOLE USCIRE UN PO'?", "SÌ, ANDIAMO AL PARCO"]], head=["CHIEDO", "LA SIGNORA RISPONDE"]) + "\n" +
        nota("☝️ CON LE PERSONE ANZIANE SI USA IL <b>LEI</b>: «COME <b>SI</b> SENTE?», NON «COME TI SENTI?»")),
    slide("🗣️ UNA MATTINA", dialogo([
        ("FATOU", "BUONGIORNO, SIGNORA ROSA! HA DORMITO BENE?"),
        ("*ROSA", "COSÌ COSÌ. MI FA UN PO' MALE IL GINOCCHIO."),
        ("FATOU", "MI DISPIACE. VUOLE UN CUSCINO SOTTO LA GAMBA?"),
        ("*ROSA", "SÌ, GRAZIE. CHE ORE SONO?"),
        ("FATOU", "SONO LE OTTO. ADESSO LA AIUTO AD ALZARSI, PIANO PIANO."),
        ("*ROSA", "HO PRESO LE MEDICINE?"),
        ("FATOU", "NON ANCORA: LE PRENDE DOPO COLAZIONE. LO SCRIVO NEL QUADERNO.")])),
    slide("📝 IL CONTRATTO", cards([
        ("🏠", "CONVIVENTE", "ABITO NELLA CASA DELLA PERSONA. HO UNA STANZA MIA"), ("⏰", "NON CONVIVENTE / A ORE", "VADO SOLO ALCUNE ORE AL GIORNO"),
        ("📄", "IL CONTRATTO DI LAVORO DOMESTICO", "LO FA LA FAMIGLIA. È OBBLIGATORIO"), ("🛌", "IL RIPOSO", "OGNI SETTIMANA HO IL GIORNO LIBERO"),
        ("🏖️", "LE FERIE", "OGNI ANNO HO LE FERIE PAGATE"), ("💶", "LA BUSTA PAGA", "OGNI MESE. CON I CONTRIBUTI INPS")], "g3") + "\n" +
        nota("🔎 PER INFORMAZIONI: UN <b>PATRONATO</b> O UN <b>SINDACATO</b>. È GRATIS.")),
    end("ORA CONOSCI IL LAVORO DI ASSISTENTE FAMILIARE!"),
]

ASSISTENTE = {
 "title": "🤲 L'assistente familiare · Esercizi", "store": "assistente-familiare", "upper": True,
 "sections": [
  {"part": "Il lavoro"},
  menu(["ASSISTENTE FAMILIARE", "COLF"],
       [("1. AIUTA LA SIGNORA A VESTIRSI.", "ASSISTENTE FAMILIARE"), ("2. PULISCE I PAVIMENTI E STIRA.", "COLF"),
        ("3. ACCOMPAGNA IL SIGNORE DAL MEDICO.", "ASSISTENTE FAMILIARE"), ("4. DÀ LE MEDICINE ALL'ORA GIUSTA.", "ASSISTENTE FAMILIARE"),
        ("5. LAVA I VETRI DELLE FINESTRE.", "COLF")],
       "1 · Chi lo fa?", "1 · Chi lo fa", "e1"),
  menu(["PAZIENTE", "PUNTUALE", "AFFIDABILE", "ATTENTA", "RISERVATA"],
       [("1. ARRIVA SEMPRE ALL'ORA GIUSTA. È…", "PUNTUALE"), ("2. NON RACCONTA A NESSUNO I FATTI DELLA FAMIGLIA. È…", "RISERVATA"),
        ("3. LA SIGNORA È LENTA, MA LEI ASPETTA E SORRIDE. È…", "PAZIENTE"), ("4. VEDE SUBITO CHE IL SIGNORE HA LA FEBBRE. È…", "ATTENTA"),
        ("5. LA FAMIGLIA SI FIDA DI LEI. È…", "AFFIDABILE")],
       "2 · Com'è?", "2 · Le qualità", "e2"),
  {"part": "La giornata"},
  ordina(["SVEGLIO LA SIGNORA E LA AIUTO AD ALZARSI.", "LA AIUTO A LAVARSI E A VESTIRSI.", "PREPARO LA COLAZIONE E LE DO LE MEDICINE.",
          "FACCIAMO UNA PASSEGGIATA.", "CUCINO IL PRANZO.", "LA AIUTO AD ANDARE A LETTO."],
         "3 · La giornata: metti in ordine", "3 · In ordine", "e3"),
  {"part": "Le domande gentili"},
  menu(["COME SI SENTE?", "HA DORMITO BENE?", "LE FA MALE QUALCOSA?", "HA PRESO LA PASTIGLIA?", "HA SETE?"],
       [("1. «SÌ, MI FA MALE LA SCHIENA.»", "LE FA MALE QUALCOSA?"), ("2. «NO, MI SONO SVEGLIATA TRE VOLTE.»", "HA DORMITO BENE?"),
        ("3. «SÌ, UN BICCHIERE D'ACQUA, GRAZIE.»", "HA SETE?"), ("4. «OGGI STO MEGLIO, GRAZIE.»", "COME SI SENTE?"),
        ("5. «SÌ, DOPO COLAZIONE.»", "HA PRESO LA PASTIGLIA?")],
       "4 · Qual è la domanda?", "4 · Le domande", "e4"),
  scrivi([("1. COME TI SENTI? → COME ___ SENTE?", ["si"]), ("2. HAI DORMITO BENE? → ___ DORMITO BENE?", ["ha"]),
          ("3. TI FA MALE? → ___ FA MALE?", ["le"]), ("4. VUOI USCIRE? → ___ USCIRE?", ["vuole"])],
         "5 · Dal tu al Lei", "5 · Il Lei", "e5", cons="CON LA SIGNORA ROSA USO IL LEI. SCRIVI LA PAROLA GIUSTA.", bank="HA · LE · SI · VUOLE"),
  {"part": "Il contratto"},
  vf(["1. L'ASSISTENTE CONVIVENTE ABITA NELLA CASA DELLA PERSONA.", "2. IL CONTRATTO DI LAVORO DOMESTICO NON È OBBLIGATORIO.",
      "3. OGNI SETTIMANA C'È UN GIORNO DI RIPOSO.", "4. L'ASSISTENTE PUÒ CAMBIARE LE MEDICINE DA SOLA.",
      "5. IL PATRONATO DÀ INFORMAZIONI GRATIS."], ["VERO", "FALSO", "VERO", "FALSO", "VERO"],
     "6 · Vero o falso?", "6 · Vero o falso", "e6"),
  parla("e7", 7, "È MATTINA. SALUTA LA SIGNORA ROSA, CHIEDI COME HA DORMITO E SE LE FA MALE QUALCOSA, POI DILLE CHE COSA FATE OGGI."),
 ]
}


# =====================================================================
# 10. IN AEREO E ALL'AGENZIA DI VIAGGI (città, A2)
# =====================================================================
AEREO_SLIDE = [
    cover("✈️", "IN AEREO E ALL'AGENZIA DI VIAGGI", "PRENOTARE UN VOLO, IL CHECK-IN, IL BAGAGLIO", "VIAGGI &bull; A2"),
    slide("CHE COSA IMPARIAMO?", cards([
        ("🧳", "ALL'AGENZIA DI VIAGGI", "CHIEDERE E PRENOTARE"), ("🛫", "IN AEROPORTO", "CHECK-IN, CONTROLLI, IMBARCO"),
        ("🎒", "IL BAGAGLIO", "A MANO O DA STIVA"), ("🗣️", "LE FRASI", "VORREI UN VOLO PER…")])),
    slide("🧳 ALL'AGENZIA DI VIAGGI", ill("agenzia-viaggi.png", "UN'IMPIEGATA DELL'AGENZIA MOSTRA UN VOLO A UNA COPPIA") + "\n" + dialogo([
        ("*IMPIEGATA", "BUONGIORNO. COME POSSO AIUTARLA?"),
        ("MOUSSA", "VORREI UN VOLO PER DAKAR, PER IL 20 DICEMBRE."),
        ("*IMPIEGATA", "SOLO ANDATA O ANDATA E RITORNO?"),
        ("MOUSSA", "ANDATA E RITORNO. TORNO IL 10 GENNAIO."),
        ("*IMPIEGATA", "C'È UN VOLO DA BARI CON SCALO A ROMA. COSTA 520 EURO, CON UN BAGAGLIO DA 23 CHILI."),
        ("MOUSSA", "C'È QUALCOSA DI MENO CARO?"),
        ("*IMPIEGATA", "SE PARTE IL 18, COSTA 460 EURO.")])),
    slide("📖 LE PAROLE DEL VOLO", table([
        ["IL VOLO DIRETTO", "SENZA FERMATE"], ["LO SCALO", "UNA FERMATA IN UN ALTRO AEROPORTO: CAMBIO AEREO"],
        ["LA PRENOTAZIONE", "IL POSTO È MIO: HO IL CODICE"], ["LA CARTA D'IMBARCO", "IL BIGLIETTO PER SALIRE SULL'AEREO"],
        ["IL GATE (L'USCITA)", "LA PORTA PER ANDARE ALL'AEREO"], ["IN ORARIO / IN RITARDO / CANCELLATO", "COME PER IL TRENO"]])),
    slide("🛫 IN AEROPORTO", ill("aeroporto.png", "VIAGGIATORI AL BANCO DEL CHECK-IN") + "\n" + passi([
        "ARRIVO IN AEROPORTO <b>2 ORE PRIMA</b> (3 ORE PER I VOLI LONTANI).",
        "FACCIO IL <b>CHECK-IN</b> (ANCHE ONLINE) E LASCIO LA VALIGIA AL BANCO: È IL <b>BAGAGLIO DA STIVA</b>.",
        "PASSO I <b>CONTROLLI DI SICUREZZA</b>: METTO BORSA, GIACCA E TELEFONO NELLA VASCHETTA.",
        "PER I VOLI FUORI DALL'EUROPA C'È IL <b>CONTROLLO PASSAPORTI</b>.",
        "VADO AL <b>GATE</b> E ASPETTO L'<b>IMBARCO</b>."])),
    slide("🎒 IL BAGAGLIO", cards([
        ("🎒", "IL BAGAGLIO A MANO", "PICCOLO, VIENE CON ME SULL'AEREO"), ("🧳", "IL BAGAGLIO DA STIVA", "GRANDE, VA SOTTO L'AEREO"),
        ("💧", "I LIQUIDI", "NEL BAGAGLIO A MANO: MASSIMO 100 ML PER BOTTIGLIETTA"), ("🚫", "VIETATO", "COLTELLI, FORBICI GRANDI, BOMBOLETTE")]) + "\n" +
        nota("⚠️ VIAGGI FUORI DALL'ITALIA? PORTA IL <b>PASSAPORTO</b> E IL <b>PERMESSO DI SOGGIORNO</b> VALIDO. CONTROLLA SE SERVE IL <b>VISTO</b>.")),
    slide("🔊 GLI ANNUNCI IN AEROPORTO", cards([
        ("📢", "«IMBARCO IMMEDIATO AL GATE 5»", "VAI SUBITO AL GATE 5"), ("📢", "«ULTIMA CHIAMATA PER IL VOLO PER ROMA»", "CORRI: L'AEREO CHIUDE"),
        ("📢", "«IL VOLO È IN RITARDO DI 40 MINUTI»", "ASPETTA"), ("📢", "«IL VOLO È STATO CANCELLATO»", "VAI AL BANCO DELLA COMPAGNIA")])),
    end("ORA SAI PRENOTARE E PRENDERE L'AEREO!"),
]

AEREO = {
 "title": "✈️ In aereo e all'agenzia di viaggi · Esercizi", "store": "aereo-viaggi", "upper": True,
 "sections": [
  {"part": "All'agenzia"},
  scegli([("1. DOVE VUOLE ANDARE MOUSSA?", ["A DAKAR", "A ROMA", "A PARIGI"], "A DAKAR"),
          ("2. QUANDO TORNA?", ["IL 10 GENNAIO", "IL 20 DICEMBRE", "IL 18 DICEMBRE"], "IL 10 GENNAIO"),
          ("3. IL VOLO È…", ["CON SCALO A ROMA", "DIRETTO", "CON SCALO A MILANO"], "CON SCALO A ROMA"),
          ("4. QUANTO COSTA SE PARTE IL 18?", ["460 EURO", "520 EURO", "23 EURO"], "460 EURO")],
         "1 · All'agenzia: leggi e rispondi", "1 · All'agenzia", "e1",
         info="IMPIEGATA: COME POSSO AIUTARLA?<br>MOUSSA: VORREI UN VOLO PER DAKAR, PER IL 20 DICEMBRE, ANDATA E RITORNO. TORNO IL 10 GENNAIO.<br>"
              "IMPIEGATA: C'È UN VOLO DA BARI CON SCALO A ROMA. COSTA 520 EURO, CON UN BAGAGLIO DA 23 CHILI.<br>MOUSSA: C'È QUALCOSA DI MENO CARO?<br>"
              "IMPIEGATA: SE PARTE IL 18, COSTA 460 EURO."),
  menu(["IL VOLO DIRETTO", "LO SCALO", "LA CARTA D'IMBARCO", "IL GATE", "LA PRENOTAZIONE"],
       [("1. LA PORTA PER ANDARE ALL'AEREO.", "IL GATE"), ("2. UN VOLO SENZA FERMATE.", "IL VOLO DIRETTO"),
        ("3. IL BIGLIETTO PER SALIRE SULL'AEREO.", "LA CARTA D'IMBARCO"), ("4. UNA FERMATA IN UN ALTRO AEROPORTO.", "LO SCALO"),
        ("5. IL POSTO È MIO, HO UN CODICE.", "LA PRENOTAZIONE")],
       "2 · Le parole del volo", "2 · Le parole", "e2"),
  {"part": "In aeroporto"},
  ordina(["ARRIVO IN AEROPORTO DUE ORE PRIMA.", "FACCIO IL CHECK-IN E LASCIO LA VALIGIA.", "PASSO I CONTROLLI DI SICUREZZA.",
          "VADO AL GATE.", "SALGO SULL'AEREO."], "3 · In aeroporto: metti in ordine", "3 · In ordine", "e3"),
  menu(["BAGAGLIO A MANO", "BAGAGLIO DA STIVA", "VIETATO"],
       [("1. UNO ZAINO PICCOLO CON IL TELEFONO E IL PASSAPORTO", "BAGAGLIO A MANO"), ("2. UNA VALIGIA GRANDE DA 23 CHILI", "BAGAGLIO DA STIVA"),
        ("3. UN COLTELLO DA CUCINA NELLO ZAINO", "VIETATO"), ("4. UNA BOTTIGLIETTA DI CREMA DA 50 ML", "BAGAGLIO A MANO"),
        ("5. UNA BOTTIGLIA D'ACQUA DA UN LITRO AI CONTROLLI", "VIETATO")],
       "4 · Dove va? Si può?", "4 · Il bagaglio", "e4"),
  menu(["VADO SUBITO AL GATE", "ASPETTO", "VADO AL BANCO DELLA COMPAGNIA"],
       [("1. «ULTIMA CHIAMATA PER IL VOLO PER TUNISI»", "VADO SUBITO AL GATE"), ("2. «IL VOLO PER MILANO È IN RITARDO DI UN'ORA»", "ASPETTO"),
        ("3. «IL VOLO PER ROMA È STATO CANCELLATO»", "VADO AL BANCO DELLA COMPAGNIA"), ("4. «IMBARCO IMMEDIATO AL GATE 3»", "VADO SUBITO AL GATE")],
       "5 · Senti l'annuncio: che cosa fai?", "5 · Gli annunci", "e5"),
  vf(["1. PER UN VOLO FUORI DALL'EUROPA PORTO IL PASSAPORTO.", "2. NEL BAGAGLIO A MANO POSSO PORTARE UNA BOTTIGLIA D'ACQUA DA UN LITRO.",
      "3. IL BAGAGLIO DA STIVA VA SOTTO L'AEREO.", "4. CON IL PERMESSO DI SOGGIORNO SCADUTO POSSO VIAGGIARE SENZA PROBLEMI."],
     ["VERO", "FALSO", "VERO", "FALSO"], "6 · Vero o falso?", "6 · Vero o falso", "e6"),
  parla("e7", 7, "SEI ALL'AGENZIA DI VIAGGI. CHIEDI UN VOLO: DOVE, QUANDO PARTI E TORNI, QUANTO COSTA, SE È DIRETTO E SE C'È IL BAGAGLIO."),
 ]
}


# =====================================================================
# 11. IN ALBERGO (città, A1/A2)
# =====================================================================
ALBERGO_SLIDE = [
    cover("🏨", "IN ALBERGO", "PRENOTARE, ARRIVARE, CHIEDERE", "VIAGGI &bull; A1/A2"),
    slide("CHE COSA IMPARIAMO?", cards([
        ("📞", "PRENOTARE", "UNA CAMERA SINGOLA, DOPPIA…"), ("🛎️", "ALLA RECEPTION", "IL CHECK-IN E LA CHIAVE"),
        ("🛏️", "LA CAMERA", "CHE COSA C'È?"), ("🔧", "UN PROBLEMA", "NON FUNZIONA…")])),
    slide("🛏️ CHE CAMERA?", cards([
        ("🛏️", "LA CAMERA SINGOLA", "PER UNA PERSONA"), ("🛏️🛏️", "LA CAMERA DOPPIA", "DUE LETTI SINGOLI"),
        ("💑", "LA CAMERA MATRIMONIALE", "UN LETTO GRANDE PER DUE"), ("👨‍👩‍👧", "LA CAMERA TRIPLA", "PER TRE PERSONE")]) + "\n" +
        nota("☕ <b>B&amp;B</b> = PERNOTTAMENTO E COLAZIONE. <b>MEZZA PENSIONE</b> = COLAZIONE E CENA. <b>PENSIONE COMPLETA</b> = COLAZIONE, PRANZO E CENA.")),
    slide("📞 PRENOTARE AL TELEFONO", dialogo([
        ("*RECEPTIONIST", "HOTEL MARE, BUONASERA."),
        ("LEILA", "BUONASERA. AVETE UNA CAMERA DOPPIA PER VENERDÌ E SABATO?"),
        ("*RECEPTIONIST", "SÌ. SONO 85 EURO A NOTTE, CON LA COLAZIONE."),
        ("LEILA", "LA CAMERA HA IL BAGNO E L'ARIA CONDIZIONATA?"),
        ("*RECEPTIONIST", "SÌ, CERTO. A CHE NOME?"),
        ("LEILA", "LEILA MANSOUR. ARRIVIAMO VERSO LE SEI."),
        ("*RECEPTIONIST", "PERFETTO. IL CHECK-IN È DALLE DUE DEL POMERIGGIO.")])),
    slide("🛎️ ALLA RECEPTION", ill("reception-albergo.png", "IL RECEPTIONIST DÀ LA CHIAVE A UN VIAGGIATORE") + "\n" + table([
        ["IL CHECK-IN", "ARRIVO: DO IL DOCUMENTO, PRENDO LA CHIAVE"], ["IL CHECK-OUT", "PARTENZA: LASCIO LA CAMERA (DI SOLITO ENTRO LE 11)"],
        ["LA CHIAVE / LA TESSERA", "PER APRIRE LA PORTA"], ["LA TASSA DI SOGGIORNO", "POCHI EURO A NOTTE PER LA CITTÀ"]])),
    slide("🛏️ NELLA CAMERA", ill("camera-albergo.png", "UNA CAMERA D'ALBERGO CON LETTO, ARMADIO E BAGNO") + "\n" + cards([
        ("🛏️", "IL LETTO", ""), ("🚪", "L'ARMADIO", ""), ("❄️", "L'ARIA CONDIZIONATA", ""), ("📺", "IL TELEVISORE", ""),
        ("🚿", "IL BAGNO CON LA DOCCIA", ""), ("🧴", "GLI ASCIUGAMANI", "")], "g3")),
    slide("🔧 C'È UN PROBLEMA!", table([
        ["NON FUNZIONA L'ARIA CONDIZIONATA.", "MANDO SUBITO UN TECNICO."], ["NON C'È L'ACQUA CALDA.", "CONTROLLIAMO."],
        ["MANCANO GLI ASCIUGAMANI.", "LI PORTIAMO SUBITO."], ["LA CAMERA È RUMOROSA. POSSO CAMBIARLA?", "VEDIAMO SE C'È UN'ALTRA CAMERA LIBERA."],
        ["QUAL È LA PASSWORD DEL WI-FI?", "È SCRITTA SUL BIGLIETTO CON LA CHIAVE."]], head=["IL CLIENTE", "LA RECEPTION"])),
    end("ORA SAI PRENOTARE E STARE IN ALBERGO!"),
]

ALBERGO = {
 "title": "🏨 In albergo · Esercizi", "store": "albergo", "upper": True,
 "sections": [
  {"part": "Le camere"},
  menu(["SINGOLA", "DOPPIA", "MATRIMONIALE", "TRIPLA"],
       [("1. VIAGGIO DA SOLO.", "SINGOLA"), ("2. SIAMO MARITO E MOGLIE E VOGLIAMO UN LETTO GRANDE.", "MATRIMONIALE"),
        ("3. SIAMO DUE AMICI: VOGLIAMO DUE LETTI.", "DOPPIA"), ("4. SIAMO MAMMA, PAPÀ E UN BAMBINO.", "TRIPLA")],
       "1 · Che camera prendo?", "1 · Le camere", "e1"),
  menu(["B&B", "MEZZA PENSIONE", "PENSIONE COMPLETA"],
       [("1. COLAZIONE, PRANZO E CENA", "PENSIONE COMPLETA"), ("2. SOLO COLAZIONE", "B&B"), ("3. COLAZIONE E CENA", "MEZZA PENSIONE")],
       "2 · Che cosa è compreso?", "2 · I pasti", "e2"),
  {"part": "Prenotare"},
  completa("RECEPTIONIST: HOTEL MARE, BUONASERA.<br>LEILA: BUONASERA. AVETE UNA CAMERA ___ PER VENERDÌ E SABATO?<br>"
           "RECEPTIONIST: SÌ. SONO 85 EURO A ___, CON LA COLAZIONE.<br>LEILA: LA CAMERA HA IL ___?<br>RECEPTIONIST: SÌ, CERTO. A CHE ___?<br>"
           "LEILA: LEILA MANSOUR.<br>RECEPTIONIST: IL ___ È DALLE DUE DEL POMERIGGIO.",
           ["doppia", "notte", "bagno", "nome", "check-in"], "3 · Completa la telefonata", "3 · Prenotare", "e3",
           "DOPPIA · NOTTE · BAGNO · NOME · CHECK-IN"),
  vf(["1. AL CHECK-IN DO UN DOCUMENTO.", "2. IL CHECK-OUT È QUANDO ARRIVO.", "3. LA TASSA DI SOGGIORNO SI PAGA PER OGNI NOTTE.",
      "4. DI SOLITO LASCIO LA CAMERA ENTRO LE 11."], ["VERO", "FALSO", "VERO", "VERO"], "4 · Vero o falso?", "4 · Vero o falso", "e4"),
  {"part": "Un problema"},
  menu(["MANDO SUBITO UN TECNICO.", "LI PORTIAMO SUBITO.", "VEDIAMO SE C'È UN'ALTRA CAMERA LIBERA.", "È SCRITTA SUL BIGLIETTO CON LA CHIAVE."],
       [("1. MANCANO GLI ASCIUGAMANI.", "LI PORTIAMO SUBITO."), ("2. QUAL È LA PASSWORD DEL WI-FI?", "È SCRITTA SUL BIGLIETTO CON LA CHIAVE."),
        ("3. L'ARIA CONDIZIONATA NON FUNZIONA.", "MANDO SUBITO UN TECNICO."), ("4. LA CAMERA È RUMOROSA. POSSO CAMBIARLA?", "VEDIAMO SE C'È UN'ALTRA CAMERA LIBERA.")],
       "5 · Che cosa risponde la reception?", "5 · Le risposte", "e5"),
  parla("e6", 6, "TELEFONI A UN ALBERGO. PRENOTA UNA CAMERA: PER QUANTE PERSONE, PER QUALI GIORNI. CHIEDI IL PREZZO E SE C'È LA COLAZIONE."),
 ]
}


# =====================================================================
# 12. DAL MECCANICO (città, A2)
# =====================================================================
MECCANICO_SLIDE = [
    cover("🔧", "DAL MECCANICO", "LA MACCHINA, I GUASTI, LA RIPARAZIONE", "MACCHINA E MOTORINO &bull; A2"),
    slide("CHE COSA IMPARIAMO?", cards([
        ("🚗", "LE PARTI DELLA MACCHINA", "RUOTE, FRENI, BATTERIA…"), ("⚠️", "I GUASTI", "CHE COSA NON VA?"),
        ("🗣️", "DAL MECCANICO", "SPIEGARE IL PROBLEMA"), ("📋", "LE REGOLE", "REVISIONE, ASSICURAZIONE")])),
    slide("🚗 LE PARTI DELLA MACCHINA", ill("parti-auto.png", "UNA MACCHINA CON LE SUE PARTI: RUOTA, FRENI, BATTERIA, FARI, SPECCHIETTO, MOTORE, TERGICRISTALLI") + "\n" + cards([
        ("🛞", "LE RUOTE / LE GOMME", ""), ("🛑", "I FRENI", "PER FERMARSI"), ("🔋", "LA BATTERIA", "PER ACCENDERE LA MACCHINA"),
        ("💡", "I FARI", "LA LUCE DAVANTI"), ("🪞", "LO SPECCHIETTO", "PER VEDERE DIETRO"), ("🌧️", "I TERGICRISTALLI", "PULISCONO IL VETRO")], "g3")),
    slide("⚠️ CHE COSA NON VA?", table([
        ["LA MACCHINA NON PARTE.", "FORSE È LA BATTERIA."], ["HO UNA GOMMA A TERRA / BUCATA.", "BISOGNA CAMBIARE LA RUOTA."],
        ["I FRENI FANNO RUMORE.", "BISOGNA CAMBIARE LE PASTIGLIE DEI FRENI."], ["SI È ACCESA UNA SPIA ROSSA.", "FERMATI E CHIAMA IL MECCANICO."],
        ["NON FUNZIONA UN FARO.", "BISOGNA CAMBIARE LA LAMPADINA."]], head=["IL PROBLEMA", "LA SOLUZIONE"])),
    slide("🗣️ ALL'OFFICINA", ill("officina.png", "UN MECCANICO IN OFFICINA CONTROLLA UNA RUOTA") + "\n" + dialogo([
        ("YUSUF", "BUONGIORNO. LA MIA MACCHINA FA UN RUMORE STRANO QUANDO FRENO."),
        ("*MECCANICO", "DA QUANTO TEMPO?"),
        ("YUSUF", "DA UNA SETTIMANA."),
        ("*MECCANICO", "SONO LE PASTIGLIE DEI FRENI. BISOGNA CAMBIARLE."),
        ("YUSUF", "QUANTO COSTA? E QUANDO È PRONTA?"),
        ("*MECCANICO", "CIRCA 120 EURO. LA PUÒ RITIRARE DOMANI POMERIGGIO."),
        ("YUSUF", "VA BENE. MI FA LA FATTURA, PER FAVORE?")])),
    slide("📋 LE REGOLE PER LA MACCHINA", cards([
        ("🪪", "LA PATENTE", "PER GUIDARE IN ITALIA. QUELLA DEL TUO PAESE VALE SOLO PER UN PO': INFORMATI"),
        ("📄", "L'ASSICURAZIONE", "OBBLIGATORIA. SENZA, NON PUOI GUIDARE"),
        ("🔍", "LA REVISIONE", "UN CONTROLLO DELLA MACCHINA: LA PRIMA DOPO 4 ANNI, POI OGNI 2 ANNI"),
        ("⛽", "IL BOLLO", "UNA TASSA CHE SI PAGA OGNI ANNO")]) + "\n" +
        nota("🦺 IN MACCHINA DEVI AVERE IL <b>GILET CATARIFRANGENTE</b> E IL <b>TRIANGOLO</b>. CON LA MACCHINA FERMA PER STRADA, METTI IL GILET!")),
    end("ORA SAI PARLARE CON IL MECCANICO!"),
]

MECCANICO = {
 "title": "🔧 Dal meccanico · Esercizi", "store": "meccanico", "upper": True,
 "sections": [
  {"part": "La macchina"},
  menu(["LE RUOTE", "I FRENI", "LA BATTERIA", "I FARI", "LO SPECCHIETTO", "I TERGICRISTALLI"],
       [("1. PER FERMARE LA MACCHINA USO…", "I FRENI"), ("2. DI NOTTE ACCENDO…", "I FARI"), ("3. PIOVE: ACCENDO…", "I TERGICRISTALLI"),
        ("4. PER VEDERE LE MACCHINE DIETRO GUARDO…", "LO SPECCHIETTO"), ("5. LA MACCHINA NON SI ACCENDE: FORSE È…", "LA BATTERIA"),
        ("6. HO UNA GOMMA BUCATA: CAMBIO UNA DELLE…", "LE RUOTE")],
       "1 · Le parti della macchina", "1 · Le parti", "e1"),
  {"part": "I guasti"},
  menu(["CAMBIARE LA BATTERIA", "CAMBIARE LA RUOTA", "CAMBIARE LE PASTIGLIE DEI FRENI", "CAMBIARE LA LAMPADINA"],
       [("1. HO UNA GOMMA A TERRA.", "CAMBIARE LA RUOTA"), ("2. LA MACCHINA NON PARTE, LA BATTERIA È VECCHIA.", "CAMBIARE LA BATTERIA"),
        ("3. I FRENI FANNO RUMORE.", "CAMBIARE LE PASTIGLIE DEI FRENI"), ("4. NON FUNZIONA UN FARO.", "CAMBIARE LA LAMPADINA")],
       "2 · Che cosa bisogna fare?", "2 · I guasti", "e2"),
  scegli([("1. CHE PROBLEMA HA LA MACCHINA DI YUSUF?", ["FA RUMORE QUANDO FRENA", "NON PARTE", "HA UNA GOMMA BUCATA"], "FA RUMORE QUANDO FRENA"),
          ("2. DA QUANTO TEMPO?", ["DA UNA SETTIMANA", "DA UN MESE", "DA IERI"], "DA UNA SETTIMANA"),
          ("3. QUANTO COSTA LA RIPARAZIONE?", ["CIRCA 120 EURO", "CIRCA 20 EURO", "NIENTE"], "CIRCA 120 EURO"),
          ("4. QUANDO È PRONTA LA MACCHINA?", ["DOMANI POMERIGGIO", "OGGI", "TRA UNA SETTIMANA"], "DOMANI POMERIGGIO")],
         "3 · All'officina: leggi e rispondi", "3 · All'officina", "e3",
         info="YUSUF: LA MIA MACCHINA FA UN RUMORE STRANO QUANDO FRENO.<br>MECCANICO: DA QUANTO TEMPO?<br>YUSUF: DA UNA SETTIMANA.<br>"
              "MECCANICO: SONO LE PASTIGLIE DEI FRENI. BISOGNA CAMBIARLE.<br>YUSUF: QUANTO COSTA? E QUANDO È PRONTA?<br>"
              "MECCANICO: CIRCA 120 EURO. LA PUÒ RITIRARE DOMANI POMERIGGIO."),
  {"part": "Le regole"},
  vf(["1. L'ASSICURAZIONE DELLA MACCHINA È OBBLIGATORIA.", "2. LA REVISIONE NON SERVE MAI.", "3. IL BOLLO SI PAGA OGNI ANNO.",
      "4. SE LA MACCHINA È FERMA PER STRADA METTO IL GILET CATARIFRANGENTE.", "5. CON LA PATENTE DEL MIO PAESE POSSO GUIDARE IN ITALIA PER SEMPRE."],
     ["VERO", "FALSO", "VERO", "VERO", "FALSO"], "4 · Vero o falso?", "4 · Vero o falso", "e4"),
  scrivi([("1. LA MACCHINA NON ___ (NON SI ACCENDE).", ["parte"]), ("2. HO UNA GOMMA ___ (CON UN BUCO).", ["bucata", "a terra"]),
          ("3. SI È ACCESA UNA ___ ROSSA.", ["spia"]), ("4. MI FA LA ___, PER FAVORE? (IL FOGLIO CON IL PREZZO E L'IVA)", ["fattura"])],
         "5 · Scrivi la parola", "5 · Le parole", "e5", bank="PARTE · BUCATA · SPIA · FATTURA"),
  parla("e6", 6, "SEI DAL MECCANICO. SPIEGA CHE PROBLEMA HA LA TUA MACCHINA (O IL MOTORINO), DA QUANDO, E CHIEDI QUANTO COSTA E QUANDO È PRONTA."),
 ]
}


# =====================================================================
# 13. AL NEGOZIO DI CASALINGHI (casa, A1)
# =====================================================================
CASALINGHI_SLIDE = [
    cover("🧹", "AL NEGOZIO DI CASALINGHI", "GLI OGGETTI PER LA CASA", "CASA &bull; A1"),
    slide("CHE COSA IMPARIAMO?", cards([
        ("🍽️", "PER LA CUCINA", "PIATTI, BICCHIERI, POSATE"), ("🧹", "PER PULIRE", "SCOPA, SECCHIO, MOCIO"),
        ("💡", "PER LA LUCE", "LAMPADINA, PROLUNGA, PRESA"), ("👕", "PER I VESTITI", "STENDINO, FERRO DA STIRO")])),
    slide("🏪 CHE COSA C'È NEL NEGOZIO?", ill("negozio-casalinghi.png", "UN NEGOZIO DI CASALINGHI CON PENTOLE, PIATTI, SCOPE E LAMPADINE") + "\n" +
        nota("IL NEGOZIO DI <b>CASALINGHI</b> VENDE TUTTO PER LA CASA. NEI NEGOZI GRANDI C'È ANCHE IL <b>FAI DA TE</b> (ATTREZZI, VITI, VERNICE).", "")),
    slide("🍽️ PER LA CUCINA", cards([
        ("🍽️", "I PIATTI", ""), ("🥛", "I BICCHIERI", ""), ("🍴", "LE POSATE", "FORCHETTE, COLTELLI, CUCCHIAI"),
        ("☕", "LE TAZZE", ""), ("🍳", "LE PENTOLE E LE PADELLE", ""), ("🫙", "I CONTENITORI", "PER IL CIBO IN FRIGORIFERO")], "g3")),
    slide("🧹 PER PULIRE", ill("oggetti-casa.png", "SCOPA, PALETTA, SECCHIO, MOCIO, LAMPADINA, PROLUNGA, FERRO DA STIRO, STENDINO, APPENDIABITI, FORBICI") + "\n" + cards([
        ("🧹", "LA SCOPA E LA PALETTA", "PER IL PAVIMENTO"), ("🪣", "IL SECCHIO E IL MOCIO", "PER LAVARE IL PAVIMENTO"),
        ("🧽", "LA SPUGNA", "PER I PIATTI"), ("🧴", "IL DETERSIVO", "PER PIATTI, PAVIMENTI, VESTITI")])),
    slide("💡 PER LA CASA", cards([
        ("💡", "LA LAMPADINA", "SI È BRUCIATA? LA CAMBIO"), ("🔌", "LA PROLUNGA / LA CIABATTA", "PIÙ PRESE PER LA CORRENTE"),
        ("👕", "LO STENDINO", "PER ASCIUGARE I VESTITI"), ("♨️", "IL FERRO DA STIRO", "PER STIRARE"),
        ("🧥", "LE GRUCCE (GLI APPENDIABITI)", "PER L'ARMADIO"), ("✂️", "LE FORBICI", "")], "g3")),
    slide("🗣️ AL NEGOZIO", dialogo([
        ("*COMMESSO", "BUONGIORNO, CERCA QUALCOSA?"),
        ("SAFIYA", "SÌ. HO BISOGNO DI UNA SCOPA, UN SECCHIO E SEI BICCHIERI."),
        ("*COMMESSO", "LE SCOPE SONO LÌ IN FONDO. I BICCHIERI DI VETRO O DI PLASTICA?"),
        ("SAFIYA", "DI VETRO. E UNA LAMPADINA PER LA CUCINA: QUESTA."),
        ("*COMMESSO", "ECCO. ALTRO?"),
        ("SAFIYA", "NO, GRAZIE. QUANTO SPENDO IN TUTTO?"),
        ("*COMMESSO", "SONO 24 EURO. VUOLE UNA BUSTA?")])),
    end("ORA SAI COMPRARE GLI OGGETTI PER LA CASA!"),
]

CASALINGHI = {
 "title": "🧹 Al negozio di casalinghi · Esercizi", "store": "casalinghi", "upper": True,
 "sections": [
  {"part": "Gli oggetti"},
  menu(["PER LA CUCINA", "PER PULIRE", "PER I VESTITI", "PER LA LUCE E LA CORRENTE"],
       [("1. LA SCOPA", "PER PULIRE"), ("2. LE POSATE", "PER LA CUCINA"), ("3. LO STENDINO", "PER I VESTITI"), ("4. LA LAMPADINA", "PER LA LUCE E LA CORRENTE"),
        ("5. IL MOCIO", "PER PULIRE"), ("6. LE TAZZE", "PER LA CUCINA"), ("7. IL FERRO DA STIRO", "PER I VESTITI"), ("8. LA PROLUNGA", "PER LA LUCE E LA CORRENTE")],
       "1 · A che cosa serve?", "1 · Gli oggetti", "e1"),
  scrivi([("1. 🧹 LA S C _ P A", ["scopa", "la scopa"]), ("2. 🪣 IL S E C C H _ O", ["secchio", "il secchio"]),
          ("3. 💡 LA L A M P A D _ N A", ["lampadina", "la lampadina"]), ("4. 🧽 LA S P U G N _", ["spugna", "la spugna"]),
          ("5. ✂️ LE F O R B _ C I", ["forbici", "le forbici"]), ("6. 🧴 IL D E T E R S I V _", ["detersivo", "il detersivo"])],
         "2 · Scrivi la parola", "2 · Le parole", "e2", cons="MANCA UNA LETTERA. SCRIVI TUTTA LA PAROLA."),
  {"part": "Al negozio"},
  menu(["LA LAMPADINA", "LO STENDINO", "IL DETERSIVO", "LE GRUCCE", "LA PROLUNGA"],
       [("1. LA LUCE IN BAGNO NON FUNZIONA. COMPRO…", "LA LAMPADINA"), ("2. HO LAVATO I VESTITI E LI VOGLIO ASCIUGARE. COMPRO…", "LO STENDINO"),
        ("3. LA PRESA È LONTANA DAL LETTO. COMPRO…", "LA PROLUNGA"), ("4. VOGLIO APPENDERE LE CAMICIE NELL'ARMADIO. COMPRO…", "LE GRUCCE"),
        ("5. VOGLIO LAVARE I PIATTI. COMPRO…", "IL DETERSIVO")],
       "3 · Che cosa compro?", "3 · Che cosa compro", "e3"),
  completa("COMMESSO: BUONGIORNO, ___ QUALCOSA?<br>SAFIYA: SÌ. HO ___ DI UNA SCOPA E SEI BICCHIERI.<br>COMMESSO: LE SCOPE SONO LÌ IN ___.<br>"
           "SAFIYA: GRAZIE. QUANTO ___ IN TUTTO?<br>COMMESSO: 24 EURO. VUOLE UNA ___?",
           ["cerca", "bisogno", "fondo", "spendo", "busta"], "4 · Completa il dialogo", "4 · Il dialogo", "e4", "CERCA · BISOGNO · FONDO · SPENDO · BUSTA"),
  parla("e5", 5, "SEI NELLA TUA CASA NUOVA. DI' CHE COSA TI SERVE PER LA CUCINA E PER PULIRE. POI CHIEDI AL COMMESSO DOVE SONO LE COSE E QUANTO COSTANO."),
 ]
}


# ---------------------------------------------------------------------
SLIDE_DRIVE = [
    ("cantiere/index.html", "IN CANTIERE", "LAVORO", CANTIERE_SLIDE, ILL_CSS),
    ("cucina-lavoro/index.html", "LAVORO IN CUCINA", "CUCINA", CUCINA_SLIDE, ILL_CSS),
    ("carne-pesce/index.html", "DAL MACELLAIO E IN PESCHERIA", "CUCINA", CARNE_SLIDE, ILL_CSS + FOTO_CSS),
    ("bar/index.html", "AL BAR", "IN CITTÀ", BAR_SLIDE, ILL_CSS + FOTO_CSS),
    ("treno/index.html", "PRENDO IL TRENO", "IN CITTÀ", TRENO_SLIDE, ILL_CSS),
    ("posta-banca/index.html", "ALLA POSTA E IN BANCA", "EDUCAZIONE CIVICA", POSTA_SLIDE, ILL_CSS),
    ("farmacia/index.html", "IN FARMACIA E AL PRONTO SOCCORSO", "SALUTE", FARMACIA_SLIDE, ILL_CSS),
    ("comune-questura/index.html", "AL COMUNE E IN QUESTURA", "EDUCAZIONE CIVICA", COMUNE_SLIDE, ILL_CSS),
    ("assistente-familiare/index.html", "L'ASSISTENTE FAMILIARE", "LAVORO", ASSISTENTE_SLIDE, ILL_CSS),
    ("aereo-viaggi/index.html", "IN AEREO E ALL'AGENZIA DI VIAGGI", "IN CITTÀ", AEREO_SLIDE, ILL_CSS),
    ("albergo/index.html", "IN ALBERGO", "IN CITTÀ", ALBERGO_SLIDE, ILL_CSS),
    ("meccanico/index.html", "DAL MECCANICO", "IN CITTÀ", MECCANICO_SLIDE, ILL_CSS),
    ("casalinghi/index.html", "AL NEGOZIO DI CASALINGHI", "LA CASA", CASALINGHI_SLIDE, ILL_CSS),
]
ESERCIZI_DRIVE = [("cantiere", CANTIERE), ("cucina-lavoro", CUCINA), ("carne-pesce", CARNE), ("bar", BAR), ("treno", TRENO),
                  ("posta-banca", POSTA), ("farmacia", FARMACIA), ("comune-questura", COMUNE), ("assistente-familiare", ASSISTENTE),
                  ("aereo-viaggi", AEREO), ("albergo", ALBERGO), ("meccanico", MECCANICO), ("casalinghi", CASALINGHI)]
