"""Seconda parte delle pagine dal confronto con i sillabi (2026-10-28).
Primi passi: LEGGO I CARTELLI, IN CLASSE, SUONI DIFFICILI.
A1: QUESTO E QUELLO, C'È / CI SONO, MI PIACE, PRENDO L'AUTOBUS, CHE TEMPO FA?, AL TELEFONO.
Tutto in STAMPATELLO MAIUSCOLO. Testi scritti per il sito."""
from genera import eq, has, all_
from unita_primi import cover, slide, cards, table, nota, dialogo, end

def say(w):
    """Pulsante 🔊: la voce del computer legge la parola (negli esercizi)."""
    return ('<button type="button" class="say" onclick="var u=new SpeechSynthesisUtterance(\'%s\');u.lang=\'it-IT\';'
            'speechSynthesis.cancel();speechSynthesis.speak(u)">🔊</button> ' % w.replace("'", "\\'"))

def esempi(rows):
    """Parole con il pulsante 🔊 nelle slide."""
    return '    <div class="mondo">\n' + "".join(
        '      <div data-say="%s">%s 🔊<span>%s</span></div>\n' % (w, w, s) for w, s in rows) + "    </div>"

CARTELLO_CSS = """
  .cartelli{display:grid; grid-template-columns:repeat(3,1fr); gap:16px;}
  .cartelli div{border-radius:14px; padding:16px; text-align:center; font-weight:bold; font-size:1.5rem; color:#fff; box-shadow:0 4px 10px rgba(0,0,0,.15); display:flex; flex-direction:column; gap:6px; justify-content:center; min-height:110px;}
  .cartelli span{font-size:1rem; font-weight:normal; opacity:.95;}
  .verde{background:#2E9E5B;} .rosso{background:#D0473F;} .blu{background:#2D6CB5;} .giallo{background:#F2B705; color:#3B2410 !important;} .grigio{background:#5b6b7b;}
  @media (max-width:900px){ .cartelli{grid-template-columns:1fr 1fr;} .cartelli div{font-size:1.1rem; min-height:90px;} }"""

def cartelli(items):
    return '    <div class="cartelli">\n' + "".join(
        '      <div class="%s">%s<span>%s</span></div>\n' % i for i in items) + "    </div>"


# Foto vere di Bari da Wikimedia Commons (scelte il 2026-10-28). CC BY-SA: autore e licenza sotto ogni foto.
BYSA = '<a href="https://creativecommons.org/licenses/by-sa/4.0/" target="_blank" rel="noopener">CC BY-SA 4.0</a>'
FOTO = [  # file, che cosa dice il cartello, autore, pagina Commons
    ("fermata-autobus-torre-a-mare", "LA FERMATA DELL'AUTOBUS (A SINISTRA) E I SEGNALI STRADALI", "Claudio.Montanaro", "Fermata_del_bus_Via_Bari_a_Torre_a_Mare.jpg"),
    ("farmacia-insegna", "LA CROCE VERDE: FARMACIA", "Lilli adnil", "Insegna_farmacia.jpg"),
    ("autobus-amtab", "L'AUTOBUS AMTAB: IL NUMERO DELLA LINEA E LA DESTINAZIONE", "Chabe01", "Bus_AMTAB_Ligne_2_Piazza_Giuseppe_Garibaldi_-_Bari_(IT75)_-_2026-10-25_-_1.jpg"),
    ("stazione-informazioni-biglietteria", "STAZIONE FERROVIARIA · INFORMAZIONI · BIGLIETTERIA", "Chabe01", "Accès_Gare_Aeroporto_Aéroport_Bari_Palese_-_Bari_(IT75)_-_2026-10-25_-_2.jpg"),
    ("treni-terminal-bus-taxi-uscita", "BARI CENTRALE: TRENI · TERMINAL BUS · USCITA · TAXI", "Chabe01", "Accès_Gare_Bari_Centrale_Via_Giuseppe_Capruzzi_-_Bari_(IT75)_-_2026-10-25_-_1.jpg"),
    ("binari-uscita", "BARI CENTRALE: BINARI 3-12 · USCITA VIA CAPRUZZI", "Chabe01", "Gare_Bari_Centrale_-_Bari_(IT75)_-_2026-10-25_-_6.jpg"),
    ("parcheggio-bike-sharing", "BIKE SHARING · P RISERVATO: QUI SI LASCIANO LE BICI", "Chabe01", "Panneau_Parking_Vélos_Partage_Via_Giovanni_Laricchia_-_Bari_(IT75)_-_2026-10-25_-_1.jpg"),
    ("targa-via-sparano", "IL NOME DELLA STRADA: VIA SPARANO DA BARI", "Chabe01", "Plaque_Via_Sparano_Bari_-_Bari_(IT75)_-_2026-10-25_-_1.jpg"),
]

def credito(autore, pagina):
    return ('FOTO: <a href="https://commons.wikimedia.org/wiki/File:%s" target="_blank" rel="noopener">%s</a>, Wikimedia Commons, %s'
            % (pagina.replace(" ", "_"), autore, BYSA))

def foto_slide(items):
    return '    <div class="foto">\n' + "".join(
        '      <figure><img src="img/%s.jpg" alt="%s" loading="lazy"><figcaption><b>%s</b><small>%s</small></figcaption></figure>\n'
        % (f, t, t, credito(a, pg)) for f, t, a, pg in items) + "    </div>"

FOTO_CSS = """
  .foto{display:grid; grid-template-columns:1fr 1fr; gap:16px;}
  .foto figure{background:#fff; border:3px solid #e3edf8; border-radius:16px; overflow:hidden; margin:0;}
  .foto img{width:100%; height:260px; object-fit:contain; background:#f1ece4; display:block;}
  .foto figcaption{padding:10px 12px; font-size:1.2rem; display:flex; flex-direction:column; gap:4px;}
  .foto small{font-size:.75rem; text-transform:none; letter-spacing:0; color:#7a6a5a;}
  .foto small a{color:inherit;}
  @media (max-width:900px){ .foto{grid-template-columns:1fr;} .foto img{height:200px;} .foto figcaption{font-size:1rem;} }"""

# =====================================================================
# LEGGO I CARTELLI (A0)
# =====================================================================
CARTELLI_SLIDE = [
    cover("🪧", "LEGGO I CARTELLI", "APERTO? CHIUSO? VIETATO?", "ENTRATA E USCITA &bull; VIETATO &bull; ATTENZIONE &bull; IN CITTÀ"),
    slide("CHE COSA IMPARIAMO?", cards([
        ("🚪", "ENTRARE E USCIRE", "ENTRATA, USCITA, SPINGERE, TIRARE"), ("🕘", "APERTO O CHIUSO", "APERTO, CHIUSO, ORARIO"),
        ("🚫", "VIETATO", "VIETATO FUMARE, VIETATO ENTRARE"), ("🏙️", "IN CITTÀ", "FERMATA, BIGLIETTERIA, FARMACIA")])),
    slide("🚪 ENTRARE E USCIRE", cartelli([
        ("verde", "ENTRATA", "DI QUI ENTRO"), ("verde", "USCITA", "DI QUI ESCO"), ("verde", "USCITA DI EMERGENZA", "PER USCIRE SE C'È PERICOLO"),
        ("blu", "SPINGERE", "SPINGO LA PORTA ➡️"), ("blu", "TIRARE", "TIRO LA PORTA ⬅️"), ("grigio", "PRIVATO", "NON POSSO ENTRARE")])),
    slide("🕘 APERTO O CHIUSO?", cartelli([
        ("verde", "APERTO", "POSSO ENTRARE"), ("rosso", "CHIUSO", "NON POSSO ENTRARE"), ("grigio", "ORARIO", "QUANDO È APERTO"),
        ("rosso", "CHIUSO PER FERIE", "CHIUSO PER LE VACANZE"), ("grigio", "TORNO SUBITO", "ASPETTA UN MOMENTO"), ("verde", "APERTO 24 ORE", "SEMPRE APERTO")])),
    slide("🚫 VIETATO = NON PUOI", cartelli([
        ("rosso", "🚭 VIETATO FUMARE", "NON PUOI FUMARE"), ("rosso", "⛔ VIETATO L'INGRESSO", "NON PUOI ENTRARE"),
        ("rosso", "🅿️ DIVIETO DI SOSTA", "NON PUOI LASCIARE LA MACCHINA"), ("rosso", "📵 SPEGNERE IL CELLULARE", "NON PUOI USARE IL TELEFONO"),
        ("rosso", "🤫 SILENZIO", "NON PARLARE FORTE"), ("rosso", "🐕 NON SI ENTRA CON I CANI", "IL CANE NON PUÒ ENTRARE")])),
    slide("⚠️ ATTENZIONE!", cartelli([
        ("giallo", "⚠️ ATTENZIONE", "FAI ATTENZIONE!"), ("giallo", "⚡ PERICOLO", "QUI È PERICOLOSO"),
        ("giallo", "🧽 PAVIMENTO BAGNATO", "PUOI CADERE"), ("giallo", "🚧 LAVORI IN CORSO", "QUI LAVORANO"),
        ("giallo", "❌ GUASTO", "NON FUNZIONA"), ("giallo", "🛗 FUORI SERVIZIO", "L'ASCENSORE NON FUNZIONA")])),
    slide("🏙️ IN CITTÀ", cartelli([
        ("blu", "🚌 FERMATA", "QUI PASSA L'AUTOBUS"), ("blu", "🎫 BIGLIETTERIA", "QUI COMPRO IL BIGLIETTO"),
        ("verde", "➕ FARMACIA", "LE MEDICINE"), ("rosso", "🚑 PRONTO SOCCORSO", "IN OSPEDALE, PER LE EMERGENZE"),
        ("giallo", "✉️ POSTE ITALIANE", "L'UFFICIO POSTALE"), ("grigio", "🚻 BAGNI · UOMINI · DONNE", "LA TOILETTE")])),
    slide("🛍️ NEI NEGOZI", cartelli([
        ("blu", "CASSA", "QUI PAGO"), ("rosso", "SALDI", "I PREZZI SONO PIÙ BASSI"), ("giallo", "OFFERTA", "OGGI COSTA MENO"),
        ("grigio", "PROVE", "IL CAMERINO: PROVO I VESTITI"), ("verde", "SI ACCETTANO CARTE", "POSSO PAGARE CON LA CARTA"), ("grigio", "AFFITTASI", "LA CASA È IN AFFITTO")])),
    slide("📸 I CARTELLI DI BARI (1)", foto_slide(FOTO[:4])),
    slide("📸 I CARTELLI DI BARI (2)", foto_slide(FOTO[4:])),
    slide("📄 LEGGO UN AVVISO", '    <div class="twocol2">\n    <div class="nota" style="background:#fff; border-color:var(--teal)">'
          "📢 <b>AVVISO</b><br>OGGI L'UFFICIO È <b>CHIUSO</b>.<br>APRIAMO <b>DOMANI ALLE 9</b>.<br>GRAZIE.</div>\n" +
          nota("OGGI POSSO ANDARE IN UFFICIO? <b>NO</b>.<br>QUANDO POSSO ANDARE? <b>DOMANI, ALLE NOVE</b>.", "") + "\n    </div>"),
    end("ORA SAI LEGGERE I CARTELLI!"),
]

CARTELLI = {
 "title": "🪧 Leggo i cartelli · Esercizi",
 "store": "cartelli",
 "upper": True,
 "sections": [
  {"part": "Che cosa vuol dire?"},
  {"id": "e1", "title": "1 · Che cosa vuol dire il cartello?", "short": "1 · Il cartello", "type": "select",
   "opts": ["NON PUOI FUMARE", "NON PUOI ENTRARE", "DI QUI ESCO", "POSSO ENTRARE, È APERTO", "NON FUNZIONA", "QUI COMPRO IL BIGLIETTO"],
   "items": [{"q": q} for q in ["🪧 1. VIETATO FUMARE", "🪧 2. USCITA", "🪧 3. APERTO", "🪧 4. GUASTO",
                                 "🪧 5. VIETATO L'INGRESSO", "🪧 6. BIGLIETTERIA"]],
   "k": [eq(a) for a in ["NON PUOI FUMARE", "DI QUI ESCO", "POSSO ENTRARE, È APERTO", "NON FUNZIONA", "NON PUOI ENTRARE", "QUI COMPRO IL BIGLIETTO"]]},
  {"id": "e2", "title": "2 · Scrivi il contrario", "short": "2 · Il contrario", "type": "text", "w": "m",
   "cons": "ESEMPIO: APERTO → CHIUSO",
   "items": [{"q": q} for q in ["1. ENTRATA →", "2. SPINGERE →", "3. UOMINI →", "4. CHIUSO →"]],
   "k": [eq("uscita"), eq("tirare"), eq("donne"), eq("aperto")]},
  {"id": "e3", "title": "3 · Posso o non posso?", "short": "3 · Posso?", "type": "choice",
   "opts": ["POSSO", "NON POSSO"], "full": True,
   "items": [{"q": q} for q in ["1. 🚭 VIETATO FUMARE. … FUMARE.", "2. ✅ APERTO. … ENTRARE.", "3. 📵 SPEGNERE IL CELLULARE. … TELEFONARE.",
                                 "4. 💳 SI ACCETTANO CARTE. … PAGARE CON LA CARTA.", "5. 🛗 FUORI SERVIZIO. … PRENDERE L'ASCENSORE.",
                                 "6. 🅿️ DIVIETO DI SOSTA. … LASCIARE QUI LA MACCHINA."]],
   "k": [eq(a) for a in ["NON POSSO", "POSSO", "NON POSSO", "POSSO", "NON POSSO", "NON POSSO"]]},

  {"part": "Dove vado?"},
  {"id": "e4", "title": "4 · Quale cartello cerchi?", "short": "4 · Dove vado", "type": "select",
   "opts": ["FERMATA", "FARMACIA", "PRONTO SOCCORSO", "CASSA", "BAGNI", "POSTE ITALIANE"],
   "items": [{"q": q} for q in ["1. VOGLIO PRENDERE L'AUTOBUS.", "2. VOGLIO PAGARE.", "3. MI SERVE UNA MEDICINA.",
                                 "4. DEVO SPEDIRE UNA LETTERA.", "5. STO MALE, È UN'EMERGENZA.", "6. CERCO LA TOILETTE."]],
   "k": [eq(a) for a in ["FERMATA", "CASSA", "FARMACIA", "POSTE ITALIANE", "PRONTO SOCCORSO", "BAGNI"]]},
  {"id": "e5", "title": "5 · Leggi l'avviso: vero o falso?", "short": "5 · L'avviso", "type": "choice",
   "opts": ["VERO", "FALSO"], "full": True,
   "info": "📢 <b>AVVISO</b><br>IL NEGOZIO È <b>CHIUSO PER FERIE</b><br>DAL 10 AL 20 AGOSTO.<br>RIAPRIAMO IL 21 AGOSTO ALLE 9:00.",
   "items": [{"q": q} for q in ["1. IL 15 AGOSTO IL NEGOZIO È APERTO.", "2. IL NEGOZIO È CHIUSO PER LE VACANZE.",
                                 "3. IL NEGOZIO RIAPRE IL 21 AGOSTO.", "4. IL 21 AGOSTO APRE ALLE 10."]],
   "k": [eq(a) for a in ["FALSO", "VERO", "VERO", "FALSO"]]},
  {"part": "I cartelli di Bari"},
  {"id": "e7", "title": "6 · Guarda la foto: dove sei?", "short": "6 · Le foto di Bari", "type": "select",
   "cons": "SONO FOTO VERE DI BARI. LEGGI IL CARTELLO E SCEGLI.",
   "opts": ["ALLA FERMATA DELL'AUTOBUS", "IN FARMACIA", "IN STAZIONE", "IN VIA SPARANO", "AL PARCHEGGIO DELLE BICI"],
   "items": [{"q": '<img src="img/%s.jpg" alt="" style="width:100%%;max-width:420px;border-radius:12px;display:block;margin-bottom:6px">'
                   '<small style="text-transform:none;font-size:.75rem;color:#7a6a5a">%s</small><br>%d.' % (FOTO[i][0], credito(FOTO[i][2], FOTO[i][3]), n + 1)}
             for n, i in enumerate([1, 5, 7, 6, 3])],
   "k": [eq(a) for a in ["IN FARMACIA", "IN STAZIONE", "IN VIA SPARANO", "AL PARCHEGGIO DELLE BICI", "IN STAZIONE"]]},
  {"id": "e6", "title": "7 ✎ · I cartelli della tua città", "type": "free", "rows": 3,
   "items": ["SCRIVI 3 CARTELLI CHE VEDI PER STRADA, A SCUOLA O AL LAVORO. CHE COSA VOGLIONO DIRE?"]},
 ]
}

# =====================================================================
# IN CLASSE: NON HO CAPITO (A0)
# =====================================================================
CLASSE_SLIDE = [
    cover("🏫", "IN CLASSE", "NON HO CAPITO. PUÒ RIPETERE, PER FAVORE?", "GLI OGGETTI &bull; L'INSEGNANTE DICE &bull; IO CHIEDO"),
    slide("CHE COSA IMPARIAMO?", cards([
        ("✏️", "GLI OGGETTI DELLA CLASSE", "LA PENNA, IL QUADERNO, IL LIBRO"), ("👩‍🏫", "L'INSEGNANTE DICE", "ASCOLTATE! SCRIVETE! LEGGETE!"),
        ("🙋", "IO CHIEDO", "NON HO CAPITO. PUÒ RIPETERE?"), ("🗣️", "LE PAROLE NUOVE", "COME SI DICE…? CHE COSA VUOL DIRE…?")])),
    slide("✏️ GLI OGGETTI DELLA CLASSE", cards([
        ("🖊️", "LA PENNA", ""), ("✏️", "LA MATITA", ""), ("🧽", "LA GOMMA", ""), ("📓", "IL QUADERNO", ""),
        ("📕", "IL LIBRO", ""), ("📄", "IL FOGLIO", ""), ("🟩", "LA LAVAGNA", ""), ("🪑", "LA SEDIA", ""), ("🎒", "LO ZAINO", "")], cols="g3")),
    slide("👩‍🏫 L'INSEGNANTE DICE", table([
        ["👂 ASCOLTATE!", "📖 LEGGETE!"], ["✍️ SCRIVETE!", "🔁 RIPETETE!"], ["📖 APRITE IL LIBRO!", "📕 CHIUDETE IL LIBRO!"],
        ["👀 GUARDATE LA LAVAGNA!", "👫 LAVORATE IN COPPIA!"], ["✔️ CONTROLLATE!", "🤫 SILENZIO, PER FAVORE!"]])),
    slide("🙋 IO CHIEDO", cards([
        ("🤔", "NON HO CAPITO.", ""), ("🔁", "PUÒ RIPETERE, PER FAVORE?", ""), ("🐢", "PIÙ PIANO, PER FAVORE.", ""),
        ("🔤", "COME SI SCRIVE?", ""), ("❓", "CHE COSA VUOL DIRE «AFFITTO»?", ""), ("🌍", "COME SI DICE «WATER» IN ITALIANO?", "")])),
    slide("🙋 ALTRE FRASI UTILI", cards([
        ("🚻", "POSSO ANDARE IN BAGNO?", ""), ("⏰", "SCUSI, SONO IN RITARDO.", ""), ("✋", "HO UNA DOMANDA.", ""),
        ("🖊️", "MI PRESTI UNA PENNA?", ""), ("✅", "HO FINITO!", ""), ("🙏", "GRAZIE!", "")])),
    slide("🗣️ IN CLASSE", dialogo([
        ("*INSEGNANTE", "BUONGIORNO! APRITE IL LIBRO A PAGINA 10."), ("STUDENTE", "SCUSI, NON HO CAPITO. PUÒ RIPETERE?"),
        ("*INSEGNANTE", "CERTO! APRITE IL LIBRO A PAGINA DIECI."), ("STUDENTE", "GRAZIE. CHE COSA VUOL DIRE «PAGINA»?"),
        ("*INSEGNANTE", "È QUESTA! 📄"), ("STUDENTE", "AH, HO CAPITO!")])),
    slide("📌 RICORDA", table([
        ["CON L'INSEGNANTE (LEI)", "PUÒ RIPETERE? · SCUSI"], ["CON UN COMPAGNO (TU)", "PUOI RIPETERE? · SCUSA"]],
        head=["CON CHI PARLO?", "CHE COSA DICO?"]) + "\n" +
        nota("NON HO CAPITO? <b>CHIEDO</b>! FARE DOMANDE È IL MODO MIGLIORE PER IMPARARE. 💪")),
    end("ORA SAI PARLARE IN CLASSE!"),
]

CLASSE = {
 "title": "🏫 In classe · Esercizi",
 "store": "in-classe",
 "upper": True,
 "sections": [
  {"part": "Gli oggetti"},
  {"id": "e1", "title": "1 · Che cos'è?", "short": "1 · Gli oggetti", "type": "select",
   "opts": ["LA PENNA", "LA MATITA", "LA GOMMA", "IL QUADERNO", "IL LIBRO", "LA SEDIA", "LO ZAINO"],
   "items": [{"q": q} for q in ["🖊️ 1.", "📓 2.", "🎒 3.", "✏️ 4.", "🪑 5.", "📕 6.", "🧽 7."]],
   "k": [eq(a) for a in ["LA PENNA", "IL QUADERNO", "LO ZAINO", "LA MATITA", "LA SEDIA", "IL LIBRO", "LA GOMMA"]]},
  {"part": "L'insegnante dice"},
  {"id": "e2", "title": "2 · Che cosa fai?", "short": "2 · L'insegnante dice", "type": "select",
   "opts": ["👂 ASCOLTO", "📖 LEGGO", "✍️ SCRIVO", "🔁 RIPETO", "👫 LAVORO CON UN COMPAGNO"],
   "items": [{"q": q} for q in ["1. «SCRIVETE!»", "2. «RIPETETE!»", "3. «ASCOLTATE!»", "4. «LAVORATE IN COPPIA!»", "5. «LEGGETE!»"]],
   "k": [eq(a) for a in ["✍️ SCRIVO", "🔁 RIPETO", "👂 ASCOLTO", "👫 LAVORO CON UN COMPAGNO", "📖 LEGGO"]]},
  {"part": "Io chiedo"},
  {"id": "e3", "title": "3 · Che cosa dici?", "short": "3 · Che cosa dici", "type": "select",
   "opts": ["NON HO CAPITO. PUÒ RIPETERE?", "PIÙ PIANO, PER FAVORE.", "CHE COSA VUOL DIRE?", "COME SI SCRIVE?", "POSSO ANDARE IN BAGNO?", "SCUSI, SONO IN RITARDO."],
   "items": [{"q": q} for q in ["1. L'INSEGNANTE PARLA TROPPO VELOCE.", "2. ARRIVI ALLE 9:20. LA LEZIONE COMINCIA ALLE 9.",
                                 "3. NON CONOSCI UNA PAROLA.", "4. NON HAI CAPITO LA FRASE.", "5. DEVI ANDARE ALLA TOILETTE.",
                                 "6. NON SAI SCRIVERE UNA PAROLA."]],
   "k": [eq(a) for a in ["PIÙ PIANO, PER FAVORE.", "SCUSI, SONO IN RITARDO.", "CHE COSA VUOL DIRE?", "NON HO CAPITO. PUÒ RIPETERE?",
                         "POSSO ANDARE IN BAGNO?", "COME SI SCRIVE?"]]},
  {"id": "e4", "title": "4 · Chi parla?", "short": "4 · Chi parla", "type": "choice",
   "opts": ["L'INSEGNANTE", "LO STUDENTE"], "full": True,
   "items": [{"q": q} for q in ["1. APRITE IL LIBRO!", "2. NON HO CAPITO.", "3. RIPETETE!", "4. HO UNA DOMANDA.", "5. SILENZIO, PER FAVORE!", "6. HO FINITO!"]],
   "k": [eq(a) for a in ["L'INSEGNANTE", "LO STUDENTE", "L'INSEGNANTE", "LO STUDENTE", "L'INSEGNANTE", "LO STUDENTE"]]},
  {"id": "e5", "title": "5 · Completa il dialogo", "short": "5 · Il dialogo", "type": "cloze",
   "bank": "CAPITO · RIPETERE · VUOL · GRAZIE",
   "parts": ["INSEGNANTE: SCRIVETE LA DATA SUL QUADERNO.<br>STUDENTE: SCUSI, NON HO ", {}, ". PUÒ ", {},
             "?<br>INSEGNANTE: SCRIVETE LA DATA. OGGI È 28 OTTOBRE.<br>STUDENTE: CHE COSA ", {}, " DIRE «DATA»?<br>INSEGNANTE: IL GIORNO E IL MESE.<br>STUDENTE: AH, ", {}, "!"],
   "k": [eq("capito"), eq("ripetere"), eq("vuol", "vuole"), eq("grazie")]},
  {"id": "e6", "title": "6 🎤 · Chiedi all'insegnante", "type": "record",
   "items": ["DI': «NON HO CAPITO. PUÒ RIPETERE, PER FAVORE?» E «COME SI DICE … IN ITALIANO?» CON UNA PAROLA DELLA TUA LINGUA."]},
 ]
}

# =====================================================================
# SUONI DIFFICILI (A0)
# =====================================================================
SUONI_CSS = """
  [data-say]{cursor:pointer;}
  .regola{display:grid; grid-template-columns:1fr 1fr; gap:16px; margin-bottom:14px;}
  .regola div{background:#fff; border:4px solid var(--teal); border-radius:16px; padding:14px; text-align:center; font-size:2rem; font-weight:bold; color:var(--blu);}
  .regola div span{display:block; font-size:1.1rem; color:var(--blu-scuro); font-weight:normal;}
  @media (max-width:900px){ .regola div{font-size:1.4rem;} .regola div span{font-size:.95rem;} }"""

def regola(a, sa, b, sb):
    return '    <div class="regola"><div>%s<span>%s</span></div><div>%s<span>%s</span></div></div>' % (a, sa, b, sb)

SUONI_SLIDE = [
    cover("👂", "SUONI DIFFICILI", "CHE, CHI, GHE, GHI, GN, GLI, SC", "ASCOLTA &bull; LEGGI &bull; RIPETI"),
    slide("👂 COME SI USA QUESTA PRESENTAZIONE", nota("TOCCA UNA PAROLA CON 🔊: IL TELEFONO O IL COMPUTER LA LEGGE.<br>ASCOLTA E RIPETI A VOCE ALTA. 🗣️", "")),
    slide("C DURA: CA, CO, CU, CHE, CHI", regola("CA · CO · CU", "COME «K»", "CHE · CHI", "COME «K» + E, I") + "\n" +
          esempi([("CASA", "🏠"), ("COSA", "❓"), ("CUORE", "❤️"), ("CHIAVE", "🔑"), ("PESCHE", "🍑"), ("ANCHE", "➕"), ("CHILO", "⚖️"), ("BANCHE", "🏦")])),
    slide("C DOLCE: CE, CI, CIA, CIO, CIU", regola("CE · CI", "COME «CIAO»", "CIA · CIO · CIU", "C + I + A, O, U") + "\n" +
          esempi([("CENA", "🍽️"), ("CINEMA", "🎬"), ("CIAO", "👋"), ("CIPOLLA", "🧅"), ("CAMICIA", "👔"), ("FACCIO", "💪"), ("DIECI", "🔟"), ("CIUCCIO", "🍼")])),
    slide("G DURA: GA, GO, GU, GHE, GHI", regola("GA · GO · GU", "COME «GATTO»", "GHE · GHI", "G + H + E, I") + "\n" +
          esempi([("GATTO", "🐈"), ("GONNA", "👗"), ("GUSTO", "😋"), ("SPAGHETTI", "🍝"), ("GHIACCIO", "🧊"), ("LUNGHE", "📏"), ("FUNGHI", "🍄"), ("LAGHI", "🏞️")])),
    slide("G DOLCE: GE, GI, GIA, GIO, GIU", regola("GE · GI", "COME «GELATO»", "GIA · GIO · GIU", "G + I + A, O, U") + "\n" +
          esempi([("GELATO", "🍦"), ("GIRO", "🔄"), ("GIALLO", "💛"), ("GIORNO", "☀️"), ("GIUGNO", "📅"), ("MANGIARE", "🍽️"), ("OGGI", "📍"), ("VALIGIA", "🧳")])),
    slide("GN E GLI", regola("GN", "LASAGNA", "GLI", "FIGLIO") + "\n" +
          esempi([("BAGNO", "🛁"), ("LASAGNA", "🍝"), ("SIGNORA", "👩"), ("GNOCCHI", "🥟"), ("FIGLIO", "👦"), ("MOGLIE", "👰"), ("AGLIO", "🧄"), ("FOGLIO", "📄")])),
    slide("SC: SCE, SCI, SCHE, SCHI", regola("SCE · SCI", "COME «SCIARPA»", "SCA · SCO · SCU · SCHE · SCHI", "COME «S» + «K»") + "\n" +
          esempi([("PESCE", "🐟"), ("SCIARPA", "🧣"), ("USCITA", "🚪"), ("SCENDERE", "⬇️"), ("SCUOLA", "🏫"), ("TASCA", "👖"), ("SCHIENA", "🔙"), ("SCHERMO", "🖥️")])),
    slide("QU", regola("QU", "Q + U + A, E, I, O", "CQU", "SOLO IN POCHE PAROLE") + "\n" +
          esempi([("QUADERNO", "📓"), ("QUATTRO", "4️⃣"), ("QUESTO", "👉"), ("QUANDO", "🕐"), ("QUI", "📍"), ("ACQUA", "💧")])),
    slide("📌 RICORDA", table([
        ["CA · CO · CU · <b>CHE · CHI</b>", "CASA · <b>CHIAVE</b>"], ["<b>CE · CI</b> · CIA · CIO · CIU", "<b>CENA</b> · CIAO"],
        ["GA · GO · GU · <b>GHE · GHI</b>", "GATTO · <b>SPAGHETTI</b>"], ["<b>GE · GI</b> · GIA · GIO · GIU", "<b>GELATO</b> · GIALLO"],
        ["GN · GLI", "BAGNO · FIGLIO"], ["SCE · SCI · <b>SCHE · SCHI</b>", "PESCE · <b>SCHIENA</b>"]], head=["IL SUONO", "LA PAROLA"])),
    end("ORA SAI LEGGERE I SUONI DIFFICILI!"),
]

SUONI = {
 "title": "👂 Suoni difficili · Esercizi",
 "store": "suoni",
 "upper": True,
 "sub": "Premi 🔊 per ascoltare la parola. Scegli le lettere giuste e premi «Controlla».",
 "sections": [
  {"part": "C o CH?"},
  {"id": "e1", "title": "1 · C o CH?", "short": "1 · C o CH", "type": "choice", "opts": ["C", "CH"],
   "cons": "ASCOLTA LA PAROLA. SCEGLI LE LETTERE CHE MANCANO.",
   "items": [{"q": say(w) + q} for w, q in [("chiave", "1. _ IAVE 🔑"), ("cena", "2. _ ENA 🍽️"), ("casa", "3. _ ASA 🏠"),
                                             ("anche", "4. AN _ E ➕"), ("cinema", "5. _ INEMA 🎬"), ("pesche", "6. PES _ E 🍑")]],
   "k": [eq(a) for a in ["CH", "C", "C", "CH", "C", "CH"]]},
  {"part": "G o GH?"},
  {"id": "e2", "title": "2 · G o GH?", "short": "2 · G o GH", "type": "choice", "opts": ["G", "GH"],
   "items": [{"q": say(w) + q} for w, q in [("spaghetti", "1. SPA _ ETTI 🍝"), ("gelato", "2. _ ELATO 🍦"), ("ghiaccio", "3. _ IACCIO 🧊"),
                                             ("giallo", "4. _ IALLO 💛"), ("funghi", "5. FUN _ I 🍄"), ("oggi", "6. OG _ I 📍")]],
   "k": [eq(a) for a in ["GH", "G", "GH", "G", "GH", "G"]]},
  {"part": "GN, GLI, SC"},
  {"id": "e3", "title": "3 · GN o GLI?", "short": "3 · GN o GLI", "type": "choice", "opts": ["GN", "GLI"],
   "items": [{"q": say(w) + q} for w, q in [("bagno", "1. BA _ O 🛁"), ("figlio", "2. FI _ O 👦"), ("lasagna", "3. LASA _ A 🍝"),
                                             ("aglio", "4. A _ O 🧄"), ("signora", "5. SI _ ORA 👩"), ("moglie", "6. MO _ E 👰")]],
   "k": [eq(a) for a in ["GN", "GLI", "GN", "GLI", "GN", "GLI"]]},
  {"id": "e4", "title": "4 · SC o SCH?", "short": "4 · SC o SCH", "type": "choice", "opts": ["SC", "SCH"],
   "items": [{"q": say(w) + q} for w, q in [("pesce", "1. PE _ E 🐟"), ("schiena", "2. _ IENA 🔙"), ("sciarpa", "3. _ IARPA 🧣"),
                                             ("schermo", "4. _ ERMO 🖥️"), ("uscita", "5. U _ ITA 🚪")]],
   "k": [eq(a) for a in ["SC", "SCH", "SC", "SCH", "SC"]]},
  {"part": "Scrivi"},
  {"id": "e5", "title": "5 · Ascolta e scrivi la parola", "short": "5 · Ascolta e scrivi", "type": "text", "w": "m",
   "items": [{"q": say(w) + "%d." % (i + 1)} for i, w in enumerate(["chiave", "giorno", "bagno", "figlio", "pesce", "quattro"])],
   "k": [eq(w) for w in ["chiave", "giorno", "bagno", "figlio", "pesce", "quattro"]]},
  {"id": "e6", "title": "6 🎤 · Leggi a voce alta", "type": "record",
   "items": ["LEGGI: CASA, CHIAVE, CENA, GATTO, SPAGHETTI, GELATO, BAGNO, FIGLIO, PESCE, SCUOLA."]},
 ]
}

# =====================================================================
# QUESTO E QUELLO (A1)
# =====================================================================
QUESTO_SLIDE = [
    cover("👉", "QUESTO E QUELLO", "QUESTA BORSA È MIA. QUELLA È TUA.", "VICINO &bull; LONTANO"),
    slide("👉 VICINO O LONTANO?", cards([
        ("👉📕", "QUESTO", "È VICINO A ME: QUESTO LIBRO"), ("👉 &nbsp; &nbsp; &nbsp; 📕", "QUELLO", "È LONTANO DA ME: QUEL LIBRO")])),
    slide("👉 QUESTO: VICINO A ME", table([
        ["QUESTO LIBRO", "QUESTI LIBRI"], ["QUESTA CASA", "QUESTE CASE"]], head=["UNO", "DUE O PIÙ"]) + "\n" +
        nota("QUESTO <b>-O</b> · QUESTA <b>-A</b> · QUESTI <b>-I</b> · QUESTE <b>-E</b><br>COME GLI AGGETTIVI: ROSSO, ROSSA, ROSSI, ROSSE.")),
    slide("👉 QUELLO: LONTANO DA ME", table([
        ["IL LIBRO", "<b>QUEL</b> LIBRO", "I LIBRI", "<b>QUEI</b> LIBRI"], ["LO ZAINO", "<b>QUELLO</b> ZAINO", "GLI ZAINI", "<b>QUEGLI</b> ZAINI"],
        ["L'ALBERO", "<b>QUELL'</b>ALBERO", "GLI ALBERI", "<b>QUEGLI</b> ALBERI"], ["LA CASA", "<b>QUELLA</b> CASA", "LE CASE", "<b>QUELLE</b> CASE"]],
        head=["ARTICOLO", "UNO", "ARTICOLO", "DUE O PIÙ"]) + "\n" +
        nota("QUELLO CAMBIA COME L'ARTICOLO: IL → QUEL, LO → QUELLO, I → QUEI, GLI → QUEGLI, LA → QUELLA, LE → QUELLE.")),
    slide("🗣️ AL NEGOZIO", dialogo([
        ("CLIENTE", "QUANTO COSTA <b>QUESTA</b> GIACCA?"), ("*COMMESSA", "60 EURO."), ("CLIENTE", "E <b>QUELLA</b> GIACCA BLU?"),
        ("*COMMESSA", "<b>QUELLA</b> COSTA 45 EURO."), ("CLIENTE", "POSSO PROVARE <b>QUEI</b> PANTALONI?"), ("*COMMESSA", "CERTO! ECCO.")])),
    slide("📌 SENZA IL NOME", dialogo([("DOMANDA", "QUALE BORSA È TUA?"), ("*RISPOSTA", "<b>QUESTA</b>. E <b>QUELLA</b> È DI MARTA.")]) + "\n" +
          nota("SENZA IL NOME DICO: QUESTO, QUESTA, QUESTI, QUESTE · QUELLO, QUELLA, QUELLI, QUELLE.")),
    end("ORA SAI USARE QUESTO E QUELLO!"),
]

QUESTO = {
 "title": "👉 Questo e quello · Esercizi",
 "store": "questo-quello",
 "upper": True,
 "sections": [
  {"part": "Questo"},
  {"id": "e1", "title": "1 · QUESTO, QUESTA, QUESTI o QUESTE?", "short": "1 · Questo", "type": "choice",
   "opts": ["QUESTO", "QUESTA", "QUESTI", "QUESTE"],
   "items": [{"q": q} for q in ["1. … PENNA", "2. … QUADERNO", "3. … SCARPE", "4. … LIBRI", "5. … CASA", "6. … PANTALONI"]],
   "k": [eq(a) for a in ["QUESTA", "QUESTO", "QUESTE", "QUESTI", "QUESTA", "QUESTI"]]},
  {"part": "Quello"},
  {"id": "e2", "title": "2 · Scegli la forma di QUELLO", "short": "2 · Quello", "type": "select",
   "opts": ["QUEL", "QUELLO", "QUELL'", "QUELLA", "QUEI", "QUEGLI", "QUELLE"],
   "cons": "PENSA ALL'ARTICOLO: IL LIBRO → QUEL LIBRO.",
   "items": [{"q": q} for q in ["1. (IL) … RAGAZZO", "2. (LA) … DONNA", "3. (I) … BAMBINI", "4. (LO) … ZAINO",
                                 "5. (LE) … SCARPE", "6. (GLI) … STUDENTI", "7. (L') … UFFICIO"]],
   "k": [eq(a) for a in ["QUEL", "QUELLA", "QUEI", "QUELLO", "QUELLE", "QUEGLI", "QUELL'"]]},
  {"part": "Vicino o lontano?"},
  {"id": "e3", "title": "3 · Vicino o lontano?", "short": "3 · Vicino o lontano", "type": "choice",
   "opts": ["VICINO 👉", "LONTANO 👉 · · ·"], "full": True,
   "items": [{"q": q} for q in ["1. QUESTA SEDIA È ROTTA.", "2. QUELLA MACCHINA È NUOVA.", "3. QUESTI LIBRI SONO MIEI.", "4. QUEL SIGNORE È IL DIRETTORE."]],
   "k": [eq("VICINO 👉"), eq("LONTANO 👉 · · ·"), eq("VICINO 👉"), eq("LONTANO 👉 · · ·")]},
  {"id": "e4", "title": "4 · Completa il dialogo", "short": "4 · Il dialogo", "type": "cloze",
   "bank": "QUESTA · QUELLA · QUESTI · QUEI",
   "parts": ["CLIENTE: QUANTO COSTA ", {}, " MAGLIETTA QUI?<br>COMMESSA: 15 EURO.<br>CLIENTE: E ", {}, " MAGLIETTA LÀ, IN VETRINA?<br>"
             "COMMESSA: 20 EURO.<br>CLIENTE: POSSO PROVARE ", {}, " JEANS QUI?<br>COMMESSA: SÌ. E ANCHE ", {}, " JEANS LÀ IN FONDO, SE VUOLE."],
   "k": [eq("questa"), eq("quella"), eq("questi"), eq("quei")]},
  {"id": "e5", "title": "5 ✎ · Nella tua stanza", "type": "free", "rows": 3,
   "items": ["GUARDA INTORNO A TE. SCRIVI 2 FRASI CON QUESTO/QUESTA E 2 CON QUELLO/QUELLA. ESEMPIO: QUESTO TELEFONO È MIO. QUELLA FINESTRA È APERTA."]},
 ]
}

# =====================================================================
# C'È / CI SONO (A1)
# =====================================================================
CE_SLIDE = [
    cover("🏠", "C'È / CI SONO", "NELLA MIA CASA C'È UNA CUCINA. CI SONO DUE CAMERE.", "UNO &bull; DUE O PIÙ &bull; DOMANDE"),
    slide("UNO O DUE?", cards([("1️⃣", "C'È", "+ UNA COSA<br>C'È UN TAVOLO."), ("🔢", "CI SONO", "+ DUE O PIÙ COSE<br>CI SONO TRE SEDIE.")])),
    slide("🏠 NELLA MIA CASA", dialogo([
        ("AMINA", "NELLA MIA CASA <b>C'È</b> UNA CUCINA."), ("AMINA", "<b>C'È</b> UN BAGNO."), ("AMINA", "<b>CI SONO</b> DUE CAMERE DA LETTO."),
        ("AMINA", "IN CUCINA <b>C'È</b> UN TAVOLO E <b>CI SONO</b> QUATTRO SEDIE.")])),
    slide("🏙️ NEL MIO QUARTIERE", dialogo([
        ("KARIM", "NEL MIO QUARTIERE <b>C'È</b> UN SUPERMERCATO."), ("KARIM", "<b>C'È</b> UNA FARMACIA."),
        ("KARIM", "<b>CI SONO</b> MOLTI BAR."), ("KARIM", "<b>NON C'È</b> UN OSPEDALE.")])),
    slide("❓ LE DOMANDE", dialogo([
        ("DOMANDA", "SCUSI, <b>C'È</b> UNA FARMACIA QUI VICINO?"), ("*RISPOSTA", "SÌ, <b>C'È</b>. È IN VIA CAVOUR."),
        ("DOMANDA", "<b>CI SONO</b> AUTOBUS PER LA STAZIONE?"), ("*RISPOSTA", "SÌ, <b>CI SONO</b>. / NO, <b>NON CI SONO</b>.")]) + "\n" +
        nota("NO → <b>NON</b> C'È · <b>NON</b> CI SONO")),
    slide("📌 RICORDA", table([["C'È", "UN, UNO, UNA, UN'", "C'È UNA FINESTRA."], ["CI SONO", "DUE, TRE… MOLTI, TANTI", "CI SONO DUE FINESTRE."],
                               ["NON C'È / NON CI SONO", "NO", "NON C'È IL BALCONE."]], head=["", "CON", "ESEMPIO"])),
    end("ORA SAI DIRE CHE COSA C'È!"),
]

CE = {
 "title": "🏠 C'è / ci sono · Esercizi",
 "store": "ce-ci-sono",
 "upper": True,
 "sections": [
  {"part": "C'è o ci sono?"},
  {"id": "e1", "title": "1 · C'È o CI SONO?", "short": "1 · C'è o ci sono", "type": "choice", "opts": ["C'È", "CI SONO"],
   "items": [{"q": q} for q in ["1. IN CUCINA … UN FRIGORIFERO.", "2. IN CLASSE … VENTI STUDENTI.", "3. IN VIA SPARANO … MOLTI NEGOZI.",
                                 "4. NEL BAGNO … UNA DOCCIA.", "5. SUL TAVOLO … DUE BICCHIERI.", "6. VICINO A CASA MIA … UN PARCO."]],
   "k": [eq(a) for a in ["C'È", "CI SONO", "CI SONO", "C'È", "CI SONO", "C'È"]]},
  {"id": "e2", "title": "2 · Rispondi NO", "short": "2 · Rispondi no", "type": "text", "w": "w",
   "cons": "ESEMPIO: C'È UN BALCONE? → NO, NON C'È.",
   "items": [{"q": q} for q in ["1. C'È UN ASCENSORE?", "2. CI SONO NEGOZI QUI VICINO?", "3. C'È LA LAVATRICE?", "4. CI SONO POSTI LIBERI?"]],
   "k": [eq("no non c'e"), eq("no non ci sono"), eq("no non c'e"), eq("no non ci sono")]},
  {"id": "e3", "title": "3 · Guarda la casa e completa", "short": "3 · La casa", "type": "cloze",
   "info": "🏠 2 CAMERE · 1 CUCINA · 1 BAGNO · 3 FINESTRE · ❌ BALCONE",
   "parts": ["NELLA CASA ", {}, " DUE CAMERE. ", {}, " UNA CUCINA E ", {}, " UN BAGNO. ", {}, " TRE FINESTRE. ", {}, " IL BALCONE."],
   "k": [eq("ci sono"), eq("c'e"), eq("c'e"), eq("ci sono"), eq("non c'e")]},
  {"id": "e4", "title": "4 ✎ · La tua casa e il tuo quartiere", "type": "free", "rows": 4,
   "items": ["CHE COSA C'È NELLA TUA CASA? E NEL TUO QUARTIERE? SCRIVI 4 FRASI CON C'È E CI SONO."]},
 ]
}

# =====================================================================
# MI PIACE (A1)
# =====================================================================
PIACE_SLIDE = [
    cover("😋", "MI PIACE, MI PIACCIONO", "MI PIACE LA PIZZA. MI PIACCIONO GLI SPAGHETTI.", "MI PIACE &bull; NON MI PIACE &bull; ANCHE A ME"),
    slide("😋 MI PIACE O MI PIACCIONO?", cards([
        ("🍕", "MI PIACE", "+ UNA COSA: MI PIACE LA PIZZA.<br>+ UN VERBO: MI PIACE CUCINARE."),
        ("🍝", "MI PIACCIONO", "+ DUE O PIÙ COSE: MI PIACCIONO GLI SPAGHETTI.")])),
    slide("😐 NON MI PIACE", dialogo([
        ("SARA", "MI PIACE IL CAFFÈ. ☕"), ("SARA", "<b>NON</b> MI PIACE IL TÈ."), ("SARA", "MI PIACCIONO I GATTI. 🐈"),
        ("SARA", "<b>NON</b> MI PIACCIONO I CANI GRANDI.")])),
    slide("👥 A CHI PIACE?", table([["(A ME)", "<b>MI</b> PIACE"], ["(A TE)", "<b>TI</b> PIACE"], ["(A LUI)", "<b>GLI</b> PIACE"],
                                    ["(A LEI)", "<b>LE</b> PIACE"], ["(A NOI)", "<b>CI</b> PIACE"], ["(A VOI)", "<b>VI</b> PIACE"], ["(A LORO)", "<b>GLI</b> PIACE"]]) + "\n" +
          dialogo([("DOMANDA", "TI PIACE BARI?"), ("*RISPOSTA", "SÌ, MI PIACE MOLTO!")])),
    slide("🤝 ANCHE A ME!", table([["MI PIACE IL MARE.", "😀 ANCHE A ME!", "😐 A ME NO."], ["NON MI PIACE IL FREDDO.", "😐 NEANCHE A ME.", "😀 A ME SÌ!"]],
                                  head=["IO DICO", "SONO D'ACCORDO", "NON SONO D'ACCORDO"])),
    slide("🗣️ UN DIALOGO", dialogo([
        ("LUCA", "TI PIACE LA CUCINA ITALIANA?"), ("*AMINA", "SÌ, MI PIACE MOLTO. MI PIACCIONO LE ORECCHIETTE."),
        ("LUCA", "ANCHE A ME! E TI PIACE IL PESCE CRUDO?"), ("*AMINA", "NO, NON MI PIACE."), ("LUCA", "A ME SÌ! 😄")])),
    end("ORA SAI DIRE CHE COSA TI PIACE!"),
]

PIACE = {
 "title": "😋 Mi piace · Esercizi",
 "store": "mi-piace",
 "upper": True,
 "sections": [
  {"part": "Piace o piacciono?"},
  {"id": "e1", "title": "1 · PIACE o PIACCIONO?", "short": "1 · Piace o piacciono", "type": "choice", "opts": ["PIACE", "PIACCIONO"],
   "items": [{"q": q} for q in ["1. MI … LA MUSICA.", "2. MI … I DOLCI.", "3. TI … BALLARE?", "4. NON MI … LE CIPOLLE.",
                                 "5. MI … IL CALCIO.", "6. TI … I FILM ITALIANI?"]],
   "k": [eq(a) for a in ["PIACE", "PIACCIONO", "PIACE", "PIACCIONO", "PIACE", "PIACCIONO"]]},
  {"id": "e2", "title": "2 · A chi piace?", "short": "2 · A chi piace", "type": "select",
   "opts": ["MI", "TI", "GLI", "LE", "CI"],
   "items": [{"q": q} for q in ["1. (A ME) … PIACE IL CAFFÈ.", "2. (A TE) … PIACE BARI?", "3. (A MARCO) … PIACE IL CALCIO.",
                                 "4. (A SARA) … PIACE LEGGERE.", "5. (A NOI) … PIACE IL MARE."]],
   "k": [eq(a) for a in ["MI", "TI", "GLI", "LE", "CI"]]},
  {"part": "Anche a me"},
  {"id": "e3", "title": "3 · Rispondi", "short": "3 · Anche a me", "type": "select",
   "opts": ["ANCHE A ME!", "A ME NO.", "NEANCHE A ME.", "A ME SÌ!"],
   "items": [{"q": q} for q in ["1. MI PIACE LA PIZZA. (😀 SEI D'ACCORDO)", "2. MI PIACE IL FREDDO. (😐 NON SEI D'ACCORDO)",
                                 "3. NON MI PIACE IL TRAFFICO. (😀 SEI D'ACCORDO)", "4. NON MI PIACE IL MARE. (😐 NON SEI D'ACCORDO)"]],
   "k": [eq(a) for a in ["ANCHE A ME!", "A ME NO.", "NEANCHE A ME.", "A ME SÌ!"]]},
  {"id": "e4", "title": "4 · Completa il dialogo", "short": "4 · Il dialogo", "type": "cloze",
   "bank": "TI · PIACE · PIACCIONO · ANCHE · NON",
   "parts": ["LUCA: ", {}, " PIACE CUCINARE?<br>AMINA: SÌ, MI ", {}, " MOLTO. MI ", {}, " I PIATTI DEL MIO PAESE.<br>LUCA: ", {},
             " A ME! E IL PEPERONCINO?<br>AMINA: NO, ", {}, " MI PIACE."],
   "k": [eq("ti"), eq("piace"), eq("piacciono"), eq("anche"), eq("non")]},
  {"id": "e5", "title": "5 ✎ · Che cosa ti piace?", "type": "free", "rows": 4,
   "items": ["SCRIVI 2 COSE CHE TI PIACCIONO E 2 COSE CHE NON TI PIACCIONO. ESEMPIO: MI PIACE IL MARE. NON MI PIACCIONO I RAGNI."]},
  {"id": "e6", "title": "6 🎤 · Parla", "type": "record", "items": ["DI' CHE COSA TI PIACE MANGIARE E CHE COSA NON TI PIACE."]},
 ]
}

# =====================================================================
# PRENDO L'AUTOBUS (A1)
# =====================================================================
AUTOBUS_SLIDE = [
    cover("🚌", "PRENDO L'AUTOBUS", "SCUSI, QUESTO AUTOBUS VA ALLA STAZIONE?", "I MEZZI &bull; IL BIGLIETTO &bull; LA FERMATA &bull; LE DOMANDE"),
    slide("CHE COSA IMPARIAMO?", cards([
        ("🚌", "I MEZZI", "L'AUTOBUS, IL TRENO, LA BICI"), ("🎫", "IL BIGLIETTO", "DOVE LO COMPRO? COME LO USO?"),
        ("🚏", "LA FERMATA", "SALIRE, SCENDERE, PRENOTARE"), ("❓", "LE DOMANDE", "A CHE ORA PASSA? DOVE DEVO SCENDERE?")])),
    slide("🚦 COME VAI?", table([["🚌 L'AUTOBUS", "VADO <b>IN</b> AUTOBUS"], ["🚆 IL TRENO", "VADO <b>IN</b> TRENO"], ["🚕 IL TAXI", "VADO <b>IN</b> TAXI"],
                                 ["🚲 LA BICI", "VADO <b>IN</b> BICI"], ["🚗 LA MACCHINA", "VADO <b>IN</b> MACCHINA"], ["🚶 A PIEDI", "VADO <b>A</b> PIEDI"]],
                                head=["IL MEZZO", "COME VAI?"]) + "\n" + nota("VADO <b>IN</b> AUTOBUS, MA VADO <b>A</b> PIEDI.")),
    slide("🎫 IL BIGLIETTO", cards([
        ("🏪", "DOVE LO COMPRO?", "IN TABACCHERIA, IN EDICOLA, ALLA BIGLIETTERIA O CON L'APP"),
        ("✅", "LO CONVALIDO", "QUANDO SALGO, METTO IL BIGLIETTO NELLA MACCHINETTA (O USO IL QR)"),
        ("👮", "IL CONTROLLORE", "CONTROLLA I BIGLIETTI. SENZA BIGLIETTO PAGO LA MULTA"),
        ("📅", "L'ABBONAMENTO", "UN BIGLIETTO PER UN MESE O PER UN ANNO")])),
    slide("🚏 ALLA FERMATA E SULL'AUTOBUS", cards([
        ("🚏", "LA FERMATA", "QUI ASPETTO L'AUTOBUS"), ("⬆️", "SALIRE", "ENTRO NELL'AUTOBUS"), ("⬇️", "SCENDERE", "ESCO DALL'AUTOBUS"),
        ("🔴", "PRENOTARE LA FERMATA", "PREMO IL PULSANTE PRIMA DI SCENDERE"), ("🔚", "IL CAPOLINEA", "L'ULTIMA FERMATA"),
        ("🕐", "L'ORARIO", "A CHE ORA PASSA L'AUTOBUS")], cols="g3")),
    slide("🗣️ ALLA FERMATA", dialogo([
        ("SAMIR", "SCUSI, QUESTO AUTOBUS VA ALLA STAZIONE CENTRALE?"), ("*SIGNORA", "NO, PER LA STAZIONE DEVE PRENDERE IL 12."),
        ("SAMIR", "A CHE ORA PASSA?"), ("*SIGNORA", "OGNI VENTI MINUTI. IL PROSSIMO È ALLE 10:15."),
        ("SAMIR", "E DOVE DEVO SCENDERE?"), ("*SIGNORA", "AL CAPOLINEA. È L'ULTIMA FERMATA."), ("SAMIR", "GRAZIE MILLE!")])),
    slide("📌 LE DOMANDE UTILI", table([
        ["❓ QUALE AUTOBUS VA ALL'OSPEDALE?"], ["❓ QUESTO AUTOBUS VA IN CENTRO?"], ["❓ A CHE ORA PASSA IL PROSSIMO?"],
        ["❓ DOVE DEVO SCENDERE?"], ["❓ DOVE COMPRO IL BIGLIETTO?"], ["❓ QUANTO COSTA IL BIGLIETTO?"]])),
    end("ORA SAI PRENDERE L'AUTOBUS!"),
]

AUTOBUS = {
 "title": "🚌 Prendo l'autobus · Esercizi",
 "store": "autobus",
 "upper": True,
 "sections": [
  {"part": "I mezzi"},
  {"id": "e1", "title": "1 · IN o A?", "short": "1 · In o a", "type": "choice", "opts": ["IN", "A"],
   "items": [{"q": q} for q in ["1. VADO … AUTOBUS.", "2. VADO … PIEDI.", "3. VADO … TRENO.", "4. VADO … BICI.", "5. VADO … MACCHINA."]],
   "k": [eq(a) for a in ["IN", "A", "IN", "IN", "IN"]]},
  {"part": "Il biglietto e la fermata"},
  {"id": "e2", "title": "2 · Che cos'è?", "short": "2 · Le parole", "type": "select",
   "opts": ["LA FERMATA", "IL CAPOLINEA", "IL CONTROLLORE", "L'ABBONAMENTO", "LA TABACCHERIA"],
   "items": [{"q": q} for q in ["1. QUI ASPETTO L'AUTOBUS.", "2. L'ULTIMA FERMATA.", "3. CONTROLLA I BIGLIETTI.",
                                 "4. UN BIGLIETTO PER UN MESE.", "5. QUI COMPRO IL BIGLIETTO."]],
   "k": [eq(a) for a in ["LA FERMATA", "IL CAPOLINEA", "IL CONTROLLORE", "L'ABBONAMENTO", "LA TABACCHERIA"]]},
  {"id": "e3", "title": "3 · SALIRE o SCENDERE?", "short": "3 · Salire o scendere", "type": "choice", "opts": ["SALGO", "SCENDO"],
   "items": [{"q": q} for q in ["1. ⬆️ ENTRO NELL'AUTOBUS: …", "2. ⬇️ ESCO DALL'AUTOBUS: …", "3. 🔴 PREMO IL PULSANTE PERCHÉ …", "4. 🎫 CONVALIDO IL BIGLIETTO QUANDO …"]],
   "k": [eq("SALGO"), eq("SCENDO"), eq("SCENDO"), eq("SALGO")]},
  {"part": "Alla fermata"},
  {"id": "e4", "title": "4 · Metti in ordine il dialogo", "short": "4 · In ordine", "type": "order",
   "cons": "SCRIVI IL NUMERO: 1 = LA PRIMA FRASE.",
   "items": ["SIGNORE: OGNI QUINDICI MINUTI.", "LUCIA: SCUSI, QUESTO AUTOBUS VA ALL'OSPEDALE?", "LUCIA: GRAZIE! E A CHE ORA PASSA?",
             "SIGNORE: NO, DEVE PRENDERE IL 3.", "LUCIA: GRAZIE MILLE, ARRIVEDERCI!"],
   "k": [eq("4"), eq("1"), eq("3"), eq("2"), eq("5")]},
  {"id": "e5", "title": "5 · Completa", "short": "5 · Completa", "type": "cloze", "bank": "VA · PASSA · SCENDERE · BIGLIETTO",
   "parts": ["SCUSI, QUESTO AUTOBUS ", {}, " IN CENTRO?<br>A CHE ORA ", {}, " IL PROSSIMO?<br>DOVE DEVO ", {}, "?<br>DOVE COMPRO IL ", {}, "?"],
   "k": [eq("va"), eq("passa"), eq("scendere"), eq("biglietto")]},
  {"id": "e6", "title": "6 ✎ · Come vai a scuola o al lavoro?", "type": "free", "rows": 3,
   "items": ["SCRIVI COME VAI A SCUOLA O AL LAVORO: CON QUALE MEZZO? DOVE SALI? DOVE SCENDI? QUANTO TEMPO CI METTI?"]},
  {"id": "e7", "title": "7 🎤 · Chiedi alla fermata", "type": "record", "items": ["CHIEDI A UNA PERSONA ALLA FERMATA: QUALE AUTOBUS VA ALLA STAZIONE E A CHE ORA PASSA."]},
 ]
}

# =====================================================================
# CHE TEMPO FA? (A1)
# =====================================================================
TEMPO_SLIDE = [
    cover("🌦️", "CHE TEMPO FA?", "OGGI C'È IL SOLE E FA CALDO!", "IL SOLE &bull; LA PIOGGIA &bull; CALDO E FREDDO"),
    slide("☀️ CHE TEMPO FA?", cards([
        ("☀️", "C'È IL SOLE", "È SERENO"), ("☁️", "È NUVOLOSO", "CI SONO LE NUVOLE"), ("🌧️", "PIOVE", "C'È LA PIOGGIA"),
        ("⛈️", "C'È UN TEMPORALE", "PIOVE TANTO, CON TUONI E LAMPI"), ("💨", "C'È VENTO", "TIRA VENTO"), ("🌫️", "C'È LA NEBBIA", "NON VEDO BENE"),
        ("❄️", "NEVICA", "C'È LA NEVE"), ("🌤️", "È BELLO", "IL TEMPO È BELLO"), ("🌧️", "È BRUTTO", "IL TEMPO È BRUTTO")], cols="g3")),
    slide("🌡️ CALDO O FREDDO?", table([["🥵 FA CALDO", "30 GRADI"], ["🙂 FA FRESCO", "15 GRADI"], ["🥶 FA FREDDO", "3 GRADI"]], head=["COME È?", "LA TEMPERATURA"]) + "\n" +
          nota("FA CALDO · FA FREDDO &nbsp;→&nbsp; CON IL VERBO <b>FARE</b><br>PIOVE · NEVICA &nbsp;→&nbsp; SENZA SOGGETTO")),
    slide("🗣️ AL TELEFONO CON LA MAMMA", dialogo([
        ("*MAMMA", "CHE TEMPO FA A BARI?"), ("YUSUF", "OGGI PIOVE E C'È VENTO. FA UN PO' FREDDO."), ("*MAMMA", "QUI A DAKAR FA CALDO! CI SONO 32 GRADI."),
        ("YUSUF", "BEATI VOI! DOMANI QUI C'È IL SOLE, MENO MALE.")])),
    slide("👕 CHE COSA METTO?", cards([("🌧️", "PIOVE", "PRENDO L'OMBRELLO ☂️"), ("🥶", "FA FREDDO", "METTO IL CAPPOTTO E LA SCIARPA 🧣"),
                                       ("🥵", "FA CALDO", "METTO LA MAGLIETTA E GLI OCCHIALI DA SOLE 🕶️"), ("💨", "C'È VENTO", "METTO LA GIACCA 🧥")])),
    end("ORA SAI DIRE CHE TEMPO FA!"),
]

TEMPO = {
 "title": "🌦️ Che tempo fa? · Esercizi",
 "store": "tempo",
 "upper": True,
 "sections": [
  {"part": "Il tempo"},
  {"id": "e1", "title": "1 · Che tempo fa?", "short": "1 · Che tempo fa", "type": "select",
   "opts": ["C'È IL SOLE", "PIOVE", "NEVICA", "C'È VENTO", "È NUVOLOSO", "C'È LA NEBBIA", "C'È UN TEMPORALE"],
   "items": [{"q": q} for q in ["🌧️ 1.", "☀️ 2.", "❄️ 3.", "💨 4.", "☁️ 5.", "⛈️ 6.", "🌫️ 7."]],
   "k": [eq(a) for a in ["PIOVE", "C'È IL SOLE", "NEVICA", "C'È VENTO", "È NUVOLOSO", "C'È UN TEMPORALE", "C'È LA NEBBIA"]]},
  {"id": "e2", "title": "2 · FA, C'È o È?", "short": "2 · Fa, c'è o è", "type": "choice", "opts": ["FA", "C'È", "È"],
   "items": [{"q": q} for q in ["1. … CALDO.", "2. … IL SOLE.", "3. … NUVOLOSO.", "4. … FREDDO.", "5. … VENTO.", "6. … BRUTTO TEMPO."]],
   "k": [eq("FA"), eq("C'È"), eq("È"), eq("FA"), eq("C'È"), eq("FA", "È")]},
  {"part": "Il meteo"},
  {"id": "e3", "title": "3 · Leggi il meteo: vero o falso?", "short": "3 · Il meteo", "type": "choice", "opts": ["VERO", "FALSO"], "full": True,
   "info": "📺 <b>IL METEO DI DOMANI</b><br>☀️ BARI: SOLE, 22 GRADI<br>🌧️ MILANO: PIOGGIA, 12 GRADI<br>❄️ TRENTO: NEVE, 0 GRADI<br>💨 PALERMO: VENTO, 20 GRADI",
   "items": [{"q": q} for q in ["1. A BARI C'È IL SOLE.", "2. A MILANO FA CALDO.", "3. A TRENTO NEVICA.", "4. A PALERMO PIOVE.", "5. A BARI CI SONO 22 GRADI."]],
   "k": [eq(a) for a in ["VERO", "FALSO", "VERO", "FALSO", "VERO"]]},
  {"id": "e4", "title": "4 · Che cosa metti?", "short": "4 · Che cosa metti", "type": "select",
   "opts": ["L'OMBRELLO", "IL CAPPOTTO", "GLI OCCHIALI DA SOLE", "LA GIACCA"],
   "items": [{"q": q} for q in ["1. PIOVE.", "2. FA MOLTO FREDDO.", "3. C'È IL SOLE E FA CALDO.", "4. C'È UN PO' DI VENTO."]],
   "k": [eq("L'OMBRELLO"), eq("IL CAPPOTTO"), eq("GLI OCCHIALI DA SOLE"), eq("LA GIACCA", "IL CAPPOTTO")]},
  {"id": "e5", "title": "5 ✎ · Il tempo oggi", "type": "free", "rows": 3,
   "items": ["CHE TEMPO FA OGGI DOVE SEI? E NEL TUO PAESE IN QUESTA STAGIONE?"]},
 ]
}

# =====================================================================
# AL TELEFONO: PRENDO UN APPUNTAMENTO (A1)
# =====================================================================
TELEFONO_SLIDE = [
    cover("📞", "AL TELEFONO", "PRONTO? VORREI PRENDERE UN APPUNTAMENTO.", "RISPONDO &bull; CHIEDO UN APPUNTAMENTO &bull; I NUMERI UTILI"),
    slide("CHE COSA IMPARIAMO?", cards([
        ("📞", "RISPONDERE AL TELEFONO", "PRONTO? CHI PARLA?"), ("📅", "PRENDERE UN APPUNTAMENTO", "VORREI UN APPUNTAMENTO CON IL DOTTORE"),
        ("🔁", "CAPIRE BENE", "PUÒ RIPETERE? PIÙ PIANO, PER FAVORE"), ("🚑", "I NUMERI UTILI", "112 · 118")])),
    slide("📞 PRONTO?", dialogo([("*SEGRETERIA", "PRONTO, STUDIO MEDICO, BUONGIORNO."), ("AMINA", "BUONGIORNO, SONO AMINA DIALLO."),
                                ("*SEGRETERIA", "MI DICA."), ("AMINA", "VORREI PRENDERE UN APPUNTAMENTO CON LA DOTTORESSA BIANCHI.")]) + "\n" +
          nota("AL TELEFONO IN ITALIA DICO <b>«PRONTO?»</b>")),
    slide("📅 L'APPUNTAMENTO", dialogo([("*SEGRETERIA", "VA BENE GIOVEDÌ ALLE 10?"), ("AMINA", "NO, GIOVEDÌ NON POSSO. LAVORO."),
                                       ("*SEGRETERIA", "E VENERDÌ ALLE 16?"), ("AMINA", "SÌ, VENERDÌ VA BENE."),
                                       ("*SEGRETERIA", "PERFETTO. VENERDÌ ALLE 16. PORTI LA TESSERA SANITARIA."), ("AMINA", "GRAZIE, ARRIVEDERCI.")])),
    slide("🔁 SE NON CAPISCO", cards([("🔁", "PUÒ RIPETERE, PER FAVORE?", ""), ("🐢", "PIÙ PIANO, PER FAVORE.", ""),
                                     ("🔤", "COME SI SCRIVE?", ""), ("📶", "NON LA SENTO BENE.", ""), ("✍️", "UN MOMENTO, SCRIVO.", ""), ("📝", "POSSO LASCIARE UN MESSAGGIO?", "")])),
    slide("🚑 I NUMERI UTILI", cards([("🆘", "112", "NUMERO UNICO DI EMERGENZA"), ("🚑", "118", "AMBULANZA: EMERGENZA SANITARIA")]) + "\n" +
          nota("AL 112 E AL 118 DICO: CHI SONO, DOVE SONO, CHE COSA SUCCEDE.<br>ESEMPIO: «MI CHIAMO KARIM. SONO IN VIA CRISANZIO 25. UN UOMO STA MALE.»")),
    end("ORA SAI TELEFONARE E PRENDERE UN APPUNTAMENTO!"),
]

TELEFONO = {
 "title": "📞 Al telefono · Esercizi",
 "store": "telefono",
 "upper": True,
 "sections": [
  {"part": "Al telefono"},
  {"id": "e1", "title": "1 · Che cosa dici?", "short": "1 · Che cosa dici", "type": "select",
   "opts": ["PRONTO?", "PUÒ RIPETERE, PER FAVORE?", "VORREI PRENDERE UN APPUNTAMENTO.", "NO, NON POSSO.", "SÌ, VA BENE.", "COME SI SCRIVE?"],
   "items": [{"q": q} for q in ["1. SUONA IL TELEFONO. RISPONDI:", "2. NON HAI CAPITO.", "3. VUOI ANDARE DAL DOTTORE.",
                                 "4. L'ORARIO VA BENE PER TE.", "5. A QUELL'ORA LAVORI.", "6. NON SAI SCRIVERE IL NOME DELLA VIA."]],
   "k": [eq(a) for a in ["PRONTO?", "PUÒ RIPETERE, PER FAVORE?", "VORREI PRENDERE UN APPUNTAMENTO.", "SÌ, VA BENE.", "NO, NON POSSO.", "COME SI SCRIVE?"]]},
  {"id": "e2", "title": "2 · Metti in ordine la telefonata", "short": "2 · In ordine", "type": "order",
   "cons": "SCRIVI IL NUMERO: 1 = LA PRIMA FRASE.",
   "items": ["SEGRETERIA: VA BENE MARTEDÌ ALLE 9?", "KARIM: BUONGIORNO, SONO KARIM HADDAD. VORREI UN APPUNTAMENTO.",
             "SEGRETERIA: PRONTO, STUDIO MEDICO.", "KARIM: SÌ, VA BENE. GRAZIE, ARRIVEDERCI.", "SEGRETERIA: PERFETTO. ARRIVEDERCI."],
   "k": [eq("3"), eq("2"), eq("1"), eq("4"), eq("5")]},
  {"id": "e3", "title": "3 · Completa la telefonata", "short": "3 · Completa", "type": "cloze",
   "bank": "PRONTO · VORREI · POSSO · VA BENE · RIPETERE",
   "parts": ["SEGRETERIA: ", {}, ", CENTRO CAF.<br>SAMIR: BUONGIORNO. ", {}, " UN APPUNTAMENTO.<br>SEGRETERIA: LUNEDÌ ALLE 11?<br>SAMIR: NO, LUNEDÌ NON ", {},
             ".<br>SEGRETERIA: MERCOLEDÌ ALLE QUINDICI E TRENTA.<br>SAMIR: SCUSI, PUÒ ", {}, "?<br>SEGRETERIA: MERCOLEDÌ ALLE 15:30.<br>SAMIR: SÌ, ", {}, ". GRAZIE!"],
   "k": [eq("pronto"), eq("vorrei"), eq("posso"), eq("ripetere"), eq("va bene")]},
  {"part": "I numeri utili"},
  {"id": "e4", "title": "4 · Che numero chiami?", "short": "4 · I numeri", "type": "choice", "opts": ["112", "118"],
   "cons": "TUTTI E DUE SONO NUMERI DI EMERGENZA. QUAL È IL PIÙ GIUSTO?",
   "items": [{"q": q} for q in ["1. UNA PERSONA STA MALE: SERVE L'AMBULANZA.", "2. C'È UN LADRO IN CASA.", "3. C'È UN INCENDIO."]],
   "k": [eq("118", "112"), eq("112"), eq("112")]},
  {"id": "e5", "title": "5 🎤 · Telefona", "type": "record",
   "items": ["FAI FINTA DI TELEFONARE: SALUTA, DI' IL TUO NOME E CHIEDI UN APPUNTAMENTO CON IL DOTTORE PER VENERDÌ MATTINA."]},
 ]
}

SLIDE2 = [
    ("cartelli/index.html", "LEGGO I CARTELLI", "PRIMI PASSI", CARTELLI_SLIDE, CARTELLO_CSS + FOTO_CSS),
    ("in-classe/index.html", "IN CLASSE", "PRIMI PASSI", CLASSE_SLIDE, ""),
    ("suoni/index.html", "SUONI DIFFICILI", "PRIMI PASSI", SUONI_SLIDE, SUONI_CSS),
    ("questo-quello/index.html", "QUESTO E QUELLO", "LIVELLO A1", QUESTO_SLIDE, ""),
    ("ce-ci-sono/index.html", "C'È / CI SONO", "LIVELLO A1", CE_SLIDE, ""),
    ("mi-piace/index.html", "MI PIACE", "LIVELLO A1", PIACE_SLIDE, ""),
    ("autobus/index.html", "PRENDO L'AUTOBUS", "LIVELLO A1", AUTOBUS_SLIDE, ""),
    ("tempo/index.html", "CHE TEMPO FA?", "LIVELLO A1", TEMPO_SLIDE, ""),
    ("telefono/index.html", "AL TELEFONO", "LIVELLO A1", TELEFONO_SLIDE, ""),
]
ESERCIZI2 = [("cartelli", CARTELLI), ("in-classe", CLASSE), ("suoni", SUONI), ("questo-quello", QUESTO), ("ce-ci-sono", CE),
             ("mi-piace", PIACE), ("autobus", AUTOBUS), ("tempo", TEMPO), ("telefono", TELEFONO)]
