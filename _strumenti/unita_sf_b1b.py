"""Percorso B1, modulo 2 («Il lavoro») sulla traccia di «Nuovo Senza frontiere 3» (Edilingua): unità 5-8.
Testi, dialoghi, nomi e ascolti NUOVI (Erila, 2026-11-23: «rifaccio tutto con testi nuovi»). Stile "b1".
Uso: python3 _strumenti/unita_sf_b1b.py   (dalla cartella principale del sito)"""
import os, sys
sys.path.insert(0, os.path.dirname(__file__))
from genera import eq, build as build_es
from unita_primi import cover, slide, cards, table, nota, dialogo, end
from unita_drive import vf, scegli, menu, ordina, parla, libero
from teoria import tab, es
from unita_sf import scrivi, ascolto, testo, build_slide, build_giochi

# =====================================================================
# B1 · UNITÀ 5 · SONO UNA MEDIATRICE CULTURALE
# =====================================================================
MED = [("F", "Buongiorno, sono Saleah, la mediatrice culturale dell'ospedale. Sono qui per aiutarvi a capirvi."),
       ("M", "Meno male! Il signore che ho visitato ieri non capisce il referto che gli ho dato."),
       ("F", "Gliel'ho appena spiegato in arabo. Il problema è un altro: è arrabbiato perché ha aspettato sei ore."),
       ("M", "Capisco. Purtroppo stanotte il Pronto Soccorso era pieno."),
       ("F", "Lui vorrebbe fare un reclamo. A chi si deve rivolgere?"),
       ("M", "All'URP, l'Ufficio Relazioni con il Pubblico, che è al piano terra. C'è un modulo che si può compilare anche online."),
       ("F", "Perfetto, lo accompagno io. Chi ha un problema deve poterlo dire, ma con calma: così lo ascoltano meglio.")]
MED_SLIDE = [
    cover("🤝", "Sono una mediatrice culturale", "Il modulo di reclamo · Chiedere le ferie · I tipi di permesso", "B1 &bull; Modulo 2 &bull; Unità 1"),
    slide("In questa unità impari a…", cards([
        ("🧑‍💼", "Descrivere un lavoro", "che cosa fa, quali compiti ha"), ("🕊️", "Mediare un conflitto", "Capisco, però… Proviamo a…"),
        ("📝", "Compilare un reclamo", "il modulo dell'URP"), ("✉️", "Scrivere un'email formale", "Gentile…, Cordiali saluti")])),
    slide("🏥 Le parole della sanità e del reclamo", cards([
        ("📄", "il referto", "il risultato scritto di una visita o di un esame"), ("🩺", "la diagnosi", "il nome della malattia"),
        ("🏢", "l'URP", "l'ufficio che riceve reclami e segnalazioni"), ("😠", "il disservizio", "un servizio che non funziona"),
        ("🔎", "lo smarrimento", "la perdita di un oggetto o di un documento"), ("🚫", "il mancato rispetto", "quando non si rispettano regole o persone")], "g3")),
    slide("🏥 Lezione A · Il modulo di reclamo", dialogo([("*Saleah" if v == "F" else "Dottor Ferri", t) for v, t in MED])),
    slide("📘 I pronomi relativi che, cui, chi", table([
        ["che", "soggetto o oggetto", "Il signore <b>che</b> ho visitato…"], ["cui", "dopo una preposizione", "L'ufficio a <b>cui</b> ti rivolgi · Il motivo per <b>cui</b> protesto"],
        ["chi", "«la persona che», senza nome prima", "<b>Chi</b> ha un problema deve poterlo dire."]], head=["pronome", "quando", "esempio"]) + "\n" +
        nota("<b>Che</b> non cambia mai. Dopo <b>a, di, da, in, con, su, per, tra</b> si usa <b>cui</b>.")),
    slide("✉️ Lezione B · Chiedere le ferie", '    <div class="box"><p><b>Oggetto:</b> richiesta di ferie</p>'
          "<p>Gentile dott.ssa Lorusso,</p><p>Le scrivo per chiederLe due settimane di ferie, dal 3 al 17 agosto, periodo nel quale "
          "vorrei tornare in Marocco per il matrimonio di mia sorella. Ho già parlato con la collega con la quale divido i turni: è disponibile a sostituirmi.</p>"
          "<p>RingraziandoLa per l'attenzione, resto in attesa di una Sua risposta.</p><p>Cordiali saluti,<br>Saleah Bennani</p></div>"),
    slide("📘 Il relativo «il quale»", table([
        ["il quale", "la quale", "Il periodo <b>nel quale</b> vorrei partire = in cui"], ["i quali", "le quali", "Le colleghe <b>con le quali</b> lavoro = con cui"]],
        head=["maschile", "femminile", "esempio"]) + "\n" + nota("<b>Il quale</b> è più formale di <b>cui</b>: si usa nelle lettere e nei documenti. Vuole l'articolo: a + il quale = <b>al quale</b>.")),
    slide("✉️ Le abbreviazioni nelle lettere", table([
        ["Sig. / Sig.ra", "Signore / Signora"], ["Gent.mo / Gent.ma", "Gentilissimo / Gentilissima"], ["Egr.", "Egregio (molto formale)"],
        ["Dott. / Dott.ssa", "Dottore / Dottoressa"], ["Avv.", "Avvocato"], ["Prof. / Prof.ssa", "Professore / Professoressa"]], head=["abbreviazione", "parola intera"])),
    slide("🪪 Educazione civica · I tipi di permesso di soggiorno", cards([
        ("💼", "per lavoro", "subordinato, autonomo, stagionale"), ("👨‍👩‍👧", "per motivi familiari", "ricongiungimento, coesione familiare"),
        ("🎓", "per studio", "università, corsi di formazione"), ("🛡️", "protezione internazionale", "asilo e protezione sussidiaria"),
        ("🕊️", "protezione speciale", "per chi rischierebbe gravi danni al rientro"), ("♾️", "UE per soggiornanti di lungo periodo", "dopo 5 anni, a tempo indeterminato")], "g3")),
    end("Ora sai fare un reclamo e scrivere un'email formale!"),
]
B1MED = {
 "title": "🤝 Sono una mediatrice culturale · Esercizi", "store": "b1-mediatrice", "livello": "b1",
 "sections": [
  {"part": "Le parole"},
  menu(["il referto", "la diagnosi", "l'URP", "il disservizio", "lo smarrimento"],
       [("1. Il risultato scritto di un esame del sangue.", "il referto"), ("2. L'ufficio a cui si presenta un reclamo.", "l'URP"),
        ("3. «Ha l'influenza»: è la …", "la diagnosi"), ("4. Ho perso la tessera sanitaria: è uno …", "lo smarrimento"),
        ("5. L'ascensore dell'ospedale non funziona da un mese: è un …", "il disservizio")],
       "1 · Che cos'è?", "1 · Le parole", "e1"),
  {"part": "Lezione A · In ospedale"},
  ascolto(vf(["1. Saleah lavora come infermiera.", "2. Il paziente non capiva il referto.", "3. Il paziente è arrabbiato per l'attesa.",
              "4. L'URP è all'ultimo piano.", "5. Il modulo di reclamo si può compilare anche online.", "6. Saleah accompagnerà il paziente."],
             ["FALSO", "VERO", "VERO", "FALSO", "VERO", "VERO"], "2 · 🎧 Ascolta il dialogo: vero o falso?", "2 · In ospedale", "e2"), [list(x) for x in MED]),
  {"part": "I pronomi relativi che, cui, chi", "teoria":
     tab(("che", "soggetto / oggetto"), ("preposizione + cui", "a cui, con cui, per cui…"), ("chi", "la persona che"), head=("pronome", "uso")) +
     es("Il medico <b>che</b> mi ha visitato. · L'ufficio <b>a cui</b> ho scritto. · <b>Chi</b> arriva tardi aspetta.")},
  menu(["che", "cui", "chi"],
       [("1. Il modulo … ho compilato è sul tavolo.", "che"), ("2. La collega con … lavoro è molto brava.", "cui"), ("3. … ha bisogno di aiuto può chiamare.", "chi"),
        ("4. Il motivo per … protesto è l'attesa.", "cui"), ("5. La mediatrice … parla arabo si chiama Saleah.", "che"), ("6. … non capisce, può chiedere.", "chi")],
       "3 · Che, cui o chi?", "3 · I relativi", "e3"),
  scrivi([("1. L'ospedale in … lavoro è grande.", ("cui",)), ("2. Il paziente … ho aiutato era molto stanco.", ("che",)),
          ("3. … vuole fare un reclamo va all'URP.", ("chi",)), ("4. La lingua di … ti parlo è il wolof.", ("cui",)),
          ("5. Il referto … mi hanno dato non è chiaro.", ("che",))],
         "4 · Completa con che, cui, chi", "4 · Completa", "e4", bank="che · cui · chi", w="s"),
  {"part": "Lezione B · Chiedere le ferie", "teoria":
     tab(("il quale / la quale", "singolare"), ("i quali / le quali", "plurale"), head=("forma", "")) +
     "Sostituisce <b>cui</b> nello stile formale, con l'articolo." + es("Il periodo <b>nel quale</b> vorrei partire. · Le colleghe <b>con le quali</b> lavoro.")},
  scegli([("1. Il collega … il quale divido i turni è disponibile.", ["con", "di", "a"], "con"), ("2. L'ufficio … quale ho scritto non risponde.", ["al", "alla", "ai"], "al"),
          ("3. Le persone con … quali lavoro sono gentili.", ["le", "i", "la"], "le"), ("4. La ragione per … quale chiedo le ferie è un matrimonio.", ["la", "il", "le"], "la")],
         "5 · Scegli la forma di «quale»", "5 · Il quale", "e5"),
  menu(["Gentile dott.ssa Lorusso,", "Le scrivo per chiederLe", "RingraziandoLa per l'attenzione,", "Cordiali saluti,", "Oggetto:"],
       [("1. Il tema dell'email, in alto.", "Oggetto:"), ("2. Il saluto iniziale.", "Gentile dott.ssa Lorusso,"), ("3. Per presentare la richiesta.", "Le scrivo per chiederLe"),
        ("4. Prima di salutare.", "RingraziandoLa per l'attenzione,"), ("5. Il saluto finale.", "Cordiali saluti,")],
       "6 · Le parti dell'email formale", "6 · L'email", "e6"),
  {"part": "Educazione civica · I permessi"},
  menu(["per lavoro", "per motivi familiari", "per studio", "protezione internazionale", "UE per soggiornanti di lungo periodo"],
       [("1. Kofi frequenta l'università a Bari.", "per studio"), ("2. Leila è arrivata per raggiungere il marito.", "per motivi familiari"),
        ("3. Ivan vive in Italia da 8 anni e ha un permesso senza scadenza.", "UE per soggiornanti di lungo periodo"),
        ("4. Abdi ha ottenuto l'asilo politico.", "protezione internazionale"), ("5. Rosa lavora in un'azienda con contratto.", "per lavoro")],
       "7 · Che permesso hanno?", "7 · I permessi", "e7"),
  libero("e8", 8, "Come comunico: un'email formale", "Scrivi un'email formale al tuo datore di lavoro per chiedere un giorno di permesso. Usa: Gentile…, Le scrivo per…, il quale / in cui, Cordiali saluti.", ["La mia email"], rows=8),
  parla("e9", 9, "Secondo te, che qualità deve avere un mediatore culturale? Hai mai avuto bisogno di un mediatore?"),
 ]
}

# =====================================================================
# B1 · UNITÀ 6 · TRASFERIRSI PER LAVORO
# =====================================================================
TRAS = [("M", "Cristian, ho una bella notizia! Mi hanno accettato il trasferimento a Bologna!"),
        ("M", "Davvero? Che sorpresa! Ma come mai hai chiesto di trasferirti?"),
        ("M", "La città dove vive mia sorella è vicina a Bologna, e lì l'azienda ha uno stabilimento più grande. Così posso crescere professionalmente."),
        ("M", "E quanti colleghi conosci lì?"),
        ("M", "Ne conosco pochi, ma quelli che conosco sono simpatici. Ho già scritto al responsabile per ringraziarlo."),
        ("M", "Sono proprio contento per te! Quando parti?"),
        ("M", "Il primo marzo. Prima devo comprare un sacco di cose online per la casa nuova!")]
TRAS_SLIDE = [
    cover("🚚", "Trasferirsi per lavoro", "La richiesta di trasferimento · Gli acquisti online · L'e-commerce", "B1 &bull; Modulo 2 &bull; Unità 2"),
    slide("In questa unità impari a…", cards([
        ("🧭", "Motivare una scelta", "Ho deciso di… perché…"), ("🎉", "Esprimere felicità e sorpresa", "Che bella notizia! Davvero?"),
        ("🙏", "Ringraziare formalmente", "La ringrazio per…"), ("🛒", "Comprare online", "carrello, spedizione, reso")])),
    slide("📋 Il modulo di trasferimento", cards([
        ("🏷️", "la qualifica", "il tuo ruolo: operaio specializzato, impiegato…"), ("📍", "la sede", "il luogo di lavoro"),
        ("🗓️", "la disponibilità", "da quando puoi cominciare"), ("✍️", "la motivazione", "perché chiedi il trasferimento")], "g2")),
    slide("🎉 Lezione A · La richiesta di trasferimento", dialogo([("Ibrahim" if i % 2 == 0 else "*Cristian", t) for i, (_, t) in enumerate(TRAS)])),
    slide("📘 Quanto / quanti e la frase con «dove»", table([
        ["quanto / quanta", "Quanto costa? Quanta pazienza!"], ["quanti / quante", "Quanti colleghi conosci? Quante ore lavori?"],
        ["dove (= in cui)", "La città <b>dove</b> vive mia sorella = la città <b>in cui</b> vive"]], head=["parola", "esempio"]) + "\n" +
        nota("<b>Quanto</b> si accorda con il nome: quant<b>i</b> colleghi, quant<b>e</b> ore.")),
    slide("🛒 Lezione B · Gli acquisti online", testo(
        "Ibrahim compra una lavatrice online. Il prodotto è in <b>disponibilità immediata</b>: parte domani. Sceglie la <b>consegna</b> a domicilio, "
        "ma poiché lavora tutto il giorno, la fa arrivare in un <b>punto di ritiro</b> sotto casa, che la tiene in <b>custodia</b> per 7 giorni.",
        "Il materasso invece è <b>esaurito</b>: Ibrahim decide di aspettare. Si fida del negozio perché ha molte recensioni positive.")),
    slide("📘 Verbi con preposizione", table([
        ["di", "decidere <b>di</b>, smettere <b>di</b>, pensare <b>di</b>, avere bisogno <b>di</b>", "Ho deciso <b>di</b> trasferirmi."],
        ["a", "cominciare <b>a</b>, riuscire <b>a</b>, abituarsi <b>a</b>, pensare <b>a</b>", "Mi abituo <b>alla</b> città nuova."],
        ["da", "dipendere <b>da</b>, partire <b>da</b>", "Dipende <b>dal</b> prezzo."], ["in", "credere <b>in</b>, sperare <b>in</b>", "Credo <b>in</b> questo progetto."]],
        head=["preposizione", "verbi", "esempio"])),
    slide("🛍️ Educazione civica · Comprare online in Italia", cards([
        ("↩️", "il diritto di recesso", "14 giorni per restituire un prodotto comprato online"), ("🛡️", "la garanzia", "2 anni sui prodotti nuovi"),
        ("🔒", "pagamenti sicuri", "siti con https, carte prepagate"), ("⭐", "le recensioni", "leggile prima di comprare"),
        ("🧾", "la fattura / lo scontrino", "conserva sempre la prova d'acquisto"), ("🚨", "attenzione", "prezzi troppo bassi possono essere truffe")], "g3")),
    end("Ora sai motivare una scelta e comprare online!"),
]
B1TRAS = {
 "title": "🚚 Trasferirsi per lavoro · Esercizi", "store": "b1-trasferirsi", "livello": "b1",
 "sections": [
  {"part": "Lezione A · Il trasferimento"},
  ascolto(scegli([("1. Ibrahim si trasferisce a…", ["Milano", "Bologna", "Torino"], "Bologna"),
                  ("2. Vicino a Bologna vive…", ["suo fratello", "sua sorella", "sua madre"], "sua sorella"),
                  ("3. A Bologna l'azienda ha…", ["uno stabilimento più grande", "un ufficio piccolo", "un negozio"], "uno stabilimento più grande"),
                  ("4. Ibrahim parte…", ["il primo marzo", "il primo maggio", "a giugno"], "il primo marzo")],
                 "1 · 🎧 Ascolta Ibrahim e Cristian", "1 · Il trasferimento", "e1"), [list(x) for x in TRAS]),
  menu(["felicità", "sorpresa", "ringraziamento"],
       [("1. Che bella notizia!", "felicità"), ("2. Davvero? Non ci credo!", "sorpresa"), ("3. La ringrazio per la Sua disponibilità.", "ringraziamento"),
        ("4. Sono proprio contento per te!", "felicità"), ("5. Ma come mai? Non me l'aspettavo!", "sorpresa"), ("6. Grazie infinite per l'aiuto.", "ringraziamento")],
       "2 · Che cosa esprimono?", "2 · Emozioni", "e2"),
  {"part": "Quanto / quanti e la frase con «dove»", "teoria":
     tab(("quanto / quanta", "singolare"), ("quanti / quante", "plurale"), ("dove", "= in cui"), head=("parola", "uso")) +
     es("<b>Quante</b> ore lavori? · La città <b>dove</b> abito.")},
  menu(["quanto", "quanta", "quanti", "quante", "dove"],
       [("1. … colleghi lavorano nello stabilimento?", "quanti"), ("2. … costa il trasloco?", "quanto"), ("3. … ore di viaggio ci sono?", "quante"),
        ("4. La fabbrica … lavoro è nuova.", "dove"), ("5. … pazienza ci vuole con la burocrazia!", "quanta"), ("6. Il quartiere … abiti è tranquillo?", "dove")],
       "3 · Scegli la parola giusta", "3 · quanto, dove", "e3"),
  {"part": "Lezione B · Gli acquisti online"},
  vf(["1. La lavatrice è in disponibilità immediata.", "2. Ibrahim la fa arrivare al lavoro.", "3. Il punto di ritiro tiene il pacco per 7 giorni.",
      "4. Il materasso è esaurito.", "5. Il negozio ha molte recensioni negative."], ["VERO", "FALSO", "VERO", "VERO", "FALSO"],
     "4 · Leggi il testo delle slide: vero o falso?", "4 · Acquisti online", "e4",
     info="Ibrahim compra una lavatrice online. Il prodotto è in disponibilità immediata: parte domani. Sceglie la consegna a domicilio, ma poiché lavora tutto il giorno, "
          "la fa arrivare in un punto di ritiro sotto casa, che la tiene in custodia per 7 giorni. Il materasso invece è esaurito: Ibrahim decide di aspettare. "
          "Si fida del negozio perché ha molte recensioni positive."),
  {"part": "Verbi con preposizione", "teoria":
     tab(("di", "decidere, smettere, pensare di"), ("a", "cominciare, riuscire, abituarsi a"), ("da", "dipendere da"), ("in", "credere, sperare in"), head=("preposizione", "verbi")) +
     es("Ho deciso <b>di</b> partire. · Non riesco <b>a</b> trovare casa.")},
  menu(["di", "a", "da", "in"],
       [("1. Ho deciso … chiedere il trasferimento.", "di"), ("2. Non riesco … trovare un appartamento.", "a"), ("3. Il prezzo dipende … quartiere.", "da"),
        ("4. Spero … una risposta veloce.", "in"), ("5. Mi devo abituare … freddo del nord.", "a"), ("6. Ho bisogno … un furgone per il trasloco.", "di")],
       "5 · Scegli la preposizione", "5 · Le preposizioni", "e5"),
  {"part": "Educazione civica · Comprare online"},
  vf(["1. Per un acquisto online c'è il diritto di recesso di 14 giorni.", "2. I prodotti nuovi hanno 2 anni di garanzia.", "3. Un prezzo molto basso è sempre un affare sicuro.",
      "4. È meglio conservare la prova d'acquisto."], ["VERO", "VERO", "FALSO", "VERO"], "6 · L'e-commerce: vero o falso?", "6 · E-commerce", "e6"),
  libero("e7", 7, "La richiesta di trasferimento", "Scrivi una breve richiesta formale di trasferimento: chi sei, dove vuoi andare, perché, da quando sei disponibile. Ringrazia alla fine.", ["La mia richiesta"], rows=7),
  parla("e8", 8, "Ti trasferiresti in un'altra città per lavoro? Perché? Che cosa compri online e che cosa preferisci comprare in negozio?"),
 ]
}

# =====================================================================
# B1 · UNITÀ 7 · LAVORO COME ELETTRICISTA
# =====================================================================
INC = [("M", "Pronto, 118? C'è stato un incidente in un cantiere in via Capruzzi, a Bari."),
       ("F", "Che cosa è successo?"),
       ("M", "Un mio collega elettricista è caduto da una scala. È cosciente, ma ha molto dolore a una gamba."),
       ("F", "Non muovetelo. Respira bene? Perde sangue?"),
       ("M", "Respira, e non perde sangue. Aveva il casco, per fortuna."),
       ("F", "Va bene. Arriviamo in dieci minuti. Restate con lui e tenetelo al caldo.")]
ELE_SLIDE = [
    cover("⚡", "Lavoro come elettricista", "Un incidente sul lavoro · Al sindacato · La sicurezza", "B1 &bull; Modulo 2 &bull; Unità 3"),
    slide("In questa unità impari a…", cards([
        ("🦺", "Capire istruzioni di sicurezza", "È obbligatorio… È vietato…"), ("🚑", "Chiamare i soccorsi", "C'è stato un incidente…"),
        ("✊", "Parlare con il sindacato", "contratto, diritti, straordinari"), ("🔁", "Usare i pronomi combinati", "Te lo dico · Gliel'ho spiegato")])),
    slide("🦺 I dispositivi di sicurezza", cards([
        ("⛑️", "il casco", "protegge la testa"), ("🧤", "i guanti isolanti", "proteggono dalla corrente"), ("🥾", "le scarpe antinfortunistiche", "con la punta rinforzata"),
        ("🦺", "il giubbotto ad alta visibilità", "per essere visti"), ("🪢", "l'imbracatura", "per lavorare in alto senza cadere"), ("🥽", "gli occhiali protettivi", "proteggono gli occhi")], "g3")),
    slide("🚑 Lezione A · Un incidente sul lavoro", dialogo([("Michele" if v == "M" else "*Operatrice 118", t) for v, t in INC])),
    slide("📘 I pronomi combinati", table([
        ["mi + lo/la/li/le/ne", "me lo, me la, me li, me le, me ne"], ["ti + …", "te lo, te la, te li, te le, te ne"],
        ["gli / le / Le + …", "glielo, gliela, glieli, gliele, gliene"], ["ci + …", "ce lo, ce la, ce li, ce le, ce ne"], ["vi + …", "ve lo, ve la, ve li, ve le, ve ne"]],
        head=["indiretto + diretto", "forma"]) + "\n" + nota("Il casco? <b>Te lo</b> presto io. · Le istruzioni? <b>Gliele</b> do subito.")),
    slide("✊ Lezione B · Al sindacato", dialogo([
        ("Michele", "Buongiorno. Il mio datore di lavoro non ci dà le scarpe antinfortunistiche. Dobbiamo comprarcele noi?"),
        ("*Sindacalista", "No, assolutamente. I dispositivi di sicurezza deve fornirveli l'azienda, gratis. Allora, gliel'avete chiesto?"),
        ("Michele", "Sì, gliel'abbiamo chiesto due volte, ma non ce le ha date."),
        ("*Sindacalista", "Dunque, scriviamo una lettera insieme. E il contratto? Me lo fa vedere?"),
        ("Michele", "Eccolo. Il problema è anche che non mi pagano gli straordinari."),
        ("*Sindacalista", "Vediamo… Qui c'è scritto chiaramente: gli straordinari devono pagarteli. Ci pensiamo noi.")])),
    slide("📘 Pronomi combinati e passato prossimo", table([
        ["Il contratto?", "<b>Me l'</b>hanno dato ieri."], ["Le scarpe?", "Non <b>ce le</b> hanno dat<b>e</b>."], ["La lettera?", "<b>Gliel'</b>abbiamo mandat<b>a</b>."]],
        head=["", "esempio"]) + "\n" + nota("Il participio si accorda con <b>lo, la, li, le</b>. Segnali del discorso: <b>allora</b>, <b>dunque</b>, <b>quindi</b>, <b>insomma</b>.")),
    slide("🛡️ Educazione civica · La sicurezza sul lavoro", cards([
        ("📚", "la formazione", "è obbligatoria e gratuita per ogni lavoratore"), ("🦺", "i DPI", "dispositivi di protezione: li dà il datore di lavoro, gratis"),
        ("🧑‍🔧", "l'RLS", "il rappresentante dei lavoratori per la sicurezza"), ("🚑", "112 / 118", "numeri per le emergenze"),
        ("📝", "l'infortunio", "va sempre comunicato e denunciato all'INAIL"), ("🚫", "il diritto di rifiutare", "puoi fermarti se c'è un pericolo grave")], "g3")),
    end("Ora sai parlare di sicurezza e dei tuoi diritti!"),
]
B1ELE = {
 "title": "⚡ Lavoro come elettricista · Esercizi", "store": "b1-elettricista", "livello": "b1",
 "sections": [
  {"part": "La sicurezza"},
  menu(["il casco", "i guanti isolanti", "le scarpe antinfortunistiche", "il giubbotto ad alta visibilità", "l'imbracatura", "gli occhiali protettivi"],
       [("1. Lavori sul tetto: per non cadere usi …", "l'imbracatura"), ("2. Tocchi i fili della corrente: usi …", "i guanti isolanti"),
        ("3. Può cadere qualcosa dall'alto: metti …", "il casco"), ("4. Lavori in strada di notte: metti …", "il giubbotto ad alta visibilità"),
        ("5. Tagli il metallo e volano schegge: usi …", "gli occhiali protettivi"), ("6. Porti pesi che possono cadere sui piedi: usi …", "le scarpe antinfortunistiche")],
       "1 · Che cosa usi?", "1 · I DPI", "e1"),
  {"part": "Lezione A · La chiamata al 118"},
  ascolto(vf(["1. L'incidente è successo in un cantiere.", "2. Il collega è caduto da un tetto.", "3. Il collega è svenuto.", "4. Aveva il casco.",
              "5. L'operatrice dice di muoverlo subito.", "6. L'ambulanza arriva in dieci minuti."],
             ["VERO", "FALSO", "FALSO", "VERO", "FALSO", "VERO"], "2 · 🎧 Ascolta la telefonata: vero o falso?", "2 · Il 118", "e2"), [list(x) for x in INC]),
  {"part": "I pronomi combinati", "teoria":
     tab(("mi / ti + lo", "me lo / te lo"), ("gli / le + lo", "glielo"), ("ci / vi + le", "ce le / ve le"), head=("pronomi", "forma")) +
     "Prima l'indiretto (a chi?), poi il diretto (che cosa?)." + es("Il casco? <b>Te lo</b> presto. · Il contratto? <b>Glielo</b> mando.")},
  scrivi([("1. Mi presti il cacciavite? Sì, … presto.", ("te lo",)), ("2. Dai le istruzioni a Michele? Sì, … do.", ("gliele",)),
          ("3. Ci porti i guanti? Sì, … porto.", ("ve li",)), ("4. Mi spieghi la procedura? Sì, … spiego.", ("te la",)),
          ("5. Mandi il certificato al capo? Sì, … mando.", ("glielo",)), ("6. Ci date il contratto? Sì, … diamo.", ("ve lo",))],
         "3 · Rispondi con i pronomi combinati", "3 · Pronomi combinati", "e3", w="s"),
  {"part": "Lezione B · Al sindacato", "teoria":
     "Con il passato prossimo il participio si accorda con lo, la, li, le." + es("Le scarpe? Non <b>ce le</b> hanno dat<b>e</b>. · La lettera? <b>Gliel'</b>abbiamo mandat<b>a</b>.")},
  scegli([("1. Le scarpe? Non ce le hanno …", ["dato", "date", "dati"], "date"), ("2. Il contratto? Me l'hanno …", ["dato", "data", "dati"], "dato"),
          ("3. La busta paga? Gliel'ho …", ["mandato", "mandata", "mandate"], "mandata"), ("4. I guanti? Ve li ho …", ["portato", "portati", "portate"], "portati")],
         "4 · Scegli il participio giusto", "4 · L'accordo", "e4"),
  vf(["1. Michele deve comprare le scarpe di sicurezza da solo.", "2. Hanno chiesto le scarpe una volta.", "3. Il sindacalista vuole vedere il contratto.",
      "4. A Michele non pagano gli straordinari."], ["FALSO", "FALSO", "VERO", "VERO"], "5 · Il dialogo al sindacato: vero o falso?", "5 · Al sindacato", "e5"),
  menu(["allora", "dunque", "insomma"],
       [("1. … , ricapitolando: l'azienda deve darvi le scarpe.", "insomma"), ("2. … , cominciamo: come si chiama?", "allora"),
        ("3. Non vi hanno dato i DPI, … scriviamo una lettera.", "dunque")],
       "6 · I segnali del discorso", "6 · Segnali", "e6"),
  {"part": "Educazione civica · La sicurezza sul lavoro"},
  vf(["1. La formazione sulla sicurezza è obbligatoria.", "2. I DPI li paga il lavoratore.", "3. L'RLS rappresenta i lavoratori per la sicurezza.",
      "4. Un infortunio va comunicato all'INAIL.", "5. Se c'è un pericolo grave, il lavoratore deve continuare a lavorare."],
     ["VERO", "FALSO", "VERO", "VERO", "FALSO"], "7 · La sicurezza: vero o falso?", "7 · Sicurezza", "e7"),
  libero("e8", 8, "Cosa dire quando chiamiamo il soccorso", "Scrivi che cosa diresti al 112/118 in caso di incidente: dove sei, che cosa è successo, come sta la persona.", ["La mia chiamata"], rows=5),
  parla("e9", 9, "Che lavoro fai o hai fatto? Quali rischi ci sono? Come ti proteggi?"),
 ]
}

# =====================================================================
# B1 · UNITÀ 8 · I DIRITTI SUL LAVORO
# =====================================================================
RIU = [("F", "Allora, colleghi, la direzione aveva detto che avrebbe rinnovato i contratti a gennaio. Siamo a marzo e non è successo niente."),
       ("M", "Ho sentito dire che l'azienda avrebbe intenzione di chiudere il reparto confezionamento. Ma non è sicuro."),
       ("F", "Secondo i dati del sindacato, negli ultimi due anni la produzione è aumentata del quindici per cento. Non ci sarebbe nessun motivo per chiudere."),
       ("M", "Io avrei preferito parlarne prima con il direttore, ma non ci ha mai ricevuto."),
       ("F", "Infatti. Per questo propongo un'assemblea venerdì e, se serve, uno sciopero di due ore."),
       ("M", "Sono d'accordo. Tra di noi dobbiamo restare uniti.")]
DIR_SLIDE = [
    cover("⚖️", "I diritti sul lavoro", "Una riunione tra colleghi · Che bella manifestazione! · I sindacati", "B1 &bull; Modulo 2 &bull; Unità 4"),
    slide("In questa unità impari a…", cards([
        ("🕰️", "Parlare del futuro nel passato", "Aveva detto che avrebbe rinnovato…"), ("❓", "Dare una notizia non confermata", "L'azienda chiuderebbe…"),
        ("📊", "Leggere dati e grafici", "è aumentato del 15%"), ("📰", "Capire un articolo di giornale", "chi, che cosa, dove, quando, perché")])),
    slide("📊 Le parole dei dati", cards([
        ("📈", "aumentare / la crescita", "+15%"), ("📉", "diminuire / il calo", "−8%"), ("➖", "restare stabile", "uguale"),
        ("🥧", "il grafico a torta", "le parti di un totale"), ("📊", "il grafico a barre", "confronto tra valori"), ("💯", "la percentuale", "per cento")], "g3")),
    slide("🗣️ Lezione A · Una riunione tra colleghi", dialogo([("*Eneida" if v == "F" else "Giovanni", t) for v, t in RIU])),
    slide("📘 Il condizionale passato", table([
        ["avrei / avresti / avrebbe… + participio", "<b>Avrei preferito</b> parlarne prima."], ["sarei / saresti / sarebbe… + participio", "<b>Sarei venuta</b>, ma ero malata."]],
        head=["forma", "esempio"]) + "\n" + nota(
        "Usi: <b>desiderio non realizzato</b> (Avrei voluto…), <b>futuro nel passato</b> (Aveva detto che <b>avrebbe rinnovato</b> i contratti), "
        "<b>notizia non confermata</b> (Secondo i giornali, l'azienda <b>avrebbe chiuso</b> il reparto).")),
    slide("📘 Verbi con le preposizioni con, su, per, tra", table([
        ["con", "parlare con, lavorare con, essere d'accordo con"], ["su", "contare su, discutere su, riflettere su"],
        ["per", "lottare per, votare per, battersi per"], ["tra / fra", "scegliere tra, dividere tra, decidere fra"]], head=["preposizione", "verbi"])),
    slide("📰 Lezione B · Che bella manifestazione!", '    <div class="box"><p><b>Bari, in mille in piazza per il lavoro sicuro</b></p>'
          "<p>Ieri mattina circa mille persone hanno sfilato da piazza della Libertà fino alla Prefettura per chiedere più sicurezza nei cantieri e nelle campagne. "
          "Alla manifestazione, organizzata dai sindacati, hanno partecipato lavoratori italiani e stranieri, studenti e famiglie.</p>"
          "<p>«È stata una giornata bellissima», racconta Cristian, operaio edile. «Avremmo voluto essere ancora di più, ma tanti colleghi lavoravano.» "
          "Secondo gli organizzatori, la Prefettura avrebbe promesso un incontro entro la fine del mese.</p></div>"),
    slide("✊ Educazione civica · I sindacati", cards([
        ("🏛️", "che cosa sono", "associazioni che difendono i diritti dei lavoratori"), ("🇮🇹", "i più grandi", "CGIL, CISL, UIL"),
        ("📄", "il contratto collettivo", "stipendi minimi, ferie, orari per ogni settore"), ("🗳️", "l'assemblea", "riunione dei lavoratori per decidere insieme"),
        ("✊", "lo sciopero", "è un diritto garantito dalla Costituzione (art. 40)"), ("🆓", "gli sportelli", "aiuto con buste paga, permessi, disoccupazione")], "g3")),
    end("Ora conosci meglio i tuoi diritti sul lavoro!"),
]
B1DIR = {
 "title": "⚖️ I diritti sul lavoro · Esercizi", "store": "b1-diritti-lavoro", "livello": "b1",
 "sections": [
  {"part": "Le parole dei dati"},
  menu(["è aumentata", "è diminuita", "è rimasta stabile"],
       [("1. Nel 2024 la produzione era 100, nel 2025 è 115: la produzione …", "è aumentata"), ("2. I dipendenti erano 50, ora sono 42: l'occupazione …", "è diminuita"),
        ("3. Lo stipendio medio era 1.400 euro e oggi è uguale: la paga …", "è rimasta stabile"), ("4. Gli incidenti erano 20, ora sono 12: la cifra …", "è diminuita")],
       "1 · Leggi i dati", "1 · I dati", "e1"),
  {"part": "Lezione A · La riunione"},
  ascolto(vf(["1. La direzione aveva promesso di rinnovare i contratti a gennaio.", "2. È sicuro che l'azienda chiuderà il reparto.",
              "3. La produzione è aumentata negli ultimi due anni.", "4. Il direttore ha ricevuto i lavoratori più volte.", "5. Eneida propone un'assemblea venerdì."],
             ["VERO", "FALSO", "VERO", "FALSO", "VERO"], "2 · 🎧 Ascolta la riunione: vero o falso?", "2 · La riunione", "e2"), [list(x) for x in RIU]),
  {"part": "Il condizionale passato", "teoria":
     tab(("avrei… + participio", "avrei preferito"), ("sarei… + participio", "sarei venuto/a"), head=("ausiliare al condizionale", "esempio")) +
     "Desiderio non realizzato, futuro nel passato, notizia non confermata." + es("Aveva detto che <b>sarebbe arrivato</b> alle 9.")},
  scrivi([("1. (volere – io) … partecipare, ma lavoravo.", ("avrei voluto",)), ("2. (rinnovare – la direzione) Aveva detto che … i contratti.", ("avrebbe rinnovato",)),
          ("3. (venire – noi) … alla manifestazione, ma pioveva.", ("saremmo venuti", "saremmo venute")), ("4. (preferire – tu) … un altro turno?", ("avresti preferito",)),
          ("5. (chiudere – l'azienda) Secondo il giornale, … il reparto.", ("avrebbe chiuso",)), ("6. (dovere – voi) … avvisarci prima!", ("avreste dovuto",))],
         "3 · Completa con il condizionale passato", "3 · Condizionale passato", "e3", w="m"),
  menu(["desiderio non realizzato", "futuro nel passato", "notizia non confermata"],
       [("1. Avrei voluto studiare medicina.", "desiderio non realizzato"), ("2. Mi aveva promesso che mi avrebbe chiamato.", "futuro nel passato"),
        ("3. Secondo alcune fonti, il sindaco si sarebbe dimesso.", "notizia non confermata"), ("4. Sapevo che sarebbe stato difficile.", "futuro nel passato"),
        ("5. Sarei andata volentieri in vacanza.", "desiderio non realizzato")],
       "4 · Che uso è?", "4 · Usi", "e4"),
  menu(["con", "su", "per", "tra"],
       [("1. Puoi contare … di me.", "su"), ("2. I lavoratori lottano … un salario giusto.", "per"), ("3. Devo scegliere … due offerte di lavoro.", "tra"),
        ("4. Sono d'accordo … te.", "con"), ("5. Discutiamo … questo problema venerdì.", "su"), ("6. Ho parlato … il delegato sindacale.", "con")],
       "5 · Scegli la preposizione", "5 · Le preposizioni", "e5"),
  {"part": "Lezione B · L'articolo di giornale"},
  scegli([("1. Chi ha organizzato la manifestazione?", ["il Comune", "i sindacati", "la Prefettura"], "i sindacati"),
          ("2. Che cosa chiedevano?", ["più sicurezza", "più ferie", "meno tasse"], "più sicurezza"),
          ("3. Dove è finito il corteo?", ["in piazza della Libertà", "alla Prefettura", "al porto"], "alla Prefettura"),
          ("4. La notizia dell'incontro con la Prefettura è…", ["sicura", "non confermata"], "non confermata")],
         "6 · Leggi l'articolo delle slide", "6 · L'articolo", "e6",
         info="Ieri mattina circa mille persone hanno sfilato da piazza della Libertà fino alla Prefettura per chiedere più sicurezza nei cantieri e nelle campagne. "
              "Alla manifestazione, organizzata dai sindacati, hanno partecipato lavoratori italiani e stranieri, studenti e famiglie. «Avremmo voluto essere ancora di più», "
              "racconta Cristian. Secondo gli organizzatori, la Prefettura avrebbe promesso un incontro entro la fine del mese."),
  {"part": "Educazione civica · I sindacati"},
  vf(["1. I sindacati difendono i diritti dei lavoratori.", "2. Lo sciopero è vietato in Italia.", "3. Il contratto collettivo stabilisce stipendi minimi e ferie.",
      "4. Gli sportelli sindacali aiutano anche con le buste paga."], ["VERO", "FALSO", "VERO", "VERO"], "7 · I sindacati: vero o falso?", "7 · I sindacati", "e7"),
  libero("e8", 8, "Le giornate internazionali", "Scegli una giornata internazionale (1 maggio, 8 marzo, 20 giugno…) e scrivi perché è importante per te.", ["La giornata"], rows=5),
  parla("e9", 9, "Quali diritti dei lavoratori sono più importanti secondo te? Com'è il lavoro nel tuo Paese?"),
 ]
}

SLIDE = [("b1-mediatrice/index.html", "Sono una mediatrice culturale", "B1", MED_SLIDE, "b1"),
         ("b1-trasferirsi/index.html", "Trasferirsi per lavoro", "B1", TRAS_SLIDE, "b1"),
         ("b1-elettricista/index.html", "Lavoro come elettricista", "B1", ELE_SLIDE, "b1"),
         ("b1-diritti-lavoro/index.html", "I diritti sul lavoro", "B1", DIR_SLIDE, "b1")]
ESERCIZI = [("b1-mediatrice", B1MED), ("b1-trasferirsi", B1TRAS), ("b1-elettricista", B1ELE), ("b1-diritti-lavoro", B1DIR)]
GIOCHI = {
 "b1-mediatrice": ("b1-cittadini", "B1", "🤝 GIOCHI: LA MEDIATRICE (B1)", [
  ["IL MEDIATORE", "🤝", "AIUTA A CAPIRSI TRA CULTURE"], ["IL REFERTO", "📄", "RISULTATO SCRITTO DI UN ESAME"], ["LA DIAGNOSI", "🩺", "IL NOME DELLA MALATTIA"], ["IL RECLAMO", "😠", "SI FA ALL'URP"],
  ["L'URP", "🏢", "UFFICIO RELAZIONI CON IL PUBBLICO"], ["LO SMARRIMENTO", "🔎", "PERDITA DI UN OGGETTO"], ["LE FERIE", "🏖️", "GIORNI DI RIPOSO PAGATI"], ["IL TURNO", "⏰", "ORARIO DI LAVORO"],
  ["L'OGGETTO", "✉️", "IL TEMA DELL'EMAIL"], ["GENTILE", "🙂", "SALUTO FORMALE"], ["CORDIALI SALUTI", "👋", "SALUTO FINALE"], ["LA DOTTORESSA", "👩‍⚕️", "DOTT.SSA"],
  ["IL SIGNORE", "🎩", "SIG."], ["IL PERMESSO", "🪪", "DI SOGGIORNO"], ["L'ASILO", "🛡️", "PROTEZIONE INTERNAZIONALE"], ["LO STUDIO", "🎓", "PERMESSO PER L'UNIVERSITÀ"],
  ["CHE", "🔗", "RELATIVO SOGGETTO O OGGETTO"], ["CUI", "🔗", "RELATIVO DOPO LA PREPOSIZIONE"]]),
 "b1-trasferirsi": ("b1-cittadini", "B1", "🚚 GIOCHI: TRASFERIRSI (B1)", [
  ["IL TRASFERIMENTO", "🚚", "CAMBIO DI SEDE DI LAVORO"], ["LA SEDE", "🏢", "IL LUOGO DI LAVORO"], ["LA QUALIFICA", "🏷️", "IL TUO RUOLO"], ["LA MOTIVAZIONE", "✍️", "IL PERCHÉ"],
  ["LO STABILIMENTO", "🏭", "GRANDE FABBRICA"], ["IL TRASLOCO", "📦", "PORTARE I MOBILI IN UNA CASA NUOVA"], ["IL CARRELLO", "🛒", "DOVE METTI I PRODOTTI ONLINE"], ["LA SPEDIZIONE", "📮", "IL PACCO VIAGGIA"],
  ["LA CONSEGNA", "🚪", "IL PACCO ARRIVA A CASA"], ["IL RESO", "↩️", "RESTITUIRE UN PRODOTTO"], ["ESAURITO", "🚫", "NON C'È PIÙ"], ["LA CUSTODIA", "🔐", "TENERE AL SICURO"],
  ["LA RECENSIONE", "⭐", "OPINIONE DI UN CLIENTE"], ["LA GARANZIA", "🛡️", "2 ANNI SUI PRODOTTI NUOVI"], ["IL RECESSO", "📅", "14 GIORNI PER RESTITUIRE"], ["DAVVERO", "😮", "SORPRESA!"],
  ["QUANTI", "🔢", "… COLLEGHI CONOSCI?"], ["DOVE", "📍", "= IN CUI"]]),
 "b1-elettricista": ("b1-cittadini", "B1", "⚡ GIOCHI: L'ELETTRICISTA (B1)", [
  ["IL CASCO", "⛑️", "PROTEGGE LA TESTA"], ["I GUANTI", "🧤", "ISOLANTI PER LA CORRENTE"], ["L'IMBRACATURA", "🪢", "PER LAVORARE IN ALTO"], ["LA SCALA", "🪜", "PER SALIRE"],
  ["IL CANTIERE", "🏗️", "LUOGO DOVE SI COSTRUISCE"], ["L'IMPIANTO", "🔌", "I FILI ELETTRICI DELLA CASA"], ["L'INFORTUNIO", "🚑", "INCIDENTE SUL LAVORO"], ["L'INAIL", "📝", "SI DENUNCIA L'INFORTUNIO"],
  ["IL SINDACATO", "✊", "DIFENDE I LAVORATORI"], ["LO STRAORDINARIO", "⏱️", "ORE DI LAVORO IN PIÙ"], ["LA BUSTA PAGA", "💶", "IL FOGLIO DELLO STIPENDIO"], ["IL CONTRATTO", "📄", "ACCORDO DI LAVORO"],
  ["LA SICUREZZA", "🦺", "NIENTE PERICOLI"], ["LA FORMAZIONE", "📚", "CORSO OBBLIGATORIO"], ["IL CACCIAVITE", "🪛", "ATTREZZO PER LE VITI"], ["IL TRAPANO", "🔩", "FA I BUCHI NEL MURO"],
  ["GLIELO", "🔁", "GLI + LO"], ["TE LO", "🔁", "TI + LO"]]),
 "b1-diritti-lavoro": ("b1-cittadini", "B1", "⚖️ GIOCHI: I DIRITTI SUL LAVORO (B1)", [
  ["LO SCIOPERO", "✊", "SI SMETTE DI LAVORARE PER PROTESTA"], ["L'ASSEMBLEA", "🗳️", "RIUNIONE DEI LAVORATORI"], ["LA MANIFESTAZIONE", "📢", "CORTEO IN PIAZZA"], ["IL DIRITTO", "⚖️", "UNA COSA GARANTITA"],
  ["IL SALARIO", "💶", "LA PAGA"], ["LE FERIE", "🏖️", "RIPOSO PAGATO"], ["LA MALATTIA", "🤒", "ASSENZA PER SALUTE"], ["IL LICENZIAMENTO", "🚪", "PERDERE IL LAVORO"],
  ["IL GRAFICO", "📊", "DISEGNO DEI DATI"], ["LA PERCENTUALE", "💯", "PER CENTO"], ["AUMENTARE", "📈", "CRESCERE"], ["DIMINUIRE", "📉", "CALARE"],
  ["LA CGIL", "🇮🇹", "UN GRANDE SINDACATO"], ["LA COSTITUZIONE", "📜", "ART. 40: LO SCIOPERO"], ["IL DELEGATO", "🙋", "RAPPRESENTA I COLLEGHI"], ["IL REPARTO", "🏭", "UNA PARTE DELLA FABBRICA"],
  ["AVREI VOLUTO", "💭", "DESIDERIO NON REALIZZATO"], ["SAREBBE", "📰", "NOTIZIA NON CONFERMATA"]]),
}

if __name__ == "__main__":
    for path, unit, top, sl, liv in SLIDE:
        os.makedirs(os.path.dirname(path), exist_ok=True)
        build_slide(path, unit, top, sl, liv)
    for cartella, dati in ESERCIZI:
        build_es(cartella + "/esercizi.html", dati)
    build_giochi(GIOCHI)
