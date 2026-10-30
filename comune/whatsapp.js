/* Invio delle risposte all'insegnante su WhatsApp.
   NUMERO: il numero dell'insegnante con il prefisso, solo cifre (es. "393331234567").
   Se è vuoto, WhatsApp si apre e lo studente sceglie a chi mandare il messaggio. */
(function(){
const NUMERO = "";

function apri(text){
  const url = "https://wa.me/" + NUMERO + "?text=" + encodeURIComponent(text);
  const w = window.open(url, "_blank");
  if(!w) location.href = url;
}

window.WA = { numero: NUMERO, apri };
})();
