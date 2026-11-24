// Contenuti del gioco «MISSIONE ALFABETO» (generati da _strumenti/missioni.py: modificare lì).
window.MISSIONE = {
 "titolo": "MISSIONE ALFABETO",
 "sottotitolo": "AIUTA TESFAYE A LEGGERE E SCRIVERE!",
 "parolaSegreta": "SCRIVO",
 "guida": "luciana",
 "protagonista": "tesfaye",
 "etichetta": "ITALIANO L2 · ALFABETIZZAZIONE",
 "portaFinale": "LA PORTA DELLA CLASSE",
 "grazie": "GRAZIE! ADESSO SO LEGGERE E SCRIVERE!",
 "imparato": "HAI RIPASSATO LE LETTERE, LE SILLABE, I NUMERI, I GIORNI, LA CASA, LA CITTÀ, LA SPESA E IL LAVORO.",
 "intro": [
  [
   "tesfaye",
   "CIAO! MI CHIAMO TESFAYE. VENGO DALL'ERITREA. ABITO A BARI."
  ],
  [
   "tesfaye",
   "VOGLIO IMPARARE A LEGGERE E A SCRIVERE IN ITALIANO."
  ],
  [
   "luciana",
   "IO SONO LUCIANA, L'INSEGNANTE DI ITALIANO. TI AIUTO IO! CI SONO 6 PORTE. DIETRO OGNI PORTA C'È UNA LETTERA."
  ],
  [
   "luciana",
   "👆 TOCCA 🔊 PER ASCOLTARE. CON LE 6 LETTERE SCOPRI LA PAROLA SEGRETA!"
  ]
 ],
 "finale": [
  [
   "tesfaye",
   "È L'ULTIMO GIORNO DEL CORSO. HO UN FOGLIO E UNA PENNA."
  ],
  [
   "luciana",
   "CHE COSA FA ADESSO TESFAYE CON LA PENNA? SCRIVI LA PAROLA SEGRETA CON LE 6 LETTERE."
  ]
 ],
 "vittoria": "TESFAYE DICE: «IO SCRIVO! SCRIVO IL MIO NOME: T-E-S-F-A-Y-E. È BELLISSIMO!»",
 "stanze": [
  {
   "id": "ciao",
   "titolo": "CIAO, IO SONO…",
   "icona": "👋",
   "lettera": "S",
   "chi": "luciana",
   "lezione": {
    "titolo": "CIAO, IO SONO",
    "link": "alfa-ciao-io-sono/"
   },
   "storia": [
    [
     "luciana",
     "PRIMA PORTA: CI PRESENTIAMO!"
    ]
   ],
   "fine": [
    "tesfaye",
    "SO DIRE IL MIO NOME!"
   ],
   "prove": [
    {
     "tipo": "scelta",
     "domanda": "LUCIANA DICE: «CIAO! COME TI CHIAMI?» TESFAYE RISPONDE:",
     "icona": "👋",
     "risposte": [
      {
       "t": "MI CHIAMO TESFAYE.",
       "i": "🙂"
      },
      {
       "t": "HO FAME.",
       "i": "🍞"
      },
      {
       "t": "SONO LE TRE.",
       "i": "🕒"
      }
     ],
     "correct": 0,
     "aiuto": "DICE IL SUO NOME.",
     "spiega": "MI CHIAMO… = IL MIO NOME È…"
    },
    {
     "tipo": "scelta",
     "domanda": "QUALE PAROLA COMINCIA CON «O»?",
     "icona": "🔤",
     "risposte": [
      {
       "t": "OCCHIO",
       "i": "👁️"
      },
      {
       "t": "MANO",
       "i": "✋"
      },
      {
       "t": "PANE",
       "i": "🍞"
      }
     ],
     "correct": 0,
     "aiuto": "ASCOLTA IL PRIMO SUONO: O…",
     "spiega": "OCCHIO COMINCIA CON O."
    },
    {
     "tipo": "scelta",
     "domanda": "QUANTI SONO? ✋✋",
     "icona": "🔢",
     "risposte": [
      {
       "t": "DIECI",
       "i": "🔟"
      },
      {
       "t": "CINQUE",
       "i": "5️⃣"
      },
      {
       "t": "DUE",
       "i": "2️⃣"
      }
     ],
     "correct": 0,
     "aiuto": "CONTA LE DITA: 5 + 5.",
     "spiega": "5 + 5 = 10, DIECI."
    }
   ]
  },
  {
   "id": "scuola",
   "titolo": "VADO AL CORSO",
   "icona": "🏫",
   "lettera": "C",
   "chi": "luciana",
   "lezione": {
    "titolo": "VADO AL CORSO",
    "link": "alfa-vado-al-corso/"
   },
   "storia": [
    [
     "tesfaye",
     "LUCIANA, CHE COSA SERVE PER IL CORSO?"
    ]
   ],
   "fine": [
    "luciana",
    "BRAVO! HAI TUTTO NELLO ZAINO."
   ],
   "prove": [
    {
     "tipo": "scelta",
     "domanda": "CON CHE COSA SCRIVO?",
     "icona": "✍️",
     "risposte": [
      {
       "t": "CON LA PENNA",
       "i": "🖊️"
      },
      {
       "t": "CON IL LIBRO",
       "i": "📖"
      },
      {
       "t": "CON LA GOMMA",
       "i": "🧽"
      }
     ],
     "correct": 0,
     "aiuto": "HA L'INCHIOSTRO.",
     "spiega": "SCRIVO CON LA PENNA O CON LA MATITA."
    },
    {
     "tipo": "completa",
     "domanda": "COMPLETA.",
     "frase": "MA + NO = ___",
     "icona": "✋",
     "risposte": [
      "MANO",
      "MONA",
      "NOMA"
     ],
     "correct": 0,
     "aiuto": "UNISCI: PRIMA MA, POI NO.",
     "spiega": "MA + NO = MANO."
    },
    {
     "tipo": "vf",
     "domanda": "IL CORSO DI ITALIANO PER ADULTI AL CPIA È GRATIS.",
     "icona": "💶",
     "correct": false,
     "aiuto": "C'È UNA QUOTA DI ISCRIZIONE.",
     "spiega": "FALSO. SI PAGA UNA PICCOLA QUOTA DI ISCRIZIONE. SERVE ANCHE UN DOCUMENTO."
    }
   ]
  },
  {
   "id": "giornata",
   "titolo": "LA MIA GIORNATA",
   "icona": "☀️",
   "lettera": "R",
   "chi": "luciana",
   "lezione": {
    "titolo": "LA MIA GIORNATA",
    "link": "alfa-la-mia-giornata/"
   },
   "storia": [
    [
     "luciana",
     "QUANDO FAI LE COSE? MATTINA, POMERIGGIO, SERA…"
    ]
   ],
   "fine": [
    "tesfaye",
    "CONOSCO I GIORNI DELLA SETTIMANA!"
   ],
   "prove": [
    {
     "tipo": "scelta",
     "domanda": "DOPO LUNEDÌ C'È…",
     "icona": "📅",
     "risposte": [
      {
       "t": "MARTEDÌ",
       "i": "2️⃣"
      },
      {
       "t": "DOMENICA",
       "i": "7️⃣"
      },
      {
       "t": "VENERDÌ",
       "i": "5️⃣"
      }
     ],
     "correct": 0,
     "aiuto": "LUNEDÌ, MARTEDÌ, MERCOLEDÌ…",
     "spiega": "LUNEDÌ → MARTEDÌ."
    },
    {
     "tipo": "scelta",
     "domanda": "🌙 LA SERA IO…",
     "icona": "🌙",
     "risposte": [
      {
       "t": "CENO",
       "i": "🍽️"
      },
      {
       "t": "FACCIO COLAZIONE",
       "i": "☕"
      },
      {
       "t": "VADO AL LAVORO ALLE 7",
       "i": "🌅"
      }
     ],
     "correct": 0,
     "aiuto": "È BUIO. MANGIO.",
     "spiega": "LA SERA CENO E POI DORMO."
    },
    {
     "tipo": "completa",
     "domanda": "COMPLETA.",
     "frase": "20 + 10 = ___",
     "icona": "🔢",
     "risposte": [
      "TRENTA",
      "VENTI",
      "DIECI"
     ],
     "correct": 0,
     "aiuto": "VENTI E DIECI…",
     "spiega": "20 + 10 = 30, TRENTA."
    }
   ]
  },
  {
   "id": "vestiti",
   "titolo": "MI DESCRIVO E STO BENE",
   "icona": "🧥",
   "lettera": "I",
   "chi": "luciana",
   "lezione": {
    "titolo": "MI DESCRIVO",
    "link": "alfa-mi-descrivo/"
   },
   "storia": [
    [
     "tesfaye",
     "OGGI È FREDDO. CHE COSA METTO?"
    ]
   ],
   "fine": [
    "luciana",
    "BENE! E ADESSO COME STAI?"
   ],
   "prove": [
    {
     "tipo": "scelta",
     "domanda": "FA FREDDO. PER LE MANI METTO…",
     "icona": "🧤",
     "risposte": [
      {
       "t": "I GUANTI",
       "i": "🧤"
      },
      {
       "t": "LE SCARPE",
       "i": "👟"
      },
      {
       "t": "I PANTALONI",
       "i": "👖"
      }
     ],
     "correct": 0,
     "aiuto": "SONO PER LE MANI.",
     "spiega": "PER LE MANI METTO I GUANTI."
    },
    {
     "tipo": "scelta",
     "domanda": "😊 TESFAYE È…",
     "icona": "😊",
     "risposte": [
      {
       "t": "FELICE",
       "i": "😊"
      },
      {
       "t": "TRISTE",
       "i": "😢"
      },
      {
       "t": "STANCO",
       "i": "😴"
      }
     ],
     "correct": 0,
     "aiuto": "GUARDA LA FACCIA: SORRIDE.",
     "spiega": "😊 = FELICE."
    },
    {
     "tipo": "scelta",
     "domanda": "TESFAYE DICE: «HO MAL DI…» E TOCCA LA TESTA.",
     "icona": "🤕",
     "risposte": [
      {
       "t": "TESTA",
       "i": "🗣️"
      },
      {
       "t": "PIEDE",
       "i": "🦶"
      },
      {
       "t": "PANCIA",
       "i": "🤰"
      }
     ],
     "correct": 0,
     "aiuto": "TOCCA LA TESTA.",
     "spiega": "HO MAL DI TESTA: VADO DAL MEDICO."
    }
   ]
  },
  {
   "id": "casa",
   "titolo": "LA CASA E LA CITTÀ",
   "icona": "🏠",
   "lettera": "V",
   "chi": "luciana",
   "lezione": {
    "titolo": "MI SCUSI, DOV'È…?",
    "link": "alfa-mi-scusi-dove/"
   },
   "storia": [
    [
     "luciana",
     "ADESSO GIRIAMO PER BARI. DOVE SONO LE COSE?"
    ]
   ],
   "fine": [
    "tesfaye",
    "SO CHIEDERE LA STRADA!"
   ],
   "prove": [
    {
     "tipo": "scelta",
     "domanda": "DOVE DORMO?",
     "icona": "🛏️",
     "risposte": [
      {
       "t": "IN CAMERA",
       "i": "🛏️"
      },
      {
       "t": "IN CUCINA",
       "i": "🍳"
      },
      {
       "t": "IN BAGNO",
       "i": "🚿"
      }
     ],
     "correct": 0,
     "aiuto": "C'È IL LETTO.",
     "spiega": "DORMO IN CAMERA DA LETTO."
    },
    {
     "tipo": "scelta",
     "domanda": "COMPRO LE MEDICINE IN…",
     "icona": "💊",
     "risposte": [
      {
       "t": "FARMACIA",
       "i": "💊"
      },
      {
       "t": "BANCA",
       "i": "🏦"
      },
      {
       "t": "POSTA",
       "i": "📮"
      }
     ],
     "correct": 0,
     "aiuto": "C'È LA CROCE VERDE.",
     "spiega": "LE MEDICINE SI COMPRANO IN FARMACIA."
    },
    {
     "tipo": "scelta",
     "domanda": "➡️ È A…",
     "icona": "➡️",
     "risposte": [
      {
       "t": "DESTRA",
       "i": "➡️"
      },
      {
       "t": "SINISTRA",
       "i": "⬅️"
      },
      {
       "t": "DRITTO",
       "i": "⬆️"
      }
     ],
     "correct": 0,
     "aiuto": "GUARDA LA FRECCIA.",
     "spiega": "➡️ = A DESTRA."
    },
    {
     "tipo": "vf",
     "domanda": "PER PRENDERE L'AUTOBUS SERVE IL BIGLIETTO.",
     "icona": "🎫",
     "correct": true,
     "aiuto": "SI COMPRA IN TABACCHERIA.",
     "spiega": "VERO. PRIMA COMPRO IL BIGLIETTO."
    }
   ]
  },
  {
   "id": "lavoro",
   "titolo": "LA SPESA E IL LAVORO",
   "icona": "🛒",
   "lettera": "O",
   "chi": "luciana",
   "lezione": {
    "titolo": "CERCO LAVORO",
    "link": "alfa-cerco-lavoro/"
   },
   "storia": [
    [
     "tesfaye",
     "ULTIMA PORTA! VADO AL MERCATO E POI CERCO LAVORO."
    ]
   ],
   "fine": [
    "luciana",
    "BRAVISSIMO, TESFAYE! APRI L'ULTIMA PORTA."
   ],
   "prove": [
    {
     "tipo": "scelta",
     "domanda": "UN ___ DI MELE, PER FAVORE.",
     "icona": "🍎",
     "risposte": [
      {
       "t": "CHILO",
       "i": "⚖️"
      },
      {
       "t": "LITRO",
       "i": "🥛"
      },
      {
       "t": "METRO",
       "i": "📏"
      }
     ],
     "correct": 0,
     "aiuto": "LE MELE SI PESANO.",
     "spiega": "UN CHILO DI MELE."
    },
    {
     "tipo": "scelta",
     "domanda": "CHI LAVORA IN CUCINA?",
     "icona": "👨‍🍳",
     "risposte": [
      {
       "t": "IL CUOCO",
       "i": "👨‍🍳"
      },
      {
       "t": "IL MURATORE",
       "i": "👷"
      },
      {
       "t": "IL MECCANICO",
       "i": "🧑‍🔧"
      }
     ],
     "correct": 0,
     "aiuto": "PREPARA DA MANGIARE.",
     "spiega": "IL CUOCO LAVORA IN CUCINA."
    },
    {
     "tipo": "completa",
     "domanda": "COMPLETA IL MODULO.",
     "frase": "NOME: TESFAYE · ___: HAILE",
     "icona": "📝",
     "risposte": [
      "COGNOME",
      "TELEFONO",
      "VIA"
     ],
     "correct": 0,
     "aiuto": "IL NOME DELLA FAMIGLIA.",
     "spiega": "NOME = TESFAYE, COGNOME = HAILE."
    },
    {
     "tipo": "scelta",
     "domanda": "CHE COSA FAI DOMANI? DOMANI ___ IL CORSO.",
     "icona": "📅",
     "risposte": [
      {
       "t": "HO",
       "i": "🫴"
      },
      {
       "t": "O",
       "i": "🔤"
      },
      {
       "t": "A",
       "i": "🔤"
      }
     ],
     "correct": 0,
     "aiuto": "AVERE: IO HO. CON LA H!",
     "spiega": "IO HO = AVERE. LA H NON SI SENTE."
    }
   ]
  }
 ],
 "sito": "https://italianol2sai.github.io/",
 "chiaveSalva": "missione-alfa-v1"
};
