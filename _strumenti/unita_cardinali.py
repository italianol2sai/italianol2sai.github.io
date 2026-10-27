from genera import eq, has, all_
from rosa import rosa

PC = ["NORD", "SUD", "EST", "OVEST"]
MAPPA = '<img src="img/italia.jpg" alt="Cartina dell\'Italia" style="display:block;width:100%;max-width:420px;background:#fff;border-radius:12px;margin:0 auto">'

ALTRI = [("MEZZANOTTE", "NORD"), ("LEVANTE", "EST"), ("MEZZOGIORNO", "SUD"), ("PONENTE", "OVEST"),
         ("ORIENTE", "EST"), ("SETTENTRIONE", "NORD"), ("MERIDIONE", "SUD"), ("OCCIDENTE", "OVEST")]

TABELLA = [("SE GUARDI A NORD, A DESTRA C'È…", "EST"), ("SE GUARDI A NORD, A SINISTRA C'È…", "OVEST"),
           ("SE GUARDI A NORD, DIETRO C'È…", "SUD"), ("SE GUARDI A EST, A DESTRA C'È…", "SUD"),
           ("SE GUARDI A EST, A SINISTRA C'È…", "NORD"), ("SE GUARDI A EST, DIETRO C'È…", "OVEST"),
           ("SE GUARDI A SUD, A DESTRA C'È…", "OVEST"), ("SE GUARDI A SUD, A SINISTRA C'È…", "EST"),
           ("SE GUARDI A SUD, DIETRO C'È…", "NORD"), ("SE GUARDI A OVEST, A DESTRA C'È…", "NORD"),
           ("SE GUARDI A OVEST, A SINISTRA C'È…", "SUD"), ("SE GUARDI A OVEST, DIETRO C'È…", "EST")]

GIRA = [("IL NORD È A SINISTRA. IN ALTO C'È…", "EST"), ("IL NORD È A SINISTRA. A DESTRA C'È…", "SUD"),
        ("IL NORD È A SINISTRA. IN BASSO C'È…", "OVEST"), ("L'OVEST È IN ALTO. A DESTRA C'È…", "NORD"),
        ("L'OVEST È IN ALTO. IN BASSO C'È…", "EST"), ("L'OVEST È IN ALTO. A SINISTRA C'È…", "SUD"),
        ("IL SUD È IN ALTO. IN BASSO C'È…", "NORD"), ("IL SUD È IN ALTO. A DESTRA C'È…", "OVEST"),
        ("L'EST È A SINISTRA. A DESTRA C'È…", "OVEST"), ("L'EST È A SINISTRA. IN ALTO C'È…", "SUD")]

VF = [("I PUNTI CARDINALI SONO 8.", "FALSO"), ("I PUNTI CARDINALI SONO RIFERIMENTI FISSI.", "VERO"),
      ("IL SOLE SORGE A NORD.", "FALSO"), ("LA BUSSOLA HA UN AGO MAGNETICO.", "VERO"),
      ("L'AGO DELLA BUSSOLA INDICA SEMPRE L'EST.", "FALSO"), ("IL SOLE A MEZZOGIORNO INDICA IL SUD.", "VERO"),
      ("DI NOTTE, SENZA IL SOLE, NON POSSIAMO ORIENTARCI.", "FALSO"),
      ("L'OVEST SI CHIAMA ANCHE OCCIDENTE E PONENTE.", "VERO")]

def ne(a, b):
    return eq(f"{a}-{b}", f"{a}{b}", f"{a} {b}", f"{a}-{b}".replace("-", " - "))

COMPLETA = [("1. NEI PUNTI CARDINALI GLI OPPOSTI SONO NORD E", "", eq("sud")),
            ("2. … ED EST E", "", eq("ovest")),
            ("3. SE GUARDIAMO VERSO NORD, ALLA NOSTRA", "TROVIAMO L'EST.", eq("destra")),
            ("4. PER ORIENTARCI DI GIORNO POSSIAMO USARE IL", "", eq("sole")),
            ("5. PER ORIENTARCI DI NOTTE POSSIAMO USARE LA", "", eq("stella polare", "bussola")),
            ("6. L'AGO DELLA BUSSOLA INDICA SEMPRE IL", "", eq("nord")),
            ("7. LA STELLA POLARE INDICA IL", "", eq("nord")),
            ("8. IL SOLE SORGE A", "", eq("est")),
            ("9. IL SOLE TRAMONTA A", "", eq("ovest")),
            ("10. QUANDO È IN ALTO NEL CIELO, IL SOLE INDICA IL", "", eq("sud")),
            ("11. LA STELLA POLARE SI TROVA NELLA COSTELLAZIONE DELL'", "", eq("orsa minore")),
            ("12. TRA IL NORD E L'EST C'È IL", "", ne("nord", "est")),
            ("13. TRA IL SUD E L'EST C'È IL", "", ne("sud", "est")),
            ("14. TRA IL SUD E L'OVEST C'È IL", "", ne("sud", "ovest")),
            ("15. TRA IL NORD E L'OVEST C'È IL", "", ne("nord", "ovest"))]

CITTA = [("ROMA SI TROVA A … DI VENEZIA.", "SUD"), ("FOGGIA SI TROVA A … DI ROMA.", "EST"),
         ("SASSARI SI TROVA A … DI NAPOLI.", "OVEST"), ("MESSINA SI TROVA A … DI PALERMO.", "EST"),
         ("GENOVA SI TROVA A … DI CAGLIARI.", "NORD"), ("MILANO SI TROVA A … DI BRESCIA, VERONA E TRIESTE.", "OVEST"),
         ("TRIESTE SI TROVA A … DI NAPOLI E CATANIA.", "NORD"), ("FIRENZE SI TROVA A … DI BOLOGNA E VERONA.", "SUD"),
         ("TARANTO SI TROVA A … DI LECCE.", "OVEST"), ("TORINO SI TROVA A … DI SASSARI E CAGLIARI.", "NORD"),
         ("PALERMO SI TROVA A … DI ROMA E VENEZIA.", "SUD"), ("VENEZIA SI TROVA A … DI VERONA, BRESCIA E MILANO.", "EST"),
         ("VERONA SI TROVA A … DI BOLOGNA E FIRENZE.", "NORD"), ("NAPOLI SI TROVA A … DI BARI.", "OVEST"),
         ("BARI SI TROVA A … DI NAPOLI.", "EST")]

CONTRARI = [("VICINO", "LONTANO"), ("DAVANTI", "DIETRO"), ("SOPRA", "SOTTO"), ("A DESTRA", "A SINISTRA"),
            ("PRIMA", "DOPO"), ("ALL'INIZIO", "ALLA FINE")]

CARDINALI = {
 "title": "🧭 I punti cardinali · Esercizi",
 "store": "punti-cardinali",
 "upper": True,
 "sections": [
  {"part": "I quattro punti cardinali"},
  {"id": "e1", "title": "1 · La rosa dei venti", "short": "1 · La rosa dei venti", "type": "select", "opts": PC,
   "cons": "Guarda la rosa dei venti. Che punto cardinale c'è al posto del numero?",
   "info": '<div style="text-align:center">' + rosa(("1", "2", "3", "4"), 240) + '</div>',
   "items": [{"q": q} for q in ["1 (IN ALTO)", "2 (A DESTRA)", "3 (IN BASSO)", "4 (A SINISTRA)"]],
   "k": [eq("NORD"), eq("EST"), eq("SUD"), eq("OVEST")]},
  {"id": "e2", "title": "2 · Altri nomi", "short": "2 · Altri nomi", "type": "choice", "opts": PC,
   "cons": "Che punto cardinale è?", "items": [{"q": f"{i}. {w}"} for i, (w, _) in enumerate(ALTRI, 1)],
   "k": [eq(a) for _, a in ALTRI]},
  {"id": "e3", "title": "3 · Vero o falso?", "short": "3 · Vero o falso", "type": "choice", "opts": ["VERO", "FALSO"],
   "full": True, "cons": "Leggi e scegli VERO o FALSO.",
   "items": [{"q": f"{i}. {f}"} for i, (f, _) in enumerate(VF, 1)], "k": [eq(a) for _, a in VF]},
  {"id": "e4", "title": "4 · Completa le frasi", "short": "4 · Completa le frasi", "type": "text", "w": "m",
   "cons": "Scrivi la parola giusta.", "bank": "NORD · SUD · EST · OVEST · DESTRA · SOLE · STELLA POLARE · ORSA MINORE · NORD-EST · NORD-OVEST · SUD-EST · SUD-OVEST",
   "items": [{"pre": a, "post": b} for a, b, _ in COMPLETA], "k": [k for *_, k in COMPLETA]},

  {"part": "Orientarsi"},
  {"id": "e5", "title": "5 · Se guardi a nord…", "short": "5 · Destra, sinistra, dietro", "type": "select", "opts": PC,
   "cons": "Immagina di guardare verso il punto cardinale. Che cosa c'è a destra, a sinistra, dietro?",
   "items": [{"q": f"{i}. {q}"} for i, (q, _) in enumerate(TABELLA, 1)], "k": [eq(a) for _, a in TABELLA]},
  {"id": "e6", "title": "6 · Gira la rosa dei venti", "short": "6 · Gira la rosa", "type": "select", "opts": PC,
   "cons": "La rosa dei venti è girata. Trova i punti cardinali che mancano.",
   "items": [{"q": f"{i}. {q}"} for i, (q, _) in enumerate(GIRA, 1)], "k": [eq(a) for _, a in GIRA]},
  {"id": "e7", "title": "7 · Il contrario", "short": "7 · In città: i contrari", "type": "select",
   "opts": sorted(b for _, b in CONTRARI), "cons": "Scegli il contrario.",
   "items": [{"q": f"{i}. {a}"} for i, (a, _) in enumerate(CONTRARI, 1)], "k": [eq(b) for _, b in CONTRARI]},

  {"part": "La cartina dell'Italia"},
  {"id": "e8", "title": "8 · Dove si trova?", "short": "8 · La cartina dell'Italia", "type": "select", "opts": PC,
   "cons": "Guarda la cartina dell'Italia e scegli il punto cardinale giusto.", "info": MAPPA,
   "items": [{"q": f"{i}. {q}"} for i, (q, _) in enumerate(CITTA, 1)], "k": [eq(a) for _, a in CITTA]},
 ]
}
