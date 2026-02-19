---
layout: default
title: "AI Career & Course Assessment 🎯"
permalink: /assessment/
description: "Comprehensive multi-step career analysis based on the RIASEC model. Discover the right courses and colleges based on your unique abilities."
---

<script src="https://cdnjs.cloudflare.com/ajax/libs/html2pdf.js/0.10.1/html2pdf.bundle.min.js"></script>

<style>
  :root {
    --primary: #0A2342;
    --secondary: #1A5276;
    --accent: #e65100;
    --bg: #f4f7f6;
    --card-bg: #ffffff;
    --border: #e0e6ed;
  }

  body { background-color: var(--bg); font-family: 'Segoe UI', system-ui, sans-serif; color: #333; margin: 0; }
  
  .assessment-header {
    background: linear-gradient(135deg, var(--primary) 0%, var(--secondary) 100%);
    color: white; padding: 60px 20px 40px; text-align: center; border-radius: 0 0 20px 20px;
    margin-bottom: 30px; box-shadow: 0 4px 15px rgba(0,0,0,0.1);
  }
  .assessment-header h1 { margin: 0 0 10px 0; font-size: 2.5rem; font-weight: 800; }
  .assessment-header p { font-size: 1.1rem; color: #e0e0e0; max-width: 700px; margin: 0 auto; }

  .container { max-width: 950px; margin: 0 auto; padding: 0 20px; }

  /* PROGRESS BAR */
  .progress-container { width: 100%; background: var(--border); border-radius: 50px; height: 10px; margin-bottom: 30px; overflow: hidden; }
  .progress-bar { height: 100%; background: var(--accent); width: 12.5%; transition: width 0.4s ease; }

  /* WIZARD CARDS */
  .step-card {
    background: var(--card-bg); padding: 40px; border-radius: 12px;
    box-shadow: 0 10px 30px rgba(0,0,0,0.05); margin-bottom: 40px;
    display: none; animation: fadeIn 0.4s;
  }
  .step-card.active { display: block; }
  .step-title { font-size: 1.6rem; font-weight: 800; color: var(--primary); margin-bottom: 5px; text-align: center; }
  .step-sub { text-align: center; color: #666; margin-bottom: 30px; font-size: 1rem; }

  /* UI COMPONENTS */
  .form-group { margin-bottom: 25px; }
  .form-label { display: block; font-weight: 700; margin-bottom: 10px; color: var(--primary); }
  .form-input, .form-textarea {
    width: 100%; padding: 15px; border: 2px solid var(--border); border-radius: 8px;
    font-size: 1rem; color: #444; background: #fcfcfc; transition: all 0.3s;
  }
  .form-input:focus, .form-textarea:focus { border-color: var(--secondary); outline: none; background: white; }
  .form-textarea { resize: vertical; min-height: 80px; }

  /* LIKERT RATING SCALES (1-5) */
  .rating-grid { display: flex; flex-direction: column; gap: 15px; margin-bottom: 30px; }
  .rating-row {
    display: flex; align-items: center; justify-content: space-between;
    background: #fafbfc; padding: 15px 20px; border-radius: 8px; border: 1px solid var(--border);
  }
  @media (max-width: 768px) { .rating-row { flex-direction: column; align-items: flex-start; gap: 10px; } }
  
  .rating-label { font-weight: 600; font-size: 1.05rem; flex: 1; }
  .rating-options { display: flex; gap: 8px; }
  
  .rate-btn {
    width: 40px; height: 40px; border-radius: 8px; border: 2px solid var(--border);
    background: white; color: #555; font-weight: bold; cursor: pointer;
    display: flex; align-items: center; justify-content: center; transition: 0.2s;
  }
  .rate-btn:hover { border-color: var(--secondary); color: var(--secondary); }
  .rate-btn.selected { background: var(--secondary); color: white; border-color: var(--secondary); box-shadow: 0 4px 10px rgba(26,82,118,0.3); }

  /* SELECT CARDS (For Personality & Strengths) */
  .options-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 15px; margin-bottom: 30px; }
  .option-card {
    border: 2px solid var(--border); border-radius: 10px; padding: 15px; cursor: pointer;
    transition: all 0.2s; background: #fafbfc; display: flex; align-items: center; gap: 15px;
  }
  .option-card:hover { border-color: var(--secondary); background: white; transform: translateY(-2px); }
  .option-card.selected { border-color: var(--accent); background: #fff8f5; box-shadow: 0 0 0 2px rgba(230,81,0,0.2); }
  .option-card input[type="checkbox"], .option-card input[type="radio"] { display: none; }
  .opt-text { font-weight: 600; color: #444; }

  /* BUTTONS */
  .btn-nav-wrapper { display: flex; justify-content: space-between; gap: 15px; margin-top: 30px; border-top: 2px solid #eee; padding-top: 25px; }
  .btn-main {
    background: var(--accent); color: white; border: none; padding: 15px 30px;
    font-size: 1.1rem; font-weight: bold; border-radius: 50px; cursor: pointer; transition: 0.3s;
  }
  .btn-main:hover { background: #bf360c; transform: translateY(-2px); box-shadow: 0 5px 15px rgba(230,81,0,0.3); }
  .btn-back { background: var(--border); color: #555; }
  .btn-back:hover { background: #cbd5e1; transform: translateY(0); box-shadow: none; }

  /* REPORT STYLES */
  #reportContainer { display: none; }
  .report-card { background: white; padding: 50px; border-radius: 12px; box-shadow: 0 10px 40px rgba(0,0,0,0.1); margin-bottom: 40px; border-top: 10px solid var(--primary); }
  .report-header { border-bottom: 2px solid #eee; padding-bottom: 20px; margin-bottom: 30px; text-align: center; }
  .report-header h2 { color: var(--primary); margin: 0 0 10px 0; font-size: 2.2rem;}
  .report-meta { color: #777; font-size: 1.1rem; }
  
  .badge-code { display: inline-block; background: var(--accent); color: white; padding: 8px 25px; border-radius: 50px; font-weight: 800; font-size: 1.5rem; margin-top: 15px; letter-spacing: 2px;}

  .report-section { margin-bottom: 35px; padding: 25px; border-radius: 12px; background: #f8fafd; border-left: 5px solid var(--secondary); }
  .report-section h3 { color: var(--primary); font-size: 1.4rem; margin-top: 0; margin-bottom: 15px; }
  .report-section p { line-height: 1.7; font-size: 1.05rem; color: #444; }
  
  .avoid-section { background: #fdf8f8; border-left-color: #e74c3c; }
  .avoid-section h3 { color: #c0392b; }

  .college-recs { display: grid; grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); gap: 20px; margin-top: 20px; }
  .rec-card { background: #fff; border: 1px solid #ddd; padding: 20px; border-radius: 8px; box-shadow: 0 4px 10px rgba(0,0,0,0.02); }
  .rec-card h4 { margin: 0 0 5px 0; color: var(--primary); font-size: 1.1rem; }
  .rec-card p { margin: 0; color: #666; font-size: 0.9rem; }

  .actions { text-align: center; margin-top: 30px; }

  @keyframes fadeIn { from { opacity: 0; transform: translateY(10px); } to { opacity: 1; transform: translateY(0); } }

  @media print {
    body { background: white; }
    .actions, .assessment-header, .progress-container { display: none !important; }
    .report-card { box-shadow: none; border: none; padding: 0; }
    .report-section { page-break-inside: avoid; border: 1px solid #ddd; }
  }
</style>

<div class="assessment-header">
  <h1>AI Career Interest Questionnaire</h1>
  <p>Based on the RIASEC global standard. Takes ~10 minutes. Answer honestly to find your true path!</p>
</div>

<div class="container">
  <div class="progress-container"><div class="progress-bar" id="progressBar"></div></div>

  <div id="wizardContainer">
    
    <div class="step-card active" id="step1">
      <h2 class="step-title">1. Academic Foundations</h2>
      <p class="step-sub">Let's start with your details and subject preferences (1 = Dislike, 5 = Love it).</p>
      
      <div class="form-group">
        <input type="text" id="studentName" class="form-input" placeholder="Your Full Name">
      </div>
      <div class="form-group">
        <select id="studentLevel" class="form-input">
          <option value="" disabled selected>Select Current Level</option>
          <option value="Class 8-10">Class 8 - 10</option>
          <option value="PUC (11-12)">PUC / 11th-12th</option>
          <option value="Undergraduate">Undergraduate</option>
        </select>
      </div>

      <div class="rating-grid">
        <script>
          // Generate 1-5 rating rows dynamically to save space
          const subjects = [
            { id: 'sub_math', label: 'Mathematics', type: 'I_C' },
            { id: 'sub_phy', label: 'Physics', type: 'I' },
            { id: 'sub_bio', label: 'Biology / Chemistry', type: 'I_S' },
            { id: 'sub_cs', label: 'Computer Science / Coding', type: 'I_R' },
            { id: 'sub_eng', label: 'English / Literature', type: 'A' },
            { id: 'sub_soc', label: 'Social Science / History', type: 'S' },
            { id: 'sub_bus', label: 'Business / Economics', type: 'E_C' },
            { id: 'sub_art', label: 'Art / Drawing / Design', type: 'A' },
            { id: 'sub_pe', label: 'Physical Education / Sports', type: 'R' }
          ];
          subjects.forEach(sub => {
            document.write(`
              <div class="rating-row" data-category="${sub.type}">
                <div class="rating-label">${sub.label}</div>
                <div class="rating-options">
                  ${[1,2,3,4,5].map(n => `<div class="rate-btn" onclick="setRating(this, '${sub.id}', ${n})">${n}</div>`).join('')}
                </div>
              </div>
            `);
          });
        </script>
      </div>
      <button class="btn-main" style="width:100%" onclick="nextStep(2)">Next: Activity Interests ➔</button>
    </div>

    <div class="step-card" id="step2">
      <h2 class="step-title">2. Activity Interests (Part 1)</h2>
      <p class="step-sub">How much would you enjoy doing these regularly? (1 = Hate it, 5 = Love it)</p>
      
      <div class="rating-grid">
        <script>
          const acts1 = [
            { id: 'act_puzzle', label: 'Solving puzzles or logical problems', type: 'I' },
            { id: 'act_exp', label: 'Doing science experiments', type: 'I' },
            { id: 'act_code', label: 'Coding or building apps', type: 'I_R' },
            { id: 'act_fix', label: 'Fixing gadgets / Understanding machines', type: 'R_I' },
            { id: 'act_draw', label: 'Drawing / Sketching / Photography', type: 'A' },
            { id: 'act_vid', label: 'Video editing / Content creation', type: 'A' }
          ];
          acts1.forEach(act => {
            document.write(`
              <div class="rating-row" data-category="${act.type}">
                <div class="rating-label">${act.label}</div>
                <div class="rating-options">
                  ${[1,2,3,4,5].map(n => `<div class="rate-btn" onclick="setRating(this, '${act.id}', ${n})">${n}</div>`).join('')}
                </div>
              </div>
            `);
          });
        </script>
      </div>
      <div class="btn-nav-wrapper">
        <button class="btn-main btn-back" onclick="prevStep(1)">⬅ Back</button>
        <button class="btn-main" onclick="nextStep(3)">Next Activities ➔</button>
      </div>
    </div>

    <div class="step-card" id="step3">
      <h2 class="step-title">3. Activity Interests (Part 2)</h2>
      <p class="step-sub">Keep rating your enjoyment levels.</p>
      
      <div class="rating-grid">
        <script>
          const acts2 = [
            { id: 'act_help', label: 'Helping classmates understand lessons', type: 'S' },
            { id: 'act_listen', label: 'Listening to friends’ problems', type: 'S' },
            { id: 'act_sell', label: 'Selling things / Managing money', type: 'E' },
            { id: 'act_lead', label: 'Leading group projects / Negotiating', type: 'E' },
            { id: 'act_build', label: 'Building models / Practical hands-on work', type: 'R' },
            { id: 'act_org', label: 'Organising data / Planning schedules', type: 'C' }
          ];
          acts2.forEach(act => {
            document.write(`
              <div class="rating-row" data-category="${act.type}">
                <div class="rating-label">${act.label}</div>
                <div class="rating-options">
                  ${[1,2,3,4,5].map(n => `<div class="rate-btn" onclick="setRating(this, '${act.id}', ${n})">${n}</div>`).join('')}
                </div>
              </div>
            `);
          });
        </script>
      </div>
      <div class="btn-nav-wrapper">
        <button class="btn-main btn-back" onclick="prevStep(2)">⬅ Back</button>
        <button class="btn-main" onclick="nextStep(4)">Next: Personality ➔</button>
      </div>
    </div>

    <div class="step-card" id="step4">
      <h2 class="step-title">4. Personality Style</h2>
      <p class="step-sub">Choose the option that describes you best.</p>
      
      <div class="form-group">
        <div class="form-label">I prefer:</div>
        <div class="options-grid">
          <div class="option-card" onclick="selectRadio('p_work', 'I_R')"><span class="opt-text">Working alone</span></div>
          <div class="option-card" onclick="selectRadio('p_work', 'S_E')"><span class="opt-text">Working with people</span></div>
        </div>
      </div>

      <div class="form-group">
        <div class="form-label">I make decisions based on:</div>
        <div class="options-grid">
          <div class="option-card" onclick="selectRadio('p_decide', 'I_C')"><span class="opt-text">Logic</span></div>
          <div class="option-card" onclick="selectRadio('p_decide', 'S_A')"><span class="opt-text">Feelings</span></div>
        </div>
      </div>

      <div class="form-group">
        <div class="form-label">I like tasks that are:</div>
        <div class="options-grid">
          <div class="option-card" onclick="selectRadio('p_task', 'C')"><span class="opt-text">Structured and clear</span></div>
          <div class="option-card" onclick="selectRadio('p_task', 'A')"><span class="opt-text">Flexible and creative</span></div>
        </div>
      </div>

      <div class="form-group">
        <div class="form-label">I am usually:</div>
        <div class="options-grid" style="grid-template-columns: repeat(3, 1fr);">
          <div class="option-card" onclick="selectRadio('p_trait', 'I')"><span class="opt-text">Curious</span></div>
          <div class="option-card" onclick="selectRadio('p_trait', 'R')"><span class="opt-text">Practical</span></div>
          <div class="option-card" onclick="selectRadio('p_trait', 'A')"><span class="opt-text">Creative</span></div>
          <div class="option-card" onclick="selectRadio('p_trait', 'S')"><span class="opt-text">Caring</span></div>
          <div class="option-card" onclick="selectRadio('p_trait', 'E')"><span class="opt-text">Ambitious</span></div>
        </div>
      </div>

      <div class="btn-nav-wrapper">
        <button class="btn-main btn-back" onclick="prevStep(3)">⬅ Back</button>
        <button class="btn-main" onclick="nextStep(5)">Next: Environment ➔</button>
      </div>
    </div>

    <div class="step-card" id="step5">
      <h2 class="step-title">5. Work Environment Preference</h2>
      <p class="step-sub">What kind of workplace sounds appealing? (1-5)</p>
      
      <div class="rating-grid">
        <script>
          const envs = [
            { id: 'env_desk', label: 'Office desk job / Government job', type: 'C' },
            { id: 'env_out', label: 'Working outdoors / Travelling', type: 'R' },
            { id: 'env_hosp', label: 'Hospital / People-interaction', type: 'S' },
            { id: 'env_lab', label: 'Lab or research environment', type: 'I' },
            { id: 'env_bus', label: 'Business / Corporate setting', type: 'E' },
            { id: 'env_free', label: 'Freelancing / Creative studio', type: 'A' }
          ];
          envs.forEach(env => {
            document.write(`
              <div class="rating-row" data-category="${env.type}">
                <div class="rating-label">${env.label}</div>
                <div class="rating-options">
                  ${[1,2,3,4,5].map(n => `<div class="rate-btn" onclick="setRating(this, '${env.id}', ${n})">${n}</div>`).join('')}
                </div>
              </div>
            `);
          });
        </script>
      </div>
      <div class="btn-nav-wrapper">
        <button class="btn-main btn-back" onclick="prevStep(4)">⬅ Back</button>
        <button class="btn-main" onclick="nextStep(6)">Next: Strengths ➔</button>
      </div>
    </div>

    <div class="step-card" id="step6">
      <h2 class="step-title">6. Strengths & Self-Perception</h2>
      <p class="step-sub">Select up to 5 things you are naturally good at.</p>
      
      <div class="options-grid" id="strengthsGrid">
        <div class="option-card" onclick="toggleStrength(this, 'C')"><span class="opt-text">Good memory / Discipline</span></div>
        <div class="option-card" onclick="toggleStrength(this, 'I')"><span class="opt-text">Logical thinking / Observation</span></div>
        <div class="option-card" onclick="toggleStrength(this, 'A')"><span class="opt-text">Creativity</span></div>
        <div class="option-card" onclick="toggleStrength(this, 'S')"><span class="opt-text">Communication / Empathy</span></div>
        <div class="option-card" onclick="toggleStrength(this, 'E')"><span class="opt-text">Leadership</span></div>
        <div class="option-card" onclick="toggleStrength(this, 'R')"><span class="opt-text">Physical stamina / Patience</span></div>
      </div>
      <div class="btn-nav-wrapper">
        <button class="btn-main btn-back" onclick="prevStep(5)">⬅ Back</button>
        <button class="btn-main" onclick="nextStep(7)">Next: Reality Check ➔</button>
      </div>
    </div>

    <div class="step-card" id="step7">
      <h2 class="step-title">7. Exposure & Reality Check</h2>
      <p class="step-sub">Be brutally honest here. This adjusts the AI analysis.</p>
      
      <div class="form-group">
        <label class="form-label">What career do your parents prefer for you?</label>
        <input type="text" id="parentCareer" class="form-input" placeholder="e.g., Doctor, Engineer, CA...">
      </div>
      
      <div class="form-group">
        <label class="form-label">If marks/society were not important, what career would you secretly choose?</label>
        <input type="text" id="secretCareer" class="form-input" placeholder="e.g., Pilot, Musician, Writer...">
      </div>

      <div class="form-group">
        <label class="form-label">What do you think a normal day looks like in your secret career?</label>
        <textarea id="dayInLife" class="form-textarea" placeholder="Briefly describe what you think you'd do every day..."></textarea>
      </div>

      <div class="btn-nav-wrapper">
        <button class="btn-main btn-back" onclick="prevStep(6)">⬅ Back</button>
        <button class="btn-main" style="background: var(--primary);" onclick="generateRIASECReport()">Analyze My Profile ✨</button>
      </div>
    </div>

  </div>

  <div id="reportContainer">
    <div class="report-card" id="reportContent">
      <div class="report-header">
        <h2>Comprehensive Career Analysis</h2>
        <div class="report-meta">
          Prepared for: <strong id="outName"></strong> | Academic Level: <span id="outLevel"></span><br>
          Date: <span id="outDate"></span>
        </div>
        <div class="badge-code" id="outCode">ISR</div>
      </div>

      <div class="report-section">
        <h3>🧠 Career Personality Profile</h3>
        <p id="outPersonalityText"></p>
      </div>

      <div class="report-section">
        <h3>🎯 Recommended Academic Stream & Careers</h3>
        <p><strong>Ideal Stream:</strong> <span id="outStream"></span></p>
        <p><strong>Top Career Matches:</strong> <span id="outCareers"></span></p>
      </div>

      <div class="report-section avoid-section">
        <h3>⚠️ Career Paths to Reconsider (Avoid)</h3>
        <p>Based on your profile, you may experience burnout or dissatisfaction in these environments:</p>
        <p><strong id="outAvoid"></strong></p>
      </div>

      <div class="report-section">
        <h3>🏛️ Top Verified College Matches</h3>
        <p>Based on our directory, here are excellent institutions for your profile:</p>
        <div class="college-recs" id="outColleges"></div>
      </div>
      
      <div style="text-align: center; font-size: 0.85rem; color: #888; margin-top: 30px;">
        Assessment generated by The Knowledge Habitat Career Guidance Engine (RIASEC Model).
      </div>
    </div>

    <div class="actions">
      <button class="btn-main" onclick="downloadPDF()">📄 Download PDF Report</button>
      <button class="btn-main btn-back" style="margin-left: 10px;" onclick="location.reload()">↺ Start Over</button>
    </div>
  </div>

</div>

<script>
  // STATE MANAGEMENT
  let state = {
    ratings: {},   // Stores 1-5 ratings
    radios: {},    // Stores single selections
    strengths: []  // Stores multiple selections
  };

  let totalSteps = 7;

  // UI HELPERS
  function setRating(btn, id, value) {
    const parent = btn.parentElement;
    Array.from(parent.children).forEach(b => b.classList.remove('selected'));
    btn.classList.add('selected');
    
    // Get category from grandparent row
    const category = parent.parentElement.dataset.category;
    state.ratings[id] = { value: value, category: category };
  }

  function selectRadio(group, val) {
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
      if(state.strengths.length >= 5) return alert("You can only select up to 5 strengths.");
      card.classList.add('selected');
      state.strengths.push(val);
    }
  }

  // NAVIGATION
  function nextStep(step) {
    document.querySelectorAll('.step-card').forEach(c => c.classList.remove('active'));
    document.getElementById('step' + step).classList.add('active');
    document.getElementById('progressBar').style.width = ((step / totalSteps) * 100) + '%';
    window.scrollTo({ top: 0, behavior: 'smooth' });
  }

  function prevStep(step) { nextStep(step); }

  // MAIN LOGIC & CALCULATION
  function generateRIASECReport() {
    let scores = { R: 0, I: 0, A: 0, S: 0, E: 0, C: 0 };

    // 1. Tally Ratings (Subjects, Activities, Environments)
    for (let key in state.ratings) {
      let item = state.ratings[key];
      // Split category (e.g. "I_C" -> ["I", "C"])
      let cats = item.category.split('_');
      cats.forEach(c => {
        // If rating is 4 or 5, add positive points. If 1 or 2, subtract.
        if(item.value >= 4) scores[c] += (item.value - 3) * 2; 
      });
    }

    // 2. Tally Radios (Personality)
    for (let key in state.radios) {
      let cats = state.radios[key].split('_');
      cats.forEach(c => scores[c] += 3);
    }

    // 3. Tally Strengths
    state.strengths.forEach(c => scores[c] += 2);

    // 4. Parental Pressure Correction Factor
    const parent = document.getElementById('parentCareer').value.toLowerCase();
    const secret = document.getElementById('secretCareer').value.toLowerCase();
    
    if (secret && parent && secret !== parent) {
      // Find current highest score
      let topCode = Object.keys(scores).reduce((a, b) => scores[a] > scores[b] ? a : b);
      // Boost it because student has secret aspiration against pressure
      scores[topCode] = Math.round(scores[topCode] * 1.5);
    }

    // 5. Determine Top 3 (Career Code)
    const sorted = Object.keys(scores).sort((a,b) => scores[b] - scores[a]);
    const finalCode = sorted.slice(0,3).join('');
    const dominant = sorted[0];

    // 6. Output Mapping Database
    const mapping = {
      'I': { 
        title: "Investigative (Thinker & Problem Solver)", 
        text: "You are a curious learner who enjoys understanding concepts deeply. You prefer meaningful, intellectual work over routine tasks. You are highly suited for careers that involve logic, problem solving, and unearthing new information.", 
        stream: "Science with Maths / Data Science",
        careers: "Engineering, Medicine, Research, Data Science, AI, Pharmacy", 
        avoid: "Highly sales-based careers or repetitive clerical jobs", 
        colleges: [{n:"IISc Bangalore", d:"#1 for Research"}, {n:"IIT Roorkee", d:"Top Engineering & AI"}, {n:"BIT Bangalore", d:"Great core tech placements"}] 
      },
      'A': { 
        title: "Artistic (Creative & Flexible)", 
        text: "You thrive in creative expression and visual/spatial tasks. You need flexibility rather than rigid corporate rules. You are best suited for environments that allow you to design, build, and imagine.", 
        stream: "Creative Arts / Architecture / Humanities",
        careers: "Architecture, Design, UX/UI, Animation, Filmmaking", 
        avoid: "Repetitive administrative jobs or rigid data-entry roles", 
        colleges: [{n:"AAAD Bangalore", d:"Specialized Architecture"}, {n:"GSAP", d:"Sustainable Design Focus"}, {n:"EWSA", d:"Dedicated B.Arch campus"}] 
      },
      'E': { 
        title: "Enterprising (Leader & Persuader)", 
        text: "You are a natural leader who enjoys persuading others and managing systems. You are driven by results, influence, and growth. You thrive in fast-paced, high-stakes environments.", 
        stream: "Commerce / Management / Law",
        careers: "Business Management, Law, MBA, Sales, Entrepreneurship", 
        avoid: "Isolated lab research or solitary backend coding", 
        colleges: [{n:"Christ University", d:"Top tier BBA/MBA"}, {n:"NMIMS Law", d:"Premier Law School"}, {n:"Jain University", d:"Focus on Entrepreneurship"}] 
      },
      'S': { 
        title: "Social (Helper & Communicator)", 
        text: "You are driven by empathy and helping others. You enjoy human interaction, collaboration, and improving society. You excel in roles that require high emotional intelligence.", 
        stream: "Humanities / Psychology / Medical",
        careers: "Psychology, Teaching, Counselling, HR, Social Work, Medicine", 
        avoid: "Strictly mechanical or numbers-only environments without human contact", 
        colleges: [{n:"Mount Carmel College", d:"Excellence in Humanities"}, {n:"St. Joseph's University", d:"Holistic Arts & Sciences"}, {n:"Christ University", d:"Top Psychology Dept"}] 
      },
      'R': { 
        title: "Realistic (Practical Builder)", 
        text: "You enjoy hands-on, practical work. You prefer doing over thinking and thrive in field-based, technical, or outdoor environments. You like working with tools, machines, or physical systems.", 
        stream: "Science / Applied Tech / Physical Education",
        careers: "Defence, Aviation, Mechanical Engineering, Sports, Skilled Trades", 
        avoid: "Static office-only desk jobs with heavy paperwork", 
        colleges: [{n:"AIT Chikkamagaluru", d:"Hands-on Robotics & Tech"}, {n:"BMSCE", d:"Core Mechanical/Civil"}, {n:"RVCE", d:"Applied Engineering"}] 
      },
      'C': { 
        title: "Conventional (Organiser & Analyst)", 
        text: "You are highly detail-oriented, organized, and reliable. You excel in environments with clear rules, structured data, and numerical accuracy.", 
        stream: "Commerce / Finance",
        careers: "CA, Banking, Accounting, Finance, Government Administration", 
        avoid: "Highly abstract, unstructured, or unpredictable creative roles", 
        colleges: [{n:"Christ University", d:"Top Commerce Programs"}, {n:"Mount Carmel", d:"Excellent B.Com placements"}, {n:"St. Joseph's", d:"Rigorous Accounting"}] 
      }
    };

    // Render Data
    const res = mapping[dominant];
    
    let studentName = document.getElementById('studentName').value || "Student";
    document.getElementById('outName').innerText = studentName;
    document.getElementById('outLevel').innerText = document.getElementById('studentLevel').value || "Not Specified";
    document.getElementById('outDate').innerText = new Date().toLocaleDateString();
    
    document.getElementById('outCode').innerText = finalCode;
    document.getElementById('outPersonalityText').innerText = `Career Personality: ${finalCode} - ${res.title}. ${res.text}`;
    document.getElementById('outStream').innerText = res.stream;
    document.getElementById('outCareers').innerText = res.careers;
    document.getElementById('outAvoid').innerText = res.avoid;

    const collDiv = document.getElementById('outColleges');
    collDiv.innerHTML = '';
    res.colleges.forEach(c => {
        collDiv.innerHTML += `
        <div class="rec-card">
          <h4>${c.n}</h4>
          <p>${c.d}</p>
        </div>`;
    });

    // Show Report
    document.getElementById('wizardContainer').style.display = 'none';
    document.querySelector('.progress-container').style.display = 'none';
    document.getElementById('reportContainer').style.display = 'block';
    window.scrollTo({ top: 0, behavior: 'smooth' });
  }

  // PDF GENERATOR
  function downloadPDF() {
    const element = document.getElementById('reportContent');
    const name = document.getElementById('outName').innerText.replace(/\s+/g, '_');
    const opt = { 
      margin: 0.5, 
      filename: `Career_Report_${name}.pdf`, 
      image: { type: 'jpeg', quality: 0.98 }, 
      html2canvas: { scale: 2 }, 
      jsPDF: { unit: 'in', format: 'a4', orientation: 'portrait' } 
    };
    html2pdf().set(opt).from(element).save();
  }
</script>
