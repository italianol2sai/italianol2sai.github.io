/* Pulsante «🖨️ Stampa» (regola di Erila, 2026-11-24): si stampa direttamente dal browser.
   - Pagine a slide (teoria): tutte le slide una sotto l'altra, senza pulsanti.
   - Pagine di esercizi (window.DATA di motore.js): una scheda pulita da compilare a penna,
     con NOME e DATA, esercizi vuoti e «ascolta l'insegnante» al posto del 🔊. Mai le soluzioni.
   Basta includere <script src="../comune/stampa.js"></script> (motore.js lo carica da solo). */
(function () {
  if (window.__stampa) return; window.__stampa = true;

  var CSS = "" +
    "@page{size:A4;margin:12mm 12mm 14mm}" +
    ".btn-stampa{cursor:pointer}" +
    "@media print{" +
    " *{-webkit-print-color-adjust:exact;print-color-adjust:exact}" +
    " .btn-stampa,.controls,.progress{display:none!important}" +
    " html,body{height:auto!important;overflow:visible!important;background:#fff!important}" +
    " body:has(.stage){display:block!important}" +
    " .topbar{position:static!important}" +
    " .stage{position:static!important;overflow:visible!important;height:auto!important;display:block!important}" +
    " .slide{position:static!important;display:flex!important;overflow:visible!important;inset:auto!important;animation:none!important;" +
    "  padding:6mm 2mm 8mm!important;break-inside:avoid;border-bottom:1px dashed #bbb;min-height:0!important;height:auto!important}" +
    " .slide:last-of-type{display:none!important}" +
    " .bubble.parla::after,.card.parla b::after{content:none!important}" +
    " body.in-stampa>*:not(#scheda-stampa){display:none!important}" +
    " body.in-stampa #scheda-stampa{display:block!important}" +
    "}" +
    "#scheda-stampa{display:none;font-size:12pt;line-height:1.45;color:#1d1d1d;background:#fff}" +
    "body.liv-alfa #scheda-stampa{font-size:15pt} body.liv-a2 #scheda-stampa{font-size:12.5pt} body.liv-b1 #scheda-stampa{font-size:11.5pt}" +
    "#scheda-stampa .s-testa{display:flex;justify-content:space-between;align-items:flex-end;border-bottom:3px solid #333;padding-bottom:6px;margin-bottom:10px}" +
    "#scheda-stampa h1{margin:0;font-size:1.5em} #scheda-stampa .s-testa small{color:#555;font-size:.7em}" +
    "#scheda-stampa .s-nome span{display:inline-block;border-bottom:1.5px solid #333;width:12em;margin:0 1.2em 0 .3em}" +
    "#scheda-stampa .s-part{background:#333;color:#fff;font-weight:700;padding:4px 10px;border-radius:6px;margin:16px 0 8px;break-after:avoid}" +
    "#scheda-stampa .teoria{border:2px solid #333;border-radius:8px;padding:8px 12px;margin:6px 0 10px;break-inside:avoid;background:#fff}" +
    "#scheda-stampa .teoria table{border-collapse:collapse;margin:6px 0;display:table} #scheda-stampa .teoria td,#scheda-stampa .teoria th{border:1px solid #999;padding:2px 8px}" +
    "#scheda-stampa .s-es{margin:10px 0 14px;break-inside:avoid} #scheda-stampa .s-es.lungo{break-inside:auto}" +
    "#scheda-stampa h3{font-size:1.05em;margin:0 0 4px;break-after:avoid}" +
    "#scheda-stampa .s-cons{font-style:italic;margin:0 0 6px}" +
    "#scheda-stampa .s-box{border:1.5px dashed #777;border-radius:6px;padding:5px 10px;margin:4px 0 8px}" +
    "#scheda-stampa ol{list-style:none;padding:0;margin:0} #scheda-stampa ol>li{margin:5px 0;break-inside:avoid}" +
    "#scheda-stampa .s-opz{display:inline-flex;flex-wrap:wrap;gap:4px 16px;margin-left:8px}" +
    "#scheda-stampa .s-opz span::before{content:'';display:inline-block;width:.8em;height:.8em;border:1.5px solid #333;border-radius:50%;margin-right:5px;vertical-align:-1px}" +
    "#scheda-stampa .full .s-opz{display:flex;margin:2px 0 0 18px}" +
    "#scheda-stampa .s-riga{display:inline-block;border-bottom:1.5px solid #333;min-width:7em;height:1.1em;margin:0 3px}" +
    "#scheda-stampa .s-riga.m{min-width:10em} #scheda-stampa .s-riga.l{min-width:16em}" +
    "#scheda-stampa .s-righe div{border-bottom:1.2px solid #555;height:1.9em}" +
    "#scheda-stampa .s-quad{display:inline-block;width:1.6em;height:1.4em;border:1.5px solid #333;border-radius:4px;margin-right:8px;vertical-align:middle}" +
    "#scheda-stampa .s-parla{border-left:4px solid #333;padding-left:8px}" +
    "#scheda-stampa img{max-width:100%;max-height:55mm}" +
    "#scheda-stampa .s-piede{margin-top:14px;font-size:.7em;color:#777;text-align:center;text-transform:none}";
  var st = document.createElement("style"); st.textContent = CSS; document.head.appendChild(st);

  function bottone(testo, onclick, classe) {
    var b = document.createElement("button"); b.type = "button"; b.className = (classe || "btn") + " btn-stampa";
    b.textContent = testo; b.onclick = onclick; return b;
  }

  // ---------- slide (teoria)
  var controls = document.querySelector(".controls");
  if (controls && document.querySelector(".stage")) {
    var b = bottone("🖨️ STAMPA", function () { window.print(); });
    controls.appendChild(b);
  }

  // ---------- esercizi (motore.js)
  var D = window.DATA;
  if (!D || !D.sections) return;
  var UP = !!D.upper;
  function T(s) { return UP ? s.toUpperCase() : s; }
  function esc(s) { return String(s == null ? "" : s).replace(/[&<>]/g, function (c) { return { "&": "&amp;", "<": "&lt;", ">": "&gt;" }[c]; }); }
  function sayIcon(q) { return String(q || "").replace(/<button[^>]*class="say"[^>]*>[\s\S]*?<\/button>/g, "🔊"); }
  function riga(w) { return '<span class="s-riga ' + ({ s: "", m: "m", l: "l" }[w || "s"] || "m") + '"></span>'; }
  function opz(o) { return '<span class="s-opz">' + (o || []).map(function (x) { return "<span>" + x + "</span>"; }).join("") + "</span>"; }

  function esercizio(ex) {
    var t = ex.type, items = ex.items || [], h = [];
    h.push('<div class="s-es' + (items.length > 8 ? " lungo" : "") + '"><h3>' + ex.title + "</h3>");
    if (ex.cons) h.push('<p class="s-cons">' + ex.cons.replace("TOCCA 🔊.", "ASCOLTA L'INSEGNANTE.").replace("Tocca 🔊.", "Ascolta l'insegnante.") + "</p>");
    if (ex.audio) h.push("<p><b>🎧 " + T("Ascolta l'insegnante.") + "</b></p>");
    if (ex.info) h.push('<div class="s-box">' + sayIcon(ex.info) + "</div>");
    if (ex.bank) h.push('<div class="s-box">' + ex.bank + "</div>");
    if (t === "choice") {
      h.push("<ol>" + items.map(function (it) {
        return "<li" + (ex.full ? ' class="full"' : "") + ">" + sayIcon(it.q) + " " + opz(it.opts || ex.opts) + "</li>"; }).join("") + "</ol>");
    } else if (t === "select") {
      h.push('<div class="s-box">' + (ex.opts || []).join(" · ") + "</div><ol>" +
        items.map(function (it) { return "<li>" + sayIcon(it.q) + " " + riga("l") + "</li>"; }).join("") + "</ol>");
    } else if (t === "text") {
      h.push("<ol>" + items.map(function (it) {
        return "<li>" + sayIcon(it.q) + " " + (it.pre || "") + riga(it.w || ex.w) + (it.post || "") + "</li>"; }).join("") + "</ol>");
    } else if (t === "cloze") {
      h.push('<div style="line-height:2.1">' + (ex.parts || []).map(function (p) { return typeof p === "string" ? p : riga("m"); }).join("") + "</div>");
    } else if (t === "order") {
      h.push("<ol>" + items.map(function (x) { return '<li><span class="s-quad"></span>' + x + "</li>"; }).join("") + "</ol>");
    } else if (t === "free") {
      items.forEach(function (lab) { h.push("<p><b>" + lab + '</b></p><div class="s-righe">' + new Array((ex.rows || 4) + 1).join("<div></div>") + "</div>"); });
    } else if (t === "record") {
      h.push('<p class="s-cons">🗣️ ' + T("Parla con l'insegnante o con un compagno.") + "</p>");
      items.forEach(function (x) { h.push('<p class="s-parla">' + x + "</p>"); });
    } else {
      // tipo sconosciuto: si stampano almeno le domande con una riga
      h.push("<ol>" + items.map(function (it) { return "<li>" + sayIcon(typeof it === "string" ? it : it.q) + " " + riga("l") + "</li>"; }).join("") + "</ol>");
    }
    h.push("</div>");
    return h.join("");
  }

  function scheda() {
    var titolo = String(D.title || "").replace(/ · Esercizi$/, "");
    var h = ['<div class="s-testa"><h1>' + esc(titolo) + " · " + T("Esercizi") + "</h1><small>ITALIANO L2</small></div>",
      '<p class="s-nome">' + T("Nome") + "<span></span>" + T("Data") + "<span></span></p>"];
    D.sections.forEach(function (ex) {
      if (ex.part && !ex.type) {
        h.push('<div class="s-part">' + ex.part + "</div>");
        if (ex.teoria) h.push('<div class="teoria"><b>📘 ' + T("La regola") + "</b>" + ex.teoria + "</div>");
      } else h.push(esercizio(ex));
    });
    h.push('<p class="s-piede">italianol2sai.github.io · Autoapprendimento Italiano L2 ETNIE</p>');
    return h.join("");
  }

  function stampa() {
    var box = document.getElementById("scheda-stampa");
    if (!box) { box = document.createElement("div"); box.id = "scheda-stampa"; document.body.appendChild(box); }
    box.innerHTML = scheda();
    document.body.classList.add("in-stampa");
    var fine = function () { document.body.classList.remove("in-stampa"); window.removeEventListener("afterprint", fine); };
    window.addEventListener("afterprint", fine);
    window.print();
  }
  window.stampaScheda = stampa;

  function metti() {
    var app = document.getElementById("app"); if (!app) return;
    var sub = app.querySelector(".sub") || app.querySelector("h1");
    var b = bottone(UP ? "🖨️ STAMPA LA SCHEDA" : "🖨️ Stampa la scheda", stampa);
    b.style.margin = "0 0 12px";
    if (sub && sub.parentNode) sub.parentNode.insertBefore(b, sub.nextSibling); else app.prepend(b);
  }
  if (document.readyState === "loading") document.addEventListener("DOMContentLoaded", metti); else metti();
})();
