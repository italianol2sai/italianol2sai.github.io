/* Motore degli esercizi interattivi — Italiano L2 ETNIE Bari
   Ogni pagina definisce window.DATA e poi carica questo file.
   Le risposte (campo k di ogni esercizio) sono codificate in base64 e non vengono mai mostrate. */
(() => {
const D = window.DATA;
const ST = "eser:" + D.store + ":";
const store = { get(k){ try{ return localStorage.getItem(ST+k); }catch(e){ return null; } },
                set(k,v){ try{ localStorage.setItem(ST+k,v); }catch(e){} },
                del(k){ try{ localStorage.removeItem(ST+k); }catch(e){} } };
const dec = s => JSON.parse(decodeURIComponent(escape(atob(s))));
const norm = s => String(s).toUpperCase().replace(/[’`´]/g,"'").normalize("NFD").replace(/[̀-ͯ]/g,"")
  .replace(/[.,!?;:«»"()]/g," ").replace(/\s+/g," ").trim();
const $ = id => document.getElementById(id);
function el(tag, attrs={}, text){ const e=document.createElement(tag); for(const k in attrs) e.setAttribute(k,attrs[k]); if(text!==undefined) e.textContent=text; return e; }
function html(tag, attrs, h){ const e=el(tag,attrs); e.innerHTML=h; return e; }
function saveable(e){ const v=store.get(e.id); if(v!==null) e.value=v;
  e.addEventListener("input",()=>store.set(e.id,e.value)); e.addEventListener("change",()=>store.set(e.id,e.value)); }
function textInput(id, w){ const i=el("input",{type:"text",class:w||"m",id,autocomplete:"off",autocapitalize:"off",spellcheck:"false"}); saveable(i); return i; }
function choice(id, labels){
  const wrap=el("div",{class:"opts"}); let val=store.get(id);
  const bs=labels.map(l=>{ const b=el("button",{class:"tog",type:"button","aria-pressed":String(val===l)},l);
    b.onclick=()=>{ if(wrap.dataset.locked) return; val=l; store.set(id,l); bs.forEach(x=>{x.setAttribute("aria-pressed",String(x===b)); x.classList.remove("ok","no");}); };
    wrap.append(b); return b; });
  return {node:wrap, get:()=>val||"", lock:()=>{wrap.dataset.locked=1;}, buttons:bs};
}
function grade(val, k){
  const v=norm(val); if(!v) return false;
  if(k.t==="all") return k.a.every(g => g.some(a => v.includes(norm(a))));
  return k.a.some(a => k.t==="has" ? v.includes(norm(a)) : v===norm(a));
}

const main=$("app");
if(D.upper) document.body.classList.add("upper");
main.append(html("a",{class:"back",href:"../"},"← Tutti i materiali"));
main.append(el("h1",{},D.title));
main.append(html("p",{class:"sub"}, D.sub || "Scrivi le risposte e premi «Controlla» alla fine di ogni esercizio. Vedi quante sono giuste. Le risposte restano salvate su questo telefono."));
if(D.name !== false){
  const s=el("section"); s.append(el("h2",{},"👤 Nome e cognome")); const i=el("input",{type:"text",class:"w",id:"nome",autocomplete:"name"}); saveable(i); s.append(i); main.append(s);
}

const results={}, graded=[], answers={};
const recordings={};

function addChecker(sec, ex, items, k){
  const max=items.length*(ex.pts||1);
  const btn=el("button",{class:"btn chk",type:"button"},"✅ Controlla");
  const fb=el("p",{class:"fb","aria-live":"polite"});
  sec.append(btn,fb);
  const run=(save)=>{
    let good=0; const seen=new Set();
    items.forEach((it,i)=>{ let g=grade(it.get(),k[i]);
      if(g && ex.type==="set"){ const v=norm(it.get()); if(seen.has(v)) g=false; seen.add(v); }
      if(g) good++;
      it.mark.textContent=g?"✓":"✗"; it.mark.className="mark "+(g?"ok":"no");
      (it.inputs||[]).forEach(x=>{ x.classList.toggle("ok",g); x.classList.toggle("no",!g); if(D.once) x.disabled=true; });
      if(D.once && it.lock) it.lock(); });
    const got=good*(ex.pts||1), r=got/max;
    fb.className="fb "+(r===1?"ok":r>=.6?"mid":"no");
    fb.textContent=(r===1?"👏 Perfetto! ":r>=.6?"👍 Bene! ":"📚 Riprova! ")+good+" risposte giuste su "+items.length+"."+(r<1&&!D.once?" Correggi le risposte con ✗ e premi di nuovo «Controlla».":"");
    if(D.once){ btn.disabled=true; btn.textContent="Controllato"; }
    results[ex.id]={got,max}; if(save) store.set("chk-"+ex.id,"1"); updateFinal();
  };
  btn.onclick=()=>{
    if(D.once && items.some(it=>!it.get().trim()) && !confirm("Ci sono risposte vuote. Vuoi controllare lo stesso? Dopo non puoi più cambiare.")) return;
    run(true);
  };
  items.forEach(it=>(it.inputs||[]).forEach(x=>x.addEventListener("input",()=>{ x.classList.remove("ok","no"); it.mark.textContent=""; })));
  return ()=>{ if(store.get("chk-"+ex.id)) run(false); };
}

function row(sec, q, nodes, opts={}){
  const r=el("div",{class:"row"}); if(q!==undefined && q!==null) r.append(html("span",{class:opts.full?"q full":"q"},q));
  nodes.forEach(n=>r.append(n)); const mark=el("span",{class:"mark"}); r.append(mark); sec.append(r); return mark;
}

const BUILD = {
  text(sec, ex){ return ex.items.map((it,i)=>{ const inp=textInput(ex.id+"-"+i, it.w||ex.w); if(it.ph) inp.placeholder=it.ph;
    const nodes=[]; if(it.pre) nodes.push(html("span",{},it.pre)); nodes.push(inp); if(it.post) nodes.push(html("span",{},it.post));
    const mark=row(sec, it.q, nodes, {full:!!it.pre||ex.full}); return {get:()=>inp.value, inputs:[inp], mark, label:it.q||it.pre||""}; }); },
  cloze(sec, ex){ const box=el("div",{class:"box cloze"}); sec.append(box); const items=[];
    ex.parts.forEach(p=>{ if(typeof p==="string"){ box.append(html("span",{},p)); return; }
      const n=items.length; const inp=textInput(ex.id+"-"+n, p.w||"s"); if(p.ph) inp.placeholder=p.ph; const mark=el("span",{class:"mark"});
      box.append(inp," ",mark); items.push({get:()=>inp.value, inputs:[inp], mark, label:"spazio "+(n+1)}); });
    return items; },
  choice(sec, ex){ return ex.items.map((it,i)=>{ const c=choice(ex.id+"-"+i, it.opts||ex.opts);
    const mark=row(sec, it.q, [c.node], {full:ex.full}); return {get:c.get, lock:c.lock, mark, label:it.q||""}; }); },
  select(sec, ex){ return ex.items.map((it,i)=>{ const s=el("select",{id:ex.id+"-"+i}); s.append(el("option",{value:""},"Scegli…"));
    (it.opts||ex.opts).forEach(o=>s.append(el("option",{value:o},o))); saveable(s);
    const mark=row(sec, it.q, [s]); return {get:()=>s.value, inputs:[s], mark, label:it.q}; }); },
  multi(sec, ex){ return ex.items.map((it,i)=>{ const cb=el("input",{type:"checkbox",id:ex.id+"-"+i}); cb.checked=store.get(cb.id)==="1";
    cb.addEventListener("change",()=>store.set(cb.id,cb.checked?"1":"0"));
    const lab=el("label",{for:cb.id,class:"q"},it); const r=el("div",{class:"row"}); const mark=el("span",{class:"mark"}); r.append(cb,lab,mark); sec.append(r);
    return {get:()=>cb.checked?"X":"-", inputs:[cb], mark, label:it, lock:()=>{cb.disabled=true;}}; }); },
  order(sec, ex){ const n=ex.items.length; return ex.items.map((it,i)=>{ const s=el("select",{id:ex.id+"-"+i,class:"num"}); s.append(el("option",{value:""},"—"));
    for(let j=1;j<=n;j++) s.append(el("option",{value:String(j)},String(j))); saveable(s);
    const r=el("div",{class:"row"}); const mark=el("span",{class:"mark"}); r.append(s, html("span",{class:"q"},it), mark); sec.append(r);
    return {get:()=>s.value, inputs:[s], mark, label:it}; }); },
  set(sec, ex){ const items=[]; for(let i=0;i<ex.n;i++){ const inp=textInput(ex.id+"-"+i, "m"); const mark=row(sec, (i+1)+".", [inp]);
      items.push({get:()=>inp.value, inputs:[inp], mark, label:"parola "+(i+1)}); } return items; },
  free(sec, ex){ ex.items.forEach((q,i)=>{ if(q) sec.append(html("p",{class:"cons"},q)); const t=el("textarea",{id:ex.id+"-"+i}); if(ex.rows) t.style.minHeight=(ex.rows*1.6)+"em"; saveable(t); sec.append(t); });
    answers[ex.id]=()=>ex.items.map((q,i)=>(ex.items.length>1?(i+1)+". ":"")+($(ex.id+"-"+i).value||"-")); return null; },
  survey(sec, ex){ const cs=ex.items.map((q,i)=>{ const c=choice(ex.id+"-"+i, ex.opts); row(sec,q,[c.node],{full:true}); return c; });
    answers[ex.id]=()=>ex.items.map((q,i)=>q+": "+(cs[i].get()||"-")); return null; },
  record(sec, ex){ recorder(sec, ex); return null; },
  info(sec, ex){ return null; }
};

function recorder(sec, ex){
  const can = navigator.mediaDevices && navigator.mediaDevices.getUserMedia && window.MediaRecorder;
  const note=el("p",{class:"note"});
  ex.items.forEach((t,i)=>{
    const key=ex.id+"-"+i;
    const box=el("div",{class:"sit"}); box.append(html("div",{},t));
    const bar=el("div",{class:"rec"}); const rb=el("button",{class:"btn",type:"button"},"⏺️ Registra");
    const timer=el("span",{class:"recdot"}); const audio=el("audio",{controls:""}); audio.hidden=true;
    const dl=el("a",{class:"btn sec"},"⬇️ Scarica"); dl.hidden=true;
    bar.append(rb,timer,dl); box.append(bar,audio); sec.append(box);
    if(!can){ rb.disabled=true; note.textContent="Questo browser non può registrare. Prova con Chrome o Safari aggiornati."; return; }
    let mr=null, chunks=[], t0=0, iv=null;
    rb.onclick=async()=>{
      if(mr && mr.state==="recording"){ mr.stop(); return; }
      try{
        const stream=await navigator.mediaDevices.getUserMedia({audio:true});
        mr=new MediaRecorder(stream); chunks=[];
        mr.ondataavailable=e=>chunks.push(e.data);
        mr.onstop=()=>{ stream.getTracks().forEach(x=>x.stop()); clearInterval(iv); timer.textContent="";
          const type=mr.mimeType||"audio/webm"; const blob=new Blob(chunks,{type});
          const ext=type.includes("mp4")?"m4a":type.includes("ogg")?"ogg":"webm";
          const who=(norm(($("nome")||{}).value||"")||"studente").replace(/\s+/g,"-").toLowerCase();
          const name=who+"-"+D.store+"-"+key+"."+ext;
          recordings[key]=new File([blob],name,{type});
          audio.src=URL.createObjectURL(blob); audio.hidden=false;
          dl.href=audio.src; dl.download=name; dl.hidden=false; rb.textContent="🔁 Registra di nuovo"; };
        mr.start(); t0=Date.now(); rb.textContent="⏹️ Stop";
        iv=setInterval(()=>{ const s=Math.floor((Date.now()-t0)/1000); timer.textContent="● "+Math.floor(s/60)+":"+String(s%60).padStart(2,"0"); },500);
      }catch(e){ note.textContent="Non riesco a usare il microfono. Controlla di aver dato il permesso al browser."; }
    };
  });
  sec.append(note);
}

const restore=[];
D.sections.forEach(ex=>{
  if(ex.part){ main.append(el("div",{class:"part"},ex.part)); return; }
  const sec=el("section",{id:"ex-"+ex.id});
  const h=el("h2"); h.append(ex.title||""); if(ex.badge) h.append(" ",el("span",{class:"pts"},ex.badge)); sec.append(h);
  if(ex.cons) sec.append(html("p",{class:"cons"},ex.cons));
  if(ex.info) sec.append(html("div",{class:"box"},ex.info));
  if(ex.img) sec.append(el("img",{src:ex.img,alt:ex.alt||"",class:"img"}));
  if(ex.bank) sec.append(html("p",{class:"bank"},"Parole: "+ex.bank));
  const items=BUILD[ex.type](sec, ex);
  if(items){ const k=dec(ex.k); graded.push(ex); answers[ex.id]=()=>items.map((it,i)=>(i+1)+". "+(it.get()||"-")); restore.push(addChecker(sec, ex, items, k)); }
  main.append(sec);
});

// risultato finale
const fin=el("section",{id:"final"}); fin.append(el("h2",{},"📊 Il tuo risultato"));
const hint=el("p",{class:"cons"}); const box=el("div"); fin.append(hint, box);
const send=el("button",{class:"btn",type:"button",style:"margin-top:12px"},"📤 Invia le risposte all'insegnante");
const sendfb=el("p",{class:"fb"}); fin.append(send, sendfb);
if(!D.once){ const reset=el("button",{class:"btn sec",type:"button",style:"margin:12px 0 0 8px"},"🗑️ Ricomincia da capo");
  reset.onclick=()=>{ if(!confirm("Vuoi cancellare tutte le risposte?")) return;
    try{ Object.keys(localStorage).filter(k=>k.startsWith(ST)).forEach(k=>localStorage.removeItem(k)); }catch(e){} location.reload(); };
  fin.append(reset); }
main.append(fin);

function updateFinal(){
  const done=graded.filter(ex=>results[ex.id]);
  const got=done.reduce((s,ex)=>s+results[ex.id].got,0);
  const max=graded.reduce((s,ex)=>s+dec(ex.k).length*(ex.pts||1),0);
  box.innerHTML="";
  if(done.length<graded.length){ hint.textContent="Hai controllato "+done.length+" esercizi su "+graded.length+". Quando li controlli tutti vedi il risultato finale."; }
  else { const pc=Math.round(got/max*100);
    const band=pc>=90?"Ottimo 🌟":pc>=75?"Buono 👍":pc>=60?"Sufficiente ✅":"Da ripassare 📚";
    hint.textContent="Ecco il tuo risultato.";
    box.append(el("div",{class:"big"},got+" / "+max), el("p",{class:"fb "+(pc>=60?"ok":"no")},band+" · "+pc+"%")); }
  const tb=el("table"); tb.append(html("tr",{},"<th>Esercizio</th><th>Punti</th>"));
  graded.forEach(ex=>{ const tr=el("tr"); tr.append(el("td",{},ex.short||ex.title), el("td",{},results[ex.id]?results[ex.id].got+" / "+results[ex.id].max:"—")); tb.append(tr); });
  box.append(tb);
  if(D.manual) box.append(el("p",{class:"note"},D.manual));
}
restore.forEach(f=>f()); updateFinal();

send.onclick=async()=>{
  const lines=[D.title.toUpperCase()+" — "+((($("nome")||{}).value)||"(senza nome)")];
  D.sections.forEach(ex=>{ if(ex.part||!answers[ex.id]) return; const r=results[ex.id];
    lines.push("", (ex.short||ex.title)+(r?" — "+r.got+"/"+r.max:"")); answers[ex.id]().forEach(a=>lines.push("  "+a)); });
  const files=Object.values(recordings);
  if(files.length) lines.push("","REGISTRAZIONI: "+files.length);
  const text=lines.join("\n");
  try{ if(navigator.share){ const data={title:D.title,text};
      if(files.length && navigator.canShare && navigator.canShare({files})) data.files=files;
      await navigator.share(data);
      if(files.length && !data.files){ sendfb.className="fb mid"; sendfb.textContent="Testo inviato. Le registrazioni mandale con «Scarica»."; }
      return; } }
  catch(e){ if(e.name==="AbortError") return; }
  try{ await navigator.clipboard.writeText(text); sendfb.className="fb ok"; sendfb.textContent="📋 Risposte copiate: incollale in un messaggio all'insegnante."+(files.length?" Le registrazioni mandale con «Scarica».":""); }
  catch(e){ sendfb.className="fb no"; sendfb.textContent="Non riesco a copiare. Fai uno screenshot."; }
};
})();
