"""Mangiare sano: esercizi nati dalle schede di educazione alimentare mandate da Erila (2026-10-29).
Le schede erano per bambini: qui i temi sono gli stessi, ma testi ed esercizi sono scritti per il sito,
per adulti che imparano l'italiano. A1 in STAMPATELLO MAIUSCOLO, A2 con letture brevi.
Non ripetono i nomi di frutta e verdura già in parole/cucina.html."""
from genera import eq, has

STAGIONI = ["PRIMAVERA", "ESTATE", "AUTUNNO", "INVERNO"]

A1 = {
 "title": "🥦 Mangiare sano · Esercizi A1",
 "store": "mangiare-sano-a1",
 "upper": True,
 "sections": [
  {"part": "FRUTTA E VERDURA A COLORI"},
  {"id": "e1", "title": "1 · METTI IN ORDINE LE SILLABE", "short": "1 · Le sillabe", "type": "text",
   "cons": "SCRIVI IL NOME DELLA FRUTTA O DELLA VERDURA.",
   "items": [{"q": q} for q in ["1. NEL · RA · LO · VA", "2. RO · PE · NE · PE", "3. CHI · NA · ZUC", "4. NA · CI · SPI",
                                 "5. CIA · RAN · A", "6. RI · DA · MAN · NO", "7. COC · BI · CA · AL", "8. GIA · LIE · CI",
                                 "9. GNA · PRU", "10. FIO · VOL · RE · CA"]],
   "k": [has(a) for a in ["ravanell", "peperon", "zucchin", "spinac", "aranc", "mandarin", "albicocc", "cilieg", "prugn", "cavolfior"]]},
  {"id": "e2", "title": "2 · DI CHE COLORE È?", "short": "2 · I colori", "type": "select",
   "info": "OGNI GIORNO MANGIA ALMENO 5 PORZIONI DI FRUTTA E VERDURA.<br>MEGLIO SE HANNO COLORI DIVERSI: "
           "🔴 ROSSO · 🟢 VERDE · 🟠 GIALLO-ARANCIO · 🟣 BLU-VIOLA · ⚪ BIANCO.",
   "opts": ["ROSSO", "VERDE", "GIALLO-ARANCIO", "BLU-VIOLA", "BIANCO"],
   "items": [{"q": q} for q in ["1. 🍅 IL POMODORO", "2. 🥦 I BROCCOLI", "3. 🥕 LA CAROTA", "4. 🍆 LA MELANZANA", "5. 🧄 L'AGLIO",
                                 "6. 🍓 LA FRAGOLA", "7. 🥝 IL KIWI", "8. 🎃 LA ZUCCA", "9. 🫐 I MIRTILLI", "10. IL FINOCCHIO",
                                 "11. 🍋 IL LIMONE", "12. 🧅 LA CIPOLLA BIANCA"]],
   "k": [eq(a) for a in ["ROSSO", "VERDE", "GIALLO-ARANCIO", "BLU-VIOLA", "BIANCO", "ROSSO", "VERDE", "GIALLO-ARANCIO",
                         "BLU-VIOLA", "BIANCO", "GIALLO-ARANCIO", "BIANCO"]]},
  {"id": "e3", "title": "3 · QUALE PARTE DELLA PIANTA MANGI?", "short": "3 · La pianta", "type": "select",
   "cons": "🌱 RADICE · GAMBO · FOGLIE · FIORE · FRUTTO · SEMI",
   "opts": ["RADICE", "GAMBO", "FOGLIE", "FIORE", "FRUTTO", "SEMI"],
   "items": [{"q": q} for q in ["1. 🥕 LA CAROTA", "2. IL SEDANO", "3. 🥬 L'INSALATA", "4. IL CARCIOFO", "5. 🍅 IL POMODORO",
                                 "6. 🫛 I PISELLI", "7. IL RAVANELLO", "8. GLI ASPARAGI", "9. GLI SPINACI", "10. IL CAVOLFIORE",
                                 "11. 🍆 LA MELANZANA", "12. I CECI"]],
   "k": [eq(a) for a in ["RADICE", "GAMBO", "FOGLIE", "FIORE", "FRUTTO", "SEMI", "RADICE", "GAMBO", "FOGLIE", "FIORE", "FRUTTO", "SEMI"]]},

  {"part": "FRUTTA E VERDURA DI STAGIONE"},
  {"id": "e4", "title": "4 · IN QUALE STAGIONE LA TROVI AL MERCATO?", "short": "4 · Le stagioni", "type": "select",
   "info": "LA FRUTTA E LA VERDURA DI STAGIONE SONO PIÙ BUONE, FANNO BENE E COSTANO MENO.<br>"
           "🌸 PRIMAVERA · ☀️ ESTATE · 🍂 AUTUNNO · ❄️ INVERNO",
   "opts": STAGIONI,
   "items": [{"q": q} for q in ["1. 🍉 L'ANGURIA", "2. 🍒 LE CILIEGIE", "3. 🍊 LE ARANCE", "4. 🎃 LA ZUCCA", "5. 🍑 LE PESCHE",
                                 "6. 🌰 LE CASTAGNE", "7. LE FAVE FRESCHE", "8. I MANDARINI", "9. I FICHI", "10. 🍓 LE FRAGOLE"]],
   "k": [eq(a) for a in ["ESTATE", "PRIMAVERA", "INVERNO", "AUTUNNO", "ESTATE", "AUTUNNO", "PRIMAVERA", "INVERNO", "ESTATE", "PRIMAVERA"]]},

  {"part": "QUANTE VOLTE?"},
  {"id": "e5", "title": "5 · QUANTE VOLTE FA BENE MANGIARLO?", "short": "5 · Quante volte", "type": "select",
   "info": "✅ <b>TUTTI I GIORNI</b>: FRUTTA, VERDURA, PANE, PASTA, RISO, ACQUA, LATTE O YOGURT.<br>"
           "🗓️ <b>ALCUNE VOLTE ALLA SETTIMANA</b>: LEGUMI, PESCE, CARNE, UOVA, FORMAGGIO.<br>"
           "⚠️ <b>RARAMENTE</b>: DOLCI, MERENDINE, BIBITE GASSATE, PATATINE, SALAME, ALCOL.",
   "opts": ["TUTTI I GIORNI", "ALCUNE VOLTE ALLA SETTIMANA", "RARAMENTE"],
   "items": [{"q": q} for q in ["1. 🍎 LE MELE", "2. 🥗 L'INSALATA", "3. 🐟 LE SARDE", "4. 🍰 LA TORTA AL CIOCCOLATO",
                                 "5. 🍞 IL PANE", "6. 🥚 LE UOVA", "7. 🥤 LA BIBITA GASSATA", "8. 💧 L'ACQUA",
                                 "9. 🫘 I CECI", "10. 🍺 LA BIRRA", "11. 🍗 IL POLLO", "12. 🥛 LO YOGURT"]],
   "k": [eq(a) for a in ["TUTTI I GIORNI", "TUTTI I GIORNI", "ALCUNE VOLTE ALLA SETTIMANA", "RARAMENTE",
                         "TUTTI I GIORNI", "ALCUNE VOLTE ALLA SETTIMANA", "RARAMENTE", "TUTTI I GIORNI",
                         "ALCUNE VOLTE ALLA SETTIMANA", "RARAMENTE", "ALCUNE VOLTE ALLA SETTIMANA", "TUTTI I GIORNI"]]},
  {"id": "e6", "title": "6 · C'È TANTO ZUCCHERO?", "short": "6 · Lo zucchero", "type": "choice", "full": True,
   "opts": ["SÌ", "NO"],
   "items": [{"q": q} for q in ["1. LE UOVA", "2. IL TÈ FREDDO IN BOTTIGLIA", "3. LA CARNE", "4. IL SUCCO DI FRUTTA",
                                 "5. LE MERENDINE", "6. IL PESCE", "7. LE BIBITE GASSATE", "8. L'ACQUA"]],
   "k": [eq(a) for a in ["NO", "SÌ", "NO", "SÌ", "SÌ", "NO", "SÌ", "NO"]]},

  {"part": "I LEGUMI"},
  {"id": "e7", "title": "7 · TROVA IL NOME DEL LEGUME", "short": "7 · I legumi", "type": "text",
   "cons": "ATTENZIONE: IN OGNI RIGA C'È UNA SILLABA IN PIÙ!",
   "items": [{"q": q} for q in ["1. GIO · FA · LI · TA", "2. SEL · PI · CA · LI", "3. TIC · LEN · MO · CHIE",
                                 "4. CI · CE · PA", "5. VE · FA · RO", "6. IA · SO · NE"]],
   "k": [has("fagiol"), has("pisell"), has("lenticch"), has("ceci"), has("fave"), has("soia")]},
  {"id": "e8", "title": "8 · TI PIACCIONO?", "type": "survey",
   "cons": "NON CI SONO RISPOSTE GIUSTE O SBAGLIATE.",
   "opts": ["NON LI HO MAI MANGIATI", "NO", "COSÌ COSÌ", "SÌ", "TANTISSIMO"],
   "items": ["I FAGIOLI", "I PISELLI", "LE LENTICCHIE", "I CECI", "LE FAVE"]},

  {"part": "DA DOVE VIENE?"},
  {"id": "e9", "title": "9 · ANIMALE O VEGETALE?", "short": "9 · Animale o vegetale", "type": "choice", "full": True,
   "opts": ["ANIMALE 🐄", "VEGETALE 🌿"],
   "items": [{"q": q} for q in ["1. LE UOVA", "2. LO ZUCCHERO", "3. IL FORMAGGIO", "4. L'OLIO", "5. IL MIELE", "6. IL CAFFÈ",
                                 "7. IL BURRO", "8. IL CIOCCOLATO", "9. IL PROSCIUTTO", "10. IL PREZZEMOLO"]],
   "k": [eq(a) for a in ["ANIMALE 🐄", "VEGETALE 🌿", "ANIMALE 🐄", "VEGETALE 🌿", "ANIMALE 🐄", "VEGETALE 🌿",
                         "ANIMALE 🐄", "VEGETALE 🌿", "ANIMALE 🐄", "VEGETALE 🌿"]]},
  {"id": "e10", "title": "10 · DA DOVE VIENE?", "short": "10 · L'origine", "type": "select",
   "opts": ["LA MUCCA 🐄", "LA PECORA 🐑", "LA GALLINA 🐔", "LE API 🐝", "IL GRANO 🌾", "L'ALBERO 🌳"],
   "items": [{"q": q} for q in ["1. 🥛 IL LATTE", "2. 🧶 LA LANA", "3. 🥖 IL PANE", "4. 📄 LA CARTA", "5. 🍯 IL MIELE",
                                 "6. 🥚 L'UOVO", "7. 🍝 LA PASTA"]],
   "k": [eq(a) for a in ["LA MUCCA 🐄", "LA PECORA 🐑", "IL GRANO 🌾", "L'ALBERO 🌳", "LE API 🐝", "LA GALLINA 🐔", "IL GRANO 🌾"]]},

  {"part": "IL FRIGORIFERO"},
  {"id": "e11", "title": "11 · DOVE LO METTI?", "short": "11 · Il frigorifero", "type": "select",
   "cons": "LEGGI. SE METTI IL CIBO AL POSTO GIUSTO, DURA DI PIÙ E NON LO BUTTI.",
   "info": "🧊 <b>IN ALTO</b>: FORMAGGI, YOGURT, UOVA.<br>"
           "🧊 <b>IN MEZZO</b>: CIBI COTTI, AVANZI, SUGHI E SALUMI APERTI.<br>"
           "🧊 <b>IN BASSO</b>: CARNE E PESCE CRUDI.<br>"
           "🧊 <b>NEI CASSETTI</b>: FRUTTA E VERDURA.<br>"
           "🧊 <b>NELLO SPORTELLO</b>: LATTE, ACQUA, BIBITE.<br>"
           "❄️ <b>NEL FREEZER</b>: CIBI SURGELATI E GELATO.",
   "opts": ["IN ALTO", "IN MEZZO", "IN BASSO", "NEI CASSETTI", "NELLO SPORTELLO", "NEL FREEZER"],
   "items": [{"q": q} for q in ["1. LA MOZZARELLA", "2. LA PASTA AVANZATA DI IERI", "3. IL POLLO CRUDO", "4. LE ZUCCHINE",
                                 "5. LA BOTTIGLIA DI LATTE", "6. IL GELATO", "7. LO YOGURT", "8. IL BARATTOLO DI SUGO APERTO",
                                 "9. LE ALICI FRESCHE", "10. LE MELE", "11. I PISELLI SURGELATI"]],
   "k": [eq(a) for a in ["IN ALTO", "IN MEZZO", "IN BASSO", "NEI CASSETTI", "NELLO SPORTELLO", "NEL FREEZER",
                         "IN ALTO", "IN MEZZO", "IN BASSO", "NEI CASSETTI", "NEL FREEZER"]]},

  {"part": "LA TORTA DI AMINA"},
  {"id": "e12", "title": "12 · METTI IN ORDINE LA STORIA", "short": "12 · La storia", "type": "order",
   "cons": "SCEGLI IL NUMERO: 1 = LA PRIMA FRASE.",
   "items": ["ARRIVA KARIM. AMINA DICE: «CIAO! LA TORTA È PRONTA. VUOI ASSAGGIARE?»",
             "AMINA PRENDE UOVA, LATTE, FARINA, ZUCCHERO, BURRO E BANANE.",
             "KARIM ASSAGGIA E FA UNA BRUTTA FACCIA. AMINA CHIEDE: «NON TI PIACE?»",
             "AMINA DICE: «OGGI VOGLIO FARE UNA TORTA!»",
             "AMINA MESCOLA TUTTO E METTE L'IMPASTO NEL FRIGORIFERO PER DUE ORE."],
   "k": [eq("4"), eq("2"), eq("5"), eq("1"), eq("3")]},
  {"id": "e13", "title": "13 · PERCHÉ LA TORTA NON È BUONA?", "short": "13 · Perché?", "type": "choice", "full": True,
   "items": [{"q": "", "opts": ["C'È POCO ZUCCHERO.", "NON È COTTA NEL FORNO.", "LE BANANE SONO VECCHIE."]}],
   "k": [eq("NON È COTTA NEL FORNO.")]},

  {"part": "E TU?"},
  {"id": "e14", "title": "14 · LE TUE ABITUDINI", "type": "survey",
   "cons": "RISPONDI CON SINCERITÀ. NON CI SONO RISPOSTE GIUSTE O SBAGLIATE.",
   "opts": ["SÌ", "A VOLTE", "NO"],
   "items": ["FAI COLAZIONE OGNI MATTINA?", "MANGI SEDUTO/A AL TAVOLO, CON CALMA?", "MANGI SEMPRE ALLA STESSA ORA?",
             "MANGI FRUTTA OGNI GIORNO?", "MANGI VERDURA OGNI GIORNO?", "BEVI BIBITE GASSATE?",
             "GUARDI IL TELEFONO O LA TV QUANDO MANGI?"]},
  {"id": "e15", "title": "15 ✎ · SCRIVI", "type": "free", "rows": 2,
   "items": ["CHE COSA MANGI A COLAZIONE? A CHE ORA?", "CHE COSA MANGI A MERENDA?",
             "INVENTA UN FRULLATO: SCEGLI 3 INGREDIENTI (ESEMPIO: BANANA, LATTE, FRAGOLE).",
             "UN CIBO DEL TUO PAESE CHE FA BENE: CHE COS'È?"]},
  {"id": "e16", "title": "16 🎤 · PARLA", "type": "record",
   "items": ["CHE COSA MANGI IN UN GIORNO? PARLA DI COLAZIONE, PRANZO, MERENDA E CENA."]},
 ]
}

VF = ["vero", "falso"]
CODICE = ("A 1 · B 2 · C 3 · D 4 · E 5 · F 6 · G 7 · H 8 · I 9 · L 10 · M 11<br>"
          "N 12 · O 13 · P 14 · Q 15 · R 16 · S 17 · T 18 · U 19 · V 20 · Z 21")

A2 = {
 "title": "🥗 Mangiare sano · Letture A2",
 "store": "mangiare-sano-a2",
 "sections": [
  {"part": "Il cibo e il corpo"},
  {"id": "e1", "title": "1 · Che cosa c'è in questo cibo?", "short": "1 · Le sostanze", "type": "select",
   "cons": "Leggi, poi scegli la sostanza più importante di ogni cibo.",
   "info": "Il cibo ci dà l'energia per vivere, lavorare e muoverci. Nel cibo ci sono sostanze diverse:<br>"
           "🍝 i <b>carboidrati</b> danno energia: sono nel pane, nella pasta, nel riso e nelle patate;<br>"
           "🥩 le <b>proteine</b> costruiscono e riparano il corpo: sono nella carne, nel pesce, nelle uova e nei legumi;<br>"
           "🫒 i <b>grassi</b> sono una riserva di energia: sono nell'olio, nel burro e nella frutta secca;<br>"
           "🥦 le <b>vitamine</b> e i <b>sali minerali</b> aiutano il corpo a funzionare bene: sono soprattutto nella frutta e nella verdura;<br>"
           "🥛 il <b>calcio</b> rende forti le ossa e i denti: è nel latte, nello yogurt e nel formaggio.<br><br>"
           "Il cibo con troppi grassi, zucchero e sale si chiama <i>junk food</i>, cioè «cibo spazzatura».",
   "opts": ["carboidrati", "proteine", "grassi", "vitamine e sali minerali"],
   "items": [{"q": q} for q in ["1. la focaccia", "2. le lenticchie", "3. le mandorle", "4. gli spinaci", "5. il tonno",
                                 "6. le friselle", "7. l'olio d'oliva", "8. i mandarini", "9. il pollo", "10. il couscous",
                                 "11. il burro", "12. i peperoni"]],
   "k": [eq(a) for a in ["carboidrati", "proteine", "grassi", "vitamine e sali minerali", "proteine", "carboidrati",
                         "grassi", "vitamine e sali minerali", "proteine", "carboidrati", "grassi", "vitamine e sali minerali"]]},
  {"id": "e2", "title": "2 · Completa le frasi", "short": "2 · Completa", "type": "cloze",
   "bank": "calcio · carboidrati · grassi · proteine · vitamine",
   "parts": ["Prima di giocare a calcio mangio un piatto di pasta: i ", {}, " mi danno energia. "
             "Mia figlia beve il latte perché il ", {}, " fa bene alle ossa. Dopo la palestra mangio uova e legumi: le ", {},
             " aiutano i muscoli. D'inverno mangio molte arance: le ", {}, " mi aiutano a non ammalarmi. "
             "Uso poco burro perché ha molti ", {}, "."],
   "k": [eq("carboidrati"), eq("calcio"), eq("proteine"), eq("vitamine"), eq("grassi")]},

  {"part": "Quante volte?"},
  {"id": "e3", "title": "3 · Leggi i consigli e scegli", "short": "3 · Quante volte", "type": "select",
   "info": "<b>Ogni giorno</b>: frutta e verdura (almeno 5 porzioni), pane, pasta o riso (meglio integrali), latte o yogurt, "
           "un po' di frutta secca e tanta acqua (circa 8 bicchieri). Per condire, olio extravergine d'oliva.<br>"
           "<b>2-3 volte alla settimana</b>: legumi, pesce, carne bianca (pollo, tacchino), uova, formaggi.<br>"
           "<b>1 volta alla settimana</b>: carne rossa.<br>"
           "<b>Solo ogni tanto</b>: dolci, salumi, bibite zuccherate, cibi fritti. E poco sale!",
   "opts": ["ogni giorno", "2-3 volte alla settimana", "1 volta alla settimana", "solo ogni tanto"],
   "items": [{"q": q} for q in ["1. la verdura", "2. il pesce", "3. la carne di manzo", "4. i fagioli", "5. le patatine fritte",
                                 "6. lo yogurt", "7. il formaggio", "8. le bibite zuccherate", "9. il riso", "10. il tacchino"]],
   "k": [eq(a) for a in ["ogni giorno", "2-3 volte alla settimana", "1 volta alla settimana", "2-3 volte alla settimana",
                         "solo ogni tanto", "ogni giorno", "2-3 volte alla settimana", "solo ogni tanto", "ogni giorno",
                         "2-3 volte alla settimana"]]},

  {"part": "Il cibo biologico"},
  {"id": "e4", "title": "4 · Vero o falso?", "short": "4 · Il biologico", "type": "choice", "full": True,
   "info": "Al supermercato vedi spesso la scritta «BIO». Che cosa vuol dire? Un prodotto biologico viene da un'agricoltura "
           "che non usa pesticidi e concimi chimici. Questi prodotti chimici possono fare male alla salute, all'ambiente e agli animali. "
           "Nei cibi biologici non ci sono coloranti e conservanti artificiali. A volte la frutta bio è meno bella "
           "(più piccola, con qualche macchia), ma è buona e sana. Di solito i prodotti bio costano un po' di più.<br>"
           "Un consiglio: compra frutta e verdura di stagione, al mercato o dai contadini della zona.",
   "opts": VF,
   "items": [{"q": q} for q in ["1. I prodotti biologici hanno la scritta «BIO».", "2. L'agricoltura biologica usa molti pesticidi.",
                                 "3. I prodotti chimici possono fare male all'ambiente.", "4. Nei cibi biologici ci sono coloranti artificiali.",
                                 "5. La frutta bio è sempre più bella.", "6. Di solito i prodotti bio costano un po' di più."]],
   "k": [eq(a) for a in ["vero", "falso", "vero", "falso", "falso", "vero"]]},

  {"part": "I sapori"},
  {"id": "e5", "title": "5 · Che sapore ha?", "short": "5 · I sapori", "type": "select",
   "info": "La lingua sente i sapori. I sapori principali sono quattro: <b>dolce</b> (lo zucchero), <b>salato</b> (il sale), "
           "<b>amaro</b> (il caffè senza zucchero) e <b>acido</b> (il limone). Nel 1908 uno scienziato giapponese, Kikunae Ikeda, "
           "ha scoperto un quinto sapore: l'<b>umami</b>. È un sapore molto saporito, come il brodo di carne, il parmigiano o i funghi secchi. "
           "Oggi alcuni ricercatori pensano che esista anche un sesto sapore: il sapore del <b>grasso</b>.",
   "opts": ["dolce", "salato", "amaro", "acido", "umami"],
   "items": [{"q": q} for q in ["1. il miele", "2. il limone", "3. le olive in salamoia", "4. il cioccolato fondente",
                                 "5. il brodo di carne", "6. la torta", "7. le patatine", "8. la cicoria", "9. lo yogurt bianco"]],
   "k": [eq("dolce"), eq("acido"), eq("salato"), eq("amaro"), eq("umami", "salato"), eq("dolce"), eq("salato"), eq("amaro"), eq("acido")]},
  {"id": "e6", "title": "6 ✎ · I tuoi sapori", "type": "free", "rows": 3,
   "items": ["Per ogni sapore scrivi un cibo che ti piace. Esempio: dolce → i datteri; salato → …"]},

  {"part": "Le spezie"},
  {"id": "e7", "title": "7 · Vero o falso?", "short": "7 · Le spezie", "type": "choice", "full": True,
   "info": "Le spezie sono semi, frutti, radici o cortecce di piante, seccati. In tutto il mondo le usiamo per dare sapore "
           "e colore al cibo e anche per conservarlo. Il <b>pepe</b> è la spezia più venduta del mondo. Lo <b>zafferano</b> è la più cara. "
           "La <b>curcuma</b> e lo <b>zenzero</b> sono usati anche come medicine naturali. Molte spezie arrivano dall'Asia. "
           "Nel 1492 Cristoforo Colombo cercava una nuova strada per l'India e le sue spezie, ma è arrivato in America: "
           "da lì il <b>peperoncino</b> è arrivato in Europa. E nel tuo paese, quali spezie usate in cucina?",
   "opts": VF,
   "items": [{"q": q} for q in ["1. Il pepe è la spezia più venduta del mondo.", "2. Lo zafferano costa poco.",
                                 "3. Le spezie servono anche a conservare il cibo.", "4. Colombo è arrivato in India.",
                                 "5. Il peperoncino è arrivato in Europa dall'America."]],
   "k": [eq(a) for a in ["vero", "falso", "vero", "falso", "vero"]]},
  {"id": "e8", "title": "8 · Metti in ordine le sillabe", "short": "8 · Nomi di spezie", "type": "text",
   "cons": "Scrivi il nome della spezia.",
   "items": [{"q": q} for q in ["1. CU · MA · CUR", "2. RO · ZEN · ZE", "3. FE · ZAF · NO · RA", "4. NEL · CAN · LA",
                                 "5. RON · PE · CI · PE · NO", "6. MO · DA · CAR · MO"]],
   "k": [has("curcuma"), has("zenzero"), has("zafferano"), has("cannella"), has("peperoncin"), has("cardamomo")]},

  {"part": "Il pesce azzurro"},
  {"id": "e9", "title": "9 · Scopri i nomi dei pesci", "short": "9 · Il codice", "type": "text",
   "info": "A Bari il pesce è una tradizione: la mattina, al porto, i pescatori vendono il pesce appena pescato. "
           "Il <b>pesce azzurro</b> è un gruppo di pesci con la schiena blu-verde e la pancia color argento. "
           "Costa poco ed è molto sano: ha proteine, vitamine, calcio, iodio e grassi «buoni», gli <b>Omega-3</b>, "
           "che aiutano il cuore e il cervello. È bene mangiare pesce 2 o 3 volte alla settimana. "
           "A Bari, per esempio, si mangiano le alici arraganate: al forno, con pangrattato e origano.<br><br>"
           "🔢 <b>Il codice</b>: " + CODICE,
   "cons": "Cambia i numeri in lettere e scrivi il nome del pesce azzurro.",
   "items": [{"q": q} for q in ["1. 1 · 10 · 9 · 3 · 9", "2. 17 · 1 · 16 · 4 · 9 · 12 · 5", "3. 17 · 7 · 13 · 11 · 2 · 16 · 13",
                                 "4. 18 · 13 · 12 · 12 · 13"]],
   "k": [has("alici"), has("sardine"), has("sgombro"), has("tonno")]},
  {"id": "e10", "title": "10 · Vero o falso?", "short": "10 · Il pesce", "type": "choice", "full": True,
   "opts": VF,
   "items": [{"q": q} for q in ["1. Il pesce azzurro costa molto.", "2. Le alici sono pesce azzurro.",
                                 "3. Gli Omega-3 aiutano il cuore.", "4. È bene mangiare pesce una volta al mese."]],
   "k": [eq(a) for a in ["falso", "vero", "vero", "falso"]]},

  {"part": "Una ricetta"},
  {"id": "e11", "title": "11 · I biscotti a spirale: completa", "short": "11 · La ricetta", "type": "cloze",
   "cons": "Ingredienti: 500 g di farina, 120 g di zucchero, 3 uova, 100 g di burro, 1 bustina di lievito, 50 g di cacao amaro, un po' di latte.",
   "bank": "aggiungi · arrotola · cuoci · dividi · mescola · sbatti · sciogli · stendi · taglia",
   "parts": ["Prima ", {}, " il burro in un pentolino. In una ciotola ", {}, " le uova con lo zucchero. ", {},
             " il burro, la farina e il lievito e ", {}, " bene. Quando l'impasto è morbido, ", {},
             " l'impasto in due parti. In una metà metti il cacao e un cucchiaio di latte. Con il mattarello ", {},
             " i due impasti, mettili uno sopra l'altro e ", {}, " tutto. ", {}, " il rotolo a fette e ", {},
             " i biscotti in forno a 180 gradi per 10-12 minuti."],
   "k": [eq("sciogli"), eq("sbatti"), eq("aggiungi"), eq("mescola"), eq("dividi"), eq("stendi"), eq("arrotola"),
         eq("taglia"), eq("cuoci")]},

  {"part": "Colazione e merenda"},
  {"id": "e12", "title": "12 · È una merenda sana?", "short": "12 · La merenda", "type": "choice", "full": True,
   "info": "In Italia molte persone fanno una colazione dolce: caffè o latte con biscotti, oppure fette biscottate e marmellata. "
           "Ma va bene anche una colazione salata, con pane e formaggio o uova. L'importante è non saltare la colazione "
           "e mangiare con calma, seduti. A metà mattina e a metà pomeriggio si può fare una piccola merenda: "
           "un frutto, uno yogurt, pane e pomodoro, un po' di frutta secca.",
   "opts": ["sì", "no"],
   "items": [{"q": q} for q in ["1. una mela", "2. un pacchetto grande di patatine", "3. uno yogurt", "4. una lattina di bibita gassata",
                                 "5. pane e pomodoro", "6. una manciata di noci", "7. tre merendine confezionate", "8. un frullato di frutta e latte"]],
   "k": [eq(a) for a in ["sì", "no", "sì", "no", "sì", "sì", "no", "sì"]]},

  {"part": "E tu?"},
  {"id": "e13", "title": "13 ✎ · Le tue abitudini", "type": "free", "rows": 3,
   "items": ["Rispetti queste regole: colazione con calma, pasti a orari regolari, acqua durante i pasti? Quali no, e perché?",
             "Queste regole sono solo per i bambini? Che cosa ne pensi?",
             "Quando mangi guardi la televisione o il telefono?"]},
  {"id": "e14", "title": "14 🎤 · Parla", "type": "record",
   "items": ["Racconta che cosa si mangia in una giornata normale nel tuo paese. È diverso dall'Italia?"]},
 ]
}
