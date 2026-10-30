// Contenuti del gioco «MISSIONE SALUTE» (generati da _strumenti/missioni.py: modificare lì).
window.MISSIONE = {
 "titolo": "MISSIONE SALUTE",
 "sottotitolo": "AIUTA KWAME A STARE MEGLIO!",
 "parolaSegreta": "CURA",
 "guida": "michele",
 "protagonista": "kwame",
 "etichetta": "ITALIANO L2 · LA SALUTE",
 "portaFinale": "LA PORTA DELLA FARMACIA",
 "grazie": "GRAZIE! ADESSO STO MEGLIO!",
 "imparato": "HAI IMPARATO LE PARTI DEL CORPO, A DIRE CHE COSA TI FA MALE, A PARLARE CON IL MEDICO E IN FARMACIA.",
 "intro": [
  [
   "kwame",
   "CIAO, SONO KWAME. STAMATTINA NON STO BENE: HO MAL DI TESTA E MAL DI GOLA."
  ],
  [
   "michele",
   "IO SONO MICHELE. TI AIUTO IO, KWAME! ANDIAMO INSIEME DAL MEDICO E IN FARMACIA."
  ],
  [
   "michele",
   "CI SONO 4 PORTE. DIETRO OGNI PORTA C'È UNA LETTERA. CON LE 4 LETTERE SCOPRI LA PAROLA SEGRETA!"
  ]
 ],
 "finale": [
  [
   "kwame",
   "SONO IN FARMACIA CON LA RICETTA DEL MEDICO."
  ],
  [
   "michele",
   "CHE COSA TI SERVE PER GUARIRE? SCRIVI LA PAROLA SEGRETA CON LE 4 LETTERE."
  ]
 ],
 "vittoria": "IL FARMACISTA DICE: «ECCO LA TUA CURA, KWAME. PRENDI LO SCIROPPO TRE VOLTE AL GIORNO. GUARISCI PRESTO!»",
 "stanze": [
  {
   "id": "corpo",
   "titolo": "IL CORPO",
   "icona": "🧍",
   "lettera": "C",
   "chi": "michele",
   "lezione": {
    "titolo": "IL CORPO E IL DOTTORE",
    "link": "corpo-dottore/"
   },
   "storia": [
    [
     "michele",
     "PRIMA RIPASSIAMO LE PARTI DEL CORPO."
    ]
   ],
   "fine": [
    "kwame",
    "CONOSCO LE PARTI DEL CORPO!"
   ],
   "prove": [
    {
     "tipo": "scelta",
     "domanda": "CON CHE COSA VEDI?",
     "icona": "👀",
     "risposte": [
      {
       "t": "CON GLI OCCHI",
       "i": "👀"
      },
      {
       "t": "CON LE ORECCHIE",
       "i": "👂"
      },
      {
       "t": "CON I PIEDI",
       "i": "🦶"
      }
     ],
     "correct": 0,
     "aiuto": "SONO DUE, SULLA FACCIA.",
     "spiega": "VEDO CON GLI OCCHI."
    },
    {
     "tipo": "scelta",
     "domanda": "CON CHE COSA SENTI LA MUSICA?",
     "icona": "🎵",
     "risposte": [
      {
       "t": "CON LE ORECCHIE",
       "i": "👂"
      },
      {
       "t": "CON IL NASO",
       "i": "👃"
      },
      {
       "t": "CON LE MANI",
       "i": "✋"
      }
     ],
     "correct": 0,
     "aiuto": "SONO AI LATI DELLA TESTA.",
     "spiega": "SENTO CON LE ORECCHIE."
    },
    {
     "tipo": "completa",
     "domanda": "COMPLETA.",
     "frase": "LA MANO HA CINQUE ___.",
     "icona": "✋",
     "risposte": [
      "DITA",
      "DITI",
      "DITE"
     ],
     "correct": 0,
     "aiuto": "IL DITO → LE DITA: È UN PLURALE SPECIALE.",
     "spiega": "IL DITO, LE DITA."
    }
   ]
  },
  {
   "id": "male",
   "titolo": "CHE COSA TI FA MALE?",
   "icona": "🤕",
   "lettera": "U",
   "chi": "michele",
   "lezione": {
    "titolo": "IL CORPO E IL DOTTORE",
    "link": "corpo-dottore/"
   },
   "storia": [
    [
     "kwame",
     "MICHELE, COME DICO AL MEDICO CHE STO MALE?"
    ]
   ],
   "fine": [
    "michele",
    "BRAVO! ADESSO SAI DIRE CHE COSA TI FA MALE."
   ],
   "prove": [
    {
     "tipo": "scelta",
     "domanda": "KWAME DICE: «MI FA MALE…»",
     "icona": "🤕",
     "risposte": [
      {
       "t": "LA TESTA",
       "i": "🧠"
      },
      {
       "t": "I DENTI",
       "i": "🦷"
      },
      {
       "t": "LE GAMBE",
       "i": "🦵"
      }
     ],
     "correct": 0,
     "aiuto": "MI FA MALE + UNA COSA SOLA.",
     "spiega": "MI FA MALE LA TESTA. MI FANNO MALE I DENTI."
    },
    {
     "tipo": "completa",
     "domanda": "COMPLETA.",
     "frase": "MI ___ MALE I PIEDI.",
     "icona": "🦶",
     "risposte": [
      "FANNO",
      "FA",
      "FAI"
     ],
     "correct": 0,
     "aiuto": "I PIEDI SONO DUE: PLURALE.",
     "spiega": "MI FANNO MALE + PLURALE."
    },
    {
     "tipo": "vf",
     "domanda": "«HO LA FEBBRE» VUOL DIRE: LA MIA TEMPERATURA È ALTA.",
     "icona": "🌡️",
     "correct": true,
     "aiuto": "PENSA AL TERMOMETRO.",
     "spiega": "VERO. SOPRA 37 °C HO LA FEBBRE."
    }
   ]
  },
  {
   "id": "medico",
   "titolo": "DAL MEDICO",
   "icona": "🩺",
   "lettera": "R",
   "chi": "michele",
   "lezione": {
    "titolo": "IL CORPO E IL DOTTORE",
    "link": "corpo-dottore/"
   },
   "storia": [
    [
     "michele",
     "ECCO LO STUDIO DEL MEDICO DI BASE. ENTRIAMO!"
    ]
   ],
   "fine": [
    "kwame",
    "IL MEDICO MI HA DATO LA RICETTA!"
   ],
   "prove": [
    {
     "tipo": "scelta",
     "domanda": "IL MEDICO CHIEDE: «CHE COSA SI SENTE?» KWAME RISPONDE:",
     "icona": "🩺",
     "risposte": [
      {
       "t": "HO MAL DI GOLA E LA TOSSE.",
       "i": "😷"
      },
      {
       "t": "SONO LE TRE.",
       "i": "🕒"
      },
      {
       "t": "ABITO A BARI.",
       "i": "🏠"
      }
     ],
     "correct": 0,
     "aiuto": "IL MEDICO VUOLE SAPERE COME STAI.",
     "spiega": "RISPONDO CON I SINTOMI: MAL DI GOLA, TOSSE, FEBBRE."
    },
    {
     "tipo": "scelta",
     "domanda": "PER COMPRARE ALCUNE MEDICINE SERVE…",
     "icona": "📄",
     "risposte": [
      {
       "t": "LA RICETTA",
       "i": "📄"
      },
      {
       "t": "IL BIGLIETTO",
       "i": "🎫"
      },
      {
       "t": "LO SCONTRINO",
       "i": "🧾"
      }
     ],
     "correct": 0,
     "aiuto": "LA SCRIVE IL MEDICO.",
     "spiega": "LA RICETTA È IL FOGLIO DEL MEDICO PER LA FARMACIA."
    },
    {
     "tipo": "vf",
     "domanda": "IN UN'EMERGENZA CHIAMO IL 112.",
     "icona": "🚑",
     "correct": true,
     "aiuto": "È IL NUMERO UNICO DI EMERGENZA.",
     "spiega": "VERO. IL 112 È IL NUMERO PER LE EMERGENZE."
    }
   ]
  },
  {
   "id": "farmacia",
   "titolo": "IN FARMACIA",
   "icona": "💊",
   "lettera": "A",
   "chi": "michele",
   "lezione": {
    "titolo": "IN FARMACIA E AL PRONTO SOCCORSO",
    "link": "farmacia/"
   },
   "storia": [
    [
     "michele",
     "ULTIMA PORTA: LA FARMACIA. C'È LA CROCE VERDE!"
    ]
   ],
   "fine": [
    "kwame",
    "HO TUTTO! GRAZIE, MICHELE."
   ],
   "prove": [
    {
     "tipo": "scelta",
     "domanda": "HO LA TOSSE. CHE COSA COMPRO?",
     "icona": "😷",
     "risposte": [
      {
       "t": "LO SCIROPPO",
       "i": "🧴"
      },
      {
       "t": "IL CEROTTO",
       "i": "🩹"
      },
      {
       "t": "IL TERMOMETRO",
       "i": "🌡️"
      }
     ],
     "correct": 0,
     "aiuto": "SI BEVE CON IL CUCCHIAIO.",
     "spiega": "PER LA TOSSE PRENDO LO SCIROPPO."
    },
    {
     "tipo": "completa",
     "domanda": "COMPLETA.",
     "frase": "PRENDA UNA PASTIGLIA DUE VOLTE AL ___.",
     "icona": "💊",
     "risposte": [
      "GIORNO",
      "ORA",
      "MESE"
     ],
     "correct": 0,
     "aiuto": "MATTINA E SERA.",
     "spiega": "DUE VOLTE AL GIORNO = MATTINA E SERA."
    },
    {
     "tipo": "vf",
     "domanda": "LA FARMACIA HA UNA CROCE VERDE.",
     "icona": "➕",
     "correct": true,
     "aiuto": "GUARDA LE INSEGNE IN CITTÀ.",
     "spiega": "VERO. LA CROCE VERDE ACCESA = FARMACIA."
    }
   ]
  }
 ],
 "sito": "https://italianol2sai.github.io/",
 "chiaveSalva": "missione-salute-v1"
};
