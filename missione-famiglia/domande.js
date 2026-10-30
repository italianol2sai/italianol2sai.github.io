// Contenuti del gioco «MISSIONE FAMIGLIA» (generati da _strumenti/missioni.py: modificare lì).
window.MISSIONE = {
 "titolo": "MISSIONE FAMIGLIA",
 "sottotitolo": "PREPARA LA FESTA DELLA NONNA!",
 "parolaSegreta": "BACI",
 "guida": "eneida",
 "protagonista": "lin",
 "etichetta": "ITALIANO L2 · LA FAMIGLIA",
 "portaFinale": "LA PORTA DELLA FESTA",
 "grazie": "GRAZIE! È UNA FESTA BELLISSIMA!",
 "imparato": "HAI IMPARATO I NOMI DEI PARENTI, I POSSESSIVI E A DESCRIVERE LE PERSONE.",
 "intro": [
  [
   "lin",
   "OGGI LA MIA NONNA COMPIE 80 ANNI! FACCIAMO UNA FESTA IN VIDEOCHIAMATA CON TUTTA LA FAMIGLIA."
  ],
  [
   "eneida",
   "CHE BELLO! TI AIUTO A PREPARARE TUTTO."
  ],
  [
   "eneida",
   "CI SONO 4 PORTE. CON LE 4 LETTERE SCOPRI CHE COSA MANDA LA FAMIGLIA ALLA NONNA!"
  ]
 ],
 "finale": [
  [
   "lin",
   "TUTTI SONO IN VIDEOCHIAMATA. LA NONNA È FELICE!"
  ],
  [
   "eneida",
   "CHE COSA MANDANO TUTTI ALLA NONNA? SCRIVI LA PAROLA SEGRETA."
  ]
 ],
 "vittoria": "TUTTI DICONO: «TANTI AUGURI, NONNA! TANTI BACI DA TUTTA LA FAMIGLIA!»",
 "stanze": [
  {
   "id": "parenti",
   "titolo": "I PARENTI",
   "icona": "👨‍👩‍👧",
   "lettera": "B",
   "chi": "eneida",
   "lezione": {
    "titolo": "LA FAMIGLIA",
    "link": "letture/famiglia.html"
   },
   "storia": [
    [
     "eneida",
     "CHI C'È NELLA TUA FAMIGLIA?"
    ]
   ],
   "fine": [
    "lin",
    "CONOSCO TUTTI I PARENTI!"
   ],
   "prove": [
    {
     "tipo": "scelta",
     "domanda": "LA MADRE DI MIA MADRE È MIA…",
     "icona": "👵",
     "risposte": [
      {
       "t": "NONNA",
       "i": "👵"
      },
      {
       "t": "ZIA",
       "i": "👩"
      },
      {
       "t": "SORELLA",
       "i": "👧"
      }
     ],
     "correct": 0,
     "aiuto": "È LA FESTEGGIATA DI OGGI!",
     "spiega": "LA MADRE DELLA MAMMA È LA NONNA."
    },
    {
     "tipo": "scelta",
     "domanda": "IL FRATELLO DI MIO PADRE È MIO…",
     "icona": "👨",
     "risposte": [
      {
       "t": "ZIO",
       "i": "👨"
      },
      {
       "t": "CUGINO",
       "i": "👦"
      },
      {
       "t": "NONNO",
       "i": "👴"
      }
     ],
     "correct": 0,
     "aiuto": "È DELLA GENERAZIONE DEI GENITORI.",
     "spiega": "IL FRATELLO DEL PAPÀ È LO ZIO."
    },
    {
     "tipo": "completa",
     "domanda": "COMPLETA.",
     "frase": "IL FIGLIO DI MIO ZIO È MIO ___.",
     "icona": "👦",
     "risposte": [
      "CUGINO",
      "NIPOTE",
      "FRATELLO"
     ],
     "correct": 0,
     "aiuto": "È DELLA MIA GENERAZIONE.",
     "spiega": "IL FIGLIO DELLO ZIO È IL CUGINO."
    }
   ]
  },
  {
   "id": "possessivi",
   "titolo": "MIO, TUO, SUO",
   "icona": "🔑",
   "lettera": "A",
   "chi": "eneida",
   "lezione": {
    "titolo": "I POSSESSIVI",
    "link": "possessivi/esercizi.html"
   },
   "storia": [
    [
     "eneida",
     "ORA PARLIAMO DEI REGALI: DI CHI SONO?"
    ]
   ],
   "fine": [
    "lin",
    "CHE FACILE!"
   ],
   "prove": [
    {
     "tipo": "completa",
     "domanda": "COMPLETA.",
     "frase": "___ NONNA SI CHIAMA FATIMA.",
     "icona": "👵",
     "risposte": [
      "MIA",
      "LA MIA",
      "MIO"
     ],
     "correct": 0,
     "aiuto": "CON I PARENTI AL SINGOLARE: NIENTE ARTICOLO.",
     "spiega": "MIA NONNA (SENZA «LA»)."
    },
    {
     "tipo": "completa",
     "domanda": "COMPLETA.",
     "frase": "___ FRATELLI ABITANO IN FRANCIA.",
     "icona": "👬",
     "risposte": [
      "I MIEI",
      "MIEI",
      "LE MIE"
     ],
     "correct": 0,
     "aiuto": "AL PLURALE CI VUOLE L'ARTICOLO.",
     "spiega": "I MIEI FRATELLI."
    },
    {
     "tipo": "vf",
     "domanda": "«SUA SORELLA» PUÒ ESSERE LA SORELLA DI LUI O DI LEI.",
     "icona": "👧",
     "correct": true,
     "aiuto": "SUO/SUA DIPENDE DALLA COSA, NON DALLA PERSONA.",
     "spiega": "VERO."
    }
   ]
  },
  {
   "id": "descrivere",
   "titolo": "COM'È?",
   "icona": "🪞",
   "lettera": "C",
   "chi": "eneida",
   "lezione": {
    "titolo": "GLI AGGETTIVI",
    "link": "aggettivi/esercizi.html"
   },
   "storia": [
    [
     "lin",
     "DESCRIVO LA MIA FAMIGLIA A ENEIDA."
    ]
   ],
   "fine": [
    "eneida",
    "CHE BELLA FAMIGLIA!"
   ],
   "prove": [
    {
     "tipo": "scelta",
     "domanda": "IL NONNO HA 90 ANNI. È…",
     "icona": "👴",
     "risposte": [
      {
       "t": "ANZIANO",
       "i": "👴"
      },
      {
       "t": "GIOVANE",
       "i": "🧒"
      },
      {
       "t": "PICCOLO",
       "i": "👶"
      }
     ],
     "correct": 0,
     "aiuto": "HA TANTI ANNI.",
     "spiega": "CON TANTI ANNI SI È ANZIANI."
    },
    {
     "tipo": "completa",
     "domanda": "COMPLETA.",
     "frase": "LE MIE CUGINE SONO ALT___.",
     "icona": "👭",
     "risposte": [
      "E",
      "I",
      "A"
     ],
     "correct": 0,
     "aiuto": "CUGINE: FEMMINILE PLURALE.",
     "spiega": "LE CUGINE SONO ALTE."
    },
    {
     "tipo": "scelta",
     "domanda": "RIDE SEMPRE ED È CONTENTA. È…",
     "icona": "😄",
     "risposte": [
      {
       "t": "ALLEGRA",
       "i": "😄"
      },
      {
       "t": "TRISTE",
       "i": "😢"
      },
      {
       "t": "ARRABBIATA",
       "i": "😠"
      }
     ],
     "correct": 0,
     "aiuto": "IL CONTRARIO DI TRISTE.",
     "spiega": "È ALLEGRA."
    }
   ]
  },
  {
   "id": "festa",
   "titolo": "LA FESTA",
   "icona": "🎂",
   "lettera": "I",
   "chi": "eneida",
   "lezione": {
    "titolo": "FESTE E TRADIZIONI",
    "link": "feste/"
   },
   "storia": [
    [
     "eneida",
     "ULTIMA PORTA: GLI AUGURI!"
    ]
   ],
   "fine": [
    "lin",
    "LA FESTA COMINCIA!"
   ],
   "prove": [
    {
     "tipo": "scelta",
     "domanda": "PER IL COMPLEANNO SI DICE…",
     "icona": "🎂",
     "risposte": [
      {
       "t": "TANTI AUGURI!",
       "i": "🎉"
      },
      {
       "t": "BUON NATALE!",
       "i": "🎄"
      },
      {
       "t": "BUON VIAGGIO!",
       "i": "✈️"
      }
     ],
     "correct": 0,
     "aiuto": "È IL GIORNO IN CUI SEI NATO.",
     "spiega": "TANTI AUGURI! / BUON COMPLEANNO!"
    },
    {
     "tipo": "completa",
     "domanda": "COMPLETA.",
     "frase": "LA NONNA ___ 80 ANNI.",
     "icona": "👵",
     "risposte": [
      "HA",
      "È",
      "FA"
     ],
     "correct": 0,
     "aiuto": "L'ETÀ SI DICE CON AVERE.",
     "spiega": "HA 80 ANNI."
    },
    {
     "tipo": "vf",
     "domanda": "SULLA TORTA CI SONO LE CANDELINE.",
     "icona": "🕯️",
     "correct": true,
     "aiuto": "SI SOFFIANO!",
     "spiega": "VERO."
    }
   ]
  }
 ],
 "sito": "https://italianol2sai.github.io/",
 "chiaveSalva": "missione-famiglia-v1"
};
