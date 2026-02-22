---
layout: default
title: "Discover Your True Path 🚀"
permalink: /assessment/
description: "A context-aware, gamified career analysis that adapts to your current academic stream."
---

<script src="https://cdnjs.cloudflare.com/ajax/libs/html2pdf.js/0.10.1/html2pdf.bundle.min.js"></script>
<script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
<script src="https://cdn.jsdelivr.net/npm/canvas-confetti@1.6.0/dist/confetti.browser.min.js"></script>

<style>
  /* --- GEN-Z GAMIFIED UI THEME --- */
  :root {
    --bg-color: #0f172a;
    --card-bg: #1e293b;
    --primary: #8b5cf6;
    --secondary: #06b6d4;
    --accent: #f43f5e;
    --text-main: #f8fafc;
    --text-muted: #94a3b8;
    --border-color: #334155;
  }

  body { background-color: var(--bg-color); font-family: 'Nunito', 'Segoe UI', sans-serif; color: var(--text-main); margin: 0; }
  
  .assessment-header {
    background: linear-gradient(135deg, #1e1b4b 0%, #0f172a 100%);
    padding: 60px 20px 40px; text-align: center; 
    border-bottom: 2px solid var(--border-color); margin-bottom: 40px;
    position: relative; overflow: hidden;
  }
  .assessment-header::before {
    content: ''; position: absolute; top: -50%; left: -50%; width: 200%; height: 200%;
    background: radial-gradient(circle, rgba(139, 92, 246, 0.15) 0%, transparent 60%);
    z-index: 0; pointer-events: none;
  }
  .assessment-header h1 { margin: 0 0 10px 0; font-size: 3rem; font-weight: 900; background: -webkit-linear-gradient(45deg, var(--secondary), var(--primary)); -webkit-background-clip: text; -webkit-text-fill-color: transparent; position: relative; z-index: 1;}
  .assessment-header p { font-size: 1.2rem; color: var(--text-muted); max-width: 600px; margin: 0 auto; position: relative; z-index: 1;}

  .container { max-width: 900px; margin: 0 auto; padding: 0 20px; }

  /* FLOATING PROGRESS BAR */
  .progress-container { width: 100%; background: #0f172a; border-radius: 50px; height: 12px; margin-bottom: 40px; border: 2px solid var(--border-color); box-shadow: 0 0 15px rgba(139, 92, 246, 0.2); }
  .progress-bar { height: 100%; background: linear-gradient(90deg, var(--primary), var(--secondary)); width: 12.5%; transition: width 0.6s cubic-bezier(0.4, 0, 0.2, 1); border-radius: 50px; position: relative; }
  
  /* WIZARD CARDS */
  .step-card {
    background: rgba(30, 41, 59, 0.7); backdrop-filter: blur(10px);
    padding: 40px; border-radius: 24px; border: 1px solid rgba(255,255,255,0.1);
    box-shadow: 0 20px 40px rgba(0,0,0,0.4); margin-bottom: 40px;
    display: none; animation: slideUp 0.5s cubic-bezier(0.4, 0, 0.2, 1);
  }
  .step-card.active { display: block; }
  .step-title { font-size: 2rem; font-weight: 800; color: white; margin-bottom: 5px; text-align: center; }
  .step-sub { text-align: center; color: var(--secondary); margin-bottom: 35px; font-size: 1.1rem; font-weight: bold; text-transform: uppercase; letter-spacing: 1px; }

  /* INPUTS */
  .form-group { margin-bottom: 25px; }
  .form-label { display: block; font-weight: 700; margin-bottom: 10px; color: var(--text-muted); font-size: 1.1rem; }
  .form-input, .form-textarea {
    width: 100%; padding: 18px; border: 2px solid var(--border-color); border-radius: 16px;
    font-size: 1.1rem; color: white; background: #0f172a; transition: all 0.3s; font-family: inherit;
  }
  .form-input:focus, .form-textarea:focus { border-color: var(--primary); outline: none; box-shadow: 0 0 0 4px rgba(139, 92, 246, 0.2); }

  /* SCALES & GRIDS */
  .rating-grid { display: flex; flex-direction: column; gap: 15px; margin-bottom: 30px; }
  .rating-row {
    display: flex; align-items: center; justify-content: space-between;
    background: #0f172a; padding: 15px 20px; border-radius: 16px; border: 1px solid var(--border-color); transition: 0.3s;
  }
  .rating-row:hover { border-color: var(--primary); transform: translateX(5px); }
  @media (max-width: 768px) { .rating-row { flex-direction: column; align-items: flex-start; gap: 15px; } }
  .rating-label { font-weight: 700; font-size: 1.1rem; flex: 1; color: white; }
  .rating-options { display: flex; gap: 10px; background: #1e293b; padding: 5px; border-radius: 50px; }
  .rate-btn {
    width: 40px; height: 40px; border-radius: 50%; border: none;
    background: transparent; font-size: 1.5rem; cursor: pointer;
    display: flex; align-items: center; justify-content: center; transition: all 0.2s;
    filter: grayscale(100%) opacity(0.5);
  }
  .rate-btn:hover { filter: grayscale(0%) opacity(1); transform: scale(1.3); }
  .rate-btn.selected { filter: grayscale(0%) opacity(1); transform: scale(1.3); background: rgba(255,255,255,0.1); box-shadow: 0 0 15px rgba(255,255,255,0.2); }

  .options-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 15px; margin-bottom: 30px; }
  .option-card {
    border: 2px solid var(--border-color); border-radius: 16px; padding: 20px; cursor: pointer;
    transition: all 0.3s; background: #0f172a; display: flex; flex-direction: column; align-items: center; text-align: center;
  }
  .option-card:hover { border-color: var(--secondary); transform: translateY(-5px); }
  .option-card.selected { border-color: var(--primary); background: rgba(139, 92, 246, 0.1); box-shadow: 0 0 0 2px var(--primary); }
  .opt-icon { font-size: 2.5rem; margin-bottom: 10px; }
  .opt-title { font-weight: 800; color: white; font-size: 1.05rem; }

  .pill-grid { display: flex; flex-wrap: wrap; gap: 12px; justify-content: center; }
  .pill-tag {
    background: #0f172a; border: 2px solid var(--border-color); padding: 12px 24px; border-radius: 50px;
    font-weight: 700; color: var(--text-muted); cursor: pointer; transition: 0.2s; font-size: 1.05rem;
  }
  .pill-tag.selected { background: var(--accent); border-color: var(--accent); color: white; box-shadow: 0 8px 15px rgba(244, 63, 94, 0.4); }

  /* CONDITIONAL STREAM SECTION */
  #streamSelection { display: none; margin-top: 30px; border-top: 2px dashed var(--border-color); padding-top: 25px; animation: slideUp 0.3s; }

  /* BUTTONS */
  .btn-nav-wrapper { display: flex; justify-content: space-between; gap: 15px; margin-top: 30px; border-top: 1px solid var(--border-color); padding-top: 25px; }
  .btn-main {
    background: linear-gradient(45deg, var(--primary), #a855f7); color: white; border: none; padding: 16px 35px;
    font-size: 1.1rem; font-weight: 900; border-radius: 50px; cursor: pointer; flex-grow: 1; transition: 0.3s; text-transform: uppercase;
  }
  .btn-main:hover { transform: translateY(-3px); box-shadow: 0 10px 20px rgba(139, 92, 246, 0.3); }
  .btn-back { background: transparent; border: 2px solid var(--border-color); color: var(--text-muted); flex-grow: 0; }
  .btn-back:hover { background: var(--border-color); color: white; transform: translateY(0); }

  /* --- REPORT STYLES (Light theme for clean PDF export) --- */
  #reportContainer { display: none; }
  .report-card { background: white; padding: 40px; border-radius: 20px; box-shadow: 0 20px 50px rgba(0,0,0,0.5); margin-bottom: 40px; color: #1e293b; }
  .report-header { border-bottom: 2px solid #e2e8f0; padding-bottom: 20px; margin-bottom: 30px; text-align: center; }
  .report-header h2 { color: #0f172a; margin: 0 0 10px 0; font-size: 2.5rem; font-weight: 900;}
  .report-meta { color: #64748b; font-size: 1.1rem; font-weight: 600; }
  
  .badge-code { display: inline-block; background: var(--primary); color: white; padding: 10px 30px; border-radius: 50px; font-weight: 900; font-size: 1.8rem; margin-top: 20px; letter-spacing: 3px; }
  .chart-container { width: 100%; max-width: 500px; margin: 0 auto 30px auto; }
  
  .report-section { margin-bottom: 30px; padding: 25px; border-radius: 16px; background: #f8fafc; border-left: 6px solid var(--secondary); }
  .report-section h3 { color: #0f172a; font-size: 1.5rem; margin-top: 0; margin-bottom: 15px; font-weight: 800;}
  .report-section p { line-height: 1.8; font-size: 1.1rem; color: #334155; margin: 0 0 10px 0;}
  
  .avoid-section { background: #fff1f2; border-left-color: var(--accent); }
  .avoid-section h3 { color: #e11d48; }
  
  /* Context box */
  .context-box { background: #EBF4FF; border: 1px solid #c3dafe; padding: 15px; border-radius: 10px; margin-bottom: 15px; font-weight: 600; color: #2b6cb0; }

  .college-recs { display: flex; flex-wrap: wrap; gap: 20px; margin-top: 20px; }
  .rec-card { background: white; border: 2px solid #e2e8f0; padding: 20px; border-radius: 12px; width: calc(50% - 10px); box-sizing: border-box; }
  .rec-card h4 { margin: 0 0 8px 0; color: var(--primary); font-size: 1.2rem; font-weight: 800; }

  @keyframes slideUp { from { opacity: 0; transform: translateY(30px) scale(0.95); } to { opacity: 1; transform: translateY(0) scale(1); } }
  
  @media print {
    body { background: white; }
    .actions, .assessment-header, .progress-container { display: none !important; }
    .report-card { box-shadow: none; border: none; padding: 0; border-top: none; }
    .report-section { page-break-inside: avoid; border: 1px solid #e2e8f0; }
    .rec-card { width: 100%; margin-bottom: 15px; } 
  }
</style>

<div class="assessment-header">
  <h1>Unlock Your Potential 🎮</h1>
  <p>Your brain is wired differently. Let's find out how.</p>
</div>

<div class="container">
  <div class="progress-container"><div class="progress-bar" id="progressBar"></div></div>

  <div id="wizardContainer">
    
    <div class="step-card active" id="step1">
      <h2 class="step-title">Create Your Character</h2>
      <p class="step-sub">LEVEL 1 / 7</p>
      
      <div class="form-group">
        <label class="form-label">Player Name:</label>
        <input type="text" id="studentName" class="form-input" placeholder="e.g. Alex Johnson">
      </div>
      
      <div class="form-group">
        <label class="form-label">Current Academic Stage:</label>
        <div class="options-grid">
          <div class="option-card" onclick="selectRadio('qLevel', '8-10')"><div class="opt-icon">🏫</div><div class="opt-title">High School (8-10)</div></div>
          <div class="option-card" onclick="selectRadio('qLevel', 'PUC')"><div class="opt-icon">📚</div><div class="opt-title">PUC / 11th-12th</div></div>
          <div class="option-card" onclick="selectRadio('qLevel', 'UG')"><div class="opt-icon">🎓</div><div class="opt-title">Undergrad</div></div>
        </div>
      </div>

      <div id="streamSelection">
        <div class="form-label" style="color:var(--secondary);">Since you are in 11th+ or UG, what is your current stream?</div>
        <div class="options-grid" style="grid-template-columns: repeat(2, 1fr);">
          <div class="option-card" onclick="selectRadio('qStream', 'Sci-Math')"><div class="opt-icon">🚀</div><div class="opt-title">Science (PCM/Tech)</div></div>
          <div class="option-card" onclick="selectRadio('qStream', 'Sci-Bio')"><div class="opt-icon">🧬</div><div class="opt-title">Science (PCB/Med)</div></div>
          <div class="option-card" onclick="selectRadio('qStream', 'Commerce')"><div class="opt-icon">📈</div><div class="opt-title">Commerce / Biz</div></div>
          <div class="option-card" onclick="selectRadio('qStream', 'Arts')"><div class="opt-icon">🎨</div><div class="opt-title">Arts / Humanities</div></div>
        </div>
      </div>

      <button class="btn-main" style="width:100%; margin-top:20px;" onclick="validateStep1()">Start Quest ➔</button>
    </div>

    <div class="step-card" id="step2">
      <h2 class="step-title">The Academic Arena</h2>
      <p class="step-sub">LEVEL 2 / 7 • Vibe Check on Subjects</p>
      
      <div class="rating-grid">
        <script>
          const subjects = [
            { id: 'sub_math', label: 'Mathematics 🧮', type: 'I_C' },
            { id: 'sub_phy', label: 'Physics ⚛️', type: 'I' },
            { id: 'sub_bio', label: 'Biology / Chem 🧬', type: 'I_S' },
            { id: 'sub_cs', label: 'Coding / Computers 💻', type: 'I_R' },
            { id: 'sub_eng', label: 'Literature / Stories 📖', type: 'A' },
            { id: 'sub_bus', label: 'Business / Econ 📈', type: 'E_C' },
            { id: 'sub_art', label: 'Art / Design 🎨', type: 'A' }
          ];
          const emojis = ['😖', '😕', '😐', '🙂', '🤩'];
          subjects.forEach(sub => {
            document.write(`
              <div class="rating-row" data-category="${sub.type}">
                <div class="rating-label">${sub.label}</div>
                <div class="rating-options">
                  ${[1,2,3,4,5].map(n => `<div class="rate-btn" onclick="setRating(this, '${sub.id}', ${n})" title="${n}/5">${emojis[n-1]}</div>`).join('')}
                </div>
              </div>
            `);
          });
        </script>
      </div>
      <div class="btn-nav-wrapper"><button class="btn-main btn-back" onclick="prevStep(1)">Back</button><button class="btn-main" onclick="nextStep(3)">Next Level ➔</button></div>
    </div>

    <div class="step-card" id="step3">
      <h2 class="step-title">Free Time Mini-Games</h2>
      <p class="step-sub">LEVEL 3 / 7 • What do you actually enjoy?</p>
      <div class="rating-grid">
        <script>
          const acts1 = [
            { id: 'act_puzzle', label: 'Solving puzzles / Strategy games 🧩', type: 'I' },
            { id: 'act_fix', label: 'Taking gadgets apart to see inside 🔧', type: 'R_I' },
            { id: 'act_draw', label: 'Sketching, painting, or video editing 🖌️', type: 'A' },
            { id: 'act_lead', label: 'Being the captain of a team or club 👑', type: 'E' },
            { id: 'act_help', label: 'Listening to friends & giving advice ❤️', type: 'S' },
            { id: 'act_org', label: 'Planning trips and making schedules 📅', type: 'C' }
          ];
          acts1.forEach(act => {
            document.write(`
              <div class="rating-row" data-category="${act.type}">
                <div class="rating-label">${act.label}</div>
                <div class="rating-options">
                  ${[1,2,3,4,5].map(n => `<div class="rate-btn" onclick="setRating(this, '${act.id}', ${n})" title="${n}/5">${emojis[n-1]}</div>`).join('')}
                </div>
              </div>
            `);
          });
        </script>
      </div>
      <div class="btn-nav-wrapper"><button class="btn-main btn-back" onclick="prevStep(2)">Back</button><button class="btn-main" onclick="nextStep(4)">Next Level ➔</button></div>
    </div>

    <div class="step-card" id="step4">
      <h2 class="step-title">Your Inner Mechanics</h2>
      <p class="step-sub">LEVEL 4 / 7 • How does your brain operate?</p>
      
      <div class="form-group"><div class="form-label">When making a tough decision, I rely on:</div>
        <div class="options-grid">
          <div class="option-card" onclick="selectRadio('p_decide', 'I_C')"><div class="opt-icon">🤖</div><div class="opt-title">Pure Logic</div></div>
          <div class="option-card" onclick="selectRadio('p_decide', 'S_A')"><div class="opt-icon">❤️</div><div class="opt-title">Gut Feelings</div></div>
        </div>
      </div>
      <div class="form-group"><div class="form-label">I prefer tasks that are:</div>
        <div class="options-grid">
          <div class="option-card" onclick="selectRadio('p_task', 'C')"><div class="opt-icon">📏</div><div class="opt-title">Structured</div></div>
          <div class="option-card" onclick="selectRadio('p_task', 'A')"><div class="opt-icon">🌊</div><div class="opt-title">Open-ended</div></div>
        </div>
      </div>
      <div class="btn-nav-wrapper"><button class="btn-main btn-back" onclick="prevStep(3)">Back</button><button class="btn-main" onclick="nextStep(5)">Next Level ➔</button></div>
    </div>

    <div class="step-card" id="step5">
      <h2 class="step-title">Choose Your Map</h2>
      <p class="step-sub">LEVEL 5 / 7 • Where do you want to spawn every day?</p>
      <div class="rating-grid">
        <script>
          const envs = [
            { id: 'env_desk', label: 'Quiet corporate desk / Stable Office 📁', type: 'C' },
            { id: 'env_out', label: 'Outdoors, traveling, or on a site 🏗️', type: 'R' },
            { id: 'env_hosp', label: 'Hospital or community centre 🏥', type: 'S' },
            { id: 'env_lab', label: 'High-tech lab or research facility 🔬', type: 'I' },
            { id: 'env_bus', label: 'Fast-paced business boardroom 👔', type: 'E' },
            { id: 'env_free', label: 'Creative design studio or freelancing 🎬', type: 'A' }
          ];
          envs.forEach(env => {
            document.write(`
              <div class="rating-row" data-category="${env.type}">
                <div class="rating-label">${env.label}</div>
                <div class="rating-options">
                  ${[1,2,3,4,5].map(n => `<div class="rate-btn" onclick="setRating(this, '${env.id}', ${n})" title="${n}/5">${emojis[n-1]}</div>`).join('')}
                </div>
              </div>
            `);
          });
        </script>
      </div>
      <div class="btn-nav-wrapper"><button class="btn-main btn-back" onclick="prevStep(4)">Back</button><button class="btn-main" onclick="nextStep(6)">Next Level ➔</button></div>
    </div>

    <div class="step-card" id="step6">
      <h2 class="step-title">Equip Your Skills</h2>
      <p class="step-sub">LEVEL 6 / 7 • Select your top 4 natural buffs.</p>
      <div class="pill-grid" id="strengthsGrid">
        <div class="pill-tag" onclick="toggleStrength(this, 'C')">Good Memory 🧠</div>
        <div class="pill-tag" onclick="toggleStrength(this, 'I')">Problem Solving 🔍</div>
        <div class="pill-tag" onclick="toggleStrength(this, 'A')">Creativity 🎨</div>
        <div class="pill-tag" onclick="toggleStrength(this, 'S')">Empathy 🫂</div>
        <div class="pill-tag" onclick="toggleStrength(this, 'E')">Public Speaking 🎤</div>
        <div class="pill-tag" onclick="toggleStrength(this, 'E')">Leadership 👑</div>
        <div class="pill-tag" onclick="toggleStrength(this, 'R')">Physical Stamina 🏃</div>
        <div class="pill-tag" onclick="toggleStrength(this, 'C')">Discipline ⏳</div>
      </div>
      <div class="btn-nav-wrapper"><button class="btn-main btn-back" onclick="prevStep(5)">Back</button><button class="btn-main" onclick="nextStep(7)">Final Boss ➔</button></div>
    </div>

    <div class="step-card" id="step7">
      <h2 class="step-title">The Secret Override 🤫</h2>
      <p class="step-sub">LEVEL 7 / 7 • Time to be brutally honest.</p>
      <div class="form-group"><label class="form-label">What career do your parents want you to do?</label><input type="text" id="parentCareer" class="form-input" placeholder="e.g., Doctor, Engineer, CA..."></div>
      <div class="form-group"><label class="form-label">If society didn't judge, what is your secret dream job?</label><input type="text" id="secretCareer" class="form-input" placeholder="e.g., Pilot, Musician, Gamer, Actor..."></div>
      <div class="btn-nav-wrapper"><button class="btn-main btn-back" onclick="prevStep(6)">Back</button><button class="btn-main" style="background: var(--accent);" id="analyzeBtn" onclick="generateRIASECReport()">Decode My Brain ✨</button></div>
    </div>

  </div>

  <div id="reportContainer">
    <div class="report-card" id="reportContent">
      <div class="report-header">
        <h2>Career Mapping Dossier</h2>
        <div class="report-meta">
          <strong><span id="outName"></span></strong> | <span id="outLevel"></span><br>
          <span style="font-size: 0.9rem; font-weight:normal;">Generated on: <span id="outDate"></span></span>
        </div>
        <div class="badge-code" id="outCode">ISR</div>
      </div>

      <div class="chart-container"><canvas id="riasecChart"></canvas></div>

      <div class="report-section">
        <h3>🧠 Your Personality Profile</h3>
        <p id="outPersonalityText"></p>
      </div>

      <div class="report-section" style="border-left-color: var(--primary);">
        <h3>🎯 Context-Aware Career Path</h3>
        <div class="context-box" id="contextBox"></div>
        <p style="font-size:1.2rem; font-weight:800; color:var(--primary); margin-bottom: 5px;" id="outStream"></p>
        <p><strong>Top Career Matches:</strong> <span id="outCareers"></span></p>
      </div>

      <div class="report-section avoid-section">
        <h3>⚠️ Danger Zones to Avoid</h3>
        <p>Based on your wiring, you may experience burnout in these environments:</p>
        <p><strong id="outAvoid"></strong></p>
      </div>

      <div class="report-section" style="border-left-color: var(--secondary);">
        <h3>🏛️ Top College Basecamps</h3>
        <p>Based on our directory, here are excellent institutions for your profile:</p>
        <div class="college-recs" id="outColleges"></div>
      </div>
    </div>

    <div class="actions">
      <button class="btn-main" id="pdfBtn" onclick="downloadPDF()">📄 Download PDF Dossier</button>
      <button class="btn-main btn-back" style="margin-left: 10px; border-color:white; color:white;" onclick="location.reload()">↺ Retake Quiz</button>
    </div>
  </div>
</div>

<script>
  let state = { ratings: {}, radios: {}, strengths: [] };
  let totalSteps = 7;
  let radarChartInstance = null;

  // HANDLE DYNAMIC STREAM DROPDOWN
  function selectRadio(group, val) {
    state.radios[group] = val;
    const cards = event.currentTarget.parentElement.querySelectorAll('.option-card');
    cards.forEach(c => c.classList.remove('selected'));
    event.currentTarget.classList.add('selected');

    if(group === 'qLevel') {
      const streamDiv = document.getElementById('streamSelection');
      if(val === 'PUC' || val === 'UG') {
        streamDiv.style.display = 'block';
      } else {
        streamDiv.style.display = 'none';
        delete state.radios['qStream']; // reset if they go back to 8-10
      }
    }
  }

  function validateStep1() {
    if(!state.radios['qLevel']) return alert("Please select your academic stage.");
    if((state.radios['qLevel'] === 'PUC' || state.radios['qLevel'] === 'UG') && !state.radios['qStream']) {
      return alert("Please select your current stream to continue.");
    }
    nextStep(2);
  }

  function setRating(btn, id, value) {
    const parent = btn.parentElement;
    Array.from(parent.children).forEach(b => b.classList.remove('selected'));
    btn.classList.add('selected');
    const category = parent.parentElement.dataset.category;
    state.ratings[id] = { value: value, category: category };
  }

  function toggleStrength(card, val) {
    if(card.classList.contains('selected')) {
      card.classList.remove('selected');
      state.strengths = state.strengths.filter(s => s !== val);
    } else {
      if(state.strengths.length >= 4) return;
      card.classList.add('selected');
      state.strengths.push(val);
    }
  }

  function nextStep(step) {
    document.querySelectorAll('.step-card').forEach(c => c.classList.remove('active'));
    document.getElementById('step' + step).classList.add('active');
    document.getElementById('progressBar').style.width = ((step / totalSteps) * 100) + '%';
    window.scrollTo({ top: 0, behavior: 'smooth' });
  }
  function prevStep(step) { nextStep(step); }

  // THE CONTEXT-AWARE MATRIX
  const careerMatrix = {
    'I': { 
      '8-10': { p: 'Science (PCM or PCB)', c: 'Engineering, Medicine, Research, Data Science, AI' },
      'Sci-Math': { p: 'Core Tech & Research', c: 'Software Engineering, AI/ML, Data Science, Astrophysics' },
      'Sci-Bio': { p: 'Medical & Life Sciences', c: 'Medicine (MBBS), Biotechnology, Forensics, Pharmacy' },
      'Commerce': { p: 'Quantitative Commerce', c: 'Data Analytics, Financial Forensics, Economics Research' },
      'Arts': { p: 'Behavioral & Social Research', c: 'UX Research, Market Research, Psychology, Policy Analysis' }
    },
    'A': { 
      '8-10': { p: 'Humanities / Arts / Design', c: 'Design, Architecture, UX/UI, Filmmaking' },
      'Sci-Math': { p: 'Technical Design', c: 'Architecture (B.Arch), Product Design, Game Design, UI/UX' },
      'Sci-Bio': { p: 'Biological Design', c: 'Medical Illustration, Biomimicry Design, Conservation Architecture' },
      'Commerce': { p: 'Creative Business', c: 'Advertising, Brand Management, Marketing Communications' },
      'Arts': { p: 'Pure Creative Arts', c: 'Fine Arts, Journalism, Filmmaking, Fashion Design, Literature' }
    },
    'E': { 
      '8-10': { p: 'Commerce / Management', c: 'Business, Law, MBA, Sales, Entrepreneurship' },
      'Sci-Math': { p: 'Tech Leadership', c: 'Tech Entrepreneurship, Engineering Management, Patent Law' },
      'Sci-Bio': { p: 'Healthcare Leadership', c: 'Hospital Management, Pharma Sales, Healthcare Admin' },
      'Commerce': { p: 'Corporate Leadership', c: 'Investment Banking, Corporate Law, MBA, Venture Capital' },
      'Arts': { p: 'Public Leadership & Media', c: 'Corporate Law, Media Management, Political Science, Journalism' }
    },
    'S': { 
      '8-10': { p: 'Humanities / Psychology', c: 'Psychology, Teaching, Counselling, HR' },
      'Sci-Math': { p: 'Tech Education & Ergonomics', c: 'EdTech Development, Human-Computer Interaction, Science Teaching' },
      'Sci-Bio': { p: 'Patient Care & Therapy', c: 'Medicine, Nursing, Clinical Psychology, Nutrition/Dietetics' },
      'Commerce': { p: 'Corporate People Management', c: 'HR Management, Public Relations, Wealth Advising, CSR' },
      'Arts': { p: 'Social Sciences', c: 'Counseling, Social Work, NGO Management, Education' }
    },
    'R': { 
      '8-10': { p: 'Science / Applied Tech', c: 'Defence, Aviation, Mechanical Fields, Sports' },
      'Sci-Math': { p: 'Applied Engineering', c: 'Mechanical Engg, Civil Engg, Aviation, Defence (NDA)' },
      'Sci-Bio': { p: 'Physical Sciences', c: 'Physiotherapy, Sports Medicine, Dental, Agriculture' },
      'Commerce': { p: 'Operations & Logistics', c: 'Retail Management, Logistics & Supply Chain, Event Operations' },
      'Arts': { p: 'Applied Arts & Hospitality', c: 'Hotel Management, Culinary Arts, Sports Management' }
    },
    'C': { 
      '8-10': { p: 'Commerce / Finance', c: 'CA, Banking, Accounting, Government Exams' },
      'Sci-Math': { p: 'Tech Systems & Quality', c: 'Data Architecture, Quality Assurance, IT Systems Management' },
      'Sci-Bio': { p: 'Medical Administration', c: 'Medical Records, Lab Management, Clinical Data Management' },
      'Commerce': { p: 'Core Finance', c: 'Chartered Accountancy, CS, Actuary, Tax Consulting' },
      'Arts': { p: 'Public Administration', c: 'Public Admin, Archivist, Legal Assistant, Gov Services' }
    }
  };

  function generateRIASECReport() {
    let btn = document.getElementById('analyzeBtn');
    btn.innerText = "Decoding Brain Waves... 🧠";
    
    setTimeout(() => {
      confetti({ particleCount: 150, spread: 70, origin: { y: 0.6 }, colors: ['#8b5cf6', '#06b6d4', '#f43f5e'] });

      let scores = { R: 0, I: 0, A: 0, S: 0, E: 0, C: 0 };

      for (let key in state.ratings) {
        let item = state.ratings[key];
        let cats = item.category.split('_');
        cats.forEach(c => { if(item.value >= 4) scores[c] += (item.value - 3) * 2; });
      }

      for (let key in state.radios) {
        if(key === 'qLevel' || key === 'qStream') continue;
        let cats = state.radios[key].split('_');
        cats.forEach(c => scores[c] += 3);
      }
      state.strengths.forEach(c => scores[c] += 2);

      const parent = document.getElementById('parentCareer').value.toLowerCase();
      const secret = document.getElementById('secretCareer').value.toLowerCase();
      if (secret && parent && secret !== parent) {
        let topCode = Object.keys(scores).reduce((a, b) => scores[a] > scores[b] ? a : b);
        scores[topCode] = Math.round(scores[topCode] * 1.5);
      }
      for(let k in scores) { if(scores[k] < 0) scores[k] = 0; }

      const sorted = Object.keys(scores).sort((a,b) => scores[b] - scores[a]);
      const finalCode = sorted.slice(0,3).join('');
      const dominant = sorted[0];

      // Base descriptions
      const baseInfo = {
        'I': { title: "The Investigative Thinker", text: "You are a curious learner who enjoys logic and problem solving.", avoid: "Highly sales-based careers", col: [{n:"IISc Bangalore", d:"#1 for Research"}, {n:"IIT Roorkee", d:"Top Engineering & AI"}] },
        'A': { title: "The Artistic Creator", text: "You thrive in creative expression and visual/spatial tasks. You need flexibility.", avoid: "Repetitive administrative jobs", col: [{n:"AAAD Bangalore", d:"Specialized Architecture"}, {n:"GSAP", d:"Design Focus"}] },
        'E': { title: "The Enterprising Leader", text: "You are a natural leader driven by results, influence, and growth.", avoid: "Isolated lab research", col: [{n:"Christ University", d:"Top tier BBA/MBA"}, {n:"NMIMS Law", d:"Premier Law School"}] },
        'S': { title: "The Social Helper", text: "You are driven by empathy and collaboration. You excel in emotional intelligence.", avoid: "Strictly mechanical environments", col: [{n:"Mount Carmel College", d:"Excellence in Humanities"}, {n:"St. Joseph's", d:"Arts & Sciences"}] },
        'R': { title: "The Realistic Builder", text: "You enjoy hands-on, practical work in field-based or technical environments.", avoid: "Static office-only desk jobs", col: [{n:"AIT Chikkamagaluru", d:"Hands-on Robotics"}, {n:"BMSCE", d:"Core Mechanical"}] },
        'C': { title: "The Conventional Organizer", text: "You are highly detail-oriented and excel with structured data.", avoid: "Highly unpredictable creative roles", col: [{n:"Christ University", d:"Commerce Programs"}, {n:"Mount Carmel", d:"Accounting"}] }
      };

      const res = baseInfo[dominant];
      
      // CONTEXT AWARE LOGIC
      let level = state.radios['qLevel'];
      let streamContext = state.radios['qStream'] || '8-10';
      let pathway = careerMatrix[dominant][streamContext];

      // Populate Report
      document.getElementById('outName').innerText = document.getElementById('studentName').value || "Awesome Student";
      
      let lvlText = level === '8-10' ? "Class 8-10" : `${level} (${streamContext.replace('Sci-Math', 'Science-PCM').replace('Sci-Bio', 'Science-PCB')})`;
      document.getElementById('outLevel').innerText = lvlText;
      
      document.getElementById('outDate').innerText = new Date().toLocaleDateString();
      document.getElementById('outCode').innerText = finalCode;
      document.getElementById('outPersonalityText').innerText = res.text;
      
      // Inject the context box
      const ctxBox = document.getElementById('contextBox');
      if (level !== '8-10') {
        ctxBox.style.display = "block";
        ctxBox.innerHTML = `💡 Since you are currently in <strong>${streamContext.replace('-', ' ')}</strong>, you can channel your inner <strong>${res.title}</strong> directly into these fields without starting over!`;
      } else {
        ctxBox.style.display = "none";
      }

      document.getElementById('outStream').innerText = pathway.p;
      document.getElementById('outCareers').innerText = pathway.c;
      document.getElementById('outAvoid').innerText = res.avoid;

      const collDiv = document.getElementById('outColleges');
      collDiv.innerHTML = '';
      res.col.forEach(c => { collDiv.innerHTML += `<div class="rec-card"><h4>${c.n}</h4><p>${c.d}</p></div>`; });

      // Chart
      const ctx = document.getElementById('riasecChart').getContext('2d');
      if(radarChartInstance) radarChartInstance.destroy();
      radarChartInstance = new Chart(ctx, {
        type: 'radar',
        data: {
          labels: ['Realistic', 'Investigative', 'Artistic', 'Social', 'Enterprising', 'Conventional'],
          datasets: [{ label: 'Brain Stats', data: [scores.R, scores.I, scores.A, scores.S, scores.E, scores.C], backgroundColor: 'rgba(139, 92, 246, 0.4)', borderColor: '#8b5cf6', borderWidth: 3 }]
        },
        options: { scales: { r: { ticks: { display: false } } }, plugins: { legend: { display: false } } }
      });

      document.getElementById('wizardContainer').style.display = 'none';
      document.querySelector('.progress-container').style.display = 'none';
      document.getElementById('reportContainer').style.display = 'block';
      window.scrollTo(0, 0);

    }, 800); 
  }

  function downloadPDF() {
    let btn = document.getElementById('pdfBtn');
    let originalText = btn.innerText;
    btn.innerText = "Forging PDF... ⏳";
    window.scrollTo(0,0);
    setTimeout(() => {
      const element = document.getElementById('reportContent');
      const name = document.getElementById('outName').innerText.replace(/\s+/g, '_');
      const opt = { margin: [0.3, 0.3, 0.3, 0.3], filename: `My_Dossier_${name}.pdf`, image: { type: 'jpeg', quality: 1 }, html2canvas: { scale: 2, useCORS: true, scrollY: 0 }, jsPDF: { unit: 'in', format: 'a4', orientation: 'portrait' } };
      html2pdf().set(opt).from(element).save().then(() => { btn.innerText = originalText; });
    }, 500); 
  }
</script>
