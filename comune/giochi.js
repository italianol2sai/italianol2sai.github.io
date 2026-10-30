// Giochi corti sulle parole di un argomento: memory, impiccato, quiz a tempo, cerca la parola.
// La pagina definisce window.GIOCHI = {titolo, parole: [[PAROLA, emoji, indizio], …]}. Testi in MAIUSCOLO.
(function () {
  var G = window.GIOCHI, P = G.parole.map(function (p) { return { w: p[0], e: p[1], h: p[2] || "" }; });
  var main = document.getElementById("giochi");
  function el(t, a, c) {
    var e = document.createElement(t);
    for (var k in a || {}) { if (k === "text") e.textContent = a[k]; else if (k === "on") e.onclick = a[k]; else e.setAttribute(k, a[k]); }
    (c || []).forEach(function (x) { if (x) e.appendChild(typeof x === "string" ? document.createTextNode(x) : x); });
    return e;
  }
  function mescola(a) { a = a.slice(); for (var i = a.length - 1; i > 0; i--) { var j = Math.floor(Math.random() * (i + 1)); var t = a[i]; a[i] = a[j]; a[j] = t; } return a; }
  function prendi(n) { return mescola(P).slice(0, n); }
  // l'articolo resta visibile: si gioca solo con il nome
  var ART = /^(IL |LO |LA |I |GLI |LE |L'|L’|UN |UNO |UNA |UN')/;
  function articolo(w) { var m = w.match(ART); return m ? m[0] : ""; }
  function nome(w) { return w.slice(articolo(w).length); }
  function leggi(k) { try { return +localStorage.getItem(k) || 0; } catch (e) { return 0; } }
  function scrivi(k, v) { try { localStorage.setItem(k, v); } catch (e) {} }
  function voce(t) { try { var u = new SpeechSynthesisUtterance(t.toLowerCase()); u.lang = "it-IT"; speechSynthesis.cancel(); speechSynthesis.speak(u); } catch (e) {} }

  var area = el("div", { class: "g-area" });
  var GIOCHI = [["memory", "🃏", "MEMORY"], ["impiccato", "🔤", "INDOVINA LA PAROLA"], ["quiz", "⏱️", "QUIZ A TEMPO"], ["cerca", "🔎", "CERCA LA PAROLA"]];
  var schede = el("div", { class: "g-schede", role: "tablist" });
  GIOCHI.forEach(function (g) {
    schede.appendChild(el("button", { class: "g-scheda", "data-g": g[0], on: function () { apri(g[0]); } }, [el("span", { text: g[1] }), " " + g[2]]));
  });
  main.appendChild(schede); main.appendChild(area);

  function apri(nome) {
    [].forEach.call(schede.children, function (b) { b.classList.toggle("on", b.getAttribute("data-g") === nome); });
    area.innerHTML = ""; if (window._timer) clearInterval(window._timer);
    giocoOra = GIOCHI.filter(function (g) { return g[0] === nome; })[0][2];
    ({ memory: memory, impiccato: impiccato, quiz: quiz, cerca: cerca })[nome]();
    try { history.replaceState(null, "", "#" + nome); } catch (e) {}
  }
  var giocoOra = "";
  function fine(msg, ancora) {
    var fb = el("p", { class: "fb" });
    area.appendChild(el("div", { class: "g-fine" }, [el("p", { text: msg }), el("button", { class: "g-btn", text: "GIOCA ANCORA ▶", on: ancora }), " ",
      el("button", { class: "g-btn", text: "📤 INVIA ALL'INSEGNANTE", on: function () { condividi(G.titolo + " · " + giocoOra, [msg], fb); } }), fb]));
  }

  // ---------------- MEMORY
  function memory() {
    var viste = {}, scelte = mescola(P).filter(function (p) { if (viste[p.e]) return false; viste[p.e] = 1; return true; }).slice(0, 6), carte = [];
    scelte.forEach(function (p, i) { carte.push({ id: i, t: p.e, img: true }); carte.push({ id: i, t: p.w }); });
    carte = mescola(carte);
    var aperte = [], trovate = 0, mosse = 0;
    var info = el("p", { class: "g-info", text: "GIRA DUE CARTE: TROVA LA PAROLA E IL SUO DISEGNO." });
    var griglia = el("div", { class: "g-memory" });
    carte.forEach(function (c) {
      var b = el("button", { class: "g-carta", "aria-label": "CARTA" }, [el("span", { text: c.t, class: c.img ? "emo" : "" })]);
      b.onclick = function () {
        if (b.classList.contains("su") || aperte.length === 2) return;
        b.classList.add("su"); aperte.push([b, c]);
        if (!c.img) voce(c.t);
        if (aperte.length === 2) {
          mosse++;
          var a = aperte;
          if (a[0][1].id === a[1][1].id) { a.forEach(function (x) { x[0].classList.add("ok"); }); aperte = []; trovate++;
            if (trovate === scelte.length) { var r = leggi("mem-" + G.id); if (!r || mosse < r) scrivi("mem-" + G.id, mosse);
              fine("BRAVO! HAI TROVATO TUTTE LE COPPIE IN " + mosse + " MOSSE." + (r ? " RECORD: " + Math.min(r, mosse) + " MOSSE." : ""), memory); } }
          else setTimeout(function () { a.forEach(function (x) { x[0].classList.remove("su"); }); aperte = []; }, 900);
        }
      };
      griglia.appendChild(b);
    });
    area.appendChild(info); area.appendChild(griglia);
  }

  // ---------------- IMPICCATO
  function impiccato() {
    var p = prendi(1)[0], art = articolo(p.w), parola = nome(p.w), prese = {}, errori = 0, MAX = 6;
    var lettereOk = function (ch) { return !/[A-ZÀÈÉÌÒÙ]/.test(ch) || prese[ch.normalize("NFD")[0]]; };
    var aiuto = el("div", { class: "g-aiuto" }, [el("span", { class: "emo", text: p.e }), el("span", { text: p.h })]);
    var vite = el("p", { class: "g-info" }), mostra = el("div", { class: "g-parola" }), tasti = el("div", { class: "g-tasti" });
    function disegna() {
      mostra.innerHTML = "";
      if (art) mostra.appendChild(el("span", { class: "art", text: art.trim() }));
      parola.split("").forEach(function (ch) { mostra.appendChild(el("span", { class: ch === " " ? "spazio" : "", text: ch === " " ? " " : (lettereOk(ch) ? ch : "_") })); });
      vite.textContent = "❤️".repeat(MAX - errori) + "🤍".repeat(errori);
    }
    "ABCDEFGHILMNOPQRSTUVZ".split("").forEach(function (l) {
      var b = el("button", { class: "g-tasto", text: l });
      b.onclick = function () {
        if (b.disabled) return; b.disabled = true; prese[l] = true;
        var c = parola.normalize("NFD").replace(/[̀-ͯ]/g, "").indexOf(l) >= 0;
        b.classList.add(c ? "ok" : "no"); if (!c) errori++;
        disegna();
        var vinto = parola.split("").every(lettereOk);
        if (vinto || errori >= MAX) {
          [].forEach.call(tasti.children, function (x) { x.disabled = true; });
          if (!vinto) { prese = {}; parola.split("").forEach(function (ch) { prese[ch.normalize("NFD")[0]] = true; }); disegna(); }
          voce(p.w);
          fine(vinto ? "BRAVO! LA PAROLA È " + p.w + "." : "PECCATO! LA PAROLA ERA " + p.w + ".", impiccato);
        }
      };
      tasti.appendChild(b);
    });
    disegna();
    area.appendChild(el("p", { class: "g-info", text: "INDOVINA LA PAROLA. TOCCA LE LETTERE." }));
    [aiuto, vite, mostra, tasti].forEach(function (x) { area.appendChild(x); });
  }

  // ---------------- QUIZ A TEMPO
  function quiz() {
    var tempo = 60, punti = 0, giro = 0;
    var barra = el("div", { class: "g-tempo" }, [el("span")]), info = el("p", { class: "g-info" }), box = el("div", { class: "g-quiz" });
    area.appendChild(el("p", { class: "g-info", text: "CHE COS'È? RISPONDI VELOCE: HAI 60 SECONDI!" }));
    area.appendChild(barra); area.appendChild(info); area.appendChild(box);
    function stato() { info.textContent = "⏱️ " + tempo + " SECONDI · ⭐ " + punti + " PUNTI"; barra.firstChild.style.width = (tempo / 60 * 100) + "%"; }
    function domanda() {
      box.innerHTML = ""; giro++;
      var giusta = prendi(1)[0], altre = mescola(P.filter(function (x) { return x.w !== giusta.w; })).slice(0, 2);
      box.appendChild(el("div", { class: "emo grande", text: giusta.e }));
      mescola([giusta].concat(altre)).forEach(function (o) {
        box.appendChild(el("button", { class: "g-btn op", text: o.w, on: function (ev) {
          if (o.w === giusta.w) { punti++; ev.target.classList.add("ok"); } else { ev.target.classList.add("no"); tempo = Math.max(0, tempo - 3); }
          stato(); setTimeout(domanda, 350);
        } }));
      });
    }
    stato(); domanda();
    window._timer = setInterval(function () {
      tempo--; stato();
      if (tempo <= 0) { clearInterval(window._timer); box.innerHTML = "";
        var r = leggi("quiz-" + G.id); if (punti > r) scrivi("quiz-" + G.id, punti);
        fine("TEMPO FINITO! HAI FATTO " + punti + " PUNTI." + (punti > r ? " NUOVO RECORD! 🏆" : " RECORD: " + r + " PUNTI."), quiz); }
    }, 1000);
  }

  // ---------------- CERCA LA PAROLA
  function cerca() {
    var N = 10, griglia = [], posti = [];
    var parole = prendi(12).map(function (p) { return nome(p.w).replace(/[^A-ZÀÈÉÌÒÙ]/g, "").normalize("NFD").replace(/[̀-ͯ]/g, ""); })
      .filter(function (w) { return w.length >= 3 && w.length <= N; }).slice(0, 6);
    for (var r = 0; r < N; r++) griglia.push(new Array(N).fill(""));
    var messe = [];
    parole.forEach(function (w) {
      for (var t = 0; t < 200; t++) {
        var oriz = Math.random() < .5, r0 = Math.floor(Math.random() * (oriz ? N : N - w.length + 1)), c0 = Math.floor(Math.random() * (oriz ? N - w.length + 1 : N));
        var ok = true;
        for (var i = 0; i < w.length; i++) { var g = griglia[r0 + (oriz ? 0 : i)][c0 + (oriz ? i : 0)]; if (g && g !== w[i]) { ok = false; break; } }
        if (!ok) continue;
        var celle = [];
        for (i = 0; i < w.length; i++) { var rr = r0 + (oriz ? 0 : i), cc = c0 + (oriz ? i : 0); griglia[rr][cc] = w[i]; celle.push(rr * N + cc); }
        messe.push({ w: w, celle: celle }); break;
      }
    });
    var ABC = "ABCDEFGHILMNOPRSTUVZ";
    var tab = el("div", { class: "g-cerca" }), lista = el("div", { class: "g-lista" }), trovate = 0, primo = null, bottoni = [];
    for (r = 0; r < N; r++) for (var c = 0; c < N; c++) {
      if (!griglia[r][c]) griglia[r][c] = ABC[Math.floor(Math.random() * ABC.length)];
      (function (idx) {
        var b = el("button", { class: "g-lettera", text: griglia[Math.floor(idx / N)][idx % N] });
        b.onclick = function () {
          if (primo === null) { primo = idx; b.classList.add("sel"); return; }
          var a = Math.min(primo, idx), z = Math.max(primo, idx);
          bottoni[primo].classList.remove("sel"); primo = null;
          var m = messe.filter(function (x) { return !x.fatta && x.celle[0] === a && x.celle[x.celle.length - 1] === z; })[0];
          if (m) { m.fatta = true; trovate++; m.celle.forEach(function (k) { bottoni[k].classList.add("ok"); }); m.li.classList.add("ok"); voce(m.w);
            if (trovate === messe.length) fine("BRAVO! HAI TROVATO TUTTE LE PAROLE!", cerca); }
          else { b.classList.add("no"); setTimeout(function () { b.classList.remove("no"); }, 400); }
        };
        bottoni[idx] = b; tab.appendChild(b);
      })(r * N + c);
    }
    messe.forEach(function (m) { m.li = el("span", { text: m.w }); lista.appendChild(m.li); });
    area.appendChild(el("p", { class: "g-info", text: "TROVA LE PAROLE: TOCCA LA PRIMA E L'ULTIMA LETTERA. SONO IN ORIZZONTALE → O IN VERTICALE ↓." }));
    area.appendChild(lista); area.appendChild(tab);
  }

  var h = (location.hash || "").slice(1);
  apri(["memory", "impiccato", "quiz", "cerca"].indexOf(h) >= 0 ? h : "memory");
})();
