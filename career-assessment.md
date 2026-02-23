---
layout: default
title: "Premium Career Assessment 🚀"
permalink: /assessment/
description: "A clinical-grade psychometric evaluation mapping your RIASEC interests, resilience, and academic eligibility."
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
    --text-dark: #0f172a;
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
  .progress-bar { height: 100%; background: linear-gradient(90deg, var(--primary), var(--secondary)); width: 14%; transition: width 0.4s ease; border-radius: 50px; }

  /* WIZARD CARDS */
  .step-card {
    background: var(--card-bg); padding: 35px; border-radius: 20px; border: 1px solid rgba(255,255,255,0.05);
    box-shadow: 0 15px 30px rgba(0,0,0,0.3); margin-bottom: 30px; display: none; animation: slideUp 0.4s ease;
  }
  .step-card.active { display: block; }
  .step-title { font-size: 1.6rem; font-weight: 800; color: white; margin-bottom: 5px; text-align: center; }
  .step-sub { text-align: center; color: var(--secondary); margin-bottom: 25px; font-weight: bold; text-transform: uppercase; letter-spacing: 1px; font-size: 0.9rem;}

  /* UI COMPONENTS */
  .grid-2col { display: grid; grid-template-columns: 1fr 1fr; gap: 20px; }
  @media (max-width: 768px) { .grid-2col { grid-template-columns: 1fr; } }
  
  .form-group { margin-bottom: 20px; }
  .form-label { display: block; font-weight: 700; margin-bottom: 8px; color: var(--text-muted); font-size: 0.95rem; text-transform: uppercase;}
  
  .form-input, .form-select, .form-textarea { 
    width: 100%; padding: 15px; border: 2px solid var(--border); border-radius: 12px; 
    font-size: 1.1rem; color: white; background: #0f172a; box-sizing: border-box; transition: 0.3s; font-family: inherit;
  }
  .form-textarea { resize: vertical; min-height: 80px; }
  .form-input:focus, .form-select:focus, .form-textarea:focus { border-color: var(--primary); outline: none; }

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
  .report-card { background: white; padding: 40px; border-radius: 16px; color: var(--text-dark); }
  .r-header { text-align: center; border-bottom: 2px solid #e2e8f0; padding-bottom: 20px; margin-bottom: 30px; }
  .r-header h2 { font-size: 2.2rem; font-weight: 900; margin: 0; color: var(--text-dark); }
  .reliability-badge { display: inline-block; padding: 5px 15px; border-radius: 50px; font-size: 0.85rem; font-weight: bold; margin-top: 10px; }
  .badge-code { display: inline-block; background: var(--primary); color: white; padding: 8px 30px; border-radius: 50px; font-weight: 900; font-size: 1.8rem; margin-top: 15px; letter-spacing: 2px; }
  
  .grid-2 { display: grid; grid-template-columns: 1fr 1fr; gap: 20px; margin-bottom: 30px; }
  @media (max-width: 768px) { .grid-2 { grid-template-columns: 1fr; } }
  
  .chart-box { max-width: 400px; margin: 0 auto; }
  .metrics-box { padding: 20px; background: #f8fafc; border-radius: 12px; border: 1px solid #e2e8f0; }
  
  .metric { margin-bottom: 12px; }
  .m-head { display: flex; justify-content: space-between; font-size: 0.9rem; font-weight: bold; color: #475569; margin-bottom: 4px; }
  .m-track { width: 100%; height: 8px; background: #e2e8f0; border-radius: 10px; overflow: hidden; }
  .m-fill { height: 100%; border-radius: 10px; }

  .r-section { background: #f8fafc; border-radius: 12px; padding: 25px; margin-bottom: 25px; border-left: 5px solid var(--secondary); }
  .r-section h3 { margin-top: 0; font-size: 1.3rem; color: var(--text-dark); border-bottom: 1px solid #e2e8f0; padding-bottom: 10px; }
  .r-section p { line-height: 1.7; font-size: 1.05rem; color: #334155; }
  
  .flag-box { background: #fff1f2; border-left-color: var(--accent); }
  .flag-box h3 { color: #e11d48; }
  .flag-item { display: flex; gap: 10px; margin-bottom: 10px; font-weight: bold; color: #9f1239; }
  
  .career-bar { display: flex; justify-content: space-between; align-items: center; background: white; padding: 12px 15px; border-radius: 8px; border: 1px solid #e2e8f0; margin-bottom: 10px; }
  .career-score { font-weight: 900; color: var(--primary); background: #f1f5f9; padding: 5px 10px; border-radius: 8px; }

  .college-recs { display: grid; grid-template-columns: 1fr 1fr; gap: 15px; margin-top: 15px; }
  .rec-card { border: 2px solid #e2e8f0; padding: 15px; border-radius: 10px; background: white; }
  .rec-card h4 { margin: 0 0 5px 0; color: var(--primary); font-size: 1.1rem; }
  .rec-card p { margin: 0; font-size: 0.9rem; color: #64748b; }

  @keyframes slideUp { from { opacity: 0; transform: translateY(15px); } to { opacity: 1; transform: translateY(0); } }

  @media print {
    body { background: white; }
    .assessment-header, .progress-container, .btn-wrapper { display: none !important; }
    .report-card { padding: 0; box-shadow: none; border: none; }
    .r-section { page-break-inside: avoid; border: 1px solid #e2e8f0; }
    .college-recs { display: block; }
    .rec-card { margin-bottom: 10px; }
  }
</style>

<div class="assessment-header">
  <h1>Premium Clinical Assessment</h1>
  <p>75-Point Psychometric Evaluation • RIASEC • Aptitude • Resilience • Stream Match</p>
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
          Candidate: <strong id="outName" style="color:var(--text-dark);"></strong> | Grade: <span id="outGrade"></span> | Stream: <span id="outStreamContext"></span><br>
          Generated: <span id="outDate"></span>
        </div>
        <div class="reliability-badge" id="outReliability"></div><br>
        <div class="badge-code" id="outCode"></div>
      </div>

      <div class="grid-2">
        <div class="chart-box"><canvas id="riasecChart"></canvas></div>
        <div class="metrics-box">
          <h3 style="margin-top:0; color:var(--text-dark); font-size:1.2rem;">Clinical Indices</h3>
          <div class="metric"><div class="m-head"><span>Aptitude Confidence</span><span id="txt-apt"></span></div><div class="m-track"><div class="m-fill" id="bar-apt" style="background:var(--primary);"></div></div></div>
          <div class="metric"><div class="m-head"><span>Stress Resilience</span><span id="txt-res"></span></div><div class="m-track"><div class="m-fill" id="bar-res" style="background:var(--success);"></div></div></div>
          <div class="metric"><div class="m-head"><span>Decision Maturity</span><span id="txt-mat"></span></div><div class="m-track"><div class="m-fill" id="bar-mat" style="background:var(--secondary);"></div></div></div>
          <div class="metric" style="margin-bottom:0;"><div class="m-head"><span>External Pressure</span><span id="txt-par"></span></div><div class="m-track"><div class="m-fill" id="bar-par" style="background:var(--warning);"></div></div></div>
        </div>
      </div>

      <div class="r-section">
        <h3>🧠 Psychological Profile Summary</h3>
        <p><strong style="font-size:1.2rem; color:var(--primary);" id="outType"></strong></p>
        <p id="outPersonalityText"></p>
      </div>

      <div class="r-section" style="border-left-color: var(--primary);">
        <h3>🎯 Weighted Career Matching Engine</h3>
        <p style="font-size:0.95rem; color:#64748b; margin-bottom: 15px;">Calculated using your unique RIASEC signature, aptitude, resilience, core values, and <strong>academic stream eligibility</strong>.</p>
        <p id="outStream" style="font-weight:900; color:var(--primary); font-size:1.3rem; margin-bottom:15px; border-bottom: 2px dashed #e2e8f0; padding-bottom: 10px;"></p>
        <p style="font-weight:bold; color:var(--text-dark); font-size:1.1rem; margin-bottom:10px;">Top 5 Aligned Pathways:</p>
        <div id="outCareers"></div>
      </div>

      <div class="r-section avoid-section">
        <h3>🚫 Vulnerability Zones (Avoid)</h3>
        <p>Careers mapped to your lowest traits where burnout or lack of motivation is highly probable:</p>
        <p id="outAvoid"></p>
      </div>

      <div class="r-section" style="border-left-color: var(--secondary);">
        <h3>🏛️ Optimal College Matches</h3>
        <div class="college-recs" id="outColleges"></div>
      </div>

      <div class="r-section flag-box" id="flagsContainer">
        <h3>⚠️ Clinical Risk Flags</h3>
        <div id="outFlags"></div>
      </div>
    </div>

    <div class="btn-wrapper" style="justify-content: center; gap: 15px;">
      <button class="btn-main" id="pdfBtn" onclick="downloadPDF()">📄 Export Dossier</button>
      <button class="btn-main btn-back" onclick="location.reload()">↺ Retake</button>
    </div>
  </div>
</div>

<script>
  // --- MULTI CAREER TEMPLATE DATABASE (Data-Driven Eligibility) ---
  const careerDB = [
    { id: "engineering", name: "Engineering & Technology", riasec: { R:0.25, I:0.35, A:0.05, S:0.05, E:0.10, C:0.20 }, resilienceNeed: 70, valueMatch: ["Fast growth opportunities","High income"], reqStream: ["PCM"] },
    { id: "medicine", name: "Medicine & Healthcare", riasec: { R:0.10, I:0.35, A:0.05, S:0.30, E:0.05, C:0.15 }, resilienceNeed: 85, valueMatch: ["Helping society","Prestige/status"], reqStream: ["PCB"] },
    { id: "design", name: "Creative Design & Media", riasec: { R:0.05, I:0.10, A:0.45, S:0.10, E:0.15, C:0.15 }, resilienceNeed: 60, valueMatch: ["Creativity","Independence"] },
    { id: "business", name: "Business & Entrepreneurship", riasec: { R:0.05, I:0.10, A:0.10, S:0.15, E:0.45, C:0.15 }, resilienceNeed: 75, valueMatch: ["High income","Fast growth opportunities"] },
    { id: "psychology", name: "Psychology & Human Services", riasec: { R:0.05, I:0.25, A:0.10, S:0.40, E:0.10, C:0.10 }, resilienceNeed: 70, valueMatch: ["Helping society","Work-life balance"] },
    { id: "finance", name: "Finance & Accounting", riasec: { R:0.05, I:0.20, A:0.05, S:0.05, E:0.25, C:0.40 }, resilienceNeed: 80, valueMatch: ["Job security","High income"], reqStream: ["Commerce", "PCM"] },
    { id: "appliedtech", name: "Applied Tech & Defence", riasec: { R:0.45, I:0.15, A:0.05, S:0.05, E:0.10, C:0.20 }, resilienceNeed: 80, valueMatch: ["Job security","Prestige/status"], reqStream: ["PCM", "PCB"] },
    { id: "law", name: "Law & Public Policy", riasec: { R:0.05, I:0.20, A:0.05, S:0.25, E:0.35, C:0.10 }, resilienceNeed: 85, valueMatch: ["Prestige/status","Helping society"] }
  ];

  // --- 75-QUESTION CLINICAL DATABASE ---
  const qBank = {
    riasec: [
      { id:'r1', text:'I enjoy building or repairing things.', cat:'R' }, { id:'r2', text:'I prefer hands-on tasks over theoretical study.', cat:'R' }, { id:'r3', text:'I like working outdoors.', cat:'R' }, { id:'r4', text:'I enjoy using tools or equipment.', cat:'R' }, { id:'r5', text:'I feel satisfied when I create something tangible.', cat:'R' }, { id:'r6', text:'I prefer practical activities over discussions.', cat:'R' },
      { id:'i1', text:'I enjoy solving complex problems.', cat:'I' }, { id:'i2', text:'I ask "why" and "how" frequently.', cat:'I' }, { id:'i3', text:'I enjoy science-based subjects.', cat:'I' }, { id:'i4', text:'I like analysing data or patterns.', cat:'I' }, { id:'i5', text:'I enjoy researching topics in depth.', cat:'I' }, { id:'i6', text:'I prefer logical reasoning over emotional decisions.', cat:'I' },
      { id:'a1', text:'I enjoy creative writing or storytelling.', cat:'A' }, { id:'a2', text:'I like drawing, designing, or visual expression.', cat:'A' }, { id:'a3', text:'I prefer flexible tasks over structured ones.', cat:'A' }, { id:'a4', text:'I enjoy music, performance, or media creation.', cat:'A' }, { id:'a5', text:'I think creatively when solving problems.', cat:'A' }, { id:'a6', text:'I dislike rigid rules.', cat:'A' },
      { id:'s1', text:'I enjoy helping others solve problems.', cat:'S' }, { id:'s2', text:'I feel fulfilled when supporting someone emotionally.', cat:'S' }, { id:'s3', text:'I like teaching or explaining concepts.', cat:'S' }, { id:'s4', text:'I am patient when listening to others.', cat:'S' }, { id:'s5', text:'I prefer people-oriented activities.', cat:'S' }, { id:'s6', text:'I feel motivated when my work benefits others.', cat:'S' },
      { id:'e1', text:'I enjoy leading group projects.', cat:'E' }, { id:'e2', text:'I like persuading or influencing others.', cat:'E' }, { id:'e3', text:'I am comfortable taking initiative.', cat:'E' }, { id:'e4', text:'I enjoy competitive environments.', cat:'E' }, { id:'e5', text:'I am interested in business or entrepreneurship.', cat:'E' }, { id:'e6', text:'I like taking calculated risks.', cat:'E' },
      { id:'c1', text:'I enjoy organising information.', cat:'C' }, { id:'c2', text:'I prefer structured instructions.', cat:'C' }, { id:'c3', text:'I like working with numbers and records.', cat:'C' }, { id:'c4', text:'I prefer predictable work environments.', cat:'C' }, { id:'c5', text:'I enjoy planning and scheduling.', cat:'C' }, { id:'c6', text:'I pay attention to small details.', cat:'C' }
    ],
    aptitude: [
      { id:'ap1', text:'I am confident in my mathematical ability.', cat:'APT' }, { id:'ap2', text:'I can understand logical problems quickly.', cat:'APT' }, { id:'ap3', text:'I communicate my thoughts clearly.', cat:'APT' }, { id:'ap4', text:'I remember information easily.', cat:'APT' }, { id:'ap5', text:'I can think in 3D or visualise objects well.', cat:'APT' }, { id:'ap6', text:'I manage time effectively.', cat:'APT' },
      { id:'ap7', text:'I stay focused for long periods.', cat:'APT' }, { id:'ap8', text:'I understand others’ emotions easily.', cat:'APT' }, { id:'ap9', text:'I am confident speaking in front of groups.', cat:'APT' }, { id:'ap10', text:'I solve problems systematically.', cat:'APT' }, { id:'ap11', text:'I learn new technical skills quickly.', cat:'APT' }, { id:'ap12', text:'I analyse mistakes and improve.', cat:'APT' }
    ],
    resilience: [
      { id:'rs1', text:'I handle academic pressure well.', cat:'RES', rev:false }, { id:'rs2', text:'I panic before important exams.', cat:'RES', rev:true }, { id:'rs3', text:'I continue working even after failure.', cat:'RES', rev:false }, { id:'rs4', text:'I give up easily when things are difficult.', cat:'RES', rev:true }, { id:'rs5', text:'I compare myself with others frequently.', cat:'RES', rev:true }, { id:'rs6', text:'I can manage long study hours.', cat:'RES', rev:false },
      { id:'rs7', text:'I recover quickly from disappointment.', cat:'RES', rev:false }, { id:'rs8', text:'I feel anxious about my future.', cat:'RES', rev:true }, { id:'rs9', text:'I stay calm during deadlines.', cat:'RES', rev:false }, { id:'rs10', text:'I seek help when overwhelmed.', cat:'RES', rev:false }, { id:'rs11', text:'I feel confident making decisions.', cat:'RES', rev:false }, { id:'rs12', text:'I overthink small mistakes.', cat:'RES', rev:true }
    ],
    maturity: [
      { id:'m1', text:'I clearly understand my strengths.', cat:'MAT', rev:false }, { id:'m2', text:'I am choosing a career mainly based on marks.', cat:'MAT', rev:true }, { id:'m3', text:'My parents strongly influence my career decisions.', cat:'PAR', rev:false },
      { id:'m4', text:'I have researched career pathways thoroughly.', cat:'MAT', rev:false }, { id:'m5', text:'I am open to exploring alternative options.', cat:'MAT', rev:false }, { id:'m6', text:'I feel confused about my career direction.', cat:'MAT', rev:true }, { id:'m7', text:'If marks were not important, I would choose a different career.', cat:'HIDDEN', rev:false }
    ],
    values: ['High income', 'Job security', 'Work-life balance', 'Prestige/status', 'Creativity', 'Helping society', 'Independence', 'Fast growth opportunities']
  };

  // --- STATE & ENGINE ---
  let state = { answers: {}, startTime: Date.now(), topValues: [], steps: [] };
  const emojis = ['😖', '😕', '😐', '🙂', '🤩'];

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
    
    // Step 0: Profile
    state.steps.push(`<div class="step-card active" id="step_0">
      <h2 class="step-title">Candidate Profile</h2><p class="step-sub">LEVEL 1 / 7</p>
      <div class="form-group"><label class="form-label">Full Name</label><input type="text" id="candName" class="form-input" placeholder="Enter your full name"></div>
      <div class="grid-2col">
        <div class="form-group"><label class="form-label">Current Grade / Level</label>
          <select id="qGrade" class="form-select">
            <option value="8-10">Grade 8 - 10</option><option value="11-12">Grade 11 - 12 (PUC)</option><option value="UG">Undergraduate</option>
          </select>
        </div>
        <div class="form-group"><label class="form-label">Target / Current Stream</label>
          <select id="qStream" class="form-select">
            <option value="PCM">Science (PCM/Tech)</option><option value="PCB">Science (PCB/Med)</option>
            <option value="Commerce">Commerce</option><option value="Arts">Arts / Humanities</option><option value="Undecided">Undecided</option>
          </select>
        </div>
      </div>
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

    // Step 6: Maturity & Reality Check
    state.steps.push(`<div class="step-card" id="step_6">
      <h2 class="step-title">Decision Maturity & Reality Check</h2>
      <p class="step-sub">LEVEL 7 / 7 • Final Step</p>
      
      ${buildLikertGrid(qBank.maturity)}
      
      <div style="margin-top: 30px; border-top: 1px solid var(--border); padding-top: 25px;">
        <h3 style="color: white; margin-bottom: 20px; font-size: 1.3rem;">Final Context Questions</h3>
        <div class="form-group">
            <label class="form-label">What career do your parents prefer for you?</label>
            <input type="text" id="qParent" class="form-input" placeholder="e.g. Doctor, Engineer, CA...">
        </div>
        <div class="form-group" style="margin-bottom:0;">
            <label class="form-label">If marks/society didn't matter, what career would you secretly choose?</label>
            <input type="text" id="qSecret" class="form-input" placeholder="e.g. Pilot, Musician, Artist...">
        </div>
      </div>

      <div class="btn-wrapper">
        <button class="btn-main btn-back" onclick="goPrev(6)">Back</button>
        <button class="btn-main" style="background:var(--success);" id="analyzeBtn" onclick="executeUIUpdate()">Compile Dossier ✨</button>
      </div>
    </div>`);

    wiz.innerHTML = state.steps.join('');
  }
  
  renderWizard();

  // --- INTERACTION LOGIC ---
  function setAns(id, val, btn, isRev, cat) {
    let p = btn.parentElement;
    Array.from(p.children).forEach(c => c.classList.remove('selected'));
    btn.classList.add('selected');
    let finalVal = isRev ? (6 - val) : val;
    state.answers[id] = { raw: val, calc: finalVal, cat: cat };
  }

  function moveValue(el, val) {
    const ranked = document.getElementById('vRanked');
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
    document.getElementById('progressBar').style.width = (((s+1) / 7) * 100) + '%';
    window.scrollTo({ top: 0, behavior: 'smooth' });
  }
  function goPrev(s) {
    document.getElementById(`step_${s}`).classList.remove('active');
    document.getElementById(`step_${s-1}`).classList.add('active');
    document.getElementById('progressBar').style.width = (((s-1) / 7) * 100) + '%';
    window.scrollTo({ top: 0, behavior: 'smooth' });
  }

  // --- SAFELY UPDATE DOM ---
  function updateElement(id, content, isHTML = false) {
    const el = document.getElementById(id);
    if(el) {
        if(isHTML) el.innerHTML = content;
        else el.innerText = content;
    }
  }

  // --- 1. PURE SCORING ENGINE ---
  function computeAssessment(data) {
    const { answers, topValues, startTime, grade, currentStream, parentCareer, secretCareer } = data;

    let riasecRaw = { R:0, I:0, A:0, S:0, E:0, C:0 };
    let metricsRaw = { APT:0, RES:0, MAT:0, PAR:0, HIDDEN:0 }; 

    for(let key in answers) {
      let ans = answers[key];
      if(['R','I','A','S','E','C'].includes(ans.cat)) riasecRaw[ans.cat] += ans.calc;
      else if(ans.cat) metricsRaw[ans.cat] += ans.calc;
    }

    // Normalization
    let scores = { 
      R: Math.max(0, Math.min(100, Math.round(((riasecRaw.R - 6) / 24) * 100))),
      I: Math.max(0, Math.min(100, Math.round(((riasecRaw.I - 6) / 24) * 100))),
      A: Math.max(0, Math.min(100, Math.round(((riasecRaw.A - 6) / 24) * 100))),
      S: Math.max(0, Math.min(100, Math.round(((riasecRaw.S - 6) / 24) * 100))),
      E: Math.max(0, Math.min(100, Math.round(((riasecRaw.E - 6) / 24) * 100))),
      C: Math.max(0, Math.min(100, Math.round(((riasecRaw.C - 6) / 24) * 100)))
    };

    let aptPct = Math.max(0, Math.min(100, Math.round(((metricsRaw.APT - 12) / 48) * 100)));
    let resPct = Math.max(0, Math.min(100, Math.round(((metricsRaw.RES - 12) / 48) * 100)));
    let matRaw = metricsRaw.MAT || 5;
    let matPct = Math.max(0, Math.min(100, Math.round(((matRaw - 5) / 20) * 100)));
    let parRaw = metricsRaw.PAR || 1; 
    let parPct = Math.max(0, Math.min(100, Math.round(((parRaw - 1) / 4) * 100)));
    
    let isHighPressure = parPct >= 70;

    // Reliability & Flags
    let timeTaken = (Date.now() - startTime) / 60000; 
    let relScore = 100;
    if(timeTaken < 7) relScore -= 20; 

    let allVals = Object.values(answers).map(a => a.raw);
    let variance = new Set(allVals).size;
    if (variance <= 2) relScore -= 15; 

    let flags = [];
    let hiddenScore = metricsRaw.HIDDEN || 1; 
    let hasParentConflict = (secretCareer && parentCareer && secretCareer !== parentCareer);
    let hasInternalConflict = (hiddenScore >= 4);
    
    if(isHighPressure) {
      flags.push(`<div class="flag-item"><span>🚩</span><span><strong>High External Pressure:</strong> Career choices appear heavily influenced by parental or societal expectations.</span></div>`);
    }
    
    // Decoupled Conflicts
    if(hasParentConflict) {
      flags.push(`<div class="flag-item"><span>🚩</span><span><strong>Parental Alignment Conflict:</strong> A significant mismatch exists between stated parental goals and true internal desires.</span></div>`);
      relScore -= 10; 
    } else if (hasInternalConflict) {
      flags.push(`<div class="flag-item"><span>🚩</span><span><strong>Internal Career Conflict:</strong> Student indicates they would choose a different path if marks/society were not factors.</span></div>`);
      relScore -= 5;
    }

    if(resPct < 50 && topValues.includes('High income')) {
      flags.push(`<div class="flag-item"><span>🚩</span><span><strong>Burnout Risk:</strong> High ambition combined with lower stress resilience. Requires coping strategy development.</span></div>`);
    }
    if(matPct < 50) {
      flags.push(`<div class="flag-item"><span>🚩</span><span><strong>Decision Confusion:</strong> Profile indicates significant uncertainty. Recommend exploratory internships before finalizing.</span></div>`);
    }
    if(flags.length === 0) flags.push(`<div style="color:var(--success); font-weight:bold;">✅ All clinical indicators are stable. No critical risks detected.</div>`);

    relScore = Math.max(0, Math.min(100, relScore));

    // Sort Traits
    const sorted = Object.keys(scores).sort((a,b) => scores[b] - scores[a]);
    const finalCode = sorted.slice(0,3).join('');
    const dom = sorted[0];
    const sec = sorted[1];
    const weakest = sorted[5];

    // Age Weightage Model
    let weightInterest = grade === "8-10" ? 0.50 : (grade === "11-12" ? 0.35 : 0.30);
    let weightAptitude = grade === "8-10" ? 0.30 : (grade === "11-12" ? 0.40 : 0.50);
    let weightResilience = grade === "11-12" ? 0.25 : 0.20;

    // Multi-Career Matching
    let careerScores = careerDB.map(career => {
      let interestScore = 0;
      for(let key in career.riasec){
        interestScore += scores[key] * career.riasec[key]; 
      }

      let finalScore = (interestScore * weightInterest) + (aptPct * weightAptitude) + (resPct * weightResilience);
      
      let resiliencePenalty = resPct < career.resilienceNeed ? -10 : 0;
      finalScore += resiliencePenalty;

      // Rank-Weighted Value Bonus
      let valueBonus = 0;
      topValues.forEach((v, index) => {
        if(career.valueMatch.includes(v)) {
          valueBonus += (5 - index) * 2; 
        }
      });
      finalScore += valueBonus;

      // Stream Penalty
      let streamPenalty = 0;
      if (currentStream !== "Undecided") {
           if (career.reqStream && !career.reqStream.includes(currentStream)) {
               streamPenalty = -30;
           }
      }
      finalScore += streamPenalty;

      return {
        name: career.name,
        score: Math.max(0, Math.min(100, Math.round(finalScore)))
      };
    });

    careerScores.sort((a,b) => b.score - a.score);
    let topCareers = careerScores.slice(0,5);
    let lowestCareers = careerScores.slice(-2);

    let topCareerScore = topCareers[0].score;
    let fitClassification = "";
    if(topCareerScore >= 85) fitClassification = "Strong Fit";
    else if(topCareerScore >= 70) fitClassification = "High Potential";
    else if(topCareerScore >= 55) fitClassification = "Moderate Fit";
    else fitClassification = "Conditional Fit";

    let profileDesc = "";
    if(scores[sorted[0]] >= 75 && scores[sorted[1]] < 65) profileDesc = `You show a <strong>Single Dominant</strong> orientation toward ${dom} tasks. You have intense, focused interests.`;
    else if(scores[sorted[0]] >= 70 && scores[sorted[1]] >= 70) profileDesc = `You have a <strong>Dual Dominant</strong> profile (${dom} & ${sec}). You combine these strengths uniquely.`;
    else if(scores[sorted[0]] < 60) profileDesc = `You have a <strong>Diffuse Interest Pattern</strong>. You are adaptable but may need more real-world exploration to find a specialized niche.`;
    else profileDesc = `You demonstrate a <strong>Balanced Exploratory Profile</strong>. You are versatile and can thrive in multi-disciplinary fields.`;

    if(aptPct < 50) profileDesc += ` <br><br><em>Note: As your aptitude confidence is currently moderate, your recommended fields will require dedicated skill-building.</em>`;

    return {
      scores, aptPct, resPct, matPct, parPct,
      relScore, flags,
      finalCode, dom, sec, weakest,
      topCareers, lowestCareers,
      fitClassification, profileDesc,
      overallFitScore: topCareerScore
    };
  }

  // --- 2. UI CONTROLLER ---
  function executeUIUpdate() {
    
    // STRICT VALIDATION
    const totalAnswered = Object.keys(state.answers).length;
    if(totalAnswered !== 67) {
      alert(`Incomplete Data! You have answered ${totalAnswered} out of 67 rating questions. Please complete all items before compiling the dossier.`);
      return;
    }
    
    const matCount = Object.values(state.answers).filter(a => a.cat === 'MAT').length;
    if(matCount < 5) {
      alert("Please complete the Decision Maturity rating section entirely.");
      return;
    }

    let btn = document.getElementById('analyzeBtn');
    if(btn) { btn.innerText = "Analyzing Psychometrics... ⏳"; btn.disabled = true; }

    const pBar = document.getElementById('progressBar');
    if(pBar) pBar.style.width = "100%";

    setTimeout(() => {
      confetti({ particleCount: 200, spread: 90, origin: { y: 0.5 } });

      // Gather DOM inputs safely
      const pEl = document.getElementById('qParent');
      const sEl = document.getElementById('qSecret');
      const gEl = document.getElementById('qGrade');
      const sCxt = document.getElementById('qStream');
      const cNameEl = document.getElementById('candName');

      const payload = {
          answers: state.answers,
          topValues: state.topValues,
          startTime: state.startTime,
          grade: gEl ? gEl.value : "8-10",
          currentStream: sCxt ? sCxt.value : "Undecided",
          parentCareer: pEl ? pEl.value.trim().toLowerCase() : "",
          secretCareer: sEl ? sEl.value.trim().toLowerCase() : ""
      };

      // RUN PURE ENGINE
      const report = computeAssessment(payload);

      // Mapping objects for UI text
      const matrixTitles = { 'I': "Investigative", 'A': "Artistic", 'E': "Enterprising", 'S': "Social", 'R': "Realistic", 'C': "Conventional" };
      const matrixAvoidMsg = {
        'I': 'Highly repetitive sales or clerical roles',
        'A': 'Rigid data-entry or heavy administrative jobs',
        'E': 'Isolated lab research or solitary backend coding',
        'S': 'Strictly mechanical environments without human contact',
        'R': 'Static office-only desk jobs',
        'C': 'Highly abstract or unpredictable creative roles'
      };

      // Inject UI
      updateElement('outName', (cNameEl && cNameEl.value) ? cNameEl.value : "Candidate");
      updateElement('outGrade', payload.grade);
      updateElement('outStreamContext', payload.currentStream);
      updateElement('outDate', new Date().toLocaleDateString());
      
      let relBadge = document.getElementById('outReliability');
      if(relBadge) {
          relBadge.innerText = `Reliability Index: ${report.relScore}%`;
          relBadge.style.background = report.relScore > 75 ? 'rgba(16, 185, 129, 0.2)' : 'rgba(245, 158, 11, 0.2)';
          relBadge.style.color = report.relScore > 75 ? 'var(--success)' : 'var(--warning)';
      }

      updateElement('outCode', report.finalCode);
      updateElement('outType', `Primary Trait: ${matrixTitles[report.dom]}`);
      updateElement('outPersonalityText', report.profileDesc, true);
      
      let careerHTML = report.topCareers.map(c => 
        `<div class="career-bar">
           <span style="font-weight:700; color:var(--text-dark);">${c.name}</span>
           <span class="career-score">${c.score}% Match</span>
         </div>`
      ).join('');

      let careerOutput = `${careerHTML} <span style="display:block; margin-top:15px; color:var(--secondary); font-size:0.95rem;"><strong>Top Compatibility Class: ${report.fitClassification}</strong></span>`;
      
      updateElement('outStream', `Primary Recommended Cluster: ${report.topCareers[0].name}`, true);
      updateElement('outCareers', careerOutput, true);
      
      let avoidHTML = `<strong>${report.lowestCareers.map(c => c.name).join(" & ")}</strong> <br><span style="font-size:0.95rem; font-weight:normal; color:#64748b; display:block; margin-top:5px;"><em>Primary Risk Factor: ${matrixAvoidMsg[report.weakest]}</em></span>`;
      updateElement('outAvoid', avoidHTML, true);
      
      updateElement('outFlags', report.flags.join(''), true);

      // Update Progress Bars safely
      const barApt = document.getElementById('bar-apt'); if(barApt) barApt.style.width = report.aptPct + '%'; 
      updateElement('txt-apt', report.aptPct + '%');
      
      const barRes = document.getElementById('bar-res'); if(barRes) barRes.style.width = report.resPct + '%'; 
      updateElement('txt-res', report.resPct + '%');
      
      const barMat = document.getElementById('bar-mat'); if(barMat) barMat.style.width = report.matPct + '%'; 
      updateElement('txt-mat', report.matPct + '%');
      
      const barPar = document.getElementById('bar-par'); if(barPar) barPar.style.width = report.parPct + '%'; 
      updateElement('txt-par', report.parPct + '% (' + (report.parPct > 70 ? 'HIGH' : 'Normal') + ')');

      // Dynamic Colleges
      const colDiv = document.getElementById('outColleges');
      if(colDiv) {
          colDiv.innerHTML = '';
          const sampleCols = [{n:"IISc Bangalore", r:['I']}, {n:"IIT Roorkee", r:['I','R']}, {n:"AAAD", r:['A']}, {n:"Christ University", r:['E','S','C']}, {n:"BMSCE", r:['R','I']}, {n:"Mount Carmel", r:['S','C']}];
          let matches = sampleCols.filter(c => c.r.includes(report.dom)).slice(0,2);
          if(matches.length===0) matches = [sampleCols[0], sampleCols[3]];
          matches.forEach(c => { colDiv.innerHTML += `<div class="rec-card"><h4>${c.n}</h4><p style="margin:0; font-size:0.9rem; color:#64748b;">Strong match for ${matrixTitles[report.dom]} profiles.</p></div>`; });
      }

      // UI Switch
      document.getElementById('wizardContainer').style.display = 'none';
      if (pBar) pBar.parentElement.style.display = 'none';
      document.getElementById('reportContainer').style.display = 'block';
      window.scrollTo(0,0);

      // Radar Chart Safely
      try {
        const canvas = document.getElementById('riasecChart');
        if (canvas) {
          const ctx = canvas.getContext('2d');
          if (window.rChart) window.rChart.destroy();
          window.rChart = new Chart(ctx, {
            type: 'radar',
            data: {
              labels: ['Realistic','Investigative','Artistic','Social','Enterprising','Conventional'],
              datasets: [{
                label: 'RIASEC Score',
                data: [report.scores.R, report.scores.I, report.scores.A, report.scores.S, report.scores.E, report.scores.C],
                backgroundColor: 'rgba(139, 92, 246, 0.4)',
                borderColor: '#8b5cf6',
                borderWidth: 2
              }]
            },
            options: {
              scales: { r: { max: 100, min: 0, ticks: { display: false } } },
              plugins: { legend: { display: false } }
            }
          });
        }
      } catch(e) {
        console.error("Chart failed:", e);
      }

    }, 400); 
  }

  function downloadPDF() {
    let btn = document.getElementById('pdfBtn');
    let orig = btn ? btn.innerText : "Exporting...";
    if(btn) btn.innerText = "Exporting Clinical PDF... ⏳";
    
    window.scrollTo(0,0);
    setTimeout(() => {
      const el = document.getElementById('reportContent');
      html2pdf().set({ 
        margin: 0.3, 
        filename: `Clinical_Report.pdf`, 
        image: { type: 'jpeg', quality: 1 }, 
        html2canvas: { scale: 2, useCORS: true, scrollY: 0 }, 
        jsPDF: { unit: 'in', format: 'a4', orientation: 'portrait' } 
      }).from(el).save().then(() => {
          if(btn) btn.innerText = orig;
      });
    }, 500);
  }
</script>
