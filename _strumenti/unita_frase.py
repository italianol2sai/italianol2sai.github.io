from genera import eq, has, all_

def img(nome):
    return f'<img src="img/{nome}.jpg" alt="" style="display:block;width:100%;max-width:300px;border-radius:12px;margin:4px 0 6px">'

RIDUCI = [("I BAMBINI GIOCANO NEL GIARDINO CON IL PALLONE DA CALCIO.", "i bambini giocano"),
          ("IL CANE CORRE SUL PRATO DEL GIARDINO DEL VICINO.", "il cane corre"),
          ("ELISA STIRA LE CAMICIE AZZURRE DEL MARITO.", "elisa stira"),
          ("LA ZIA CUCINA UN POLLO PER GLI OSPITI.", "la zia cucina"),
          ("GLI AEREI SORVOLANO I MONTI IMBIANCATI DALLA NEVE.", "gli aerei sorvolano"),
          ("MARIO MANGIA UNA PERA RACCOLTA DAL NONNO.", "mario mangia"),
          ("IL GABBIANO VOLA NEL CIELO SOPRA IL MARE.", "il gabbiano vola"),
          ("FABRIZIO PESCA LE TROTE NEL LAGO.", "fabrizio pesca"),
          ("FRANCESCA GUIDA L'AUTO SPORTIVA DELLO ZIO.", "francesca guida"),
          ("IL BAMBINO DORME NELLA CULLA DA TRE ORE.", "il bambino dorme"),
          ("GLI SCOLARI ASCOLTANO ATTENTAMENTE LA LEZIONE.", "gli scolari ascoltano")]

PREDICATI = [("IL LUPO", "ULULA"), ("GLI ELICOTTERI", "VOLANO"), ("I CAVALLI", "NITRISCONO"), ("I FIORI", "PROFUMANO"),
             ("LA MAMMA", "CUCINA"), ("I CANI", "ABBAIANO"), ("IL PAGLIACCIO", "SCHERZA"), ("LE STELLE", "BRILLANO"),
             ("GLI ALUNNI", "STUDIANO"), ("IL SERPENTE", "STRISCIA")]

ESPANSIONI = [("LA MAMMA HA STESO", "IL BUCATO"), ("LUIGI MANGIA", "IL GELATO"), ("IL NONNO RACCONTA", "UNA STORIA"),
              ("LA RONDINE COSTRUISCE", "IL NIDO"), ("I BAMBINI GIOCANO", "A NASCONDINO"), ("IL MEDICO CURA", "I PAZIENTI"),
              ("LE ROSE FIORISCONO", "IN PRIMAVERA"), ("IL SOLE ILLUMINA", "LA TERRA"), ("IL MECCANICO RIPARA", "LE AUTO"),
              ("I GATTI RINCORRONO", "I TOPI")]

SOG_PRED = [("MARCO legge un libro.", "MARCO", "SOGGETTO"), ("Marco LEGGE un libro.", "LEGGE", "PREDICATO"),
            ("IL CANE corre sul prato.", "IL CANE", "SOGGETTO"), ("Il cane CORRE sul prato.", "CORRE", "PREDICATO"),
            ("La mamma CUCINA la pasta.", "CUCINA", "PREDICATO"), ("LE STELLE brillano nel cielo.", "LE STELLE", "SOGGETTO"),
            ("Gli alunni STUDIANO in classe.", "STUDIANO", "PREDICATO"), ("IL MEDICO cura i pazienti.", "IL MEDICO", "SOGGETTO")]

FRASE = {
 "title": "🧱 La frase minima · Esercizi",
 "store": "frase-minima",
 "upper": True,
 "sections": [
  {"part": "Soggetto e predicato"},
  {"id": "e1", "title": "1 · Soggetto o predicato?", "short": "1 · Soggetto o predicato", "type": "choice",
   "opts": ["SOGGETTO", "PREDICATO"], "full": True,
   "cons": "SOGGETTO = CHI? · PREDICATO = CHE COSA FA? Guarda la parola in grande e scegli.",
   "items": [{"q": f"{i}. {f.replace(w, '<b><u>' + w + '</u></b>')}"} for i, (f, w, _) in enumerate(SOG_PRED, 1)],
   "k": [eq(a) for *_, a in SOG_PRED]},
  {"id": "e2", "title": "2 · Chi fa che cosa? Collega", "short": "2 · Soggetto + predicato", "type": "select",
   "cons": "Collega ogni soggetto al suo predicato.", "opts": sorted(p for _, p in PREDICATI),
   "items": [{"q": f"{i}. {s}"} for i, (s, _) in enumerate(PREDICATI, 1)], "k": [eq(p) for _, p in PREDICATI]},

  {"part": "Trova la frase minima"},
  {"id": "e3", "title": "3 · Scrivi la frase minima", "short": "3 · Riduci la frase", "type": "text", "w": "w",
   "cons": "Togli le parti che non servono. Scrivi solo SOGGETTO + PREDICATO. Esempio: MARCO LEGGE UN LIBRO → MARCO LEGGE.",
   "items": [{"q": f"{i}. {f}"} for i, (f, _) in enumerate(RIDUCI, 1)], "k": [eq(r) for _, r in RIDUCI]},
  {"id": "e4", "title": "4 · Guarda il disegno: chi? che cosa fa?", "short": "4 · Frasi e disegni", "type": "text", "w": "w",
   "cons": "Scrivi la frase minima per ogni disegno. Esempio: LA BAMBINA DORME.",
   "items": [{"q": f"{i}.<br>" + img(n)} for i, n in enumerate(["sveglia", "biscotti", "cucina", "fiori"], 1)],
   "k": [has("sveglia"), has("mangia"), has("cucina"), has("innaffia", "annaffia", "bagna")]},

  {"part": "Espandere la frase"},
  {"id": "e5", "title": "5 · Completa la frase", "short": "5 · Le espansioni", "type": "select",
   "cons": "Collega ogni frase minima alla parte giusta.", "opts": sorted(e for _, e in ESPANSIONI),
   "items": [{"q": f"{i}. {f} …"} for i, (f, _) in enumerate(ESPANSIONI, 1)], "k": [eq(e) for _, e in ESPANSIONI]},
  {"id": "e6", "title": "6 ✎ · Allunga la frase", "type": "free", "rows": 2,
   "items": ["1. LA RANA SALTA (DOVE?)", "2. LA PRIMAVERA È ARRIVATA (QUANDO?)", "3. LEONARDO PASSEGGIA (CON CHI?)",
             "4. MARTA MANGIA (CHE COSA?)", "5. ROCCO PARTE (PER DOVE?)", "6. LA MAMMA TELEFONA (A CHI?)",
             "7. LA BAMBINA PIANGE (PERCHÉ?)", "8. LA TAZZA È DECORATA (COME?)"]},
 ]
}
