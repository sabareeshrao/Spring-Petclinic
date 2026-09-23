const state={book:null,chapter:null,questions:[],index:-1};
const simMap={intellij:"intellij",spring_initializer:"spring_initializer",git:"git",github:"github",github_actions:"github_actions",mysqlworkbench:"mysql_workbench",pgadmin:"pgadmin",redis:"redis",cmd:"cmd",linux:"linux",jenkins:"jenkins"};
const $=id=>document.getElementById(id);

async function boot(){
  const book=await fetch("curriculum/book.json").then(r=>r.json());
  state.book=book;$("bookTitle").textContent=book.title;
  renderChapters();
  const first=book.chapters.find(c=>c.source);
  if(first) await loadChapter(first);
  wireCodeViewer();
}
function renderChapters(){
  const nav=$("courseNav");nav.innerHTML="";
  state.book.chapters.forEach(ch=>{
    const wrap=document.createElement("div");wrap.className="chapter";wrap.dataset.id=ch.id;
    const b=document.createElement("button");b.textContent=`${ch.id}. ${ch.title}`;
    b.onclick=()=>ch.source&&loadChapter(ch);
    wrap.appendChild(b);nav.appendChild(wrap);
  });
}
async function loadChapter(ch){
  if(!ch.source)return;
  document.querySelectorAll(".chapter").forEach(x=>x.classList.toggle("active",x.dataset.id===ch.id));
  const data=await fetch("curriculum/"+ch.source).then(r=>r.json());
  state.chapter=data;state.questions=[];
  const holder=document.querySelector(`.chapter[data-id="${ch.id}"]`);
  holder.querySelectorAll(".lesson").forEach(x=>x.remove());
  data.lessons.forEach(lesson=>{
    const l=document.createElement("div");l.className="lesson";
    const t=document.createElement("div");t.className="lessonTitle";t.textContent=lesson.title;l.appendChild(t);
    lesson.questions.forEach(q=>{
      const i=state.questions.length;state.questions.push({...q,lessonTitle:lesson.title});
      const qb=document.createElement("button");qb.className="questionLink";qb.textContent=`${q.id} · ${q.question.slice(0,52)}…`;
      qb.onclick=()=>selectQuestion(i);l.appendChild(qb);
    });holder.appendChild(l);
  });
  if(state.questions.length)selectQuestion(0);
}
function selectQuestion(i){
  state.index=i;const q=state.questions[i];if(!q)return;
  document.querySelectorAll(".questionLink").forEach((x,n)=>x.classList.toggle("active",n===i));
  $("questionId").textContent=q.id;$("questionText").textContent=q.question;$("answerText").textContent=q.answer;
  $("answerBox").hidden=true;
  $("crumb").textContent=`${state.book.title} → ${state.chapter.title} → ${q.lessonTitle} → ${q.id}`;
  const sim=simMap[q.software]||"intellij";$("softwareLabel").textContent="Software: "+q.software;
  const wanted=`software/simulator/${sim}/index.html`;
  if(!$("simFrame").src.endsWith(wanted))$("simFrame").src=wanted;
}
$("showAnswerBtn").onclick=()=>{$("answerBox").hidden=!$("answerBox").hidden};
$("prevBtn").onclick=()=>{if(state.index>0)selectQuestion(state.index-1)};
$("nextBtn").onclick=()=>{if(state.index+1<state.questions.length)selectQuestion(state.index+1)};

function wireCodeViewer(){
  const dlg=$("codeDialog");$("fullCodeBtn").onclick=()=>dlg.showModal();$("closeCodeBtn").onclick=()=>dlg.close();
  fetch("project-files.json").then(r=>r.json()).then(files=>{
    const list=$("fileList");list.innerHTML="";
    files.forEach(path=>{
      const b=document.createElement("button");b.className="fileBtn";b.textContent=path;
      b.onclick=async()=>{const r=await fetch("project/"+path);if(!r.ok){$("codeView").textContent="Unable to display this file.";return}
        const ct=r.headers.get("content-type")||"";if(/image|font|octet-stream/.test(ct)){$("codeView").textContent="Binary asset: "+path;return}
        $("codeView").textContent=await r.text();
      };list.appendChild(b);
    });
  }).catch(()=>{});
}
boot();
