"""Escape room per ogni argomento della home (2026-10-30, Erila: «crea per ogni argomento un'escape room»).
Stesso motore di missione-casa/ (gioco.js, stile.css); i personaggi di missione-casa e missione-lavoro sono uniti in persone.js.
Ogni gioco: 4 porte × 3 prove, una lettera per porta, parola segreta finale. A1, STAMPATELLO MAIUSCOLO.
Uso: python3 _strumenti/missioni.py → crea missione-<argomento>/ (index.html, domande.js, gioco.js, stile.css, persone.js)."""
import json, os, re, shutil
from operatori import OPERATORI_JS

RADICE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def S(domanda, icona, risposte, aiuto, spiega):
    """scelta: la prima risposta è quella giusta (il gioco le mescola)"""
    return {"tipo": "scelta", "domanda": domanda, "icona": icona, "risposte": [{"t": t, "i": i} for t, i in risposte], "correct": 0, "aiuto": aiuto, "spiega": spiega}

def VF(domanda, icona, giusto, aiuto, spiega):
    return {"tipo": "vf", "domanda": domanda, "icona": icona, "correct": giusto, "aiuto": aiuto, "spiega": spiega}

def C(domanda, frase, icona, risposte, aiuto, spiega):
    return {"tipo": "completa", "domanda": domanda, "frase": frase, "icona": icona, "risposte": risposte, "correct": 0, "aiuto": aiuto, "spiega": spiega}

def porta(id, titolo, icona, lettera, chi, lezione, storia, fine, prove):
    return {"id": id, "titolo": titolo, "icona": icona, "lettera": lettera, "chi": chi, "lezione": {"titolo": lezione[0], "link": lezione[1]},
            "storia": storia, "fine": fine, "prove": prove}

GIOCHI = {}

# ------------------------------------------------------------------ SALUTE
GIOCHI["salute"] = dict(
  titolo="MISSIONE SALUTE", sottotitolo="AIUTA KWAME A STARE MEGLIO!", parolaSegreta="CURA", guida="michele", protagonista="kwame",
  etichetta="ITALIANO L2 · LA SALUTE", portaFinale="LA PORTA DELLA FARMACIA", grazie="GRAZIE! ADESSO STO MEGLIO!",
  imparato="HAI IMPARATO LE PARTI DEL CORPO, A DIRE CHE COSA TI FA MALE, A PARLARE CON IL MEDICO E IN FARMACIA.",
  intro=[["kwame", "CIAO, SONO KWAME. STAMATTINA NON STO BENE: HO MAL DI TESTA E MAL DI GOLA."],
         ["michele", "IO SONO MICHELE. TI AIUTO IO, KWAME! ANDIAMO INSIEME DAL MEDICO E IN FARMACIA."],
         ["michele", "CI SONO 4 PORTE. DIETRO OGNI PORTA C'È UNA LETTERA. CON LE 4 LETTERE SCOPRI LA PAROLA SEGRETA!"]],
  finale=[["kwame", "SONO IN FARMACIA CON LA RICETTA DEL MEDICO."], ["michele", "CHE COSA TI SERVE PER GUARIRE? SCRIVI LA PAROLA SEGRETA CON LE 4 LETTERE."]],
  vittoria="IL FARMACISTA DICE: «ECCO LA TUA CURA, KWAME. PRENDI LO SCIROPPO TRE VOLTE AL GIORNO. GUARISCI PRESTO!»",
  stanze=[
    porta("corpo", "IL CORPO", "🧍", "C", "michele", ("IL CORPO E IL DOTTORE", "corpo-dottore/"),
          [["michele", "PRIMA RIPASSIAMO LE PARTI DEL CORPO."]], ["kwame", "CONOSCO LE PARTI DEL CORPO!"], [
      S("CON CHE COSA VEDI?", "👀", [("CON GLI OCCHI", "👀"), ("CON LE ORECCHIE", "👂"), ("CON I PIEDI", "🦶")], "SONO DUE, SULLA FACCIA.", "VEDO CON GLI OCCHI."),
      S("CON CHE COSA SENTI LA MUSICA?", "🎵", [("CON LE ORECCHIE", "👂"), ("CON IL NASO", "👃"), ("CON LE MANI", "✋")], "SONO AI LATI DELLA TESTA.", "SENTO CON LE ORECCHIE."),
      C("COMPLETA.", "LA MANO HA CINQUE ___.", "✋", ["DITA", "DITI", "DITE"], "IL DITO → LE DITA: È UN PLURALE SPECIALE.", "IL DITO, LE DITA.")]),
    porta("male", "CHE COSA TI FA MALE?", "🤕", "U", "michele", ("IL CORPO E IL DOTTORE", "corpo-dottore/"),
          [["kwame", "MICHELE, COME DICO AL MEDICO CHE STO MALE?"]], ["michele", "BRAVO! ADESSO SAI DIRE CHE COSA TI FA MALE."], [
      S("KWAME DICE: «MI FA MALE…»", "🤕", [("LA TESTA", "🧠"), ("I DENTI", "🦷"), ("LE GAMBE", "🦵")], "MI FA MALE + UNA COSA SOLA.", "MI FA MALE LA TESTA. MI FANNO MALE I DENTI."),
      C("COMPLETA.", "MI ___ MALE I PIEDI.", "🦶", ["FANNO", "FA", "FAI"], "I PIEDI SONO DUE: PLURALE.", "MI FANNO MALE + PLURALE."),
      VF("«HO LA FEBBRE» VUOL DIRE: LA MIA TEMPERATURA È ALTA.", "🌡️", True, "PENSA AL TERMOMETRO.", "VERO. SOPRA 37 °C HO LA FEBBRE.")]),
    porta("medico", "DAL MEDICO", "🩺", "R", "michele", ("IL CORPO E IL DOTTORE", "corpo-dottore/"),
          [["michele", "ECCO LO STUDIO DEL MEDICO DI BASE. ENTRIAMO!"]], ["kwame", "IL MEDICO MI HA DATO LA RICETTA!"], [
      S("IL MEDICO CHIEDE: «CHE COSA SI SENTE?» KWAME RISPONDE:", "🩺", [("HO MAL DI GOLA E LA TOSSE.", "😷"), ("SONO LE TRE.", "🕒"), ("ABITO A BARI.", "🏠")], "IL MEDICO VUOLE SAPERE COME STAI.", "RISPONDO CON I SINTOMI: MAL DI GOLA, TOSSE, FEBBRE."),
      S("PER COMPRARE ALCUNE MEDICINE SERVE…", "📄", [("LA RICETTA", "📄"), ("IL BIGLIETTO", "🎫"), ("LO SCONTRINO", "🧾")], "LA SCRIVE IL MEDICO.", "LA RICETTA È IL FOGLIO DEL MEDICO PER LA FARMACIA."),
      VF("IN UN'EMERGENZA CHIAMO IL 112.", "🚑", True, "È IL NUMERO UNICO DI EMERGENZA.", "VERO. IL 112 È IL NUMERO PER LE EMERGENZE.")]),
    porta("farmacia", "IN FARMACIA", "💊", "A", "michele", ("IN FARMACIA E AL PRONTO SOCCORSO", "farmacia/"),
          [["michele", "ULTIMA PORTA: LA FARMACIA. C'È LA CROCE VERDE!"]], ["kwame", "HO TUTTO! GRAZIE, MICHELE."], [
      S("HO LA TOSSE. CHE COSA COMPRO?", "😷", [("LO SCIROPPO", "🧴"), ("IL CEROTTO", "🩹"), ("IL TERMOMETRO", "🌡️")], "SI BEVE CON IL CUCCHIAIO.", "PER LA TOSSE PRENDO LO SCIROPPO."),
      C("COMPLETA.", "PRENDA UNA PASTIGLIA DUE VOLTE AL ___.", "💊", ["GIORNO", "ORA", "MESE"], "MATTINA E SERA.", "DUE VOLTE AL GIORNO = MATTINA E SERA."),
      VF("LA FARMACIA HA UNA CROCE VERDE.", "➕", True, "GUARDA LE INSEGNE IN CITTÀ.", "VERO. LA CROCE VERDE ACCESA = FARMACIA.")]),
  ])

# ------------------------------------------------------------------ CUCINA
GIOCHI["cucina"] = dict(
  titolo="MISSIONE CUCINA", sottotitolo="PREPARA LA CENA CON FATOU!", parolaSegreta="PANE", guida="giovanni", protagonista="fatou",
  etichetta="ITALIANO L2 · IL CIBO", portaFinale="LA PORTA DELLA CUCINA", grazie="GRAZIE! LA CENA È PRONTA!",
  imparato="HAI IMPARATO I NEGOZI, LA FRUTTA E LA VERDURA, I VERBI DELLA CUCINA E COME SI ORDINA AL RISTORANTE.",
  intro=[["fatou", "STASERA INVITO A CENA LE MIE AMICHE! DEVO FARE LA SPESA E CUCINARE."], ["giovanni", "IO SONO GIOVANNI. TI AIUTO IO, FATOU!"],
         ["giovanni", "CI SONO 4 PORTE. CON LE 4 LETTERE SCOPRI CHE COSA NON PUÒ MANCARE A TAVOLA!"]],
  finale=[["fatou", "LA TAVOLA È PRONTA. MA MANCA UNA COSA…"], ["giovanni", "CHE COSA MANCA? SCRIVI LA PAROLA SEGRETA."]],
  vittoria="LE AMICHE DICONO: «CHE BUONO IL PANE CALDO, FATOU! E ANCHE LA CENA È BUONISSIMA!»",
  stanze=[
    porta("negozi", "I NEGOZI", "🏪", "P", "giovanni", ("AL MERCATO", "mercato/"), [["giovanni", "PRIMA ANDIAMO A FARE LA SPESA."]], ["fatou", "HO COMPRATO TUTTO!"], [
      S("DOVE COMPRO IL PANE?", "🥖", [("DAL PANETTIERE", "🥖"), ("DAL MACELLAIO", "🥩"), ("IN FARMACIA", "💊")], "IL PANETTIERE FA IL PANE.", "IL PANE SI COMPRA DAL PANETTIERE O AL FORNO."),
      S("DOVE COMPRO IL POLLO?", "🍗", [("DAL MACELLAIO", "🥩"), ("DAL PESCIVENDOLO", "🐟"), ("DAL FRUTTIVENDOLO", "🍎")], "VENDE LA CARNE.", "LA CARNE SI COMPRA DAL MACELLAIO."),
      C("COMPLETA.", "VORREI UN CHILO ___ PATATE.", "🥔", ["DI", "A", "IN"], "UN CHILO, UN LITRO, UN ETTO + …", "UN CHILO DI PATATE.")]),
    porta("frutta", "FRUTTA E VERDURA", "🍅", "A", "giovanni", ("IL CIBO E LA CUCINA", "parole/cucina.html"), [["giovanni", "ORA IL FRUTTIVENDOLO!"]], ["fatou", "CHE BELLA FRUTTA!"], [
      S("È ROSSO E SI USA PER IL SUGO.", "🍅", [("IL POMODORO", "🍅"), ("LA BANANA", "🍌"), ("LA CAROTA", "🥕")], "LA PASTA AL ___.", "IL POMODORO È ROSSO: CON LUI FACCIAMO IL SUGO."),
      S("È GIALLO E ACIDO.", "🍋", [("IL LIMONE", "🍋"), ("LA FRAGOLA", "🍓"), ("L'UVA", "🍇")], "SI METTE SUL PESCE.", "IL LIMONE È GIALLO E ACIDO."),
      VF("LE MELE E LE PERE SONO FRUTTA.", "🍎", True, "SI MANGIANO DOPO IL PRANZO.", "VERO.")]),
    porta("cucinare", "CUCINIAMO!", "🍳", "N", "giovanni", ("LAVORO IN CUCINA", "cucina-lavoro/"), [["giovanni", "A CASA! ADESSO SI CUCINA."]], ["fatou", "LA PASTA È PRONTA!"], [
      S("PRIMA DI MANGIARE LA FRUTTA LA DEVO…", "💧", [("LAVARE", "💧"), ("FRIGGERE", "🍳"), ("CONGELARE", "❄️")], "CON L'ACQUA.", "LA FRUTTA SI LAVA."),
      C("COMPLETA.", "METTO L'ACQUA SUL FUOCO E ___ LA PASTA.", "🍝", ["CUOCIO", "BEVO", "TAGLIO"], "LA PASTA VA IN ACQUA CHE BOLLE.", "CUOCIO LA PASTA PER 10 MINUTI."),
      S("CON CHE COSA TAGLIO IL PANE?", "🔪", [("CON IL COLTELLO", "🔪"), ("CON IL CUCCHIAIO", "🥄"), ("CON IL BICCHIERE", "🥛")], "È AFFILATO.", "TAGLIO CON IL COLTELLO.")]),
    porta("tavola", "A TAVOLA", "🍽️", "E", "giovanni", ("AL RISTORANTE", "ristorante/"), [["fatou", "ARRIVANO LE AMICHE! PREPARIAMO LA TAVOLA."]], ["giovanni", "BRAVISSIMA, FATOU!"], [
      S("UN'AMICA CHIEDE L'ACQUA. CHE COSA DICE?", "💧", [("MI PASSI L'ACQUA, PER FAVORE?", "🙏"), ("DAMMI ACQUA!", "😠"), ("ACQUA NO.", "🙅")], "È GENTILE.", "SI DICE «PER FAVORE»."),
      C("COMPLETA.", "BUON ___!", "😋", ["APPETITO", "GIORNO", "VIAGGIO"], "SI DICE PRIMA DI MANGIARE.", "BUON APPETITO!"),
      VF("IN ITALIA IL PRANZO È DI SOLITO VERSO L'UNA.", "🕐", True, "TRA MEZZOGIORNO E LE DUE.", "VERO.")]),
  ])

# ------------------------------------------------------------------ FAMIGLIA
GIOCHI["famiglia"] = dict(
  titolo="MISSIONE FAMIGLIA", sottotitolo="PREPARA LA FESTA DELLA NONNA!", parolaSegreta="BACI", guida="eneida", protagonista="lin",
  etichetta="ITALIANO L2 · LA FAMIGLIA", portaFinale="LA PORTA DELLA FESTA", grazie="GRAZIE! È UNA FESTA BELLISSIMA!",
  imparato="HAI IMPARATO I NOMI DEI PARENTI, I POSSESSIVI E A DESCRIVERE LE PERSONE.",
  intro=[["lin", "OGGI LA MIA NONNA COMPIE 80 ANNI! FACCIAMO UNA FESTA IN VIDEOCHIAMATA CON TUTTA LA FAMIGLIA."], ["eneida", "CHE BELLO! SONO ENEIDA, LA COORDINATRICE. TI AIUTO A PREPARARE TUTTO."],
         ["eneida", "CI SONO 4 PORTE. CON LE 4 LETTERE SCOPRI CHE COSA MANDA LA FAMIGLIA ALLA NONNA!"]],
  finale=[["lin", "TUTTI SONO IN VIDEOCHIAMATA. LA NONNA È FELICE!"], ["eneida", "CHE COSA MANDANO TUTTI ALLA NONNA? SCRIVI LA PAROLA SEGRETA."]],
  vittoria="TUTTI DICONO: «TANTI AUGURI, NONNA! TANTI BACI DA TUTTA LA FAMIGLIA!»",
  stanze=[
    porta("parenti", "I PARENTI", "👨‍👩‍👧", "B", "eneida", ("LA FAMIGLIA", "letture/famiglia.html"), [["eneida", "CHI C'È NELLA TUA FAMIGLIA?"]], ["lin", "CONOSCO TUTTI I PARENTI!"], [
      S("LA MADRE DI MIA MADRE È MIA…", "👵", [("NONNA", "👵"), ("ZIA", "👩"), ("SORELLA", "👧")], "È LA FESTEGGIATA DI OGGI!", "LA MADRE DELLA MAMMA È LA NONNA."),
      S("IL FRATELLO DI MIO PADRE È MIO…", "👨", [("ZIO", "👨"), ("CUGINO", "👦"), ("NONNO", "👴")], "È DELLA GENERAZIONE DEI GENITORI.", "IL FRATELLO DEL PAPÀ È LO ZIO."),
      C("COMPLETA.", "IL FIGLIO DI MIO ZIO È MIO ___.", "👦", ["CUGINO", "NIPOTE", "FRATELLO"], "È DELLA MIA GENERAZIONE.", "IL FIGLIO DELLO ZIO È IL CUGINO.")]),
    porta("possessivi", "MIO, TUO, SUO", "🔑", "A", "eneida", ("I POSSESSIVI", "possessivi/esercizi.html"), [["eneida", "ORA PARLIAMO DEI REGALI: DI CHI SONO?"]], ["lin", "CHE FACILE!"], [
      C("COMPLETA.", "___ NONNA SI CHIAMA FATIMA.", "👵", ["MIA", "LA MIA", "MIO"], "CON I PARENTI AL SINGOLARE: NIENTE ARTICOLO.", "MIA NONNA (SENZA «LA»)."),
      C("COMPLETA.", "___ FRATELLI ABITANO IN FRANCIA.", "👬", ["I MIEI", "MIEI", "LE MIE"], "AL PLURALE CI VUOLE L'ARTICOLO.", "I MIEI FRATELLI."),
      VF("«SUA SORELLA» PUÒ ESSERE LA SORELLA DI LUI O DI LEI.", "👧", True, "SUO/SUA DIPENDE DALLA COSA, NON DALLA PERSONA.", "VERO.")]),
    porta("descrivere", "COM'È?", "🪞", "C", "eneida", ("GLI AGGETTIVI", "aggettivi/esercizi.html"), [["lin", "DESCRIVO LA MIA FAMIGLIA A ENEIDA."]], ["eneida", "CHE BELLA FAMIGLIA!"], [
      S("IL NONNO HA 90 ANNI. È…", "👴", [("ANZIANO", "👴"), ("GIOVANE", "🧒"), ("PICCOLO", "👶")], "HA TANTI ANNI.", "CON TANTI ANNI SI È ANZIANI."),
      C("COMPLETA.", "LE MIE CUGINE SONO ALT___.", "👭", ["E", "I", "A"], "CUGINE: FEMMINILE PLURALE.", "LE CUGINE SONO ALTE."),
      S("RIDE SEMPRE ED È CONTENTA. È…", "😄", [("ALLEGRA", "😄"), ("TRISTE", "😢"), ("ARRABBIATA", "😠")], "IL CONTRARIO DI TRISTE.", "È ALLEGRA.")]),
    porta("festa", "LA FESTA", "🎂", "I", "eneida", ("FESTE E TRADIZIONI", "feste/"), [["eneida", "ULTIMA PORTA: GLI AUGURI!"]], ["lin", "LA FESTA COMINCIA!"], [
      S("PER IL COMPLEANNO SI DICE…", "🎂", [("TANTI AUGURI!", "🎉"), ("BUON NATALE!", "🎄"), ("BUON VIAGGIO!", "✈️")], "È IL GIORNO IN CUI SEI NATO.", "TANTI AUGURI! / BUON COMPLEANNO!"),
      C("COMPLETA.", "LA NONNA ___ 80 ANNI.", "👵", ["HA", "È", "FA"], "L'ETÀ SI DICE CON AVERE.", "HA 80 ANNI."),
      VF("SULLA TORTA CI SONO LE CANDELINE.", "🕯️", True, "SI SOFFIANO!", "VERO.")]),
  ])

# ------------------------------------------------------------------ VESTITI
GIOCHI["vestiti"] = dict(
  titolo="MISSIONE VESTITI", sottotitolo="TROVA I VESTITI GIUSTI PER IL COLLOQUIO!", parolaSegreta="MODA", guida="cristian", protagonista="ravi",
  etichetta="ITALIANO L2 · I VESTITI", portaFinale="LA PORTA DEL NEGOZIO", grazie="GRAZIE! ORA SONO PRONTO!",
  imparato="HAI IMPARATO I VESTITI, I COLORI, COME SI COMPRA IN UN NEGOZIO E CHE COSA SI METTE CON IL TEMPO DIVERSO.",
  intro=[["ravi", "LUNEDÌ HO UN COLLOQUIO DI LAVORO. DEVO COMPRARE DEI VESTITI NUOVI!"], ["cristian", "SONO CRISTIAN. ANDIAMO INSIEME AL NEGOZIO."],
         ["cristian", "CI SONO 4 PORTE. CON LE 4 LETTERE SCOPRI LA PAROLA SEGRETA!"]],
  finale=[["ravi", "HO LA GIACCA, LA CAMICIA E LE SCARPE NUOVE!"], ["cristian", "SEI ELEGANTISSIMO! SEI ALLA… SCRIVI LA PAROLA SEGRETA."]],
  vittoria="CRISTIAN DICE: «SEI ALLA MODA, RAVI! IN BOCCA AL LUPO PER IL COLLOQUIO!»",
  stanze=[
    porta("capi", "I VESTITI", "👕", "M", "cristian", ("I VESTITI", "abbigliamento/"), [["cristian", "PRIMA RIPASSIAMO I NOMI DEI VESTITI."]], ["ravi", "CONOSCO I VESTITI!"], [
      S("SI METTE SOPRA LA CAMICIA, PER IL COLLOQUIO.", "🧥", [("LA GIACCA", "🧥"), ("IL COSTUME", "🩱"), ("IL PIGIAMA", "🛌")], "È ELEGANTE.", "LA GIACCA SI METTE SOPRA LA CAMICIA."),
      S("SI METTONO AI PIEDI.", "👞", [("LE SCARPE", "👞"), ("I GUANTI", "🧤"), ("IL CAPPELLO", "🎩")], "CAMMINI CON…", "LE SCARPE SI METTONO AI PIEDI."),
      C("COMPLETA.", "UN ___ DI PANTALONI.", "👖", ["PAIO", "PAIA", "PEZZO"], "PER LE COSE DOPPIE: UN ___ DI SCARPE.", "UN PAIO DI PANTALONI.")]),
    porta("colori", "I COLORI", "🎨", "O", "cristian", ("VESTITI E COLORI", "parole/vestiti.html"), [["cristian", "DI CHE COLORE LA VUOI?"]], ["ravi", "MI PIACE IL BLU!"], [
      C("COMPLETA.", "LA CAMICIA BIANC___.", "👔", ["A", "O", "HE"], "CAMICIA È FEMMINILE.", "LA CAMICIA BIANCA."),
      C("COMPLETA.", "LE SCARPE NER___.", "👞", ["E", "I", "O"], "SCARPE: FEMMINILE PLURALE.", "LE SCARPE NERE."),
      VF("«BLU» NON CAMBIA: UNA GIACCA BLU, DUE GIACCHE BLU.", "🔵", True, "ALCUNI COLORI NON CAMBIANO MAI.", "VERO. ANCHE ROSA E VIOLA NON CAMBIANO.")]),
    porta("negozio", "AL NEGOZIO", "🛍️", "D", "cristian", ("I VESTITI", "abbigliamento/"), [["cristian", "ENTRIAMO NEL NEGOZIO."]], ["ravi", "HO COMPRATO TUTTO!"], [
      S("LA COMMESSA CHIEDE: «CHE TAGLIA PORTA?»", "📏", [("LA 50.", "📏"), ("IL 42 DI SCARPE.", "👞"), ("40 EURO.", "💶")], "PER I VESTITI: 46, 48, 50… O S, M, L.", "LA TAGLIA DEI VESTITI È UN NUMERO O UNA LETTERA."),
      S("VUOI PROVARE LA GIACCA. CHE COSA CHIEDI?", "🚪", [("POSSO PROVARLA?", "🙂"), ("QUANTO È ALTA?", "📐"), ("C'È IL BAGNO?", "🚻")], "C'È IL CAMERINO.", "POSSO PROVARLA? DOV'È IL CAMERINO?"),
      C("COMPLETA.", "QUANTO ___ QUESTE SCARPE?", "💶", ["COSTANO", "COSTA", "SONO COSTA"], "LE SCARPE: PLURALE.", "QUANTO COSTANO?")]),
    porta("tempo", "CHE COSA METTO?", "🌦️", "A", "cristian", ("IL TEMPO", "tempo/"), [["cristian", "LUNEDÌ CHE TEMPO FA?"]], ["ravi", "SONO PRONTO PER OGNI TEMPO!"], [
      S("PIOVE. CHE COSA PRENDI?", "🌧️", [("L'OMBRELLO", "☂️"), ("GLI OCCHIALI DA SOLE", "🕶️"), ("IL COSTUME", "🩱")], "TI PROTEGGE DALL'ACQUA.", "CON LA PIOGGIA PRENDO L'OMBRELLO."),
      S("FA FREDDO. CHE COSA METTI?", "❄️", [("IL CAPPOTTO", "🧥"), ("I PANTALONCINI", "🩳"), ("I SANDALI", "🩴")], "È PESANTE E CALDO.", "D'INVERNO METTO IL CAPPOTTO."),
      VF("D'ESTATE A BARI FA MOLTO CALDO.", "☀️", True, "LUGLIO E AGOSTO…", "VERO.")]),
  ])

# ------------------------------------------------------------------ CITTÀ
GIOCHI["citta"] = dict(
  titolo="MISSIONE CITTÀ", sottotitolo="AIUTA MARIELA A MUOVERSI A BARI!", parolaSegreta="META", guida="saleah", protagonista="mariela",
  etichetta="ITALIANO L2 · LA CITTÀ", portaFinale="LA PORTA DELLA STAZIONE", grazie="GRAZIE! SONO ARRIVATA!",
  imparato="HAI IMPARATO I LUOGHI DELLA CITTÀ, LE INDICAZIONI, L'AUTOBUS, IL TRENO E I CARTELLI.",
  intro=[["mariela", "OGGI DEVO ANDARE IN TANTI POSTI A BARI. MA NON CONOSCO BENE LA CITTÀ!"], ["saleah", "SONO SALEAH. TI ACCOMPAGNO IO!"],
         ["saleah", "CI SONO 4 PORTE. CON LE 4 LETTERE SCOPRI LA PAROLA SEGRETA: È LA FINE DEL VIAGGIO!"]],
  finale=[["mariela", "HO PRESO L'AUTOBUS E IL TRENO. ECCO IL MARE DI POLIGNANO!"], ["saleah", "COME SI CHIAMA IL POSTO DOVE ARRIVI? SCRIVI LA PAROLA SEGRETA."]],
  vittoria="SALEAH DICE: «SEI ARRIVATA ALLA META, MARIELA! ADESSO CONOSCI LA CITTÀ.»",
  stanze=[
    porta("luoghi", "I LUOGHI", "🏙️", "M", "saleah", ("LA CITTÀ", "#citta"), [["saleah", "DOVE DEVI ANDARE, MARIELA?"]], ["mariela", "CONOSCO I LUOGHI!"], [
      S("DEVO SPEDIRE UN PACCO. DOVE VADO?", "📦", [("ALLA POSTA", "🏤"), ("IN FARMACIA", "💊"), ("AL BAR", "☕")], "C'È LO SPORTELLO GIALLO.", "UN PACCO SI SPEDISCE ALLA POSTA."),
      S("DEVO PRENDERE IL TRENO. DOVE VADO?", "🚆", [("ALLA STAZIONE", "🚉"), ("ALL'OSPEDALE", "🏥"), ("IN BANCA", "🏦")], "CI SONO I BINARI.", "IL TRENO SI PRENDE ALLA STAZIONE."),
      C("COMPLETA.", "VADO ___ SUPERMERCATO.", "🛒", ["AL", "IN", "A"], "A + IL = …", "VADO AL SUPERMERCATO.")]),
    porta("strada", "LE INDICAZIONI", "🧭", "E", "saleah", ("I PUNTI CARDINALI", "punti-cardinali/"), [["mariela", "SCUSI, DOV'È LA FERMATA?"]], ["saleah", "PERFETTO!"], [
      S("➡️ VUOL DIRE…", "➡️", [("GIRA A DESTRA", "➡️"), ("GIRA A SINISTRA", "⬅️"), ("TORNA INDIETRO", "↩️")], "LA MANO CON CUI SCRIVONO TANTE PERSONE.", "➡️ = A DESTRA."),
      C("COMPLETA.", "VAI SEMPRE ___ PER 100 METRI.", "⬆️", ["DRITTO", "DESTRA", "SOPRA"], "NON GIRARE.", "SEMPRE DRITTO."),
      VF("«È DI FRONTE ALLA CHIESA» VUOL DIRE: È DALL'ALTRA PARTE DELLA STRADA.", "⛪", True, "LA VEDI DAVANTI A TE.", "VERO.")]),
    porta("autobus", "L'AUTOBUS", "🚌", "T", "saleah", ("PRENDO L'AUTOBUS", "autobus/"), [["saleah", "ECCO LA FERMATA DELL'AUTOBUS."]], ["mariela", "SONO SULL'AUTOBUS!"], [
      S("DOVE COMPRO IL BIGLIETTO DELL'AUTOBUS?", "🎫", [("IN TABACCHERIA O CON L'APP", "📱"), ("IN FARMACIA", "💊"), ("DAL MEDICO", "🩺")], "C'È LA T.", "IL BIGLIETTO SI COMPRA IN TABACCHERIA, IN EDICOLA O CON L'APP."),
      VF("SULL'AUTOBUS DEVO CONVALIDARE IL BIGLIETTO.", "🎫", True, "SE NON LO FAI, PUOI PRENDERE UNA MULTA.", "VERO."),
      C("COMPLETA.", "SCUSI, A CHE ORA ___ L'AUTOBUS?", "🕐", ["PASSA", "PASSANO", "PASSI"], "L'AUTOBUS: UNO SOLO.", "A CHE ORA PASSA L'AUTOBUS?")]),
    porta("treno", "IL TRENO", "🚆", "A", "saleah", ("PRENDO IL TRENO", "treno/"), [["saleah", "ULTIMA PORTA: LA STAZIONE."]], ["mariela", "IL TRENO PARTE!"], [
      S("IL TABELLONE DICE «BIN. 3». CHE COSA VUOL DIRE?", "🚉", [("BINARIO 3", "🛤️"), ("BIGLIETTO 3", "🎫"), ("3 EURO", "💶")], "È IL POSTO DOVE SI FERMA IL TRENO.", "BIN. = BINARIO."),
      C("COMPLETA.", "VORREI UN BIGLIETTO ___ POLIGNANO.", "🎫", ["PER", "DA", "IN"], "LA DESTINAZIONE.", "UN BIGLIETTO PER POLIGNANO."),
      VF("«IN RITARDO» VUOL DIRE CHE IL TRENO ARRIVA PRIMA.", "⏱️", False, "RITARDO = TARDI.", "FALSO. IN RITARDO = ARRIVA DOPO L'ORARIO.")]),
  ])

# ------------------------------------------------------------------ EDUCAZIONE CIVICA
GIOCHI["civica"] = dict(
  titolo="MISSIONE CITTADINO", sottotitolo="AIUTA TESFAYE CON I DOCUMENTI!", parolaSegreta="DIRITTI", guida="silvia2", protagonista="tesfaye",
  etichetta="ITALIANO L2 · EDUCAZIONE CIVICA", portaFinale="LA PORTA DEL COMUNE", grazie="GRAZIE! ORA CONOSCO I MIEI DIRITTI E I MIEI DOVERI!",
  imparato="HAI IMPARATO I DOCUMENTI, GLI UFFICI, I DIRITTI E I DOVERI E LE REGOLE DELLA CONVIVENZA.",
  intro=[["tesfaye", "DEVO FARE TANTI DOCUMENTI: CODICE FISCALE, RESIDENZA, CARTA D'IDENTITÀ…"], ["silvia2", "NON TI PREOCCUPARE, TI AIUTO IO."],
         ["silvia2", "CI SONO 7 PORTE. CON LE 7 LETTERE SCOPRI CHE COSA HANNO TUTTE LE PERSONE IN ITALIA!"]],
  finale=[["tesfaye", "HO TUTTI I DOCUMENTI!"], ["silvia2", "LA COSTITUZIONE DICE CHE TUTTI HANNO DEI… SCRIVI LA PAROLA SEGRETA."]],
  vittoria="SILVIA DICE: «TUTTE LE PERSONE HANNO DIRITTI E DOVERI. BENVENUTO, TESFAYE!»",
  stanze=[
    porta("codice", "IL CODICE FISCALE", "🪪", "D", "silvia2", ("IL CODICE FISCALE", "codice-fiscale/"), [["silvia2", "IL PRIMO DOCUMENTO È IL CODICE FISCALE."]], ["tesfaye", "HO IL CODICE FISCALE!"], [
      S("DOVE CHIEDO IL CODICE FISCALE?", "🏢", [("ALL'AGENZIA DELLE ENTRATE", "🏢"), ("AL SUPERMERCATO", "🛒"), ("IN STAZIONE", "🚉")], "È L'UFFICIO DELLE TASSE.", "IL CODICE FISCALE SI CHIEDE ALL'AGENZIA DELLE ENTRATE."),
      VF("IL CODICE FISCALE HA 16 CARATTERI: LETTERE E NUMERI.", "🔢", True, "CONTA: RSSMRA80A01A662X.", "VERO.")]),
    porta("residenza", "LA RESIDENZA", "🏠", "I", "silvia2", ("IN COMUNE E IN QUESTURA", "comune-questura/"), [["silvia2", "ORA LA RESIDENZA, IN COMUNE."]], ["tesfaye", "HO LA RESIDENZA!"], [
      S("DOVE CHIEDO LA RESIDENZA?", "🏛️", [("ALL'ANAGRAFE DEL COMUNE", "🏛️"), ("IN QUESTURA", "👮"), ("IN BANCA", "🏦")], "È L'UFFICIO DEL COMUNE PER I CITTADINI.", "LA RESIDENZA SI CHIEDE ALL'ANAGRAFE."),
      VF("LA RESIDENZA È L'INDIRIZZO DOVE ABITO DI SOLITO.", "📍", True, "È DOVE VIVI.", "VERO.")]),
    porta("carta", "LA CARTA D'IDENTITÀ", "🪪", "R", "silvia2", ("IN COMUNE E IN QUESTURA", "comune-questura/"), [["silvia2", "CON LA RESIDENZA PUOI CHIEDERE LA CARTA D'IDENTITÀ."]], ["tesfaye", "ECCO LA MIA CIE!"], [
      S("LA CARTA D'IDENTITÀ ELETTRONICA SI CHIAMA…", "💳", [("CIE", "💳"), ("SPID", "📱"), ("IBAN", "🏦")], "C-I-E.", "CIE = CARTA D'IDENTITÀ ELETTRONICA."),
      VF("PER LA CIE SERVE UNA FOTO.", "📷", True, "SULLA CARTA C'È LA TUA FACCIA.", "VERO.")]),
    porta("permesso", "IL PERMESSO DI SOGGIORNO", "📄", "I", "silvia2", ("IN COMUNE E IN QUESTURA", "comune-questura/"), [["tesfaye", "IL MIO PERMESSO SCADE FRA DUE MESI!"]], ["silvia2", "BRAVO, NON DIMENTICARE LA DATA!"], [
      S("DOVE RINNOVO IL PERMESSO DI SOGGIORNO?", "👮", [("IN QUESTURA", "👮"), ("DAL MEDICO", "🩺"), ("A SCUOLA", "🏫")], "È L'UFFICIO DELLA POLIZIA.", "IL PERMESSO SI RINNOVA IN QUESTURA (CON IL KIT DELLA POSTA)."),
      VF("IL PERMESSO SI PUÒ RINNOVARE ANCHE DOPO TRE ANNI DALLA SCADENZA.", "📅", False, "BISOGNA FARLO PRIMA.", "FALSO. SI CHIEDE IL RINNOVO PRIMA DELLA SCADENZA.")]),
    porta("diritti", "DIRITTI E DOVERI", "⚖️", "T", "silvia2", ("EDUCAZIONE CIVICA", "#educazione-civica"), [["silvia2", "IN ITALIA HAI DIRITTI E DOVERI."]], ["tesfaye", "HO CAPITO!"], [
      S("QUALE È UN DOVERE?", "💶", [("PAGARE LE TASSE", "💶"), ("ANDARE AL MARE", "🏖️"), ("GUARDARE LA TV", "📺")], "SERVE PER LE SCUOLE E GLI OSPEDALI.", "PAGARE LE TASSE È UN DOVERE."),
      VF("TUTTI HANNO DIRITTO ALLE CURE MEDICHE URGENTI.", "🏥", True, "LO DICE LA COSTITUZIONE (ARTICOLO 32).", "VERO.")]),
    porta("costituzione", "LA COSTITUZIONE", "📜", "T", "silvia2", ("EDUCAZIONE CIVICA", "#educazione-civica"), [["silvia2", "LA LEGGE PIÙ IMPORTANTE È LA COSTITUZIONE."]], ["tesfaye", "CHE INTERESSANTE!"], [
      S("IL 2 GIUGNO È…", "🇮🇹", [("LA FESTA DELLA REPUBBLICA", "🇮🇹"), ("NATALE", "🎄"), ("FERRAGOSTO", "☀️")], "NEL 1946 GLI ITALIANI HANNO VOTATO.", "IL 2 GIUGNO È LA FESTA DELLA REPUBBLICA."),
      VF("LA COSTITUZIONE ITALIANA È DEL 1948.", "📜", True, "È ENTRATA IN VIGORE IL 1° GENNAIO 1948.", "VERO.")]),
    porta("regole", "LE REGOLE DI TUTTI I GIORNI", "♻️", "I", "silvia2", ("LA RACCOLTA DIFFERENZIATA", "raccolta-differenziata/"), [["silvia2", "ULTIMA PORTA: LE REGOLE DELLA CONVIVENZA."]], ["tesfaye", "RISPETTO LE REGOLE!"], [
      S("DOVE BUTTO LA BOTTIGLIA DI VETRO?", "🍾", [("NEL VETRO", "🟩"), ("NELL'ORGANICO", "🟫"), ("PER STRADA", "🚮")], "C'È UN BIDONE SOLO PER IL VETRO.", "IL VETRO VA NEL BIDONE DEL VETRO."),
      VF("IN AUTO TUTTI DEVONO METTERE LA CINTURA.", "🚗", True, "ANCHE DIETRO.", "VERO.")]),
  ])

def costruisci():
    base = os.path.join(RADICE, "missione-casa")
    persone = open(os.path.join(base, "persone.js"), encoding="utf-8").read().rstrip().rstrip("};").rstrip().rstrip(",")
    altre = open(os.path.join(RADICE, "missione-lavoro", "persone.js"), encoding="utf-8").read()
    altre = altre[altre.index("{") + 1:].rstrip().rstrip(";").rstrip().rstrip("}")
    tutte = persone + ",\n" + altre.strip().rstrip(",") + ",\n" + OPERATORI_JS + "\n};\n"
    for nome, g in GIOCHI.items():
        assert "".join(st["lettera"] for st in g["stanze"]) == g["parolaSegreta"], nome
        d = os.path.join(RADICE, "missione-" + nome)
        os.makedirs(d, exist_ok=True)
        for f in ("gioco.js", "stile.css"):
            shutil.copy(os.path.join(base, f), d)
        open(os.path.join(d, "persone.js"), "w", encoding="utf-8").write(tutte)
        dati = dict(g, sito="https://italianol2sai.github.io/", chiaveSalva="missione-%s-v1" % nome)
        open(os.path.join(d, "domande.js"), "w", encoding="utf-8").write(
            "// Contenuti del gioco «%s» (generati da _strumenti/missioni.py: modificare lì).\nwindow.MISSIONE = %s;\n" % (g["titolo"], json.dumps(dati, ensure_ascii=False, indent=1)))
        html = open(os.path.join(base, "index.html"), encoding="utf-8").read()
        parole = g["titolo"].split(" ", 1)
        html = html.replace("<title>MISSIONE CASA</title>", "<title>%s</title>" % g["titolo"]).replace("MISSIONE<br>CASA", "%s<br>%s" % tuple(parole))
        open(os.path.join(d, "index.html"), "w", encoding="utf-8").write(html)
        print("scritto", d)

if __name__ == "__main__":
    costruisci()
