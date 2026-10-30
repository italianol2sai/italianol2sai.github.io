// Contenuti del gioco «MISSIONE CUCINA» (generati da _strumenti/missioni.py: modificare lì).
window.MISSIONE = {
 "titolo": "MISSIONE CUCINA",
 "sottotitolo": "PREPARA LA CENA CON FATOU!",
 "parolaSegreta": "PANE",
 "guida": "giovanni",
 "protagonista": "fatou",
 "etichetta": "ITALIANO L2 · IL CIBO",
 "portaFinale": "LA PORTA DELLA CUCINA",
 "grazie": "GRAZIE! LA CENA È PRONTA!",
 "imparato": "HAI IMPARATO I NEGOZI, LA FRUTTA E LA VERDURA, I VERBI DELLA CUCINA E COME SI ORDINA AL RISTORANTE.",
 "intro": [
  [
   "fatou",
   "STASERA INVITO A CENA LE MIE AMICHE! DEVO FARE LA SPESA E CUCINARE."
  ],
  [
   "giovanni",
   "IO SONO GIOVANNI. TI AIUTO IO, FATOU!"
  ],
  [
   "giovanni",
   "CI SONO 4 PORTE. CON LE 4 LETTERE SCOPRI CHE COSA NON PUÒ MANCARE A TAVOLA!"
  ]
 ],
 "finale": [
  [
   "fatou",
   "LA TAVOLA È PRONTA. MA MANCA UNA COSA…"
  ],
  [
   "giovanni",
   "CHE COSA MANCA? SCRIVI LA PAROLA SEGRETA."
  ]
 ],
 "vittoria": "LE AMICHE DICONO: «CHE BUONO IL PANE CALDO, FATOU! E ANCHE LA CENA È BUONISSIMA!»",
 "stanze": [
  {
   "id": "negozi",
   "titolo": "I NEGOZI",
   "icona": "🏪",
   "lettera": "P",
   "chi": "giovanni",
   "lezione": {
    "titolo": "AL MERCATO",
    "link": "mercato/"
   },
   "storia": [
    [
     "giovanni",
     "PRIMA ANDIAMO A FARE LA SPESA."
    ]
   ],
   "fine": [
    "fatou",
    "HO COMPRATO TUTTO!"
   ],
   "prove": [
    {
     "tipo": "scelta",
     "domanda": "DOVE COMPRO IL PANE?",
     "icona": "🥖",
     "risposte": [
      {
       "t": "DAL PANETTIERE",
       "i": "🥖"
      },
      {
       "t": "DAL MACELLAIO",
       "i": "🥩"
      },
      {
       "t": "IN FARMACIA",
       "i": "💊"
      }
     ],
     "correct": 0,
     "aiuto": "IL PANETTIERE FA IL PANE.",
     "spiega": "IL PANE SI COMPRA DAL PANETTIERE O AL FORNO."
    },
    {
     "tipo": "scelta",
     "domanda": "DOVE COMPRO IL POLLO?",
     "icona": "🍗",
     "risposte": [
      {
       "t": "DAL MACELLAIO",
       "i": "🥩"
      },
      {
       "t": "DAL PESCIVENDOLO",
       "i": "🐟"
      },
      {
       "t": "DAL FRUTTIVENDOLO",
       "i": "🍎"
      }
     ],
     "correct": 0,
     "aiuto": "VENDE LA CARNE.",
     "spiega": "LA CARNE SI COMPRA DAL MACELLAIO."
    },
    {
     "tipo": "completa",
     "domanda": "COMPLETA.",
     "frase": "VORREI UN CHILO ___ PATATE.",
     "icona": "🥔",
     "risposte": [
      "DI",
      "A",
      "IN"
     ],
     "correct": 0,
     "aiuto": "UN CHILO, UN LITRO, UN ETTO + …",
     "spiega": "UN CHILO DI PATATE."
    }
   ]
  },
  {
   "id": "frutta",
   "titolo": "FRUTTA E VERDURA",
   "icona": "🍅",
   "lettera": "A",
   "chi": "giovanni",
   "lezione": {
    "titolo": "IL CIBO E LA CUCINA",
    "link": "parole/cucina.html"
   },
   "storia": [
    [
     "giovanni",
     "ORA IL FRUTTIVENDOLO!"
    ]
   ],
   "fine": [
    "fatou",
    "CHE BELLA FRUTTA!"
   ],
   "prove": [
    {
     "tipo": "scelta",
     "domanda": "È ROSSO E SI USA PER IL SUGO.",
     "icona": "🍅",
     "risposte": [
      {
       "t": "IL POMODORO",
       "i": "🍅"
      },
      {
       "t": "LA BANANA",
       "i": "🍌"
      },
      {
       "t": "LA CAROTA",
       "i": "🥕"
      }
     ],
     "correct": 0,
     "aiuto": "LA PASTA AL ___.",
     "spiega": "IL POMODORO È ROSSO: CON LUI FACCIAMO IL SUGO."
    },
    {
     "tipo": "scelta",
     "domanda": "È GIALLO E ACIDO.",
     "icona": "🍋",
     "risposte": [
      {
       "t": "IL LIMONE",
       "i": "🍋"
      },
      {
       "t": "LA FRAGOLA",
       "i": "🍓"
      },
      {
       "t": "L'UVA",
       "i": "🍇"
      }
     ],
     "correct": 0,
     "aiuto": "SI METTE SUL PESCE.",
     "spiega": "IL LIMONE È GIALLO E ACIDO."
    },
    {
     "tipo": "vf",
     "domanda": "LE MELE E LE PERE SONO FRUTTA.",
     "icona": "🍎",
     "correct": true,
     "aiuto": "SI MANGIANO DOPO IL PRANZO.",
     "spiega": "VERO."
    }
   ]
  },
  {
   "id": "cucinare",
   "titolo": "CUCINIAMO!",
   "icona": "🍳",
   "lettera": "N",
   "chi": "giovanni",
   "lezione": {
    "titolo": "LAVORO IN CUCINA",
    "link": "cucina-lavoro/"
   },
   "storia": [
    [
     "giovanni",
     "A CASA! ADESSO SI CUCINA."
    ]
   ],
   "fine": [
    "fatou",
    "LA PASTA È PRONTA!"
   ],
   "prove": [
    {
     "tipo": "scelta",
     "domanda": "PRIMA DI MANGIARE LA FRUTTA LA DEVO…",
     "icona": "💧",
     "risposte": [
      {
       "t": "LAVARE",
       "i": "💧"
      },
      {
       "t": "FRIGGERE",
       "i": "🍳"
      },
      {
       "t": "CONGELARE",
       "i": "❄️"
      }
     ],
     "correct": 0,
     "aiuto": "CON L'ACQUA.",
     "spiega": "LA FRUTTA SI LAVA."
    },
    {
     "tipo": "completa",
     "domanda": "COMPLETA.",
     "frase": "METTO L'ACQUA SUL FUOCO E ___ LA PASTA.",
     "icona": "🍝",
     "risposte": [
      "CUOCIO",
      "BEVO",
      "TAGLIO"
     ],
     "correct": 0,
     "aiuto": "LA PASTA VA IN ACQUA CHE BOLLE.",
     "spiega": "CUOCIO LA PASTA PER 10 MINUTI."
    },
    {
     "tipo": "scelta",
     "domanda": "CON CHE COSA TAGLIO IL PANE?",
     "icona": "🔪",
     "risposte": [
      {
       "t": "CON IL COLTELLO",
       "i": "🔪"
      },
      {
       "t": "CON IL CUCCHIAIO",
       "i": "🥄"
      },
      {
       "t": "CON IL BICCHIERE",
       "i": "🥛"
      }
     ],
     "correct": 0,
     "aiuto": "È AFFILATO.",
     "spiega": "TAGLIO CON IL COLTELLO."
    }
   ]
  },
  {
   "id": "tavola",
   "titolo": "A TAVOLA",
   "icona": "🍽️",
   "lettera": "E",
   "chi": "giovanni",
   "lezione": {
    "titolo": "AL RISTORANTE",
    "link": "ristorante/"
   },
   "storia": [
    [
     "fatou",
     "ARRIVANO LE AMICHE! PREPARIAMO LA TAVOLA."
    ]
   ],
   "fine": [
    "giovanni",
    "BRAVISSIMA, FATOU!"
   ],
   "prove": [
    {
     "tipo": "scelta",
     "domanda": "UN'AMICA CHIEDE L'ACQUA. CHE COSA DICE?",
     "icona": "💧",
     "risposte": [
      {
       "t": "MI PASSI L'ACQUA, PER FAVORE?",
       "i": "🙏"
      },
      {
       "t": "DAMMI ACQUA!",
       "i": "😠"
      },
      {
       "t": "ACQUA NO.",
       "i": "🙅"
      }
     ],
     "correct": 0,
     "aiuto": "È GENTILE.",
     "spiega": "SI DICE «PER FAVORE»."
    },
    {
     "tipo": "completa",
     "domanda": "COMPLETA.",
     "frase": "BUON ___!",
     "icona": "😋",
     "risposte": [
      "APPETITO",
      "GIORNO",
      "VIAGGIO"
     ],
     "correct": 0,
     "aiuto": "SI DICE PRIMA DI MANGIARE.",
     "spiega": "BUON APPETITO!"
    },
    {
     "tipo": "vf",
     "domanda": "IN ITALIA IL PRANZO È DI SOLITO VERSO L'UNA.",
     "icona": "🕐",
     "correct": true,
     "aiuto": "TRA MEZZOGIORNO E LE DUE.",
     "spiega": "VERO."
    }
   ]
  }
 ],
 "sito": "https://italianol2sai.github.io/",
 "chiaveSalva": "missione-cucina-v1"
};
