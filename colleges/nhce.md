---
layout: default
title: "New Horizon College of Engineering (NHCE) Course Portal 🎓"
permalink: /colleges/nhce/
image: "https://images.unsplash.com/photo-1562774053-701939374585?ixlib=rb-4.0.3&auto=format&fit=crop&w=1200&q=80"
description: "Browse B.E, M.Tech, MBA, MCA and PhD courses at NHCE. Check 2025 Fees, Eligibility, Minor Degrees and Placements."
---

<meta property="og:title" content="NHCE Course Portal 🎓">
<meta property="og:description" content="Access details for 25+ courses: B.E, MBA, MCA, M.Tech & PhD. Check 2025 Fees, Eligibility, and Minor Degree options.">
<meta property="og:image" content="https://images.unsplash.com/photo-1562774053-701939374585?ixlib=rb-4.0.3&auto=format&fit=crop&w=1200&q=80">

<style>
  /* 1. LAYOUT RESET */
  .main-content { max-width: 100% !important; padding: 0 !important; margin: 0 !important; }
  body { background-color: #f4f6f8; font-family: 'Segoe UI', system-ui, sans-serif; color: #333; }

  /* 2. HERO SECTION */
  .nhce-hero {
    background: linear-gradient(rgba(0, 51, 102, 0.8), rgba(0, 0, 0, 0.7)), url('https://images.unsplash.com/photo-1562774053-701939374585?ixlib=rb-4.0.3&auto=format&fit=crop&w=1600&q=80');
    background-size: cover;
    background-position: center;
    color: white;
    text-align: center;
    padding: 80px 20px;
    margin-bottom: 0;
  }
  
  .nhce-hero h1 { font-size: 2.8rem; margin: 0; font-weight: 800; color: white !important; }
  .nhce-hero p { font-size: 1.1rem; color: #ddd !important; margin-top: 10px; max-width: 700px; margin-left: auto; margin-right: auto; }

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
    border-top: 4px solid #1a237e; /* NHCE Dark Blue */
    flex-shrink: 0;
  }

  .filter-group { margin-bottom: 20px; }
  .filter-label { display: block; font-weight: 700; margin-bottom: 8px; color: #1a237e; font-size: 0.9rem; }
  
  .filter-input, .filter-select {
    width: 100%;
    padding: 10px 15px;
    border: 1px solid #ddd;
    border-radius: 8px;
    font-size: 0.95rem;
    outline: none;
    transition: border 0.2s;
  }
  .filter-input:focus, .filter-select:focus { border-color: #1a237e; }

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
  .course-card:hover { transform: translateY(-3px); box-shadow: 0 8px 25px rgba(0,0,0,0.08); border-left-color: #1a237e; }

  /* Department Colors */
  .dept-Engg { border-left-color: #2196f3; }
  .dept-Mgmt { border-left-color: #9c27b0; }
  .dept-Res { border-left-color: #795548; }
  .dept-Minor { border-left-color: #ff9800; }

  .c-dept { font-size: 0.75rem; text-transform: uppercase; font-weight: 700; color: #888; margin-bottom: 5px; }
  .c-title { font-size: 1.1rem; font-weight: 700; color: #333; margin: 0 0 10px 0; line-height: 1.4; }
  .c-meta { display: flex; gap: 8px; flex-wrap: wrap; margin-bottom: 15px; }
  .c-badge { display: inline-block; background: #f0f2f5; padding: 4px 10px; border-radius: 4px; font-size: 0.75rem; font-weight: 600; color: #555; }
  
  .c-footer { margin-top: auto; display: flex; justify-content: space-between; align-items: center; border-top: 1px solid #f0f0f0; padding-top: 15px; }
  
  .view-btn {
    background: transparent; border: 1px solid #1a237e; color: #1a237e;
    padding: 6px 15px; border-radius: 50px; font-size: 0.85rem; font-weight: 600; cursor: pointer; transition: 0.2s;
  }
  .view-btn:hover { background: #1a237e; color: white; }

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
    background: #1a237e; padding: 20px 25px; color: white; display: flex; justify-content: space-between; align-items: center;
    position: sticky; top: 0; z-index: 10;
  }
  .modal-title { margin: 0; font-size: 1.2rem; font-weight: 700; }
  .close-modal { background: none; border: none; color: white; font-size: 2rem; cursor: pointer; }
  
  .modal-body { padding: 25px; }

  .info-block { margin-bottom: 25px; }
  .info-head { font-size: 0.95rem; font-weight: 700; color: #1a237e; border-bottom: 2px solid #f0f0f0; padding-bottom: 5px; margin-bottom: 10px; display: flex; align-items: center; gap: 8px; }
  .info-content { font-size: 0.95rem; color: #444; line-height: 1.6; }
  
  .fee-table { width: 100%; border-collapse: collapse; margin-top: 10px; font-size: 0.9rem; background: #fdfdfd; }
  .fee-table td { padding: 10px; border-bottom: 1px solid #eee; }
  .fee-table td:first-child { font-weight: 600; color: #555; }
  .fee-table td:last-child { text-align: right; font-weight: bold; color: #1a237e; }

  @keyframes slideUp { from { transform: translateY(50px); opacity: 0; } to { transform: translateY(0); opacity: 1; } }

  /* Mobile */
  @media (max-width: 900px) {
    .app-container { flex-direction: column; }
    .filters-sidebar { width: 100%; position: static; }
  }
</style>

<div class="nhce-hero">
  <h1>New Horizon College of Engineering</h1>
  <p>Autonomous College affiliated to VTU | NAAC 'A' Grade | Ranked among Top Engineering Colleges in Bangalore</p>
</div>

<div class="app-container">

  <aside class="filters-sidebar">
    <div class="filter-group">
      <label class="filter-label">🔍 Search Course</label>
      <input type="text" id="searchInput" class="filter-input" placeholder="e.g. AI, MBA, Robotics..." onkeyup="renderCourses()">
    </div>
    
    <div class="filter-group">
      <label class="filter-label">🎓 Programme Level</label>
      <select id="levelFilter" class="filter-select" onchange="renderCourses()">
        <option value="All">All Levels</option>
        <option value="UG">Undergraduate (B.E)</option>
        <option value="PG">Postgraduate (MBA/MCA/M.Tech)</option>
        <option value="PhD">PhD / Research</option>
        <option value="Minor">Minor Degree</option>
      </select>
    </div>

    <div class="filter-group">
      <label class="filter-label">🏫 Department</label>
      <select id="deptFilter" class="filter-select" onchange="renderCourses()">
        <option value="All">All Departments</option>
        <option value="Engg">Engineering</option>
        <option value="Mgmt">Management & CA</option>
        <option value="Res">Research Sciences</option>
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
        <a href="https://newhorizoncollegeofengineering.in/admissions/" target="_blank" style="background:#1a237e; color:white; padding:12px 30px; border-radius:50px; text-decoration:none; font-weight:bold;">Official Admission Page ↗</a>
      </div>

    </div>
  </div>
</div>

<script>
  // --- 1. COURSE DATABASE (NHCE) ---
  const courses = [
    // --- UG (B.E) ---
    { id: 1, name: "B.E. Computer Science & Engg", dept: "Engg", level: "UG", fee: { "CET": "₹1,14,706", "Mgmt": "₹3.5 - 4.5 Lakhs" }, elig: "10+2 with 45% (PCM).", career: "Software Engineer, Full Stack Dev, System Architect." },
    { id: 2, name: "B.E. Artificial Intelligence & ML", dept: "Engg", level: "UG", fee: { "CET": "₹1,14,706", "Mgmt": "₹3.5 - 4.5 Lakhs" }, elig: "10+2 with 45% (PCM).", career: "AI Engineer, ML Specialist, Data Analyst." },
    { id: 3, name: "B.E. CSE (Data Science)", dept: "Engg", level: "UG", fee: { "CET": "₹1,14,706", "Mgmt": "₹3.5 - 4.0 Lakhs" }, elig: "10+2 with 45% (PCM).", career: "Data Scientist, Business Analyst, Big Data Engineer." },
    { id: 4, name: "B.E. Information Science & Engg", dept: "Engg", level: "UG", fee: { "CET": "₹1,14,706", "Mgmt": "₹3.0 - 3.5 Lakhs" }, elig: "10+2 with 45% (PCM).", career: "IT Consultant, Web Developer, Cyber Security Analyst." },
    { id: 5, name: "B.E. Electronics & Communication", dept: "Engg", level: "UG", fee: { "CET": "₹1,14,706", "Mgmt": "₹2.5 - 3.5 Lakhs" }, elig: "10+2 with 45% (PCM).", career: "VLSI Design, Embedded Systems, Telecom Engineer." },
    { id: 6, name: "B.E. Electrical & Electronics", dept: "Engg", level: "UG", fee: { "CET": "₹1,14,706", "Mgmt": "₹2.0 - 2.5 Lakhs" }, elig: "10+2 with 45% (PCM).", career: "Electrical Engineer, Power Systems, Grid Management." },
    { id: 7, name: "B.E. Mechanical Engineering", dept: "Engg", level: "UG", fee: { "CET": "₹1,14,706", "Mgmt": "₹1.5 - 2.0 Lakhs" }, elig: "10+2 with 45% (PCM).", career: "Mechanical Design, Robotics, Automotive Engineer." },

    // --- PG (MBA, MCA, M.Tech) ---
    { id: 8, name: "Master of Business Admin (MBA)", dept: "Mgmt", level: "PG", fee: { "Total": "₹7,00,000 (2 Years)" }, elig: "Degree (50%) + PGCET/KMAT/MAT.", career: "Marketing Manager, HR Specialist, Finance Analyst." },
    { id: 9, name: "Master of Computer App (MCA)", dept: "Mgmt", level: "PG", fee: { "Total": "₹7,00,000 (2 Years)" }, elig: "Degree (50%) with Maths + PGCET/KMAT.", career: "Software Developer, System Analyst, App Developer." },
    { id: 10, name: "M.Tech (Computer Science)", dept: "Engg", level: "PG", fee: { "Total": "₹2,00,000 (2 Years)" }, elig: "B.E./B.Tech (50%) + GATE/PGCET.", career: "Research Scientist, Senior Engineer, Tech Lead." },

    // --- MINOR DEGREES (For B.E Students) ---
    { id: 11, name: "Minor in Artificial Intelligence", dept: "Minor", level: "Minor", fee: { "Note": "Add-on to Major Degree" }, elig: "Min 5 CGPA up to 4th Sem (No Backlogs).", career: "Adds AI expertise to Core Engineering." },
    { id: 12, name: "Minor in Data Science", dept: "Minor", level: "Minor", fee: { "Note": "Add-on to Major Degree" }, elig: "Min 5 CGPA up to 4th Sem (No Backlogs).", career: "Adds Data Analytics skills to Core Engineering." },
    { id: 13, name: "Minor in Robotics & Automation", dept: "Minor", level: "Minor", fee: { "Note": "Add-on to Major Degree" }, elig: "Min 5 CGPA up to 4th Sem (No Backlogs).", career: "Automation Specialist, Robotics Control." },
    { id: 14, name: "Minor in VLSI Design", dept: "Minor", level: "Minor", fee: { "Note": "Add-on to Major Degree" }, elig: "Min 5 CGPA up to 4th Sem (No Backlogs).", career: "Chip Design, Semiconductor Industry." },
    { id: 15, name: "Minor in Digital Marketing", dept: "Minor", level: "Minor", fee: { "Note": "Add-on to Major Degree" }, elig: "Min 5 CGPA up to 4th Sem (No Backlogs).", career: "Tech Marketing, Product Management." },
    { id: 16, name: "Minor in Fin-Tech", dept: "Minor", level: "Minor", fee: { "Note": "Add-on to Major Degree" }, elig: "Min 5 CGPA up to 4th Sem (No Backlogs).", career: "Financial Technology, Banking Software." },

    // --- PHD / RESEARCH ---
    { id: 17, name: "Ph.D in Computer Science", dept: "Res", level: "PhD", fee: { "Tuition": "As per VTU Norms" }, elig: "Master's Degree in CS/IT + VTU ETR/GATE.", career: "Professor, R&D Scientist." },
    { id: 18, name: "Ph.D in Management (MBA)", dept: "Res", level: "PhD", fee: { "Tuition": "As per VTU Norms" }, elig: "MBA + VTU ETR/UGC-NET.", career: "Business Researcher, Academician." },
    { id: 19, name: "Ph.D in Mechanical Engg", dept: "Res", level: "PhD", fee: { "Tuition": "As per VTU Norms" }, elig: "M.Tech in Mech + VTU ETR.", career: "Research in Thermodynamics, Design." },
    { id: 20, name: "Ph.D in Mathematics/Chemistry", dept: "Res", level: "PhD", fee: { "Tuition": "As per VTU Norms" }, elig: "M.Sc + VTU ETR.", career: "Scientific Research, Teaching." }
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
        // Exception for Minor degrees to use a specific color
        if(course.level === 'Minor') colorClass = 'dept-Minor';

        const card = `
          <div class="course-card ${colorClass}" style="animation-delay: ${count * 0.05}s">
            <div>
              <span class="c-dept">${getDeptName(course.dept)}</span>
              <h3 class="c-title">${course.name}</h3>
              <div class="c-meta">
                <span class="c-badge">${course.level}</span>
                <span class="c-badge">Bangalore</span>
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
    if (code === 'Engg') return 'Engineering';
    if (code === 'Mgmt') return 'Management';
    if (code === 'Res') return 'Research';
    if (code === 'Minor') return 'Specialization';
    return code;
  }

  // --- 3. DETAILS MODAL LOGIC ---
  function openDetails(id) {
    const course = courses.find(c => c.id === id);
    if (!course) return;

    document.getElementById('mTitle').innerText = course.name;
    document.getElementById('mElig').innerText = course.elig;
    
    let process = "Entrance Exam (KCET / COMEDK) or Management Quota.";
    if(course.level === "PG") process = "PGCET / GATE / KMAT.";
    if(course.level === "PhD") process = "VTU Eligibility Test for Research (ETR) + Interview.";
    if(course.level === "Minor") process = "Must have Min 5 CGPA in Major Degree (No Backlogs). Register in 5th Sem.";
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
