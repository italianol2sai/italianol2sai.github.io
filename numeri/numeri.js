// Nomi dei numeri da 1 a 1000, divisi in pezzi (centinaia, decine, unità) per colorarli.
// Usato da numeri/index.html e numeri/giochi.html.
(function () {
  var UNITS = ["", "uno", "due", "tre", "quattro", "cinque", "sei", "sette", "otto", "nove"];
  var TEENS = ["dieci", "undici", "dodici", "tredici", "quattordici", "quindici",
               "sedici", "diciassette", "diciotto", "diciannove"];
  var TENS = ["", "", "venti", "trenta", "quaranta", "cinquanta", "sessanta", "settanta", "ottanta", "novanta"];

  // pezzi: [{t: testo, k: "c" | "d" | "u"}]
  function pezzi(n) {
    if (n === 1000) return [{ t: "mille", k: "c" }];
    var h = Math.floor(n / 100), r = n % 100, out = [];
    if (h) out.push({ t: h === 1 ? "cento" : UNITS[h] + "cento", k: "c" });
    if (r) {
      if (r < 10) out.push({ t: UNITS[r], k: "u" });
      else if (r < 20) out.push({ t: TEENS[r - 10], k: "d" });
      else {
        var t = Math.floor(r / 10), u = r % 10, d = TENS[t];
        if (u === 1 || u === 8) d = d.slice(0, -1);          // ventuno, ventotto
        out.push({ t: d, k: "d" });
        if (u) out.push({ t: UNITS[u], k: "u" });
      }
    }
    // cento + otto → centotto, cento + ottanta → centottanta
    if (h && out.length > 1 && out[1].t.charAt(0) === "o") out[0] = { t: out[0].t.slice(0, -1), k: "c" };
    // ventitré, centotré (ma: tre)
    var last = out[out.length - 1];
    if (n > 10 && last.t === "tre") last.t = "tré";
    return out;
  }
  function nome(n) { return pezzi(n).map(function (p) { return p.t; }).join(""); }

  // Come si scompone: 345 → [300, 40, 5]
  function somma(n) {
    if (n === 1000) return [1000];
    var h = Math.floor(n / 100) * 100, r = n % 100, out = [];
    if (h) out.push(h);
    if (r >= 20) { out.push(Math.floor(r / 10) * 10); if (r % 10) out.push(r % 10); }
    else if (r) out.push(r);
    return out;
  }

  var voci = [];
  function voce(testo, rate) {
    try {
      speechSynthesis.cancel();
      var u = new SpeechSynthesisUtterance(String(testo).toLowerCase());
      u.lang = "it-IT"; u.rate = rate || 0.8;
      if (!voci.length) voci = speechSynthesis.getVoices();
      var it = voci.filter(function (x) { return x.lang && x.lang.indexOf("it") === 0; })[0];
      if (it) u.voice = it;
      speechSynthesis.speak(u);
    } catch (e) {}
  }
  try { speechSynthesis.onvoiceschanged = function () { voci = speechSynthesis.getVoices(); }; } catch (e) {}

  window.NUMERI = { nome: nome, pezzi: pezzi, somma: somma, voce: voce };
})();
