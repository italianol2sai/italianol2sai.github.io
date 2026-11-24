"""Percorso B1, modulo 3 («La scuola») sulla traccia di «Nuovo Senza frontiere 3» (Edilingua): unità 9-12.
Testi, dialoghi, nomi e ascolti NUOVI. Stile "b1".
Uso: python3 _strumenti/unita_sf_b1c.py   (dalla cartella principale del sito)"""
import os, sys
sys.path.insert(0, os.path.dirname(__file__))
from genera import build as build_es
from unita_primi import cover, slide, cards, table, nota, dialogo, end
from unita_drive import vf, scegli, menu, ordina, parla, libero
from teoria import tab, es
from unita_sf import scrivi, ascolto, testo, build_slide, build_giochi

# =====================================================================
# B1 · UNITÀ 9 · STUDIANDO SI IMPARA
# =====================================================================
CLA = [("F", "Buonasera a tutti. Prima di cominciare, vorrei sapere: secondo voi, perché è importante studiare l'italiano?"),
       ("M", "Credo che sia importante per trovare un lavoro migliore. Senza la lingua è tutto più difficile."),
       ("F", "Giusto. E tu, Eneida, che ne pensi?"),
       ("F", "Penso che la lingua serva soprattutto per aiutare i miei figli con la scuola. Ho paura che loro parlino meglio di me!"),
       ("M", "Io invece spero che il corso mi aiuti a prendere la patente."),
       ("F", "Bene. Allora è necessario che ognuno abbia un obiettivo chiaro. Scrivete il vostro sul quaderno.")]
STU_SLIDE = [
    cover("📚", "Studiando si impara", "In classe · I compiti per casa · L'analfabetismo in Italia", "B1 &bull; Modulo 3 &bull; Unità 1"),
    slide("In questa unità impari a…", cards([
        ("💬", "Dare la tua opinione", "Credo che… Penso che…"), ("🙏", "Esprimere speranza e paura", "Spero che… Ho paura che…"),
        ("🎬", "Raccontare la trama di un film", "La storia parla di…"), ("🎯", "Parlare dei tuoi obiettivi", "Il mio obiettivo è…")])),
    slide("🏫 Le parole della scuola", cards([
        ("📓", "il quaderno", "dove scrivi gli esercizi"), ("📝", "i compiti", "esercizi da fare a casa"), ("🎓", "il diploma", "il titolo di studio finale"),
        ("📋", "l'iscrizione", "il modulo per entrare a scuola"), ("🧑‍🏫", "il CPIA", "il centro pubblico per l'istruzione degli adulti"), ("🏅", "il voto", "il giudizio numerico")], "g3")),
    slide("🗣️ Lezione A · In classe", dialogo([("*Insegnante Silvia" if i in (0, 2, 5) else ("*Eneida" if i == 3 else ("Kwame" if i == 1 else "Rashid")), t)
                                              for i, (_, t) in enumerate(CLA)])),
    slide("📘 Il congiuntivo presente: verbi regolari", table([
        ["che io / tu / lui", "parl<b>i</b>", "prend<b>a</b>", "dorm<b>a</b> / fin<b>isca</b>"],
        ["che noi", "parl<b>iamo</b>", "prend<b>iamo</b>", "dorm<b>iamo</b> / fin<b>iamo</b>"],
        ["che voi", "parl<b>iate</b>", "prend<b>iate</b>", "dorm<b>iate</b> / fin<b>iate</b>"],
        ["che loro", "parl<b>ino</b>", "prend<b>ano</b>", "dorm<b>ano</b> / fin<b>iscano</b>"]], head=["", "-are", "-ere", "-ire"]) + "\n" +
        nota("Si usa dopo <b>penso che, credo che, spero che, ho paura che, è importante che</b>: verbi di opinione, speranza, paura.")),
    slide("📘 Essere e avere al congiuntivo", table([
        ["che io / tu / lui", "sia", "abbia"], ["che noi", "siamo", "abbiamo"], ["che voi", "siate", "abbiate"], ["che loro", "siano", "abbiano"]],
        head=["", "essere", "avere"]) + "\n" + nota("Credo che <b>sia</b> importante. · È necessario che ognuno <b>abbia</b> un obiettivo.")),
    slide("🎬 Lezione B · I compiti per casa", testo(
        "Per casa la maestra Silvia chiede di guardare un film italiano e raccontarne la trama. Kwame sceglie una storia vera:",
        "<i>«Il film parla di un ragazzo che arriva in Sicilia dal Mali. Non sa leggere, ma vuole a tutti i costi che sua madre possa ricevere le sue lettere. "
        "Un vecchio pescatore gli insegna l'alfabeto sulla spiaggia. Alla fine il ragazzo scrive la prima lettera da solo. Penso che sia un film bellissimo, "
        "anche se il finale mi sembra un po' triste.»</i>")),
    slide("📘 Congiuntivo irregolare e modali", table([
        ["andare", "vada"], ["fare", "faccia"], ["venire", "venga"], ["dire", "dica"], ["stare", "stia"], ["dare", "dia"],
        ["potere", "possa"], ["volere", "voglia"], ["dovere", "debba"], ["sapere", "sappia"]], head=["verbo", "che io / tu / lui"]) + "\n" +
        nota("Plurale: vad<b>ano</b>, facci<b>ano</b>, possi<b>amo</b>… · Voglio che tu <b>venga</b> a lezione!")),
    slide("📖 Educazione civica · L'analfabetismo in Italia", cards([
        ("📜", "nel 1951", "quasi 1 italiano su 7 non sapeva leggere e scrivere"), ("🏫", "l'UNLA", "Unione Nazionale per la Lotta contro l'Analfabetismo, nata nel 1947"),
        ("📺", "«Non è mai troppo tardi»", "il maestro Alberto Manzi insegnava in TV (1960-68)"), ("🧑‍🏫", "i CPIA oggi", "corsi gratuiti per adulti italiani e stranieri"),
        ("🔤", "analfabetismo funzionale", "saper leggere, ma non capire un testo"), ("💪", "mai troppo tardi", "si può imparare a ogni età")], "g3")),
    end("Ora sai dare la tua opinione con il congiuntivo!"),
]
B1STU = {
 "title": "📚 Studiando si impara · Esercizi", "store": "b1-studiando", "livello": "b1",
 "sections": [
  {"part": "Lezione A · In classe"},
  ascolto(scegli([("1. Per Kwame l'italiano serve per…", ["trovare un lavoro migliore", "fare amicizia", "viaggiare"], "trovare un lavoro migliore"),
                  ("2. Eneida vuole aiutare…", ["il marito", "i figli con la scuola", "i colleghi"], "i figli con la scuola"),
                  ("3. Eneida ha paura che i figli…", ["parlino meglio di lei", "non studino", "cambino scuola"], "parlino meglio di lei"),
                  ("4. Rashid spera di…", ["prendere la patente", "fare l'università", "cambiare casa"], "prendere la patente")],
                 "1 · 🎧 Ascolta la lezione", "1 · In classe", "e1"), [list(x) for x in CLA]),
  {"part": "Il congiuntivo presente regolare", "teoria":
     tab(("-are", "che lui parli, che loro parlino"), ("-ere", "che lui prenda, che loro prendano"), ("-ire", "che lui dorma / finisca"), head=("verbi", "congiuntivo")) +
     "Dopo penso che, credo che, spero che, ho paura che, è importante che." + es("Spero che tu <b>capisca</b>. · Credo che loro <b>studino</b> molto.")},
  scrivi([("1. Spero che il corso (cominciare) … presto.", ("cominci",)), ("2. Credo che Rashid (studiare) … molto.", ("studi",)),
          ("3. Penso che i ragazzi (leggere) … poco.", ("leggano",)), ("4. È importante che voi (scrivere) … ogni giorno.", ("scriviate",)),
          ("5. Ho paura che lei non (capire) … la lezione.", ("capisca",)), ("6. Spero che noi (finire) … in tempo.", ("finiamo",))],
         "2 · Completa con il congiuntivo", "2 · Congiuntivo regolare", "e2", w="s"),
  menu(["sia", "siano", "abbia", "abbiano", "siate"],
       [("1. Penso che l'italiano … una lingua difficile.", "sia"), ("2. Credo che i miei figli … molti compiti.", "abbiano"),
        ("3. Spero che voi … contenti del corso.", "siate"), ("4. È necessario che ognuno … un quaderno.", "abbia"), ("5. Ho paura che le lezioni … troppo lunghe.", "siano")],
       "3 · Essere o avere?", "3 · Essere e avere", "e3"),
  {"part": "Lezione B · Il film"},
  vf(["1. Il ragazzo del film arriva in Sicilia.", "2. Il ragazzo sa già leggere bene.", "3. Un pescatore gli insegna l'alfabeto.", "4. Alla fine scrive una lettera da solo.",
      "5. Kwame pensa che il film sia brutto."], ["VERO", "FALSO", "VERO", "VERO", "FALSO"], "4 · La trama del film: vero o falso?", "4 · Il film", "e4",
     info="Il film parla di un ragazzo che arriva in Sicilia dal Mali. Non sa leggere, ma vuole a tutti i costi che sua madre possa ricevere le sue lettere. "
          "Un vecchio pescatore gli insegna l'alfabeto sulla spiaggia. Alla fine il ragazzo scrive la prima lettera da solo. Penso che sia un film bellissimo, anche se il finale mi sembra un po' triste."),
  {"part": "Congiuntivo irregolare e modali", "teoria":
     tab(("andare / fare / venire", "vada / faccia / venga"), ("dire / stare / dare", "dica / stia / dia"), ("potere / volere / dovere / sapere", "possa / voglia / debba / sappia"), head=("verbo", "che lui")) +
     es("Voglio che tu <b>venga</b>. · Spero che <b>possano</b> venire.")},
  scrivi([("1. La maestra vuole che noi (fare) … i compiti.", ("facciamo",)), ("2. Spero che tu (potere) … venire domani.", ("possa",)),
          ("3. Penso che Kwame (andare) … a scuola la sera.", ("vada",)), ("4. È importante che i bambini (stare) … attenti.", ("stiano",)),
          ("5. Credo che lei (sapere) … già la risposta.", ("sappia",)), ("6. Bisogna che voi (venire) … puntuali.", ("veniate",))],
         "5 · Completa con il congiuntivo irregolare", "5 · Irregolari", "e5", w="s"),
  {"part": "Educazione civica · L'analfabetismo"},
  vf(["1. Nel 1951 molti italiani non sapevano leggere.", "2. L'UNLA è nata nel 1947.", "3. Alberto Manzi insegnava alla radio.",
      "4. I CPIA offrono corsi gratuiti per adulti.", "5. L'analfabetismo funzionale è non capire bene un testo."], ["VERO", "VERO", "FALSO", "VERO", "VERO"],
     "6 · L'analfabetismo: vero o falso?", "6 · Analfabetismo", "e6"),
  libero("e7", 7, "La trama di un film", "Racconta la trama di un film che ti è piaciuto e di' che cosa ne pensi (Penso che… Credo che…).", ["Il mio film"], rows=7),
  parla("e8", 8, "Perché studi l'italiano? Che cosa speri che cambi nella tua vita quando lo parlerai bene?"),
 ]
}

# =====================================================================
# B1 · UNITÀ 10 · SCUOLA E FAMIGLIA
# =====================================================================
COL = [("F", "Buongiorno, signor Mensah. Si accomodi. Sono la professoressa Ruggiero, insegno italiano a Kofi."),
       ("M", "Buongiorno. Come va mio figlio? Sono un po' preoccupato."),
       ("F", "Kofi è un ragazzo intelligente e gentile. Però, benché sia bravo, a volte non fa i compiti."),
       ("M", "Lo so. Il pomeriggio lavora con me al mercato, prima che io torni a casa."),
       ("F", "Capisco. Ma affinché possa recuperare, è meglio che studi almeno un'ora al giorno. C'è anche il doposcuola gratuito il martedì."),
       ("M", "Va bene, a patto che finisca entro le sei. Grazie, professoressa, ne parlerò con lui.")]
FAM_SLIDE = [
    cover("👨‍👩‍👦", "Scuola e famiglia", "Il colloquio con gli insegnanti · La pagella · Ritornare studenti", "B1 &bull; Modulo 3 &bull; Unità 2"),
    slide("In questa unità impari a…", cards([
        ("🧑‍🏫", "Parlare con gli insegnanti", "Come va mio figlio?"), ("📄", "Leggere la pagella", "voti e giudizi"),
        ("⚖️", "Esprimere condizioni e scopi", "affinché, purché, a patto che"), ("🎯", "Parlare delle competenze", "saper fare, saper essere")])),
    slide("🏫 La scuola in Italia", table([
        ["0-6 anni", "nido e scuola dell'infanzia", "non obbligatoria"], ["6-11 anni", "scuola primaria (elementare)", "5 anni"],
        ["11-14 anni", "scuola secondaria di primo grado (media)", "3 anni, esame finale"], ["14-19 anni", "scuola secondaria di secondo grado (superiore)", "5 anni, maturità"]],
        head=["età", "scuola", ""]) + "\n" + nota("La scuola è <b>obbligatoria dai 6 ai 16 anni</b>.")),
    slide("🗣️ Lezione A · Il colloquio genitori-insegnanti", dialogo([("*Prof.ssa Ruggiero" if v == "F" else "Sig. Mensah", t) for v, t in COL])),
    slide("📘 Congiunzioni con il congiuntivo", table([
        ["benché / sebbene", "concessione", "<b>Benché</b> sia bravo, non fa i compiti."], ["affinché / perché", "scopo", "<b>Affinché</b> possa recuperare…"],
        ["purché / a patto che", "condizione", "Va bene, <b>a patto che</b> finisca entro le sei."], ["prima che", "tempo", "<b>Prima che</b> io torni a casa."],
        ["senza che", "modo", "Esce <b>senza che</b> io lo sappia."]], head=["congiunzione", "significato", "esempio"])),
    slide("📄 Lezione B · La pagella e le competenze", testo(
        "Nella pagella della scuola primaria non ci sono più i numeri: ci sono i <b>giudizi</b> (avanzato, intermedio, base, in via di prima acquisizione). "
        "Alle medie e alle superiori si usano i <b>voti da 1 a 10</b>: il 6 è la sufficienza.",
        "Oltre ai voti, la scuola valuta le <b>competenze</b>: saper comunicare, lavorare in gruppo, usare il computer, imparare a imparare.")),
    slide("📘 Espressioni impersonali + congiuntivo", table([
        ["è importante che", "È importante che i genitori <b>partecipino</b> ai colloqui."], ["è necessario che / bisogna che", "Bisogna che Kofi <b>studi</b> di più."],
        ["è meglio che", "È meglio che tu <b>parli</b> con l'insegnante."], ["è possibile che / può darsi che", "Può darsi che <b>abbia</b> l'insufficienza."],
        ["è un peccato che", "È un peccato che non <b>venga</b> al doposcuola."]], head=["espressione", "esempio"])),
    slide("🎒 Educazione civica · Ritornare studenti", cards([
        ("🏫", "il CPIA", "terza media e italiano per adulti, gratis"), ("🌙", "i corsi serali", "diploma superiore per chi lavora"),
        ("📜", "il riconoscimento dei titoli", "far valere il diploma preso all'estero"), ("🧾", "la dichiarazione di valore", "si chiede al consolato italiano"),
        ("💼", "la formazione professionale", "corsi per un mestiere, spesso gratuiti"), ("🎓", "l'università", "anche da adulti, con borse di studio")], "g3")),
    end("Ora sai parlare con la scuola dei tuoi figli!"),
]
B1FAM = {
 "title": "👨‍👩‍👦 Scuola e famiglia · Esercizi", "store": "b1-scuola-famiglia", "livello": "b1",
 "sections": [
  {"part": "La scuola in Italia"},
  menu(["la scuola dell'infanzia", "la scuola primaria", "la scuola secondaria di primo grado", "la scuola secondaria di secondo grado"],
       [("1. Amira ha 8 anni: va al…", "la scuola primaria"), ("2. Kofi ha 13 anni: va alla…", "la scuola secondaria di primo grado"),
        ("3. Lina ha 4 anni: va alla…", "la scuola dell'infanzia"), ("4. Samir ha 17 anni: va alla…", "la scuola secondaria di secondo grado")],
       "1 · Che scuola frequentano?", "1 · La scuola", "e1"),
  {"part": "Lezione A · Il colloquio"},
  ascolto(vf(["1. La professoressa insegna matematica.", "2. Kofi è un ragazzo intelligente.", "3. Kofi fa sempre i compiti.", "4. Il pomeriggio Kofi lavora al mercato.",
              "5. Il doposcuola costa 20 euro.", "6. Il padre parlerà con Kofi."], ["FALSO", "VERO", "FALSO", "VERO", "FALSO", "VERO"],
             "2 · 🎧 Ascolta il colloquio: vero o falso?", "2 · Il colloquio", "e2"), [list(x) for x in COL]),
  {"part": "Congiunzioni con il congiuntivo", "teoria":
     tab(("benché / sebbene", "anche se"), ("affinché", "per (scopo)"), ("purché / a patto che", "solo se"), ("prima che", "prima di"), head=("congiunzione", "significato")) +
     es("<b>Benché</b> sia stanco, studia. · Ti aiuto <b>purché</b> tu <b>faccia</b> i compiti.")},
  menu(["benché", "affinché", "purché", "prima che", "senza che"],
       [("1. … sia stanca, Eneida va al corso serale.", "benché"), ("2. Parlo piano … tutti capiscano.", "affinché"),
        ("3. Puoi uscire, … torni per cena.", "purché"), ("4. Prepara lo zaino … arrivi lo scuolabus.", "prima che"),
        ("5. Il bambino è uscito … la maestra se ne accorgesse.", "senza che")],
       "3 · Scegli la congiunzione", "3 · Congiunzioni", "e3"),
  scrivi([("1. Benché (piovere) …, andiamo a scuola a piedi.", ("piova",)), ("2. Te lo spiego affinché tu (capire) ….", ("capisca",)),
          ("3. Va bene, purché voi (essere) … puntuali.", ("siate",)), ("4. Prima che i bambini (tornare) …, preparo la merenda.", ("tornino",))],
         "4 · Completa con il congiuntivo", "4 · Completa", "e4", w="s"),
  {"part": "Lezione B · La pagella"},
  vf(["1. Alla primaria ci sono i voti numerici.", "2. Alle medie i voti vanno da 1 a 10.", "3. Il 5 è la sufficienza.", "4. La scuola valuta anche il lavoro di gruppo."],
     ["FALSO", "VERO", "FALSO", "VERO"], "5 · La pagella: vero o falso?", "5 · La pagella", "e5",
     info="Nella pagella della scuola primaria non ci sono più i numeri: ci sono i giudizi. Alle medie e alle superiori si usano i voti da 1 a 10: il 6 è la sufficienza. "
          "Oltre ai voti, la scuola valuta le competenze: saper comunicare, lavorare in gruppo, usare il computer, imparare a imparare."),
  {"part": "Espressioni impersonali", "teoria":
     tab(("è importante / necessario che", "+ congiuntivo"), ("bisogna che", "+ congiuntivo"), ("è meglio / possibile che", "+ congiuntivo"), head=("espressione", "")) +
     es("Bisogna che Kofi <b>studi</b> di più.")},
  scrivi([("1. È importante che i genitori (andare) … ai colloqui.", ("vadano",)), ("2. Bisogna che tu (firmare) … la giustificazione.", ("firmi",)),
          ("3. È meglio che noi (parlare) … con la maestra.", ("parliamo",)), ("4. Può darsi che oggi la scuola (chiudere) … prima.", ("chiuda",)),
          ("5. È un peccato che Kofi non (venire) … al doposcuola.", ("venga",))],
         "6 · Completa le frasi", "6 · Impersonali", "e6", w="s"),
  {"part": "Educazione civica · Ritornare studenti"},
  menu(["il CPIA", "i corsi serali", "la dichiarazione di valore", "la formazione professionale"],
       [("1. Grace vuole la licenza media italiana: va al…", "il CPIA"), ("2. Ivan lavora di giorno e vuole il diploma: frequenta…", "i corsi serali"),
        ("3. Per far valere il diploma preso in Perù serve…", "la dichiarazione di valore"), ("4. Omar vuole diventare idraulico: sceglie…", "la formazione professionale")],
       "7 · Che cosa scelgono?", "7 · Tornare a studiare", "e7"),
  libero("e8", 8, "Un'email all'insegnante", "Scrivi un'email all'insegnante di tuo figlio per chiedere un colloquio. Usa almeno una congiunzione con il congiuntivo (affinché, benché…).", ["La mia email"], rows=7),
  parla("e9", 9, "Com'è la scuola nel tuo Paese? Che cosa è diverso dall'Italia? Vorresti tornare a studiare?"),
 ]
}

# =====================================================================
# B1 · UNITÀ 11 · LA SCUOLA SUPERIORE
# =====================================================================
SUP = [("F", "Mamma, ho deciso: voglio fare l'istituto tecnico per il turismo."),
       ("F", "Sei sicura? Mi chiedo se non sia meglio il liceo. Tuo fratello dice che il liceo apre più porte."),
       ("F", "Lo so, ma vorrei lavorare presto. Al tecnico studiano tre lingue e fanno stage negli alberghi."),
       ("F", "Va bene. Ma sai come funziona l'iscrizione? Non so se si faccia ancora in segreteria."),
       ("F", "No, si fa online, sulla piattaforma del Ministero. Serve il codice meccanografico della scuola."),
       ("F", "E dove si trova questo codice?"),
       ("F", "Sul sito della scuola, o su «Scuola in chiaro». Ti faccio vedere stasera!")]
SUP_SLIDE = [
    cover("🎒", "La scuola superiore", "Il piano di studi · L'iscrizione online · La scelta", "B1 &bull; Modulo 3 &bull; Unità 3"),
    slide("In questa unità impari a…", cards([
        ("🤔", "Esprimere dubbi", "Non so se… Mi chiedo se…"), ("❓", "Fare domande indirette", "Mi sa dire dove…?"),
        ("💻", "Iscriversi online", "codice meccanografico, SPID"), ("🧭", "Scegliere una scuola", "liceo, tecnico, professionale")])),
    slide("🧭 I tre tipi di scuola superiore", cards([
        ("🏛️", "il liceo", "classico, scientifico, linguistico, artistico…: prepara all'università"),
        ("⚙️", "l'istituto tecnico", "economico o tecnologico: teoria e laboratori, lavoro o università"),
        ("🔧", "l'istituto professionale", "per un mestiere: tanta pratica, stage in azienda")], "g3")),
    slide("🗣️ Lezione A · Il piano di studi", dialogo([("*Salma" if i % 2 == 0 else "Mamma Nadia", t) for i, (_, t) in enumerate(SUP)])),
    slide("📘 Le domande indirette (1)", table([
        ["Dove si trova il codice?", "Mi sa dire <b>dove si trova</b> il codice?"], ["Si fa in segreteria?", "Non so <b>se si faccia</b> in segreteria."],
        ["Quando apre la scuola?", "Le chiedo <b>quando apre</b> la scuola."]], head=["domanda diretta", "domanda indiretta"]) + "\n" +
        nota("Dopo <b>non so, mi chiedo, vorrei sapere, mi sa dire</b> si usa la domanda indiretta. Per le domande sì/no si usa <b>se</b>.")),
    slide("💻 Lezione B · La nuova scuola!", testo(
        "Come si fa l'<b>iscrizione online</b> alla prima superiore:",
        "1. Entri sulla piattaforma «Unica» del Ministero con <b>SPID</b> o CIE. 2. Cerchi la scuola e copi il <b>codice meccanografico</b> (per esempio BATD01000X). "
        "3. Compili la domanda: dati dello studente, indirizzo di studio, lingua straniera. 4. Puoi indicare fino a <b>tre scuole</b> in ordine di preferenza. "
        "5. Invii la domanda entro la scadenza (di solito a gennaio) e ricevi una <b>email di conferma</b>.")),
    slide("📘 Le domande indirette (2)", table([
        ["indicativo", "più comune nella lingua parlata", "Non so dove <b>è</b> la segreteria."], ["congiuntivo", "più formale, scritto", "Non so dove <b>sia</b> la segreteria."],
        ["infinito", "quando il soggetto è lo stesso", "Non so <b>che cosa scegliere</b>."]], head=["modo", "quando", "esempio"])),
    slide("🧭 Educazione civica · La scelta della scuola superiore", cards([
        ("📅", "quando", "si sceglie in terza media, l'iscrizione è a gennaio"), ("🗣️", "il consiglio orientativo", "la scuola media dà un suggerimento"),
        ("🏫", "gli open day", "giornate per visitare le scuole"), ("🔍", "Scuola in chiaro", "il sito con i dati di tutte le scuole"),
        ("👨‍👩‍👧", "la famiglia", "decide insieme al ragazzo"), ("↩️", "cambiare si può", "le «passerelle» per cambiare indirizzo")], "g3")),
    end("Ora sai scegliere una scuola e fare domande indirette!"),
]
B1SUP = {
 "title": "🎒 La scuola superiore · Esercizi", "store": "b1-scuola-superiore", "livello": "b1",
 "sections": [
  {"part": "I tipi di scuola"},
  menu(["il liceo", "l'istituto tecnico", "l'istituto professionale"],
       [("1. Hamid vuole fare l'università di medicina.", "il liceo"), ("2. Ana vuole diventare parrucchiera e fare tanta pratica.", "l'istituto professionale"),
        ("3. Salma vuole lavorare nel turismo e studiare tre lingue.", "l'istituto tecnico"), ("4. Yuri ama il latino e il greco.", "il liceo")],
       "1 · Che scuola scelgono?", "1 · Le scuole", "e1"),
  {"part": "Lezione A · Il piano di studi"},
  ascolto(vf(["1. Salma vuole fare il liceo.", "2. Al tecnico per il turismo si studiano tre lingue.", "3. L'iscrizione si fa in segreteria.",
              "4. Serve il codice meccanografico.", "5. Il codice si trova sul sito della scuola."], ["FALSO", "VERO", "FALSO", "VERO", "VERO"],
             "2 · 🎧 Ascolta Salma e la mamma: vero o falso?", "2 · La scelta", "e2"), [list(x) for x in SUP]),
  {"part": "Le domande indirette", "teoria":
     tab(("Dove si trova?", "Mi sa dire dove si trova?"), ("Si fa online?", "Non so se si faccia online."), head=("diretta", "indiretta")) +
     "Domande sì/no: <b>se</b>. Le altre: dove, quando, come, che cosa…" + es("Vorrei sapere <b>quando</b> apre la segreteria.")},
  scrivi([("1. «A che ora apre la scuola?» → Mi sa dire a che ora … la scuola?", ("apre",)), ("2. «C'è la mensa?» → Vorrei sapere … c'è la mensa.", ("se",)),
          ("3. «Dove si compra il libro?» → Non so … si compra il libro.", ("dove",)), ("4. «Quanto costa la gita?» → Mi chiedo … costa la gita.", ("quanto",)),
          ("5. «Che cosa devo portare?» → Non so che cosa … portare.", ("devo",))],
         "3 · Trasforma in domanda indiretta", "3 · Domande indirette", "e3", w="s"),
  {"part": "Lezione B · L'iscrizione online"},
  ordina(["Entri sulla piattaforma con SPID o CIE.", "Cerchi la scuola e copi il codice meccanografico.", "Compili la domanda con i dati dello studente.",
          "Indichi fino a tre scuole in ordine di preferenza.", "Invii la domanda e ricevi l'email di conferma."],
         "4 · Metti in ordine i passaggi dell'iscrizione", "4 · L'iscrizione", "e4"),
  scegli([("1. Non so dove … la segreteria. (formale)", ["sia", "siamo", "essere"], "sia"), ("2. Non so che cosa … (stesso soggetto)", ["scegliere", "scelga", "sceglie"], "scegliere"),
          ("3. Mi chiedo se la scuola … il laboratorio. (formale)", ["abbia", "avere", "abbiamo"], "abbia"), ("4. Non so come … i moduli. (stesso soggetto)", ["compilare", "compili", "compilano"], "compilare")],
         "5 · Indicativo, congiuntivo o infinito?", "5 · I modi", "e5"),
  {"part": "Educazione civica · La scelta"},
  vf(["1. La scuola superiore si sceglie in terza media.", "2. L'iscrizione è di solito a gennaio.", "3. Il consiglio orientativo è obbligatorio da seguire.",
      "4. Gli open day servono a visitare le scuole.", "5. Dopo la scelta non si può più cambiare scuola."], ["VERO", "VERO", "FALSO", "VERO", "FALSO"],
     "6 · La scelta della scuola: vero o falso?", "6 · La scelta", "e6"),
  libero("e7", 7, "Domande per l'open day", "Vai all'open day di una scuola. Scrivi 4 domande indirette da fare (Vorrei sapere se… Mi sa dire quando…).", ["Le mie domande"], rows=5),
  parla("e8", 8, "Che scuola consiglieresti a un ragazzo di 14 anni? Perché? Tu che scuola hai fatto?"),
 ]
}

# =====================================================================
# B1 · UNITÀ 12 · LIBRI E VIAGGI
# =====================================================================
BIB = [("M", "Buongiorno, vorrei iscrivermi alla biblioteca. Che cosa devo fare?"),
       ("F", "Buongiorno. Compili questo modulo e mi dia un documento d'identità, per favore."),
       ("M", "Ecco la carta d'identità. Quanti libri posso prendere in prestito?"),
       ("F", "Fino a tre libri per un mese. Se vuole tenerli di più, rinnovi il prestito online."),
       ("M", "Cerco un romanzo facile, per migliorare il mio italiano."),
       ("F", "Guardi lo scaffale «Facile da leggere», in fondo a destra. E prenda anche il programma degli incontri con gli autori!")]
LIB_SLIDE = [
    cover("📖", "Libri e viaggi", "In biblioteca · In partenza · La letteratura della migrazione", "B1 &bull; Modulo 3 &bull; Unità 4"),
    slide("In questa unità impari a…", cards([
        ("📚", "Iscriverti in biblioteca", "prestito, rinnovo, tessera"), ("🧾", "Dare istruzioni formali", "Compili… Mi dia…"),
        ("📕", "Parlare di libri", "romanzo, giallo, poesia"), ("🧳", "Organizzare un viaggio", "prenotare, partire, visitare")])),
    slide("📕 I generi dei libri", cards([
        ("🕵️", "il giallo", "un mistero, un'indagine"), ("💕", "il romanzo rosa", "una storia d'amore"), ("🐉", "il fantasy", "mondi magici"),
        ("📜", "la biografia", "la vita di una persona vera"), ("✒️", "la poesia", "versi e rime"), ("🍳", "il manuale", "libro per imparare a fare qualcosa")], "g3")),
    slide("📚 Lezione A · In biblioteca", dialogo([("Michele" if v == "M" else "*Bibliotecaria", t) for v, t in BIB])),
    slide("📘 L'imperativo formale (Lei): verbi regolari", table([
        ["compilare", "(Lei) compil<b>i</b>!", "Non compili a matita."], ["leggere", "(Lei) legg<b>a</b>!", "Non legga in fretta."],
        ["aprire", "(Lei) apr<b>a</b>!", "Non apra la porta."], ["finire", "(Lei) fin<b>isca</b>!", "Non finisca subito."]], head=["verbo", "imperativo con Lei", "negativo"]) + "\n" +
        nota("L'imperativo con <b>Lei</b> ha le stesse forme del congiuntivo. I pronomi vanno <b>prima</b>: <b>Lo</b> compili! <b>Mi</b> dica!")),
    slide("🧳 Lezione B · In partenza", dialogo([
        ("Cristian", "Buongiorno, vorrei prenotare un viaggio a Matera per il fine settimana."),
        ("*Agente di viaggio", "Certo. Venga, si sieda. Preferisce il treno o il pullman?"),
        ("Cristian", "Il pullman costa meno, vero?"),
        ("*Agente di viaggio", "Sì. Allora faccia così: vada in stazione alle 8, prenda il pullman delle 8:30 e stia attento alla fermata: è «Matera Villa Longo»."),
        ("Cristian", "E per l'albergo?"),
        ("*Agente di viaggio", "Ecco la prenotazione. Abbia con sé un documento e non dimentichi di visitare i Sassi!")])),
    slide("📘 L'imperativo formale irregolare", table([
        ["andare", "vada"], ["venire", "venga"], ["fare", "faccia"], ["dire", "dica"], ["dare", "dia"], ["stare", "stia"], ["essere", "sia"], ["avere", "abbia"],
        ["sedersi", "si sieda"], ["salire", "salga"]], head=["verbo", "(Lei)"]) + "\n" + nota("Mi <b>dica</b>! · <b>Si sieda</b>, prego. · <b>Abbia</b> pazienza!")),
    slide("✒️ Educazione civica · La letteratura italiana della migrazione", cards([
        ("📚", "che cos'è", "libri scritti in italiano da autori arrivati da altri Paesi"), ("🌍", "dagli anni '90", "i primi romanzi di autori senegalesi, marocchini, albanesi"),
        ("🗣️", "temi", "il viaggio, l'identità, la lingua nuova, la famiglia lontana"), ("🏆", "i premi", "concorsi letterari dedicati, come il premio Eks&Tra"),
        ("🧒", "le seconde generazioni", "ragazzi nati in Italia che raccontano la loro doppia identità"), ("✍️", "anche tu", "scrivere nella nuova lingua è una conquista")], "g3")),
    end("Ora sai usare la biblioteca e organizzare un viaggio!"),
]
B1LIB = {
 "title": "📖 Libri e viaggi · Esercizi", "store": "b1-libri-viaggi", "livello": "b1",
 "sections": [
  {"part": "I generi dei libri"},
  menu(["il giallo", "il romanzo rosa", "il fantasy", "la biografia", "la poesia", "il manuale"],
       [("1. «Chi ha ucciso il direttore?»: è …", "il giallo"), ("2. La vita di Nelson Mandela: è …", "la biografia"), ("3. Draghi e maghi: è …", "il fantasy"),
        ("4. Come riparare la bicicletta: è …", "il manuale"), ("5. Due ragazzi si innamorano a Venezia: è …", "il romanzo rosa"), ("6. Versi brevi sul mare: è …", "la poesia")],
       "1 · Che genere è?", "1 · I generi", "e1"),
  {"part": "Lezione A · In biblioteca"},
  ascolto(vf(["1. Per iscriversi serve un documento.", "2. Si possono prendere cinque libri.", "3. Il prestito dura un mese.", "4. Il prestito si rinnova solo di persona.",
              "5. Lo scaffale «Facile da leggere» è in fondo a destra."], ["VERO", "FALSO", "VERO", "FALSO", "VERO"],
             "2 · 🎧 Ascolta in biblioteca: vero o falso?", "2 · In biblioteca", "e2"), [list(x) for x in BIB]),
  {"part": "L'imperativo formale (Lei)", "teoria":
     tab(("-are", "compili!"), ("-ere / -ire", "legga! apra!"), ("-isc-", "finisca!"), head=("verbi", "Lei")) +
     "Uguale al congiuntivo. I pronomi vanno prima." + es("<b>Lo</b> compili, per favore. · Non <b>apra</b> la finestra.")},
  scrivi([("1. (compilare) … il modulo, per favore.", ("compili",)), ("2. (leggere) … le istruzioni.", ("legga",)), ("3. (aspettare) … un momento.", ("aspetti",)),
          ("4. (scrivere) … il Suo nome qui.", ("scriva",)), ("5. (restituire) … il libro entro un mese.", ("restituisca",)), ("6. Non (parlare) … ad alta voce.", ("parli",))],
         "3 · Completa con l'imperativo formale", "3 · Imperativo regolare", "e3", w="s"),
  {"part": "Lezione B · In partenza", "teoria":
     tab(("andare / venire / fare", "vada / venga / faccia"), ("dire / dare / stare", "dica / dia / stia"), ("essere / avere", "sia / abbia"), head=("verbo", "Lei")) +
     es("<b>Venga</b>, <b>si sieda</b>. · <b>Abbia</b> con sé un documento.")},
  scegli([("1. Per la stazione … sempre dritto.", ["vada", "va", "andate"], "vada"), ("2. Prego, … pure!", ["si sieda", "siediti", "si siede"], "si sieda"),
          ("3. … attento alla fermata!", ["Stia", "Sta", "State"], "Stia"), ("4. Mi … il Suo nome, per favore.", ["dica", "dici", "dice"], "dica"),
          ("5. … pazienza, il pullman è in ritardo.", ["Abbia", "Hai", "Ha"], "Abbia")],
         "4 · Scegli l'imperativo formale", "4 · Irregolari", "e4"),
  vf(["1. Cristian va a Matera in treno.", "2. Il pullman parte alle 8:30.", "3. La fermata è «Matera Villa Longo».", "4. L'agente consiglia di visitare i Sassi."],
     ["FALSO", "VERO", "VERO", "VERO"], "5 · Il dialogo in agenzia: vero o falso?", "5 · In agenzia", "e5"),
  {"part": "Educazione civica · La letteratura della migrazione"},
  vf(["1. Sono libri scritti in italiano da autori di altri Paesi.", "2. I primi romanzi sono degli anni '90.", "3. Parlano solo di sport.",
      "4. Anche i ragazzi delle seconde generazioni scrivono libri."], ["VERO", "VERO", "FALSO", "VERO"], "6 · La letteratura della migrazione: vero o falso?", "6 · Letteratura", "e6"),
  libero("e7", 7, "Consigli a un turista", "Un turista ti chiede come arrivare in un posto bello della tua città. Dagli 5 indicazioni con l'imperativo formale (vada, prenda, giri…).", ["Le mie indicazioni"], rows=6),
  parla("e8", 8, "Qual è un libro importante per te? Che viaggio vorresti fare in Italia?"),
 ]
}

SLIDE = [("b1-studiando/index.html", "Studiando si impara", "B1", STU_SLIDE, "b1"),
         ("b1-scuola-famiglia/index.html", "Scuola e famiglia", "B1", FAM_SLIDE, "b1"),
         ("b1-scuola-superiore/index.html", "La scuola superiore", "B1", SUP_SLIDE, "b1"),
         ("b1-libri-viaggi/index.html", "Libri e viaggi", "B1", LIB_SLIDE, "b1")]
ESERCIZI = [("b1-studiando", B1STU), ("b1-scuola-famiglia", B1FAM), ("b1-scuola-superiore", B1SUP), ("b1-libri-viaggi", B1LIB)]
GIOCHI = {
 "b1-studiando": ("b1-cittadini", "B1", "📚 GIOCHI: STUDIANDO SI IMPARA (B1)", [
  ["IL QUADERNO", "📓", "DOVE SCRIVI GLI ESERCIZI"], ["I COMPITI", "📝", "ESERCIZI DA FARE A CASA"], ["IL DIPLOMA", "🎓", "TITOLO DI STUDIO"], ["L'ISCRIZIONE", "📋", "MODULO PER ENTRARE"],
  ["IL CPIA", "🧑‍🏫", "SCUOLA PER ADULTI"], ["IL VOTO", "🏅", "GIUDIZIO NUMERICO"], ["L'ALFABETO", "🔤", "DALLA A ALLA ZETA"], ["LA TRAMA", "🎬", "LA STORIA DEL FILM"],
  ["L'OBIETTIVO", "🎯", "QUELLO CHE VUOI RAGGIUNGERE"], ["LA LAVAGNA", "🖊️", "L'INSEGNANTE CI SCRIVE"], ["L'ANALFABETISMO", "❌", "NON SAPER LEGGERE"], ["MANZI", "📺", "MAESTRO IN TV"],
  ["SIA", "🔁", "CONGIUNTIVO DI ESSERE"], ["ABBIA", "🔁", "CONGIUNTIVO DI AVERE"], ["VADA", "🔁", "CONGIUNTIVO DI ANDARE"], ["FACCIA", "🔁", "CONGIUNTIVO DI FARE"],
  ["POSSA", "🔁", "CONGIUNTIVO DI POTERE"], ["SPERO CHE", "🙏", "+ CONGIUNTIVO"]]),
 "b1-scuola-famiglia": ("b1-cittadini", "B1", "👨‍👩‍👦 GIOCHI: SCUOLA E FAMIGLIA (B1)", [
  ["IL COLLOQUIO", "🗣️", "INCONTRO CON L'INSEGNANTE"], ["LA PAGELLA", "📄", "IL DOCUMENTO DEI VOTI"], ["LA SUFFICIENZA", "6️⃣", "IL VOTO 6"], ["IL GIUDIZIO", "💬", "VALUTAZIONE A PAROLE"],
  ["LE COMPETENZE", "🧠", "SAPER FARE"], ["IL DOPOSCUOLA", "🕓", "AIUTO NEL POMERIGGIO"], ["LA PRIMARIA", "🏫", "LA SCUOLA ELEMENTARE"], ["LA MEDIA", "🏫", "DAGLI 11 AI 14 ANNI"],
  ["LA MATURITÀ", "🎓", "ESAME FINALE DELLE SUPERIORI"], ["LA GIUSTIFICAZIONE", "✍️", "FIRMA PER UN'ASSENZA"], ["IL CORSO SERALE", "🌙", "SCUOLA PER CHI LAVORA"], ["LA MERENDA", "🍎", "SPUNTINO A METÀ MATTINA"],
  ["BENCHÉ", "🔗", "ANCHE SE"], ["AFFINCHÉ", "🎯", "PER, CON SCOPO"], ["PURCHÉ", "✅", "SOLO SE"], ["PRIMA CHE", "⏪", "PRIMA DI"],
  ["BISOGNA CHE", "❗", "È NECESSARIO CHE"], ["LO ZAINO", "🎒", "LO PORTI A SCUOLA"]]),
 "b1-scuola-superiore": ("b1-cittadini", "B1", "🎒 GIOCHI: LA SCUOLA SUPERIORE (B1)", [
  ["IL LICEO", "🏛️", "PREPARA ALL'UNIVERSITÀ"], ["IL TECNICO", "⚙️", "TEORIA E LABORATORI"], ["IL PROFESSIONALE", "🔧", "PER UN MESTIERE"], ["LO STAGE", "💼", "ESPERIENZA IN AZIENDA"],
  ["IL LABORATORIO", "🧪", "AULA PER ESPERIMENTI"], ["L'OPEN DAY", "🚪", "GIORNATA DI VISITA"], ["LO SPID", "🔑", "IDENTITÀ DIGITALE"], ["IL CODICE", "🔢", "MECCANOGRAFICO DELLA SCUOLA"],
  ["LA SEGRETERIA", "🗂️", "UFFICIO DELLA SCUOLA"], ["LA SCADENZA", "📅", "ULTIMO GIORNO"], ["LA CONFERMA", "📧", "EMAIL DOPO L'ISCRIZIONE"], ["L'INDIRIZZO", "🧭", "TIPO DI STUDI"],
  ["LA MENSA", "🍝", "DOVE SI MANGIA A SCUOLA"], ["LA GITA", "🚌", "VIAGGIO CON LA CLASSE"], ["LA PASSERELLA", "↔️", "PER CAMBIARE INDIRIZZO"], ["NON SO SE", "🤔", "DUBBIO"],
  ["MI CHIEDO", "❓", "DOMANDA INDIRETTA"], ["IL TURISMO", "🧳", "SALMA LO VUOLE STUDIARE"]]),
 "b1-libri-viaggi": ("b1-cittadini", "B1", "📖 GIOCHI: LIBRI E VIAGGI (B1)", [
  ["LA BIBLIOTECA", "📚", "DOVE PRENDI I LIBRI IN PRESTITO"], ["IL PRESTITO", "🤝", "PRENDERE E RESTITUIRE"], ["LA TESSERA", "💳", "PER LA BIBLIOTECA"], ["LO SCAFFALE", "🗄️", "DOVE STANNO I LIBRI"],
  ["IL GIALLO", "🕵️", "LIBRO CON UN MISTERO"], ["IL ROMANZO", "📕", "LUNGA STORIA INVENTATA"], ["LA POESIA", "✒️", "VERSI E RIME"], ["LA BIOGRAFIA", "📜", "VITA DI UNA PERSONA"],
  ["L'AUTORE", "✍️", "CHI SCRIVE IL LIBRO"], ["IL PULLMAN", "🚌", "AUTOBUS PER VIAGGI LUNGHI"], ["LA PRENOTAZIONE", "🧾", "RISERVARE UN POSTO"], ["L'ALBERGO", "🏨", "DOVE DORMI IN VIAGGIO"],
  ["MATERA", "🏘️", "LA CITTÀ DEI SASSI"], ["LA VALIGIA", "🧳", "LA PREPARI PRIMA DI PARTIRE"], ["MI DICA", "💬", "IMPERATIVO DI DIRE (LEI)"], ["SI SIEDA", "🪑", "IMPERATIVO DI SEDERSI (LEI)"],
  ["VENGA", "👋", "IMPERATIVO DI VENIRE (LEI)"], ["COMPILI", "📝", "IMPERATIVO DI COMPILARE (LEI)"]]),
}

if __name__ == "__main__":
    for path, unit, top, sl, liv in SLIDE:
        os.makedirs(os.path.dirname(path), exist_ok=True)
        build_slide(path, unit, top, sl, liv)
    for cartella, dati in ESERCIZI:
        build_es(cartella + "/esercizi.html", dati)
    build_giochi(GIOCHI)
