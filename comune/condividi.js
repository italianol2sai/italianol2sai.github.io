/* Invio dei risultati all'insegnante (esercizi, giochi, escape room).
   Due pulsanti uguali dappertutto:
   - «📤 Invia all'insegnante»: menu Condividi del telefono; se non c'è o non funziona, apre WhatsApp.
   - «💬 Invia con WhatsApp»: apre WhatsApp con il messaggio già scritto (funziona anche dove il menu
     Condividi copia solo il testo, per esempio su alcuni Samsung). Niente numero: lo studente sceglie la chat.
   API: condividi(titolo, righe, fb) · whatsapp(titolo, righe, fb) · bottoniInvio(titolo, righeFn, opz) → elemento
        compilaNome(input) · testoInvio(titolo, righe) */
(function(){
const KEY = "studente-nome";

function leggiNome(){ try{ return localStorage.getItem(KEY) || ""; }catch(e){ return ""; } }
function nome(){
  const campo = document.getElementById("nome");
  let n = campo && campo.value.trim() ? campo.value.trim() : leggiNome();
  if(!n){
    n = (prompt("COME TI CHIAMI?") || "").trim();
    if(campo && n){ campo.value = n; campo.dispatchEvent(new Event("input", { bubbles: true })); }
  }
  if(n) try{ localStorage.setItem(KEY, n); }catch(e){}
  return n || "(senza nome)";
}
function testoInvio(titolo, righe){
  if(typeof righe === "string") return righe;
  return [String(titolo).toUpperCase() + " — " + nome(), ""].concat(righe || []).join("\n");
}
function msg(fb, cls, t){ if(fb){ fb.className = "fb " + cls; fb.textContent = t; } }

function apriWhatsApp(text){
  const enc = encodeURIComponent(text.length > 3500 ? text.slice(0, 3500) + "\n…" : text);
  const ua = navigator.userAgent || "";
  const tel = /Android|iPhone|iPad|iPod/i.test(ua);
  const url = (tel ? "whatsapp://send?text=" : "https://wa.me/?text=") + enc;
  if(tel){
    // su Android/iPhone apre direttamente l'app; se non c'è, dopo un attimo prova il sito
    const t = setTimeout(() => { if(!document.hidden) location.href = "https://wa.me/?text=" + enc; }, 1500);
    document.addEventListener("visibilitychange", () => { if(document.hidden) clearTimeout(t); }, { once: true });
    location.href = url;
  } else if(!window.open(url, "_blank")) location.href = url;
}

async function copia(text){ try{ await navigator.clipboard.writeText(text); return true; }catch(e){ return false; } }

async function whatsapp(titolo, righe, fb){
  const text = testoInvio(titolo, righe);
  const c = await copia(text);
  msg(fb, "ok", "💬 Si apre WhatsApp con le tue risposte: scegli l'insegnante e premi Invia." + (c ? " (Sono anche copiate.)" : ""));
  apriWhatsApp(text);
}

async function condividi(titolo, righe, fb, files){
  const text = testoInvio(titolo, righe);
  if(navigator.share){
    try{
      const data = { title: String(titolo), text };
      if(files && files.length && navigator.canShare && navigator.canShare({ files })) data.files = files;
      await navigator.share(data);
      return "share";
    }catch(e){ if(e.name === "AbortError") return "abort"; }
  }
  await whatsapp(titolo, text, fb);
  return "whatsapp";
}

function bottoniInvio(titolo, righeFn, opz){
  opz = opz || {};
  const box = document.createElement("div"); box.className = "invio-box"; box.style.cssText = "display:flex;flex-wrap:wrap;gap:10px;margin-top:12px;align-items:center";
  const fb = opz.fb || document.createElement("p"); if(!opz.fb) fb.className = "fb";
  const cls = opz.classe || "btn";
  const up = opz.maiuscolo;
  const b1 = document.createElement("button"); b1.type = "button"; b1.className = cls;
  b1.textContent = up ? "📤 INVIA ALL'INSEGNANTE" : "📤 Invia all'insegnante";
  const b2 = document.createElement("button"); b2.type = "button"; b2.className = cls + " btn-wa";
  b2.textContent = up ? "💬 INVIA CON WHATSAPP" : "💬 Invia con WhatsApp";
  b2.style.cssText = "background:#25D366;border-color:#1ea952;color:#fff";
  b1.onclick = async () => { const r = await condividi(titolo, righeFn(), fb, opz.files && opz.files()); if(r === "share" && opz.dopo) opz.dopo(); };
  b2.onclick = () => whatsapp(titolo, righeFn(), fb);
  box.append(b1, b2);
  if(!opz.fb) box.append(fb);
  return box;
}

function compilaNome(input){
  if(!input || input.value.trim()) return;
  const n = leggiNome(); if(!n) return;
  input.value = n; input.dispatchEvent(new Event("input", { bubbles: true })); input.dispatchEvent(new Event("change", { bubbles: true }));
}

Object.assign(window, { condividi, whatsapp, bottoniInvio, compilaNome, testoInvio });
})();
