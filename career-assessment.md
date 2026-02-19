---
layout: default
title: "AI Career & Course Assessment 🎯"
permalink: /assessment/
description: "Comprehensive multi-step RIASEC career analysis based on your unique abilities, environment preferences, and motivations."
---

<script src="https://cdnjs.cloudflare.com/ajax/libs/html2pdf.js/0.10.1/html2pdf.bundle.min.js"></script>

<style>
  body { background-color: #f4f7f6; font-family: 'Segoe UI', system-ui, sans-serif; color: #333; }
  
  .assessment-header {
    background: linear-gradient(135deg, #0A2342 0%, #1A5276 100%);
    color: white; padding: 60px 20px 40px; text-align: center; border-radius: 0 0 20px 20px;
    margin-bottom: 40px; box-shadow: 0 4px 15px rgba(0,0,0,0.1);
  }
  .assessment-header h1 { margin: 0 0 10px 0; font-size: 2.5rem; font-weight: 800; }
  .assessment-header p { font-size: 1.1rem; color: #e0e0e0; max-width: 600px; margin: 0 auto; }

  .container { max-width: 950px; margin: 0 auto; padding: 0 20px; }

  /* PROGRESS BAR */
  .progress-container { width: 100%; background: #e0e6ed; border-radius: 50px; height: 10px; margin-bottom: 30px; overflow: hidden; }
  .progress-bar { height: 100%; background: #e65100; width: 12.5%; transition: width 0.4s ease; }

  /* STEP WIZARD STYLES */
  .step-card {
    background: white; padding: 40px; border-radius: 12px;
    box-shadow: 0 10px 30px rgba(0,0,0,0.05); margin-bottom: 40px;
    display: none; animation: fadeIn 0.4s;
  }
  .step-card.active { display: block; }
  .step-title { font-size: 1.6rem; font-weight: 800; color: #0A2342; margin-bottom: 10px; text-align: center; }
  .step-sub { text-align: center; color: #666; margin-bottom: 30px; font-size: 1rem; }
  
  /* INPUTS */
  .form-input {
    width: 100%; padding: 15px; border: 2px solid #e0e6ed; border-radius: 8px;
    font-size: 1rem; color: #444; background: #fcfcfc; transition: all 0.3s; margin-bottom: 20px;
  }

  /* OPTIONS GRID */
  .options-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(240px, 1fr)); gap: 15px; margin-bottom: 30px; }
  .option-card {
    border: 2px solid #e0e6ed; border-radius: 10px; padding: 15px; cursor: pointer;
    transition: all 0.2s; background: #fafbfc; display: flex; flex-direction: column; align-items: center; text-align: center;
  }
  .option-card:hover { border-color: #1A5276; background: white; transform: translateY(-3px); }
  .option-card.selected { border-color: #e65100; background: #fff8f5; box-shadow: 0 0 0 2px rgba(230,81,0,0.2); }
  .opt-icon { font-size: 1.8rem; margin-bottom: 10px; }
  .opt-title { font-weight: 700; color: #0A2342; font-size: 0.95rem; }

  /* RATING STYLES */
  .rating-row { display: flex; align-items: center; justify-content: space-between; padding: 12px 0; border-bottom: 1px solid #eee; }
  .rating-label { font-weight: 600; flex: 1; }
  .rating-stars { display: flex; gap: 8px; }
  .star { cursor: pointer; font-size: 1.2rem; color: #ccc; transition: 0.2s; }
  .star.active { color: #f39c12; }

  /* BUTTONS */
  .btn-nav-wrapper { display: flex; justify-content: space-between; gap: 15px; margin-top: 20px; }
  .btn-main {
    background: #e65100; color: white; border: none; padding: 15px 30px;
    font-size: 1.1rem; font-weight: bold; border-radius: 50px; cursor: pointer; flex-grow: 1; transition: 0.3s;
  }
  .btn-main:hover { background: #bf360c; transform: translateY(-2px); }
  .btn-back { background: #e0e6ed; color: #555; }

  /* REPORT */
  #reportContainer { display: none; }
  .report-card { background: white; padding: 40px; border-radius: 12px; box-shadow: 0 10px 40px rgba(0,0,0,0.1); border-top: 10px solid #0A2342; }
  .report-section { margin-bottom: 25px; padding: 20px; border-radius: 8px; background: #f8fafd; }
  .report-section h3 { color: #0A2342; margin-bottom: 10px; border-bottom: 2px solid #0A2342; display: inline-block; }
  .badge-code { background: #e65100; color: white; padding: 5px 15px; border-radius: 50px; font-weight: 800; font-size: 1.2rem; }

  @keyframes fadeIn { from { opacity: 0; transform: translateY(10px); } to { opacity: 1; transform: translateY(0); } }
</style>

<div class="assessment-header">
  <h1>AI Career & Course Selector</h1>
  <p>Step-by-step career mapping based on the RIASEC global standard.</p>
</div>

<div class="container">
  <div class="progress-container"><div class="progress-bar" id="progressBar"></div></div>

  <div id="wizardContainer">
    
    <div class="step-card active" id="step1">
      <h2 class="step-title">Welcome! Let's get started.</h2>
      <p class="step-sub">Enter your details to begin your personalized mapping.</p>
      <input type="text" id="qName" class="form-input" placeholder="Enter your full name">
      <div class="options-grid" id="qLevel">
        <div class="option-card" onclick="selectOption('qLevel', 'Class 10')"><div class="opt-icon">🏫</div><div class="opt-title">Class 10</div></div>
        <div class="option-card" onclick="selectOption('qLevel', 'PUC')"><div class="opt-icon">📚</div><div class="opt-title">PUC / 12th</div></div>
        <div class="option-card" onclick="selectOption('qLevel', 'UG')"><div class="opt-icon">🎓</div><div class="opt-title">Undergraduate</div></div>
        <div class="option-card" onclick="selectOption('qLevel', 'PG')"><div class="opt-icon">🔬</div><div class="opt-title">Postgraduate</div></div>
      </div>
      <button class="btn-main" onclick="nextStep(2)">Next Step ➔</button>
    </div>

    <div class="step-card" id="step2">
      <h2 class="step-title">What sounds like a fun weekend?</h2>
      <p class="step-sub">Pick the activity you'd enjoy most.</p>
      <div class="options-grid" id="qInterest">
        <div class="option-card" onclick="selectOption('qInterest', 'I')"><div class="opt-icon">💻</div><div class="opt-title">Coding or building an app</div></div>
        <div class="option-card" onclick="selectOption('qInterest', 'A')"><div class="opt-icon">🎨</div><div class="opt-title">Drawing / Photo Editing</div></div>
        <div class="option-card" onclick="selectOption('qInterest', 'S')"><div class="opt-icon">🤝</div><div class="opt-title">Teaching or helping friends</div></div>
        <div class="option-card" onclick="selectOption('qInterest', 'E')"><div class="opt-icon">💰</div><div class="opt-title">Managing a small business</div></div>
        <div class="option-card" onclick="selectOption('qInterest', 'R')"><div class="opt-icon">🔧</div><div class="opt-title">Fixing a gadget or cooking</div></div>
        <div class="option-card" onclick="selectOption('qInterest', 'C')"><div class="opt-icon">📊</div><div class="opt-title">Organising data / planning</div></div>
      </div>
      <div class="btn-nav-wrapper">
        <button class="btn-main btn-back" onclick="prevStep(1)">Back</button>
        <button class="btn-main" onclick="nextStep(3)">Next Step ➔</button>
      </div>
    </div>

    <div class="step-card" id="step3">
      <h2 class="step-title">Describe your style</h2>
      <div class="options-grid" id="qStyle1">
        <div class="option-card" onclick="selectOption('qStyle1', 'I')"><div class="opt-icon">🧠</div><div class="opt-title">I base decisions on LOGIC</div></div>
        <div class="option-card" onclick="selectOption('qStyle1', 'S')"><div class="opt-icon">❤️</div><div class="opt-title">I base decisions on FEELINGS</div></div>
      </div>
      <div class="options-grid" id="qStyle2">
        <div class="option-card" onclick="selectOption('qStyle2', 'C')"><div class="opt-icon">📐</div><div class="opt-title">I like STRUCTURED tasks</div></div>
        <div class="option-card" onclick="selectOption('qStyle2', 'A')"><div class="opt-icon">🌊</div><div class="opt-title">I like FLEXIBLE tasks</div></div>
      </div>
      <div class="btn-nav-wrapper">
        <button class="btn-main btn-back" onclick="prevStep(2)">Back</button>
        <button class="btn-main" onclick="nextStep(4)">Next Step ➔</button>
      </div>
    </div>

    <div class="step-card" id="step4">
      <h2 class="step-title">Work Environment Preference</h2>
      <p class="step-sub">How appealing do these sound? (1-5 Stars)</p>
      <div id="envRatings">
        <div class="rating-row" data-ria="I">
            <span class="rating-label">Lab or research environment</span>
            <div class="rating-stars" onclick="handleStar(event)">
                <span class="star" data-val="1">★</span><span class="star" data-val="2">★</span><span class="star" data-val="3">★</span><span class="star" data-val="4">★</span><span class="star" data-val="5">★</span>
            </div>
        </div>
        <div class="rating-row" data-ria="E">
            <span class="rating-label">High-stakes business setting</span>
            <div class="rating-stars" onclick="handleStar(event)">
                <span class="star" data-val="1">★</span><span class="star" data-val="2">★</span><span class="star" data-val="3">★</span><span class="star" data-val="4">★</span><span class="star" data-val="5">★</span>
            </div>
        </div>
        <div class="rating-row" data-ria="A">
            <span class="rating-label">Freelancing / Creative studio</span>
            <div class="rating-stars" onclick="handleStar(event)">
                <span class="star" data-val="1">★</span><span class="star" data-val="2">★</span><span class="star" data-val="3">★</span><span class="star" data-val="4">★</span><span class="star" data-val="5">★</span>
            </div>
        </div>
      </div>
      <div class="btn-nav-wrapper">
        <button class="btn-main btn-back" onclick="prevStep(3)">Back</button>
        <button class="btn-main" onclick="nextStep(5)">Next Step ➔</button>
      </div>
    </div>

    <div class="step-card" id="step5">
      <h2 class="step-title">What are you naturally good at?</h2>
      <div class="options-grid" id="qAcademic">
        <div class="option-card" onclick="selectOption('qAcademic', 'I')"><div class="opt-icon">🔬</div><div class="opt-title">Science / Solving Why</div></div>
        <div class="option-card" onclick="selectOption('qAcademic', 'C')"><div class="opt-icon">📉</div><div class="opt-title">Maths / Accuracy</div></div>
        <div class="option-card" onclick="selectOption('qAcademic', 'S')"><div class="opt-icon">📖</div><div class="opt-title">Languages / Social Studies</div></div>
      </div>
      <div class="btn-nav-wrapper">
        <button class="btn-main btn-back" onclick="prevStep(4)">Back</button>
        <button class="btn-main" onclick="nextStep(6)">Next Step ➔</button>
      </div>
    </div>

    <div class="step-card" id="step6">
      <h2 class="step-title">The "Marks Aside" Question</h2>
      <p class="step-sub">If marks and society were not important, what career would you choose secretly?</p>
      <input type="text" id="qSecret" class="form-input" placeholder="e.g. Pilot, Musician, Surgeon...">
      <p class="step-sub">What do your parents want you to become?</p>
      <input type="text" id="qParent" class="form-input" placeholder="e.g. Engineer, Doctor...">
      
      <div class="btn-nav-wrapper">
        <button class="btn-main btn-back" onclick="prevStep(5)">Back</button>
        <button class="btn-main" onclick="generateRIASECReport()">Analyze My Future ✨</button>
      </div>
    </div>

  </div>

  <div id="reportContainer">
    <div class="report-card" id="reportContent">
      <div style="text-align:center; margin-bottom: 30px;">
        <h1 style="color:#0A2342;">Career Mapping Report</h1>
        <p>Student: <strong id="outName"></strong> | Level: <span id="outLevel"></span></p>
        <div class="badge-code" id="outCode">ISR</div>
      </div>

      <div class="report-section">
        <h3>Career Personality</h3>
        <p id="outPersonalityText"></p>
      </div>

      <div class="report-section">
        <h3>Recommended Path</h3>
        <p><strong>Primary Suggestion:</strong> <span id="outPrimary"></span></p>
        <p><strong>Avoid:</strong> <span id="outAvoid" style="color:#c0392b;"></span></p>
      </div>

      <div class="report-section">
        <h3>Verified College Matches</h3>
        <div id="outColleges" style="display:grid; grid-template-columns:1fr 1fr; gap:15px;"></div>
      </div>
    </div>

    <div class="actions">
      <button class="btn-download" onclick="downloadPDF()">📄 Download PDF Report</button>
      <button class="btn-download" style="background:white; color:#0A2342; border:2px solid #0A2342; margin-left:10px;" onclick="location.reload()">↺ Start Over</button>
    </div>
  </div>
</div>

<script>
  let answers = { level: "", interest: "", style1: "", style2: "", academic: "", secret: "", parent: "" };
  let riasecScores = { R: 0, I: 0, A: 0, S: 0, E: 0, C: 0 };

  function handleStar(e) {
    if(!e.target.classList.contains('star')) return;
    const val = parseInt(e.target.dataset.val);
    const row = e.target.closest('.rating-row');
    const ria = row.dataset.ria;
    const stars = row.querySelectorAll('.star');
    stars.forEach(s => s.classList.toggle('active', parseInt(s.dataset.val) <= val));
    riasecScores[ria] = val; // Direct score from stars
  }

  function selectOption(group, value) {
    answers[group.replace('q', '').toLowerCase()] = value;
    const cards = document.getElementById(group).querySelectorAll('.option-card');
    cards.forEach(c => c.classList.remove('selected'));
    event.currentTarget.classList.add('selected');
  }

  function nextStep(s) {
    document.querySelectorAll('.step-card').forEach(c => c.classList.remove('active'));
    document.getElementById('step' + s).classList.add('active');
    document.getElementById('progressBar').style.width = (s * 16.6) + '%';
  }

  function prevStep(s) {
    document.querySelectorAll('.step-card').forEach(c => c.classList.remove('active'));
    document.getElementById('step' + s).classList.add('active');
    document.getElementById('progressBar').style.width = (s * 16.6) + '%';
  }

  function generateRIASECReport() {
    // 1. Scoring logic
    riasecScores[answers.interest] += 5;
    riasecScores[answers.style1] += 3;
    riasecScores[answers.style2] += 3;
    riasecScores[answers.academic] += 4;

    // 2. Parental Pressure Correction Factor
    if(answers.secret.toLowerCase() !== answers.parent.toLowerCase()) {
        const topCode = Object.keys(riasecScores).reduce((a, b) => riasecScores[a] > riasecScores[b] ? a : b);
        riasecScores[topCode] *= 1.4; // Boost top interest confidence
    }

    const sorted = Object.keys(riasecScores).sort((a,b) => riasecScores[b] - riasecScores[a]);
    const finalCode = sorted.slice(0,3).join('');
    const dominant = sorted[0];

    const mapping = {
      'I': { title: "Investigative dominant", text: "You are a curious learner who enjoys understanding concepts deeply. You prefer meaningful work rather than routine tasks.", suger: "Engineering, Medicine, Data Science, AI", avoid: "Highly sales-based roles", colleges: ["IISc Bangalore", "IIT Roorkee", "BIT Bangalore"] },
      'A': { title: "Artistic dominant", text: "You thrive in creative expression and visual spatial tasks. You need flexibility rather than rigid rules.", suger: "Design, Architecture, UX/UI, Filmmaking", avoid: "Repetitive clerical or administrative jobs", colleges: ["AAAD Bangalore", "GSAP Bangalore", "EWSA"] },
      'E': { title: "Enterprising dominant", text: "You are a natural leader who enjoys persuading others and managing systems. You are driven by results and growth.", suger: "Business Management, Law, MBA, Entrepreneurship", avoid: "Isolated lab research or solitary data entry", colleges: ["Christ University", "Jain University", "NMIMS Law"] },
      'S': { title: "Social dominant", text: "You are driven by empathy and helping others. You enjoy human interaction and collaborative problem solving.", suger: "Psychology, Teaching, Counselling, HR", avoid: "Strictly mechanical or numbers-only environments", colleges: ["Mount Carmel College", "St. Joseph's University", "TISS"] },
      'R': { title: "Realistic dominant", text: "You enjoy hands-on, practical work. You prefer doing over thinking and thrive in field-based or technical environments.", suger: "Aviation, Defence, Mechanical Engineering, Sports", avoid: "Static office-only desk jobs", colleges: ["AIT Chikkamagaluru", "RVCE Bangalore", "NDA"] },
      'C': { title: "Conventional dominant", text: "You are detail-oriented and organized. You excel in environments with clear rules and structured data.", suger: "CA, Finance, Banking, Accounting", avoid: "Highly abstract or unpredictable creative roles", colleges: ["Mount Carmel (Commerce)", "Christ (B.Com)", "SRCC"] }
    };

    const res = mapping[dominant];
    document.getElementById('outName').innerText = document.getElementById('qName').value || "Student";
    document.getElementById('outLevel').innerText = answers.level;
    document.getElementById('outCode').innerText = finalCode;
    document.getElementById('outPersonalityText').innerText = res.text;
    document.getElementById('outPrimary').innerText = res.suger;
    document.getElementById('outAvoid').innerText = res.avoid;

    const collDiv = document.getElementById('outColleges');
    collDiv.innerHTML = '';
    res.colleges.forEach(c => {
        collDiv.innerHTML += `<div style="background:#fff; border:1px solid #ddd; padding:10px; border-radius:8px;"><strong>${c}</strong><br><small>Top matched institution</small></div>`;
    });

    document.getElementById('wizardContainer').style.display = 'none';
    document.getElementById('reportContainer').style.display = 'block';
    window.scrollTo({ top: 0, behavior: 'smooth' });
  }

  function downloadPDF() {
    const element = document.getElementById('reportContent');
    const name = document.getElementById('outName').innerText.replace(/\s+/g, '_');
    const opt = { margin: 0.5, filename: `Report_${name}.pdf`, image: { type: 'jpeg', quality: 0.98 }, html2canvas: { scale: 2 }, jsPDF: { unit: 'in', format: 'a4', orientation: 'portrait' } };
    html2pdf().set(opt).from(element).save();
  }
</script>
