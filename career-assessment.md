---
layout: default
title: "AI Career & Course Assessment 🎯"
permalink: /assessment/
description: "Comprehensive multi-step career analysis. Discover the right courses and colleges based on your unique abilities, environment preferences, and motivations."
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

  .container { max-width: 900px; margin: 0 auto; padding: 0 20px; }

  /* PROGRESS BAR */
  .progress-container { width: 100%; background: #e0e6ed; border-radius: 50px; height: 10px; margin-bottom: 30px; overflow: hidden; }
  .progress-bar { height: 100%; background: #e65100; width: 20%; transition: width 0.4s ease; }

  /* STEP WIZARD STYLES */
  .step-card {
    background: white; padding: 40px; border-radius: 12px;
    box-shadow: 0 10px 30px rgba(0,0,0,0.05); margin-bottom: 40px;
    display: none; animation: fadeIn 0.4s;
  }
  .step-card.active { display: block; }
  
  .step-title { font-size: 1.5rem; font-weight: 800; color: #0A2342; margin-bottom: 20px; text-align: center; }
  
  /* INPUTS */
  .form-input {
    width: 100%; padding: 15px; border: 2px solid #e0e6ed; border-radius: 8px;
    font-size: 1rem; color: #444; background: #fcfcfc; transition: all 0.3s; margin-bottom: 20px;
  }
  .form-input:focus { border-color: #1A5276; outline: none; background: white; }

  /* CLICKABLE OPTIONS GRID */
  .options-grid { display: grid; grid-template-columns: 1fr 1fr; gap: 15px; margin-bottom: 30px; }
  @media (max-width: 600px) { .options-grid { grid-template-columns: 1fr; } }
  
  .option-card {
    border: 2px solid #e0e6ed; border-radius: 10px; padding: 20px; cursor: pointer;
    transition: all 0.2s; background: #fafbfc; display: flex; flex-direction: column; align-items: center; text-align: center;
  }
  .option-card:hover { border-color: #1A5276; background: white; transform: translateY(-3px); box-shadow: 0 5px 15px rgba(0,0,0,0.05); }
  .option-card.selected { border-color: #e65100; background: #fff8f5; box-shadow: 0 0 0 2px rgba(230,81,0,0.2); }
  
  .opt-icon { font-size: 2rem; margin-bottom: 10px; }
  .opt-title { font-weight: 700; color: #0A2342; margin-bottom: 5px; }
  .opt-desc { font-size: 0.85rem; color: #666; }

  /* BUTTONS */
  .btn-nav-wrapper { display: flex; justify-content: space-between; gap: 15px; }
  .btn-main {
    background: #e65100; color: white; border: none; padding: 15px 30px;
    font-size: 1.1rem; font-weight: bold; border-radius: 50px; cursor: pointer; flex-grow: 1; transition: 0.3s;
  }
  .btn-main:hover { background: #bf360c; transform: translateY(-2px); box-shadow: 0 5px 15px rgba(230,81,0,0.3); }
  .btn-main:disabled { background: #ccc; cursor: not-allowed; transform: none; box-shadow: none; }
  
  .btn-back { background: #e0e6ed; color: #555; }
  .btn-back:hover { background: #cbd5e1; }

  /* REPORT STYLES */
  #reportContainer { display: none; }
  .report-card { background: white; padding: 50px; border-radius: 12px; box-shadow: 0 10px 30px rgba(0,0,0,0.08); margin-bottom: 40px; border-top: 8px solid #0A2342; }
  .report-header { border-bottom: 2px solid #eee; padding-bottom: 20px; margin-bottom: 30px; }
  .report-header h2 { color: #0A2342; margin: 0 0 5px 0; }
  .report-meta { color: #777; font-size: 0.95rem; }

  .analysis-section { margin-bottom: 30px; }
  .analysis-section h3 { color: #1A5276; font-size: 1.3rem; margin-bottom: 15px; display: flex; align-items: center; gap: 10px;}
  .analysis-text { line-height: 1.7; color: #444; font-size: 1.05rem; background: #f8fafd; padding: 20px; border-radius: 8px; border-left: 4px solid #1A5276; }
  .why-not-text { border-left-color: #e74c3c; background: #fdf8f8; }

  .college-recs { display: grid; grid-template-columns: 1fr 1fr; gap: 20px; margin-top: 20px; }
  .rec-card { background: #fff; border: 1px solid #ddd; padding: 20px; border-radius: 8px; box-shadow: 0 4px 10px rgba(0,0,0,0.02); }
  .rec-card h4 { margin: 0 0 10px 0; color: #0A2342; font-size: 1.1rem; }
  .rec-card p { margin: 0; color: #666; font-size: 0.9rem; line-height: 1.4; }

  .actions { text-align: center; margin-top: 30px; }
  .btn-download { background: #0A2342; color: white; border: none; padding: 12px 25px; font-size: 1rem; font-weight: bold; border-radius: 50px; cursor: pointer; transition: 0.3s; }
  .btn-download:hover { background: #1A5276; }

  @keyframes fadeIn { from { opacity: 0; transform: translateY(10px); } to { opacity: 1; transform: translateY(0); } }

  /* Print specific styles for PDF */
  @media print {
    body { background: white; }
    .actions, .assessment-header, .progress-container { display: none !important; }
    .report-card { box-shadow: none; border: none; padding: 0; }
  }
</style>

<div class="assessment-header">
  <h1>AI Career & Course Selector</h1>
  <p>Our intelligent engine analyzes your skills and motivations to recommend the perfect educational path.</p>
</div>

<div class="container">
  
  <div class="progress-container" id="progressWrapper">
    <div class="progress-bar" id="progressBar"></div>
  </div>

  <div id="wizardContainer">
    
    <div class="step-card active" id="step1">
      <h2 class="step-title">Let's start with the basics</h2>
      <input type="text" id="qName" class="form-input" placeholder="What is your full name?">
      
      <div class="options-grid" id="qLevel">
        <div class="option-card" onclick="selectOption('qLevel', 'Class 10')">
          <div class="opt-icon">🏫</div><div class="opt-title">Class 10</div><div class="opt-desc">Looking for streams (Sci/Comm/Arts)</div>
        </div>
        <div class="option-card" onclick="selectOption('qLevel', 'PUC')">
          <div class="opt-icon">📚</div><div class="opt-title">PUC / 12th</div><div class="opt-desc">Looking for UG Degrees</div>
        </div>
        <div class="option-card" onclick="selectOption('qLevel', 'UG')">
          <div class="opt-icon">🎓</div><div class="opt-title">Undergraduate</div><div class="opt-desc">Looking for Master's</div>
        </div>
        <div class="option-card" onclick="selectOption('qLevel', 'PG')">
          <div class="opt-icon">🔬</div><div class="opt-title">Postgraduate</div><div class="opt-desc">Looking for Ph.D / Research</div>
        </div>
      </div>
      <button class="btn-main" onclick="nextStep(2)">Next Step ➔</button>
    </div>

    <div class="step-card" id="step2">
      <h2 class="step-title">What is your strongest natural ability?</h2>
      <div class="options-grid" id="qSkill">
        <div class="option-card" onclick="selectOption('qSkill', 'math')">
          <div class="opt-icon">🧮</div><div class="opt-title">Logic & Numbers</div><div class="opt-desc">I am great at math, puzzles, and structure.</div>
        </div>
        <div class="option-card" onclick="selectOption('qSkill', 'spatial')">
          <div class="opt-icon">🎨</div><div class="opt-title">Visual & Spatial</div><div class="opt-desc">I think in pictures and have a great eye for design.</div>
        </div>
        <div class="option-card" onclick="selectOption('qSkill', 'communication')">
          <div class="opt-icon">🗣️</div><div class="opt-title">Empathy & Words</div><div class="opt-desc">I am great at reading people, writing, and debating.</div>
        </div>
        <div class="option-card" onclick="selectOption('qSkill', 'science')">
          <div class="opt-icon">🧬</div><div class="opt-title">Observation & Biology</div><div class="opt-desc">I am fascinated by nature, chemistry, and life systems.</div>
        </div>
      </div>
      <div class="btn-nav-wrapper">
        <button class="btn-main btn-back" onclick="prevStep(1)">⬅ Back</button>
        <button class="btn-main" onclick="nextStep(3)">Next Step ➔</button>
      </div>
    </div>

    <div class="step-card" id="step3">
      <h2 class="step-title">Where do you see yourself working?</h2>
      <div class="options-grid" id="qEnv">
        <div class="option-card" onclick="selectOption('qEnv', 'corporate')">
          <div class="opt-icon">🏢</div><div class="opt-title">Corporate Office</div><div class="opt-desc">Boardrooms, teams, and fast-paced environments.</div>
        </div>
        <div class="option-card" onclick="selectOption('qEnv', 'studio')">
          <div class="opt-icon">🖌️</div><div class="opt-title">Creative Studio</div><div class="opt-desc">Drafting tables, 3D models, and design tools.</div>
        </div>
        <div class="option-card" onclick="selectOption('qEnv', 'lab')">
          <div class="opt-icon">🧪</div><div class="opt-title">Research Lab / Clinic</div><div class="opt-desc">Quiet, controlled experiments or healthcare.</div>
        </div>
        <div class="option-card" onclick="selectOption('qEnv', 'field')">
          <div class="opt-icon">🏗️</div><div class="opt-title">On The Field</div><div class="opt-desc">Construction sites, outdoors, or on the move.</div>
        </div>
      </div>
      <div class="btn-nav-wrapper">
        <button class="btn-main btn-back" onclick="prevStep(2)">⬅ Back</button>
        <button class="btn-main" onclick="nextStep(4)">Next Step ➔</button>
      </div>
    </div>

    <div class="step-card" id="step4">
      <h2 class="step-title">What ultimately drives you?</h2>
      <div class="options-grid" id="qDrive">
        <div class="option-card" onclick="selectOption('qDrive', 'build')">
          <div class="opt-icon">⚙️</div><div class="opt-title">Building Systems</div><div class="opt-desc">I want to invent new tech and automate things.</div>
        </div>
        <div class="option-card" onclick="selectOption('qDrive', 'lead')">
          <div class="opt-icon">📈</div><div class="opt-title">Leadership & Wealth</div><div class="opt-desc">I want to scale businesses and lead organizations.</div>
        </div>
        <div class="option-card" onclick="selectOption('qDrive', 'help')">
          <div class="opt-icon">🤝</div><div class="opt-title">Advocacy & Helping</div><div class="opt-desc">I want to defend, heal, or improve society.</div>
        </div>
        <div class="option-card" onclick="selectOption('qDrive', 'discover')">
          <div class="opt-icon">🔭</div><div class="opt-title">Discovering Truths</div><div class="opt-desc">I want to push the boundaries of scientific knowledge.</div>
        </div>
      </div>
      <div class="btn-nav-wrapper">
        <button class="btn-main btn-back" onclick="prevStep(3)">⬅ Back</button>
        <button class="btn-main" onclick="generateReport()" style="background:#0A2342;">Generate Full Report ✨</button>
      </div>
    </div>

  </div>

  <div id="reportContainer">
    <div class="report-card" id="reportContent">
      
      <div class="report-header">
        <h2>Comprehensive Career Analysis Report</h2>
        <div class="report-meta">
          Prepared for: <strong id="outName">Student</strong> | Level: <strong id="outLevel">Level</strong> | Date: <span id="outDate"></span>
        </div>
      </div>

      <div class="analysis-section">
        <h3>✅ Recommended Path: <span id="outCourse" style="color:#e65100; margin-left: 5px;"></span></h3>
        <div class="analysis-text" id="outWhyThis"></div>
      </div>

      <div class="analysis-section">
        <h3>⚠️ Paths to Reconsider (Why Not Other Options)</h3>
        <div class="analysis-text why-not-text" id="outWhyNot"></div>
      </div>

      <div class="analysis-section">
        <h3>🏛️ Top Verified College Matches</h3>
        <p style="color: #666; margin-bottom: 15px;">Based on your profile, here are highly-rated institutions in our database that excel in your recommended field:</p>
        <div class="college-recs" id="outColleges"></div>
      </div>
      
      <div style="margin-top: 40px; text-align: center; border-top: 1px solid #eee; padding-top: 20px; font-size: 0.85rem; color: #888;">
        Report generated by The Knowledge Habitat Career Guidance System.
      </div>
    </div>

    <div class="actions">
      <button class="btn-download" onclick="downloadPDF()">📄 Download PDF Report</button>
      <button class="btn-download" style="background: white; color: #0A2342; border: 2px solid #0A2342; margin-left: 10px;" onclick="location.reload()">↺ Retake Assessment</button>
    </div>
  </div>

</div>

<script>
  // STATE MANAGEMENT
  let answers = { name: "", level: "", skill: "", env: "", drive: "" };

  // UI NAVIGATION
  function nextStep(step) {
    if(step === 2) answers.name = document.getElementById('qName').value || "Student";
    
    document.querySelectorAll('.step-card').forEach(c => c.classList.remove('active'));
    document.getElementById('step' + step).classList.add('active');
    document.getElementById('progressBar').style.width = (step * 25) + '%';
  }

  function prevStep(step) {
    document.querySelectorAll('.step-card').forEach(c => c.classList.remove('active'));
    document.getElementById('step' + step).classList.add('active');
    document.getElementById('progressBar').style.width = (step * 25) + '%';
  }

  function selectOption(group, value) {
    // Save answer
    let key = group.replace('q', '').toLowerCase();
    answers[key] = value;

    // Visual selection state
    let cards = document.getElementById(group).getElementsByClassName('option-card');
    for(let card of cards) { card.classList.remove('selected'); }
    event.currentTarget.classList.add('selected');
  }

  // LOGIC & KNOWLEDGE BASE
  const knowledgeBase = {
    tech: {
      title: "Engineering & Technology (CSE, AI, Core)",
      whyThis: "Your strong inclination towards logic, numbers, and building systems makes engineering an excellent fit. You thrive in structured environments where you can apply analytical reasoning. A degree in Technology, Artificial Intelligence, or Core Engineering will leverage your mindset to solve complex, real-world problems and automate the future.",
      whyNot: "A pure humanities or heavily empathetic role (like counseling) might feel subjective and frustrating to you. You prefer concrete answers and tangible outputs rather than theoretical debates without a definitive 'correct' answer.",
      colleges: [
        { name: "IIT Roorkee", desc: "Top-tier institution for rigorous engineering, AI, and excellent tech placements." },
        { name: "B.M.S. College of Engineering", desc: "India's first private engineering college, known for stellar CS and Core placements." },
        { name: "RV College of Engineering", desc: "Highly reputed for Computer Science, innovation, and industry ties." },
        { name: "Adichunchanagiri Institute of Technology", desc: "Specialized streams in Robotics, AI, and Data Science." }
      ]
    },
    design: {
      title: "Architecture & Spatial Design (B.Arch)",
      whyThis: "You possess a unique blend of spatial awareness and creativity. Architecture and Design will allow you to channel your out-of-the-box thinking into tangible, structural realities. This field satisfies your need for both visual aesthetics and functional, real-world application.",
      whyNot: "A standard corporate Management desk job or a pure coding degree may stifle your creativity. Those fields often rely on rigid frameworks, whereas you need a studio environment that rewards visual mapping and spatial innovation.",
      colleges: [
        { name: "Aditya Academy of Architecture (AAAD)", desc: "Specializes in B.Arch and Interior Design with great studio culture." },
        { name: "Gopalan School of Architecture (GSAP)", desc: "Focuses heavily on sustainable environments and construction management." },
        { name: "East West School of Architecture (EWSA)", desc: "Dedicated campus for extensive 5-year B.Arch training." }
      ]
    },
    business: {
      title: "Business Management (BBA / MBA)",
      whyThis: "Your profile indicates a strong affinity for people, systems, and leadership. Management studies will train you to lead teams, optimize resources, and understand market dynamics. Your drive for growth and corporate environments works perfectly for navigating business challenges and driving wealth.",
      whyNot: "A heavily isolated research role or pure coding job would likely cause burnout. You draw energy from interaction, negotiation, and dynamic team environments, making solitary lab work unsuitable for your long-term ambitions.",
      colleges: [
        { name: "Christ (Deemed to be University)", desc: "Renowned globally for its rigorous Management, BBA, and MBA programs." },
        { name: "Jain University", desc: "Strong focus on entrepreneurship, sports, and business incubation." },
        { name: "Mount Carmel College", desc: "Excellent commerce and management faculties with a holistic approach." }
      ]
    },
    science: {
      title: "Pure Sciences & Research (B.Sc Research / M.Sc)",
      whyThis: "Your deep curiosity and analytical nature make you a natural fit for fundamental sciences. You are driven by discovering the 'why' behind phenomena rather than just applying them. A track in physics, chemistry, or applied mathematics allows you to engage in long-term research and discovery.",
      whyNot: "Fast-paced corporate degrees or target-driven sales roles might frustrate you. You value deep, thorough understanding and rigorous scientific truth over quick, commercial fixes or quarterly profit goals.",
      colleges: [
        { name: "Indian Institute of Science (IISc)", desc: "India's undisputed #1 institute for advanced scientific research." },
        { name: "St. Joseph's University", desc: "Heritage institution with highly respected basic science and humanities departments." },
        { name: "IIT Roorkee", desc: "Offers excellent integrated M.Sc programs and advanced laboratories." }
      ]
    },
    humanities: {
      title: "Humanities, Law & Psychology",
      whyThis: "You have a high degree of empathy and exceptional communication skills. You are driven by advocacy, understanding society, and helping people. Pursuing Law, Psychology, or Sociology will allow you to critically analyze human behavior and influence public policy or individual well-being.",
      whyNot: "A math-heavy engineering curriculum or a purely technical path ignores your strongest asset: your emotional intelligence. You need a career that deals with human nuance, not just machines.",
      colleges: [
        { name: "Kirit P. Mehta School of Law (NMIMS)", desc: "Top-tier private law school known for rigorous curriculum and Moot Courts." },
        { name: "Christ (Deemed to be University)", desc: "Exceptional programs in Law, Psychology, and Social Sciences." },
        { name: "Mount Carmel College", desc: "Known for an empowering culture and excellence in Arts & Humanities." }
      ]
    },
    bio: {
      title: "Biosciences, Medicine & Allied Health",
      whyThis: "Your fascination with life systems combined with a drive to help or discover makes the biosciences perfect for you. Whether it's clinical medicine, biotechnology, or genetics, this path allows you to work in labs or clinics to directly impact biological understanding and human health.",
      whyNot: "Fields like pure Corporate Finance or Civil Architecture lack the biological and human-health impact you crave. You are better suited to environments focused on living organisms and chemical interactions.",
      colleges: [
        { name: "Indian Institute of Science (IISc)", desc: "Premier biological and interdisciplinary bioengineering research." },
        { name: "IIT Roorkee", desc: "Offers specialized B.Tech and M.Tech in Biosciences and Bioengineering." },
        { name: "Mount Carmel College", desc: "Highly rated undergraduate programs in Life Sciences and Biotechnology." }
      ]
    }
  };

  // CALCULATE RESULTS
  function calculateResult() {
    let scores = { tech: 0, design: 0, business: 0, science: 0, humanities: 0, bio: 0 };
    
    // Evaluate Skill
    if(answers.skill === 'math') { scores.tech += 3; scores.science += 1; scores.business += 1; }
    if(answers.skill === 'spatial') { scores.design += 3; scores.tech += 1; }
    if(answers.skill === 'communication') { scores.humanities += 3; scores.business += 2; }
    if(answers.skill === 'science') { scores.bio += 3; scores.science += 2; }

    // Evaluate Env
    if(answers.env === 'corporate') { scores.business += 3; scores.tech += 1; }
    if(answers.env === 'studio') { scores.design += 3; }
    if(answers.env === 'lab') { scores.science += 3; scores.bio += 2; }
    if(answers.env === 'field') { scores.design += 1; scores.tech += 1; scores.bio += 1; }

    // Evaluate Drive
    if(answers.drive === 'build') { scores.tech += 3; }
    if(answers.drive === 'lead') { scores.business += 3; scores.humanities += 1; }
    if(answers.drive === 'help') { scores.humanities += 3; scores.bio += 2; }
    if(answers.drive === 'discover') { scores.science += 3; scores.bio += 1; scores.tech += 1; }

    // Find Winner
    let winner = Object.keys(scores).reduce((a, b) => scores[a] > scores[b] ? a : b);
    return winner;
  }

  function generateReport() {
    // Validation
    if(!answers.level || !answers.skill || !answers.env || !answers.drive) {
      alert("Please ensure you select an option on all steps!");
      return;
    }

    const winnerKey = calculateResult();
    const resultData = knowledgeBase[winnerKey];

    // Populate Report
    document.getElementById('outName').innerText = answers.name;
    document.getElementById('outLevel').innerText = answers.level;
    document.getElementById('outDate').innerText = new Date().toLocaleDateString();
    
    // Adjust title slightly based on Level
    let finalTitle = resultData.title;
    if(answers.level === "PG" || answers.level === "UG") {
      finalTitle = finalTitle.replace("B.Arch", "M.Arch").replace("BBA", "MBA").replace("B.Sc", "M.Sc").replace("CSE", "M.Tech CSE");
    }
    document.getElementById('outCourse').innerText = finalTitle;
    document.getElementById('outWhyThis').innerText = resultData.whyThis;
    document.getElementById('outWhyNot').innerText = resultData.whyNot;

    // Populate Colleges
    const collegeContainer = document.getElementById('outColleges');
    collegeContainer.innerHTML = ''; 
    resultData.colleges.forEach(college => {
      collegeContainer.innerHTML += `
        <div class="rec-card">
          <h4>${college.name}</h4>
          <p>${college.desc}</p>
        </div>
      `;
    });

    // Hide Wizard, Show Report
    document.getElementById('progressWrapper').style.display = 'none';
    document.getElementById('wizardContainer').style.display = 'none';
    document.getElementById('reportContainer').style.display = 'block';
    
    window.scrollTo({ top: 0, behavior: 'smooth' });
  }

  // PDF GENERATOR
  function downloadPDF() {
    const element = document.getElementById('reportContent');
    const name = document.getElementById('outName').innerText.replace(/\s+/g, '_');
    
    const opt = {
      margin:       0.5,
      filename:     `Career_Analysis_${name}.pdf`,
      image:        { type: 'jpeg', quality: 0.98 },
      html2canvas:  { scale: 2, useCORS: true },
      jsPDF:        { unit: 'in', format: 'a4', orientation: 'portrait' }
    };

    html2pdf().set(opt).from(element).save();
  }
</script>
