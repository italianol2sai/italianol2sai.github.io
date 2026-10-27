from genera import eq, has, all_

SPESA = [("LA BIRRA", "LA"), ("L'ACQUA", "LA"), ("LO ZUCCHERO", "LO"), ("IL SALE", "LO"), ("LA PASTA", "LA"),
         ("L'INSALATA", "LA"), ("I PEPERONI", "LI"), ("LE FRAGOLE", "LE"), ("IL PESCE", "LO"), ("LA CARNE", "LA"),
         ("IL DETERSIVO", "LO"), ("GLI SPAGHETTI", "LI"), ("IL PANE", "LO"), ("I POMODORI", "LI"), ("LE BANANE", "LE")]

TELEFONA = [("A TE · LUI", "ti telefona"), ("A VOI · NOI", "vi telefoniamo"), ("A ME · VOI", "mi telefonate"),
            ("A TE · LORO", "ti telefonano"), ("A TE · IO", "ti telefono"), ("A VOI · LORO", "vi telefonano"),
            ("A LORO · NOI", "gli telefoniamo|telefoniamo loro"), ("A LEI · TU", "le telefoni"),
            ("A LUI · IO", "gli telefono"), ("A NOI · LEI", "ci telefona")]

IO_IND = [("REGALARE (A TE)", "ti regalo"), ("COMPRARE (A LUI)", "gli compro"), ("PORTARE (A LORO)", "gli porto|porto loro"),
          ("TELEFONARE (A VOI)", "vi telefono"), ("DARE (A LEI)", "le do"), ("RACCONTARE (A VOI)", "vi racconto"),
          ("MOSTRARE (A TE)", "ti mostro"), ("CREDERE (A LEI)", "le credo"), ("VENDERE (A LORO)", "gli vendo|vendo loro"),
          ("CHIEDERE (A TE)", "ti chiedo"), ("SCRIVERE (A LUI)", "gli scrivo"), ("PRESTARE (A TE)", "ti presto"),
          ("SPEDIRE (A VOI)", "vi spedisco"), ("OFFRIRE (A VOI)", "vi offro"), ("SPIEGARE (A VOI)", "vi spiego"),
          ("RISPONDERE (A LEI)", "le rispondo")]

MISTI = [("(IO VEDERE) IL TAVOLO", "lo vedo"), ("(TU REGALARE) ALLA ZIA", "le regali"),
         ("(VOI REGALARE) AI FRATELLI", "gli regalate|regalate loro"), ("(LORO VEDERE) I DOCUMENTI", "li vedono"),
         ("(NOI REGALARE) A TE", "ti regaliamo"), ("(VOI VEDERE) LE SCALE", "le vedete"),
         ("(NOI VEDERE) LA MACCHINA", "la vediamo"), ("(NOI VEDERE) LE BAMBINE", "le vediamo"),
         ("(TU VEDERE) I SOLDI", "li vedi"), ("(NOI REGALARE) AL DOTTORE", "gli regaliamo"),
         ("(VOI VEDERE) LA MAMMA", "la vedete"), ("(NOI TELEFONARE) A LUIGI", "gli telefoniamo"),
         ("(IO VEDERE) ANNA", "la vedo"), ("(TU VEDERE) MARIO E GIANNI", "li vedi")]

def si(*risposte):
    out = []
    for r in risposte:
        out += [r, "si " + r, "sì " + r]
    return eq(*out)

PASSATO = [("HAI PRESO I SOLDI?", si("li ho presi")), ("AVETE PAGATO LE BOLLETTE?", si("le abbiamo pagate")),
           ("HAI COMPRATO LA BICICLETTA?", si("l'ho comprata")), ("HAI ASPETTATO I BAMBINI?", si("li ho aspettati")),
           ("AVETE FATTO GLI ESERCIZI?", si("li abbiamo fatti")), ("AVETE COMPRATO IL PANE?", si("l'abbiamo comprato")),
           ("HANNO BEVUTO IL LATTE?", si("l'hanno bevuto")), ("AVETE CHIUSO LA PORTA?", si("l'abbiamo chiusa")),
           ("AVETE INVITATO GLI AMICI?", si("li abbiamo invitati")), ("HAI PORTATO IL LIBRO?", si("l'ho portato"))]

PRONOMI = {
 "title": "👉 I pronomi · Esercizi",
 "store": "pronomi",
 "upper": True,
 "sections": [
  {"part": "I pronomi diretti: lo, la, li, le"},
  {"id": "e1", "title": "1 · Che cosa compri?", "short": "1 · Lo, la, li, le", "type": "choice",
   "opts": ["LO", "LA", "LI", "LE"], "cons": "Esempio: LA BIRRA → LA COMPRO. IL PANE → LO COMPRO.",
   "items": [{"q": f"{i}. {n} → … COMPRO"} for i, (n, _) in enumerate(SPESA, 1)], "k": [eq(a) for _, a in SPESA]},
  {"part": "I pronomi indiretti: mi, ti, gli, le, ci, vi"},
  {"id": "e2", "title": "2 · A chi telefona?", "short": "2 · A chi telefona?", "type": "text", "w": "m",
   "cons": "Scrivi il pronome e il verbo TELEFONARE. Esempio: A ME · TU → MI TELEFONI.",
   "items": [{"q": f"{i}. {q}"} for i, (q, _) in enumerate(TELEFONA, 1)], "k": [eq(*r.split("|")) for _, r in TELEFONA]},
  {"id": "e3", "title": "3 · Sempre IO", "short": "3 · Pronomi indiretti", "type": "text", "w": "m",
   "cons": "Scrivi il pronome e il verbo con IO. Esempio: REGALARE (A TE) → TI REGALO.",
   "items": [{"q": f"{i}. {q}"} for i, (q, _) in enumerate(IO_IND, 1)], "k": [eq(*r.split("|")) for _, r in IO_IND]},
  {"part": "Diretti e indiretti"},
  {"id": "e4", "title": "4 · Scrivi il pronome e il verbo", "short": "4 · Diretti o indiretti", "type": "text", "w": "m",
   "cons": "CHI? CHE COSA? → LO, LA, LI, LE · A CHI? → MI, TI, GLI, LE, CI, VI. Esempio: (IO VEDERE) IL TAVOLO → LO VEDO.",
   "items": [{"q": f"{i}. {q}"} for i, (q, _) in enumerate(MISTI, 1)], "k": [eq(*r.split("|")) for _, r in MISTI]},
  {"id": "e5", "title": "5 · Rispondi con il pronome (passato prossimo)", "short": "5 · Pronomi e passato", "type": "text", "w": "w",
   "cons": "Rispondi SÌ con il pronome. Attenzione: L'HO COMPRATA (la bicicletta), LI HO PRESI (i soldi).",
   "items": [{"q": f"{i}. {q}"} for i, (q, _) in enumerate(PASSATO, 1)], "k": [k for _, k in PASSATO]},
 ]
}
