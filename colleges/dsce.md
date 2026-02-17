---
layout: default
title: "Dayananda Sagar College of Engineering (DSCE) Course Portal 🎓"
permalink: /colleges/dsce/
image: "https://www.dsce.edu.in/images/slider/01.jpg"
description: "Browse B.E, M.Tech, MBA, and MCA courses at DSCE. Check 2025-26 Fees (CET, COMEDK, Mgmt), Eligibility, and Placements."
---

<meta property="og:title" content="DSCE Course Portal 🎓">
<meta property="og:description" content="Access details for 30+ courses: B.E, MBA, M.Tech, MCA. Check 2025 Fees, Eligibility, and Career Outcomes.">
<meta property="og:image" content="https://www.dsce.edu.in/images/slider/01.jpg">

<style>
  /* 1. LAYOUT RESET */
  .main-content { max-width: 100% !important; padding: 0 !important; margin: 0 !important; }
  body { background-color: #f4f6f8; font-family: 'Segoe UI', system-ui, sans-serif; color: #333; }

  /* 2. HERO SECTION */
  .dsce-hero {
    background: linear-gradient(rgba(0, 51, 102, 0.8), rgba(0, 0, 0, 0.7)), url('https://www.dsce.edu.in/images/slider/01.jpg');
    background-size: cover;
    background-position: center;
    color: white;
    text-align: center;
    padding: 80px 20px;
    margin-bottom: 0;
  }
  
  .dsce-hero h1 { font-size: 2.8rem; margin: 0; font-weight: 800; color: white !important; }
  .dsce-hero p { font-size: 1.1rem; color: #ddd !important; margin-top: 10px; max-width: 700px; margin-left: auto; margin-right: auto; }

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
    border-top: 4px solid #003366; /* DSCE Blue */
    flex-shrink: 0;
  }

  .filter-group { margin-bottom: 20px; }
  .filter-label { display: block; font-weight: 700; margin-bottom: 8px; color: #003366; font-size: 0.9rem; }
  
  .filter-input, .filter-select {
    width: 100%;
    padding: 10px 15px;
    border: 1px solid #ddd;
    border-radius: 8px;
    font-size: 0.95rem;
    outline: none;
    transition: border 0.2s;
  }
  .filter-input:focus, .filter-select:focus { border-color: #003366; }

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
  .course-card:hover { transform: translateY(-3px); box-shadow: 0 8px 25px rgba(0,0,0,0.08); border-left-color: #003366; }

  /* Department Colors */
  .dept-Engg { border-left-color: #2196f3; }
  .dept-Mgmt { border-left-color: #9c27b0; }
  .dept-CA { border-left-color: #009688; }
  .dept-Arch { border-left-color: #ff9800; }
  .dept-Res { border-left-color: #795548; }

  .c-dept { font-size: 0.75rem; text-transform: uppercase; font-weight: 700; color: #888; margin-bottom: 5px; }
  .c-title { font-size: 1.1rem; font-weight: 700; color: #333; margin: 0 0 10px 0; line-height: 1.4; }
  .c-meta { display: flex; gap: 8px; flex-wrap: wrap; margin-bottom: 15px; }
  .c-badge { display: inline-block; background: #f0f2f5; padding: 4px 10px; border-radius: 4px; font-size: 0.75rem; font-weight: 600; color: #555; }
  
  .c-footer { margin-top: auto; display: flex; justify-content: space-between; align-items: center; border-top: 1px solid #f0f0f0; padding-top: 15px; }
  
  .view-btn {
    background: transparent; border: 1px solid #003366; color: #003366;
    padding: 6px 15px; border-radius: 50px; font-size: 0.85rem; font-weight: 600; cursor: pointer; transition: 0.2s;
  }
  .view-btn:hover { background: #003366; color: white; }

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
    background: #003366; padding: 20px 25px; color: white; display: flex; justify-content: space-between; align-items: center;
    position: sticky; top: 0; z-index: 10;
  }
  .modal-title { margin: 0; font-size: 1.2rem; font-weight: 700; }
  .close-modal { background: none; border: none; color: white; font-size: 2rem; cursor: pointer; }
  
  .modal-body { padding: 25px; }

  .info-block { margin-bottom: 25px; }
  .info-head { font-size: 0.95rem; font-weight: 700; color: #003366; border-bottom: 2px solid #f0f0f0; padding-bottom: 5px; margin-bottom: 10px; display: flex; align-items: center; gap: 8px; }
  .info-content { font-size: 0.95rem; color: #444; line-height: 1.6; }
  
  .fee-table { width: 100%; border-collapse: collapse; margin-top: 10px; font-size: 0.9rem; background: #fdfdfd; }
  .fee-table td { padding: 10px; border-bottom: 1px solid #eee; }
  .fee-table td:first-child { font-weight: 600; color: #555; }
  .fee-table td:last-child { text-align: right; font-weight: bold; color: #003366; }

  @keyframes slideUp { from { transform: translateY(50px); opacity: 0; } to { transform: translateY(0); opacity: 1; } }

  /* Mobile */
  @media (max-width: 900px) {
    .app-container { flex-direction: column; }
    .filters-sidebar { width: 100%; position: static; }
  }
</style>

<div class="dsce-hero">
  <h1>Dayananda Sagar College of Engineering</h1>
  <p>An Autonomous Institute Affiliated to VTU. Approved by AICTE & UGC. Accredited by NAAC with 'A' Grade.</p>
</div>

<div class="app-container">

  <aside class="filters-sidebar">
    <div class="filter-group">
      <label class="filter-label">🔍 Search Course</label>
      <input type="text" id="searchInput" class="filter-input" placeholder="e.g. Artificial Intelligence, MBA..." onkeyup="renderCourses()">
    </div>
    
    <div class="filter-group">
      <label class="filter-label">🎓 Programme Level</label>
      <select id="levelFilter" class="filter-select" onchange="renderCourses()">
        <option value="All">All Levels</option>
        <option value="UG">Undergraduate (B.E/B.Arch)</option>
        <option value="PG">Postgraduate (M.Tech/MBA/MCA)</option>
        <option value="PhD">Doctoral (PhD)</option>
      </select>
    </div>

    <div class="filter-group">
      <label class="filter-label">🏫 Department</label>
      <select id="deptFilter" class="filter-select" onchange="renderCourses()">
        <option value="All">All Departments</option>
        <option value="Engg">Engineering</option>
        <option value="Arch">Architecture</option>
        <option value="Mgmt">Management</option>
        <option value="CA">Computer Applications</option>
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
        <a href="https://www.dsce.edu.in/admissions" target="_blank" style="background:#003366; color:white; padding:12px 30px; border-radius:50px; text-decoration:none; font-weight:bold;">Official Admission Page ↗</a>
      </div>

    </div>
  </div>
</div>

<script>
  // --- 1. COURSE DATABASE (DSCE) ---
  const courses = [
    // --- B.E. / B.Tech (UG) ---
    { id: 1, name: "B.E. Computer Science & Engg", dept: "Engg", level: "UG", fee: { "CET": "₹1,14,706", "COMEDK": "₹2,61,260", "Mgmt": "₹4.5 - 6.5 Lakhs" }, elig: "10+2 with 45% (Physics & Maths Compulsory).", career: "Software Engineer, Data Scientist, System Architect." },
    { id: 2, name: "B.E. Artificial Intelligence & ML", dept: "Engg", level: "UG", fee: { "CET": "₹1,14,706", "COMEDK": "₹2,61,260", "Mgmt": "₹5.0 - 7.0 Lakhs" }, elig: "10+2 with 45% (PCM).", career: "AI Engineer, ML Specialist, Robotics." },
    { id: 3, name: "B.E. Electronics & Communication", dept: "Engg", level: "UG", fee: { "CET": "₹1,14,706", "COMEDK": "₹2,61,260", "Mgmt": "₹3.5 - 4.5 Lakhs" }, elig: "10+2 with 45% (PCM).", career: "VLSI Engineer, Embedded Systems, Telecom." },
    { id: 4, name: "B.E. Mechanical Engineering", dept: "Engg", level: "UG", fee: { "CET": "₹1,14,706", "COMEDK": "₹2,61,260", "Mgmt": "₹2.0 - 3.0 Lakhs" }, elig: "10+2 with 45% (PCM).", career: "Mechanical Design, Automotive Engg, Manufacturing." },
    { id: 5, name: "B.E. Civil Engineering", dept: "Engg", level: "UG", fee: { "CET": "₹1,14,706", "COMEDK": "₹2,61,260", "Mgmt": "₹1.5 - 2.5 Lakhs" }, elig: "10+2 with 45% (PCM).", career: "Structural Engineer, Construction Manager." },
    { id: 6, name: "B.E. Aerospace Engineering", dept: "Engg", level: "UG", fee: { "CET": "₹1,14,706", "COMEDK": "₹2,61,260", "Mgmt": "₹3.0 - 4.0 Lakhs" }, elig: "10+2 with 45% (PCM).", career: "Aerospace Engineer, Avionics, Defense R&D." },
    { id: 7, name: "B.E. Biotechnology", dept: "Engg", level: "UG", fee: { "CET": "₹1,14,706", "COMEDK": "₹2,61,260", "Mgmt": "₹2.5 Lakhs" }, elig: "10+2 with 45% (PCB/M).", career: "Biotech Researcher, Pharma Industry, Lab Tech." },
    { id: 8, name: "B.E. Chemical Engineering", dept: "Engg", level: "UG", fee: { "CET": "₹1,14,706", "COMEDK": "₹2,61,260", "Mgmt": "₹2.0 Lakhs" }, elig: "10+2 with 45% (PCM).", career: "Process Engineer, Petrochemical Industry." },
    { id: 9, name: "B.E. Information Science & Engg", dept: "Engg", level: "UG", fee: { "CET": "₹1,14,706", "COMEDK": "₹2,61,260", "Mgmt": "₹4.0 - 5.0 Lakhs" }, elig: "10+2 with 45% (PCM).", career: "IT Consultant, Web Dev, Database Admin." },
    { id: 10, name: "B.E. Medical Electronics", dept: "Engg", level: "UG", fee: { "CET": "₹1,14,706", "COMEDK": "₹2,61,260", "Mgmt": "₹2.0 Lakhs" }, elig: "10+2 with 45% (PCM).", career: "Biomedical Engineer, Healthcare Tech." },
    { id: 11, name: "B.E. Robotics & AI", dept: "Engg", level: "UG", fee: { "CET": "₹1,14,706", "COMEDK": "₹2,61,260", "Mgmt": "₹3.5 - 4.5 Lakhs" }, elig: "10+2 with 45% (PCM).", career: "Robotics Engineer, Automation Specialist." },
    { id: 12, name: "B.E. Cyber Security", dept: "Engg", level: "UG", fee: { "CET": "₹1,14,706", "COMEDK": "₹2,61,260", "Mgmt": "₹4.5 - 5.5 Lakhs" }, elig: "10+2 with 45% (PCM).", career: "Cyber Security Analyst, Network Security." },
    
    // --- ARCHITECTURE ---
    { id: 13, name: "B.Arch (Architecture)", dept: "Arch", level: "UG", fee: { "CET": "₹1,14,706", "COMEDK": "₹2,61,260", "Mgmt": "₹3.5 Lakhs" }, elig: "10+2 with 50% (Maths) + NATA Score.", career: "Architect, Urban Planner, Interior Designer." },

    // --- PG (MBA, MCA, M.Tech) ---
    { id: 14, name: "Master of Business Admin (MBA)", dept: "Mgmt", level: "PG", fee: { "PGCET": "₹1,00,000", "Mgmt": "₹3.5 Lakhs" }, elig: "Degree (50%) + PGCET/KMAT/CMAT.", career: "HR Manager, Marketing Lead, Finance Analyst." },
    { id: 15, name: "Master of Computer App (MCA)", dept: "CA", level: "PG", fee: { "PGCET": "₹1,00,000", "Mgmt": "₹2.5 Lakhs" }, elig: "Degree (50%) with Maths + PGCET/KMAT.", career: "Software Engineer, System Analyst." },
    { id: 16, name: "M.Tech (Structural/Highway/VLSI)", dept: "Engg", level: "PG", fee: { "PGCET": "₹1,00,000", "Mgmt": "₹1.5 Lakhs" }, elig: "B.E./B.Tech (50%) + GATE/PGCET.", career: "Specialized Engineer, R&D, Consultant." },
    { id: 17, name: "M.Tech (Computer Science)", dept: "Engg", level: "PG", fee: { "PGCET": "₹1,00,000", "Mgmt": "₹1.5 Lakhs" }, elig: "B.E./B.Tech (50%) + GATE/PGCET.", career: "Senior Engineer, Tech Lead, R&D." },

    // --- PHD ---
    { id: 18, name: "Ph.D / M.Sc (Engg) by Research", dept: "Res", level: "PhD", fee: { "Tuition": "As per VTU Norms" }, elig: "Master's Degree in relevant field + Interview.", career: "Professor, Research Scientist." }
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
    if (code === 'Arch') return 'Architecture';
    if (code === 'Mgmt') return 'Management';
    if (code === 'CA') return 'Computer App';
    if (code === 'Res') return 'Research';
    return code;
  }

  // --- 3. DETAILS MODAL LOGIC ---
  function openDetails(id) {
    const course = courses.find(c => c.id === id);
    if (!course) return;

    document.getElementById('mTitle').innerText = course.name;
    document.getElementById('mElig').innerText = course.elig;
    
    let process = "Entrance Exam (KCET / COMEDK) or Management Quota.";
    if(course.level === "PG") process = "PGCET / GATE / KMAT / CMAT.";
    if(course.dept === "Arch") process = "NATA Score + 10+2 Marks.";
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
