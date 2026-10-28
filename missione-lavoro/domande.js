// Contenuti del gioco «Missione lavoro»: storia, stanze e prove.
// Tutti i testi visibili sono scritti in MAIUSCOLO.
// Per cambiare una domanda basta modificare questo file.
//
// Le battute della storia sono coppie [chi parla, testo]; chi parla è una
// chiave di persone.js (silvia, francesco, giulio, mohammad).
//
// Tipi di prova:
//   scelta   – scegli una risposta (correct = indice della risposta giusta)
//   vf       – vero o falso (correct = true / false)
//   completa – completa la frase: «___» nel testo viene riempito
//   collega  – collega a sinistra e a destra (coppie nell'ordine giusto)
//   ordine   – tocca le azioni nell'ordine giusto (items nell'ordine giusto)
//   errore   – tocca la riga sbagliata di un documento (correct = indice della riga)
//
// Le risposte vengono mescolate quando il gioco parte.

window.MISSIONE = {
  titolo: "MISSIONE LAVORO",
  sottotitolo: "APRI LE PORTE DEL TUO FUTURO!",
  parolaSegreta: "ASSUNTO",
  sito: "https://italianol2sai.github.io/",

  intro: [
    ["mohammad", "CIAO! MI CHIAMO MOHAMMAD. HO 19 ANNI. SONO IN ITALIA DA DUE ANNI. ABITO A BARI."],
    ["mohammad", "SONO NEL PROGETTO SAI DI BARI. LA MATTINA STUDIO ITALIANO. ADESSO VOGLIO LAVORARE. MA NON SO DA DOVE COMINCIARE…"],
    ["silvia", "IO SONO SILVIA. TU PUOI AIUTARE MOHAMMAD!"],
    ["silvia", "IO, FRANCESCO E GIULIO LAVORIAMO PER ETNIE, NEL PROGETTO SAI DI BARI. SIAMO OPERATORI DI ORIENTAMENTO AL LAVORO."],
    ["silvia", "CI SONO 7 PORTE. DIETRO OGNI PORTA C’È UNA LETTERA. CON LE 7 LETTERE SCOPRI COME FINISCE LA STORIA!"]
  ],

  finale: [
    ["mohammad", "È IL 31 MAGGIO. OGGI FINISCE IL MIO CONTRATTO. ANNA MI ASPETTA IN UFFICIO: HA UNA NOTIZIA PER ME…"],
    ["giulio", "CORAGGIO, MOHAMMAD! HAI LAVORATO BENE."],
    ["silvia", "CHE COSA DICE ANNA? SCRIVI LA PAROLA SEGRETA CON LE 7 LETTERE DEL TUO BADGE."]
  ],
  vittoria: "ANNA DICE: «MOHAMMAD, LAVORI BENE. ECCO UN CONTRATTO NUOVO: SEI ASSUNTO!»",

  stanze: [
    {
      id: "lavori",
      titolo: "CHE LAVORO FAI?",
      icona: "👷",
      lettera: "A",
      chi: "francesco",
      lezione: { titolo: "CHE LAVORO FAI?", link: "che-lavoro-fai/" },
      storia: [
        ["francesco", "MOHAMMAD, CHE LAVORO VUOI FARE?"],
        ["mohammad", "NON LO SO. CONOSCO POCHI NOMI DI LAVORI."],
        ["francesco", "ALLORA FACCIAMO UN GIRO IN CITTÀ. GUARDA BENE!"]
      ],
      fine: ["mohammad", "ADESSO CONOSCO TANTI LAVORI. IO VOGLIO LAVORARE IN CUCINA!"],
      prove: [
        {
          tipo: "scelta",
          domanda: "IN OFFICINA UN UOMO RIPARA LA MACCHINA. CHE LAVORO FA?",
          icona: "🚗",
          risposte: [
            { t: "IL MECCANICO", i: "🔧" },
            { t: "IL MURATORE", i: "🧱" },
            { t: "L’AUTISTA", i: "🚌" }
          ],
          correct: 0,
          aiuto: "L’AUTISTA GUIDA. IL MURATORE COSTRUISCE LE CASE.",
          spiega: "IL MECCANICO RIPARA LA MACCHINA IN OFFICINA."
        },
        {
          tipo: "collega",
          domanda: "DOVE LAVORANO? COLLEGA.",
          coppie: [
            ["💉 L’INFERMIERA", "🏥 IN OSPEDALE"],
            ["🏭 L’OPERAIO", "⚙️ IN FABBRICA"],
            ["🍽️ IL CAMERIERE", "🍝 AL RISTORANTE"],
            ["🧱 IL MURATORE", "🏗️ IN CANTIERE"]
          ],
          aiuto: "TOCCA UNA PERSONA. POI TOCCA IL POSTO.",
          spiega: "OGNI LAVORO HA IL SUO POSTO: OSPEDALE, FABBRICA, RISTORANTE, CANTIERE."
        },
        {
          tipo: "completa",
          domanda: "OMAR, UN AMICO DI MOHAMMAD, PARLA DEL SUO LAVORO. COMPLETA.",
          frase: "OMAR: «IO ___ IL CUOCO IN UN RISTORANTE.»",
          icona: "🧑‍🍳",
          risposte: ["FACCIO", "FA", "FANNO"],
          correct: 0,
          aiuto: "IO FACCIO, LUI FA, LORO FANNO.",
          spiega: "IO FACCIO IL CUOCO. LUI FA IL CUOCO."
        },
        {
          tipo: "scelta",
          domanda: "OMAR LAVORA DALLE 8 ALLE 16, DAL LUNEDÌ AL VENERDÌ. CHE ORARIO HA?",
          icona: "🕗",
          risposte: [
            { t: "A TEMPO PIENO", i: "🕗" },
            { t: "PART-TIME", i: "🕓" },
            { t: "SU TURNI", i: "🔄" }
          ],
          correct: 0,
          aiuto: "CONTA LE ORE: 8 ORE AL GIORNO, 5 GIORNI.",
          spiega: "8 ORE AL GIORNO, 40 ORE ALLA SETTIMANA = TEMPO PIENO."
        },
        {
          tipo: "completa",
          domanda: "MOHAMMAD PARLA DI SÉ. COMPLETA.",
          frase: "MOHAMMAD: «ADESSO NON HO UN LAVORO. SONO ___.»",
          icona: "🔍",
          risposte: ["DISOCCUPATO", "PENSIONATO", "IMPIEGATO"],
          correct: 0,
          aiuto: "IL PENSIONATO È ANZIANO E NON LAVORA PIÙ.",
          spiega: "DISOCCUPATO = NON HA UN LAVORO. CERCA LAVORO."
        }
      ]
    },

    {
      id: "documenti",
      titolo: "I MIEI DOCUMENTI",
      icona: "🪪",
      lettera: "S",
      chi: "francesco",
      lezione: { titolo: "CERCO LAVORO A BARI E IN PUGLIA", link: "cercare-lavoro/" },
      storia: [
        ["mohammad", "FRANCESCO, HO DECISO: VOGLIO LAVORARE IN CUCINA. ADESSO CHE COSA DEVO FARE?"],
        ["francesco", "BUONGIORNO, MOHAMMAD! PRIMA CONTROLLIAMO I DOCUMENTI."],
        ["francesco", "SENZA I DOCUMENTI GIUSTI, IL DATORE DI LAVORO NON PUÒ FARE IL CONTRATTO."]
      ],
      fine: ["francesco", "PERFETTO! MOHAMMAD HA TUTTI I DOCUMENTI. POSSIAMO CERCARE LAVORO."],
      prove: [
        {
          tipo: "scelta",
          domanda: "MOHAMMAD HA 19 ANNI. PUÒ LAVORARE IN ITALIA?",
          icona: "🎂",
          risposte: [
            { t: "SÌ: HA PIÙ DI 18 ANNI", i: "✅" },
            { t: "NO: DEVE AVERE 21 ANNI", i: "❌" },
            { t: "NO: DEVE AVERE 25 ANNI", i: "❌" }
          ],
          correct: 0,
          aiuto: "PER LAVORARE DEVI AVERE 18 ANNI.",
          spiega: "A 18 ANNI PUOI LAVORARE. MOHAMMAD HA 19 ANNI: VA BENE!"
        },
        {
          tipo: "scelta",
          domanda: "IL DATORE DI LAVORO REGISTRA IL CONTRATTO. QUALE NUMERO GLI SERVE?",
          icona: "✍️",
          risposte: [
            { t: "IL CODICE FISCALE", i: "🔑" },
            { t: "L’IBAN", i: "🏦" },
            { t: "IL NUMERO DI TELEFONO", i: "📞" }
          ],
          correct: 0,
          aiuto: "È IL TUO NUMERO PERSONALE IN ITALIA.",
          spiega: "IL CONTRATTO È REGISTRATO CON IL CODICE FISCALE."
        },
        {
          tipo: "scelta",
          domanda: "COME RICEVE LO STIPENDIO MOHAMMAD?",
          icona: "💶",
          risposte: [
            { t: "SUL SUO CONTO IN BANCA, CON L’IBAN", i: "🏦" },
            { t: "CON IL CODICE FISCALE", i: "🔑" },
            { t: "CON IL PERMESSO DI SOGGIORNO", i: "🪪" }
          ],
          correct: 0,
          aiuto: "I SOLDI ARRIVANO IN BANCA.",
          spiega: "CON L’IBAN LO STIPENDIO ARRIVA SUL CONTO IN BANCA."
        },
        {
          tipo: "vf",
          domanda: "UN AMICO DICE: «C’È UN LAVORO SENZA CONTRATTO.» SE MOHAMMAD SI FA MALE, È PROTETTO.",
          icona: "🤕",
          correct: false,
          aiuto: "SENZA CONTRATTO È LAVORO IN NERO.",
          spiega: "FALSO. NEL LAVORO IN NERO, SE TI FAI MALE, NON SEI PAGATO."
        },
        {
          tipo: "scelta",
          domanda: "MOHAMMAD DEVE RINNOVARE IL PERMESSO DI SOGGIORNO. QUALE LAVORO SERVE?",
          icona: "🗂️",
          risposte: [
            { t: "UN LAVORO REGOLARE, CON IL CONTRATTO", i: "📄" },
            { t: "UN LAVORO IN NERO", i: "🕶️" },
            { t: "TUTTI E DUE VANNO BENE", i: "🤷" }
          ],
          correct: 0,
          aiuto: "IL LAVORO IN NERO, PER LO STATO, NON ESISTE.",
          spiega: "IL LAVORO IN NERO NON SERVE PER RINNOVARE IL PERMESSO DI SOGGIORNO."
        }
      ]
    },

    {
      id: "cercare",
      titolo: "CERCO LAVORO",
      icona: "🔍",
      lettera: "S",
      chi: "francesco",
      lezione: { titolo: "CERCO LAVORO A BARI E IN PUGLIA", link: "cercare-lavoro/" },
      storia: [
        ["francesco", "ORA CERCHIAMO LAVORO. DOMANI ANDIAMO INSIEME AL CENTRO PER L’IMPIEGO."],
        ["mohammad", "ATTENZIONE: LA MATTINA IO VADO A SCUOLA DI ITALIANO!"],
        ["francesco", "VA BENE. CERCHIAMO UN LAVORO GIUSTO PER TE."]
      ],
      fine: ["mohammad", "HO MANDATO IL MIO CV AL RISTORANTE «IL PORTO». SPERIAMO…"],
      prove: [
        {
          tipo: "scelta",
          domanda: "MOHAMMAD VUOLE AIUTO PER CERCARE LAVORO E CORSI. DOVE VA? NON PAGA NIENTE.",
          icona: "🆓",
          risposte: [
            { t: "AL CENTRO PER L’IMPIEGO", i: "🏢" },
            { t: "IN BANCA", i: "🏦" },
            { t: "IN QUESTURA", i: "🚓" }
          ],
          correct: 0,
          aiuto: "È UN UFFICIO PUBBLICO PER IL LAVORO.",
          spiega: "IL CENTRO PER L’IMPIEGO È GRATIS. AIUTA A CERCARE LAVORO E CORSI."
        },
        {
          tipo: "scelta",
          domanda: "LA MATTINA MOHAMMAD VA A SCUOLA. QUALE ANNUNCIO VA BENE PER LUI?",
          icona: "📋",
          risposte: [
            { t: "RISTORANTE «IL PORTO» CERCA AIUTO CUOCO. ⏰ 16–23", i: "🍝" },
            { t: "BAR CERCA BARISTA. ⏰ 6–12", i: "☕" },
            { t: "SUPERMERCATO CERCA MAGAZZINIERE. ⏰ 7–13", i: "📦" }
          ],
          correct: 0,
          aiuto: "GUARDA L’ORARIO ⏰. LA MATTINA MOHAMMAD NON PUÒ.",
          spiega: "IL RISTORANTE CERCA UN AIUTO CUOCO IL POMERIGGIO E LA SERA."
        },
        {
          tipo: "scelta",
          domanda: "LEGGI L’ANNUNCIO. COME SI CANDIDA MOHAMMAD?",
          documento: {
            titolo: "📋 ANNUNCIO",
            righe: [
              "RISTORANTE «IL PORTO» – BARI",
              "CERCHIAMO AIUTO CUOCO.",
              "⏰ ORARIO: 16–23.",
              "📧 MANDA IL CV CON UN’EMAIL AL RISTORANTE."
            ]
          },
          risposte: [
            { t: "MANDA IL CV CON L’EMAIL", i: "📧" },
            { t: "TELEFONA ALLE 23", i: "📞" },
            { t: "VA AL RISTORANTE SENZA CV", i: "🚶" }
          ],
          correct: 0,
          aiuto: "GUARDA L’ULTIMA RIGA DELL’ANNUNCIO.",
          spiega: "SEGUI LE ISTRUZIONI DELL’ANNUNCIO: MANDA IL CV."
        },
        {
          tipo: "ordine",
          domanda: "FRANCESCO SPIEGA L’APP «LAVORO PER TE PUGLIA». METTI IN ORDINE.",
          items: [
            "📲 SCARICO L’APP",
            "📄 METTO IL MIO CV",
            "🔍 CERCO LE OFFERTE A BARI",
            "✅ TOCCO «CANDIDATI»"
          ],
          aiuto: "PRIMA DEVI AVERE L’APP SUL TELEFONO. ALLA FINE TI CANDIDI.",
          spiega: "SCARICO L’APP, METTO IL CV, CERCO, MI CANDIDO."
        },
        {
          tipo: "scelta",
          domanda: "MOHAMMAD ENTRA IN UN BAR CON IL SUO CV. CHE COSA DICE?",
          icona: "☕",
          risposte: [
            { t: "BUONGIORNO! CERCATE PERSONALE? HO IL MIO CV.", i: "🙂" },
            { t: "BUONGIORNO! UN CAFFÈ, PER FAVORE.", i: "☕" },
            { t: "BUONGIORNO! QUANTO PAGATE?", i: "💶" }
          ],
          correct: 0,
          aiuto: "MOHAMMAD VUOLE LAVORARE, NON BERE UN CAFFÈ.",
          spiega: "«CERCATE PERSONALE?» È LA DOMANDA GIUSTA PER CHIEDERE LAVORO."
        }
      ]
    },

    {
      id: "curriculum",
      titolo: "IL MIO CURRICULUM",
      icona: "📄",
      lettera: "U",
      chi: "giulio",
      lezione: { titolo: "IL CURRICULUM VITAE", link: "curriculum/" },
      storia: [
        ["mohammad", "GIULIO, AIUTO! IL RISTORANTE VUOLE IL MIO CV, MA IO NON HO UN CV!"],
        ["giulio", "TRANQUILLO. LO SCRIVIAMO INSIEME, IN UFFICIO."],
        ["giulio", "MA ATTENZIONE: NEL TUO CV CI SONO ALCUNI ERRORI…"]
      ],
      fine: ["giulio", "ECCO IL CV DI MOHAMMAD: PULITO E CHIARO. È IL SUO BIGLIETTO DA VISITA!"],
      prove: [
        {
          tipo: "scelta",
          domanda: "IL DATORE DI LAVORO LEGGE IL CV. CHE COSA VUOLE SAPERE?",
          icona: "📄",
          risposte: [
            { t: "CHI SEI, DOVE HAI LAVORATO, CHE COSA SAI FARE", i: "📄" },
            { t: "QUANTI AMICI HAI E DOVE VAI IN VACANZA", i: "🏖️" },
            { t: "QUANTO PAGHI DI AFFITTO", i: "🏠" }
          ],
          correct: 0,
          aiuto: "NEL CV CI SONO LE INFORMAZIONI PER IL LAVORO.",
          spiega: "IL CV PRESENTA LE TUE INFORMAZIONI, LE ESPERIENZE E LE COMPETENZE."
        },
        {
          tipo: "collega",
          domanda: "COLLEGA L’IMMAGINE E LA PAROLA DEL CV.",
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
          domanda: "C’È UN ERRORE NEL CV DI MOHAMMAD. TOCCA LA RIGA SBAGLIATA.",
          documento: { titolo: "📄 CURRICULUM VITAE" },
          righe: [
            "👤 NOME E COGNOME: MOHAMMAD ALI",
            "🎂 DATA DI NASCITA: 12/05/2007",
            "📧 EMAIL: MOMO_BOMBER07@…",
            "🗣️ LINGUE: ITALIANO A1, INGLESE A2"
          ],
          correct: 2,
          aiuto: "UN DATORE DI LAVORO LEGGE QUESTA RIGA. È SERIA?",
          spiega: "NEL CV USA UN’EMAIL SERIA: NOME.COGNOME@…"
        },
        {
          tipo: "scelta",
          domanda: "MOHAMMAD NON HA ESPERIENZE DI LAVORO. CHE COSA SCRIVE NEL CV?",
          icona: "💼",
          risposte: [
            { t: "«NESSUNA ESPERIENZA LAVORATIVA»", i: "✍️" },
            { t: "NIENTE: LASCIA LO SPAZIO VUOTO", i: "⬜" },
            { t: "INVENTA UN LAVORO", i: "🤥" }
          ],
          correct: 0,
          aiuto: "NEL CV NON LASCI SPAZI VUOTI. E DICI SEMPRE LA VERITÀ.",
          spiega: "SE NON HAI ESPERIENZA SCRIVI «NESSUNA». NON DIRE BUGIE."
        },
        {
          tipo: "completa",
          domanda: "MOHAMMAD SCRIVE LE SUE COMPETENZE. COMPLETA.",
          frase: "SO ___ : AIUTO SEMPRE MIA MADRE IN CUCINA.",
          icona: "⭐",
          risposte: ["CUCINARE", "GUIDARE", "CUCIRE"],
          correct: 0,
          aiuto: "IN CUCINA SI…",
          spiega: "SO CUCINARE. È UNA COMPETENZA PERFETTA PER UN AIUTO CUOCO!"
        }
      ]
    },

    {
      id: "colloquio",
      titolo: "IL COLLOQUIO",
      icona: "🤝",
      lettera: "N",
      chi: "silvia",
      lezione: { titolo: "IL COLLOQUIO E IL CONTRATTO", link: "colloquio-contratti/" },
      storia: [
        ["mohammad", "📞 IL TELEFONO SUONA! È IL RISTORANTE «IL PORTO»: COLLOQUIO DOMANI ALLE 16:00!"],
        ["silvia", "«IL PORTO»? CONOSCO ANNA, LA TITOLARE. È SIMPATICA, MA SERIA."],
        ["silvia", "TI PREPARO IO. NON SBAGLIARE NIENTE!"]
      ],
      fine: ["silvia", "BRAVO, MOHAMMAD! ANNA HA DETTO: «È UN RAGAZZO SERIO.»"],
      prove: [
        {
          tipo: "scelta",
          domanda: "IL COLLOQUIO È ALLE 16:00. A CHE ORA ARRIVA MOHAMMAD?",
          icona: "⏰",
          risposte: [
            { t: "ALLE 15:50", i: "🕒" },
            { t: "ALLE 16:15", i: "🕓" },
            { t: "ALLE 14:00", i: "🕑" }
          ],
          correct: 0,
          aiuto: "NON IN RITARDO. MA NON DUE ORE PRIMA!",
          spiega: "ARRIVA PUNTUALE: 5–10 MINUTI PRIMA."
        },
        {
          tipo: "scelta",
          domanda: "CHE COSA METTE NELLO ZAINO MOHAMMAD?",
          icona: "🎒",
          risposte: [
            { t: "IL CV STAMPATO E I DOCUMENTI", i: "📋" },
            { t: "SOLO IL TELEFONO: IL CV È NELL’EMAIL", i: "📱" },
            { t: "NIENTE: ANNA HA GIÀ TUTTO", i: "🤷" }
          ],
          correct: 0,
          aiuto: "PORTA SEMPRE IL CV STAMPATO.",
          spiega: "PORTA IL CV STAMPATO (2 COPIE), IL PERMESSO DI SOGGIORNO E IL CODICE FISCALE."
        },
        {
          tipo: "scelta",
          domanda: "ANNA DICE: «BUONGIORNO. MI PARLI DI LEI.» CHE COSA RISPONDE MOHAMMAD?",
          icona: "🗣️",
          risposte: [
            { t: "MI CHIAMO MOHAMMAD, HO 19 ANNI. STUDIO ITALIANO E SO CUCINARE.", i: "🙂" },
            { t: "QUANTO È LO STIPENDIO?", i: "💶" },
            { t: "NON LO SO.", i: "😶" }
          ],
          correct: 0,
          aiuto: "ANNA VUOLE CONOSCERE MOHAMMAD.",
          spiega: "PARLA DI TE: NOME, ETÀ, STUDIO, COSA SAI FARE."
        },
        {
          tipo: "scelta",
          domanda: "ANNA PARLA VELOCE. MOHAMMAD NON CAPISCE. CHE COSA FA?",
          icona: "❓",
          risposte: [
            { t: "DICE: «PUÒ RIPETERE, PER FAVORE?»", i: "🙋" },
            { t: "DICE «SÌ, SÌ» MA NON CAPISCE", i: "😅" },
            { t: "GUARDA IL TELEFONO", i: "📱" }
          ],
          correct: 0,
          aiuto: "NON CAPIRE È NORMALE. PUOI CHIEDERE.",
          spiega: "SE NON CAPISCI, DICI: «PUÒ RIPETERE, PER FAVORE?»"
        },
        {
          tipo: "scelta",
          domanda: "ALLA FINE ANNA DICE: «HA DOMANDE?» CHE COSA CHIEDE MOHAMMAD?",
          icona: "🙋",
          risposte: [
            { t: "CHE TIPO DI CONTRATTO OFFRITE?", i: "📄" },
            { t: "POSSO ARRIVARE QUANDO VOGLIO?", i: "🕰️" },
            { t: "POSSO USARE IL TELEFONO IN CUCINA?", i: "📱" }
          ],
          correct: 0,
          aiuto: "È UNA DOMANDA SERIA SUL LAVORO.",
          spiega: "PUOI CHIEDERE: IL CONTRATTO, L’ORARIO, I TURNI, LO STIPENDIO."
        }
      ]
    },

    {
      id: "contratto",
      titolo: "IL CONTRATTO",
      icona: "✍️",
      lettera: "T",
      chi: "francesco",
      lezione: { titolo: "IL COLLOQUIO E IL CONTRATTO", link: "colloquio-contratti/" },
      storia: [
        ["silvia", "MOHAMMAD! ANNA HA CHIAMATO: TI VUOLE NELLA SUA CUCINA!"],
        ["mohammad", "C’È UN CONTRATTO DA FIRMARE. MA CI SONO TANTE PAROLE DIFFICILI…"],
        ["francesco", "ASPETTA! PRIMA DI FIRMARE, LEGGIAMO INSIEME."]
      ],
      fine: ["mohammad", "HO LETTO TUTTO E HO FIRMATO. DAL 1° NOVEMBRE LAVORO AL «PORTO»!"],
      prove: [
        {
          tipo: "scelta",
          domanda: "ANNA DICE: «FIRMI QUI.» MOHAMMAD NON CAPISCE TUTTO. CHE COSA FA?",
          icona: "✍️",
          risposte: [
            { t: "CHIEDE TEMPO PER LEGGERE E CHIEDE AIUTO", i: "📖" },
            { t: "FIRMA SUBITO: HA PAURA DI PERDERE IL LAVORO", i: "😰" },
            { t: "NON FIRMA E VA VIA", i: "🚪" }
          ],
          correct: 0,
          aiuto: "PRIMA DI FIRMARE, LEGGI SEMPRE.",
          spiega: "PRIMA DI FIRMARE, LEGGI IL CONTRATTO. SE NON CAPISCI, CHIEDI AIUTO."
        },
        {
          tipo: "scelta",
          domanda: "CHI AIUTA GRATIS A CAPIRE IL CONTRATTO?",
          icona: "🤝",
          risposte: [
            { t: "IL SINDACATO (CGIL, CISL, UIL)", i: "🤝" },
            { t: "LA BANCA", i: "🏦" },
            { t: "L’AGENZIA DI VIAGGI", i: "✈️" }
          ],
          correct: 0,
          aiuto: "CGIL, CISL E UIL AIUTANO I LAVORATORI.",
          spiega: "IL SINDACATO TI AIUTA GRATIS."
        },
        {
          tipo: "scelta",
          domanda: "LEGGI IL CONTRATTO. IL LAVORO FINISCE?",
          documento: {
            titolo: "📄 CONTRATTO DI LAVORO",
            righe: [
              "LAVORATORE: MOHAMMAD ALI",
              "MANSIONE: AIUTO CUOCO",
              "A TEMPO DETERMINATO",
              "📅 DAL 1/11 AL 31/5"
            ]
          },
          risposte: [
            { t: "SÌ: FINISCE IL 31 MAGGIO (POI PUÒ CONTINUARE)", i: "📅" },
            { t: "NO: NON FINISCE MAI", i: "♾️" },
            { t: "NON SI SA", i: "🤷" }
          ],
          correct: 0,
          aiuto: "TEMPO DETERMINATO = C’È UNA DATA DI FINE.",
          spiega: "IL CONTRATTO A TEMPO DETERMINATO HA UNA DATA DI FINE. POI FINISCE O SI RINNOVA."
        },
        {
          tipo: "collega",
          domanda: "I DIRITTI DI MOHAMMAD. COLLEGA.",
          coppie: [
            ["🌞 LE FERIE", "VACANZA PAGATA"],
            ["🤒 LA MALATTIA", "CERTIFICATO DEL MEDICO"],
            ["🦺 LA SICUREZZA", "GUANTI E SCARPE DI SICUREZZA"]
          ],
          aiuto: "🌞 = VACANZA. 🤒 = SONO MALATO.",
          spiega: "QUESTI DIRITTI SONO PER TUTTI I LAVORATORI, ANCHE PER GLI STRANIERI."
        }
      ]
    },

    {
      id: "busta-paga",
      titolo: "LA BUSTA PAGA",
      icona: "💶",
      lettera: "O",
      chi: "giulio",
      lezione: { titolo: "LA BUSTA PAGA", link: "busta-paga/" },
      storia: [
        ["mohammad", "È IL 30 NOVEMBRE. È ARRIVATA LA MIA PRIMA BUSTA PAGA!"],
        ["mohammad", "MA… C’È UN PROBLEMA. CI SONO DUE NUMERI DIVERSI! QUALE È IL MIO?"],
        ["giulio", "TRANQUILLO! TI SPIEGO IO."]
      ],
      fine: ["mohammad", "HO CAPITO TUTTO! E CONSERVO LA BUSTA PAGA IN UNA CARTELLA."],
      prove: [
        {
          tipo: "scelta",
          domanda: "QUANTI SOLDI ARRIVANO SUL CONTO DI MOHAMMAD?",
          documento: {
            titolo: "💳 BUSTA PAGA · NOVEMBRE · ESEMPIO",
            tabella: [
              ["📈 LORDO", "1.000,00 €"],
              ["✂️ TASSE E INPS", "− 150,00 €"],
              ["📉 NETTO", "850,00 €"]
            ]
          },
          risposte: [
            { t: "850,00 €", i: "📉" },
            { t: "1.000,00 €", i: "📈" },
            { t: "150,00 €", i: "✂️" }
          ],
          correct: 0,
          aiuto: "I SOLDI VERI CHE RICEVI SONO IL NETTO.",
          spiega: "IL NETTO SONO I SOLDI CHE ARRIVANO SUL CONTO."
        },
        {
          tipo: "vf",
          domanda: "IL NETTO È PIÙ BASSO DEL LORDO. È NORMALE.",
          icona: "⚖️",
          correct: true,
          aiuto: "DAL LORDO SI TOLGONO LE TASSE E I CONTRIBUTI INPS.",
          spiega: "VERO. NETTO = LORDO − TASSE − CONTRIBUTI INPS."
        },
        {
          tipo: "scelta",
          domanda: "MOHAMMAD PAGA I CONTRIBUTI INPS. A CHE COSA SERVONO?",
          icona: "🏛️",
          risposte: [
            { t: "PER LA PENSIONE E SE SEI MALATO", i: "🏛️" },
            { t: "PER PAGARE IL RISTORANTE", i: "🍝" },
            { t: "PER IL PERMESSO DI SOGGIORNO", i: "🪪" }
          ],
          correct: 0,
          aiuto: "L’INPS PENSA AL TUO FUTURO E ALLA TUA SALUTE.",
          spiega: "I CONTRIBUTI INPS SERVONO PER LA PENSIONE E PER PROTEGGERTI SE SEI MALATO."
        },
        {
          tipo: "scelta",
          domanda: "MOHAMMAD VUOLE AFFITTARE UNA CASA. CHE COSA CHIEDE SPESSO IL PROPRIETARIO?",
          icona: "🏠",
          risposte: [
            { t: "LE ULTIME BUSTE PAGA", i: "💳" },
            { t: "IL CERTIFICATO DEL MEDICO", i: "🩺" },
            { t: "LA PAGELLA DELLA SCUOLA", i: "📘" }
          ],
          correct: 0,
          aiuto: "IL PROPRIETARIO VUOLE SAPERE SE PUOI PAGARE L’AFFITTO.",
          spiega: "CONSERVA SEMPRE LE BUSTE PAGA: SERVONO PER LA CASA E PER IL PERMESSO DI SOGGIORNO."
        }
      ]
    }
  ]
};
