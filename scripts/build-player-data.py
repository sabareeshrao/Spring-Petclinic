#!/usr/bin/env python3
import json
import pathlib

ROOT = pathlib.Path(".")
OUT = ROOT / "_site"
PROJECT = ROOT / "project"
CURRICULUM = ROOT / "curriculum"

def read_json(path):
    return json.loads(path.read_text(encoding="utf-8"))

def language_for(path):
    name = path.name.lower()
    ext = path.suffix.lower().lstrip(".")
    if name == "pom.xml": return "xml"
    if name in {"mvnw","gradlew"}: return "shell"
    return {
        "java":"java","xml":"xml","properties":"properties","yml":"yaml","yaml":"yaml",
        "sql":"sql","html":"html","css":"css","scss":"scss","js":"javascript","json":"json",
        "md":"markdown","gradle":"groovy","sh":"shell","bat":"batch","cmd":"batch","txt":"text",
        "gitignore":"text","gitattributes":"text","editorconfig":"text","dockerfile":"dockerfile"
    }.get(ext or name, ext or "text")

def is_text(data):
    if b"\0" in data[:4096]:
        return False
    try:
        data.decode("utf-8")
        return True
    except UnicodeDecodeError:
        return False

book = read_json(CURRICULUM / "book.json")
stages = []
for ref in book.get("chapters", []):
    if not ref.get("source"):
        continue
    stage = {
        "title": f'{ref["id"]}. {ref["title"]}',
        "subtitle": "",
        "stepLabel": "questions",
        "steps": []
    }
    chapter = read_json(CURRICULUM / ref["source"])
    stage["subtitle"] = chapter.get("title","")
    for lesson in chapter.get("lessons", []):
        for q in lesson.get("questions", []):
            action = q.get("action") or {"action":"highlightTarget","data":{"target":"project"}}
            stage["steps"].append({
                "title": f'{q.get("id","Q")} · {q.get("title", q.get("id","Question"))}',
                "why": q.get("question",""),
                "answer": str(q.get("answer","")),
                "originalActionTranscript": (
                    str(q.get("original_action", {}).get("description",""))
                    if isinstance(q.get("original_action"), dict)
                    else str(q.get("original_action_transcript",""))
                ),
                "lesson": lesson.get("title",""),
                "software": q.get("software","intellij"),
                "action": action
            })
    if stage["steps"]:
        stages.append(stage)

course = {
    "title": book.get("title","Build Spring PetClinic from Zero to Final"),
    "subtitle": "Question-driven reconstruction using the Experiment-VS-Code player contract.",
    "stepLabel": "questions",
    "books": [{
        "id":"book-1",
        "title":book.get("title","Spring PetClinic"),
        "subtitle":"Build the canonical Spring PetClinic project from zero through teaching questions.",
        "chapterStart":1,
        "chapterEnd":max(1,len(stages))
    }],
    "package": {
        "apps": {
            "intellij_idea": {
                "project":{"name":"spring-petclinic","sdk":"Java 17","languageLevel":"17"},
                "tree":[],"files":{},"problems":[],"breakpoints":[],"runConfigurations":[],
                "maven":{},"spring":{},"jpa":{},"git":{"branch":"main","changes":[],"history":[]},
                "database":{},"tests":{},"terminal":"","console":"","visibleFeatures":[]
            },
            "spring_initializer": {
                "projectType":"Maven","language":"Java","bootVersion":"3.5.6",
                "group":"com.example","artifact":"demo",
                "name":"demo","packageName":"com.example.demo",
                "description":"Demo project for Spring Boot","packaging":"Jar",
                "javaVersion":"17","configFormat":"Properties","dependencies":[]
            }
        }
    },
    "stages": stages
}
(OUT / "lessons.js").write_text("window.COURSE = "+json.dumps(course,indent=2)+";\n",encoding="utf-8")

files = {}
if PROJECT.exists():
    for p in sorted(x for x in PROJECT.rglob("*") if x.is_file()):
        rel = p.relative_to(PROJECT).as_posix()
        data = p.read_bytes()
        if is_text(data):
            content = data.decode("utf-8")
            lang = language_for(p)
        else:
            content = "// Binary project asset: "+rel+"\n"
            lang = "binary"
        files[rel] = {"language":lang,"content":content}

parts=[{} for _ in range(8)]
for i,(path,meta) in enumerate(files.items()):
    parts[i % 8][path]=meta
pdata=OUT/"project-data"
pdata.mkdir(parents=True,exist_ok=True)
for i,part in enumerate(parts,1):
    (pdata/f"part-{i:02d}.js").write_text(
        "window.FULL_PROJECT_PARTS=window.FULL_PROJECT_PARTS||[];window.FULL_PROJECT_PARTS.push("+
        json.dumps(part,separators=(",",":"))+");\n",encoding="utf-8")

def node_for(path):
    rel=path.relative_to(PROJECT).as_posix()
    if path.is_dir():
        return {"name":path.name,"path":rel,"type":"folder","open":path.parent==PROJECT,
                "children":[node_for(x) for x in sorted(path.iterdir(),key=lambda z:(not z.is_dir(),z.name.lower()))]}
    return {"name":path.name,"path":rel,"type":"file","language":language_for(path)}

tree=[]
if PROJECT.exists():
    tree=[node_for(x) for x in sorted(PROJECT.iterdir(),key=lambda z:(not z.is_dir(),z.name.lower()))]
initial="src/main/java/org/springframework/samples/petclinic/PetClinicApplication.java"
meta={
    "project":{"name":"spring-petclinic","sdk":"Java 17","languageLevel":"17"},
    "tree":tree,"initialFile":initial if initial in files else (next(iter(files),None)),
    "problems":[],"breakpoints":[],"runConfigurations":[],"maven":{},"spring":{},"jpa":{},
    "git":{"branch":"main","changes":[],"history":[]},"database":{},"tests":{},
    "terminal":"","console":"","visibleFeatures":[]
}
(pdata/"index.js").write_text(
    "window.FULL_PROJECT_META="+json.dumps(meta,separators=(",",":"))+";\n"+
    "window.buildFullProjectPackage=function(){const files=Object.assign({},...(window.FULL_PROJECT_PARTS||[]));return {apps:{intellij_idea:{...window.FULL_PROJECT_META,files}}};};\n",
    encoding="utf-8"
)
