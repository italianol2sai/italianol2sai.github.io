"""Livello B1 (2026-10-29): cinque unità con gli argomenti del manuale «Nuovo Contatto B1»
(cronaca e persone, vacanze, tempo libero, lavoro, convivenza e problemi).
Il manuale è servito solo come guida per argomenti e tipi di esercizio: testi, dialoghi ed esercizi
sono scritti nuovi per il sito. Gli ascolti sono letti dalla voce del computer (campo "audio").
Al B1 si scrive in maiuscolo e minuscolo, come nei testi normali."""
from genera import eq, has, all_
from unita_primi import cover, slide, cards, table, nota, dialogo

B1_CSS = """
  body{text-transform:none; letter-spacing:0;}
  .cover h1{font-size:3rem;}
  .esempio{font-size:1.35rem; line-height:1.6; background:#fff; border-radius:14px; padding:14px 18px; border:3px solid #e3edf8; margin-top:12px;}
  .esempio b{color:var(--blu);}
  table.plur{font-size:1.3rem;} table.plur td{text-align:left;}
  @media (max-width:900px){ .cover h1{font-size:2rem;} .esempio{font-size:1.1rem;} table.plur{font-size:.8rem;} table.plur th, table.plur td{padding:6px 3px; overflow-wrap:normal;} }"""


def fine(lead):
    return ('  <section class="slide center cover">\n    <div class="big">🎉</div>\n    <h1>Bravi!</h1>\n'
            '    <p class="lead" style="margin-top:14px;">%s</p>\n'
            '    <a class="badge" href="esercizi.html" style="text-decoration:none">Adesso facciamo gli esercizi 📱</a>\n'
            '  </section>' % lead)


def esempio(t):
    return '    <div class="esempio">%s</div>' % t


def vf(items):
    """Vero o falso: items = [(frase, True/False)]."""
    return ([{"q": f"{i}. {q}"} for i, (q, _) in enumerate(items, 1)],
            [eq("Vero" if r else "Falso") for _, r in items])


def sc(items):
    """Scelta con opzioni diverse per ogni riga: items = [(domanda, [opzioni], giusta)]."""
    return ([{"q": f"{i}. {q}", "opts": o} for i, (q, o, _) in enumerate(items, 1)],
            [eq(r) for *_, r in items])


def tx(items):
    """Scrivi: items = [(prima, dopo, risposta|altra)]."""
    return ([{"pre": f"{i}. {a}", "post": b} for i, (a, b, _) in enumerate(items, 1)],
            [eq(*r.split("|")) for *_, r in items])


def ex(id, title, short, typ, cons, data, **kw):
    items, k = data
    d = {"id": id, "title": title, "short": short, "type": typ, "cons": cons, "items": items, "k": k}
    d.update(kw)
    return d


VF = ["Vero", "Falso"]

# =====================================================================
# 1. CHE COSA È SUCCESSO?  Cronaca, persone, emozioni
# =====================================================================
U1_SLIDE = [
    cover("📰", "Che cosa è successo?", "Raccontare fatti di cronaca, descrivere le persone, parlare delle emozioni", "Livello B1 · Unità 1"),
    slide("Che cosa impariamo?", cards([
        ("🗞️", "La cronaca", "furto, incidente, arresto, salvataggio"),
        ("⏪", "Raccontare al passato", "passato prossimo, imperfetto, trapassato"),
        ("🧑‍🤝‍🧑", "Descrivere le persone", "aspetto fisico e carattere"),
        ("😮", "Le emozioni", "mi fa paura, sono arrabbiato, che rabbia!")])),
    slide("🗞️ Le parole della cronaca", table([
        ["il furto", "qualcuno ruba una cosa (il ladro)"],
        ["la rapina", "un furto con violenza o con un'arma"],
        ["l'incidente", "due macchine si scontrano, una persona cade…"],
        ["l'arresto", "la polizia prende una persona: l'arresta"],
        ["il salvataggio", "qualcuno salva una persona o un animale"],
        ["il testimone", "una persona che ha visto il fatto"],
        ["la denuncia", "racconti alla polizia un reato (fare denuncia)"]], ["parola", "che cosa vuol dire"])),
    slide("🚓 Chi chiamo?", cards([
        ("🚔", "Polizia / Carabinieri", "furti, rapine, pericolo per le persone"),
        ("🚒", "Vigili del fuoco", "incendi, persone bloccate, alberi caduti"),
        ("🚑", "Ambulanza (118)", "una persona sta male o è ferita"),
        ("👮", "Polizia locale (vigili urbani)", "traffico, multe, problemi in città")]) + "\n" +
        nota("☎️ In Italia il numero unico per le emergenze è il <b>112</b>.")),
    slide("⏪ Passato prossimo o imperfetto?", table([
        ["<b>Passato prossimo</b>: un'azione finita, un fatto", "Ieri sera <b>ho visto</b> un incidente."],
        ["<b>Passato prossimo</b>: azioni una dopo l'altra", "<b>Sono uscito</b>, <b>ho preso</b> l'autobus e <b>sono arrivato</b>."],
        ["<b>Imperfetto</b>: la situazione, la descrizione", "<b>Pioveva</b> e <b>c'era</b> molto traffico."],
        ["<b>Imperfetto</b>: un'abitudine nel passato", "Da bambino <b>andavo</b> sempre al mare."],
        ["<b>Imperfetto + passato prossimo</b>: un'azione interrompe l'altra", "<b>Camminavo</b> quando <b>ho sentito</b> un rumore."]],
        ["quando si usa", "esempio"])),
    slide("⏪ Il trapassato prossimo", '    <p class="lead">Un fatto <b>prima</b> di un altro fatto passato.<br>'
          'Si forma con <b>avevo / ero</b> + participio.</p>\n' +
          esempio("Quando la polizia <b>è arrivata</b>, il ladro <b>era</b> già <b>scappato</b>.<br>"
                  "Ho perso il treno perché <b>avevo dimenticato</b> la sveglia.<br>"
                  "Non sono entrato: <b>avevo lasciato</b> le chiavi in ufficio.") + "\n" +
          table([["io", "avevo mangiato", "ero partito/a"], ["tu", "avevi mangiato", "eri partito/a"],
                 ["lui / lei", "aveva mangiato", "era partito/a"], ["noi", "avevamo mangiato", "eravamo partiti/e"],
                 ["voi", "avevate mangiato", "eravate partiti/e"], ["loro", "avevano mangiato", "erano partiti/e"]],
                ["", "con avere", "con essere"])),
    slide("⏳ Stare per / stare + gerundio", cards([
        ("⏭️", "stare per + infinito", "un'azione che comincia tra poco: <i>Il treno sta per partire.</i>"),
        ("▶️", "stare + gerundio", "un'azione che succede adesso: <i>Il treno sta partendo.</i>")]) + "\n" +
        esempio("Al passato: <b>Stavo per uscire</b> quando ha telefonato Ahmed. · <b>Stavamo mangiando</b> quando è andata via la luce.")),
    slide("🧑‍🤝‍🧑 Descrivere le persone", cards([
        ("👀", "L'aspetto", "alto, basso, magro, robusto · capelli ricci, lisci, corti · la barba, i baffi, gli occhiali"),
        ("👕", "I vestiti", "indossava una giacca di pelle, una felpa con il cappuccio, una gonna a righe"),
        ("👍", "Le qualità", "generoso, affidabile, paziente, simpatico, sincero"),
        ("👎", "I difetti", "pigro, egoista, testardo, permaloso, disordinato")])),
    slide("🐢 Modi di dire con gli animali", table([
        ["testardo come un mulo", "non cambia mai idea"], ["lento come una lumaca", "fa tutto molto lentamente"],
        ["essere un pesce fuor d'acqua", "sentirsi a disagio in un posto nuovo"], ["avere una memoria da elefante", "ricordare tutto"],
        ["essere un orso", "non ama stare con le persone"]], ["espressione", "significato"])),
    slide("😮 Le emozioni", cards([
        ("😨", "La paura", "Mi fa paura il buio. · Ho paura dei cani."),
        ("😡", "La rabbia", "Sono arrabbiato! · Ho un diavolo per capello."),
        ("😢", "La tristezza", "Mi sento giù. · Ho un nodo alla gola."),
        ("😄", "L'allegria", "La musica mi mette allegria. · Sono al settimo cielo!")]) + "\n" +
        nota("Esclamazioni: <b>Accidenti!</b> <b>Cavoli!</b> <b>Che spavento!</b> <b>Meno male!</b>")),
    slide("💬 Mi hanno rubato la borsa!", dialogo([
        ("Agente", "Buongiorno, mi dica. Che cosa è successo?"),
        ("*Fatima", "Mi hanno rubato la borsa sull'autobus 12. C'era tantissima gente."),
        ("Agente", "Ha visto la persona?"),
        ("*Fatima", "Sì, era un ragazzo alto, con una felpa grigia. Quando me ne sono accorta, era già sceso."),
        ("Agente", "Che cosa c'era nella borsa?"),
        ("*Fatima", "Il portafoglio, il permesso di soggiorno e il telefono."),
        ("Agente", "Va bene, facciamo la denuncia. Mi dà un documento, per favore?")])),
    fine("Ora sai raccontare un fatto al passato e descrivere una persona."),
]

U1_NOTIZIA = ("Buongiorno, ecco le notizie della mattina. A Bari, ieri sera, un incendio è scoppiato in un "
              "appartamento di via Napoli. I vigili del fuoco sono arrivati in pochi minuti e hanno salvato "
              "una signora anziana e il suo gatto. Nessuno è rimasto ferito. "
              "A Lecce la polizia ha arrestato due ragazzi che avevano rubato tre biciclette davanti alla stazione. "
              "Un testimone aveva fotografato la targa del loro furgone. "
              "Infine il meteo: oggi cielo nuvoloso, nel pomeriggio arriva la pioggia su tutta la Puglia.")
U1_DIAL = [("F", "Ciao Marco! Che faccia! Che cosa ti è successo?"),
           ("M", "Lascia stare, ieri è stata una giornata terribile. Ero al bar con Luca e avevo lo zaino vicino alla sedia."),
           ("F", "E allora?"),
           ("M", "Mentre parlavamo, è passato un uomo con un cappello nero. Quando mi sono girato, lo zaino non c'era più!"),
           ("F", "Accidenti! E che cosa c'era dentro?"),
           ("M", "Per fortuna il telefono era in tasca. Ma nello zaino c'erano il computer e la patente."),
           ("F", "Hai fatto la denuncia?"),
           ("M", "Sì, sono andato subito dai carabinieri. Mi hanno detto di aspettare. Ero furioso!")]

U1_PPI = sc([
    ("Ieri ___ a casa alle otto.", ["sono tornato", "tornavo"], "sono tornato"),
    ("Da bambina ___ sempre con mia nonna.", ["ho giocato", "giocavo"], "giocavo"),
    ("Mentre ___ la cena, è suonato il telefono.", ["ho preparato", "preparavo"], "preparavo"),
    ("Quando sono uscito, ___ molto freddo.", ["ha fatto", "faceva"], "faceva"),
    ("Sabato scorso ___ un film bellissimo.", ["abbiamo visto", "vedevamo"], "abbiamo visto"),
    ("Il ladro ___ una giacca nera e i jeans.", ["ha indossato", "indossava"], "indossava"),
    ("Ho dormito male perché ___ mal di testa.", ["ho avuto", "avevo"], "avevo"),
    ("Ieri ___ in biblioteca dalle 9 alle 13.", ["ho studiato", "studiavo"], "ho studiato"),
    ("Ogni estate i miei genitori ___ al mare.", ["sono andati", "andavano"], "andavano"),
    ("All'improvviso ___ un forte rumore.", ["abbiamo sentito", "sentivamo"], "abbiamo sentito")])

U1_TRAP = tx([
    ("Quando sono arrivato alla stazione, il treno (partire) già", "", "era partito|era gia partito"),
    ("Non avevo fame perché (mangiare)", "un panino alle cinque.", "avevo mangiato"),
    ("Quando la polizia è arrivata, i ladri (scappare)", ".", "erano scappati|erano gia scappati"),
    ("Maria era stanca perché (lavorare)", "tutta la notte.", "aveva lavorato"),
    ("Abbiamo visto il film che tu ci (consigliare)", ".", "avevi consigliato"),
    ("Non sono entrati perché (dimenticare)", "le chiavi.", "avevano dimenticato"),
    ("Ho ritrovato la borsa che (perdere)", "in autobus.", "avevo perso"),
    ("Quando ho telefonato, voi (uscire)", "già.", "eravate usciti|eravate gia usciti")])

U1_STARE = sc([
    ("Corri! Il film ___.", ["sta per cominciare", "sta cominciando"], "sta per cominciare"),
    ("Non posso rispondere, ___ (adesso, in questo momento).", ["sto per guidare", "sto guidando"], "sto guidando"),
    ("Ero sulla porta: ___ quando hai chiamato.", ["stavo per uscire", "stavo uscendo da un'ora"], "stavo per uscire"),
    ("Silenzio, i bambini ___. Non svegliarli!", ["stanno per dormire", "stanno dormendo"], "stanno dormendo"),
    ("Prendi l'ombrello: ___ piovere.", ["sta per", "sta"], "sta per")])

U1_CARATTERE = sc([
    ("Aiuta sempre tutti e regala le sue cose.", ["generoso", "egoista", "pigro"], "generoso"),
    ("Non vuole mai lavorare, sta sempre sul divano.", ["pigro", "affidabile", "preciso"], "pigro"),
    ("Pensa solo a sé stesso.", ["sincero", "egoista", "paziente"], "egoista"),
    ("Puoi contare su di lui: fa sempre quello che promette.", ["affidabile", "testardo", "permaloso"], "affidabile"),
    ("Non cambia mai idea, anche quando ha torto.", ["testardo", "generoso", "timido"], "testardo"),
    ("Si offende per ogni piccola cosa.", ["permaloso", "simpatico", "allegro"], "permaloso"),
    ("Dice sempre la verità.", ["sincero", "bugiardo", "pigro"], "sincero"),
    ("Aspetta senza nervosismo, anche per molto tempo.", ["paziente", "nervoso", "egoista"], "paziente")])

U1_MODI = sc([
    ("Nella nuova scuola non conosco nessuno: mi sento…", ["un pesce fuor d'acqua", "al settimo cielo"], "un pesce fuor d'acqua"),
    ("Mio nonno ricorda tutti i compleanni: ha…", ["una memoria da elefante", "un diavolo per capello"], "una memoria da elefante"),
    ("Ho vinto la borsa di studio! Sono…", ["al settimo cielo", "testardo come un mulo"], "al settimo cielo"),
    ("Il capo ha urlato tutto il giorno: aveva…", ["un diavolo per capello", "una memoria da elefante"], "un diavolo per capello"),
    ("Quando saluto mia madre all'aeroporto ho…", ["un nodo alla gola", "un pesce fuor d'acqua"], "un nodo alla gola"),
    ("Karim non ascolta nessuno, è…", ["testardo come un mulo", "lento come una lumaca"], "testardo come un mulo")])

U1_CHI = sc([
    ("In cucina c'è un incendio.", ["i vigili del fuoco", "la polizia locale", "l'ambulanza"], "i vigili del fuoco"),
    ("Un uomo è caduto e non si muove.", ["l'ambulanza", "i vigili del fuoco", "la polizia locale"], "l'ambulanza"),
    ("Qualcuno è entrato in casa tua e ha rubato.", ["i carabinieri", "l'ambulanza", "i vigili del fuoco"], "i carabinieri"),
    ("Una macchina è parcheggiata davanti al tuo garage.", ["la polizia locale", "l'ambulanza", "i vigili del fuoco"], "la polizia locale"),
    ("Il tuo vicino anziano è chiuso in casa e non risponde.", ["i vigili del fuoco", "la polizia locale", "nessuno"], "i vigili del fuoco")])

U1_CLOZE = ("Venerdì sera (essere) [ero] a casa da sola. (piovere) [pioveva] forte e (guardare) [guardavo] la TV. "
            "All'improvviso (sentire) [ho sentito] un rumore strano in cucina. (avere) [avevo] paura, ma (prendere) [ho preso] "
            "una scopa e (andare) [sono andata] a vedere. Sul tavolo c'era un piccolo gatto bagnato: (entrare) [era entrato] "
            "dalla finestra che io (lasciare) [avevo lasciato] aperta! Alla fine il gatto (dormire) [ha dormito] con me tutta la notte.")


def cloze(t):
    import re
    p = re.split(r"\[([^\]]+)\]", t)
    return ([x if i % 2 == 0 else {"w": "m"} for i, x in enumerate(p) if x],
            [eq(*x.split("|")) for i, x in enumerate(p) if i % 2])


U1 = {
 "title": "📰 Che cosa è successo? · Esercizi B1",
 "store": "b1-cronaca",
 "sections": [
  {"part": "Ascoltare"},
  ex("e1", "1 · 🎧 Le notizie della mattina", "1 · Ascolto: notizie", "choice",
     "Ascolta il notiziario alla radio. Poi scegli: vero o falso?",
     vf([("L'incendio è scoppiato di notte, a Lecce.", False), ("I vigili del fuoco hanno salvato una signora e un gatto.", True),
         ("Una persona è rimasta ferita.", False), ("La polizia ha arrestato due ragazzi.", True),
         ("I ragazzi avevano rubato delle macchine.", False), ("Un testimone ha fotografato la targa.", True),
         ("Nel pomeriggio piove.", True)]), opts=VF, audio=U1_NOTIZIA),
  ex("e2", "2 · 🎧 Lo zaino di Marco", "2 · Ascolto: dialogo", "choice",
     "Ascolta Marco e la sua amica. Scegli la risposta giusta.",
     sc([("Dov'era Marco?", ["al bar", "in autobus", "a casa"], "al bar"),
         ("Con chi era?", ["con Luca", "con sua sorella", "da solo"], "con Luca"),
         ("Com'era l'uomo?", ["aveva un cappello nero", "era molto basso", "aveva gli occhiali"], "aveva un cappello nero"),
         ("Che cosa NON era nello zaino?", ["il telefono", "il computer", "la patente"], "il telefono"),
         ("Dove è andato dopo?", ["dai carabinieri", "all'ospedale", "in ufficio"], "dai carabinieri"),
         ("Come si sentiva?", ["furioso", "felice", "tranquillo"], "furioso")]), audio=U1_DIAL),
  {"part": "Grammatica"},
  ex("e3", "3 · Passato prossimo o imperfetto?", "3 · Passato o imperfetto", "choice",
     "Scegli la forma giusta. Ricorda: imperfetto per descrivere e per le abitudini, passato prossimo per i fatti.", U1_PPI),
  ex("e4", "4 · Il trapassato prossimo", "4 · Trapassato", "text",
     "Scrivi il verbo tra parentesi al trapassato prossimo (avevo mangiato, ero partito…).", U1_TRAP, w="m"),
  ex("e5", "5 · Stare per o stare + gerundio?", "5 · Stare per", "choice",
     "Scegli la forma giusta.", U1_STARE),
  {"id": "e6", "title": "6 · Una sera di pioggia", "short": "6 · Racconto", "type": "cloze",
   "cons": "Leggi il racconto e scrivi i verbi al passato prossimo, all'imperfetto o al trapassato prossimo.",
   "parts": cloze(U1_CLOZE)[0], "k": cloze(U1_CLOZE)[1]},
  {"part": "Parole"},
  ex("e7", "7 · Com'è questa persona?", "7 · Il carattere", "choice",
     "Leggi la descrizione e scegli l'aggettivo giusto.", U1_CARATTERE),
  ex("e8", "8 · Modi di dire", "8 · Modi di dire", "choice", "Completa la frase con l'espressione giusta.", U1_MODI),
  ex("e9", "9 · Chi chiami?", "9 · Emergenze", "choice", "Che cosa fai? Scegli chi chiamare.", U1_CHI),
  {"part": "Scrivere e parlare"},
  {"id": "e10", "title": "10 ✎ · Una disavventura", "type": "free", "rows": 8,
   "items": ["Racconta una brutta avventura (vera o inventata): dove eri, che tempo faceva, che cosa è successo, come ti sentivi. Scrivi almeno 8 frasi."]},
  {"id": "e11", "title": "11 🎤 · Descrivi una persona", "type": "record",
   "cons": "Premi «Registra» e descrivi una persona che conosci bene: com'è fisicamente, com'è di carattere, che cosa indossa di solito.",
   "items": ["Parla per circa un minuto."]},
 ]
}

# =====================================================================
# 2. IO VORREI ANDARE IN SARDEGNA, MA…  Vacanze, consigli, ipotesi
# =====================================================================
U2_SLIDE = [
    cover("🏖️", "Io vorrei andare in Sardegna, ma…", "Parlare di vacanze, dare consigli, fare ipotesi", "Livello B1 · Unità 2"),
    slide("Che cosa impariamo?", cards([
        ("🧳", "Le vacanze", "mare, montagna, città d'arte"),
        ("💭", "Il condizionale", "vorrei, potresti, dovremmo"),
        ("🔢", "Il pronome ne", "Quanti biglietti? Ne ho due."),
        ("🍝", "Il cibo locale", "piccante, saporito, alla griglia")])),
    slide("⛰️ Mare e montagna", cards([
        ("🏖️", "Al mare", "la spiaggia, la baia, gli scogli, il porto, l'ombrellone, fare il bagno"),
        ("🏔️", "In montagna", "la cima, il sentiero, il bosco, il rifugio, fare trekking, sciare"),
        ("🏛️", "In città", "il centro storico, il museo, la piazza, visitare i monumenti"),
        ("🚆", "Il viaggio", "il binario, il ritardo, la coincidenza, il casello, la coda in autostrada")])),
    slide("💭 Il condizionale presente", table([
        ["io", "parler<b>ei</b>", "prender<b>ei</b>", "partir<b>ei</b>"], ["tu", "parler<b>esti</b>", "prender<b>esti</b>", "partir<b>esti</b>"],
        ["lui / lei", "parler<b>ebbe</b>", "prender<b>ebbe</b>", "partir<b>ebbe</b>"], ["noi", "parler<b>emmo</b>", "prender<b>emmo</b>", "partir<b>emmo</b>"],
        ["voi", "parler<b>este</b>", "prender<b>este</b>", "partir<b>este</b>"], ["loro", "parler<b>ebbero</b>", "prender<b>ebbero</b>", "partir<b>ebbero</b>"]],
        ["", "parlare", "prendere", "partire"]) + "\n" +
        nota("Irregolari: essere → <b>sarei</b> · avere → <b>avrei</b> · andare → <b>andrei</b> · fare → <b>farei</b> · potere → <b>potrei</b> · "
             "dovere → <b>dovrei</b> · volere → <b>vorrei</b> · venire → <b>verrei</b> · stare → <b>starei</b>", "margin-top:14px;")),
    slide("💭 A che cosa serve?", cards([
        ("🙏", "Chiedere con gentilezza", "<i>Potrebbe</i> aiutarmi? <i>Vorrei</i> un biglietto per Lecce."),
        ("🌟", "Un desiderio", "<i>Mi piacerebbe</i> vedere le Dolomiti."),
        ("👉", "Un consiglio", "<i>Dovresti</i> prenotare presto. <i>Al tuo posto</i> andrei in treno."),
        ("🤔", "Un'ipotesi, una notizia non sicura", "Secondo il giornale, domani <i>ci sarebbe</i> sciopero.")]) + "\n" +
        nota("Attenzione: <b>partiremo</b> (futuro, è sicuro) ≠ <b>partiremmo</b> (condizionale, forse). Ascolta la doppia <b>mm</b>!", "margin-top:14px;")),
    slide("🔢 Il pronome NE", '    <p class="lead"><b>Ne</b> sostituisce una quantità o «di + qualcosa».</p>\n' +
          esempio("— Quante valigie porti? — <b>Ne</b> porto <b>due</b>.<br>"
                  "— Hai comprato delle cartoline? — Sì, <b>ne</b> ho comprat<b>e</b> cinque.<br>"
                  "— Hai letto dei libri sulla Puglia? — No, non <b>ne</b> ho letto <b>nessuno</b>.<br>"
                  "— Che cosa pensi di questo albergo? — <b>Ne</b> penso bene. (= di questo albergo)") + "\n" +
          nota("Al passato prossimo il participio si accorda: <b>ne</b> ho mangiat<b>i</b> tre (biscotti) · <b>ne</b> ho mangiat<b>e</b> tre (mele)", "margin-top:14px;")),
    slide("✨ Quello e bello", table([
        ["il → quel / bel", "quel ragazzo · un bel paese"], ["lo → quello / bello", "quello zaino · un bello spettacolo"],
        ["l' → quell' / bell'", "quell'albergo · una bell'isola"], ["la → quella / bella", "quella spiaggia · una bella città"],
        ["i → quei / bei", "quei sentieri · dei bei giorni"], ["gli → quegli / begli", "quegli scogli · dei begli occhi"],
        ["le → quelle / belle", "quelle montagne · delle belle vacanze"]], ["articolo", "esempi"])),
    slide("🔤 Parole nuove da altre parole", cards([
        ("🏠", "-ino / -etto: piccolo", "casa → casetta · locale → localino · paese → paesino"),
        ("🌩️", "-accio: brutto", "tempo → tempaccio · parola → parolaccia"),
        ("💪", "-one: grande", "uomo → omone · libro → librone"),
        ("✅", "-abile / -ibile: si può", "che non si può dimenticare → indimenticabile · che si può vedere → visibile")])),
    slide("🍝 Com'è il piatto?", cards([
        ("🌶️", "piccante", "c'è molto peperoncino"), ("🧂", "insipido / salato", "c'è poco sale / troppo sale"),
        ("🔥", "alla griglia, al forno, fritto", "modi di cucinare"), ("😋", "saporito, gustoso", "ha molto sapore, è buono")], "g2")),
    slide("💬 Dove andiamo quest'estate?", dialogo([
        ("Sara", "Io vorrei andare in Sardegna, ma i traghetti costano tanto."),
        ("*Omar", "Al tuo posto andrei in Salento: è vicino e il mare è bellissimo."),
        ("Sara", "Hai ragione, ma ci sarebbe troppa gente ad agosto."),
        ("*Omar", "Allora dovresti partire a giugno. Potresti prendere una casetta a Otranto."),
        ("Sara", "Buona idea! Quanti giorni ci staresti?"),
        ("*Omar", "Ci starei almeno una settimana. Ne vale la pena!")])),
    fine("Ora sai dare consigli e parlare dei tuoi desideri per le vacanze."),
]

U2_ANNUNCI = [("F", "Annuncio ai viaggiatori. Il treno regionale delle ore 10 e 15 per Lecce partirà dal binario 4 invece che dal binario 2."),
              ("F", "Il treno Frecciarossa per Milano, previsto alle ore 10 e 30, viaggia con un ritardo di 20 minuti. Ci scusiamo per il disagio."),
              ("M", "Notizie dal traffico. Sulla statale 16, tra Bari e Mola, c'è una coda di 5 chilometri per un incidente. "
                    "Consigliamo di uscire al casello di Bari Sud e di prendere la strada provinciale.")]
U2_DIAL = [("M", "Allora, Nadia, hai deciso dove andare ad agosto?"),
           ("F", "Non ancora. Mi piacerebbe andare in montagna, perché al mare fa troppo caldo."),
           ("M", "Hai ragione. Io al tuo posto andrei in Trentino. Ci sono sentieri bellissimi e i rifugi sono economici."),
           ("F", "Sì, ma il viaggio è lungo. Ci vorrebbero almeno dieci ore di treno."),
           ("M", "Potresti prendere l'aereo fino a Verona. Costa poco se prenoti adesso."),
           ("F", "È vero. E poi potrei fare trekking ogni giorno. Quanti giorni ci staresti tu?"),
           ("M", "Io ne starei almeno dieci. Ma porta una giacca: la sera fa freddo!")]

U2_COND = tx([
    ("(io, volere)", "un caffè, per favore.", "vorrei"), ("Tu (dovere)", "riposare di più.", "dovresti"),
    ("(Lei, potere)", "chiudere la finestra?", "potrebbe"), ("Noi (andare)", "volentieri al mare.", "andremmo"),
    ("Mi (piacere)", "vedere Roma.", "piacerebbe"), ("Voi che cosa (fare)", "al mio posto?", "fareste"),
    ("Loro (venire)", "con noi, ma lavorano.", "verrebbero"), ("Al tuo posto io non (comprare)", "quella macchina.", "comprerei"),
    ("Senza di te io non (essere)", "felice.", "sarei"), ("Noi (avere)", "bisogno di un consiglio.", "avremmo")])

U2_FUT = sc([
    ("Domani alle 8 ___ per Napoli: abbiamo già i biglietti.", ["partiremo", "partiremmo"], "partiremo"),
    ("Se avessimo tempo, ___ anche per la Sicilia.", ["partiremo", "partiremmo"], "partiremmo"),
    ("Scusi, ___ un'informazione?", ["mi darà", "mi darebbe"], "mi darebbe"),
    ("L'anno prossimo ___ in una casa nuova: abbiamo già firmato.", ["abiteremo", "abiteremmo"], "abiteremo"),
    ("Sei stanco: ___ andare a dormire.", ["dovrai", "dovresti"], "dovresti"),
    ("Secondo la radio, l'incidente ___ causato da un camion (non è sicuro).", ["sarà stato", "sarebbe stato"], "sarebbe stato")])

U2_NE = tx([
    ("— Quanti fratelli hai? — ", "ho tre.", "ne"),
    ("— Vuoi delle ciliegie? — Sì, ne vorrei", "chilo (1).", "un"),
    ("— Quante foto hai fatto? — Ne ho fatt", "cento!", "e"),
    ("— Quanti panini hai mangiato? — Ne ho mangiat", "due.", "i"),
    ("— Hai degli amici a Bari? — No, non ne ho", ".", "nessuno"),
    ("— Che cosa pensi del film? — ", "penso tutto il bene possibile.", "ne"),
    ("— Quanto zucchero metti? — Ne metto", ".", "poco|un po'|un cucchiaino")])

U2_QB = sc([
    ("Guarda ___ montagne!", ["quelle", "quei", "quegli"], "quelle"),
    ("Ti piace ___ albergo?", ["quell'", "quello", "quel"], "quell'"),
    ("Ho visto un ___ film.", ["bel", "bello", "bell'"], "bel"),
    ("Chi sono ___ studenti?", ["quegli", "quei", "quelli"], "quegli"),
    ("Abbiamo passato dei ___ giorni in Calabria.", ["bei", "begli", "belli"], "bei"),
    ("Siamo andati in ___ spiaggia vicino al porto.", ["quella", "quel", "quell'"], "quella"),
    ("Che ___ zaino!", ["bello", "bel", "bell'"], "bello"),
    ("Non mi piacciono ___ ristoranti per turisti.", ["quei", "quegli", "quelle"], "quei")])

U2_PAROLE = tx([
    ("Una casa piccola e carina: una", "", "casetta|casina"), ("Un paese piccolo: un", "", "paesino|paesetto"),
    ("Un tempo molto brutto: un", "", "tempaccio"), ("Un uomo grande e grosso: un", "", "omone"),
    ("Una vacanza che non si può dimenticare: una vacanza", "", "indimenticabile"),
    ("Un'acqua che si può bere: acqua", "", "potabile"), ("Una cosa che non si può credere: una cosa", "", "incredibile"),
    ("Un sentiero che si può percorrere: un sentiero", "", "percorribile")])

U2_CIBO = sc([
    ("C'è troppo peperoncino: è…", ["piccante", "insipido", "dolce"], "piccante"),
    ("Non hai messo il sale: è…", ["insipido", "salato", "piccante"], "insipido"),
    ("Il pesce cotto sul fuoco, sulla griglia: è…", ["alla griglia", "fritto", "crudo"], "alla griglia"),
    ("Le patate cotte nell'olio bollente sono…", ["fritte", "al forno", "lesse"], "fritte"),
    ("Le orecchiette con le cime di rapa sono un piatto tipico…", ["pugliese", "siciliano", "veneto"], "pugliese")])

U2 = {
 "title": "🏖️ Io vorrei andare in Sardegna, ma… · Esercizi B1",
 "store": "b1-vacanze",
 "sections": [
  {"part": "Ascoltare"},
  ex("e1", "1 · 🎧 Annunci e traffico", "1 · Ascolto: annunci", "choice",
     "Ascolta gli annunci in stazione e le notizie dal traffico. Scegli la risposta giusta.",
     sc([("Il regionale per Lecce parte alle…", ["10:15", "10:30", "10:50"], "10:15"),
         ("Da quale binario parte?", ["binario 4", "binario 2", "binario 14"], "binario 4"),
         ("Il Frecciarossa va a…", ["Milano", "Roma", "Lecce"], "Milano"),
         ("Quanti minuti di ritardo?", ["20", "10", "30"], "20"),
         ("Quanti chilometri di coda sulla statale 16?", ["5", "15", "2"], "5"),
         ("Perché c'è la coda?", ["per un incidente", "per i lavori", "per la neve"], "per un incidente")]), audio=U2_ANNUNCI),
  ex("e2", "2 · 🎧 Mare o montagna?", "2 · Ascolto: dialogo", "choice",
     "Ascolta Nadia e il suo amico. Vero o falso?",
     vf([("Nadia ha già deciso dove andare.", False), ("Nadia vorrebbe andare in montagna.", True),
         ("L'amico consiglia la Sardegna.", False), ("In treno il viaggio è lungo.", True),
         ("L'amico consiglia di prendere l'aereo fino a Verona.", True), ("L'amico ci starebbe cinque giorni.", False),
         ("La sera in montagna fa freddo.", True)]), opts=VF, audio=U2_DIAL),
  {"part": "Grammatica"},
  ex("e3", "3 · Il condizionale presente", "3 · Condizionale", "text",
     "Scrivi il verbo tra parentesi al condizionale presente.", U2_COND, w="m"),
  ex("e4", "4 · Futuro o condizionale?", "4 · Futuro o condizionale", "choice",
     "Scegli la forma giusta: il futuro è sicuro, il condizionale è un desiderio, un consiglio o una cosa non sicura.", U2_FUT),
  ex("e5", "5 · Il pronome NE", "5 · Ne", "text",
     "Completa. Attenzione all'accordo del participio (ne ho mangiati, ne ho fatte).", U2_NE, w="s"),
  ex("e6", "6 · Quello e bello", "6 · Quello e bello", "choice", "Scegli la forma giusta.", U2_QB),
  {"part": "Parole"},
  ex("e7", "7 · Parole nuove da altre parole", "7 · Suffissi", "text",
     "Scrivi la parola giusta con -ino, -etto, -accio, -one, -abile o -ibile.", U2_PAROLE, w="m"),
  ex("e8", "8 · A tavola", "8 · Il cibo", "choice", "Scegli la parola giusta.", U2_CIBO),
  {"part": "Scrivere e parlare"},
  {"id": "e9", "title": "9 ✎ · Dai un consiglio", "type": "free", "rows": 7,
   "items": ["Un amico arriva in Puglia per una settimana a luglio. Scrivigli un messaggio con almeno 5 consigli: dove dovrebbe andare, che cosa potrebbe mangiare, come potrebbe viaggiare. Usa il condizionale (dovresti, potresti, al tuo posto andrei…)."]},
  {"id": "e10", "title": "10 🎤 · La vacanza dei sogni", "type": "record",
   "cons": "Premi «Registra» e racconta: dove ti piacerebbe andare in vacanza? Con chi? Che cosa faresti?",
   "items": ["Parla per circa un minuto."]},
 ]
}

# =====================================================================
# 3. SU DAI, USCIAMO!  Tempo libero, opinioni, social
# =====================================================================
U3_SLIDE = [
    cover("🎬", "Su dai, usciamo!", "Il tempo libero, lo sport, gli spettacoli, i social. Dire che cosa pensi.", "Livello B1 · Unità 3"),
    slide("Che cosa impariamo?", cards([
        ("📱", "I social media", "condividere, mettere «mi piace», seguire"),
        ("💭", "Dare un'opinione", "Penso che sia… Mi sembra che abbia…"),
        ("🔁", "Me lo, te lo, ce lo", "i pronomi combinati"),
        ("🏆", "Migliore, peggiore", "comparativi e superlativi")])),
    slide("📱 Internet e social", cards([
        ("🌐", "navigare in internet", "cercare informazioni, guardare video"),
        ("📸", "condividere / postare", "una foto, una storia, un video"),
        ("👍", "mettere «mi piace»", "commentare, seguire una persona"),
        ("🔔", "le notifiche", "il telefono suona sempre: dipendenza dal cellulare?")])),
    slide("🎟️ Uscire e divertirsi", cards([
        ("🎸", "Il concerto", "il cantante, il gruppo, il palco, i biglietti esauriti"),
        ("🎬", "Il cinema", "il film d'azione, la commedia, la scena, la colonna sonora, avvincente"),
        ("🖼️", "La mostra", "il museo, i quadri, le foto"),
        ("⚽", "Lo sport", "la partita, la squadra, tifare per…, vincere, perdere, pareggiare")])),
    slide("💭 Il congiuntivo: essere e avere", table([
        ["che io", "sia", "abbia"], ["che tu", "sia", "abbia"], ["che lui / lei", "sia", "abbia"],
        ["che noi", "siamo", "abbiamo"], ["che voi", "siate", "abbiate"], ["che loro", "siano", "abbiano"]], ["", "essere", "avere"]) + "\n" +
        nota("Dopo <b>penso che, credo che, mi sembra che, mi pare che</b> si usa il <b>congiuntivo</b>:<br>"
             "Penso che il film <b>sia</b> noioso. · Mi sembra che Ali <b>abbia</b> ragione.", "margin-top:14px;")),
    slide("💭 Opinione o certezza?", cards([
        ("🤔", "Opinione → congiuntivo", "Credo che domani <b>sia</b> festa. · Non penso che <b>abbiano</b> tempo."),
        ("✅", "Certezza → indicativo", "So che domani <b>è</b> festa. · Sono sicuro che <b>hanno</b> tempo."),
        ("🙋", "Secondo me + indicativo", "Secondo me, il concerto <b>è</b> troppo caro."),
        ("🔀", "Stessa persona → di + infinito", "Penso <b>di</b> uscire stasera. (io penso, io esco)")])),
    slide("🔁 I pronomi combinati", '    <p class="lead">Un pronome indiretto + <b>lo, la, li, le, ne</b>.</p>\n' +
          table([["mi", "me lo · me la · me li · me le · me ne"], ["ti", "te lo · te la · te li · te le · te ne"],
                 ["ci", "ce lo · ce la · ce li · ce le · ce ne"], ["vi", "ve lo · ve la · ve li · ve le · ve ne"],
                 ["gli / le", "glielo · gliela · glieli · gliele · gliene"]], ["", "+ lo, la, li, le, ne"]) + "\n" +
          esempio("— Mi presti il libro? — Sì, <b>te lo</b> presto. · — Ci mandi le foto? — Sì, <b>ve le</b> mando stasera.")),
    slide("🏆 Comparativi e superlativi", table([
        ["buono", "più buono / <b>migliore</b>", "il migliore · buonissimo / <b>ottimo</b>"],
        ["cattivo", "più cattivo / <b>peggiore</b>", "il peggiore · cattivissimo / <b>pessimo</b>"],
        ["grande", "più grande / <b>maggiore</b>", "il maggiore · grandissimo / <b>massimo</b>"],
        ["piccolo", "più piccolo / <b>minore</b>", "il minore · piccolissimo / <b>minimo</b>"]], ["", "comparativo", "superlativo"]) + "\n" +
        esempio("Questa pizza è <b>migliore</b> di quella. · Mio fratello <b>maggiore</b> vive a Torino. · È il film <b>più bello</b> dell'anno.")),
    slide("🔗 Che e chi", cards([
        ("👉", "che", "unisce due frasi: <i>Il ragazzo <b>che</b> suona la chitarra è mio cugino.</i>"),
        ("🙋", "chi = la persona che", "<i><b>Chi</b> arriva tardi non entra.</i> · <i><b>Chi</b> dorme non piglia pesci.</i> (proverbio)")])),
    slide("💬 Dai, vieni al concerto!", dialogo([
        ("Lucia", "Sabato c'è il concerto in piazza. Dai, vieni con noi!"),
        ("*Samir", "Non so… penso che sia pieno di gente."),
        ("Lucia", "Ma dai! È gratis e la musica è bellissima. Credo che ci siano anche i tuoi colleghi."),
        ("*Samir", "Davvero? Allora magari vengo. Mi mandi l'indirizzo?"),
        ("Lucia", "Certo, te lo mando su WhatsApp."),
        ("*Samir", "Va bene, ci vediamo sabato!")])),
    fine("Ora sai dare la tua opinione e convincere un amico a uscire."),
]

U3_DIAL = [("F", "Ehi Ahmed, che fai stasera? Usciamo?"),
           ("M", "Mah, sono stanco. Penso di restare a casa a guardare una serie."),
           ("F", "Ancora? Dai, sei sempre sul divano con il telefono! C'è un film nuovo al cinema Galleria."),
           ("M", "Che tipo di film?"),
           ("F", "Un film d'azione, molto avvincente. Dicono che sia il migliore dell'anno."),
           ("M", "Mmm, a che ora comincia?"),
           ("F", "Alle nove e mezza. Prima possiamo mangiare una pizza vicino al teatro Petruzzelli."),
           ("M", "Va bene, mi hai convinto! Però i biglietti li compri tu, io ti offro la pizza.")]
U3_INTERV = [("M", "Oggi parliamo di giovani e cellulare. Giulia, tu quante ore al giorno usi il telefono?"),
             ("F", "Troppe, purtroppo! Credo almeno cinque ore. Soprattutto per i social e per la musica."),
             ("M", "E pensi che sia un problema?"),
             ("F", "Un po' sì. A volte esco con gli amici e tutti guardano il telefono invece di parlare. "
                   "Per questo il sabato lo spengo e vado a giocare a pallavolo.")]

U3_CONG = tx([
    ("Penso che Marta (essere)", "a casa.", "sia"), ("Credo che voi (avere)", "ragione.", "abbiate"),
    ("Mi sembra che i biglietti (essere)", "esauriti.", "siano"), ("Non penso che loro (avere)", "tempo.", "abbiano"),
    ("Mi pare che tu (essere)", "stanco.", "sia"), ("Credo che noi (avere)", "un problema.", "abbiamo"),
    ("Penso che il concerto (essere)", "alle nove.", "sia"), ("Mi sembra che Omar (avere)", "la febbre.", "abbia")])

U3_IND = sc([
    ("So che il museo ___ chiuso il lunedì.", ["è", "sia"], "è"),
    ("Penso che il museo ___ chiuso il lunedì.", ["è", "sia"], "sia"),
    ("Secondo me Ali ___ ragione.", ["ha", "abbia"], "ha"),
    ("Mi sembra che Ali ___ ragione.", ["ha", "abbia"], "abbia"),
    ("Sono sicura che voi ___ bravissimi.", ["siete", "siate"], "siete"),
    ("Penso ___ andare al cinema stasera.", ["di", "che"], "di"),
    ("Credo ___ tu abbia bisogno di riposo.", ["che", "di"], "che")])

U3_COMB = tx([
    ("— Mi presti la bici? — Sì,", "presto.", "te la"), ("— Ci mandi le foto? — Sì,", "mando.", "ve le"),
    ("— Mi compri i biglietti? — Sì,", "compro io.", "te li"), ("— Ti ha detto la verità? — Sì,", "ha detta.", "me l'|me la"),
    ("— Ci prepari il caffè? — Sì,", "preparo subito.", "ve lo"), ("— Mi dai un consiglio? — Sì,", "do volentieri.", "te lo"),
    ("— Vi hanno spiegato le regole? — Sì,", "hanno spiegate.", "ce le")])

U3_COMP = sc([
    ("Questa pizza è buonissima, è la ___ di Bari!", ["migliore", "peggiore", "maggiore"], "migliore"),
    ("Mia sorella ___ ha 30 anni, io ne ho 25.", ["maggiore", "minore", "migliore"], "maggiore"),
    ("Il tempo è bruttissimo: è ___.", ["pessimo", "ottimo", "massimo"], "pessimo"),
    ("Il film di ieri era ___ di questo: mi è piaciuto di più.", ["migliore", "peggiore", "minore"], "migliore"),
    ("Mio fratello ___ va ancora a scuola.", ["minore", "maggiore", "peggiore"], "minore"),
    ("Questo è il ___ ristorante del quartiere: si mangia malissimo!", ["peggiore", "migliore", "massimo"], "peggiore")])

U3_REL = sc([
    ("Il ragazzo ___ ho conosciuto ieri si chiama Jamal.", ["che", "chi"], "che"),
    ("___ vuole venire alla festa deve portare qualcosa da mangiare.", ["Chi", "Che"], "Chi"),
    ("La serie ___ guardo adesso è spagnola.", ["che", "chi"], "che"),
    ("___ dorme non piglia pesci.", ["Chi", "Che"], "Chi"),
    ("Ho perso il telefono ___ mi hai regalato.", ["che", "chi"], "che")])

U3_LESS = sc([
    ("Metto una foto su Instagram: la…", ["condivido", "scarico", "spengo"], "condivido"),
    ("I biglietti per il concerto non ci sono più: sono…", ["esauriti", "gratuiti", "scontati"], "esauriti"),
    ("La musica di un film è la…", ["colonna sonora", "scena", "trama"], "colonna sonora"),
    ("Un film che ti tiene attento fino alla fine è…", ["avvincente", "noioso", "lento"], "avvincente"),
    ("Sono un tifoso del Bari: ___ per il Bari.", ["tifo", "gioco", "vinco"], "tifo"),
    ("La partita è finita 1 a 1: le squadre hanno…", ["pareggiato", "vinto", "perso"], "pareggiato")])

U3 = {
 "title": "🎬 Su dai, usciamo! · Esercizi B1",
 "store": "b1-tempo-libero",
 "sections": [
  {"part": "Ascoltare"},
  ex("e1", "1 · 🎧 Usciamo stasera?", "1 · Ascolto: invito", "choice",
     "Ascolta Ahmed e la sua amica. Scegli la risposta giusta.",
     sc([("Che cosa voleva fare Ahmed?", ["restare a casa", "andare a ballare", "fare sport"], "restare a casa"),
         ("Dove propone di andare l'amica?", ["al cinema", "a teatro", "allo stadio"], "al cinema"),
         ("Che film è?", ["un film d'azione", "una commedia", "un documentario"], "un film d'azione"),
         ("A che ora comincia?", ["alle 21:30", "alle 20:00", "alle 22:30"], "alle 21:30"),
         ("Che cosa fanno prima?", ["mangiano una pizza", "prendono un aperitivo", "vanno a teatro"], "mangiano una pizza"),
         ("Chi paga la pizza?", ["Ahmed", "l'amica", "pagano insieme"], "Ahmed")]), audio=U3_DIAL),
  ex("e2", "2 · 🎧 Giovani e cellulare", "2 · Ascolto: intervista", "choice",
     "Ascolta l'intervista a Giulia. Vero o falso?",
     vf([("Giulia usa il telefono circa cinque ore al giorno.", True), ("Lo usa soprattutto per studiare.", False),
         ("Pensa che sia un po' un problema.", True), ("Con gli amici parlano sempre molto.", False),
         ("Il sabato spegne il telefono.", True), ("Gioca a calcio.", False)]), opts=VF, audio=U3_INTERV),
  {"part": "Grammatica"},
  ex("e3", "3 · Congiuntivo di essere e avere", "3 · Congiuntivo", "text",
     "Scrivi il verbo al congiuntivo presente.", U3_CONG, w="s"),
  ex("e4", "4 · Opinione o certezza?", "4 · Indicativo o congiuntivo", "choice", "Scegli la forma giusta.", U3_IND),
  ex("e5", "5 · I pronomi combinati", "5 · Pronomi combinati", "text",
     "Rispondi con il pronome combinato giusto (te lo, ve le, ce li…).", U3_COMB, w="s"),
  ex("e6", "6 · Migliore o peggiore?", "6 · Comparativi", "choice", "Scegli la parola giusta.", U3_COMP),
  ex("e7", "7 · Che o chi?", "7 · Che o chi", "choice", "Scegli il pronome relativo giusto.", U3_REL),
  {"part": "Parole"},
  ex("e8", "8 · Tempo libero e social", "8 · Lessico", "choice", "Scegli la parola giusta.", U3_LESS),
  {"part": "Scrivere e parlare"},
  {"id": "e9", "title": "9 ✎ · Selfie sempre?", "type": "free", "rows": 7,
   "items": ["Che cosa pensi dei selfie e dei social? Scrivi la tua opinione in almeno 6 frasi. Usa: penso che, mi sembra che, secondo me, invece."]},
  {"id": "e10", "title": "10 🎤 · Convinci un amico", "type": "record",
   "cons": "Il tuo amico non vuole mai uscire. Premi «Registra» e convincilo a venire con te a una festa o a una partita.",
   "items": ["Parla per circa un minuto. Usa: dai!, vieni anche tu, ti piacerà, penso che sia…"]},
 ]
}

# =====================================================================
# 4. COME HA SAPUTO DI QUESTO LAVORO?  Lavoro, colloquio, email formale
# =====================================================================
U4_SLIDE = [
    cover("💼", "Come ha saputo di questo lavoro?", "Annunci, colloqui, qualità personali, l'e-mail formale", "Livello B1 · Unità 4"),
    slide("Che cosa impariamo?", cards([
        ("📋", "Gli annunci di lavoro", "requisiti, contratto, retribuzione"),
        ("🤝", "Il colloquio", "parlare delle proprie esperienze"),
        ("💭", "Il congiuntivo presente", "spero che tu trovi lavoro"),
        ("✉️", "L'e-mail formale", "Gentile…, Cordiali saluti")])),
    slide("📋 Leggere un annuncio", table([
        ["si richiede / requisiti", "che cosa deve sapere o avere il candidato"],
        ["esperienza pluriennale", "esperienza di più anni"], ["automunito", "con la macchina propria"],
        ["full-time / part-time", "tempo pieno / tempo parziale"], ["contratto a tempo determinato", "con una data di fine"],
        ["retribuzione", "lo stipendio, quanto si guadagna"], ["inviare il CV a…", "mandare il curriculum"]], ["nell'annuncio", "vuol dire"])),
    slide("👩‍🔧 I nomi dei mestieri", table([
        ["-tore → -trice", "il lavoratore → la lavoratrice · l'attore → l'attrice"],
        ["-ista (uguale)", "il / la barista · il / la giornalista · il / la farmacista"],
        ["-aio → -aia", "il fornaio → la fornaia · il giornalaio → la giornalaia"],
        ["-iere → -iera", "l'infermiere → l'infermiera · il cameriere → la cameriera"],
        ["-ante / -ente (uguale)", "l'insegnante · l'assistente · il / la cantante"]], ["fine", "maschile → femminile"])),
    slide("⭐ Le qualità sul lavoro", table([
        ["preciso", "la precisione"], ["flessibile", "la flessibilità"], ["puntuale", "la puntualità"],
        ["paziente", "la pazienza"], ["chiaro", "la chiarezza"], ["gentile", "la gentilezza"],
        ["competente", "la competenza"], ["responsabile", "la responsabilità"]], ["aggettivo", "nome"]) + "\n" +
        nota("Il contrario: capace ≠ <b>in</b>capace · preparato ≠ <b>im</b>preparato · organizzato ≠ <b>dis</b>organizzato", "margin-top:14px;")),
    slide("💭 Il congiuntivo presente", table([
        ["che io", "lavor<b>i</b>", "scriv<b>a</b>", "dorm<b>a</b>", "cap<b>isca</b>"],
        ["che tu", "lavor<b>i</b>", "scriv<b>a</b>", "dorm<b>a</b>", "cap<b>isca</b>"],
        ["che lui / lei", "lavor<b>i</b>", "scriv<b>a</b>", "dorm<b>a</b>", "cap<b>isca</b>"],
        ["che noi", "lavor<b>iamo</b>", "scriv<b>iamo</b>", "dorm<b>iamo</b>", "cap<b>iamo</b>"],
        ["che voi", "lavor<b>iate</b>", "scriv<b>iate</b>", "dorm<b>iate</b>", "cap<b>iate</b>"],
        ["che loro", "lavor<b>ino</b>", "scriv<b>ano</b>", "dorm<b>ano</b>", "cap<b>iscano</b>"]],
        ["", "lavorare", "scrivere", "dormire", "capire"]) + "\n" +
        nota("Si usa dopo: <b>spero che, voglio che, è importante che, è meglio che, penso che</b>.", "margin-top:14px;")),
    slide("🔀 Di + infinito o che + congiuntivo?", cards([
        ("👤", "Stessa persona → di + infinito", "<i>(Io) spero <b>di trovare</b> lavoro.</i>"),
        ("👥", "Persone diverse → che + congiuntivo", "<i>(Io) spero che <b>tu trovi</b> lavoro.</i>")]) + "\n" +
        esempio("Il direttore vuole <b>che</b> i dipendenti <b>arrivino</b> puntuali. · Decido <b>di</b> mandare il CV. · Provo <b>a</b> chiamare l'ufficio.")),
    slide("🔗 I pronomi relativi: che e cui", cards([
        ("👉", "che", "<i>L'azienda <b>che</b> cerca personale è a Modugno.</i>"),
        ("📍", "preposizione + cui", "<i>L'ufficio <b>in cui</b> lavoro · Il collega <b>con cui</b> parlo · La ditta <b>per cui</b> lavoro</i>"),
        ("📝", "il quale / la quale", "più formale: <i>La signora <b>alla quale</b> ho scritto…</i>")])),
    slide("✉️ L'e-mail formale", table([
        ["Apertura", "Gentile dottoressa Rossi, / Spettabile Ditta,"],
        ["Il motivo", "Le scrivo con riferimento all'annuncio pubblicato su…"],
        ["Presentarsi", "Mi chiamo… e ho esperienza come…"],
        ["Allegati", "In allegato Le invio il mio curriculum vitae."],
        ["Chiusura", "In attesa di un Suo cortese riscontro, porgo cordiali saluti."],
        ["Firma", "Nome e cognome, numero di telefono"]], ["parte", "esempio"])),
    slide("💬 Il colloquio", dialogo([
        ("Selezionatrice", "Buongiorno, si accomodi. Come ha saputo di questo lavoro?"),
        ("*Moussa", "Ho visto il vostro annuncio sul sito del Centro per l'impiego."),
        ("Selezionatrice", "Che esperienza ha come magazziniere?"),
        ("*Moussa", "Ho lavorato per tre anni in un magazzino a Bari. Ho il patentino per il muletto."),
        ("Selezionatrice", "Bene. È importante che Lei sia flessibile con gli orari. Per Lei va bene?"),
        ("*Moussa", "Sì, nessun problema. Sono anche automunito."),
        ("Selezionatrice", "Perfetto. Speriamo di risponderLe entro una settimana.")])),
    fine("Ora sai leggere un annuncio, fare un colloquio e scrivere un'e-mail formale."),
]

U4_DIAL = [("F", "Buongiorno, signor Diallo. Si accomodi pure. Come ha saputo di questo lavoro?"),
           ("M", "Buongiorno. Me ne ha parlato un amico che lavora qui in cucina."),
           ("F", "Ah, bene. Mi parli delle sue esperienze."),
           ("M", "Ho lavorato due anni come aiuto cuoco in un ristorante a Monopoli. Prima facevo il cameriere in un albergo."),
           ("F", "Quali sono le sue qualità?"),
           ("M", "Sono preciso e puntuale. E mi piace lavorare in gruppo."),
           ("F", "Il contratto è di sei mesi, part-time, dal martedì alla domenica. Il lunedì è il giorno libero. Per Lei va bene?"),
           ("M", "Sì, va benissimo."),
           ("F", "Perfetto. Le faremo sapere entro venerdì.")]

U4_ANNUNCIO = ('<p><b>Supermercato a Bari cerca addetto/a al reparto frutta e verdura.</b></p>'
               '<p>Si richiede: esperienza di almeno un anno, disponibilità a lavorare nei fine settimana, buona conoscenza della lingua italiana. '
               'Preferibilmente automunito/a.</p>'
               '<p>Si offre: contratto a tempo determinato di 12 mesi, part-time 30 ore settimanali, retribuzione secondo il contratto nazionale.</p>'
               '<p>Inviare il CV a lavoro@esempio.it entro il 30 novembre.</p>')

U4_FEM = tx([
    ("il cameriere → la", "", "cameriera"), ("il lavoratore → la", "", "lavoratrice"), ("il fornaio → la", "", "fornaia"),
    ("il farmacista → la", "", "farmacista"), ("l'infermiere → l'", "", "infermiera"), ("l'insegnante (m.) → l'", "", "insegnante"),
    ("l'attore → l'", "", "attrice"), ("il direttore → la", "", "direttrice")])

U4_NOMI = tx([
    ("preciso → la", "", "precisione"), ("flessibile → la", "", "flessibilita"), ("paziente → la", "", "pazienza"),
    ("gentile → la", "", "gentilezza"), ("puntuale → la", "", "puntualita"), ("competente → la", "", "competenza"),
    ("chiaro → la", "", "chiarezza"), ("responsabile → la", "", "responsabilita")])

U4_CONG = tx([
    ("Spero che tu (trovare)", "presto un lavoro.", "trovi"), ("È importante che voi (arrivare)", "puntuali.", "arriviate"),
    ("Il capo vuole che noi (finire)", "entro le sei.", "finiamo"), ("Penso che Amina (scrivere)", "bene l'italiano.", "scriva"),
    ("È meglio che loro (partire)", "presto.", "partano"), ("Spero che il direttore (leggere)", "il mio CV.", "legga"),
    ("Credo che i clienti (capire)", "il problema.", "capiscano"), ("Voglio che tu (dormire)", "di più.", "dorma")])

U4_DICHE = sc([
    ("Spero ___ trovare un lavoro vicino a casa.", ["di", "che"], "di"),
    ("Spero ___ tu trovi un lavoro vicino a casa.", ["che", "di"], "che"),
    ("Ho deciso ___ fare un corso di cucina.", ["di", "a"], "di"),
    ("Proverò ___ chiamare l'ufficio domani.", ["a", "di"], "a"),
    ("Il direttore vuole ___ tutti indossino la divisa.", ["che", "di"], "che"),
    ("Penso ___ cambiare lavoro l'anno prossimo.", ["di", "che"], "di")])

U4_CUI = sc([
    ("L'azienda ___ lavoro è molto grande.", ["per cui", "che", "chi"], "per cui"),
    ("Il collega ___ parlo di più è Antonio.", ["con cui", "che", "di che"], "con cui"),
    ("Il magazzino ___ ho fatto il tirocinio è a Modugno.", ["in cui", "che", "cui"], "in cui"),
    ("La signora ___ mi ha chiamato è la responsabile.", ["che", "cui", "in cui"], "che"),
    ("Questo è il corso ___ ti ho parlato.", ["di cui", "che", "con cui"], "di cui"),
    ("Le persone ___ ho mandato il CV non hanno risposto.", ["a cui", "che", "di cui"], "a cui")])

U4_GLI = tx([
    ("— Hai dato il CV al direttore? — Sì,", "ho dato ieri.", "gliel'|glielo"),
    ("— Hai spiegato le regole a Omar? — Sì,", "ho spiegate.", "gliele"),
    ("— Mandi la lettera alla signora Rossi? — Sì,", "mando oggi.", "gliela"),
    ("— Hai portato i documenti a Fatima? — Sì,", "ho portati.", "glieli"),
    ("— Hai parlato del contratto al capo? — Sì,", "ho parlato.", "gliene")])

U4_MAIL = sc([
    ("Inizio di un'e-mail al direttore:", ["Gentile direttore,", "Ciao direttore!", "Ehi!"], "Gentile direttore,"),
    ("Per scrivere a un'azienda:", ["Spettabile Ditta,", "Cara Ditta,", "Salve gente,"], "Spettabile Ditta,"),
    ("Il motivo dell'e-mail:", ["Le scrivo con riferimento all'annuncio…", "Ti scrivo per l'annuncio…", "Allora, l'annuncio…"],
     "Le scrivo con riferimento all'annuncio…"),
    ("Il curriculum:", ["In allegato Le invio il mio curriculum.", "Ti mando il CV, guardalo!", "Ecco il CV."],
     "In allegato Le invio il mio curriculum."),
    ("La chiusura:", ["Cordiali saluti", "Un bacio", "A presto, ciao"], "Cordiali saluti")])

U4 = {
 "title": "💼 Come ha saputo di questo lavoro? · Esercizi B1",
 "store": "b1-lavoro",
 "sections": [
  {"part": "Ascoltare e leggere"},
  ex("e1", "1 · 🎧 Il colloquio in ristorante", "1 · Ascolto: colloquio", "choice",
     "Ascolta il colloquio di lavoro. Scegli la risposta giusta.",
     sc([("Come ha saputo del lavoro il signor Diallo?", ["da un amico", "da un annuncio online", "dal Centro per l'impiego"], "da un amico"),
         ("Dove ha lavorato come aiuto cuoco?", ["a Monopoli", "a Bari", "a Lecce"], "a Monopoli"),
         ("Per quanti anni?", ["due", "tre", "sei"], "due"),
         ("Quali qualità dice di avere?", ["preciso e puntuale", "creativo e simpatico", "veloce e paziente"], "preciso e puntuale"),
         ("Il contratto è…", ["di sei mesi, part-time", "a tempo indeterminato", "di un anno, full-time"], "di sei mesi, part-time"),
         ("Il giorno libero è…", ["il lunedì", "la domenica", "il martedì"], "il lunedì")]), audio=U4_DIAL),
  ex("e2", "2 · Leggi l'annuncio", "2 · Lettura: annuncio", "choice",
     "Leggi l'annuncio. Vero o falso?",
     vf([("Il lavoro è nel reparto frutta e verdura.", True), ("Non serve esperienza.", False),
         ("Bisogna lavorare anche il sabato e la domenica.", True), ("Avere la macchina è obbligatorio.", False),
         ("Il contratto è a tempo indeterminato.", False), ("Si lavora 30 ore alla settimana.", True),
         ("Si può mandare il CV fino al 30 novembre.", True)]), opts=VF, info=U4_ANNUNCIO),
  {"part": "Parole"},
  ex("e3", "3 · Al femminile", "3 · Mestieri", "text", "Scrivi il nome del mestiere al femminile.", U4_FEM, w="m"),
  ex("e4", "4 · Le qualità", "4 · Qualità", "text", "Scrivi il nome che viene dall'aggettivo.", U4_NOMI, w="m"),
  {"part": "Grammatica"},
  ex("e5", "5 · Il congiuntivo presente", "5 · Congiuntivo", "text",
     "Scrivi il verbo al congiuntivo presente.", U4_CONG, w="s"),
  ex("e6", "6 · Di, a o che?", "6 · Di o che", "choice", "Scegli la parola giusta.", U4_DICHE),
  ex("e7", "7 · Che o cui?", "7 · Relativi", "choice", "Scegli il pronome relativo giusto.", U4_CUI),
  ex("e8", "8 · Glielo, gliela…", "8 · Pronomi combinati", "text",
     "Rispondi con il pronome combinato giusto (glielo, gliela, glieli, gliele, gliene).", U4_GLI, w="s"),
  ex("e9", "9 · Formale o informale?", "9 · E-mail formale", "choice",
     "Stai scrivendo un'e-mail per un lavoro. Scegli la frase giusta.", U4_MAIL),
  {"part": "Scrivere e parlare"},
  {"id": "e10", "title": "10 ✎ · La tua e-mail di presentazione", "type": "free", "rows": 10,
   "items": ["Rispondi all'annuncio del supermercato (esercizio 2). Scrivi un'e-mail formale: apertura, il motivo, chi sei e che esperienza hai, l'allegato, la chiusura."]},
  {"id": "e11", "title": "11 🎤 · Il colloquio", "type": "record",
   "cons": "Premi «Registra» e rispondi come in un colloquio di lavoro.",
   "items": ["1. Mi parli delle sue esperienze di lavoro.", "2. Quali sono le sue qualità? E i suoi difetti?",
             "3. Perché vuole lavorare con noi?"]},
 ]
}

# =====================================================================
# 5. CHE PROBLEMA C'È?  Convivenza, lamentele, volontariato
# =====================================================================
U5_SLIDE = [
    cover("🏘️", "Che problema c'è?", "Vicini, coinquilini, famiglia, quartiere. Lamentarsi e spiegare le proprie ragioni.", "Livello B1 · Unità 5"),
    slide("Che cosa impariamo?", cards([
        ("😤", "Lamentarsi", "Non è giusto che… Mi dà fastidio che…"),
        ("🏢", "La vita in condominio", "i vicini, l'amministratore, le regole"),
        ("💭", "Il congiuntivo (2)", "vada, faccia, possa, esca"),
        ("✉️", "La lettera di lamentela", "Le scrivo per manifestare il mio disappunto…")])),
    slide("🏢 Problemi di convivenza", cards([
        ("🔊", "Il rumore", "la musica alta di notte, i lavori in casa"),
        ("🗑️", "La spazzatura", "i sacchi davanti alla porta, la raccolta differenziata"),
        ("🧽", "La pulizia", "il coinquilino che non lava mai i piatti"),
        ("🚗", "Il parcheggio", "la macchina davanti al portone")])),
    slide("😤 Lamentarsi e rispondere", table([
        ["Lamentarsi", "Mi dà fastidio che… · Non è giusto che… · Non ne posso più! · Uffa!"],
        ["Chiedere", "Le dispiacerebbe abbassare la musica? · Potrebbe fare più attenzione?"],
        ["Spiegare le proprie ragioni", "Non è colpa mia. · Mi scusi, non lo sapevo. · Il fatto è che…"],
        ["Trovare un accordo", "Facciamo così… · Va bene, d'ora in poi… · Patti chiari, amicizia lunga!"]], ["", "espressioni"])),
    slide("💭 Il congiuntivo: verbi irregolari", table([
        ["andare", "vada, vada, vada, andiamo, andiate, vadano"], ["fare", "faccia, faccia, faccia, facciamo, facciate, facciano"],
        ["potere", "possa, possa, possa, possiamo, possiate, possano"], ["uscire", "esca, esca, esca, usciamo, usciate, escano"],
        ["venire", "venga, venga, venga, veniamo, veniate, vengano"], ["dire", "dica, dica, dica, diciamo, diciate, dicano"],
        ["stare / dare", "stia… / dia…"]], ["verbo", "che io, tu, lui, noi, voi, loro"])),
    slide("💭 Quando si usa il congiuntivo?", cards([
        ("⚖️", "Giudizi", "<i>Non è giusto che</i> i vicini <b>facciano</b> rumore."),
        ("📌", "Necessità", "<i>Bisogna che</i> tu <b>vada</b> dall'amministratore."),
        ("😟", "Sentimenti", "<i>Mi dà fastidio che</i> nessuno <b>pulisca</b> le scale."),
        ("🚫", "Negazione", "<i>Non è che</i> io non <b>voglia</b> aiutare, ma non ho tempo.")]) + "\n" +
        nota("Senza persona: <b>bisogna, occorre, basta</b> + infinito → <i>Bisogna pagare entro il 5. · Basta chiedere!</i>", "margin-top:14px;")),
    slide("🔄 La forma passiva", '    <p class="lead">Attiva: <b>L\'amministratore</b> ha convocato la riunione.<br>'
          'Passiva: La riunione <b>è stata convocata</b> dall\'amministratore.</p>\n' +
          table([["presente", "La spazzatura <b>è raccolta</b> / <b>viene raccolta</b> il martedì."],
                 ["passato prossimo", "Le regole <b>sono state cambiate</b>."],
                 ["futuro", "La riunione <b>sarà fatta</b> in cortile."]], ["tempo", "esempio"])),
    slide("🔢 Qualche, ogni, nessuno…", cards([
        ("1️⃣", "qualche + singolare", "<i>Ho <b>qualche</b> problema con il vicino.</i> (= alcuni problemi)"),
        ("🔁", "ogni + singolare", "<i><b>Ogni</b> sera mette la musica alta.</i>"),
        ("🚫", "nessuno / niente", "<i>Non è venuto <b>nessuno</b>. · Non ho detto <b>niente</b>.</i>"),
        ("✨", "qualcosa di / da", "<i>qualcosa <b>di</b> buono · qualcosa <b>da</b> fare</i>")])),
    slide("🤝 Anche se, benché…", cards([
        ("➕", "anche se + indicativo", "<i><b>Anche se</b> sono stanco, aiuto la mia vicina.</i>"),
        ("✍️", "benché / sebbene / nonostante + congiuntivo", "<i><b>Benché</b> sia stanco, aiuto la mia vicina.</i>")]) + "\n" +
        nota("Verbi utili: <b>farcela</b> (riuscire) · <b>andarsene</b> (andare via) · <b>prendersela</b> (offendersi) · <b>cavarsela</b> (riuscire in una situazione difficile)", "margin-top:14px;")),
    slide("💬 La musica del vicino", dialogo([
        ("Signora Greco", "Buonasera. Mi scusi, ma sono le due di notte e la musica è altissima!"),
        ("*Yusuf", "Oh, mi dispiace. È il compleanno del mio coinquilino."),
        ("Signora Greco", "Capisco, ma non è giusto che tutto il palazzo non possa dormire."),
        ("*Yusuf", "Ha ragione. Non me la prenda, abbassiamo subito."),
        ("Signora Greco", "Grazie. La prossima volta basta avvisare prima."),
        ("*Yusuf", "Certo, d'ora in poi lo facciamo. Buonanotte!")])),
    fine("Ora sai lamentarti con gentilezza e trovare un accordo."),
]

U5_DIAL = [("F", "Pronto, studio dell'amministratore Lorusso, buongiorno."),
           ("M", "Buongiorno, sono Karim Haddad, abito in via Crisanzio 25, al terzo piano. Chiamo per un problema."),
           ("F", "Mi dica pure."),
           ("M", "L'ascensore è rotto da due settimane. Al quinto piano abita una signora anziana che non può uscire di casa."),
           ("F", "Ha ragione, mi dispiace. Il tecnico doveva venire lunedì, ma non è venuto."),
           ("M", "Non è giusto che paghiamo le spese e nessuno risolva il problema."),
           ("F", "Capisco. Bisogna che io richiami la ditta oggi stesso. Le prometto che entro giovedì l'ascensore sarà riparato."),
           ("M", "Va bene, aspetto fino a giovedì. Altrimenti scriverò una lettera a tutti i condomini.")]
U5_VOLONT = ("Mi chiamo Chiara e da due anni faccio volontariato in un'associazione del mio quartiere, a Bari Vecchia. "
             "Ogni mercoledì pomeriggio aiutiamo i bambini a fare i compiti e il sabato mattina distribuiamo la spesa alle famiglie in difficoltà. "
             "All'inizio avevo paura di non farcela, perché lavoro tutto il giorno. Ma basta organizzarsi! "
             "Anche se sono stanca, quando torno a casa sono felice: ho conosciuto tante persone e ho imparato molto.")

U5_CONG = tx([
    ("Bisogna che tu (andare)", "dall'amministratore.", "vada"), ("Non è giusto che loro (fare)", "rumore di notte.", "facciano"),
    ("Mi dà fastidio che il vicino non (dire)", "mai buongiorno.", "dica"), ("È meglio che voi (uscire)", "prima delle otto.", "usciate"),
    ("Spero che tu (potere)", "venire alla riunione.", "possa"), ("Bisogna che noi (fare)", "la raccolta differenziata.", "facciamo"),
    ("Non è che io non (volere)", "aiutarti.", "voglia"), ("Voglio che i bambini (stare)", "tranquilli.", "stiano")])

U5_INDEF = sc([
    ("Ho ___ problema con il mio coinquilino.", ["qualche", "alcuni", "nessuno"], "qualche"),
    ("___ giorno il vicino lascia la spazzatura sulle scale.", ["Ogni", "Ognuno", "Qualche"], "Ogni"),
    ("Alla riunione non è venuto ___.", ["nessuno", "niente", "qualcuno"], "nessuno"),
    ("Hai qualcosa ___ bere?", ["da", "di", "a"], "da"),
    ("È successo qualcosa ___ strano.", ["di", "da", "a"], "di"),
    ("___ deve pulire la sua parte di cucina.", ["Ognuno", "Ogni", "Qualche"], "Ognuno"),
    ("Non ho capito ___.", ["niente", "nessuno", "ogni"], "niente")])

U5_PASS = tx([
    ("Il vicino ha riparato la porta. → La porta", "dal vicino.", "e stata riparata"),
    ("L'amministratore convoca la riunione. → La riunione", "dall'amministratore.", "e convocata|viene convocata"),
    ("I volontari hanno organizzato la festa. → La festa", "dai volontari.", "e stata organizzata"),
    ("Il comune raccoglie la spazzatura. → La spazzatura", "dal comune.", "e raccolta|viene raccolta"),
    ("I condomini hanno approvato le regole. → Le regole", "dai condomini.", "sono state approvate")])

U5_CONC = sc([
    ("___ è tardi, i vicini fanno ancora rumore.", ["Anche se", "Benché"], "Anche se"),
    ("___ sia stanca, Chiara va all'associazione.", ["Benché", "Anche se"], "Benché"),
    ("Nonostante ___ freddo, i bambini giocano in cortile.", ["faccia", "fa"], "faccia"),
    ("Anche se ___ poco tempo, faccio volontariato.", ["ho", "abbia"], "ho"),
    ("Sebbene il vicino ___ gentile, la sua musica mi dà fastidio.", ["sia", "è"], "sia")])

U5_PRON = sc([
    ("L'esame era difficile, ma ce l'ho fatta: ___.", ["ci sono riuscito", "sono andato via", "mi sono offeso"], "ci sono riuscito"),
    ("Era tardi, così me ne sono andato: ___.", ["sono andato via", "ci sono riuscito", "mi sono arrabbiato"], "sono andato via"),
    ("Non prendertela! Vuol dire: ___.", ["non offenderti", "non andare via", "non prenderlo"], "non offenderti"),
    ("Parla poco italiano, ma se la cava: ___.", ["riesce a comunicare", "non capisce niente", "va via"], "riesce a comunicare")])

U5_LETTERA = sc([
    ("Apertura:", ["Gentile amministratore,", "Caro Mario,", "Ciao!"], "Gentile amministratore,"),
    ("Il motivo:", ["Le scrivo per segnalare un problema…", "Ti scrivo perché sono arrabbiato…", "Allora, c'è un problema…"],
     "Le scrivo per segnalare un problema…"),
    ("La lamentela:", ["Vorrei manifestare il mio disappunto per…", "Che schifo!", "Non ne posso più, uffa!"],
     "Vorrei manifestare il mio disappunto per…"),
    ("La richiesta:", ["La prego di risolvere il problema al più presto.", "Fallo subito!", "Sbrigati."],
     "La prego di risolvere il problema al più presto."),
    ("Chiusura:", ["Distinti saluti", "Baci e abbracci", "Ci sentiamo"], "Distinti saluti")])

U5 = {
 "title": "🏘️ Che problema c'è? · Esercizi B1",
 "store": "b1-problemi",
 "sections": [
  {"part": "Ascoltare"},
  ex("e1", "1 · 🎧 Telefonata all'amministratore", "1 · Ascolto: telefonata", "choice",
     "Ascolta la telefonata. Scegli la risposta giusta.",
     sc([("A che piano abita Karim?", ["al terzo", "al quinto", "al primo"], "al terzo"),
         ("Qual è il problema?", ["l'ascensore è rotto", "c'è rumore", "manca l'acqua"], "l'ascensore è rotto"),
         ("Da quanto tempo?", ["da due settimane", "da due giorni", "da un mese"], "da due settimane"),
         ("Chi ha più difficoltà?", ["una signora anziana", "un bambino", "il portiere"], "una signora anziana"),
         ("Entro quando sarà riparato?", ["entro giovedì", "entro lunedì", "entro fine mese"], "entro giovedì"),
         ("Che cosa farà Karim, se non lo riparano?", ["scriverà una lettera", "chiamerà la polizia", "cambierà casa"], "scriverà una lettera")]),
     audio=U5_DIAL),
  ex("e2", "2 · 🎧 Il volontariato di Chiara", "2 · Ascolto: racconto", "choice",
     "Ascolta Chiara. Vero o falso?",
     vf([("Chiara fa volontariato da due anni.", True), ("L'associazione è a Bari Vecchia.", True),
         ("Il mercoledì aiuta gli anziani.", False), ("Il sabato distribuisce la spesa alle famiglie.", True),
         ("Chiara non lavora.", False), ("Dopo il volontariato si sente felice.", True)]), opts=VF, audio=U5_VOLONT),
  {"part": "Grammatica"},
  ex("e3", "3 · Il congiuntivo dei verbi irregolari", "3 · Congiuntivo", "text",
     "Scrivi il verbo al congiuntivo presente.", U5_CONG, w="s"),
  ex("e4", "4 · Qualche, ogni, nessuno…", "4 · Indefiniti", "choice", "Scegli la parola giusta.", U5_INDEF),
  ex("e5", "5 · La forma passiva", "5 · Passiva", "text",
     "Trasforma la frase al passivo. Usa lo stesso tempo.", U5_PASS, w="m"),
  ex("e6", "6 · Anche se o benché?", "6 · Anche se, benché", "choice",
     "Scegli la forma giusta: anche se + indicativo, benché / sebbene / nonostante + congiuntivo.", U5_CONC),
  {"part": "Parole"},
  ex("e7", "7 · Farcela, andarsene…", "7 · Verbi pronominali", "choice", "Che cosa vuol dire? Scegli.", U5_PRON),
  ex("e8", "8 · La lettera di lamentela", "8 · Lettera formale", "choice",
     "Scrivi all'amministratore del palazzo. Scegli la frase giusta per una lettera formale.", U5_LETTERA),
  {"part": "Scrivere e parlare"},
  {"id": "e9", "title": "9 ✎ · Scrivi una lettera di lamentela", "type": "free", "rows": 10,
   "items": ["Nel tuo palazzo c'è un problema (rumore, spazzatura, ascensore, parcheggio…). Scrivi una lettera formale all'amministratore: spiega il problema, da quanto tempo c'è, che cosa chiedi."]},
  {"id": "e10", "title": "10 🎤 · Il mio quartiere", "type": "record",
   "cons": "Premi «Registra» e parla del quartiere dove vivi.",
   "items": ["Che cosa ti piace? Che cosa non ti piace? Che cosa bisognerebbe cambiare?"]},
 ]
}

UNITA = [
    ("b1-cronaca", "Che cosa è successo?", U1_SLIDE, U1),
    ("b1-vacanze", "Vorrei andare in Sardegna", U2_SLIDE, U2),
    ("b1-tempo-libero", "Su dai, usciamo!", U3_SLIDE, U3),
    ("b1-lavoro", "Come ha saputo di questo lavoro?", U4_SLIDE, U4),
    ("b1-problemi", "Che problema c'è?", U5_SLIDE, U5),
]

if __name__ == "__main__":
    import genera, slide as sl
    for cartella, nome, slides, dati in UNITA:
        sl.build(cartella + "/index.html", nome, "LIVELLO B1", slides, B1_CSS)
        genera.build(cartella + "/esercizi.html", dati)
