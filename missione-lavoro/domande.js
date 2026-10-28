// Contenuti del gioco «Missione lavoro».
// Tutti i testi visibili sono scritti in MAIUSCOLO.
// Per cambiare una domanda basta modificare questo file.
//
// Tipi di prova:
//   scelta  – scegli una risposta (correct = indice della risposta giusta)
//   vf      – vero o falso (correct = true / false)
//   completa – completa la frase: «___» nel testo viene riempito
//   collega – collega a sinistra e a destra (coppie nell'ordine giusto)
//   ordine  – tocca le azioni nell'ordine giusto (items nell'ordine giusto)
//   errore  – tocca la riga sbagliata di un documento (correct = indice della riga)
//
// Le risposte vengono mescolate quando il gioco parte.

window.MISSIONE = {
  titolo: "MISSIONE LAVORO",
  sottotitolo: "APRI LE PORTE DEL TUO FUTURO!",
  parolaSegreta: "LAVORO",
  sito: "https://italianol2sai.github.io/",

  stanze: [
    {
      id: "lavori",
      titolo: "CHE LAVORO FAI?",
      icona: "👷",
      lettera: "L",
      lezione: { titolo: "CHE LAVORO FAI?", link: "che-lavoro-fai/" },
      rosa: "QUI CI SONO TANTI LAVORI. TU CONOSCI I NOMI DEI LAVORI?",
      prove: [
        {
          tipo: "scelta",
          domanda: "CHI RIPARA LA MACCHINA?",
          icona: "🚗",
          risposte: [
            { t: "IL MECCANICO", i: "🔧" },
            { t: "LA SARTA", i: "🧵" },
            { t: "IL POSTINO", i: "✉️" }
          ],
          correct: 0,
          aiuto: "LAVORA IN OFFICINA.",
          spiega: "IL MECCANICO RIPARA LA MACCHINA."
        },
        {
          tipo: "collega",
          domanda: "DOVE LAVORA? COLLEGA.",
          coppie: [
            ["💉 L’INFERMIERA", "🏥 IN OSPEDALE"],
            ["🏭 L’OPERAIO", "⚙️ IN FABBRICA"],
            ["🍽️ IL CAMERIERE", "🍝 AL RISTORANTE"]
          ],
          aiuto: "TOCCA UNA PERSONA. POI TOCCA IL POSTO.",
          spiega: "L’INFERMIERA LAVORA IN OSPEDALE."
        },
        {
          tipo: "completa",
          domanda: "COMPLETA LA FRASE.",
          frase: "OMAR: «IO ___ IL CUOCO.»",
          icona: "🧑‍🍳",
          risposte: ["FACCIO", "FAI", "FANNO"],
          correct: 0,
          aiuto: "IO FACCIO, TU FAI, LORO FANNO.",
          spiega: "IO FACCIO IL CUOCO."
        },
        {
          tipo: "scelta",
          domanda: "LAVORO 8 ORE AL GIORNO, 40 ORE ALLA SETTIMANA. CHE ORARIO È?",
          icona: "🕗",
          risposte: [
            { t: "A TEMPO PIENO", i: "🕗" },
            { t: "PART-TIME", i: "🕓" },
            { t: "GIORNO LIBERO", i: "🛋️" }
          ],
          correct: 0,
          aiuto: "PART-TIME = MENO ORE.",
          spiega: "TEMPO PIENO: 8 ORE AL GIORNO, 40 ORE ALLA SETTIMANA."
        }
      ]
    },

    {
      id: "documenti",
      titolo: "I MIEI DOCUMENTI",
      icona: "🪪",
      lettera: "A",
      lezione: { titolo: "CERCO LAVORO A BARI E IN PUGLIA", link: "cercare-lavoro/" },
      rosa: "PER LAVORARE IN ITALIA SERVONO ALCUNI DOCUMENTI. LI CONOSCI?",
      prove: [
        {
          tipo: "scelta",
          domanda: "IL DOCUMENTO PER STARE IN ITALIA IN REGOLA È…",
          icona: "🗂️",
          risposte: [
            { t: "IL PERMESSO DI SOGGIORNO", i: "🪪" },
            { t: "IL CURRICULUM", i: "📄" },
            { t: "IL BIGLIETTO DELL’AUTOBUS", i: "🎫" }
          ],
          correct: 0,
          aiuto: "È UN DOCUMENTO CON LA TUA FOTO.",
          spiega: "IL PERMESSO DI SOGGIORNO SERVE PER STARE IN ITALIA IN REGOLA."
        },
        {
          tipo: "scelta",
          domanda: "IL TUO NUMERO PERSONALE IN ITALIA È…",
          icona: "🔑",
          risposte: [
            { t: "IL CODICE FISCALE", i: "🔑" },
            { t: "IL NUMERO DI SCARPE", i: "👟" },
            { t: "IL NUMERO DELL’AUTOBUS", i: "🚌" }
          ],
          correct: 0,
          aiuto: "IL CONTRATTO DI LAVORO È REGISTRATO CON QUESTO NUMERO.",
          spiega: "IL CODICE FISCALE È IL TUO NUMERO PERSONALE."
        },
        {
          tipo: "scelta",
          domanda: "PER RICEVERE LO STIPENDIO SERVE…",
          icona: "💶",
          risposte: [
            { t: "UN CONTO IN BANCA CON L’IBAN", i: "🏦" },
            { t: "UNA BICICLETTA", i: "🚲" },
            { t: "UN BIGLIETTO DEL TRENO", i: "🚆" }
          ],
          correct: 0,
          aiuto: "I SOLDI ARRIVANO IN BANCA.",
          spiega: "CON L’IBAN RICEVI LO STIPENDIO SUL CONTO."
        },
        {
          tipo: "vf",
          domanda: "LAVORO IN NERO: SE MI FACCIO MALE, SONO PAGATO.",
          icona: "🤕",
          correct: false,
          aiuto: "NEL LAVORO IN NERO NON C’È UN CONTRATTO.",
          spiega: "FALSO. NEL LAVORO IN NERO, SE TI FAI MALE, NON SEI PAGATO."
        },
        {
          tipo: "scelta",
          domanda: "PRIMA DI COMINCIARE A LAVORARE, CHE COSA CHIEDI?",
          icona: "✍️",
          risposte: [
            { t: "UN CONTRATTO SCRITTO", i: "📄" },
            { t: "UN CAFFÈ", i: "☕" },
            { t: "NIENTE", i: "🤐" }
          ],
          correct: 0,
          aiuto: "CON IL LAVORO REGOLARE HAI UN DOCUMENTO.",
          spiega: "CHIEDI SEMPRE UN CONTRATTO SCRITTO PRIMA DI COMINCIARE."
        }
      ]
    },

    {
      id: "cercare",
      titolo: "CERCO LAVORO",
      icona: "🔍",
      lettera: "V",
      lezione: { titolo: "CERCO LAVORO A BARI E IN PUGLIA", link: "cercare-lavoro/" },
      rosa: "ADESSO CERCHI LAVORO. DOVE CERCHI? CHE COSA DICI?",
      prove: [
        {
          tipo: "vf",
          domanda: "IL CENTRO PER L’IMPIEGO È GRATIS.",
          icona: "🏢",
          correct: true,
          aiuto: "È UN UFFICIO PUBBLICO.",
          spiega: "VERO. IL CENTRO PER L’IMPIEGO È UN UFFICIO PUBBLICO. È GRATIS."
        },
        {
          tipo: "scelta",
          domanda: "LEGGI L’ANNUNCIO. QUANDO È IL LAVORO?",
          documento: {
            titolo: "📋 ANNUNCIO",
            righe: [
              "UN RISTORANTE CERCA UN AIUTO CUOCO.",
              "📍 LUOGO: BARI.",
              "⏰ ORARIO: MATTINA."
            ]
          },
          risposte: [
            { t: "LA MATTINA", i: "🌅" },
            { t: "LA SERA", i: "🌆" },
            { t: "LA NOTTE", i: "🌙" }
          ],
          correct: 0,
          aiuto: "GUARDA L’OROLOGIO ⏰.",
          spiega: "ORARIO: MATTINA."
        },
        {
          tipo: "scelta",
          domanda: "VUOI CANDIDARTI. CHE COSA FAI?",
          documento: {
            titolo: "📋 ANNUNCIO",
            righe: [
              "UN RISTORANTE CERCA UN AIUTO CUOCO.",
              "📍 LUOGO: BARI.",
              "⏰ ORARIO: MATTINA."
            ]
          },
          risposte: [
            { t: "LEGGO LE INFORMAZIONI E SEGUO LE ISTRUZIONI PER CANDIDARMI.", i: "📨" },
            { t: "BUTTO VIA L’ANNUNCIO.", i: "🗑️" },
            { t: "VADO AL MARE.", i: "🏖️" }
          ],
          correct: 0,
          aiuto: "CANDIDARSI = MANDARE IL CV PER UN LAVORO.",
          spiega: "LA CANDIDATURA: MANDO IL CV PER UN LAVORO."
        },
        {
          tipo: "ordine",
          domanda: "L’APP «LAVORO PER TE PUGLIA». METTI IN ORDINE.",
          items: [
            "📲 SCARICO L’APP",
            "📄 METTO IL MIO CV",
            "✅ TOCCO «CANDIDATI»"
          ],
          aiuto: "PRIMA DEVI AVERE L’APP SUL TELEFONO.",
          spiega: "SCARICO L’APP, METTO IL CV, TOCCO «CANDIDATI»."
        },
        {
          tipo: "scelta",
          domanda: "ENTRI IN UN NEGOZIO. VUOI LAVORARE LÌ. CHE COSA DICI?",
          icona: "🛍️",
          risposte: [
            { t: "BUONGIORNO! CERCATE PERSONALE?", i: "🙂" },
            { t: "DAMMI UN LAVORO!", i: "😠" },
            { t: "CIAO BELLO, CHE VUOI?", i: "😏" }
          ],
          correct: 0,
          aiuto: "SALUTA E PARLA CON EDUCAZIONE.",
          spiega: "«BUONGIORNO! CERCATE PERSONALE? HO IL MIO CV.»"
        }
      ]
    },

    {
      id: "curriculum",
      titolo: "IL MIO CURRICULUM",
      icona: "📄",
      lettera: "O",
      lezione: { titolo: "IL CURRICULUM VITAE", link: "curriculum/" },
      rosa: "PER CERCARE LAVORO SERVE UN CURRICULUM. PREPARIAMO IL TUO!",
      prove: [
        {
          tipo: "scelta",
          domanda: "CHE COSA È UN CURRICULUM?",
          icona: "📄",
          risposte: [
            { t: "UN DOCUMENTO CON LE MIE INFORMAZIONI E LE MIE ESPERIENZE", i: "📄" },
            { t: "UN CONTRATTO DI AFFITTO", i: "🏠" },
            { t: "UN BIGLIETTO DELL’AUTOBUS", i: "🎫" }
          ],
          correct: 0,
          aiuto: "LO DAI AL DATORE DI LAVORO.",
          spiega: "IL CURRICULUM PRESENTA LE TUE INFORMAZIONI E LE TUE ESPERIENZE."
        },
        {
          tipo: "collega",
          domanda: "COLLEGA L’IMMAGINE E LA PAROLA.",
          coppie: [
            ["📞", "IL TELEFONO"],
            ["📧", "L’EMAIL"],
            ["💼", "L’ESPERIENZA"],
            ["⭐", "LE COMPETENZE"]
          ],
          aiuto: "💼 = DOVE HO LAVORATO. ⭐ = COSA SO FARE.",
          spiega: "L’ESPERIENZA = DOVE HO LAVORATO. LE COMPETENZE = COSA SO FARE."
        },
        {
          tipo: "errore",
          domanda: "C’È UN ERRORE NEL CV DI JOHN. TOCCA LA RIGA SBAGLIATA.",
          documento: { titolo: "📄 CURRICULUM VITAE" },
          righe: [
            "👤 NOME E COGNOME: JOHN OKAFOR",
            "🎂 DATA DI NASCITA: 12/05/1999",
            "📧 EMAIL: SUPERMARIO99@…",
            "🗣️ LINGUE: INGLESE, ITALIANO A1"
          ],
          correct: 2,
          aiuto: "GUARDA L’EMAIL. È SERIA?",
          spiega: "NEL CV USA UN’EMAIL SERIA: NOME.COGNOME@…"
        },
        {
          tipo: "scelta",
          domanda: "VUOI METTERE UNA FOTO NEL CV. QUALE SCEGLI?",
          icona: "📷",
          risposte: [
            { t: "UNA FOTO FORMALE CON VESTITI PULITI", i: "👔" },
            { t: "UN SELFIE CON GLI OCCHIALI DA SOLE", i: "😎" },
            { t: "UNA FOTO AL MARE", i: "🏖️" }
          ],
          correct: 0,
          aiuto: "IL CV È IL TUO BIGLIETTO DA VISITA.",
          spiega: "FOTO FORMALE: VESTITI PULITI, SFONDO BIANCO."
        },
        {
          tipo: "completa",
          domanda: "COMPLETA LA FRASE PER IL CV.",
          frase: "SO ___ : HO LA PATENTE B.",
          icona: "🚗",
          risposte: ["GUIDARE", "CUCIRE", "CUCINARE"],
          correct: 0,
          aiuto: "LA PATENTE SERVE PER LA MACCHINA.",
          spiega: "SO GUIDARE: HO LA PATENTE B."
        }
      ]
    },

    {
      id: "colloquio",
      titolo: "IL COLLOQUIO",
      icona: "🤝",
      lettera: "R",
      lezione: { titolo: "IL COLLOQUIO E IL CONTRATTO", link: "colloquio-contratti/" },
      rosa: "UN’AZIENDA TI CHIAMA PER UN COLLOQUIO. SEI PRONTO? SEI PRONTA?",
      prove: [
        {
          tipo: "scelta",
          domanda: "CHE COSA PORTI AL COLLOQUIO?",
          icona: "🎒",
          risposte: [
            { t: "IL CV STAMPATO E I DOCUMENTI", i: "📋" },
            { t: "IL PALLONE", i: "⚽" },
            { t: "NIENTE", i: "🤷" }
          ],
          correct: 0,
          aiuto: "IL DATORE DI LAVORO VUOLE LEGGERE LE TUE INFORMAZIONI.",
          spiega: "PORTA IL CV STAMPATO E I DOCUMENTI."
        },
        {
          tipo: "scelta",
          domanda: "IL COLLOQUIO È ALLE 9:00. A CHE ORA ARRIVI?",
          icona: "⏰",
          risposte: [
            { t: "ALLE 8:50", i: "🕘" },
            { t: "ALLE 9:30", i: "🕤" },
            { t: "ALLE 10:00", i: "🕙" }
          ],
          correct: 0,
          aiuto: "ARRIVA UN PO’ PRIMA.",
          spiega: "ARRIVA PUNTUALE: 5–10 MINUTI PRIMA."
        },
        {
          tipo: "scelta",
          domanda: "SEI A UN COLLOQUIO DI LAVORO. COME SALUTI?",
          icona: "🤝",
          risposte: [
            { t: "BUONGIORNO.", i: "🙂" },
            { t: "CIAO BELLO, CHE VUOI?", i: "😏" },
            { t: "NON DICO NIENTE.", i: "😶" }
          ],
          correct: 0,
          aiuto: "È UN SALUTO GENTILE E FORMALE.",
          spiega: "SORRIDI, DICI «BUONGIORNO» E DAI LA MANO."
        },
        {
          tipo: "scelta",
          domanda: "NON CAPISCI UNA DOMANDA. CHE COSA DICI?",
          icona: "❓",
          risposte: [
            { t: "PUÒ RIPETERE, PER FAVORE?", i: "🙋" },
            { t: "VADO VIA.", i: "🚪" },
            { t: "NON DICO NIENTE.", i: "😶" }
          ],
          correct: 0,
          aiuto: "CHIEDI DI DIRE ANCORA LA DOMANDA.",
          spiega: "SE NON CAPISCI, DICI: «PUÒ RIPETERE, PER FAVORE?»"
        },
        {
          tipo: "vf",
          domanda: "AL COLLOQUIO IL TELEFONO È ACCESO.",
          icona: "📱",
          correct: false,
          aiuto: "IL TELEFONO PUÒ SUONARE DURANTE IL COLLOQUIO.",
          spiega: "FALSO. AL COLLOQUIO SPEGNI IL TELEFONO."
        }
      ]
    },

    {
      id: "contratto",
      titolo: "CONTRATTO E BUSTA PAGA",
      icona: "✍️",
      lettera: "O",
      lezione: { titolo: "LA BUSTA PAGA", link: "busta-paga/" },
      lezione2: { titolo: "IL COLLOQUIO E IL CONTRATTO", link: "colloquio-contratti/" },
      rosa: "OTTIMO! IL COLLOQUIO È ANDATO BENE. ADESSO C’È IL CONTRATTO.",
      prove: [
        {
          tipo: "scelta",
          domanda: "PRIMA DI FIRMARE IL CONTRATTO, CHE COSA FAI?",
          icona: "✍️",
          risposte: [
            { t: "LEGGO IL CONTRATTO. SE NON CAPISCO, CHIEDO AIUTO.", i: "📖" },
            { t: "FIRMO SUBITO E NON LEGGO.", i: "🙈" },
            { t: "BUTTO VIA IL CONTRATTO.", i: "🗑️" }
          ],
          correct: 0,
          aiuto: "IL CONTRATTO È UN DOCUMENTO IMPORTANTE.",
          spiega: "PRIMA DI FIRMARE, LEGGI IL CONTRATTO!"
        },
        {
          tipo: "vf",
          domanda: "NON CAPISCI IL CONTRATTO. IL SINDACATO TI AIUTA GRATIS.",
          icona: "🤝",
          correct: true,
          aiuto: "CGIL, CISL, UIL SONO SINDACATI.",
          spiega: "VERO. IL SINDACATO (CGIL, CISL, UIL) TI AIUTA GRATIS."
        },
        {
          tipo: "collega",
          domanda: "I TUOI DIRITTI. COLLEGA.",
          coppie: [
            ["🌞 LE FERIE", "VACANZA PAGATA"],
            ["🤒 LA MALATTIA", "CERTIFICATO DEL MEDICO"],
            ["🦺 LA SICUREZZA", "GUANTI, CASCO, SCARPE"]
          ],
          aiuto: "🌞 = VACANZA. 🤒 = SONO MALATO.",
          spiega: "QUESTI DIRITTI SONO PER TUTTI I LAVORATORI, ANCHE PER GLI STRANIERI."
        },
        {
          tipo: "scelta",
          domanda: "GUARDA LA BUSTA PAGA. QUANTI SOLDI RICEVI SUL CONTO?",
          documento: {
            titolo: "💳 BUSTA PAGA · MAGGIO",
            tabella: [
              ["📈 LORDO", "1.490,64 €"],
              ["✂️ TASSE E INPS", "− 247,89 €"],
              ["📉 NETTO", "1.242,75 €"]
            ]
          },
          risposte: [
            { t: "1.242,75 €", i: "📉" },
            { t: "1.490,64 €", i: "📈" },
            { t: "247,89 €", i: "✂️" }
          ],
          correct: 0,
          aiuto: "I SOLDI VERI CHE RICEVI SONO IL NETTO.",
          spiega: "IL NETTO È PIÙ BASSO DEL LORDO. È NORMALE!"
        },
        {
          tipo: "scelta",
          domanda: "LA BUSTA PAGA: CHE COSA FAI?",
          icona: "🗄️",
          risposte: [
            { t: "LA CONSERVO SEMPRE", i: "🗄️" },
            { t: "LA BUTTO VIA", i: "🗑️" },
            { t: "LA REGALO A UN AMICO", i: "🎁" }
          ],
          correct: 0,
          aiuto: "SERVE ANCHE PER IL PERMESSO DI SOGGIORNO.",
          spiega: "CONSERVALA: SERVE PER IL PERMESSO DI SOGGIORNO E PER AFFITTARE UNA CASA."
        }
      ]
    }
  ]
};
