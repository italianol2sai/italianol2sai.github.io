"""Ritratti SVG dei nuovi operatori delle escape room per argomento (2026-10-30, Erila: «usa nomi degli operatori diversi,
tipo Giovanni, Cristian, Michele, Silvia (un'altra), Saleah, Eneida»). Stesso stile dei ritratti di missione-casa e missione-lavoro.
Usato da missioni.py: OPERATORI_JS viene aggiunto a persone.js."""

def ritratto(k, sfondo, pelle, ombra, capelli, maglia, stile, barba=False, occhiali=False, orecchini=None, occhi="#3A2416"):
    p = ['<svg xmlns="http://www.w3.org/2000/svg" viewBox="16 16 68 68" aria-hidden="true" focusable="false">'
         '<defs><clipPath id="%s-c"><circle cx="50" cy="50" r="34"/></clipPath></defs><g clip-path="url(#%s-c)">' % (k, k),
         '<rect width="100" height="100" fill="%s"/>' % sfondo]
    if stile == "lunghi":
        p.append('<path d="M50 28 Q30 28 31 50 Q29 64 27 80 L73 80 Q71 64 69 50 Q70 28 50 28 Z" fill="%s"/>' % capelli)
    if stile == "chignon":
        p.append('<circle cx="50" cy="27" r="9" fill="%s"/>' % capelli)
    if stile == "mossi":
        p.append('<g fill="%s"><circle cx="33" cy="48" r="9"/><circle cx="67" cy="48" r="9"/><circle cx="31" cy="62" r="8"/><circle cx="69" cy="62" r="8"/>'
                 '<circle cx="34" cy="73" r="6"/><circle cx="66" cy="73" r="6"/><circle cx="50" cy="32" r="16"/></g>' % capelli)
    p.append('<path d="M16 100 Q18 82 38 79 L62 79 Q82 82 84 100 Z" fill="%s"/>' % maglia)
    p.append('<path d="M41 79 Q50 87 59 79" fill="%s"/>' % ombra)
    p.append('<rect x="43" y="66" width="14" height="15" rx="5" fill="%s"/>' % ombra)
    p.append('<ellipse cx="50" cy="52" rx="16" ry="19" fill="%s"/>' % pelle)
    if stile in ("corti", "rasati", "calvo"):
        p.append('<ellipse cx="34" cy="54" rx="3" ry="4.5" fill="%s"/><ellipse cx="66" cy="54" rx="3" ry="4.5" fill="%s"/>' % (ombra, ombra))
    tetto = {
        "corti": '<path d="M34 50 Q31 30 50 30 Q69 30 66 50 Q64 40 57 38 Q50 41 42 38 Q36 41 34 50 Z" fill="%s"/>',
        "rasati": '<path d="M34.5 48 Q34 32 50 32 Q66 32 65.5 48 Q63 40 50 39 Q37 40 34.5 48 Z" fill="%s" opacity=".85"/>',
        "calvo": '<path d="M34 54 Q33 44 36 41 L37 52 Z M66 54 Q67 44 64 41 L63 52 Z" fill="%s"/>',
        "lunghi": '<path d="M34 50 Q32 31 50 31 Q68 31 66 50 Q60 38 50 37 Q42 39 34 50 Z" fill="%s"/>',
        "chignon": '<path d="M34 49 Q33 33 50 33 Q67 33 66 49 Q62 39 50 39 Q38 39 34 49 Z" fill="%s"/>',
        "turbante": '<path d="M33 50 Q30 26 50 24 Q70 26 67 50 Q64 38 50 37 Q36 38 33 50 Z" fill="%s"/><path d="M38 33 Q50 27 62 33 M36 40 Q50 33 64 40" stroke="#fff" stroke-opacity=".45" stroke-width="1.6" fill="none"/>',
        "mossi": '<path d="M34 49 Q34 33 50 33 Q66 33 66 49 Q62 40 54 39 Q50 43 46 39 Q38 40 34 49 Z" fill="%s"/>',
    }[stile]
    p.append(tetto % capelli)
    if barba:
        p.append('<path d="M34.5 55 Q35 71 50 72 Q65 71 65.5 55 Q63 63 57 61.5 Q50 60 43 61.5 Q37 63 34.5 55 Z" fill="%s" opacity=".9"/>' % capelli)
    p.append('<path d="M39 45 Q43 43.5 46 45 M54 45 Q57 43.5 61 45" stroke="%s" stroke-width="1.7" fill="none" stroke-linecap="round"/>' % capelli)
    p.append('<ellipse cx="43" cy="51" rx="2.3" ry="2.6" fill="%s"/><ellipse cx="57" cy="51" rx="2.3" ry="2.6" fill="%s"/>'
             '<circle cx="43.7" cy="50.2" r=".7" fill="#fff"/><circle cx="57.7" cy="50.2" r=".7" fill="#fff"/>' % (occhi, occhi))
    p.append('<path d="M50 52 Q51.5 58 49 59" stroke="%s" stroke-width="1.3" fill="none" stroke-linecap="round"/>' % ombra)
    p.append('<path d="M44.5 63.5 Q50 67 55.5 63.5" stroke="#A04A3E" stroke-width="1.8" fill="none" stroke-linecap="round"/>')
    if occhiali:
        p.append('<g fill="none" stroke="#1F2A36" stroke-width="1.4"><circle cx="43" cy="51" r="5"/><circle cx="57" cy="51" r="5"/>'
                 '<path d="M48 50.5 L52 50.5 M38 50.5 L34.5 49.5 M62 50.5 L65.5 49.5"/></g>')
    if orecchini:
        p.append('<circle cx="34.5" cy="59" r="1.8" fill="%s"/><circle cx="65.5" cy="59" r="1.8" fill="%s"/>' % (orecchini, orecchini))
    p.append('</g></svg>')
    return "".join(p)

OPERATORI = {
 "giovanni": ("GIOVANNI", "OPERATORE · SAI BARI", ritratto("gv", "#FCE9D2", "#EBC3A0", "#D3A27E", "#4A2E1E", "#D9822B", "corti", barba=True)),
 "cristian": ("CRISTIAN", "OPERATORE · SAI BARI", ritratto("cr", "#DDEFF0", "#E2B48E", "#C99670", "#1E1A18", "#C0392B", "rasati")),
 "michele":  ("MICHELE", "OPERATORE · SAI BARI", ritratto("mi", "#E4F2E0", "#F0CBAA", "#D6A784", "#6E5A4A", "#3F7F4F", "calvo", barba=True, occhiali=True)),
 "silvia2":  ("SILVIA", "OPERATRICE · SAI BARI", ritratto("s2", "#EFE3F6", "#F2CFB4", "#D9AE8E", "#C9A04E", "#7B4FA0", "lunghi", orecchini="#E7C35A", occhi="#4E7A9E")),
 "saleah":   ("SALEAH", "OPERATRICE · SAI BARI", ritratto("sa", "#FFF1D6", "#B47A55", "#966042", "#1B120D", "#E0A21B", "chignon", orecchini="#C9A227")),
 "eneida":   ("ENEIDA", "COORDINATRICE · SAI BARI", ritratto("en", "#E0F0F4", "#EFC6A6", "#D4A381", "#8A3B1E", "#2A8C8C", "mossi", occhi="#4C6B3A")),
}

# Protagonisti (Erila: «usa anche altri nomi inventati dei protagonisti, sempre nomi stranieri, etnie diverse»)
PROTAGONISTI = {
 "kwame":   ("KWAME", "24 ANNI · GHANA", ritratto("kw", "#E8F1DC", "#7A4A2E", "#61391F", "#141010", "#2D6CB5", "rasati")),
 "fatou":   ("FATOU", "29 ANNI · SENEGAL", ritratto("fa", "#FFE9DF", "#6E4228", "#56321C", "#D1495B", "#F2A93B", "turbante", orecchini="#F2C14E")),
 "lin":     ("LIN", "31 ANNI · CINA", ritratto("li", "#FDEFF3", "#F3D2B3", "#DDB08C", "#16110F", "#C2185B", "lunghi")),
 "ravi":    ("RAVI", "27 ANNI · INDIA", ritratto("ra", "#EAE6F7", "#B98257", "#9C673F", "#16110F", "#5C6BC0", "corti", barba=True)),
 "mariela": ("MARIELA", "22 ANNI · PERÙ", ritratto("me", "#E3F4EC", "#C8936B", "#AE7A53", "#3B2416", "#E64A19", "mossi", orecchini="#E7C35A", occhi="#2B1A12")),
 "tesfaye": ("TESFAYE", "33 ANNI · ERITREA", ritratto("te", "#F6EBDD", "#8A5634", "#6F4226", "#1A1310", "#00897B", "corti", occhiali=True)),
}

OPERATORI_JS = ",\n".join('  %s: { nome: "%s", ruolo: "%s", svg: \'%s\' }' % (k, n, r, s) for k, (n, r, s) in list(OPERATORI.items()) + list(PROTAGONISTI.items()))
