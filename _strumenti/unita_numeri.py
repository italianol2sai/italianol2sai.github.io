"""Esercizi «I numeri 1–1000» (A0/A1, MAIUSCOLO) → numeri/esercizi.html.
Uso: python3 _strumenti/unita_numeri.py   (dalla cartella principale del sito)
La flashcard e i giochi sono in numeri/index.html e numeri/giochi.html (stessi nomi dei numeri di numeri/numeri.js)."""
import base64, os, sys
sys.path.insert(0, os.path.dirname(__file__))
from genera import eq, build

UNITS = ["", "UNO", "DUE", "TRE", "QUATTRO", "CINQUE", "SEI", "SETTE", "OTTO", "NOVE"]
TEENS = ["DIECI", "UNDICI", "DODICI", "TREDICI", "QUATTORDICI", "QUINDICI", "SEDICI", "DICIASSETTE", "DICIOTTO", "DICIANNOVE"]
TENS = ["", "", "VENTI", "TRENTA", "QUARANTA", "CINQUANTA", "SESSANTA", "SETTANTA", "OTTANTA", "NOVANTA"]

def pezzi(n, elidi=True):
    if n == 1000: return ["MILLE"]
    h, r, out = n // 100, n % 100, []
    if h: out.append("CENTO" if h == 1 else UNITS[h] + "CENTO")
    if r:
        if r < 10: out.append(UNITS[r])
        elif r < 20: out.append(TEENS[r - 10])
        else:
            t, u = divmod(r, 10); d = TENS[t]
            if u in (1, 8): d = d[:-1]
            out.append(d)
            if u: out.append(UNITS[u])
    if elidi and h and len(out) > 1 and out[1][0] == "O": out[0] = out[0][:-1]
    if n > 10 and out[-1] == "TRE": out[-1] = "TRÉ"
    return out

def nome(n): return "".join(pezzi(n))

def lettere(n):
    """Risposte accettate in lettere: CENTOTTO / CENTOOTTO, anche staccato (il motore toglie gli accenti)."""
    v = []
    for el in (True, False):
        p = pezzi(n, el)
        for s in ("".join(p), " ".join(p)):
            if s not in v: v.append(s)
    return eq(*v)

def cifra(n): return eq(str(n), "{:,}".format(n).replace(",", "."))

def ascolta(n):
    """Pulsante che legge il numero con la voce del computer; il numero non è scritto nella pagina."""
    b = base64.b64encode(nome(n).lower().encode()).decode()
    return ('<button type="button" class="say" onclick="var u=new SpeechSynthesisUtterance(decodeURIComponent(escape(atob(\'%s\'))));'
            'u.lang=\'it-IT\';u.rate=.75;speechSynthesis.cancel();speechSynthesis.speak(u)">🔊</button>' % b)

E1 = [12, 14, 15, 17, 19, 13]
E2 = [30, 50, 70, 90, 60, 80]
E3 = [21, 28, 33, 46, 58, 71, 83, 99]
E4 = [200, 500, 700, 900, 300, 1000]
E5 = [101, 108, 115, 123, 180, 199]
E6 = [345, 278, 412, 650, 803, 999]
E7 = [(300, 40, 5), (200, 70, 1), (600, 8), (900, 90, 3), (100, 50), (400, 10)]
E8 = [24, 67, 150, 316, 480, 725, 888, 1000]
E9 = [("L'AFFITTO COSTA <b>SEICENTOCINQUANTA</b> EURO AL MESE.", 650),
      ("GIOVANNI ABITA IN VIA SPARANO <b>CENTOQUARANTACINQUE</b>.", 145),
      ("SILVIA PAGA LA BOLLETTA: <b>DUECENTOTRENTA</b> EURO.", 230),
      ("IL TRENO PER LECCE COSTA <b>DICIOTTO</b> EURO.", 18),
      ("CRISTIAN LAVORA <b>CENTOSESSANTA</b> ORE AL MESE.", 160),
      ("SALEAH COMPRA UN TELEFONO DA <b>TRECENTONOVANTANOVE</b> EURO.", 399)]

TEORIA_20 = ("<p>DA 1 A 20 I NUMERI SI IMPARANO A MEMORIA.</p><p>11 UNDICI · 12 DODICI · 13 TREDICI · 14 QUATTORDICI · 15 QUINDICI · "
             "16 SEDICI · 17 DICIASSETTE · 18 DICIOTTO · 19 DICIANNOVE · 20 VENTI</p>")
TEORIA_DEC = ("<p>LE DECINE: 10 DIECI · 20 VENTI · 30 TRENTA · 40 QUARANTA · 50 CINQUANTA · 60 SESSANTA · 70 SETTANTA · 80 OTTANTA · 90 NOVANTA · 100 CENTO</p>"
              "<p>DECINA + UNITÀ = UNA PAROLA: VENTI + DUE = <b>VENTIDUE</b>.</p>"
              "<p>CON <b>UNO</b> E <b>OTTO</b> LA DECINA PERDE L'ULTIMA LETTERA: VENT<b>UNO</b>, TRENT<b>OTTO</b>.<br>"
              "CON <b>TRE</b> C'È L'ACCENTO: VENTITRÉ, TRENTATRÉ.</p>")
TEORIA_CENT = ("<p>100 <b>CENTO</b> · 200 DUECENTO · 300 TRECENTO · 400 QUATTROCENTO · 500 CINQUECENTO · 600 SEICENTO · "
               "700 SETTECENTO · 800 OTTOCENTO · 900 NOVECENTO · 1000 <b>MILLE</b></p>"
               "<p>I NUMERI GRANDI SI LEGGONO A PEZZI, COME UN TRENO 🚂: CENTINAIA + DECINE + UNITÀ.<br>"
               "345 = 300 + 40 + 5 = TRECENTO + QUARANTA + CINQUE = <b>TRECENTOQUARANTACINQUE</b></p>"
               "<p>SI SCRIVE TUTTO ATTACCATO. CENTO + OTTO = <b>CENTOTTO</b> (O CENTOOTTO).</p>")

def sel(id_, title, short, nums, opts_extra, cons=None):
    opts = sorted({nome(n) for n in nums} | set(opts_extra))
    s = {"id": id_, "title": title, "short": short, "type": "select", "opts": opts,
         "items": [{"q": "%d. <b>%d</b>" % (i + 1, n)} for i, n in enumerate(nums)], "k": [eq(nome(n)) for n in nums]}
    if cons: s["cons"] = cons
    return s

NUMERI = {
 "title": "🔢 I numeri 1–1000 · Esercizi",
 "store": "numeri1000",
 "upper": True,
 "sub": "PRIMA GUARDA LA REGOLA, POI SCRIVI E PREMI «CONTROLLA». LE RISPOSTE RESTANO SALVATE SU QUESTO TELEFONO.",
 "sections": [
  {"part": "1 · Da 1 a 20", "teoria": TEORIA_20},
  sel("e1", "1 · Come si dice?", "1 · Da 11 a 20", E1, ["SEDICI", "DICIOTTO", "VENTI", "UNDICI"]),

  {"part": "2 · Le decine", "teoria": TEORIA_DEC},
  {"id": "e2", "title": "2 · Scrivi il numero con le cifre", "short": "2 · Le decine", "type": "text", "w": "s",
   "cons": "ESEMPIO: QUARANTA → 40",
   "items": [{"q": "%d. %s" % (i + 1, nome(n))} for i, n in enumerate(E2)], "k": [cifra(n) for n in E2]},
  {"id": "e3", "title": "3 · Scrivi il numero in lettere", "short": "3 · Decine e unità", "type": "text", "w": "m",
   "cons": "ESEMPIO: 22 → VENTIDUE. ATTENZIONE A UNO, OTTO E TRE!",
   "items": [{"q": "%d. <b>%d</b>" % (i + 1, n)} for i, n in enumerate(E3)], "k": [lettere(n) for n in E3]},

  {"part": "3 · Le centinaia e i numeri grandi", "teoria": TEORIA_CENT},
  sel("e4", "4 · Le centinaia: come si dice?", "4 · Le centinaia", E4, ["OTTOCENTO", "SEICENTO", "CENTO", "MILLECENTO"]),
  {"id": "e5", "title": "5 · Da 100 a 200: scrivi in lettere", "short": "5 · Da 100 a 200", "type": "text", "w": "m",
   "cons": "ESEMPIO: 102 → CENTODUE · 130 → CENTOTRENTA",
   "items": [{"q": "%d. <b>%d</b>" % (i + 1, n)} for i, n in enumerate(E5)], "k": [lettere(n) for n in E5]},
  {"id": "e6", "title": "6 · Leggi la parola e scrivi il numero", "short": "6 · Dalla parola al numero", "type": "text", "w": "s",
   "cons": "ESEMPIO: DUECENTOCINQUANTUNO → 251",
   "items": [{"q": "%d. %s" % (i + 1, nome(n))} for i, n in enumerate(E6)], "k": [cifra(n) for n in E6]},
  {"id": "e7", "title": "7 · Costruisci il numero 🚂", "short": "7 · Costruisci", "type": "text", "w": "s",
   "cons": "METTI INSIEME I PEZZI. ESEMPIO: 200 + 30 + 4 = 234",
   "items": [{"q": "%d. %s =" % (i + 1, " + ".join(map(str, p)))} for i, p in enumerate(E7)], "k": [cifra(sum(p)) for p in E7]},

  {"part": "4 · Ascolta"},
  {"id": "e8", "title": "8 · Ascolta e scrivi il numero con le cifre", "short": "8 · Ascolta", "type": "text", "w": "s",
   "cons": "TOCCA 🔊 E SCRIVI IL NUMERO. PUOI ASCOLTARE TANTE VOLTE.",
   "items": [{"q": "%d. %s" % (i + 1, ascolta(n))} for i, n in enumerate(E8)], "k": [cifra(n) for n in E8]},

  {"part": "5 · I numeri nella vita"},
  {"id": "e9", "title": "9 · Leggi e scrivi il numero", "short": "9 · Nella vita", "type": "text", "w": "s",
   "cons": "SCRIVI IL NUMERO IN CIFRE.",
   "items": [{"q": "%d. %s" % (i + 1, q)} for i, (q, n) in enumerate(E9)], "k": [cifra(n) for q, n in E9]},
  {"id": "e10", "title": "10 🎤 · Leggi ad alta voce", "type": "record",
   "items": ["LEGGI QUESTI NUMERI: 17 · 45 · 100 · 128 · 360 · 799 · 1000. POI DI' QUANTO PAGHI DI AFFITTO O DI SPESA IN UN MESE."]},
 ]
}

if __name__ == "__main__":
    build("numeri/esercizi.html", NUMERI)
