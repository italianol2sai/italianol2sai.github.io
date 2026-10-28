// Contenuti del gioco «Missione casa»: storia, stanze e prove.
// Tutti i testi visibili sono scritti in MAIUSCOLO.
// Per cambiare una domanda basta modificare questo file.
//
// Le battute della storia sono coppie [chi parla, testo]; chi parla è una
// chiave di persone.js (serena, maryam, rosa).
//
// Tipi di prova:
//   scelta   – scegli una risposta (correct = indice della risposta giusta)
//   vf       – vero o falso (correct = true / false)
//   completa – completa la frase: «___» nel testo viene riempito
//   collega  – collega a sinistra e a destra (coppie nell'ordine giusto)
//   ordine   – tocca le frasi nell'ordine giusto (items nell'ordine giusto)
//   errore   – tocca la riga sbagliata di un documento (correct = indice della riga)
//
// Le risposte vengono mescolate quando il gioco parte.

window.MISSIONE = {
  titolo: "MISSIONE CASA",
  sottotitolo: "TROVA LA TUA CASA A BARI!",
  parolaSegreta: "CHIAVI",
  sito: "https://italianol2sai.github.io/",
  chiaveSalva: "missione-casa-v1",
  guida: "serena",
  protagonista: "maryam",
  etichetta: "ITALIANO L2 · LA CASA",
  portaFinale: "LA PORTA DI CASA",
  grazie: "GRAZIE! SENZA DI TE NON CE LA FACEVO!",
  imparato: "HAI IMPARATO A LEGGERE GLI ANNUNCI, A SCRIVERE AL PROPRIETARIO E A TELEFONARE PER UNA CASA.",

  intro: [
    ["maryam", "CIAO! MI CHIAMO MARYAM. HO 26 ANNI. SONO IN ITALIA DA DUE ANNI. ABITO A BARI, IN UN APPARTAMENTO DEL PROGETTO SAI."],
    ["maryam", "ADESSO LAVORO IN UN NEGOZIO COME COMMESSA, A TEMPO PIENO. TRA DUE MESI DEVO LASCIARE L’APPARTAMENTO DEL SAI. CERCO UNA CASA TUTTA MIA!"],
    ["serena", "IO SONO SERENA. LAVORO PER ETNIE, NEL PROGETTO SAI DI BARI. TU PUOI AIUTARE MARYAM!"],
    ["serena", "CI SONO 6 PORTE. DIETRO OGNI PORTA C’È UNA LETTERA. CON LE 6 LETTERE SCOPRI CHE COSA RICEVE MARYAM ALLA FINE!"]
  ],

  finale: [
    ["maryam", "È SABATO MATTINA. OGGI FIRMO IL CONTRATTO CON LA SIGNORA ROSA. SONO EMOZIONATA!"],
    ["rosa", "BUONGIORNO, MARYAM! ECCO IL CONTRATTO. E ADESSO HO UNA COSA PER TE…"],
    ["serena", "CHE COSA DÀ LA SIGNORA ROSA A MARYAM? SCRIVI LA PAROLA SEGRETA CON LE 6 LETTERE DEL TUO BADGE."]
  ],
  vittoria: "LA SIGNORA ROSA DICE: «ECCO LE CHIAVI, MARYAM. BENVENUTA NELLA TUA NUOVA CASA!»",

  stanze: [
    {
      id: "stanze",
      titolo: "LE STANZE DELLA CASA",
      icona: "🛋️",
      lettera: "C",
      chi: "serena",
      lezione: { titolo: "CERCARE CASA A BARI", link: "cercare-casa/" },
      storia: [
        ["maryam", "SERENA, VOGLIO CERCARE UNA CASA. MA GLI ANNUNCI SONO DIFFICILI!"],
        ["serena", "TRANQUILLA, MARYAM. PRIMA RIPASSIAMO LE PAROLE DELLA CASA."]
      ],
      fine: ["maryam", "CONOSCO TUTTE LE STANZE. ADESSO POSSO LEGGERE GLI ANNUNCI!"],
      prove: [
        {
          tipo: "collega",
          domanda: "A CHE COSA SERVONO LE STANZE? COLLEGA.",
          coppie: [
            ["🍳 LA CUCINA", "CUCINARE E MANGIARE"],
            ["🛏️ LA CAMERA DA LETTO", "DORMIRE"],
            ["🚿 IL BAGNO", "LAVARSI E FARE LA DOCCIA"],
            ["📺 IL SOGGIORNO", "GUARDARE LA TV E STARE INSIEME"]
          ],
          aiuto: "TOCCA UNA STANZA. POI TOCCA CHE COSA FAI LÌ.",
          spiega: "IN CUCINA CUCINO, IN CAMERA DORMO, IN BAGNO MI LAVO, IN SOGGIORNO STO CON GLI AMICI."
        },
        {
          tipo: "scelta",
          domanda: "LA DOMENICA MARYAM BEVE IL CAFFÈ FUORI, AL SOLE E ALL’ARIA. DOVE È?",
          icona: "☀️",
          risposte: [
            { t: "SUL BALCONE", i: "🌿" },
            { t: "IN SOGGIORNO", i: "📺" },
            { t: "IN CANTINA", i: "📦" }
          ],
          correct: 0,
          aiuto: "È FUORI, MA È ANCORA A CASA.",
          spiega: "IL BALCONE SERVE PER PRENDERE IL SOLE E L’ARIA."
        },
        {
          tipo: "scelta",
          domanda: "LA SERA MARYAM GUARDA UN FILM CON LE AMICHE. IN QUALE STANZA SONO?",
          icona: "🍿",
          risposte: [
            { t: "IN SOGGIORNO", i: "🛋️" },
            { t: "IN CAMERA DA LETTO", i: "🛏️" },
            { t: "SUL BALCONE", i: "🌿" }
          ],
          correct: 0,
          aiuto: "È LA STANZA PER STARE INSIEME. C’È IL DIVANO.",
          spiega: "IL SOGGIORNO SERVE PER GUARDARE LA TV E STARE INSIEME."
        },
        {
          tipo: "completa",
          domanda: "MARYAM PREPARA LA CENA. COMPLETA.",
          frase: "MARYAM CUCINA IL RISO IN ___.",
          icona: "🍚",
          risposte: ["CUCINA", "CANTINA", "CAMERA"],
          correct: 0,
          aiuto: "LA CANTINA È SOTTO IL PALAZZO. IN CAMERA SI DORME.",
          spiega: "IN CUCINA SI CUCINA E SI MANGIA."
        },
        {
          tipo: "completa",
          domanda: "LA CASA È SOPRA, NEL PALAZZO: 1°, 2°, 3°… COMPLETA.",
          frase: "LA CASA È AL TERZO ___.",
          icona: "🏢",
          risposte: ["PIANO", "METRO", "BAGNO"],
          correct: 0,
          aiuto: "PIANO TERRA, PRIMO, SECONDO, TERZO…",
          spiega: "AL TERZO PIANO = SOPRA, NEL PALAZZO. A VOLTE C’È L’ASCENSORE."
        }
      ]
    },

    {
      id: "parole",
      titolo: "LE PAROLE DEGLI ANNUNCI",
      icona: "📋",
      lettera: "H",
      chi: "serena",
      lezione: { titolo: "CERCARE CASA A BARI", link: "cercare-casa/" },
      storia: [
        ["maryam", "GUARDA QUESTO ANNUNCIO: «BILO ARRED., 45 MQ, RISC. AUT.». NON CAPISCO NIENTE!"],
        ["serena", "NEGLI ANNUNCI SI SCRIVE CORTO. TI SPIEGO LE PAROLE PIÙ IMPORTANTI."]
      ],
      fine: ["serena", "BRAVA, MARYAM! ADESSO CAPISCI LE PAROLE DEGLI ANNUNCI."],
      prove: [
        {
          tipo: "scelta",
          domanda: "UNA CASA CON 2 STANZE + IL BAGNO È UN…",
          icona: "🏠",
          risposte: [
            { t: "BILOCALE", i: "2️⃣" },
            { t: "MONOLOCALE", i: "1️⃣" },
            { t: "TRILOCALE", i: "3️⃣" }
          ],
          correct: 0,
          aiuto: "MONO = 1, BI = 2, TRI = 3.",
          spiega: "BILOCALE = 2 STANZE + BAGNO. MONOLOCALE = 1 STANZA, TRILOCALE = 3 STANZE."
        },
        {
          tipo: "scelta",
          domanda: "L’ANNUNCIO DICE: «APPARTAMENTO ARREDATO». CHE COSA VUOL DIRE?",
          icona: "🛋️",
          risposte: [
            { t: "CON I MOBILI DENTRO", i: "🛏️" },
            { t: "CON IL RISCALDAMENTO", i: "🔥" },
            { t: "CON L’ASCENSORE", i: "🛗" }
          ],
          correct: 0,
          aiuto: "PENSA AL LETTO, AL TAVOLO, AL DIVANO…",
          spiega: "ARREDATO = CON I MOBILI. NON DEVI COMPRARE IL LETTO E IL TAVOLO."
        },
        {
          tipo: "collega",
          domanda: "LE PAROLE CORTE DEGLI ANNUNCI. COLLEGA.",
          coppie: [
            ["BILO", "BILOCALE"],
            ["ARRED.", "ARREDATO"],
            ["MQ", "METRI QUADRI"],
            ["RISC. AUT.", "RISCALDAMENTO AUTONOMO"]
          ],
          aiuto: "GUARDA LE PRIME LETTERE DI OGNI PAROLA.",
          spiega: "BILO = BILOCALE, ARRED. = ARREDATO, MQ = METRI QUADRI, RISC. AUT. = RISCALDAMENTO AUTONOMO."
        },
        {
          tipo: "scelta",
          domanda: "CHE COSA SONO LE «SPESE CONDOMINIALI»?",
          icona: "🏢",
          risposte: [
            { t: "SOLDI PER IL PALAZZO: SCALE, ASCENSORE, PULIZIA", i: "🧹" },
            { t: "SOLDI DI GARANZIA PER IL PROPRIETARIO", i: "💰" },
            { t: "L’AFFITTO DI OGNI MESE", i: "📅" }
          ],
          correct: 0,
          aiuto: "IL CONDOMINIO È IL PALAZZO DOVE ABITANO TANTE FAMIGLIE.",
          spiega: "LE SPESE CONDOMINIALI PAGANO LE SCALE, L’ASCENSORE E LA PULIZIA DEL PALAZZO."
        },
        {
          tipo: "completa",
          domanda: "COMPLETA LA FRASE.",
          frase: "IL ___ È L’AFFITTO DI OGNI MESE.",
          icona: "💶",
          risposte: ["CANONE", "CAUZIONE", "CONDOMINIO"],
          correct: 0,
          aiuto: "LA CAUZIONE È LA GARANZIA. IL CONDOMINIO È IL PALAZZO.",
          spiega: "CANONE = L’AFFITTO CHE PAGHI OGNI MESE."
        },
        {
          tipo: "vf",
          domanda: "«RISCALDAMENTO AUTONOMO» VUOL DIRE: LO ACCENDI TU E LO PAGHI TU.",
          icona: "🔥",
          correct: true,
          aiuto: "AUTONOMO = SOLO PER LA TUA CASA, NON PER TUTTO IL PALAZZO.",
          spiega: "VERO. CON IL RISCALDAMENTO AUTONOMO DECIDI TU E PAGHI TU."
        }
      ]
    },

    {
      id: "annunci",
      titolo: "LEGGO GLI ANNUNCI",
      icona: "📰",
      lettera: "I",
      chi: "serena",
      lezione: { titolo: "CERCARE CASA A BARI", link: "cercare-casa/" },
      storia: [
        ["serena", "ECCO ALCUNI ANNUNCI DI BARI E PROVINCIA. QUANTO PUOI SPENDERE, MARYAM?"],
        ["maryam", "AL MASSIMO 500 € AL MESE, CON LE SPESE. NON HO LA MACCHINA E LAVORO IN CITTÀ."],
        ["serena", "ALLORA LEGGIAMO BENE. ATTENZIONE AI PREZZI E ALLE SPESE!"]
      ],
      fine: ["maryam", "HO TROVATO LA MIA CASA: IL BILOCALE A SAN PASQUALE! 450 €, SPESE INCLUSE, CON L’ASCENSORE."],
      prove: [
        {
          tipo: "scelta",
          domanda: "MARYAM HA 500 € AL MESE E NON VUOLE PAGARE LE SPESE A PARTE. QUALE CASA PUÒ PRENDERE?",
          documento: {
            titolo: "📰 TRE ANNUNCI",
            tabella: [
              ["🏙️ MURAT", "690 € + SPESE"],
              ["🌊 MOLA DI BARI", "600 € + SPESE"],
              ["🏘️ SAN PASQUALE", "450 € SPESE INCLUSE"]
            ]
          },
          risposte: [
            { t: "SAN PASQUALE", i: "🏘️" },
            { t: "MOLA DI BARI", i: "🌊" },
            { t: "MURAT", i: "🏙️" }
          ],
          correct: 0,
          aiuto: "«+ SPESE» VUOL DIRE CHE PAGHI ANCORA DI PIÙ.",
          spiega: "SAN PASQUALE: 450 € CON LE SPESE. LE ALTRE CASE COSTANO PIÙ DI 500 €."
        },
        {
          tipo: "vf",
          domanda: "LA CASA A MURAT HA L’ASCENSORE.",
          documento: {
            titolo: "📰 ANNUNCIO · MURAT (CENTRO)",
            righe: ["BILOCALE ARREDATO, 50 MQ, PIANO RIALZATO, SENZA ASCENSORE. RISCALDAMENTO AUTONOMO. VICINO ALL’UNIVERSITÀ. 690 €/MESE + SPESE."]
          },
          correct: false,
          aiuto: "CERCA LA PAROLA «ASCENSORE» NELL’ANNUNCIO. CHE PAROLA C’È PRIMA?",
          spiega: "FALSO. L’ANNUNCIO DICE «SENZA ASCENSORE»."
        },
        {
          tipo: "scelta",
          domanda: "IL TRILOCALE A CARBONARA È ARREDATO?",
          documento: {
            titolo: "📰 ANNUNCIO · CARBONARA (PERIFERIA)",
            righe: ["TRILOCALE NON ARREDATO, 80 MQ, 2° PIANO, SENZA ASCENSORE. TERRAZZO E CANTINA. 550 €/MESE + SPESE."]
          },
          risposte: [
            { t: "NO: NON CI SONO I MOBILI", i: "❌" },
            { t: "SÌ: CI SONO TUTTI I MOBILI", i: "✅" },
            { t: "SÌ, MA SOLO LA CUCINA", i: "🍳" }
          ],
          correct: 0,
          aiuto: "LEGGI LA PRIMA RIGA: «TRILOCALE NON…»",
          spiega: "«NON ARREDATO» = SENZA MOBILI. DEVI COMPRARE TU IL LETTO E IL TAVOLO."
        },
        {
          tipo: "collega",
          domanda: "QUALE CASA PER QUALE PERSONA? COLLEGA.",
          coppie: [
            ["👩 FATIMA LAVORA IN CENTRO E NON HA LA MACCHINA", "🏙️ MURAT"],
            ["👨‍👩‍👧‍👦 AHMED HA UNA FAMIGLIA GRANDE", "🏡 TRILOCALE A CARBONARA"],
            ["🧍 LUAN VIVE SOLO E HA POCHI SOLDI", "🏠 MONOLOCALE A LIBERTÀ"],
            ["🚗 MARIA AMA IL MARE E HA LA MACCHINA", "🌊 MOLA DI BARI"]
          ],
          aiuto: "UNA FAMIGLIA GRANDE HA BISOGNO DI TANTE STANZE. CHI È SOLO SPENDE POCO.",
          spiega: "MURAT È IN CENTRO, CARBONARA HA 3 STANZE, LIBERTÀ COSTA POCO, MOLA È VICINO AL MARE."
        },
        {
          tipo: "errore",
          domanda: "MARYAM LEGGE: «MODUGNO, BILOCALE ARREDATO, PIANO TERRA, POSTO AUTO, 480 € SPESE INCLUSE». POI SCRIVE GLI APPUNTI. TOCCA LA RIGA SBAGLIATA.",
          documento: { titolo: "📝 APPUNTI DI MARYAM · MODUGNO" },
          righe: [
            "🏠 BILOCALE ARREDATO",
            "🚪 PIANO TERRA",
            "🚗 CON POSTO AUTO",
            "💶 480 € + SPESE"
          ],
          correct: 3,
          aiuto: "CONTROLLA IL PREZZO: LE SPESE SONO A PARTE O INCLUSE?",
          spiega: "L’ANNUNCIO DICE «SPESE INCLUSE»: 480 € CON TUTTO."
        },
        {
          tipo: "scelta",
          domanda: "PERCHÉ IL BILOCALE A SAN PASQUALE VA BENE PER MARYAM?",
          documento: {
            titolo: "📰 ANNUNCIO · SAN PASQUALE",
            righe: ["BILOCALE ARREDATO, 45 MQ, 3° PIANO CON ASCENSORE. RISCALDAMENTO AUTONOMO. ZONA TRANQUILLA. 450 €/MESE, SPESE INCLUSE. DISPONIBILE DA SUBITO."]
          },
          risposte: [
            { t: "COSTA MENO DI 500 € E C’È GIÀ TUTTO", i: "👍" },
            { t: "È UN TRILOCALE CON IL TERRAZZO", i: "🌇" },
            { t: "È VICINO AL MARE, CON IL POSTO AUTO", i: "🌊" }
          ],
          correct: 0,
          aiuto: "MARYAM HA 500 € E NON HA I MOBILI.",
          spiega: "450 € CON LE SPESE, ARREDATO, DISPONIBILE DA SUBITO: PERFETTO PER MARYAM!"
        }
      ]
    },

    {
      id: "documenti",
      titolo: "DOCUMENTI E SOLDI",
      icona: "🪪",
      lettera: "A",
      chi: "serena",
      lezione: { titolo: "CERCARE CASA A BARI", link: "cercare-casa/" },
      storia: [
        ["maryam", "SERENA, CHE COSA MI SERVE PER AFFITTARE LA CASA?"],
        ["serena", "SERVONO I DOCUMENTI GIUSTI E UN PO’ DI SOLDI PER COMINCIARE. VEDIAMO INSIEME."]
      ],
      fine: ["serena", "BENE: MARYAM HA I DOCUMENTI E I SOLDI PER COMINCIARE. ADESSO SCRIVIAMO AL PROPRIETARIO!"],
      prove: [
        {
          tipo: "scelta",
          domanda: "QUALE DOCUMENTO NON SERVE PER AFFITTARE UNA CASA?",
          icona: "📂",
          risposte: [
            { t: "LA PATENTE DI GUIDA", i: "🚗" },
            { t: "IL CODICE FISCALE", i: "🔢" },
            { t: "IL PERMESSO DI SOGGIORNO", i: "📄" }
          ],
          correct: 0,
          aiuto: "SERVONO: DOCUMENTO, CODICE FISCALE, PERMESSO DI SOGGIORNO, PROVA DEL LAVORO.",
          spiega: "LA PATENTE SERVE PER GUIDARE, NON PER LA CASA."
        },
        {
          tipo: "scelta",
          domanda: "L’ANNUNCIO DICE «SOLO REFERENZIATI». CHE COSA DEVE MOSTRARE MARYAM?",
          icona: "💼",
          risposte: [
            { t: "IL CONTRATTO DI LAVORO O LA BUSTA PAGA", i: "💼" },
            { t: "LA TESSERA SANITARIA", i: "🏥" },
            { t: "IL CERTIFICATO DELLA SCUOLA DI ITALIANO", i: "📘" }
          ],
          correct: 0,
          aiuto: "IL PROPRIETARIO VUOLE SAPERE SE PUOI PAGARE L’AFFITTO OGNI MESE.",
          spiega: "«SOLO REFERENZIATI» = DEVI MOSTRARE CHE HAI UN LAVORO."
        },
        {
          tipo: "scelta",
          domanda: "CHE COSA È LA CAUZIONE?",
          icona: "💰",
          risposte: [
            { t: "2 O 3 MESI DI GARANZIA: LA RIPRENDI ALLA FINE", i: "🔙" },
            { t: "L’AFFITTO DEL PRIMO MESE", i: "1️⃣" },
            { t: "I SOLDI PER L’AGENZIA", i: "🤝" }
          ],
          correct: 0,
          aiuto: "È UNA GARANZIA PER IL PROPRIETARIO, SE ROMPI QUALCOSA.",
          spiega: "LA CAUZIONE È UNA GARANZIA DI 2–3 MESI. SE LASCI LA CASA IN ORDINE, LA RIPRENDI."
        },
        {
          tipo: "scelta",
          domanda: "LA CASA COSTA 450 € AL MESE. LA CAUZIONE È DI 2 MESI. NON C’È L’AGENZIA. QUANTO PAGA MARYAM ALL’INIZIO?",
          documento: {
            titolo: "🧮 ALL’INIZIO PAGHI",
            tabella: [
              ["1️⃣ PRIMO MESE", "450 €"],
              ["💰 CAUZIONE (2 MESI)", "? €"],
              ["🤝 AGENZIA", "0 €"]
            ]
          },
          risposte: [
            { t: "1.350 €", i: "✅" },
            { t: "900 €", i: "🤔" },
            { t: "450 €", i: "🤔" }
          ],
          correct: 0,
          aiuto: "PRIMO MESE + 2 MESI DI CAUZIONE = 3 VOLTE 450 €.",
          spiega: "450 + 900 = 1.350 €. ALL’INIZIO SERVONO TANTI SOLDI: METTILI DA PARTE!"
        },
        {
          tipo: "collega",
          domanda: "LE PAROLE DIFFICILI DEGLI ANNUNCI. COLLEGA.",
          coppie: [
            ["NO AGENZIE", "SCRIVI DIRETTAMENTE AL PROPRIETARIO"],
            ["USO TRANSITORIO", "CONTRATTO BREVE: MASSIMO 18 MESI"],
            ["CONTRATTO 4+4", "CONTRATTO LUNGO: 4 ANNI + 4"],
            ["DISPONIBILE", "PUOI ENTRARE IN CASA"]
          ],
          aiuto: "TRANSITORIO = PER POCO TEMPO. 4+4 = TANTI ANNI.",
          spiega: "NO AGENZIE = SOLO PROPRIETARIO. USO TRANSITORIO = BREVE. 4+4 = LUNGO. DISPONIBILE = LIBERA."
        },
        {
          tipo: "vf",
          domanda: "A BARI UN BILOCALE IN CENTRO (MURAT) COSTA DI PIÙ CHE IN PROVINCIA (MODUGNO).",
          icona: "🏙️",
          correct: true,
          aiuto: "MURAT: 650–750 €. MODUGNO: 400–550 €.",
          spiega: "VERO. IL CENTRO È PIÙ CARO. IN PERIFERIA E IN PROVINCIA PAGHI MENO."
        }
      ]
    },

    {
      id: "messaggio",
      titolo: "SCRIVO AL PROPRIETARIO",
      icona: "✉️",
      lettera: "V",
      chi: "serena",
      lezione: { titolo: "CERCARE CASA · ESERCIZI", link: "cercare-casa/esercizi.html" },
      storia: [
        ["maryam", "VOGLIO SCRIVERE ALLA PROPRIETARIA DI SAN PASQUALE, LA SIGNORA ROSA. MA HO PAURA DI SBAGLIARE!"],
        ["serena", "TI AIUTO IO. RIPASSIAMO LE PAROLE PICCOLE E LE FRASI GENTILI."]
      ],
      fine: ["maryam", "HO MANDATO IL MESSAGGIO! LA SIGNORA ROSA RISPONDE: «MI TELEFONI DOMANI, PER FAVORE.»"],
      prove: [
        {
          tipo: "completa",
          domanda: "SCEGLI LA PAROLA GIUSTA.",
          frase: "IL BILOCALE È AL TERZO PIANO ___ ASCENSORE: NON FAI LE SCALE!",
          icona: "🛗",
          risposte: ["CON", "SENZA", "PER"],
          correct: 0,
          aiuto: "NON FAI LE SCALE: L’ASCENSORE C’È O NON C’È?",
          spiega: "CON ASCENSORE = L’ASCENSORE C’È. SENZA ASCENSORE = DEVI FARE LE SCALE."
        },
        {
          tipo: "completa",
          domanda: "SCEGLI LA PAROLA GIUSTA.",
          frase: "MARYAM PAGA 450 EURO ___ MESE.",
          icona: "📅",
          risposte: ["AL", "IN", "CON"],
          correct: 0,
          aiuto: "SI DICE: AL PIANO, AL MESE.",
          spiega: "450 EURO AL MESE. RICORDA: IN CENTRO, AL 3° PIANO, AL MESE."
        },
        {
          tipo: "completa",
          domanda: "MARYAM CHIEDE AL PROPRIETARIO. COMPLETA CON «POTERE».",
          frase: "MARYAM: «___ VEDERE LA CASA DOMANI?»",
          icona: "👀",
          risposte: ["POSSO", "PUÒ", "DEVO"],
          correct: 0,
          aiuto: "PARLA MARYAM: IO… IO POSSO, LEI PUÒ.",
          spiega: "IO POSSO, TU PUOI, LEI PUÒ. «POSSO VEDERE LA CASA?» = CHIEDO IL PERMESSO."
        },
        {
          tipo: "completa",
          domanda: "COMPLETA CON «DOVERE».",
          frase: "PER AFFITTARE LA CASA, MARYAM ___ PAGARE DUE MESI DI CAUZIONE.",
          icona: "💰",
          risposte: ["DEVE", "DEVO", "PUÒ"],
          correct: 0,
          aiuto: "MARYAM = LEI. IO DEVO, LEI…",
          spiega: "IO DEVO, TU DEVI, LEI DEVE. È OBBLIGATORIO: DEVE PAGARE."
        },
        {
          tipo: "scelta",
          domanda: "MARYAM SCRIVE ALLA SIGNORA ROSA. QUALE FRASE È PIÙ GENTILE?",
          icona: "🌸",
          risposte: [
            { t: "«VORREI UN APPUNTAMENTO, PER FAVORE.»", i: "😊" },
            { t: "«VOGLIO UN APPUNTAMENTO.»", i: "😐" },
            { t: "«DAMMI UN APPUNTAMENTO.»", i: "😠" }
          ],
          correct: 0,
          aiuto: "CON UNA PERSONA CHE NON CONOSCI DICI «VORREI…», NON «VOGLIO».",
          spiega: "«VORREI» È GENTILE. ANCHE «È POSSIBILE…?» È GENTILE."
        },
        {
          tipo: "ordine",
          domanda: "METTI IN ORDINE IL MESSAGGIO DI MARYAM.",
          items: [
            "BUONGIORNO,",
            "SCRIVO PER L’ANNUNCIO DEL BILOCALE A SAN PASQUALE.",
            "SONO MARYAM, HO UN LAVORO A TEMPO PIENO.",
            "LA CASA È ANCORA DISPONIBILE? È POSSIBILE VEDERLA?",
            "GRAZIE E CORDIALI SALUTI, MARYAM."
          ],
          aiuto: "PRIMA IL SALUTO, POI PERCHÉ SCRIVI, POI CHI SEI, POI LA DOMANDA. ALLA FINE I SALUTI.",
          spiega: "SALUTO → ANNUNCIO → CHI SONO → DOMANDA → SALUTI E NOME."
        }
      ]
    },

    {
      id: "telefonata",
      titolo: "LA TELEFONATA",
      icona: "📞",
      lettera: "I",
      chi: "serena",
      lezione: { titolo: "CERCARE CASA · ESERCIZI", link: "cercare-casa/esercizi.html" },
      storia: [
        ["serena", "OGGI TELEFONI ALLA SIGNORA ROSA. PROVIAMO PRIMA INSIEME?"],
        ["maryam", "SÌ, GRAZIE! AL TELEFONO SONO SEMPRE AGITATA."],
        ["rosa", "PRONTO, BUONGIORNO!"]
      ],
      fine: ["rosa", "LA CASA TI PIACE, MARYAM? BENE! SABATO FIRMIAMO IL CONTRATTO."],
      prove: [
        {
          tipo: "completa",
          domanda: "MARYAM COMINCIA LA TELEFONATA. COMPLETA.",
          frase: "MARYAM: «BUONGIORNO. CHIAMO PER L’___ DEL BILOCALE A SAN PASQUALE.»",
          icona: "📞",
          risposte: ["ANNUNCIO", "AFFITTO", "ASCENSORE"],
          correct: 0,
          aiuto: "MARYAM HA LETTO LA CASA SU INTERNET, SU IDEALISTA.",
          spiega: "«CHIAMO PER L’ANNUNCIO…» = TELEFONO PERCHÉ HO LETTO IL TUO ANNUNCIO."
        },
        {
          tipo: "completa",
          domanda: "MARYAM CHIEDE DELLE SPESE. COMPLETA.",
          frase: "MARYAM: «LE SPESE SONO ___?» ROSA: «SÌ, 450 € CON TUTTO.»",
          icona: "💶",
          risposte: ["INCLUSE", "DISPONIBILI", "ARREDATE"],
          correct: 0,
          aiuto: "«CON TUTTO» = LE SPESE SONO GIÀ NEL PREZZO.",
          spiega: "SPESE INCLUSE = NEL PREZZO C’È GIÀ TUTTO."
        },
        {
          tipo: "completa",
          domanda: "MARYAM CHIEDE LA VISITA CON GENTILEZZA. COMPLETA.",
          frase: "MARYAM: «È ___ VEDERE LA CASA GIOVEDÌ POMERIGGIO?»",
          icona: "🗓️",
          risposte: ["POSSIBILE", "DISPONIBILE", "LIBERO"],
          correct: 0,
          aiuto: "«POSSO VEDERE…?» CON GENTILEZZA DIVENTA «È … VEDERE…?»",
          spiega: "«È POSSIBILE VEDERE LA CASA?» È UNA DOMANDA GENTILE."
        },
        {
          tipo: "ordine",
          domanda: "METTI IN ORDINE LA TELEFONATA.",
          items: [
            "🙋‍♀️ PRONTO, BUONGIORNO. CHIAMO PER L’ANNUNCIO.",
            "👵 BUONGIORNO. SÌ, MI DICA.",
            "🙋‍♀️ LA CASA È ANCORA LIBERA?",
            "👵 SÌ, È ANCORA LIBERA.",
            "🙋‍♀️ È POSSIBILE VEDERLA GIOVEDÌ?",
            "👵 CERTO, GIOVEDÌ ALLE 17 VA BENE."
          ],
          aiuto: "🙋‍♀️ = MARYAM, 👵 = ROSA. MARYAM FA UNA DOMANDA, ROSA RISPONDE.",
          spiega: "SALUTO → «MI DICA» → DOMANDA → RISPOSTA → APPUNTAMENTO."
        },
        {
          tipo: "vf",
          domanda: "ROSA DICE: «GIOVEDÌ ALLE 17 VA BENE.» MARYAM VA A VEDERE LA CASA GIOVEDÌ MATTINA.",
          icona: "🕔",
          correct: false,
          aiuto: "LE 17 SONO LE CINQUE. È MATTINA O POMERIGGIO?",
          spiega: "FALSO. ALLE 17 = ALLE CINQUE DEL POMERIGGIO."
        },
        {
          tipo: "scelta",
          domanda: "LA TELEFONATA FINISCE. CHE COSA DICE MARYAM?",
          icona: "👋",
          risposte: [
            { t: "«GRAZIE MILLE, ALLORA A GIOVEDÌ!»", i: "😊" },
            { t: "«PRONTO, CHI PARLA?»", i: "📞" },
            { t: "«SCRIVO PER L’ANNUNCIO.»", i: "✉️" }
          ],
          correct: 0,
          aiuto: "ALLA FINE RINGRAZI E SALUTI.",
          spiega: "«GRAZIE MILLE, ALLORA A GIOVEDÌ. BUONA GIORNATA!»"
        }
      ]
    }
  ]
};
