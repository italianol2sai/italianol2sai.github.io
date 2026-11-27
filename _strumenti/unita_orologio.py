"""L'OROLOGIO: CHE ORE SONO? (A1, 2026-11-27, richiesta di Erila: «esercizi e teoria sulla lettura dell'orario e dell'orologio a1»).
Continua ore-giorni/ (A0, solo le ore intere e qualche esempio): qui l'orologio con le lancette, E/MENO, il quarto e la mezza,
mattina/pomeriggio/sera, le 24 ore di treni e uffici, A CHE ORA? / DALLE… ALLE…
Tutto in STAMPATELLO MAIUSCOLO. Gli orologi sono disegni SVG fatti qui (niente emoji come figure).
Uso: python3 _strumenti/unita_orologio.py → orologio/index.html (teoria) e orologio/esercizi.html.
I giochi (orologio/giochi.html) usano orologio/orologio.js, scritto a mano."""
import math, os, sys

sys.path.insert(0, os.path.dirname(__file__))
from genera import eq, has, build as build_esercizi
from slide import build as build_slide
from unita_primi import cover, slide, cards, table, nota, dialogo

# =====================================================================
# numeri e ore in parole
# =====================================================================
U = ["", "UNO", "DUE", "TRE", "QUATTRO", "CINQUE", "SEI", "SETTE", "OTTO", "NOVE", "DIECI", "UNDICI", "DODICI",
     "TREDICI", "QUATTORDICI", "QUINDICI", "SEDICI", "DICIASSETTE", "DICIOTTO", "DICIANNOVE"]
D = {2: "VENTI", 3: "TRENTA", 4: "QUARANTA", 5: "CINQUANTA"}

def numero(n):
    if n < 20: return U[n]
    d, u = divmod(n, 10)
    t = D[d]
    if u in (1, 8): t = t[:-1]
    return t + ("TRÉ" if u == 3 else U[u])

def ora_nome(h):
    """h = 1..12 → L'UNA, LE DUE…"""
    return "L'UNA" if h == 1 else "LE " + numero(h)

MIN_E = {5: "CINQUE", 10: "DIECI", 15: "UN QUARTO", 20: "VENTI", 25: "VENTICINQUE", 30: "MEZZA"}
MIN_MENO = {35: "VENTICINQUE", 40: "VENTI", 45: "UN QUARTO", 50: "DIECI", 55: "CINQUE"}

def parole(h, m, mezzogiorno=True):
    """La frase più naturale per un orologio con le lancette. h 0..23."""
    if m in MIN_MENO and m >= 40:
        h, coda = (h + 1) % 24, " MENO " + MIN_MENO[m]
    elif m == 0:
        coda = ""
    else:
        coda = " E " + (MIN_E.get(m) or numero(m))
    if mezzogiorno and h == 12: base = "MEZZOGIORNO"
    elif mezzogiorno and h in (0, 24): base = "MEZZANOTTE"
    else: base = ora_nome(h % 12 or 12)
    verbo = "È" if base in ("L'UNA", "MEZZOGIORNO", "MEZZANOTTE") else "SONO"
    return verbo + " " + base + coda

def varianti(h, m):
    """Tutte le risposte giuste (con e senza «SONO/È», e mezza/mezzo/trenta, ecc.) per l'ora h:m."""
    out = set()
    def base_list(hh):
        hh = hh % 24
        b = [ora_nome(hh % 12 or 12)]
        if hh == 12: b.append("MEZZOGIORNO")
        if hh == 0: b.append("MEZZANOTTE")
        if hh % 12 == 0: b += ["LE DODICI", "MEZZOGIORNO", "MEZZANOTTE"]
        return b
    code_e = [" E " + numero(m)] if m else [""]
    if m == 15: code_e.append(" E UN QUARTO")
    if m == 30: code_e += [" E MEZZA", " E MEZZO"]
    if m in MIN_E: code_e.append(" E " + MIN_E[m])
    for b in base_list(h):
        for c in code_e: out.add(b + c)
    if m >= 35:
        for b in base_list(h + 1):
            out.add(b + " MENO " + (MIN_MENO.get(m) or numero(60 - m)))
            if m == 45: out.add(b + " MENO UN QUARTO")
    res = set()
    for o in out:
        verbo = "È" if o.startswith(("L'UNA", "MEZZOGIORNO", "MEZZANOTTE")) else "SONO"
        res |= {o, verbo + " " + o}
    return sorted(res)

def cifre(h, m):
    """8:15 → ['8:15', '08:15', '20:15', ...] per le risposte con le cifre (orologio con le lancette: mattina o sera)."""
    out = []
    for hh in {h % 12, h % 12 + 12} | ({12, 0, 24} if h % 12 == 0 else set()):
        out += ["%d:%02d" % (hh, m), "%02d:%02d" % (hh, m)]
    return out

# =====================================================================
# disegni: orologio con le lancette e orologio digitale
# =====================================================================
def orologio(h, m, px=150, numeri=True, cls="clk"):
    a_m = m * 6
    a_h = (h % 12) * 30 + m * 0.5
    def punta(ang, r):
        x = 100 + r * math.sin(math.radians(ang)); y = 100 - r * math.cos(math.radians(ang))
        return "%.1f" % x, "%.1f" % y
    tacche = []
    for i in range(60):
        ang = math.radians(i * 6); r1 = 86 if i % 5 else 80
        tacche.append('<line x1="%.1f" y1="%.1f" x2="%.1f" y2="%.1f" stroke="#3B2410" stroke-width="%s"/>' % (
            100 + r1 * math.sin(ang), 100 - r1 * math.cos(ang), 100 + 91 * math.sin(ang), 100 - 91 * math.cos(ang),
            "3.5" if i % 5 == 0 else "1.2"))
    num = ""
    if numeri:
        for n in range(1, 13):
            ang = math.radians(n * 30)
            num += '<text x="%.1f" y="%.1f">%d</text>' % (100 + 67 * math.sin(ang), 100 - 67 * math.cos(ang) + 7, n)
    hx, hy = punta(a_h, 46); mx, my = punta(a_m, 74)
    return ('<svg class="%s" viewBox="0 0 200 200" width="%d" height="%d" role="img" aria-label="OROLOGIO">'
            '<circle cx="100" cy="100" r="96" fill="#fff" stroke="#E07A1F" stroke-width="7"/>%s'
            '<g font-family="Arial,sans-serif" font-size="21" font-weight="bold" fill="#3B2410" text-anchor="middle">%s</g>'
            '<line x1="100" y1="100" x2="%s" y2="%s" stroke="#c8323b" stroke-width="9" stroke-linecap="round"/>'
            '<line x1="100" y1="100" x2="%s" y2="%s" stroke="#2f63ad" stroke-width="5" stroke-linecap="round"/>'
            '<circle cx="100" cy="100" r="7" fill="#3B2410"/></svg>'
            % (cls, px, px, "".join(tacche), num, hx, hy, mx, my))

def digitale(h, m, grande=False):
    fs = "2.6rem" if grande else "1.6rem"
    return ('<span class="dig" style="display:inline-block; background:#1e2a22; color:#7CFC9A; font-family:\'Courier New\',monospace; '
            'font-weight:bold; font-size:%s; letter-spacing:2px; padding:4px 14px; border-radius:10px; border:3px solid #555;">%02d:%02d</span>'
            % (fs, h, m))

def q_orologio(n, h, m, px=110):
    return '<span style="display:inline-flex; align-items:center; gap:8px;"><b>%d.</b> %s</span>' % (n, orologio(h, m, px))

# =====================================================================
# TEORIA (slide)
# =====================================================================
CSS = """
  .orologi{display:grid; grid-template-columns:repeat(4,1fr); gap:14px;}
  .orologi div{background:#fff; border:3px solid #f3e1cc; border-radius:16px; padding:12px; text-align:center; font-size:1.25rem; font-weight:bold; line-height:1.3;}
  .orologi svg{display:block; margin:0 auto 8px; width:100%; max-width:150px; height:auto;}
  .orologi small{display:block; color:#8a6a4a; font-weight:normal; font-size:.95rem;}
  .orologi .dig{margin:4px 0 8px;}
  .duo{display:grid; grid-template-columns:auto 1fr; gap:30px; align-items:center;}
  .duo .big-clk svg{width:300px; height:auto;}
  .legenda{font-size:1.5rem; line-height:1.8;}
  .legenda .r{color:#c8323b; font-weight:bold;} .legenda .b{color:#2f63ad; font-weight:bold;}
  .tabellone{background:#0f1b2d; color:#ffd54a; font-family:'Courier New',monospace; border-radius:14px; padding:14px 18px; font-size:1.35rem; max-width:820px; overflow-x:auto;}
  .tabellone table{border-collapse:collapse; width:100%;} .tabellone th{color:#9fb3c8; text-align:left; font-size:1rem; padding:4px 10px; border-bottom:2px solid #33475f;}
  .tabellone td{padding:6px 10px; border-bottom:1px dashed #33475f; white-space:nowrap;}
  .cartello{background:#fff; border:5px solid var(--teal); border-radius:18px; padding:18px 24px; font-size:1.5rem; line-height:1.6; max-width:700px;}
  @media (max-width:900px){ .orologi{grid-template-columns:1fr 1fr;} .orologi div{font-size:1rem;} .duo{grid-template-columns:1fr; gap:12px;}
    .duo .big-clk svg{width:210px;} .legenda{font-size:1.1rem;} .tabellone{font-size:.95rem; padding:10px;} .cartello{font-size:1.1rem;} }"""

def orologi(items):
    """items: (h, m, testo, sotto) → griglia di orologi; tocchi e senti la frase."""
    out = '    <div class="orologi">\n'
    for h, m, t, sotto in items:
        out += '      <div data-say="%s">%s%s%s</div>\n' % (t.replace("<br>", " "), orologio(h, m), t,
                                                           "<small>%s</small>" % sotto if sotto else "")
    return out + "    </div>"

def digitali(items):
    out = '    <div class="orologi">\n'
    for h, m, t, sotto in items:
        out += '      <div data-say="%s">%s<br>%s%s</div>\n' % (t, digitale(h, m), t, "<small>%s</small>" % sotto if sotto else "")
    return out + "    </div>"

def fine():
    return ('  <section class="slide center cover">\n    <div class="big">🎉</div>\n    <h1>BRAVI!</h1>\n'
            '    <p class="lead" style="margin-top:14px;">ORA SAI LEGGERE L\'OROLOGIO E GLI ORARI!</p>\n'
            '    <a class="badge" href="esercizi.html" style="text-decoration:none">ADESSO FACCIAMO GLI ESERCIZI 📱</a>\n'
            '    <a class="badge" href="giochi.html" style="text-decoration:none">🎲 I GIOCHI CON L\'OROLOGIO</a>\n'
            '  </section>')

SLIDE = [
    cover("🕰️", "L'OROLOGIO: CHE ORE SONO?", "SONO LE TRE E UN QUARTO. A CHE ORA PARTE IL TRENO?", "A1 &bull; LE LANCETTE &bull; E / MENO &bull; GLI ORARI"),
    slide("CHE COSA IMPARIAMO?", cards([
        ("🕰️", "LEGGERE L'OROLOGIO", "LA LANCETTA CORTA E LA LANCETTA LUNGA"),
        ("❓", "CHIEDERE L'ORA", "CHE ORE SONO? → SONO LE CINQUE."),
        ("➕", "E · MENO · UN QUARTO · MEZZA", "LE TRE E MEZZA, LE QUATTRO MENO UN QUARTO"),
        ("🚆", "GLI ORARI", "IL TRENO PARTE ALLE 14:35. L'UFFICIO È APERTO DALLE 9 ALLE 13.")])),
    slide("🕰️ L'OROLOGIO CON LE LANCETTE",
          '    <div class="duo">\n      <div class="big-clk" data-say="sono le dieci e dieci">%s</div>\n'
          '      <div class="legenda" data-say="la lancetta corta indica le ore. la lancetta lunga indica i minuti.">'
          '<span class="r">▬ LA LANCETTA CORTA E GROSSA</span> = LE <b>ORE</b><br>'
          '<span class="b">▬▬ LA LANCETTA LUNGA E SOTTILE</span> = I <b>MINUTI</b><br><br>'
          '1 ORA = 60 MINUTI<br>MEZZ\'ORA = 30 MINUTI<br>UN QUARTO D\'ORA = 15 MINUTI<br><br>'
          'QUI: SONO LE <b>DIECI</b> E <b>DIECI</b>.</div>\n    </div>' % orologio(10, 10, 300)),
    slide("📱 L'OROLOGIO DIGITALE",
          '    <div class="duo">\n      <div class="big-clk">%s</div>\n      <div class="legenda">%s<br><br>'
          'PRIMA LE <b>ORE</b> : POI I <b>MINUTI</b><br>8:15 = LE OTTO E QUINDICI<br>= LE OTTO E UN QUARTO</div>\n    </div>\n'
          % (orologio(8, 15, 300), digitale(8, 15, True)) +
          nota("SUL TELEFONO, SUL COMPUTER, IN STAZIONE L'OROLOGIO È <b>DIGITALE</b>: SOLO NUMERI.")),
    slide("❓ COME CHIEDO L'ORA?", dialogo([
        ("KOFI", "SCUSI, <b>CHE ORE SONO</b>?"), ("*SIGNORA", "SONO LE DUE."),
        ("LEILA", "SCUSA, <b>CHE ORA È</b>?"), ("*PEDRO", "È L'UNA.")]) + "\n" +
        nota("CHE ORE SONO? = CHE ORA È? &nbsp; LE DUE DOMANDE SONO UGUALI.<br>CON UNA PERSONA CHE NON CONOSCI: <b>SCUSI</b>, CHE ORE SONO?")),
    slide("📘 LA REGOLA: È O SONO?", table([
        ["1", "<b>È</b> L'UNA"], ["12:00", "<b>È</b> MEZZOGIORNO"], ["24:00", "<b>È</b> MEZZANOTTE"],
        ["2, 3, 4, 5…", "<b>SONO</b> LE DUE, LE TRE, LE QUATTRO, LE CINQUE…"]], head=["L'ORA", "SI DICE"]) + "\n" +
        nota("L'UNA = 1 ORA → <b>È</b> (SINGOLARE). &nbsp; LE DUE, LE TRE… = TANTE ORE → <b>SONO</b> (PLURALE).")),
    slide("🕐 LE ORE ESATTE", orologi([
        (1, 0, "È L'UNA", ""), (2, 0, "SONO LE DUE", ""), (4, 0, "SONO LE QUATTRO", ""), (6, 0, "SONO LE SEI", ""),
        (7, 0, "SONO LE SETTE", ""), (9, 0, "SONO LE NOVE", ""), (11, 0, "SONO LE UNDICI", ""), (12, 0, "È MEZZOGIORNO", "O MEZZANOTTE")]) + "\n" +
        nota("LA LANCETTA LUNGA È SUL 12 → ORA ESATTA.", "margin-top:14px;")),
    slide("➕ E · DOPO L'ORA (DA 1 A 30 MINUTI)", orologi([
        (3, 5, "LE TRE E CINQUE", ""), (3, 10, "LE TRE E DIECI", ""), (3, 15, "LE TRE E UN QUARTO", "= E QUINDICI"),
        (3, 20, "LE TRE E VENTI", ""), (3, 25, "LE TRE E VENTICINQUE", ""), (3, 30, "LE TRE E MEZZA", "= E TRENTA")]) + "\n" +
        nota("ORA + <b>E</b> + MINUTI. &nbsp; LA LANCETTA LUNGA È A DESTRA (DAL 12 AL 6).", "margin-top:14px;")),
    slide("➖ MENO · PRIMA DELL'ORA DOPO", orologi([
        (3, 40, "LE QUATTRO MENO VENTI", "= LE TRE E QUARANTA"), (3, 45, "LE QUATTRO MENO UN QUARTO", "= LE TRE E QUARANTACINQUE"),
        (3, 50, "LE QUATTRO MENO DIECI", "= LE TRE E CINQUANTA"), (3, 55, "LE QUATTRO MENO CINQUE", "= LE TRE E CINQUANTACINQUE")]) + "\n" +
        nota("DOPO LA MEZZA GUARDO L'ORA <b>DOPO</b> E DICO QUANTO MANCA: <b>MENO</b>.<br>"
             "3:45 → MANCANO 15 MINUTI ALLE 4 → LE QUATTRO <b>MENO UN QUARTO</b>.", "margin-top:14px;")),
    slide("📘 LA REGOLA IN BREVE", table([
        [":00", "SONO LE TRE", "—"], [":15", "LE TRE <b>E UN QUARTO</b>", "E QUINDICI"], [":30", "LE TRE <b>E MEZZA</b>", "E TRENTA"],
        [":45", "LE QUATTRO <b>MENO UN QUARTO</b>", "LE TRE E QUARANTACINQUE"], [":50", "LE QUATTRO <b>MENO DIECI</b>", "LE TRE E CINQUANTA"]],
        head=["MINUTI", "SI DICE", "SI PUÒ DIRE ANCHE"]) + "\n" +
        nota("UN QUARTO = 15 MINUTI &nbsp;&nbsp; MEZZA = 30 MINUTI &nbsp;&nbsp; UN QUARTO D'ORA, MEZZ'ORA, UN'ORA")),
    slide("🌅 MATTINA, POMERIGGIO, SERA, NOTTE", table([
        ["🌅 DI MATTINA", "6:00 – 12:00", "SONO LE OTTO <b>DI MATTINA</b>"], ["☀️ DEL POMERIGGIO", "13:00 – 18:00", "SONO LE TRE <b>DEL POMERIGGIO</b>"],
        ["🌆 DI SERA", "18:00 – 23:00", "SONO LE NOVE <b>DI SERA</b>"], ["🌙 DI NOTTE", "24:00 – 5:00", "SONO LE DUE <b>DI NOTTE</b>"]],
        head=["QUANDO?", "ORE", "ESEMPIO"]) + "\n" +
        nota("L'OROLOGIO CON LE LANCETTE HA SOLO 12 ORE: 3:00 = LE TRE DI NOTTE O LE TRE DEL POMERIGGIO.")),
    slide("🔢 LE 24 ORE", digitali([
        (13, 0, "LE TREDICI", "= L'UNA DEL POMERIGGIO"), (15, 0, "LE QUINDICI", "= LE TRE DEL POMERIGGIO"),
        (18, 30, "LE DICIOTTO E TRENTA", "= LE SEI E MEZZA DI SERA"), (20, 0, "LE VENTI", "= LE OTTO DI SERA"),
        (21, 15, "LE VENTUNO E QUINDICI", "= LE NOVE E UN QUARTO DI SERA"), (0, 0, "MEZZANOTTE", "= LE VENTIQUATTRO")]) + "\n" +
        nota("DOPO MEZZOGIORNO: ORA + 12. &nbsp; 3 DEL POMERIGGIO → 3 + 12 = <b>15</b>.", "margin-top:14px;")),
    slide("🚆 GLI ORARI DEL TRENO",
          '    <div class="tabellone"><b>🚉 BARI CENTRALE · PARTENZE</b><table>'
          '<tr><th>ORA</th><th>DESTINAZIONE</th><th>BINARIO</th></tr>'
          '<tr><td>07:05</td><td>FOGGIA</td><td>2</td></tr><tr><td>09:40</td><td>LECCE</td><td>4</td></tr>'
          '<tr><td>13:15</td><td>TARANTO</td><td>1</td></tr><tr><td>17:50</td><td>MONOPOLI</td><td>3</td></tr></table></div>\n' +
          nota("NEGLI ORARI DI TRENI, AUTOBUS E UFFICI USO <b>LE 24 ORE</b> E DICO I MINUTI CON IL NUMERO:<br>"
               "17:50 → IL TRENO PARTE <b>ALLE DICIASSETTE E CINQUANTA</b>.")),
    slide("⏰ A CHE ORA?", dialogo([
        ("YUSUF", "<b>A CHE ORA</b> COMINCIA IL CORSO?"), ("*MARTA", "<b>ALLE</b> NOVE E MEZZA."),
        ("YUSUF", "E A CHE ORA FINISCE?"), ("*MARTA", "<b>A</b> MEZZOGIORNO. IL GIOVEDÌ FINISCE <b>ALL'</b>UNA.")]) + "\n" +
        table([["ALLE", "ALLE DUE, ALLE OTTO E MEZZA, ALLE 14:35"], ["ALL'", "ALL'UNA"], ["A", "A MEZZOGIORNO, A MEZZANOTTE"]],
              head=["A CHE ORA?", "ESEMPIO"])),
    slide("🏢 DALLE… ALLE…",
          '    <div class="cartello">📮 <b>UFFICIO POSTALE</b><br>LUNEDÌ – VENERDÌ: 8:20 – 13:35<br>SABATO: 8:20 – 12:35<br>DOMENICA: <b>CHIUSO</b></div>\n' +
          nota("L'UFFICIO È APERTO <b>DALLE</b> OTTO E VENTI <b>ALLE</b> TREDICI E TRENTACINQUE.<br>"
               "DAL LUNEDÌ AL VENERDÌ. LA DOMENICA È <b>CHIUSO</b>.")),
    slide("💬 IN STAZIONE", dialogo([
        ("ANNA", "SCUSI, A CHE ORA PARTE IL TRENO PER LECCE?"), ("*IMPIEGATO", "ALLE 9:40, DAL BINARIO 4."),
        ("ANNA", "CHE ORE SONO ADESSO?"), ("*IMPIEGATO", "SONO LE NOVE E UN QUARTO."),
        ("ANNA", "ALLORA HO ANCORA VENTICINQUE MINUTI. GRAZIE!"), ("*IMPIEGATO", "PREGO, BUON VIAGGIO!")])),
    fine(),
]

# =====================================================================
# ESERCIZI
# =====================================================================
def tutte(*ore):
    return [eq(*varianti(h, m)) for h, m in ore]

T1 = ("<p>L'OROLOGIO HA DUE LANCETTE:</p><p>LA LANCETTA <b>CORTA E GROSSA</b> = LE <b>ORE</b><br>LA LANCETTA <b>LUNGA E SOTTILE</b> = I <b>MINUTI</b></p>"
      "<p>1 ORA = 60 MINUTI. &nbsp; SUL TELEFONO SCRIVO PRIMA LE ORE, POI I MINUTI: <b>8:15</b></p>")
T2 = ("<table><tr><th>1</th><td><b>È</b> L'UNA</td></tr><tr><th>12:00 · 24:00</th><td><b>È</b> MEZZOGIORNO · <b>È</b> MEZZANOTTE</td></tr>"
      "<tr><th>2, 3, 4…</th><td><b>SONO</b> LE DUE, LE TRE, LE QUATTRO…</td></tr></table>")
T3 = ("<p>DA 1 A 30 MINUTI → <b>E</b>: LE TRE <b>E</b> DIECI, LE TRE <b>E UN QUARTO</b> (15), LE TRE <b>E MEZZA</b> (30)</p>"
      "<p>DOPO 30 MINUTI → L'ORA DOPO + <b>MENO</b>: 3:45 = LE QUATTRO <b>MENO UN QUARTO</b> · 3:50 = LE QUATTRO <b>MENO DIECI</b></p>")
T4 = ("<table><tr><th>DI MATTINA</th><td>6:00 – 12:00</td></tr><tr><th>DEL POMERIGGIO</th><td>13:00 – 18:00</td></tr>"
      "<tr><th>DI SERA</th><td>18:00 – 23:00</td></tr><tr><th>DI NOTTE</th><td>24:00 – 5:00</td></tr></table>"
      "<p>LE 24 ORE: DOPO MEZZOGIORNO ORA + 12 → LE TRE DEL POMERIGGIO = <b>15:00</b></p>")
T5 = ("<p>A CHE ORA? → <b>ALLE</b> NOVE · <b>ALL'</b>UNA · <b>A</b> MEZZOGIORNO · <b>A</b> MEZZANOTTE</p>"
      "<p>QUANDO È APERTO? → <b>DALLE</b> 9 <b>ALLE</b> 13</p>"
      "<p>NEGLI ORARI (TRENI, UFFICI) USO LE 24 ORE: 14:35 = LE QUATTORDICI E TRENTACINQUE</p>")

E1 = [(3, 0), (9, 0), (6, 30), (10, 15), (2, 45), (11, 50)]
E4 = [(5, 30), (8, 15), (1, 0), (6, 45), (12, 0), (9, 20)]
E4_OPTS = [parole(h, m) for h, m in E4]
E6 = [(7, 30), (4, 15), (12, 0), (9, 45), (1, 10), (5, 50)]
TABELLONE = ('<div style="background:#0f1b2d; color:#ffd54a; font-family:\'Courier New\',monospace; border-radius:12px; padding:10px 12px; overflow-x:auto;">'
             '<b>🚉 BARI CENTRALE · PARTENZE</b><table style="border-collapse:collapse; width:100%; margin-top:6px;">'
             '<tr style="color:#9fb3c8;"><th style="text-align:left; padding:3px 8px;">ORA</th><th style="text-align:left; padding:3px 8px;">DESTINAZIONE</th><th style="text-align:left; padding:3px 8px;">BINARIO</th></tr>'
             + "".join('<tr><td style="padding:3px 8px;">%s</td><td style="padding:3px 8px;">%s</td><td style="padding:3px 8px;">%s</td></tr>' % r for r in [
                 ("06:50", "BARLETTA", "5"), ("08:25", "FOGGIA", "2"), ("12:10", "MONOPOLI", "3"),
                 ("14:35", "LECCE", "4"), ("16:45", "TARANTO", "1"), ("21:05", "FOGGIA", "2")]) +
             "</table></div>")

ESERCIZI = {
 "title": "🕰️ L'orologio: che ore sono? · Esercizi",
 "store": "orologio",
 "upper": True,
 "sub": "GUARDA L'OROLOGIO, SCRIVI O SCEGLI E PREMI «CONTROLLA» ALLA FINE DI OGNI ESERCIZIO. LE RISPOSTE RESTANO SALVATE SU QUESTO TELEFONO.",
 "sections": [
  {"part": "L'orologio", "teoria": T1},
  {"id": "e1", "title": "1 · Che ore sono? Scrivi con i numeri", "short": "1 · Con i numeri", "type": "text", "w": "s",
   "cons": "GUARDA L'OROLOGIO E SCRIVI L'ORA COME SUL TELEFONO. ESEMPIO: 7:00",
   "items": [{"q": q_orologio(i, h, m), "ph": "0:00"} for i, (h, m) in enumerate(E1, 1)],
   "k": [eq(*cifre(h, m)) for h, m in E1]},
  {"id": "e2", "title": "2 · La lancetta corta o la lancetta lunga?", "short": "2 · Le lancette", "type": "choice", "full": True,
   "opts": ["LA LANCETTA CORTA", "LA LANCETTA LUNGA"],
   "items": [{"q": q} for q in ["1. INDICA LE ORE.", "2. INDICA I MINUTI.", "3. ALLE 6:00 È SUL 12.", "4. ALLE 6:00 È SUL 6.", "5. IN UN'ORA FA UN GIRO INTERO."]],
   "k": [eq(a) for a in ["LA LANCETTA CORTA", "LA LANCETTA LUNGA", "LA LANCETTA LUNGA", "LA LANCETTA CORTA", "LA LANCETTA LUNGA"]]},

  {"part": "È l'una · Sono le due", "teoria": T2},
  {"id": "e3", "title": "3 · È o SONO?", "short": "3 · È o sono", "type": "choice",
   "opts": ["È", "SONO"],
   "items": [{"q": q} for q in ["1. … LE CINQUE.", "2. … L'UNA E MEZZA.", "3. … MEZZANOTTE.", "4. … LE DUE MENO UN QUARTO.",
                                 "5. … MEZZOGIORNO E UN QUARTO.", "6. … LE DIECI E VENTI.", "7. … L'UNA MENO CINQUE."]],
   "k": [eq(a) for a in ["SONO", "È", "È", "SONO", "È", "SONO", "È"]]},

  {"part": "E · meno · un quarto · mezza", "teoria": T3},
  {"id": "e4", "title": "4 · Guarda l'orologio e scegli", "short": "4 · Scegli l'ora", "type": "select",
   "opts": sorted(E4_OPTS),
   "items": [{"q": q_orologio(i, h, m)} for i, (h, m) in enumerate(E4, 1)],
   "k": [eq(a) for a in E4_OPTS]},
  {"id": "e5", "title": "5 · E o MENO?", "short": "5 · E o meno", "type": "choice",
   "opts": ["E", "MENO"],
   "items": [{"q": "%d. %s → %s" % (i, digitale(h, mm), t)} for i, (h, mm, t) in enumerate([
       (4, 20, "SONO LE QUATTRO … VENTI"), (6, 50, "SONO LE SETTE … DIECI"), (8, 15, "SONO LE OTTO … UN QUARTO"),
       (1, 45, "SONO LE DUE … UN QUARTO"), (11, 30, "SONO LE UNDICI … MEZZA"), (9, 55, "SONO LE DIECI … CINQUE")], 1)],
   "k": [eq(a) for a in ["E", "MENO", "E", "MENO", "E", "MENO"]]},
  {"id": "e6", "title": "6 · Scrivi l'ora con le parole", "short": "6 · Con le parole", "type": "text", "w": "w",
   "cons": "ESEMPIO: 4:30 → SONO LE QUATTRO E MEZZA",
   "items": [{"q": q_orologio(i, h, m)} for i, (h, m) in enumerate(E6, 1)],
   "k": tutte(*E6)},

  {"part": "Mattina, pomeriggio, sera · le 24 ore", "teoria": T4},
  {"id": "e7", "title": "7 · Che ore sono? Scegli", "short": "7 · Le 24 ore", "type": "select",
   "opts": ["LE SETTE DI MATTINA", "L'UNA E UN QUARTO DEL POMERIGGIO", "LE TRE DEL POMERIGGIO", "LE OTTO E MEZZA DI SERA", "LE UNDICI DI SERA", "LE DUE DI NOTTE"],
   "items": [{"q": "%d. %s" % (i, digitale(h, m))} for i, (h, m) in enumerate([(15, 0), (20, 30), (7, 0), (23, 0), (13, 15), (2, 0)], 1)],
   "k": [eq(a) for a in ["LE TRE DEL POMERIGGIO", "LE OTTO E MEZZA DI SERA", "LE SETTE DI MATTINA", "LE UNDICI DI SERA",
                         "L'UNA E UN QUARTO DEL POMERIGGIO", "LE DUE DI NOTTE"]]},
  {"id": "e8", "title": "8 · Scrivi con i numeri (24 ore)", "short": "8 · Scrivi 24 ore", "type": "text", "w": "s",
   "cons": "ESEMPIO: LE TRE DEL POMERIGGIO → 15:00",
   "items": [{"q": q, "ph": "0:00"} for q in ["1. LE NOVE DI SERA", "2. LE QUATTRO DEL POMERIGGIO", "3. LE SEI E MEZZA DI MATTINA",
                                               "4. MEZZOGIORNO", "5. LE CINQUE E UN QUARTO DEL POMERIGGIO", "6. LE OTTO MENO DIECI DI SERA"]],
   "k": [eq("21:00", "21"), eq("16:00", "16"), eq("6:30", "06:30"), eq("12:00", "12"), eq("17:15"), eq("19:50")]},

  {"part": "Gli orari: treni e uffici", "teoria": T5},
  {"id": "e9", "title": "9 · Leggi il tabellone della stazione", "short": "9 · Il tabellone", "type": "text", "w": "m",
   "cons": "GUARDA LE PARTENZE E RISPONDI. PUOI SCRIVERE CON I NUMERI. ESEMPIO: ALLE 6:50",
   "info": TABELLONE,
   "items": [{"q": q} for q in ["1. A CHE ORA PARTE IL TRENO PER LECCE?", "2. A CHE ORA PARTE IL TRENO PER TARANTO?",
                                 "3. QUALE TRENO PARTE ALLE 12:10?", "4. DA QUALE BINARIO PARTE IL TRENO PER LECCE?",
                                 "5. KOFI VUOLE ANDARE A FOGGIA LA SERA. A CHE ORA PARTE?"]],
   "k": [has("14:35", "14 35", "quattordici e trentacinque", "due e trentacinque"),
         has("16:45", "16 45", "sedici e quarantacinque", "cinque meno un quarto"),
         has("monopoli"), has("4", "quattro"),
         has("21:05", "21 05", "ventuno e cinque", "nove e cinque")]},
  {"id": "e10", "title": "10 · ALLE, ALL', A, DALLE?", "short": "10 · Alle, all', a", "type": "cloze",
   "cons": "COMPLETA CON: ALLE · ALL' · A · DALLE",
   "parts": ["1. IL CORSO COMINCIA ", {}, " NOVE.<br>2. GIOVANNI FINISCE DI LAVORARE ", {}, "UNA.<br>3. PRANZIAMO ",
             {}, " MEZZOGIORNO.<br>4. IL NEGOZIO È APERTO ", {}, " 9 ", {}, " 13.<br>5. LEILA VA A DORMIRE ",
             {}, " MEZZANOTTE.<br>6. IL TRENO PARTE ", {}, " 14:35."],
   "k": [eq("alle"), eq("all'", "all"), eq("a"), eq("dalle"), eq("alle"), eq("a"), eq("alle")]},
  {"id": "e11", "title": "11 · L'orario dell'ufficio postale", "short": "11 · Vero o falso", "type": "choice",
   "opts": ["VERO", "FALSO"], "full": True,
   "info": "📮 <b>UFFICIO POSTALE</b><br>LUNEDÌ – VENERDÌ: 8:20 – 13:35<br>SABATO: 8:20 – 12:35<br>DOMENICA: <b>CHIUSO</b>",
   "items": [{"q": q} for q in ["1. IL LUNEDÌ APRE ALLE OTTO E VENTI.", "2. LA DOMENICA È CHIUSO.", "3. IL MARTEDÌ ALLE 15:00 È APERTO.",
                                 "4. IL SABATO CHIUDE PRIMA.", "5. IL VENERDÌ CHIUDE ALLE TREDICI E TRENTACINQUE.", "6. IL SABATO APRE ALLE NOVE."]],
   "k": [eq(a) for a in ["VERO", "VERO", "FALSO", "VERO", "VERO", "FALSO"]]},
  {"id": "e12", "title": "12 ✎ · La mia giornata", "type": "free", "rows": 5,
   "items": ["A CHE ORA TI SVEGLI? A CHE ORA MANGI? A CHE ORA VAI AL CORSO O AL LAVORO? A CHE ORA VAI A DORMIRE?<br>"
             "ESEMPIO: MI SVEGLIO ALLE SETTE. VADO AL CORSO ALLE NOVE E MEZZA. PRANZO ALL'UNA."]},
 ]
}

PATH_SLIDE = "orologio/index.html"
SLIDE_OROLOGIO = [(PATH_SLIDE, "L'OROLOGIO", "A1 &bull; CHE ORE SONO?", SLIDE, CSS)]

if __name__ == "__main__":
    for path, unit, topbar, slides, css in SLIDE_OROLOGIO:
        build_slide(path, unit, topbar, slides, css)
        t = open(path, encoding="utf-8").read()
        tag = '<script src="../comune/stampa.js?v=20261127"></script>\n'
        while t.count(tag) > 1:  # il modello ha già lo script della stampa
            i = t.rindex(tag); t = t[:i] + t[i + len(tag):]
        open(path, "w", encoding="utf-8").write(t)
    build_esercizi("orologio/esercizi.html", ESERCIZI)
