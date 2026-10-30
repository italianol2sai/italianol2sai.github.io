"""Italiano per lavorare in cucina, A2 (2026-10-30). Erila: «usa anche attività di L'italiano per la cucina». Il libro è sul suo PC
ed è protetto: qui si prendono solo gli argomenti tipici (brigata, cotture, igiene/HACCP, ricette) che mancavano in cucina-lavoro/.
Testi ed esercizi scritti per il sito. Pagine in cucina-pro/<nome>.html, minuscolo."""
from unita_drive import vf, scegli, menu, scrivi, ordina, completa, libero, parla
from teoria import tab, es

def pagina(icona, titolo, sections):
    return {"title": "%s %s · Esercizi A2" % (icona, titolo), "store": "cucpro-" + titolo.lower().replace(" ", "-")[:18], "sections": sections}

P = {}

P["brigata"] = pagina("👨‍🍳", "La brigata di cucina", [
  {"part": "Chi fa che cosa?", "teoria":
     tab(("lo chef / il capocuoco", "dirige la cucina, decide il menù"), ("il sous-chef", "aiuta e sostituisce lo chef"), ("il cuoco di partita", "prepara un tipo di piatti (primi, carni, pesce…)"),
         ("il pasticciere", "prepara i dolci"), ("il commis / l'aiuto cuoco", "aiuta, pulisce e taglia le verdure"), ("il lavapiatti", "lava piatti, pentole e attrezzi")) +
     "in cucina si danno ordini brevi con l'imperativo: <b>Taglia</b> le cipolle! <b>Porta</b> il sale! <b>Pulisci</b> il banco!"},
  menu(["lo chef", "il pasticciere", "l'aiuto cuoco", "il lavapiatti", "il sous-chef"],
       [("1. Oggi lo chef è malato: chi lo sostituisce?", "il sous-chef"), ("2. Chi prepara il tiramisù?", "il pasticciere"),
        ("3. Chi lava le pentole?", "il lavapiatti"), ("4. Chi pela le patate e taglia le verdure?", "l'aiuto cuoco"), ("5. Chi decide il menù della settimana?", "lo chef")],
       "1 · Chi è?", "1 · La brigata", "e1"),
  scrivi([("1. (tagliare, tu) ___ le zucchine a rondelle!", ["taglia"]), ("2. (lavare, tu) ___ l'insalata!", ["lava"]), ("3. (accendere, tu) ___ il forno a 180 gradi!", ["accendi"]),
          ("4. (pulire, tu) ___ il piano di lavoro!", ["pulisci"]), ("5. (mettere, tu) ___ l'acqua sul fuoco!", ["metti"])], "2 · Gli ordini dello chef", "2 · L'imperativo", "e2"),
  parla("e3", 3, "Sei il capo della cucina. Dai 4 ordini al tuo aiuto per preparare un piatto di pasta."),
])

P["cotture"] = pagina("🔥", "Come si cuoce?", [
  {"part": "I metodi di cottura", "teoria":
     tab(("bollire / lessare", "in acqua che bolle", "la pasta, le uova sode"), ("friggere", "in olio molto caldo", "le patatine, il pesce"),
         ("arrostire / cuocere al forno", "nel forno, a calore secco", "l'arrosto, le patate al forno"), ("grigliare / alla griglia", "sulla griglia o sulla piastra", "la carne, le verdure"),
         ("saltare in padella", "in padella, velocemente", "le verdure, la pasta con il sugo"), ("cuocere al vapore", "con il vapore, senza toccare l'acqua", "le verdure, il pesce")) +
     "il participio diventa aggettivo: pasta <b>bollita</b>, pesce <b>fritto</b>, carne <b>arrosto</b> / <b>arrostita</b>, verdure <b>grigliate</b>."},
  menu(["bollire", "friggere", "al forno", "alla griglia", "al vapore"],
       [("1. Le patatine nell'olio caldo: le devo ___.", "friggere"), ("2. Gli spaghetti in pentola con l'acqua: li devo ___.", "bollire"),
        ("3. La lasagna: la cuocio ___.", "al forno"), ("4. Le verdure senza grassi, sopra l'acqua: le cuocio ___.", "al vapore"),
        ("5. La bistecca sulla piastra: la cuocio ___.", "alla griglia")], "1 · Come lo cuoci?", "1 · Le cotture", "e1"),
  scrivi([("1. pesce (friggere) → pesce ___", ["fritto"]), ("2. uova (bollire) → uova ___", ["bollite", "sode"]), ("3. melanzane (grigliare) → melanzane ___", ["grigliate"]),
          ("4. patate (arrostire) → patate ___", ["arrostite", "arrosto"]), ("5. verdure (cuocere al vapore) → verdure ___ al vapore", ["cotte"])],
         "2 · Scrivi l'aggettivo", "2 · Il participio", "e2", cons="Attenzione all'accordo: maschile/femminile, singolare/plurale."),
  vf(["1. Per friggere serve olio molto caldo.", "2. Al vapore il cibo è dentro l'acqua.", "3. La pasta si cuoce in acqua che bolle.", "4. Saltare in padella vuol dire cuocere per molte ore."],
     ["Vero", "Falso", "Vero", "Falso"], "3 · Vero o falso?", "3 · Vero o falso", "e3"),
])

P["igiene"] = pagina("🧼", "Igiene e sicurezza in cucina", [
  {"part": "Le regole", "teoria":
     "in cucina si seguono le regole <b>HACCP</b> per un cibo sicuro. Per dire una regola:" +
     tab(("bisogna / è obbligatorio + infinito", "Bisogna lavarsi le mani."), ("è vietato + infinito", "È vietato fumare."), ("si deve / non si deve + infinito", "Non si deve ricongelare il cibo."),
         ("va / vanno + participio", "La carne cruda va tenuta separata.")) +
     "parole utili: la temperatura, il frigorifero (0-4 °C), il congelatore (-18 °C), la data di scadenza, il tagliere, i guanti, la cuffia."},
  vf(["1. Prima di cucinare bisogna lavarsi le mani.", "2. Si può usare lo stesso tagliere per la carne cruda e per la verdura cotta senza lavarlo.",
      "3. Il frigorifero deve stare fra 0 e 4 gradi.", "4. Un cibo scongelato si può ricongelare.", "5. In cucina bisogna mettere la cuffia sui capelli."],
     ["Vero", "Falso", "Vero", "Falso", "Vero"], "1 · Vero o falso?", "1 · Le regole", "e1"),
  menu(["bisogna", "è vietato", "va"],
       [("1. ___ fumare in cucina.", "è vietato"), ("2. ___ controllare la data di scadenza.", "bisogna"), ("3. Il pesce fresco ___ conservato in frigorifero.", "va"),
        ("4. ___ entrare in cucina con gli anelli e l'orologio.", "è vietato"), ("5. ___ pulire il banco dopo ogni lavorazione.", "bisogna")], "2 · Completa la regola", "2 · Le regole", "e2"),
  libero("e3", 3, "Le regole della mia cucina", "Scrivi 5 regole di igiene per un nuovo collega che comincia a lavorare con te.", ["Le regole"], rows=5),
])

P["ricetta"] = pagina("📋", "Leggere e scrivere una ricetta", [
  {"part": "Quantità e misure", "teoria":
     tab(("g / kg", "grammi / chili", "500 g di farina"), ("ml / l", "millilitri / litri", "250 ml di latte"), ("un cucchiaio / un cucchiaino", "", "un cucchiaio d'olio"),
         ("un pizzico", "pochissimo", "un pizzico di sale"), ("q.b.", "quanto basta", "pepe q.b."), ("uno spicchio", "di aglio", "uno spicchio d'aglio")) +
     "nella ricetta i verbi sono all'imperativo (tu o voi) o all'infinito: <b>Aggiungi</b> / <b>Aggiungere</b> il sale."},
  menu(["un pizzico", "uno spicchio", "un cucchiaio", "q.b.", "un litro"],
       [("1. ___ di sale", "un pizzico"), ("2. ___ d'aglio", "uno spicchio"), ("3. ___ di brodo", "un litro"), ("4. ___ d'olio", "un cucchiaio"), ("5. pepe ___", "q.b.")],
       "1 · La quantità giusta", "1 · Le quantità", "e1"),
  ordina(["Metti l'acqua sul fuoco e porta a bollore.", "Aggiungi il sale grosso.", "Butta le orecchiette e mescola.", "Dopo 12 minuti scola la pasta.", "Condisci con le cime di rapa e servi."],
         "2 · Metti in ordine la ricetta", "2 · La ricetta", "e2"),
  libero("e3", 3, "La mia ricetta", "Scrivi una ricetta del tuo paese: ingredienti con le quantità e preparazione con l'imperativo.", ["Ingredienti", "Preparazione"], rows=5),
])

PAGINE = [("cucina-pro/%s.html" % k, d) for k, d in P.items()]
