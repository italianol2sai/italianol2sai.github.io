/* L'orologio (A1): disegno SVG dell'orologio con le lancette e l'ora in parole.
   Le stesse regole di _strumenti/unita_orologio.py. API: OROLOGIO.svg(h, m, px), .parole(h, m), .digitale(h, m), .voce(testo) */
(function () {
  var U = ["", "UNO", "DUE", "TRE", "QUATTRO", "CINQUE", "SEI", "SETTE", "OTTO", "NOVE", "DIECI", "UNDICI", "DODICI"];
  var E = { 5: "CINQUE", 10: "DIECI", 15: "UN QUARTO", 20: "VENTI", 25: "VENTICINQUE", 30: "MEZZA" };
  var MENO = { 40: "VENTI", 45: "UN QUARTO", 50: "DIECI", 55: "CINQUE" };
  function ora(h) { return h === 1 ? "L'UNA" : "LE " + U[h]; }
  function parole(h, m) {
    var coda = "";
    if (MENO[m]) { h = (h + 1) % 24; coda = " MENO " + MENO[m]; }
    else if (m) coda = " E " + E[m];
    var b = h === 12 ? "MEZZOGIORNO" : h === 0 ? "MEZZANOTTE" : ora(h % 12 || 12);
    return (b === "L'UNA" || b === "MEZZOGIORNO" || b === "MEZZANOTTE" ? "È " : "SONO ") + b + coda;
  }
  function svg(h, m, px) {
    px = px || 160;
    var s = '<svg viewBox="0 0 200 200" width="' + px + '" height="' + px + '" role="img" aria-label="OROLOGIO">' +
      '<circle cx="100" cy="100" r="96" fill="#fff" stroke="#E07A1F" stroke-width="7"/>';
    for (var i = 0; i < 60; i++) {
      var a = i * 6 * Math.PI / 180, r1 = i % 5 ? 86 : 80;
      s += '<line x1="' + (100 + r1 * Math.sin(a)).toFixed(1) + '" y1="' + (100 - r1 * Math.cos(a)).toFixed(1) +
        '" x2="' + (100 + 91 * Math.sin(a)).toFixed(1) + '" y2="' + (100 - 91 * Math.cos(a)).toFixed(1) +
        '" stroke="#3B2410" stroke-width="' + (i % 5 ? 1.2 : 3.5) + '"/>';
    }
    s += '<g font-family="Arial,sans-serif" font-size="21" font-weight="bold" fill="#3B2410" text-anchor="middle">';
    for (var n = 1; n <= 12; n++) { var b = n * 30 * Math.PI / 180;
      s += '<text x="' + (100 + 67 * Math.sin(b)).toFixed(1) + '" y="' + (100 - 67 * Math.cos(b) + 7).toFixed(1) + '">' + n + '</text>'; }
    s += '</g>';
    var ah = ((h % 12) * 30 + m * 0.5) * Math.PI / 180, am = m * 6 * Math.PI / 180;
    s += '<line x1="100" y1="100" x2="' + (100 + 46 * Math.sin(ah)).toFixed(1) + '" y2="' + (100 - 46 * Math.cos(ah)).toFixed(1) +
      '" stroke="#c8323b" stroke-width="9" stroke-linecap="round"/>' +
      '<line x1="100" y1="100" x2="' + (100 + 74 * Math.sin(am)).toFixed(1) + '" y2="' + (100 - 74 * Math.cos(am)).toFixed(1) +
      '" stroke="#2f63ad" stroke-width="5" stroke-linecap="round"/><circle cx="100" cy="100" r="7" fill="#3B2410"/></svg>';
    return s;
  }
  // orologio «delle 24 ore» (Erila 2026-11-27): ore 1-12 grandi, 13-24 nel cerchio grigio, minuti fuori nei cerchietti
  function svg24(h, m, px) {
    px = px || 260;
    var C = 150, P = function (a, r) { a = a * Math.PI / 180; return [C + r * Math.sin(a), C - r * Math.cos(a)]; }, f = function (x) { return x.toFixed(1); };
    var s = '<svg class="clk24" viewBox="0 0 300 300" width="' + px + '" height="' + px + '" role="img" aria-label="OROLOGIO 24 ORE">' +
      '<circle cx="150" cy="150" r="114" fill="#fff" stroke="#E07A1F" stroke-width="6"/><circle cx="150" cy="150" r="62" fill="#eeeeee" stroke="#999" stroke-width="1.5"/>';
    for (var i = 0; i < 60; i++) { var a = P(i * 6, i % 5 ? 106 : 100), b = P(i * 6, 111);
      s += '<line x1="' + f(a[0]) + '" y1="' + f(a[1]) + '" x2="' + f(b[0]) + '" y2="' + f(b[1]) + '" stroke="#3B2410" stroke-width="' + (i % 5 ? 1 : 3) + '"/>'; }
    var T = '<text text-anchor="middle" font-family="Arial,sans-serif" font-weight="bold" ';
    for (var n = 0; n < 12; n++) { var q = P(n * 30, 133);
      s += '<circle cx="' + f(q[0]) + '" cy="' + f(q[1]) + '" r="12.5" fill="#fff" stroke="#2f63ad" stroke-width="2"/>' +
        T + 'x="' + f(q[0]) + '" y="' + f(q[1] + 4.6) + '" font-size="13" fill="#2f63ad">' + (n < 2 ? "0" : "") + n * 5 + '</text>'; }
    var hh = P((h % 12) * 30 + m * 0.5, 58), mm = P(m * 6, 98);
    s += '<line x1="150" y1="150" x2="' + f(mm[0]) + '" y2="' + f(mm[1]) + '" stroke="#2f63ad" stroke-width="5" stroke-linecap="round"/>' +
      '<line x1="150" y1="150" x2="' + f(hh[0]) + '" y2="' + f(hh[1]) + '" stroke="#c8323b" stroke-width="10" stroke-linecap="round"/><circle cx="150" cy="150" r="8" fill="#3B2410"/>';
    for (var k = 1; k <= 12; k++) { var g = P(k * 30, 83), r = P(k * 30, 45);
      s += T + 'x="' + f(g[0]) + '" y="' + f(g[1] + 9) + '" font-size="26" fill="#3B2410" stroke="#fff" stroke-width="4" paint-order="stroke">' + k + '</text>' +
        T + 'x="' + f(r[0]) + '" y="' + f(r[1] + 5.3) + '" font-size="15" fill="#c8323b" stroke="#eeeeee" stroke-width="4" paint-order="stroke">' + (k + 12) + '</text>'; }
    return s + '</svg>';
  }
  function digitale(h, m) { return (h < 10 ? "0" : "") + h + ":" + (m < 10 ? "0" : "") + m; }
  function voce(t) {
    if (!window.speechSynthesis) return;
    var u = new SpeechSynthesisUtterance(String(t).toLowerCase()); u.lang = "it-IT"; u.rate = .85;
    speechSynthesis.cancel(); speechSynthesis.speak(u);
  }
  window.OROLOGIO = { svg: svg, svg24: svg24, parole: parole, digitale: digitale, voce: voce };
})();
