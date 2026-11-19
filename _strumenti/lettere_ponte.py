"""Le lettere ponte L M N R (A0, chiesta da Erila il 2026-11-19, dal suo PDF «lettere-ponte-A0-generale»).
Scrive:
  lettere-ponte/parole.js        dati per index.html (esercizi) e giochi.html (le risposte degli esercizi in base64)
  lettere-ponte/registra.html    pagina dove Erila registra i suoni (da _strumenti/registra_modello.html)
  /mnt/project-files/lettere-ponte/DA-REGISTRARE.txt  (se la cartella esiste) elenco dei file audio che mancano
Audio: le pagine cercano prima lettere-ponte/audio/, poi ../sillabe/audio/ e ../sillabe-difficili/audio/, poi la voce del computer.
Uso: python3 _strumenti/lettere_ponte.py   (dalla cartella principale del sito)"""
import base64, json, os, re, unicodedata

def enc(k): return base64.b64encode(json.dumps(k, ensure_ascii=False).encode()).decode()

def slug(t):
    t = unicodedata.normalize("NFD", t.lower())
    t = "".join(c for c in t if unicodedata.category(c) != "Mn")
    return re.sub(r"[^a-z0-9]+", "-", t).strip("-")

# ===== TANTE PAROLE CON IL PONTE: la lettera ponte è tra [ ] =====
BANCA = {
 "L": ["A[L]BERO 🌳", "CA[L]DO 🥵", "PA[L]MA 🌴", "CA[L]ZA 🧦", "VO[L]PE 🦊", "PO[L]PO 🐙", "DO[L]CE 🍬", "FA[L]CO 🦅",
       "CA[L]CIO ⚽", "SO[L]DI 💶", "SA[L]TO 🤸", "DE[L]FINO 🐬", "CO[L]TELLO 🔪", "A[L]BA 🌅", "SA[L]SA 🥫", "PA[L]CO 🎭"],
 "M": ["CA[M]PO 🌾", "GA[M]BA 🦵", "LA[M]PADA 💡", "BO[M]BA 💣", "LA[M]PO ⚡", "BA[M]BINO 🧒", "CA[M]PANA 🔔", "TRO[M]BA 🎺",
       "PO[M]PIERE 🧑‍🚒", "O[M]BRELLO ☂️", "CO[M]PUTER 💻", "GA[M]BERO 🦐", "COLO[M]BA 🕊️", "ZA[M]PA 🐾", "TE[M]PO ⏱️", "LA[M]PONE 🍇"],
 "N": ["DE[N]TE 🦷", "VE[N]TO 🌬️", "MO[N]DO 🌍", "PO[N]TE 🌉", "TE[N]DA ⛺", "PA[N]DA 🐼", "BA[N]CA 🏦", "ME[N]TA 🌿",
       "FO[N]TANA ⛲", "CA[N]DELA 🕯️", "ARA[N]CIA 🍊", "A[N]CORA ⚓", "MO[N]TAGNA ⛰️", "GUA[N]TO 🧤", "SA[N]DALO 👡", "O[N]DA 🌊"],
 "R": ["PO[R]TA 🚪", "BA[R]CA ⛵", "TO[R]TA 🎂", "CA[R]TA 📄", "BO[R]SA 👜", "VE[R]DE 🟢", "CA[R]NE 🥩", "O[R]SO 🐻",
       "CE[R]VO 🦌", "FO[R]MAGGIO 🧀", "SCA[R]PA 👟", "FA[R]FALLA 🦋", "MA[R]TELLO 🔨", "TA[R]TARUGA 🐢", "FO[R]CHETTA 🍴", "A[R]COBALENO 🌈"],
}

def parola(s):
    w, e = s.rsplit(" ", 1)
    i = w.index("[")
    return {"w": w.replace("[", "").replace("]", ""), "i": i, "l": w[i + 1], "e": e}

bank = [parola(s) for l in "LMNR" for s in BANCA[l]]

# ===== ESERCIZI (index.html) =====
SILLABE = {l: [v + l for v in "AEIOU"] for l in "LMNR"}
SCALA = [["CA", "CAL", "CALDO", "🥵"], ["CA", "CAM", "CAMPO", "🌾"], ["CA", "CAN", "CANTO", "🎤"], ["CA", "CAR", "CARTA", "📄"]]

# B · completo la parola (dal PDF)
B = [("🚪", "PO", "TA", "R"), ("🌾", "CA", "PO", "M"), ("🦷", "DE", "TE", "N"), ("🦊", "VO", "PE", "L"),
     ("🦵", "GA", "BA", "M"), ("🌬️", "VE", "TO", "N"), ("⛵", "BA", "CA", "R"), ("🐙", "PO", "PO", "L"),
     ("💡", "LA", "PADA", "M"), ("🌍", "MO", "DO", "N"), ("🎂", "TO", "TA", "R"), ("🍬", "DO", "CE", "L")]
# C · divido in sillabe (dal PDF)
C = [("🌉", "PON-TE"), ("⛺", "TEN-DA"), ("🌴", "PAL-MA"), ("🧦", "CAL-ZA"), ("👜", "BOR-SA"),
     ("🍰", "TOR-TA"), ("🌳", "AL-BE-RO"), ("🧒", "BAM-BI-NO"), ("🎤", "CAN-TAN-TE"), ("🐍", "SER-PEN-TE")]
# D · trovo l'intruso (dal PDF): l'intruso è la parola senza ponte
D = [(["SALTO", "CANE", "ALTO", "PALCO"], 1), (["MANO", "CAMPO", "BOMBA", "LAMPO"], 0), (["VENTO", "CANTO", "NAVE", "DENTE"], 2),
     (["ROSA", "PORTA", "BARCA", "VERDE"], 0), (["CAMPANA", "MELA", "PONTE", "ORTO"], 1)]
# E · scrivo la lettera ponte (parole nuove)
E = [("🦋", "FA", "FALLA", "R"), ("🐬", "DE", "FINO", "L"), ("🐼", "PA", "DA", "N"), ("🎺", "TRO", "BA", "M"),
     ("🐻", "O", "SO", "R"), ("👡", "SA", "DALO", "N"), ("🔪", "CO", "TELLO", "L"), ("☂️", "O", "BRELLO", "M")]
# F · ascolto e scelgo: (parola detta, altra parola)
F = [("CARNE", "CANE"), ("CAPO", "CAMPO"), ("MONDO", "MODO"), ("CALDO", "CADO"), ("VENTO", "VETO"), ("PACCO", "PALCO")]
F_ORD = [1, 0, 0, 1, 0, 1]   # 0 = la parola detta è la prima
FRASI = ["GIOVANNI APRE LA PORTA.", "SILVIA MANGIA LA TORTA.", "CRISTIAN HA UNA BORSA VERDE.", "OGGI FA CALDO E C'È VENTO.",
         "MICHELE VA AL PARCO CON IL BAMBINO.", "SALEAH COMPRA IL FORMAGGIO.", "ENEIDA HA UN OMBRELLO ROSSO."]

def dati():
    f_opts = []
    for (a, b), o in zip(F, F_ORD):
        f_opts.append([a, b] if o == 0 else [b, a])
    return {
        "bank": bank, "sillabe": SILLABE, "scala": SCALA, "frasi": FRASI,
        "B": [{"e": e, "pre": p, "post": q} for e, p, q, _ in B], "kB": enc([k for *_, k in B]),
        "C": [{"e": e, "w": w.replace("-", "")} for e, w in C],
        "kC": enc([[len("".join(w.split("-")[:j + 1])) for j in range(len(w.split("-")) - 1)] for _, w in C]),
        "D": [ws for ws, _ in D], "kD": enc([k for _, k in D]),
        "E": [{"e": e, "pre": p, "post": q} for e, p, q, _ in E], "kE": enc([k for *_, k in E]),
        "F": [{"a": enc(a), "opts": o} for (a, _), o in zip(F, f_opts)], "kF": enc(F_ORD),
    }

def da_registrare():
    """[sezione, slug, testo] in ordine di importanza."""
    out, seen = [], set()
    def add(sez, t):
        sl = slug(t)
        if sl not in seen: seen.add(sl); out.append([sez, sl, t])
    for n in ["ELLE", "EMME", "ENNE", "ERRE"]: add("SILLABE", n)       # i nomi delle lettere (griglia A)
    for l in "LMNR": [add("SILLABE", s) for s in SILLABE[l]]
    for s in SCALA: [add("SILLABE", x) for x in s[:2]]
    for s in SCALA: add("PAROLE", s[2])
    for e, p, q, k in B: add("PAROLE", p + k + q)
    for e, w in C: add("PAROLE", w.replace("-", ""))
    for ws, _ in D: [add("PAROLE", w) for w in ws]
    for e, p, q, k in E: add("PAROLE", p + k + q)
    for a, _ in F: add("PAROLE", a)
    for b in bank: add("ALTRE PAROLE", b["w"])
    for f in FRASI: add("FRASI", f)
    return out

def build():
    os.makedirs("lettere-ponte/audio", exist_ok=True)
    with open("lettere-ponte/parole.js", "w", encoding="utf-8") as f:
        f.write("/* creato da _strumenti/lettere_ponte.py: non modificare a mano */\nwindow.PONTE = "
                + json.dumps(dati(), ensure_ascii=False, indent=1) + ";\n")
    print("scritto lettere-ponte/parole.js:", len(bank), "parole nella banca")
    have = set()
    for d in ["sillabe/audio", "sillabe-difficili/audio", "lettere-ponte/audio"]:
        have |= {os.path.splitext(x)[0] for x in os.listdir(d)}
    tutte = da_registrare()
    altrove = {os.path.splitext(x)[0] for d in ["sillabe/audio", "sillabe-difficili/audio"] for x in os.listdir(d)}
    rec = [r for r in tutte if r[1] not in altrove]       # in registra.html: tutto quello che non c'è già in sillabe*
    tpl = open(os.path.join(os.path.dirname(__file__), "registra_modello.html"), encoding="utf-8").read()
    s = tpl.replace("/*LISTA*/[]", json.dumps(rec, ensure_ascii=False))
    s = s.replace("<title>REGISTRA LE SILLABE DIFFICILI</title>", "<title>REGISTRA LE LETTERE PONTE</title>")
    s = s.replace("← SILLABE DIFFICILI", "← LE LETTERE PONTE")
    s = s.replace('"registra-sillabe-difficili"', '"registra-lettere-ponte"')
    s = s.replace("audio-sillabe-difficili.zip", "audio-lettere-ponte.zip")
    s = s.replace('<meta name="robots" content="noindex">', '<meta name="robots" content="noindex">', 1)
    open("lettere-ponte/registra.html", "w", encoding="utf-8").write(s)
    print("scritto lettere-ponte/registra.html con", len(rec), "voci")
    manca = [r for r in tutte if r[1] not in have]
    dest = "/mnt/project-files/lettere-ponte"
    if os.path.isdir("/mnt/project-files"):
        os.makedirs(dest, exist_ok=True)
        with open(dest + "/DA-REGISTRARE.txt", "w", encoding="utf-8") as f:
            f.write("REGISTRAZIONI PER «LE LETTERE PONTE» (L M N R)\n\n"
                    "IL MODO PIÙ SEMPLICE: apri https://italianol2sai.github.io/lettere-ponte/registra.html\n"
                    "tocca 🎙️, di' la parola, tocca ⏹️. Alla fine tocca «SCARICA ZIP» e manda lo zip a Claude nella chat.\n"
                    "Le registrazioni restano nel browser: puoi farne poche alla volta.\n\n"
                    "Oppure: un file per riga con questo nome (.mp3, .m4a o .wav vanno bene).\n"
                    "Se un file manca, la pagina usa la voce del computer.\n"
                    "Le sillabe e le parole già registrate per «Sillabe» e «Sillabe difficili» non servono di nuovo.\n")
            sez = None
            for s_, sl, t in manca:
                if s_ != sez:
                    sez = s_; f.write("\n=== %s ===\n" % sez)
                f.write("%-22s %s\n" % (sl, t))
        print("scritto", dest + "/DA-REGISTRARE.txt:", len(manca), "audio mancanti")

if __name__ == "__main__":
    build()
