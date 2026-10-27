import re
from genera import eq, has, all_

def g(f):
    """«sono andato» -> accetta anche andata / andati / andate quando serve: f usa * per la desinenza (andat*)."""
    if "*" not in f: return [f]
    return [f.replace("*", e) for e in "oaie"]

def k(*forme):
    out = []
    for f in forme:
        for x in f.split("|"): out += g(x)
    return eq(*out)

AUS = [("1. IO", "MANGIATO", "ho"), ("2. TU", "ANDATO", "sei"), ("3. IO E ANNA", "COMPRATO", "abbiamo"),
       ("4. TU E AMIN", "TORNATI", "siete"), ("5. MARIO E ANNA", "TELEFONATO", "hanno"), ("6. IO", "PARTITO", "sono"),
       ("7. VOI", "SCRITTO", "avete"), ("8. MARIO E LUIGI", "ARRIVATI", "sono"), ("9. TU E ANNA", "CUCINATO", "avete"),
       ("10. ANNA E MARIA", "ENTRATE", "sono"), ("11. LORO", "PAGATO", "hanno"), ("12. IO E ANNA", "PARTITI", "siamo"),
       ("13. LUISA", "GUARDATO", "ha"), ("14. LUISA", "ANDATA", "è"), ("15. TU", "PULITO", "hai"),
       ("16. NOI", "LETTO", "abbiamo"), ("17. VOI", "STATI", "siete"), ("18. LUIGI", "LAVORATO", "ha"),
       ("19. LUIGI E IO", "PARTITI", "siamo"), ("20. TU", "PARTITO", "sei")]

PART = [("MANGIARE", "mangiato"), ("DORMIRE", "dormito"), ("AVERE", "avuto"), ("FARE", "fatto"), ("DIRE", "detto"),
        ("BERE", "bevuto"), ("LEGGERE", "letto"), ("SCRIVERE", "scritto"), ("PRENDERE", "preso"), ("METTERE", "messo"),
        ("VEDERE", "visto|veduto"), ("APRIRE", "aperto"), ("CHIUDERE", "chiuso"), ("CHIEDERE", "chiesto"),
        ("RISPONDERE", "risposto"), ("CAPIRE", "capito"), ("VENIRE", "venuto"), ("RIMANERE", "rimasto"),
        ("PERDERE", "perso|perduto"), ("ESSERE", "stato")]

AVERE_PP = [("NOI", "MANGIARE", "mangiamo", "abbiamo mangiato"), ("IO", "PREPARARE", "preparo", "ho preparato"),
            ("LUI", "COMPRARE", "compra", "ha comprato"), ("LORO", "APRIRE", "aprono", "hanno aperto"),
            ("VOI", "CHIUDERE", "chiudete", "avete chiuso"), ("TU", "SCRIVERE", "scrivi", "hai scritto"),
            ("LUI", "PIANGERE", "piange", "ha pianto"), ("NOI", "RIDERE", "ridiamo", "abbiamo riso"),
            ("IO", "CHIEDERE", "chiedo", "ho chiesto"), ("LUI", "FARE", "fa", "ha fatto"),
            ("VOI", "PULIRE", "pulite", "avete pulito"), ("TU", "LAVARE", "lavi", "hai lavato")]
ESSERE_PP = [("NOI", "ANDARE", "andiamo", "siamo andat*"), ("IO", "TORNARE", "torno", "sono tornat*"),
             ("LUI", "ARRIVARE", "arriva", "è arrivato"), ("LORO", "PARTIRE", "partono", "sono partit*"),
             ("VOI", "STARE", "state", "siete stat*"), ("IO", "USCIRE", "esco", "sono uscit*"),
             ("TU", "ENTRARE", "entri", "sei entrat*"), ("VOI", "RIMANERE", "rimanete", "siete rimast*"),
             ("LUI", "CADERE", "cade", "è caduto"), ("IO", "SALIRE", "salgo", "sono salit*"),
             ("LUI", "SCENDERE", "scende", "è sceso"), ("NOI", "DIVENTARE", "diventiamo", "siamo diventat*")]

def tabella(righe):
    parts, ks = [], []
    for i, (p, v, pres, pas) in enumerate(righe, 1):
        parts += [f"{i}. <b>{p} · {v}</b><br>PRESENTE ", {}, " PASSATO ", {"w": "m"}, "<br>"]
        ks += [eq(pres), k(pas)]
    return parts, ks

TAB_A = tabella(AVERE_PP)
TAB_E = tabella(ESSERE_PP)

def frasi(items):
    return ([{"pre": f"{i}. {a}", "post": b} for i, (a, b, _) in enumerate(items, 1)], [k(r) for *_, r in items])

ESS = frasi([("ANNA (TORNARE)", "ALLE 8", "è tornata"), ("MARIO (ANDARE)", "A VENEZIA", "è andato"),
             ("MARIO E ANNA (PARTIRE)", "IERI", "sono partiti"), ("L'AUTOBUS (ARRIVARE)", "TARDI", "è arrivato"),
             ("I TRENI (PARTIRE)", "PUNTUALI", "sono partiti"), ("GLI ZII (ANDARE)", "ALLA QUESTURA", "sono andati"),
             ("SUA FIGLIA (CRESCERE)", "MOLTO", "è cresciuta"), ("I BAMBINI (DIVENTARE)", "GRANDI", "sono diventati"),
             ("LA SIGNORA (CADERE)", "DALLE SCALE", "è caduta"), ("MARIO E ANTONIO (SALIRE)", "IN AUTOBUS", "sono saliti"),
             ("LUI (SCENDERE)", "DAL TRENO", "è sceso"), ("LEI (NASCERE)", "NEL 1998", "è nata"),
             ("LA MAMMA (TORNARE)", "STAMATTINA", "è tornata"), ("LE MIE SORELLE (ARRIVARE)", "IN MACCHINA", "sono arrivate"),
             ("IL CANE (ENTRARE)", "IN CASA", "è entrato"), ("IL PAPÀ (USCIRE)", "CON LA MAMMA", "è uscito")])
AVE = frasi([("ANNA (MANGIARE)", "IL DOLCE", "ha mangiato"), ("LUIGI (COMPRARE)", "LA FRUTTA", "ha comprato"),
             ("MARCO E ROBERTO (PAGARE)", "I CAFFÈ", "hanno pagato"), ("IL CANE (BERE)", "L'ACQUA", "ha bevuto"),
             ("LA MAMMA (BACIARE)", "IL BAMBINO", "ha baciato"), ("L'IMPIEGATO (APRIRE)", "L'UFFICIO", "ha aperto"),
             ("PATRIZIA E LUCIA (SCRIVERE)", "UNA MAIL", "hanno scritto"), ("I BAMBINI (GIOCARE)", "AL PARCO", "hanno giocato"),
             ("LA BAMBINA (GUARDARE)", "LA TV", "ha guardato"), ("IL MAESTRO (LEGGERE)", "IL LIBRO", "ha letto"),
             ("LA NIPOTE (TELEFONARE)", "ALLO ZIO", "ha telefonato"), ("TU E AMIN (PRENDERE)", "IL TRENO", "avete preso"),
             ("GLI STUDENTI (STUDIARE)", "L'ITALIANO", "hanno studiato"), ("IL FIGLIO (PORTARE)", "I FIORI ALLA MAMMA", "ha portato"),
             ("LE SORELLE (CUCINARE)", "LA TORTA", "hanno cucinato"), ("MIA MAMMA E MIA SORELLA (FARE)", "LA SPESA", "hanno fatto")])
MISTO = frasi([("ANNA (RICEVERE)", "UNA E-MAIL", "ha ricevuto"), ("IO (CAPIRE)", "LA LEZIONE", "ho capito"),
               ("PAOLO (TROVARE)", "UN LAVORO", "ha trovato"), ("PIETRO (SPEGNERE)", "LA LUCE", "ha spento"),
               ("STAMATTINA MIO PADRE (PARTIRE)", "ALLE 8", "è partito"), ("CHI (PAGARE)", "I CAFFÈ?", "ha pagato"),
               ("STAMATTINA IO (PERDERE)", "L'AUTOBUS", "ho perso"), ("IO E GIANNI (TORNARE)", "TARDI", "siamo tornat*"),
               ("IERI NOI NON (USCIRE)", "", "siamo uscit*"), ("STANOTTE IO (DORMIRE)", "POCO", "ho dormito"),
               ("IO (CHIUDERE)", "LA FINESTRA", "ho chiuso"), ("(NOI, ANDARE)", "A VISITARE VENEZIA", "siamo andat*"),
               ("FACEVA CALDO E IO (BERE)", "MOLTO", "ho bevuto"), ("IO E MIO ZIO (ARRIVARE)", "QUI UN ANNO FA", "siamo arrivat*")])

RIEMPI = re.split(r"\[([^\]]+)\]",
    "IERI È STATA UNA GIORNATA MOLTO FATICOSA. MI (SVEGLIARE) [sono svegliat*] ALLE 6 E (FARE) [ho fatto] "
    "UN'ABBONDANTE COLAZIONE CON LATTE, BISCOTTI E SUCCO D'ARANCIA, DOPODICHÉ MI (VESTIRE) [sono vestit*] "
    "E (ANDARE) [sono andat*] A SCUOLA. LA LEZIONE DI MATEMATICA (ESSERE) [è stata] LA PIÙ NOIOSA, "
    "SEMBRAVA NON FINIRE MAI. ALLE 14.00 (TORNARE) [sono tornat*] A CASA. ERO STANCO E AFFAMATO, MA PER FORTUNA "
    "MIA MADRE MI (PREPARARE) [ha preparato] UN PRANZO COI FIOCCHI: PASTA AL RAGÙ, POLLO ARROSTO E TIRAMISÙ. "
    "SUBITO DOPO PRANZO, I MIEI GENITORI MI (PORTARE) [hanno portato] A CASA DEL MIO AMICO LUCA PER FARE I COMPITI. "
    "(STUDIARE) [abbiamo studiato] PER DUE ORE E POI (ANDARE) [siamo andati] A LEZIONE DI NUOTO. "
    "ALLE 19.00 (FINIRE) [abbiamo finito] DI STUDIARE E (ENTRARE) [siamo entrati] IN PISCINA. "
    "ALLE 20.00 (TORNARE) [sono tornat*] A CASA E SICCOME MORIVO DI FAME, (CENARE) [ho cenato] CON UN BEL PIATTO "
    "DI MINESTRONE E FINALMENTE ALLE 22.00 (ANDARE) [sono andat*] A LETTO.")
RIEMPI_P = [p if i % 2 == 0 else {"w": "m"} for i, p in enumerate(RIEMPI) if p]
RIEMPI_K = [k(p) for i, p in enumerate(RIEMPI) if i % 2]

PASSATO = {
 "title": "⏪ Il passato prossimo · Esercizi",
 "store": "passato-prossimo",
 "upper": True,
 "sections": [
  {"part": "Avere o essere? Il participio"},
  {"id": "e1", "title": "1 · Avere o essere?", "short": "1 · L'ausiliare", "type": "text", "w": "s",
   "cons": "Scrivi AVERE o ESSERE al presente. Guarda la fine del participio: ANDATI, PARTITE… vogliono ESSERE.",
   "items": [{"pre": a, "post": b} for a, b, _ in AUS], "k": [eq(r) for *_, r in AUS]},
  {"id": "e2", "title": "2 · Il participio passato", "short": "2 · Il participio", "type": "text", "w": "m",
   "cons": "Scrivi il participio passato. Esempio: LAVORARE → LAVORATO.",
   "items": [{"q": f"{i}. {v} →"} for i, (v, _) in enumerate(PART, 1)], "k": [eq(*p.split("|")) for _, p in PART]},
  {"id": "e3", "title": "3 · Presente e passato (con AVERE)", "short": "3 · Presente e passato (avere)", "type": "cloze",
   "cons": "Scrivi il verbo al presente e al passato prossimo. Esempio: IO · GUARDARE → GUARDO · HO GUARDATO.",
   "parts": TAB_A[0], "k": TAB_A[1]},
  {"id": "e4", "title": "4 · Presente e passato (con ESSERE)", "short": "4 · Presente e passato (essere)", "type": "cloze",
   "cons": "Scrivi il verbo al presente e al passato prossimo. Esempio: IO · ANDARE → VADO · SONO ANDATO/A.",
   "parts": TAB_E[0], "k": TAB_E[1]},

  {"part": "Scrivi il passato"},
  {"id": "e5", "title": "5 · Verbi con ESSERE", "short": "5 · Frasi con essere", "type": "text", "w": "m",
   "cons": "Scrivi il verbo al passato prossimo con ESSERE. Attenzione: ANNA È TORNATA, I TRENI SONO PARTITI.",
   "items": ESS[0], "k": ESS[1]},
  {"id": "e6", "title": "6 · Verbi con AVERE", "short": "6 · Frasi con avere", "type": "text", "w": "m",
   "cons": "Scrivi il verbo al passato prossimo con AVERE.", "items": AVE[0], "k": AVE[1]},
  {"id": "e7", "title": "7 · Avere o essere? Scrivi il passato", "short": "7 · Avere o essere", "type": "text", "w": "m",
   "cons": "Scrivi il verbo al passato prossimo. Scegli tu AVERE o ESSERE.", "items": MISTO[0], "k": MISTO[1]},
  {"id": "e8", "title": "8 · Una giornata faticosa", "short": "8 · Riempi gli spazi", "type": "cloze",
   "cons": "Leggi il racconto e scrivi i verbi tra parentesi al passato prossimo.", "parts": RIEMPI_P, "k": RIEMPI_K},
  {"id": "e9", "title": "9 ✎ · E tu? Che cosa hai fatto ieri?", "type": "free", "rows": 6,
   "items": ["Scrivi 5 frasi al passato. Esempio: IERI SERA ANTONIO HA GUARDATO LA TV. IO SONO ANDATO AL MERCATO…"]},
 ]
}
