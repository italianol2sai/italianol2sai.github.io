"""Pagine «Giochi» per i livelli B1, B2, C1, C2 (2026-11-06, Erila: «puoi aggiungere giochi per i livelli più alti»).
Tre giochi da comune/giochi-avanzati.js: quiz a tempo (completa la frase), abbina, riordina la frase.
Testi scritti da Claude sugli argomenti delle unità di ogni livello, in minuscolo (regola: maiuscolo solo A0/A1).
Uso: python3 _strumenti/giochi_avanzati.py → giochi/<livello>.html"""
import json, os

RADICE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# quiz: [frase con ___, risposta giusta, sbagliata, sbagliata]
LIVELLI = {
 "b1": dict(titolo="🚀 Giochi B1", sotto="Congiuntivo, condizionale, ci e ne, pronomi relativi, connettivi", quiz=[
  ["Penso che Marco ___ ragione.", "abbia", "ha", "avesse"],
  ["Se avessi tempo, ___ un corso di cucina.", "farei", "faccio", "farò"],
  ["La ragazza ___ ti ho parlato è Silvia.", "di cui", "che", "a cui"],
  ["Vai al mercato? Sì, ___ vado domani.", "ci", "ne", "lo"],
  ["Quante mele compri? ___ compro tre.", "Ne", "Ci", "Le"],
  ["Spero che domani non ___.", "piova", "piove", "pioverà"],
  ["Al tuo posto, io ___ dal medico.", "andrei", "vado", "andassi"],
  ["Quando ero piccolo, ___ sempre al mare.", "andavo", "sono andato", "andrei"],
  ["Ieri ___ Giovanni alla stazione.", "ho incontrato", "incontravo", "incontrerei"],
  ["Studio molto ___ voglio superare l'esame.", "perché", "anche se", "invece"],
  ["È stanco, ___ continua a lavorare.", "eppure", "perciò", "quindi"],
  ["Il libro ___ leggo è interessante.", "che", "cui", "di cui"],
  ["Bisogna che tutti ___ il modulo.", "firmino", "firmano", "firmeranno"],
  ["Se piove, ___ a casa.", "resto", "resterei", "restassi"],
  ["Credo che loro ___ già partiti.", "siano", "sono", "fossero"],
  ["Domani ___ a Bari alle otto, se il treno è puntuale.", "arriverò", "arriverei", "arrivassi"],
 ], coppie=[
  ["perciò", "quindi"], ["invece", "al contrario"], ["anche se", "nonostante questo"], ["inoltre", "in più"],
  ["comunque", "in ogni caso"], ["cioè", "vale a dire"], ["purtroppo", "per sfortuna"], ["finalmente", "dopo tanta attesa"],
 ], frasi=[
  "Penso che sia una buona idea", "Se avessi soldi comprerei una casa", "Ne ho comprati tre chili",
  "La città in cui vivo è Bari", "Vorrei prenotare un tavolo per due", "Spero che tu stia bene",
  "Quando sono arrivato pioveva", "Ci vado ogni giorno in autobus",
 ]),
 "b2": dict(titolo="🏔️ Giochi B2", sotto="Periodo ipotetico, discorso indiretto, passivo, pronomi combinati, futuro anteriore", quiz=[
  ["Se l'avessi saputo, te l'___ detto.", "avrei", "avessi", "avrò"],
  ["Ha detto che ___ il giorno dopo.", "sarebbe venuto", "verrà", "venga"],
  ["La casa è ___ costruita nel 1950.", "stata", "stato", "essere"],
  ["Pensavo che tu ___ già a casa.", "fossi", "sei", "sarai"],
  ["Il libro? ___ ho prestato ieri a Michele.", "Gliel'", "Gli l'", "Lo gli"],
  ["Non risponde: ___ il telefono a casa.", "avrà dimenticato", "dimenticherà", "dimenticasse"],
  ["___ di casa tardi, ha perso il treno.", "Essendo uscito", "Uscendo stato", "Uscito essendo"],
  ["Vorrei che voi ___ più attenzione.", "faceste", "fate", "farete"],
  ["Benché ___ stanca, Saleah è uscita.", "fosse", "era", "sarà"],
  ["Le chiavi? Te ___ do subito.", "le", "gli", "ne"],
  ["Questa legge ___ approvata dal Parlamento nel 2020.", "venne", "ebbe", "fece"],
  ["Finito il lavoro, Cristian ___ a casa.", "è tornato", "tornando", "tornato"],
  ["Se ___ più tempo, studierei il cinese.", "avessi", "avrei", "ho"],
  ["Dubito che ___ vero.", "sia", "è", "sarà"],
  ["Secondo me, ___ meglio lavorare da casa.", "sarebbe", "fosse", "sia stato"],
 ], coppie=[
  ["tuttavia", "però"], ["dunque", "quindi"], ["sebbene", "anche se"], ["affinché", "con lo scopo che"],
  ["qualora", "nel caso in cui"], ["a patto che", "solo se"], ["malgrado", "nonostante"], ["poiché", "dato che"],
 ], frasi=[
  "Se fossi in te accetterei il lavoro", "Mi ha detto che sarebbe arrivato tardi", "Il ponte è stato costruito in due anni",
  "Pensavo che fosse un film comico", "Gliel'ho spiegato tre volte", "Avrà perso l'autobus",
  "Uscendo di casa ho incontrato Eneida", "Secondo me il lavoro da casa è utile",
 ]),
 "c1": dict(titolo="🦅 Giochi C1", sotto="Passato remoto, concordanza, registro formale, burocrazia, verbi pronominali", quiz=[
  ["Garibaldi ___ a Marsala nel 1860.", "sbarcò", "sbarcava", "sbarcasse"],
  ["Credevo che lui ___ già la notizia.", "avesse saputo", "ha saputo", "saprà"],
  ["Magari ___ vero!", "fosse", "è", "sarebbe"],
  ["Non ___ la faccio più: sono stanchissimo.", "ce", "ci", "ne"],
  ["Purché tu ___ in orario, puoi venire.", "arrivi", "arrivassi", "arriverai"],
  ["Perché te la ___? Era solo uno scherzo!", "prendi", "fai", "cavi"],
  ["___ Direttore, Le scrivo per chiedere un appuntamento.", "Gentile", "Ciao", "Caro amico"],
  ["A meno che non ___, partiamo domani.", "piova", "piove", "pioverà"],
  ["Il richiedente ___ allegare copia del documento.", "è tenuto ad", "ha voglia di", "gli tocca"],
  ["___ la lettera, uscì di casa.", "Scritta", "Scrivente", "Scrisse"],
  ["Sapevo che ___ alle otto.", "sarebbe partito", "partirà", "parta"],
  ["Qualora ___ problemi, contatti l'ufficio.", "ci fossero", "ci sono", "ci saranno"],
  ["Dopo ___, guardarono un film.", "aver cenato", "cenando", "cenato"],
  ["Nonostante ___ tardi, continuarono a lavorare.", "fosse", "era", "sarà"],
  ["Me la sono ___: l'esame è andato bene!", "cavata", "cavato", "cavati"],
 ], coppie=[
  ["in allegato", "insieme a questa lettera"], ["il richiedente", "chi fa la domanda"], ["entro e non oltre", "al massimo fino a"],
  ["pervenire", "arrivare"], ["la scadenza", "l'ultimo giorno utile"], ["esibire", "mostrare"],
  ["il modulo", "il foglio da compilare"], ["previo appuntamento", "solo se hai prenotato"],
 ], frasi=[
  "Le scrivo per chiedere un appuntamento", "Magari fosse vero", "Non ce la faccio più",
  "Benché piovesse uscirono lo stesso", "Finita la lezione tornammo a casa", "Credevo che fossi già partito",
  "La domanda va presentata entro il 30 giugno", "Me la sono cavata bene all'esame",
 ]),
 "c2": dict(titolo="👑 Giochi C2", sotto="Modi di dire, frasi scisse e dislocazioni, ipotesi senza se, nominalizzazione", quiz=[
  ["Non vedo l'ora: sono sulle ___.", "spine", "nuvole", "ali"],
  ["In bocca al ___!", "lupo", "gatto", "cane"],
  ["È stato Giovanni ___ ha chiamato.", "che", "a", "di"],
  ["Il caffè, ___ prendo sempre amaro.", "lo", "la", "ne"],
  ["___ saputo prima, sarei venuto.", "Avessi", "Avrei", "Ho"],
  ["Dovesse ___, chiamami.", "piovere", "piove", "pioverà"],
  ["La ___ del ponte è durata tre anni.", "costruzione", "costruire", "costruito"],
  ["L'___ dei prezzi preoccupa le famiglie.", "aumento", "aumentare", "aumentato"],
  ["Questa borsa costa un occhio della ___.", "testa", "faccia", "mano"],
  ["Prendere due piccioni con una ___.", "fava", "pietra", "mano"],
  ["Ha ___ un errore grave.", "commesso", "emesso", "ammesso"],
  ["Acqua in ___: non dirlo a nessuno!", "bocca", "gola", "testa"],
  ["Ne ho fin sopra i ___: sono stufo.", "capelli", "occhi", "piedi"],
  ["Non mettere il carro davanti ai ___.", "buoi", "cavalli", "asini"],
  ["Di questo problema, ___ parleremo domani.", "ne", "ci", "lo"],
 ], coppie=[
  ["essere al verde", "non avere soldi"], ["costare un occhio della testa", "costare moltissimo"], ["acqua in bocca", "non dirlo a nessuno"],
  ["in bocca al lupo", "buona fortuna"], ["avere le mani bucate", "spendere troppo"], ["tagliare la corda", "andare via di nascosto"],
  ["non avere peli sulla lingua", "dire tutto apertamente"], ["fare orecchie da mercante", "fingere di non sentire"],
 ], frasi=[
  "È stata Silvia a trovare la soluzione", "Il giornale lo compro ogni mattina", "Avessi saputo prima sarei venuto",
  "L'aumento dei prezzi preoccupa molti", "Ne ho fin sopra i capelli", "Dovesse servirti chiamami pure",
  "Di questo problema ne parleremo domani", "Non ha peli sulla lingua",
 ]),
}

PAGINA = """<!doctype html>
<html lang="it">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>%(titolo_breve)s</title>
<link href="https://fonts.googleapis.com/css2?family=Atkinson+Hyperlegible:wght@400;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="../comune/giochi.css">
<style>
  body { text-transform: none; }
  .g-schede.tre { grid-template-columns: repeat(3, 1fr); }
  .g-frase { font-size: 1.25rem; font-weight: 700; text-align: center; margin: 8px 0 14px; line-height: 1.5; }
  .g-frase .buco { display: inline-block; min-width: 3.5em; border-bottom: 3px solid var(--g-acc); color: var(--g-acc); }
  .g-abbina { display: grid; grid-template-columns: 1fr 1fr; gap: 8px; }
  .g-col { display: flex; flex-direction: column; gap: 8px; }
  .g-col .g-btn { font-size: .95rem; padding: 10px; min-height: 56px; }
  .g-btn.op.sel { border-color: var(--g-acc); background: var(--g-acc); color: #fff; }
  .g-btn:disabled { cursor: default; }
  .g-riga { min-height: 64px; border: 2px dashed var(--g-line); border-radius: 12px; padding: 8px; display: flex; flex-wrap: wrap; gap: 6px; align-content: flex-start; }
  .g-pezzi { display: flex; flex-wrap: wrap; gap: 6px; justify-content: center; margin: 12px 0; min-height: 48px; }
  .g-pezzo { border: 2px solid var(--g-line); background: var(--g-bg); color: var(--g-ink); border-radius: 10px; padding: 10px 12px; font: inherit; font-weight: 700; cursor: pointer; }
  .g-riga .g-pezzo { background: var(--g-acc); border-color: var(--g-acc); color: #fff; }
  .g-esito { text-align: center; font-weight: 700; min-height: 1.4em; } .g-esito.ok { color: var(--g-ok); } .g-esito.no { color: var(--g-no); }
  .g-azioni { display: flex; gap: 8px; justify-content: center; flex-wrap: wrap; }
</style>
</head>
<body>
<div class="g-wrap">
  <a class="back" href="../#%(sezione)s">← Tutti i materiali</a>
  <h1>%(titolo)s</h1>
  <p class="sub">%(sotto)s · 3 giochi corti per ripassare</p>
  <main id="giochi"></main>
</div>
<script>window.GIOCHI = %(dati)s;</script>
<script src="../comune/giochi-avanzati.js"></script>
</body>
</html>
"""

if __name__ == "__main__":
    os.makedirs(os.path.join(RADICE, "giochi"), exist_ok=True)
    for liv, d in LIVELLI.items():
        dati = json.dumps({"id": liv, "quiz": d["quiz"], "coppie": d["coppie"], "frasi": d["frasi"]}, ensure_ascii=False)
        open(os.path.join(RADICE, "giochi", liv + ".html"), "w", encoding="utf-8").write(
            PAGINA % {"titolo": d["titolo"], "titolo_breve": d["titolo"].split(" ", 1)[1], "sotto": d["sotto"], "sezione": liv, "dati": dati})
        print("scritto giochi/%s.html" % liv)
