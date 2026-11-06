// Giochi per i livelli B1-C2: quiz a tempo (frasi con lo spazio), abbina, riordina la frase.
// La pagina definisce window.GIOCHI = {id, quiz: [[frase con ___, giusta, sbagliata, sbagliata], …],
//   coppie: [[a, b], …], frasi: ["frase da riordinare", …]}. Testi in minuscolo (livello A2 e oltre).
// Come negli esercizi del sito, la risposta giusta non viene mai mostrata: si riprova o si salta.
(function () {
  var G = window.GIOCHI, main = document.getElementById("giochi");
  function el(t, a, c) {
    var e = document.createElement(t);
    for (var k in a || {}) { if (k === "text") e.textContent = a[k]; else if (k === "on") e.onclick = a[k]; else e.setAttribute(k, a[k]); }
    (c || []).forEach(function (x) { if (x) e.appendChild(typeof x === "string" ? document.createTextNode(x) : x); });
    return e;
  }
  function mescola(a) { a = a.slice(); for (var i = a.length - 1; i > 0; i--) { var j = Math.floor(Math.random() * (i + 1)); var t = a[i]; a[i] = a[j]; a[j] = t; } return a; }
  function leggi(k) { try { return +localStorage.getItem(k) || 0; } catch (e) { return 0; } }
  function scrivi(k, v) { try { localStorage.setItem(k, v); } catch (e) {} }

  var area = el("div", { class: "g-area" });
  var GIOCHI = [["quiz", "⏱️", "Quiz a tempo"], ["abbina", "🔗", "Abbina"], ["riordina", "🧩", "Riordina la frase"]];
  var schede = el("div", { class: "g-schede tre", role: "tablist" });
  GIOCHI.forEach(function (g) {
    schede.appendChild(el("button", { class: "g-scheda", "data-g": g[0], on: function () { apri(g[0]); } }, [el("span", { text: g[1] }), " " + g[2]]));
  });
  main.appendChild(schede); main.appendChild(area);

  function apri(nome) {
    [].forEach.call(schede.children, function (b) { b.classList.toggle("on", b.getAttribute("data-g") === nome); });
    area.innerHTML = ""; if (window._timer) clearInterval(window._timer);
    ({ quiz: quiz, abbina: abbina, riordina: riordina })[nome]();
    try { history.replaceState(null, "", "#" + nome); } catch (e) {}
  }
  function fine(msg, ancora) {
    area.appendChild(el("div", { class: "g-fine" }, [el("p", { text: msg }), el("button", { class: "g-btn", text: "Gioca ancora ▶", on: ancora })]));
  }

  // ---------------- QUIZ A TEMPO: completa la frase
  function quiz() {
    var tempo = 90, punti = 0, ordine = mescola(G.quiz), n = 0;
    var barra = el("div", { class: "g-tempo" }, [el("span")]), info = el("p", { class: "g-info" }), box = el("div", { class: "g-quiz" });
    area.appendChild(el("p", { class: "g-info", text: "Completa la frase: hai 90 secondi. Ogni errore toglie 3 secondi." }));
    area.appendChild(barra); area.appendChild(info); area.appendChild(box);
    function stato() { info.textContent = "⏱️ " + tempo + " secondi · ⭐ " + punti + " punti"; barra.firstChild.style.width = (tempo / 90 * 100) + "%"; }
    function domanda() {
      box.innerHTML = "";
      if (n >= ordine.length) { ordine = mescola(G.quiz); n = 0; }
      var q = ordine[n++], parti = q[0].split("___");
      box.appendChild(el("p", { class: "g-frase" }, [parti[0], el("span", { class: "buco", text: "…" }), parti[1] || ""]));
      mescola(q.slice(1)).forEach(function (o) {
        box.appendChild(el("button", { class: "g-btn op", text: o, on: function (ev) {
          if (o === q[1]) { punti++; ev.target.classList.add("ok"); }
          else { ev.target.classList.add("no"); tempo = Math.max(0, tempo - 3); }
          stato(); [].forEach.call(box.querySelectorAll("button"), function (b) { b.disabled = true; });
          setTimeout(domanda, 450);
        } }));
      });
    }
    stato(); domanda();
    window._timer = setInterval(function () {
      tempo--; stato();
      if (tempo <= 0) { clearInterval(window._timer); box.innerHTML = "";
        var r = leggi("quiz-" + G.id); if (punti > r) scrivi("quiz-" + G.id, punti);
        fine("Tempo finito! Hai fatto " + punti + " punti." + (punti > r ? " Nuovo record! 🏆" : " Record: " + r + " punti."), quiz); }
    }, 1000);
  }

  // ---------------- ABBINA: tocca un elemento a sinistra e poi quello giusto a destra
  function abbina() {
    var scelte = mescola(G.coppie).slice(0, 6), sel = null, fatte = 0, errori = 0;
    var sx = el("div", { class: "g-col" }), dx = el("div", { class: "g-col" });
    scelte.forEach(function (c, i) {
      var a = el("button", { class: "g-btn op", text: c[0], "data-i": i });
      a.onclick = function () { if (a.disabled) return; if (sel) sel.classList.remove("sel"); sel = a; a.classList.add("sel"); };
      sx.appendChild(a);
    });
    mescola(scelte.map(function (c, i) { return [c[1], i]; })).forEach(function (c) {
      var b = el("button", { class: "g-btn op", text: c[0] });
      b.onclick = function () {
        if (!sel || b.disabled) return;
        if (+sel.getAttribute("data-i") === c[1]) {
          [sel, b].forEach(function (x) { x.classList.remove("sel"); x.classList.add("ok"); x.disabled = true; });
          sel = null; fatte++;
          if (fatte === scelte.length) fine(errori ? "Fatto! Hai sbagliato " + errori + (errori === 1 ? " volta." : " volte.") : "Perfetto! Nessun errore. 🏆", abbina);
        } else { errori++; b.classList.add("no"); setTimeout(function () { b.classList.remove("no"); }, 500); }
      };
      dx.appendChild(b);
    });
    area.appendChild(el("p", { class: "g-info", text: "Tocca un'espressione a sinistra, poi il suo significato a destra." }));
    area.appendChild(el("div", { class: "g-abbina" }, [sx, dx]));
  }

  // ---------------- RIORDINA LA FRASE
  function riordina() {
    var frasi = mescola(G.frasi).slice(0, 5), n = 0, giuste = 0;
    var info = el("p", { class: "g-info" }), riga = el("div", { class: "g-riga" }), pezzi = el("div", { class: "g-pezzi" }), esito = el("p", { class: "g-esito" });
    var bott = el("div", { class: "g-azioni" });
    area.appendChild(el("p", { class: "g-info", text: "Tocca le parole nell'ordine giusto. Tocca una parola nella riga per toglierla." }));
    [info, riga, pezzi, esito, bott].forEach(function (x) { area.appendChild(x); });
    function giro() {
      if (n >= frasi.length) { area.innerHTML = ""; fine("Hai riordinato bene " + giuste + " frasi su " + frasi.length + ".", riordina); return; }
      var parole = frasi[n].split(" "), primo = true;
      info.textContent = "Frase " + (n + 1) + " di " + frasi.length;
      riga.innerHTML = ""; pezzi.innerHTML = ""; esito.textContent = ""; bott.innerHTML = "";
      var mix = mescola(parole); if (mix.join(" ") === frasi[n] && parole.length > 1) mix = mix.slice(1).concat(mix[0]);
      mix.forEach(function (w) {
        var b = el("button", { class: "g-pezzo", text: w });
        b.onclick = function () { (b.parentNode === pezzi ? riga : pezzi).appendChild(b); esito.textContent = ""; };
        pezzi.appendChild(b);
      });
      bott.appendChild(el("button", { class: "g-btn", text: "Controlla ✓", on: function () {
        var fatta = [].map.call(riga.children, function (b) { return b.textContent; }).join(" ");
        if (pezzi.children.length) { esito.textContent = "Usa tutte le parole."; return; }
        if (fatta === frasi[n]) { if (primo) giuste++; esito.textContent = "✓ Giusto!"; esito.className = "g-esito ok"; n++; setTimeout(giro, 900); }
        else { primo = false; esito.textContent = "✗ Non è ancora giusto: riprova."; esito.className = "g-esito no"; }
      } }));
      bott.appendChild(el("button", { class: "g-btn op", text: "Salta ⏭", on: function () { n++; giro(); } }));
    }
    giro();
  }

  var h = (location.hash || "").slice(1);
  apri(["quiz", "abbina", "riordina"].indexOf(h) >= 0 ? h : "quiz");
})();
