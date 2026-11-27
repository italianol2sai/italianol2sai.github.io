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
  function digitale(h, m) { return (h < 10 ? "0" : "") + h + ":" + (m < 10 ? "0" : "") + m; }
  function voce(t) {
    if (!window.speechSynthesis) return;
    var u = new SpeechSynthesisUtterance(String(t).toLowerCase()); u.lang = "it-IT"; u.rate = .85;
    speechSynthesis.cancel(); speechSynthesis.speak(u);
  }
  window.OROLOGIO = { svg: svg, parole: parole, digitale: digitale, voce: voce };
})();
