"""Primi passi (Pre-A1) e A1, dal confronto con i sillabi (2026-10-28):
I MIEI DATI, CHE ORE SONO? GIORNI E MESI, GLI EURO, AL MERCATO E AL SUPERMERCATO.
Tutto in STAMPATELLO MAIUSCOLO. Testi scritti per il sito, non copiati da altri materiali."""
from foto_cibi import foto_quiz
from genera import eq, has, all_

# ---------- pezzi delle slide ----------
def cover(emoji, title, lead, badge):
    return ('  <section class="slide center cover">\n    <div class="big">%s</div>\n    <h1>%s</h1>\n'
            '    <p class="lead" style="margin-top:14px;">%s</p>\n    <span class="badge">%s</span>\n  </section>'
            % (emoji, title, lead, badge))

def slide(h2, inner):
    return '  <section class="slide">\n    <h2>%s</h2>\n%s\n  </section>' % (h2, inner)

def cards(items, cols="g2"):
    return ('    <div class="grid %s">\n' % cols +
            "".join('      <div class="card"><span class="emoji">%s</span><b>%s</b><span>%s</span></div>\n' % c for c in items) +
            "    </div>")

def table(rows, head=None):
    h = "<tr>" + "".join("<th>%s</th>" % c for c in head) + "</tr>" if head else ""
    return ('    <table class="plur">' + h +
            "".join("<tr>" + "".join("<td>%s</td>" % c for c in r) + "</tr>" for r in rows) + "</table>")

def nota(t, style="margin-top:20px;"):
    return '    <div class="nota" style="%s">%s</div>' % (style, t)

def dialogo(lines):
    out = '    <div class="dialogo">\n'
    for who, t in lines:
        cls = "bubble med" if who.startswith("*") else "bubble"
        out += '      <div class="%s"><span class="who">%s:</span> %s</div>\n' % (cls, who.lstrip("*"), t)
    return out + "    </div>"

def end(lead):
    return ('  <section class="slide center cover">\n    <div class="big">🎉</div>\n    <h1>BRAVI!</h1>\n'
            '    <p class="lead" style="margin-top:14px;">%s</p>\n'
            '    <a class="badge" href="esercizi.html" style="text-decoration:none">ADESSO FACCIAMO GLI ESERCIZI 📱</a>\n'
            '  </section>' % lead)

# =====================================================================
# 1. I MIEI DATI
# =====================================================================
MODULO = table([
    ["COGNOME", "<b>DIALLO</b>"], ["NOME", "<b>AMINA</b>"], ["SESSO", "M ☐ &nbsp; F ☒"],
    ["DATA DI NASCITA", "<b>12 / 03 / 1995</b>"], ["LUOGO DI NASCITA", "<b>DAKAR (SENEGAL)</b>"],
    ["CITTADINANZA", "<b>SENEGALESE</b>"], ["INDIRIZZO", "<b>VIA SPARANO 10, 70121 BARI</b>"],
    ["TELEFONO", "<b>333 123 4567</b>"], ["FIRMA", "<i>AMINA DIALLO</i>"]])

DATI_SLIDE = [
    cover("🪪", "I MIEI DATI", "NOME, COGNOME, DATA DI NASCITA, DOCUMENTI", "MI PRESENTO &bull; I DOCUMENTI &bull; IL MODULO"),
    slide("CHE COSA IMPARIAMO?", cards([
        ("🙋", "NOME E COGNOME", "MI CHIAMO AMINA DIALLO"),
        ("🎂", "DATA E LUOGO DI NASCITA", "SONO NATA IL 12 MARZO 1995 A DAKAR"),
        ("🏠", "INDIRIZZO E TELEFONO", "ABITO IN VIA SPARANO 10, A BARI"),
        ("📄", "DOCUMENTI E MODULI", "PERMESSO DI SOGGIORNO, TESSERA SANITARIA")])),
    slide("🙋 NOME E COGNOME", cards([
        ("👩", "NOME", "AMINA"), ("👪", "COGNOME", "DIALLO<br><small>(IL NOME DELLA FAMIGLIA)</small>")]) + "\n" +
        dialogo([("DOMANDA", "COME TI CHIAMI?"), ("*RISPOSTA", "MI CHIAMO AMINA."),
                 ("DOMANDA", "QUAL È IL TUO COGNOME?"), ("*RISPOSTA", "DIALLO.")])),
    slide("🎩 FORMALE: CON IL LEI", table([
        ["COME TI CHIAMI?", "COME SI CHIAMA?"], ["DI DOVE SEI?", "DI DOV'È?"],
        ["QUANTI ANNI HAI?", "QUANTI ANNI HA?"], ["DOVE ABITI?", "DOVE ABITA?"]],
        head=["INFORMALE (TU) 🧑‍🤝‍🧑", "FORMALE (LEI) 🏢"]) + "\n" +
        nota("IN UN UFFICIO, IN QUESTURA, DAL MEDICO: L'IMPIEGATO USA IL <b>LEI</b>.")),
    slide("🌍 DI DOVE SEI?", dialogo([
        ("DOMANDA", "DI DOVE SEI?"), ("*RISPOSTA", "SONO SENEGALESE. SONO DEL SENEGAL."),
        ("DOMANDA", "DOVE SEI NATA?"), ("*RISPOSTA", "SONO NATA A DAKAR, IN SENEGAL.")]) + "\n" +
        nota("👨 UN UOMO: SONO NAT<b>O</b> &nbsp;&nbsp; 👩 UNA DONNA: SONO NAT<b>A</b><br>"
             "LUOGO DI NASCITA = LA CITTÀ DOVE SONO NATO/NATA<br>CITTADINANZA = IL MIO PAESE (SENEGALESE, AFGHANA, NIGERIANA…)")),
    slide("🎂 LA DATA DI NASCITA", table([
        ["12 / 03 / 1995", "12 MARZO 1995"], ["01 / 09 / 2000", "1 SETTEMBRE 2000"], ["25 / 12 / 1988", "25 DICEMBRE 1988"]],
        head=["CON I NUMERI", "CON LE PAROLE"]) + "\n" +
        dialogo([("DOMANDA", "QUANDO SEI NATA?"), ("*RISPOSTA", "IL 12 MARZO 1995."),
                 ("DOMANDA", "QUANTI ANNI HAI?"), ("*RISPOSTA", "HO 30 ANNI.")]) + "\n" +
        nota("IN ITALIA PRIMA IL <b>GIORNO</b>, POI IL <b>MESE</b>, POI L'<b>ANNO</b>: 12 / 03 / 1995.")),
    slide("🏠 INDIRIZZO, TELEFONO, EMAIL", cards([
        ("📍", "INDIRIZZO", "VIA SPARANO 10<br>70121 BARI"), ("📞", "TELEFONO", "333 123 4567"),
        ("✉️", "EMAIL", "AMINA@MAIL.IT<br><small>@ = CHIOCCIOLA</small>"),
        ("🗣️", "DOMANDE", "DOVE ABITI? ABITO IN VIA SPARANO.<br>QUAL È IL TUO NUMERO? È 333…")])),
    slide("📄 I DOCUMENTI", cards([
        ("🛂", "IL PASSAPORTO", "PER VIAGGIARE IN UN ALTRO PAESE"),
        ("🇮🇹", "IL PERMESSO DI SOGGIORNO", "PER STARE IN ITALIA. LO DÀ LA QUESTURA"),
        ("🪪", "LA CARTA D'IDENTITÀ", "IL DOCUMENTO DEL COMUNE"),
        ("🏥", "LA TESSERA SANITARIA", "PER ANDARE DAL MEDICO E IN FARMACIA"),
        ("🔢", "IL CODICE FISCALE", "16 LETTERE E NUMERI. SERVE PER IL LAVORO, LA CASA, IL MEDICO"),
        ("✍️", "LA FIRMA", "IL MIO NOME SCRITTO CON LA MIA MANO")], cols="g3")),
    slide("📝 IL MODULO", '    <div class="twocol2">\n' + MODULO + "\n" +
          nota("UN <b>MODULO</b> È UN FOGLIO CON LE DOMANDE.<br>IO SCRIVO I MIEI DATI NEGLI SPAZI.<br><br>"
               "✍️ SCRIVO IN <b>STAMPATELLO</b>: A B C<br>✍️ ALLA FINE METTO LA <b>FIRMA</b>.", "") + "\n    </div>"),
    slide("🗣️ ALLO SPORTELLO", dialogo([
        ("IMPIEGATO", "BUONGIORNO. COME SI CHIAMA?"), ("*AMINA", "BUONGIORNO. MI CHIAMO AMINA DIALLO."),
        ("IMPIEGATO", "DI DOV'È?"), ("*AMINA", "SONO SENEGALESE."),
        ("IMPIEGATO", "QUANDO È NATA?"), ("*AMINA", "IL 12 MARZO 1995."),
        ("IMPIEGATO", "HA IL PERMESSO DI SOGGIORNO?"), ("*AMINA", "SÌ, ECCO."),
        ("IMPIEGATO", "GRAZIE. FIRMI QUI, PER FAVORE."), ("*AMINA", "VA BENE. GRAZIE, ARRIVEDERCI!")])),
    end("ORA SAI DIRE E SCRIVERE I TUOI DATI!"),
]

DATI = {
 "title": "🪪 I miei dati · Esercizi",
 "store": "dati-personali",
 "upper": True,
 "sections": [
  {"part": "Il modulo"},
  {"id": "e1", "title": "1 · Che cosa scrivo nel modulo?", "short": "1 · Il modulo", "type": "select",
   "cons": "LEGGI LA DOMANDA. SCEGLI LA PAROLA DEL MODULO.",
   "opts": ["NOME", "COGNOME", "DATA DI NASCITA", "LUOGO DI NASCITA", "CITTADINANZA", "INDIRIZZO", "TELEFONO"],
   "items": [{"q": q} for q in ["1. COME TI CHIAMI?", "2. QUAL È IL NOME DELLA TUA FAMIGLIA?", "3. QUANDO SEI NATO?",
                                 "4. DOVE SEI NATO?", "5. DI CHE PAESE SEI?", "6. DOVE ABITI?", "7. QUAL È IL TUO NUMERO?"]],
   "k": [eq(a) for a in ["NOME", "COGNOME", "DATA DI NASCITA", "LUOGO DI NASCITA", "CITTADINANZA", "INDIRIZZO", "TELEFONO"]]},
  {"id": "e2", "title": "2 · Leggi il modulo di Karim: vero o falso?", "short": "2 · Vero o falso", "type": "choice",
   "opts": ["VERO", "FALSO"], "full": True,
   "info": "COGNOME: <b>HADDAD</b> · NOME: <b>KARIM</b> · SESSO: <b>M</b><br>DATA DI NASCITA: <b>05/07/1998</b> · "
           "LUOGO DI NASCITA: <b>CASABLANCA (MAROCCO)</b><br>CITTADINANZA: <b>MAROCCHINA</b> · "
           "INDIRIZZO: <b>VIA CRISANZIO 25, BARI</b> · TELEFONO: <b>347 555 0102</b>",
   "items": [{"q": q} for q in ["1. IL NOME È HADDAD.", "2. KARIM È UN UOMO.", "3. KARIM È NATO A LUGLIO.",
                                 "4. KARIM È NATO IN MAROCCO.", "5. KARIM ABITA A CASABLANCA.", "6. IL COGNOME È HADDAD."]],
   "k": [eq(a) for a in ["FALSO", "VERO", "VERO", "VERO", "FALSO", "VERO"]]},

  {"part": "Mi presento"},
  {"id": "e3", "title": "3 · Completa: Amina si presenta", "short": "3 · Mi presento", "type": "cloze",
   "cons": "SCRIVI LA PAROLA GIUSTA.", "bank": "MI CHIAMO · SONO · HO · ABITO",
   "parts": ["CIAO! ", {}, " AMINA DIALLO.<br>", {}, " SENEGALESE.<br>", {}, " 30 ANNI.<br>", {}, " A BARI, IN VIA SPARANO."],
   "k": [eq("mi chiamo"), eq("sono"), eq("ho"), eq("abito")]},
  {"id": "e4", "title": "4 · Tu o Lei?", "short": "4 · Tu o Lei", "type": "choice",
   "opts": ["INFORMALE (TU)", "FORMALE (LEI)"], "full": True,
   "cons": "LA DOMANDA È CON IL TU (AMICI) O CON IL LEI (UFFICIO)?",
   "items": [{"q": q} for q in ["1. COME TI CHIAMI?", "2. COME SI CHIAMA?", "3. DOVE ABITA?",
                                 "4. QUANTI ANNI HAI?", "5. DI DOV'È?", "6. DI DOVE SEI?"]],
   "k": [eq(a) for a in ["INFORMALE (TU)", "FORMALE (LEI)", "FORMALE (LEI)", "INFORMALE (TU)", "FORMALE (LEI)", "INFORMALE (TU)"]]},

  {"part": "I documenti"},
  {"id": "e5", "title": "5 · Che documento è?", "short": "5 · I documenti", "type": "select",
   "opts": ["IL PASSAPORTO", "IL PERMESSO DI SOGGIORNO", "LA CARTA D'IDENTITÀ", "LA TESSERA SANITARIA", "IL CODICE FISCALE"],
   "items": [{"q": q} for q in ["🏥 1. PER ANDARE DAL MEDICO E IN FARMACIA", "✈️ 2. PER VIAGGIARE IN UN ALTRO PAESE",
                                 "🇮🇹 3. PER STARE IN ITALIA. LO DÀ LA QUESTURA", "🔢 4. 16 LETTERE E NUMERI",
                                 "🏛️ 5. IL DOCUMENTO DEL COMUNE"]],
   "k": [eq(a) for a in ["LA TESSERA SANITARIA", "IL PASSAPORTO", "IL PERMESSO DI SOGGIORNO", "IL CODICE FISCALE", "LA CARTA D'IDENTITÀ"]]},
  {"id": "e6", "title": "6 · Scrivi la data con le parole", "short": "6 · La data", "type": "text", "w": "m",
   "cons": "ESEMPIO: 12/03 → 12 MARZO",
   "bank": "GENNAIO · FEBBRAIO · MARZO · APRILE · MAGGIO · GIUGNO · LUGLIO · AGOSTO · SETTEMBRE · OTTOBRE · NOVEMBRE · DICEMBRE",
   "items": [{"q": q} for q in ["1. 05/07", "2. 20/01", "3. 15/08", "4. 03/10", "5. 25/12"]],
   "k": [eq("5 luglio", "05 luglio", "cinque luglio"), eq("20 gennaio", "venti gennaio"), eq("15 agosto", "quindici agosto"),
         eq("3 ottobre", "03 ottobre", "tre ottobre"), eq("25 dicembre", "venticinque dicembre")]},

  {"part": "Allo sportello"},
  {"id": "e7", "title": "7 · Rispondi all'impiegato", "short": "7 · Allo sportello", "type": "select",
   "cons": "L'IMPIEGATO FA UNA DOMANDA. SCEGLI LA RISPOSTA GIUSTA.",
   "opts": ["MI CHIAMO AMINA DIALLO.", "SONO SENEGALESE.", "IL 12 MARZO 1995.", "SÌ, ECCO IL PERMESSO.", "IN VIA SPARANO 10."],
   "items": [{"q": q} for q in ["1. COME SI CHIAMA?", "2. DOVE ABITA?", "3. QUANDO È NATA?", "4. DI DOV'È?",
                                 "5. HA UN DOCUMENTO?"]],
   "k": [eq(a) for a in ["MI CHIAMO AMINA DIALLO.", "IN VIA SPARANO 10.", "IL 12 MARZO 1995.", "SONO SENEGALESE.", "SÌ, ECCO IL PERMESSO."]]},
  {"id": "e8", "title": "8 ✎ · Compila il tuo modulo", "type": "free", "rows": 1,
   "cons": "SCRIVI IN STAMPATELLO. SE VUOI, PUOI USARE DATI INVENTATI.",
   "items": ["COGNOME", "NOME", "DATA DI NASCITA", "LUOGO DI NASCITA", "CITTADINANZA", "INDIRIZZO", "TELEFONO"]},
  {"id": "e9", "title": "9 🎤 · Presentati a voce", "type": "record",
   "items": ["DI' IL TUO NOME E COGNOME, DI DOVE SEI, QUANTI ANNI HAI E DOVE ABITI."]},
 ]
}

# =====================================================================
# 2. CHE ORE SONO? GIORNI E MESI
# =====================================================================
ORE_CSS = """
  .orologi{display:grid; grid-template-columns:repeat(4,1fr); gap:14px;}
  .orologi div{background:#fff; border:3px solid #f3e1cc; border-radius:16px; padding:14px; text-align:center; font-size:1.4rem; font-weight:bold;}
  .orologi .ora{display:block; font-size:2.4rem; color:var(--blu); font-family:monospace; margin-bottom:6px;}
  .cartello{background:#fff; border:5px solid var(--teal); border-radius:18px; padding:18px 24px; font-size:1.6rem; line-height:1.6; max-width:700px;}
  @media (max-width:900px){ .orologi{grid-template-columns:1fr 1fr;} .orologi div{font-size:1.05rem;} .orologi .ora{font-size:1.7rem;} .cartello{font-size:1.15rem;} }"""

def orologi(items):
    return '    <div class="orologi">\n' + "".join(
        '      <div><span class="ora">%s</span>%s</div>\n' % i for i in items) + "    </div>"

ORE_SLIDE = [
    cover("🕐", "CHE ORE SONO?", "I GIORNI, I MESI, LE ORE", "LA SETTIMANA &bull; L'ANNO &bull; L'ORARIO"),
    slide("CHE COSA IMPARIAMO?", cards([
        ("📅", "I GIORNI DELLA SETTIMANA", "LUNEDÌ, MARTEDÌ, MERCOLEDÌ…"), ("🗓️", "I MESI E LE STAGIONI", "GENNAIO, FEBBRAIO… L'INVERNO, L'ESTATE"),
        ("🕐", "LE ORE", "SONO LE TRE. È L'UNA."), ("🏢", "GLI ORARI", "L'UFFICIO È APERTO DALLE 9 ALLE 13.")])),
    slide("📅 I GIORNI DELLA SETTIMANA", table([
        ["1", "<b>LUNEDÌ</b>"], ["2", "<b>MARTEDÌ</b>"], ["3", "<b>MERCOLEDÌ</b>"], ["4", "<b>GIOVEDÌ</b>"],
        ["5", "<b>VENERDÌ</b>"], ["6", "<b>SABATO</b>"], ["7", "<b>DOMENICA</b>"]]) + "\n" +
        nota("SABATO E DOMENICA = IL <b>FINE SETTIMANA</b>. LA DOMENICA MOLTI NEGOZI SONO CHIUSI.")),
    slide("⏪ IERI, OGGI, DOMANI ⏩", cards([
        ("⏪", "IERI", "IERI ERA LUNEDÌ."), ("📍", "OGGI", "OGGI È MARTEDÌ."), ("⏩", "DOMANI", "DOMANI È MERCOLEDÌ.")], cols="g3") + "\n" +
        dialogo([("DOMANDA", "CHE GIORNO È OGGI?"), ("*RISPOSTA", "OGGI È MARTEDÌ 28 OTTOBRE.")])),
    slide("🗓️ I MESI DELL'ANNO", '    <div class="mondo">\n' + "".join(
        "      <div>%s<span>%s</span></div>\n" % (m, n) for n, m in enumerate(
            ["GENNAIO", "FEBBRAIO", "MARZO", "APRILE", "MAGGIO", "GIUGNO", "LUGLIO", "AGOSTO",
             "SETTEMBRE", "OTTOBRE", "NOVEMBRE", "DICEMBRE"], 1)) + "    </div>\n" +
        nota("IN QUALE MESE È IL TUO COMPLEANNO? 🎂 IL MIO COMPLEANNO È A MARZO.")),
    slide("🌸 LE STAGIONI", cards([
        ("🌸", "LA PRIMAVERA", "MARZO, APRILE, MAGGIO"), ("☀️", "L'ESTATE", "GIUGNO, LUGLIO, AGOSTO"),
        ("🍂", "L'AUTUNNO", "SETTEMBRE, OTTOBRE, NOVEMBRE"), ("❄️", "L'INVERNO", "DICEMBRE, GENNAIO, FEBBRAIO")])),
    slide("🕐 CHE ORE SONO?", orologi([
        ("1:00", "È L'UNA"), ("2:00", "SONO LE DUE"), ("3:00", "SONO LE TRE"), ("8:00", "SONO LE OTTO"),
        ("12:00", "È MEZZOGIORNO"), ("24:00", "È MEZZANOTTE"), ("15:00", "SONO LE QUINDICI<br><small>= LE TRE DEL POMERIGGIO</small>"),
        ("20:00", "SONO LE VENTI<br><small>= LE OTTO DI SERA</small>")]) + "\n" +
        nota("1 → <b>È</b> L'UNA &nbsp;&nbsp; 2, 3, 4… → <b>SONO</b> LE DUE, LE TRE, LE QUATTRO")),
    slide("🕧 E MEZZA, E UN QUARTO, MENO UN QUARTO", orologi([
        ("3:10", "SONO LE TRE E DIECI"), ("3:15", "SONO LE TRE E UN QUARTO"), ("3:30", "SONO LE TRE E MEZZA"),
        ("3:45", "SONO LE QUATTRO MENO UN QUARTO"), ("3:50", "SONO LE QUATTRO MENO DIECI"), ("9:30", "SONO LE NOVE E MEZZA"),
        ("1:15", "È L'UNA E UN QUARTO"), ("12:30", "È MEZZOGIORNO E MEZZA")]) + "\n" +
        nota("15 MINUTI = UN QUARTO &nbsp;&nbsp; 30 MINUTI = MEZZA")),
    slide("⏰ A CHE ORA?", dialogo([
        ("DOMANDA", "A CHE ORA COMINCIA LA LEZIONE?"), ("*RISPOSTA", "<b>ALLE</b> NOVE."),
        ("DOMANDA", "A CHE ORA FINISCI DI LAVORARE?"), ("*RISPOSTA", "<b>ALLE</b> CINQUE. / <b>ALL'</b>UNA."),
        ("DOMANDA", "QUANDO È APERTO IL NEGOZIO?"), ("*RISPOSTA", "<b>DALLE</b> 9 <b>ALLE</b> 13.")]) + "\n" +
        nota("CHE ORE SONO? → SONO LE NOVE. &nbsp;&nbsp; A CHE ORA? → ALLE NOVE.")),
    slide("🏢 LEGGO UN ORARIO", '    <div class="twocol2">\n    <div class="cartello">🏛️ <b>UFFICIO ANAGRAFE</b><br>'
          "LUNEDÌ – VENERDÌ: 9:00 – 12:30<br>MARTEDÌ E GIOVEDÌ ANCHE: 15:30 – 17:30<br>SABATO E DOMENICA: <b>CHIUSO</b></div>\n" +
          nota("L'UFFICIO È <b>APERTO</b> DAL LUNEDÌ AL VENERDÌ, DALLE 9 ALLE 12 E MEZZA.<br>"
               "IL MARTEDÌ E IL GIOVEDÌ È APERTO ANCHE IL POMERIGGIO.<br>IL SABATO È <b>CHIUSO</b>.", "") + "\n    </div>"),
    end("ORA SAI DIRE I GIORNI, I MESI E LE ORE!"),
]

ORE = {
 "title": "🕐 Che ore sono? · Esercizi",
 "store": "ore-giorni",
 "upper": True,
 "sections": [
  {"part": "I giorni"},
  {"id": "e1", "title": "1 · Che giorno viene dopo?", "short": "1 · I giorni", "type": "text", "w": "m",
   "cons": "SCRIVI IL GIORNO DOPO. ESEMPIO: LUNEDÌ → MARTEDÌ",
   "items": [{"q": q} for q in ["1. MARTEDÌ →", "2. GIOVEDÌ →", "3. SABATO →", "4. DOMENICA →", "5. MERCOLEDÌ →"]],
   "k": [eq("mercoledi"), eq("venerdi"), eq("domenica"), eq("lunedi"), eq("giovedi")]},
  {"id": "e2", "title": "2 · Ieri, oggi, domani", "short": "2 · Ieri e domani", "type": "cloze",
   "cons": "OGGI È VENERDÌ. COMPLETA.",
   "parts": ["OGGI È VENERDÌ.<br>IERI ERA ", {}, ".<br>DOMANI È ", {}, ".<br>IL FINE SETTIMANA È SABATO E ", {}, "."],
   "k": [eq("giovedi"), eq("sabato"), eq("domenica")]},

  {"part": "I mesi e le stagioni"},
  {"id": "e3", "title": "3 · Il numero e il mese", "short": "3 · I mesi", "type": "select",
   "opts": ["GENNAIO", "FEBBRAIO", "MARZO", "APRILE", "MAGGIO", "GIUGNO", "LUGLIO", "AGOSTO", "SETTEMBRE", "OTTOBRE", "NOVEMBRE", "DICEMBRE"],
   "items": [{"q": q} for q in ["1. IL MESE 3", "2. IL MESE 8", "3. IL MESE 1", "4. IL MESE 12", "5. IL MESE 6", "6. IL MESE 10"]],
   "k": [eq(a) for a in ["MARZO", "AGOSTO", "GENNAIO", "DICEMBRE", "GIUGNO", "OTTOBRE"]]},
  {"id": "e4", "title": "4 · Che stagione è?", "short": "4 · Le stagioni", "type": "choice",
   "opts": ["PRIMAVERA", "ESTATE", "AUTUNNO", "INVERNO"],
   "items": [{"q": q} for q in ["1. 🌸 APRILE", "2. ❄️ GENNAIO", "3. ☀️ LUGLIO", "4. 🍂 NOVEMBRE", "5. 🌸 MAGGIO", "6. ☀️ AGOSTO"]],
   "k": [eq(a) for a in ["PRIMAVERA", "INVERNO", "ESTATE", "AUTUNNO", "PRIMAVERA", "ESTATE"]]},

  {"part": "Le ore"},
  {"id": "e5", "title": "5 · Che ore sono? Scegli", "short": "5 · Le ore", "type": "select",
   "opts": ["È L'UNA", "SONO LE DUE E MEZZA", "SONO LE OTTO E UN QUARTO", "È MEZZOGIORNO", "SONO LE SEI MENO UN QUARTO", "SONO LE DIECI E DIECI"],
   "items": [{"q": q} for q in ["🕐 1. 12:00", "🕐 2. 8:15", "🕐 3. 1:00", "🕐 4. 2:30", "🕐 5. 10:10", "🕐 6. 5:45"]],
   "k": [eq(a) for a in ["È MEZZOGIORNO", "SONO LE OTTO E UN QUARTO", "È L'UNA", "SONO LE DUE E MEZZA", "SONO LE DIECI E DIECI", "SONO LE SEI MENO UN QUARTO"]]},
  {"id": "e6", "title": "6 · È o SONO?", "short": "6 · È o sono", "type": "choice",
   "opts": ["È", "SONO"],
   "items": [{"q": q} for q in ["1. … LE TRE.", "2. … L'UNA.", "3. … MEZZOGIORNO.", "4. … LE NOVE E MEZZA.", "5. … MEZZANOTTE.", "6. … LE UNDICI."]],
   "k": [eq(a) for a in ["SONO", "È", "È", "SONO", "È", "SONO"]]},
  {"id": "e7", "title": "7 · Scrivi l'ora con le parole", "short": "7 · Scrivi l'ora", "type": "text", "w": "w",
   "cons": "ESEMPIO: 4:00 → SONO LE QUATTRO",
   "items": [{"q": q} for q in ["1. 7:00", "2. 9:30", "3. 11:15", "4. 1:00"]],
   "k": [eq("sono le sette"), eq("sono le nove e mezza", "sono le nove e mezzo", "sono le nove e trenta"),
         eq("sono le undici e un quarto", "sono le undici e quindici"), eq("e l'una", "è l'una")]},

  {"part": "Gli orari"},
  {"id": "e8", "title": "8 · Leggi l'orario della farmacia", "short": "8 · L'orario", "type": "choice",
   "opts": ["VERO", "FALSO"], "full": True,
   "info": "💊 <b>FARMACIA SAN NICOLA</b><br>LUNEDÌ – SABATO: 8:30 – 13:00 E 16:30 – 20:00<br>DOMENICA: <b>CHIUSO</b>",
   "items": [{"q": q} for q in ["1. LA FARMACIA È APERTA IL LUNEDÌ.", "2. LA DOMENICA È APERTA.", "3. APRE ALLE OTTO E MEZZA.",
                                 "4. ALLE DUE DEL POMERIGGIO (14:00) È APERTA.", "5. CHIUDE ALLE OTTO DI SERA.", "6. IL SABATO È APERTA."]],
   "k": [eq(a) for a in ["VERO", "FALSO", "VERO", "FALSO", "VERO", "VERO"]]},
  {"id": "e9", "title": "9 ✎ · La mia settimana", "type": "free", "rows": 4,
   "items": ["CHE COSA FAI OGNI GIORNO? A CHE ORA? ESEMPIO: IL LUNEDÌ ALLE NOVE VADO A SCUOLA. IL SABATO LAVORO."]},
 ]
}

# =====================================================================
# 3. GLI EURO: QUANTO COSTA?
# =====================================================================
EURO_CSS = """
  .soldi{display:flex; flex-wrap:wrap; gap:16px; justify-content:center; margin:10px 0;}
  .moneta{width:96px; height:96px; border-radius:50%; display:flex; align-items:center; justify-content:center; text-align:center; font-weight:bold; font-size:1.2rem; border:5px solid #b8860b; background:radial-gradient(circle at 35% 35%,#ffe9a0,#d4a72c); color:#4a3000; line-height:1.1;}
  .moneta.rame{border-color:#8b4513; background:radial-gradient(circle at 35% 35%,#f2b48a,#b8673a); color:#3a1600;}
  .moneta.due{background:radial-gradient(circle at 50% 50%,#e7e7e7 0 45%,#d4a72c 46%); }
  .moneta.uno{background:radial-gradient(circle at 50% 50%,#d4a72c 0 45%,#e7e7e7 46%); }
  .banconota{width:170px; height:92px; border-radius:10px; display:flex; align-items:center; justify-content:center; font-size:2rem; font-weight:bold; color:#fff; text-shadow:0 2px 3px rgba(0,0,0,.4); box-shadow:0 4px 10px rgba(0,0,0,.15);}
  .scontrino{background:#fff; font-family:monospace; font-size:1.4rem; border:2px dashed #999; padding:18px 24px; max-width:420px; line-height:1.5;}
  @media (max-width:900px){ .moneta{width:70px; height:70px; font-size:.95rem;} .banconota{width:120px; height:66px; font-size:1.4rem;} .scontrino{font-size:1.05rem;} }"""

EURO_SLIDE = [
    cover("💶", "GLI EURO", "QUANTO COSTA? QUANTO COSTANO?", "LE MONETE &bull; LE BANCONOTE &bull; I PREZZI &bull; ALLA CASSA"),
    slide("CHE COSA IMPARIAMO?", cards([
        ("🪙", "LE MONETE", "1, 2, 5, 10, 20, 50 CENTESIMI · 1 E 2 EURO"), ("💵", "LE BANCONOTE", "5, 10, 20, 50, 100, 200 EURO"),
        ("🏷️", "I PREZZI", "2,50 € = DUE EURO E CINQUANTA"), ("🧾", "ALLA CASSA", "IL TOTALE, IL RESTO, LO SCONTRINO")])),
    slide("🪙 LE MONETE", '    <div class="soldi">\n' + "".join(
        '      <div class="moneta%s">%s</div>\n' % c for c in [
            (" rame", "1<br>CENT"), (" rame", "2<br>CENT"), (" rame", "5<br>CENT"), ("", "10<br>CENT"),
            ("", "20<br>CENT"), ("", "50<br>CENT"), (" uno", "1 €"), (" due", "2 €")]) + "    </div>\n" +
        nota("100 CENTESIMI = 1 EURO<br>CENT = CENTESIMI")),
    slide("💵 LE BANCONOTE", '    <div class="soldi">\n' + "".join(
        '      <div class="banconota" style="background:%s">%s €</div>\n' % c for c in [
            ("#8a8d91", "5"), ("#d0473f", "10"), ("#3a7bd5", "20"), ("#e67e22", "50"), ("#2e9e5b", "100"), ("#c9a227", "200")]) +
        "    </div>\n" + nota("€ = EURO. &nbsp; UNA BANCONOTA, DUE BANCONOTE. &nbsp; UNA MONETA, DUE MONETE.")),
    slide("🏷️ COME SI LEGGE IL PREZZO?", table([
        ["1 €", "UN EURO"], ["3 €", "TRE EURO"], ["2,50 €", "DUE EURO E CINQUANTA"], ["0,80 €", "OTTANTA CENTESIMI"],
        ["1,20 €", "UN EURO E VENTI"], ["10,99 €", "DIECI EURO E NOVANTANOVE"]], head=["IL PREZZO", "SI DICE"]) + "\n" +
        nota("IN ITALIA C'È LA <b>VIRGOLA</b>: 2<b>,</b>50 €")),
    slide("❓ QUANTO COSTA? QUANTO COSTANO?", '    <div class="twocol2">\n' + dialogo([
        ("DOMANDA", "QUANTO <b>COSTA</b> IL PANE?"), ("*RISPOSTA", "<b>COSTA</b> 2 EURO."),
        ("DOMANDA", "QUANTO <b>COSTANO</b> LE MELE?"), ("*RISPOSTA", "<b>COSTANO</b> 1 EURO E 80 AL CHILO.")]) + "\n" +
        nota("1 COSA → <b>COSTA</b><br>2, 3, 4… COSE → <b>COSTANO</b><br><br>IL LATTE COSTA… / LE UOVA COSTANO…", "") + "\n    </div>"),
    slide("🧾 ALLA CASSA", '    <div class="twocol2">\n    <div class="scontrino">SUPERMERCATO<br>-----------------<br>PANE &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;2,00<br>'
          "LATTE &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;1,30<br>MELE &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;4,00<br>-----------------<br><b>TOTALE &nbsp;&nbsp;&nbsp;&nbsp;7,30</b><br>"
          "CONTANTI &nbsp;&nbsp;10,00<br><b>RESTO &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;2,70</b></div>\n" +
          nota("<b>IL TOTALE</b> = QUANTO PAGO.<br><b>IL RESTO</b> = I SOLDI CHE TORNANO A ME.<br><b>LO SCONTRINO</b> = IL FOGLIO DELLA SPESA.", "") + "\n    </div>"),
    slide("🗣️ COME PAGO?", dialogo([
        ("CASSIERA", "SONO 7 EURO E 30."), ("*CLIENTE", "ECCO 10 EURO."),
        ("CASSIERA", "ECCO IL RESTO: 2 EURO E 70. VUOLE LO SCONTRINO?"), ("*CLIENTE", "SÌ, GRAZIE."),
        ("CASSIERA", "PAGA CON LA CARTA O IN CONTANTI?"), ("*CLIENTE", "CON LA CARTA. / IN CONTANTI.")])),
    slide("💡 PAROLE UTILI", cards([
        ("💰", "CARO", "COSTA TANTO"), ("👍", "ECONOMICO", "COSTA POCO"),
        ("🏷️", "LO SCONTO", "-50% = METÀ PREZZO"), ("⭐", "L'OFFERTA", "OGGI COSTA MENO"),
        ("💳", "LA CARTA", "IL BANCOMAT"), ("💶", "I CONTANTI", "MONETE E BANCONOTE")], cols="g3")),
    end("ORA SAI LEGGERE I PREZZI E PAGARE!"),
]

EURO = {
 "title": "💶 Gli euro · Esercizi",
 "store": "euro",
 "upper": True,
 "sections": [
  {"part": "I prezzi"},
  {"id": "e1", "title": "1 · Come si dice il prezzo?", "short": "1 · Leggi il prezzo", "type": "select",
   "opts": ["DUE EURO E CINQUANTA", "CINQUANTA CENTESIMI", "UN EURO E VENTI", "CINQUE EURO", "DODICI EURO E NOVANTA", "VENTI CENTESIMI"],
   "items": [{"q": q} for q in ["🏷️ 1. 5,00 €", "🏷️ 2. 0,50 €", "🏷️ 3. 2,50 €", "🏷️ 4. 12,90 €", "🏷️ 5. 1,20 €", "🏷️ 6. 0,20 €"]],
   "k": [eq(a) for a in ["CINQUE EURO", "CINQUANTA CENTESIMI", "DUE EURO E CINQUANTA", "DODICI EURO E NOVANTA", "UN EURO E VENTI", "VENTI CENTESIMI"]]},
  {"id": "e2", "title": "2 · Scrivi il prezzo con i numeri", "short": "2 · Scrivi il prezzo", "type": "text", "w": "s",
   "cons": "ESEMPIO: TRE EURO E VENTI → 3,20", "items": [{"q": q, "post": " €"} for q in [
       "1. QUATTRO EURO", "2. UN EURO E CINQUANTA", "3. SETTANTA CENTESIMI", "4. DIECI EURO E TRENTA", "5. DUE EURO E NOVANTANOVE"]],
   "k": [eq("4", "4,00", "4 €", "4€"), eq("1,50", "1,5", "1,50 €", "1,50€"), eq("0,70", "0,7", "0,70 €", "0,70€"),
         eq("10,30", "10,3", "10,30 €", "10,30€"), eq("2,99", "2,99 €", "2,99€")]},

  {"part": "Costa o costano?"},
  {"id": "e3", "title": "3 · COSTA o COSTANO?", "short": "3 · Costa o costano", "type": "choice",
   "opts": ["COSTA", "COSTANO"],
   "items": [{"q": q} for q in ["1. QUANTO … IL PANE?", "2. QUANTO … LE PATATE?", "3. QUANTO … IL LATTE?",
                                 "4. QUANTO … I POMODORI?", "5. QUANTO … LA PASTA?", "6. QUANTO … LE UOVA?"]],
   "k": [eq(a) for a in ["COSTA", "COSTANO", "COSTA", "COSTANO", "COSTA", "COSTANO"]]},

  {"part": "Alla cassa"},
  {"id": "e4", "title": "4 · Quanto è il resto?", "short": "4 · Il resto", "type": "text", "w": "s",
   "cons": "ESEMPIO: COSTA 3 €. PAGO CON 5 €. IL RESTO È 2 €.",
   "items": [{"q": q, "post": " €"} for q in ["1. COSTA 4 €. PAGO CON 5 €. IL RESTO È", "2. COSTA 7 €. PAGO CON 10 €. IL RESTO È",
                                              "3. COSTA 15 €. PAGO CON 20 €. IL RESTO È", "4. COSTA 1,50 €. PAGO CON 2 €. IL RESTO È"]],
   "k": [eq("1", "1,00", "1 €"), eq("3", "3,00", "3 €"), eq("5", "5,00", "5 €"), eq("0,50", "0,5", "0,50 €", "50 centesimi")]},
  {"id": "e5", "title": "5 · Leggi lo scontrino", "short": "5 · Lo scontrino", "type": "select",
   "info": '<div style="font-family:monospace">PASTA ....... 1,20<br>POMODORI .... 2,80<br>ACQUA ....... 0,90<br>'
           "<b>TOTALE ...... 4,90</b><br>CONTANTI .... 5,00<br><b>RESTO ....... 0,10</b></div>",
   "opts": ["1,20 €", "2,80 €", "0,90 €", "4,90 €", "5,00 €", "0,10 €"],
   "items": [{"q": q} for q in ["1. QUANTO COSTA LA PASTA?", "2. QUANTO COSTANO I POMODORI?", "3. QUANTO È IL TOTALE?",
                                 "4. QUANTI SOLDI DÀ IL CLIENTE?", "5. QUANTO È IL RESTO?"]],
   "k": [eq(a) for a in ["1,20 €", "2,80 €", "4,90 €", "5,00 €", "0,10 €"]]},
  {"id": "e6", "title": "6 · Completa il dialogo", "short": "6 · Il dialogo", "type": "cloze",
   "bank": "COSTA · RESTO · CARTA · SCONTRINO",
   "parts": ["CLIENTE: QUANTO ", {}, " QUESTO PANE?<br>CASSIERE: 2 EURO.<br>CLIENTE: ECCO 5 EURO.<br>CASSIERE: ECCO IL ", {},
             ": 3 EURO. VUOLE LO ", {}, "?<br>CLIENTE: SÌ, GRAZIE. DOMANI PAGO CON LA ", {}, "."],
   "k": [eq("costa"), eq("resto"), eq("scontrino"), eq("carta")]},
  {"id": "e7", "title": "7 🎤 · Chiedi il prezzo", "type": "record",
   "items": ["CHIEDI IL PREZZO DI DUE COSE: «QUANTO COSTA…?» E «QUANTO COSTANO…?»"]},
 ]
}

# =====================================================================
# 4. AL MERCATO E AL SUPERMERCATO (A1)
# =====================================================================
MERCATO_SLIDE = [
    cover("🛒", "AL MERCATO E AL SUPERMERCATO", "VORREI UN CHILO DI MELE, PER FAVORE!", "I NEGOZI &bull; LE QUANTITÀ &bull; VORREI &bull; ALLA CASSA"),
    slide("CHE COSA IMPARIAMO?", cards([
        ("🏪", "I NEGOZI", "IL PANIFICIO, LA MACELLERIA, IL MERCATO…"), ("⚖️", "LE QUANTITÀ", "UN CHILO, UN LITRO, UN PACCO…"),
        ("🙏", "CHIEDERE CON GENTILEZZA", "VORREI… QUANTO COSTA?"), ("🛒", "AL SUPERMERCATO", "IL REPARTO, LA CASSA, LA BUSTA")])),
    slide("🏪 DOVE COMPRO?", cards([
        ("🥖", "IL PANIFICIO", "IL PANE, LA FOCACCIA"), ("🥩", "LA MACELLERIA", "LA CARNE, IL POLLO"),
        ("🐟", "LA PESCHERIA", "IL PESCE"), ("🍅", "IL FRUTTIVENDOLO", "LA FRUTTA E LA VERDURA"),
        ("🧺", "IL MERCATO", "TANTE BANCARELLE: FRUTTA, VESTITI…"), ("🛒", "IL SUPERMERCATO", "TUTTO!")], cols="g3")),
    slide("⚖️ LE QUANTITÀ", table([
        ["⚖️ UN CHILO (1 KG) DI…", "MELE, PATATE, PASTA"], ["⚖️ MEZZO CHILO (1/2 KG) DI…", "POMODORI, CIPOLLE"],
        ["⚖️ UN ETTO (100 G) DI…", "PROSCIUTTO, FORMAGGIO"], ["🥛 UN LITRO DI…", "LATTE, OLIO"],
        ["🍾 UNA BOTTIGLIA DI…", "ACQUA, OLIO"], ["📦 UN PACCO DI…", "PASTA, BISCOTTI, ZUCCHERO"],
        ["🥫 UNA SCATOLA DI…", "TONNO, PELATI"], ["🥚 UNA CONFEZIONE DA 6…", "UOVA"]], head=["QUANTO?", "CHE COSA?"])),
    slide("🙏 VORREI = VOGLIO, MA PIÙ GENTILE", '    <div class="twocol2">\n' + dialogo([
        ("CLIENTE", "<b>VORREI</b> UN CHILO DI MELE, PER FAVORE."), ("CLIENTE", "<b>VORREI</b> DUE ETTI DI PROSCIUTTO."),
        ("CLIENTE", "<b>VORREI</b> UNA BOTTIGLIA D'ACQUA.")]) + "\n" +
        nota("😐 VOGLIO IL PANE. &nbsp;→&nbsp; 🙂 <b>VORREI</b> IL PANE, PER FAVORE.<br><br>"
             "UN CHILO <b>DI</b> MELE · UN LITRO <b>DI</b> LATTE · UNA BOTTIGLIA <b>D'</b>ACQUA", "") + "\n    </div>"),
    slide("🍅 AL MERCATO, DAL FRUTTIVENDOLO", dialogo([
        ("*VENDITORE", "BUONGIORNO, SIGNORA! DICA!"), ("CLIENTE", "BUONGIORNO. VORREI UN CHILO DI POMODORI."),
        ("*VENDITORE", "ECCO. ALTRO?"), ("CLIENTE", "SÌ, MEZZO CHILO DI CIPOLLE."),
        ("*VENDITORE", "BASTA COSÌ?"), ("CLIENTE", "SÌ, BASTA COSÌ. QUANTO PAGO?"),
        ("*VENDITORE", "3 EURO E 50."), ("CLIENTE", "ECCO A LEI. GRAZIE, ARRIVEDERCI!")])),
    slide("🛒 AL SUPERMERCATO", cards([
        ("🛒", "IL CARRELLO", "PER METTERE LA SPESA"), ("🧺", "IL CESTINO", "PER POCHE COSE"),
        ("🥫", "IL REPARTO", "IL REPARTO FRUTTA, IL REPARTO PANE…"), ("💳", "LA CASSA", "QUI PAGO"),
        ("🛍️", "LA BUSTA", "PER PORTARE A CASA LA SPESA"), ("🧾", "LO SCONTRINO", "IL FOGLIO CON I PREZZI")], cols="g3")),
    slide("🗣️ AL SUPERMERCATO: LE DOMANDE", dialogo([
        ("CLIENTE", "SCUSI, DOVE SONO I BISCOTTI?"), ("*COMMESSO", "NEL REPARTO COLAZIONE, IN FONDO A DESTRA."),
        ("*CASSIERA", "BUONASERA. VUOLE UNA BUSTA?"), ("CLIENTE", "SÌ, UNA, GRAZIE."),
        ("*CASSIERA", "HA LA TESSERA DEL SUPERMERCATO?"), ("CLIENTE", "NO, NON CE L'HO."),
        ("*CASSIERA", "SONO 12 EURO E 40.")])),
    slide("📝 LA LISTA DELLA SPESA", '    <div class="twocol2">\n    <div class="scontrino" style="font-family:inherit">'
          "📝 <b>LA MIA LISTA</b><br>☐ 1 KG DI PASTA<br>☐ 1 LITRO DI LATTE<br>☐ 6 UOVA<br>☐ 2 ETTI DI FORMAGGIO<br>☐ 1 KG DI MELE<br>☐ 1 PACCO DI CAFFÈ</div>\n" +
          nota("PRIMA DI ANDARE A FARE LA SPESA SCRIVO LA <b>LISTA</b>.<br>COSÌ NON DIMENTICO NIENTE!", "") + "\n    </div>"),
    slide("📌 RICORDA", table([
        ["🙏 CHIEDO", "VORREI… PER FAVORE"], ["💶 IL PREZZO", "QUANTO COSTA? / QUANTO COSTANO?"],
        ["❓ IL VENDITORE", "DICA! · ALTRO? · BASTA COSÌ?"], ["✅ RISPONDO", "SÌ, BASTA COSÌ. · NO, ANCHE…"],
        ["💳 ALLA CASSA", "QUANTO PAGO? · ECCO A LEI."]])),
    end("ORA SAI FARE LA SPESA IN ITALIANO!"),
]

MERCATO = {
 "title": "🛒 Al mercato e al supermercato · Esercizi",
 "store": "mercato",
 "upper": True,
 "sections": [
  {"part": "I negozi"},
  {"id": "e1", "title": "1 · Dove compro?", "short": "1 · I negozi", "type": "select",
   "opts": ["IL PANIFICIO", "LA MACELLERIA", "LA PESCHERIA", "IL FRUTTIVENDOLO", "LA FARMACIA"],
   "items": [{"q": q} for q in ["🥖 1. IL PANE", "🐟 2. IL PESCE", "🥩 3. LA CARNE", "🍎 4. LE MELE", "💊 5. LE MEDICINE", "🥕 6. LE CAROTE"]],
   "k": [eq(a) for a in ["IL PANIFICIO", "LA PESCHERIA", "LA MACELLERIA", "IL FRUTTIVENDOLO", "LA FARMACIA", "IL FRUTTIVENDOLO"]]},

  {"part": "Le foto"},
  foto_quiz("f1", "1b · Guarda la foto: che cos'è?", "1b · Le foto",
            [("pomodori", "I POMODORI"), ("cipolle", "LE CIPOLLE"), ("uova", "LE UOVA"), ("mozzarella", "LA MOZZARELLA"), ("carote", "LE CAROTE"),
             ("riso", "IL RISO"), ("olio-oliva", "L'OLIO"), ("banane", "LE BANANE"), ("latte", "IL LATTE"), ("patate", "LE PATATE"),
             ("zucchero", "LO ZUCCHERO"), ("insalata", "L'INSALATA")],
            ["IL LATTE", "IL RISO", "L'INSALATA", "L'OLIO", "LA MOZZARELLA", "LE BANANE", "LE CAROTE", "LE CIPOLLE", "LE PATATE",
             "LE UOVA", "LO ZUCCHERO", "I POMODORI"]),
  foto_quiz("f2", "1c · Dove lo compro?", "1c · Dove compro",
            [("pane", "IL PANIFICIO"), ("mele", "IL FRUTTIVENDOLO"), ("formaggio", "IL SUPERMERCATO"), ("arance", "IL FRUTTIVENDOLO"),
             ("bistecca-manzo", "LA MACELLERIA"), ("orata", "LA PESCHERIA")],
            ["IL PANIFICIO", "LA MACELLERIA", "LA PESCHERIA", "IL FRUTTIVENDOLO", "IL SUPERMERCATO"], cons="GUARDA LA FOTO. DOVE LO COMPRO?"),
  {"part": "Le quantità"},
  {"id": "e2", "title": "2 · Quanto?", "short": "2 · Le quantità", "type": "select",
   "cons": "SCEGLI LA QUANTITÀ GIUSTA.",
   "opts": ["UN CHILO", "UN ETTO", "UN LITRO", "UN PACCO", "UNA SCATOLA", "UNA CONFEZIONE"],
   "items": [{"q": q} for q in ["1. … DI LATTE", "2. … DI PROSCIUTTO", "3. … DI PATATE", "4. … DI TONNO", "5. … DI BISCOTTI", "6. … DA 6 UOVA"]],
   "k": [eq("UN LITRO"), eq("UN ETTO"), eq("UN CHILO"), eq("UNA SCATOLA"), eq("UN PACCO"), eq("UNA CONFEZIONE")]},

  {"part": "Al mercato"},
  {"id": "e3", "title": "3 · Chi parla?", "short": "3 · Chi parla", "type": "choice",
   "opts": ["IL CLIENTE", "IL VENDITORE"], "full": True,
   "items": [{"q": q} for q in ["1. DICA!", "2. VORREI UN CHILO DI MELE.", "3. ALTRO?", "4. QUANTO PAGO?", "5. BASTA COSÌ?", "6. ECCO A LEI."]],
   "k": [eq("IL VENDITORE"), eq("IL CLIENTE"), eq("IL VENDITORE"), eq("IL CLIENTE"), eq("IL VENDITORE"), eq("IL CLIENTE", "IL VENDITORE")]},
  {"id": "e4", "title": "4 · Metti in ordine il dialogo", "short": "4 · In ordine", "type": "order",
   "cons": "SCRIVI IL NUMERO: 1 = LA PRIMA FRASE.",
   "items": ["VENDITORE: ECCO. ALTRO?", "CLIENTE: BUONGIORNO. VORREI MEZZO CHILO DI FRAGOLE.", "VENDITORE: 2 EURO E 50.",
             "VENDITORE: BUONGIORNO! DICA!", "CLIENTE: NO, BASTA COSÌ. QUANTO PAGO?", "CLIENTE: ECCO A LEI. ARRIVEDERCI!"],
   "k": [eq("3"), eq("2"), eq("5"), eq("1"), eq("4"), eq("6")]},
  {"id": "e5", "title": "5 · Completa il dialogo", "short": "5 · Il dialogo", "type": "cloze",
   "bank": "VORREI · DI · ALTRO · BASTA · QUANTO",
   "parts": ["VENDITORE: BUONGIORNO! DICA!<br>CLIENTE: ", {}, " UN CHILO ", {}, " ARANCE.<br>VENDITORE: ECCO. ", {},
             "?<br>CLIENTE: NO, ", {}, " COSÌ. ", {}, " PAGO?<br>VENDITORE: 2 EURO."],
   "k": [eq("vorrei"), eq("di"), eq("altro"), eq("basta"), eq("quanto")]},

  {"part": "Al supermercato"},
  {"id": "e6", "title": "6 · Che cos'è?", "short": "6 · Al supermercato", "type": "select",
   "opts": ["IL CARRELLO", "LA CASSA", "LA BUSTA", "LO SCONTRINO", "IL REPARTO"],
   "items": [{"q": q} for q in ["1. QUI PAGO LA SPESA.", "2. IL FOGLIO CON I PREZZI.", "3. PORTO LA SPESA A CASA DENTRO QUESTA.",
                                 "4. METTO LA SPESA DENTRO E LO SPINGO.", "5. LA PARTE DEL SUPERMERCATO CON LA FRUTTA."]],
   "k": [eq(a) for a in ["LA CASSA", "LO SCONTRINO", "LA BUSTA", "IL CARRELLO", "IL REPARTO"]]},
  {"id": "e7", "title": "7 ✎ · La tua lista della spesa", "type": "free", "rows": 5,
   "items": ["SCRIVI 5 COSE DA COMPRARE CON LA QUANTITÀ. ESEMPIO: 1 KG DI PASTA, 1 LITRO DI LATTE…"]},
  {"id": "e8", "title": "8 🎤 · Al mercato: parla", "type": "record",
   "items": ["SEI AL MERCATO. SALUTA, CHIEDI DUE COSE CON «VORREI…», CHIEDI IL PREZZO E SALUTA."]},
 ]
}

SLIDE = [
    ("dati-personali/index.html", "I MIEI DATI", "PRIMI PASSI", DATI_SLIDE, ""),
    ("ore-giorni/index.html", "CHE ORE SONO?", "PRIMI PASSI", ORE_SLIDE, ORE_CSS),
    ("euro/index.html", "GLI EURO", "PRIMI PASSI", EURO_SLIDE, EURO_CSS),
    ("mercato/index.html", "AL MERCATO", "LIVELLO A1", MERCATO_SLIDE, EURO_CSS),
]
