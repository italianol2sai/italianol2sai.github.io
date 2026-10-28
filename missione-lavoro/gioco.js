// Motore del gioco «Missione lavoro». I contenuti stanno in domande.js.
(function () {
  "use strict";

  var M = window.MISSIONE;
  var P = window.PERSONE;
  var STANZE = M.stanze;
  var CHIAVE_SALVA = "missione-lavoro-v2";
  var PUNTI_PRIMO = 10, PUNTI_DOPO = 5;
  var MSG_SI = ["BRAVO! RISPOSTA CORRETTA!", "OTTIMO!", "ESATTO!"];
  var MSG_NO = ["NON ANCORA. PROVA DI NUOVO!", "RIPROVA. GUARDA BENE!"];

  var root = document.getElementById("gioco");
  var S; // stato salvato
  var Q; // stato della prova in corso (non salvato)

  // ---------- salvataggio ----------
  function statoVuoto() {
    return { s: 0, p: 0, res: {}, lettere: STANZE.map(function () { return false; }), fine: false };
  }
  function carica() {
    try {
      var d = JSON.parse(localStorage.getItem(CHIAVE_SALVA));
      if (d && d.res && d.lettere && d.lettere.length === STANZE.length) {
        // se tutte le prove di una stanza sono fatte, la lettera è presa
        STANZE.forEach(function (st, s) {
          if (st.prove.every(function (_, p) { return d.res[chiave(s, p)]; })) d.lettere[s] = true;
        });
        return d;
      }
    } catch (e) {}
    return statoVuoto();
  }
  function salva() {
    try { localStorage.setItem(CHIAVE_SALVA, JSON.stringify(S)); } catch (e) {}
  }

  // ---------- utilità ----------
  function el(tag, attrs, figli) {
    var n = document.createElement(tag);
    if (attrs) for (var k in attrs) {
      if (k === "class") n.className = attrs[k];
      else if (k === "text") n.textContent = attrs[k];
      else if (k.slice(0, 2) === "on") n.addEventListener(k.slice(2), attrs[k]);
      else n.setAttribute(k, attrs[k]);
    }
    (figli || []).forEach(function (f) {
      if (f == null) return;
      n.appendChild(typeof f === "string" ? document.createTextNode(f) : f);
    });
    return n;
  }
  function mescola(arr) {
    var a = arr.slice();
    for (var i = a.length - 1; i > 0; i--) {
      var j = Math.floor(Math.random() * (i + 1));
      var t = a[i]; a[i] = a[j]; a[j] = t;
    }
    return a;
  }
  // mescola gli indici 0..n-1 evitando, se possibile, l'ordine originale
  function indiciMescolati(n) {
    var base = []; for (var i = 0; i < n; i++) base.push(i);
    var a = mescola(base), prove = 0;
    while (n > 1 && prove++ < 10 && a.every(function (v, k) { return v === k; })) a = mescola(base);
    return a;
  }
  function caso(lista) { return lista[Math.floor(Math.random() * lista.length)]; }
  function chiave(s, p) { return STANZE[s].id + "-" + p; }
  function totaleProve() { return STANZE.reduce(function (t, st) { return t + st.prove.length; }, 0); }
  function puntiFatti() {
    var t = 0; for (var k in S.res) t += S.res[k].pti; return t;
  }
  function schermo(figli) {
    root.innerHTML = "";
    root.appendChild(el("div", { class: "schermo" }, figli));
    window.scrollTo(0, 0);
    aggiornaBarra();
  }
  // una battuta: ritratto + nome + fumetto
  function battuta(chi, testo) {
    var p = P[chi];
    var faccia = el("div", { class: "faccia" });
    faccia.innerHTML = p.svg;
    return el("div", { class: "guida" + (chi === "mohammad" ? " lui" : "") }, [
      faccia,
      el("div", { class: "fumetto" }, [el("b", { text: p.nome + " · " + p.ruolo }), el("p", { text: testo })])
    ]);
  }
  function silvia(testo) { return battuta("silvia", testo); }
  function dialogo(righe) { return righe.map(function (r) { return battuta(r[0], r[1]); }); }
  function btn(testo, cls, fn) {
    return el("button", { type: "button", class: "btn " + cls, onclick: fn, text: testo });
  }
  function aggiornaBarra() {
    var b = document.getElementById("badge");
    b.innerHTML = "";
    STANZE.forEach(function (st, i) {
      b.appendChild(el("span", { class: S.lettere[i] ? "preso" : "", text: S.lettere[i] ? st.lettera : "" }));
    });
    document.getElementById("punti").textContent = puntiFatti() + " PUNTI";
  }

  // ---------- voce (se il telefono la ha) ----------
  var voce = "speechSynthesis" in window && typeof SpeechSynthesisUtterance !== "undefined";
  function parla(testo) {
    if (!voce) return;
    try {
      speechSynthesis.cancel();
      var u = new SpeechSynthesisUtterance(testo.toLowerCase().replace(/[«»]/g, ""));
      u.lang = "it-IT"; u.rate = 0.9;
      speechSynthesis.speak(u);
    } catch (e) {}
  }
  function zitto() { if (voce) try { speechSynthesis.cancel(); } catch (e) {} }

  // ---------- copertina ----------
  function copertina() {
    var iniziato = Object.keys(S.res).length > 0;
    var conferma = el("div", { class: "schermo", hidden: "" }, [
      el("p", { class: "domanda", text: "VUOI RICOMINCIARE? PERDI I PUNTI DI ADESSO." }),
      el("div", { class: "attrezzi" }, [
        btn("SÌ, RICOMINCIO", "btn-vai", function () { S = statoVuoto(); salva(); mappa(); }),
        btn("NO", "btn-piano", function () { conferma.hidden = true; })
      ])
    ]);
    var porte = el("div", { class: "porte-mini", "aria-hidden": "true" });
    STANZE.forEach(function () { porte.appendChild(el("i")); });
    var azioni = [];
    if (S.fine) {
      azioni.push(btn("VEDI IL RISULTATO", "btn-vai", risultati));
    } else {
      azioni.push(btn(iniziato ? "CONTINUA LA MISSIONE ▶" : "INIZIA LA MISSIONE ▶", "btn-vai", mappa));
    }
    if (iniziato) azioni.push(btn("RICOMINCIA DA CAPO", "btn-piano", function () { conferma.hidden = false; }));
    schermo([
      el("div", { class: "copertina" }, [
        el("p", { class: "sopra", style: "color:inherit;opacity:.8", text: "ITALIANO L2 · IL LAVORO" }),
        el("h1", {}, [M.titolo, el("span", { text: M.sottotitolo })]),
        porte
      ]),
      el("div", { class: "schermo" }, dialogo(M.intro)),
      el("div", { class: "schermo" }, azioni),
      conferma
    ]);
  }

  // ---------- mappa delle porte ----------
  function stanzaAttuale() {
    for (var i = 0; i < STANZE.length; i++) if (!S.lettere[i]) return i;
    return STANZE.length; // tutte aperte: tocca alla porta finale
  }
  function mappa() {
    zitto();
    var ora = stanzaAttuale();
    var griglia = el("div", { class: "porte" });
    STANZE.forEach(function (st, i) {
      var stato = S.lettere[i] ? "aperta" : (i === ora ? "adesso" : "chiusa");
      var etichetta = "PORTA " + (i + 1) + ": " + st.titolo + (stato === "aperta" ? " (APERTA)" : stato === "chiusa" ? " (CHIUSA)" : "");
      var b = el("button", { type: "button", class: "porta " + stato, "aria-label": etichetta,
        onclick: function () {
          if (stato === "adesso") ingresso(i);
          else if (stato === "chiusa") avviso.querySelector("p").textContent = "QUESTA PORTA È CHIUSA. PRIMA APRI LA PORTA " + (ora + 1) + ".";
        } }, [
        el("span", { class: "num", text: stato === "aperta" ? st.lettera : String(i + 1) }),
        el("span", { class: "ic", "aria-hidden": "true", text: stato === "chiusa" ? "🔒" : st.icona }),
        el("span", { class: "nome", text: st.titolo })
      ]);
      if (stato === "aperta") b.disabled = true;
      griglia.appendChild(b);
    });
    var tutte = ora === STANZE.length;
    var fin = el("button", { type: "button", class: "porta porta-finale " + (tutte ? "adesso" : "chiusa"),
      onclick: function () {
        if (tutte) finale();
        else avviso.querySelector("p").textContent = "L’ULTIMA PORTA È CHIUSA. PRIMA APRI LA PORTA " + (ora + 1) + ".";
      } }, [
      el("span", { class: "num", text: "?" }),
      el("span", { class: "ic", "aria-hidden": "true", text: tutte ? "🏆" : "🔒" }),
      el("span", { class: "nome", text: "ULTIMA PORTA" })
    ]);
    griglia.appendChild(fin);

    var avviso;
    var testoGuida = tutte
      ? "HAI TUTTE LE LETTERE! TOCCA L’ULTIMA PORTA."
      : (ora === 0 ? "TOCCA LA PORTA 1 PER COMINCIARE." : "BENE! ADESSO TOCCA LA PORTA " + (ora + 1) + ".");
    avviso = silvia(testoGuida);
    schermo([
      el("p", { class: "sopra", text: "LE PORTE" }),
      el("h2", { text: "SCEGLI LA PORTA" }),
      avviso,
      griglia,
      btn("◀ TORNA ALL’INIZIO", "btn-piano", copertina)
    ]);
  }

  // ---------- ingresso nella stanza ----------
  function ingresso(s) {
    var st = STANZE[s];
    // se la stanza era già cominciata riprende dalla prova giusta
    if (S.lettere[s]) { mappa(); return; }
    var p = (S.s === s && S.p < st.prove.length) ? S.p : 0;
    S.s = s; S.p = p; salva();
    schermo([
      el("p", { class: "sopra", text: "PORTA " + (s + 1) + " DI " + STANZE.length }),
      el("div", { class: "grande-ic", "aria-hidden": "true", text: st.icona }),
      el("h2", { text: st.titolo }),
      el("div", { class: "schermo" }, dialogo(st.storia)),
      el("p", { class: "sopra", text: P[st.chi].nome + " TI AIUTA. CI SONO " + st.prove.length + " PROVE." }),
      btn(p > 0 ? "CONTINUA ▶" : "ENTRA ▶", "btn-vai", function () { prova(s, S.p); }),
      btn("◀ LE PORTE", "btn-piano", mappa)
    ]);
  }

  // ---------- una prova ----------
  function prova(s, p) {
    zitto();
    var st = STANZE[s], d = st.prove[p];
    Q = { s: s, p: p, errori: 0, aiuto: false, finito: false };
    S.s = s; S.p = p; salva();

    var passi = el("div", { class: "passi", "aria-hidden": "true" });
    st.prove.forEach(function (_, i) { passi.appendChild(el("i", { class: i < p ? "fatto" : i === p ? "ora" : "" })); });

    var esito = el("div", { class: "esito", hidden: "", role: "status" });
    var avanti = btn(p === st.prove.length - 1 ? "PRENDI LA CHIAVE 🔑" : "AVANTI ▶", "btn-vai", function () { prossima(); });
    avanti.hidden = true;

    var corpo = el("div", { class: "prova" });
    if (d.icona) corpo.appendChild(el("div", { class: "grande-ic", "aria-hidden": "true", text: d.icona }));
    corpo.appendChild(el("p", { class: "domanda", text: d.domanda }));
    if (d.documento && d.tipo !== "errore") corpo.appendChild(documento(d.documento));

    var api = {
      giusto: function () { giusto(d, esito, avanti); },
      sbagliato: function () { sbagliato(d, esito); }
    };
    var testoVoce = d.domanda;
    var area;
    switch (d.tipo) {
      case "scelta": area = faiScelta(d, api); testoVoce += ". " + d.risposte.map(function (r) { return r.t; }).join(". "); break;
      case "vf": area = faiVF(d, api); testoVoce += ". VERO O FALSO?"; break;
      case "completa": area = faiCompleta(d, api, corpo); testoVoce += ". " + d.frase.replace("___", "…") + ". " + d.risposte.join(". "); break;
      case "collega": area = faiCollega(d, api); break;
      case "ordine": area = faiOrdine(d, api); testoVoce += ". " + d.items.join(". "); break;
      case "errore": area = faiErrore(d, api); testoVoce += ". " + d.righe.join(". "); break;
    }
    if (d.documento && d.documento.righe && d.tipo !== "errore") testoVoce = d.documento.righe.join(" ") + " " + testoVoce;
    if (d.documento && d.documento.tabella) testoVoce = d.documento.tabella.map(function (r) { return r.join(" "); }).join(". ") + ". " + testoVoce;
    corpo.appendChild(area);

    var attrezzi = el("div", { class: "attrezzi" }, [
      voce ? btn("🔊 ASCOLTA", "btn-piano", function () { parla(testoVoce); }) : null,
      btn("💡 AIUTO", "btn-piano", function () { mostraAiuto(d, esito); })
    ]);
    if (!voce) attrezzi.style.gridTemplateColumns = "1fr";

    schermo([
      el("div", { class: "testa" }, [
        el("p", { class: "sopra", text: "PORTA " + (s + 1) + " · " + st.titolo + " · PROVA " + (p + 1) + " DI " + st.prove.length }),
        passi
      ]),
      corpo,
      esito,
      avanti,
      attrezzi,
      btn("◀ LE PORTE", "btn-piano", mappa)
    ]);
  }

  function documento(doc) {
    var box = el("div", { class: "doc" }, [el("span", { class: "t", text: doc.titolo })]);
    (doc.righe || []).forEach(function (r) { box.appendChild(el("p", { text: r })); });
    if (doc.tabella) {
      var tb = el("table");
      doc.tabella.forEach(function (r) { tb.appendChild(el("tr", {}, [el("td", { text: r[0] }), el("td", { text: r[1] })])); });
      box.appendChild(tb);
    }
    return box;
  }

  function mostraEsito(box, cls, titolo, sotto) {
    box.className = "esito " + cls;
    box.innerHTML = "";
    box.appendChild(el("span", { text: titolo }));
    if (sotto) box.appendChild(el("small", { text: sotto }));
    box.hidden = false;
    try { box.scrollIntoView({ block: "nearest" }); } catch (e) {}
  }
  function mostraAiuto(d, box) {
    if (Q.finito) return;
    Q.aiuto = true;
    mostraEsito(box, "aiuto", "💡 " + P[STANZE[Q.s].chi].nome + " DICE:", d.aiuto);
  }
  function sbagliato(d, box) {
    Q.errori++;
    if (Q.errori >= 2) { Q.aiuto = true; mostraEsito(box, "no", caso(MSG_NO), "💡 " + d.aiuto); }
    else mostraEsito(box, "no", caso(MSG_NO));
  }
  function giusto(d, box, avanti) {
    Q.finito = true;
    var primo = Q.errori === 0 && !Q.aiuto;
    var k = chiave(Q.s, Q.p);
    if (!S.res[k]) S.res[k] = { pti: primo ? PUNTI_PRIMO : PUNTI_DOPO, primo: primo };
    S.p = Q.p + 1;
    if (S.p >= STANZE[Q.s].prove.length) { S.lettere[Q.s] = true; S.s = Q.s + 1; S.p = 0; }
    salva();
    aggiornaBarra();
    mostraEsito(box, "si", "✓ " + caso(MSG_SI) + "  +" + S.res[k].pti, d.spiega);
    avanti.hidden = false;
    try { avanti.focus({ preventScroll: true }); } catch (e) {}
  }
  function prossima() {
    var st = STANZE[Q.s];
    if (Q.p + 1 < st.prove.length) prova(Q.s, Q.p + 1);
    else chiaveTrovata(Q.s);
  }
  function blocca(lista) { lista.forEach(function (b) { b.disabled = true; }); }

  // --- scegli una risposta ---
  function faiScelta(d, api) {
    var box = el("div", { class: "scelte" });
    var bottoni = [];
    indiciMescolati(d.risposte.length).forEach(function (i) {
      var r = d.risposte[i];
      var b = el("button", { type: "button", class: "scelta" }, [
        r.i ? el("span", { class: "i", "aria-hidden": "true", text: r.i }) : null,
        el("span", { text: r.t })
      ]);
      b.addEventListener("click", function () {
        if (Q.finito) return;
        if (i === d.correct) { b.classList.add("si"); blocca(bottoni); api.giusto(); }
        else { b.classList.add("no"); b.disabled = true; api.sbagliato(); }
      });
      bottoni.push(b); box.appendChild(b);
    });
    return box;
  }

  // --- vero o falso ---
  function faiVF(d, api) {
    var box = el("div", { class: "vf" });
    var bottoni = [];
    [[true, "✅ VERO"], [false, "❌ FALSO"]].forEach(function (o) {
      var b = el("button", { type: "button", class: "scelta", text: o[1] });
      b.addEventListener("click", function () {
        if (Q.finito) return;
        if (o[0] === d.correct) { b.classList.add("si"); blocca(bottoni); api.giusto(); }
        else { b.classList.add("no"); b.disabled = true; api.sbagliato(); }
      });
      bottoni.push(b); box.appendChild(b);
    });
    return box;
  }

  // --- completa la frase ---
  function faiCompleta(d, api, corpo) {
    var parti = d.frase.split("___");
    var buco = el("span", { class: "buco", text: " " });
    corpo.appendChild(el("p", { class: "frase" }, [parti[0], buco, parti[1] || ""]));
    var box = el("div", { class: "scelte" });
    var bottoni = [];
    indiciMescolati(d.risposte.length).forEach(function (i) {
      var b = el("button", { type: "button", class: "scelta", style: "justify-content:center", text: d.risposte[i] });
      b.addEventListener("click", function () {
        if (Q.finito) return;
        if (i === d.correct) { b.classList.add("si"); buco.textContent = d.risposte[i]; blocca(bottoni); api.giusto(); }
        else { b.classList.add("no"); b.disabled = true; api.sbagliato(); }
      });
      bottoni.push(b); box.appendChild(b);
    });
    return box;
  }

  // --- collega: tocca a sinistra, poi a destra ---
  function faiCollega(d, api) {
    var sinistra = el("div", { class: "col" }), destra = el("div", { class: "col" });
    var scelto = null, fatte = 0, numero = 0;
    var bS = [], bD = [];
    function grosso(t) { return /^\S+$/.test(t) && !/[A-Z]/.test(t) ? " grosso" : ""; }
    indiciMescolati(d.coppie.length).forEach(function (i) {
      var t = d.coppie[i][0];
      var b = el("button", { type: "button", class: "scelta" + grosso(t), text: t });
      b.dataset.k = i;
      b.addEventListener("click", function () {
        if (b.classList.contains("coppia")) return;
        bS.forEach(function (x) { x.classList.remove("sel"); });
        b.classList.add("sel"); scelto = b;
      });
      bS.push(b); sinistra.appendChild(b);
    });
    indiciMescolati(d.coppie.length).forEach(function (i) {
      var b = el("button", { type: "button", class: "scelta", text: d.coppie[i][1] });
      b.addEventListener("click", function () {
        if (b.classList.contains("coppia") || Q.finito) return;
        if (!scelto) { mostraEsito(document.querySelector(".esito"), "aiuto", "PRIMA TOCCA A SINISTRA.", null); return; }
        if (Number(scelto.dataset.k) === i) {
          numero++;
          [scelto, b].forEach(function (x) {
            x.classList.remove("sel"); x.classList.add("coppia"); x.disabled = true;
            x.appendChild(el("span", { class: "n", text: String(numero) }));
          });
          scelto = null; fatte++;
          if (fatte === d.coppie.length) api.giusto();
        } else {
          api.sbagliato();
        }
      });
      bD.push(b); destra.appendChild(b);
    });
    return el("div", { class: "collega" }, [sinistra, destra]);
  }

  // --- metti in ordine: tocca le azioni una dopo l'altra ---
  function faiOrdine(d, api) {
    var fila = el("div", { class: "fila" });
    var slot = d.items.map(function (_, i) {
      var s = el("div", { class: "slot" }, [el("b", { text: String(i + 1) }), el("span", { text: "" })]);
      fila.appendChild(s); return s;
    });
    var box = el("div", { class: "scelte" });
    var prossimo = 0;
    indiciMescolati(d.items.length).forEach(function (i) {
      var b = el("button", { type: "button", class: "scelta", text: d.items[i] });
      b.addEventListener("click", function () {
        if (Q.finito) return;
        if (i === prossimo) {
          slot[prossimo].classList.add("pieno");
          slot[prossimo].lastChild.textContent = d.items[i];
          b.hidden = true; prossimo++;
          if (prossimo === d.items.length) api.giusto();
        } else {
          api.sbagliato();
        }
      });
      box.appendChild(b);
    });
    return el("div", { class: "schermo", style: "gap:14px" }, [
      fila, el("p", { class: "sopra", text: "TOCCA: PRIMA, POI, ALLA FINE" }), box
    ]);
  }

  // --- trova l'errore: tocca la riga sbagliata ---
  function faiErrore(d, api) {
    var box = el("div", { class: "doc righe-doc" }, [el("span", { class: "t", text: d.documento.titolo })]);
    var bottoni = [];
    d.righe.forEach(function (r, i) {
      var b = el("button", { type: "button", class: "scelta", text: r });
      b.addEventListener("click", function () {
        if (Q.finito) return;
        if (i === d.correct) { b.classList.add("si"); blocca(bottoni); api.giusto(); }
        else { b.classList.add("no"); b.disabled = true; api.sbagliato(); }
      });
      bottoni.push(b); box.appendChild(b);
    });
    return box;
  }

  // ---------- chiave trovata ----------
  function chiaveTrovata(s) {
    var st = STANZE[s];
    S.lettere[s] = true;
    salva();
    var ultima = s === STANZE.length - 1;
    schermo([
      el("div", { class: "chiave" }, [
        el("p", { class: "sopra", style: "color:inherit;opacity:.85", text: "PORTA " + (s + 1) + " APERTA" }),
        el("h2", { text: "OTTIMO! HAI TROVATO LA CHIAVE!" }),
        el("div", { class: "lettera-grande", "aria-label": "LETTERA " + st.lettera, text: st.lettera }),
        el("p", { text: "LA LETTERA È SUL TUO BADGE, IN ALTO." })
      ]),
      battuta(st.fine[0], st.fine[1]),
      ultima ? silvia("HAI TUTTE LE " + STANZE.length + " LETTERE! ADESSO APRI L’ULTIMA PORTA.") : null,
      btn(ultima ? "VAI ALL’ULTIMA PORTA ▶" : "TORNA ALLE PORTE ▶", "btn-vai", mappa)
    ]);
  }

  // ---------- porta finale ----------
  function finale() {
    var campo = el("input", { id: "codice", class: "codice", type: "text", maxlength: "12",
      autocomplete: "off", autocapitalize: "characters", spellcheck: "false", "aria-label": "LA PAROLA SEGRETA" });
    var esito = el("div", { class: "esito", hidden: "", role: "status" });
    var lettere = STANZE.map(function (st) { return st.lettera; }).join(" · ");
    function prova() {
      var v = campo.value.toUpperCase().replace(/[^A-Z]/g, "");
      if (v === M.parolaSegreta) { S.fine = true; salva(); risultati(); }
      else mostraEsito(esito, "no", "NON ANCORA. PROVA DI NUOVO!", "💡 GUARDA IL TUO BADGE: " + lettere);
    }
    campo.addEventListener("keydown", function (e) { if (e.key === "Enter") prova(); });
    schermo([
      el("p", { class: "sopra", text: "ULTIMA PORTA" }),
      el("div", { class: "grande-ic", "aria-hidden": "true", text: "🔐" }),
      el("h2", { text: "LA PORTA DEL TUO FUTURO" }),
      el("div", { class: "schermo" }, dialogo(M.finale)),
      campo,
      btn("APRI LA PORTA 🔓", "btn-vai", prova),
      esito,
      btn("◀ LE PORTE", "btn-piano", mappa)
    ]);
  }

  // ---------- risultati ----------
  function risultati() {
    zitto();
    var n = totaleProve();
    var fatte = Object.keys(S.res).length;
    var primo = 0;
    for (var k in S.res) if (S.res[k].primo) primo++;
    var perc = n ? Math.round(primo / n * 100) : 0;
    var bene = [], ripassa = [];
    STANZE.forEach(function (st, s) {
      var ok = st.prove.every(function (_, p) { var r = S.res[chiave(s, p)]; return r && r.primo; });
      (ok ? bene : ripassa).push(st);
    });
    function vocePorta(st, conLink) {
      var li = el("li", {}, [el("span", { "aria-hidden": "true", text: st.icona }), el("span", { text: st.titolo })]);
      if (conLink) {
        var links = el("span", { style: "display:block" });
        [st.lezione].forEach(function (lz) {
          if (!lz) return;
          links.appendChild(el("a", { href: M.sito + lz.link, target: "_blank", rel: "noopener", text: "📖 " + lz.titolo }));
          links.appendChild(el("br"));
        });
        li.lastChild.appendChild(links);
      }
      return li;
    }
    var liste = [];
    if (bene.length) liste.push(el("div", { class: "lista" }, [
      el("h3", { text: "✅ HAI RIPASSATO BENE" }),
      el("ul", {}, bene.map(function (st) { return vocePorta(st, false); }))
    ]));
    if (ripassa.length) liste.push(el("div", { class: "lista" }, [
      el("h3", { text: "📖 DA RIPASSARE" }),
      el("p", { class: "nota", text: "QUI HAI FATTO QUALCHE ERRORE O HAI USATO L’AIUTO. GUARDA ANCORA LA LEZIONE." }),
      el("ul", {}, ripassa.map(function (st) { return vocePorta(st, true); }))
    ]));
    schermo([
      el("div", { class: "chiave" }, [
        el("div", { class: "grande-ic", "aria-hidden": "true", text: "🏆" }),
        el("h2", { text: "MISSIONE COMPLETATA!" }),
        el("p", { text: M.vittoria })
      ]),
      battuta("mohammad", "GRAZIE! SENZA DI TE NON CE LA FACEVO!"),
      el("p", { text: "HAI IMPARATO NUOVE PAROLE E NUOVE STRATEGIE PER CERCARE LAVORO." }),
      el("div", { class: "numeri" }, [
        el("div", {}, [el("b", { text: String(puntiFatti()) }), el("span", { text: "PUNTI SU " + n * PUNTI_PRIMO })]),
        el("div", {}, [el("b", { text: fatte + "/" + n }), el("span", { text: "PROVE SUPERATE" })]),
        el("div", {}, [el("b", { text: perc + "%" }), el("span", { text: "GIUSTE AL PRIMO TENTATIVO" })])
      ]),
      liste[0], liste[1],
      silvia(ripassa.length ? "PUOI RIPROVARE PER MIGLIORARE IL TUO PUNTEGGIO." : "COMPLIMENTI! ADESSO TOCCA A TE. IN BOCCA AL LUPO!"),
      el("p", { class: "nota", text: "IL PUNTEGGIO È SOLO PER TE. NON È UN CERTIFICATO E NON VA ALL’INSEGNANTE." }),
      btn("GIOCA DI NUOVO ↻", "btn-vai", function () { S = statoVuoto(); salva(); copertina(); }),
      el("a", { class: "btn btn-piano", href: M.sito, style: "text-decoration:none", text: "TORNA AL SITO" })
    ]);
  }

  // ---------- avvio ----------
  S = carica();
  copertina();
})();
