/* Pulsante «🖨️ Stampa» (regole di Erila, 2026-11-24): si stampa dal browser, impaginato come un libro.
   - Pagina a slide (teoria): «🖨️ STAMPA L'UNITÀ» stampa la teoria e poi la scheda degli esercizi
     (letta da esercizi.html della stessa cartella), come un capitolo di libro.
   - Pagina di esercizi (window.DATA di motore.js): «🖨️ Stampa la scheda» stampa solo gli esercizi.
   Scheda: NOME e DATA, righe vuote, pallini, «ascolta l'insegnante» al posto del 🔊. Mai le soluzioni.
   Basta includere <script src="../comune/stampa.js"></script> (motore.js lo carica da solo). */
(function () {
  if (window.__stampa) return; window.__stampa = true;

  var LIV = { alfa: "Alfabetizzazione", a2: "Livello A2", b1: "Livello B1" };
  var ACC = { alfa: "#0b7a75", a2: "#c2410c", b1: "#5b3fa3" };

  var CSS = "" +
    ".btn-stampa{cursor:pointer}" +
    "#libro{display:none}" +
    "@media print{" +
    " @page{size:A4;margin:15mm 15mm 17mm}" +
    " *{-webkit-print-color-adjust:exact;print-color-adjust:exact}" +
    " html,body{height:auto!important;min-height:0!important;overflow:visible!important;background:#fff!important;display:block!important;margin:0!important;padding:0!important}" +
    " body.in-stampa>*:not(#libro){display:none!important}" +
    " body.in-stampa #libro{display:block!important}" +
    "}" +
    // ---------------- impaginazione «libro»
    "#libro{--acc:#0b7a75;color:#1c1c1c;font-size:11.5pt;line-height:1.45}" +
    "#libro.l-alfa{font-size:14pt;letter-spacing:.02em} #libro.l-a2{font-size:12pt} #libro.l-b1{font-size:11pt}" +
    "#libro .upper{text-transform:uppercase}" +
    "#libro .apertura{background:var(--acc);color:#fff;border-radius:0 0 14px 14px;padding:12px 18px 14px;margin:0 0 14px;display:flex;justify-content:space-between;align-items:flex-end;gap:16px}" +
    "#libro .apertura small{display:block;font-size:.68em;letter-spacing:.14em;text-transform:uppercase;opacity:.9;margin-bottom:2px}" +
    "#libro .apertura h1{margin:0;font-size:1.9em;line-height:1.1;color:#fff}" +
    "#libro .apertura .ico{font-size:2.4em;line-height:1}" +
    "#libro .nome{display:flex;gap:18px;margin:0 0 12px;font-size:.9em;font-weight:700}" +
    "#libro .nome span{flex:1;border-bottom:1.5px solid #444}" +
    "#libro .capitolo{break-before:page}" +
    "#libro .sez{color:var(--acc);font-size:.8em;font-weight:800;letter-spacing:.14em;text-transform:uppercase;border-bottom:2.5px solid var(--acc);padding:0 0 3px;margin:16px 0 8px;break-after:avoid}" +
    "#libro .teoria{background:color-mix(in srgb,var(--acc) 9%,#fff);border:0;border-left:6px solid var(--acc);border-radius:0 10px 10px 0;padding:8px 14px;margin:6px 0 12px;break-inside:avoid;line-height:1.5}" +
    "#libro .teoria>b:first-child{display:inline-block;background:var(--acc);color:#fff;font-size:.75em;letter-spacing:.1em;text-transform:uppercase;padding:1px 8px;border-radius:4px;margin-bottom:5px}" +
    "#libro .teoria table{border-collapse:collapse;margin:6px 0;display:table;max-width:100%} #libro .teoria td,#libro .teoria th{border:1px solid color-mix(in srgb,var(--acc) 35%,#fff);padding:2px 8px;text-align:left;white-space:normal}" +
    "#libro .teoria th{background:color-mix(in srgb,var(--acc) 18%,#fff)}" +
    "#libro .es{margin:12px 0 14px;break-inside:avoid} #libro .es.lungo{break-inside:auto}" +
    "#libro .es h3{display:flex;align-items:baseline;gap:8px;font-size:1em;margin:0 0 4px;break-after:avoid}" +
    "#libro .num{flex:0 0 auto;display:inline-grid;place-items:center;min-width:1.7em;height:1.7em;border-radius:50%;background:var(--acc);color:#fff;font-size:.85em;font-weight:800}" +
    "#libro .cons{font-style:italic;margin:0 0 6px;color:#333}" +
    "#libro .box{border:1.5px solid color-mix(in srgb,var(--acc) 50%,#fff);border-radius:8px;padding:5px 10px;margin:4px 0 8px;background:color-mix(in srgb,var(--acc) 5%,#fff)}" +
    "#libro ol{list-style:none;padding:0;margin:0} #libro ol>li{margin:6px 0;break-inside:avoid}" +
    "#libro ol.due{columns:2;column-gap:24px}" +
    "#libro .opz{display:inline-flex;flex-wrap:wrap;gap:4px 16px;margin-left:8px}" +
    "#libro .opz span::before{content:'';display:inline-block;width:.8em;height:.8em;border:1.5px solid #333;border-radius:50%;margin-right:5px;vertical-align:-1px}" +
    "#libro .full .opz{display:flex;margin:2px 0 0 18px}" +
    "#libro .riga{display:inline-block;border-bottom:1.5px solid #333;min-width:7em;height:1.1em;margin:0 3px}" +
    "#libro .riga.m{min-width:10em} #libro .riga.l{min-width:15em}" +
    "#libro .righe div{border-bottom:1.2px solid #777;height:2em}" +
    "#libro .quad{display:inline-block;width:1.6em;height:1.4em;border:1.5px solid #333;border-radius:4px;margin-right:8px;vertical-align:middle}" +
    "#libro .parla{border-left:4px solid var(--acc);padding-left:8px}" +
    "#libro .emo{font-size:1.6em;line-height:1}" +
    "#libro img{max-width:100%;max-height:60mm}" +
    "#libro .piede{margin-top:16px;font-size:.7em;color:#888;text-align:center;text-transform:none;letter-spacing:0}" +
    // ---------------- teoria (le slide diventano pagine di libro)
    "#libro .teoria-slide{zoom:.72}" +
    "#libro .teoria-slide .slide{display:block!important;position:static!important;inset:auto!important;overflow:visible!important;height:auto!important;min-height:0!important;padding:0 0 14px!important;animation:none!important;break-inside:auto}" +
    "#libro .teoria-slide .slide h2{break-after:avoid;margin-top:10px}" +
    "#libro .teoria-slide .card,#libro .teoria-slide .bubble,#libro .teoria-slide table,#libro .teoria-slide .nota,#libro .teoria-slide img,#libro .teoria-slide .grid>*{break-inside:avoid}" +
    "#libro .teoria-slide .bubble.parla::after,#libro .teoria-slide .card.parla b::after{content:none!important}" +
    "#libro .teoria-slide .ill{max-height:80mm;width:auto;display:block;margin:0 auto 10px}";
  var st = document.createElement("style"); st.textContent = CSS; document.head.appendChild(st);
  var pagina = document.createElement("style"); document.head.appendChild(pagina);

  function bottone(testo, onclick, classe) {
    var b = document.createElement("button"); b.type = "button"; b.className = (classe || "btn") + " btn-stampa";
    b.textContent = testo; b.onclick = onclick; return b;
  }
  function esc(s) { return String(s == null ? "" : s).replace(/[&<>"]/g, function (c) { return { "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "\\\"" }[c]; }); }
  function sayIcon(q) { return String(q || "").replace(/<button[^>]*class="say"[^>]*>[\s\S]*?<\/button>/g, "🔊"); }
  function riga(w) { return '<span class="riga ' + ({ s: "", m: "m", l: "l" }[w || "s"] || "m") + '"></span>'; }
  function opz(o) { return '<span class="opz">' + (o || []).map(function (x) { return "<span>" + x + "</span>"; }).join("") + "</span>"; }
  function testo(h) { var d = document.createElement("div"); d.innerHTML = h || ""; return d.textContent; }

  // ---------- scheda degli esercizi da window.DATA
  function titoloEs(t) {
    var m = String(t).match(/^\s*(\d+)\s*[·.]?\s*(.*)$/);
    return m ? '<span class="num">' + m[1] + "</span><span>" + m[2].replace(/^[✎·\s]+/, "").replace(/^(\S{1,3})\s*·\s*/, "$1 ") + "</span>" : "<span>" + t + "</span>";
  }
  function esercizio(ex, T) {
    var t = ex.type, items = ex.items || [], h = [];
    h.push('<div class="es' + (items.length > 8 ? " lungo" : "") + '"><h3>' + titoloEs(ex.title) + "</h3>");
    if (ex.cons) h.push('<p class="cons">' + ex.cons.replace("TOCCA 🔊.", "ASCOLTA L'INSEGNANTE.").replace("Tocca 🔊.", "Ascolta l'insegnante.") + "</p>");
    if (ex.audio) h.push("<p><b>🎧 " + T("Ascolta l'insegnante.") + "</b></p>");
    if (ex.info) h.push('<div class="box">' + sayIcon(ex.info) + "</div>");
    if (ex.bank) h.push('<div class="box">' + ex.bank + "</div>");
    var corti = items.length > 4 && items.every(function (it) {
      return typeof it === "object" && !it.pre && (testo(it.q) + (it.opts || ex.opts || []).join("  ")).length < 22; });
    // opzioni brevi (VERO / FALSO…): sulla stessa riga della frase
    var full = ex.full && (ex.opts || []).join("").length > 14;
    if (t === "choice") {
      h.push("<ol" + (corti && !ex.full ? ' class="due"' : "") + ">" + items.map(function (it) {
        return "<li" + (full ? ' class="full"' : "") + ">" + sayIcon(it.q) + " " + opz(it.opts || ex.opts) + "</li>"; }).join("") + "</ol>");
    } else if (t === "select") {
      h.push('<div class="box">' + (ex.opts || []).join(" · ") + "</div><ol>" +
        items.map(function (it) { return "<li>" + sayIcon(it.q) + " " + riga("l") + "</li>"; }).join("") + "</ol>");
    } else if (t === "text") {
      h.push("<ol" + (corti ? ' class="due"' : "") + ">" + items.map(function (it) {
        return "<li>" + sayIcon(it.q) + " " + (it.pre || "") + riga(it.w || ex.w) + (it.post || "") + "</li>"; }).join("") + "</ol>");
    } else if (t === "cloze") {
      h.push('<div style="line-height:2.2">' + (ex.parts || []).map(function (p) { return typeof p === "string" ? p : riga("m"); }).join("") + "</div>");
    } else if (t === "order") {
      h.push("<ol>" + items.map(function (x) { return '<li><span class="quad"></span>' + x + "</li>"; }).join("") + "</ol>");
    } else if (t === "free") {
      items.forEach(function (lab) { h.push("<p><b>" + lab + '</b></p><div class="righe">' + new Array((ex.rows || 4) + 1).join("<div></div>") + "</div>"); });
    } else if (t === "record") {
      h.push('<p class="cons">🗣️ ' + T("Parla con l'insegnante o con un compagno.") + "</p>");
      items.forEach(function (x) { h.push('<p class="parla">' + x + "</p>"); });
    } else {
      h.push("<ol>" + items.map(function (it) { return "<li>" + sayIcon(typeof it === "string" ? it : it.q) + " " + riga("l") + "</li>"; }).join("") + "</ol>");
    }
    h.push("</div>");
    return h.join("");
  }
  function scheda(D, conApertura) {
    var UP = !!D.upper, T = function (s) { return UP ? s.toUpperCase() : s; };
    var titolo = String(D.title || "").replace(/\s*·\s*Esercizi$/i, "");
    var h = [];
    if (conApertura) h.push(apertura(D.livello, T("Esercizi"), titolo));
    else h.push('<div class="sez" style="font-size:1.1em;margin-top:0">' + T("Esercizi") + "</div>");
    h.push('<p class="nome">' + T("Nome") + "<span></span>" + T("Data") + "<span></span></p>");
    D.sections.forEach(function (ex) {
      if (ex.part && !ex.type) {
        h.push('<div class="sez">' + ex.part + "</div>");
        if (ex.teoria) h.push('<div class="teoria"><b>📘 ' + T("La regola") + "</b><br>" + ex.teoria + "</div>");
      } else h.push(esercizio(ex, T));
    });
    return '<div class="' + (UP ? "upper" : "") + '">' + h.join("") + "</div>";
  }
  function apertura(liv, sopra, titolo, ico) {
    return '<div class="apertura"><div><small>Italiano L2 · ' + (LIV[liv] || "") + (sopra ? " · " + sopra : "") + "</small><h1>" + titolo + "</h1></div>" +
      (ico ? '<div class="ico">' + ico + "</div>" : "") + "</div>";
  }

  // ---------- stampa
  function stampa(html, liv, piede) {
    var box = document.getElementById("libro");
    if (!box) { box = document.createElement("div"); box.id = "libro"; document.body.appendChild(box); }
    box.className = "l-" + (liv || "b1");
    box.style.setProperty("--acc", ACC[liv] || "#333");
    box.innerHTML = html + '<p class="piede">italianol2sai.github.io · Autoapprendimento Italiano L2 ETNIE</p>';
    pagina.textContent = "@media print{@page{" +
      "@bottom-left{content:\"" + esc(piede) + "\";font:8pt sans-serif;color:#888}" +
      "@bottom-right{content:counter(page);font:bold 9pt sans-serif;color:" + (ACC[liv] || "#333") + "}}}";
    document.body.classList.add("in-stampa");
    var fine = function () { document.body.classList.remove("in-stampa"); window.removeEventListener("afterprint", fine); };
    window.addEventListener("afterprint", fine);
    var imgs = [].slice.call(box.querySelectorAll("img"));
    imgs.forEach(function (i) { i.loading = "eager"; });
    imgs = imgs.filter(function (i) { return !i.complete; });
    var attesa = Promise.all(imgs.map(function (i) { return new Promise(function (r) { i.addEventListener("load", r); i.addEventListener("error", r); }); }));
    Promise.race([attesa, new Promise(function (r) { setTimeout(r, 2500); })]).then(function () { window.print(); });
  }

  function datiDa(htmlTesto) {
    var m = htmlTesto.match(/window\.DATA\s*=\s*(\{[\s\S]*?\});?\s*<\/script>/);
    return m ? JSON.parse(m[1]) : null;
  }
  function livelloSlide() {
    var t = (document.querySelector(".topbar .unit") || {}).textContent || "";
    return /ALFABETIZZAZIONE/i.test(t) ? "alfa" : /A2/.test(t) ? "a2" : /B1/.test(t) ? "b1" : "";
  }

  // ---------- pagina a slide (teoria + esercizi)
  var controls = document.querySelector(".controls");
  if (controls && document.querySelector(".stage")) {
    var liv = livelloSlide();
    controls.appendChild(bottone("🖨️ STAMPA L'UNITÀ", function () {
      var slides = [].slice.call(document.querySelectorAll(".stage .slide"));
      var cover = slides[0], titolo = (cover.querySelector("h1") || {}).textContent || document.title;
      var sopra = ((cover.querySelector(".badge") || {}).textContent || "").replace(/^.*•\s*/, "");
      var ico = (cover.querySelector(".big") || {}).textContent || "";
      var corpo = slides.slice(1, -1).map(function (s) {
        var c = s.cloneNode(true); c.classList.remove("active"); return c.outerHTML; }).join("");
      var html = apertura(liv, sopra, titolo, ico) +
        ((cover.querySelector(".lead") || {}).textContent ? '<p class="cons">' + cover.querySelector(".lead").textContent + "</p>" : "") +
        '<div class="teoria-slide">' + corpo + "</div>";
      var piede = "Italiano L2 · " + titolo;
      fetch("esercizi.html").then(function (r) { return r.ok ? r.text() : ""; }).then(function (t) {
        var D = t && datiDa(t);
        stampa(html + (D ? '<div class="capitolo">' + scheda(D, false) + "</div>" : ""), liv, piede);
      }).catch(function () { stampa(html, liv, piede); });
    }));
  }

  // ---------- pagina di esercizi
  var D = window.DATA;
  if (!D || !D.sections) return;
  function metti() {
    var app = document.getElementById("app"); if (!app) return;
    var sub = app.querySelector(".sub") || app.querySelector("h1");
    var b = bottone(D.upper ? "🖨️ STAMPA LA SCHEDA" : "🖨️ Stampa la scheda", function () {
      stampa(scheda(D, true), D.livello, "Italiano L2 · " + String(D.title || "").replace(/\s*·\s*Esercizi$/i, ""));
    });
    b.style.margin = "0 0 12px";
    if (sub && sub.parentNode) sub.parentNode.insertBefore(b, sub.nextSibling); else app.prepend(b);
  }
  if (document.readyState === "loading") document.addEventListener("DOMContentLoaded", metti); else metti();
})();
