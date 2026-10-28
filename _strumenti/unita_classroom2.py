"""Esercizi nuovi sugli argomenti dei lavori del corso Classroom (giochi Wordwall, Kahoot,
Quizizz, Language Guide…): non sono copie dei giochi, sono esercizi scritti per il sito."""
import random
from genera import eq, has, all_

def anagramma(w, seed):
    r = random.Random(seed)
    while True:
        l = list(w); r.shuffle(l)
        if "".join(l) != w:
            return " - ".join(l)

CUCINA = {
 "title": "🍝 Il cibo e la cucina · Esercizi",
 "store": "parole-cucina",
 "upper": True,
 "sections": [
  {"part": "I VERBI DELLA CUCINA"},
  {"id": "e1", "title": "1 · CHE COSA FAI? SCEGLI IL VERBO", "short": "1 · I verbi", "type": "select",
   "opts": ["BOLLIRE", "FRIGGERE", "GRATTUGIARE", "INFORNARE", "LAVARE", "MESCOLARE", "PELARE", "TAGLIARE", "VERSARE"],
   "items": [{"q": q} for q in ["1. 🔪 LA CIPOLLA A PEZZETTI", "2. 🥔 TOLGO LA BUCCIA ALLA PATATA", "3. 🧀 IL FORMAGGIO SULLA PASTA",
                                 "4. 💧 L'ACQUA A 100 GRADI", "5. 🍟 LE PATATINE NELL'OLIO CALDO", "6. 🥄 GIRO IL SUGO CON IL CUCCHIAIO",
                                 "7. 🍅 I POMODORI SOTTO L'ACQUA", "8. 🍕 LA PIZZA NEL FORNO", "9. 🥛 IL LATTE NEL BICCHIERE"]],
   "k": [eq(a) for a in ["TAGLIARE", "PELARE", "GRATTUGIARE", "BOLLIRE", "FRIGGERE", "MESCOLARE", "LAVARE", "INFORNARE", "VERSARE"]]},
  {"id": "e2", "title": "2 · LA PASTA AL POMODORO: COMPLETA", "short": "2 · La ricetta", "type": "cloze",
   "bank": "ACCENDO · AGGIUNGO · ASSAGGIO · BOLLE · LAVO · MESCOLO · TAGLIO",
   "parts": ["PRIMA ", {}, " I POMODORI E LI ", {}, " A PEZZETTI. ", {}, " IL FUOCO E METTO L'ACQUA NELLA PENTOLA. "
             "QUANDO L'ACQUA ", {}, ", BUTTO LA PASTA. NELLA PADELLA CUOCIO I POMODORI E ", {}, " UN PO' DI SALE. ",
             {}, " IL SUGO CON IL CUCCHIAIO. ALLA FINE ", {}, ": È BUONISSIMA!"],
   "k": [eq("lavo"), eq("taglio"), eq("accendo"), eq("bolle"), eq("aggiungo"), eq("mescolo"), eq("assaggio")]},
  {"id": "e3", "title": "3 · IL VERBO GIUSTO", "short": "3 · Collega", "type": "choice", "full": True,
   "items": [{"q": "1. … LA PASTA IN ACQUA CHE BOLLE", "opts": ["CUOCERE", "GRATTUGIARE"]},
             {"q": "2. … LE UOVA CON LA FORCHETTA", "opts": ["SBATTERE", "PELARE"]},
             {"q": "3. … LA TORTA NEL FORNO", "opts": ["FRIGGERE", "INFORNARE"]},
             {"q": "4. … IL PANE A FETTE", "opts": ["TAGLIARE", "VERSARE"]},
             {"q": "5. … L'OLIO NELLA PADELLA", "opts": ["VERSARE", "LAVARE"]},
             {"q": "6. … LA CAROTA (TOGLIERE LA BUCCIA)", "opts": ["MESCOLARE", "PELARE"]}],
   "k": [eq("CUOCERE"), eq("SBATTERE"), eq("INFORNARE"), eq("TAGLIARE"), eq("VERSARE"), eq("PELARE")]},

  {"part": "FRUTTA, VERDURA E BEVANDE"},
  {"id": "e4", "title": "4 · LA FRUTTA: SCRIVI IL NOME", "short": "4 · La frutta", "type": "text",
   "bank": "ANGURIA · ARANCIA · BANANA · FRAGOLA · LIMONE · MELA · PERA · PESCA · UVA",
   "items": [{"q": q} for q in ["1. 🍎", "2. 🍌", "3. 🍊", "4. 🍐", "5. 🍇", "6. 🍓", "7. 🍋", "8. 🍉", "9. 🍑"]],
   "k": [has(a) for a in ["mela", "banana", "arancia", "pera", "uva", "fragol", "limon", "anguria", "pesca"]]},
  {"id": "e5", "title": "5 · LA VERDURA: SCRIVI IL NOME", "short": "5 · La verdura", "type": "text",
   "bank": "AGLIO · BROCCOLI · CAROTA · CETRIOLO · CIPOLLA · INSALATA · MELANZANA · PATATA · PEPERONE · POMODORO",
   "items": [{"q": q} for q in ["1. 🥕", "2. 🍅", "3. 🥔", "4. 🧅", "5. 🍆", "6. 🥒", "7. 🥬", "8. 🫑", "9. 🧄", "10. 🥦"]],
   "k": [has("carot"), has("pomodor"), has("patat"), has("cipoll"), has("melanzan"), has("cetriol"),
         has("insalata", "lattuga"), has("peperon"), has("aglio"), has("broccol")]},
  {"id": "e6", "title": "6 · LE BEVANDE: SCEGLI", "short": "6 · Le bevande", "type": "select",
   "opts": ["ACQUA", "BIRRA", "CAFFÈ", "LATTE", "SPREMUTA D'ARANCIA", "TÈ", "VINO"],
   "items": [{"q": q} for q in ["1. 💧", "2. ☕", "3. 🍵", "4. 🥛", "5. 🍷", "6. 🍺", "7. 🍊 + 🥤"]],
   "k": [eq(a) for a in ["ACQUA", "CAFFÈ", "TÈ", "LATTE", "VINO", "BIRRA", "SPREMUTA D'ARANCIA"]]},
  {"id": "e7", "title": "7 · FRUTTA, VERDURA O BEVANDA?", "short": "7 · Che cos'è", "type": "choice",
   "opts": ["FRUTTA", "VERDURA", "BEVANDA"], "full": True,
   "items": [{"q": q} for q in ["1. LA ZUCCHINA", "2. IL SUCCO DI MELA", "3. L'ALBICOCCA", "4. IL CAVOLFIORE",
                                 "5. LA CILIEGIA", "6. L'ACQUA FRIZZANTE", "7. GLI SPINACI", "8. IL KIWI"]],
   "k": [eq(a) for a in ["VERDURA", "BEVANDA", "FRUTTA", "VERDURA", "FRUTTA", "BEVANDA", "VERDURA", "FRUTTA"]]},
  {"id": "e8", "title": "8 ✎ · UNA RICETTA DEL TUO PAESE", "type": "free", "rows": 6,
   "items": ["SCRIVI UNA RICETTA CHE TI PIACE. CHE COSA SERVE? CHE COSA FAI? USA I VERBI: LAVO, TAGLIO, CUOCIO, MESCOLO…"]},
 ]
}

CASA = {
 "title": "🏠 Le stanze e gli oggetti della casa · Esercizi",
 "store": "parole-casa",
 "upper": True,
 "sections": [
  {"part": "LE STANZE"},
  {"id": "e1", "title": "1 · IN QUALE STANZA È?", "short": "1 · Le stanze", "type": "select",
   "opts": ["BAGNO", "CAMERA DA LETTO", "CUCINA", "GIARDINO", "RIPOSTIGLIO", "SALA DA PRANZO", "SOGGIORNO"],
   "items": [{"q": q} for q in ["1. 🛏️ IL LETTO", "2. 🚿 LA DOCCIA", "3. 🧊 IL FRIGORIFERO", "4. 🛋️ IL DIVANO",
                                 "5. 🧹 LA SCOPA E IL SECCHIO", "6. 🌷 I FIORI E L'ERBA", "7. 🪥 LO SPAZZOLINO",
                                 "8. 🍽️ IL TAVOLO GRANDE PER MANGIARE CON GLI OSPITI", "9. 👔 L'ARMADIO CON I VESTITI", "10. 🍳 IL FORNELLO",
                                 "11. 📺 LA TELEVISIONE", "12. 🛁 LA VASCA"]],
   "k": [eq(a) for a in ["CAMERA DA LETTO", "BAGNO", "CUCINA", "SOGGIORNO", "RIPOSTIGLIO", "GIARDINO", "BAGNO",
                         "SALA DA PRANZO", "CAMERA DA LETTO", "CUCINA", "SOGGIORNO", "BAGNO"]]},
  {"part": "GLI OGGETTI"},
  {"id": "e2", "title": "2 · SCRIVI IL NOME DELL'OGGETTO", "short": "2 · Gli oggetti", "type": "text",
   "bank": "DIVANO · FINESTRA · LAMPADA · LETTO · PORTA · SEDIA · SPECCHIO · VASCA · WATER",
   "items": [{"q": q} for q in ["1. 🛏️", "2. 🛋️", "3. 🪑", "4. 🚪", "5. 🪟", "6. 🛁", "7. 🚽", "8. 🪞", "9. 💡"]],
   "k": [has(a) for a in ["letto", "divano", "sedia", "porta", "finestra", "vasca", "water", "specchio", "lampad"]]},
  {"id": "e3", "title": "3 · CHE COS'È?", "short": "3 · Che cos'è", "type": "choice", "full": True,
   "items": [{"q": "1. SERVE PER DORMIRE.", "opts": ["IL LETTO", "LA SEDIA", "IL FORNO"]},
             {"q": "2. CI METTO IL CIBO PER TENERLO FREDDO.", "opts": ["L'ARMADIO", "IL FRIGORIFERO", "LA LAVATRICE"]},
             {"q": "3. LAVA I VESTITI.", "opts": ["LA LAVASTOVIGLIE", "LA LAVATRICE", "IL LAVANDINO"]},
             {"q": "4. LAVA I PIATTI.", "opts": ["LA LAVASTOVIGLIE", "LA DOCCIA", "IL DIVANO"]},
             {"q": "5. MI GUARDO E MI PETTINO.", "opts": ["LA FINESTRA", "LO SPECCHIO", "IL QUADRO"]},
             {"q": "6. CI METTO I VESTITI.", "opts": ["L'ARMADIO", "IL FORNO", "LA VASCA"]},
             {"q": "7. MI ASCIUGO DOPO LA DOCCIA.", "opts": ["IL CUSCINO", "L'ASCIUGAMANO", "IL TAPPETO"]},
             {"q": "8. CI APPOGGIO LA TESTA QUANDO DORMO.", "opts": ["IL CUSCINO", "IL TAVOLO", "LA SCOPA"]}],
   "k": [eq("IL LETTO"), eq("IL FRIGORIFERO"), eq("LA LAVATRICE"), eq("LA LAVASTOVIGLIE"), eq("LO SPECCHIO"),
         eq("L'ARMADIO"), eq("L'ASCIUGAMANO"), eq("IL CUSCINO")]},
  {"id": "e4", "title": "4 · L'ARTICOLO GIUSTO", "short": "4 · Gli articoli", "type": "select",
   "opts": ["IL", "LO", "LA", "L'", "I", "GLI", "LE"],
   "items": [{"q": q} for q in ["1. … ARMADIO", "2. … SPECCHIO", "3. … CUSCINI", "4. … SEDIE", "5. … ASCIUGAMANI",
                                 "6. … LAVATRICE", "7. … TAVOLO", "8. … SCAFFALI", "9. … SPAZZOLINO"]],
   "k": [eq(a) for a in ["L'", "LO", "I", "LE", "GLI", "LA", "IL", "GLI", "LO"]]},
  {"id": "e5", "title": "5 · TROVA L'INTRUSO", "short": "5 · L'intruso", "type": "choice", "full": True,
   "cons": "QUALE OGGETTO NON È IN QUELLA STANZA?",
   "items": [{"q": "1. CUCINA", "opts": ["IL FORNO", "IL FRIGORIFERO", "IL LETTO"]},
             {"q": "2. BAGNO", "opts": ["IL DIVANO", "LA DOCCIA", "IL WATER"]},
             {"q": "3. CAMERA DA LETTO", "opts": ["IL COMODINO", "IL LAVANDINO DEI PIATTI", "L'ARMADIO"]},
             {"q": "4. SOGGIORNO", "opts": ["LA POLTRONA", "LA TELEVISIONE", "LA VASCA"]}],
   "k": [eq("IL LETTO"), eq("IL DIVANO"), eq("IL LAVANDINO DEI PIATTI"), eq("LA VASCA")]},
  {"id": "e6", "title": "6 ✎ · LA MIA CASA", "type": "free", "rows": 5,
   "items": ["DESCRIVI LA TUA CASA: QUANTE STANZE CI SONO? CHE COSA C'È IN CUCINA? E IN CAMERA DA LETTO?"]},
 ]
}

VESTITI_AN = ["GONNA", "CAMICIA", "SCIARPA", "SCARPE", "GIACCA", "CALZINI", "CAPPELLO", "MAGLIETTA"]

VESTITI = {
 "title": "👕 I vestiti: le parole · Esercizi",
 "store": "parole-vestiti",
 "upper": True,
 "sections": [
  {"part": "LE PAROLE DEI VESTITI"},
  {"id": "e1", "title": "1 · SCRIVI IL NOME", "short": "1 · I nomi", "type": "text",
   "bank": "BORSA · CALZINI · CAPPELLO · CAPPOTTO · GUANTI · JEANS · MAGLIETTA · SCARPE · SCIARPA · STIVALI · VESTITO",
   "items": [{"q": q} for q in ["1. 👗", "2. 👖", "3. 👕", "4. 🧥", "5. 🧣", "6. 🧤", "7. 🧦", "8. 👟", "9. 🧢", "10. 👜", "11. 🥾"]],
   "k": [has("vestit", "abito"), has("jeans", "pantalon"), has("magliett", "t-shirt"), has("cappott", "giacc", "giubbott"),
         has("sciarp"), has("guant"), has("calzin", "calze"), has("scarp"), has("cappell", "berrett"), has("borsa"), has("stival")]},
  {"id": "e2", "title": "2 · ANAGRAMMI: METTI IN ORDINE LE LETTERE", "short": "2 · Anagrammi", "type": "text",
   "items": [{"q": f"{i + 1}. {anagramma(w, i)}"} for i, w in enumerate(VESTITI_AN)],
   "k": [eq(w.lower()) for w in VESTITI_AN]},
  {"id": "e3", "title": "3 · DONNA, UOMO O TUTTI E DUE?", "short": "3 · Donna o uomo", "type": "choice",
   "opts": ["DONNA", "UOMO", "TUTTI E DUE"], "full": True,
   "cons": "DI SOLITO, IN ITALIA, CHI LO PORTA?",
   "items": [{"q": q} for q in ["1. LA GONNA", "2. LA CRAVATTA", "3. I JEANS", "4. IL REGGISENO", "5. LA MAGLIETTA", "6. LE SCARPE COL TACCO"]],
   "k": [eq("DONNA"), eq("UOMO"), eq("TUTTI E DUE"), eq("DONNA"), eq("TUTTI E DUE"), eq("DONNA")]},
  {"id": "e4", "title": "4 · I VESTITI PER L'INVERNO", "short": "4 · L'inverno", "type": "multi",
   "cons": "METTI LA SPUNTA VICINO AI 5 VESTITI PER QUANDO FA FREDDO.",
   "items": ["IL CAPPOTTO", "IL COSTUME DA BAGNO", "LA SCIARPA", "I SANDALI", "I GUANTI", "IL MAGLIONE", "I PANTALONCINI", "GLI STIVALI"],
   "k": [eq(a) for a in ["X", "-", "X", "-", "X", "X", "-", "X"]]},
  {"part": "VESTITI E COLORI"},
  {"id": "e5", "title": "5 · DI CHE COLORE È?", "short": "5 · I colori", "type": "text",
   "cons": "ATTENZIONE: IL COLORE CAMBIA CON IL NOME (MASCHILE, FEMMINILE, PLURALE).",
   "items": [{"q": q} for q in ["1. 🟥 LA MAGLIETTA È …", "2. 🟨 LA GONNA È …", "3. ⬛ LE SCARPE SONO …", "4. ⬜ LA CAMICIA È …",
                                 "5. 🟩 IL CAPPELLO È …", "6. 🟥 I CALZINI SONO …", "7. ⬛ IL CAPPOTTO È …", "8. ⬜ I PANTALONI SONO …"]],
   "k": [eq(a) for a in ["rossa", "gialla", "nere", "bianca", "verde", "rossi", "nero", "bianchi"]]},
  {"id": "e6", "title": "6 ✎ · CHE COSA METTI?", "type": "free", "rows": 4,
   "items": ["CHE COSA METTI PER ANDARE A SCUOLA? E QUANDO FA FREDDO? SCRIVI 3 FRASI. ESEMPIO: METTO I JEANS BLU E…"]},
 ]
}

PRIMI = {
 "title": "🎨 Colori, numeri, emozioni · Esercizi",
 "store": "parole-primi",
 "upper": True,
 "sections": [
  {"part": "I COLORI"},
  {"id": "e1", "title": "1 · DI CHE COLORE È?", "short": "1 · I colori", "type": "select",
   "opts": ["ARANCIONE", "BIANCO", "BLU", "GIALLO", "GRIGIO", "MARRONE", "NERO", "ROSA", "ROSSO", "VERDE", "VIOLA"],
   "items": [{"q": q} for q in ["1. 🍅", "2. 🍌", "3. 🌿", "4. 🌊", "5. 🍊", "6. 🐘", "7. 🍫", "8. 🌸", "9. 🍆", "10. ⛄", "11. 🎱"]],
   "k": [eq("ROSSO"), eq("GIALLO"), eq("VERDE"), eq("BLU"), eq("ARANCIONE"), eq("GRIGIO"), eq("MARRONE"),
         eq("ROSA"), eq("VIOLA"), eq("BIANCO"), eq("NERO")]},
  {"part": "I NUMERI"},
  {"id": "e2", "title": "2 · SCRIVI IL NUMERO CON LE PAROLE", "short": "2 · Numero → parola", "type": "text",
   "items": [{"q": q} for q in ["1. 3", "2. 7", "3. 11", "4. 14", "5. 16", "6. 20", "7. 21", "8. 28", "9. 45", "10. 100"]],
   "k": [eq("tre"), eq("sette"), eq("undici"), eq("quattordici"), eq("sedici"), eq("venti"), eq("ventuno"),
         eq("ventotto"), eq("quarantacinque"), eq("cento")]},
  {"id": "e3", "title": "3 · SCRIVI IL NUMERO CON LE CIFRE", "short": "3 · Parola → numero", "type": "text",
   "items": [{"q": q} for q in ["1. NOVE", "2. DODICI", "3. DICIANNOVE", "4. TRENTA", "5. TRENTATRÉ", "6. CINQUANTA",
                                 "7. SESSANTOTTO", "8. NOVANTANOVE"]],
   "k": [eq(a) for a in ["9", "12", "19", "30", "33", "50", "68", "99"]]},
  {"part": "LE EMOZIONI"},
  {"id": "e4", "title": "4 · COME SI SENTE?", "short": "4 · Le emozioni", "type": "select",
   "opts": ["ANNOIATO", "ARRABBIATO", "FELICE", "INNAMORATO", "PREOCCUPATO", "SORPRESO", "SPAVENTATO", "STANCO", "TRISTE"],
   "items": [{"q": q} for q in ["1. 😀", "2. 😢", "3. 😠", "4. 😴", "5. 😱", "6. 😲", "7. 🥱", "8. 😍", "9. 😟"]],
   "k": [eq(a) for a in ["FELICE", "TRISTE", "ARRABBIATO", "STANCO", "SPAVENTATO", "SORPRESO", "ANNOIATO", "INNAMORATO", "PREOCCUPATO"]]},
  {"id": "e5", "title": "5 · COME TI SENTI?", "short": "5 · Le situazioni", "type": "choice", "full": True,
   "items": [{"q": "1. HAI LAVORATO 10 ORE.", "opts": ["SONO STANCO", "SONO INNAMORATO"]},
             {"q": "2. HAI TROVATO UN BUON LAVORO.", "opts": ["SONO TRISTE", "SONO FELICE"]},
             {"q": "3. IL TUO AMICO NON È VENUTO ALL'APPUNTAMENTO.", "opts": ["SONO ARRABBIATO", "SONO SORPRESO"]},
             {"q": "4. DOMANI HAI L'ESAME DI ITALIANO.", "opts": ["SONO PREOCCUPATO", "SONO ANNOIATO"]},
             {"q": "5. LA TUA FAMIGLIA È LONTANA.", "opts": ["SONO FELICE", "SONO TRISTE"]}],
   "k": [eq("SONO STANCO"), eq("SONO FELICE"), eq("SONO ARRABBIATO"), eq("SONO PREOCCUPATO"), eq("SONO TRISTE")]},
  {"id": "e6", "title": "6 ✎ · E TU, COME STAI OGGI?", "type": "free", "rows": 3,
   "items": ["SCRIVI 2 FRASI. ESEMPIO: OGGI SONO FELICE PERCHÉ…"]},
 ]
}

CULTURA = {
 "title": "🇮🇹 Test di lingua e cultura · Quiz",
 "store": "quiz-cultura",
 "sections": [
  {"part": "Livello A1 · A2"},
  {"id": "e1", "title": "1 · L'Italia", "short": "1 · L'Italia", "type": "choice", "full": True,
   "items": [{"q": "1. Qual è la capitale d'Italia?", "opts": ["Milano", "Roma", "Napoli"]},
             {"q": "2. Di che colori è la bandiera italiana?", "opts": ["verde, bianco e rosso", "blu, bianco e rosso", "giallo e rosso"]},
             {"q": "3. In quale regione si trova Bari?", "opts": ["Sicilia", "Calabria", "Puglia"]},
             {"q": "4. Chi è il santo patrono di Bari?", "opts": ["San Nicola", "San Gennaro", "San Marco"]},
             {"q": "5. Qual è un piatto tipico di Bari?", "opts": ["le orecchiette con le cime di rapa", "il risotto alla milanese", "la pizza alla napoletana"]},
             {"q": "6. Quale moneta usiamo in Italia?", "opts": ["la lira", "l'euro", "il dollaro"]},
             {"q": "7. Il 2 giugno in Italia è…", "opts": ["la Festa della Repubblica", "Natale", "Capodanno"]},
             {"q": "8. Qual è il numero unico per le emergenze?", "opts": ["112", "100", "911"]}],
   "k": [eq("Roma"), eq("verde, bianco e rosso"), eq("Puglia"), eq("San Nicola"), eq("le orecchiette con le cime di rapa"),
         eq("l'euro"), eq("la Festa della Repubblica"), eq("112")]},
  {"id": "e2", "title": "2 · La lingua di tutti i giorni", "short": "2 · La lingua", "type": "choice", "full": True,
   "items": [{"q": "1. Arrivi dal medico alle 18. Dici:", "opts": ["Buongiorno", "Buonasera", "Buonanotte"]},
             {"q": "2. Con il medico usi:", "opts": ["il «tu»", "il «Lei»"]},
             {"q": "3. Al bar chiedi il caffè. Dici:", "opts": ["Un caffè, per favore.", "Dammi un caffè!", "Caffè!"]},
             {"q": "4. Vuoi sapere il prezzo. Chiedi:", "opts": ["Quanto costa?", "Quanti anni ha?", "Che ore sono?"]},
             {"q": "5. Per lavorare in Italia serve il…", "opts": ["codice fiscale", "codice postale", "codice della strada"]},
             {"q": "6. «Mi scusi, dov'è la stazione?» è una domanda…", "opts": ["formale", "informale"]}],
   "k": [eq("Buonasera"), eq("il «Lei»"), eq("Un caffè, per favore."), eq("Quanto costa?"), eq("codice fiscale"), eq("formale")]},
 ]
}

MISTO = {
 "title": "🧩 Test misto di grammatica · Quiz",
 "store": "quiz-misto",
 "upper": True,
 "sections": [
  {"part": "LIVELLO A1"},
  {"id": "e1", "title": "1 · ESSERE O AVERE?", "short": "1 · Essere o avere", "type": "select",
   "opts": ["SONO", "SEI", "È", "SIAMO", "SIETE", "HO", "HAI", "HA", "ABBIAMO", "HANNO"],
   "items": [{"q": q} for q in ["1. IO … 25 ANNI.", "2. MARCO … MAROCCHINO.", "3. NOI … DUE FIGLI.", "4. TU … STANCO?",
                                 "5. LORO … FAME.", "6. VOI … DI BARI?", "7. LEI … UNA SORELLA.", "8. NOI … IN CLASSE."]],
   "k": [eq("HO"), eq("È"), eq("ABBIAMO"), eq("SEI"), eq("HANNO"), eq("SIETE"), eq("HA"), eq("SIAMO")]},
  {"id": "e2", "title": "2 · I VERBI IRREGOLARI", "short": "2 · Irregolari", "type": "text",
   "items": [{"q": q} for q in ["1. IO (ANDARE) … A SCUOLA.", "2. TU (FARE) … LA SPESA?", "3. LUI (VENIRE) … DOMANI.",
                                 "4. NOI (DIRE) … LA VERITÀ.", "5. LORO (USCIRE) … ALLE 8.", "6. IO (STARE) … BENE.",
                                 "7. VOI (BERE) … IL CAFFÈ?", "8. LEI (DARE) … IL LIBRO A MARIA."]],
   "k": [eq(a) for a in ["vado", "fai", "viene", "diciamo", "escono", "sto", "bevete", "dà"]] },
  {"id": "e3", "title": "3 · L'ARTICOLO E IL PLURALE", "short": "3 · Articoli e plurale", "type": "text",
   "cons": "SCRIVI IL PLURALE CON L'ARTICOLO. ESEMPIO: IL LIBRO → I LIBRI",
   "items": [{"q": q} for q in ["1. LA CASA →", "2. LO ZAINO →", "3. L'AMICO →", "4. L'AMICA →", "5. IL TELEFONO →", "6. LA CHIAVE →"]],
   "k": [eq(a) for a in ["le case", "gli zaini", "gli amici", "le amiche", "i telefoni", "le chiavi"]]},
  {"id": "e4", "title": "4 · LE PREPOSIZIONI", "short": "4 · Preposizioni", "type": "select",
   "opts": ["A", "DA", "DI", "IN", "CON", "PER", "AL", "DAL"],
   "items": [{"q": q} for q in ["1. ABITO … BARI.", "2. VADO … ITALIA.", "3. TORNO … SCUOLA ALLE 14.",
                                 "4. VADO … MEDICO.", "5. STUDIO ITALIANO … I MIEI AMICI.", "6. QUESTO REGALO È … TE.",
                                 "7. IL LIBRO … MARCO È SUL TAVOLO.", "8. VADO … LAVORO ALLE 7."]],
   "k": [eq("A"), eq("IN"), eq("DA"), eq("DAL"), eq("CON"), eq("PER"), eq("DI"), eq("AL", "A")]},
 ]
}

# emoji da sole più grandi
import re as _re
for _p in (CUCINA, CASA, VESTITI, PRIMI):
    for _s in _p["sections"]:
        for _it in _s.get("items", []):
            if isinstance(_it, dict):
                _m = _re.match(r"^(\d+\.) ([^\w\s]+(?: \+ [^\w\s]+)?)$", _it["q"])
                if _m:
                    _it["q"] = f'{_m.group(1)} <span style="font-size:34px;vertical-align:middle">{_m.group(2)}</span>'
