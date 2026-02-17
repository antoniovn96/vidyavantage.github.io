---
layout: default
title: "Jain (Deemed-to-be University) Course Portal 🎓"
permalink: /colleges/jain-university/
image: "https://www.jainuniversity.ac.in/uploads/blog/e856868d40026e690069352693821033.jpg"
description: "Browse 150+ courses at Jain University: Allied Health, Engineering, Management, Design, Law, Sciences, and Sports. Check 2025 JET Exam, Fees, and Placements."
---

<meta property="og:title" content="Jain University Course Portal 🎓">
<meta property="og:description" content="Access details for B.Tech, MBA, B.Des, BCA, Allied Health, and more. Check Eligibility, Fees, and Career Outcomes.">
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
  .jain-hero p { font-size: 1.1rem; color: #fff !important; margin-top: 10px; max-width: 800px; margin-left: auto; margin-right: auto; }

  /* 3. APP CONTAINER */
  .app-container {
    max-width: 1400px;
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
    grid-template-columns: repeat(auto-fill, minmax(320px, 1fr));
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
  .school-Health { border-left-color: #f44336; }
  .school-Commerce { border-left-color: #ff9800; }
  .school-Design { border-left-color: #e91e63; }
  .school-Engg { border-left-color: #2196f3; }
  .school-Humanities { border-left-color: #9c27b0; }
  .school-Languages { border-left-color: #673ab7; }
  .school-Mgmt { border-left-color: #3f51b5; }
  .school-Law { border-left-color: #795548; }
  .school-Science { border-left-color: #4caf50; }
  .school-Computing { border-left-color: #00bcd4; }
  .school-Sports { border-left-color: #8bc34a; }

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
  <p>A hub for Learning, Innovation, and Entrepreneurship. Browse 150+ Programmes.</p>
</div>

<div class="app-container">

  <aside class="filters-sidebar">
    <div class="filter-group">
      <label class="filter-label">🔍 Search Course</label>
      <input type="text" id="searchInput" class="filter-input" placeholder="e.g. Psychology, MBA, Design..." onkeyup="renderCourses()">
    </div>
    
    <div class="filter-group">
      <label class="filter-label">🎓 Programme Level</label>
      <select id="levelFilter" class="filter-select" onchange="renderCourses()">
        <option value="All">All Levels</option>
        <option value="UG">Undergraduate (UG)</option>
        <option value="PG">Postgraduate (PG)</option>
        <option value="PhD">Doctoral (PhD)</option>
        <option value="Diploma">Diploma/Certificate</option>
      </select>
    </div>

    <div class="filter-group">
      <label class="filter-label">🏫 School/Faculty</label>
      <select id="schoolFilter" class="filter-select" onchange="renderCourses()">
        <option value="All">All Schools</option>
        <option value="Health">Allied Health Sciences</option>
        <option value="Commerce">Commerce</option>
        <option value="Design">Design & Arts</option>
        <option value="Engg">Engineering & Tech</option>
        <option value="Humanities">Humanities & Social Sci</option>
        <option value="Mgmt">Management (CMS)</option>
        <option value="Law">Law</option>
        <option value="Science">Sciences</option>
        <option value="Computing">IT & Computing</option>
        <option value="Sports">Sports Education</option>
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
  // --- 1. COURSE DATABASE (FULL LIST) ---
  const courses = [
    // --- ALLIED HEALTH SCIENCES ---
    { id: 101, name: "Bachelors of Physiotherapy (BPT)", school: "Health", level: "UG", fee: { "Annual": "₹2.25 Lakhs" }, elig: "10+2 (PCB) Min 50%.", career: "Physiotherapist, Rehab Specialist, Sports Physio." },
    { id: 102, name: "Bachelor in Psychology (B.Psy)", school: "Health", level: "UG", fee: { "Annual": "₹1.5 Lakhs" }, elig: "10+2 (Any stream).", career: "Counselor, HR, Clinical Psychologist (after PG)." },
    { id: 103, name: "B.Sc Cancer Biology", school: "Health", level: "UG", fee: { "Annual": "₹1.8 Lakhs" }, elig: "10+2 (PCB).", career: "Oncology Researcher, Lab Technologist." },
    { id: 104, name: "B.Sc Cardiac Technology", school: "Health", level: "UG", fee: { "Annual": "₹1.8 Lakhs" }, elig: "10+2 (PCB).", career: "Cardiac Technologist, Cath Lab Tech." },
    { id: 105, name: "B.Sc Medical Lab Technology", school: "Health", level: "UG", fee: { "Annual": "₹1.4 Lakhs" }, elig: "10+2 (PCB).", career: "Lab Manager, Pathology Technician." },
    { id: 106, name: "B.Sc Nuclear Medicine Tech", school: "Health", level: "UG", fee: { "Annual": "₹1.8 Lakhs" }, elig: "10+2 (PCB).", career: "Nuclear Med Tech, Radiology Assistant." },
    { id: 107, name: "B.Sc Nutrition & Dietetics", school: "Health", level: "UG", fee: { "Annual": "₹1.5 Lakhs" }, elig: "10+2 (Science).", career: "Dietician, Nutritionist, Food Analyst." },
    { id: 108, name: "Bachelor of Optometry (B.Optom)", school: "Health", level: "UG", fee: { "Annual": "₹1.6 Lakhs" }, elig: "10+2 (PCB/PCM).", career: "Optometrist, Vision Therapist." },
    { id: 109, name: "B.Sc Anesthesia & OT Tech", school: "Health", level: "UG", fee: { "Annual": "₹1.6 Lakhs" }, elig: "10+2 (Science).", career: "OT Technician, Anesthesia Asst." },
    { id: 110, name: "B.Sc Medical Imaging (BMRIT)", school: "Health", level: "UG", fee: { "Annual": "₹1.6 Lakhs" }, elig: "10+2 (Science).", career: "Radiographer, MRI/CT Tech." },
    { id: 111, name: "BMS Healthcare Management", school: "Health", level: "UG", fee: { "Annual": "₹1.8 Lakhs" }, elig: "10+2 (Any stream).", career: "Hospital Admin, Healthcare Ops." },

    // --- COMMERCE ---
    { id: 201, name: "B.Com (Honours - Regular)", school: "Commerce", level: "UG", fee: { "Annual": "₹1.4 Lakhs" }, elig: "10+2 (Commerce/Science).", career: "Accountant, Banker, Tax Consultant." },
    { id: 202, name: "B.Com (Professional - CA/CS)", school: "Commerce", level: "UG", fee: { "Annual": "₹1.6 Lakhs" }, elig: "10+2 (Commerce/Science).", career: "Chartered Accountant, Company Secretary." },
    { id: 203, name: "B.Com (International Finance - ACCA)", school: "Commerce", level: "UG", fee: { "Annual": "₹2.0 Lakhs" }, elig: "10+2 (Commerce).", career: "ACCA Professional, Global Auditor." },
    { id: 204, name: "B.Com (Strategic Finance - US CMA)", school: "Commerce", level: "UG", fee: { "Annual": "₹2.0 Lakhs" }, elig: "10+2 (Commerce).", career: "Management Accountant, Finance Strategist." },
    { id: 205, name: "B.Com (Logistics & Supply Chain - CIPS)", school: "Commerce", level: "UG", fee: { "Annual": "₹1.8 Lakhs" }, elig: "10+2 (Commerce).", career: "Supply Chain Manager, Logistics Analyst." },
    { id: 206, name: "M.Com (Dual Specialisation)", school: "Commerce", level: "PG", fee: { "Annual": "₹1.0 Lakhs" }, elig: "B.Com/BBA.", career: "Lecturer, Finance Manager." },
    { id: 207, name: "M.Com (Global Professional - ACCA)", school: "Commerce", level: "PG", fee: { "Annual": "₹1.5 Lakhs" }, elig: "B.Com/BBA.", career: "International Finance Consultant." },

    // --- DESIGN ---
    { id: 301, name: "Bachelor of Design (Product/Comm/UI)", school: "Design", level: "UG", fee: { "Annual": "₹3.5 - 4.0 Lakhs" }, elig: "10+2 + JET Design Exam.", career: "Product Designer, UX Designer, Graphic Artist." },
    { id: 302, name: "B.Sc Interior Design", school: "Design", level: "UG", fee: { "Annual": "₹2.0 Lakhs" }, elig: "10+2 (Any stream).", career: "Interior Designer, Space Planner." },
    { id: 303, name: "Master of Design (Product/UX)", school: "Design", level: "PG", fee: { "Annual": "₹3.8 Lakhs" }, elig: "Degree in Design/Arch/Tech.", career: "Design Lead, UX Researcher." },
    { id: 304, name: "MA (Communication/Fashion/Film)", school: "Design", level: "PG", fee: { "Annual": "₹2.5 Lakhs" }, elig: "Graduation.", career: "Creative Director, Fashion Stylist, Filmmaker." },

    // --- ENGINEERING ---
    { id: 401, name: "B.Tech Computer Science & Engg", school: "Engg", level: "UG", fee: { "Merit": "₹2.75L", "Mgmt": "₹4.5L" }, elig: "10+2 PCM (45%).", career: "Software Engineer, Full Stack Dev." },
    { id: 402, name: "B.Tech Aerospace Engineering", school: "Engg", level: "UG", fee: { "Merit": "₹2.25L", "Mgmt": "₹3.5L" }, elig: "10+2 PCM (45%).", career: "Aerospace Engineer, Avionics." },
    { id: 403, name: "B.Tech AI & Data Science", school: "Engg", level: "UG", fee: { "Merit": "₹3.0L", "Mgmt": "₹5.0L" }, elig: "10+2 PCM (60%).", career: "AI Specialist, Data Scientist." },
    { id: 404, name: "B.Tech Mechanical Engineering", school: "Engg", level: "UG", fee: { "Merit": "₹1.75L", "Mgmt": "₹2.5L" }, elig: "10+2 PCM.", career: "Mechanical Engineer, Robotics." },
    { id: 405, name: "M.Tech (Various Specialisations)", school: "Engg", level: "PG", fee: { "Annual": "₹1.5 Lakhs" }, elig: "BE/B.Tech.", career: "R&D Engineer, Structural Consultant." },

    // --- HUMANITIES ---
    { id: 501, name: "BA (Journalism & Mass Comm)", school: "Humanities", level: "UG", fee: { "Annual": "₹1.5 Lakhs" }, elig: "10+2 (Any stream).", career: "Journalist, Content Creator, PR." },
    { id: 502, name: "BA (Economics & Data Analytics)", school: "Humanities", level: "UG", fee: { "Annual": "₹1.5 Lakhs" }, elig: "10+2 (Any stream).", career: "Economist, Data Analyst." },
    { id: 503, name: "MA (Public Policy / Economics)", school: "Humanities", level: "PG", fee: { "Annual": "₹1.2 Lakhs" }, elig: "Graduation.", career: "Policy Analyst, Researcher." },

    // --- MANAGEMENT ---
    { id: 601, name: "BBA (Branding & Advertising)", school: "Mgmt", level: "UG", fee: { "Annual": "₹2.2 Lakhs" }, elig: "10+2.", career: "Brand Manager, Ad Executive." },
    { id: 602, name: "BBA (Strategic Finance - US CMA)", school: "Mgmt", level: "UG", fee: { "Annual": "₹2.5 Lakhs" }, elig: "10+2.", career: "Corporate Finance, Strategy." },
    { id: 603, name: "BMS (Aviation / Healthcare / IB)", school: "Mgmt", level: "UG", fee: { "Annual": "₹2.0 Lakhs" }, elig: "10+2.", career: "Airport Mgr, Hospital Admin, IB Exec." },
    { id: 604, name: "MBA (Single / Dual Specialisation)", school: "Mgmt", level: "PG", fee: { "Total": "₹10-12 Lakhs" }, elig: "Graduation + JET/CAT/MAT.", career: "Manager, Consultant, Entrepreneur." },
    { id: 605, name: "MBA Dual Degree (Intl Universities)", school: "Mgmt", level: "PG", fee: { "Total": "₹15+ Lakhs" }, elig: "Graduation + JET.", career: "Global Business Leader." },

    // --- LAW ---
    { id: 701, name: "BA LLB (Honours)", school: "Law", level: "UG", fee: { "Annual": "₹2.0 Lakhs" }, elig: "10+2 (45%) + JET Law.", career: "Lawyer, Judge, Legal Advisor." },
    { id: 702, name: "BBA LLB (Honours)", school: "Law", level: "UG", fee: { "Annual": "₹2.2 Lakhs" }, elig: "10+2 (45%) + JET Law.", career: "Corporate Lawyer, Legal Consultant." },
    { id: 703, name: "LLM (Master of Law)", school: "Law", level: "PG", fee: { "Annual": "₹1.5 Lakhs" }, elig: "LLB.", career: "Legal Researcher, Specialist Counsel." },

    // --- SCIENCES ---
    { id: 801, name: "B.Sc (Forensic Science)", school: "Science", level: "UG", fee: { "Annual": "₹1.5 Lakhs" }, elig: "10+2 Science.", career: "Forensic Scientist, Investigator." },
    { id: 802, name: "B.Sc (Biotech / Biochem / Genetics)", school: "Science", level: "UG", fee: { "Annual": "₹1.2 Lakhs" }, elig: "10+2 Science.", career: "Research Assistant, Lab Tech." },
    { id: 803, name: "M.Sc (Forensic / Psychology / Chem)", school: "Science", level: "PG", fee: { "Annual": "₹1.5 Lakhs" }, elig: "B.Sc relevant.", career: "Scientist, Psychologist, Chemist." },

    // --- APPLIED COMPUTING ---
    { id: 901, name: "BCA (AI & Machine Learning)", school: "Computing", level: "UG", fee: { "Annual": "₹1.8 Lakhs" }, elig: "10+2.", career: "AI Developer, ML Engineer." },
    { id: 902, name: "BCA (Cloud Computing / CyberSec)", school: "Computing", level: "UG", fee: { "Annual": "₹1.8 Lakhs" }, elig: "10+2.", career: "Cloud Engineer, Security Analyst." },
    { id: 903, name: "B.Sc (Animation / Gaming)", school: "Computing", level: "UG", fee: { "Annual": "₹2.5 Lakhs" }, elig: "10+2.", career: "Game Developer, Animator." },
    { id: 904, name: "MCA (AI / Cloud / Security)", school: "Computing", level: "PG", fee: { "Annual": "₹2.5 Lakhs" }, elig: "BCA/B.Sc CS.", career: "Senior Developer, System Architect." },

    // --- SPORTS ---
    { id: 1001, name: "B.Sc Physical Education & Sports", school: "Sports", level: "UG", fee: { "Annual": "₹1.5 Lakhs" }, elig: "10+2.", career: "Sports Coach, PE Teacher." },
    { id: 1002, name: "M.Sc Applied Sports Science", school: "Sports", level: "PG", fee: { "Annual": "₹1.8 Lakhs" }, elig: "B.Sc Sports/PE.", career: "Sports Scientist, Performance Analyst." },

    // --- PHD ---
    { id: 1101, name: "PhD (Engg / Mgmt / Science / Law)", school: "Science", level: "PhD", fee: { "Annual": "₹1.0 Lakhs" }, elig: "Masters + Entrance.", career: "Researcher, Professor." }
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
        let colorClass = 'school-' + course.school;
        // Fallback for PhD or unmapped
        if(course.level === 'PhD') colorClass = 'school-Science';

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
    if (code === 'Engg') return 'Engineering';
    if (code === 'Mgmt') return 'Management';
    if (code === 'Design') return 'Design';
    if (code === 'Commerce') return 'Commerce';
    if (code === 'Science') return 'Sciences';
    if (code === 'Law') return 'Law';
    if (code === 'Computing') return 'IT & Computing';
    if (code === 'Health') return 'Allied Health';
    if (code === 'Sports') return 'Sports';
    if (code === 'Humanities') return 'Humanities';
    return code;
  }

  // --- 3. DETAILS MODAL LOGIC ---
  function openDetails(id) {
    const course = courses.find(c => c.id === id);
    if (!course) return;

    document.getElementById('mTitle').innerText = course.name;
    document.getElementById('mElig').innerText = course.elig;
    document.getElementById('mProcess').innerText = "Jain Entrance Test (JET) + Personal Interview (where applicable).";
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
