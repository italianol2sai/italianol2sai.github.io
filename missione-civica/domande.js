// Contenuti del gioco «MISSIONE CITTADINO» (generati da _strumenti/missioni.py: modificare lì).
window.MISSIONE = {
 "titolo": "MISSIONE CITTADINO",
 "sottotitolo": "AIUTA MOHAMMAD CON I DOCUMENTI!",
 "parolaSegreta": "DIRITTI",
 "guida": "serena",
 "protagonista": "mohammad",
 "etichetta": "ITALIANO L2 · EDUCAZIONE CIVICA",
 "portaFinale": "LA PORTA DEL COMUNE",
 "grazie": "GRAZIE! ORA CONOSCO I MIEI DIRITTI E I MIEI DOVERI!",
 "imparato": "HAI IMPARATO I DOCUMENTI, GLI UFFICI, I DIRITTI E I DOVERI E LE REGOLE DELLA CONVIVENZA.",
 "intro": [
  [
   "mohammad",
   "DEVO FARE TANTI DOCUMENTI: CODICE FISCALE, RESIDENZA, CARTA D'IDENTITÀ…"
  ],
  [
   "serena",
   "NON TI PREOCCUPARE, TI AIUTO IO."
  ],
  [
   "serena",
   "CI SONO 7 PORTE. CON LE 7 LETTERE SCOPRI CHE COSA HANNO TUTTE LE PERSONE IN ITALIA!"
  ]
 ],
 "finale": [
  [
   "mohammad",
   "HO TUTTI I DOCUMENTI!"
  ],
  [
   "serena",
   "LA COSTITUZIONE DICE CHE TUTTI HANNO DEI… SCRIVI LA PAROLA SEGRETA."
  ]
 ],
 "vittoria": "SERENA DICE: «TUTTE LE PERSONE HANNO DIRITTI E DOVERI. BENVENUTO, MOHAMMAD!»",
 "stanze": [
  {
   "id": "codice",
   "titolo": "IL CODICE FISCALE",
   "icona": "🪪",
   "lettera": "D",
   "chi": "serena",
   "lezione": {
    "titolo": "IL CODICE FISCALE",
    "link": "codice-fiscale/"
   },
   "storia": [
    [
     "serena",
     "IL PRIMO DOCUMENTO È IL CODICE FISCALE."
    ]
   ],
   "fine": [
    "mohammad",
    "HO IL CODICE FISCALE!"
   ],
   "prove": [
    {
     "tipo": "scelta",
     "domanda": "DOVE CHIEDO IL CODICE FISCALE?",
     "icona": "🏢",
     "risposte": [
      {
       "t": "ALL'AGENZIA DELLE ENTRATE",
       "i": "🏢"
      },
      {
       "t": "AL SUPERMERCATO",
       "i": "🛒"
      },
      {
       "t": "IN STAZIONE",
       "i": "🚉"
      }
     ],
     "correct": 0,
     "aiuto": "È L'UFFICIO DELLE TASSE.",
     "spiega": "IL CODICE FISCALE SI CHIEDE ALL'AGENZIA DELLE ENTRATE."
    },
    {
     "tipo": "vf",
     "domanda": "IL CODICE FISCALE HA 16 CARATTERI: LETTERE E NUMERI.",
     "icona": "🔢",
     "correct": true,
     "aiuto": "CONTA: RSSMRA80A01A662X.",
     "spiega": "VERO."
    }
   ]
  },
  {
   "id": "residenza",
   "titolo": "LA RESIDENZA",
   "icona": "🏠",
   "lettera": "I",
   "chi": "serena",
   "lezione": {
    "titolo": "IN COMUNE E IN QUESTURA",
    "link": "comune-questura/"
   },
   "storia": [
    [
     "serena",
     "ORA LA RESIDENZA, IN COMUNE."
    ]
   ],
   "fine": [
    "mohammad",
    "HO LA RESIDENZA!"
   ],
   "prove": [
    {
     "tipo": "scelta",
     "domanda": "DOVE CHIEDO LA RESIDENZA?",
     "icona": "🏛️",
     "risposte": [
      {
       "t": "ALL'ANAGRAFE DEL COMUNE",
       "i": "🏛️"
      },
      {
       "t": "IN QUESTURA",
       "i": "👮"
      },
      {
       "t": "IN BANCA",
       "i": "🏦"
      }
     ],
     "correct": 0,
     "aiuto": "È L'UFFICIO DEL COMUNE PER I CITTADINI.",
     "spiega": "LA RESIDENZA SI CHIEDE ALL'ANAGRAFE."
    },
    {
     "tipo": "vf",
     "domanda": "LA RESIDENZA È L'INDIRIZZO DOVE ABITO DI SOLITO.",
     "icona": "📍",
     "correct": true,
     "aiuto": "È DOVE VIVI.",
     "spiega": "VERO."
    }
   ]
  },
  {
   "id": "carta",
   "titolo": "LA CARTA D'IDENTITÀ",
   "icona": "🪪",
   "lettera": "R",
   "chi": "serena",
   "lezione": {
    "titolo": "IN COMUNE E IN QUESTURA",
    "link": "comune-questura/"
   },
   "storia": [
    [
     "serena",
     "CON LA RESIDENZA PUOI CHIEDERE LA CARTA D'IDENTITÀ."
    ]
   ],
   "fine": [
    "mohammad",
    "ECCO LA MIA CIE!"
   ],
   "prove": [
    {
     "tipo": "scelta",
     "domanda": "LA CARTA D'IDENTITÀ ELETTRONICA SI CHIAMA…",
     "icona": "💳",
     "risposte": [
      {
       "t": "CIE",
       "i": "💳"
      },
      {
       "t": "SPID",
       "i": "📱"
      },
      {
       "t": "IBAN",
       "i": "🏦"
      }
     ],
     "correct": 0,
     "aiuto": "C-I-E.",
     "spiega": "CIE = CARTA D'IDENTITÀ ELETTRONICA."
    },
    {
     "tipo": "vf",
     "domanda": "PER LA CIE SERVE UNA FOTO.",
     "icona": "📷",
     "correct": true,
     "aiuto": "SULLA CARTA C'È LA TUA FACCIA.",
     "spiega": "VERO."
    }
   ]
  },
  {
   "id": "permesso",
   "titolo": "IL PERMESSO DI SOGGIORNO",
   "icona": "📄",
   "lettera": "I",
   "chi": "serena",
   "lezione": {
    "titolo": "IN COMUNE E IN QUESTURA",
    "link": "comune-questura/"
   },
   "storia": [
    [
     "mohammad",
     "IL MIO PERMESSO SCADE FRA DUE MESI!"
    ]
   ],
   "fine": [
    "serena",
    "BRAVO, NON DIMENTICARE LA DATA!"
   ],
   "prove": [
    {
     "tipo": "scelta",
     "domanda": "DOVE RINNOVO IL PERMESSO DI SOGGIORNO?",
     "icona": "👮",
     "risposte": [
      {
       "t": "IN QUESTURA",
       "i": "👮"
      },
      {
       "t": "DAL MEDICO",
       "i": "🩺"
      },
      {
       "t": "A SCUOLA",
       "i": "🏫"
      }
     ],
     "correct": 0,
     "aiuto": "È L'UFFICIO DELLA POLIZIA.",
     "spiega": "IL PERMESSO SI RINNOVA IN QUESTURA (CON IL KIT DELLA POSTA)."
    },
    {
     "tipo": "vf",
     "domanda": "IL PERMESSO SI PUÒ RINNOVARE ANCHE DOPO TRE ANNI DALLA SCADENZA.",
     "icona": "📅",
     "correct": false,
     "aiuto": "BISOGNA FARLO PRIMA.",
     "spiega": "FALSO. SI CHIEDE IL RINNOVO PRIMA DELLA SCADENZA."
    }
   ]
  },
  {
   "id": "diritti",
   "titolo": "DIRITTI E DOVERI",
   "icona": "⚖️",
   "lettera": "T",
   "chi": "serena",
   "lezione": {
    "titolo": "EDUCAZIONE CIVICA",
    "link": "#educazione-civica"
   },
   "storia": [
    [
     "serena",
     "IN ITALIA HAI DIRITTI E DOVERI."
    ]
   ],
   "fine": [
    "mohammad",
    "HO CAPITO!"
   ],
   "prove": [
    {
     "tipo": "scelta",
     "domanda": "QUALE È UN DOVERE?",
     "icona": "💶",
     "risposte": [
      {
       "t": "PAGARE LE TASSE",
       "i": "💶"
      },
      {
       "t": "ANDARE AL MARE",
       "i": "🏖️"
      },
      {
       "t": "GUARDARE LA TV",
       "i": "📺"
      }
     ],
     "correct": 0,
     "aiuto": "SERVE PER LE SCUOLE E GLI OSPEDALI.",
     "spiega": "PAGARE LE TASSE È UN DOVERE."
    },
    {
     "tipo": "vf",
     "domanda": "TUTTI HANNO DIRITTO ALLE CURE MEDICHE URGENTI.",
     "icona": "🏥",
     "correct": true,
     "aiuto": "LO DICE LA COSTITUZIONE (ARTICOLO 32).",
     "spiega": "VERO."
    }
   ]
  },
  {
   "id": "costituzione",
   "titolo": "LA COSTITUZIONE",
   "icona": "📜",
   "lettera": "T",
   "chi": "serena",
   "lezione": {
    "titolo": "EDUCAZIONE CIVICA",
    "link": "#educazione-civica"
   },
   "storia": [
    [
     "serena",
     "LA LEGGE PIÙ IMPORTANTE È LA COSTITUZIONE."
    ]
   ],
   "fine": [
    "mohammad",
    "CHE INTERESSANTE!"
   ],
   "prove": [
    {
     "tipo": "scelta",
     "domanda": "IL 2 GIUGNO È…",
     "icona": "🇮🇹",
     "risposte": [
      {
       "t": "LA FESTA DELLA REPUBBLICA",
       "i": "🇮🇹"
      },
      {
       "t": "NATALE",
       "i": "🎄"
      },
      {
       "t": "FERRAGOSTO",
       "i": "☀️"
      }
     ],
     "correct": 0,
     "aiuto": "NEL 1946 GLI ITALIANI HANNO VOTATO.",
     "spiega": "IL 2 GIUGNO È LA FESTA DELLA REPUBBLICA."
    },
    {
     "tipo": "vf",
     "domanda": "LA COSTITUZIONE ITALIANA È DEL 1948.",
     "icona": "📜",
     "correct": true,
     "aiuto": "È ENTRATA IN VIGORE IL 1° GENNAIO 1948.",
     "spiega": "VERO."
    }
   ]
  },
  {
   "id": "regole",
   "titolo": "LE REGOLE DI TUTTI I GIORNI",
   "icona": "♻️",
   "lettera": "I",
   "chi": "serena",
   "lezione": {
    "titolo": "LA RACCOLTA DIFFERENZIATA",
    "link": "raccolta-differenziata/"
   },
   "storia": [
    [
     "serena",
     "ULTIMA PORTA: LE REGOLE DELLA CONVIVENZA."
    ]
   ],
   "fine": [
    "mohammad",
    "RISPETTO LE REGOLE!"
   ],
   "prove": [
    {
     "tipo": "scelta",
     "domanda": "DOVE BUTTO LA BOTTIGLIA DI VETRO?",
     "icona": "🍾",
     "risposte": [
      {
       "t": "NEL VETRO",
       "i": "🟩"
      },
      {
       "t": "NELL'ORGANICO",
       "i": "🟫"
      },
      {
       "t": "PER STRADA",
       "i": "🚮"
      }
     ],
     "correct": 0,
     "aiuto": "C'È UN BIDONE SOLO PER IL VETRO.",
     "spiega": "IL VETRO VA NEL BIDONE DEL VETRO."
    },
    {
     "tipo": "vf",
     "domanda": "IN AUTO TUTTI DEVONO METTERE LA CINTURA.",
     "icona": "🚗",
     "correct": true,
     "aiuto": "ANCHE DIETRO.",
     "spiega": "VERO."
    }
   ]
  }
 ],
 "sito": "https://italianol2sai.github.io/",
 "chiaveSalva": "missione-civica-v1"
};
