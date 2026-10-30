"""Riquadri «La regola» aggiunti alle pagine di grammatica più vecchie (2026-10-30, regola di Erila: prima degli esercizi
di grammatica sempre una teoria pratica e semplice). genera.py importa questo modulo prima di costruire le pagine."""
from teoria import tab, es, minus, ESSERE_AVERE, AGGETTIVI, ARTICOLI, PRESENTE, RIFLESSIVI, MODALI, PIACERE, PASSATO, PREP, PRONOMI_DIR, POSSESSIVI

def applica(pagina, teorie):
    for parte, testo in teorie.items():
        trovate = [s for s in pagina["sections"] if s.get("part") == parte]
        assert len(trovate) == 1, (pagina["title"], parte)
        trovate[0]["teoria"] = testo if pagina.get("upper") else minus(testo)

from unita_aggettivi import AGGETTIVI as P_AGG
from unita_nomi import NOMI as P_NOMI
from unita_presente import PRESENTE as P_PRES
from unita_possessivi import POSSESSIVI as P_POSS
from unita_frase import FRASE as P_FRASE
from unita_domande import DOMANDE as P_DOM
from unita_passato import PASSATO as P_PASS
from unita_modali import MODALI as P_MOD
from unita_riflessivi import RIFLESSIVI as P_RIFL
from unita_preposizioni import PREPOSIZIONI as P_PREP
from unita_pronomi import PRONOMI as P_PRON
from unita_primi2 import SUONI, QUESTO, CE, PIACE
from unita_libri import TEMPO, VAC
from unita_lavoro import CHE_LAVORO
from unita_b1 import U1, U2, U3, U4, U5

applica(P_AGG, {
  "Che cos'è un aggettivo?": "L'AGGETTIVO DICE <b>COM'È</b> UNA PERSONA O UNA COSA. DI SOLITO VA DOPO IL NOME." + es("UNA CASA <b>GRANDE</b>. UN RAGAZZO <b>SIMPATICO</b>."),
  "Maschile, femminile, singolare, plurale": AGGETTIVI,
  "Le nazionalità": tab(("-O / -A", "ITALIANO, ITALIANA", "ITALIANI, ITALIANE"), ("-E", "FRANCESE, CINESE", "FRANCESI, CINESI"), head=("", "SINGOLARE", "PLURALE"))})
applica(P_NOMI, {
  "Maschile o femminile?": tab(("-O", "MASCHILE", "IL LIBRO"), ("-A", "FEMMINILE", "LA CASA"), ("-E", "MASCHILE O FEMMINILE", "IL PADRE, LA CHIAVE")) +
                           "CON I NOMI IN -E GUARDA L'ARTICOLO O IL DIZIONARIO.",
  "Il plurale": tab(("-O → -I", "IL LIBRO → I LIBRI"), ("-A → -E", "LA CASA → LE CASE"), ("-E → -I", "IL PADRE → I PADRI, LA CHIAVE → LE CHIAVI")) +
                "NON CAMBIANO: LE PAROLE CON L'ACCENTO (IL CAFFÈ → I CAFFÈ) E LE PAROLE STRANIERE (IL BAR → I BAR).",
  "Gli articoli": ARTICOLI})
applica(P_PRES, {
  "I verbi regolari: -ARE, -ERE, -IRE": PRESENTE,
  "I verbi in -ISC (finire, capire, pulire, preferire)": tab(("IO", "FINISCO"), ("TU", "FINISCI"), ("LUI / LEI", "FINISCE"), ("NOI", "FINIAMO"), ("VOI", "FINITE"), ("LORO", "FINISCONO")) +
      "-ISC- SOLO CON IO, TU, LUI/LEI, LORO. NOI E VOI SONO NORMALI.",
  "Essere e avere": ESSERE_AVERE,
  "Andare, venire, fare, dare, stare": tab(("IO", "VADO", "VENGO", "FACCIO", "DO", "STO"), ("TU", "VAI", "VIENI", "FAI", "DAI", "STAI"), ("LUI / LEI", "VA", "VIENE", "FA", "DÀ", "STA"),
                                          ("NOI", "ANDIAMO", "VENIAMO", "FACCIAMO", "DIAMO", "STIAMO"), ("VOI", "ANDATE", "VENITE", "FATE", "DATE", "STATE"),
                                          ("LORO", "VANNO", "VENGONO", "FANNO", "DANNO", "STANNO"), head=("", "ANDARE", "VENIRE", "FARE", "DARE", "STARE"))})
applica(P_POSS, {"Il mio, la mia, i miei, le mie": POSSESSIVI})
applica(P_FRASE, {"Soggetto e predicato": "LA FRASE MINIMA = <b>CHI?</b> (SOGGETTO) + <b>CHE COSA FA?</b> (PREDICATO, IL VERBO)." + es("AMIRA (CHI?) LAVORA (CHE COSA FA?).") +
                  "<br>POI POSSIAMO AGGIUNGERE: DOVE? QUANDO? CON CHI?" + es("AMIRA LAVORA IN UN BAR LA MATTINA.")})
applica(P_DOM, {"Le parole per fare domande": tab(("CHI?", "UNA PERSONA", "CHI È?"), ("CHE COSA?", "UNA COSA", "CHE COSA MANGI?"), ("DOVE?", "UN POSTO", "DOVE ABITI?"),
                                                  ("QUANDO?", "UN MOMENTO", "QUANDO ARRIVI?"), ("COME?", "IL MODO", "COME STAI?"), ("PERCHÉ?", "IL MOTIVO", "PERCHÉ STUDI?"),
                                                  ("QUANTO?", "LA QUANTITÀ, IL PREZZO", "QUANTO COSTA?"), ("QUALE?", "UNA SCELTA", "QUALE PREFERISCI?"))})
applica(P_PASS, {"Avere o essere? Il participio": PASSATO})
applica(P_MOD, {"Potere, dovere, volere, sapere": MODALI + "<br>SAPERE: SO, SAI, SA, SAPPIAMO, SAPETE, SANNO. <b>SO</b> NUOTARE = HO IMPARATO. <b>POSSO</b> NUOTARE = È PERMESSO / È POSSIBILE."})
applica(P_RIFL, {"Mi, ti, si, ci, vi, si": RIFLESSIVI,
                 "Presente e passato": "AL PASSATO PROSSIMO I RIFLESSIVI USANO SEMPRE <b>ESSERE</b>." + es("MI SONO ALZATO / ALZATA. CI SIAMO VESTITI.")})
applica(P_PREP, {"Le preposizioni semplici": "DI · A · DA · IN · CON · SU · PER · TRA / FRA" + PREP,
                 "Le preposizioni articolate": tab(("A", "AL", "ALLO", "ALLA", "ALL'", "AI", "AGLI", "ALLE"), ("DA", "DAL", "DALLO", "DALLA", "DALL'", "DAI", "DAGLI", "DALLE"),
                                                               ("IN", "NEL", "NELLO", "NELLA", "NELL'", "NEI", "NEGLI", "NELLE"), ("SU", "SUL", "SULLO", "SULLA", "SULL'", "SUI", "SUGLI", "SULLE"),
                                                               ("DI", "DEL", "DELLO", "DELLA", "DELL'", "DEI", "DEGLI", "DELLE"), head=("", "IL", "LO", "LA", "L'", "I", "GLI", "LE")) +
                                               "PREPOSIZIONE + ARTICOLO = UNA PAROLA SOLA: IN + IL = NEL."})
applica(P_PRON, {"I pronomi diretti: lo, la, li, le": PRONOMI_DIR,
                 "I pronomi indiretti: mi, ti, gli, le, ci, vi": "RISPONDONO ALLA DOMANDA <b>A CHI?</b>" +
                     tab(("A ME", "MI"), ("A TE", "TI"), ("A LUI", "GLI"), ("A LEI", "LE"), ("A NOI", "CI"), ("A VOI", "VI"), ("A LORO", "GLI")) + es("TELEFONO A MARIA → LE TELEFONO.")})
applica(SUONI, {"C o CH?": tab(("CA · CO · CU · CHE · CHI", "DURO", "CASA, CHIAVE"), ("CE · CI", "DOLCE", "CENA, CIAO")),
                "G o GH?": tab(("GA · GO · GU · GHE · GHI", "DURO", "GATTO, SPAGHETTI"), ("GE · GI", "DOLCE", "GELATO, GIRO")),
                "GN, GLI, SC": tab(("GN", "BAGNO, LAVAGNA"), ("GLI", "FIGLIO, MOGLIE"), ("SCE · SCI", "PESCE, SCIARPA"), ("SCA · SCO · SCU · SCHE · SCHI", "SCARPA, SCUOLA, SCHIENA"))})
applica(QUESTO, {"Questo": "<b>QUESTO</b> = VICINO A ME." + tab(("QUESTO", "QUESTA", "QUESTI", "QUESTE"), head=("M. SING.", "F. SING.", "M. PLUR.", "F. PLUR.")),
                 "Quello": "<b>QUELLO</b> = LONTANO. CAMBIA COME L'ARTICOLO:" + tab(("IL → QUEL", "LO → QUELLO", "L' → QUELL'", "LA → QUELLA"), ("I → QUEI", "GLI → QUEGLI", "", "LE → QUELLE"))})
applica(CE, {"C'è o ci sono?": tab(("C'È", "+ UNA COSA", "C'È UN BAR."), ("CI SONO", "+ TANTE COSE", "CI SONO DUE FARMACIE."))})
applica(PIACE, {"Piace o piacciono?": PIACERE, "Anche a me": tab(("MI PIACE.", "ANCHE A ME. 😀", "A ME NO. 😐"), ("NON MI PIACE.", "NEANCHE A ME. 😐", "A ME SÌ. 😀"))})
applica(TEMPO, {"Quante volte?": "SEMPRE · SPESSO · QUALCHE VOLTA · RARAMENTE · MAI. CON MAI: <b>NON</b> + VERBO + <b>MAI</b>." + es("VADO SPESSO AL PARCO. NON VADO MAI IN DISCOTECA."),
                "Mi piace": PIACERE})
applica(VAC, {"Il passato prossimo": PASSATO})
applica(CHE_LAVORO, {"La grammatica": "IL FEMMINILE DEI LAVORI: -O → -A (CUOCO → CUOCA) · -IERE → -IERA (INFERMIERE → INFERMIERA) · -TORE → -TRICE (ATTORE → ATTRICE)." +
                     "<br>FARE + IL LAVORO: FACCIO IL MURATORE. LAVORARE: LAVORO, LAVORI, LAVORA, LAVORIAMO, LAVORATE, LAVORANO."})

# B1 (minuscolo)
applica(U1, {"Grammatica": "<b>imperfetto</b> = descrizione, situazione (pioveva, era tardi). <b>passato prossimo</b> = il fatto (è arrivato un messaggio).<br>"
             "<b>trapassato prossimo</b> = un'azione prima di un'altra nel passato: avevo / ero + participio." + es("Quando sono arrivato, il treno era già partito.") +
             "<br><b>stare per</b> + infinito = sta per succedere. <b>stare</b> + gerundio = succede adesso."})
applica(U2, {"Grammatica": "<b>condizionale presente</b>: parlerei, prenderei, partirei · vorrei, potrei, dovrei, andrei, sarei, avrei. Serve per desideri, consigli, richieste gentili." +
             "<br><b>futuro</b> = un fatto sicuro nel futuro; <b>condizionale</b> = un desiderio o una possibilità.<br><b>ne</b> = di questo / una quantità di questo." + es("Quanti giorni stai? Ne sto cinque.")})
applica(U3, {"Grammatica": "<b>congiuntivo</b> dopo verbi di opinione, speranza, dubbio: penso che, credo che, spero che, mi sembra che." +
             tab(("io / tu / lui", "sia", "abbia"), ("noi", "siamo", "abbiamo"), ("voi", "siate", "abbiate"), ("loro", "siano", "abbiano"), head=("", "essere", "avere")) +
             "Certezza → indicativo (so che è vero). Opinione → congiuntivo (penso che sia vero).<br><b>pronomi combinati</b>: me lo, te lo, glielo, ce lo, ve lo, glielo." + es("Ti presto il libro → te lo presto.")})
applica(U4, {"Grammatica": tab(("-are", "parli", "parliamo", "parliate", "parlino"), ("-ere", "prenda", "prendiamo", "prendiate", "prendano"), ("-ire", "parta", "partiamo", "partiate", "partano"),
                               head=("", "io / tu / lui", "noi", "voi", "loro")) +
             "<b>che</b> = soggetto o oggetto (la persona che lavora). <b>cui</b> = dopo una preposizione (la ditta in cui lavoro, la persona a cui scrivo)."})
applica(U5, {"Grammatica": "congiuntivo irregolare: vada, faccia, venga, possa, debba, voglia, sappia, dia, stia, esca." +
             "<br><b>qualche</b> + singolare (qualche giorno) · <b>ogni</b> + singolare (ogni mese) · <b>nessuno</b> + non (non c'è nessuno)." +
             "<br><b>forma passiva</b>: essere + participio (+ da)." + es("Il palazzo è stato costruito nel 1960.")})
