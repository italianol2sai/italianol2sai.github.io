from genera import eq, has, all_
from unita_nomi import cl, scegli

def completa(righe):
    """[(prima, dopo, risposta|alternativa), ...] -> esercizio con campo in mezzo alla frase."""
    return ([{"pre": f"{i}. {a}", "post": b} for i, (a, b, _) in enumerate(righe, 1)],
            [eq(*r.split("|")) for _, _, r in righe])

# --- Possessivo e plurale (Esercizi integrativi pag. 45) ---
E1_P, E1_K = cl("<br>".join(f"{i}. {p} – {n}: [{s}] → [{pl}]" for i, (p, n, s, pl) in enumerate([
    ("IO", "LIBRO", "il mio libro", "i miei libri"), ("LORO", "APPARTAMENTO", "il loro appartamento", "i loro appartamenti"),
    ("NOI", "AUTOBUS", "il nostro autobus", "i nostri autobus"), ("TU", "PENNA", "la tua penna", "le tue penne"),
    ("LUI", "SCARPA", "la sua scarpa", "le sue scarpe"), ("VOI", "MANO", "la vostra mano", "le vostre mani"),
    ("NOI", "PASSAPORTO", "il nostro passaporto", "i nostri passaporti"), ("LORO", "CASA", "la loro casa", "le loro case"),
    ("TU", "ESERCIZIO", "il tuo esercizio", "i tuoi esercizi"), ("NOI", "LAVORO", "il nostro lavoro", "i nostri lavori"),
    ("IO", "AMICO", "il mio amico", "i miei amici"), ("VOI", "PROFESSORE", "il vostro professore", "i vostri professori"),
    ("NOI", "AULA", "la nostra aula", "le nostre aule"), ("LEI", "OMBRELLO", "il suo ombrello", "i suoi ombrelli"),
    ("TU", "CAPPELLO", "il tuo cappello", "i tuoi cappelli"), ("LORO", "COMPUTER", "il loro computer", "i loro computer"),
    ("NOI", "PAESE", "il nostro paese", "i nostri paesi"), ("LORO", "CITTÀ", "la loro città", "le loro città")], 1)))

# --- Collega (pag. 46) ---
GRUPPI = [(["OROLOGIO", "BORSA", "PANTALONI", "SCARPE"], [("IL MIO", "OROLOGIO"), ("LA MIA", "BORSA"), ("I MIEI", "PANTALONI"), ("LE MIE", "SCARPE")]),
          (["PADRE", "MADRE", "SORELLE", "FIGLI"], [("SUO", "PADRE"), ("SUA", "MADRE"), ("LE SUE", "SORELLE"), ("I SUOI", "FIGLI")]),
          (["AMICO", "CASA", "SOLDI", "AMICHE"], [("IL TUO", "AMICO"), ("LA TUA", "CASA"), ("I TUOI", "SOLDI"), ("LE TUE", "AMICHE")]),
          (["SORELLA", "INDIRIZZO", "DOCUMENTI", "FAMIGLIE"], [("VOSTRA", "SORELLA"), ("IL VOSTRO", "INDIRIZZO"), ("I VOSTRI", "DOCUMENTI"), ("LE VOSTRE", "FAMIGLIE")]),
          (["MADRE", "NONNI", "LAVORO", "SCARPE"], [("NOSTRA", "MADRE"), ("I NOSTRI", "NONNI"), ("IL NOSTRO", "LAVORO"), ("LE NOSTRE", "SCARPE")])]
E2_I = [{"q": p, "opts": sorted(o)} for o, cs in GRUPPI for p, _ in cs]
E2_K = [eq(n) for _, cs in GRUPPI for _, n in cs]

# --- Possessivi e parenti (pag. 47) ---
E3 = [("(IO) AMICO", "il mio amico"), ("(TU) FRATELLO", "tuo fratello"), ("(LUI) CUGINI", "i suoi cugini"),
      ("(VOI) FIGLIO", "vostro figlio"), ("(LORO) ZIO", "il loro zio"), ("(NOI) PADRE", "nostro padre"),
      ("(VOI) FRATELLI", "i vostri fratelli"), ("(TU) SORELLE", "le tue sorelle"), ("(VOI) BAMBINO", "il vostro bambino"),
      ("(LORO) MARITI", "i loro mariti"), ("(VOI) MOGLI", "le vostre mogli"), ("(NOI) NIPOTI", "i nostri nipoti"),
      ("(LUI) ZII", "i suoi zii"), ("(LORO) GENITORI", "i loro genitori"), ("(TU) AMICI", "i tuoi amici"),
      ("(VOI) SORELLA", "vostra sorella"), ("(LUI) FIGLI", "i suoi figli"), ("(TU) CUGINA", "tua cugina"),
      ("(LEI) FIDANZATO", "il suo fidanzato"), ("(TU) MADRE", "tua madre")]
E3_I = [{"q": f"{i}. {q}"} for i, (q, _) in enumerate(E3, 1)]
E3_K = [eq(r, r.rsplit(" ", 1)[0]) for _, r in E3]

# --- Metti i possessivi (pag. 48) ---
E4_I, E4_K = completa([("LA SERA (IO) ESCO CON", "AMICI.", "i miei"), ("È QUESTO", "OMBRELLO, SIGNORE?", "il suo"),
    ("È DIFFICILE", "LAVORO, MARCO?", "il tuo"), ("VOI VIVETE CON", "GENITORI?", "i vostri"),
    ("HO SPESO TUTTI (IO)", "SOLDI.", "i miei"), ("MARIA, SONO", "SCARPE?", "le tue"),
    ("SIGNORA,", "FIGLIO È DIVENTATO GRANDE!", "suo"), ("ANNA, DOV'È", "CASA?", "la tua"),
    ("NON TROVO PIÙ (IO)", "LIBRO.", "il mio"), ("SIGNORI ROSSI, COME STANNO", "BAMBINI?", "i vostri|i loro"),
    ("(NOI)", "LAVORO È MOLTO FATICOSO.", "il nostro"), ("È QUESTO (TU)", "AUTOBUS?", "il tuo"),
    ("CIAO ANNA! COME STA", "MARITO?", "tuo"), ("CARLO, VIENE ANCHE (TU)", "FRATELLO CON NOI?", "tuo"),
    ("OGGI (NOI) ANDIAMO AL MARE CON", "FAMIGLIE.", "le nostre"), ("SIGNORA, È A CASA", "MARITO?", "suo"),
    ("ORA DEVO ANDARE, QUESTA È (IO)", "FERMATA.", "la mia"), ("DOVE SI TROVA (VOI)", "SCUOLA?", "la vostra"),
    ("DEVO TELEFONARE A (IO)", "MADRE.", "mia"), ("BELLO (TU)", "OROLOGIO! DOVE L'HAI COMPRATO?", "il tuo")])

# --- Possessivi (possessivo_elem, esercizi 1, 2, 3) ---
E5_I, E5_K = completa([("IO HO UN VESTITO ROSSO. →", "È ROSSO.", "il mio vestito"),
    ("GLI STUDENTI HANNO UNO ZAINO NUOVO. →", "È NUOVO.", "il loro zaino"),
    ("IO HO UN AMICO SIMPATICO. →", "È SIMPATICO.", "il mio amico"),
    ("LORO HANNO UNA CASA GRANDE. →", "È GRANDE.", "la loro casa"),
    ("TU HAI UNA MADRE SIMPATICA. →", "È SIMPATICA.", "tua madre"),
    ("ELENA HA UN VESTITO ELEGANTE. →", "È ELEGANTE.", "il suo vestito"),
    ("NOI ABBIAMO UN'AUTOMOBILE COMODA. →", "È COMODA.", "la nostra automobile"),
    ("I RAGAZZI HANNO CAMICIE AZZURRE. →", "SONO AZZURRE.", "le loro camicie"),
    ("LA NONNA HA UN CAPPOTTO VECCHIO. →", "È VECCHIO.", "il suo cappotto"),
    ("ELENA E ARTURO HANNO UN AMICO TEDESCO. →", "È TEDESCO.", "il loro amico"),
    ("TU HAI UN FRATELLO STUDIOSO. →", "È STUDIOSO.", "tuo fratello"),
    ("GIORGIO HA DELLE SORELLE MOLTO BELLE. →", "SONO MOLTO BELLE.", "le sue sorelle")])
for _it in E5_I:
    _it["w"] = "m"
E6_I, E6_K = completa([("STASERA ARTURO ESCE CON", "AMICI.", "i suoi"), ("ELENA HA PERSO", "PASSAPORTO.", "il suo"),
    ("DOMENICA VENGONO ANCHE MARIO E LAURA CON", "FIGLI.", "i loro"), ("AVETE MESSO IN ORDINE", "CAMERA?", "la vostra"),
    ("MARIO E LAURA DICONO CHE", "CASA È TROPPO GRANDE.", "la loro"), ("SIGNOR NERI, HA TROVATO", "OCCHIALI?", "i suoi"),
    ("ARTURO, A CHE ORA TORNA DA SCUOLA", "SORELLA?", "tua"), ("«CHE ORE SONO?» «NON LO SO,", "OROLOGIO È FERMO.»", "il mio"),
    ("GIORGIO, COME STA", "PADRE?", "tuo"), ("E COME STANNO", "SORELLE, GIORGIO?", "le tue"),
    ("ELENA ASPETTA UNA TELEFONATA DI", "FIGLIA.", "sua"), ("SABATO (NOI) ABBIAMO PULITO", "APPARTAMENTO.", "il nostro")])
E7_I, E7_K = completa([("QUESTE FOTOGRAFIE SONO TUE? NO, NON SONO", ".", "mie"),
    ("È VOSTRO QUESTO GATTO? SÌ, È", ".", "nostro"), ("ELENA, SONO TUOI QUESTI GUANTI? NO, NON SONO", ".", "miei"),
    ("È DI LUIGI QUESTO CAPPELLO? SÌ, È", ".", "suo"), ("SONO DI TUO PADRE QUESTI SIGARI? SÌ, SONO", ".", "suoi"),
    ("SIGNORA, È SUO QUESTO SCIALLE? NO, NON È", ", È DI ELENA.", "mio"),
    ("SONO QUESTI I NOSTRI SOLDI? NO, QUESTI SONO I MIEI E QUELLI SONO", ".", "i vostri|vostri"),
    ("POSSO PRENDERE LA TUA BICI? NO, TU HAI", "BICI!", "la tua")])

POSSESSIVI = {
 "title": "🔑 I possessivi · Esercizi",
 "store": "possessivi",
 "upper": True,
 "sections": [
  {"part": "Il mio, la mia, i miei, le mie"},
  {"id": "e1", "title": "1 · Scrivi il possessivo e fai il plurale", "short": "1 · Possessivo e plurale", "type": "cloze",
   "cons": "Esempio: IO – CASA → LA MIA CASA → LE MIE CASE.", "parts": E1_P, "k": E1_K},
  {"id": "e2", "title": "2 · Collega il possessivo con il nome", "short": "2 · Collega", "type": "select",
   "cons": "Ci sono 5 gruppi di 4. Scegli il nome giusto per ogni possessivo.", "items": E2_I, "k": E2_K},
  {"id": "e3", "title": "3 · Trasforma la frase", "short": "3 · Trasforma", "type": "text",
   "cons": "Esempio: IO HO UNA BELLA BORSA. → LA MIA BORSA È BELLA.", "items": E5_I, "k": E5_K},

  {"part": "Possessivi e famiglia"},
  {"id": "e4", "title": "4 · L'articolo serve o no?", "short": "4 · Parenti", "type": "text", "w": "m",
   "cons": "Scrivi il possessivo con l'articolo, se serve. Esempio: (IO) MADRE → MIA MADRE · (IO) FRATELLI → I MIEI FRATELLI.",
   "items": E3_I, "k": E3_K},

  {"part": "Metti i possessivi"},
  {"id": "e5", "title": "5 · Metti il possessivo (1)", "short": "5 · Metti il possessivo 1", "type": "text", "w": "s",
   "cons": "Scrivi il possessivo con l'articolo, se serve. Attenzione: SIGNORE, SIGNORA = LEI.", "items": E4_I, "k": E4_K},
  {"id": "e6", "title": "6 · Metti il possessivo (2)", "short": "6 · Metti il possessivo 2", "type": "text", "w": "s",
   "items": E6_I, "k": E6_K},
  {"id": "e7", "title": "7 · Di chi è?", "short": "7 · Di chi è", "type": "text", "w": "s",
   "cons": "Rispondi con il possessivo. Esempio: È TUO QUESTO LIBRO? SÌ, È MIO.", "items": E7_I, "k": E7_K},
  {"id": "e8", "title": "8 ✎ · E tu? La tua famiglia", "type": "free", "rows": 5,
   "items": ["Scrivi 3 o 4 frasi. Esempio: MIA MADRE SI CHIAMA AMINA. I MIEI FRATELLI ABITANO IN MAROCCO. LA MIA CASA È PICCOLA."]},
 ]
}
