from genera import eq, has, all_
from unita_presente import coniuga, verbo, righe

TAB_P, TAB_K = coniuga([("POTERE", ["posso", "puoi", "può", "possiamo", "potete", "possono"]),
    ("DOVERE", ["devo", "devi", "deve", "dobbiamo", "dovete", "devono"]),
    ("VOLERE", ["voglio", "vuoi", "vuole", "vogliamo", "volete", "vogliono"]),
    ("SAPERE", ["so", "sai", "sa", "sappiamo", "sapete", "sanno"])], ["IO", "TU", "LUI/LEI", "NOI", "VOI", "LORO"])

MOD = {"io": "posso|devo|voglio", "tu": "puoi|devi|vuoi", "lei": "può|deve|vuole",
       "noi": "possiamo|dobbiamo|vogliamo", "voi": "potete|dovete|volete", "loro": "possono|devono|vogliono"}
LIBERO = [("(NOI)", "ENTRARE?", "noi"), ("(VOI)", "ANDARE A LAVORARE!", "voi"), ("(TU)", "VENIRE CON NOI?", "tu"),
          ("(IO) NON", "DORMIRE.", "io"), ("(LEI)", "TELEFONARMI DOMANI?", "lei"), ("(NOI)", "PAGARE LE BOLLETTE.", "noi"),
          ("(TU)", "STUDIARE LA LINGUA ITALIANA.", "tu"), ("(LORO)", "ANDARE IN FERIE AD AGOSTO!", "loro"),
          ("(VOI)", "VENIRE A BARI CON NOI?", "voi")]
LIB_I = [{"pre": f"{i}. {a}", "post": b} for i, (a, b, _) in enumerate(LIBERO, 1)]
LIB_K = [eq(*MOD[p].split("|")) for *_, p in LIBERO]

SCOPO = [("POSSO ENTRARE?", "PERMESSO"), ("DEVO PRENDERE LE MEDICINE!", "OBBLIGO"),
         ("POSSO AVERE DUE CAFFÈ, PER FAVORE?", "GENTILEZZA"), ("VOGLIO COMPRARE LA FRUTTA!", "DESIDERIO"),
         ("POSSO APRIRE LA FINESTRA?", "PERMESSO"), ("DEVO LAVARE I PANTALONI!", "OBBLIGO"),
         ("VOGLIO ANDARE A SCUOLA!", "DESIDERIO"), ("POSSO ANDARE AL BAGNO?", "PERMESSO"),
         ("DEVO LAVORARE FINO A TARDI!", "OBBLIGO"), ("VOGLIO ANDARE A VENEZIA!", "DESIDERIO"),
         ("DEVO ANDARE A VENEZIA!", "OBBLIGO"), ("DEVO MANGIARE POCO!", "OBBLIGO"),
         ("VOGLIO TROVARE UN LAVORO!", "DESIDERIO"), ("POSSO SEDERMI?", "PERMESSO|GENTILEZZA"),
         ("VOGLIO FARE LA PATENTE!", "DESIDERIO"), ("DEVO ANDARE A CASA!", "OBBLIGO"),
         ("PUÒ RIPETERE, PER FAVORE?", "GENTILEZZA"), ("VORREI UN BICCHIERE D'ACQUA.", "GENTILEZZA")]

SA_PO = righe([("IO … PARLARE INGLESE E FRANCESE.", ["SO", "POSSO"], "SO"),
               ("SCUSI, … ENTRARE?", ["SO", "POSSO"], "POSSO"),
               ("TU … GUIDARE LA MACCHINA?", ["SAI", "PUOI"], "SAI"),
               ("OGGI NON … VENIRE: SONO MALATO.", ["SO", "POSSO"], "POSSO"),
               ("LEI … CUCINARE MOLTO BENE.", ["SA", "PUÒ"], "SA"),
               ("NOI NON … USCIRE: PIOVE TROPPO.", ["SAPPIAMO", "POSSIAMO"], "POSSIAMO"),
               ("I BAMBINI … LEGGERE E SCRIVERE.", ["SANNO", "POSSONO"], "SANNO"),
               ("VOI … NUOTARE?", ["SAPETE", "POTETE"], "SAPETE")])

VUOI = verbo([("(VOLERE) IO", "UN CAFFÈ", "voglio"), ("(DOVERE) TU", "STUDIARE DI PIÙ", "devi"),
              ("(POTERE) LUI NON", "VENIRE STASERA", "può"), ("(SAPERE) NOI", "CUCINARE LA PIZZA", "sappiamo"),
              ("(VOLERE) VOI", "VENIRE AL CINEMA?", "volete"), ("(DOVERE) LORO", "LAVORARE DOMANI", "devono"),
              ("(POTERE) IO", "APRIRE LA FINESTRA?", "posso"), ("(SAPERE) TU", "DOV'È LA STAZIONE?", "sai"),
              ("(VOLERE) LEI", "IMPARARE L'ITALIANO", "vuole"), ("(DOVERE) NOI", "PAGARE L'AFFITTO", "dobbiamo")])

MODALI = {
 "title": "🔑 I verbi modali · Esercizi",
 "store": "modali",
 "upper": True,
 "sections": [
  {"part": "Potere, dovere, volere, sapere"},
  {"id": "e1", "title": "1 · Coniuga i verbi", "short": "1 · Coniuga", "type": "cloze",
   "cons": "Scrivi il verbo per ogni persona.", "parts": TAB_P, "k": TAB_K},
  {"id": "e2", "title": "2 · Scrivi il verbo giusto", "short": "2 · Il verbo giusto", "type": "text", "w": "s",
   "cons": "Scrivi il verbo tra parentesi al presente.", "items": VUOI[0], "k": VUOI[1]},
  {"id": "e3", "title": "3 · POTERE, DOVERE o VOLERE?", "short": "3 · Potere, dovere o volere", "type": "text", "w": "s",
   "cons": "Scegli tu il verbo: POTERE, DOVERE o VOLERE. Attenzione alla persona!", "items": LIB_I, "k": LIB_K},
  {"part": "Che cosa vuol dire?"},
  {"id": "e4", "title": "4 · Obbligo, desiderio, permesso o gentilezza?", "short": "4 · Che cosa vuol dire?", "type": "choice",
   "opts": ["OBBLIGO", "DESIDERIO", "PERMESSO", "GENTILEZZA"], "full": True,
   "cons": "DEVO = OBBLIGO · VOGLIO = DESIDERIO · POSSO …? = PERMESSO · PUÒ…? VORREI… = GENTILEZZA",
   "items": [{"q": f"{i}. {f}"} for i, (f, _) in enumerate(SCOPO, 1)], "k": [eq(*a.split("|")) for _, a in SCOPO]},
  {"id": "e5", "title": "5 · SAPERE o POTERE?", "short": "5 · Sapere o potere", "type": "choice",
   "cons": "SAPERE = sono capace (SO NUOTARE). POTERE = ho il permesso, è possibile (POSSO ENTRARE?).",
   "items": SA_PO[0], "k": SA_PO[1]},
  {"id": "e6", "title": "6 ✎ · E tu?", "type": "free", "rows": 2,
   "items": ["Che cosa VUOI fare quest'anno?", "Che cosa DEVI fare domani?", "Che cosa SAI fare bene?"]},
 ]
}
