---
layout: default
title: "AI Stream Selector 🧭"
permalink: /stream-selector/
image: "/assets/images/stream-preview.png"
description: "Not just a career test. A psychometric engine to predict your perfect stream based on aptitude, tolerance, and motivation."
---

<style>
  /* 1. LAYOUT & RESET */
  .main-content {
    max-width: 100% !important;
    padding: 0 !important;
    margin: 0 !important;
  }
  
  body { 
    background-color: #f0f2f5; 
    font-family: 'Segoe UI', Helvetica, Arial, sans-serif;
    color: #333;
  }

  /* 2. PROGRESS BAR */
  .progress-container {
    position: fixed;
    top: 60px; /* Adjust based on your nav height */
    left: 0;
    width: 100%;
    height: 6px;
    background: #e0e0e0;
    z-index: 100;
  }

  .progress-bar {
    height: 100%;
    background: linear-gradient(90deg, #D4AF37, #f6e05e);
    width: 0%;
    transition: width 0.4s ease;
  }

  /* 3. QUIZ CONTAINER */
  .quiz-wrapper {
    max-width: 800px;
    margin: 100px auto 60px;
    padding: 20px;
    min-height: 60vh;
    display: flex;
    flex-direction: column;
    justify-content: center;
  }

  .question-card {
    background: white;
    padding: 40px;
    border-radius: 20px;
    box-shadow: 0 10px 40px rgba(0,0,0,0.08);
    text-align: center;
    animation: fadeIn 0.5s ease;
  }

  @keyframes fadeIn {
    from { opacity: 0; transform: translateY(10px); }
    to { opacity: 1; transform: translateY(0); }
  }

  .q-category {
    text-transform: uppercase;
    font-size: 0.85rem;
    letter-spacing: 1.5px;
    color: #888;
    margin-bottom: 10px;
    font-weight: 700;
  }

  .q-text {
    font-size: 1.8rem;
    color: #0A2342;
    margin-bottom: 30px;
    font-weight: 700;
  }

  .options-grid {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 15px;
  }

  @media (max-width: 600px) {
    .options-grid { grid-template-columns: 1fr; }
    .q-text { font-size: 1.4rem; }
  }

  .option-btn {
    background: #f8f9fa;
    border: 2px solid #e9ecef;
    padding: 20px;
    border-radius: 12px;
    font-size: 1.1rem;
    color: #555;
    cursor: pointer;
    transition: all 0.2s;
    font-weight: 500;
  }

  .option-btn:hover {
    background: #e3f2fd;
    border-color: #0A2342;
    color: #0A2342;
    transform: translateY(-2px);
  }

  /* 4. RESULTS SECTION (Hidden by default) */
  .result-container {
    display: none;
    max-width: 1000px;
    margin: 80px auto;
    padding: 20px;
  }

  .result-header {
    text-align: center;
    margin-bottom: 40px;
  }

  .stream-badge {
    background: #0A2342;
    color: #FFD700;
    padding: 10px 30px;
    border-radius: 50px;
    font-size: 1.2rem;
    font-weight: bold;
    display: inline-block;
    margin-bottom: 20px;
    box-shadow: 0 4px 15px rgba(10, 35, 66, 0.3);
  }

  .stream-title {
    font-size: 3rem;
    color: #0A2342;
    margin: 0;
  }

  /* 5. REPORT CARDS (Student, Parent, School) */
  .report-tabs {
    display: flex;
    justify-content: center;
    gap: 10px;
    margin-bottom: 30px;
    flex-wrap: wrap;
  }

  .report-tab-btn {
    padding: 12px 25px;
    border: none;
    background: white;
    border-radius: 50px;
    font-weight: bold;
    color: #555;
    cursor: pointer;
    box-shadow: 0 4px 10px rgba(0,0,0,0.05);
    transition: 0.3s;
  }

  .report-tab-btn.active {
    background: #0A2342;
    color: white;
  }

  .report-section {
    display: none;
    animation: fadeIn 0.4s;
  }
  .report-section.active { display: block; }

  /* Student Report Styles */
  .student-box {
    background: white;
    padding: 40px;
    border-radius: 15px;
    box-shadow: 0 5px 20px rgba(0,0,0,0.05);
  }

  .analysis-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
    gap: 30px;
    margin-top: 30px;
  }

  .analysis-item {
    background: #f8f9fa;
    padding: 20px;
    border-radius: 10px;
    border-left: 4px solid #D4AF37;
  }

  .analysis-item h4 { margin: 0 0 10px 0; color: #0A2342; }

  /* Parent Report Styles (PDF Look) */
  .pdf-paper {
    background: white;
    padding: 50px;
    border: 1px solid #ddd;
    max-width: 800px;
    margin: 0 auto;
    font-family: 'Georgia', serif; /* Document feel */
  }
  
  .pdf-header { border-bottom: 2px solid #333; padding-bottom: 20px; margin-bottom: 30px; }
  .pdf-row { display: flex; justify-content: space-between; margin-bottom: 10px; border-bottom: 1px dotted #ccc; padding-bottom: 5px; }

  /* School Dashboard Styles */
  .dashboard-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
    gap: 20px;
    margin-bottom: 30px;
  }

  .stat-card {
    background: white;
    padding: 20px;
    border-radius: 10px;
    text-align: center;
    box-shadow: 0 2px 10px rgba(0,0,0,0.05);
  }
  
  .stat-num { font-size: 2.5rem; font-weight: bold; color: #0A2342; }
  .stat-label { font-size: 0.9rem; color: #666; text-transform: uppercase; }

  .flag-table {
    width: 100%;
    border-collapse: collapse;
    background: white;
    box-shadow: 0 2px 10px rgba(0,0,0,0.05);
  }
  
  .flag-table th, .flag-table td { padding: 15px; text-align: left; border-bottom: 1px solid #eee; }
  .flag-table th { background: #0A2342; color: white; }
  .flag-tag { padding: 4px 8px; border-radius: 4px; font-size: 0.8rem; font-weight: bold; }
  .flag-red { background: #ffebee; color: #c62828; }
  .flag-yellow { background: #fffde7; color: #f9a825; }

</style>

<div class="progress-container"><div class="progress-bar" id="progressBar"></div></div>

<div class="quiz-wrapper" id="quizBox">
  <div class="question-card">
    <div class="q-category" id="qCategory">Category</div>
    <div class="q-text" id="qText">Loading Question...</div>
    <div class="options-grid" id="optionsBox">
      </div>
  </div>
</div>

<div class="result-container" id="resultBox">
  
  <div class="result-header">
    <div class="stream-badge">Assessment Complete</div>
    <h1 class="stream-title" id="finalStreamTitle">Stream Name</h1>
    <p style="font-size:1.2rem; color:#666; margin-top:10px;">Based on your aptitude, tolerance, and motivation.</p>
  </div>

  <div class="report-tabs">
    <button class="report-tab-btn active" onclick="showTab('student')">👨‍🎓 Student Result</button>
    <button class="report-tab-btn" onclick="showTab('parent')">👪 Parent Report</button>
    <button class="report-tab-btn" onclick="showTab('school')">🏫 School Dashboard</button>
  </div>

  <div id="student" class="report-section active">
    <div class="student-box">
      <h2 style="color:#0A2342; margin-top:0;">Why this suits you</h2>
      <p id="studentWhy" style="font-size:1.1rem; line-height:1.6;">Reasoning goes here...</p>
      
      <div class="analysis-grid">
        <div class="analysis-item">
          <h4>🔥 Natural Strengths</h4>
          <p id="studentStrengths">...</p>
        </div>
        <div class="analysis-item">
          <h4>⚠️ Possible Struggles</h4>
          <p id="studentStruggles">...</p>
        </div>
        <div class="analysis-item">
          <h4>🚀 Career Directions</h4>
          <p id="studentCareers">...</p>
        </div>
      </div>
      
      <div style="margin-top:30px; padding:20px; background:#e3f2fd; border-radius:10px;">
        <strong>💡 Good Alternative:</strong> <span id="studentAlt">Alternative Stream</span>
      </div>

      <div style="text-align:center; margin-top:40px;">
        <p style="font-style:italic; color:#666;">"This is not locking your future. It shows where you are most likely to succeed with least struggle."</p>
        <a href="{{ '/book-expert/' | relative_url }}" class="option-btn" style="background:#0A2342; color:white; display:inline-block; text-decoration:none; margin-top:10px;">Talk to a Counsellor</a>
      </div>
    </div>
  </div>

  <div id="parent" class="report-section">
    <div class="pdf-paper">
      <div class="pdf-header">
        <h2 style="margin:0;">CONFIDENTIAL PARENT REPORT</h2>
        <p style="margin:5px 0 0 0; color:#666;">Automated Psychometric Analysis</p>
      </div>

      <h3>1. Student Profile Summary</h3>
      <div class="pdf-row"><span>Learning Style:</span><strong id="pdfStyle">...</strong></div>
      <div class="pdf-row"><span>Effort Tolerance:</span><strong id="pdfEffort">...</strong></div>
      <div class="pdf-row"><span>Academic Pressure:</span><strong id="pdfPressure">...</strong></div>

      <h3>2. Risk Analysis (If wrong stream chosen)</h3>
      <p id="pdfRisk" style="font-size:0.95rem; line-height:1.5; color:#444;">...</p>

      <h3>3. 12-Month Action Plan</h3>
      <ul style="font-size:0.95rem; line-height:1.6;">
        <li><strong>Month 1-2:</strong> Career awareness videos & discussions.</li>
        <li><strong>Month 3-4:</strong> Basic skill exploration (internships/shadowing).</li>
        <li><strong>Month 5-8:</strong> Begin structured learning aligned with recommended stream.</li>
      </ul>

      <div style="margin-top:40px; border-top:1px solid #ddd; padding-top:10px; font-size:0.8rem; color:#888;">
        <strong>Note:</strong> This assessment indicates suitability, not ability. Students can succeed in any stream with sustained motivation, but mismatch increases stress.
      </div>
    </div>
  </div>

  <div id="school" class="report-section">
    <div style="background:#0A2342; color:white; padding:20px; border-radius:10px 10px 0 0;">
      <h2 style="margin:0;">Admin Console: Class 10-A</h2>
      <p style="margin:5px 0 0 0; opacity:0.8;">Live Psychometric Data Overview</p>
    </div>
    
    <div style="background:white; padding:30px; border-radius:0 0 10px 10px; box-shadow:0 5px 20px rgba(0,0,0,0.05);">
      
      <h3>Class Overview</h3>
      <div class="dashboard-grid">
        <div class="stat-card">
          <div class="stat-num" style="color:#3182ce;">38%</div>
          <div class="stat-label">Science Inclination</div>
        </div>
        <div class="stat-card">
          <div class="stat-num" style="color:#d69e2e;">34%</div>
          <div class="stat-label">Commerce Inclination</div>
        </div>
        <div class="stat-card">
          <div class="stat-num" style="color:#805ad5;">18%</div>
          <div class="stat-label">Arts Inclination</div>
        </div>
      </div>

      <h3>⚠️ Priority Student Flags (Counsellor Action Required)</h3>
      <table class="flag-table">
        <thead>
          <tr>
            <th>Student ID</th>
            <th>Flag Type</th>
            <th>Recommended Action</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td>#ST-204 (Current User)</td>
            <td><span class="flag-tag flag-yellow">Stream Clarity Check</span></td>
            <td>Verify motivation vs aptitude</td>
          </tr>
          <tr>
            <td>#ST-199</td>
            <td><span class="flag-tag flag-red">High Burnout Risk</span></td>
            <td>Parent meeting required</td>
          </tr>
          <tr>
            <td>#ST-215</td>
            <td><span class="flag-tag flag-yellow">Under-Challenged</span></td>
            <td>Encourage Olympiads</td>
          </tr>
        </tbody>
      </table>

      <p style="margin-top:20px; color:#666; font-size:0.9rem;">
        <em>“This data does not predict marks. It predicts learning comfort.”</em>
      </p>
    </div>
  </div>

</div>

<script>
  // --- CONFIGURATION ---
  const questions = [
    // SECTION 1: LEARNING BRAIN
    {
      cat: "Learning Brain Type",
      text: "Which class feels fastest for you?",
      options: [
        { t: "Solving numerical problems", s: {sci:3, comm:1, arts:0, skill:0} },
        { t: "Understanding concepts", s: {sci:2, comm:1, arts:2, skill:0} },
        { t: "Discussions & opinions", s: {sci:0, comm:1, arts:3, skill:0} },
        { t: "Activities/projects", s: {sci:0, comm:0, arts:1, skill:3} }
      ]
    },
    {
      cat: "Learning Brain Type",
      text: "If exams had no marks, which would you still enjoy?",
      options: [
        { t: "Maths / logical puzzles", s: {sci:3, comm:1, arts:0, skill:0} },
        { t: "Business / money topics", s: {sci:0, comm:3, arts:1, skill:0} },
        { t: "Social issues / psychology", s: {sci:0, comm:1, arts:3, skill:0} },
        { t: "Making things / practical", s: {sci:0, comm:0, arts:0, skill:3} }
      ]
    },
    {
      cat: "Learning Brain Type",
      text: "You learn best by:",
      options: [
        { t: "Practicing problems", s: {sci:3, comm:1, arts:0, skill:0} },
        { t: "Understanding theory", s: {sci:1, comm:1, arts:3, skill:0} },
        { t: "Talking & debating", s: {sci:0, comm:1, arts:3, skill:0} },
        { t: "Doing hands-on", s: {sci:0, comm:0, arts:0, skill:3} }
      ]
    },
    {
      cat: "Learning Brain Type",
      text: "Which homework do you delay the most? (Reverse Scored)",
      options: [
        { t: "Long calculations", s: {sci:0, comm:1, arts:1, skill:2} },
        { t: "Long theory answers", s: {sci:2, comm:2, arts:0, skill:1} },
        { t: "Presentations", s: {sci:2, comm:1, arts:0, skill:1} },
        { t: "Lab / craft work", s: {sci:2, comm:2, arts:2, skill:0} }
      ]
    },
    // SECTION 2: TOLERANCE
    {
      cat: "Difficulty Tolerance",
      text: "Can you study the same topic daily for 2 years?",
      options: [
        { t: "Yes comfortably", s: {sci:3, comm:2, arts:2, skill:0} },
        { t: "Only if interesting", s: {sci:1, comm:2, arts:2, skill:1} },
        { t: "I get bored quickly", s: {sci:0, comm:0, arts:1, skill:3} }
      ]
    },
    {
      cat: "Difficulty Tolerance",
      text: "Your reaction to tough problems:",
      options: [
        { t: "I keep trying", s: {sci:3, comm:2, arts:1, skill:0} },
        { t: "I try later", s: {sci:1, comm:2, arts:2, skill:1} },
        { t: "I avoid", s: {sci:0, comm:0, arts:1, skill:3} }
      ]
    },
    {
      cat: "Difficulty Tolerance",
      text: "How many hours can you realistically study daily?",
      options: [
        { t: "5+ hours", s: {sci:3, comm:2, arts:2, skill:0} },
        { t: "2–4 hours", s: {sci:1, comm:3, arts:2, skill:1} },
        { t: "Less than 2 hours", s: {sci:0, comm:0, arts:1, skill:3} }
      ]
    },
    {
      cat: "Difficulty Tolerance",
      text: "Do competitive exams scare you?",
      options: [
        { t: "No", s: {sci:3, comm:2, arts:2, skill:0} },
        { t: "A little", s: {sci:1, comm:2, arts:2, skill:1} },
        { t: "Very much", s: {sci:0, comm:0, arts:1, skill:3} }
      ]
    },
    // SECTION 3: MOTIVATION
    {
      cat: "Career Motivation",
      text: "Which life sounds better?",
      options: [
        { t: "High salary after struggle", s: {sci:2, comm:3, arts:1, skill:1} },
        { t: "Balanced life", s: {sci:1, comm:3, arts:2, skill:1} },
        { t: "Freedom & creativity", s: {sci:0, comm:1, arts:3, skill:1} },
        { t: "Earn early", s: {sci:0, comm:0, arts:1, skill:3} }
      ]
    },
    {
      cat: "Career Motivation",
      text: "You would rather work:",
      options: [
        { t: "With machines or tech", s: {sci:3, comm:0, arts:0, skill:1} },
        { t: "With money or business", s: {sci:0, comm:3, arts:1, skill:0} },
        { t: "With people", s: {sci:0, comm:1, arts:3, skill:0} },
        { t: "With tools or skills", s: {sci:0, comm:0, arts:0, skill:3} }
      ]
    },
    {
      cat: "Career Motivation",
      text: "What feels satisfying?",
      options: [
        { t: "Solving tough problems", s: {sci:3, comm:1, arts:0, skill:0} },
        { t: "Planning things", s: {sci:1, comm:3, arts:1, skill:0} },
        { t: "Helping others", s: {sci:0, comm:1, arts:3, skill:0} },
        { t: "Building something", s: {sci:0, comm:0, arts:0, skill:3} }
      ]
    },
    // SECTION 4: PERSONALITY
    {
      cat: "Personality Fit",
      text: "Friends ask you for help in:",
      options: [
        { t: "Studies", s: {sci:3, comm:1, arts:1, skill:0} },
        { t: "Advice", s: {sci:0, comm:1, arts:3, skill:0} },
        { t: "Ideas", s: {sci:0, comm:2, arts:2, skill:0} },
        { t: "Fixing things", s: {sci:0, comm:0, arts:0, skill:3} }
      ]
    },
    {
      cat: "Personality Fit",
      text: "You prefer instructions that are:",
      options: [
        { t: "Exact steps", s: {sci:3, comm:1, arts:0, skill:1} },
        { t: "Clear concepts", s: {sci:2, comm:2, arts:2, skill:0} },
        { t: "Flexible", s: {sci:0, comm:2, arts:3, skill:0} },
        { t: "Learn by doing", s: {sci:0, comm:0, arts:0, skill:3} }
      ]
    },
    {
      cat: "Personality Fit",
      text: "Your patience level:",
      options: [
        { t: "Very patient", s: {sci:3, comm:2, arts:2, skill:0} },
        { t: "Moderate", s: {sci:1, comm:3, arts:2, skill:1} },
        { t: "Low", s: {sci:0, comm:0, arts:1, skill:3} }
      ]
    },
    {
      cat: "Personality Fit",
      text: "If forced to attend a 3-hour class daily:",
      options: [
        { t: "I can manage", s: {sci:3, comm:2, arts:2, skill:0} },
        { t: "Sometimes difficult", s: {sci:1, comm:3, arts:2, skill:1} },
        { t: "Impossible", s: {sci:0, comm:0, arts:1, skill:3} }
      ]
    }
  ];

  let currentQ = 0;
  let scores = { sci: 0, comm: 0, arts: 0, skill: 0 };

  function renderQuestion() {
    const q = questions[currentQ];
    document.getElementById('qCategory').innerText = `${q.cat} (${currentQ + 1}/${questions.length})`;
    document.getElementById('qText').innerText = q.text;
    
    const optionsHtml = q.options.map((opt, index) => 
      `<div class="option-btn" onclick="handleAnswer(${index})">${opt.t}</div>`
    ).join('');
    
    document.getElementById('optionsBox').innerHTML = optionsHtml;
    document.getElementById('progressBar').style.width = `${((currentQ) / questions.length) * 100}%`;
  }

  function handleAnswer(optIndex) {
    const pts = questions[currentQ].options[optIndex].s;
    scores.sci += pts.sci;
    scores.comm += pts.comm;
    scores.arts += pts.arts;
    scores.skill += pts.skill;

    currentQ++;
    if (currentQ < questions.length) {
      renderQuestion();
    } else {
      showResults();
    }
  }

  function showResults() {
    document.getElementById('quizBox').style.display = 'none';
    document.getElementById('resultBox').style.display = 'block';
    document.getElementById('progressBar').style.width = '100%';

    // --- DECISION LOGIC ---
    // 1. Find Highest
    let results = [
      { id: 'sci', val: scores.sci, name: 'Science' },
      { id: 'comm', val: scores.comm, name: 'Commerce' },
      { id: 'arts', val: scores.arts, name: 'Arts/Humanities' },
      { id: 'skill', val: scores.skill, name: 'Skill/Diploma' }
    ];
    results.sort((a, b) => b.val - a.val);

    const best = results[0];
    const second = results[1];

    let finalTitle = best.name;
    let subtitle = "";

    // 1.2x Logic
    if (best.val >= second.val * 1.2) {
      subtitle = "Strong Recommendation";
    } else {
      subtitle = `Close match with ${second.name}`;
      finalTitle = `${best.name} (or ${second.name})`;
    }

    document.getElementById('finalStreamTitle').innerText = finalTitle;

    // --- POPULATE TEXT CONTENT (DATA FROM PROMPT) ---
    const content = {
      'sci': {
        why: "You show strong problem-solving ability, patience and comfort with challenging subjects. You don’t easily give up when concepts are difficult and you are willing to study consistently over long periods.",
        strength: "Logical thinking, Handling pressure, Long-term focus.",
        struggle: "Rote memorisation, Careers with too much uncertainty.",
        career: "Engineering, Medicine, Research, Data Science, Defence.",
        alt: "Commerce with Maths",
        risk: "May experience chronic academic stress if not motivated."
      },
      'comm': {
        why: "You show an analytical but practical thinking style. You prefer understanding systems like money, business and planning rather than heavy theoretical memorisation. You balance effort and results well.",
        strength: "Decision making, Planning & organisation, Understanding real-world applications.",
        struggle: "Extremely technical subjects, Highly unpredictable creative careers.",
        career: "Finance, Business, Law, Banking, Marketing.",
        alt: "Arts with Economics",
        risk: "Likely disengagement if forced into Science."
      },
      'arts': {
        why: "You think in ideas, opinions and understanding people rather than formulas. You learn best through discussion, interpretation and meaning-based learning.",
        strength: "Communication, Critical thinking, Understanding behaviour, Creativity.",
        struggle: "Highly repetitive numerical practice, Mechanical learning environments.",
        career: "Psychology, Law, Civil Services, Design, Media.",
        alt: "Commerce without Maths",
        risk: "Possible under-stimulation in rigid streams."
      },
      'skill': {
        why: "You learn best by doing rather than long academic study. You prefer practical work and quicker entry into real-world environments. You show lower tolerance for long exam-based preparation.",
        strength: "Hands-on learning, Real-world problem solving, Quick adaptation.",
        struggle: "Long theory courses, Competitive academic exams.",
        career: "Technical trades, Design, Animation, Hotel Management.",
        alt: "Commerce with Vocational subjects",
        risk: "High frustration with formal education structures."
      }
    };

    const c = content[best.id];

    // Student Tab
    document.getElementById('studentWhy').innerText = c.why;
    document.getElementById('studentStrengths').innerText = c.strength;
    document.getElementById('studentStruggles').innerText = c.struggle;
    document.getElementById('studentCareers').innerText = c.career;
    document.getElementById('studentAlt').innerText = c.alt;

    // Parent Tab (Simulated PDF Data)
    document.getElementById('pdfStyle').innerText = best.id === 'skill' ? "Kinesthetic (Hands-on)" : "Analytical/Conceptual";
    document.getElementById('pdfEffort').innerText = scores.sci > 30 ? "High" : "Moderate";
    document.getElementById('pdfPressure').innerText = scores.sci > 30 ? "High Resilience" : "Balanced Preference";
    document.getElementById('pdfRisk').innerText = c.risk;
  }

  function showTab(tabId) {
    document.querySelectorAll('.report-section').forEach(el => el.classList.remove('active'));
    document.querySelectorAll('.report-tab-btn').forEach(el => el.classList.remove('active'));
    
    document.getElementById(tabId).classList.add('active');
    event.currentTarget.classList.add('active');
  }

  // Start
  renderQuestion();
</script>
