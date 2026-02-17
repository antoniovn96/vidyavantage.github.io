---
layout: default
title: "Jain (Deemed-to-be University) Course Portal 🎓"
permalink: /colleges/jain-university/
image: "https://www.jainuniversity.ac.in/uploads/blog/e856868d40026e690069352693821033.jpg"
description: "Browse 100+ courses at Jain University (Engineering, Management, Design, Law). Check 2025 JET Exam, Fees, and Placements."
---

<meta property="og:title" content="Jain University Course Portal 🎓">
<meta property="og:description" content="Access details for B.Tech, MBA, B.Des, BCA, and more. Check Eligibility, Fees, and Career Outcomes.">
<meta property="og:image" content="https://www.jainuniversity.ac.in/uploads/blog/e856868d40026e690069352693821033.jpg">

<style>
  /* 1. LAYOUT RESET */
  .main-content { max-width: 100% !important; padding: 0 !important; margin: 0 !important; }
  body { background-color: #f4f6f8; font-family: 'Segoe UI', system-ui, sans-serif; color: #333; }

  /* 2. HERO SECTION */
  .jain-hero {
    background: linear-gradient(rgba(255, 152, 0, 0.9), rgba(230, 81, 0, 0.8)), url('https://www.jainuniversity.ac.in/uploads/blog/e856868d40026e690069352693821033.jpg');
    background-size: cover;
    background-position: center;
    color: white;
    text-align: center;
    padding: 80px 20px;
    margin-bottom: 0;
  }
  
  .jain-hero h1 { font-size: 2.8rem; margin: 0; font-weight: 800; color: white !important; }
  .jain-hero p { font-size: 1.1rem; color: #fff !important; margin-top: 10px; max-width: 700px; margin-left: auto; margin-right: auto; }

  /* 3. APP CONTAINER */
  .app-container {
    max-width: 1300px;
    margin: 0 auto;
    display: flex;
    gap: 30px;
    padding: 30px 20px;
    align-items: flex-start;
  }

  /* 4. SIDEBAR FILTERS */
  .filters-sidebar {
    width: 280px;
    background: white;
    padding: 25px;
    border-radius: 12px;
    box-shadow: 0 5px 20px rgba(0,0,0,0.05);
    position: sticky;
    top: 90px;
    border-top: 4px solid #e65100; /* Jain Orange */
    flex-shrink: 0;
  }

  .filter-group { margin-bottom: 20px; }
  .filter-label { display: block; font-weight: 700; margin-bottom: 8px; color: #e65100; font-size: 0.9rem; }
  
  .filter-input, .filter-select {
    width: 100%;
    padding: 10px 15px;
    border: 1px solid #ddd;
    border-radius: 8px;
    font-size: 0.95rem;
    outline: none;
    transition: border 0.2s;
  }
  .filter-input:focus, .filter-select:focus { border-color: #e65100; }

  /* 5. COURSE GRID */
  .results-area { flex-grow: 1; }
  
  .course-grid {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
    gap: 20px;
  }

  .course-card {
    background: white;
    border-radius: 10px;
    padding: 20px;
    border-left: 4px solid #ddd;
    box-shadow: 0 4px 10px rgba(0,0,0,0.03);
    transition: transform 0.2s, box-shadow 0.2s;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
  }
  .course-card:hover { transform: translateY(-3px); box-shadow: 0 8px 25px rgba(0,0,0,0.08); border-left-color: #e65100; }

  /* School Colors */
  .school-Engg { border-left-color: #2196f3; }
  .school-Mgmt { border-left-color: #9c27b0; }
  .school-Design { border-left-color: #e91e63; }
  .school-Science { border-left-color: #4caf50; }
  .school-Commerce { border-left-color: #ff9800; }
  .school-Law { border-left-color: #795548; }

  .c-school { font-size: 0.75rem; text-transform: uppercase; font-weight: 700; color: #888; margin-bottom: 5px; }
  .c-title { font-size: 1.1rem; font-weight: 700; color: #333; margin: 0 0 10px 0; line-height: 1.4; }
  .c-meta { display: flex; gap: 8px; flex-wrap: wrap; margin-bottom: 15px; }
  .c-badge { display: inline-block; background: #f0f2f5; padding: 4px 10px; border-radius: 4px; font-size: 0.75rem; font-weight: 600; color: #555; }
  
  .c-footer { margin-top: auto; display: flex; justify-content: space-between; align-items: center; border-top: 1px solid #f0f0f0; padding-top: 15px; }
  
  .view-btn {
    background: transparent; border: 1px solid #e65100; color: #e65100;
    padding: 6px 15px; border-radius: 50px; font-size: 0.85rem; font-weight: 600; cursor: pointer; transition: 0.2s;
  }
  .view-btn:hover { background: #e65100; color: white; }

  /* 6. MODAL */
  .modal-overlay {
    display: none; position: fixed; top: 0; left: 0; width: 100%; height: 100%;
    background: rgba(0,0,0,0.7); z-index: 2000; align-items: center; justify-content: center; backdrop-filter: blur(4px);
  }
  .modal-box {
    background: white; width: 95%; max-width: 700px; max-height: 90vh; overflow-y: auto;
    border-radius: 12px; position: relative; animation: slideUp 0.3s;
  }
  .modal-header {
    background: #e65100; padding: 20px 25px; color: white; display: flex; justify-content: space-between; align-items: center;
    position: sticky; top: 0; z-index: 10;
  }
  .modal-title { margin: 0; font-size: 1.2rem; font-weight: 700; }
  .close-modal { background: none; border: none; color: white; font-size: 2rem; cursor: pointer; }
  
  .modal-body { padding: 25px; }

  .info-block { margin-bottom: 25px; }
  .info-head { font-size: 0.95rem; font-weight: 700; color: #e65100; border-bottom: 2px solid #f0f0f0; padding-bottom: 5px; margin-bottom: 10px; display: flex; align-items: center; gap: 8px; }
  .info-content { font-size: 0.95rem; color: #444; line-height: 1.6; }
  
  .fee-table { width: 100%; border-collapse: collapse; margin-top: 10px; font-size: 0.9rem; background: #fdfdfd; }
  .fee-table td { padding: 10px; border-bottom: 1px solid #eee; }
  .fee-table td:first-child { font-weight: 600; color: #555; }
  .fee-table td:last-child { text-align: right; font-weight: bold; color: #e65100; }

  @keyframes slideUp { from { transform: translateY(50px); opacity: 0; } to { transform: translateY(0); opacity: 1; } }

  /* Mobile */
  @media (max-width: 900px) {
    .app-container { flex-direction: column; }
    .filters-sidebar { width: 100%; position: static; }
  }
</style>

<div class="jain-hero">
  <h1>Jain (Deemed-to-be University)</h1>
  <p>A hub for Learning, Innovation, and Entrepreneurship. Ranked among India's top universities.</p>
</div>

<div class="app-container">

  <aside class="filters-sidebar">
    <div class="filter-group">
      <label class="filter-label">🔍 Search Course</label>
      <input type="text" id="searchInput" class="filter-input" placeholder="e.g. B.Tech, MBA, Design..." onkeyup="renderCourses()">
    </div>
    
    <div class="filter-group">
      <label class="filter-label">🎓 Programme Level</label>
      <select id="levelFilter" class="filter-select" onchange="renderCourses()">
        <option value="All">All Levels</option>
        <option value="UG">Undergraduate (UG)</option>
        <option value="PG">Postgraduate (PG)</option>
        <option value="PhD">Doctoral (PhD)</option>
      </select>
    </div>

    <div class="filter-group">
      <label class="filter-label">🏫 School/Faculty</label>
      <select id="schoolFilter" class="filter-select" onchange="renderCourses()">
        <option value="All">All Schools</option>
        <option value="Engg">Engineering & Tech</option>
        <option value="Mgmt">Management (CMS)</option>
        <option value="Design">Design & Arts</option>
        <option value="Commerce">Commerce</option>
        <option value="Science">Sciences & Allied Health</option>
        <option value="Law">Law</option>
        <option value="IT">IT & Computer Applications</option>
      </select>
    </div>

    <div style="margin-top:20px; font-size:0.8rem; color:#888;">
      Showing <strong id="countDisplay">0</strong> courses
    </div>
  </aside>

  <div class="results-area">
    <div id="courseGrid" class="course-grid">
      </div>
  </div>

</div>

<div id="courseModal" class="modal-overlay" onclick="closeModal(event)">
  <div class="modal-box">
    <div class="modal-header">
      <h2 class="modal-title" id="mTitle">Course Name</h2>
      <button class="close-modal" onclick="closeModalBtn()">&times;</button>
    </div>
    <div class="modal-body">
      
      <div class="info-block">
        <div class="info-head">📋 Eligibility & Admission</div>
        <div class="info-content">
          <p><strong>Eligibility:</strong> <span id="mElig"></span></p>
          <p><strong>Process:</strong> <span id="mProcess"></span></p>
        </div>
      </div>

      <div class="info-block">
        <div class="info-head">💰 Fee Structure (Approx/Year)</div>
        <table class="fee-table" id="mFees"></table>
      </div>

      <div class="info-block">
        <div class="info-head">🚀 Career Outcomes</div>
        <div class="info-content" id="mCareers"></div>
      </div>
      
      <div style="text-align:center; margin-top:30px;">
        <a href="https://www.jainuniversity.ac.in/admissions" target="_blank" style="background:#e65100; color:white; padding:12px 30px; border-radius:50px; text-decoration:none; font-weight:bold;">Apply Now ↗</a>
      </div>

    </div>
  </div>
</div>

<script>
  // --- 1. COURSE DATABASE (Jain University) ---
  const courses = [
    // --- ENGINEERING (B.Tech) ---
    { id: 1, name: "B.Tech Computer Science & Engg", school: "Engg", level: "UG", fee: { "Merit": "₹2.75 Lakhs", "Mgmt": "₹4.5 Lakhs" }, elig: "10+2 with Physics & Math (Min 45%).", career: "Software Engineer, Data Scientist, AI Specialist." },
    { id: 2, name: "B.Tech Aerospace Engineering", school: "Engg", level: "UG", fee: { "Merit": "₹2.25 Lakhs", "Mgmt": "₹3.5 Lakhs" }, elig: "10+2 with PCM (Min 45%).", career: "Aerodynamics Engineer, Defense R&D, Aviation Analyst." },
    { id: 3, name: "B.Tech Artificial Intelligence & ML", school: "Engg", level: "UG", fee: { "Merit": "₹3.0 Lakhs", "Mgmt": "₹5.0 Lakhs" }, elig: "10+2 with PCM (Min 60%).", career: "AI Engineer, ML Architect, Robotics Specialist." },
    { id: 4, name: "B.Tech Civil Engineering", school: "Engg", level: "UG", fee: { "Merit": "₹1.75 Lakhs", "Mgmt": "₹2.5 Lakhs" }, elig: "10+2 with PCM.", career: "Structural Engineer, Construction Manager." },

    // --- MANAGEMENT (BBA/MBA) ---
    { id: 5, name: "BBA (Branding & Advertising)", school: "Mgmt", level: "UG", fee: { "Annual": "₹2.2 Lakhs" }, elig: "10+2 (Any stream).", career: "Brand Manager, Advertising Executive, Media Planner." },
    { id: 6, name: "BBA (International Finance - ACCA)", school: "Mgmt", level: "UG", fee: { "Annual": "₹2.5 Lakhs" }, elig: "10+2 (Commerce/Science).", career: "Global Accountant, Financial Analyst, Auditor." },
    { id: 7, name: "BBA (Sports Management)", school: "Mgmt", level: "UG", fee: { "Annual": "₹2.0 Lakhs" }, elig: "10+2 (Any stream).", career: "Sports Agent, Team Manager, Event Coordinator." },
    { id: 8, name: "MBA (Marketing & Finance)", school: "Mgmt", level: "PG", fee: { "Total (2 Years)": "₹10-12 Lakhs" }, elig: "Graduation (50%) + JET/MAT/CAT/CMAT.", career: "Marketing Manager, Investment Banker, HR Head." },
    { id: 9, name: "MBA (Aviation Management)", school: "Mgmt", level: "PG", fee: { "Total (2 Years)": "₹10 Lakhs" }, elig: "Graduation (50%).", career: "Airport Manager, Airline Operations, Logistics Lead." },

    // --- COMMERCE (B.Com) ---
    { id: 10, name: "B.Com (Honours - Regular)", school: "Commerce", level: "UG", fee: { "Annual": "₹1.4 Lakhs" }, elig: "10+2 (Commerce).", career: "Accountant, Tax Consultant, Banker." },
    { id: 11, name: "B.Com (Risk Mgmt - CIMA UK)", school: "Commerce", level: "UG", fee: { "Annual": "₹1.8 Lakhs" }, elig: "10+2 (Commerce/Science).", career: "Risk Analyst, Management Accountant." },
    { id: 12, name: "B.Com (Strategic Finance - CFA)", school: "Commerce", level: "UG", fee: { "Annual": "₹2.0 Lakhs" }, elig: "10+2 (Commerce).", career: "Investment Analyst, Portfolio Manager." },

    // --- DESIGN (B.Des/M.Des) ---
    { id: 13, name: "B.Des (Product Design)", school: "Design", level: "UG", fee: { "Annual": "₹3.5 Lakhs" }, elig: "10+2 + JET Design Exam.", career: "Product Designer, Industrial Designer." },
    { id: 14, name: "B.Des (Communication Design)", school: "Design", level: "UG", fee: { "Annual": "₹3.5 Lakhs" }, elig: "10+2 + JET Design Exam.", career: "Graphic Designer, Art Director, UI Designer." },
    { id: 15, name: "M.Des (User Experience Design)", school: "Design", level: "PG", fee: { "Annual": "₹3.8 Lakhs" }, elig: "B.Des/B.Arch/B.Tech.", career: "UX Researcher, Interaction Designer." },

    // --- IT & COMPUTER APPLICATIONS ---
    { id: 16, name: "BCA (Artificial Intelligence)", school: "IT", level: "UG", fee: { "Annual": "₹1.8 Lakhs" }, elig: "10+2 (Science/Commerce).", career: "AI Developer, Data Analyst." },
    { id: 17, name: "BCA (Cloud Technology)", school: "IT", level: "UG", fee: { "Annual": "₹1.8 Lakhs" }, elig: "10+2 (Any stream).", career: "Cloud Architect, System Admin." },
    { id: 18, name: "MCA (Information Security)", school: "IT", level: "PG", fee: { "Annual": "₹2.5 Lakhs" }, elig: "BCA/B.Sc CS.", career: "Cyber Security Analyst, Ethical Hacker." },

    // --- SCIENCES & ALLIED HEALTH ---
    { id: 19, name: "B.Sc (Forensic Science)", school: "Science", level: "UG", fee: { "Annual": "₹1.5 Lakhs" }, elig: "10+2 (Science).", career: "Forensic Expert, Crime Scene Investigator." },
    { id: 20, name: "B.Sc (Cardiac Technology)", school: "Science", level: "UG", fee: { "Annual": "₹1.6 Lakhs" }, elig: "10+2 (PCB).", career: "Cardiac Technologist, Cath Lab Tech." },
    { id: 21, name: "B.Sc (Psychology)", school: "Science", level: "UG", fee: { "Annual": "₹1.4 Lakhs" }, elig: "10+2 (Any stream).", career: "Counselor, HR, Psychologist (after Masters)." },
    { id: 22, name: "M.Sc (Biotechnology)", school: "Science", level: "PG", fee: { "Annual": "₹1.6 Lakhs" }, elig: "B.Sc Life Sciences.", career: "Biotech Researcher, Pharma QC." },

    // --- LAW ---
    { id: 23, name: "BA LLB (Honours)", school: "Law", level: "UG", fee: { "Annual": "₹2.0 Lakhs" }, elig: "10+2 (45%) + JET Law Exam.", career: "Litigation, Corporate Law, Judiciary." },
    { id: 24, name: "LLM (Corporate Law)", school: "Law", level: "PG", fee: { "Annual": "₹1.5 Lakhs" }, elig: "LLB Degree.", career: "Legal Consultant, Corporate Counsel." },

    // --- PHD ---
    { id: 25, name: "PhD in Management", school: "Mgmt", level: "PhD", fee: { "Annual": "₹1.0 Lakhs" }, elig: "Master's Degree + Entrance.", career: "Professor, Researcher." },
    { id: 26, name: "PhD in Engineering", school: "Engg", level: "PhD", fee: { "Annual": "₹1.0 Lakhs" }, elig: "M.Tech + Entrance.", career: "R&D Scientist, Academician." }
  ];

  // --- 2. RENDER ENGINE ---
  function renderCourses() {
    const searchText = document.getElementById('searchInput').value.toLowerCase();
    const levelFilter = document.getElementById('levelFilter').value;
    const schoolFilter = document.getElementById('schoolFilter').value;
    const grid = document.getElementById('courseGrid');
    
    grid.innerHTML = '';
    let count = 0;

    courses.forEach(course => {
      const matchSearch = course.name.toLowerCase().includes(searchText);
      const matchLevel = levelFilter === 'All' || course.level === levelFilter;
      const matchSchool = schoolFilter === 'All' || course.school === schoolFilter;

      if (matchSearch && matchLevel && matchSchool) {
        count++;
        // School Color Class
        let colorClass = 'school-Engg';
        if (course.school === 'Mgmt') colorClass = 'school-Mgmt';
        if (course.school === 'Design') colorClass = 'school-Design';
        if (course.school === 'Commerce') colorClass = 'school-Commerce';
        if (course.school === 'Science') colorClass = 'school-Science';
        if (course.school === 'Law') colorClass = 'school-Law';

        const card = `
          <div class="course-card ${colorClass}" style="animation-delay: ${count * 0.05}s">
            <div>
              <span class="c-school">${getSchoolName(course.school)}</span>
              <h3 class="c-title">${course.name}</h3>
              <div class="c-meta">
                <span class="c-badge">${course.level}</span>
                <span class="c-badge">📍 Bangalore</span>
              </div>
            </div>
            <div class="c-footer">
              <button class="view-btn" onclick="openDetails(${course.id})">View Details</button>
            </div>
          </div>
        `;
        grid.innerHTML += card;
      }
    });

    document.getElementById('countDisplay').innerText = count;
  }

  function getSchoolName(code) {
    if (code === 'Engg') return 'Engineering & Tech';
    if (code === 'Mgmt') return 'Management (CMS)';
    if (code === 'Design') return 'Design School';
    if (code === 'Commerce') return 'Commerce';
    if (code === 'Science') return 'Sciences';
    if (code === 'Law') return 'Law School';
    if (code === 'IT') return 'IT & Computer App';
    return code;
  }

  // --- 3. DETAILS MODAL LOGIC ---
  function openDetails(id) {
    const course = courses.find(c => c.id === id);
    if (!course) return;

    document.getElementById('mTitle').innerText = course.name;
    document.getElementById('mElig').innerText = course.elig;
    document.getElementById('mProcess').innerText = "Jain Entrance Test (JET) + Personal Interview (for applicable courses).";
    document.getElementById('mCareers').innerText = course.career;

    // Fees Table
    const table = document.getElementById('mFees');
    table.innerHTML = "";
    for (const [k, v] of Object.entries(course.fee)) {
      table.innerHTML += `<tr><td>${k}</td><td>${v}</td></tr>`;
    }

    document.getElementById('courseModal').style.display = 'flex';
  }

  function closeModalBtn() { document.getElementById('courseModal').style.display = 'none'; }
  function closeModal(e) { if(e.target.className === 'modal-overlay') document.getElementById('courseModal').style.display = 'none'; }

  // Initial Render
  renderCourses();
</script>
