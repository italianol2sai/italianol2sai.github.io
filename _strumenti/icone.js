// Rigenera le icone del sito dal logo icone/logo-etnie.png (serve Playwright):  node _strumenti/icone.js
// Crea: favicon-32/48, icona-192/512, apple-touch-icon (con «autoapprendimento»), condividi.png. Poi favicon.ico con Python/PIL.
const {chromium}=require('playwright');const fs=require('fs');(async()=>{const b=await chromium.launch();
const logo='data:image/png;base64,'+fs.readFileSync('icone/logo-etnie.png').toString('base64');
const ROSSO='#e3161b';
async function shot(w,h,html,out,trasp){const p=await b.newPage({viewport:{width:w,height:h}});await p.setContent(`<html><body style="margin:0;font-family:Inter;background:transparent">${html}</body></html>`);await p.waitForTimeout(200);await p.screenshot({path:out,omitBackground:!!trasp});await p.close();}
// favicon piccola: logo intero su quadrato bianco arrotondato
const piccola=(s)=>`<div style="width:${s}px;height:${s}px;background:#fff;border-radius:${s*.2}px;display:flex;align-items:center;justify-content:center"><img src="${logo}" style="width:${s*.96}px"></div>`;
await shot(32,32,piccola(32),'icone/favicon-32.png',true);
await shot(64,64,piccola(64),'icone/favicon-64.png',true);
// icona grande: logo + scritta autoapprendimento
const big=(s)=>`<div style="width:${s}px;height:${s}px;background:radial-gradient(circle at 35% 35%,#fff 0,#fff 45%,#fff3e0 75%,#ffe1dc 100%);display:flex;flex-direction:column;align-items:center;justify-content:center;gap:${s*.02}px">
<img src="${logo}" style="width:${s*.82}px">
<div style="color:#fff;background:linear-gradient(90deg,#e3161b,#f26a1b 55%,#f2a516);box-shadow:0 ${s*.015}px ${s*.04}px #e3161b55;border-radius:${s}px;font-weight:800;font-size:${s*.076}px;padding:${s*.012}px ${s*.05}px ${s*.02}px">autoapprendimento</div></div>`;
await shot(180,180,big(180),'icone/apple-touch-icon.png');
await shot(192,192,big(192),'icone/icona-192.png');
await shot(512,512,big(512),'icone/icona-512.png');
// immagine di condivisione (WhatsApp ecc.)
await shot(1200,630,`<div style="width:1200px;height:630px;background:#fff;display:flex;align-items:center;gap:40px;padding:0 60px;box-sizing:border-box;position:relative;overflow:hidden">
<div style="position:absolute;right:-140px;top:-140px;width:420px;height:420px;border-radius:50%;background:#f2a51626"></div>
<div style="position:absolute;right:140px;bottom:-180px;width:360px;height:360px;border-radius:50%;background:#22a35a1c"></div>
<div style="position:absolute;left:0;bottom:0;width:100%;height:16px;background:linear-gradient(90deg,#e3161b,#f2a516,#7bc043,#1f8a4c,#2b7bd6,#a14cd8)"></div>
<img src="${logo}" style="width:470px;flex:none">
<div style="position:relative"><div style="font-size:30px;font-weight:700;color:${ROSSO};letter-spacing:.12em">ITALIANO L2 · BARI</div>
<div style="font-size:60px;font-weight:900;color:#1f2933;line-height:1;margin:12px 0 18px;letter-spacing:-.03em">autoapprendimento</div>
<div style="font-size:30px;color:#4b5563;line-height:1.3">Esercizi, giochi e video<br>da fare da soli,<br>su telefono e computer</div></div></div>`,'icone/condividi.png');
await b.close()})()
