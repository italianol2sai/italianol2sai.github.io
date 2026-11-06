"""Genera una pagina di PROVA dell'indice (prova-indice/index.html) leggendo index.html.

Non modifica index.html né nessun link: legge le attività dalla pagina principale,
le classifica per argomento, livello e tipo e le mostra in 4 viste diverse.

Uso:  python3 _strumenti/indice_prova.py            -> prova-indice/index.html (link relativi al sito)
      python3 _strumenti/indice_prova.py --standalone FILE
                                                    -> file unico con link assoluti al sito pubblicato
"""
import html, json, os, re, sys
from urllib.parse import urljoin
from collections import Counter

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SITE = "https://italianol2sai.github.io/"

# ---- argomenti (schede) -------------------------------------------------
TOPICS = [
    ("primi-passi", "🔤", "Primi passi (A0)"),
    ("casa", "🏠", "La casa"),
    ("cucina", "🍝", "Il cibo e la cucina"),
    ("vestiti", "👕", "I vestiti"),
    ("salute", "🩺", "La salute"),
    ("citta", "🏙️", "La città"),
    ("lavoro", "💼", "Il lavoro"),
    ("famiglia", "👨‍👩‍👧", "La famiglia"),
    ("vivere-italia", "🇮🇹", "Vivere in Italia e educazione civica"),
    ("grammatica", "🧩", "Grammatica"),
    ("video", "🎬", "Videogrammatica"),
    ("percorsi", "📒", "Percorsi e schede"),
    ("altri", "🗂️", "Altri argomenti e letture"),
    ("attualita", "📰", "Tempo libero, feste e società"),
    ("letture", "🎧", "Letture e ascolti"),
    ("scrivere", "✍️", "Scrivere e argomentare"),
    ("lessico", "💬", "Lessico, stile e varietà dell'italiano"),
    ("verifiche", "📝", "Verifiche e simulazioni d'esame"),
]
# id di sezione di index.html -> argomento (si cerca dalla sezione più interna)
SEC2TOPIC = {
    "primi-passi": "primi-passi", "primi-passi-giochi": "primi-passi",
    "casa": "casa", "casa-giochi": "casa", "cucina": "cucina",
    "vestiti": "vestiti", "vestiti-giochi": "vestiti",
    "salute": "salute", "salute-giochi": "salute",
    "citta": "citta", "a1-orientarsi": "citta",
    "lavoro": "lavoro", "lavoro-giochi": "lavoro", "famiglia": "famiglia",
    "educazione-civica": "vivere-italia", "a1-vivere-italia": "vivere-italia", "a2-vivere-italia": "vivere-italia",
    "a1-verbi": "grammatica", "a1-verbi-giochi": "grammatica", "a1-nomi": "grammatica", "a1-nomi-giochi": "grammatica",
    "a1-frase": "grammatica", "a1-preposizioni": "grammatica", "a1-grammatica-extra": "grammatica",
    "a2-grammatica-sito": "grammatica", "a2-grammatica": "grammatica", "b1-grammatica": "grammatica",
    "a1-videogrammatica": "video", "a2-videogrammatica": "video",
    "a1-eserciziario": "percorsi", "a1-percorso": "percorsi", "a2-percorso": "percorsi",
    "a1-argomenti": "altri", "a2-argomenti": "altri",
    "b1": "grammatica", "b2": "grammatica", "c1": "grammatica", "c2": "grammatica",
    "esami": "verifiche",
    "a1": "altri", "a2": "altri",
}
# livelli B1-C2: argomento scelto dalla pagina (se non c'è, resta "grammatica")
HREF2TOPIC = {
    "tempo-libero/": "attualita", "feste/": "attualita", "in-vacanza/": "attualita",
    "ristorante/": "cucina", "letture/macchina": "letture", "https://www.raiplaysound.it": "letture",
    "https://audio-lingua.eu": "letture", "https://kahoot.it/challenge/02754690": "vivere-italia",
    "giochi/c2.html": "lessico",
    "b1-cronaca/": "attualita", "b1-vacanze/": "attualita", "b1-tempo-libero/": "attualita",
    "avanzato/b2-passivo-ambiente": "attualita", "avanzato/b2-congiuntivo-opinioni": "attualita",
    "avanzato/b2-congiuntivo-passato-cinema": "attualita",
    "b1-lavoro/": "lavoro", "b1-problemi/": "casa",
    "avanzato/b2-argomentare": "scrivere", "avanzato/c1-registro-formale": "scrivere",
    "avanzato/c1-saggio-breve": "scrivere",
    "avanzato/c1-linguaggio-burocratico": "vivere-italia",
    "avanzato/b2-lingua-dialetti": "lessico", "avanzato/c1-lingua-che-cambia": "lessico",
    "avanzato/c2-modi-di-dire": "lessico", "avanzato/c2-sfumature-lessico": "lessico",
    "avanzato/c2-varieta-italiano": "lessico", "avanzato/c2-punteggiatura-stile": "lessico",
}
EXERCISE_SITES = ("impariamoitaliano", "onlineitalianclub")
TYPES = [
    ("lezione", "📘", "Lezione"),
    ("flashcard", "🃏", "Flashcard"),
    ("esercizi", "📱", "Esercizi"),
    ("giochi", "🎲", "Giochi e quiz"),
    ("escape", "🔐", "Escape room"),
    ("video", "🎬", "Video"),
    ("verifica", "📝", "Verifiche"),
]
LEVELS = ["A0", "A1", "A2", "B1", "B2", "C1", "C2"]
GAME_SITES = ("wordwall", "kahoot", "learningapps", "languageguide", "impariamoitaliano", "onlineitalianclub",
              "italianonline", "quizlet", "liveworksheets", "wordwall.net")


def parse():
    h = open(os.path.join(ROOT, "index.html"), encoding="utf8").read()
    h = re.sub(r"<!--.*?-->", "", h, flags=re.S)
    tok = re.compile(r'<details([^>]*)>|</details>|<a class="item([^"]*)" href="([^"]+)"[^>]*>(.*?)</a>', re.S)
    stack, items = [], []
    for m in tok.finditer(h):
        s = m.group(0)
        if s.startswith("<details"):
            i = re.search(r'id="([^"]+)"', m.group(1))
            stack.append(i.group(1) if i else None)
        elif s == "</details>":
            stack.pop()
        else:
            b = m.group(4)
            t = re.search(r"<strong>(.*?)</strong>", b, re.S)
            d = re.search(r"</strong>\s*<span>(.*?)</span>", b, re.S)
            tag = re.search(r'class="tag">(.*?)</span>', b)
            title = re.sub(r'<span class="tag">.*?</span>', "", t.group(1)) if t else ""
            clean = lambda x: html.unescape(re.sub(r"<.*?>", "", x)).strip()
            items.append(dict(secs=[x for x in stack if x], href=m.group(3), title=clean(title),
                              desc=clean(d.group(1)) if d else "", tag=tag.group(1) if tag else ""))
    return items


def classify(it):
    href, title, desc = it["href"], it["title"], it["desc"]
    ext = href.startswith("http")
    low = href.lower()
    if "flashcard" in low or "flashcard" in desc.lower():
        ty = "flashcard"
    elif "drive.google.com" in low or "youtube.com" in low or "youtu.be" in low:
        ty = "video"
    elif low.startswith(("missione-", "escape-room")):
        ty = "escape"
    elif ext and any(g in low for g in EXERCISE_SITES):
        ty = "esercizi"
    elif ext and any(g in low for g in GAME_SITES):
        ty = "giochi"
    elif low.startswith("giochi/") or title.lower().startswith("giochi"):
        ty = "giochi"
    elif low.endswith("esercizi.html") or low.startswith("eserciziario-a1/") or title.lower().startswith(("esercizi", "scheda")):
        ty = "esercizi"
    elif low.startswith(("esami/", "verifica-a2", "quiz/")) or title.lower().startswith(("verifica", "simulazione", "test", "quiz")):
        ty = "verifica"
    elif ext:
        ty = "giochi"
    else:
        ty = "lezione"
    # argomento
    tp = "altri"
    for s in reversed(it["secs"]):
        if s in SEC2TOPIC:
            tp = SEC2TOPIC[s]
            break
    for k, v in HREF2TOPIC.items():
        if href.startswith(k):
            tp = v
    if ty == "verifica" and (tp == "altri" or (it["secs"] and it["secs"][0] in ("b1", "b2", "c1", "c2"))):
        tp = "verifiche"
    # livello
    lv = [x for x in LEVELS if re.search(r"\b" + x + r"\b", it["tag"])]
    if not lv:
        top = it["secs"][0] if it["secs"] else ""
        fixed = {"primi-passi": ["A0"], "b1": ["B1"], "b2": ["B2"], "c1": ["C1"], "c2": ["C2"]}
        if top in fixed:
            lv = fixed[top]
        elif top == "a1":
            lv = ["A2"] if "a2" in it["secs"] else ["A1"]
    return ty, tp, lv, ext


def folder(href):
    return "" if href.startswith("http") else href.split("/")[0]


def added_dates():
    """Data (timestamp) in cui ogni file del sito è stato aggiunto, dalla storia git."""
    import subprocess
    out = subprocess.run(["git", "-C", ROOT, "log", "--diff-filter=A", "--name-only", "--format=@%ct", "--", "."],
                         capture_output=True, text=True).stdout
    dates, cur = {}, 0
    for line in out.splitlines():
        if line.startswith("@"):
            cur = int(line[1:])
        elif line:
            dates.setdefault(line, cur)  # il log va dal più nuovo al più vecchio: teniamo la prima aggiunta
            dates[line] = cur
    return dates


def build():
    items, seen = [], set()
    for it in parse():
        if it["href"] in seen:
            continue
        seen.add(it["href"])
        ty, tp, lv, ext = classify(it)
        items.append(dict(t=it["title"], h=it["href"], ty=ty, tp=tp, lv=lv, x=1 if ext else 0))
    # livello mancante: si prende quello della lezione nella stessa cartella (es. casa/ -> casa/esercizi.html)
    lvdir = {}
    for i in items:
        if i["lv"] and folder(i["h"]) and not i["h"].endswith("esercizi.html"):
            lvdir.setdefault(folder(i["h"]), i["lv"])
    for i in items:
        if not i["lv"]:
            i["lv"] = list(lvdir.get(folder(i["h"]), []))
    # data di aggiunta, per «Ultime aggiunte»
    dates = added_dates()
    for i in items:
        if not i["x"]:
            p = i["h"].split("#")[0]
            p = p + "index.html" if p.endswith("/") or not p else p
            if p in dates:
                i["d"] = dates[p]
    return dict(topics=[dict(id=a, icon=b, name=c) for a, b, c in TOPICS],
                types=[dict(id=a, icon=b, name=c) for a, b, c in TYPES], levels=LEVELS, items=items)


TEMPLATE = open(os.path.join(ROOT, "_strumenti", "indice_prova.html"), encoding="utf8").read()


def main():
    data = build()
    c = Counter(i["ty"] for i in data["items"])
    print(len(data["items"]), "attività;", dict(c), "senza livello:", sum(1 for i in data["items"] if not i["lv"]))
    page = TEMPLATE.replace("__DATA__", json.dumps(data, ensure_ascii=False))
    if "--standalone" in sys.argv:
        out = sys.argv[sys.argv.index("--standalone") + 1]
        # pagina fuori dal sito (anteprima): niente <base>, link assoluti che si aprono in una scheda nuova
        for it in data["items"]:
            it["h"] = urljoin(SITE, it["h"])
        page = TEMPLATE.replace("__DATA__", json.dumps(data, ensure_ascii=False))
        page = page.replace('<base href="__BASE__">', '<base target="_blank">').replace('href="../"', 'href="%s"' % SITE)
    else:
        out = os.path.join(ROOT, "prova-indice", "index.html")
        os.makedirs(os.path.dirname(out), exist_ok=True)
        page = page.replace("__BASE__", "../")
    open(out, "w", encoding="utf8").write(page)
    print("scritto", out)


if __name__ == "__main__":
    main()
