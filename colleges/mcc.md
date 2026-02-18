---
layout: default
title: "Mount Carmel College (MCC) Course Portal 🎓"
permalink: /colleges/mcc/
image: "https://images.unsplash.com/photo-1564981797816-1043664bf78d?ixlib=rb-4.0.3&auto=format&fit=crop&w=1200&q=80"
description: "Browse B.Com, B.Sc, B.A., MBA, and PhD courses at MCC Bangalore. Check 2025 Fees, Eligibility, and International Programs."
---

<meta property="og:title" content="MCC Bangalore Course Portal 🎓">
<meta property="og:description" content="Access details for 40+ courses: B.Sc, B.Com, B.A, MBA & PhD. Check 2025 Fees, Eligibility, and Career Outcomes.">
<meta property="og:image" content="https://images.unsplash.com/photo-1564981797816-1043664bf78d?ixlib=rb-4.0.3&auto=format&fit=crop&w=1200&q=80">

<style>
  /* 1. LAYOUT RESET */
  .main-content { max-width: 100% !important; padding: 0 !important; margin: 0 !important; }
  body { background-color: #f4f6f8; font-family: 'Segoe UI', system-ui, sans-serif; color: #333; }

  /* 2. HERO SECTION */
  .mcc-hero {
    background: linear-gradient(rgba(139, 0, 0, 0.8), rgba(50, 0, 0, 0.7)), url('https://images.unsplash.com/photo-1564981797816-1043664bf78d?ixlib=rb-4.0.3&auto=format&fit=crop&w=1600&q=80');
    background-size: cover;
    background-position: center;
    color: white;
    text-align: center;
    padding: 80px 20px;
    margin-bottom: 0;
  }
  
  .mcc-hero h1 { font-size: 2.8rem; margin: 0; font-weight: 800; color: white !important; }
  .mcc-hero p { font-size: 1.1rem; color: #ddd !important; margin-top: 10px; max-width: 700px; margin-left: auto; margin-right: auto; }

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
    border-top: 4px solid #8b0000; /* MCC Maroon */
    flex-shrink: 0;
  }

  .filter-group { margin-bottom: 20px; }
  .filter-label { display: block; font-weight: 700; margin-bottom: 8px; color: #8b0000; font-size: 0.9rem; }
  
  .filter-input, .filter-select {
    width: 100%;
    padding: 10px 15px;
    border: 1px solid #ddd;
    border-radius: 8px;
    font-size: 0.95rem;
    outline: none;
    transition: border 0.2s;
  }
  .filter-input:focus, .filter-select:focus { border-color: #8b0000; }

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
  .course-card:hover { transform: translateY(-3px); box-shadow: 0 8px 25px rgba(0,0,0,0.08); border-left-color: #8b0000; }

  /* Department Colors */
  .dept-Science { border-left-color: #2e7d32; } /* Green */
  .dept-Arts { border-left-color: #d81b60; } /* Pink/Red */
  .dept-Comm { border-left-color: #f57c00; } /* Orange */
  .dept-Mgmt { border-left-color: #3f51b5; } /* Blue */
  .dept-Res { border-left-color: #795548; } /* Brown */

  .c-dept { font-size: 0.75rem; text-transform: uppercase; font-weight: 700; color: #888; margin-bottom: 5px; }
  .c-title { font-size: 1.1rem; font-weight: 700; color: #333; margin: 0 0 10px 0; line-height: 1.4; }
  .c-meta { display: flex; gap: 8px; flex-wrap: wrap; margin-bottom: 15px; }
  .c-badge { display: inline-block; background: #f0f2f5; padding: 4px 10px; border-radius: 4px; font-size: 0.75rem; font-weight: 600; color: #555; }
  
  .c-footer { margin-top: auto; display: flex; justify-content: space-between; align-items: center; border-top: 1px solid #f0f0f0; padding-top: 15px; }
  
  .view-btn {
    background: transparent; border: 1px solid #8b0000; color: #8b0000;
    padding: 6px 15px; border-radius: 50px; font-size: 0.85rem; font-weight: 600; cursor: pointer; transition: 0.2s;
  }
  .view-btn:hover { background: #8b0000; color: white; }

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
    background: #8b0000; padding: 20px 25px; color: white; display: flex; justify-content: space-between; align-items: center;
    position: sticky; top: 0; z-index: 10;
  }
  .modal-title { margin: 0; font-size: 1.2rem; font-weight: 700; }
  .close-modal { background: none; border: none; color: white; font-size: 2rem; cursor: pointer; }
  
  .modal-body { padding: 25px; }

  .info-block { margin-bottom: 25px; }
  .info-head { font-size: 0.95rem; font-weight: 700; color: #8b0000; border-bottom: 2px solid #f0f0f0; padding-bottom: 5px; margin-bottom: 10px; display: flex; align-items: center; gap: 8px; }
  .info-content { font-size: 0.95rem; color: #444; line-height: 1.6; }
  
  .fee-table { width: 100%; border-collapse: collapse; margin-top: 10px; font-size: 0.9rem; background: #fdfdfd; }
  .fee-table td { padding: 10px; border-bottom: 1px solid #eee; }
  .fee-table td:first-child { font-weight: 600; color: #555; }
  .fee-table td:last-child { text-align: right; font-weight: bold; color: #8b0000; }

  @keyframes slideUp { from { transform: translateY(50px); opacity: 0; } to { transform: translateY(0); opacity: 1; } }

  /* Mobile */
  @media (max-width: 900px) {
    .app-container { flex-direction: column; }
    .filters-sidebar { width: 100%; position: static; }
  }
</style>

<div class="mcc-hero">
  <h1>Mount Carmel College, Autonomous</h1>
  <p>A Premier Institution for Women Education | NAAC A+ Grade | 75+ Years of Excellence</p>
</div>

<div class="app-container">

  <aside class="filters-sidebar">
    <div class="filter-group">
      <label class="filter-label">🔍 Search Course</label>
      <input type="text" id="searchInput" class="filter-input" placeholder="e.g. Psychology, B.Com, MBA..." onkeyup="renderCourses()">
    </div>
    
    <div class="filter-group">
      <label class="filter-label">🎓 Programme Level</label>
      <select id="levelFilter" class="filter-select" onchange="renderCourses()">
        <option value="All">All Levels</option>
        <option value="UG">Undergraduate (B.Sc/B.A/B.Com)</option>
        <option value="PG">Postgraduate (M.Sc/M.A/MBA)</option>
        <option value="PhD">Doctoral Programs</option>
        <option value="Diploma">Diploma / PG Diploma</option>
      </select>
    </div>

    <div class="filter-group">
      <label class="filter-label">🏫 School / Stream</label>
      <select id="deptFilter" class="filter-select" onchange="renderCourses()">
        <option value="All">All Schools</option>
        <option value="Science">Natural & Applied Sciences</option>
        <option value="Arts">Humanities & Social Sciences</option>
        <option value="Comm">Commerce</option>
        <option value="Mgmt">Management & Int. Programs</option>
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
        <div class="info-head">📋 Eligibility Criteria</div>
        <div class="info-content" id="mElig"></div>
      </div>

      <div class="info-block">
        <div class="info-head">📝 Admission Process</div>
        <div class="info-content" id="mProcess"></div>
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
        <a href="https://mccblr.edu.in/admission-process/" target="_blank" style="background:#8b0000; color:white; padding:12px 30px; border-radius:50px; text-decoration:none; font-weight:bold;">Official Admission Page ↗</a>
      </div>

    </div>
  </div>
</div>

<script>
  // --- 1. COURSE DATABASE (MCC) ---
  const courses = [
    // --- SCHOOL OF NATURAL & APPLIED SCIENCES ---
    { id: 1, name: "B.Sc - Biotechnology, Chemistry, Zoology", dept: "Science", level: "UG", fee: { "1st Year": "₹1,07,500", "2nd Year": "₹1,19,200" }, elig: "10+2 (PUC/CBSE) with Biology & Chemistry.", career: "Biotech Researcher, Lab Technician, Pharma Industry." },
    { id: 2, name: "B.Sc - Computer Science, Maths, Electronics", dept: "Science", level: "UG", fee: { "1st Year": "₹95,000", "2nd Year": "₹1,05,000" }, elig: "10+2 with Physics & Maths.", career: "Software Developer, Electronics Engineer, Data Analyst." },
    { id: 3, name: "B.Sc - Nutrition & Dietetics", dept: "Science", level: "UG", fee: { "1st Year": "₹1,15,000", "2nd Year": "₹1,25,000" }, elig: "10+2 with Science (Chem/Bio).", career: "Clinical Dietitian, Food Analyst, Health Coach." },
    { id: 4, name: "BCA (Bachelor of Computer App)", dept: "Science", level: "UG", fee: { "Total": "₹4.52 - 5.71 Lakhs (3 Years)" }, elig: "10+2 with Maths/Comp Sci/Business Maths.", career: "App Developer, Web Designer, IT Support." },
    { id: 5, name: "M.Sc - Biotechnology", dept: "Science", level: "PG", fee: { "1st Year": "₹1,18,000", "2nd Year": "₹1,29,000" }, elig: "B.Sc in Life Sciences with 50%.", career: "Research Scientist, Quality Control, Academia." },
    { id: 6, name: "M.Sc - Food Science & Nutrition", dept: "Science", level: "PG", fee: { "1st Year": "₹1,25,000", "2nd Year": "₹1,35,000" }, elig: "B.Sc Home Science/Nutrition with 50%.", career: "Nutritionist, Food Safety Officer, R&D." },
    { id: 7, name: "MCA (Master of Computer App)", dept: "Science", level: "PG", fee: { "Total": "₹2.94 Lakhs (2 Years)" }, elig: "BCA/B.Sc IT with 50% + PGCET/KMAT.", career: "Software Engineer, System Analyst, Tech Lead." },

    // --- SCHOOL OF HUMANITIES & SOCIAL SCIENCES ---
    { id: 8, name: "B.A. - Psychology, English Lit, Journalism", dept: "Arts", level: "UG", fee: { "1st Year": "₹89,500", "2nd Year": "₹1,00,300" }, elig: "10+2 in any stream.", career: "Content Writer, Counselor, Journalist, HR." },
    { id: 9, name: "B.A. - History, Economics, Pol. Science", dept: "Arts", level: "UG", fee: { "1st Year": "₹60,000", "2nd Year": "₹70,000" }, elig: "10+2 in any stream.", career: "Civil Services, Policy Analyst, Historian." },
    { id: 10, name: "B.A. - Communication Studies", dept: "Arts", level: "UG", fee: { "1st Year": "₹1,20,000", "2nd Year": "₹1,30,000" }, elig: "10+2 + Entrance Test.", career: "Media Professional, PR Specialist, Ad Agency." },
    { id: 11, name: "M.Sc - Psychology", dept: "Arts", level: "PG", fee: { "1st Year": "₹1,30,000", "2nd Year": "₹1,40,000" }, elig: "B.A./B.Sc Psychology with 50%.", career: "Clinical Psychologist, Corporate Trainer, HR." },
    { id: 12, name: "M.A. - English", dept: "Arts", level: "PG", fee: { "Total": "₹2.02 Lakhs (2 Years)" }, elig: "B.A. with English Major.", career: "Editor, Lecturer, Creative Writer." },

    // --- SCHOOL OF COMMERCE ---
    { id: 13, name: "B.Com - Regular", dept: "Comm", level: "UG", fee: { "1st Year": "₹85,000", "2nd Year": "₹95,000" }, elig: "10+2 with Commerce/Accountancy.", career: "Accountant, Tax Consultant, Banking." },
    { id: 14, name: "B.Com - Industry Integrated", dept: "Comm", level: "UG", fee: { "1st Year": "₹1,10,000", "2nd Year": "₹1,20,000" }, elig: "10+2 with Commerce (High Cutoff).", career: "Corporate Finance, Auditing, Business Analyst." },
    { id: 15, name: "B.Com - International A&F (ACCA)", dept: "Comm", level: "UG", fee: { "1st Year": "₹1,40,000", "2nd Year": "₹1,50,000" }, elig: "10+2 Commerce.", career: "Global Auditor, Financial Analyst, ACCA Professional." },
    { id: 16, name: "M.Com - Finance", dept: "Comm", level: "PG", fee: { "Total": "₹2.35 Lakhs (2 Years)" }, elig: "B.Com/BBA with 50%.", career: "Investment Banker, Finance Manager." },

    // --- SCHOOL OF MANAGEMENT ---
    { id: 17, name: "BBA - Regular", dept: "Mgmt", level: "UG", fee: { "1st Year": "₹1,86,500", "2nd Year": "₹2,02,200" }, elig: "10+2 (Any Stream) + MCMAT Entrance.", career: "Business Admin, Startups, Junior Manager." },
    { id: 18, name: "BBA - Branding & Advertising", dept: "Mgmt", level: "UG", fee: { "1st Year": "₹2,10,000", "2nd Year": "₹2,25,000" }, elig: "10+2 + MCMAT.", career: "Brand Manager, Ad Executive, Marketing Strategy." },
    { id: 19, name: "MBA (Master of Business Admin)", dept: "Mgmt", level: "PG", fee: { "Total": "₹5.25 - 7.0 Lakhs" }, elig: "Degree (50%) + PGCET/MAT/KMAT.", career: "Marketing Head, HR Manager, Operations Lead." },
    
    // --- INTERNATIONAL & DIPLOMA PROGRAMS ---
    { id: 20, name: "PGDBA (PG Diploma in Business Admin)", dept: "Mgmt", level: "Diploma", fee: { "Total": "₹99,900" }, elig: "Any Graduate.", career: "Business Ops, Admin Roles (1 Year Course)." },
    { id: 21, name: "PG Diploma in International Business (PGDBIA)", dept: "Mgmt", level: "Diploma", fee: { "Total": "₹1,15,000" }, elig: "Any Graduate.", career: "Export/Import Manager, Global Trade Analyst." },

    // --- DOCTORAL PROGRAMS ---
    { id: 22, name: "Ph.D in Biotechnology", dept: "Res", level: "PhD", fee: { "Tuition": "As per University Norms" }, elig: "M.Sc in Biotech + Entrance.", career: "Senior Scientist, Professor." },
    { id: 23, name: "Ph.D in Commerce", dept: "Res", level: "PhD", fee: { "Tuition": "As per University Norms" }, elig: "M.Com + Entrance.", career: "Research Scholar, Academician." }
  ];

  // --- 2. RENDER ENGINE ---
  function renderCourses() {
    const searchText = document.getElementById('searchInput').value.toLowerCase();
    const levelFilter = document.getElementById('levelFilter').value;
    const deptFilter = document.getElementById('deptFilter').value;
    const grid = document.getElementById('courseGrid');
    
    grid.innerHTML = '';
    let count = 0;

    courses.forEach(course => {
      const matchSearch = course.name.toLowerCase().includes(searchText);
      const matchLevel = levelFilter === 'All' || course.level === levelFilter;
      const matchDept = deptFilter === 'All' || course.dept === deptFilter;

      if (matchSearch && matchLevel && matchDept) {
        count++;
        // Department Color Class
        let colorClass = 'dept-' + course.dept;

        const card = `
          <div class="course-card ${colorClass}" style="animation-delay: ${count * 0.05}s">
            <div>
              <span class="c-dept">${getDeptName(course.dept)}</span>
              <h3 class="c-title">${course.name}</h3>
              <div class="c-meta">
                <span class="c-badge">${course.level}</span>
                <span class="c-badge">Autonomous</span>
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

  function getDeptName(code) {
    if (code === 'Science') return 'Natural & Applied Sci';
    if (code === 'Arts') return 'Humanities';
    if (code === 'Comm') return 'Commerce';
    if (code === 'Mgmt') return 'Management';
    if (code === 'Res') return 'Research';
    return code;
  }

  // --- 3. DETAILS MODAL LOGIC ---
  function openDetails(id) {
    const course = courses.find(c => c.id === id);
    if (!course) return;

    document.getElementById('mTitle').innerText = course.name;
    document.getElementById('mElig').innerText = course.elig;
    
    let process = "Merit Based (12th Marks) + Interview.";
    if(course.name.includes("BBA") || course.name.includes("Communication")) process = "Entrance Test (MCMAT) + GD + Interview.";
    if(course.level === "PG") process = "Entrance Exam (PGCET/KMAT) for MBA/MCA. Interview for others.";
    if(course.level === "PhD") process = "University Entrance Test + Interview.";
    document.getElementById('mProcess').innerText = process;
    
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
