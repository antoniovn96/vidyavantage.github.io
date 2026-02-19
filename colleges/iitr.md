---
layout: default
title: "IIT Roorkee Course Portal 🎓"
permalink: /colleges/iitr/
image: "https://images.unsplash.com/photo-1590012314607-cda9d9b699ae?ixlib=rb-4.0.3&auto=format&fit=crop&w=1600&q=80"
description: "Explore B.Tech, M.Tech, MBA, and Ph.D. programs at the Indian Institute of Technology Roorkee (IITR). Check 2025 Fees and Admission details."
---

<meta property="og:title" content="IIT Roorkee Course Portal 🎓">
<meta property="og:description" content="Access details for Engineering, Architecture, Sciences, and Management courses at IIT Roorkee. Check 2025 Fees, JEE Advanced/GATE Eligibility.">
<meta property="og:image" content="https://images.unsplash.com/photo-1590012314607-cda9d9b699ae?ixlib=rb-4.0.3&auto=format&fit=crop&w=1600&q=80">

<style>
  /* 1. LAYOUT RESET */
  .main-content { max-width: 100% !important; padding: 0 !important; margin: 0 !important; }
  body { background-color: #f4f6f8; font-family: 'Segoe UI', system-ui, sans-serif; color: #333; }

  /* 2. HERO SECTION */
  .iitr-hero {
    background: linear-gradient(rgba(0, 51, 102, 0.85), rgba(0, 0, 0, 0.7)), url('https://images.unsplash.com/photo-1590012314607-cda9d9b699ae?ixlib=rb-4.0.3&auto=format&fit=crop&w=1600&q=80');
    background-size: cover;
    background-position: center;
    color: white;
    text-align: center;
    padding: 80px 20px;
    margin-bottom: 0;
  }
  
  .iitr-hero h1 { font-size: 2.8rem; margin: 0; font-weight: 800; color: white !important; }
  .iitr-hero p { font-size: 1.1rem; color: #f0f0f0 !important; margin-top: 10px; max-width: 700px; margin-left: auto; margin-right: auto; }

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
    border-top: 4px solid #003366; /* IITR Blue Theme */
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
  .dept-Engg { border-left-color: #003366; } /* Blue */
  .dept-Arch { border-left-color: #c0392b; } /* Red */
  .dept-Sci { border-left-color: #27ae60; } /* Green */
  .dept-Mgmt { border-left-color: #f39c12; } /* Orange */
  .dept-Hum { border-left-color: #8e44ad; } /* Purple */

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

<div class="iitr-hero">
  <h1>Indian Institute of Technology Roorkee</h1>
  <p>NIRF Ranked #5 (Engineering) | Est. 1847 (Thomason College of Civil Engineering)</p>
</div>

<div class="app-container">

  <aside class="filters-sidebar">
    <div class="filter-group">
      <label class="filter-label">🔍 Search Course</label>
      <input type="text" id="searchInput" class="filter-input" placeholder="e.g. CSE, Data Science, MBA..." onkeyup="renderCourses()">
    </div>
    
    <div class="filter-group">
      <label class="filter-label">🎓 Programme Level</label>
      <select id="levelFilter" class="filter-select" onchange="renderCourses()">
        <option value="All">All Levels</option>
        <option value="UG">Undergraduate (B.Tech/B.Arch)</option>
        <option value="PG">Postgraduate (M.Tech/M.Sc/MBA)</option>
        <option value="PhD">Ph.D. / Research</option>
      </select>
    </div>

    <div class="filter-group">
      <label class="filter-label">🏫 Department</label>
      <select id="deptFilter" class="filter-select" onchange="renderCourses()">
        <option value="All">All Departments</option>
        <option value="Engg">Engineering & Tech</option>
        <option value="Arch">Architecture & Planning</option>
        <option value="Sci">Basic Sciences</option>
        <option value="Mgmt">Management Studies</option>
        <option value="Hum">Humanities & SS</option>
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
        <div class="info-head">🚀 Career Outcomes / Research Focus</div>
        <div class="info-content" id="mCareers"></div>
      </div>
      
      <div style="text-align:center; margin-top:30px;">
        <a href="https://iitr.ac.in/" target="_blank" style="background:#003366; color:white; padding:12px 30px; border-radius:50px; text-decoration:none; font-weight:bold;">Official Website ↗</a>
      </div>

    </div>
  </div>
</div>

<script>
  // --- 1. COURSE DATABASE (IIT ROORKEE) ---
  const courses = [
    // --- UNDERGRADUATE (B.Tech / B.Arch) ---
    { id: 1, name: "B.Tech. Computer Science & Engineering", dept: "Engg", level: "UG", fee: { "Tuition": "₹2,00,000 / year", "Hostel & Mess": "₹60,000 / year" }, elig: "10+2 with PCM (75%).", career: "Software Engineer, AI Researcher, System Architect." },
    { id: 2, name: "B.Tech. Electronics & Communication", dept: "Engg", level: "UG", fee: { "Tuition": "₹2,00,000 / year", "Hostel & Mess": "₹60,000 / year" }, elig: "10+2 with PCM (75%).", career: "VLSI Engineer, Telecom Specialist, Embedded Systems." },
    { id: 3, name: "B.Tech. Civil Engineering", dept: "Engg", level: "UG", fee: { "Tuition": "₹2,00,000 / year", "Hostel & Mess": "₹60,000 / year" }, elig: "10+2 with PCM (75%).", career: "Structural Engineer, Project Manager, Public Sector (IES)." },
    { id: 4, name: "B.Tech. Mechanical Engineering", dept: "Engg", level: "UG", fee: { "Tuition": "₹2,00,000 / year", "Hostel & Mess": "₹60,000 / year" }, elig: "10+2 with PCM (75%).", career: "Automotive Design, Robotics, Manufacturing Lead." },
    { id: 5, name: "B.Tech. Data Science & AI", dept: "Engg", level: "UG", fee: { "Tuition": "₹2,00,000 / year", "Hostel & Mess": "₹60,000 / year" }, elig: "10+2 with PCM (75%).", career: "Data Scientist, ML Engineer, AI Ethicist." },
    { id: 6, name: "B.Tech. Biosciences & Bioengineering", dept: "Engg", level: "UG", fee: { "Tuition": "₹2,00,000 / year", "Hostel & Mess": "₹60,000 / year" }, elig: "10+2 with PCM (75%).", career: "Biotech Researcher, Pharma R&D, Biomedical Engineer." },
    { id: 7, name: "Bachelor of Architecture (B.Arch)", dept: "Arch", level: "UG", fee: { "Tuition": "₹2,00,000 / year", "Hostel & Mess": "₹60,000 / year" }, elig: "10+2 with PCM (75%).", career: "Licensed Architect, Urban Planner, Landscape Designer." },
    { id: 8, name: "B.Tech. Chemical Engineering", dept: "Engg", level: "UG", fee: { "Tuition": "₹2,00,000 / year", "Hostel & Mess": "₹60,000 / year" }, elig: "10+2 with PCM (75%).", career: "Process Engineer, Petrochemical Analyst, Plant Manager." },

    // --- POSTGRADUATE (M.Tech, M.Sc, MBA) ---
    { id: 9, name: "M.Tech in Computer Science & Engg", dept: "Engg", level: "PG", fee: { "Tuition": "₹25,000 / year", "Hostel": "₹60,000 / year" }, elig: "B.E./B.Tech + Valid GATE Score.", career: "Senior Developer, Research Scientist, Academia." },
    { id: 10, name: "M.Tech in Artificial Intelligence", dept: "Engg", level: "PG", fee: { "Tuition": "₹25,000 / year", "Hostel": "₹60,000 / year" }, elig: "B.E./B.Tech + Valid GATE Score.", career: "AI Specialist, NLP Engineer, Computer Vision Expert." },
    { id: 11, name: "M.Tech in Structural Engineering", dept: "Engg", level: "PG", fee: { "Tuition": "₹25,000 / year", "Hostel": "₹60,000 / year" }, elig: "B.E. Civil + Valid GATE Score.", career: "Structural Consultant, Bridge Design Expert." },
    { id: 12, name: "M.Tech in VLSI & Microelectronics", dept: "Engg", level: "PG", fee: { "Tuition": "₹25,000 / year", "Hostel": "₹60,000 / year" }, elig: "B.E. ECE/EE + Valid GATE Score.", career: "Chip Designer, Verification Engineer, R&D." },
    { id: 13, name: "Master of Urban & Rural Planning (MURP)", dept: "Arch", level: "PG", fee: { "Tuition": "₹25,000 / year", "Hostel": "₹60,000 / year" }, elig: "B.Arch/B.Plan + GATE.", career: "City Planner, Smart City Consultant, Govt Advisor." },
    { id: 14, name: "M.Sc. in Chemistry", dept: "Sci", level: "PG", fee: { "Tuition": "₹20,000 / year", "Hostel": "₹60,000 / year" }, elig: "B.Sc + JAM Score.", career: "Industrial Chemist, Pharma Scientist, PhD Scholar." },
    { id: 15, name: "M.Sc. in Applied Geology", dept: "Sci", level: "PG", fee: { "Tuition": "₹20,000 / year", "Hostel": "₹60,000 / year" }, elig: "B.Sc + JAM Score.", career: "Geologist, Mining Consultant, Petroleum Industry." },
    { id: 16, name: "Master of Business Administration (MBA)", dept: "Mgmt", level: "PG", fee: { "Total Program Fee": "₹8,00,000 - ₹10,00,000" }, elig: "Graduation (60%) + CAT Score.", career: "Product Manager, Strategy Consultant, Finance Analyst." },

    // --- DOCTORAL (Ph.D.) ---
    { id: 17, name: "Ph.D. in Engineering (All Streams)", dept: "Engg", level: "PhD", fee: { "Tuition": "₹15,000 / year" }, elig: "M.Tech + GATE/NET or B.Tech (CFTI) with high CGPA.", career: "Professor, Chief Scientist, R&D Head." },
    { id: 18, name: "Ph.D. in Sciences (Phy/Chem/Maths)", dept: "Sci", level: "PhD", fee: { "Tuition": "₹15,000 / year" }, elig: "M.Sc + GATE/NET/JRF.", career: "Academic Researcher, Scientific Officer." },
    { id: 19, name: "Ph.D. in Humanities & Social Sciences", dept: "Hum", level: "PhD", fee: { "Tuition": "₹15,000 / year" }, elig: "MA/M.Sc + NET/JRF.", career: "Sociologist, Economist, Public Policy Expert." }
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
                <span class="c-badge">IIT Status</span>
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
    if (code === 'Sci') return 'Sciences';
    if (code === 'Mgmt') return 'Management';
    if (code === 'Hum') return 'Humanities';
    return code;
  }

  // --- 3. DETAILS MODAL LOGIC ---
  function openDetails(id) {
    const course = courses.find(c => c.id === id);
    if (!course) return;

    document.getElementById('mTitle').innerText = course.name;
    document.getElementById('mElig').innerText = course.elig;
    
    let process = "";
    if (course.level === "UG") process = "JoSAA Counselling based on JEE Advanced Rank. (JEE Main is screening only).";
    else if (course.name.includes("M.Tech")) process = "COAP Counselling based on GATE Score.";
    else if (course.name.includes("M.Sc")) process = "CCMN Counselling based on JAM Score.";
    else if (course.name.includes("MBA")) process = "Shortlisting via CAT Score + Personal Interview.";
    else if (course.level === "PhD") process = "Departmental Written Test + Interview. (NET/JRF/GATE required).";
    
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
