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

/* REGISTRATORE dello studente: 🎙️ registra, ▶️ riascolta. La voce resta solo su questo telefono (non si invia). */
const voci = {};           // chiave -> URL della registrazione
let rec = null;            // { key, mr, stream, btn }
function recBtns(key, label) {
  return `<span class="recbox"><button class="rec" data-rec="${key}" aria-label="REGISTRO">🎙️${label ? " " + label : ""}</button>` +
         `<button class="play" data-play="${key}" ${voci[key] ? "" : "disabled"} aria-label="RIASCOLTO">▶️${label ? " MI ASCOLTO" : ""}</button></span>`;
}
async function registra(key, btn) {
  if (rec) { const same = rec.key === key; rec.mr.stop(); if (same) return; }
  if (!(navigator.mediaDevices && navigator.mediaDevices.getUserMedia && window.MediaRecorder)) {
    alert("QUESTO BROWSER NON PUÒ REGISTRARE. PROVA CON CHROME O SAFARI."); return; }
  let stream;
  try { stream = await navigator.mediaDevices.getUserMedia({ audio: true }); }
  catch (e) { alert("NON POSSO USARE IL MICROFONO. DAI IL PERMESSO AL BROWSER."); return; }
  if (current) current.pause(); if (window.speechSynthesis) speechSynthesis.cancel();
  const mr = new MediaRecorder(stream), chunks = [];
  mr.ondataavailable = (e) => chunks.push(e.data);
  mr.onstop = () => {
    stream.getTracks().forEach((t) => t.stop());
    btn.classList.remove("on"); btn.innerHTML = btn.innerHTML.replace("⏹️", "🎙️");
    if (voci[key]) URL.revokeObjectURL(voci[key]);
    voci[key] = URL.createObjectURL(new Blob(chunks, { type: mr.mimeType || "audio/webm" }));
    document.querySelectorAll(`[data-play="${key}"]`).forEach((p) => { p.disabled = false; p.classList.add("pop"); });
    rec = null;
  };
  rec = { key, mr, stream, btn };
  btn.classList.add("on"); btn.innerHTML = btn.innerHTML.replace("🎙️", "⏹️");
  mr.start();
}
function riascolta(key) {
  if (!voci[key]) return;
  if (current) current.pause(); if (window.speechSynthesis) speechSynthesis.cancel();
  current = new Audio(voci[key]); current.play().catch(() => {});
}

document.addEventListener("click", (e) => {
  const b = e.target.closest("[data-say]"); if (b) say(b.dataset.say);
  const r = e.target.closest("[data-rec]"); if (r) registra(r.dataset.rec, r);
  const p = e.target.closest("[data-play]"); if (p) riascolta(p.dataset.play);
});
