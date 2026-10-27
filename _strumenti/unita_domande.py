from genera import eq, has, all_

INTERR = [("", "AUTOBUS PRENDI?", "che|quale"), ("", "GIORNALE LEGGI?", "che|quale"),
          ("", "FATE DOMENICA?", "cosa|che cosa|che"), ("DI", "PARLA IL TELEGIORNALE?", "cosa|che cosa|che"),
          ("", "È LA STRADA PER LA STAZIONE?", "qual|quale|dov|dov'|dove"), ("", "PAGATE PER L'AFFITTO DI CASA?", "quanto"),
          ("", "POSSO TROVARE UNA GELATERIA?", "dove"), ("DA", "VIENE, SIGNORINA?", "dove"),
          ("", "CARAMELLE HAI MANGIATO?", "quante"), ("DA", "TEMPO STUDI L'ITALIANO?", "quanto"),
          ("SU", "GIORNALE POSSO CERCARE UN LAVORO?", "quale|che"), ("", "DURA LA LEZIONE?", "quanto"),
          ("", "GIORNI ALLA SETTIMANA VAI A SCUOLA?", "quanti"), ("", "SI TROVA LA SCUOLA?", "dove"),
          ("IN", "CITTÀ ABITA TUO FRATELLO?", "quale|che"), ("DI", "TESSUTO È QUESTA GIACCA?", "che|quale"),
          ("A", "HAI TELEFONATO?", "chi"), ("", "NON SEI VENUTO A SCUOLA?", "perché|perche"),
          ("", "TI CHIAMI?", "come"), ("", "ANNI HAI?", "quanti")]

RISPOSTE = [("MI CHIAMO AHMED.", "COME TI CHIAMI?"), ("VENGO DAL SENEGAL.", "DA CHE PAESE VIENI?"),
            ("HO 30 ANNI.", "QUANTI ANNI HAI?"), ("ABITO IN VIA PIAVE 12.", "QUAL È IL TUO INDIRIZZO?"),
            ("FACCIO IL MURATORE.", "CHE LAVORO FAI?"), ("ABITO CON MIA MOGLIE E I MIEI FIGLI.", "CON CHI ABITI?"),
            ("SONO IN ITALIA DA DUE ANNI.", "DA QUANTO TEMPO SEI IN ITALIA?"), ("COSTA 2 EURO.", "QUANTO COSTA?"),
            ("VADO A SCUOLA IL LUNEDÌ E IL GIOVEDÌ.", "QUANDO VAI A SCUOLA?"),
            ("PERCHÉ HO MAL DI TESTA.", "PERCHÉ NON VIENI?")]

TIPO = [("MARCO.", "CHI?"), ("A CASA.", "DOVE?"), ("DOMANI.", "QUANDO?"), ("10 EURO.", "QUANTO?"),
        ("UN PANINO.", "CHE COSA?"), ("IN AUTOBUS.", "COME?"), ("PERCHÉ SONO STANCO.", "PERCHÉ?"),
        ("ALLE OTTO.", "QUANDO?"), ("LA MIA AMICA FATIMA.", "CHI?"), ("A PIEDI.", "COME?")]

DOMANDE = {
 "title": "❓ Le domande · Esercizi",
 "store": "domande",
 "upper": True,
 "sections": [
  {"part": "Le parole per fare domande"},
  {"id": "e1", "title": "1 · Che domanda è?", "short": "1 · Che domanda è?", "type": "choice",
   "opts": ["CHI?", "CHE COSA?", "DOVE?", "QUANDO?", "QUANTO?", "COME?", "PERCHÉ?"],
   "cons": "Leggi la risposta. Che parola c'era nella domanda?",
   "items": [{"q": f"{i}. «{r}»"} for i, (r, _) in enumerate(TIPO, 1)], "k": [eq(a) for _, a in TIPO]},
  {"id": "e2", "title": "2 · Completa la domanda", "short": "2 · Completa la domanda", "type": "text", "w": "s",
   "cons": "Scrivi la parola giusta.", "bank": "CHI · CHE · COSA · QUALE · DOVE · QUANDO · QUANTO · QUANTI · QUANTE · COME · PERCHÉ",
   "items": [{"pre": f"{i}. {a}", "post": b} for i, (a, b, _) in enumerate(INTERR, 1)],
   "k": [eq(*r.split("|")) for *_, r in INTERR]},
  {"id": "e3", "title": "3 · Scegli la domanda giusta", "short": "3 · Domanda e risposta", "type": "select",
   "cons": "Leggi la risposta e scegli la domanda.", "opts": sorted(d for _, d in RISPOSTE),
   "items": [{"q": f"{i}. «{r}»"} for i, (r, _) in enumerate(RISPOSTE, 1)], "k": [eq(d) for _, d in RISPOSTE]},

  {"part": "Parla di te"},
  {"id": "e4", "title": "4 ✎ · Rispondi alle domande", "type": "free", "rows": 1,
   "items": ["COME TI CHIAMI?", "DA CHE PAESE VIENI?", "DA QUALE CITTÀ?", "DA QUANTO TEMPO SEI IN ITALIA?",
             "QUANTI ANNI HAI?", "QUANDO SEI NATO/A?", "QUAL È IL TUO INDIRIZZO?", "CON CHI ABITI?",
             "CHE LAVORO FAI?", "QUAL È IL TUO NUMERO DI TELEFONO? (puoi scrivere un numero inventato)"]},
  {"id": "e5", "title": "5 ✎ · Ora fai una domanda tu", "type": "free", "rows": 1,
   "items": ["CHI?", "COSA?", "DI CHI?", "DOVE?", "QUANDO?", "QUANTO?", "QUANTI/QUANTE?", "QUALE?", "PERCHÉ?", "COME?"]},
 ]
}
