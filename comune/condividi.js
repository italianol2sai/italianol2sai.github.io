/* Pulsante «Invia all'insegnante» per giochi ed escape room.
   condividi(titolo, righe, fb): chiede il nome (una volta sola, poi lo ricorda), poi apre il menu Condividi;
   se il menu non c'è (computer), copia il testo e apre WhatsApp con il messaggio pronto. */
(function(){
const KEY = "studente-nome";

function nome(){
  let n = "";
  try{ n = localStorage.getItem(KEY) || ""; }catch(e){}
  if(!n){
    n = (prompt("COME TI CHIAMI?") || "").trim();
    if(n) try{ localStorage.setItem(KEY, n); }catch(e){}
  }
  return n || "(senza nome)";
}

async function condividi(titolo, righe, fb){
  const text = [titolo.toUpperCase() + " — " + nome(), ""].concat(righe).join("\n");
  const msg = (cls, t) => { if(fb){ fb.className = "fb " + cls; fb.textContent = t; } };
  try{ if(navigator.share){ await navigator.share({ title: titolo, text }); return; } }
  catch(e){ if(e.name === "AbortError") return; }
  let copied = false; try{ await navigator.clipboard.writeText(text); copied = true; }catch(e){}
  const url = "https://wa.me/?text=" + encodeURIComponent(text); if(!window.open(url, "_blank")) location.href = url;
  msg("ok", "💬 SI APRE WHATSAPP CON IL TUO RISULTATO: SCEGLI L'INSEGNANTE E PREMI INVIA." + (copied ? " (È ANCHE COPIATO.)" : ""));
}

// pagine con il campo «Nome»: se è vuoto, chiede il nome e lo scrive nel campo
function compilaNome(input){
  if(!input || input.value.trim()) return;
  const n = nome(); if(n === "(senza nome)") return;
  input.value = n; input.dispatchEvent(new Event("input", { bubbles: true })); input.dispatchEvent(new Event("change", { bubbles: true }));
}

window.condividi = condividi;
window.compilaNome = compilaNome;
})();
