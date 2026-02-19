---
layout: default
title: "Bangalore Institute of Technology (BIT) Course Portal 🎓"
permalink: /colleges/bit/
image: "https://images.unsplash.com/photo-1541339907198-e08756dedf3f?ixlib=rb-4.0.3&auto=format&fit=crop&w=1200&q=80"
description: "Browse B.E in AI, Data Science, IoT, along with MBA, MCA, M.Tech, and Ph.D. programs at BIT Bangalore."
---

<meta property="og:title" content="BIT Bangalore Course Portal 🎓">
<meta property="og:description" content="Access details for Engineering, Management, and Research courses at BIT. Check 2025/2026 Fees & Eligibility.">
<meta property="og:image" content="https://images.unsplash.com/photo-1541339907198-e08756dedf3f?ixlib=rb-4.0.3&auto=format&fit=crop&w=1200&q=80">

<style>
  /* 1. LAYOUT RESET */
  .main-content { max-width: 100% !important; padding: 0 !important; margin: 0 !important; }
  body { background-color: #f4f6f8; font-family: 'Segoe UI', system-ui, sans-serif; color: #333; }

  /* 2. HERO SECTION */
  .bit-hero {
    background: linear-gradient(rgba(0, 51, 160, 0.85), rgba(0, 0, 0, 0.7)), url('https://images.unsplash.com/photo-1564069114553-7215e1ff1890?ixlib=rb-4.0.3&auto=format&fit=crop&w=1600&q=80');
    background-size: cover;
    background-position: center;
    color: white;
    text-align: center;
    padding: 80px 20px;
    margin-bottom: 0;
  }
  
  .bit-hero h1 { font-size: 2.8rem; margin: 0; font-weight: 800; color: white !important; }
  .bit-hero p { font-size: 1.1rem; color: #f0f0f0 !important; margin-top: 10px; max-width: 700px; margin-left: auto; margin-right: auto; }

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
    border-top: 4px solid #0033a0; /* Royal Blue */
    flex-shrink: 0;
  }

  .filter-group { margin-bottom: 20px; }
  .filter-label { display: block; font-weight: 700; margin-bottom: 8px; color: #0033a0; font-size: 0.9rem; }
  
  .filter-input, .filter-select {
    width: 100%;
    padding: 10px 15px;
    border: 1px solid #ddd;
    border-radius: 8px;
    font-size: 0.95rem;
    outline: none;
    transition: border 0.2s;
  }
  .filter-input:focus, .filter-select:focus { border-color: #0033a0; }

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
  .course-card:hover { transform: translateY(-3px); box-shadow: 0 8px 25px rgba(0,0,0,0.08); border-left-color: #0033a0; }

  /* Department Colors */
  .dept-Engg { border-left-color: #0033a0; } /* Blue */
  .dept-Mgmt { border-left-color: #e65100; } /* Orange */
  .dept-CA { border-left-color: #2e7d32; } /* Green */
  .dept-Res { border-left-color: #6a1b9a; } /* Purple */

  .c-dept { font-size: 0.75rem; text-transform: uppercase; font-weight: 700; color: #888; margin-bottom: 5px; }
  .c-title { font-size: 1.1rem; font-weight: 700; color: #333; margin: 0 0 10px 0; line-height: 1.4; }
  .c-meta { display: flex; gap: 8px; flex-wrap: wrap; margin-bottom: 15px; }
  .c-badge { display: inline-block; background: #f0f2f5; padding: 4px 10px; border-radius: 4px; font-size: 0.75rem; font-weight: 600; color: #555; }
  
  .c-footer { margin-top: auto; display: flex; justify-content: space-between; align-items: center; border-top: 1px solid #f0f0f0; padding-top: 15px; }
  
  .view-btn {
    background: transparent; border: 1px solid #0033a0; color: #0033a0;
    padding: 6px 15px; border-radius: 50px; font-size: 0.85rem; font-weight: 600; cursor: pointer; transition: 0.2s;
  }
  .view-btn:hover { background: #0033a0; color: white; }

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
    background: #0033a0; padding: 20px 25px; color: white; display: flex; justify-content: space-between; align-items: center;
    position: sticky; top: 0; z-index: 10;
  }
  .modal-title { margin: 0; font-size: 1.2rem; font-weight: 700; }
  .close-modal { background: none; border: none; color: white; font-size: 2rem; cursor: pointer; }
  
  .modal-body { padding: 25px; }

  .info-block { margin-bottom: 25px; }
  .info-head { font-size: 0.95rem; font-weight: 700; color: #0033a0; border-bottom: 2px solid #f0f0f0; padding-bottom: 5px; margin-bottom: 10px; display: flex; align-items: center; gap: 8px; }
  .info-content { font-size: 0.95rem; color: #444; line-height: 1.6; }
  
  .fee-table { width: 100%; border-collapse: collapse; margin-top: 10px; font-size: 0.9rem; background: #fdfdfd; }
  .fee-table td { padding: 10px; border-bottom: 1px solid #eee; }
  .fee-table td:first-child { font-weight: 600; color: #555; }
  .fee-table td:last-child { text-align: right; font-weight: bold; color: #0033a0; }

  @keyframes slideUp { from { transform: translateY(50px); opacity: 0; } to { transform: translateY(0); opacity: 1; } }

  /* Mobile */
  @media (max-width: 900px) {
    .app-container { flex-direction: column; }
    .filters-sidebar { width: 100%; position: static; }
  }
</style>

<div class="bit-hero">
  <h1>Bangalore Institute of Technology (BIT)</h1>
  <p>Affiliated to VTU | Approved by AICTE | Recognized Research Centers | Est. 1979</p>
</div>

<div class="app-container">

  <aside class="filters-sidebar">
    <div class="filter-group">
      <label class="filter-label">🔍 Search Course</label>
      <input type="text" id="searchInput" class="filter-input" placeholder="e.g. AI, VLSI, Physics..." onkeyup="renderCourses()">
    </div>
    
    <div class="filter-group">
      <label class="filter-label">🎓 Programme Level</label>
      <select id="levelFilter" class="filter-select" onchange="renderCourses()">
        <option value="All">All Levels</option>
        <option value="UG">Undergraduate (B.E)</option>
        <option value="PG">Postgraduate (MBA/MCA/M.Tech)</option>
        <option value="PhD">Ph.D. / Research</option>
      </select>
    </div>

    <div class="filter-group">
      <label class="filter-label">🏫 Department</label>
      <select id="deptFilter" class="filter-select" onchange="renderCourses()">
        <option value="All">All Departments</option>
        <option value="Engg">Core Engineering</option>
        <option value="Mgmt">Management Studies (MBA)</option>
        <option value="CA">Computer Applications (MCA)</option>
        <option value="Res">Basic Sciences & Research</option>
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
        <div class="info-head">🚀 Career Outcomes / Research Area</div>
        <div class="info-content" id="mCareers"></div>
      </div>
      
      <div style="text-align:center; margin-top:30px;">
        <a href="https://bit-bangalore.edu.in/admissions" target="_blank" style="background:#0033a0; color:white; padding:12px 30px; border-radius:50px; text-decoration:none; font-weight:bold;">Official Admission Page ↗</a>
      </div>

    </div>
  </div>
</div>

<script>
  // --- 1. COURSE DATABASE (BIT BANGALORE) ---
  const courses = [
    // --- UNDERGRADUATE (B.E.) ---
    { id: 1, name: "B.E. Computer Science & Engineering", dept: "Engg", level: "UG", fee: { "CET": "₹1,14,706", "COMEDK": "₹2,61,260", "Mgmt": "₹4.5 - 6.5 Lakhs" }, elig: "10+2 with 45% (PCM).", career: "Software Engineer, System Architect, Backend Developer." },
    { id: 2, name: "B.E. Information Science & Engineering", dept: "Engg", level: "UG", fee: { "CET": "₹1,14,706", "COMEDK": "₹2,61,260", "Mgmt": "₹4.0 - 5.5 Lakhs" }, elig: "10+2 with 45% (PCM).", career: "Database Administrator, IT Consultant, Cloud Engineer." },
    { id: 3, name: "B.E. Artificial Intelligence & Machine Learning", dept: "Engg", level: "UG", fee: { "CET": "₹1,14,706", "COMEDK": "₹2,61,260", "Mgmt": "₹4.0 - 6.0 Lakhs" }, elig: "10+2 with 45% (PCM).", career: "AI Engineer, ML Specialist, Deep Learning Researcher." },
    { id: 4, name: "B.E. CSE (Data Science)", dept: "Engg", level: "UG", fee: { "CET": "₹1,14,706", "COMEDK": "₹2,61,260", "Mgmt": "₹4.0 - 5.5 Lakhs" }, elig: "10+2 with 45% (PCM).", career: "Data Scientist, Data Analyst, Business Intelligence Analyst." },
    { id: 5, name: "B.E. CSE (IoT, Cyber Security & Blockchain)", dept: "Engg", level: "UG", fee: { "CET": "₹1,14,706", "COMEDK": "₹2,61,260", "Mgmt": "₹3.5 - 5.0 Lakhs" }, elig: "10+2 with 45% (PCM).", career: "Cyber Security Analyst, IoT Solutions Architect, Blockchain Developer." },
    { id: 6, name: "B.E. Electronics & Communication", dept: "Engg", level: "UG", fee: { "CET": "₹1,14,706", "COMEDK": "₹2,61,260", "Mgmt": "₹3.0 - 4.5 Lakhs" }, elig: "10+2 with 45% (PCM).", career: "VLSI Design, Telecommunications, Embedded Systems." },
    { id: 7, name: "B.E. Electrical & Electronics Engineering", dept: "Engg", level: "UG", fee: { "CET": "₹1,14,706", "COMEDK": "₹2,61,260", "Mgmt": "₹2.0 - 3.0 Lakhs" }, elig: "10+2 with 45% (PCM).", career: "Power Systems Engineer, EV Technology, Control Systems." },
    { id: 8, name: "B.E. Mechanical Engineering", dept: "Engg", level: "UG", fee: { "CET": "₹1,14,706", "COMEDK": "₹2,61,260", "Mgmt": "₹1.5 - 2.5 Lakhs" }, elig: "10+2 with 45% (PCM).", career: "Mechanical Design, HVAC, Automotive Engineering." },
    { id: 9, name: "B.E. Civil Engineering", dept: "Engg", level: "UG", fee: { "CET": "₹1,14,706", "COMEDK": "₹2,61,260", "Mgmt": "₹1.5 - 2.5 Lakhs" }, elig: "10+2 with 45% (PCM).", career: "Structural Engineer, Construction Manager, Urban Planner." },
    { id: 10, name: "B.E. Electronics & Instrumentation", dept: "Engg", level: "UG", fee: { "CET": "₹1,14,706", "COMEDK": "₹2,61,260", "Mgmt": "₹2.0 Lakhs" }, elig: "10+2 with 45% (PCM).", career: "Automation Engineer, Instrumentation Specialist." },
    { id: 11, name: "B.E. Industrial Engineering & Management", dept: "Engg", level: "UG", fee: { "CET": "₹1,14,706", "COMEDK": "₹2,61,260", "Mgmt": "₹2.0 Lakhs" }, elig: "10+2 with 45% (PCM).", career: "Operations Manager, Quality Control, Supply Chain." },
    { id: 12, name: "B.E. Robotics & Artificial Intelligence", dept: "Engg", level: "UG", fee: { "CET": "₹1,14,706", "COMEDK": "₹2,61,260", "Mgmt": "₹3.0 - 4.0 Lakhs" }, elig: "10+2 with 45% (PCM).", career: "Robotics Engineer, Automation Architect." },
    { id: 13, name: "B.E. Electronics Engg (VLSI Design & Tech)", dept: "Engg", level: "UG", fee: { "CET": "₹1,14,706", "COMEDK": "₹2,61,260", "Mgmt": "₹3.0 - 4.0 Lakhs" }, elig: "10+2 with 45% (PCM).", career: "Chip Design, Semiconductor Engineer, Hardware Architecture." },
    
    // --- POSTGRADUATE (MBA, MCA, M.Tech) ---
    { id: 14, name: "Master of Business Administration (MBA)", dept: "Mgmt", level: "PG", fee: { "PGCET": "₹1,00,000", "Mgmt": "₹2.5 - 3.5 Lakhs" }, elig: "Any Degree with 50%.", career: "Finance Manager, Marketing Head, HR Professional." },
    { id: 15, name: "Master of Computer Applications (MCA)", dept: "CA", level: "PG", fee: { "PGCET": "₹1,00,000", "Mgmt": "₹2.5 Lakhs" }, elig: "Degree (50%) with Maths at 10+2 or Degree level.", career: "Software Engineer, Full Stack Developer, Systems Analyst." },
    { id: 16, name: "M.Tech in VLSI Design & Embedded Systems", dept: "Engg", level: "PG", fee: { "PGCET": "₹1,00,000", "Mgmt": "₹1.5 Lakhs" }, elig: "B.E./B.Tech with 50%.", career: "Senior VLSI Engineer, Embedded Software Developer." },
    { id: 17, name: "M.Tech in Structural Engineering", dept: "Engg", level: "PG", fee: { "PGCET": "₹1,00,000", "Mgmt": "₹1.5 Lakhs" }, elig: "B.E. Civil with 50%.", career: "Structural Consultant, Principal Engineer." },

    // --- DOCTORAL & RESEARCH (Ph.D.) ---
    { id: 18, name: "Ph.D in Information Science (ISE)", dept: "Res", level: "PhD", fee: { "Tuition": "As per VTU Norms" }, elig: "M.Tech + VTU ETR.", career: "Research Areas: Data Mining, Image Processing, Wireless Networks." },
    { id: 19, name: "Ph.D in Electronics & Communication (ECE)", dept: "Res", level: "PhD", fee: { "Tuition": "As per VTU Norms" }, elig: "M.Tech + VTU ETR.", career: "Research Areas: Sensor Networks, VLSI, Antennas, Video Processing." },
    { id: 20, name: "Ph.D in Basic Sciences (Physics/Chemistry/Maths)", dept: "Res", level: "PhD", fee: { "Tuition": "As per VTU Norms" }, elig: "M.Sc + VTU ETR.", career: "Research Areas: Spectroscopy, Material Science, Polymers." }
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
        let colorClass = 'dept-' + course.dept;

        const card = `
          <div class="course-card ${colorClass}" style="animation-delay: ${count * 0.05}s">
            <div>
              <span class="c-dept">${getDeptName(course.dept)}</span>
              <h3 class="c-title">${course.name}</h3>
              <div class="c-meta">
                <span class="c-badge">${course.level}</span>
                <span class="c-badge">VTU Affiliated</span>
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
    if (code === 'CA') return 'Computer Applications';
    if (code === 'Res') return 'Research / Sciences';
    return code;
  }

  // --- 3. DETAILS MODAL LOGIC ---
  function openDetails(id) {
    const course = courses.find(c => c.id === id);
    if (!course) return;

    document.getElementById('mTitle').innerText = course.name;
    document.getElementById('mElig').innerText = course.elig;
    
    let process = "KCET / COMEDK Counselling or Management Quota.";
    if(course.level === "PG") process = "PGCET (Karnataka) / KMAT / GATE + Counselling.";
    if(course.level === "PhD") process = "VTU Eligibility Test for Research (ETR) + Interview. UGC-NET/GATE qualifiers are exempt from ETR.";
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
