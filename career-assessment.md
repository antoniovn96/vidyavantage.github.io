---
layout: default
title: "Premium Career & Aptitude Assessment 🚀"
permalink: /assessment/
description: "A clinical-grade psychometric career analysis calculating RIASEC, Resilience, Maturity, and Parental Influence."
---

<script src="https://cdnjs.cloudflare.com/ajax/libs/html2pdf.js/0.10.1/html2pdf.bundle.min.js"></script>
<script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
<script src="https://cdn.jsdelivr.net/npm/canvas-confetti@1.6.0/dist/confetti.browser.min.js"></script>

<style>
  /* --- PREMIUM GAMIFIED UI THEME --- */
  :root {
    --bg-color: #0f172a; --card-bg: #1e293b;
    --primary: #8b5cf6; --secondary: #06b6d4; --accent: #f43f5e;
    --text-main: #f8fafc; --text-muted: #94a3b8; --border-color: #334155;
    --success: #10b981; --warning: #f59e0b; --danger: #ef4444;
  }

  body { background-color: var(--bg-color); font-family: 'Nunito', 'Segoe UI', sans-serif; color: var(--text-main); margin: 0; }
  
  .assessment-header {
    background: linear-gradient(135deg, #1e1b4b 0%, #0f172a 100%); padding: 60px 20px 40px; text-align: center; 
    border-bottom: 2px solid var(--border-color); margin-bottom: 40px; position: relative; overflow: hidden;
  }
  .assessment-header h1 { margin: 0 0 10px 0; font-size: 2.8rem; font-weight: 900; background: -webkit-linear-gradient(45deg, var(--secondary), var(--primary)); -webkit-background-clip: text; -webkit-text-fill-color: transparent; }
  .assessment-header p { font-size: 1.1rem; color: var(--text-muted); max-width: 600px; margin: 0 auto; }

  .container { max-width: 1000px; margin: 0 auto; padding: 0 20px; }

  /* PROGRESS BAR */
  .progress-container { width: 100%; background: #0f172a; border-radius: 50px; height: 12px; margin-bottom: 40px; border: 2px solid var(--border-color); }
  .progress-bar { height: 100%; background: linear-gradient(90deg, var(--primary), var(--secondary)); width: 10%; transition: width 0.4s ease; border-radius: 50px; }

  /* WIZARD CARDS */
  .step-card {
    background: rgba(30, 41, 59, 0.7); backdrop-filter: blur(10px); padding: 40px; border-radius: 24px; 
    border: 1px solid rgba(255,255,255,0.05); box-shadow: 0 20px 40px rgba(0,0,0,0.4); margin-bottom: 40px;
    display: none; animation: slideUp 0.4s ease;
  }
  .step-card.active { display: block; }
  .step-title { font-size: 1.8rem; font-weight: 800; color: white; margin-bottom: 5px; text-align: center; }
  .step-sub { text-align: center; color: var(--secondary); margin-bottom: 30px; font-size: 1rem; font-weight: bold; text-transform: uppercase; letter-spacing: 1px; }

  /* COMPACT GRIDS & INPUTS */
  .grid-2col { display: grid; grid-template-columns: 1fr 1fr; gap: 20px; margin-bottom: 20px; }
  @media (max-width: 768px) { .grid-2col { grid-template-columns: 1fr; } }
  
  .form-group { margin-bottom: 20px; }
  .form-label { display: block; font-weight: 700; margin-bottom: 8px; color: var(--text-main); font-size: 1rem; }
  .form-input, .form-select, .form-textarea {
    width: 100%; padding: 15px; border: 2px solid var(--border-color); border-radius: 12px;
    font-size: 1rem; color: white; background: #0f172a; transition: 0.3s; font-family: inherit; box-sizing: border-box;
  }
  .form-input:focus, .form-select:focus, .form-textarea:focus { border-color: var(--primary); outline: none; }
  .form-textarea { min-height: 80px; resize: vertical; }

  /* RATING SCALES */
  .scale-legend { display: flex; justify-content: space-between; color: var(--text-muted); font-size: 0.8rem; font-weight: bold; margin-bottom: 10px; padding: 0 10px; text-transform: uppercase; }
  .rating-grid { display: grid; grid-template-columns: 1fr; gap: 10px; margin-bottom: 30px; max-height: 500px; overflow-y: auto; padding-right: 10px; }
  .rating-grid::-webkit-scrollbar { width: 6px; }
  .rating-grid::-webkit-scrollbar-thumb { background: var(--border-color); border-radius: 10px; }
  
  .rating-row {
    display: flex; align-items: center; justify-content: space-between; background: #0f172a; 
    padding: 12px 20px; border-radius: 12px; border: 1px solid var(--border-color); transition: 0.2s;
  }
  .rating-row:hover { border-color: var(--primary); }
  .rating-label { font-weight: 600; font-size: 1rem; flex: 1; color: var(--text-main); }
  .rating-options { display: flex; gap: 8px; background: #1e293b; padding: 4px; border-radius: 50px; }
  
  .rate-btn {
    width: 35px; height: 35px; border-radius: 50%; border: none; background: transparent; 
    font-size: 1.2rem; cursor: pointer; display: flex; align-items: center; justify-content: center; transition: 0.2s;
    filter: grayscale(100%) opacity(0.4);
  }
  .rate-btn:hover { filter: grayscale(0%) opacity(1); transform: scale(1.2); }
  .rate-btn.selected { filter: grayscale(0%) opacity(1); transform: scale(1.2); background: rgba(255,255,255,0.1); box-shadow: 0 0 10px rgba(255,255,255,0.1); }

  /* PILL TAGS */
  .pill-grid { display: flex; flex-wrap: wrap; gap: 10px; margin-bottom: 20px; }
  .pill-tag {
    background: #0f172a; border: 2px solid var(--border-color); padding: 10px 20px; border-radius: 50px;
    font-weight: 700; color: var(--text-muted); cursor: pointer; transition: 0.2s; font-size: 0.95rem; user-select: none;
  }
  .pill-tag.selected { background: var(--primary); border-color: var(--primary); color: white; box-shadow: 0 5px 15px rgba(139, 92, 246, 0.3); }

  /* BUTTONS */
  .btn-nav-wrapper { display: flex; justify-content: space-between; gap: 15px; margin-top: 30px; border-top: 1px solid var(--border-color); padding-top: 25px; }
  .btn-main {
    background: linear-gradient(45deg, var(--primary), #a855f7); color: white; border: none; padding: 15px 35px;
    font-size: 1.1rem; font-weight: 900; border-radius: 50px; cursor: pointer; flex-grow: 1; transition: 0.3s; text-transform: uppercase;
  }
  .btn-main:hover { transform: translateY(-2px); box-shadow: 0 10px 20px rgba(139, 92, 246, 0.3); }
  .btn-back { background: transparent; border: 2px solid var(--border-color); color: var(--text-muted); flex-grow: 0; }

  /* --- CLINICAL REPORT STYLES (Light theme for PDF) --- */
  #reportContainer { display: none; }
  .report-card { background: white; padding: 40px; border-radius: 16px; margin-bottom: 40px; color: #0f172a; }
  .report-header { text-align: center; border-bottom: 2px solid #e2e8f0; padding-bottom: 20px; margin-bottom: 30px; }
  .report-header h2 { font-size: 2.5rem; font-weight: 900; margin: 0; color: #0f172a; }
  .badge-code { display: inline-block; background: var(--primary); color: white; padding: 8px 25px; border-radius: 50px; font-weight: 900; font-size: 1.5rem; margin-top: 10px; letter-spacing: 2px; }

  .chart-container { max-width: 400px; margin: 0 auto 30px auto; }
  
  .report-section { background: #f8fafc; border-radius: 12px; padding: 25px; margin-bottom: 30px; border-left: 6px solid var(--secondary); }
  .report-section h3 { margin-top: 0; font-size: 1.4rem; color: #0f172a; font-weight: 800; border-bottom: 1px solid #e2e8f0; padding-bottom: 10px; }
  .report-section p { font-size: 1.05rem; line-height: 1.6; color: #334155; }

  /* CLINICAL BARS */
  .clinical-metric { margin-bottom: 15px; }
  .metric-header { display: flex; justify-content: space-between; font-weight: 700; margin-bottom: 5px; font-size: 0.95rem; color: #475569; }
  .metric-track { width: 100%; height: 10px; background: #e2e8f0; border-radius: 10px; overflow: hidden; }
  .metric-fill { height: 100%; border-radius: 10px; }

  .college-recs { display: grid; grid-template-columns: 1fr 1fr; gap: 15px; margin-top: 15px; }
  .rec-card { border: 2px solid #e2e8f0; padding: 15px; border-radius: 10px; background: white; }
  .rec-card h4 { margin: 0 0 5px 0; color: var(--primary); font-size: 1.1rem; }

  @keyframes slideUp { from { opacity: 0; transform: translateY(20px); } to { opacity: 1; transform: translateY(0); } }

  @media print {
    body { background: white; }
    .actions, .assessment-header, .progress-container { display: none !important; }
    .report-card { padding: 0; box-shadow: none; }
    .report-section { page-break-inside: avoid; border: 1px solid #e2e8f0; margin-bottom: 20px; }
    .college-recs { display: block; }
    .rec-card { margin-bottom: 10px; }
  }
</style>

<div class="assessment-header">
  <h1>Premium Clinical Assessment</h1>
  <p>An advanced psychometric evaluation of your interests, aptitudes, and resilience.</p>
</div>

<div class="container">
  <div class="progress-container"><div class="progress-bar" id="progressBar"></div></div>

  <div id="wizardContainer">
    
    <div class="step-card active" id="step1">
      <h2 class="step-title">Academic Context</h2>
      <p class="step-sub">LEVEL 1 / 8</p>
      
      <div class="grid-2col">
        <div class="form-group"><label class="form-label">Full Name</label><input type="text" id="qName" class="form-input"></div>
        <div class="form-group">
          <label class="form-label">Current Grade/Level</label>
          <select id="qGrade" class="form-select" onchange="toggleStreamView()">
            <option value="8-10">Grade 8 - 10</option>
            <option value="11-12">Grade 11 - 12 (PUC)</option>
            <option value="UG">Undergraduate</option>
          </select>
        </div>
      </div>
      
      <div class="grid-2col">
        <div class="form-group"><label class="form-label">Average Marks (%)</label><input type="number" id="qMarks" class="form-input" placeholder="e.g. 85"></div>
        <div class="form-group">
          <label class="form-label" id="streamLabel">Target Stream (After 10th)</label>
          <select id="qStream" class="form-select">
            <option value="PCM">Science (PCM/Tech)</option>
            <option value="PCB">Science (PCB/Med)</option>
            <option value="Commerce">Commerce</option>
            <option value="Arts">Arts / Humanities</option>
            <option value="Undecided">Undecided</option>
          </select>
        </div>
      </div>
      
      <div class="grid-2col">
        <div class="form-group"><label class="form-label">Strongest Subject</label><input type="text" id="qStrong" class="form-input"></div>
        <div class="form-group"><label class="form-label">Weakest Subject</label><input type="text" id="qWeak" class="form-input"></div>
      </div>
      
      <button class="btn-main" style="width:100%" onclick="nextStep(2)">Proceed to Evaluation ➔</button>
    </div>

    <div class="step-card" id="step2">
      <h2 class="step-title">Academic Interests</h2>
      <p class="step-sub">LEVEL 2 / 8 • Rate how much you genuinely enjoy these.</p>
      <div class="scale-legend"><span>1 = Strongly Disagree</span><span>5 = Strongly Agree</span></div>
      <div class="rating-grid" id="grid-acad"></div>
      <div class="btn-nav-wrapper"><button class="btn-main btn-back" onclick="prevStep(1)">Back</button><button class="btn-main" onclick="nextStep(3)">Next ➔</button></div>
    </div>

    <div class="step-card" id="step3">
      <h2 class="step-title">Activity Preferences</h2>
      <p class="step-sub">LEVEL 3 / 8 • Core RIASEC Mapping (Scroll to see all)</p>
      <div class="scale-legend"><span>1 = Hate it</span><span>5 = Love it</span></div>
      <div class="rating-grid" id="grid-acts"></div>
      <div class="btn-nav-wrapper"><button class="btn-main btn-back" onclick="prevStep(2)">Back</button><button class="btn-main" onclick="nextStep(4)">Next ➔</button></div>
    </div>

    <div class="step-card" id="step4">
      <h2 class="step-title">Aptitude & Environment</h2>
      <p class="step-sub">LEVEL 4 / 8 • Self-Perception</p>
      
      <h3 style="color:var(--secondary); font-size:1.1rem;">How confident are you in:</h3>
      <div class="rating-grid" style="max-height:250px;" id="grid-apt"></div>
      
      <h3 style="color:var(--secondary); font-size:1.1rem; margin-top:20px;">I prefer a job that:</h3>
      <div class="rating-grid" style="max-height:250px;" id="grid-env"></div>

      <div class="btn-nav-wrapper"><button class="btn-main btn-back" onclick="prevStep(3)">Back</button><button class="btn-main" onclick="nextStep(5)">Next ➔</button></div>
    </div>

    <div class="step-card" id="step5">
      <h2 class="step-title">Career Values Matrix</h2>
      <p class="step-sub">LEVEL 5 / 8 • Select exactly your TOP 5 most important values.</p>
      <div class="pill-grid" id="valuesGrid">
        <div class="pill-tag" onclick="toggleValue(this)">High income</div>
        <div class="pill-tag" onclick="toggleValue(this)">Work-life balance</div>
        <div class="pill-tag" onclick="toggleValue(this)">Helping society</div>
        <div class="pill-tag" onclick="toggleValue(this)">Prestige/status</div>
        <div class="pill-tag" onclick="toggleValue(this)">Job security</div>
        <div class="pill-tag" onclick="toggleValue(this)">Creativity</div>
        <div class="pill-tag" onclick="toggleValue(this)">Independence</div>
        <div class="pill-tag" onclick="toggleValue(this)">Fast career growth</div>
        <div class="pill-tag" onclick="toggleValue(this)">Stability</div>
        <div class="pill-tag" onclick="toggleValue(this)">Work flexibility</div>
      </div>
      <div class="btn-nav-wrapper"><button class="btn-main btn-back" onclick="prevStep(4)">Back</button><button class="btn-main" onclick="validateValues()">Next ➔</button></div>
    </div>

    <div class="step-card" id="step6">
      <h2 class="step-title">Clinical Mindset Index</h2>
      <p class="step-sub">LEVEL 6 / 8 • Maturity & Resilience Check</p>
      <div class="scale-legend"><span>1 = Strongly Disagree</span><span>5 = Strongly Agree</span></div>
      <div class="rating-grid" id="grid-mind"></div>
      <div class="btn-nav-wrapper"><button class="btn-main btn-back" onclick="prevStep(5)">Back</button><button class="btn-main" onclick="nextStep(7)">Next ➔</button></div>
    </div>

    <div class="step-card" id="step7">
      <h2 class="step-title">The Reality Check</h2>
      <p class="step-sub">LEVEL 7 / 8 • Internal Conflict Resolution</p>
      
      <div class="form-group"><label class="form-label">If marks did not matter, what career would you secretly choose?</label><input type="text" id="qSecret" class="form-input"></div>
      <div class="form-group"><label class="form-label">Why does that career attract you?</label><input type="text" class="form-input"></div>
      <div class="form-group"><label class="form-label">What career do your parents prefer for you?</label><input type="text" id="qParent" class="form-input"></div>
      <div class="form-group"><label class="form-label">What is your biggest fear about career decisions?</label><textarea class="form-textarea"></textarea></div>

      <div class="btn-nav-wrapper"><button class="btn-main btn-back" onclick="prevStep(6)">Back</button><button class="btn-main" style="background:var(--success);" id="analyzeBtn" onclick="generateReport()">Compile Dossier ✨</button></div>
    </div>
  </div>

  <div id="reportContainer">
    <div class="report-card" id="reportContent">
      <div class="report-header">
        <h2>Psychometric Career Dossier</h2>
        <div class="report-meta">
          <strong><span id="outName"></span></strong> | Grade: <span id="outGrade"></span> | Stream: <span id="outStreamContext"></span><br>
          Generated: <span id="outDate"></span>
        </div>
        <div class="badge-code" id="outCode">ISR</div>
      </div>

      <div class="grid-2col">
        <div class="chart-container"><canvas id="riasecChart"></canvas></div>
        
        <div class="report-section" style="margin-bottom:0; padding:15px;">
          <h3>📊 Clinical Indices</h3>
          
          <div class="clinical-metric">
            <div class="metric-header"><span>Aptitude Confidence</span><span id="txt-conf"></span></div>
            <div class="metric-track"><div class="metric-fill" id="bar-conf" style="background:var(--primary); width:0%;"></div></div>
          </div>
          
          <div class="clinical-metric">
            <div class="metric-header"><span>Stress Resilience</span><span id="txt-res"></span></div>
            <div class="metric-track"><div class="metric-fill" id="bar-res" style="background:var(--success); width:0%;"></div></div>
          </div>
          
          <div class="clinical-metric">
            <div class="metric-header"><span>Decision Maturity</span><span id="txt-mat"></span></div>
            <div class="metric-track"><div class="metric-fill" id="bar-mat" style="background:var(--secondary); width:0%;"></div></div>
          </div>
          
          <div class="clinical-metric" style="margin-bottom:0;">
            <div class="metric-header"><span>Parental Influence</span><span id="txt-par"></span></div>
            <div class="metric-track"><div class="metric-fill" id="bar-par" style="background:var(--warning); width:0%;"></div></div>
          </div>
        </div>
      </div>

      <div class="report-section">
        <h3>🧠 Core Personality & Pathway</h3>
        <p id="outPersonalityText"></p>
        <p style="margin-top:15px; font-weight:bold; color:var(--primary);">Recommended Path: <span id="outStream"></span></p>
        <p><strong>Ideal Careers:</strong> <span id="outCareers"></span></p>
      </div>

      <div class="report-section avoid-section">
        <h3>⚠️ Vulnerability Zones (Avoid)</h3>
        <p>Careers mapped to your lowest RIASEC scores where burnout is highly probable:</p>
        <p><strong id="outAvoid"></strong></p>
      </div>

      <div class="report-section" style="border-left-color: var(--secondary);">
        <h3>🏛️ Optimal College Basecamps</h3>
        <div class="college-recs" id="outColleges"></div>
      </div>
      
    </div>

    <div class="actions">
      <button class="btn-main" id="pdfBtn" onclick="downloadPDF()">📄 Export Clinical PDF</button>
      <button class="btn-main btn-back" style="margin-left: 10px; border-color:white; color:white;" onclick="location.reload()">↺ Restart</button>
    </div>
  </div>
</div>

<script>
  // --- DATA INJECTION SCRIPT ---
  const questions = {
    acad: [
      {id:'a1', label:'Solving mathematical problems', trait:'I_C'}, {id:'a2', label:'Conducting science experiments', trait:'I_R'},
      {id:'a3', label:'Understanding how machines work', trait:'R_I'}, {id:'a4', label:'Learning about human behaviour', trait:'S_I'},
      {id:'a5', label:'Writing essays or stories', trait:'A'}, {id:'a6', label:'Drawing/designing', trait:'A'},
      {id:'a7', label:'Debating or convincing others', trait:'E'}, {id:'a8', label:'Managing money/accounts', trait:'C_E'},
      {id:'a9', label:'Working with computers/coding', trait:'I_R'}, {id:'a10', label:'Memorising theory-based subjects', trait:'C'}
    ],
    acts: [
      {id:'ac1', label:'Analysing data & researching topics', trait:'I'}, {id:'ac2', label:'Solving logical puzzles', trait:'I'},
      {id:'ac3', label:'Asking “why” and “how” questions', trait:'I'}, {id:'ac4', label:'Building or repairing things', trait:'R'},
      {id:'ac5', label:'Outdoor work & physical activity', trait:'R'}, {id:'ac6', label:'Practical hands-on tasks', trait:'R'},
      {id:'ac7', label:'Creative writing / Video creation', trait:'A'}, {id:'ac8', label:'Designing or sketching', trait:'A'},
      {id:'ac9', label:'Music or performing arts', trait:'A'}, {id:'ac10', label:'Helping others with problems', trait:'S'},
      {id:'ac11', label:'Teaching & listening to concerns', trait:'S'}, {id:'ac12', label:'Volunteering', trait:'S'},
      {id:'ac13', label:'Leading group projects', trait:'E'}, {id:'ac14', label:'Starting small business ideas', trait:'E'},
      {id:'ac15', label:'Persuading & Public speaking', trait:'E'}, {id:'ac16', label:'Organising data & records', trait:'C'},
      {id:'ac17', label:'Following structured instructions', trait:'C'}, {id:'ac18', label:'Working with spreadsheets', trait:'C'}
    ],
    apt: [
      {id:'ap1', label:'Numerical ability', cat:'conf'}, {id:'ap2', label:'Logical reasoning', cat:'conf'},
      {id:'ap3', label:'Communication skills', cat:'conf'}, {id:'ap4', label:'Memory retention', cat:'conf'},
      {id:'ap5', label:'Attention to detail', cat:'conf'}, {id:'ap6', label:'Creativity', cat:'conf'},
      {id:'ap7', label:'Emotional understanding', cat:'conf'}, {id:'ap8', label:'Leadership ability', cat:'conf'}
    ],
    env: [
      {id:'e1', label:'Has stable working hours', cat:'C'}, {id:'e2', label:'Involves frequent social interaction', cat:'S'},
      {id:'e3', label:'Requires independent work', cat:'I_R'}, {id:'e4', label:'Allows creativity', cat:'A'},
      {id:'e5', label:'High job security (Govt)', cat:'C'}, {id:'e6', label:'Offers high income potential', cat:'E'}
    ],
    mind: [
      {id:'m1', label:'I know my strengths clearly.', cat:'mat_pos'}, {id:'m2', label:'I feel confused about my future.', cat:'mat_neg'},
      {id:'m3', label:'I am choosing a career mainly because of marks.', cat:'par_pos'}, {id:'m4', label:'My parents strongly influence my choice.', cat:'par_pos'},
      {id:'m5', label:'I worry about disappointing my parents.', cat:'par_pos'}, {id:'m6', label:'I have explored careers beyond traditional ones.', cat:'mat_pos'},
      {id:'m7', label:'I handle academic pressure well.', cat:'res_pos'}, {id:'m8', label:'I panic before exams.', cat:'res_neg'},
      {id:'m9', label:'I give up easily when things are difficult.', cat:'res_neg'}, {id:'m10', label:'I continue trying even after failure.', cat:'res_pos'},
      {id:'m11', label:'ATTENTION CHECK: Select "Agree" (4) for this row.', cat:'check'}
    ]
  };

  const emojis = ['😖', '😕', '😐', '🙂', '🤩'];
  let state = { scores: {}, selValues: 0 };

  // Generator Function
  function renderGrid(containerId, dataArray) {
    const container = document.getElementById(containerId);
    let html = '';
    dataArray.forEach(q => {
      html += `<div class="rating-row" data-id="${q.id}" data-cat="${q.trait || q.cat}">
        <div class="rating-label">${q.label}</div>
        <div class="rating-options">
          ${[1,2,3,4,5].map(n => `<div class="rate-btn" onclick="setRate(this, '${q.id}', ${n})">${emojis[n-1]}</div>`).join('')}
        </div>
      </div>`;
    });
    container.innerHTML = html;
  }

  // Init Grids
  renderGrid('grid-acad', questions.acad);
  renderGrid('grid-acts', questions.acts);
  renderGrid('grid-apt', questions.apt);
  renderGrid('grid-env', questions.env);
  renderGrid('grid-mind', questions.mind);

  function toggleStreamView() {
    let lvl = document.getElementById('qGrade').value;
    document.getElementById('streamLabel').innerText = lvl === '8-10' ? "Target Stream (After 10th)" : "Current Stream";
  }

  function setRate(btn, id, val) {
    let p = btn.parentElement;
    Array.from(p.children).forEach(c => c.classList.remove('selected'));
    btn.classList.add('selected');
    let cat = p.parentElement.dataset.cat;
    state.scores[id] = { val: val, cat: cat };
  }

  function toggleValue(el) {
    if(el.classList.contains('selected')) {
      el.classList.remove('selected'); state.selValues--;
    } else {
      if(state.selValues >= 5) return alert("Select only 5 values.");
      el.classList.add('selected'); state.selValues++;
    }
  }

  function validateValues() {
    if(state.selValues !== 5) return alert("Please select exactly 5 core values.");
    nextStep(6);
  }

  function nextStep(s) {
    document.querySelectorAll('.step-card').forEach(c => c.classList.remove('active'));
    document.getElementById('step' + s).classList.add('active');
    document.getElementById('progressBar').style.width = ((s / 7) * 100) + '%';
    window.scrollTo({ top: 0, behavior: 'smooth' });
  }
  function prevStep(s) { nextStep(s); }

  // MATRIX
  const matrix = {
    'I': { p: 'Research, Tech & Analysis', c: 'Engineering, Medicine, Data Science, AI, Pharmacy' },
    'A': { p: 'Creative Arts & Design', c: 'Architecture, UX/UI, Animation, Filmmaking, Writing' },
    'E': { p: 'Commerce & Leadership', c: 'Business Management, Law, MBA, Entrepreneurship' },
    'S': { p: 'Humanities & Care', c: 'Psychology, Teaching, Counselling, HR, Social Work' },
    'R': { p: 'Applied Tech & Fieldwork', c: 'Defence, Aviation, Mechanical Engg, Sports' },
    'C': { p: 'Finance & Administration', c: 'CA, Banking, Accounting, Government Administration' }
  };

  function generateReport() {
    let btn = document.getElementById('analyzeBtn');
    btn.innerText = "Processing Clinical Data... ⏳";
    
    setTimeout(() => {
      confetti({ particleCount: 150, spread: 70, origin: { y: 0.6 } });

      let riasec = { R:0, I:0, A:0, S:0, E:0, C:0 };
      let metrics = { conf:0, res:0, mat:0, par:0 };
      let counts = { conf:0, res:0, mat:0, par:0 };

      // Process Scores
      for(let key in state.scores) {
        let item = state.scores[key];
        
        // Attention Check
        if(item.cat === 'check' && item.val !== 4) console.warn("Attention check failed.");

        // RIASEC Categories (split by underscore e.g., I_C)
        if(['R','I','A','S','E','C'].some(t => item.cat.includes(t))) {
          item.cat.split('_').forEach(c => {
            if(riasec[c] !== undefined) riasec[c] += (item.val - 3) * 2; 
          });
        }
        
        // Clinical Metrics
        if(item.cat === 'conf') { metrics.conf += item.val; counts.conf++; }
        if(item.cat === 'mat_pos') { metrics.mat += item.val; counts.mat++; }
        if(item.cat === 'mat_neg') { metrics.mat += (6 - item.val); counts.mat++; }
        if(item.cat === 'res_pos') { metrics.res += item.val; counts.res++; }
        if(item.cat === 'res_neg') { metrics.res += (6 - item.val); counts.res++; }
        if(item.cat === 'par_pos') { metrics.par += item.val; counts.par++; }
      }

      // Parental Index Correction
      const parent = document.getElementById('qParent').value.toLowerCase();
      const secret = document.getElementById('qSecret').value.toLowerCase();
      if(secret && parent && secret !== parent) {
        let topCode = Object.keys(riasec).reduce((a, b) => riasec[a] > riasec[b] ? a : b);
        riasec[topCode] = Math.round(riasec[topCode] * 1.5); // Boost
        metrics.par += 5; counts.par++; // Increase parent pressure score
      }
      
      for(let k in riasec) { if(riasec[k] < 0) riasec[k] = 0; }

      const sorted = Object.keys(riasec).sort((a,b) => riasec[b] - riasec[a]);
      const finalCode = sorted.slice(0,3).join('');
      const dominant = sorted[0];
      const weakest = sorted[5];

      // Calculate Percentages (Max score per question is 5)
      const pctConf = Math.round((metrics.conf / (counts.conf * 5)) * 100) || 50;
      const pctRes = Math.round((metrics.res / (counts.res * 5)) * 100) || 50;
      const pctMat = Math.round((metrics.mat / (counts.mat * 5)) * 100) || 50;
      const pctPar = Math.round((metrics.par / (counts.par * 5)) * 100) || 50;

      // Populate UI
      document.getElementById('outName').innerText = document.getElementById('qName').value || "Student";
      document.getElementById('outGrade').innerText = document.getElementById('qGrade').value;
      document.getElementById('outStreamContext').innerText = document.getElementById('qStream').value;
      document.getElementById('outDate').innerText = new Date().toLocaleDateString();
      document.getElementById('outCode').innerText = finalCode;
      
      const resData = matrix[dominant];
      document.getElementById('outStream').innerText = resData.p;
      document.getElementById('outCareers').innerText = resData.c;
      document.getElementById('outAvoid').innerText = matrix[weakest].c;
      
      document.getElementById('outPersonalityText').innerText = `Your dominant trait is ${dominant}. You lean towards ${resData.p}, thriving in environments that match this energy while avoiding ${matrix[weakest].p}. Your decision maturity indicates you are ${pctMat > 60 ? 'ready' : 'still exploring'} to make final stream choices.`;

      // Set Progress Bars
      document.getElementById('bar-conf').style.width = pctConf + '%'; document.getElementById('txt-conf').innerText = pctConf + '%';
      document.getElementById('bar-res').style.width = pctRes + '%'; document.getElementById('txt-res').innerText = pctRes + '%';
      document.getElementById('bar-mat').style.width = pctMat + '%'; document.getElementById('txt-mat').innerText = pctMat + '%';
      
      let parBar = document.getElementById('bar-par');
      parBar.style.width = pctPar + '%'; document.getElementById('txt-par').innerText = pctPar + '%';
      if(pctPar > 70) parBar.style.background = 'var(--danger)'; // High pressure warning

      // Dynamic Colleges
      const colDiv = document.getElementById('outColleges');
      colDiv.innerHTML = '';
      const sampleCols = [{n:"IISc Bangalore", r:['I']}, {n:"IIT Roorkee", r:['I','R']}, {n:"AAAD", r:['A']}, {n:"Christ University", r:['E','S','C']}, {n:"BMSCE", r:['R','I']}, {n:"Mount Carmel", r:['S','C']}];
      let matches = sampleCols.filter(c => c.r.includes(dominant)).slice(0,3);
      if(matches.length===0) matches = [sampleCols[0], sampleCols[3]];
      matches.forEach(c => { colDiv.innerHTML += `<div class="rec-card"><h4>${c.n}</h4><p>Strong match for ${dominant} profiles.</p></div>`; });

      // Render Chart
      const ctx = document.getElementById('riasecChart').getContext('2d');
      if(window.rChart) window.rChart.destroy();
      window.rChart = new Chart(ctx, {
        type: 'radar',
        data: {
          labels: ['Realistic', 'Investigative', 'Artistic', 'Social', 'Enterprising', 'Conventional'],
          datasets: [{ label: 'RIASEC Profile', data: [riasec.R, riasec.I, riasec.A, riasec.S, riasec.E, riasec.C], backgroundColor: 'rgba(139, 92, 246, 0.4)', borderColor: '#8b5cf6', borderWidth: 2 }]
        },
        options: { scales: { r: { ticks: { display: false } } }, plugins: { legend: { display: false } } }
      });

      document.getElementById('wizardContainer').style.display = 'none';
      document.querySelector('.progress-container').style.display = 'none';
      document.getElementById('reportContainer').style.display = 'block';
      window.scrollTo(0,0);
    }, 1000);
  }

  function downloadPDF() {
    let btn = document.getElementById('pdfBtn');
    let orig = btn.innerText;
    btn.innerText = "Exporting... ⏳";
    window.scrollTo(0,0);
    setTimeout(() => {
      const el = document.getElementById('reportContent');
      html2pdf().set({ margin: 0.3, filename: `Clinical_Report.pdf`, image: { type: 'jpeg', quality: 1 }, html2canvas: { scale: 2, useCORS: true }, jsPDF: { unit: 'in', format: 'a4', orientation: 'portrait' } }).from(el).save().then(()=> btn.innerText = orig);
    }, 500);
  }
</script>
