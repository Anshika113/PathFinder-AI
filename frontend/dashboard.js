let careerChart, growthChart, marketChart

/* ================= ANALYZE ================= */
async function analyze(){
try{

let skills=document.getElementById("skills").value
.split(",").map(s=>s.trim().toLowerCase())

let experience=parseInt(document.getElementById("experience").value || 1)

let res=await fetch("http://127.0.0.1:5000/api/analyze",{
method:"POST",
headers:{"Content-Type":"application/json"},
body:JSON.stringify({skills,experience})
})

let data=await res.json()

renderAll(data)

}catch(err){
console.error(err)
alert("Analyze failed")
}
}

/* ================= RENDER ================= */
function renderAll(data){

if(!data) return

/* ===== Career ===== */
if(careerChart) careerChart.destroy()

careerChart=new Chart(document.getElementById("careerChart"),{
type:"bar",
data:{
labels:data.career_match.map(c=>c.career),
datasets:[{
label:"Match %",
data:data.career_match.map(c=>c.match_score)
}]
}
})

/* ===== Growth ===== */
if(growthChart) growthChart.destroy()

growthChart=new Chart(document.getElementById("growthChart"),{
type:"line",
data:{
labels:data.career_growth.map(g=>g.year),
datasets:[{
label:"Salary",
data:data.career_growth.map(g=>g.salary)
}]
}
})

/* ===== Market ===== */
if(marketChart) marketChart.destroy()

marketChart=new Chart(document.getElementById("marketChart"),{
type:"pie",
data:{
labels:Object.keys(data.job_market_skill_demand || {}),
datasets:[{
data:Object.values(data.job_market_skill_demand || {})
}]
}
})

/* ===== LISTS ===== */
fill("gap",data.skill_gap)
fill("projects",data.projects)
fill("certs",data.certifications)
fill("resources",data.learning_resources)
fill("study",data.study_plan)

/* ===== JOBS ===== */
let jobs=document.getElementById("jobs")
jobs.innerHTML=""

if(data.jobs){
data.jobs.forEach(j=>{
let li=document.createElement("li")

li.innerHTML = `
<b>${j.job_title}</b><br>
📍 ${j.location}<br>
💰 ${j.salary}<br>
🧑‍💻 ${j.experience}<br>
🏢 ${j.work_mode}
`

jobs.appendChild(li)
})
}

}

/* ================= COMMON LIST ================= */
function fill(id,arr){

let el=document.getElementById(id)
el.innerHTML=""

if(!arr) return

arr.forEach(i=>{
let li=document.createElement("li")
li.textContent=i
el.appendChild(li)
})

}

/* ================= RESUME ================= */
async function uploadResume(){

try{

let file=document.getElementById("resumeFile").files[0]
if(!file) return alert("Upload file")

let form=new FormData()
form.append("resume",file)

let res=await fetch("http://127.0.0.1:5000/api/resume",{
method:"POST",
body:form
})

let data=await res.json()

/* FIXED ACCESS */
let ats = data?.resume_analysis?.summary?.ats_score || "N/A"
let strength = data?.resume_analysis?.summary?.resume_strength || "N/A"

document.getElementById("resumeResult").innerHTML =
`<b>ATS:</b> ${ats}<br><b>Strength:</b> ${strength}`

/* IMPORTANT: FULL ANALYSIS RENDER */
renderAll(data)

}catch(err){
console.error(err)
alert("Resume error")
}
}

/* ================= GITHUB ================= */
async function analyzeGithub(){

try{

let user=document.getElementById("githubUser").value.trim()
if(!user) return alert("Enter username")

let res=await fetch("http://127.0.0.1:5000/api/github",{
method:"POST",
headers:{"Content-Type":"application/json"},
body:JSON.stringify({username:user})
})

let data=await res.json()

if(data.error){
document.getElementById("githubResult").innerHTML=data.error
return
}

let html=`<b>Total Repos:</b> ${data.total_repos}<br><br><b>Languages:</b><ul>`

for(let lang in data.languages){
html+=`<li>${lang}: ${data.languages[lang]}</li>`
}

html+="</ul>"

document.getElementById("githubResult").innerHTML=html

}catch(err){
console.error(err)
alert("GitHub error")
}
}

/* ================= PORTFOLIO ================= */
async function analyzePortfolio(){

try{

let input=document.getElementById("portfolioInput").value
if(!input) return alert("Enter projects")

let projects=input.split(",").map(p=>p.trim())

let res=await fetch("http://127.0.0.1:5000/api/portfolio",{
method:"POST",
headers:{"Content-Type":"application/json"},
body:JSON.stringify({projects})
})

let data=await res.json()

document.getElementById("portfolioResult").innerHTML=
`<pre>${JSON.stringify(data,null,2)}</pre>`

}catch(err){
console.error(err)
alert("Portfolio error")
}
}

/* ================= MENTOR ================= */
async function askMentor(){

try{

let q=document.getElementById("mentorQuestion").value.trim()

if(!q){
alert("Please enter a question")
return
}

document.getElementById("mentorAnswer").innerText="Thinking..."

let res=await fetch("http://127.0.0.1:5000/api/mentor",{
method:"POST",
headers:{"Content-Type":"application/json"},
body: JSON.stringify({
    question:q,
    skills: document.getElementById("skills").value,
    experience: document.getElementById("experience").value
})
})

let data=await res.json()

if(data.error){
document.getElementById("mentorAnswer").innerText=data.error
return
}

document.getElementById("mentorAnswer").innerText =
data.answer || "No response"

}catch(err){
console.error(err)
alert("Mentor error")
}
}