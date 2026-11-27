/* Pulsante «🖨️ Stampa» (regole di Erila, 2026-11-24): si stampa dal browser, impaginato come un libro.
   - Pagina a slide (teoria): «🖨️ STAMPA L'UNITÀ» stampa la teoria e poi la scheda degli esercizi
     (letta da esercizi.html della stessa cartella), come un capitolo di libro.
   - Pagina di esercizi (window.DATA di motore.js): «🖨️ Stampa la scheda» stampa solo gli esercizi.
   Scheda: NOME e DATA, righe vuote, pallini, «ascolta l'insegnante» al posto del 🔊. Mai le soluzioni.
   Basta includere <script src="../comune/stampa.js"></script> (motore.js lo carica da solo). */
(function () {
  if (window.__stampa) return; window.__stampa = true;
  var me = document.currentScript;

  var LIV = { alfa: "Alfabetizzazione", a1: "Livello A1", a2: "Livello A2", b1: "Livello B1" };
  var ACC = { alfa: "#0b7a75", a1: "#0369a1", a2: "#c2410c", b1: "#5b3fa3" };

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
    "#libro .capitolo{margin-top:18px;border-top:3px double #000;padding-top:6px}" +
    "#libro .sez{color:var(--acc);font-size:.8em;font-weight:800;letter-spacing:.14em;text-transform:uppercase;border-bottom:2.5px solid var(--acc);padding:0 0 3px;margin:16px 0 8px;break-after:avoid}" +
    "#libro .teoria{background:color-mix(in srgb,var(--acc) 9%,#fff);border:0;border-left:6px solid var(--acc);border-radius:0 10px 10px 0;padding:8px 14px;margin:6px 0 12px;break-inside:avoid;line-height:1.5}" +
    "#libro .teoria>b:first-child{display:inline-block;background:var(--acc);color:#fff;font-size:.75em;letter-spacing:.1em;text-transform:uppercase;padding:1px 8px;border-radius:4px;margin-bottom:5px}" +
    "#libro .teoria table{border-collapse:collapse;margin:6px 0;display:table;max-width:100%} #libro .teoria td,#libro .teoria th{border:1px solid color-mix(in srgb,var(--acc) 35%,#fff);padding:2px 8px;text-align:left;white-space:normal}" +
    "#libro .teoria th{background:color-mix(in srgb,var(--acc) 18%,#fff)}" +
    "#libro .es{margin:10px 0 12px;break-inside:auto} #libro .es h3,#libro .es .cons,#libro .es>.box{break-after:avoid}" +
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
    // niente zoom (sbagliava i salti pagina e lasciava buchi): si rimpicciolisce la base rem delle slide
    "@media print{html:has(body.in-stampa){font-size:12px!important} html:has(#libro.l-alfa){font-size:14.5px!important}}" +
    // Alfa: quaderno semplice (caratteri grandi, una colonna, più spazio per scrivere)
    "#libro.l-alfa{font-size:17pt;line-height:1.6} #libro.l-alfa ol.due{columns:1}" +
    "#libro.l-alfa .apertura{border-radius:10px} #libro.l-alfa .num{background:#fff;color:var(--acc);border:2.5px solid var(--acc)}" +
    "#libro.l-alfa ol>li{margin:8px 0} #libro.l-alfa .riga{height:1.4em;min-width:9em} #libro.l-alfa .righe div{height:2.6em}" +
    "#libro.l-alfa .opz{gap:6px 26px} #libro.l-alfa .es{margin:12px 0 14px}" +
    "#libro .teoria-slide .slide{display:block!important;position:static!important;inset:auto!important;overflow:visible!important;height:auto!important;min-height:0!important;padding:0 0 14px!important;animation:none!important;break-inside:auto}" +
    "#libro .teoria-slide .slide h2{break-after:avoid;margin-top:10px}" +
    "#libro .teoria-slide .card,#libro .teoria-slide .bubble,#libro .teoria-slide table,#libro .teoria-slide .nota,#libro .teoria-slide img,#libro .teoria-slide .grid>*{break-inside:avoid}" +
    "#libro .teoria-slide .bubble.parla::after,#libro .teoria-slide .card.parla b::after{content:none!important}" +
    "#libro .teoria-slide .ill{max-height:80mm;width:auto;display:block;margin:0 auto 10px}" +
    // ---------------- bianco e nero (Erila 2026-11-27): niente fondi colorati, testo nero, bordi e linee nere/grigie,
    // titoli con bordo invece del fondo pieno → si legge bene con la stampante in b/n e si risparmia inchiostro
    "#libro{--acc:#000!important;color:#000}" +
    "#libro *{background:transparent!important;box-shadow:none!important;text-shadow:none!important;color:#000!important}" +
    "#libro *:not(.riga):not(.righe div):not(.quad){border-color:#000!important}" +
    "#libro .apertura{border:2.5px solid #000;border-radius:10px} #libro .apertura h1{font-weight:900}" +
    "#libro .num{border:2px solid #000;background:#fff!important} #libro.l-alfa .num{border-width:2.5px}" +
    "#libro .teoria{border:1.5px solid #000;border-left:6px solid #000;border-radius:0 8px 8px 0}" +
    "#libro .teoria>b:first-child{border:1.5px solid #000;padding:0 6px}" +
    "#libro .teoria th,#libro table th{background:#e6e6e6!important;font-weight:800}" +
    "#libro .sez{border-bottom:2.5px solid #000}" +
    "#libro .box{border:1.5px dashed #000}" +
    "#libro b,#libro strong{font-weight:900}" +
    "#libro .bubble{border:1.5px solid #000!important;border-left:6px solid #000!important}" +
    "#libro .bubble.med{border-left-style:double!important}" +
    "#libro .nota{border:2px dashed #000!important}" +
    "#libro .card{border:1.5px solid #000!important}" +
    // disegni SVG (orologi): tutto nero; lancetta delle ore grossa, dei minuti sottile
    "#libro svg circle{fill:#fff} #libro svg circle[r='7']{fill:#000} #libro svg [stroke]{stroke:#000}" +
    "#libro svg line[stroke-width='5']{stroke-width:4}" +
    "#libro svg text{fill:#000}" +
    "#libro .dig{background:#fff!important;color:#000!important;border:2px solid #000!important}" +
    "#libro img{filter:grayscale(1) contrast(1.1)}" +
    // meno spazi vuoti (Erila 2026-11-27): liste con disegni (orologi…) in 3 colonne, slide compatte
    // (inline-flex e non grid: con la griglia Chrome mandava tutto alla pagina dopo)
    "#libro ol:has(svg){display:block;font-size:0}" +
    "#libro ol:has(svg)>li{display:inline-flex;vertical-align:top;width:33.3%;box-sizing:border-box;padding-right:12px;align-items:center;gap:6px;margin:2px 0;font-size:11.5pt}" +
    "#libro.l-alfa ol:has(svg)>li{font-size:17pt}" +
    "#libro ol:has(svg)>li>span:first-child{display:inline-flex!important;align-items:center;gap:4px}" +
    "#libro ol svg{width:28mm;height:auto} #libro ol:has(svg) .riga{min-width:0;flex:1}" +
    "#libro .teoria-slide .slide{padding:0 0 8px!important} #libro .teoria-slide .slide h2{margin:6px 0 8px!important;padding-bottom:4px!important}" +
    "#libro .teoria-slide .grid,#libro .teoria-slide .orologi{gap:8px!important;margin-top:4px!important}" +
    "#libro .teoria-slide .card,#libro .teoria-slide .orologi>div{padding:6px 8px!important}" +
    "#libro .teoria-slide .nota{padding:8px 12px!important;margin-top:8px!important}" +
    "#libro .teoria-slide .bubble{margin:5px 0!important;padding:6px 12px!important}" +
    "#libro .teoria-slide .orologi{grid-template-columns:repeat(4,1fr)!important} #libro .teoria-slide .orologi svg{max-width:28mm}" +
    "#libro .teoria-slide .duo{grid-template-columns:auto 1fr!important} #libro .teoria-slide .big-clk svg{width:45mm!important}";
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
    if (ex.img) h.push('<p><img src="' + ex.img + '" alt=""></p>');
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
    } else if (t === "multi") {
      h.push("<ol" + (corti ? ' class="due"' : "") + ">" + items.map(function (x) { return '<li><span class="quad"></span>' + (typeof x === "string" ? x : x.q) + "</li>"; }).join("") + "</ol>");
    } else if (t === "survey") {
      h.push("<ol>" + items.map(function (x) { return "<li>" + (typeof x === "string" ? x : x.q) + " " + opz(ex.opts) + "</li>"; }).join("") + "</ol>");
    } else if (t === "set") {
      h.push("<ol" + ((ex.n || 4) > 4 ? ' class="due"' : "") + ">" + new Array((ex.n || 4) + 1).join("<li>" + riga("l") + "</li>") + "</ol>");
    } else if (t === "info") {
      // solo testo da leggere (è già nel riquadro)
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
    if (conApertura) h.push(apertura(livelloDati(D), T("Esercizi"), titolo));
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

  // livello delle schede vecchie senza D.livello: maiuscolo = A1 (quaderno), altrimenti A2/B1+
  function livelloDati(D) {
    if (D.livello) return D.livello;
    if (D.upper) return "a1";
    return /\b(B1|B2|C1|C2)\b/.test((D.title || "") + " " + (D.sub || "")) ? "b1" : "a2";
  }

  // ---------- stampa
  function stampa(html, liv, piede) {
    // Alfa / A0 / A1: tutto in stampatello maiuscolo, anche il piè di pagina (regola di Erila)
    var su = liv === "alfa" || liv === "a1" || (window.DATA && window.DATA.upper);
    if (su) piede = piede.toUpperCase();
    var box = document.getElementById("libro");
    if (!box) { box = document.createElement("div"); box.id = "libro"; document.body.appendChild(box); }
    box.className = liv === "a1" ? "l-alfa l-a1" : "l-" + (liv || "b1");
    box.style.setProperty("--acc", ACC[liv] || "#333");
    var firma = "italianol2sai.github.io · Autoapprendimento Italiano L2 ETNIE";
    box.innerHTML = html + '<p class="piede">' + (su ? firma.toUpperCase() : firma) + "</p>";
    pagina.textContent = "@media print{@page{" +
      "@bottom-left{content:\"" + esc(piede) + "\";font:8pt sans-serif;color:#333}" +
      "@bottom-right{content:counter(page);font:bold 9pt sans-serif;color:#000}}}";
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
    var t = ((document.querySelector(".topbar .unit") || {}).textContent || "") + " " +
      ((document.querySelector(".stage .slide .badge") || {}).textContent || "");
    return /ALFABETIZZAZIONE/i.test(t) ? "alfa" : /\b(B1|B2|C1|C2)\b/.test(t) ? "b1" : /\bA1\b/.test(t) ? "a1" : /\bA2\b/.test(t) ? "a2" : "a1";
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
        if (D && !D.sections) D = null;
        stampa(html + (D ? '<div class="capitolo">' + scheda(D, false) + "</div>" : ""), liv, piede);
      }).catch(function () { stampa(html, liv, piede); });
    }));
  }

  // ---------- pagine fatte a mano (verifiche, flashcard, ascolto…): si stampa la pagina com'è,
  // senza pulsanti; con data-scheda in cima c'è NOME / DATA
  var D = window.DATA;
  if (!(controls && document.querySelector(".stage")) && !(D && D.sections)) {
    var conScheda = me && me.hasAttribute("data-scheda");
    var su2 = me && me.hasAttribute("data-maiuscolo");
    var css2 = document.createElement("style");
    css2.textContent = ".stampa-fissa{position:fixed;right:14px;bottom:14px;z-index:9999;font:700 15px system-ui,sans-serif;padding:10px 16px;border-radius:999px;border:0;background:#1f3a5f;color:#fff;box-shadow:0 3px 12px rgba(0,0,0,.25)}" +
      ".stampa-testa{display:none}" +
      "@media print{@page{size:A4;margin:14mm}" +
      " *{-webkit-print-color-adjust:exact;print-color-adjust:exact}" +
      " html,body{height:auto!important;overflow:visible!important}" +
      " .stampa-fissa,.np,nav,.no-print{display:none!important}" +
      " .stampa-testa{display:flex!important;gap:18px;font:700 12pt sans-serif;margin:0 0 12px}" +
      " .stampa-testa span{flex:1;border-bottom:1.5px solid #444}" +
      " input[type=text],input:not([type]),textarea{border:0!important;border-bottom:1.5px solid #333!important;border-radius:0!important;background:none!important;box-shadow:none!important}" +
      " section,.card,.box,img,table,li{break-inside:avoid}" +
      // bianco e nero (2026-11-27): fondi bianchi, testo nero, immagini in grigi
      " body,body *{background-color:transparent!important;background-image:none!important;box-shadow:none!important;text-shadow:none!important;color:#000!important}" +
      " img{filter:grayscale(1) contrast(1.1)} svg [stroke]{stroke:#000} svg text{fill:#000}}";
    // pulsanti di comando (Controlla, Invia, Avanti…): non si stampano; le risposte a scelta sì
    var COMANDI = /controlla|invia|whatsapp|condividi|ricomincia|cancella|stampa|indietro|avanti|mescola|prossim|successiv|giochi|registr|^\s*[◀▶⏮⏭🔊🔀↺⟲]/i;
    window.addEventListener("beforeprint", function () {
      [].forEach.call(document.querySelectorAll("button,.btn,a.btn"), function (x) {
        if (COMANDI.test(x.textContent) || x.classList.contains("say") || x.classList.contains("btn-stampa")) x.classList.add("np"); });
    });
    document.head.appendChild(css2);
    var metti2 = function () {
      if (conScheda) {
        var t = document.createElement("p"); t.className = "stampa-testa";
        t.innerHTML = (su2 ? "NOME" : "Nome") + "<span></span>" + (su2 ? "DATA" : "Data") + "<span></span>";
        document.body.insertBefore(t, document.body.firstChild);
      }
      var b = bottone(su2 ? "🖨️ STAMPA" : "🖨️ Stampa", function () {
        window.print();
      }, "stampa-fissa");
      b.title = su2 ? "STAMPA QUESTA PAGINA" : "Stampa questa pagina";
      document.body.appendChild(b);
    };
    if (document.readyState === "loading") document.addEventListener("DOMContentLoaded", metti2); else metti2();
    return;
  }

  // ---------- pagina di esercizi
  if (!D || !D.sections) return;
  function metti() {
    var app = document.getElementById("app"); if (!app) return;
    var sub = app.querySelector(".sub") || app.querySelector("h1");
    var b = bottone(D.upper ? "🖨️ STAMPA LA SCHEDA" : "🖨️ Stampa la scheda", function () {
      stampa(scheda(D, true), livelloDati(D), "Italiano L2 · " + String(D.title || "").replace(/\s*·\s*Esercizi$/i, ""));
    });
    b.style.margin = "0 0 12px";
    if (sub && sub.parentNode) sub.parentNode.insertBefore(b, sub.nextSibling); else app.prepend(b);
  }
  if (document.readyState === "loading") document.addEventListener("DOMContentLoaded", metti); else metti();
})();
