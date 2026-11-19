/* Le lettere ponte — funzioni comuni: audio con la voce di Erila, condividi, memoria del telefono */
const $ = (id) => document.getElementById(id);
const dec = (s) => JSON.parse(decodeURIComponent(escape(atob(s))));
const mem = {
  get(k) { try { return localStorage.getItem("ponte:" + k); } catch (e) { return null; } },
  set(k, v) { try { localStorage.setItem("ponte:" + k, v); } catch (e) {} },
  del(k) { try { localStorage.removeItem("ponte:" + k); } catch (e) {} },
};
const shuffle = (a) => { a = a.slice(); for (let i = a.length - 1; i > 0; i--) { const j = Math.floor(Math.random() * (i + 1)); [a[i], a[j]] = [a[j], a[i]]; } return a; };

/* AUDIO: prima audio/<parola>, poi ../sillabe/audio e ../sillabe-difficili/audio (registrazioni di Erila), altrimenti voce del computer */
const slug = (t) => t.toLowerCase().normalize("NFD").replace(/[̀-ͯ]/g, "").replace(/[^a-z0-9]+/g, "-").replace(/^-|-$/g, "");
const found = {};
let current = null;
function tryLoad(url) {
  return new Promise((ok, ko) => { const a = new Audio(); a.preload = "auto"; a.oncanplaythrough = () => ok(); a.onerror = ko; a.src = url; });
}
async function say(text) {
  if (current) { current.pause(); current = null; }
  if (window.speechSynthesis) speechSynthesis.cancel();
  const s = slug(text);
  if (!(s in found)) {
    found[s] = null;
    for (const d of ["audio", "../sillabe/audio", "../sillabe-difficili/audio"])
      for (const ext of ["wav", "mp3", "m4a"]) {
        if (found[s]) break;
        try { await tryLoad(`${d}/${s}.${ext}`); found[s] = `${d}/${s}.${ext}`; } catch (e) {}
      }
  }
  if (found[s]) { current = new Audio(found[s]); current.play().catch(() => {}); return; }
  if (!window.speechSynthesis) return;
  // una lettera da sola: si dice il SUONO (lll, mmm), mai il nome (elle, emme)
  const SUONO = { L: "lll", M: "mmm", N: "nnn", R: "rrr" };
  let t = SUONO[text] || text.toLowerCase(); t = t.charAt(0).toUpperCase() + t.slice(1);
  const u = new SpeechSynthesisUtterance(t); u.lang = "it-IT"; u.rate = 0.75;
  const v = speechSynthesis.getVoices().find((v) => v.lang && v.lang.startsWith("it")); if (v) u.voice = v;
  speechSynthesis.speak(u);
}
if (window.speechSynthesis) speechSynthesis.getVoices();

/* illustrazione Canva (img/…) se c'è, altrimenti l'emoji */
const fig = (o) => o.im ? `<img class="pic" src="${o.im}" alt="" loading="lazy" onerror="this.outerHTML='${o.e}'">` : o.e;

/* la lettera ponte evidenziata: vocale + L/M/N/R + consonante diversa */
function ponte(w) {
  return w.replace(/([AEIOUÀÈÉÌÒÙ])([LMNR])(?=([B-DF-HJ-NP-TV-Z]))/g, (m, v, l, nx) => nx === l ? m : v + "<b>" + l + "</b>");
}

/* nome dello studente: chiesto una volta, ricordato sul telefono */
function nomeStudente() {
  let n = ""; try { n = localStorage.getItem("studente-nome") || ""; } catch (e) {}
  return n;
}
function salvaNome(n) { try { localStorage.setItem("studente-nome", n.trim().toUpperCase()); } catch (e) {} }

/* un solo pulsante: Condividi (cellulare) oppure copia + WhatsApp (computer) */
async function condividi(titolo, righe, fb) {
  let nome = nomeStudente();
  if (!nome) { nome = (prompt("COME TI CHIAMI?") || "").trim().toUpperCase(); if (nome) salvaNome(nome); }
  const text = [titolo + " — " + (nome || "(SENZA NOME)"), ""].concat(righe).join("\n");
  try { if (navigator.share) { await navigator.share({ title: titolo, text }); return; } }
  catch (e) { if (e.name === "AbortError") return; }
  try { await navigator.clipboard.writeText(text); } catch (e) {}
  if (fb) { fb.className = "fb ok"; fb.textContent = "📋 RISULTATO COPIATO. SI APRE WHATSAPP: SCEGLI L'INSEGNANTE."; }
  window.open("https://wa.me/?text=" + encodeURIComponent(text), "_blank");
}

document.addEventListener("click", (e) => {
  const b = e.target.closest("[data-say]"); if (b) say(b.dataset.say);
});
