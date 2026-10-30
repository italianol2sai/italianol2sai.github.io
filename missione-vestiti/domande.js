// Contenuti del gioco «MISSIONE VESTITI» (generati da _strumenti/missioni.py: modificare lì).
window.MISSIONE = {
 "titolo": "MISSIONE VESTITI",
 "sottotitolo": "TROVA I VESTITI GIUSTI PER IL COLLOQUIO!",
 "parolaSegreta": "MODA",
 "guida": "giulio",
 "protagonista": "mohammad",
 "etichetta": "ITALIANO L2 · I VESTITI",
 "portaFinale": "LA PORTA DEL NEGOZIO",
 "grazie": "GRAZIE! ORA SONO PRONTO!",
 "imparato": "HAI IMPARATO I VESTITI, I COLORI, COME SI COMPRA IN UN NEGOZIO E CHE COSA SI METTE CON IL TEMPO DIVERSO.",
 "intro": [
  [
   "mohammad",
   "LUNEDÌ HO UN COLLOQUIO DI LAVORO. DEVO COMPRARE DEI VESTITI NUOVI!"
  ],
  [
   "giulio",
   "SONO GIULIO. ANDIAMO INSIEME AL NEGOZIO."
  ],
  [
   "giulio",
   "CI SONO 4 PORTE. CON LE 4 LETTERE SCOPRI LA PAROLA SEGRETA!"
  ]
 ],
 "finale": [
  [
   "mohammad",
   "HO LA GIACCA, LA CAMICIA E LE SCARPE NUOVE!"
  ],
  [
   "giulio",
   "SEI ELEGANTISSIMO! SEI ALLA… SCRIVI LA PAROLA SEGRETA."
  ]
 ],
 "vittoria": "GIULIO DICE: «SEI ALLA MODA, MOHAMMAD! IN BOCCA AL LUPO PER IL COLLOQUIO!»",
 "stanze": [
  {
   "id": "capi",
   "titolo": "I VESTITI",
   "icona": "👕",
   "lettera": "M",
   "chi": "giulio",
   "lezione": {
    "titolo": "I VESTITI",
    "link": "abbigliamento/"
   },
   "storia": [
    [
     "giulio",
     "PRIMA RIPASSIAMO I NOMI DEI VESTITI."
    ]
   ],
   "fine": [
    "mohammad",
    "CONOSCO I VESTITI!"
   ],
   "prove": [
    {
     "tipo": "scelta",
     "domanda": "SI METTE SOPRA LA CAMICIA, PER IL COLLOQUIO.",
     "icona": "🧥",
     "risposte": [
      {
       "t": "LA GIACCA",
       "i": "🧥"
      },
      {
       "t": "IL COSTUME",
       "i": "🩱"
      },
      {
       "t": "IL PIGIAMA",
       "i": "🛌"
      }
     ],
     "correct": 0,
     "aiuto": "È ELEGANTE.",
     "spiega": "LA GIACCA SI METTE SOPRA LA CAMICIA."
    },
    {
     "tipo": "scelta",
     "domanda": "SI METTONO AI PIEDI.",
     "icona": "👞",
     "risposte": [
      {
       "t": "LE SCARPE",
       "i": "👞"
      },
      {
       "t": "I GUANTI",
       "i": "🧤"
      },
      {
       "t": "IL CAPPELLO",
       "i": "🎩"
      }
     ],
     "correct": 0,
     "aiuto": "CAMMINI CON…",
     "spiega": "LE SCARPE SI METTONO AI PIEDI."
    },
    {
     "tipo": "completa",
     "domanda": "COMPLETA.",
     "frase": "UN ___ DI PANTALONI.",
     "icona": "👖",
     "risposte": [
      "PAIO",
      "PAIA",
      "PEZZO"
     ],
     "correct": 0,
     "aiuto": "PER LE COSE DOPPIE: UN ___ DI SCARPE.",
     "spiega": "UN PAIO DI PANTALONI."
    }
   ]
  },
  {
   "id": "colori",
   "titolo": "I COLORI",
   "icona": "🎨",
   "lettera": "O",
   "chi": "giulio",
   "lezione": {
    "titolo": "VESTITI E COLORI",
    "link": "parole/vestiti.html"
   },
   "storia": [
    [
     "giulio",
     "DI CHE COLORE LA VUOI?"
    ]
   ],
   "fine": [
    "mohammad",
    "MI PIACE IL BLU!"
   ],
   "prove": [
    {
     "tipo": "completa",
     "domanda": "COMPLETA.",
     "frase": "LA CAMICIA BIANC___.",
     "icona": "👔",
     "risposte": [
      "A",
      "O",
      "HE"
     ],
     "correct": 0,
     "aiuto": "CAMICIA È FEMMINILE.",
     "spiega": "LA CAMICIA BIANCA."
    },
    {
     "tipo": "completa",
     "domanda": "COMPLETA.",
     "frase": "LE SCARPE NER___.",
     "icona": "👞",
     "risposte": [
      "E",
      "I",
      "O"
     ],
     "correct": 0,
     "aiuto": "SCARPE: FEMMINILE PLURALE.",
     "spiega": "LE SCARPE NERE."
    },
    {
     "tipo": "vf",
     "domanda": "«BLU» NON CAMBIA: UNA GIACCA BLU, DUE GIACCHE BLU.",
     "icona": "🔵",
     "correct": true,
     "aiuto": "ALCUNI COLORI NON CAMBIANO MAI.",
     "spiega": "VERO. ANCHE ROSA E VIOLA NON CAMBIANO."
    }
   ]
  },
  {
   "id": "negozio",
   "titolo": "AL NEGOZIO",
   "icona": "🛍️",
   "lettera": "D",
   "chi": "giulio",
   "lezione": {
    "titolo": "I VESTITI",
    "link": "abbigliamento/"
   },
   "storia": [
    [
     "giulio",
     "ENTRIAMO NEL NEGOZIO."
    ]
   ],
   "fine": [
    "mohammad",
    "HO COMPRATO TUTTO!"
   ],
   "prove": [
    {
     "tipo": "scelta",
     "domanda": "LA COMMESSA CHIEDE: «CHE TAGLIA PORTA?»",
     "icona": "📏",
     "risposte": [
      {
       "t": "LA 50.",
       "i": "📏"
      },
      {
       "t": "IL 42 DI SCARPE.",
       "i": "👞"
      },
      {
       "t": "40 EURO.",
       "i": "💶"
      }
     ],
     "correct": 0,
     "aiuto": "PER I VESTITI: 46, 48, 50… O S, M, L.",
     "spiega": "LA TAGLIA DEI VESTITI È UN NUMERO O UNA LETTERA."
    },
    {
     "tipo": "scelta",
     "domanda": "VUOI PROVARE LA GIACCA. CHE COSA CHIEDI?",
     "icona": "🚪",
     "risposte": [
      {
       "t": "POSSO PROVARLA?",
       "i": "🙂"
      },
      {
       "t": "QUANTO È ALTA?",
       "i": "📐"
      },
      {
       "t": "C'È IL BAGNO?",
       "i": "🚻"
      }
     ],
     "correct": 0,
     "aiuto": "C'È IL CAMERINO.",
     "spiega": "POSSO PROVARLA? DOV'È IL CAMERINO?"
    },
    {
     "tipo": "completa",
     "domanda": "COMPLETA.",
     "frase": "QUANTO ___ QUESTE SCARPE?",
     "icona": "💶",
     "risposte": [
      "COSTANO",
      "COSTA",
      "SONO COSTA"
     ],
     "correct": 0,
     "aiuto": "LE SCARPE: PLURALE.",
     "spiega": "QUANTO COSTANO?"
    }
   ]
  },
  {
   "id": "tempo",
   "titolo": "CHE COSA METTO?",
   "icona": "🌦️",
   "lettera": "A",
   "chi": "giulio",
   "lezione": {
    "titolo": "IL TEMPO",
    "link": "tempo/"
   },
   "storia": [
    [
     "giulio",
     "LUNEDÌ CHE TEMPO FA?"
    ]
   ],
   "fine": [
    "mohammad",
    "SONO PRONTO PER OGNI TEMPO!"
   ],
   "prove": [
    {
     "tipo": "scelta",
     "domanda": "PIOVE. CHE COSA PRENDI?",
     "icona": "🌧️",
     "risposte": [
      {
       "t": "L'OMBRELLO",
       "i": "☂️"
      },
      {
       "t": "GLI OCCHIALI DA SOLE",
       "i": "🕶️"
      },
      {
       "t": "IL COSTUME",
       "i": "🩱"
      }
     ],
     "correct": 0,
     "aiuto": "TI PROTEGGE DALL'ACQUA.",
     "spiega": "CON LA PIOGGIA PRENDO L'OMBRELLO."
    },
    {
     "tipo": "scelta",
     "domanda": "FA FREDDO. CHE COSA METTI?",
     "icona": "❄️",
     "risposte": [
      {
       "t": "IL CAPPOTTO",
       "i": "🧥"
      },
      {
       "t": "I PANTALONCINI",
       "i": "🩳"
      },
      {
       "t": "I SANDALI",
       "i": "🩴"
      }
     ],
     "correct": 0,
     "aiuto": "È PESANTE E CALDO.",
     "spiega": "D'INVERNO METTO IL CAPPOTTO."
    },
    {
     "tipo": "vf",
     "domanda": "D'ESTATE A BARI FA MOLTO CALDO.",
     "icona": "☀️",
     "correct": true,
     "aiuto": "LUGLIO E AGOSTO…",
     "spiega": "VERO."
    }
   ]
  }
 ],
 "sito": "https://italianol2sai.github.io/",
 "chiaveSalva": "missione-vestiti-v1"
};
