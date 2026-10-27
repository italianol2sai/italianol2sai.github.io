from genera import eq, has, all_
from unita_presente import coniuga, verbo, cl
from unita_passato import k as kp

PRON = [("IO … LAVO LE MANI.", "MI"), ("TU … ALZI ALLE 7.", "TI"), ("LUI … VESTE.", "SI"), ("NOI … SVEGLIAMO PRESTO.", "CI"),
        ("VOI … RIPOSATE.", "VI"), ("LORO … DIVERTONO.", "SI"), ("LEI … PETTINA.", "SI"), ("IO … CHIAMO FATIMA.", "MI")]

TAB_P, TAB_K = coniuga([("LAVARSI", ["mi lavo", "ti lavi", "si lava", "ci laviamo", "vi lavate", "si lavano"]),
    ("METTERSI", ["mi metto", "ti metti", "si mette", "ci mettiamo", "vi mettete", "si mettono"]),
    ("VESTIRSI", ["mi vesto", "ti vesti", "si veste", "ci vestiamo", "vi vestite", "si vestono"])],
    ["IO", "TU", "LUI/LEI", "NOI", "VOI", "LORO"])

PRES_P, PRES_K = cl("1. IO (SVEGLIARSI) [mi sveglio] ALLE OTTO.<br><br>2. TU (ALZARSI) [ti alzi] ALLE NOVE.<br><br>"
    "3. LUI (METTERSI) [si mette] IL GIUBBOTTO.<br><br>4. IO (SPOGLIARSI) [mi spoglio] E (ADDORMENTARSI) [mi addormento].<br><br>"
    "5. TU (DIVERTIRSI) [ti diverti] ALLA FESTA.<br><br>6. VOI (LAVARSI) [vi lavate] IN FRETTA.<br><br>"
    "7. NOI (FARSI) [ci facciamo] LA DOCCIA E (PREPARARSI) [ci prepariamo].<br><br>"
    "8. LORO (PETTINARSI) [si pettinano] E POI (TRUCCARSI) [si truccano].")

def cl_pass(testo):
    import re
    parts, ks = [], []
    for i, p in enumerate(re.split(r"\[([^\]]+)\]", testo)):
        if i % 2: parts.append({"w": "m"}); ks.append(kp(p))
        elif p: parts.append(p)
    return parts, ks

PASS_P, PASS_K = cl_pass("1. IERI IO (SVEGLIARSI) [mi sono svegliat*] ALLE OTTO.<br><br>2. IERI TU (ALZARSI) [ti sei alzat*] ALLE NOVE.<br><br>"
    "3. IERI LUI (METTERSI) [si è messo] IL GIUBBOTTO.<br><br>4. IERI IO (ADDORMENTARSI) [mi sono addormentat*] TARDI.<br><br>"
    "5. IERI TU (DIVERTIRSI) [ti sei divertit*] ALLA FESTA.<br><br>6. IERI VOI (LAVARSI) [vi siete lavat*] IN FRETTA.<br><br>"
    "7. IERI NOI (PREPARARSI) [ci siamo preparat*] PER LA FESTA.<br><br>8. IERI LORO (PETTINARSI) [si sono pettinat§].")

AZIONI = [("⏰ APRO GLI OCCHI LA MATTINA.", "MI SVEGLIO"), ("🛏️ ESCO DAL LETTO.", "MI ALZO"),
          ("🚿 USO L'ACQUA E IL SAPONE.", "MI LAVO"), ("👕 METTO I VESTITI.", "MI VESTO"),
          ("💇 USO IL PETTINE.", "MI PETTINO"), ("🪑 PRENDO UNA SEDIA.", "MI SIEDO"),
          ("😴 LA SERA DORMO.", "MI ADDORMENTO"), ("🎉 SONO ALLA FESTA E STO BENE.", "MI DIVERTO")]

RIFLESSIVI = {
 "title": "🪞 I verbi riflessivi · Esercizi",
 "store": "riflessivi",
 "upper": True,
 "sections": [
  {"part": "Mi, ti, si, ci, vi, si"},
  {"id": "e1", "title": "1 · Scegli il pronome", "short": "1 · Il pronome", "type": "choice",
   "opts": ["MI", "TI", "SI", "CI", "VI"], "cons": "IO MI · TU TI · LUI/LEI SI · NOI CI · VOI VI · LORO SI",
   "items": [{"q": f"{i}. {f}"} for i, (f, _) in enumerate(PRON, 1)], "k": [eq(a) for _, a in PRON]},
  {"id": "e2", "title": "2 · Coniuga i verbi riflessivi", "short": "2 · Coniuga", "type": "cloze",
   "cons": "Scrivi il pronome e il verbo. Esempio: ALZARSI → IO MI ALZO.", "parts": TAB_P, "k": TAB_K},
  {"id": "e3", "title": "3 · Che cosa faccio?", "short": "3 · La mia mattina", "type": "select",
   "cons": "Leggi e scegli il verbo riflessivo giusto.", "opts": sorted(a for _, a in AZIONI),
   "items": [{"q": f"{i}. {q}"} for i, (q, _) in enumerate(AZIONI, 1)], "k": [eq(a) for _, a in AZIONI]},
  {"part": "Presente e passato"},
  {"id": "e4", "title": "4 · Scrivi il presente", "short": "4 · Il presente", "type": "cloze",
   "cons": "Scrivi il pronome e il verbo al presente.", "parts": PRES_P, "k": PRES_K},
  {"id": "e5", "title": "5 · Scrivi il passato", "short": "5 · Il passato", "type": "cloze",
   "cons": "Al passato i verbi riflessivi vogliono sempre ESSERE: IO MI SONO LAVATO/A.", "parts": PASS_P, "k": PASS_K},
  {"id": "e6", "title": "6 ✎ · La tua mattina", "type": "free", "rows": 5,
   "items": ["Che cosa fai la mattina? Scrivi 5 frasi: MI SVEGLIO ALLE…, MI ALZO…, MI LAVO…"]},
 ]
}
