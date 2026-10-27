from genera import eq, has, all_
from unita_presente import cl

SEMPLICI = cl("1. IO VADO [da] ANDREA [in] TRENO.<br>2. IL LIBRO È [di] MARIA.<br>3. MIA MAMMA TELEFONA [a] MILANO.<br>"
    "4. [a] VENEZIA C'È IL MARE.<br>5. TU VAI [a] SCUOLA [con] MARIA.<br>6. [tra|fra] VENTI MINUTI PRENDO L'AEREO.<br>"
    "7. [a] MARIO PIACE IL PESCE.<br>8. NOI ABITIAMO [in] VIA PIAVE.<br>9. OGGI ANDIAMO [a] SCUOLA.<br>"
    "10. L'OROLOGIO [di] MARIO È ROTTO.<br>11. [in] CAMERA LA LUCE È SPENTA.<br>12. VOI VENITE [da] ROMA.<br>"
    "13. LORO VANNO [a] PADOVA.<br>14. LUI VA [a] CASA [di] MARIO.<br>15. IO ESCO [con] MARIA E LUISA.<br>"
    "16. NOI PARTIAMO [per] ROMA.<br>17. PENSO [di] ANDARE A CASA.<br>18. MARIO VIVE [con] UN'AMICA.<br>"
    "19. SONO IN ITALIA [da] DUE ANNI.<br>20. QUESTO È UN REGALO [per] TE.<br>21. IL LIBRO È [su] UN TAVOLO.<br>"
    "22. IL BAR È [tra|fra] LA FARMACIA E IL TABACCAIO.")

ANDARE = cl("1. IO VADO [a] BARI [in] AUTOBUS.<br>2. VOI ANDATE [in] PIAZZA [a] PIEDI.<br>"
    "3. LORO VANNO [in] PIZZERIA [in] MACCHINA.<br>4. IO VADO [dal] DOTTORE [con] UN MIO AMICO.<br>"
    "5. TU VAI [al] SUPERMERCATO [a|per] COMPRARE IL SAPONE.<br>6. LUI VA [a] ROMA [a|per] LAVORARE.<br>"
    "7. NOI ANDIAMO [in] CINA, [in] CENTRO, [a] CASA.<br>8. LEI VIENE [da] PADOVA.")

ART1 = cl("<b>A + ARTICOLO</b><br>1. I NEGOZI APRONO [alle] NOVE.<br>2. LA FERMATA È DI FRONTE [alla] FARMACIA.<br>"
    "3. LA STAZIONE È VICINO [al] CENTRO.<br>4. LUI LAVORA [al] MERCATO.<br><br>"
    "<b>DI + ARTICOLO</b><br>5. SCUSI, DOV'È LA FERMATA [dell'] AUTOBUS?<br>6. IL LIBRO È [del] MIO AMICO.<br>"
    "7. DOVE SONO LE CHIAVI [della] CAMERA?<br>8. QUESTA È L'ENTRATA [del] SUPERMERCATO.<br><br>"
    "<b>SU + ARTICOLO</b><br>9. IL LIBRO È [sul] TAVOLO.<br>10. LE CHIAVI SONO [sulla] SEDIA.<br>"
    "11. GLI UCCELLI SONO [sugli] ALBERI.<br>12. LA FINESTRA DÀ [sulla] PIAZZA.<br><br>"
    "<b>DA + ARTICOLO</b><br>13. I NEGOZI SONO CHIUSI [dalle] 12.30 ALLE 15.30.<br>14. ADESSO VADO [dal] DOTTORE.<br>"
    "15. LAVORO [dalle] 8 ALLE 17.<br><br>"
    "<b>IN + ARTICOLO</b><br>16. [nel] FRIGORIFERO C'È IL PRANZO DI OGGI.<br>17. [nella] MIA CASA CI SONO 4 STANZE.<br>"
    "18. HO MESSO LE COPERTE [nell'] ARMADIO.<br>19. [nelle] GRANDI CITTÀ C'È MOLTO TRAFFICO.")

ART2 = cl("1. CI TROVIAMO A CASA [degli] AMICI.<br>2. SALITE ANCHE VOI [sull'] AUTOBUS?<br>"
    "3. COMINCIO A LAVORARE [alle] OTTO E FINISCO [alle] CINQUE.<br>4. SE CERCHI LE CHIAVI, SONO [sul] TAVOLO.<br>"
    "5. MANGIO SPESSO [al] RISTORANTE.<br>6. CI TROVIAMO [all'] USCITA DELLA SCUOLA.<br>"
    "7. QUEI DUE RAGAZZI VENGONO [dal] BANGLADESH.<br>8. ABITO LONTANO [dalla] STAZIONE.<br>"
    "9. MARIO TELEFONA ALLA MOGLIE DUE VOLTE [al] GIORNO.<br>10. QUANDO TORNATE [dalla] FRANCIA?<br>"
    "11. I PIATTI SONO [nell'] ARMADIO DELLA CUCINA.<br>12. L'ACQUA È [nei] BICCHIERI.<br>"
    "13. CI VEDIAMO [al] BAR [dell'] ANGOLO.<br>14. [nella] MIA CLASSE CI SONO 20 STUDENTI.<br>"
    "15. LA DOMENICA VADO [al] MARE.")

SU = ["SUL", "SULLA", "SULL'", "SULLO", "SUI", "SULLE", "SUGLI"]
IN = ["NEL", "NELLA", "NELL'", "NELLO", "NEI", "NELLE", "NEGLI"]
A = ["AL", "ALLA", "ALL'", "ALLO", "AI", "ALLE", "AGLI"]
DI = ["DEL", "DELLA", "DELL'", "DELLO", "DEI", "DELLE", "DEGLI"]
DA = ["DAL", "DALLA", "DALL'", "DALLO", "DAI", "DALLE", "DAGLI"]
COLL1 = [(SU, [("TAVOLO", "SUL"), ("SEDIA", "SULLA"), ("ARMADIO", "SULL'"), ("STENDINO", "SULLO"), ("LIBRI", "SUI"),
               ("SCALE", "SULLE"), ("ASTUCCI", "SUGLI")]),
         (IN, [("CASSETTO", "NEL"), ("STANZA", "NELLA"), ("ACQUA", "NELL'"), ("ZAINO", "NELLO"), ("GIARDINI", "NEI"),
               ("MACCHINE", "NELLE"), ("ALBERI", "NEGLI")])]
COLL2 = [(A, [("PAPÀ", "AL"), ("MAMMA", "ALLA"), ("ANZIANO", "ALL'"), ("ZIO", "ALLO"), ("CUGINI", "AI"),
              ("SORELLE", "ALLE"), ("AMICI", "AGLI")]),
         (DI, [("GATTO", "DEL"), ("NONNA", "DELLA"), ("OPERAIO", "DELL'"), ("STUDIO", "DELLO"), ("PANTALONI", "DEI"),
               ("SCARPE", "DELLE"), ("OCCHIALI", "DEGLI")]),
         (DA, [("DOTTORE", "DAL"), ("CASA", "DALLA"), ("AVVOCATO", "DALL'"), ("STUDIO", "DALLO"), ("BAMBINI", "DAI"),
               ("CUGINE", "DALLE"), ("UOMINI", "DAGLI")])]

def collega(gruppi):
    items, ks, n = [], [], 0
    for forme, coppie in gruppi:
        for nome, a in coppie:
            n += 1; items.append({"q": f"{n}. … {nome}", "opts": forme}); ks.append(eq(a))
    return items, ks

C1 = collega(COLL1)
C2 = collega(COLL2)

APP = [("IL BAR · 8.00 · ENTRATA", ["all'entrata del bar"], ["8"]),
       ("LA SCUOLA · 10.00 · USCITA", ["all'uscita della scuola"], ["10"]),
       ("LA FERMATA · 7.15 · VICINO", ["vicino alla fermata"], ["7"]),
       ("IL SUPERMERCATO · 16.00 · ENTRATA", ["all'entrata del supermercato"], ["16", "4"]),
       ("LA PIZZERIA · 20.00 · DIETRO", ["dietro alla pizzeria", "dietro la pizzeria"], ["20", "8"]),
       ("IL NEGOZIO · 17.00 · DAVANTI", ["davanti al negozio"], ["17", "5"]),
       ("LA LIBRERIA · 19.00 · VICINO", ["vicino alla libreria"], ["19", "7"]),
       ("LA CHIESA · 9.00 · DIETRO", ["dietro alla chiesa", "dietro la chiesa"], ["9"]),
       ("LA STAZIONE · 6.00 · INGRESSO", ["all'ingresso della stazione"], ["6"])]

def apostrofo(ks):
    """DELL' vale anche senza apostrofo (DELL)."""
    for k in ks:
        k["a"] += [x[:-1] for x in k["a"] if x.endswith("'")]
    return ks

for _ks in (ART1[1], ART2[1]):
    apostrofo(_ks)

PREPOSIZIONI = {
 "title": "🔗 Le preposizioni · Esercizi",
 "store": "preposizioni",
 "upper": True,
 "sections": [
  {"part": "Le preposizioni semplici"},
  {"id": "e1", "title": "1 · DI, A, DA, IN, CON, SU, PER, TRA", "short": "1 · Preposizioni semplici", "type": "cloze",
   "cons": "Scrivi la preposizione giusta.", "bank": "DI · A · DA · IN · CON · SU · PER · TRA / FRA",
   "parts": SEMPLICI[0], "k": SEMPLICI[1]},
  {"id": "e2", "title": "2 · Andare e venire", "short": "2 · Andare e venire", "type": "cloze",
   "cons": "ANDARE A (casa, Bari, piedi) · IN (Cina, centro, autobus) · DA (un amico) · VENIRE DA (Padova)",
   "parts": ANDARE[0], "k": ANDARE[1]},
  {"part": "Le preposizioni articolate"},
  {"id": "e3", "title": "3 · SU e IN + articolo", "short": "3 · Su, in + articolo", "type": "choice",
   "cons": "Scegli la forma giusta.", "items": C1[0], "k": C1[1]},
  {"id": "e4", "title": "4 · A, DI e DA + articolo", "short": "4 · A, di, da + articolo", "type": "choice",
   "cons": "Scegli la forma giusta.", "items": C2[0], "k": C2[1]},
  {"id": "e5", "title": "5 · Completa le frasi", "short": "5 · Completa (1)", "type": "cloze",
   "cons": "Scrivi la preposizione articolata giusta.", "parts": ART1[0], "k": ART1[1]},
  {"id": "e6", "title": "6 · Completa ancora", "short": "6 · Completa (2)", "type": "cloze",
   "cons": "Scrivi la preposizione giusta (semplice o articolata).", "parts": ART2[0], "k": ART2[1]},
  {"part": "Dove e quando ci vediamo?"},
  {"id": "e7", "title": "7 · Prendiamo un appuntamento", "short": "7 · Appuntamenti", "type": "text", "w": "w",
   "cons": "Scrivi la frase. Esempio: IL BAR · 8.00 · ENTRATA → CI VEDIAMO ALL'ENTRATA DEL BAR ALLE 8.",
   "items": [{"q": f"{i}. {q}"} for i, (q, *_) in enumerate(APP, 1)],
   "k": [all_(dove, ora) for _, dove, ora in APP]},
 ]
}
