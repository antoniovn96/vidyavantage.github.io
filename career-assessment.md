---
layout: default
title: "Premium Career Assessment 🚀"
permalink: /assessment/
description: "A clinical-grade psychometric evaluation mapping your RIASEC interests, resilience, and aptitude."
---

<script src="https://cdnjs.cloudflare.com/ajax/libs/html2pdf.js/0.10.1/html2pdf.bundle.min.js"></script>
<script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
<script src="https://cdn.jsdelivr.net/npm/canvas-confetti@1.6.0/dist/confetti.browser.min.js"></script>

<style>
  /* --- GAMIFIED CLINICAL UI THEME --- */
  :root {
    --bg: #0f172a; --card-bg: #1e293b;
    --primary: #8b5cf6; --secondary: #06b6d4; --accent: #f43f5e;
    --text-main: #f8fafc; --text-muted: #94a3b8; --border: #334155;
    --success: #10b981; --warning: #f59e0b; --danger: #ef4444;
  }

  body { background-color: var(--bg); font-family: 'Nunito', 'Segoe UI', sans-serif; color: var(--text-main); margin: 0; }
  
  .assessment-header {
    background: linear-gradient(135deg, #1e1b4b 0%, #0f172a 100%); padding: 50px 20px 30px; text-align: center; 
    border-bottom: 2px solid var(--border); margin-bottom: 30px;
  }
  .assessment-header h1 { margin: 0 0 10px 0; font-size: 2.5rem; font-weight: 900; background: -webkit-linear-gradient(45deg, var(--secondary), var(--primary)); -webkit-background-clip: text; -webkit-text-fill-color: transparent; }
  .assessment-header p { font-size: 1.1rem; color: var(--text-muted); }

  .container { max-width: 900px; margin: 0 auto; padding: 0 20px; }

  /* PROGRESS BAR */
  .progress-container { width: 100%; background: #0f172a; border-radius: 50px; height: 12px; margin-bottom: 30px; border: 2px solid var(--border); }
  .progress-bar { height: 100%; background: linear-gradient(90deg, var(--primary), var(--secondary)); width: 10%; transition: width 0.4s ease; border-radius: 50px; }

  /* WIZARD CARDS */
  .step-card {
    background: var(--card-bg); padding: 35px; border-radius: 20px; border: 1px solid rgba(255,255,255,0.05);
    box-shadow: 0 15px 30px rgba(0,0,0,0.3); margin-bottom: 30px; display: none; animation: slideUp 0.4s ease;
  }
  .step-card.active { display: block; }
  .step-title { font-size: 1.6rem; font-weight: 800; color: white; margin-bottom: 5px; text-align: center; }
  .step-sub { text-align: center; color: var(--secondary); margin-bottom: 25px; font-weight: bold; text-transform: uppercase; letter-spacing: 1px; font-size: 0.9rem;}

  /* UI COMPONENTS */
  .form-input { width: 100%; padding: 15px; border: 2px solid var(--border); border-radius: 12px; font-size: 1.1rem; color: white; background: #0f172a; margin-bottom: 20px; box-sizing: border-box;}
  .form-input:focus { border-color: var(--primary); outline: none; }

  /* RATING SCALES */
  .scale-legend { display: flex; justify-content: space-between; color: var(--text-muted); font-size: 0.8rem; font-weight: bold; margin-bottom: 15px; text-transform: uppercase; }
  .rating-grid { display: grid; gap: 10px; margin-bottom: 25px; }
  .rating-row { display: flex; align-items: center; justify-content: space-between; background: #0f172a; padding: 12px 15px; border-radius: 12px; border: 1px solid var(--border); transition: 0.2s; }
  .rating-row:hover { border-color: var(--primary); }
  @media (max-width: 768px) { .rating-row { flex-direction: column; align-items: flex-start; gap: 10px; } }
  
  .rating-label { font-weight: 600; font-size: 1rem; flex: 1; padding-right: 15px;}
  .rating-options { display: flex; gap: 6px; background: #1e293b; padding: 4px; border-radius: 50px; }
  .rate-btn {
    width: 35px; height: 35px; border-radius: 50%; border: none; background: transparent; 
    font-size: 1.1rem; cursor: pointer; display: flex; align-items: center; justify-content: center; transition: 0.2s;
    filter: grayscale(100%) opacity(0.4);
  }
  .rate-btn:hover { filter: grayscale(0%) opacity(1); transform: scale(1.2); }
  .rate-btn.selected { filter: grayscale(0%) opacity(1); transform: scale(1.2); background: rgba(255,255,255,0.1); }

  /* RANKING UI (VALUES) */
  .values-container { display: flex; gap: 20px; }
  @media (max-width: 768px) { .values-container { flex-direction: column; } }
  .value-pool, .value-ranked { flex: 1; background: #0f172a; padding: 20px; border-radius: 12px; border: 1px solid var(--border); min-height: 250px;}
  .value-pool h3, .value-ranked h3 { color: var(--text-muted); font-size: 1rem; margin-top: 0; text-align: center; }
  .val-pill { background: var(--card-bg); border: 1px solid var(--border); padding: 10px 15px; border-radius: 8px; margin-bottom: 8px; cursor: pointer; font-weight: bold; transition: 0.2s; text-align: center; }
  .val-pill:hover { border-color: var(--primary); color: var(--primary); }
  .ranked-slot { display: flex; align-items: center; gap: 10px; margin-bottom: 8px; }
  .rank-num { background: var(--secondary); color: white; width: 30px; height: 30px; display: flex; align-items: center; justify-content: center; border-radius: 50%; font-weight: bold; flex-shrink: 0;}
  
  /* BUTTONS */
  .btn-wrapper { display: flex; justify-content: space-between; margin-top: 25px; border-top: 1px solid var(--border); padding-top: 20px; }
  .btn-main { background: linear-gradient(45deg, var(--primary), #a855f7); color: white; border: none; padding: 12px 30px; font-size: 1.1rem; font-weight: 900; border-radius: 50px; cursor: pointer; transition: 0.3s; }
  .btn-main:hover { transform: translateY(-2px); box-shadow: 0 10px 20px rgba(139, 92, 246, 0.3); }
  .btn-back { background: transparent; border: 2px solid var(--border); color: var(--text-muted); }

  /* --- CLINICAL REPORT STYLES (Light for PDF) --- */
  #reportContainer { display: none; }
  .report-card { background: white; padding: 40px; border-radius: 16px; color: #0f172a; }
  .r-header { text-align: center; border-bottom: 2px solid #e2e8f0; padding-bottom: 20px; margin-bottom: 30px; }
  .r-header h2 { font-size: 2.2rem; font-weight: 900; margin: 0; color: #0f172a; }
  .reliability-badge { display: inline-block; padding: 5px 15px; border-radius: 50px; font-size: 0.85rem; font-weight: bold; margin-top: 10px; }
  
  .grid-2 { display: grid; grid-template-columns: 1fr 1fr; gap: 20px; margin-bottom: 30px; }
  @media (max-width: 768px) { .grid-2 { grid-template-columns: 1fr; } }
  
  .chart-box { max-width: 400px; margin: 0 auto; }
  .metrics-box { padding: 20px; background: #f8fafc; border-radius: 12px; border: 1px solid #e2e8f0; }
  
  .metric { margin-bottom: 12px; }
  .m-head { display: flex; justify-content: space-between; font-size: 0.9rem; font-weight: bold; color: #475569; margin-bottom: 4px; }
  .m-track { width: 100%; height: 8px; background: #e2e8f0; border-radius: 10px; overflow: hidden; }
  .m-fill { height: 100%; border-radius: 10px; }

  .r-section { background: #f8fafc; border-radius: 12px; padding: 25px; margin-bottom: 25px; border-left: 5px solid var(--secondary); }
  .r-section h3 { margin-top: 0; font-size: 1.3rem; color: #0f172a; border-bottom: 1px solid #e2e8f0; padding-bottom: 10px; }
  .r-section p { line-height: 1.7; font-size: 1.05rem; color: #334155; }
  
  .flag-box { background: #fff1f2; border-left-color: var(--accent); }
  .flag-box h3 { color: #e11d48; }
  .flag-item { display: flex; gap: 10px; margin-bottom: 10px; font-weight: bold; color: #9f1239; }

  @keyframes slideUp { from { opacity: 0; transform: translateY(15px); } to { opacity: 1; transform: translateY(0); } }

  @media print {
    body { background: white; }
    .assessment-header, .progress-container, .btn-wrapper { display: none !important; }
    .report-card { padding: 0; box-shadow: none; }
    .r-section { page-break-inside: avoid; border: 1px solid #e2e8f0; }
  }
</style>

<div class="assessment-header">
  <h1>Premium Clinical Assessment</h1>
  <p>75-Point Psychometric Evaluation • RIASEC • Aptitude • Resilience</p>
</div>

<div class="container">
  <div class="progress-container"><div class="progress-bar" id="progressBar"></div></div>

  <div id="wizardContainer">
    </div>

  <div id="reportContainer">
    <div class="report-card" id="reportContent">
      <div class="r-header">
        <h2>Psychometric Career Dossier</h2>
        <div style="color:#64748b; font-size: 1.1rem; font-weight:600;">
          Candidate: <strong id="outName" style="color:#0f172a;"></strong> | Date: <span id="outDate"></span>
        </div>
        <div class="reliability-badge" id="outReliability"></div>
      </div>

      <div class="grid-2">
        <div class="chart-box"><canvas id="riasecChart"></canvas></div>
        <div class="metrics-box">
          <h3 style="margin-top:0; color:#0f172a; font-size:1.2rem;">Clinical Indices</h3>
          <div class="metric"><div class="m-head"><span>Aptitude Confidence</span><span id="txt-apt"></span></div><div class="m-track"><div class="m-fill" id="bar-apt" style="background:var(--primary);"></div></div></div>
          <div class="metric"><div class="m-head"><span>Stress Resilience</span><span id="txt-res"></span></div><div class="m-track"><div class="m-fill" id="bar-res" style="background:var(--success);"></div></div></div>
          <div class="metric"><div class="m-head"><span>Decision Maturity</span><span id="txt-mat"></span></div><div class="m-track"><div class="m-fill" id="bar-mat" style="background:var(--secondary);"></div></div></div>
          <div class="metric" style="margin-bottom:0;"><div class="m-head"><span>Parental Influence</span><span id="txt-par"></span></div><div class="m-track"><div class="m-fill" id="bar-par" style="background:var(--warning);"></div></div></div>
        </div>
      </div>

      <div class="r-section">
        <h3>🧠 Psychological Profile Summary</h3>
        <p><strong style="font-size:1.2rem; color:var(--primary);" id="outType"></strong></p>
        <p id="outProfileText"></p>
      </div>

      <div class="r-section" style="border-left-color: var(--primary);">
        <h3>🎯 Actionable Career Matches</h3>
        <p style="font-weight:bold; color:var(--primary); font-size:1.1rem;">Strongly Aligned Pathways:</p>
        <p id="outCareers"></p>
      </div>

      <div class="r-section flag-box" id="flagsContainer">
        <h3>⚠️ Clinical Risk Flags</h3>
        <div id="outFlags"></div>
      </div>
    </div>

    <div class="btn-wrapper" style="justify-content: center; gap: 15px;">
      <button class="btn-main" onclick="downloadPDF()">📄 Export Dossier</button>
      <button class="btn-main btn-back" onclick="location.reload()">↺ Retake</button>
    </div>
  </div>
</div>

<script>
  // --- 75-QUESTION CLINICAL DATABASE ---
  const qBank = {
    // SECTION 1: INTEREST (36 Qs)
    riasec: [
      // Realistic (1-6)
      { id:'r1', text:'I enjoy building or repairing things.', cat:'R' }, { id:'r2', text:'I prefer hands-on tasks over theoretical study.', cat:'R' }, { id:'r3', text:'I like working outdoors.', cat:'R' }, { id:'r4', text:'I enjoy using tools or equipment.', cat:'R' }, { id:'r5', text:'I feel satisfied when I create something tangible.', cat:'R' }, { id:'r6', text:'I prefer practical activities over discussions.', cat:'R' },
      // Investigative (7-12)
      { id:'i1', text:'I enjoy solving complex problems.', cat:'I' }, { id:'i2', text:'I ask "why" and "how" frequently.', cat:'I' }, { id:'i3', text:'I enjoy science-based subjects.', cat:'I' }, { id:'i4', text:'I like analysing data or patterns.', cat:'I' }, { id:'i5', text:'I enjoy researching topics in depth.', cat:'I' }, { id:'i6', text:'I prefer logical reasoning over emotional decisions.', cat:'I' },
      // Artistic (13-18)
      { id:'a1', text:'I enjoy creative writing or storytelling.', cat:'A' }, { id:'a2', text:'I like drawing, designing, or visual expression.', cat:'A' }, { id:'a3', text:'I prefer flexible tasks over structured ones.', cat:'A' }, { id:'a4', text:'I enjoy music, performance, or media creation.', cat:'A' }, { id:'a5', text:'I think creatively when solving problems.', cat:'A' }, { id:'a6', text:'I dislike rigid rules.', cat:'A' },
      // Social (19-24)
      { id:'s1', text:'I enjoy helping others solve problems.', cat:'S' }, { id:'s2', text:'I feel fulfilled when supporting someone emotionally.', cat:'S' }, { id:'s3', text:'I like teaching or explaining concepts.', cat:'S' }, { id:'s4', text:'I am patient when listening to others.', cat:'S' }, { id:'s5', text:'I prefer people-oriented activities.', cat:'S' }, { id:'s6', text:'I feel motivated when my work benefits others.', cat:'S' },
      // Enterprising (25-30)
      { id:'e1', text:'I enjoy leading group projects.', cat:'E' }, { id:'e2', text:'I like persuading or influencing others.', cat:'E' }, { id:'e3', text:'I am comfortable taking initiative.', cat:'E' }, { id:'e4', text:'I enjoy competitive environments.', cat:'E' }, { id:'e5', text:'I am interested in business or entrepreneurship.', cat:'E' }, { id:'e6', text:'I like taking calculated risks.', cat:'E' },
      // Conventional (31-36)
      { id:'c1', text:'I enjoy organising information.', cat:'C' }, { id:'c2', text:'I prefer structured instructions.', cat:'C' }, { id:'c3', text:'I like working with numbers and records.', cat:'C' }, { id:'c4', text:'I prefer predictable work environments.', cat:'C' }, { id:'c5', text:'I enjoy planning and scheduling.', cat:'C' }, { id:'c6', text:'I pay attention to small details.', cat:'C' }
    ],
    // SECTION 2: APTITUDE (37-48)
    aptitude: [
      { id:'ap1', text:'I am confident in my mathematical ability.', cat:'APT' }, { id:'ap2', text:'I can understand logical problems quickly.', cat:'APT' }, { id:'ap3', text:'I communicate my thoughts clearly.', cat:'APT' }, { id:'ap4', text:'I remember information easily.', cat:'APT' }, { id:'ap5', text:'I can think in 3D or visualise objects well.', cat:'APT' }, { id:'ap6', text:'I manage time effectively.', cat:'APT' },
      { id:'ap7', text:'I stay focused for long periods.', cat:'APT' }, { id:'ap8', text:'I understand others’ emotions easily.', cat:'APT' }, { id:'ap9', text:'I am confident speaking in front of groups.', cat:'APT' }, { id:'ap10', text:'I solve problems systematically.', cat:'APT' }, { id:'ap11', text:'I learn new technical skills quickly.', cat:'APT' }, { id:'ap12', text:'I analyse mistakes and improve.', cat:'APT' }
    ],
    // SECTION 4: RESILIENCE (57-68) [Note: 2, 4, 5, 8, 12 are Reverse Scored]
    resilience: [
      { id:'rs1', text:'I handle academic pressure well.', cat:'RES', rev:false }, { id:'rs2', text:'I panic before important exams.', cat:'RES', rev:true }, { id:'rs3', text:'I continue working even after failure.', cat:'RES', rev:false }, { id:'rs4', text:'I give up easily when things are difficult.', cat:'RES', rev:true }, { id:'rs5', text:'I compare myself with others frequently.', cat:'RES', rev:true }, { id:'rs6', text:'I can manage long study hours.', cat:'RES', rev:false },
      { id:'rs7', text:'I recover quickly from disappointment.', cat:'RES', rev:false }, { id:'rs8', text:'I feel anxious about my future.', cat:'RES', rev:true }, { id:'rs9', text:'I stay calm during deadlines.', cat:'RES', rev:false }, { id:'rs10', text:'I seek help when overwhelmed.', cat:'RES', rev:false }, { id:'rs11', text:'I feel confident making decisions.', cat:'RES', rev:false }, { id:'rs12', text:'I overthink small mistakes.', cat:'RES', rev:true }
    ],
    // SECTION 5: MATURITY (69-75) [Note: 2, 3, 6, 7 are Reverse Scored]
    maturity: [
      { id:'m1', text:'I clearly understand my strengths.', cat:'MAT', rev:false }, { id:'m2', text:'I am choosing a career mainly based on marks.', cat:'MAT', rev:true }, { id:'m3', text:'My parents strongly influence my career decisions.', cat:'PAR', rev:false }, // Tracked separately for flag
      { id:'m4', text:'I have researched career pathways thoroughly.', cat:'MAT', rev:false }, { id:'m5', text:'I am open to exploring alternative options.', cat:'MAT', rev:false }, { id:'m6', text:'I feel confused about my career direction.', cat:'MAT', rev:true }, { id:'m7', text:'If marks were not important, I would choose a different career.', cat:'PAR', rev:false } // Tracked separately for flag
    ],
    // SECTION 3: VALUES (49-56)
    values: ['High income', 'Job security', 'Work-life balance', 'Prestige/status', 'Creativity', 'Helping society', 'Independence', 'Fast growth opportunities']
  };

  // --- STATE & ENGINE ---
  let state = { answers: {}, startTime: Date.now(), topValues: [], steps: [] };
  const emojis = ['😖', '😕', '😐', '🙂', '🤩'];
  let currentStep = 0;

  // --- UI GENERATOR ---
  function buildLikertGrid(qs) {
    return `<div class="scale-legend"><span>1 = Strongly Disagree</span><span>5 = Strongly Agree</span></div>
            <div class="rating-grid">` + 
      qs.map(q => `
        <div class="rating-row" id="row_${q.id}">
          <div class="rating-label">${q.text}</div>
          <div class="rating-options">
            ${[1,2,3,4,5].map(n => `<div class="rate-btn" onclick="setAns('${q.id}', ${n}, this, ${q.rev || false}, '${q.cat}')">${emojis[n-1]}</div>`).join('')}
          </div>
        </div>`).join('') + `</div>`;
  }

  function renderWizard() {
    const wiz = document.getElementById('wizardContainer');
    
    // Step 0: Info
    state.steps.push(`<div class="step-card active" id="step_0">
      <h2 class="step-title">Candidate Profile</h2><p class="step-sub">LEVEL 1 / 7</p>
      <input type="text" id="candName" class="form-input" placeholder="Your Full Name">
      <div class="btn-wrapper"><button class="btn-main" style="width:100%" onclick="goNext(0)">Start Assessment ➔</button></div>
    </div>`);

    // Step 1: RIASEC (R, I, A)
    state.steps.push(`<div class="step-card" id="step_1"><h2 class="step-title">Activity Preferences I</h2><p class="step-sub">LEVEL 2 / 7</p>
      ${buildLikertGrid(qBank.riasec.slice(0, 18))}
      <div class="btn-wrapper"><button class="btn-main btn-back" onclick="goPrev(1)">Back</button><button class="btn-main" onclick="goNext(1)">Next ➔</button></div></div>`);

    // Step 2: RIASEC (S, E, C)
    state.steps.push(`<div class="step-card" id="step_2"><h2 class="step-title">Activity Preferences II</h2><p class="step-sub">LEVEL 3 / 7</p>
      ${buildLikertGrid(qBank.riasec.slice(18, 36))}
      <div class="btn-wrapper"><button class="btn-main btn-back" onclick="goPrev(2)">Back</button><button class="btn-main" onclick="goNext(2)">Next ➔</button></div></div>`);

    // Step 3: Aptitude
    state.steps.push(`<div class="step-card" id="step_3"><h2 class="step-title">Aptitude Confidence</h2><p class="step-sub">LEVEL 4 / 7</p>
      ${buildLikertGrid(qBank.aptitude)}
      <div class="btn-wrapper"><button class="btn-main btn-back" onclick="goPrev(3)">Back</button><button class="btn-main" onclick="goNext(3)">Next ➔</button></div></div>`);

    // Step 4: Values Ranking
    let valHtml = `<div class="step-card" id="step_4"><h2 class="step-title">Career Values</h2><p class="step-sub">LEVEL 5 / 7 • Click to select your TOP 5</p>
      <div class="values-container">
        <div class="value-pool" id="vPool"><h3>Available Values</h3>${qBank.values.map(v => `<div class="val-pill" onclick="moveValue(this, '${v}')">${v}</div>`).join('')}</div>
        <div class="value-ranked" id="vRanked"><h3>Your Top 5</h3></div>
      </div>
      <div class="btn-wrapper"><button class="btn-main btn-back" onclick="goPrev(4)">Back</button><button class="btn-main" onclick="validateValues(4)">Next ➔</button></div></div>`;
    state.steps.push(valHtml);

    // Step 5: Resilience
    state.steps.push(`<div class="step-card" id="step_5"><h2 class="step-title">Emotional Resilience</h2><p class="step-sub">LEVEL 6 / 7</p>
      ${buildLikertGrid(qBank.resilience)}
      <div class="btn-wrapper"><button class="btn-main btn-back" onclick="goPrev(5)">Back</button><button class="btn-main" onclick="goNext(5)">Next ➔</button></div></div>`);

    // Step 6: Maturity & Real Check
    state.steps.push(`<div class="step-card" id="step_6"><h2 class="step-title">Decision Maturity</h2><p class="step-sub">LEVEL 7 / 7 • Final Step</p>
      ${buildLikertGrid(qBank.maturity)}
      <div class="btn-wrapper"><button class="btn-main btn-back" onclick="goPrev(6)">Back</button><button class="btn-main" style="background:var(--success);" onclick="processClinicalData()">Compile Dossier ✨</button></div></div>`);

    wiz.innerHTML = state.steps.join('');
  }
  renderWizard();

  // --- INTERACTION LOGIC ---
  function setAns(id, val, btn, isRev, cat) {
    let p = btn.parentElement;
    Array.from(p.children).forEach(c => c.classList.remove('selected'));
    btn.classList.add('selected');
    
    // Process Reverse Scoring Immediately
    let finalVal = isRev ? (6 - val) : val;
    state.answers[id] = { raw: val, calc: finalVal, cat: cat };
  }

  function moveValue(el, val) {
    const ranked = document.getElementById('vRanked');
    const pool = document.getElementById('vPool');
    
    if (el.parentElement.id === 'vPool') {
      if(state.topValues.length >= 5) return alert("You can only select 5 values.");
      state.topValues.push(val);
      el.remove();
      ranked.innerHTML += `<div class="ranked-slot" id="rank_${val.replace(/\s/g,'')}"><div class="rank-num">${state.topValues.length}</div><div class="val-pill" onclick="unmoveValue(this, '${val}')" style="margin:0; flex:1;">${val}</div></div>`;
    }
  }
  function unmoveValue(el, val) {
    const pool = document.getElementById('vPool');
    state.topValues = state.topValues.filter(v => v !== val);
    el.parentElement.remove();
    pool.innerHTML += `<div class="val-pill" onclick="moveValue(this, '${val}')">${val}</div>`;
    // Re-number remaining
    let slots = document.getElementById('vRanked').querySelectorAll('.ranked-slot');
    slots.forEach((s, i) => s.querySelector('.rank-num').innerText = i + 1);
  }

  function validateValues(s) {
    if(state.topValues.length !== 5) return alert("Please select exactly 5 career values.");
    goNext(s);
  }

  function goNext(s) {
    document.getElementById(`step_${s}`).classList.remove('active');
    document.getElementById(`step_${s+1}`).classList.add('active');
    document.getElementById('progressBar').style.width = (((s+1) / 6) * 100) + '%';
    window.scrollTo({ top: 0, behavior: 'smooth' });
  }
  function goPrev(s) {
    document.getElementById(`step_${s}`).classList.remove('active');
    document.getElementById(`step_${s-1}`).classList.add('active');
    document.getElementById('progressBar').style.width = (((s-1) / 6) * 100) + '%';
    window.scrollTo({ top: 0, behavior: 'smooth' });
  }

  // --- CLINICAL ALGORITHM ---
  function processClinicalData() {
    confetti({ particleCount: 200, spread: 90, origin: { y: 0.5 } });

    // 1. RIASEC Calculation (Normalize to 0-100)
    let riasecRaw = { R:0, I:0, A:0, S:0, E:0, C:0 };
    let metricsRaw = { APT:0, RES:0, MAT:0, PAR:0 }; // Parental influence tracked separately

    for(let key in state.answers) {
      let ans = state.answers[key];
      if(['R','I','A','S','E','C'].includes(ans.cat)) riasecRaw[ans.cat] += ans.calc;
      else if(ans.cat) metricsRaw[ans.cat] += ans.calc;
    }

    // Formula: (Raw - 6) / 24 * 100
    let R = Math.round(((riasecRaw.R || 6) - 6) / 24 * 100);
    let I = Math.round(((riasecRaw.I || 6) - 6) / 24 * 100);
    let A = Math.round(((riasecRaw.A || 6) - 6) / 24 * 100);
    let S = Math.round(((riasecRaw.S || 6) - 6) / 24 * 100);
    let E = Math.round(((riasecRaw.E || 6) - 6) / 24 * 100);
    let C = Math.round(((riasecRaw.C || 6) - 6) / 24 * 100);
    let scores = { R:R, I:I, A:A, S:S, E:E, C:C };

    // 2. Metrics Calculation
    let aptPct = Math.round(((metricsRaw.APT || 12) - 12) / 48 * 100);
    let resPct = Math.round(((metricsRaw.RES || 12) - 12) / 48 * 100);
    // Maturity has 5 questions mapped to MAT. Min=5, Max=25. Formula: (Raw-5)/20 * 100
    let matPct = Math.round(((metricsRaw.MAT || 5) - 5) / 20 * 100);
    
    // 3. Reliability & Flags
    let timeTaken = (Date.now() - state.startTime) / 60000; // in minutes
    let relScore = 100;
    if(timeTaken < 3) relScore -= 20; // Answered too fast

    let flags = [];
    // Parental Pressure Check (Q m3 and m7 mapped to PAR in raw data. High raw = high pressure)
    // Actually m3 is direct, m7 is "If marks not important... choose different". 
    let parScore = metricsRaw.PAR || 0; // Max 10. If > 7, high pressure.
    let isHighPressure = parScore >= 8;
    if(isHighPressure) {
      flags.push(`<div class="flag-item"><span>🚩</span><span><strong>Parental Alignment Conflict:</strong> High probability that current career ideas are externally driven rather than internally motivated.</span></div>`);
      // Correction factor: Boost top RIASEC score to cut through pressure
    }

    if(resPct < 50 && state.topValues.includes('High income')) {
      flags.push(`<div class="flag-item"><span>🚩</span><span><strong>Burnout Risk:</strong> High ambition/income value combined with lower stress resilience. Needs coping strategy development.</span></div>`);
    }
    
    if(matPct < 50) {
      flags.push(`<div class="flag-item"><span>🚩</span><span><strong>Decision Confusion:</strong> Profile indicates significant uncertainty. Recommending exploratory internships before finalizing streams.</span></div>`);
    }

    if(flags.length === 0) flags.push(`<div style="color:var(--success); font-weight:bold;">✅ All clinical indicators are stable. No critical risks detected.</div>`);

    // 4. Determine Profile
    const sorted = Object.keys(scores).sort((a,b) => scores[b] - scores[a]);
    const finalCode = sorted.slice(0,3).join('');
    const dom = sorted[0];

    // 5. Interpret Output
    let profileDesc = "";
    if(scores[sorted[0]] >= 75 && scores[sorted[1]] < 65) profileDesc = `You show a <strong>Single Dominant</strong> orientation toward ${dom} tasks. You have intense, focused interests.`;
    else if(scores[sorted[0]] >= 70 && scores[sorted[1]] >= 70) profileDesc = `You have a <strong>Dual Dominant</strong> profile (${sorted[0]} & ${sorted[1]}). You combine these strengths uniquely.`;
    else if(scores[sorted[0]] < 60) profileDesc = `You have a <strong>Diffuse Interest Pattern</strong>. You are adaptable but may need more real-world exploration to find a specialized niche.`;
    else profileDesc = `You demonstrate a <strong>Balanced Exploratory Profile</strong>. You are versatile and can thrive in multi-disciplinary fields.`;

    const matrix = {
      'I': { c: 'Engineering, Medicine, Research, Data Science, AI', a: 'Highly repetitive sales or clerical roles' },
      'A': { c: 'Architecture, UX/UI, Animation, Media, Filmmaking', a: 'Rigid data-entry or heavy administrative jobs' },
      'E': { c: 'Business Management, Law, Entrepreneurship, Marketing', a: 'Isolated lab research or solitary backend coding' },
      'S': { c: 'Psychology, Teaching, HR, Social Work, Medicine', a: 'Strictly mechanical environments without human contact' },
      'R': { c: 'Defence, Aviation, Mechanical Engg, Applied Tech', a: 'Static office-only desk jobs' },
      'C': { c: 'Chartered Accountancy, Banking, Actuary, Govt Admin', a: 'Highly abstract or unpredictable creative roles' }
    };

    // 6. Inject UI
    document.getElementById('outName').innerText = document.getElementById('candName').value || "Candidate";
    document.getElementById('outDate').innerText = new Date().toLocaleDateString();
    
    let relBadge = document.getElementById('outReliability');
    relBadge.innerText = `Reliability Index: ${relScore}%`;
    relBadge.style.background = relScore > 80 ? 'rgba(16, 185, 129, 0.2)' : 'rgba(245, 158, 11, 0.2)';
    relBadge.style.color = relScore > 80 ? 'var(--success)' : 'var(--warning)';

    document.getElementById('outCode').innerText = finalCode;
    document.getElementById('outPersonalityText').innerHTML = profileDesc;
    
    document.getElementById('outStream').innerText = `${matrix[dom].c.split(',')[0]} & Adjacent`;
    document.getElementById('outCareers').innerText = matrix[dom].c;
    document.getElementById('outAvoid').innerText = matrix[dom].a;
    
    document.getElementById('outFlags').innerHTML = flags.join('');

    // Progress Bars
    document.getElementById('bar-apt').style.width = aptPct + '%'; document.getElementById('txt-apt').innerText = aptPct + '%';
    document.getElementById('bar-res').style.width = resPct + '%'; document.getElementById('txt-res').innerText = resPct + '%';
    document.getElementById('bar-mat').style.width = matPct + '%'; document.getElementById('txt-mat').innerText = matPct + '%';
    document.getElementById('bar-par').style.width = (parScore * 10) + '%'; document.getElementById('txt-par').innerText = isHighPressure ? 'HIGH' : 'LOW';

    // Colleges
    const colDiv = document.getElementById('outColleges');
    colDiv.innerHTML = '';
    const sampleCols = [{n:"IISc Bangalore", r:['I']}, {n:"IIT Roorkee", r:['I','R']}, {n:"AAAD", r:['A']}, {n:"Christ University", r:['E','S','C']}, {n:"BMSCE", r:['R','I']}, {n:"Mount Carmel", r:['S','C']}];
    let matches = sampleCols.filter(c => c.r.includes(dom)).slice(0,2);
    if(matches.length===0) matches = [sampleCols[0], sampleCols[3]];
    matches.forEach(c => { colDiv.innerHTML += `<div class="rec-card"><h4>${c.n}</h4><p>Strong match for ${dom} profiles.</p></div>`; });

    // Radar Chart
    const ctx = document.getElementById('riasecChart').getContext('2d');
    if(window.rChart) window.rChart.destroy();
    window.rChart = new Chart(ctx, {
      type: 'radar',
      data: {
        labels: ['Realistic', 'Investigative', 'Artistic', 'Social', 'Enterprising', 'Conventional'],
        datasets: [{ label: 'RIASEC Profile (%)', data: [scores.R, scores.I, scores.A, scores.S, scores.E, scores.C], backgroundColor: 'rgba(139, 92, 246, 0.4)', borderColor: '#8b5cf6', borderWidth: 2 }]
      },
      options: { scales: { r: { max: 100, min: 0, ticks: { display: false } } }, plugins: { legend: { display: false } } }
    });

    document.getElementById('wizardContainer').style.display = 'none';
    document.querySelector('.progress-container').style.display = 'none';
    document.getElementById('reportContainer').style.display = 'block';
    window.scrollTo(0,0);
  }

  function downloadPDF() {
    let btn = document.getElementById('pdfBtn');
    let orig = btn.innerText;
    btn.innerText = "Exporting Clinical PDF... ⏳";
    window.scrollTo(0,0);
    setTimeout(() => {
      const el = document.getElementById('reportContent');
      html2pdf().set({ margin: 0.3, filename: `Clinical_Report.pdf`, image: { type: 'jpeg', quality: 1 }, html2canvas: { scale: 2, useCORS: true }, jsPDF: { unit: 'in', format: 'a4', orientation: 'portrait' } }).from(el).save().then(()=> btn.innerText = orig);
    }, 500);
  }
</script>
