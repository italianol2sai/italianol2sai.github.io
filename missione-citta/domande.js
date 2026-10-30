// Contenuti del gioco «MISSIONE CITTÀ» (generati da _strumenti/missioni.py: modificare lì).
window.MISSIONE = {
 "titolo": "MISSIONE CITTÀ",
 "sottotitolo": "AIUTA MARIELA A MUOVERSI A BARI!",
 "parolaSegreta": "META",
 "guida": "saleah",
 "protagonista": "mariela",
 "etichetta": "ITALIANO L2 · LA CITTÀ",
 "portaFinale": "LA PORTA DELLA STAZIONE",
 "grazie": "GRAZIE! SONO ARRIVATA!",
 "imparato": "HAI IMPARATO I LUOGHI DELLA CITTÀ, LE INDICAZIONI, L'AUTOBUS, IL TRENO E I CARTELLI.",
 "intro": [
  [
   "mariela",
   "OGGI DEVO ANDARE IN TANTI POSTI A BARI. MA NON CONOSCO BENE LA CITTÀ!"
  ],
  [
   "saleah",
   "SONO SALEAH. TI ACCOMPAGNO IO!"
  ],
  [
   "saleah",
   "CI SONO 4 PORTE. CON LE 4 LETTERE SCOPRI LA PAROLA SEGRETA: È LA FINE DEL VIAGGIO!"
  ]
 ],
 "finale": [
  [
   "mariela",
   "HO PRESO L'AUTOBUS E IL TRENO. ECCO IL MARE DI POLIGNANO!"
  ],
  [
   "saleah",
   "COME SI CHIAMA IL POSTO DOVE ARRIVI? SCRIVI LA PAROLA SEGRETA."
  ]
 ],
 "vittoria": "SALEAH DICE: «SEI ARRIVATA ALLA META, MARIELA! ADESSO CONOSCI LA CITTÀ.»",
 "stanze": [
  {
   "id": "luoghi",
   "titolo": "I LUOGHI",
   "icona": "🏙️",
   "lettera": "M",
   "chi": "saleah",
   "lezione": {
    "titolo": "LA CITTÀ",
    "link": "#citta"
   },
   "storia": [
    [
     "saleah",
     "DOVE DEVI ANDARE, MARIELA?"
    ]
   ],
   "fine": [
    "mariela",
    "CONOSCO I LUOGHI!"
   ],
   "prove": [
    {
     "tipo": "scelta",
     "domanda": "DEVO SPEDIRE UN PACCO. DOVE VADO?",
     "icona": "📦",
     "risposte": [
      {
       "t": "ALLA POSTA",
       "i": "🏤"
      },
      {
       "t": "IN FARMACIA",
       "i": "💊"
      },
      {
       "t": "AL BAR",
       "i": "☕"
      }
     ],
     "correct": 0,
     "aiuto": "C'È LO SPORTELLO GIALLO.",
     "spiega": "UN PACCO SI SPEDISCE ALLA POSTA."
    },
    {
     "tipo": "scelta",
     "domanda": "DEVO PRENDERE IL TRENO. DOVE VADO?",
     "icona": "🚆",
     "risposte": [
      {
       "t": "ALLA STAZIONE",
       "i": "🚉"
      },
      {
       "t": "ALL'OSPEDALE",
       "i": "🏥"
      },
      {
       "t": "IN BANCA",
       "i": "🏦"
      }
     ],
     "correct": 0,
     "aiuto": "CI SONO I BINARI.",
     "spiega": "IL TRENO SI PRENDE ALLA STAZIONE."
    },
    {
     "tipo": "completa",
     "domanda": "COMPLETA.",
     "frase": "VADO ___ SUPERMERCATO.",
     "icona": "🛒",
     "risposte": [
      "AL",
      "IN",
      "A"
     ],
     "correct": 0,
     "aiuto": "A + IL = …",
     "spiega": "VADO AL SUPERMERCATO."
    }
   ]
  },
  {
   "id": "strada",
   "titolo": "LE INDICAZIONI",
   "icona": "🧭",
   "lettera": "E",
   "chi": "saleah",
   "lezione": {
    "titolo": "I PUNTI CARDINALI",
    "link": "punti-cardinali/"
   },
   "storia": [
    [
     "mariela",
     "SCUSI, DOV'È LA FERMATA?"
    ]
   ],
   "fine": [
    "saleah",
    "PERFETTO!"
   ],
   "prove": [
    {
     "tipo": "scelta",
     "domanda": "➡️ VUOL DIRE…",
     "icona": "➡️",
     "risposte": [
      {
       "t": "GIRA A DESTRA",
       "i": "➡️"
      },
      {
       "t": "GIRA A SINISTRA",
       "i": "⬅️"
      },
      {
       "t": "TORNA INDIETRO",
       "i": "↩️"
      }
     ],
     "correct": 0,
     "aiuto": "LA MANO CON CUI SCRIVONO TANTE PERSONE.",
     "spiega": "➡️ = A DESTRA."
    },
    {
     "tipo": "completa",
     "domanda": "COMPLETA.",
     "frase": "VAI SEMPRE ___ PER 100 METRI.",
     "icona": "⬆️",
     "risposte": [
      "DRITTO",
      "DESTRA",
      "SOPRA"
     ],
     "correct": 0,
     "aiuto": "NON GIRARE.",
     "spiega": "SEMPRE DRITTO."
    },
    {
     "tipo": "vf",
     "domanda": "«È DI FRONTE ALLA CHIESA» VUOL DIRE: È DALL'ALTRA PARTE DELLA STRADA.",
     "icona": "⛪",
     "correct": true,
     "aiuto": "LA VEDI DAVANTI A TE.",
     "spiega": "VERO."
    }
   ]
  },
  {
   "id": "autobus",
   "titolo": "L'AUTOBUS",
   "icona": "🚌",
   "lettera": "T",
   "chi": "saleah",
   "lezione": {
    "titolo": "PRENDO L'AUTOBUS",
    "link": "autobus/"
   },
   "storia": [
    [
     "saleah",
     "ECCO LA FERMATA DELL'AUTOBUS."
    ]
   ],
   "fine": [
    "mariela",
    "SONO SULL'AUTOBUS!"
   ],
   "prove": [
    {
     "tipo": "scelta",
     "domanda": "DOVE COMPRO IL BIGLIETTO DELL'AUTOBUS?",
     "icona": "🎫",
     "risposte": [
      {
       "t": "IN TABACCHERIA O CON L'APP",
       "i": "📱"
      },
      {
       "t": "IN FARMACIA",
       "i": "💊"
      },
      {
       "t": "DAL MEDICO",
       "i": "🩺"
      }
     ],
     "correct": 0,
     "aiuto": "C'È LA T.",
     "spiega": "IL BIGLIETTO SI COMPRA IN TABACCHERIA, IN EDICOLA O CON L'APP."
    },
    {
     "tipo": "vf",
     "domanda": "SULL'AUTOBUS DEVO CONVALIDARE IL BIGLIETTO.",
     "icona": "🎫",
     "correct": true,
     "aiuto": "SE NON LO FAI, PUOI PRENDERE UNA MULTA.",
     "spiega": "VERO."
    },
    {
     "tipo": "completa",
     "domanda": "COMPLETA.",
     "frase": "SCUSI, A CHE ORA ___ L'AUTOBUS?",
     "icona": "🕐",
     "risposte": [
      "PASSA",
      "PASSANO",
      "PASSI"
     ],
     "correct": 0,
     "aiuto": "L'AUTOBUS: UNO SOLO.",
     "spiega": "A CHE ORA PASSA L'AUTOBUS?"
    }
   ]
  },
  {
   "id": "treno",
   "titolo": "IL TRENO",
   "icona": "🚆",
   "lettera": "A",
   "chi": "saleah",
   "lezione": {
    "titolo": "PRENDO IL TRENO",
    "link": "treno/"
   },
   "storia": [
    [
     "saleah",
     "ULTIMA PORTA: LA STAZIONE."
    ]
   ],
   "fine": [
    "mariela",
    "IL TRENO PARTE!"
   ],
   "prove": [
    {
     "tipo": "scelta",
     "domanda": "IL TABELLONE DICE «BIN. 3». CHE COSA VUOL DIRE?",
     "icona": "🚉",
     "risposte": [
      {
       "t": "BINARIO 3",
       "i": "🛤️"
      },
      {
       "t": "BIGLIETTO 3",
       "i": "🎫"
      },
      {
       "t": "3 EURO",
       "i": "💶"
      }
     ],
     "correct": 0,
     "aiuto": "È IL POSTO DOVE SI FERMA IL TRENO.",
     "spiega": "BIN. = BINARIO."
    },
    {
     "tipo": "completa",
     "domanda": "COMPLETA.",
     "frase": "VORREI UN BIGLIETTO ___ POLIGNANO.",
     "icona": "🎫",
     "risposte": [
      "PER",
      "DA",
      "IN"
     ],
     "correct": 0,
     "aiuto": "LA DESTINAZIONE.",
     "spiega": "UN BIGLIETTO PER POLIGNANO."
    },
    {
     "tipo": "vf",
     "domanda": "«IN RITARDO» VUOL DIRE CHE IL TRENO ARRIVA PRIMA.",
     "icona": "⏱️",
     "correct": false,
     "aiuto": "RITARDO = TARDI.",
     "spiega": "FALSO. IN RITARDO = ARRIVA DOPO L'ORARIO."
    }
   ]
  }
 ],
 "sito": "https://italianol2sai.github.io/",
 "chiaveSalva": "missione-citta-v1"
};
