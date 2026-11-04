"""Unità sulle pagine «In Italia» e sull'Educazione civica di «Italiano anch'io» (Ornimi), mandate da Erila il 2026-11-04
(italiano 4.pdf = eserciziario 1-19, «parte 2 anche io» = unità 6-8, «parte 2 c» / Scan = unità 8-19 + educazione civica).
Le unità di lessico e grammatica del libro sono già sul sito (eserciziario-a1/, grammatica/, presente/, possessivi/…):
qui si fanno SOLO gli argomenti che mancavano. Testi, dialoghi ed esercizi sono scritti per il sito, ambientati a Bari.
A1 (STAMPATELLO MAIUSCOLO): condominio/, autocertificazione/, piatti-dal-mondo/, volontariato/, in-strada/, cup-specialisti/
A2 (stampatello minuscolo): tasse/, centro-periferia/, feste-repubblica/, unione-europea/, stato-italiano/, enti-locali/"""
from genera import eq
from unita_primi import cover, slide, cards, table, nota, dialogo, end
from unita_drive import ILL_CSS, vf, scegli, menu, scrivi, ordina, completa, parla, libero
from teoria import tab, es

A2_CSS = ILL_CSS + "\n  body, .btn, button{text-transform:none !important;}  /* A2: stampatello minuscolo */"

# =====================================================================
# 1. VIVERE IN CONDOMINIO (casa, A1)
# =====================================================================
COND_SLIDE = [
    cover("🏢", "VIVERE IN CONDOMINIO", "LE PARTI DEL PALAZZO E LE REGOLE PER STARE BENE INSIEME", "CASA &bull; A1"),
    slide("CHE COSA IMPARIAMO?", cards([
        ("🏢", "IL PALAZZO", "SCALE, PIANEROTTOLO, CORTILE…"), ("📜", "LE REGOLE", "IL REGOLAMENTO DEL CONDOMINIO"),
        ("🚫", "È VIETATO…", "NON SI PUÒ…"), ("🧑‍💼", "L'AMMINISTRATORE", "CHI CHIAMO SE C'È UN PROBLEMA?")])),
    slide("🏢 LE PARTI DEL PALAZZO", cards([
        ("🚪", "IL PORTONE", "L'ENTRATA DEL PALAZZO"), ("🪜", "LE SCALE", "PER SALIRE E SCENDERE"),
        ("🟫", "IL PIANEROTTOLO", "LO SPAZIO DAVANTI ALLE PORTE"), ("🛗", "L'ASCENSORE", ""),
        ("📬", "LE CASSETTE DELLA POSTA", "UNA PER OGNI FAMIGLIA"), ("🌳", "IL CORTILE", "LO SPAZIO FUORI, DI TUTTI"),
        ("🔔", "IL CITOFONO", "SUONO E PARLO"), ("🅿️", "IL GARAGE / LA CANTINA", "SOTTO IL PALAZZO"),
        ("♿", "LA RAMPA", "PER LE CARROZZINE E I PASSEGGINI")], "g3")),
    slide("🤝 CHE COS'È IL CONDOMINIO?", nota(
        "IL <b>CONDOMINIO</b> È UN PALAZZO CON TANTI APPARTAMENTI. LE FAMIGLIE ABITANO IN CASE DIVERSE, MA LE SCALE, L'ASCENSORE, "
        "IL CORTILE E IL PORTONE SONO DI <b>TUTTI</b>. PER QUESTO CI SONO DELLE <b>REGOLE</b>: IL <b>REGOLAMENTO DEL CONDOMINIO</b>.", "font-size:1.3rem;text-align:left")),
    slide("📜 LE REGOLE PIÙ IMPORTANTI", cards([
        ("🤫", "SILENZIO", "DALLE 22:00 ALLE 8:00 E DALLE 14:00 ALLE 16:00"), ("🔊", "TV E MUSICA", "NON TROPPO FORTE"),
        ("📦", "SCALE LIBERE", "È VIETATO LASCIARE BICI, SCARPE, SCATOLE SUL PIANEROTTOLO"), ("🧺", "LA TOVAGLIA", "NON SI SCUOTE DAL BALCONE"),
        ("🚬", "LE SIGARETTE", "È VIETATO BUTTARE I MOZZICONI DAL BALCONE"), ("🗑️", "LA SPAZZATURA", "SOLO NEI BIDONI, NEI GIORNI GIUSTI")], "g2")),
    slide("🧑‍💼 L'AMMINISTRATORE E LE SPESE", cards([
        ("🧑‍💼", "L'AMMINISTRATORE", "CONTROLLA IL PALAZZO E I CONTI"), ("💶", "LE SPESE CONDOMINIALI", "OGNI MESE PAGO LA MIA PARTE"),
        ("🗓️", "L'ASSEMBLEA", "LA RIUNIONE DI TUTTI I CONDOMINI"), ("📋", "IL CARTELLO NELL'ATRIO", "LEGGO GLI AVVISI")]) + "\n" +
        nota("💡 SE L'ASCENSORE NON FUNZIONA O C'È ACQUA SULLE SCALE, TELEFONO ALL'<b>AMMINISTRATORE</b>.")),
    slide("🗣️ SUL PIANEROTTOLO", dialogo([
        ("SIGNORA ROSA", "BUONGIORNO! LEI È IL NUOVO VICINO?"),
        ("*TESFAYE", "SÌ, BUONGIORNO. MI CHIAMO TESFAYE, ABITO AL TERZO PIANO."),
        ("SIGNORA ROSA", "PIACERE! SCUSI, LA SUA BICI È SUL PIANEROTTOLO. È VIETATO, LO DICE IL REGOLAMENTO."),
        ("*TESFAYE", "OH, MI DISPIACE! DOVE POSSO METTERE LA BICI?"),
        ("SIGNORA ROSA", "IN CORTILE C'È UN POSTO PER LE BICI."),
        ("*TESFAYE", "GRAZIE MILLE, SIGNORA. LA SPOSTO SUBITO.")])),
    slide("📘 È VIETATO / NON SI PUÒ", table([
        ["È VIETATO", "+ INFINITO", "È VIETATO FUMARE NELL'ASCENSORE."], ["NON SI PUÒ", "+ INFINITO", "NON SI PUÒ GIOCARE A PALLONE IN CORTILE."],
        ["BISOGNA", "+ INFINITO", "BISOGNA CHIUDERE IL PORTONE."], ["SI PUÒ", "+ INFINITO", "SI PUÒ PARCHEGGIARE LA BICI IN CORTILE."]],
        head=["", "", "ESEMPIO"])),
    end("ORA SAI LE REGOLE DEL CONDOMINIO!"),
]
COND = {
 "title": "🏢 Vivere in condominio · Esercizi", "store": "condominio", "upper": True,
 "sections": [
  {"part": "Il palazzo"},
  menu(["IL PORTONE", "LE SCALE", "IL PIANEROTTOLO", "IL CITOFONO", "IL CORTILE", "LA CASSETTA DELLA POSTA"],
       [("1. SUONO E DICO: «SONO IO, APRI!»", "IL CITOFONO"), ("2. LO SPAZIO DAVANTI ALLA PORTA DI CASA.", "IL PIANEROTTOLO"),
        ("3. QUI ARRIVANO LE LETTERE.", "LA CASSETTA DELLA POSTA"), ("4. L'ENTRATA GRANDE DEL PALAZZO.", "IL PORTONE"),
        ("5. LO SPAZIO FUORI, CON GLI ALBERI.", "IL CORTILE"), ("6. LE USO SE NON C'È L'ASCENSORE.", "LE SCALE")],
       "1 · Che cos'è?", "1 · Il palazzo", "e1"),
  vf(["1. IL CONDOMINIO È UN PALAZZO CON TANTI APPARTAMENTI.", "2. LE SCALE SONO SOLO DELLA FAMIGLIA DEL PRIMO PIANO.",
      "3. ALLE 23:00 POSSO ASCOLTARE LA MUSICA MOLTO FORTE.", "4. LA SPAZZATURA VA NEI BIDONI.",
      "5. POSSO LASCIARE LE SCARPE SUL PIANEROTTOLO.", "6. SE L'ASCENSORE NON VA, CHIAMO L'AMMINISTRATORE."],
     ["VERO", "FALSO", "FALSO", "VERO", "FALSO", "VERO"], "2 · Vero o falso?", "2 · Le regole", "e2"),
  {"part": "È vietato, si può", "teoria":
     tab(("È VIETATO", "+ INFINITO", "È VIETATO FUMARE."), ("NON SI PUÒ", "+ INFINITO", "NON SI PUÒ CORRERE SULLE SCALE."),
         ("BISOGNA", "+ INFINITO", "BISOGNA CHIUDERE IL PORTONE."), ("SI PUÒ", "+ INFINITO", "SI PUÒ METTERE LA BICI IN CORTILE.")) +
     "DOPO QUESTE PAROLE IL VERBO È ALL'<b>INFINITO</b> (-ARE, -ERE, -IRE)." + es("NON SI PUÒ <b>BUTTARE</b> LA SIGARETTA DAL BALCONE.")},
  scegli([("1. È VIETATO ___ NELL'ASCENSORE.", ["FUMARE", "FUMO", "FUMI"], "FUMARE"),
          ("2. BISOGNA ___ IL PORTONE LA SERA.", ["CHIUDERE", "CHIUDO", "CHIUDE"], "CHIUDERE"),
          ("3. NON SI PUÒ ___ LA TOVAGLIA DAL BALCONE.", ["SCUOTERE", "SCUOTO", "SCUOTONO"], "SCUOTERE"),
          ("4. SI PUÒ ___ LA BICI IN CORTILE.", ["METTERE", "METTO", "METTETE"], "METTERE")],
         "3 · Scegli il verbo giusto", "3 · L'infinito", "e3"),
  menu(["È VIETATO", "SI PUÒ"],
       [("1. ___ LASCIARE LE SCATOLE SULLE SCALE.", "È VIETATO"), ("2. ___ USARE L'ASCENSORE.", "SI PUÒ"),
        ("3. ___ FARE RUMORE ALLE 2 DI NOTTE.", "È VIETATO"), ("4. ___ PARLARE CON L'AMMINISTRATORE.", "SI PUÒ"),
        ("5. ___ BUTTARE LA SPAZZATURA DAL BALCONE.", "È VIETATO")], "4 · È vietato o si può?", "4 · Vietato o no", "e4"),
  {"part": "Sul pianerottolo"},
  completa("SIGNORA ROSA: LEI È IL NUOVO ___?<br>TESFAYE: SÌ, ABITO AL TERZO ___.<br>SIGNORA ROSA: LA SUA BICI È SUL PIANEROTTOLO. È ___.<br>"
           "TESFAYE: MI ___! DOVE LA METTO?<br>SIGNORA ROSA: IN ___ C'È UN POSTO PER LE BICI.",
           ["vicino", "piano", "vietato", "dispiace", "cortile"], "5 · Completa il dialogo", "5 · Il dialogo", "e5",
           "VICINO · PIANO · VIETATO · DISPIACE · CORTILE"),
  libero("e6", 6, "Un avviso", "SCRIVI UN AVVISO PER IL CARTELLO DEL PALAZZO: 3 REGOLE CON «È VIETATO», «BISOGNA», «SI PUÒ».", ["AVVISO PER I CONDOMINI"], rows=4),
  parla("e7", 7, "PRESENTATI A UN NUOVO VICINO: CHI SEI, A CHE PIANO ABITI, CON CHI VIVI."),
 ]
}

# =====================================================================
# 2. L'AUTOCERTIFICAZIONE DELLO STATO DI FAMIGLIA (famiglia/civica, A1)
# =====================================================================
MODULO = table([
    ["1", "DIALLO AMADOU", "DAKAR (SENEGAL)", "12/03/1988", "INTESTATARIO"],
    ["2", "BA AISSATOU", "THIÈS (SENEGAL)", "04/09/1992", "MOGLIE"],
    ["3", "DIALLO IBRAHIMA", "BARI", "21/06/2017", "FIGLIO"],
    ["4", "DIALLO AWA", "BARI", "15/01/2021", "FIGLIA"]], head=["N.", "COGNOME E NOME", "LUOGO DI NASCITA", "DATA DI NASCITA", "PARENTELA"])

AUTO_SLIDE = [
    cover("📝", "L'AUTOCERTIFICAZIONE", "LO STATO DI FAMIGLIA: CHI ABITA CON ME?", "FAMIGLIA &bull; A1"),
    slide("CHE COSA IMPARIAMO?", cards([
        ("📝", "CHE COS'È", "UN FOGLIO CHE SCRIVO E FIRMO IO"), ("👨‍👩‍👧", "LO STATO DI FAMIGLIA", "LE PERSONE DELLA MIA CASA"),
        ("📅", "LE DATE", "NATO IL 12 MARZO 1988"), ("✍️", "LA FIRMA", "DATA E FIRMA ALLA FINE")])),
    slide("📝 CHE COS'È?", nota(
        "L'<b>AUTOCERTIFICAZIONE</b> È UN FOGLIO CHE <b>SCRIVO IO</b>. NON VADO IN COMUNE A CHIEDERE IL CERTIFICATO: "
        "SCRIVO I MIEI DATI E <b>FIRMO</b>. SE SCRIVO UNA COSA FALSA, È UN REATO.", "font-size:1.3rem;text-align:left") + "\n" +
        nota("💡 LA POSSONO USARE GLI ITALIANI, I CITTADINI EUROPEI E GLI STRANIERI CON IL PERMESSO DI SOGGIORNO, PER I DATI CHE SONO IN ITALIA.")),
    slide("👨‍👩‍👧 A CHE COSA SERVE?", cards([
        ("🏫", "A SCUOLA", "PER ISCRIVERE I FIGLI"), ("🏦", "IN BANCA", "PER UN MUTUO (UN PRESTITO PER LA CASA)"),
        ("💶", "PER I BONUS", "AIUTI E SOLDI PER LE FAMIGLIE"), ("🏥", "ALL'ASL", "PER IL MEDICO DEI BAMBINI")])),
    slide("📋 IL MODULO DELLA FAMIGLIA DIALLO", nota("IO SOTTOSCRITTO <b>DIALLO AMADOU</b>, NATO A <b>DAKAR (SENEGAL)</b> IL <b>12/03/1988</b>, "
        "DICHIARO CHE LA MIA FAMIGLIA, RESIDENTE A <b>BARI</b> IN <b>VIA CAPRUZZI 15</b>, È COSÌ COMPOSTA:", "text-align:left") + "\n" + MODULO),
    slide("👪 LE PAROLE DELLA PARENTELA", cards([
        ("🧑", "L'INTESTATARIO", "CHI SCRIVE IL FOGLIO"), ("💍", "IL MARITO / LA MOGLIE", ""),
        ("👦", "IL FIGLIO / LA FIGLIA", ""), ("👵", "LA SUOCERA / IL SUOCERO", "LA MADRE / IL PADRE DI MIA MOGLIE"),
        ("🧒", "IL NIPOTE / LA NIPOTE", "IL FIGLIO DI MIO FIGLIO O DI MIO FRATELLO"), ("👫", "IL CONVIVENTE", "VIVE CON ME, MA NON SIAMO SPOSATI")], "g3")),
    slide("📅 COME SI SCRIVE LA DATA?", table([
        ["12/03/1988", "IL 12 MARZO 1988"], ["04/09/1992", "IL 4 SETTEMBRE 1992"], ["01/05/2020", "IL PRIMO MAGGIO 2020"]],
        head=["IN NUMERI", "IN PAROLE"]) + "\n" + nota("NATO (UOMO) · NATA (DONNA) · NATI (PIÙ PERSONE)")),
    slide("🗣️ A SCUOLA", dialogo([
        ("*MICHELE (SEGRETERIA)", "BUONGIORNO. PER L'ISCRIZIONE DI IBRAHIMA SERVE LO STATO DI FAMIGLIA."),
        ("AMADOU", "DEVO ANDARE IN COMUNE?"),
        ("*MICHELE (SEGRETERIA)", "NO, PUÒ FARE L'AUTOCERTIFICAZIONE. ECCO IL MODULO."),
        ("AMADOU", "SCRIVO I NOMI DI TUTTA LA FAMIGLIA?"),
        ("*MICHELE (SEGRETERIA)", "SÌ, LE PERSONE CHE ABITANO CON LEI. POI DATA E FIRMA."),
        ("AMADOU", "PERFETTO, GRAZIE!")])),
    end("ORA SAI SCRIVERE L'AUTOCERTIFICAZIONE!"),
]
AUTO = {
 "title": "📝 L'autocertificazione · Esercizi", "store": "autocertificazione", "upper": True,
 "sections": [
  {"part": "Leggo il modulo"},
  scegli([("1. CHI SCRIVE IL MODULO?", ["AMADOU", "AISSATOU", "IBRAHIMA"], "AMADOU"),
          ("2. DOVE ABITA LA FAMIGLIA?", ["A BARI", "A DAKAR", "A THIÈS"], "A BARI"),
          ("3. QUANTE PERSONE CI SONO NELLA FAMIGLIA?", ["4", "3", "2"], "4"),
          ("4. CHI È AWA?", ["LA FIGLIA", "LA MOGLIE", "LA SUOCERA"], "LA FIGLIA"),
          ("5. DOVE È NATO IBRAHIMA?", ["A BARI", "A DAKAR", "IN COMUNE"], "A BARI")],
         "1 · Leggi il modulo e rispondi", "1 · Il modulo", "e1", info=MODULO.replace('table class="plur"', 'table class="plur" style="width:100%;font-size:13px"')),
  vf(["1. L'AUTOCERTIFICAZIONE LA SCRIVO IO.", "2. PER L'AUTOCERTIFICAZIONE DEVO ANDARE SEMPRE IN COMUNE.",
      "3. ALLA FINE CI SONO LA DATA E LA FIRMA.", "4. SE SCRIVO UNA COSA FALSA, NON È UN PROBLEMA."],
     ["VERO", "FALSO", "VERO", "FALSO"], "2 · Vero o falso?", "2 · Che cos'è", "e2"),
  {"part": "La parentela"},
  menu(["MARITO", "MOGLIE", "FIGLIO", "FIGLIA", "SUOCERA", "NIPOTE"],
       [("1. AISSATOU È LA ___ DI AMADOU.", "MOGLIE"), ("2. AMADOU È IL ___ DI AISSATOU.", "MARITO"),
        ("3. IBRAHIMA È IL ___ DI AMADOU.", "FIGLIO"), ("4. AWA È LA ___ DI AISSATOU.", "FIGLIA"),
        ("5. LA MADRE DI MIA MOGLIE È MIA ___.", "SUOCERA"), ("6. IL FIGLIO DI MIA SORELLA È MIO ___.", "NIPOTE")],
       "3 · Chi è?", "3 · La parentela", "e3"),
  {"part": "Le date", "teoria":
     tab(("GENNAIO 01", "FEBBRAIO 02", "MARZO 03", "APRILE 04"), ("MAGGIO 05", "GIUGNO 06", "LUGLIO 07", "AGOSTO 08"),
         ("SETTEMBRE 09", "OTTOBRE 10", "NOVEMBRE 11", "DICEMBRE 12")) +
     "IN ITALIA LA DATA È: <b>GIORNO / MESE / ANNO</b>. SI DICE «IL 4 SETTEMBRE», MA «IL <b>PRIMO</b> MAGGIO».<br>"
     "NATO + UOMO · NATA + DONNA." + es("AISSATOU È NAT<b>A</b> IL 4 SETTEMBRE 1992.")},
  scrivi([("1. 12/03/1988 → IL 12 ___ 1988", ["marzo"]), ("2. 04/09/1992 → IL 4 ___ 1992", ["settembre"]),
          ("3. 21/06/2017 → IL 21 ___ 2017", ["giugno"]), ("4. 15/01/2021 → IL 15 ___ 2021", ["gennaio"]),
          ("5. 01/05/2020 → IL ___ MAGGIO 2020", ["primo", "1"])], "4 · Scrivi il mese", "4 · Le date", "e4", w="m"),
  menu(["NATO", "NATA", "NATI"],
       [("1. AWA È ___ A BARI.", "NATA"), ("2. AMADOU È ___ A DAKAR.", "NATO"), ("3. IBRAHIMA E AWA SONO ___ IN ITALIA.", "NATI"),
        ("4. MIA MOGLIE È ___ NEL 1992.", "NATA")], "5 · Nato, nata o nati?", "5 · Nato / nata", "e5"),
  libero("e6", 6, "La mia famiglia", "SCRIVI L'AUTOCERTIFICAZIONE DELLA TUA FAMIGLIA (O DI UNA FAMIGLIA INVENTATA): NOME, LUOGO E DATA DI NASCITA, PARENTELA.",
         ["IO SOTTOSCRITTO / SOTTOSCRITTA…", "PERSONA 2", "PERSONA 3"], rows=2),
  parla("e7", 7, "PARLA DELLA TUA FAMIGLIA: CHI ABITA CON TE? QUANDO E DOVE SONO NATI?"),
 ]
}

# =====================================================================
# 3. PIATTI DAL MONDO (cucina, A1)
# =====================================================================
PIATTI_SLIDE = [
    cover("🌍", "PIATTI DAL MONDO", "MANGIARE IN ITALIA E NEL MONDO", "CIBO &bull; A1"),
    slide("CHE COSA IMPARIAMO?", cards([
        ("🍕", "PIATTI FAMOSI", "PIZZA, KEBAB, SUSHI, CUSCUS…"), ("🥄", "È FATTO CON…", "GLI INGREDIENTI"),
        ("📍", "DI DOV'È?", "LA PIZZA È DI NAPOLI"), ("😋", "COM'È?", "PICCANTE, DOLCE, SALATO")])),
    slide("🍕 LA PIZZA", nota("LA <b>PIZZA</b> È NATA A <b>NAPOLI</b>. OGGI SI MANGIA IN TUTTO IL MONDO. LA PIZZA MARGHERITA È FATTA CON "
        "<b>POMODORO, MOZZARELLA E BASILICO</b>: ROSSO, BIANCO E VERDE, COME LA BANDIERA ITALIANA.", "font-size:1.25rem;text-align:left")),
    slide("🌯 IL KEBAB", nota("IL <b>KEBAB</b> È UN PIATTO DELLA TURCHIA E DEL MEDIO ORIENTE. È FATTO CON <b>CARNE</b> (POLLO, AGNELLO O MANZO) "
        "CUCINATA SU UNO SPIEDO, CON PANE, VERDURA E SALSA. IN ITALIA CI SONO TANTI NEGOZI DI KEBAB.", "font-size:1.25rem;text-align:left")),
    slide("🍣 IL SUSHI", nota("IL <b>SUSHI</b> È UN PIATTO DEL <b>GIAPPONE</b>. È FATTO CON <b>RISO</b>, PESCE CRUDO, VERDURA E ALGHE. "
        "SI MANGIA CON LE BACCHETTE.", "font-size:1.25rem;text-align:left")),
    slide("🌍 E NEI NOSTRI PAESI?", cards([
        ("🇲🇦", "IL CUSCUS", "MAROCCO, TUNISIA, ALGERIA: SEMOLA, VERDURA, CARNE"), ("🇪🇹", "L'INJERA", "ETIOPIA, ERITREA: UN PANE MORBIDO E GRANDE"),
        ("🇵🇰", "IL BIRYANI", "PAKISTAN, INDIA, BANGLADESH: RISO, SPEZIE, POLLO"), ("🇸🇳", "IL THIEBOUDIENNE", "SENEGAL: RISO E PESCE"),
        ("🇳🇬", "IL JOLLOF RICE", "NIGERIA, GHANA: RISO ROSSO CON POMODORO"), ("🇮🇹", "LE ORECCHIETTE", "PUGLIA: PASTA CON LE CIME DI RAPA")], "g3")),
    slide("😋 COM'È?", cards([
        ("🌶️", "PICCANTE", "CON IL PEPERONCINO"), ("🍯", "DOLCE", "CON LO ZUCCHERO"), ("🧂", "SALATO", "CON IL SALE"),
        ("🍋", "ASPRO", "COME IL LIMONE"), ("🔥", "CALDO", ""), ("🧊", "FREDDO", "")], "g3")),
    slide("🗣️ CHE COSA MANGIAMO?", dialogo([
        ("SALEAH", "CRISTIAN, STASERA CENIAMO INSIEME? CUCINO IO IL BIRYANI."),
        ("*CRISTIAN", "CHE COS'È IL BIRYANI?"),
        ("SALEAH", "È UN PIATTO DEL PAKISTAN. È FATTO CON RISO, POLLO E TANTE SPEZIE."),
        ("*CRISTIAN", "È PICCANTE?"),
        ("SALEAH", "UN PO'. MA PER TE METTO POCO PEPERONCINO!"),
        ("*CRISTIAN", "PERFETTO! IO PORTO IL DOLCE: UN TIRAMISÙ.")])),
    end("ORA SAI PARLARE DEI PIATTI DEL MONDO!"),
]
PIATTI = {
 "title": "🌍 Piatti dal mondo · Esercizi", "store": "piatti-dal-mondo", "upper": True,
 "sections": [
  {"part": "Di dov'è?"},
  menu(["ITALIA", "GIAPPONE", "TURCHIA", "MAROCCO", "ETIOPIA", "PAKISTAN"],
       [("1. LA PIZZA", "ITALIA"), ("2. IL SUSHI", "GIAPPONE"), ("3. IL KEBAB", "TURCHIA"), ("4. IL CUSCUS", "MAROCCO"),
        ("5. L'INJERA", "ETIOPIA"), ("6. IL BIRYANI", "PAKISTAN")], "1 · Di che paese è il piatto?", "1 · Di dov'è", "e1"),
  vf(["1. LA PIZZA È NATA A ROMA.", "2. LA MARGHERITA HA POMODORO, MOZZARELLA E BASILICO.", "3. IL SUSHI È FATTO CON IL RISO.",
      "4. IL KEBAB È FATTO CON IL PESCE.", "5. LE ORECCHIETTE SONO UNA PASTA DELLA PUGLIA."],
     ["FALSO", "VERO", "VERO", "FALSO", "VERO"], "2 · Vero o falso?", "2 · Vero o falso", "e2"),
  {"part": "È fatto con…", "teoria":
     tab(("IL KEBAB", "È FATTO", "CON LA CARNE"), ("LA PIZZA", "È FATTA", "CON LA FARINA"), ("GLI SPAGHETTI", "SONO FATTI", "CON LA FARINA"),
         ("LE ORECCHIETTE", "SONO FATTE", "CON LA SEMOLA"), head=("IL PIATTO", "", "INGREDIENTE")) +
     "<b>FATTO</b> CAMBIA COME UN AGGETTIVO: FATTO · FATTA · FATTI · FATTE." + es("IL CUSCUS È FATT<b>O</b> CON LA SEMOLA.")},
  menu(["FATTO", "FATTA", "FATTI", "FATTE"],
       [("1. IL SUSHI È ___ CON IL RISO.", "FATTO"), ("2. LA PIZZA È ___ CON LA FARINA.", "FATTA"),
        ("3. GLI SPAGHETTI SONO ___ CON LA FARINA.", "FATTI"), ("4. LE ORECCHIETTE SONO ___ CON LA SEMOLA.", "FATTE"),
        ("5. L'INJERA È ___ CON UN CEREALE CHE SI CHIAMA TEFF.", "FATTA")], "3 · Fatto, fatta, fatti o fatte?", "3 · È fatto con", "e3"),
  scegli([("1. C'È IL PEPERONCINO: È ___.", ["PICCANTE", "DOLCE", "FREDDO"], "PICCANTE"),
          ("2. C'È TANTO ZUCCHERO: È ___.", ["DOLCE", "SALATO", "PICCANTE"], "DOLCE"),
          ("3. IL GELATO È ___.", ["FREDDO", "CALDO", "PICCANTE"], "FREDDO"),
          ("4. IL LIMONE È ___.", ["ASPRO", "DOLCE", "SALATO"], "ASPRO")], "4 · Com'è?", "4 · Com'è", "e4"),
  completa("SALEAH: STASERA CUCINO IL ___.<br>CRISTIAN: CHE COS'È?<br>SALEAH: È UN PIATTO DEL PAKISTAN. È ___ CON RISO, POLLO E SPEZIE.<br>"
           "CRISTIAN: È ___?<br>SALEAH: UN PO'. PER TE METTO ___ PEPERONCINO.",
           ["biryani", "fatto", "piccante", "poco"], "5 · Completa il dialogo", "5 · Il dialogo", "e5", "BIRYANI · FATTO · PICCANTE · POCO"),
  libero("e6", 6, "Il piatto del mio paese", "SCRIVI UN PIATTO DEL TUO PAESE: COME SI CHIAMA? CON CHE COSA È FATTO? COM'È? QUANDO SI MANGIA?", ["IL PIATTO DEL MIO PAESE"], rows=4),
  parla("e7", 7, "SPIEGA A UN AMICO ITALIANO IL TUO PIATTO PREFERITO: INGREDIENTI E COME SI CUCINA."),
 ]
}

# =====================================================================
# 4. IL VOLONTARIATO (città, A1)
# =====================================================================
VOL_SLIDE = [
    cover("🤲", "IL VOLONTARIATO", "AIUTARE GLI ALTRI, GRATIS", "CITTÀ &bull; A1"),
    slide("CHE COSA IMPARIAMO?", cards([
        ("🤲", "CHI È IL VOLONTARIO", "AIUTA SENZA SOLDI"), ("🏥", "LE ASSOCIAZIONI", "CROCE ROSSA, AVIS, CARITAS…"),
        ("🩸", "DONARE", "IL SANGUE, IL TEMPO, I VESTITI"), ("🙋", "POSSO AIUTARE?", "COME DIVENTO VOLONTARIO")])),
    slide("🤲 CHI È IL VOLONTARIO?", nota("IL <b>VOLONTARIO</b> È UNA PERSONA CHE <b>AIUTA GLI ALTRI GRATIS</b>, NEL SUO TEMPO LIBERO. "
        "IN ITALIA CI SONO MILIONI DI VOLONTARI: AIUTANO I MALATI, GLI ANZIANI, I BAMBINI, I MIGRANTI, I POVERI.", "font-size:1.3rem;text-align:left")),
    slide("🏥 ALCUNE ASSOCIAZIONI", cards([
        ("➕", "LA CROCE ROSSA", "AMBULANZE, PRIMO SOCCORSO, AIUTO NELLE EMERGENZE"), ("🩸", "L'AVIS", "LE PERSONE CHE DONANO IL SANGUE"),
        ("🍲", "LA CARITAS", "MENSA, VESTITI E ASCOLTO PER CHI HA BISOGNO"), ("👵", "L'AUSER", "COMPAGNIA E AIUTO PER GLI ANZIANI"),
        ("🩺", "EMERGENCY", "OSPEDALI E CURE GRATUITE"), ("🧸", "L'UNICEF", "I DIRITTI DEI BAMBINI NEL MONDO")], "g3")),
    slide("🙋 CHE COSA FA UN VOLONTARIO?", cards([
        ("🍲", "SERVE I PASTI", "ALLA MENSA"), ("📚", "AIUTA I BAMBINI", "A FARE I COMPITI"), ("🚑", "GUIDA L'AMBULANZA", ""),
        ("👕", "DIVIDE I VESTITI", "PER LE FAMIGLIE"), ("🗣️", "TRADUCE", "PER CHI NON PARLA ITALIANO"), ("🌳", "PULISCE", "I PARCHI E LE SPIAGGE")], "g3")),
    slide("🗣️ VOGLIO FARE IL VOLONTARIO", dialogo([
        ("KWAME", "BUONGIORNO. VOGLIO FARE IL VOLONTARIO. È POSSIBILE?"),
        ("*SILVIA (CARITAS)", "CERTO! CHE COSA SAI FARE?"),
        ("KWAME", "PARLO INGLESE, FRANCESE E TWI. E SO CUCINARE."),
        ("*SILVIA (CARITAS)", "BENISSIMO! ALLA MENSA SERVE AIUTO IL SABATO. E A VOLTE SERVE UN TRADUTTORE."),
        ("KWAME", "IL SABATO SONO LIBERO. A CHE ORA?"),
        ("*SILVIA (CARITAS)", "DALLE 11 ALLE 14. TI ASPETTIAMO!")])),
    slide("📘 SO / POSSO / VOGLIO", table([
        ["SAPERE", "SO CUCINARE", "HO IMPARATO, SONO CAPACE"], ["POTERE", "POSSO VENIRE IL SABATO", "HO TEMPO, È POSSIBILE"],
        ["VOLERE", "VOGLIO AIUTARE", "MI PIACE, HO DESIDERIO"]], head=["VERBO", "ESEMPIO", "SIGNIFICA"])),
    end("ORA SAI CHE COS'È IL VOLONTARIATO!"),
]
VOL = {
 "title": "🤲 Il volontariato · Esercizi", "store": "volontariato", "upper": True,
 "sections": [
  {"part": "Le associazioni"},
  menu(["LA CROCE ROSSA", "L'AVIS", "LA CARITAS", "L'AUSER", "L'UNICEF"],
       [("1. DONO IL SANGUE.", "L'AVIS"), ("2. C'È UN INCIDENTE: ARRIVA L'AMBULANZA.", "LA CROCE ROSSA"),
        ("3. UNA MENSA PER CHI NON HA SOLDI.", "LA CARITAS"), ("4. AIUTO PER GLI ANZIANI SOLI.", "L'AUSER"),
        ("5. I DIRITTI DEI BAMBINI.", "L'UNICEF")], "1 · Quale associazione?", "1 · Le associazioni", "e1"),
  vf(["1. IL VOLONTARIO PRENDE UNO STIPENDIO.", "2. IL VOLONTARIO AIUTA NEL SUO TEMPO LIBERO.", "3. KWAME PARLA TRE LINGUE.",
      "4. KWAME È LIBERO IL SABATO.", "5. LA MENSA È APERTA DALLE 8 ALLE 10."],
     ["FALSO", "VERO", "VERO", "VERO", "FALSO"], "2 · Vero o falso?", "2 · Vero o falso", "e2"),
  {"part": "Sapere, potere, volere", "teoria":
     tab(("IO", "SO", "POSSO", "VOGLIO"), ("TU", "SAI", "PUOI", "VUOI"), ("LUI / LEI", "SA", "PUÒ", "VUOLE"),
         ("NOI", "SAPPIAMO", "POSSIAMO", "VOGLIAMO"), ("VOI", "SAPETE", "POTETE", "VOLETE"), ("LORO", "SANNO", "POSSONO", "VOGLIONO"),
         head=("", "SAPERE", "POTERE", "VOLERE")) +
     "<b>SO</b> = SONO CAPACE · <b>POSSO</b> = HO TEMPO / È POSSIBILE · <b>VOGLIO</b> = HO DESIDERIO. DOPO C'È L'INFINITO." +
     es("SO GUIDARE. POSSO VENIRE DOMANI. VOGLIO AIUTARE.")},
  menu(["SO", "POSSO", "VOGLIO"],
       [("1. ___ PARLARE ARABO E FRANCESE: HO STUDIATO.", "SO"), ("2. SABATO SONO LIBERO: ___ VENIRE ALLA MENSA.", "POSSO"),
        ("3. MI PIACE AIUTARE: ___ FARE IL VOLONTARIO.", "VOGLIO"), ("4. NON ___ NUOTARE: NON HO MAI IMPARATO.", "SO"),
        ("5. OGGI LAVORO, NON ___ VENIRE.", "POSSO")], "3 · So, posso o voglio?", "3 · So / posso / voglio", "e3"),
  scrivi([("1. TU (SAPERE) ___ CUCINARE?", ["sai"]), ("2. NOI (POTERE) ___ AIUTARE IL SABATO.", ["possiamo"]),
          ("3. LORO (VOLERE) ___ DONARE IL SANGUE.", ["vogliono"]), ("4. LEI (SAPERE) ___ GUIDARE L'AMBULANZA.", ["sa"]),
          ("5. VOI (POTERE) ___ VENIRE DOMANI?", ["potete"])], "4 · Scrivi il verbo", "4 · I verbi", "e4", w="s"),
  completa("KWAME: VOGLIO FARE IL ___.<br>SILVIA: CHE COSA SAI ___?<br>KWAME: PARLO TRE LINGUE E SO ___.<br>"
           "SILVIA: ALLA ___ SERVE AIUTO IL SABATO.<br>KWAME: IL SABATO SONO ___!",
           ["volontario", "fare", "cucinare", "mensa", "libero"], "5 · Completa il dialogo", "5 · Il dialogo", "e5",
           "VOLONTARIO · FARE · CUCINARE · MENSA · LIBERO"),
  libero("e6", 6, "Io volontario", "SCRIVI: CHE COSA SAI FARE? QUANDO PUOI AIUTARE? CHE VOLONTARIATO VUOI FARE?", ["SO…", "POSSO…", "VOGLIO…"], rows=2),
  parla("e7", 7, "NEL TUO PAESE CI SONO VOLONTARI? CHE COSA FANNO? TU HAI MAI AIUTATO QUALCUNO?"),
 ]
}

# =====================================================================
# 5. IN STRADA: PEDONI E BICI (città, A1)
# =====================================================================
STRADA_SLIDE = [
    cover("🚸", "IN STRADA", "A PIEDI E IN BICI: LE REGOLE PER LA SICUREZZA", "CITTÀ &bull; A1"),
    slide("CHE COSA IMPARIAMO?", cards([
        ("🚶", "IL PEDONE", "CHI VA A PIEDI"), ("🦓", "LE STRISCE", "DOVE ATTRAVERSO"), ("🚦", "IL SEMAFORO", "ROSSO, GIALLO, VERDE"),
        ("🚲", "LA BICI", "CASCO, LUCI, PISTA CICLABILE")])),
    slide("🛣️ LE PAROLE DELLA STRADA", cards([
        ("🚶", "IL MARCIAPIEDE", "LA PARTE PER I PEDONI"), ("🦓", "LE STRISCE PEDONALI", ""), ("🚦", "IL SEMAFORO", ""),
        ("🚲", "LA PISTA CICLABILE", "LA STRADA PER LE BICI"), ("↩️", "L'INCROCIO", "DOVE SI INCONTRANO DUE STRADE"), ("🚌", "LA FERMATA", "DELL'AUTOBUS")], "g3")),
    slide("🚦 IL SEMAFORO", cards([
        ("🔴", "ROSSO", "STOP! ASPETTA."), ("🟡", "GIALLO", "ATTENZIONE! NON INIZIARE AD ATTRAVERSARE."), ("🟢", "VERDE", "ATTRAVERSA, MA GUARDA LE MACCHINE.")], "g3")),
    slide("🚶 LE REGOLE PER IL PEDONE", cards([
        ("🚶", "CAMMINA SUL MARCIAPIEDE", ""), ("🦓", "ATTRAVERSA SULLE STRISCE", ""), ("👀", "GUARDA A DESTRA E A SINISTRA", ""),
        ("📵", "NON USARE IL TELEFONO", "QUANDO ATTRAVERSI"), ("🌙", "DI SERA", "VESTITI CHIARI O LUCI"), ("🧒", "DAI LA MANO AI BAMBINI", "")], "g3")),
    slide("🚲 LE REGOLE PER LA BICI", cards([
        ("⛑️", "METTI IL CASCO", "È PIÙ SICURO"), ("💡", "ACCENDI LE LUCI", "DI SERA E DI NOTTE"), ("🛣️", "USA LA PISTA CICLABILE", "SE C'È"),
        ("🚫", "NON ANDARE SUL MARCIAPIEDE", ""), ("✋", "SEGNALA CON IL BRACCIO", "QUANDO GIRI"), ("🎧", "NON USARE LE CUFFIE", "")], "g3") + "\n" +
        nota("🛴 ANCHE CON IL MONOPATTINO ELETTRICO CI SONO REGOLE: CASCO, NIENTE MARCIAPIEDE, UNA PERSONA SOLA.")),
    slide("🗣️ A PIEDI PER BARI", dialogo([
        ("FATOU", "DAI, ATTRAVERSIAMO QUI! NON PASSA NESSUNO."),
        ("*GIOVANNI", "NO, ASPETTA! LE STRISCE SONO LÀ, VICINO AL SEMAFORO."),
        ("FATOU", "MA È LONTANO…"),
        ("*GIOVANNI", "SONO SOLO 20 METRI. QUI LE MACCHINE VANNO VELOCI. ED È PIÙ SICURO."),
        ("FATOU", "HAI RAGIONE. OH, È VERDE! ANDIAMO."),
        ("*GIOVANNI", "GUARDA PRIMA A DESTRA E A SINISTRA!")])),
    slide("📘 L'IMPERATIVO (TU)", table([
        ["-ARE", "GUARDARE → <b>GUARDA</b>!", "NON GUARDARE!"], ["-ERE", "METTERE → <b>METTI</b>!", "NON METTERE!"],
        ["-IRE", "SENTIRE → <b>SENTI</b>!", "NON SENTIRE!"]], head=["VERBO", "SÌ", "NO: NON + INFINITO"])),
    end("ORA SAI LE REGOLE DELLA STRADA!"),
]
STRADA = {
 "title": "🚸 In strada · Esercizi", "store": "in-strada", "upper": True,
 "sections": [
  {"part": "Le parole della strada"},
  menu(["IL MARCIAPIEDE", "LE STRISCE", "IL SEMAFORO", "LA PISTA CICLABILE", "IL CASCO"],
       [("1. LO METTO SULLA TESTA QUANDO VADO IN BICI.", "IL CASCO"), ("2. È ROSSO, GIALLO O VERDE.", "IL SEMAFORO"),
        ("3. LÌ ATTRAVERSO LA STRADA.", "LE STRISCE"), ("4. LA STRADA SOLO PER LE BICI.", "LA PISTA CICLABILE"),
        ("5. LA PARTE DELLA STRADA PER I PEDONI.", "IL MARCIAPIEDE")], "1 · Che cos'è?", "1 · Le parole", "e1"),
  scegli([("1. IL SEMAFORO È ROSSO. CHE COSA FAI?", ["ASPETTO", "ATTRAVERSO", "CORRO"], "ASPETTO"),
          ("2. VAI IN BICI DI SERA. CHE COSA FAI?", ["ACCENDO LE LUCI", "VADO SUL MARCIAPIEDE", "METTO LE CUFFIE"], "ACCENDO LE LUCI"),
          ("3. DEVI ATTRAVERSARE. DOVE?", ["SULLE STRISCE", "IN MEZZO ALLA STRADA", "ALL'INCROCIO SENZA GUARDARE"], "SULLE STRISCE"),
          ("4. GIRI A DESTRA IN BICI. CHE COSA FAI?", ["SEGNALO CON IL BRACCIO", "CHIUDO GLI OCCHI", "SUONO IL TELEFONO"], "SEGNALO CON IL BRACCIO")],
         "2 · Che cosa fai?", "2 · Che cosa fai", "e2"),
  {"part": "L'imperativo", "teoria":
     tab(("-ARE", "GUARDARE", "GUARDA!", "NON GUARDARE!"), ("-ERE", "METTERE", "METTI!", "NON METTERE!"), ("-IRE", "SENTIRE", "SENTI!", "NON SENTIRE!"),
         head=("", "VERBO", "SÌ (TU)", "NO (TU)")) +
     "PER DARE UN CONSIGLIO O UN ORDINE A UN AMICO: -ARE → <b>-A</b>, -ERE / -IRE → <b>-I</b>.<br>NEGATIVO: <b>NON + INFINITO</b>." +
     es("ASPETTA IL VERDE! NON CORRERE!")},
  scrivi([("1. (ASPETTARE) ___ IL VERDE!", ["aspetta"]), ("2. (METTERE) ___ IL CASCO!", ["metti"]),
          ("3. (GUARDARE) ___ A DESTRA E A SINISTRA!", ["guarda"]), ("4. (ACCENDERE) ___ LE LUCI DELLA BICI!", ["accendi"]),
          ("5. (ATTRAVERSARE) ___ SULLE STRISCE!", ["attraversa"])], "3 · Scrivi l'imperativo", "3 · Imperativo sì", "e3", w="m"),
  scrivi([("1. CORRERE → NON ___!", ["correre"]), ("2. USARE IL TELEFONO → NON ___ IL TELEFONO!", ["usare"]),
          ("3. ANDARE SUL MARCIAPIEDE → NON ___ SUL MARCIAPIEDE!", ["andare"]), ("4. ATTRAVERSARE COL ROSSO → NON ___ COL ROSSO!", ["attraversare"])],
         "4 · Scrivi la forma negativa", "4 · Imperativo no", "e4", w="m"),
  vf(["1. FATOU VUOLE ATTRAVERSARE LONTANO DALLE STRISCE.", "2. GIOVANNI DICE: «ASPETTA!».", "3. LE STRISCE SONO A 200 METRI.",
      "4. ATTRAVERSANO CON IL VERDE."], ["VERO", "VERO", "FALSO", "VERO"], "5 · Leggi il dialogo: vero o falso?", "5 · Il dialogo", "e5",
     info="FATOU: DAI, ATTRAVERSIAMO QUI! · GIOVANNI: NO, ASPETTA! LE STRISCE SONO LÀ, VICINO AL SEMAFORO. · FATOU: MA È LONTANO… · "
          "GIOVANNI: SONO SOLO 20 METRI. QUI LE MACCHINE VANNO VELOCI. · FATOU: HAI RAGIONE. OH, È VERDE! ANDIAMO."),
  libero("e6", 6, "I consigli", "SCRIVI 4 CONSIGLI A UN AMICO CHE VA IN BICI PER LA PRIMA VOLTA A BARI. USA L'IMPERATIVO.", ["1.", "2.", "3.", "4."], rows=1),
  parla("e7", 7, "COME VAI A SCUOLA O AL LAVORO? A PIEDI, IN BICI, IN AUTOBUS? CHE COSA FAI PER ESSERE SICURO?"),
 ]
}

# =====================================================================
# 6. IL CUP E I MEDICI SPECIALISTI (salute, A1)
# =====================================================================
CUP_SLIDE = [
    cover("🏥", "IL CUP E GLI SPECIALISTI", "LA SALUTE È UN DIRITTO: PRENOTO UNA VISITA", "SALUTE &bull; A1"),
    slide("CHE COSA IMPARIAMO?", cards([
        ("⚖️", "UN DIRITTO", "LA SALUTE NELLA COSTITUZIONE"), ("💳", "LA TESSERA SANITARIA", "E IL TESSERINO STP"),
        ("🩺", "GLI SPECIALISTI", "CARDIOLOGO, DENTISTA…"), ("📞", "IL CUP", "COME PRENOTO UNA VISITA")])),
    slide("⚖️ LA SALUTE È UN DIRITTO", nota("LA <b>COSTITUZIONE ITALIANA</b> (ARTICOLO 32) DICE CHE LA SALUTE È UN <b>DIRITTO DI TUTTI</b>. "
        "IL <b>SERVIZIO SANITARIO NAZIONALE (SSN)</b> CURA TUTTE LE PERSONE. LE CURE URGENTI SONO PER TUTTI, ANCHE PER CHI NON HA DOCUMENTI.", "font-size:1.25rem;text-align:left")),
    slide("💳 I DOCUMENTI PER IL MEDICO", cards([
        ("💳", "LA TESSERA SANITARIA", "LA CHIEDO ALL'ASL CON IL PERMESSO DI SOGGIORNO E IL CODICE FISCALE"),
        ("👨‍⚕️", "IL MEDICO DI BASE", "LO SCELGO ALL'ASL: È GRATIS"),
        ("🧒", "IL PEDIATRA", "IL MEDICO DEI BAMBINI FINO A 14 ANNI"),
        ("📄", "IL TESSERINO STP", "PER CHI NON HA IL PERMESSO DI SOGGIORNO: CURE URGENTI, GRAVIDANZA, BAMBINI")])),
    slide("🩺 GLI SPECIALISTI", cards([
        ("❤️", "IL CARDIOLOGO", "IL CUORE"), ("🦷", "IL DENTISTA", "I DENTI"), ("👁️", "L'OCULISTA", "GLI OCCHI"),
        ("👂", "L'OTORINO", "ORECCHIE, NASO, GOLA"), ("🧴", "IL DERMATOLOGO", "LA PELLE"), ("🦴", "L'ORTOPEDICO", "LE OSSA"),
        ("🤰", "IL GINECOLOGO", "LA DONNA, LA GRAVIDANZA"), ("🧒", "IL PEDIATRA", "I BAMBINI"), ("🧠", "IL NEUROLOGO", "LA TESTA, I NERVI")], "g3")),
    slide("📞 COME PRENOTO UNA VISITA?", cards([
        ("1️⃣", "VADO DAL MEDICO DI BASE", "MI SCRIVE L'IMPEGNATIVA (LA RICETTA)"), ("2️⃣", "CHIAMO IL CUP", "O VADO ALLO SPORTELLO O IN FARMACIA"),
        ("3️⃣", "DICO I DATI", "CODICE FISCALE E NUMERO DELL'IMPEGNATIVA"), ("4️⃣", "PAGO IL TICKET", "UNA PICCOLA PARTE (SE NON SONO ESENTE)")]) + "\n" +
        nota("💡 <b>CUP</b> = CENTRO UNICO DI PRENOTAZIONE.")),
    slide("🗣️ AL TELEFONO CON IL CUP", dialogo([
        ("*OPERATRICE", "CUP, BUONGIORNO. MI DICE IL CODICE FISCALE?"),
        ("MARIELA", "SÌ: R-M-R-M-R-L… ECCO. HO UN'IMPEGNATIVA PER UNA VISITA DERMATOLOGICA."),
        ("*OPERATRICE", "IL NUMERO DELL'IMPEGNATIVA, PER FAVORE."),
        ("MARIELA", "1600 A 4 2 7 7 1 3."),
        ("*OPERATRICE", "C'È UN POSTO IL 12 DICEMBRE ALLE 9:30, AL POLICLINICO."),
        ("MARIELA", "VA BENE. DEVO PORTARE QUALCOSA?"),
        ("*OPERATRICE", "L'IMPEGNATIVA, LA TESSERA SANITARIA E LA RICEVUTA DEL TICKET.")])),
    slide("📘 DEVO / BISOGNA", table([
        ["DEVO", "+ INFINITO", "DEVO PRENOTARE LA VISITA."], ["DEVI", "+ INFINITO", "DEVI PORTARE LA TESSERA."],
        ["DEVE", "+ INFINITO", "LEI DEVE PAGARE IL TICKET."], ["BISOGNA", "+ INFINITO (PER TUTTI)", "BISOGNA AVERE L'IMPEGNATIVA."]],
        head=["", "", "ESEMPIO"])),
    end("ORA SAI PRENOTARE UNA VISITA!"),
]
CUP = {
 "title": "🏥 Il CUP e gli specialisti · Esercizi", "store": "cup-specialisti", "upper": True,
 "sections": [
  {"part": "Gli specialisti"},
  menu(["IL CARDIOLOGO", "IL DENTISTA", "L'OCULISTA", "L'OTORINO", "IL DERMATOLOGO", "L'ORTOPEDICO", "IL PEDIATRA"],
       [("1. HO MALE A UN DENTE.", "IL DENTISTA"), ("2. NON VEDO BENE.", "L'OCULISTA"), ("3. HO UNA MACCHIA SULLA PELLE.", "IL DERMATOLOGO"),
        ("4. MIO FIGLIO DI 3 ANNI HA LA FEBBRE.", "IL PEDIATRA"), ("5. MI FA MALE IL CUORE.", "IL CARDIOLOGO"),
        ("6. MI FA MALE LA GOLA E NON SENTO BENE.", "L'OTORINO"), ("7. SONO CADUTO: FORSE HO UN OSSO ROTTO.", "L'ORTOPEDICO")],
       "1 · Da quale specialista vai?", "1 · Gli specialisti", "e1"),
  vf(["1. LA SALUTE È UN DIRITTO SOLO PER GLI ITALIANI.", "2. IL MEDICO DI BASE È GRATIS.", "3. IL PEDIATRA È IL MEDICO DEI BAMBINI.",
      "4. CHI NON HA IL PERMESSO DI SOGGIORNO PUÒ AVERE IL TESSERINO STP.", "5. PER PRENOTARE AL CUP SERVE L'IMPEGNATIVA."],
     ["FALSO", "VERO", "VERO", "VERO", "VERO"], "2 · Vero o falso?", "2 · Vero o falso", "e2"),
  {"part": "Prenoto la visita"},
  ordina(["VADO DAL MEDICO DI BASE.", "IL MEDICO MI SCRIVE L'IMPEGNATIVA.", "CHIAMO IL CUP.", "DICO IL CODICE FISCALE E IL NUMERO DELL'IMPEGNATIVA.",
          "PAGO IL TICKET.", "IL GIORNO DELLA VISITA VADO IN OSPEDALE CON LA TESSERA SANITARIA."], "3 · Metti in ordine", "3 · In ordine", "e3"),
  {"part": "Devo, bisogna", "teoria":
     tab(("IO", "DEVO"), ("TU", "DEVI"), ("LUI / LEI", "DEVE"), ("NOI", "DOBBIAMO"), ("VOI", "DOVETE"), ("LORO", "DEVONO"), head=("", "DOVERE")) +
     "DOPO <b>DOVERE</b> C'È L'INFINITO. <b>BISOGNA</b> + INFINITO È PER TUTTI (NON CAMBIA)." + es("DEVO CHIAMARE IL CUP. BISOGNA PORTARE LA TESSERA.")},
  scrivi([("1. IO ___ PRENOTARE UNA VISITA.", ["devo"]), ("2. TU ___ PORTARE L'IMPEGNATIVA.", ["devi"]),
          ("3. MARIELA ___ ANDARE AL POLICLINICO.", ["deve"]), ("4. NOI ___ PAGARE IL TICKET.", ["dobbiamo"]),
          ("5. I BAMBINI ___ ANDARE DAL PEDIATRA.", ["devono"])], "4 · Scrivi il verbo dovere", "4 · Dovere", "e4", w="s"),
  completa("OPERATRICE: CUP, BUONGIORNO. MI DICE IL CODICE ___?<br>MARIELA: ECCO. HO UN'___ PER UNA VISITA.<br>"
           "OPERATRICE: C'È UN POSTO IL 12 DICEMBRE ALLE 9:30.<br>MARIELA: VA BENE. ___ PORTARE QUALCOSA?<br>OPERATRICE: LA TESSERA ___ E LA RICEVUTA DEL ___.",
           ["fiscale", "impegnativa", "devo", "sanitaria", "ticket"], "5 · Completa il dialogo", "5 · Il CUP", "e5",
           "FISCALE · IMPEGNATIVA · DEVO · SANITARIA · TICKET"),
  libero("e6", 6, "La mia visita", "SCRIVI: CHE SPECIALISTA TI SERVE? PERCHÉ? CHE COSA DEVI FARE PER PRENOTARE?", ["LA MIA VISITA"], rows=4),
  parla("e7", 7, "TELEFONA AL CUP: DI' IL TUO NOME, CHE VISITA VUOI PRENOTARE E QUANDO SEI LIBERO."),
 ]
}

# =====================================================================
# 7. PAGARE LE TASSE (civica, A2 minuscolo)
# =====================================================================
TASSE_SLIDE = [
    cover("💶", "Pagare le tasse", "Perché si pagano, quali sono, chi ci aiuta", "Educazione civica &bull; A2"),
    slide("Che cosa impariamo?", cards([
        ("⚖️", "Un dovere", "l'articolo 53 della Costituzione"), ("🏫", "A che cosa servono", "scuole, ospedali, strade"),
        ("🧾", "Le tasse principali", "IRPEF, IVA, TARI, bollo"), ("🧑‍💼", "Chi mi aiuta", "il CAF e il patronato")])),
    slide("⚖️ Perché si pagano?", nota("La Costituzione (<b>articolo 53</b>) dice: «Tutti sono tenuti a concorrere alle spese pubbliche in ragione della loro "
        "capacità contributiva». Significa: <b>tutti pagano</b>, e chi guadagna di più paga di più.", "font-size:1.25rem;text-align:left") + "\n" +
        nota("Con le tasse lo Stato paga le scuole, gli ospedali, le strade, gli autobus, la polizia, le pensioni.")),
    slide("🧾 Le tasse principali", cards([
        ("👷", "L'IRPEF", "la tassa sullo stipendio: il datore di lavoro la toglie dalla busta paga"),
        ("🛒", "L'IVA", "è dentro il prezzo delle cose che compro (es. 22%)"),
        ("🗑️", "La TARI", "la tassa sui rifiuti: la paga chi abita in una casa"),
        ("🚗", "Il bollo auto", "ogni anno, se ho una macchina"),
        ("🏠", "L'IMU", "per chi ha una seconda casa"),
        ("🎫", "Il ticket", "una piccola parte per visite ed esami")], "g3")),
    slide("🗑️ La TARI", nota("La <b>TARI</b> serve a pagare la raccolta e lo smaltimento dei rifiuti. La paga chi <b>abita</b> in un appartamento "
        "(proprietario o in affitto). Il Comune manda a casa l'avviso con il modulo <b>F24</b> o il PagoPA. Se non pago, arriva una multa.", "font-size:1.2rem;text-align:left") + "\n" +
        nota("💡 Quando cambio casa, devo comunicarlo all'ufficio TARI del Comune.")),
    slide("📅 Il 730: la dichiarazione dei redditi", cards([
        ("📄", "Che cos'è", "un modulo: dico allo Stato quanto ho guadagnato in un anno"), ("📅", "Quando", "di solito entro il 30 settembre"),
        ("💰", "Il rimborso", "a volte lo Stato mi restituisce dei soldi"), ("👶", "Le detrazioni", "spese mediche, figli, affitto: pago meno")])),
    slide("🧑‍💼 Chi mi aiuta?", cards([
        ("🏢", "Il CAF", "fa il 730 e l'ISEE, spesso gratis o con poca spesa"), ("🤝", "Il patronato", "pensioni, disoccupazione, permessi"),
        ("🏛️", "L'Agenzia delle Entrate", "il codice fiscale, le informazioni")])),
    slide("🗣️ Al CAF", dialogo([
        ("*Eneida", "Buongiorno Ravi, sei venuto per il 730?"),
        ("Ravi", "Sì. Ho lavorato tutto l'anno in un ristorante. Che cosa devo portare?"),
        ("*Eneida", "La Certificazione Unica, che ti dà il datore di lavoro, il documento e il codice fiscale."),
        ("Ravi", "Ho anche le ricevute del dentista. Servono?"),
        ("*Eneida", "Sì! Le spese mediche si possono detrarre: pagherai meno tasse."),
        ("Ravi", "Perfetto. E la TARI? È arrivata una lettera dal Comune."),
        ("*Eneida", "La TARI si paga con l'F24 o con PagoPA, anche in posta o in tabaccheria.")])),
    end("Ora sai perché e come si pagano le tasse!"),
]
TASSE = {
 "title": "💶 Pagare le tasse · Esercizi", "store": "tasse",
 "sections": [
  {"part": "Le tasse"},
  menu(["IRPEF", "IVA", "TARI", "bollo auto", "ticket"],
       [("1. È dentro il prezzo del pane e dei vestiti.", "IVA"), ("2. Si toglie dallo stipendio.", "IRPEF"),
        ("3. Serve per la raccolta dei rifiuti.", "TARI"), ("4. Si paga ogni anno per la macchina.", "bollo auto"),
        ("5. Una piccola parte per una visita medica.", "ticket")], "1 · Quale tassa?", "1 · Le tasse", "e1", cons="Scegli la tassa giusta."),
  vf(["1. Le tasse le pagano solo gli italiani.", "2. Chi guadagna di più paga di più.", "3. Con le tasse si pagano scuole e ospedali.",
      "4. La TARI la paga anche chi abita in affitto.", "5. Il 730 è un documento per l'affitto."],
     ["FALSO", "VERO", "VERO", "VERO", "FALSO"], "2 · Vero o falso?", "2 · Vero o falso", "e2"),
  {"part": "Il si impersonale", "teoria":
     tab(("si paga", "+ una cosa", "La TARI si paga con l'F24."), ("si pagano", "+ tante cose", "Le tasse si pagano ogni anno."),
         ("si può / si deve", "+ infinito", "Si può pagare in posta.")) +
     "Con <b>si</b> parliamo in generale, per tutte le persone. Il verbo è alla 3ª persona: singolare con una cosa, plurale con tante cose." +
     es("In Italia si pagano le tasse. Il 730 si fa al CAF.")},
  menu(["si paga", "si pagano"],
       [("1. La TARI ___ al Comune.", "si paga"), ("2. Le tasse ___ in base allo stipendio.", "si pagano"),
        ("3. Il bollo auto ___ una volta all'anno.", "si paga"), ("4. Le multe ___ entro 60 giorni.", "si pagano"),
        ("5. L'IVA ___ quando compri qualcosa.", "si paga")], "3 · Si paga o si pagano?", "3 · Si impersonale", "e3"),
  scrivi([("1. Il 730 (fare) si ___ al CAF.", ["fa"]), ("2. Le ricevute del dentista (portare) si ___ al CAF.", ["portano"]),
          ("3. La lettera della TARI (ricevere) si ___ a casa.", ["riceve"]), ("4. I moduli (compilare) si ___ con i dati personali.", ["compilano"])],
         "4 · Scrivi il verbo con si", "4 · Si + verbo", "e4", cons="Scrivi il verbo alla 3ª persona (singolare o plurale).", w="m"),
  completa("Ravi ha lavorato tutto l'anno in un ___. Al CAF porta la Certificazione ___, il documento e il codice fiscale. "
           "Porta anche le ricevute del ___: le spese mediche si possono detrarre. La ___ invece si paga con l'F24 o con PagoPA.",
           ["ristorante", "unica", "dentista", "tari"], "5 · Completa il testo", "5 · Al CAF", "e5", "ristorante · Unica · dentista · TARI", cons="Scrivi la parola giusta."),
  libero("e6", 6, "Le tasse nel mio paese", "Scrivi 4-5 frasi: nel tuo paese si pagano le tasse? Quali? Che cosa paga lo Stato con le tasse?", ["Nel mio paese…"], rows=5),
  parla("e7", 7, "Spiega a un amico appena arrivato che cos'è la TARI e come si paga."),
 ]
}

# =====================================================================
# 8. CENTRO O PERIFERIA? (città, A2 minuscolo)
# =====================================================================
CP_SLIDE = [
    cover("🏙️", "Centro o periferia?", "Dove vivere in città: vantaggi e svantaggi", "Città &bull; A2"),
    slide("Che cosa impariamo?", cards([
        ("🏙️", "Il centro", "negozi, uffici, rumore"), ("🏘️", "La periferia", "case più grandi, meno servizi"),
        ("⚖️", "Confrontare", "più… di, meno… di, come"), ("💬", "Dare un'opinione", "secondo me, per me")])),
    slide("🏙️ Vivere in centro", cards([
        ("👍", "Vantaggi", "tutto è vicino: uffici, negozi, scuole, ospedale; tanti autobus; si va a piedi"),
        ("👎", "Svantaggi", "le case costano di più, c'è traffico e rumore, è difficile parcheggiare")])),
    slide("🏘️ Vivere in periferia", cards([
        ("👍", "Vantaggi", "affitti più bassi, case più grandi, più verde e più silenzio"),
        ("👎", "Svantaggi", "pochi servizi, autobus meno frequenti, serve spesso la macchina")])),
    slide("📍 A Bari", nota("A Bari il <b>centro</b> è il quartiere Murat, vicino a Bari Vecchia. I quartieri di <b>periferia</b> sono per esempio "
        "San Paolo, Japigia, Santo Spirito. Tra centro e periferia ci sono i quartieri <b>semicentrali</b>, come Libertà, Madonnella, Poggiofranco.", "font-size:1.2rem;text-align:left")),
    slide("🗣️ Dove cerchiamo casa?", dialogo([
        ("Mariela", "Michele, io e mio marito cerchiamo casa. Secondo te è meglio il centro o la periferia?"),
        ("*Michele", "Dipende. Il centro è più comodo della periferia, ma è anche più caro."),
        ("Mariela", "Noi abbiamo due bambini: ci serve una casa grande."),
        ("*Michele", "In periferia le case sono più grandi e costano meno. E ci sono più parchi."),
        ("Mariela", "Ma noi non abbiamo la macchina…"),
        ("*Michele", "Allora cercate vicino alla stazione o a una fermata dell'autobus: è importante come la casa!")])),
    slide("📘 I comparativi", table([
        ["più + aggettivo + di", "Il centro è più caro della periferia."], ["meno + aggettivo + di", "La periferia è meno rumorosa del centro."],
        ["(così) + aggettivo + come", "Libertà è grande come Japigia."], ["migliore / peggiore", "= più buono / più cattivo"]],
        head=["forma", "esempio"])),
    end("Ora sai confrontare centro e periferia!"),
]
CP = {
 "title": "🏙️ Centro o periferia? · Esercizi", "store": "centro-periferia",
 "sections": [
  {"part": "Centro e periferia"},
  menu(["centro", "periferia"],
       [("1. Gli affitti sono più bassi.", "periferia"), ("2. Ci sono tanti negozi e uffici vicini.", "centro"),
        ("3. C'è più traffico e rumore.", "centro"), ("4. Ci sono più parchi e silenzio.", "periferia"),
        ("5. Spesso serve la macchina.", "periferia"), ("6. È difficile parcheggiare.", "centro")], "1 · Centro o periferia?", "1 · Dove?", "e1",
       cons="Leggi la frase: parla del centro o della periferia?"),
  {"part": "I comparativi", "teoria":
     tab(("più … di", "Il centro è più caro della periferia."), ("meno … di", "La periferia è meno cara del centro."),
         ("… come", "Questa casa è grande come quella.")) +
     "Dopo <b>di</b> l'articolo si unisce: di + il = <b>del</b> · di + la = <b>della</b> · di + l' = <b>dell'</b>. <br>Attenzione: più buono = <b>migliore</b>, più cattivo = <b>peggiore</b>." +
     es("Japigia è più tranquilla del centro.")},
  scegli([("1. In centro le case sono ___ care della periferia.", ["più", "meno", "come"], "più"),
          ("2. La periferia è ___ rumorosa del centro.", ["meno", "più", "come"], "meno"),
          ("3. Il centro è più comodo ___ periferia.", ["della", "del", "dei"], "della"),
          ("4. L'autobus è veloce ___ la metro? No, è più lento.", ["come", "di", "che"], "come"),
          ("5. Questo quartiere è ___ di quello: ci sono più servizi.", ["migliore", "più migliore", "peggio"], "migliore")],
         "2 · Scegli la parola giusta", "2 · Comparativi", "e2"),
  scrivi([("1. La casa in centro (+ piccola) ___ casa in periferia.", ["e piu piccola della"]),
          ("2. Il centro (− tranquillo) ___ periferia.", ["e meno tranquillo della"]),
          ("3. L'affitto a Poggiofranco (+ caro) ___ affitto a San Paolo.", ["e piu caro dell'", "e piu caro dell"])],
         "3 · Scrivi il comparativo", "3 · Scrivi", "e3", cons="Scrivi: è + più/meno + aggettivo + di (con l'articolo).", w="l"),
  vf(["1. Mariela cerca casa con il marito.", "2. Michele dice che il centro è più economico.", "3. Mariela ha due bambini.",
      "4. In periferia le case sono più piccole.", "5. Mariela ha la macchina."], ["VERO", "FALSO", "VERO", "FALSO", "FALSO"],
     "4 · Leggi il dialogo: vero o falso?", "4 · Il dialogo", "e4",
     info="Mariela: Cerchiamo casa. È meglio il centro o la periferia? · Michele: Il centro è più comodo della periferia, ma è anche più caro. · "
          "Mariela: Abbiamo due bambini: ci serve una casa grande. · Michele: In periferia le case sono più grandi e costano meno. · Mariela: Ma noi non abbiamo la macchina…"),
  libero("e5", 5, "Il mio quartiere", "Dove abiti? È centro o periferia? Scrivi 5 frasi con vantaggi e svantaggi. Usa più… di, meno… di.", ["Il mio quartiere"], rows=5),
  parla("e6", 6, "Secondo te è meglio vivere in centro o in periferia? Perché? Confronta anche con la città del tuo paese."),
 ]
}

# =====================================================================
# 9. LE FESTE DELLA REPUBBLICA E LE FESTE POPOLARI (A2 minuscolo)
# =====================================================================
FR_SLIDE = [
    cover("🇮🇹", "Feste civili e feste popolari", "Le date della Repubblica e le tradizioni delle città", "Tempo libero &bull; A2"),
    slide("Che cosa impariamo?", cards([
        ("🇮🇹", "Le feste civili", "25 aprile, 1° maggio, 2 giugno"), ("⛪", "Le feste religiose", "Natale, Pasqua, Ramadan…"),
        ("🎭", "Le feste popolari", "Carnevale, sagre, San Nicola"), ("📅", "Festivo e feriale", "i giorni di festa e di lavoro")])),
    slide("📅 Festivo o feriale?", cards([
        ("🎉", "Giorno festivo", "un giorno di festa: scuole e uffici sono chiusi"), ("💼", "Giorno feriale", "un giorno di lavoro, dal lunedì al sabato"),
        ("🇮🇹", "Festa civile", "ricorda un fatto importante della storia dello Stato"), ("🎂", "Anniversario", "il giorno che ricorda un fatto, ogni anno")])),
    slide("🇮🇹 Le feste civili", cards([
        ("🕊️", "25 aprile", "Festa della Liberazione: nel 1945 finisce la guerra e il fascismo"),
        ("👷", "1° maggio", "Festa dei lavoratori: si ricordano i diritti di chi lavora"),
        ("🗳️", "2 giugno", "Festa della Repubblica: nel 1946 gli italiani (anche le donne!) votano e scelgono la Repubblica")], "g3")),
    slide("🎭 Le feste popolari", cards([
        ("🎭", "Il Carnevale", "febbraio: maschere e carri (Venezia, Viareggio, Putignano in Puglia)"),
        ("🐎", "Il Palio di Siena", "luglio e agosto: una corsa di cavalli in piazza"),
        ("⛵", "San Nicola a Bari", "maggio: il corteo storico e la statua portata in mare"),
        ("🍝", "La sagra", "una festa di paese dedicata a un cibo: la sagra del polpo, delle orecchiette…")], "g2")),
    slide("📖 La festa di San Nicola", nota("Ogni anno a <b>maggio</b> Bari festeggia <b>San Nicola</b>, il santo patrono. Il <b>7 maggio</b> c'è il corteo storico: "
        "centinaia di persone in costume sfilano per la città. L'<b>8 maggio</b> la statua del santo va in mare su una barca e tante barche la seguono. "
        "San Nicola è importante per i cattolici e per gli ortodossi: arrivano pellegrini anche dalla Russia e dall'Est Europa.", "font-size:1.15rem;text-align:left")),
    slide("🗣️ Che cosa fai il 2 giugno?", dialogo([
        ("Cristian", "Ravi, il 2 giugno lavori?"),
        ("*Ravi", "No, è festa. È la Festa della Repubblica, giusto?"),
        ("Cristian", "Sì. A Roma c'è la parata, e qui a Bari ci sono eventi in piazza. Vieni con noi?"),
        ("*Ravi", "Volentieri! Nel mio paese, in India, la festa della Repubblica è il 26 gennaio."),
        ("Cristian", "Davvero? E come la festeggiate?"),
        ("*Ravi", "Con una grande parata a Nuova Delhi e la bandiera su tutte le case.")])),
    end("Ora conosci le feste italiane!"),
]
FR = {
 "title": "🇮🇹 Feste civili e popolari · Esercizi", "store": "feste-repubblica",
 "sections": [
  {"part": "Le date"},
  menu(["25 aprile", "1° maggio", "2 giugno", "8 maggio", "febbraio"],
       [("1. Festa della Repubblica", "2 giugno"), ("2. Festa dei lavoratori", "1° maggio"), ("3. Festa della Liberazione", "25 aprile"),
        ("4. La statua di San Nicola va in mare", "8 maggio"), ("5. Il Carnevale", "febbraio")], "1 · Quando?", "1 · Le date", "e1", cons="Scegli la data giusta."),
  menu(["festivo", "feriale"],
       [("1. Il 25 dicembre è un giorno ___.", "festivo"), ("2. Martedì 14 ottobre è un giorno ___.", "feriale"),
        ("3. Il 2 giugno è un giorno ___.", "festivo"), ("4. Un giorno normale di lavoro è ___.", "feriale")], "2 · Festivo o feriale?", "2 · Festivo / feriale", "e2"),
  {"part": "Leggo il testo"},
  vf(["1. San Nicola è il patrono di Bari.", "2. Il corteo storico è il 7 maggio.", "3. La statua va in montagna.",
      "4. San Nicola è importante solo per i cattolici.", "5. Arrivano pellegrini dall'Est Europa."],
     ["VERO", "VERO", "FALSO", "FALSO", "VERO"], "3 · San Nicola: vero o falso?", "3 · San Nicola", "e3",
     info="Ogni anno a maggio Bari festeggia San Nicola, il santo patrono. Il 7 maggio c'è il corteo storico. L'8 maggio la statua del santo va in mare su una barca. "
          "San Nicola è importante per i cattolici e per gli ortodossi: arrivano pellegrini anche dalla Russia e dall'Est Europa."),
  {"part": "Il passato prossimo", "teoria":
     tab(("avere", "ho festeggiato, abbiamo visto", "la maggior parte dei verbi"), ("essere", "sono andato/a, siamo usciti/e", "andare, venire, uscire, partire, tornare…")) +
     "Per raccontare una festa del passato: <b>avere/essere + participio</b>. Con essere il participio cambia (andato, andata, andati, andate)." +
     es("Il 2 giugno siamo andati in piazza e abbiamo visto i fuochi.")},
  scrivi([("1. L'anno scorso io (andare) ___ al Carnevale di Putignano.", ["sono andato", "sono andata"]),
          ("2. Noi (vedere) ___ i carri.", ["abbiamo visto"]), ("3. I bambini (mettere) ___ la maschera.", ["hanno messo"]),
          ("4. Il 1° maggio Ravi (fare) ___ un picnic.", ["ha fatto"]), ("5. Le ragazze (tornare) ___ a casa tardi.", ["sono tornate"])],
         "4 · Racconta al passato", "4 · Passato prossimo", "e4", w="m"),
  libero("e5", 5, "Una festa del mio paese", "Racconta una festa del tuo paese (civile, religiosa o popolare): quando è, che cosa si fa, che cosa hai fatto l'ultima volta.", ["La festa"], rows=5),
  parla("e6", 6, "Racconta la festa più bella che hai fatto in Italia: dove, quando, con chi, che cosa avete fatto."),
 ]
}

# =====================================================================
# 10-12. EDUCAZIONE CIVICA: UNIONE EUROPEA, STATO ITALIANO, ENTI LOCALI (A2 minuscolo)
# =====================================================================
UE_SLIDE = [
    cover("🇪🇺", "L'Unione europea", "27 paesi insieme: storia, istituzioni, diritti", "Educazione civica &bull; A2"),
    slide("Che cosa impariamo?", cards([
        ("📜", "La storia", "dal 1957 a oggi"), ("🏛️", "Le istituzioni", "Parlamento, Commissione, Consiglio, Corte"),
        ("💶", "L'euro", "la moneta comune"), ("🧳", "I diritti", "viaggiare, studiare, lavorare")])),
    slide("📜 Un po' di storia", table([
        ["1957", "Trattati di Roma: 6 paesi (Italia, Francia, Germania, Belgio, Paesi Bassi, Lussemburgo) creano la Comunità economica europea"],
        ["1992", "Trattato di Maastricht: nasce l'Unione europea"], ["2002", "l'euro entra nelle tasche dei cittadini"],
        ["oggi", "27 paesi, circa 450 milioni di persone"]], head=["anno", "che cosa succede"])),
    slide("🏛️ Le istituzioni", cards([
        ("🗳️", "Il Parlamento europeo", "a Strasburgo e Bruxelles: i cittadini lo votano ogni 5 anni"),
        ("📋", "La Commissione europea", "a Bruxelles: propone le leggi e controlla che si rispettino"),
        ("🤝", "Il Consiglio dell'Unione", "i ministri dei 27 paesi: approva le leggi con il Parlamento"),
        ("⚖️", "La Corte di giustizia", "in Lussemburgo: controlla che le leggi europee siano rispettate")])),
    slide("⭐ I simboli", cards([
        ("🇪🇺", "La bandiera", "12 stelle d'oro in cerchio su sfondo blu: unità e armonia"), ("🎵", "L'inno", "l'«Inno alla gioia» di Beethoven"),
        ("📅", "La festa", "il 9 maggio, Festa dell'Europa"), ("💬", "Il motto", "«Unita nella diversità»")])),
    slide("🧳 Che cosa cambia per le persone?", cards([
        ("🛂", "Viaggiare", "nell'area Schengen non ci sono controlli alle frontiere"), ("🎓", "Studiare", "con l'Erasmus si studia in un altro paese"),
        ("💼", "Lavorare", "i cittadini UE possono lavorare in tutti i paesi dell'Unione"), ("📱", "Telefonare", "il roaming nell'UE costa come a casa")]) + "\n" +
        nota("⚠️ Chi ha un permesso di soggiorno italiano può viaggiare nei paesi Schengen per turismo fino a 90 giorni, ma non può lavorare lì senza un altro permesso.")),
    end("Ora conosci l'Unione europea!"),
]
UE = {
 "title": "🇪🇺 L'Unione europea · Esercizi", "store": "unione-europea",
 "sections": [
  {"part": "Le istituzioni"},
  menu(["Parlamento europeo", "Commissione europea", "Consiglio dell'Unione", "Corte di giustizia"],
       [("1. I cittadini lo votano ogni 5 anni.", "Parlamento europeo"), ("2. Propone le leggi.", "Commissione europea"),
        ("3. Ci sono i ministri dei 27 paesi.", "Consiglio dell'Unione"), ("4. Controlla che le leggi siano rispettate.", "Corte di giustizia")],
       "1 · Quale istituzione?", "1 · Le istituzioni", "e1", cons="Scegli l'istituzione giusta."),
  scegli([("1. Quanti paesi ci sono oggi nell'Unione europea?", ["27", "12", "50"], "27"),
          ("2. Dove sono stati firmati i trattati del 1957?", ["a Roma", "a Parigi", "a Berlino"], "a Roma"),
          ("3. Quando entra in uso l'euro?", ["nel 2002", "nel 1957", "nel 1992"], "nel 2002"),
          ("4. Quante stelle ci sono sulla bandiera?", ["12", "27", "6"], "12"),
          ("5. Qual è la festa dell'Europa?", ["il 9 maggio", "il 2 giugno", "il 25 aprile"], "il 9 maggio")],
         "2 · Scegli la risposta giusta", "2 · Storia e simboli", "e2"),
  {"part": "Le date e i numeri", "teoria":
     tab(("nel + anno", "nel 1957, nel 2002"), ("il + giorno + mese", "il 9 maggio"), ("da … a …", "dal 1957 a oggi"),
         ("circa", "circa 450 milioni")) +
     "Con gli anni si usa <b>nel</b> (in + il). I numeri grandi: mille (1.000), un milione (1.000.000), un miliardo." +
     es("L'Italia è entrata nella Comunità europea nel 1957.")},
  menu(["nel", "il", "dal", "circa"],
       [("1. L'euro è nato ___ 2002.", "nel"), ("2. La Festa dell'Europa è ___ 9 maggio.", "il"),
        ("3. L'Italia è nell'Unione ___ 1957.", "dal"), ("4. Nell'Unione vivono ___ 450 milioni di persone.", "circa")],
       "3 · Completa con la parola giusta", "3 · Date e numeri", "e3"),
  vf(["1. Nell'area Schengen non ci sono controlli alle frontiere.", "2. Con l'Erasmus si studia all'estero.",
      "3. Con il permesso di soggiorno italiano posso lavorare in Germania senza altri documenti.", "4. Il Parlamento europeo è a Strasburgo e Bruxelles."],
     ["VERO", "VERO", "FALSO", "VERO"], "4 · Vero o falso?", "4 · I diritti", "e4"),
  libero("e5", 5, "Il mio paese e l'Europa", "Il tuo paese fa parte di un'unione di stati (per esempio Unione africana, Lega araba, ASEAN)? Scrivi 4-5 frasi.", ["Il mio paese…"], rows=5),
  parla("e6", 6, "Secondo te che cosa è utile dell'Unione europea per le persone che vivono in Italia?"),
 ]
}

STATO_SLIDE = [
    cover("🏛️", "Lo Stato italiano", "La Costituzione e i poteri dello Stato", "Educazione civica &bull; A2"),
    slide("Che cosa impariamo?", cards([
        ("📜", "La Costituzione", "la legge più importante"), ("🗳️", "Il Parlamento", "fa le leggi"), ("🏢", "Il Governo", "governa il paese"),
        ("⚖️", "La magistratura", "giudica"), ("👤", "Il Presidente della Repubblica", "rappresenta l'unità del paese")], "g3")),
    slide("📜 La Costituzione", nota("L'Italia è una <b>Repubblica democratica</b> dal 2 giugno 1946. La <b>Costituzione</b> è entrata in vigore il "
        "<b>1° gennaio 1948</b>. Ha 139 articoli e dice i diritti e i doveri di tutte le persone.", "font-size:1.2rem;text-align:left") + "\n" +
        table([["Art. 1", "L'Italia è una Repubblica democratica, fondata sul lavoro."], ["Art. 3", "Tutti sono uguali davanti alla legge, senza differenze di sesso, razza, lingua, religione."],
               ["Art. 32", "La salute è un diritto."], ["Art. 34", "La scuola è aperta a tutti."]], head=["articolo", "che cosa dice (in parole semplici)"])),
    slide("⚖️ I tre poteri", cards([
        ("🗳️", "Potere legislativo", "il Parlamento (Camera dei deputati + Senato) fa le leggi"),
        ("🏢", "Potere esecutivo", "il Governo (Presidente del Consiglio e ministri) mette in pratica le leggi"),
        ("⚖️", "Potere giudiziario", "i giudici (la magistratura) controllano che le leggi siano rispettate")], "g3") + "\n" +
        nota("I tre poteri sono <b>separati</b>: così nessuno ha tutto il potere.")),
    slide("👤 Il Presidente della Repubblica", cards([
        ("🗳️", "Chi lo elegge", "il Parlamento, ogni 7 anni"), ("🏰", "Dove lavora", "al Palazzo del Quirinale, a Roma"),
        ("✍️", "Che cosa fa", "firma le leggi, nomina il Presidente del Consiglio, è capo delle forze armate"),
        ("🇮🇹", "Che cosa rappresenta", "l'unità di tutto il paese")])),
    slide("🗳️ Le elezioni", cards([
        ("🗳️", "Chi vota", "i cittadini italiani dai 18 anni"), ("📅", "Ogni quanto", "il Parlamento si vota ogni 5 anni"),
        ("🏘️", "Le elezioni comunali", "anche i cittadini UE residenti possono votare per il sindaco")])),
    end("Ora conosci lo Stato italiano!"),
]
STATO = {
 "title": "🏛️ Lo Stato italiano · Esercizi", "store": "stato-italiano",
 "sections": [
  {"part": "I poteri dello Stato"},
  menu(["Parlamento", "Governo", "magistratura", "Presidente della Repubblica"],
       [("1. Fa le leggi.", "Parlamento"), ("2. Mette in pratica le leggi.", "Governo"), ("3. Giudica chi non rispetta la legge.", "magistratura"),
        ("4. Lavora al Quirinale e firma le leggi.", "Presidente della Repubblica"), ("5. È formato da Camera e Senato.", "Parlamento"),
        ("6. Ha un Presidente del Consiglio e i ministri.", "Governo")], "1 · Chi è?", "1 · I poteri", "e1", cons="Scegli la risposta giusta."),
  scegli([("1. Da quando l'Italia è una Repubblica?", ["dal 1946", "dal 1861", "dal 2002"], "dal 1946"),
          ("2. Quando è entrata in vigore la Costituzione?", ["il 1° gennaio 1948", "il 2 giugno 1946", "il 25 aprile 1945"], "il 1° gennaio 1948"),
          ("3. Ogni quanti anni si elegge il Presidente della Repubblica?", ["7", "5", "4"], "7"),
          ("4. Che cosa dice l'articolo 3?", ["tutti sono uguali davanti alla legge", "la scuola è a pagamento", "solo gli italiani hanno diritti"], "tutti sono uguali davanti alla legge")],
         "2 · Scegli la risposta giusta", "2 · La Costituzione", "e2"),
  {"part": "Il passivo (essere + participio)", "teoria":
     tab(("attivo", "Il Parlamento <b>elegge</b> il Presidente."), ("passivo", "Il Presidente <b>è eletto</b> dal Parlamento.")) +
     "Nei testi di educazione civica si usa spesso il <b>passivo</b>: essere + participio + <b>da</b>. Il participio cambia come un aggettivo (eletto, eletta, eletti, elette)." +
     es("Le leggi sono fatte dal Parlamento.")},
  menu(["è eletto", "sono fatte", "è formato", "sono eletti", "è firmata"],
       [("1. Il Presidente ___ dal Parlamento.", "è eletto"), ("2. Le leggi ___ dal Parlamento.", "sono fatte"),
        ("3. Il Parlamento ___ dalla Camera e dal Senato.", "è formato"), ("4. I deputati ___ dai cittadini.", "sono eletti"),
        ("5. La legge ___ dal Presidente.", "è firmata")], "3 · Completa con il passivo", "3 · Il passivo", "e3"),
  ordina(["2 giugno 1946: gli italiani votano.", "Nasce la Repubblica italiana.", "1° gennaio 1948: entra in vigore la Costituzione.",
          "Ogni 5 anni i cittadini votano il Parlamento."], "4 · Metti in ordine la storia", "4 · In ordine", "e4", cons="Metti in ordine: 1, 2, 3…"),
  libero("e5", 5, "Lo Stato nel mio paese", "Nel tuo paese chi fa le leggi? C'è un presidente o un re? Ogni quanto si vota? Scrivi 5 frasi.", ["Nel mio paese…"], rows=5),
  parla("e6", 6, "Quale articolo della Costituzione italiana ti sembra più importante? Perché?"),
 ]
}

ENTI_SLIDE = [
    cover("🗺️", "Regione, città metropolitana, Comune", "Gli enti locali: chi decide vicino a noi", "Educazione civica &bull; A2"),
    slide("Che cosa impariamo?", cards([
        ("🗺️", "La Regione", "20 regioni: la Puglia"), ("🏙️", "La città metropolitana", "Bari e i comuni vicini"),
        ("🏘️", "Il Comune", "il sindaco e il consiglio comunale"), ("📋", "I servizi", "chi fa che cosa")])),
    slide("🗺️ Le Regioni", nota("L'Italia ha <b>20 regioni</b>. Ogni regione ha un <b>Presidente</b>, una <b>Giunta</b> e un <b>Consiglio regionale</b>. "
        "La Regione decide soprattutto sulla <b>sanità</b> (ospedali, ASL), i trasporti locali, la formazione professionale. "
        "La nostra regione è la <b>Puglia</b>: il capoluogo è Bari.", "font-size:1.2rem;text-align:left")),
    slide("🏙️ Province e città metropolitane", nota("Le <b>province</b> sono più grandi di un comune e più piccole di una regione. Nelle città grandi c'è la "
        "<b>città metropolitana</b>: a Bari unisce 41 comuni. Si occupa per esempio delle strade provinciali e delle scuole superiori.", "font-size:1.2rem;text-align:left")),
    slide("🏘️ Il Comune", cards([
        ("👤", "Il sindaco", "è il capo del Comune: i cittadini lo votano ogni 5 anni"), ("👥", "La giunta", "il sindaco e gli assessori (scuola, trasporti, ambiente…)"),
        ("🗳️", "Il consiglio comunale", "i consiglieri votati dai cittadini: approvano le decisioni"),
        ("🏛️", "Il municipio", "il palazzo del Comune; a Bari ci sono anche 5 municipi di quartiere")])),
    slide("📋 Chi fa che cosa?", table([
        ["Comune", "anagrafe, residenza, carta d'identità, asili e scuole primarie, rifiuti e TARI, vigili urbani"],
        ["Città metropolitana", "strade provinciali, edifici delle scuole superiori"],
        ["Regione", "ospedali e ASL, treni regionali, corsi di formazione"],
        ["Stato", "permesso di soggiorno (Questura), tasse nazionali, scuola, esercito"]], head=["ente", "servizi"])),
    slide("🗣️ A chi chiedo?", dialogo([
        ("Tesfaye", "Eneida, la strada davanti a casa è piena di buche. A chi devo scrivere?"),
        ("*Eneida", "Dipende dalla strada: se è una via di Bari, al Comune. Puoi segnalarlo anche sul sito del Comune."),
        ("Tesfaye", "E per il corso di formazione da saldatore?"),
        ("*Eneida", "Quelli li organizza la Regione Puglia, con i centri di formazione."),
        ("Tesfaye", "E il rinnovo del permesso?"),
        ("*Eneida", "Quello no: è della Questura, cioè dello Stato.")])),
    end("Ora sai chi decide vicino a te!"),
]
ENTI = {
 "title": "🗺️ Gli enti locali · Esercizi", "store": "enti-locali",
 "sections": [
  {"part": "Chi fa che cosa?"},
  menu(["Comune", "Regione", "Stato", "città metropolitana"],
       [("1. La carta d'identità.", "Comune"), ("2. Gli ospedali e le ASL.", "Regione"), ("3. Il permesso di soggiorno.", "Stato"),
        ("4. La raccolta dei rifiuti.", "Comune"), ("5. Le strade provinciali.", "città metropolitana"), ("6. I corsi di formazione professionale.", "Regione")],
       "1 · Chi se ne occupa?", "1 · Chi fa che cosa", "e1", cons="Scegli l'ente giusto."),
  scegli([("1. Quante regioni ha l'Italia?", ["20", "27", "41"], "20"), ("2. Qual è il capoluogo della Puglia?", ["Bari", "Lecce", "Foggia"], "Bari"),
          ("3. Chi è il capo del Comune?", ["il sindaco", "il prefetto", "il ministro"], "il sindaco"),
          ("4. Ogni quanti anni si vota il sindaco?", ["5", "7", "2"], "5")], "2 · Scegli la risposta giusta", "2 · Gli enti", "e2"),
  {"part": "I pronomi diretti", "teoria":
     tab(("lo", "il sindaco → <b>lo</b> votano i cittadini"), ("la", "la carta d'identità → <b>la</b> fa il Comune"),
         ("li", "i corsi → <b>li</b> organizza la Regione"), ("le", "le strade → <b>le</b> controlla il Comune")) +
     "Per non ripetere una parola usiamo il <b>pronome</b>, prima del verbo." + es("Il permesso di soggiorno? Lo rinnova la Questura.")},
  menu(["lo", "la", "li", "le"],
       [("1. Il sindaco? ___ votano i cittadini.", "lo"), ("2. La TARI? ___ paghiamo al Comune.", "la"),
        ("3. I corsi di formazione? ___ organizza la Regione.", "li"), ("4. Le scuole superiori? ___ gestisce la città metropolitana.", "le"),
        ("5. Il permesso? ___ rinnova la Questura.", "lo")], "3 · Lo, la, li o le?", "3 · Pronomi", "e3"),
  completa("Tesfaye vuole segnalare le ___ nella strada: deve scrivere al ___. Per il corso da saldatore deve chiedere alla ___ Puglia. "
           "Per il rinnovo del permesso va in ___.",
           ["buche", "comune", "regione", "questura"], "4 · Completa il testo", "4 · A chi chiedo", "e4", "buche · Comune · Regione · Questura", cons="Scrivi la parola giusta."),
  libero("e5", 5, "Il mio Comune", "Scrivi 4-5 frasi: in che Comune abiti? Chi è il sindaco? Quali servizi del Comune usi?", ["Il mio Comune"], rows=5),
  parla("e6", 6, "Che cosa vorresti cambiare nel tuo quartiere? A chi devi chiedere: al Comune, alla Regione o allo Stato?"),
 ]
}

SLIDE_ANCHIO = [
    ("condominio/index.html", "VIVERE IN CONDOMINIO", "CASA", COND_SLIDE, ILL_CSS),
    ("autocertificazione/index.html", "L'AUTOCERTIFICAZIONE", "FAMIGLIA", AUTO_SLIDE, ILL_CSS),
    ("piatti-dal-mondo/index.html", "PIATTI DAL MONDO", "CIBO", PIATTI_SLIDE, ILL_CSS),
    ("volontariato/index.html", "IL VOLONTARIATO", "CITTÀ", VOL_SLIDE, ILL_CSS),
    ("in-strada/index.html", "IN STRADA", "CITTÀ", STRADA_SLIDE, ILL_CSS),
    ("cup-specialisti/index.html", "IL CUP E GLI SPECIALISTI", "SALUTE", CUP_SLIDE, ILL_CSS),
    ("tasse/index.html", "Pagare le tasse", "Educazione civica", TASSE_SLIDE, A2_CSS),
    ("centro-periferia/index.html", "Centro o periferia?", "Città", CP_SLIDE, A2_CSS),
    ("feste-repubblica/index.html", "Feste civili e popolari", "Tempo libero", FR_SLIDE, A2_CSS),
    ("unione-europea/index.html", "L'Unione europea", "Educazione civica", UE_SLIDE, A2_CSS),
    ("stato-italiano/index.html", "Lo Stato italiano", "Educazione civica", STATO_SLIDE, A2_CSS),
    ("enti-locali/index.html", "Gli enti locali", "Educazione civica", ENTI_SLIDE, A2_CSS),
]
ESERCIZI_ANCHIO = [("condominio", COND), ("autocertificazione", AUTO), ("piatti-dal-mondo", PIATTI), ("volontariato", VOL),
                   ("in-strada", STRADA), ("cup-specialisti", CUP), ("tasse", TASSE), ("centro-periferia", CP),
                   ("feste-repubblica", FR), ("unione-europea", UE), ("stato-italiano", STATO), ("enti-locali", ENTI)]

# ---------------------------------------------------------------- 2026-11-04, Erila: la teoria semplice anche prima degli altri esercizi
# (lessico e letture): un riquadro «La regola» in ogni parte, non solo in quelle di grammatica
_TEORIA_EXTRA = {
  ("condominio", "Il palazzo"): tab(("IL PORTONE", "L'ENTRATA"), ("LE SCALE / L'ASCENSORE", "PER SALIRE"), ("IL PIANEROTTOLO", "DAVANTI ALLA PORTA"),
      ("IL CORTILE", "LO SPAZIO FUORI"), ("IL CITOFONO", "SUONO E PARLO")) + "LE PARTI COMUNI SONO DI <b>TUTTI</b>: PER QUESTO CI SONO LE REGOLE." +
      es("IL SILENZIO: DALLE 22 ALLE 8."),
  ("condominio", "Sul pianerottolo"): tab(("SALUTARE", "BUONGIORNO! PIACERE!"), ("PRESENTARSI", "MI CHIAMO… ABITO AL TERZO PIANO."),
      ("SCUSARSI", "MI DISPIACE! LO SPOSTO SUBITO.")) + "CON UN VICINO CHE NON CONOSCI USA <b>LEI</b>: «LEI È IL NUOVO VICINO?»",
  ("autocertificazione", "Leggo il modulo"): tab(("COGNOME E NOME", "DIALLO AMADOU"), ("LUOGO DI NASCITA", "DOVE SEI NATO"),
      ("DATA DI NASCITA", "GIORNO / MESE / ANNO"), ("PARENTELA", "CHI È PER TE: MOGLIE, FIGLIO…")) +
      "NEI MODULI SI SCRIVE PRIMA IL <b>COGNOME</b>, POI IL <b>NOME</b>. ALLA FINE: <b>DATA E FIRMA</b>.",
  ("autocertificazione", "La parentela"): tab(("MARITO", "MOGLIE"), ("FIGLIO", "FIGLIA"), ("SUOCERO", "SUOCERA"), ("NIPOTE", "NIPOTE"),
      head=("UOMO", "DONNA")) + "IL <b>NIPOTE</b> È IL FIGLIO DI MIO FIGLIO O DI MIO FRATELLO / MIA SORELLA." + es("AISSATOU È LA MOGLIE DI AMADOU."),
  ("piatti-dal-mondo", "Di dov'è?"): tab(("LA PIZZA", "ITALIA (NAPOLI)"), ("IL SUSHI", "GIAPPONE"), ("IL KEBAB", "TURCHIA"),
      ("IL CUSCUS", "MAROCCO, TUNISIA, ALGERIA"), ("L'INJERA", "ETIOPIA, ERITREA"), ("IL BIRYANI", "PAKISTAN, INDIA")) +
      "PER DIRE DA DOVE VIENE: «È UN PIATTO <b>DEL</b> GIAPPONE», «<b>DELLA</b> TURCHIA», «<b>DELL'</b>ITALIA»." + es("IL SUSHI È UN PIATTO DEL GIAPPONE."),
  ("volontariato", "Le associazioni"): tab(("CROCE ROSSA", "AMBULANZE, EMERGENZE"), ("AVIS", "DONARE IL SANGUE"), ("CARITAS", "MENSA, VESTITI"),
      ("AUSER", "ANZIANI"), ("UNICEF", "BAMBINI")) + "IL <b>VOLONTARIO</b> AIUTA <b>GRATIS</b>, NEL TEMPO LIBERO." + es("ALL'AVIS DONO IL SANGUE."),
  ("in-strada", "Le parole della strada"): tab(("🔴 ROSSO", "STOP, ASPETTA"), ("🟡 GIALLO", "ATTENZIONE"), ("🟢 VERDE", "ATTRAVERSA")) +
      "IL PEDONE CAMMINA SUL <b>MARCIAPIEDE</b> E ATTRAVERSA SULLE <b>STRISCE</b>. LA BICI VA SULLA <b>PISTA CICLABILE</b>, CON IL <b>CASCO</b>.",
  ("cup-specialisti", "Gli specialisti"): tab(("CUORE", "CARDIOLOGO"), ("DENTI", "DENTISTA"), ("OCCHI", "OCULISTA"), ("GOLA, NASO", "OTORINO"),
      ("PELLE", "DERMATOLOGO"), ("OSSA", "ORTOPEDICO"), ("BAMBINI", "PEDIATRA")) + "PER ANDARE DALLO SPECIALISTA DI SOLITO SERVE L'<b>IMPEGNATIVA</b> DEL MEDICO DI BASE." +
      es("MI FA MALE UN DENTE: VADO DAL DENTISTA."),
  ("cup-specialisti", "Prenoto la visita"): "1. MEDICO DI BASE → 2. IMPEGNATIVA → 3. CUP (TELEFONO, SPORTELLO O FARMACIA) → 4. TICKET → 5. VISITA." +
      "<br>IL GIORNO DELLA VISITA PORTO: IMPEGNATIVA, <b>TESSERA SANITARIA</b>, RICEVUTA DEL TICKET.",
  ("tasse", "Le tasse"): tab(("IRPEF", "sullo stipendio"), ("IVA", "nel prezzo delle cose"), ("TARI", "sui rifiuti, per chi abita in una casa"),
      ("bollo auto", "per la macchina"), ("ticket", "per visite ed esami")) + "Con le tasse lo Stato paga <b>scuole, ospedali, strade</b>. Chi guadagna di più paga di più (art. 53).",
  ("centro-periferia", "Centro e periferia"): tab(("centro", "servizi vicini, tanti autobus", "case care, traffico, rumore"),
      ("periferia", "affitti bassi, case grandi, verde", "pochi servizi, serve la macchina"), head=("", "👍 vantaggi", "👎 svantaggi")) +
      "Per dare un'opinione: <b>secondo me</b>…, <b>per me</b>…, <b>dipende</b>." + es("Secondo me il centro è comodo ma caro."),
  ("feste-repubblica", "Le date"): tab(("25 aprile", "Liberazione"), ("1° maggio", "Festa dei lavoratori"), ("2 giugno", "Festa della Repubblica"),
      ("7-8 maggio", "San Nicola a Bari"), ("febbraio", "Carnevale")) + "<b>Festivo</b> = giorno di festa (uffici chiusi). <b>Feriale</b> = giorno di lavoro." +
      es("Il 2 giugno è un giorno festivo."),
  ("feste-repubblica", "Leggo il testo"): "Prima di leggere guarda le <b>date</b> e i <b>nomi</b>: ti aiutano a capire. Poi leggi tutto e rispondi." +
      tab(("patrono", "il santo protettore della città"), ("corteo", "tante persone che camminano insieme"), ("pellegrino", "chi viaggia per motivi religiosi")),
  ("unione-europea", "Le istituzioni"): tab(("Parlamento europeo", "votato dai cittadini ogni 5 anni"), ("Commissione europea", "propone le leggi"),
      ("Consiglio dell'Unione", "i ministri dei 27 paesi"), ("Corte di giustizia", "controlla il rispetto delle leggi")) +
      "Le leggi europee le approvano <b>insieme</b> il Parlamento e il Consiglio.",
  ("stato-italiano", "I poteri dello Stato"): tab(("legislativo", "Parlamento (Camera + Senato)", "fa le leggi"),
      ("esecutivo", "Governo", "mette in pratica le leggi"), ("giudiziario", "magistratura", "giudica"), head=("potere", "chi", "che cosa fa")) +
      "Il <b>Presidente della Repubblica</b> rappresenta l'unità del paese e firma le leggi.",
  ("enti-locali", "Chi fa che cosa?"): tab(("Comune", "anagrafe, carta d'identità, rifiuti, TARI"), ("Città metropolitana", "strade provinciali, scuole superiori"),
      ("Regione", "ospedali, ASL, formazione"), ("Stato", "Questura, permesso di soggiorno")) +
      "Dal più piccolo al più grande: <b>Comune → città metropolitana → Regione → Stato</b>.",
}
for _d, _p in ESERCIZI_ANCHIO:
    for _s in _p["sections"]:
        _t = _TEORIA_EXTRA.get((_d, _s.get("part")))
        if _t:
            assert "teoria" not in _s
            _s["teoria"] = _t
assert all(any(s.get("part") == part for s in dict(ESERCIZI_ANCHIO)[d]["sections"]) for d, part in _TEORIA_EXTRA)
