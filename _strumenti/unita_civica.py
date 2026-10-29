"""Educazione civica (2026-10-29), dai materiali di Erila: Agenzia delle Entrate, modello AA4/8, guida CIE e CieID.
Tre unità: L'AGENZIA DELLE ENTRATE, IL CODICE FISCALE E IL MODULO AA4/8, ATTIVO LA CIE.
Tutto in STAMPATELLO MAIUSCOLO. Testi riscritti per il sito. Persone, indirizzi e codici sono inventati."""
from genera import eq, has, all_
from unita_primi import cover, slide, cards, table, nota, dialogo, end

TOP = "EDUCAZIONE CIVICA"

PASSI_CSS = """
  .passi{display:flex; flex-direction:column; gap:12px; max-width:1000px;}
  .passi div{background:#fff; border:3px solid #e3edf8; border-radius:14px; padding:12px 16px; font-size:1.45rem; display:flex; gap:14px; align-items:center;}
  .passi .n{flex:none; width:44px; height:44px; line-height:44px; text-align:center; border-radius:50%; background:var(--blu); color:#fff; font-weight:bold;}
  .cf{display:flex; flex-wrap:wrap; gap:8px; font-family:monospace; font-size:2rem; font-weight:bold; margin:8px 0 14px;}
  .cf span{background:#fff; border:3px solid var(--teal); border-radius:12px; padding:8px 12px; text-align:center;}
  .cf small{display:block; font-family:inherit; font-size:.85rem; font-weight:normal; color:#5b6b7b; margin-top:4px;}
  .pin{font-family:monospace; font-size:2.3rem; font-weight:bold; letter-spacing:4px;}
  .card, .card b, table.plur td, table.plur th{overflow-wrap:normal; word-break:normal; hyphens:none;}
  table.plur td b{white-space:nowrap;}
  @media (max-width:520px){ .g2, .g4{grid-template-columns:1fr;} }
  @media (max-width:900px){ .passi div{font-size:1.1rem;} .cf{font-size:1.3rem;} .cf small{font-size:.7rem;} .pin{font-size:1.5rem; letter-spacing:2px;} }"""

def passi(items):
    return '    <div class="passi">\n' + "".join(
        '      <div><span class="n">%d</span><span>%s</span></div>\n' % (i + 1, t) for i, t in enumerate(items)) + "    </div>"

# =====================================================================
# 1. L'AGENZIA DELLE ENTRATE (A1/A2)
# =====================================================================
ENTRATE_SLIDE = [
    cover("🏛️", "L'AGENZIA DELLE ENTRATE", "CHE COS'È? CHE COSA FA?", "IL CODICE FISCALE &bull; LE TASSE &bull; L'AFFITTO &bull; LA PARTITA IVA"),
    slide("CHE COSA IMPARIAMO?", cards([
        ("🔢", "IL CODICE FISCALE", "CHE COS'È E A CHE COSA SERVE"), ("💶", "LE TASSE", "CHE COSA SONO E CHI LE PAGA"),
        ("🏠", "IL CONTRATTO D'AFFITTO", "BISOGNA REGISTRARLO"), ("🏪", "LA PARTITA IVA", "PER APRIRE UN'ATTIVITÀ")])),
    slide("🏛️ CHE COS'È?", nota("L'AGENZIA DELLE ENTRATE È UN <b>UFFICIO DELLO STATO</b>.<br>"
                                "C'È UN UFFICIO IN OGNI CITTÀ. ANCHE A BARI.", "") + "\n" + cards([
        ("🔢", "DÀ IL CODICE FISCALE", "UN CODICE IMPORTANTE PER LA VITA IN ITALIA"),
        ("💶", "GESTISCE LE TASSE", "I SOLDI CHE PAGHIAMO ALLO STATO"),
        ("🔍", "CONTROLLA", "CONTROLLA CHE LE PERSONE PAGANO LE TASSE GIUSTE"),
        ("🤝", "AIUTA", "HAI UN PROBLEMA CON LE TASSE O CON IL CODICE FISCALE? CHIEDI ALL'UFFICIO")])),
    slide("🔢 IL CODICE FISCALE SERVE PER…", cards([
        ("🏥", "LA TESSERA SANITARIA", "SCEGLIERE IL DOTTORE, PRENOTARE UNA VISITA"),
        ("💼", "IL CONTRATTO DI LAVORO", "SENZA CODICE FISCALE NON PUOI ESSERE ASSUNTO"),
        ("🏦", "IL CONTO CORRENTE", "ALLA POSTA O IN BANCA: I TUOI SOLDI SONO AL SICURO"),
        ("🏠", "AFFITTARE UNA CASA", "IL CONTRATTO D'AFFITTO HA IL TUO CODICE FISCALE")])),
    slide("💶 CHE COSA SONO LE TASSE?", '    <div class="twocol2">\n' +
          nota("LE <b>TASSE</b> SONO I SOLDI CHE PAGHIAMO ALLO <b>STATO</b>:<br>QUANDO LAVORIAMO, QUANDO ABBIAMO UNA CASA O UN TERRENO.", "") + "\n" +
          cards([("🏫", "LE SCUOLE", ""), ("🏥", "GLI OSPEDALI", ""), ("🛣️", "LE STRADE", ""), ("🌳", "I PARCHI", "")]) +
          "\n    </div>\n" + nota("CON LE TASSE LO STATO PAGA I SERVIZI <b>PER TUTTI</b>. COSÌ LA SCUOLA E L'OSPEDALE COSTANO POCO O SONO GRATIS.")),
    slide("⚖️ CHI PAGA DI PIÙ?", table([
        ["💰💰💰", "CHI GUADAGNA DI PIÙ", "PAGA DI PIÙ"],
        ["💰", "CHI GUADAGNA DI MENO", "PAGA DI MENO"],
        ["—", "CHI NON HA NIENTE", "NON PAGA"]], head=["", "CHI?", "QUANTO PAGA?"]) + "\n" +
        nota("SE LAVORI CON UN CONTRATTO, IL <b>DATORE DI LAVORO</b> PAGA LE TASSE PER TE OGNI MESE.<br>"
             "LE VEDI NELLA <b>BUSTA PAGA</b>: IL LORDO MENO LE TASSE = IL NETTO.")),
    slide("📋 LA DICHIARAZIONE DEI REDDITI", cards([
        ("📅", "UNA VOLTA ALL'ANNO", "DICO ALLO STATO QUANTI SOLDI HO GUADAGNATO"),
        ("📄", "LA CU (CERTIFICAZIONE UNICA)", "LA DÀ IL DATORE DI LAVORO. DICE QUANTO HO GUADAGNATO IN UN ANNO"),
        ("💊", "LE SPESE PER LA SALUTE", "MEDICINE, DOTTORI: CONSERVO GLI SCONTRINI"),
        ("🧑‍💼", "IL CAF", "UN UFFICIO CHE MI AIUTA A FARE LA DICHIARAZIONE. DI SOLITO COSTA 25-30 EURO")])),
    slide("✉️ UN ERRORE? ARRIVA UN AVVISO", passi([
        "C'È UN ERRORE NELLA DICHIARAZIONE: L'AGENZIA DELLE ENTRATE MANDA UN <b>AVVISO</b>.",
        "NON RISPONDO E NON PAGO? ARRIVA LA <b>CARTELLA DI PAGAMENTO</b>: QUANTO PAGARE E ENTRO QUALE GIORNO (LA <b>SCADENZA</b>).",
        "NON PAGO ENTRO LA SCADENZA? C'È IL <b>FERMO</b>: NON POSSO USARE LA MACCHINA O IL MOTORINO."]) + "\n" +
        nota("⚠️ HAI RICEVUTO UNA LETTERA E NON CAPISCI? NON ASPETTARE: CHIEDI AIUTO AL CAF O AGLI OPERATORI.")),
    slide("🏠 IL CONTRATTO D'AFFITTO", cards([
        ("📝", "REGISTRARE IL CONTRATTO", "IL CONTRATTO D'AFFITTO VA REGISTRATO ALL'AGENZIA DELLE ENTRATE"),
        ("📅", "ENTRO 30 GIORNI", "DAL GIORNO DELLA FIRMA"),
        ("👤", "CHI LO FA?", "DI SOLITO IL PROPRIETARIO, O L'AGENZIA IMMOBILIARE. MA PUÒ FARLO ANCHE CHI PRENDE LA CASA IN AFFITTO"),
        ("➗", "QUANTO COSTA?", "DI SOLITO IL COSTO È DIVISO A METÀ: PROPRIETARIO E INQUILINO")]) + "\n" +
        nota("COMPRI UNA CASA? QUI È IL <b>NOTAIO</b> CHE REGISTRA TUTTO.")),
    slide("🏪 APRO UN'ATTIVITÀ: LA PARTITA IVA", '    <div class="twocol2">\n' +
          nota("VOGLIO APRIRE UN NEGOZIO O LAVORARE IN PROPRIO?<br>DEVO APRIRE LA <b>PARTITA IVA</b>.<br><br>"
               "LA PARTITA IVA È COME UN CODICE FISCALE PER I NEGOZI E LE ATTIVITÀ.", "") + "\n" +
          cards([("💻", "ONLINE", ""), ("🏛️", "ALL'AGENZIA DELLE ENTRATE", ""), ("🧑‍💼", "AL CAF", ""),
                 ("📄", "MODELLO AA9/12", "PORTO UN DOCUMENTO E COMPILO IL MODELLO CON L'AIUTO DI UN IMPIEGATO")]) + "\n    </div>"),
    slide("🗣️ ALLO SPORTELLO", dialogo([
        ("*IMPIEGATA", "BUONGIORNO. MI DICA."),
        ("YUSUF", "BUONGIORNO. VORREI IL CODICE FISCALE."),
        ("*IMPIEGATA", "HA UN DOCUMENTO?"),
        ("YUSUF", "SÌ, ECCO IL PASSAPORTO."),
        ("*IMPIEGATA", "BENE. HA COMPILATO IL MODULO AA4/8?"),
        ("YUSUF", "SÌ, ECCOLO. QUANTO COSTA?"),
        ("*IMPIEGATA", "NIENTE, È GRATIS. ECCO IL SUO CODICE FISCALE.")])),
    end("ORA SAI CHE COSA FA L'AGENZIA DELLE ENTRATE!"),
]

ENTRATE = {
 "title": "🏛️ L'Agenzia delle Entrate · Esercizi",
 "store": "agenzia-entrate",
 "upper": True,
 "sections": [
  {"part": "Che cosa fa?"},
  {"id": "e1", "title": "1 · L'Agenzia delle Entrate: vero o falso?", "short": "1 · Vero o falso", "type": "choice",
   "opts": ["VERO", "FALSO"], "full": True,
   "items": [{"q": q} for q in ["1. L'AGENZIA DELLE ENTRATE È UN UFFICIO DELLO STATO.", "2. L'AGENZIA DELLE ENTRATE DÀ IL CODICE FISCALE.",
                                 "3. L'AGENZIA DELLE ENTRATE DÀ IL PERMESSO DI SOGGIORNO.", "4. L'AGENZIA CONTROLLA CHE LE PERSONE PAGANO LE TASSE GIUSTE.",
                                 "5. SE HO UN PROBLEMA CON IL CODICE FISCALE, POSSO CHIEDERE AIUTO ALL'AGENZIA.", "6. IL CODICE FISCALE COSTA 50 EURO."]],
   "k": [eq(a) for a in ["VERO", "VERO", "FALSO", "VERO", "VERO", "FALSO"]]},
  {"id": "e2", "title": "2 · A che cosa serve il codice fiscale?", "short": "2 · Il codice fiscale", "type": "multi",
   "cons": "METTI LA SPUNTA VICINO ALLE 4 COSE GIUSTE.",
   "items": ["FARE LA TESSERA SANITARIA", "PRENDERE L'AUTOBUS", "AVERE UN CONTRATTO DI LAVORO", "APRIRE UN CONTO CORRENTE",
             "COMPRARE IL PANE", "AFFITTARE UNA CASA"],
   "k": [eq(a) for a in ["X", "-", "X", "X", "-", "X"]]},

  {"part": "Le tasse"},
  {"id": "e3", "title": "3 · Completa: le tasse", "short": "3 · Le tasse", "type": "cloze",
   "cons": "SCRIVI LA PAROLA GIUSTA.", "bank": "STATO · SCUOLE · DI PIÙ · BUSTA PAGA · TUTTI",
   "parts": ["LE TASSE SONO I SOLDI CHE PAGHIAMO ALLO ", {}, ".<br>CON LE TASSE LO STATO PAGA I SERVIZI PER ", {},
             ": LE ", {}, ", GLI OSPEDALI, LE STRADE.<br>CHI GUADAGNA DI PIÙ PAGA ", {}, ".<br>SE LAVORO CON UN CONTRATTO, VEDO LE TASSE NELLA ", {}, "."],
   "k": [eq("stato"), eq("tutti"), eq("scuole"), eq("di piu"), eq("busta paga")]},
  {"id": "e4", "title": "4 · Leggi e rispondi", "short": "4 · La dichiarazione", "type": "choice", "full": True,
   "info": "🧑 <b>YUSUF</b> LAVORA IN UN MAGAZZINO A BARI CON UN CONTRATTO.<br>A MARZO IL DATORE DI LAVORO GLI DÀ LA <b>CU</b>.<br>"
           "YUSUF VA AL <b>CAF</b> CON LA CU E GLI SCONTRINI DELLA FARMACIA.<br>AL CAF FANNO LA <b>DICHIARAZIONE DEI REDDITI</b>. YUSUF PAGA 30 EURO.",
   "items": [{"q": "1. CHI DÀ LA CU A YUSUF?", "opts": ["IL DATORE DI LAVORO", "IL CAF", "LA FARMACIA"]},
             {"q": "2. CHE COSA DICE LA CU?", "opts": ["QUANTO HA GUADAGNATO IN UN ANNO", "DOVE ABITA", "QUANTI ANNI HA"]},
             {"q": "3. PERCHÉ PORTA GLI SCONTRINI DELLA FARMACIA?", "opts": ["SONO SPESE PER LA SALUTE", "SONO BIGLIETTI DELL'AUTOBUS", "SONO PER IL CONTRATTO"]},
             {"q": "4. CHI FA LA DICHIARAZIONE DEI REDDITI?", "opts": ["IL CAF", "IL MEDICO", "IL COMUNE"]},
             {"q": "5. OGNI QUANTO SI FA LA DICHIARAZIONE?", "opts": ["UNA VOLTA ALL'ANNO", "OGNI MESE", "OGNI SETTIMANA"]}],
   "k": [eq(a) for a in ["IL DATORE DI LAVORO", "QUANTO HA GUADAGNATO IN UN ANNO", "SONO SPESE PER LA SALUTE", "IL CAF", "UNA VOLTA ALL'ANNO"]]},
  {"id": "e5", "title": "5 · Che cosa succede dopo?", "short": "5 · L'avviso", "type": "order",
   "cons": "METTI IN ORDINE: 1, 2, 3, 4.",
   "items": ["ARRIVA LA CARTELLA DI PAGAMENTO CON LA SCADENZA.", "C'È UN ERRORE NELLA DICHIARAZIONE DEI REDDITI.",
             "NON PAGO ENTRO LA SCADENZA: C'È IL FERMO DELLA MACCHINA.", "L'AGENZIA DELLE ENTRATE MANDA UN AVVISO."],
   "k": [eq(a) for a in ["3", "1", "4", "2"]]},

  {"part": "La casa e il lavoro"},
  {"id": "e6", "title": "6 · Il contratto d'affitto", "short": "6 · L'affitto", "type": "choice", "full": True,
   "items": [{"q": "1. DOVE SI REGISTRA IL CONTRATTO D'AFFITTO?", "opts": ["ALL'AGENZIA DELLE ENTRATE", "IN QUESTURA", "IN FARMACIA"]},
             {"q": "2. ENTRO QUANTI GIORNI DALLA FIRMA?", "opts": ["30 GIORNI", "3 GIORNI", "UN ANNO"]},
             {"q": "3. CHI LO REGISTRA DI SOLITO?", "opts": ["IL PROPRIETARIO", "IL DOTTORE", "IL VICINO DI CASA"]},
             {"q": "4. CHI PAGA LA REGISTRAZIONE?", "opts": ["DI SOLITO METÀ IL PROPRIETARIO E METÀ L'INQUILINO", "SOLO LO STATO", "NESSUNO, È GRATIS"]},
             {"q": "5. COMPRO UNA CASA: CHI REGISTRA L'ATTO?", "opts": ["IL NOTAIO", "IL CAF", "IL DATORE DI LAVORO"]}],
   "k": [eq(a) for a in ["ALL'AGENZIA DELLE ENTRATE", "30 GIORNI", "IL PROPRIETARIO", "DI SOLITO METÀ IL PROPRIETARIO E METÀ L'INQUILINO", "IL NOTAIO"]]},
  {"id": "e7", "title": "7 · Di che cosa ho bisogno?", "short": "7 · Di che cosa ho bisogno", "type": "select",
   "opts": ["IL CODICE FISCALE", "LA PARTITA IVA", "LA DICHIARAZIONE DEI REDDITI", "LA REGISTRAZIONE DEL CONTRATTO"],
   "items": [{"q": q} for q in ["1. VOGLIO APRIRE UN NEGOZIO DI ALIMENTARI.", "2. SONO APPENA ARRIVATO IN ITALIA E VOGLIO LAVORARE.",
                                 "3. HO FIRMATO IL CONTRATTO PER UNA CASA IN AFFITTO.", "4. VOGLIO DIRE ALLO STATO QUANTO HO GUADAGNATO QUEST'ANNO."]],
   "k": [eq(a) for a in ["LA PARTITA IVA", "IL CODICE FISCALE", "LA REGISTRAZIONE DEL CONTRATTO", "LA DICHIARAZIONE DEI REDDITI"]]},

  {"part": "Allo sportello"},
  {"id": "e8", "title": "8 · Riordina il dialogo allo sportello", "short": "8 · Allo sportello", "type": "order",
   "items": ["YUSUF: SÌ, ECCO IL PASSAPORTO.", "IMPIEGATA: BUONGIORNO. MI DICA.", "IMPIEGATA: NIENTE, È GRATIS.",
             "YUSUF: BUONGIORNO. VORREI IL CODICE FISCALE.", "YUSUF: QUANTO COSTA?", "IMPIEGATA: HA UN DOCUMENTO?"],
   "k": [eq(a) for a in ["4", "1", "6", "2", "5", "3"]]},
  {"id": "e9", "title": "9 🎤 · Allo sportello: parla tu", "type": "record",
   "items": ["SALUTA L'IMPIEGATO, DI' CHE VUOI IL CODICE FISCALE, DAI IL TUO DOCUMENTO E CHIEDI QUANTO COSTA."]},
 ]
}

# =====================================================================
# 2. IL CODICE FISCALE E IL MODULO AA4/8 (A1)
# =====================================================================
CF_PEZZI = [("DLL", "COGNOME"), ("MNA", "NOME"), ("95", "ANNO"), ("C", "MESE"), ("52", "GIORNO E SESSO"), ("Z343", "LUOGO"), ("?", "CONTROLLO")]

def cf_box():
    return '    <div class="cf">' + "".join('<span>%s<small>%s</small></span>' % p for p in CF_PEZZI) + "</div>"

AA48 = table([
    ["QUADRO&nbsp;A", "CHI FA LA DOMANDA E CHE COSA CHIEDE"],
    ["QUADRO&nbsp;B", "I DATI ANAGRAFICI: COGNOME, NOME, SESSO, DATA E LUOGO DI NASCITA"],
    ["QUADRO&nbsp;C", "LA RESIDENZA IN ITALIA: COMUNE, INDIRIZZO, CAP"],
    ["QUADRO&nbsp;D", "LA RESIDENZA ALL'ESTERO (SOLO SE ABITI FUORI DALL'ITALIA)"],
    ["QUADRO&nbsp;E", "ALTRI CODICI FISCALI (SE NE HAI GIÀ AVUTO UNO)"],
    ["FIRMA", "LA DATA E LA TUA FIRMA"]], head=["PARTE", "CHE COSA SCRIVO?"])

CF_SLIDE = [
    cover("🔢", "IL CODICE FISCALE", "CHIEDO IL CODICE FISCALE: IL MODULO AA4/8", "CHE COS'È &bull; DOVE LO CHIEDO &bull; IL MODULO &bull; LA TESSERA"),
    slide("🔢 CHE COS'È IL CODICE FISCALE?", nota("È UN CODICE DI <b>16 CARATTERI</b>: LETTERE E NUMERI.<br>"
                                                 "OGNI PERSONA HA IL SUO CODICE FISCALE. È SOLO TUO.", "") + "\n" + cards([
        ("🏥", "PER IL DOTTORE", "TESSERA SANITARIA, VISITE"), ("💼", "PER LAVORARE", "IL CONTRATTO DI LAVORO"),
        ("🏦", "PER LA BANCA E LA POSTA", "IL CONTO CORRENTE"), ("🏠", "PER LA CASA", "IL CONTRATTO D'AFFITTO")], "g4")),
    slide("🔍 CHE COSA C'È DENTRO?", cf_box() + "\n" + nota(
        "ESEMPIO INVENTATO: <b>AMINA DIALLO</b>, NATA IL <b>12 MARZO 1995</b> IN <b>SENEGAL</b>.<br>"
        "COGNOME → CONSONANTI <b>D L L</b> &nbsp;·&nbsp; NOME → <b>M N A</b> &nbsp;·&nbsp; MARZO → <b>C</b><br>"
        "GIORNO 12: PER LE DONNE + 40 → <b>52</b> &nbsp;·&nbsp; NATI ALL'ESTERO: <b>Z</b> + IL NUMERO DEL PAESE<br>"
        "L'ULTIMA LETTERA È UNA LETTERA DI CONTROLLO.", "")),
    slide("🏛️ DOVE LO CHIEDO?", cards([
        ("🏛️", "ALL'AGENZIA DELLE ENTRATE", "VADO ALL'UFFICIO. È MEGLIO PRENDERE UN APPUNTAMENTO"),
        ("📄", "IL MODULO AA4/8", "LO COMPILO PRIMA, O IN UFFICIO"),
        ("🛂", "UN DOCUMENTO", "IL PASSAPORTO O UN ALTRO DOCUMENTO D'IDENTITÀ"),
        ("🆓", "È GRATIS", "IL CODICE FISCALE NON COSTA NIENTE")]) + "\n" +
        nota("POI A CASA ARRIVA LA <b>TESSERA SANITARIA</b>: SOPRA C'È ANCHE IL CODICE FISCALE.")),
    slide("📄 IL MODULO AA4/8", AA48),
    slide("🅰️ QUADRO A: CHI? CHE COSA?", '    <div class="twocol2">\n' + table([
        ["D", "LA DOMANDA È PER ME"], ["T", "LA DOMANDA È PER UN'ALTRA PERSONA (CON LA DELEGA)"]], head=["CHI?", ""]) + "\n" + table([
        ["1", "ATTRIBUZIONE CODICE FISCALE: È LA PRIMA VOLTA"], ["2", "VARIAZIONE DATI: UN DATO È CAMBIATO (ES. LA CASA)"],
        ["4", "CERTIFICATO DI CODICE FISCALE: UN FOGLIO CHE DICE IL MIO CODICE"],
        ["5", "DUPLICATO: HO PERSO LA TESSERA SANITARIA"]], head=["CHE COSA?", ""]) + "\n    </div>"),
    slide("🅱️ QUADRO B E C: I MIEI DATI", '    <div class="twocol2">\n' + table([
        ["COGNOME", "<b>DIALLO</b>"], ["NOME", "<b>AMINA</b>"], ["SESSO", "<b>F</b>"],
        ["COMUNE (O STATO ESTERO) DI NASCITA", "<b>SENEGAL</b>"], ["DATA DI NASCITA", "<b>12 03 1995</b>"]], head=["QUADRO&nbsp;B", ""]) + "\n" + table([
        ["COMUNE", "<b>BARI</b>"], ["PROVINCIA", "<b>BA</b>"], ["C.A.P.", "<b>70122</b>"],
        ["TIPOLOGIA", "<b>VIA</b>"], ["INDIRIZZO", "<b>DEI GIGLI</b>"], ["NUMERO CIVICO", "<b>8</b>"]], head=["QUADRO&nbsp;C", ""]) + "\n    </div>\n" +
        nota("ATTENZIONE: SCRIVO IN <b>STAMPATELLO</b>. LA PERSONA E L'INDIRIZZO SONO INVENTATI.")),
    slide("✍️ LA FIRMA E LA DELEGA", cards([
        ("✍️", "SOTTOSCRIZIONE", "SCRIVO LA DATA DI OGGI E FIRMO"),
        ("🧑‍🤝‍🧑", "LA DELEGA", "NON POSSO ANDARE IO? UN'ALTRA PERSONA VA PER ME. IO SCRIVO I MIEI DATI E FIRMO LA DELEGA"),
        ("📎", "ALLEGATI", "LA FOTOCOPIA DEL DOCUMENTO")])),
    end("ORA SAI CHIEDERE IL CODICE FISCALE!"),
]

FATIMA = ("👩 <b>MI CHIAMO FATIMA SAIDI</b>. SONO UNA DONNA. SONO NATA IN <b>TUNISIA</b> L'<b>8 APRILE 1999</b>.<br>"
          "ABITO A <b>BARI</b> (PROVINCIA <b>BA</b>), IN <b>VIA DELLE ROSE 21</b>. IL CAP È <b>70124</b>.<br>"
          "NON HO IL CODICE FISCALE: È LA PRIMA VOLTA. VADO IO ALL'AGENZIA DELLE ENTRATE.<br>"
          "<small>(FATIMA E IL SUO INDIRIZZO SONO INVENTATI)</small>")

CF = {
 "title": "🔢 Il codice fiscale e il modulo AA4/8 · Esercizi",
 "store": "codice-fiscale",
 "upper": True,
 "sections": [
  {"part": "Il codice fiscale"},
  {"id": "e1", "title": "1 · Il codice fiscale: vero o falso?", "short": "1 · Vero o falso", "type": "choice",
   "opts": ["VERO", "FALSO"], "full": True,
   "items": [{"q": q} for q in ["1. IL CODICE FISCALE HA 16 CARATTERI.", "2. IL CODICE FISCALE HA SOLO NUMERI.",
                                 "3. LO CHIEDO ALL'AGENZIA DELLE ENTRATE.", "4. IL CODICE FISCALE COSTA 16 EURO.",
                                 "5. IL CODICE FISCALE È ANCHE SULLA TESSERA SANITARIA.", "6. IO E MIO FRATELLO ABBIAMO LO STESSO CODICE FISCALE."]],
   "k": [eq(a) for a in ["VERO", "FALSO", "VERO", "FALSO", "VERO", "FALSO"]]},
  {"id": "e2", "title": "2 · Che cosa c'è dentro il codice fiscale?", "short": "2 · Che cosa c'è dentro", "type": "multi",
   "cons": "METTI LA SPUNTA VICINO ALLE 5 COSE GIUSTE.",
   "items": ["IL COGNOME", "IL NUMERO DI TELEFONO", "IL NOME", "LA DATA DI NASCITA", "L'INDIRIZZO DI CASA", "IL SESSO (UOMO O DONNA)",
             "IL LAVORO", "IL LUOGO DI NASCITA"],
   "k": [eq(a) for a in ["X", "-", "X", "X", "-", "X", "-", "X"]]},

  {"part": "Il modulo AA4/8"},
  {"id": "e3", "title": "3 · In quale parte del modulo scrivo?", "short": "3 · Le parti del modulo", "type": "select",
   "opts": ["QUADRO&nbsp;A", "QUADRO B", "QUADRO C", "QUADRO D", "SOTTOSCRIZIONE"],
   "items": [{"q": q} for q in ["1. IL MIO COGNOME E IL MIO NOME", "2. IL MIO INDIRIZZO A BARI", "3. CHE COSA CHIEDO (ES. IL PRIMO CODICE FISCALE)",
                                 "4. LA DATA DI OGGI E LA FIRMA", "5. LA MIA DATA DI NASCITA", "6. IL MIO INDIRIZZO IN UN ALTRO PAESE (SE ABITO ALL'ESTERO)"]],
   "k": [eq(a) for a in ["QUADRO&nbsp;B", "QUADRO C", "QUADRO A", "SOTTOSCRIZIONE", "QUADRO B", "QUADRO D"]]},
  {"id": "e4", "title": "4 · Quadro A: che cosa metto?", "short": "4 · Il quadro A", "type": "select",
   "cons": "LEGGI. SCEGLI LA CASELLA GIUSTA.",
   "opts": ["D · PER ME", "T · PER UN'ALTRA PERSONA", "1 · ATTRIBUZIONE CODICE FISCALE", "2 · VARIAZIONE DATI", "5 · DUPLICATO TESSERA SANITARIA"],
   "items": [{"q": q} for q in ["1. NON HO IL CODICE FISCALE. È LA PRIMA VOLTA.", "2. HO PERSO LA TESSERA SANITARIA.",
                                 "3. VADO IO ALL'UFFICIO, LA DOMANDA È PER ME.", "4. HO CAMBIATO CASA E INDIRIZZO.",
                                 "5. MIA SORELLA VA ALL'UFFICIO PER ME, CON LA DELEGA."]],
   "k": [eq(a) for a in ["1 · ATTRIBUZIONE CODICE FISCALE", "5 · DUPLICATO TESSERA SANITARIA", "D · PER ME", "2 · VARIAZIONE DATI", "T · PER UN'ALTRA PERSONA"]]},
  {"id": "e5", "title": "5 · Compila il modulo di Fatima", "short": "5 · Il modulo di Fatima", "type": "text", "w": "m",
   "info": FATIMA, "cons": "LEGGI. SCRIVI I DATI DI FATIMA NEL MODULO.",
   "items": [{"q": q} for q in ["QUADRO A · TIPOLOGIA (D O T):", "QUADRO A · TIPO DI RICHIESTA (NUMERO):", "QUADRO B · COGNOME:", "QUADRO B · NOME:",
                                 "QUADRO B · SESSO (M O F):", "QUADRO B · STATO ESTERO DI NASCITA:", "QUADRO B · DATA DI NASCITA:",
                                 "QUADRO C · COMUNE:", "QUADRO C · PROVINCIA:", "QUADRO C · C.A.P.:", "QUADRO C · TIPOLOGIA (VIA, PIAZZA…):",
                                 "QUADRO C · INDIRIZZO:", "QUADRO C · NUMERO CIVICO:"]],
   "k": [eq("d"), eq("1"), eq("saidi"), eq("fatima"), eq("f"), eq("tunisia"),
         eq("08 04 1999", "8 04 1999", "08/04/1999", "8/4/1999", "08/4/1999", "8/04/1999", "08 4 1999", "8 4 1999", "08-04-1999", "8 aprile 1999"),
         eq("bari"), eq("ba"), eq("70124"), eq("via"), eq("delle rose"), eq("21")]},
  {"id": "e6", "title": "6 · Che cosa porto all'ufficio?", "short": "6 · Che cosa porto", "type": "multi",
   "cons": "METTI LA SPUNTA VICINO ALLE 3 COSE GIUSTE.",
   "items": ["IL PASSAPORTO O UN DOCUMENTO D'IDENTITÀ", "IL MODULO AA4/8 COMPILATO", "50 EURO PER PAGARE", "LA FOTOCOPIA DEL DOCUMENTO", "LA BUSTA PAGA"],
   "k": [eq(a) for a in ["X", "X", "-", "X", "-"]]},
  {"id": "e7", "title": "7 ✎ · Compila il tuo modulo", "type": "free", "rows": 1,
   "cons": "SCRIVI IN STAMPATELLO. SE VUOI, PUOI USARE DATI INVENTATI.",
   "items": ["COGNOME", "NOME", "SESSO", "COMUNE O STATO ESTERO DI NASCITA", "DATA DI NASCITA", "COMUNE DI RESIDENZA", "INDIRIZZO E NUMERO CIVICO", "C.A.P."]},
  {"id": "e8", "title": "8 🎤 · Spiega a un amico", "type": "record",
   "items": ["UN AMICO È APPENA ARRIVATO A BARI. SPIEGA: CHE COS'È IL CODICE FISCALE, DOVE LO CHIEDE E CHE COSA DEVE PORTARE."]},
 ]
}

# =====================================================================
# 3. ATTIVO LA CIE: L'APP CieID (A1)
# =====================================================================
CIE_SLIDE = [
    cover("🪪", "ATTIVO LA CIE", "LA CARTA D'IDENTITÀ ELETTRONICA E L'APP CIEID", "IL PIN &bull; L'APP &bull; L'NFC &bull; ENTRO NEI SITI"),
    slide("🪪 CHE COS'È LA CIE?", cards([
        ("🪪", "CIE = CARTA D'IDENTITÀ ELETTRONICA", "LA DÀ IL COMUNE. HA UN CHIP"),
        ("💻", "SERVE ANCHE ONLINE", "CON LA CIE ENTRI NEI SITI DELLO STATO: INPS, AGENZIA DELLE ENTRATE, LA SALUTE"),
        ("📱", "L'APP CIEID", "SUL TELEFONO. SERVE PER USARE LA CIE ONLINE"),
        ("🔐", "IL PIN", "UN CODICE SEGRETO DI 8 NUMERI")])),
    slide("🧰 CHE COSA MI SERVE?", cards([
        ("🪪", "LA CIE", ""), ("🔢", "IL PIN (8 NUMERI)", "E IL PUK"), ("📱", "UNO SMARTPHONE CON NFC", ""), ("⬇️", "L'APP CIEID", "")], "g4")),
    slide("1️⃣ PREPARA IL PIN E IL PUK", '    <div class="twocol2">\n' + cards([
        ("🏛️", "PEZZO 1: LE PRIME 4 CIFRE", "SONO SUL FOGLIO (LA RICEVUTA) CHE TI HA DATO IL COMUNE"),
        ("✉️", "PEZZO 2: LE ULTIME 4 CIFRE", "SONO NELLA LETTERA CHE È ARRIVATA A CASA CON LA CARTA")], "g1") + "\n" +
        nota('ESEMPIO INVENTATO:<br><span class="pin">2468</span> (COMUNE)<br>+ <span class="pin">1357</span> (LETTERA)<br>'
             '= <span class="pin">24681357</span><br>IL PIN COMPLETO: 8 CIFRE', "") + "\n    </div>\n" +
        nota("🔐 IL PIN È SEGRETO: NON DARLO A NESSUNO. NON SCRIVERLO SULLA CARTA.")),
    slide("2️⃣ 3️⃣ L'APP E L'NFC", cards([
        ("⬇️", "SCARICA L'APP", "CERCA «CIEID» NEL NEGOZIO DI APP DEL TELEFONO (PLAY STORE O APP STORE)"),
        ("📶", "ATTIVA L'NFC", "IMPOSTAZIONI → DISPOSITIVI CONNESSI → PREFERENZE DI CONNESSIONE → NFC.<br>OPPURE CERCA «NFC» NELLE IMPOSTAZIONI")])),
    slide("4️⃣ REGISTRA LA CARTA", passi([
        "APRI L'APP CIEID.", "PREMI IL TASTO «REGISTRA LA TUA CARTA».", "SCRIVI IL PIN DI 8 CIFRE.",
        "METTI LA CARTA DIETRO IL TELEFONO. ASPETTA: L'APP DICE «OK».",
        "SCEGLI UN CODICE DI 6 NUMERI O USA L'IMPRONTA DIGITALE: COSÌ ENTRI PIÙ VELOCE."])),
    slide("💻 USO LA CIE NEI SITI (ES. INPS)", passi([
        "SUL SITO CLICCA SU «ENTRA CON CIE».", "SUL TELEFONO L'APP CIEID TI CHIEDE DI CONFERMARE CHI SEI.", "FATTO! SEI DENTRO IL SITO. 🎉"])),
    slide("😟 HO PERSO IL PIN O IL PUK!", cards([
        ("🏛️", "VAI IN COMUNE", "ALL'UFFICIO CHE FA LE CARTE D'IDENTITÀ. CHIEDI DI STAMPARE DI NUOVO I CODICI"),
        ("🌐", "IL SITO UFFICIALE", "SUL SITO DELLA CARTA D'IDENTITÀ ELETTRONICA TROVI AIUTO")]) + "\n" +
        nota("🗣️ «BUONGIORNO. HO PERSO IL PIN DELLA CARTA D'IDENTITÀ. POSSO AVERE DI NUOVO I CODICI?»")),
    end("ORA SAI ATTIVARE LA CIE!"),
]

CIE = {
 "title": "🪪 Attivo la CIE · Esercizi",
 "store": "cie",
 "upper": True,
 "sections": [
  {"part": "La CIE e il PIN"},
  {"id": "e1", "title": "1 · Che cosa mi serve?", "short": "1 · Che cosa mi serve", "type": "multi",
   "cons": "PER ATTIVARE LA CIE SUL TELEFONO. METTI LA SPUNTA VICINO ALLE 4 COSE GIUSTE.",
   "items": ["LA CARTA D'IDENTITÀ ELETTRONICA (CIE)", "IL PIN DI 8 CIFRE", "LA TESSERA DELL'AUTOBUS", "UNO SMARTPHONE CON NFC",
             "L'APP CIEID", "LA BUSTA PAGA"],
   "k": [eq(a) for a in ["X", "X", "-", "X", "X", "-"]]},
  {"id": "e2", "title": "2 · Scrivi il PIN completo", "short": "2 · Il PIN", "type": "text", "w": "m",
   "cons": "PRIMO PEZZO (COMUNE) + SECONDO PEZZO (LETTERA) = PIN DI 8 CIFRE. I NUMERI SONO INVENTATI.",
   "items": [{"q": q} for q in ["1. 2468 + 1357 =", "2. 9012 + 3344 =", "3. 7070 + 1818 =", "4. 0550 + 2026 ="]],
   "k": [eq("24681357"), eq("90123344"), eq("70701818"), eq("05502026")]},
  {"id": "e3", "title": "3 · Dove trovo i pezzi del PIN?", "short": "3 · Dove trovo il PIN", "type": "choice", "full": True,
   "items": [{"q": "1. LE PRIME 4 CIFRE SONO…", "opts": ["SULLA RICEVUTA DEL COMUNE", "SUL TELEFONO", "SULLA TESSERA SANITARIA"]},
             {"q": "2. LE ULTIME 4 CIFRE SONO…", "opts": ["NELLA LETTERA ARRIVATA CON LA CARTA", "SUL PASSAPORTO", "NELL'APP"]},
             {"q": "3. QUANTE CIFRE HA IL PIN COMPLETO?", "opts": ["8", "4", "16"]}],
   "k": [eq(a) for a in ["SULLA RICEVUTA DEL COMUNE", "NELLA LETTERA ARRIVATA CON LA CARTA", "8"]]},

  {"part": "L'app CieID"},
  {"id": "e4", "title": "4 · Metti in ordine: registro la carta", "short": "4 · Registro la carta", "type": "order",
   "items": ["SCRIVO IL PIN DI 8 CIFRE.", "APRO L'APP CIEID.", "SCELGO UN CODICE DI 6 NUMERI O L'IMPRONTA DIGITALE.",
             "PREMO «REGISTRA LA TUA CARTA».", "METTO LA CARTA DIETRO IL TELEFONO E ASPETTO «OK»."],
   "k": [eq(a) for a in ["3", "1", "5", "2", "4"]]},
  {"id": "e5", "title": "5 · Vero o falso?", "short": "5 · Vero o falso", "type": "choice",
   "opts": ["VERO", "FALSO"], "full": True,
   "items": [{"q": q} for q in ["1. PRIMA DI REGISTRARE LA CARTA ATTIVO L'NFC.", "2. METTO LA CARTA DAVANTI ALLO SCHERMO DEL COMPUTER.",
                                 "3. SUL SITO DELL'INPS CLICCO SU «ENTRA CON CIE».", "4. DO IL MIO PIN A UN AMICO, COSÌ MI AIUTA.",
                                 "5. CON L'IMPRONTA DIGITALE ENTRO PIÙ VELOCE."]],
   "k": [eq(a) for a in ["VERO", "FALSO", "VERO", "FALSO", "VERO"]]},
  {"id": "e6", "title": "6 · Che cosa faccio?", "short": "6 · Che cosa faccio", "type": "select",
   "opts": ["VADO IN COMUNE", "ATTIVO L'NFC", "SCARICO L'APP CIEID", "CLICCO SU «ENTRA CON CIE»"],
   "items": [{"q": q} for q in ["1. HO PERSO LA LETTERA CON IL PIN.", "2. SUL TELEFONO NON HO L'APP.",
                                 "3. IL TELEFONO NON LEGGE LA CARTA.", "4. VOGLIO ENTRARE NEL SITO DELL'INPS."]],
   "k": [eq(a) for a in ["VADO IN COMUNE", "SCARICO L'APP CIEID", "ATTIVO L'NFC", "CLICCO SU «ENTRA CON CIE»"]]},
  {"id": "e7", "title": "7 · In Comune: completa", "short": "7 · In Comune", "type": "cloze",
   "bank": "PERSO · CODICI · DOCUMENTO · GRAZIE",
   "parts": ["IMPIEGATO: BUONGIORNO, MI DICA.<br>AMINA: BUONGIORNO. HO ", {}, " IL PIN DELLA CARTA D'IDENTITÀ.<br>"
             "IMPIEGATO: NESSUN PROBLEMA. HA UN ", {}, "?<br>AMINA: SÌ, ECCO LA CARTA.<br>IMPIEGATO: ECCO, HO STAMPATO DI NUOVO I ", {},
             ".<br>AMINA: ", {}, " MILLE!"],
   "k": [eq("perso"), eq("documento"), eq("codici"), eq("grazie")]},
  {"id": "e8", "title": "8 🎤 · Spiega a un amico", "type": "record",
   "items": ["SPIEGA A UN AMICO COME ATTIVARE LA CIE: IL PIN, L'APP, L'NFC E LA CARTA DIETRO IL TELEFONO."]},
 ]
}

SLIDE_CIVICA = [
    ("agenzia-entrate/index.html", "L'AGENZIA DELLE ENTRATE", TOP, ENTRATE_SLIDE, PASSI_CSS),
    ("codice-fiscale/index.html", "IL CODICE FISCALE", TOP, CF_SLIDE, PASSI_CSS),
    ("cie/index.html", "ATTIVO LA CIE", TOP, CIE_SLIDE, PASSI_CSS),
]
ESERCIZI_CIVICA = [("agenzia-entrate", ENTRATE), ("codice-fiscale", CF), ("cie", CIE)]
