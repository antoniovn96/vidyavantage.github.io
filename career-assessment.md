---
layout: default
title: "The Ultimate Career Finder 🚀"
permalink: /assessment/
description: "Discover your true potential with our gamified RIASEC assessment. Includes visual personality mapping and college matching."
---

<script src="https://cdnjs.cloudflare.com/ajax/libs/html2pdf.js/0.10.1/html2pdf.bundle.min.js"></script>
<script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
<script src="https://cdn.jsdelivr.net/npm/canvas-confetti@1.6.0/dist/confetti.browser.min.js"></script>

<style>
  /* --- VIBRANT STUDENT THEME --- */
  :root {
    --bg-color: #F0F4F8;
    --primary: #6366F1; /* Indigo */
    --primary-dark: #4338CA;
    --secondary: #14B8A6; /* Teal */
    --accent: #F59E0B; /* Amber */
    --card-bg: #ffffff;
    --text-main: #1F2937;
    --font-family: 'Segoe UI', system-ui, sans-serif;
  }

  body { background-color: var(--bg-color); font-family: var(--font-family); color: var(--text-main); margin: 0; }
  
  /* HEADER WITH SHAPE DIVIDER */
  .hero-header {
    background: linear-gradient(135deg, var(--primary) 0%, #8B5CF6 100%);
    padding: 80px 20px 100px; text-align: center; color: white;
    clip-path: polygon(0 0, 100% 0, 100% 85%, 0 100%);
    margin-bottom: -40px;
  }
  .hero-header h1 { margin: 0; font-size: 3rem; font-weight: 800; letter-spacing: -1px; text-shadow: 0 4px 10px rgba(0,0,0,0.2); }
  .hero-header p { font-size: 1.25rem; opacity: 0.9; margin-top: 10px; font-weight: 500; }

  .container { max-width: 900px; margin: 0 auto; padding: 0 20px; position: relative; z-index: 10; }

  /* PROGRESS BAR */
  .progress-wrapper {
    background: white; padding: 15px 25px; border-radius: 50px;
    box-shadow: 0 10px 30px rgba(0,0,0,0.08); display: flex; align-items: center; gap: 15px;
    margin-bottom: 30px;
  }
  .progress-track { flex-grow: 1; background: #E5E7EB; height: 12px; border-radius: 20px; overflow: hidden; }
  .progress-fill { height: 100%; background: linear-gradient(90deg, var(--accent), #FBBF24); width: 10%; transition: width 0.5s ease; border-radius: 20px; }
  .step-count { font-weight: 800; color: var(--primary); font-size: 0.9rem; white-space: nowrap; }

  /* ANIMATED CARDS */
  .step-card {
    background: var(--card-bg); padding: 40px; border-radius: 24px;
    box-shadow: 0 20px 40px rgba(0,0,0,0.06); margin-bottom: 40px;
    display: none; animation: slideUp 0.6s cubic-bezier(0.16, 1, 0.3, 1);
    border: 1px solid rgba(255,255,255,0.5);
  }
  .step-card.active { display: block; }
  
  .step-title { font-size: 1.8rem; font-weight: 800; color: var(--primary); margin-bottom: 5px; text-align: center; }
  .step-subtitle { text-align: center; color: #6B7280; margin-bottom: 35px; font-size: 1.1rem; }

  /* EMOJI RATING ROWS */
  .rating-grid { display: flex; flex-direction: column; gap: 15px; }
  .rating-row {
    display: flex; align-items: center; justify-content: space-between;
    background: #F9FAFB; padding: 15px 20px; border-radius: 16px; border: 2px solid transparent;
    transition: 0.2s;
  }
  .rating-row:hover { border-color: #D1D5DB; background: white; transform: translateX(5px); }
  @media (max-width: 700px) { .rating-row { flex-direction: column; align-items: flex-start; gap: 10px; } }
  
  .rating-label { font-weight: 700; color: #374151; font-size: 1.05rem; }
  .emoji-scale { display: flex; gap: 8px; }
  .rate-btn {
    width: 42px; height: 42px; border-radius: 50%; background: white;
    border: 2px solid #E5E7EB; display: flex; align-items: center; justify-content: center;
    font-size: 1.4rem; cursor: pointer; transition: all 0.2s;
  }
  .rate-btn:hover { transform: scale(1.2) rotate(10deg); border-color: var(--secondary); }
  .rate-btn.selected { background: var(--secondary); border-color: var(--secondary); transform: scale(1.2); box-shadow: 0 5px 15px rgba(20, 184, 166, 0.3); }

  /* "THIS OR THAT" BIG CARDS */
  .binary-grid { display: grid; grid-template-columns: 1fr 1fr; gap: 20px; margin-bottom: 25px; }
  .binary-card {
    background: white; border: 2px solid #E5E7EB; border-radius: 20px; padding: 25px;
    text-align: center; cursor: pointer; transition: 0.3s;
  }
  .binary-card:hover { border-color: var(--primary); transform: translateY(-5px); box-shadow: 0 10px 25px rgba(99, 102, 241, 0.15); }
  .binary-card.selected { background: #EEF2FF; border-color: var(--primary); box-shadow: 0 0 0 3px rgba(99, 102, 241, 0.2); }
  .binary-icon { font-size: 2.5rem; display: block; margin-bottom: 10px; }
  .binary-text { font-weight: 800; color: #374151; font-size: 1.1rem; }

  /* LIFESTYLE PILLS */
  .pill-container { display: flex; flex-wrap: wrap; gap: 10px; justify-content: center; }
  .pill-select {
    background: white; border: 2px solid #E5E7EB; padding: 12px 24px; border-radius: 50px;
    font-weight: 700; color: #4B5563; cursor: pointer; transition: 0.2s; font-size: 1rem;
  }
  .pill-select:hover { border-color: var(--accent); color: var(--accent); }
  .pill-select.selected { background: var(--accent); border-color: var(--accent); color: white; box-shadow: 0 5px 15px rgba(245, 158, 11, 0.3); }

  /* TEXT INPUTS */
  .form-input {
    width: 100%; padding: 16px; border: 2px solid #E5E7EB; border-radius: 12px;
    font-size: 1rem; transition: 0.3s; background: #F9FAFB;
  }
  .form-input:focus { border-color: var(--primary); background: white; outline: none; }

  /* NAVIGATION BUTTONS */
  .nav-area { display: flex; justify-content: space-between; margin-top: 40px; padding-top: 20px; border-top: 2px dashed #E5E7EB; }
  .btn {
    padding: 14px 30px; border-radius: 50px; font-weight: 800; cursor: pointer; border: none; font-size: 1rem; transition: 0.3s;
  }
  .btn-next { background: var(--primary); color: white; flex-grow: 1; margin-left: 15px; box-shadow: 0 5px 15px rgba(99, 102, 241, 0.3); }
  .btn-next:hover { background: var(--primary-dark); transform: translateY(-2px); }
  .btn-back { background: #E5E7EB; color: #6B7280; }
  .btn-back:hover { background: #D1D5DB; }

  /* LOADING OVERLAY */
  #loadingOverlay {
    position: fixed; top: 0; left: 0; width: 100%; height: 100%;
    background: rgba(255,255,255,0.95); z-index: 100; display: none;
    align-items: center; justify-content: center; flex-direction: column;
  }
  .loader-text { font-size: 1.5rem; font-weight: 800; color: var(--primary); margin-top: 20px; animation: pulse 1.5s infinite; }

  /* REPORT CARD */
  #reportContainer { display: none; }
  .report-box { background: white; padding: 50px; border-radius: 20px; box-shadow: 0 20px 50px rgba(0,0,0,0.1); border-top: 10px solid var(--primary); }
  .chart-wrapper { max-width: 500px; margin: 30px auto; position: relative; }
  
  .report-section { 
    background: #F3F4F6; padding: 25px; border-radius: 16px; margin-bottom: 25px; 
    border-left: 6px solid var(--secondary);
  }
  .report-section h3 { margin-top: 0; color: var(--primary-dark); font-weight: 800; }
  .college-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); gap: 15px; margin-top: 15px; }
  .college-card-mini { background: white; padding: 15px; border-radius: 12px; border: 1px solid #E5E7EB; }
  .college-card-mini h4 { margin: 0 0 5px; color: var(--primary); }

  @keyframes slideUp { from { opacity: 0; transform: translateY(20px); } to { opacity: 1; transform: translateY(0); } }
  @keyframes pulse { 0% { opacity: 0.6; } 50% { opacity: 1; } 100% { opacity: 0.6; } }

  /* PDF Print Rules */
  @media print {
    body { background: white; }
    .hero-header, .progress-wrapper, .nav-area { display: none !important; }
    .report-box { box-shadow: none; padding: 0; border: none; }
    .report-section { break-inside: avoid; border: 1px solid #ddd; }
  }
</style>

<div class="hero-header">
  <h1>🚀 The Ultimate Career Finder</h1>
  <p>Stop guessing. Start analyzing. A data-backed roadmap for your future.</p>
</div>

<div class="container">
  
  <div class="progress-wrapper" id="progressBox">
    <div class="step-count">Step <span id="currentStepNum">1</span> of 8</div>
    <div class="progress-track"><div class="progress-fill" id="progressBar"></div></div>
  </div>

  <div id="wizard">
    
    <div class="step-card active" id="step1">
      <h2 class="step-title">Who are you? 🤔</h2>
      <p class="step-subtitle">Let's personalize your career dossier.</p>
      
      <div class="form-group">
        <label class="form-label">Full Name</label>
        <input type="text" id="studentName" class="form-input" placeholder="e.g. Aditi Sharma">
      </div>
      <div class="form-group">
        <label class="form-label">Current Academic Stage</label>
        <div class="pill-container">
          <div class="pill-select" onclick="selectSinglePill('qLevel', 'Class 8-10', this)">Class 8 - 10</div>
          <div class="pill-select" onclick="selectSinglePill('qLevel', 'PUC (11-12)', this)">PUC / 11th-12th</div>
          <div class="pill-select" onclick="selectSinglePill('qLevel', 'Undergraduate', this)">Undergraduate</div>
        </div>
      </div>
      <div class="nav-area">
        <div style="flex-grow:1"></div> <button class="btn btn-next" onclick="nextStep(2)">Start Engine ➔</button>
      </div>
    </div>

    <div class="step-card" id="step2">
      <h2 class="step-title">School Vibes 📚</h2>
      <p class="step-subtitle">Rate these subjects based on your *honest* enjoyment.</p>
      
      <div class="rating-grid">
        <script>
          const subjects = [
            { id: 'math', label: 'Maths & Logic 🧮', cat: 'I_C' },
            { id: 'sci', label: 'Physics / Chemistry ⚛️', cat: 'I' },
            { id: 'bio', label: 'Biology / Life Science 🧬', cat: 'I_S' },
            { id: 'art', label: 'Art / Design / Drama 🎨', cat: 'A' },
            { id: 'biz', label: 'Business / Economics 📈', cat: 'E_C' },
            { id: 'lit', label: 'English / History 📖', cat: 'S_A' },
            { id: 'code', label: 'Computer Science 💻', cat: 'R_I' }
          ];
          const emojis = ['😫','😕','😐','🙂','🤩'];
          subjects.forEach(s => {
            document.write(`
              <div class="rating-row" data-cat="${s.cat}">
                <div class="rating-label">${s.label}</div>
                <div class="emoji-scale">
                  ${[1,2,3,4,5].map(n => `<div class="rate-btn" onclick="setRating(this, '${s.id}', ${n})">${emojis[n-1]}</div>`).join('')}
                </div>
              </div>
            `);
          });
        </script>
      </div>
      <div class="nav-area">
        <button class="btn btn-back" onclick="prevStep(1)">Back</button>
        <button class="btn btn-next" onclick="nextStep(3)">Next ➔</button>
      </div>
    </div>

    <div class="step-card" id="step3">
      <h2 class="step-title">What lights you up? 🔥</h2>
      <p class="step-subtitle">Forget school for a second. What do you actually enjoy doing?</p>
      <div class="rating-grid">
        <script>
          const acts = [
            { id: 'puzzle', label: 'Solving riddles / Sudoku 🧩', cat: 'I' },
            { id: 'fix', label: 'Fixing broken things / Gadgets 🔧', cat: 'R' },
            { id: 'create', label: 'Writing stories / Editing videos 🎬', cat: 'A' },
            { id: 'lead', label: 'Leading a team / Debating 🎤', cat: 'E' },
            { id: 'help', label: 'Helping friends with problems 🤝', cat: 'S' },
            { id: 'plan', label: 'Making lists / Organizing trips 📅', cat: 'C' }
          ];
          acts.forEach(a => {
            document.write(`
              <div class="rating-row" data-cat="${a.cat}">
                <div class="rating-label">${a.label}</div>
                <div class="emoji-scale">
                  ${[1,2,3,4,5].map(n => `<div class="rate-btn" onclick="setRating(this, '${a.id}', ${n})">${emojis[n-1]}</div>`).join('')}
                </div>
              </div>
            `);
          });
        </script>
      </div>
      <div class="nav-area">
        <button class="btn btn-back" onclick="prevStep(2)">Back</button>
        <button class="btn btn-next" onclick="nextStep(4)">Next ➔</button>
      </div>
    </div>

    <div class="step-card" id="step4">
      <h2 class="step-title">The "You" Factor 🧠</h2>
      <p class="step-subtitle">Pick the one that sounds most like you.</p>
      
      <p class="form-label" style="text-align:center">I prefer to work:</p>
      <div class="binary-grid">
        <div class="binary-card" onclick="selectBinary('p_work', 'R_I_C', this)">
          <span class="binary-icon">🏝️</span>
          <span class="binary-text">Independently</span>
        </div>
        <div class="binary-card" onclick="selectBinary('p_work', 'S_E', this)">
          <span class="binary-icon">👯</span>
          <span class="binary-text">With People</span>
        </div>
      </div>

      <p class="form-label" style="text-align:center">I make decisions using:</p>
      <div class="binary-grid">
        <div class="binary-card" onclick="selectBinary('p_decide', 'I_C', this)">
          <span class="binary-icon">🤖</span>
          <span class="binary-text">Cold Logic</span>
        </div>
        <div class="binary-card" onclick="selectBinary('p_decide', 'S_A', this)">
          <span class="binary-icon">❤️</span>
          <span class="binary-text">Values & Feelings</span>
        </div>
      </div>

      <div class="nav-area">
        <button class="btn btn-back" onclick="prevStep(3)">Back</button>
        <button class="btn btn-next" onclick="nextStep(5)">Next ➔</button>
      </div>
    </div>

    <div class="step-card" id="step5">
      <h2 class="step-title">Future Lifestyle 🌍</h2>
      <p class="step-subtitle">What matters most to you in a career?</p>
      
      <div class="form-group">
        <label class="form-label">Top Priority (Choose 1)</label>
        <div class="pill-container">
          <div class="pill-select" onclick="selectSinglePill('life_pri', 'Wealth', this)">High Income 💰</div>
          <div class="pill-select" onclick="selectSinglePill('life_pri', 'Balance', this)">Work-Life Balance 🧘</div>
          <div class="pill-select" onclick="selectSinglePill('life_pri', 'Fame', this)">Social Respect 🌟</div>
          <div class="pill-select" onclick="selectSinglePill('life_pri', 'Creativity', this)">Creative Freedom 🎨</div>
        </div>
      </div>

      <div class="form-group">
        <label class="form-label">How long are you willing to study?</label>
        <div class="pill-container">
          <div class="pill-select" onclick="selectSinglePill('life_study', '3-4 Years', this)">3-4 Years (Standard)</div>
          <div class="pill-select" onclick="selectSinglePill('life_study', '5-6 Years', this)">5-6 Years (Masters)</div>
          <div class="pill-select" onclick="selectSinglePill('life_study', '8+ Years', this)">8+ Years (Doctor/PhD)</div>
        </div>
      </div>

      <div class="nav-area">
        <button class="btn btn-back" onclick="prevStep(4)">Back</button>
        <button class="btn btn-next" onclick="nextStep(6)">Next ➔</button>
      </div>
    </div>

    <div class="step-card" id="step6">
      <h2 class="step-title">Dream Office 🏢</h2>
      <p class="step-subtitle">Where do you see yourself working happily?</p>
      <div class="rating-grid">
        <script>
          const envs = [
            { id: 'e_corp', label: 'Corporate Office / Boardroom 👔', cat: 'E_C' },
            { id: 'e_field', label: 'Outdoors / Construction Site 🏗️', cat: 'R' },
            { id: 'e_lab', label: 'Science Lab / Research Center 🔬', cat: 'I' },
            { id: 'e_hosp', label: 'Hospital / Clinic 🏥', cat: 'S' },
            { id: 'e_studio', label: 'Art Studio / Flexible Space 🎨', cat: 'A' }
          ];
          envs.forEach(e => {
            document.write(`
              <div class="rating-row" data-cat="${e.cat}">
                <div class="rating-label">${e.label}</div>
                <div class="emoji-scale">
                  ${[1,2,3,4,5].map(n => `<div class="rate-btn" onclick="setRating(this, '${e.id}', ${n})">${emojis[n-1]}</div>`).join('')}
                </div>
              </div>
            `);
          });
        </script>
      </div>
      <div class="nav-area">
        <button class="btn btn-back" onclick="prevStep(5)">Back</button>
        <button class="btn btn-next" onclick="nextStep(7)">Next ➔</button>
      </div>
    </div>

    <div class="step-card" id="step7">
      <h2 class="step-title">Self-Perception 💪</h2>
      <p class="step-subtitle">Pick your top 3 natural strengths.</p>
      <div class="pill-container" id="strengthContainer">
        <div class="pill-select" onclick="toggleStrength(this, 'I')">Logical Thinking</div>
        <div class="pill-select" onclick="toggleStrength(this, 'A')">Creativity</div>
        <div class="pill-select" onclick="toggleStrength(this, 'S')">Empathy</div>
        <div class="pill-select" onclick="toggleStrength(this, 'E')">Leadership</div>
        <div class="pill-select" onclick="toggleStrength(this, 'C')">Discipline</div>
        <div class="pill-select" onclick="toggleStrength(this, 'R')">Physical Stamina</div>
      </div>

      <div class="form-group" style="margin-top:20px;">
        <label class="form-label">Which school subject do you wait for the most?</label>
        <input type="text" id="favSub" class="form-input" placeholder="e.g. History, PT, Physics...">
      </div>

      <div class="nav-area">
        <button class="btn btn-back" onclick="prevStep(6)">Back</button>
        <button class="btn btn-next" onclick="nextStep(8)">Final Step ➔</button>
      </div>
    </div>

    <div class="step-card" id="step8">
      <h2 class="step-title">The Truth Serum 🧪</h2>
      <p class="step-subtitle">This adjusts the AI to filter out external pressure.</p>
      
      <div class="form-group">
        <label class="form-label">What career do your parents want for you?</label>
        <input type="text" id="parentCareer" class="form-input" placeholder="e.g. Doctor, Engineer">
      </div>
      
      <div class="form-group">
        <label class="form-label">If money/society didn't matter, what would you be?</label>
        <input type="text" id="secretCareer" class="form-input" placeholder="e.g. Gamer, Chef, Pilot">
      </div>

      <div class="form-group">
        <label class="form-label">Who is your career role model?</label>
        <input type="text" id="roleModel" class="form-input" placeholder="e.g. Elon Musk, My Dad...">
      </div>

      <div class="nav-area">
        <button class="btn btn-back" onclick="prevStep(7)">Back</button>
        <button class="btn btn-next" style="background:var(--accent)" onclick="generateReport()">Analyze My Brain 🧠</button>
      </div>
    </div>

  </div>

  <div id="loadingOverlay">
    <div style="font-size: 3rem;">⚙️</div>
    <div class="loader-text">Mapping Neural Pathways...</div>
  </div>

  <div id="reportContainer">
    <div class="report-box" id="reportContent">
      <div style="text-align:center; padding-bottom: 20px; border-bottom: 2px dashed #E5E7EB; margin-bottom: 30px;">
        <h1 style="color:var(--primary); margin:0;">Career Dossier</h1>
        <p style="color:#6B7280; margin-top:5px;">Prepared for: <strong id="outName">Student</strong> | Level: <span id="outLevel"></span></p>
      </div>

      <div class="report-section">
        <h3>🧠 Your Career DNA (RIASEC Profile)</h3>
        <div class="chart-wrapper">
          <canvas id="radarChart"></canvas>
        </div>
        <p id="outPersonalityText"></p>
        <p><strong>Top Code:</strong> <span id="outCode" style="background:var(--accent); color:white; padding:2px 8px; border-radius:4px; font-weight:bold;"></span></p>
      </div>

      <div class="report-section">
        <h3>🎯 Recommended Path</h3>
        <p><strong>Ideal Stream:</strong> <span id="outStream"></span></p>
        <p><strong>Top Careers:</strong> <span id="outCareers"></span></p>
      </div>

      <div class="report-section" style="border-left-color: #EF4444; background: #FEF2F2;">
        <h3 style="color:#B91C1C;">⚠️ Environments to Avoid</h3>
        <p>Based on your low scores in certain areas, avoid these to prevent burnout:</p>
        <p id="outAvoid" style="font-weight:600; color:#7F1D1D;"></p>
      </div>

      <div class="report-section">
        <h3>🏛️ Top College Matches</h3>
        <div class="college-grid" id="outColleges"></div>
      </div>

      <div style="margin-top:30px; font-size:0.9rem; color:#6B7280; display:flex; justify-content:space-between;">
        <span><strong>Lifestyle Priority:</strong> <span id="outLife"></span></span>
        <span><strong>Role Model:</strong> <span id="outRole"></span></span>
      </div>
    </div>

    <div class="actions">
      <button class="btn btn-next" onclick="downloadPDF()">📄 Download Official PDF</button>
      <button class="btn btn-back" style="margin-left: 10px;" onclick="location.reload()">↺ Start Over</button>
    </div>
  </div>

</div>

<script>
  let state = {
    ratings: {},
    pills: {},
    strengths: [],
    scores: { R:0, I:0, A:0, S:0, E:0, C:0 }
  };
  let totalSteps = 8;

  // --- UI HANDLERS ---
  function setRating(btn, id, val) {
    const row = btn.closest('.rating-row');
    row.querySelectorAll('.rate-btn').forEach(b => b.classList.remove('selected'));
    btn.classList.add('selected');
    state.ratings[id] = { val: val, cat: row.dataset.cat };
  }

  function selectSinglePill(group, val, btn) {
    state.pills[group] = val;
    btn.parentElement.querySelectorAll('.pill-select').forEach(p => p.classList.remove('selected'));
    btn.classList.add('selected');
  }

  function selectBinary(group, val, card) {
    state.pills[group] = val;
    card.parentElement.querySelectorAll('.binary-card').forEach(c => c.classList.remove('selected'));
    card.classList.add('selected');
  }

  function toggleStrength(btn, cat) {
    if(btn.classList.contains('selected')) {
      btn.classList.remove('selected');
      state.strengths = state.strengths.filter(s => s !== cat);
    } else {
      if(state.strengths.length >= 3) return alert("Pick top 3 only!");
      btn.classList.add('selected');
      state.strengths.push(cat);
    }
  }

  // --- NAVIGATION ---
  function nextStep(n) {
    document.querySelector('.step-card.active').classList.remove('active');
    document.getElementById('step'+n).classList.add('active');
    document.getElementById('progressBar').style.width = ((n/totalSteps)*100) + '%';
    document.getElementById('currentStepNum').innerText = n;
    window.scrollTo(0,0);
  }
  function prevStep(n) { nextStep(n); }

  // --- ANALYSIS ENGINE ---
  function generateReport() {
    document.getElementById('loadingOverlay').style.display = 'flex';
    
    setTimeout(() => {
      // 1. Calculate Scores
      for (let key in state.ratings) {
        let r = state.ratings[key];
        if(r.val >= 4) {
          r.cat.split('_').forEach(c => state.scores[c] += (r.val - 3) * 2);
        }
      }
      
      if(state.pills.p_work) state.pills.p_work.split('_').forEach(c => state.scores[c] += 3);
      if(state.pills.p_decide) state.pills.p_decide.split('_').forEach(c => state.scores[c] += 3);
      
      state.strengths.forEach(c => state.scores[c] += 3);

      // Correction Factor
      let parent = document.getElementById('parentCareer').value;
      let secret = document.getElementById('secretCareer').value;
      if(parent && secret && parent !== secret) {
        let top = Object.keys(state.scores).reduce((a, b) => state.scores[a] > state.scores[b] ? a : b);
        state.scores[top] += 5; // Boost true interest
      }

      // 2. Sort & Map
      let sorted = Object.keys(state.scores).sort((a,b) => state.scores[b] - state.scores[a]);
      let dominant = sorted[0];
      
      const mapping = {
        'I': { title: "The Investigative Thinker", text: "You thrive on logic, research, and solving complex problems.", stream: "Science (PCM / PCB)", careers: "Engineering, Medicine, Data Science, Research", avoid: "Sales, Routine Clerical Work", cols: [{n:"IISc", d:"Research"}, {n:"IIT Roorkee", d:"Tech"}] },
        'A': { title: "The Artistic Creator", text: "You need creative freedom and self-expression.", stream: "Arts / Design / Architecture", careers: "Architecture, UX Design, Media, Writing", avoid: "Strict Data Entry, rigid corporate rules", cols: [{n:"AAAD", d:"Design"}, {n:"GSAP", d:"Architecture"}] },
        'S': { title: "The Social Helper", text: "You are driven by empathy and helping others grow.", stream: "Humanities / Medical", careers: "Psychology, Teaching, HR, Doctor", avoid: "Isolated Lab Work, Machinery", cols: [{n:"Christ", d:"Psychology"}, {n:"St. Josephs", d:"Humanities"}] },
        'E': { title: "The Enterprising Leader", text: "You love persuasion, leadership, and high-stakes goals.", stream: "Commerce / Management", careers: "MBA, Entrepreneurship, Law, Sales", avoid: "Solitary Research, Backend Coding", cols: [{n:"Christ", d:"BBA"}, {n:"NMIMS", d:"Law"}] },
        'C': { title: "The Conventional Organizer", text: "You value structure, data accuracy, and stability.", stream: "Commerce / Finance", careers: "CA, Banking, Accounting, Gov Admin", avoid: "Unstructured Art, Chaos", cols: [{n:"Mount Carmel", d:"Commerce"}] },
        'R': { title: "The Realistic Doer", text: "You prefer hands-on work with tools, machines, or outdoors.", stream: "Engineering / Applied Science", careers: "Pilot, Defence, Mech Eng, Sports", avoid: "Desk-bound Theory, HR", cols: [{n:"AIT", d:"Mech/Robotics"}, {n:"BMSCE", d:"Core Eng"}] }
      };

      let res = mapping[dominant];

      // 3. Populate HTML
      document.getElementById('outName').innerText = document.getElementById('studentName').value || "Student";
      document.getElementById('outLevel').innerText = state.pills.qLevel || "N/A";
      document.getElementById('outPersonalityText').innerText = res.text;
      document.getElementById('outCode').innerText = sorted.slice(0,3).join('');
      document.getElementById('outStream').innerText = res.stream;
      document.getElementById('outCareers').innerText = res.careers;
      document.getElementById('outAvoid').innerText = res.avoid;
      document.getElementById('outLife').innerText = state.pills.life_pri || "N/A";
      document.getElementById('outRole').innerText = document.getElementById('roleModel').value || "N/A";

      let colHTML = '';
      res.cols.forEach(c => colHTML += `<div class="college-card-mini"><h4>${c.n}</h4><p>${c.d}</p></div>`);
      document.getElementById('outColleges').innerHTML = colHTML;

      // 4. Render Chart
      document.getElementById('loadingOverlay').style.display = 'none';
      document.getElementById('wizard').style.display = 'none';
      document.getElementById('progressBox').style.display = 'none';
      document.getElementById('reportContainer').style.display = 'block';
      
      renderChart(state.scores);
      confetti({ particleCount: 150, spread: 70, origin: { y: 0.6 } });
      
    }, 2000);
  }

  function renderChart(scores) {
    const ctx = document.getElementById('radarChart').getContext('2d');
    new Chart(ctx, {
      type: 'radar',
      data: {
        labels: ['Realistic', 'Investigative', 'Artistic', 'Social', 'Enterprising', 'Conventional'],
        datasets: [{
          label: 'Your Career Profile',
          data: [scores.R, scores.I, scores.A, scores.S, scores.E, scores.C],
          backgroundColor: 'rgba(99, 102, 241, 0.2)',
          borderColor: '#6366F1',
          pointBackgroundColor: '#F59E0B',
          pointBorderColor: '#fff',
          pointHoverBackgroundColor: '#fff',
          pointHoverBorderColor: '#F59E0B'
        }]
      },
      options: {
        scales: {
          r: {
            angleLines: { color: '#E5E7EB' },
            grid: { color: '#E5E7EB' },
            suggestedMin: 0,
            suggestedMax: 20
          }
        }
      }
    });
  }

  // --- FIXED PDF EXPORT ---
  function downloadPDF() {
    window.scrollTo(0,0);
    const element = document.getElementById('reportContent');
    const opt = {
      margin: 0.2,
      filename: `Career_Report_${document.getElementById('studentName').value}.pdf`,
      image: { type: 'jpeg', quality: 0.98 },
      html2canvas: { scale: 2, scrollY: 0 },
      jsPDF: { unit: 'in', format: 'a4', orientation: 'portrait' }
    };
    html2pdf().set(opt).from(element).save();
  }
</script>
