"""Unità sugli argomenti di Nuovo Espresso 1 e Dieci A1/A2 che il sito non aveva (2026-10-30).
Dei libri si prendono solo gli argomenti: testi, dialoghi ed esercizi sono scritti per il sito, ambientati a Bari.
  tempo-libero/ (A1)  · che cosa fai nel tempo libero? sempre, spesso, qualche volta, mai
  ristorante/ (A1)    · al ristorante da cliente: prenotare, il menù, ordinare, il conto
  feste/ (A1)         · feste e tradizioni, gli auguri, i mesi
  in-vacanza/ (A2)    · raccontare una vacanza al passato prossimo (stampatello minuscolo: è A2)
A1 in STAMPATELLO MAIUSCOLO."""
from genera import eq
from unita_primi import cover, slide, cards, table, nota, dialogo, end
from foto_cibi import foto, crediti_slide, FOTO_CSS
from unita_drive import ILL_CSS, vf, scegli, menu, scrivi, ordina, completa, parla, libero

# =====================================================================
# 1. IL TEMPO LIBERO (A1)
# =====================================================================
TEMPO_SLIDE = [
    cover("⚽", "IL TEMPO LIBERO", "CHE COSA FAI QUANDO NON LAVORI?", "TEMPO LIBERO &bull; A1"),
    slide("CHE COSA IMPARIAMO?", cards([
        ("🎬", "LE ATTIVITÀ", "VADO AL CINEMA, GIOCO A CALCIO…"), ("🔁", "QUANTE VOLTE?", "SEMPRE, SPESSO, MAI"),
        ("❤️", "MI PIACE", "MI PIACE BALLARE, NON MI PIACE CORRERE"), ("📅", "PROPORRE", "TI VA DI…? VA BENE!")])),
    slide("🎬 CHE COSA FACCIO?", cards([
        ("⚽", "GIOCO A CALCIO", "CON GLI AMICI"), ("🏃", "CORRO", "AL PARCO, SUL LUNGOMARE"), ("🎬", "VADO AL CINEMA", ""),
        ("📖", "LEGGO", "UN LIBRO, IL GIORNALE"), ("🎵", "ASCOLTO LA MUSICA", ""), ("📺", "GUARDO LA TV", "LE SERIE, IL CALCIO"),
        ("🍳", "CUCINO", "PER LA FAMIGLIA"), ("🕌", "VADO IN MOSCHEA / IN CHIESA", ""), ("🏖️", "VADO AL MARE", "D'ESTATE")], "g3")),
    slide("🔁 QUANTE VOLTE?", table([
        ["SEMPRE", "100%", "LA DOMENICA <b>SEMPRE</b> CUCINO IO."], ["DI SOLITO", "80%", "<b>DI SOLITO</b> IL SABATO VADO AL MARE."],
        ["SPESSO", "60%", "VADO <b>SPESSO</b> AL CINEMA."], ["QUALCHE VOLTA", "30%", "<b>QUALCHE VOLTA</b> GIOCO A CALCIO."],
        ["RARAMENTE", "10%", "GUARDO <b>RARAMENTE</b> LA TV."], ["MAI", "0%", "NON CORRO <b>MAI</b>."]], head=["PAROLA", "", "ESEMPIO"]) + "\n" +
        nota("⚠️ CON <b>MAI</b> SERVE ANCHE <b>NON</b>: «NON VADO MAI IN PALESTRA».")),
    slide("📅 OGNI GIORNO, UNA VOLTA…", cards([
        ("📆", "OGNI GIORNO", "TUTTI I GIORNI"), ("1️⃣", "UNA VOLTA ALLA SETTIMANA", "PER ESEMPIO IL SABATO"),
        ("2️⃣", "DUE VOLTE AL MESE", ""), ("🌙", "LA SERA / IL FINE SETTIMANA", "QUANDO NON LAVORO")])),
    slide("❤️ MI PIACE / NON MI PIACE", cards([
        ("😀", "MI PIACE BALLARE", "MI PIACE + VERBO"), ("😀", "MI PIACE IL CALCIO", "MI PIACE + UNA COSA"),
        ("😀", "MI PIACCIONO I FILM", "MI PIACCIONO + TANTE COSE"), ("🙁", "NON MI PIACE CORRERE", "")]) + "\n" +
        nota("E A TE? → «TI PIACE LEGGERE?» «SÌ, MOLTO!» / «NO, PER NIENTE.»")),
    slide("🗣️ TI VA DI…?", dialogo([
        ("AMINA", "CIAO GRACE! CHE COSA FAI SABATO?"),
        ("*GRACE", "NIENTE DI SPECIALE. DI SOLITO IL SABATO PULISCO LA CASA."),
        ("AMINA", "TI VA DI ANDARE AL CINEMA LA SERA?"),
        ("*GRACE", "SÌ, VOLENTIERI! IO VADO RARAMENTE AL CINEMA."),
        ("AMINA", "PERFETTO. CI VEDIAMO ALLE 8 DAVANTI AL CINEMA?"),
        ("*GRACE", "VA BENE. A SABATO!")])),
    slide("🗣️ COME RISPONDO?", table([
        ["✅ SÌ", "VOLENTIERI! · VA BENE! · CHE BELLO!"], ["❌ NO", "MI DISPIACE, NON POSSO. · SABATO LAVORO."],
        ["🤔 FORSE", "NON SO, TI CHIAMO DOMANI."]], head=["", "FRASI"])),
    end("ORA SAI PARLARE DEL TUO TEMPO LIBERO!"),
]
TEMPO = {
 "title": "⚽ Il tempo libero · Esercizi", "store": "tempo-libero", "upper": True,
 "sections": [
  {"part": "Le attività"},
  menu(["GIOCO", "VADO", "LEGGO", "ASCOLTO", "GUARDO"],
       [("1. ___ A CALCIO CON GLI AMICI.", "GIOCO"), ("2. ___ AL CINEMA IL SABATO.", "VADO"), ("3. ___ LA MUSICA IN AUTOBUS.", "ASCOLTO"),
        ("4. ___ UN LIBRO PRIMA DI DORMIRE.", "LEGGO"), ("5. ___ LA TV LA SERA.", "GUARDO"), ("6. ___ AL MARE D'ESTATE.", "VADO")],
       "1 · Scegli il verbo", "1 · I verbi", "e1"),
  {"part": "Quante volte?"},
  ordina(["MAI", "RARAMENTE", "QUALCHE VOLTA", "SPESSO", "DI SOLITO", "SEMPRE"],
         "2 · Da 0% a 100%: metti in ordine", "2 · In ordine", "e2", cons="METTI IN ORDINE: 1 = MAI (0%) … 6 = SEMPRE (100%)."),
  scegli([("1. GRACE ___ VA AL CINEMA: UNA VOLTA ALL'ANNO.", ["RARAMENTE", "SEMPRE", "SPESSO"], "RARAMENTE"),
          ("2. LA DOMENICA AMINA ___ CUCINA PER TUTTI: OGNI DOMENICA!", ["SEMPRE", "MAI", "QUALCHE VOLTA"], "SEMPRE"),
          ("3. YUSUF NON BEVE ___ IL CAFFÈ.", ["MAI", "SPESSO", "SEMPRE"], "MAI"),
          ("4. VADO IN PALESTRA ___ ALLA SETTIMANA.", ["DUE VOLTE", "DUE GIORNO", "DUE SEMPRE"], "DUE VOLTE")],
         "3 · Scegli la parola giusta", "3 · Quante volte", "e3"),
  {"part": "Mi piace"},
  menu(["MI PIACE", "MI PIACCIONO"],
       [("1. ___ IL CALCIO.", "MI PIACE"), ("2. ___ I FILM COMICI.", "MI PIACCIONO"), ("3. ___ CUCINARE.", "MI PIACE"),
        ("4. ___ LE CANZONI ARABE.", "MI PIACCIONO"), ("5. ___ LA PIZZA.", "MI PIACE")], "4 · Piace o piacciono?", "4 · Mi piace", "e4"),
  completa("AMINA: CHE COSA FAI ___?<br>GRACE: DI ___ IL SABATO PULISCO LA CASA.<br>AMINA: TI ___ DI ANDARE AL CINEMA?<br>"
           "GRACE: SÌ, ___! CI VEDIAMO ALLE 8?<br>AMINA: VA ___. A SABATO!",
           ["sabato", "solito", "va", "volentieri", "bene"], "5 · Completa il dialogo", "5 · Il dialogo", "e5", "SABATO · SOLITO · VA · VOLENTIERI · BENE"),
  libero("e6", 6, "Il mio tempo libero", "SCRIVI 4 FRASI: CHE COSA FAI NEL TEMPO LIBERO E QUANTE VOLTE? USA SEMPRE, SPESSO, QUALCHE VOLTA, MAI.", ["IL MIO TEMPO LIBERO"], rows=4),
  parla("e7", 7, "INVITA UN AMICO A FARE UNA COSA INSIEME IL FINE SETTIMANA. DI' CHE COSA, DOVE E A CHE ORA."),
 ]
}

# =====================================================================
# 2. AL RISTORANTE (A1)
# =====================================================================
MENU_TAB = table([
    ["ANTIPASTI", "BRUSCHETTA AL POMODORO", "4 €"], ["", "POLPO CRUDO E COZZE", "10 €"],
    ["PRIMI", "ORECCHIETTE ALLE CIME DI RAPA", "9 €"], ["", "SPAGHETTI ALLE VONGOLE", "12 €"],
    ["SECONDI", "ORATA AL FORNO CON PATATE", "14 €"], ["", "BRACIOLE AL SUGO", "12 €"],
    ["CONTORNI", "INSALATA MISTA · PATATE FRITTE", "4 €"], ["DOLCI", "TIRAMISÙ · FRUTTA", "5 €"],
    ["BEVANDE", "ACQUA (1 L) · VINO DELLA CASA (1/4)", "2 € · 4 €"]], head=["", "MENÙ DEL GIORNO", "PREZZO"])

RIST_SLIDE = [
    cover("🍝", "AL RISTORANTE", "PRENOTARE, ORDINARE, PAGARE", "CIBO &bull; A1"),
    slide("CHE COSA IMPARIAMO?", cards([
        ("📞", "PRENOTARE", "UN TAVOLO PER 4, ALLE 8"), ("📋", "IL MENÙ", "ANTIPASTO, PRIMO, SECONDO…"),
        ("🗣️", "ORDINARE", "PER ME… IO PRENDO…"), ("🧾", "IL CONTO", "IL CONTO, PER FAVORE!")])),
    slide("📞 PRENOTO UN TAVOLO", dialogo([
        ("*CAMERIERE", "RISTORANTE «IL GOZZO», BUONASERA!"),
        ("OMAR", "BUONASERA. VORREI PRENOTARE UN TAVOLO PER SABATO SERA."),
        ("*CAMERIERE", "PER QUANTE PERSONE?"),
        ("OMAR", "PER QUATTRO, ALLE OTTO E MEZZA."),
        ("*CAMERIERE", "VA BENE. A CHE NOME?"),
        ("OMAR", "TOURÉ. T-O-U-R-E."),
        ("*CAMERIERE", "PERFETTO, SIGNOR TOURÉ. A SABATO!")])),
    slide("📋 IL MENÙ", MENU_TAB),
    slide("🍽️ I PIATTI DEL MENÙ", cards([
        (foto("polpo"), "IL POLPO", "ANTIPASTO"), (foto("orecchiette-cime-di-rapa"), "LE ORECCHIETTE", "PRIMO"),
        (foto("spaghetti"), "GLI SPAGHETTI", "PRIMO"), (foto("orata"), "L'ORATA AL FORNO", "SECONDO"),
        (foto("insalata"), "L'INSALATA", "CONTORNO"), (foto("fetta-torta"), "IL DOLCE", "UNA FETTA DI TORTA")], "g3")),
    slide("🍽️ COME SI MANGIA IN ITALIA?", cards([
        ("1️⃣", "L'ANTIPASTO", "PRIMA DI TUTTO, POCO"), ("2️⃣", "IL PRIMO", "PASTA, RISO, ZUPPA"),
        ("3️⃣", "IL SECONDO", "CARNE O PESCE"), ("🥗", "IL CONTORNO", "VERDURA, CON IL SECONDO"),
        ("🍰", "IL DOLCE", "ALLA FINE"), ("☕", "IL CAFFÈ", "DOPO IL DOLCE")], "g3") + "\n" +
        nota("NON È OBBLIGATORIO PRENDERE TUTTO! MOLTE PERSONE PRENDONO SOLO UN PRIMO O UN SECONDO.")),
    slide("🗣️ ORDINO", dialogo([
        ("*CAMERIERE", "AVETE SCELTO?"),
        ("FATIMA", "SÌ. PER ME LE ORECCHIETTE ALLE CIME DI RAPA."),
        ("OMAR", "IO PRENDO L'ORATA AL FORNO. C'È IL MAIALE NELLE ORECCHIETTE?"),
        ("*CAMERIERE", "NO, SOLO VERDURA, AGLIO E OLIO. E DA BERE?"),
        ("FATIMA", "UNA BOTTIGLIA D'ACQUA NATURALE, GRAZIE."),
        ("*CAMERIERE", "BENISSIMO.")])),
    slide("🧾 IL CONTO", dialogo([
        ("OMAR", "SCUSI! IL CONTO, PER FAVORE."),
        ("*CAMERIERE", "ECCO. SONO 27 EURO."),
        ("OMAR", "POSSO PAGARE CON LA CARTA?"),
        ("*CAMERIERE", "CERTO. ERA TUTTO BUONO?"),
        ("FATIMA", "BUONISSIMO, GRAZIE! ARRIVEDERCI.")]) + "\n" +
        nota("💶 IL <b>COPERTO</b> È UN PICCOLO PREZZO (1-3 €) PER IL PANE E LA TAVOLA. LA MANCIA NON È OBBLIGATORIA.")),
    slide("🗣️ LE FRASI UTILI", table([
        ["ENTRO", "AVETE UN TAVOLO PER DUE?"], ["CHIEDO", "CHE COSA C'È OGGI? · C'È CARNE DENTRO?"],
        ["ORDINO", "PER ME… · IO PRENDO… · VORREI…"], ["CHIEDO ANCORA", "UN ALTRO PO' DI PANE, PER FAVORE."],
        ["PAGO", "IL CONTO, PER FAVORE. · POSSO PAGARE CON LA CARTA?"]], head=["QUANDO", "FRASE"])),
    slide("📷 LE FOTO", crediti_slide(["polpo", "orecchiette-cime-di-rapa", "spaghetti", "orata", "insalata", "fetta-torta"])),
    end("ORA SAI ANDARE AL RISTORANTE!"),
]
RIST = {
 "title": "🍝 Al ristorante · Esercizi", "store": "ristorante", "upper": True,
 "sections": [
  {"part": "Il menù"},
  menu(["ANTIPASTO", "PRIMO", "SECONDO", "CONTORNO", "DOLCE"],
       [("1. SPAGHETTI ALLE VONGOLE", "PRIMO"), ("2. TIRAMISÙ", "DOLCE"), ("3. ORATA AL FORNO", "SECONDO"), ("4. BRUSCHETTA", "ANTIPASTO"),
        ("5. INSALATA MISTA", "CONTORNO"), ("6. ORECCHIETTE", "PRIMO"), ("7. BRACIOLE AL SUGO", "SECONDO")],
       "1 · Che piatto è?", "1 · Il menù", "e1"),
  scegli([("1. QUANTO COSTANO LE ORECCHIETTE?", ["9 €", "12 €", "4 €"], "9 €"),
          ("2. FATIMA NON MANGIA CARNE. CHE SECONDO PRENDE?", ["L'ORATA AL FORNO", "LE BRACIOLE AL SUGO", "IL TIRAMISÙ"], "L'ORATA AL FORNO"),
          ("3. OMAR PRENDE SPAGHETTI E ACQUA. QUANTO SPENDE?", ["14 €", "12 €", "16 €"], "14 €")],
         "2 · Leggi il menù", "2 · Leggi il menù", "e2", info=MENU_TAB.replace('table class="plur"', 'table class="plur" style="width:100%;font-size:14px"')),
  {"part": "Al ristorante"},
  ordina(["BUONASERA, AVETE UN TAVOLO PER DUE?", "AVETE SCELTO?", "PER ME LE ORECCHIETTE, GRAZIE.", "E DA BERE?",
          "UNA BOTTIGLIA D'ACQUA.", "IL CONTO, PER FAVORE."], "3 · Metti in ordine", "3 · In ordine", "e3"),
  menu(["IL CONTO, PER FAVORE.", "AVETE UN TAVOLO PER QUATTRO?", "C'È CARNE DENTRO?", "PER ME UN PRIMO.", "UN ALTRO PO' DI PANE, PER FAVORE."],
       [("1. ENTRI NEL RISTORANTE CON 3 AMICI.", "AVETE UN TAVOLO PER QUATTRO?"), ("2. NON MANGI CARNE E NON SAI CHE COSA C'È NEL PIATTO.", "C'È CARNE DENTRO?"),
        ("3. HAI FINITO E VUOI PAGARE.", "IL CONTO, PER FAVORE."), ("4. IL PANE È FINITO.", "UN ALTRO PO' DI PANE, PER FAVORE."),
        ("5. IL CAMERIERE CHIEDE: «CHE COSA PRENDE?»", "PER ME UN PRIMO.")], "4 · Che cosa dici?", "4 · Che cosa dici", "e4"),
  completa("CAMERIERE: BUONASERA! ___ SCELTO?<br>OMAR: SÌ. IO ___ L'ORATA AL FORNO.<br>CAMERIERE: E DA ___?<br>OMAR: ACQUA NATURALE.<br>"
           "…<br>OMAR: SCUSI, IL ___, PER FAVORE. POSSO PAGARE CON LA ___?",
           ["avete|ha", "prendo", "bere", "conto", "carta"], "5 · Completa il dialogo", "5 · Il dialogo", "e5", "AVETE · PRENDO · BERE · CONTO · CARTA"),
  parla("e6", 6, "TELEFONA AL RISTORANTE E PRENOTA UN TAVOLO: GIORNO, ORA, QUANTE PERSONE, IL TUO NOME."),
 ]
}

# =====================================================================
# 3. FESTE E TRADIZIONI (A1)
# =====================================================================
FESTE_SLIDE = [
    cover("🎉", "FESTE E TRADIZIONI", "LE FESTE IN ITALIA E NEL MIO PAESE", "TEMPO LIBERO &bull; A1"),
    slide("CHE COSA IMPARIAMO?", cards([
        ("📅", "LE FESTE", "QUANDO SONO?"), ("🎁", "GLI AUGURI", "BUON NATALE! BUON COMPLEANNO!"),
        ("🍰", "CHE COSA SI FA?", "SI MANGIA, SI BALLA, SI REGALA…"), ("🌍", "IL MIO PAESE", "LE FESTE DA NOI")])),
    slide("📅 LE FESTE IN ITALIA", table([
        ["1 GENNAIO", "CAPODANNO", "IL PRIMO GIORNO DELL'ANNO"], ["MARZO O APRILE", "PASQUA", "FESTA CRISTIANA, SI MANGIANO LE UOVA DI CIOCCOLATO"],
        ["25 APRILE", "FESTA DELLA LIBERAZIONE", "LA FINE DELLA GUERRA, 1945"], ["1 MAGGIO", "FESTA DEI LAVORATORI", ""],
        ["2 GIUGNO", "FESTA DELLA REPUBBLICA", "NASCE LA REPUBBLICA ITALIANA, 1946"], ["15 AGOSTO", "FERRAGOSTO", "TUTTI AL MARE!"],
        ["25 DICEMBRE", "NATALE", "FESTA CRISTIANA, SI FANNO I REGALI"]], head=["QUANDO?", "LA FESTA", "CHE COS'È?"]) + "\n" +
        nota("💙 A BARI IL <b>7-9 MAGGIO</b> E IL <b>6 DICEMBRE</b> C'È LA FESTA DI <b>SAN NICOLA</b>, IL SANTO PATRONO DELLA CITTÀ.")),
    slide("🌍 LE FESTE DI TUTTI", cards([
        ("🌙", "IL RAMADAN E L'EID AL-FITR", "UN MESE DI DIGIUNO E POI LA FESTA"), ("🐑", "L'EID AL-ADHA", "LA FESTA DEL SACRIFICIO"),
        ("🎄", "IL NATALE ORTODOSSO", "IL 7 GENNAIO"), ("🎂", "IL COMPLEANNO", "LA FESTA DI OGNI PERSONA")]) + "\n" +
        nota("IN ITALIA VIVONO PERSONE DI TANTE RELIGIONI E CULTURE: OGNUNO PUÒ FESTEGGIARE LE SUE FESTE.")),
    slide("🎁 GLI AUGURI", table([
        ["BUON NATALE!", "IL 25 DICEMBRE"], ["BUON ANNO! / FELICE ANNO NUOVO!", "IL 1 GENNAIO"], ["BUONA PASQUA!", "A PASQUA"],
        ["EID MUBARAK! / BUONA FESTA!", "ALL'EID"], ["BUON COMPLEANNO! / TANTI AUGURI!", "AL COMPLEANNO"], ["AUGURI!", "SEMPRE 😉"]],
        head=["CHE COSA DICO?", "QUANDO?"])),
    slide("🍰 CHE COSA SI FA?", cards([
        ("👨‍👩‍👧", "SI STA CON LA FAMIGLIA", ""), ("🍲", "SI MANGIA INSIEME", "I PIATTI DELLA FESTA"), ("🎁", "SI FANNO I REGALI", ""),
        ("💃", "SI BALLA, SI CANTA", ""), ("🎆", "SI GUARDANO I FUOCHI", "A CAPODANNO"), ("🕯️", "SI VA IN CHIESA / IN MOSCHEA", "")], "g3") + "\n" +
        nota("«<b>SI</b> MANGIA» = TUTTE LE PERSONE MANGIANO.")),
    slide("🗣️ COME FESTEGGI?", dialogo([
        ("GIULIA", "SAMIR, COME FESTEGGI L'EID NEL TUO PAESE?"),
        ("*SAMIR", "LA MATTINA ANDIAMO IN MOSCHEA. POI MANGIAMO INSIEME CON TUTTA LA FAMIGLIA."),
        ("GIULIA", "E CHE COSA MANGIATE?"),
        ("*SAMIR", "TANTI DOLCI! E I BAMBINI RICEVONO VESTITI NUOVI E UN PO' DI SOLDI."),
        ("GIULIA", "CHE BELLO! DA NOI A NATALE I BAMBINI RICEVONO I REGALI."),
        ("*SAMIR", "ALLORA… BUONE FESTE A TUTTI!")])),
    end("ORA SAI PARLARE DELLE FESTE!"),
]
FESTE = {
 "title": "🎉 Feste e tradizioni · Esercizi", "store": "feste", "upper": True,
 "sections": [
  {"part": "Le feste"},
  menu(["IL 25 DICEMBRE", "IL 1 GENNAIO", "IL 15 AGOSTO", "IL 2 GIUGNO", "IL 1 MAGGIO", "IL 25 APRILE"],
       [("1. NATALE", "IL 25 DICEMBRE"), ("2. CAPODANNO", "IL 1 GENNAIO"), ("3. FERRAGOSTO", "IL 15 AGOSTO"),
        ("4. LA FESTA DELLA REPUBBLICA", "IL 2 GIUGNO"), ("5. LA FESTA DEI LAVORATORI", "IL 1 MAGGIO"), ("6. LA FESTA DELLA LIBERAZIONE", "IL 25 APRILE")],
       "1 · Quando è?", "1 · Quando è", "e1"),
  {"part": "Gli auguri"},
  menu(["BUON NATALE!", "BUON COMPLEANNO!", "BUON ANNO!", "EID MUBARAK!", "BUONA PASQUA!"],
       [("1. È IL 25 DICEMBRE.", "BUON NATALE!"), ("2. LA TUA AMICA COMPIE 30 ANNI.", "BUON COMPLEANNO!"), ("3. È MEZZANOTTE DEL 31 DICEMBRE.", "BUON ANNO!"),
        ("4. È FINITO IL RAMADAN.", "EID MUBARAK!"), ("5. È LA DOMENICA DI PASQUA.", "BUONA PASQUA!")], "2 · Che cosa dici?", "2 · Gli auguri", "e2"),
  vf(["1. A FERRAGOSTO MOLTI ITALIANI VANNO AL MARE.", "2. SAN NICOLA È IL SANTO PATRONO DI BARI.", "3. IL 2 GIUGNO SI FESTEGGIA IL NATALE.",
      "4. IL NATALE ORTODOSSO È IL 7 GENNAIO.", "5. IL 1 MAGGIO È LA FESTA DEI BAMBINI."], ["VERO", "VERO", "FALSO", "VERO", "FALSO"],
     "3 · Vero o falso?", "3 · Vero o falso", "e3"),
  completa("GIULIA: SAMIR, COME ___ L'EID?<br>SAMIR: LA MATTINA ANDIAMO IN ___. POI MANGIAMO INSIEME CON TUTTA LA ___.<br>"
           "GIULIA: E I BAMBINI?<br>SAMIR: RICEVONO VESTITI ___ E UN PO' DI SOLDI.<br>GIULIA: CHE ___!",
           ["festeggi", "moschea", "famiglia", "nuovi", "bello"], "4 · Completa il dialogo", "4 · Il dialogo", "e4", "FESTEGGI · MOSCHEA · FAMIGLIA · NUOVI · BELLO"),
  libero("e5", 5, "La festa del mio paese", "SCRIVI 4 FRASI: COME SI CHIAMA LA FESTA? QUANDO È? CHE COSA SI FA? CHE COSA SI MANGIA?", ["LA MIA FESTA"], rows=4),
  parla("e6", 6, "RACCONTA LA TUA FESTA PREFERITA: QUANDO È, CON CHI FESTEGGI, CHE COSA FATE."),
 ]
}

# =====================================================================
# 4. IN VACANZA (A2) — stampatello minuscolo
# =====================================================================
VAC_SLIDE = [
    cover("🏖️", "Com'è andata la vacanza?", "Raccontare un viaggio al passato prossimo", "Tempo libero &bull; A2"),
    slide("Che cosa impariamo?", cards([
        ("🧳", "Il viaggio", "Dove sei andato? Con chi?"), ("⏪", "Il passato prossimo", "Sono andato, ho visitato"),
        ("🌦️", "Com'era?", "Bello, caldo, affollato…"), ("🗣️", "Raccontare", "Prima, poi, alla fine")])),
    slide("🧳 Le parole del viaggio", cards([
        ("🏨", "L'albergo / il B&B", "dove dormo"), ("🎒", "lo zaino / la valigia", ""), ("🚆", "il treno, il pullman, l'aereo", "come viaggio"),
        ("🗺️", "la gita", "un viaggio di un giorno"), ("📸", "le foto", "faccio le foto"), ("🏛️", "il museo, il centro storico", "che cosa visito")], "g3")),
    slide("⏪ Il passato prossimo", table([
        ["avere + -ato/-uto/-ito", "ho visitato · ho visto · ho dormito · ho mangiato"],
        ["essere + -ato/-uto/-ito", "sono andato/a · sono partito/a · sono tornato/a · sono stato/a"]], head=["come si fa", "esempi"]) + "\n" +
        nota("Con <b>essere</b> il participio cambia: Marco è andat<b>o</b>, Sara è andat<b>a</b>, noi siamo andat<b>i</b>.")),
    slide("📖 La vacanza di Lamine", '    <div class="nota" style="font-size:1.3rem;text-align:left">'
        "Ad agosto <b>sono andato</b> in Salento con due amici. <b>Siamo partiti</b> da Bari in treno e <b>abbiamo dormito</b> in un B&B vicino al mare. "
        "La mattina <b>abbiamo fatto</b> il bagno, il pomeriggio <b>abbiamo visitato</b> Lecce e Otranto. Una sera <b>siamo andati</b> a un concerto in piazza. "
        "Il cibo era buonissimo, ma faceva molto caldo! <b>Siamo tornati</b> dopo una settimana: stanchi ma felici.</div>"),
    slide("🗣️ Com'è andata?", dialogo([
        ("Sara", "Ciao Lamine! Com'è andata la vacanza?"),
        ("*Lamine", "Benissimo! Sono stato in Salento con due amici."),
        ("Sara", "Che bello! E che cosa avete fatto?"),
        ("*Lamine", "Siamo andati al mare ogni giorno e abbiamo visitato Lecce."),
        ("Sara", "Avete speso molto?"),
        ("*Lamine", "No, abbiamo dormito in un B&B economico e abbiamo mangiato spesso la pizza!")])),
    slide("🔗 Per raccontare", table([
        ["prima", "prima siamo andati a Lecce…"], ["poi / dopo", "poi abbiamo visitato Otranto…"],
        ["il primo giorno / l'ultimo giorno", "il primo giorno è piovuto"], ["alla fine", "alla fine siamo tornati a casa"]], head=["parola", "esempio"])),
    end("Ora sai raccontare una vacanza!"),
]
VAC = {
 "title": "🏖️ Com'è andata la vacanza? · Esercizi", "store": "in-vacanza",
 "sections": [
  {"part": "Il passato prossimo"},
  menu(["ho", "sono"], [("1. ___ visitato il museo.", "ho"), ("2. ___ andata al mare.", "sono"), ("3. ___ dormito in albergo.", "ho"),
                        ("4. ___ partito alle sei.", "sono"), ("5. ___ fatto tante foto.", "ho"), ("6. ___ tornata domenica.", "sono")],
       "1 · Essere o avere?", "1 · Essere o avere", "e1", cons="Scegli l'ausiliare giusto."),
  scrivi([("1. Ieri io (visitare) ___ Matera.", ["ho visitato"]), ("2. Sara (partire) ___ in aereo.", ["e partita"]),
          ("3. Noi (mangiare) ___ il pesce.", ["abbiamo mangiato"]), ("4. I ragazzi (andare) ___ al concerto.", ["sono andati"]),
          ("5. Tu (fare) ___ il bagno?", ["hai fatto"]), ("6. Lamine (stare) ___ in Salento.", ["e stato"])],
         "2 · Scrivi il passato prossimo", "2 · Il passato", "e2", cons="Scrivi il verbo al passato prossimo (ausiliare + participio).", w="m"),
  {"part": "La vacanza di Lamine"},
  vf(["1. Lamine è andato in vacanza da solo.", "2. Sono partiti in treno.", "3. Hanno dormito in un B&B.",
      "4. Hanno visitato Lecce e Otranto.", "5. Faceva freddo.", "6. Sono stati via un mese."],
     ["FALSO", "VERO", "VERO", "VERO", "FALSO", "FALSO"], "3 · Vero o falso?", "3 · Vero o falso", "e3",
     info="Ad agosto sono andato in Salento con due amici. Siamo partiti da Bari in treno e abbiamo dormito in un B&B vicino al mare. "
          "La mattina abbiamo fatto il bagno, il pomeriggio abbiamo visitato Lecce e Otranto. Una sera siamo andati a un concerto in piazza. "
          "Il cibo era buonissimo, ma faceva molto caldo! Siamo tornati dopo una settimana: stanchi ma felici."),
  ordina(["Prima abbiamo prenotato il B&B su internet.", "Poi siamo partiti da Bari in treno.", "Il primo giorno siamo andati al mare.",
          "Dopo abbiamo visitato Lecce.", "Alla fine siamo tornati a casa stanchi ma felici."],
         "4 · Metti in ordine il racconto", "4 · In ordine", "e4", cons="Metti in ordine: 1, 2, 3…"),
  libero("e5", 5, "La mia vacanza", "Racconta una vacanza o una gita (6-8 frasi): dove sei andato, con chi, che cosa avete fatto, com'era. Usa prima, poi, alla fine.",
         ["La mia vacanza"], rows=6),
  parla("e6", 6, "Racconta il viaggio più bello della tua vita: dove, quando, con chi, che cosa è successo."),
 ]
}

SLIDE_LIBRI = [
    ("tempo-libero/index.html", "IL TEMPO LIBERO", "TEMPO LIBERO", TEMPO_SLIDE, ILL_CSS),
    ("ristorante/index.html", "AL RISTORANTE", "CIBO", RIST_SLIDE, ILL_CSS + FOTO_CSS),
    ("feste/index.html", "FESTE E TRADIZIONI", "TEMPO LIBERO", FESTE_SLIDE, ILL_CSS),
    ("in-vacanza/index.html", "Com'è andata la vacanza?", "Tempo libero", VAC_SLIDE, ILL_CSS + "\n  body, .btn, button{text-transform:none !important;}  /* A2: stampatello minuscolo */"),
]
ESERCIZI_LIBRI = [("tempo-libero", TEMPO), ("ristorante", RIST), ("feste", FESTE), ("in-vacanza", VAC)]
