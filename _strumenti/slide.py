"""Crea le presentazioni a slide (stile di saluti/index.html) a partire da una lista di slide in HTML.
Uso: python3 _strumenti/slide.py   (dalla cartella principale del sito)"""
import os, re, sys

sys.path.insert(0, os.path.dirname(__file__))
MODELLO = "saluti/index.html"
# tocca una parola, un fumetto o una riga: la voce del computer la legge (in minuscolo, senza emoji)
SAY = r"""<script>
(function(){
  const sel='.bubble, .card, .cartelli div, .orologi div, .mondo div, .regola div, table.plur td, .nota, .lead, .big2';
  document.querySelectorAll(sel).forEach(e=>e.classList.add('parla'));
  document.addEventListener('click',ev=>{ const d=ev.target.closest('[data-say], .parla'); if(!d||!window.speechSynthesis||ev.target.closest('a,button')) return;
    ev.stopPropagation();
    const t=(d.dataset.say||d.innerText).replace(/[\u{1F000}-\u{1FFFF}\u{2600}-\u{27BF}\u{2B00}-\u{2BFF}\uFE0F\u200D]/gu,' ').replace(/[←→▶◀•…_]/g,' ').toLowerCase();
    const u=new SpeechSynthesisUtterance(t); u.lang='it-IT'; u.rate=.85; speechSynthesis.cancel(); speechSynthesis.speak(u);
    document.querySelectorAll('.parlando').forEach(x=>x.classList.remove('parlando')); d.classList.add('parlando');
    u.onend=()=>d.classList.remove('parlando'); });
})();
</script>"""
# parole lunghe (FRUTTIVENDOLO, SUPERMERCATO…) sul telefono
COMUNE = """
  .parla, [data-say]{cursor:pointer;} .bubble.parla::after, .card.parla b::after{content:" 🔊"; font-size:.8em; opacity:.55;}
  .parlando{outline:4px solid var(--arancio); outline-offset:2px;}
  .card, .card b, .cover h1, .bubble, table.plur td{overflow-wrap:anywhere;}
  @media (max-width:900px){ .cover h1{font-size:2.1rem;} .card b{font-size:1.05rem;} .card{padding:12px;} }
  @media (max-width:520px){ .g3{grid-template-columns:1fr;} .g3 .card{flex-direction:row; flex-wrap:wrap; align-items:center; column-gap:12px;} .g3 .card .emoji{font-size:2rem;} .g3 .card span:last-child{flex-basis:100%;} }"""

def build(path, unit, topbar, slides, css=""):
    src = open(MODELLO, encoding="utf-8").read()
    head = src[:src.index('<div class="topbar">')]
    tail = src[src.index('<div class="controls">'):]
    head = re.sub(r"<title>.*?</title>", "<title>%s - ITALIANO L2</title>" % unit, head)
    head = head.replace("</style>", COMUNE + css + "\n</style>")
    body = ('<div class="topbar">\n  <span class="unit">ITALIANO L2 &bull; %s</span>\n  <span>%s</span>\n</div>\n'
            '<div class="progress"><div id="bar"></div></div>\n\n<div class="stage" id="stage">\n\n' % (topbar, unit))
    body += "\n\n".join(slides) + "\n\n</div>\n\n"
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(head + body + tail.replace("</body>", SAY + "\n</body>"))
    print("scritto", path)

if __name__ == "__main__":
    from unita_primi import SLIDE
    from unita_primi2 import SLIDE2
    from unita_civica import SLIDE_CIVICA
    from unita_drive import SLIDE_DRIVE
    for path, unit, topbar, slides, css in SLIDE + SLIDE2 + SLIDE_CIVICA + SLIDE_DRIVE:
        build(path, unit, topbar, slides, css)
