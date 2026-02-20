---
layout: default
title: "Discover Your True Path 🚀"
permalink: /assessment/
description: "A fun, interactive career analysis to find your perfect courses and colleges."
---

<script src="https://cdnjs.cloudflare.com/ajax/libs/html2pdf.js/0.10.1/html2pdf.bundle.min.js"></script>

<style>
  /* --- STUDENT FRIENDLY UI THEME --- */
  :root {
    --bg-color: #F3F6FD;
    --primary: #6C63FF; /* Fun vibrant purple */
    --secondary: #4FD1C5; /* Teal */
    --accent: #FF6584; /* Coral/Pink */
    --text-dark: #2D3748;
    --card-bg: #ffffff;
  }

  body { background-color: var(--bg-color); font-family: 'Nunito', 'Segoe UI', sans-serif; color: var(--text-dark); margin: 0; }
  
  .assessment-header {
    background: linear-gradient(135deg, var(--primary) 0%, #8A2BE2 100%);
    color: white; padding: 60px 20px 40px; text-align: center; 
    border-radius: 0 0 30px 30px; margin-bottom: 40px;
    box-shadow: 0 10px 20px rgba(108, 99, 255, 0.2);
  }
  .assessment-header h1 { margin: 0 0 10px 0; font-size: 2.8rem; font-weight: 800; }
  .assessment-header p { font-size: 1.2rem; color: #E9D8FD; max-width: 600px; margin: 0 auto; font-weight: 600;}

  .container { max-width: 900px; margin: 0 auto; padding: 0 20px; }

  /* CHUNKY PROGRESS BAR */
  .progress-container { width: 100%; background: #E2E8F0; border-radius: 50px; height: 16px; margin-bottom: 40px; overflow: hidden; box-shadow: inset 0 2px 4px rgba(0,0,0,0.05); }
  .progress-bar { height: 100%; background: linear-gradient(90deg, var(--secondary), #38B2AC); width: 12.5%; transition: width 0.5s cubic-bezier(0.4, 0, 0.2, 1); border-radius: 50px; }

  /* WIZARD CARDS */
  .step-card {
    background: var(--card-bg); padding: 40px; border-radius: 24px;
    box-shadow: 0 15px 35px rgba(0,0,0,0.04); margin-bottom: 40px;
    display: none; animation: slideUp 0.5s ease; border: 2px solid #EDF2F7;
  }
  .step-card.active { display: block; }
  .step-title { font-size: 1.8rem; font-weight: 800; color: var(--primary); margin-bottom: 5px; text-align: center; }
  .step-sub { text-align: center; color: #718096; margin-bottom: 35px; font-size: 1.1rem; }

  /* INPUTS */
  .form-group { margin-bottom: 25px; }
  .form-label { display: block; font-weight: 700; margin-bottom: 10px; color: var(--text-dark); font-size: 1.1rem; }
  .form-input, .form-textarea {
    width: 100%; padding: 18px; border: 2px solid #E2E8F0; border-radius: 16px;
    font-size: 1.1rem; color: #444; background: #F7FAFC; transition: all 0.3s;
    font-family: inherit;
  }
  .form-input:focus, .form-textarea:focus { border-color: var(--primary); outline: none; background: white; box-shadow: 0 0 0 4px rgba(108, 99, 255, 0.1); }
  .form-textarea { resize: vertical; min-height: 100px; }

  /* EMOJI RATING SCALES */
  .rating-grid { display: flex; flex-direction: column; gap: 15px; margin-bottom: 30px; }
  .rating-row {
    display: flex; align-items: center; justify-content: space-between;
    background: white; padding: 15px 20px; border-radius: 16px; border: 2px solid #E2E8F0;
    transition: 0.3s;
  }
  .rating-row:hover { border-color: #CBD5E0; }
  @media (max-width: 768px) { .rating-row { flex-direction: column; align-items: flex-start; gap: 15px; } }
  
  .rating-label { font-weight: 700; font-size: 1.1rem; flex: 1; color: var(--text-dark); }
  .rating-options { display: flex; gap: 10px; }
  
  .rate-btn {
    width: 45px; height: 45px; border-radius: 50%; border: 2px solid #E2E8F0;
    background: #F7FAFC; font-size: 1.5rem; cursor: pointer;
    display: flex; align-items: center; justify-content: center; transition: all 0.2s cubic-bezier(0.4, 0, 0.2, 1);
  }
  .rate-btn:hover { transform: scale(1.15); border-color: var(--secondary); background: white; }
  .rate-btn.selected { background: var(--secondary); border-color: var(--secondary); transform: scale(1.15); box-shadow: 0 10px 15px rgba(79, 209, 197, 0.3); }

  /* SELECT CARDS */
  .options-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 15px; margin-bottom: 30px; }
  .option-card {
    border: 2px solid #E2E8F0; border-radius: 16px; padding: 20px; cursor: pointer;
    transition: all 0.3s; background: white; display: flex; flex-direction: column; align-items: center; text-align: center;
  }
  .option-card:hover { border-color: var(--primary); transform: translateY(-5px); box-shadow: 0 10px 20px rgba(108, 99, 255, 0.1); }
  .option-card.selected { border-color: var(--primary); background: #EBF4FF; box-shadow: 0 0 0 2px rgba(108, 99, 255, 0.2); }
  .opt-icon { font-size: 2.5rem; margin-bottom: 10px; }
  .opt-title { font-weight: 800; color: var(--text-dark); font-size: 1.05rem; }

  /* PILL TAGS FOR STRENGTHS */
  .pill-grid { display: flex; flex-wrap: wrap; gap: 12px; justify-content: center; }
  .pill-tag {
    background: #F7FAFC; border: 2px solid #E2E8F0; padding: 12px 24px; border-radius: 50px;
    font-weight: 700; color: #4A5568; cursor: pointer; transition: 0.2s; font-size: 1.05rem;
  }
  .pill-tag:hover { border-color: var(--accent); color: var(--accent); }
  .pill-tag.selected { background: var(--accent); border-color: var(--accent); color: white; box-shadow: 0 8px 15px rgba(255, 101, 132, 0.3); }

  /* BUTTONS */
  .btn-nav-wrapper { display: flex; justify-content: space-between; gap: 15px; margin-top: 30px; border-top: 2px dashed #EDF2F7; padding-top: 25px; }
  .btn-main {
    background: var(--primary); color: white; border: none; padding: 16px 35px;
    font-size: 1.1rem; font-weight: 800; border-radius: 50px; cursor: pointer; flex-grow: 1; transition: 0.3s;
  }
  .btn-main:hover { background: #5a52d5; transform: translateY(-3px); box-shadow: 0 10px 20px rgba(108, 99, 255, 0.3); }
  .btn-back { background: #EDF2F7; color: #4A5568; flex-grow: 0; }
  .btn-back:hover { background: #E2E8F0; transform: translateY(0); box-shadow: none; }

  /* --- PRINT/PDF SAFE REPORT STYLES --- */
  #reportContainer { display: none; }
  .report-card { 
    background: white; padding: 40px; border-radius: 20px; 
    box-shadow: 0 15px 40px rgba(0,0,0,0.08); margin-bottom: 40px; 
    border-top: 15px solid var(--primary);
  }
  
  /* Use simple blocks for PDF compatibility */
  .report-header { border-bottom: 2px solid #E2E8F0; padding-bottom: 20px; margin-bottom: 30px; text-align: center; }
  .report-header h2 { color: var(--text-dark); margin: 0 0 10px 0; font-size: 2.2rem; font-weight: 900;}
  .report-meta { color: #718096; font-size: 1.1rem; font-weight: 600; }
  
  .badge-code { 
    display: inline-block; background: var(--accent); color: white; 
    padding: 10px 30px; border-radius: 50px; font-weight: 900; 
    font-size: 1.8rem; margin-top: 20px; letter-spacing: 2px;
  }

  .report-section { margin-bottom: 30px; padding: 25px; border-radius: 16px; background: #F7FAFC; border-left: 6px solid var(--secondary); display: block; }
  .report-section h3 { color: var(--text-dark); font-size: 1.5rem; margin-top: 0; margin-bottom: 15px; font-weight: 800;}
  .report-section p { line-height: 1.8; font-size: 1.1rem; color: #4A5568; margin: 0 0 10px 0;}
  
  .avoid-section { background: #FFF5F5; border-left-color: var(--accent); }
  .avoid-section h3 { color: #C53030; }

  .college-recs { display: flex; flex-wrap: wrap; gap: 20px; margin-top: 20px; }
  .rec-card { background: white; border: 2px solid #E2E8F0; padding: 20px; border-radius: 12px; width: calc(50% - 10px); box-sizing: border-box; }
  .rec-card h4 { margin: 0 0 8px 0; color: var(--primary); font-size: 1.2rem; font-weight: 800; }
  .rec-card p { margin: 0; color: #718096; font-size: 0.95rem; line-height: 1.5;}

  .actions { text-align: center; margin-top: 30px; }

  @keyframes slideUp { from { opacity: 0; transform: translateY(20px); } to { opacity: 1; transform: translateY(0); } }

  /* PDF Print Fixes */
  @media print {
    body { background: white; }
    .actions, .assessment-header, .progress-container { display: none !important; }
    .report-card { box-shadow: none; border: none; padding: 0; border-top: none; }
    .report-section { page-break-inside: avoid; border: 1px solid #E2E8F0; }
    .rec-card { width: 100%; margin-bottom: 15px; } /* Stack colleges in PDF to prevent cut-offs */
  }
</style>

<div class="assessment-header">
  <h1>Discover Your True Path 🚀</h1>
  <p>Answer honestly. No wrong answers. Let's find out what you are naturally built to do!</p>
</div>

<div class="container">
  <div class="progress-container"><div class="progress-bar" id="progressBar"></div></div>

  <div id="wizardContainer">
    
    <div class="step-card active" id="step1">
      <h2 class="step-title">1. Tell us about yourself</h2>
      <p class="step-sub">We need this to personalize your final dossier.</p>
      
      <div class="form-group">
        <label class="form-label">What's your name?</label>
        <input type="text" id="studentName" class="form-input" placeholder="e.g. Alex Johnson">
      </div>
      <div class="form-group">
        <label class="form-label">Where are you currently?</label>
        <div class="options-grid">
          <div class="option-card" onclick="selectRadio('qLevel', 'Class 8-10')"><div class="opt-icon">🏫</div><div class="opt-title">High School (8-10)</div></div>
          <div class="option-card" onclick="selectRadio('qLevel', 'PUC (11-12)')"><div class="opt-icon">📚</div><div class="opt-title">PUC / 11th-12th</div></div>
          <div class="option-card" onclick="selectRadio('qLevel', 'Undergraduate')"><div class="opt-icon">🎓</div><div class="opt-title">Undergraduate</div></div>
        </div>
      </div>
      <button class="btn-main" style="width:100%" onclick="nextStep(2)">Next: Fun Stuff ➔</button>
    </div>

    <div class="step-card" id="step2">
      <h2 class="step-title">2. Subject Vibes 📚</h2>
      <p class="step-sub">How do you feel when you have to study these?</p>
      <div style="display:flex; justify-content:flex-end; gap:10px; margin-bottom: 10px; font-size: 0.8rem; color:#718096; font-weight:bold;">
        <span>Hate it</span><span>➔</span><span>Love it</span>
      </div>
      
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
      <div class="btn-nav-wrapper">
        <button class="btn-main btn-back" onclick="prevStep(1)">Back</button>
        <button class="btn-main" onclick="nextStep(3)">Next ➔</button>
      </div>
    </div>

    <div class="step-card" id="step3">
      <h2 class="step-title">3. Weekend Vibes 🎮</h2>
      <p class="step-sub">If you had free time, how much would you enjoy doing these?</p>
      
      <div class="rating-grid">
        <script>
          const acts1 = [
            { id: 'act_puzzle', label: 'Solving puzzles / Sudoku 🧩', type: 'I' },
            { id: 'act_fix', label: 'Taking gadgets apart to see how they work 🔧', type: 'R_I' },
            { id: 'act_draw', label: 'Sketching, painting, or video editing 🖌️', type: 'A' },
            { id: 'act_lead', label: 'Being the captain of a team or club 👑', type: 'E' },
            { id: 'act_help', label: 'Listening to friends problems and helping ❤️', type: 'S' },
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
      <div class="btn-nav-wrapper">
        <button class="btn-main btn-back" onclick="prevStep(2)">Back</button>
        <button class="btn-main" onclick="nextStep(4)">Next ➔</button>
      </div>
    </div>

    <div class="step-card" id="step4">
      <h2 class="step-title">4. How do you operate? 🧠</h2>
      <p class="step-sub">Pick the side that sounds most like you.</p>
      
      <div class="form-group">
        <div class="form-label">When making a tough decision, I rely on:</div>
        <div class="options-grid">
          <div class="option-card" onclick="selectRadio('p_decide', 'I_C')"><div class="opt-icon">🤖</div><div class="opt-title">Pure Logic & Facts</div></div>
          <div class="option-card" onclick="selectRadio('p_decide', 'S_A')"><div class="opt-icon">❤️</div><div class="opt-title">Gut Feelings & Empathy</div></div>
        </div>
      </div>

      <div class="form-group">
        <div class="form-label">I prefer tasks that are:</div>
        <div class="options-grid">
          <div class="option-card" onclick="selectRadio('p_task', 'C')"><div class="opt-icon">📏</div><div class="opt-title">Structured & Clear</div></div>
          <div class="option-card" onclick="selectRadio('p_task', 'A')"><div class="opt-icon">🌊</div><div class="opt-title">Flexible & Open-ended</div></div>
        </div>
      </div>

      <div class="btn-nav-wrapper">
        <button class="btn-main btn-back" onclick="prevStep(3)">Back</button>
        <button class="btn-main" onclick="nextStep(5)">Next ➔</button>
      </div>
    </div>

    <div class="step-card" id="step5">
      <h2 class="step-title">5. Dream Workplace 🏢</h2>
      <p class="step-sub">Rate how much you'd like to work in these places.</p>
      
      <div class="rating-grid">
        <script>
          const envs = [
            { id: 'env_desk', label: 'Quiet corporate desk / Stable Govt Job 📁', type: 'C' },
            { id: 'env_out', label: 'Outdoors, traveling, or on a site 🏗️', type: 'R' },
            { id: 'env_hosp', label: 'Hospital or people-focused community centre 🏥', type: 'S' },
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
      <div class="btn-nav-wrapper">
        <button class="btn-main btn-back" onclick="prevStep(4)">Back</button>
        <button class="btn-main" onclick="nextStep(6)">Next ➔</button>
      </div>
    </div>

    <div class="step-card" id="step6">
      <h2 class="step-title">6. Your Superpowers ⚡</h2>
      <p class="step-sub">Tap up to 4 things you are naturally good at.</p>
      
      <div class="pill-grid" id="strengthsGrid">
        <div class="pill-tag" onclick="toggleStrength(this, 'C')">Good Memory 🧠</div>
        <div class="pill-tag" onclick="toggleStrength(this, 'I')">Problem Solving 🔍</div>
        <div class="pill-tag" onclick="toggleStrength(this, 'A')">Creativity 🎨</div>
        <div class="pill-tag" onclick="toggleStrength(this, 'S')">Empathy & Listening 🫂</div>
        <div class="pill-tag" onclick="toggleStrength(this, 'E')">Public Speaking 🎤</div>
        <div class="pill-tag" onclick="toggleStrength(this, 'E')">Leadership 👑</div>
        <div class="pill-tag" onclick="toggleStrength(this, 'R')">Physical Stamina 🏃</div>
        <div class="pill-tag" onclick="toggleStrength(this, 'C')">Discipline & Focus ⏳</div>
      </div>
      <div class="btn-nav-wrapper">
        <button class="btn-main btn-back" onclick="prevStep(5)">Back</button>
        <button class="btn-main" onclick="nextStep(7)">Next ➔</button>
      </div>
    </div>

    <div class="step-card" id="step7">
      <h2 class="step-title">7. The Reality Check 🕵️‍♂️</h2>
      <p class="step-sub">Be brutally honest. This ensures the AI gives you the right advice.</p>
      
      <div class="form-group">
        <label class="form-label">What career do your parents or teachers want you to do?</label>
        <input type="text" id="parentCareer" class="form-input" placeholder="e.g., Doctor, Engineer, CA...">
      </div>
      
      <div class="form-group">
        <label class="form-label">If marks, money, and society didn't matter, what is your secret dream job?</label>
        <input type="text" id="secretCareer" class="form-input" placeholder="e.g., Pilot, Musician, Writer, Gamer...">
      </div>

      <div class="btn-nav-wrapper">
        <button class="btn-main btn-back" onclick="prevStep(6)">Back</button>
        <button class="btn-main" style="background: var(--accent);" id="analyzeBtn" onclick="generateRIASECReport()">Generate My Future ✨</button>
      </div>
    </div>

  </div>

  <div id="reportContainer">
    <div class="report-card" id="reportContent">
      <div class="report-header">
        <h2>Career Mapping Dossier</h2>
        <div class="report-meta">
          Student: <strong id="outName" style="color:var(--text-dark);"></strong> | Level: <span id="outLevel"></span><br>
          <span style="font-size: 0.9rem; color:#A0AEC0;">Generated on: <span id="outDate"></span></span>
        </div>
        <div class="badge-code" id="outCode">ISR</div>
      </div>

      <div class="report-section">
        <h3>🧠 Your Unique Personality Profile</h3>
        <p id="outPersonalityText"></p>
      </div>

      <div class="report-section" style="border-left-color: var(--primary);">
        <h3>🎯 Recommended Academic Path</h3>
        <p style="font-size:1.2rem; font-weight:800; color:var(--primary); margin-bottom: 5px;" id="outStream"></p>
        <p><strong>Top Career Matches:</strong> <span id="outCareers"></span></p>
      </div>

      <div class="report-section avoid-section">
        <h3>⚠️ Environments to Reconsider</h3>
        <p>Based on your profile, you may experience burnout or frustration in these environments:</p>
        <p><strong id="outAvoid"></strong></p>
      </div>

      <div class="report-section" style="border-left-color: #38B2AC;">
        <h3>🏛️ Top Verified College Matches</h3>
        <p>Based on our directory, here are excellent institutions for your profile:</p>
        <div class="college-recs" id="outColleges"></div>
      </div>
      
      <div style="text-align: center; font-size: 0.85rem; color: #A0AEC0; margin-top: 40px;">
        Assessment generated by The Knowledge Habitat Career Guidance Engine (RIASEC).
      </div>
    </div>

    <div class="actions">
      <button class="btn-main" id="pdfBtn" onclick="downloadPDF()">📄 Download PDF Report</button>
      <button class="btn-main btn-back" style="margin-left: 10px;" onclick="location.reload()">↺ Start Over</button>
    </div>
  </div>

</div>

<script>
  // STATE MANAGEMENT
  let state = {
    ratings: {},   
    radios: {},    
    strengths: []  
  };

  let totalSteps = 7;

  // UI HELPERS
  function setRating(btn, id, value) {
    const parent = btn.parentElement;
    Array.from(parent.children).forEach(b => b.classList.remove('selected'));
    btn.classList.add('selected');
    const category = parent.parentElement.dataset.category;
    state.ratings[id] = { value: value, category: category };
  }

  function selectRadio(group, val) {
    if(group === 'qLevel') state.level = val;
    state.radios[group] = val;
    const cards = event.currentTarget.parentElement.querySelectorAll('.option-card');
    cards.forEach(c => c.classList.remove('selected'));
    event.currentTarget.classList.add('selected');
  }

  function toggleStrength(card, val) {
    if(card.classList.contains('selected')) {
      card.classList.remove('selected');
      state.strengths = state.strengths.filter(s => s !== val);
    } else {
      if(state.strengths.length >= 4) return alert("You can only select up to 4 strengths!");
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

  // MAIN LOGIC
  function generateRIASECReport() {
    let btn = document.getElementById('analyzeBtn');
    btn.innerText = "Analyzing Brain Waves... 🧠";
    btn.style.opacity = "0.8";

    setTimeout(() => {
      let scores = { R: 0, I: 0, A: 0, S: 0, E: 0, C: 0 };

      // Ratings Tally
      for (let key in state.ratings) {
        let item = state.ratings[key];
        let cats = item.category.split('_');
        cats.forEach(c => { if(item.value >= 4) scores[c] += (item.value - 3) * 2; });
      }

      // Radios Tally
      for (let key in state.radios) {
        if(key === 'qLevel') continue;
        let cats = state.radios[key].split('_');
        cats.forEach(c => scores[c] += 3);
      }

      // Strengths Tally
      state.strengths.forEach(c => scores[c] += 2);

      // Correction Factor
      const parent = document.getElementById('parentCareer').value.toLowerCase();
      const secret = document.getElementById('secretCareer').value.toLowerCase();
      if (secret && parent && secret !== parent) {
        let topCode = Object.keys(scores).reduce((a, b) => scores[a] > scores[b] ? a : b);
        scores[topCode] = Math.round(scores[topCode] * 1.5);
      }

      const sorted = Object.keys(scores).sort((a,b) => scores[b] - scores[a]);
      const finalCode = sorted.slice(0,3).join('');
      const dominant = sorted[0];

      // Output Database
      const mapping = {
        'I': { 
          title: "The Investigative Thinker", 
          text: "You are a curious learner who enjoys understanding concepts deeply. You prefer meaningful, intellectual work over routine tasks. You are highly suited for careers that involve logic, problem solving, and unearthing new information.", 
          stream: "Science with Maths / Data Science",
          careers: "Engineering, Medicine, Research, Data Science, AI, Pharmacy", 
          avoid: "Highly sales-based careers or repetitive clerical jobs", 
          colleges: [{n:"IISc Bangalore", d:"#1 for Research"}, {n:"IIT Roorkee", d:"Top Engineering & AI"}, {n:"BIT Bangalore", d:"Great core tech placements"}] 
        },
        'A': { 
          title: "The Artistic Creator", 
          text: "You thrive in creative expression and visual/spatial tasks. You need flexibility rather than rigid corporate rules. You are best suited for environments that allow you to design, build, and imagine.", 
          stream: "Creative Arts / Architecture / Humanities",
          careers: "Architecture, Design, UX/UI, Animation, Filmmaking", 
          avoid: "Repetitive administrative jobs or rigid data-entry roles", 
          colleges: [{n:"AAAD Bangalore", d:"Specialized Architecture"}, {n:"GSAP", d:"Sustainable Design Focus"}, {n:"EWSA", d:"Dedicated B.Arch campus"}] 
        },
        'E': { 
          title: "The Enterprising Leader", 
          text: "You are a natural leader who enjoys persuading others and managing systems. You are driven by results, influence, and growth. You thrive in fast-paced, high-stakes environments.", 
          stream: "Commerce / Management / Law",
          careers: "Business Management, Law, MBA, Sales, Entrepreneurship", 
          avoid: "Isolated lab research or solitary backend coding", 
          colleges: [{n:"Christ University", d:"Top tier BBA/MBA"}, {n:"NMIMS Law", d:"Premier Law School"}, {n:"Jain University", d:"Focus on Entrepreneurship"}] 
        },
        'S': { 
          title: "The Social Helper", 
          text: "You are driven by empathy and helping others. You enjoy human interaction, collaboration, and improving society. You excel in roles that require high emotional intelligence.", 
          stream: "Humanities / Psychology / Medical",
          careers: "Psychology, Teaching, Counselling, HR, Social Work, Medicine", 
          avoid: "Strictly mechanical or numbers-only environments without human contact", 
          colleges: [{n:"Mount Carmel College", d:"Excellence in Humanities"}, {n:"St. Joseph's University", d:"Holistic Arts & Sciences"}, {n:"Christ University", d:"Top Psychology Dept"}] 
        },
        'R': { 
          title: "The Realistic Builder", 
          text: "You enjoy hands-on, practical work. You prefer doing over thinking and thrive in field-based, technical, or outdoor environments. You like working with tools, machines, or physical systems.", 
          stream: "Science / Applied Tech",
          careers: "Defence, Aviation, Mechanical Engineering, Sports, Skilled Trades", 
          avoid: "Static office-only desk jobs with heavy paperwork", 
          colleges: [{n:"AIT Chikkamagaluru", d:"Hands-on Robotics & Tech"}, {n:"BMSCE", d:"Core Mechanical/Civil"}, {n:"RVCE", d:"Applied Engineering"}] 
        },
        'C': { 
          title: "The Conventional Organizer", 
          text: "You are highly detail-oriented, organized, and reliable. You excel in environments with clear rules, structured data, and numerical accuracy.", 
          stream: "Commerce / Finance",
          careers: "CA, Banking, Accounting, Finance, Government Administration", 
          avoid: "Highly abstract, unstructured, or unpredictable creative roles", 
          colleges: [{n:"Christ University", d:"Top Commerce Programs"}, {n:"Mount Carmel", d:"Excellent B.Com placements"}, {n:"St. Joseph's", d:"Rigorous Accounting"}] 
        }
      };

      const res = mapping[dominant];
      
      document.getElementById('outName').innerText = document.getElementById('studentName').value || "Amazing Student";
      document.getElementById('outLevel').innerText = state.level || "Not Specified";
      document.getElementById('outDate').innerText = new Date().toLocaleDateString();
      
      document.getElementById('outCode').innerText = finalCode;
      document.getElementById('outPersonalityText').innerText = res.text;
      document.getElementById('outStream').innerText = res.stream;
      document.getElementById('outCareers').innerText = res.careers;
      document.getElementById('outAvoid').innerText = res.avoid;

      const collDiv = document.getElementById('outColleges');
      collDiv.innerHTML = '';
      res.colleges.forEach(c => {
          collDiv.innerHTML += `<div class="rec-card"><h4>${c.n}</h4><p>${c.d}</p></div>`;
      });

      document.getElementById('wizardContainer').style.display = 'none';
      document.querySelector('.progress-container').style.display = 'none';
      document.getElementById('reportContainer').style.display = 'block';
      
      // Fix for PDF: scroll to top so html2canvas doesn't capture a cropped view
      window.scrollTo(0, 0);

    }, 800); // slight delay for cool effect
  }

  // FIXED PDF GENERATOR
  function downloadPDF() {
    let btn = document.getElementById('pdfBtn');
    let originalText = btn.innerText;
    btn.innerText = "Generating PDF... ⏳";
    
    // Scroll to top immediately to prevent blank clipping bug in html2canvas
    window.scrollTo(0,0);
    
    setTimeout(() => {
      const element = document.getElementById('reportContent');
      const name = document.getElementById('outName').innerText.replace(/\s+/g, '_');
      
      const opt = { 
        margin: [0.3, 0.3, 0.3, 0.3], // inches
        filename: `Career_Report_${name}.pdf`, 
        image: { type: 'jpeg', quality: 1 }, 
        html2canvas: { 
          scale: 2, 
          useCORS: true,
          scrollY: 0, // Force capture from top
          windowY: 0
        }, 
        jsPDF: { unit: 'in', format: 'a4', orientation: 'portrait' } 
      };
      
      html2pdf().set(opt).from(element).save().then(() => {
        btn.innerText = originalText;
      });
    }, 500); // 500ms delay ensures DOM is fully painted at the top before capturing
  }
</script>
