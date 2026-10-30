// Contenuti del gioco «MISSIONE FAMIGLIA» (generati da _strumenti/missioni.py: modificare lì).
window.MISSIONE = {
 "titolo": "MISSIONE FAMIGLIA",
 "sottotitolo": "ORGANIZZA IL MATRIMONIO DI MARYAM E MAKARI!",
 "parolaSegreta": "FEDE",
 "guida": "eneida",
 "protagonista": "maryam2",
 "etichetta": "ITALIANO L2 · LA FAMIGLIA",
 "portaFinale": "LA PORTA DELLA FESTA",
 "grazie": "GRAZIE! È UN MATRIMONIO BELLISSIMO!",
 "imparato": "HAI IMPARATO I NOMI DEI PARENTI, I POSSESSIVI E A DESCRIVERE LE PERSONE.",
 "intro": [
  [
   "maryam2",
   "GRANDE NOTIZIA: IO E MAKARI CI SPOSIAMO! MA C'È TANTO DA ORGANIZZARE…"
  ],
  [
   "makari",
   "CIAO, SONO MAKARI. DOBBIAMO INVITARE TUTTE LE NOSTRE FAMIGLIE!"
  ],
  [
   "eneida",
   "CHE BELLO! SONO ENEIDA, LA COORDINATRICE. VI AIUTO A ORGANIZZARE TUTTO."
  ],
  [
   "eneida",
   "CI SONO 4 PORTE. CON LE 4 LETTERE SCOPRI CHE COSA SI SCAMBIANO GLI SPOSI!"
  ]
 ],
 "finale": [
  [
   "maryam2",
   "SIAMO DAVANTI AL SINDACO. È IL MOMENTO DEGLI ANELLI!"
  ],
  [
   "eneida",
   "COME SI CHIAMA L'ANELLO DEL MATRIMONIO? SCRIVI LA PAROLA SEGRETA."
  ]
 ],
 "vittoria": "TUTTI DICONO: «VIVA GLI SPOSI! AUGURI, MARYAM E MAKARI!»",
 "stanze": [
  {
   "id": "parenti",
   "titolo": "GLI INVITATI",
   "icona": "👨‍👩‍👧",
   "lettera": "F",
   "chi": "eneida",
   "lezione": {
    "titolo": "LA FAMIGLIA",
    "link": "letture/famiglia.html"
   },
   "storia": [
    [
     "eneida",
     "PRIMA LA LISTA DEGLI INVITATI. CHI C'È NELLA VOSTRA FAMIGLIA?"
    ]
   ],
   "fine": [
    "maryam2",
    "ABBIAMO INVITATO TUTTI I PARENTI!"
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
     "aiuto": "È ANZIANA E MOLTO IMPORTANTE ALLA FESTA!",
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
     "frase": "LA MADRE DI MAKARI È LA ___ DI MARYAM.",
     "icona": "👩",
     "risposte": [
      "SUOCERA",
      "SORELLA",
      "CUGINA"
     ],
     "correct": 0,
     "aiuto": "È LA MAMMA DEL MARITO.",
     "spiega": "LA MADRE DEL MARITO È LA SUOCERA."
    }
   ]
  },
  {
   "id": "possessivi",
   "titolo": "MIO, TUO, SUO",
   "icona": "🔑",
   "lettera": "E",
   "chi": "eneida",
   "lezione": {
    "titolo": "I POSSESSIVI",
    "link": "possessivi/esercizi.html"
   },
   "storia": [
    [
     "eneida",
     "ORA I REGALI: DI CHI SONO?"
    ]
   ],
   "fine": [
    "makari",
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
     "frase": "___ FRATELLI ARRIVANO DALLA FRANCIA.",
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
   "lettera": "D",
   "chi": "eneida",
   "lezione": {
    "titolo": "GLI AGGETTIVI",
    "link": "aggettivi/esercizi.html"
   },
   "storia": [
    [
     "maryam2",
     "ENEIDA, TI DESCRIVO IL MIO VESTITO E LA FAMIGLIA DI MAKARI."
    ]
   ],
   "fine": [
    "eneida",
    "CHE BELLO TUTTO!"
   ],
   "prove": [
    {
     "tipo": "scelta",
     "domanda": "IL VESTITO DA SPOSA È…",
     "icona": "👰",
     "risposte": [
      {
       "t": "BIANCO E LUNGO",
       "i": "👰"
      },
      {
       "t": "NERO E CORTO",
       "i": "🖤"
      },
      {
       "t": "VERDE E VECCHIO",
       "i": "🟢"
      }
     ],
     "correct": 0,
     "aiuto": "È IL COLORE PIÙ CLASSICO.",
     "spiega": "IL VESTITO DA SPOSA È SPESSO BIANCO E LUNGO."
    },
    {
     "tipo": "completa",
     "domanda": "COMPLETA.",
     "frase": "LE SORELLE DI MAKARI SONO ALT___.",
     "icona": "👭",
     "risposte": [
      "E",
      "I",
      "A"
     ],
     "correct": 0,
     "aiuto": "SORELLE: FEMMINILE PLURALE.",
     "spiega": "LE SORELLE SONO ALTE."
    },
    {
     "tipo": "scelta",
     "domanda": "MAKARI RIDE SEMPRE ED È CONTENTO. È…",
     "icona": "😄",
     "risposte": [
      {
       "t": "ALLEGRO",
       "i": "😄"
      },
      {
       "t": "TRISTE",
       "i": "😢"
      },
      {
       "t": "ARRABBIATO",
       "i": "😠"
      }
     ],
     "correct": 0,
     "aiuto": "IL CONTRARIO DI TRISTE.",
     "spiega": "È ALLEGRO."
    }
   ]
  },
  {
   "id": "festa",
   "titolo": "IL MATRIMONIO",
   "icona": "💍",
   "lettera": "E",
   "chi": "eneida",
   "lezione": {
    "titolo": "FESTE E TRADIZIONI",
    "link": "feste/"
   },
   "storia": [
    [
     "eneida",
     "ULTIMA PORTA: IL GRANDE GIORNO!"
    ]
   ],
   "fine": [
    "makari",
    "LA FESTA COMINCIA!"
   ],
   "prove": [
    {
     "tipo": "scelta",
     "domanda": "AGLI SPOSI SI DICE…",
     "icona": "💐",
     "risposte": [
      {
       "t": "AUGURI E FIGLI MASCHI… O FEMMINE!",
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
     "aiuto": "È UN AUGURIO PER LA NUOVA FAMIGLIA.",
     "spiega": "AGLI SPOSI SI FANNO GLI AUGURI. «VIVA GLI SPOSI!»"
    },
    {
     "tipo": "completa",
     "domanda": "COMPLETA.",
     "frase": "MARYAM E MAKARI ___ SPOSANO IN COMUNE.",
     "icona": "🏛️",
     "risposte": [
      "SI",
      "CI",
      "LO"
     ],
     "correct": 0,
     "aiuto": "SPOSARSI È UN VERBO RIFLESSIVO.",
     "spiega": "SI SPOSANO."
    },
    {
     "tipo": "vf",
     "domanda": "AL MATRIMONIO GLI SPOSI REGALANO I CONFETTI AGLI INVITATI.",
     "icona": "🍬",
     "correct": true,
     "aiuto": "SONO DOLCI BIANCHI CON LA MANDORLA.",
     "spiega": "VERO: È LA BOMBONIERA CON I CONFETTI."
    }
   ]
  }
 ],
 "sito": "https://italianol2sai.github.io/",
 "chiaveSalva": "missione-famiglia-v1"
};
