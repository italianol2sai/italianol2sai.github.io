"""Teoria «pratica» prima degli esercizi di grammatica (regola di Erila, 2026-10-30): poche righe, una tabellina,
esempi. Si aggiunge a un blocco {"part": ...} con la chiave "teoria"; motore.js la mostra in un riquadro «La regola»."""

def tab(*righe, head=None):
    h = "<tr>%s</tr>" % "".join("<th>%s</th>" % c for c in head) if head else ""
    return "<table>%s%s</table>" % (h, "".join("<tr>%s</tr>" % "".join("<td>%s</td>" % c for c in r) for r in righe))

def es(*frasi):
    return "".join('<span class="esempio">👉 %s</span>' % f for f in frasi)

def aggiungi(pagine, teorie):
    """pagine: lista di dizionari-pagina; teorie: {(indice pagina, titolo della parte): html}"""
    for (i, parte), testo in teorie.items():
        trovate = [s for s in pagine[i]["sections"] if s.get("part") == parte]
        assert len(trovate) == 1, (i, parte)
        trovate[0]["teoria"] = testo

# ---------------------------------------------------------------- blocchi riusabili
ESSERE_AVERE = tab(("IO", "SONO", "HO"), ("TU", "SEI", "HAI"), ("LUI / LEI", "È", "HA"), ("NOI", "SIAMO", "ABBIAMO"), ("VOI", "SIETE", "AVETE"),
                   ("LORO", "SONO", "HANNO"), head=("", "ESSERE", "AVERE")) + \
    "ESSERE: CHI SEI, DI DOVE SEI, COME SEI. AVERE: L'ETÀ, LE COSE, LA FAMIGLIA." + es("SONO DEL SENEGAL. HO 25 ANNI.")

AGGETTIVI = tab(("-O", "ALTO", "ALTA", "ALTI", "ALTE"), ("-E", "GENTILE", "GENTILE", "GENTILI", "GENTILI"),
                head=("", "MASCHILE", "FEMMINILE", "MASCHILI", "FEMMINILI")) + \
    "L'AGGETTIVO CAMBIA COME IL NOME: MASCHILE O FEMMINILE, SINGOLARE O PLURALE." + es("UN RAGAZZO ALTO → DUE RAGAZZE ALTE")

ARTICOLI = tab(("IL", "I", "IL LIBRO → I LIBRI"), ("LO (S+CONS., Z)", "GLI", "LO ZAINO → GLI ZAINI"), ("L' (VOCALE)", "GLI / LE", "L'AMICO → GLI AMICI"),
               ("LA", "LE", "LA PENNA → LE PENNE"), head=("SINGOLARE", "PLURALE", "ESEMPIO")) + \
    "UN · UNO · UNA · UN' (UN' SOLO PER LE PAROLE FEMMINILI CON LA VOCALE: UN'AULA)."

PRESENTE = tab(("IO", "PARLO", "PRENDO", "DORMO", "FINISCO"), ("TU", "PARLI", "PRENDI", "DORMI", "FINISCI"), ("LUI / LEI", "PARLA", "PRENDE", "DORME", "FINISCE"),
               ("NOI", "PARLIAMO", "PRENDIAMO", "DORMIAMO", "FINIAMO"), ("VOI", "PARLATE", "PRENDETE", "DORMITE", "FINITE"), ("LORO", "PARLANO", "PRENDONO", "DORMONO", "FINISCONO"),
               head=("", "-ARE", "-ERE", "-IRE", "-IRE (ISC)"))

RIFLESSIVI = tab(("IO", "MI", "MI ALZO"), ("TU", "TI", "TI ALZI"), ("LUI / LEI", "SI", "SI ALZA"), ("NOI", "CI", "CI ALZIAMO"), ("VOI", "VI", "VI ALZATE"), ("LORO", "SI", "SI ALZANO")) + \
    "IL PRONOME (MI, TI, SI…) VA PRIMA DEL VERBO."

MODALI = tab(("IO", "DEVO", "POSSO", "VOGLIO"), ("TU", "DEVI", "PUOI", "VUOI"), ("LUI / LEI", "DEVE", "PUÒ", "VUOLE"), ("NOI", "DOBBIAMO", "POSSIAMO", "VOGLIAMO"),
             ("VOI", "DOVETE", "POTETE", "VOLETE"), ("LORO", "DEVONO", "POSSONO", "VOGLIONO"), head=("", "DOVERE", "POTERE", "VOLERE")) + \
    "DOPO IL VERBO MODALE C'È UN VERBO ALL'INFINITO." + es("DEVO LAVORARE. POSSO ENTRARE? VOGLIO DORMIRE.")

PIACERE = tab(("MI PIACE", "+ UNA COSA / UN VERBO", "MI PIACE LA PIZZA. MI PIACE BALLARE."), ("MI PIACCIONO", "+ TANTE COSE", "MI PIACCIONO LE ARANCE.")) + \
    "NO: <s>IO PIACCIO</s>. SÌ: <b>MI PIACE</b>. NEGATIVO: <b>NON MI PIACE</b>."

PASSATO = ("PASSATO PROSSIMO = <b>AVERE / ESSERE</b> + PARTICIPIO (-ARE → -ATO · -ERE → -UTO · -IRE → -ITO)." +
           tab(("AVERE", "LA MAGGIOR PARTE DEI VERBI", "HO MANGIATO, HAI LAVORATO"),
               ("ESSERE", "ANDARE, VENIRE, PARTIRE, ARRIVARE, USCIRE, RESTARE, NASCERE…", "SONO ANDATO / ANDATA")) +
           "CON <b>ESSERE</b> IL PARTICIPIO CAMBIA: ANDATO · ANDATA · ANDATI · ANDATE.<br>IRREGOLARI: FATTO, SCRITTO, PRESO, VISTO, MESSO, APERTO, DETTO, LETTO.")

PREP = (tab(("A", "CITTÀ", "VADO A BARI"), ("IN", "NAZIONE, NEGOZI IN -IA, MEZZI", "IN ITALIA, IN FARMACIA, IN TRENO"),
            ("DA", "PERSONE", "VADO DAL MEDICO"), ("PER", "DESTINAZIONE DEL TRENO", "IL TRENO PER FOGGIA")) +
        "A + IL = AL · A + LA = ALLA · A + L' = ALL' · DA + IL = DAL · DA + LA = DALLA")

FUTURO = (tab(("IO", "PARLERÒ", "PRENDERÒ", "PARTIRÒ"), ("TU", "PARLERAI", "PRENDERAI", "PARTIRAI"), ("LUI / LEI", "PARLERÀ", "PRENDERÀ", "PARTIRÀ"),
              ("NOI", "PARLEREMO", "PRENDEREMO", "PARTIREMO"), ("VOI", "PARLERETE", "PRENDERETE", "PARTIRETE"), ("LORO", "PARLERANNO", "PRENDERANNO", "PARTIRANNO"),
              head=("", "-ARE", "-ERE", "-IRE")) +
          "IRREGOLARI: SARÒ, AVRÒ, ANDRÒ, FARÒ, VERRÒ, POTRÒ, DOVRÒ, VORRÒ." + es("SE DOMANI PIOVE / PIOVERÀ, RESTERÒ A CASA."))

PRONOMI_DIR = (tab(("IL / LO", "LO", "IL PANE? LO COMPRO."), ("LA", "LA", "LA PIZZA? LA MANGIO."), ("I / GLI", "LI", "I BIGLIETTI? LI PRENDO."), ("LE", "LE", "LE FOTO? LE FACCIO."),
                   head=("LA COSA", "PRONOME", "ESEMPIO")) +
               "IL PRONOME VA PRIMA DEL VERBO. AL PASSATO: L'HO VISTO / L'HO VISTA · LI HO PRESI · LE HO FATTE.")

POSSESSIVI = (tab(("IO", "MIO", "MIA", "MIEI", "MIE"), ("TU", "TUO", "TUA", "TUOI", "TUE"), ("LUI / LEI", "SUO", "SUA", "SUOI", "SUE"),
                  ("NOI", "NOSTRO", "NOSTRA", "NOSTRI", "NOSTRE"), ("VOI", "VOSTRO", "VOSTRA", "VOSTRI", "VOSTRE"), ("LORO", "LORO", "LORO", "LORO", "LORO"),
                  head=("", "M. SING.", "F. SING.", "M. PLUR.", "F. PLUR.")) +
              "DI SOLITO CON L'ARTICOLO: LA MIA CASA, I MIEI AMICI. MA CON LA FAMIGLIA AL SINGOLARE SENZA ARTICOLO: MIA MADRE, MIO FRATELLO.")

def minus(h):
    """per le pagine A2: stesso contenuto in minuscolo (le parole in maiuscolo dentro i tag restano leggibili)"""
    import re
    return re.sub(r">([^<]+)<", lambda m: ">" + m.group(1).lower() + "<", "<x>" + h + "</x>")[3:-4]

# ---------------------------------------------------------------- eserciziario A1 (19 schede, indice 0-18)
TEORIA_SCHEDE = {
  (0, "Essere e avere"): ESSERE_AVERE + "<br>DA DOVE VIENI? VENGO <b>DA</b> + CITTÀ · <b>DAL</b> + NAZIONE MASCHILE · <b>DALLA</b> + NAZIONE FEMMINILE · <b>DALL'</b> + VOCALE."
                         + es("VENGO DA DAKAR. VENGO DAL SENEGAL. VENGO DALLA TUNISIA."),
  (0, "I numeri"): tab(("1 UNO", "6 SEI", "11 UNDICI", "16 SEDICI"), ("2 DUE", "7 SETTE", "12 DODICI", "17 DICIASSETTE"), ("3 TRE", "8 OTTO", "13 TREDICI", "18 DICIOTTO"),
                       ("4 QUATTRO", "9 NOVE", "14 QUATTORDICI", "19 DICIANNOVE"), ("5 CINQUE", "10 DIECI", "15 QUINDICI", "20 VENTI")) +
                   "DECINE: 30 TRENTA · 40 QUARANTA · 50 CINQUANTA · 60 SESSANTA · 70 SETTANTA · 80 OTTANTA · 90 NOVANTA · 100 CENTO · 1000 MILLE." + es("21 VENTUNO · 28 VENTOTTO · 33 TRENTATRÉ"),
  (1, "Descrivere"): AGGETTIVI + "<br>ATTENZIONE: SIMPATICO → SIMPATICI · BIANCO → BIANCHI.",
  (1, "La frase negativa"): "PER DIRE NO METTI <b>NON</b> PRIMA DEL VERBO." + es("SONO STANCO → NON SONO STANCO.", "HO LA MACCHINA → NON HO LA MACCHINA."),
  (2, "Gli articoli"): ARTICOLI,
  (2, "C'è / ci sono"): tab(("C'È", "+ UNA COSA", "C'È UNA LAVAGNA."), ("CI SONO", "+ TANTE COSE", "CI SONO DUE FINESTRE.")) + es("NELLA MIA CLASSE C'È UN COMPUTER E CI SONO 20 SEDIE."),
  (3, "Il verbo fare"): tab(("IO", "FACCIO"), ("TU", "FAI"), ("LUI / LEI", "FA"), ("NOI", "FACCIAMO"), ("VOI", "FATE"), ("LORO", "FANNO")) +
                        "FARE + LAVORO: FACCIO IL CUOCO. FARE + ATTIVITÀ: FACCIO LA SPESA, FACCIO COLAZIONE, FACCIO SPORT.<br>" + PRESENTE,
  (4, "Andare, venire, uscire, stare"): tab(("IO", "VADO", "VENGO", "ESCO", "STO"), ("TU", "VAI", "VIENI", "ESCI", "STAI"), ("LUI / LEI", "VA", "VIENE", "ESCE", "STA"),
                                            ("NOI", "ANDIAMO", "VENIAMO", "USCIAMO", "STIAMO"), ("VOI", "ANDATE", "VENITE", "USCITE", "STATE"), ("LORO", "VANNO", "VENGONO", "ESCONO", "STANNO"),
                                            head=("", "ANDARE", "VENIRE", "USCIRE", "STARE")),
  (4, "Proporre"): tab(("PROPORRE", "TI VA DI…? PERCHÉ NON…? ANDIAMO…?"), ("ACCETTARE", "SÌ, VOLENTIERI! VA BENE! PERCHÉ NO?"), ("RIFIUTARE", "MI DISPIACE, NON POSSO. NO, GRAZIE.")),
  (5, "I numeri ordinali"): "PER IL PIANO, LA CLASSIFICA, LE DATE IMPORTANTI USIAMO I NUMERI ORDINALI." +
                            tab(("1° PRIMO", "2° SECONDO", "3° TERZO", "4° QUARTO", "5° QUINTO"), ("6° SESTO", "7° SETTIMO", "8° OTTAVO", "9° NONO", "10° DECIMO")),
  (5, "Dov'è?"): tab(("SOPRA / SU", "⬆️"), ("SOTTO", "⬇️"), ("DAVANTI A", "IN FRONTE"), ("DIETRO", "DALL'ALTRA PARTE"), ("ACCANTO A / VICINO A", "DI FIANCO")) +
                 "A + IL = AL · A + LA = ALLA." + es("LA SEDIA È ACCANTO AL TAVOLO. LA BORSA È DIETRO LA PORTA."),
  (5, "I lavori di casa"): PRESENTE,
  (6, "I possessivi"): POSSESSIVI,
  (6, "Quanto?"): tab(("QUANTO", "MASCHILE SINGOLARE", "QUANTO TEMPO?"), ("QUANTA", "FEMMINILE SINGOLARE", "QUANTA ACQUA?"),
                      ("QUANTI", "MASCHILE PLURALE", "QUANTI FIGLI?"), ("QUANTE", "FEMMINILE PLURALE", "QUANTE SORELLE?")),
  (7, "Mangiare, bere, preferire"): tab(("IO", "MANGIO", "BEVO", "PREFERISCO"), ("TU", "MANGI", "BEVI", "PREFERISCI"), ("LUI / LEI", "MANGIA", "BEVE", "PREFERISCE"),
                                        ("NOI", "MANGIAMO", "BEVIAMO", "PREFERIAMO"), ("VOI", "MANGIATE", "BEVETE", "PREFERITE"), ("LORO", "MANGIANO", "BEVONO", "PREFERISCONO"),
                                        head=("", "MANGIARE", "BERE", "PREFERIRE")) + PIACERE,
  (8, "I verbi riflessivi"): RIFLESSIVI,
  (8, "L'ora"): tab(("CHE ORE SONO?", "SONO LE + NUMERO", "SONO LE 8"), ("1:00", "È L'UNA", ""), ("12:00 / 24:00", "È MEZZOGIORNO / MEZZANOTTE", ""),
                    ("+15 / +30 / -15", "E UN QUARTO / E MEZZA / MENO UN QUARTO", "SONO LE 9 E MEZZA")),
  (8, "Sempre, spesso, mai"): "SEMPRE · SPESSO · QUALCHE VOLTA · MAI. L'AVVERBIO VA DOPO IL VERBO. CON MAI: <b>NON</b> + VERBO + <b>MAI</b>." + es("BEVO SEMPRE IL CAFFÈ. NON BEVO MAI IL TÈ."),
  (9, "La frase"): "ORDINE DELLA FRASE: CHI? + VERBO + CHE COSA? + COME?. IL COLORE VA DOPO IL NOME." + es("MARIA PORTA UNA GONNA BLU.") +
                   "<br>COLORI CHE NON CAMBIANO: BLU, ROSA, VIOLA, MARRONE (PLURALE: MARRONI)." + AGGETTIVI,
  (10, "Dovere e andare"): MODALI,
  (10, "Ci vuole / ci vogliono"): tab(("CI VUOLE", "+ UNA COSA", "CI VUOLE UN'ORA."), ("CI VOGLIONO", "+ TANTE COSE", "CI VOGLIONO 10 MINUTI.")),
  (11, "Partire, potere, volere"): MODALI + "<br>PARTIRE: PARTO, PARTI, PARTE, PARTIAMO, PARTITE, PARTONO.<br>" + PREP,
  (12, "Il corpo e i sintomi"): tab(("MI FA MALE", "+ UNA PARTE DEL CORPO", "MI FA MALE LA TESTA."), ("MI FANNO MALE", "+ TANTE PARTI", "MI FANNO MALE I PIEDI.")) +
                               "HO + MALATTIA: HO LA FEBBRE, HO LA TOSSE, HO IL RAFFREDDORE.",
  (13, "Questo e quello"): "<b>QUESTO</b> = VICINO A ME. <b>QUELLO</b> = LONTANO." +
                           tab(("QUESTO", "QUESTA", "QUESTI", "QUESTE"), head=("M. SING.", "F. SING.", "M. PLUR.", "F. PLUR.")) +
                           "QUELLO CAMBIA COME L'ARTICOLO: <b>QUEL</b> PACCO (IL) · <b>QUELLO</b> SPORTELLO (LO) · <b>QUELL'</b>UFFICIO (L') · <b>QUELLA</b> BUSTA (LA) · "
                           "<b>QUEI</b> PACCHI (I) · <b>QUEGLI</b> SPORTELLI (GLI) · <b>QUELLE</b> BUSTE (LE).",
  (14, "Stare + gerundio"): "PER UN'AZIONE CHE SUCCEDE <b>ADESSO</b>: STARE + GERUNDIO." +
                            tab(("-ARE → -ANDO", "PARLARE → PARLANDO"), ("-ERE → -ENDO", "SCRIVERE → SCRIVENDO"), ("-IRE → -ENDO", "DORMIRE → DORMENDO")) +
                            "IRREGOLARI: FARE → FACENDO · BERE → BEVENDO · DIRE → DICENDO.<br>STO, STAI, STA, STIAMO, STATE, STANNO." + es("STO ASPETTANDO IL MIO TURNO."),
  (15, "Il passato prossimo"): PASSATO,
  (16, "Il futuro"): FUTURO,
  (17, "Il si impersonale"): "PER DIRE CHE COSA FANNO <b>TUTTI</b>: SI + VERBO (LUI/LEI)." + es("IN ITALIA SI MANGIA TARDI.") +
                             "<br>CON UN NOME PLURALE IL VERBO VA AL PLURALE:" + es("SI MANGIANO LE ORECCHIETTE."),
  (18, "Lo, la, li, le"): PRONOMI_DIR,
}

# ---------------------------------------------------------------- percorso A1-A2 (13 unità, indice 0-12)
TEORIA_PERCORSO = {
  (0, "L'alfabeto"): tab(("CA · CO · CU", "SUONO DURO [K]", "CASA, COSA"), ("CHE · CHI", "SUONO DURO [K]", "PERCHÉ, CHIAVE"),
                         ("CE · CI", "SUONO DOLCE [Tʃ]", "CENA, CIAO")) + "LO STESSO CON G: GA GO GU · GHE GHI (DURO) · GE GI (DOLCE).",
  (1, "Presentarsi"): "PRONOMI: IO · TU · LUI · LEI · NOI · VOI · LORO. IN ITALIANO SPESSO NON SI DICONO: «SONO INGRID» (= IO SONO INGRID).<br>" +
                      "NAZIONALITÀ: -O/-A (ITALIANO, ITALIANA) OPPURE -E PER TUTTI (CINESE, FRANCESE).",
  (1, "Domande e negazioni"): ESSERE_AVERE + "<br>DOMANDA: STESSA FRASE CON IL «?» (SEI ITALIANO?). NEGAZIONE: NON + VERBO (NON SONO ITALIANO).",
  (2, "Verbi in -are e -ere"): PRESENTE,
  (3, "Verbi in -ire, fare, dare, venire"): PRESENTE + tab(("IO", "FACCIO", "DO", "VENGO"), ("TU", "FAI", "DAI", "VIENI"), ("LUI / LEI", "FA", "DÀ", "VIENE"),
                                                          ("NOI", "FACCIAMO", "DIAMO", "VENIAMO"), ("VOI", "FATE", "DATE", "VENITE"), ("LORO", "FANNO", "DANNO", "VENGONO"),
                                                          head=("", "FARE", "DARE", "VENIRE")),
  (4, "Dire, bere, uscire"): tab(("IO", "DICO", "BEVO", "ESCO"), ("TU", "DICI", "BEVI", "ESCI"), ("LUI / LEI", "DICE", "BEVE", "ESCE"),
                                 ("NOI", "DICIAMO", "BEVIAMO", "USCIAMO"), ("VOI", "DITE", "BEVETE", "USCITE"), ("LORO", "DICONO", "BEVONO", "ESCONO"),
                                 head=("", "DIRE", "BERE", "USCIRE")) + PIACERE,
  (5, "Volere, potere, dovere"): MODALI,
  (6, "Il passato prossimo"): minus(PASSATO),
  (6, "Già e ancora"): minus("<b>GIÀ</b> = È SUCCESSO PRIMA DEL PREVISTO (HO GIÀ MANGIATO). <b>NON… ANCORA</b> = NON È SUCCESSO, MA SUCCEDERÀ (NON HO ANCORA MANGIATO).<br>"
                             "PER RACCONTARE IN ORDINE: PRIMA → POI → DOPO → INFINE."),
  (7, "Stare + gerundio"): minus("STARE + GERUNDIO = UN'AZIONE IN CORSO ADESSO." +
                                 tab(("-ARE → -ANDO", "CUCINARE → CUCINANDO"), ("-ERE / -IRE → -ENDO", "LEGGERE → LEGGENDO, DORMIRE → DORMENDO")) +
                                 "STO, STAI, STA, STIAMO, STATE, STANNO."),
  (7, "Preposizioni articolate"): minus(tab(("A", "AL", "ALLO", "ALLA", "ALL'", "AI", "AGLI", "ALLE"), ("DA", "DAL", "DALLO", "DALLA", "DALL'", "DAI", "DAGLI", "DALLE"),
                                            ("IN", "NEL", "NELLO", "NELLA", "NELL'", "NEI", "NEGLI", "NELLE"), ("SU", "SUL", "SULLO", "SULLA", "SULL'", "SUI", "SUGLI", "SULLE"),
                                            ("DI", "DEL", "DELLO", "DELLA", "DELL'", "DEI", "DEGLI", "DELLE"),
                                            head=("", "IL", "LO", "LA", "L'", "I", "GLI", "LE")) + "PREPOSIZIONE + ARTICOLO = UNA PAROLA SOLA: IN + IL = NEL."),
  (7, "La famiglia e i possessivi"): minus(POSSESSIVI + "<br>MA CON L'ARTICOLO: AL PLURALE (I MIEI FRATELLI), CON I DIMINUTIVI (LA MIA SORELLINA) E CON «LORO» (LA LORO MADRE)."),
  (8, "I pronomi diretti e ne"): minus(PRONOMI_DIR + "<br><b>NE</b> = UNA PARTE / UNA QUANTITÀ: QUANTI FIGLI HAI? NE HO DUE."),
  (9, "L'imperfetto"): minus(tab(("IO", "ABITAVO", "AVEVO", "DORMIVO"), ("TU", "ABITAVI", "AVEVI", "DORMIVI"), ("LUI / LEI", "ABITAVA", "AVEVA", "DORMIVA"),
                                 ("NOI", "ABITAVAMO", "AVEVAMO", "DORMIVAMO"), ("VOI", "ABITAVATE", "AVEVATE", "DORMIVATE"), ("LORO", "ABITAVANO", "AVEVANO", "DORMIVANO"),
                                 head=("", "-ARE", "-ERE", "-IRE")) +
                             "ESSERE: ERO, ERI, ERA, ERAVAMO, ERAVATE, ERANO. FARE: FACEVO…<br>"
                             "<b>IMPERFETTO</b> = ABITUDINI, DESCRIZIONI, AZIONI IN CORSO (DA BAMBINO GIOCAVO…, MENTRE CUCINAVO…).<br>"
                             "<b>PASSATO PROSSIMO</b> = UN FATTO PRECISO, FINITO (IERI MI SONO SVEGLIATO ALLE 7)."),
  (10, "I pronomi indiretti"): minus("RISPONDONO ALLA DOMANDA <b>A CHI?</b>" +
                                     tab(("A ME", "MI"), ("A TE", "TI"), ("A LUI", "GLI"), ("A LEI / A LEI (FORMALE)", "LE"), ("A NOI", "CI"), ("A VOI", "VI"), ("A LORO", "GLI")) +
                                     "IL PRONOME VA PRIMA DEL VERBO: TI TELEFONO DOMANI."),
  (11, "Futuro e condizionale"): minus(FUTURO + "<br><b>CONDIZIONALE</b> (-EREI): VORREI, POTREI, DOVRESTI, MI PIACEREBBE. "
                                       "SERVE PER CHIEDERE GENTILMENTE, DARE UN CONSIGLIO, DIRE UN DESIDERIO."),
  (12, "L'imperativo"): minus(tab(("TU", "PARLA!", "PRENDI!", "FINISCI!"), ("LEI (FORMALE)", "PARLI!", "PRENDA!", "FINISCA!"), ("VOI", "PARLATE!", "PRENDETE!", "FINITE!"),
                                  head=("", "-ARE", "-ERE", "-IRE")) +
                              "NEGATIVO CON TU: NON + INFINITO (NON PARLARE!). IRREGOLARI CON TU: FA', VA', DA', STA', DI'."),
  (12, "Il lavoro"): minus("NEGLI ANNUNCI SI USA IL <b>SI</b> IMPERSONALE: SI CERCA + UNA PERSONA / SI CERCANO + TANTE PERSONE." + es("SI CERCA UN CUOCO. SI CERCANO DUE CAMERIERI.")),
}
