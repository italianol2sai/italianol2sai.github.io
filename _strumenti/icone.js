// Rigenera le icone del sito da icone/favicon.svg (serve Playwright):  node _strumenti/icone.js
const {chromium}=require('playwright');const fs=require('fs');(async()=>{const b=await chromium.launch();
const svg=fs.readFileSync('icone/favicon.svg','utf8').replace('<svg ','<svg width="100%" height="100%" ');
const bubble=svg.replace(/<rect[^>]*\/>/,'');
async function shot(w,h,html,out){const p=await b.newPage({viewport:{width:w,height:h}});await p.setContent(`<html><body style="margin:0;font-family:Inter">${html}</body></html>`);await p.waitForTimeout(200);await p.screenshot({path:out});await p.close();}
// icona grande (quadrata piena, l'OS arrotonda)
const big=(s)=>`<div style="width:${s}px;height:${s}px;background:linear-gradient(135deg,#22a35a,#0f6b4a);display:flex;flex-direction:column;align-items:center;justify-content:center">
<div style="width:${s*.78}px;height:${s*.66}px;margin-top:${s*.02}px">${bubble}</div>
<div style="color:#fff;font-weight:800;font-size:${s*.093}px;letter-spacing:-.01em;margin-top:-${s*.03}px">autoapprendimento</div></div>`;
await shot(180,180,big(180),'icone/apple-touch-icon.png');
await shot(512,512,big(512),'icone/icona-512.png');
await shot(192,192,big(192),'icone/icona-192.png');
// immagine di condivisione
await shot(1200,630,`<div style="width:1200px;height:630px;background:#fbf7f0;display:flex;align-items:center;gap:50px;padding:0 70px;box-sizing:border-box;position:relative;overflow:hidden">
<div style="position:absolute;right:-120px;top:-120px;width:420px;height:420px;border-radius:50%;background:#f2a51633"></div>
<div style="position:absolute;right:120px;bottom:-160px;width:360px;height:360px;border-radius:50%;background:#e04a3f22"></div>
<div style="position:absolute;left:0;bottom:0;width:100%;height:18px;background:linear-gradient(90deg,#22a35a 0 33%,#fff 33% 66%,#e04a3f 66%)"></div>
<div style="width:280px;height:280px;flex:none;filter:drop-shadow(0 18px 30px #0f6b4a44)">${svg}</div>
<div style="position:relative"><div style="font-size:34px;font-weight:700;color:#0f6b4a;letter-spacing:.12em">ITALIANO L2 · BARI</div>
<div style="font-size:68px;font-weight:900;color:#1f2933;line-height:1;margin:10px 0 18px;letter-spacing:-.03em">autoapprendimento</div>
<div style="font-size:34px;color:#4b5563">Esercizi, giochi e video<br>da fare da soli, su telefono e computer</div></div></div>`,'icone/condividi.png');
await b.close()})()
