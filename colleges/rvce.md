---
layout: default
title: "RV College of Engineering (RVCE) ⚙️"
permalink: /colleges/rvce/
image: "https://rvce.edu.in/sites/default/files/logo_0.png"
description: "Admission 2025: Check Fees (KCET, COMEDK, Management), Placements, and Cutoffs for B.E., M.Tech, and MCA at RVCE Bangalore."
---

<meta property="og:title" content="RV College of Engineering Course Portal ⚙️">
<meta property="og:description" content="Admission 2025: Check Fees (KCET, COMEDK, Management), Placements, and Cutoffs.">
<meta property="og:image" content="https://rvce.edu.in/sites/default/files/logo_0.png">

<style>
  /* 1. LAYOUT RESET */
  .main-content { max-width: 100% !important; padding: 0 !important; margin: 0 !important; }
  body { background-color: #f4f6f8; font-family: 'Segoe UI', system-ui, sans-serif; color: #333; }

  /* 2. HERO SECTION */
  .rvce-hero {
    background: linear-gradient(rgba(0, 51, 102, 0.9), rgba(0, 51, 102, 0.8)), url('https://rvce.edu.in/sites/default/files/slider/slider1.jpg');
    background-size: cover;
    background-position: center;
    color: white;
    text-align: center;
    padding: 80px 20px;
    margin-bottom: 0;
    border-bottom: 5px solid #FFC107; /* RVCE Yellow */
  }
  
  .rvce-hero h1 { font-size: 2.8rem; margin: 0; font-weight: 800; color: #fff !important; }
  .rvce-hero p { font-size: 1.1rem; color: #ddd !important; margin-top: 10px; max-width: 700px; margin-left: auto; margin-right: auto; }

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
    border-top: 4px solid #003366;
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
  .course-card:hover { transform: translateY(-3px); box-shadow: 0 8px 25px rgba(0,0,0,0.08); border-left-color: #FFC107; }

  /* Level Colors */
  .level-UG { border-left-color: #003366; }
  .level-PG { border-left-color: #E91E63; }
  .level-PhD { border-left-color: #4CAF50; }

  .c-school { font-size: 0.75rem; text-transform: uppercase; font-weight: 700; color: #888; margin-bottom: 5px; }
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

<div class="rvce-hero">
  <h1>RV College of Engineering (RVCE)</h1>
  <p>Bengaluru's Top Rated Autonomous Institution. Excellence in Technical Education since 1963.</p>
</div>

<div class="app-container">

  <aside class="filters-sidebar">
    <div class="filter-group">
      <label class="filter-label">🔍 Search Course</label>
      <input type="text" id="searchInput" class="filter-input" placeholder="e.g. CSE, Aerospace, MCA..." onkeyup="renderCourses()">
    </div>
    
    <div class="filter-group">
      <label class="filter-label">🎓 Programme Level</label>
      <select id="levelFilter" class="filter-select" onchange="renderCourses()">
        <option value="All">All Levels</option>
        <option value="UG">B.E. (Undergraduate)</option>
        <option value="PG">M.Tech / MCA</option>
        <option value="PhD">Doctoral (PhD)</option>
      </select>
    </div>

    <div class="filter-group">
      <label class="filter-label">🏫 Department</label>
      <select id="deptFilter" class="filter-select" onchange="renderCourses()">
        <option value="All">All Departments</option>
        <option value="CS">Computer Science (CSE/ISE/AI)</option>
        <option value="Circuit">Electronics (ECE/EEE/EIE)</option>
        <option value="Core">Core Engg (Mech/Civil/Chem)</option>
        <option value="Special">Specialized (Aero/Bio)</option>
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
        <div class="info-head">📋 Programme Overview</div>
        <div class="info-content" id="mOverview"></div>
      </div>

      <div class="info-block">
        <div class="info-head">✅ Eligibility & Admission</div>
        <div class="info-content">
          <p><strong>Criteria:</strong> <span id="mElig"></span></p>
          <p><strong>Entrance Exams:</strong> <span id="mSelect"></span></p>
        </div>
      </div>

      <div class="info-block">
        <div class="info-head">💰 Fee Structure (Approx/Year)</div>
        <table class="fee-table" id="mFees"></table>
        <p style="font-size:0.8rem; color:#666; margin-top:5px;">*Management Quota fees are significantly higher than KCET/COMEDK fees.</p>
      </div>

      <div class="info-block">
        <div class="info-head">🚀 Placement Highlights</div>
        <div class="info-content" id="mCareers"></div>
      </div>
      
      <div style="text-align:center; margin-top:30px;">
        <a href="https://rvce.edu.in/admission" target="_blank" style="background:#003366; color:white; padding:12px 30px; border-radius:50px; text-decoration:none; font-weight:bold;">Official Admissions Page ↗</a>
      </div>

    </div>
  </div>
</div>

<script>
  // --- 1. COURSE DATABASE (Based on 2025 Data) ---
  const courses = [
    // --- B.E. COMPUTER SCIENCE CLUSTER ---
    { 
      id: 1, name: "B.E. Computer Science & Engineering (CSE)", level: "UG", dept: "CS",
      elig: "10+2 with Physics & Maths (Min 70% in Maths/Science for Mgmt Quota).",
      process: "KCET / COMEDK / Management Quota.",
      fee: { "KCET": "₹1.07 Lakhs", "COMEDK": "₹2.6 Lakhs", "Mgmt Quota": "₹16-18 Lakhs" },
      desc: "Top-tier program with 100% placement record. Focus on Algorithms, Systems, and AI.",
      career: "Highest Package: ₹62 LPA. Recruiters: Atlassian, Microsoft, Cisco."
    },
    { 
      id: 2, name: "B.E. CSE (Artificial Intelligence & ML)", level: "UG", dept: "CS",
      elig: "10+2 with Physics & Maths.",
      process: "KCET / COMEDK / Management Quota.",
      fee: { "KCET": "₹1.07 Lakhs", "COMEDK": "₹2.6 Lakhs", "Mgmt Quota": "₹14-16 Lakhs" },
      desc: "Specialized curriculum for AI, Neural Networks, and Deep Learning.",
      career: "AI Engineer, ML Specialist. Avg Package: ₹18 LPA."
    },
    { 
      id: 3, name: "B.E. CSE (Data Science)", level: "UG", dept: "CS",
      elig: "10+2 with Physics & Maths.",
      process: "KCET / COMEDK / Management Quota.",
      fee: { "KCET": "₹1.07 Lakhs", "COMEDK": "₹2.6 Lakhs", "Mgmt Quota": "₹13-15 Lakhs" },
      desc: "Focus on Big Data, Analytics, and Statistical Modeling.",
      career: "Data Scientist, Data Analyst. Avg Package: ₹16 LPA."
    },
    { 
      id: 4, name: "B.E. CSE (Cyber Security)", level: "UG", dept: "CS",
      elig: "10+2 with Physics & Maths.",
      process: "KCET / COMEDK / Management Quota.",
      fee: { "KCET": "₹1.07 Lakhs", "COMEDK": "₹2.6 Lakhs", "Mgmt Quota": "₹12-14 Lakhs" },
      desc: "Network Security, Cryptography, and Ethical Hacking.",
      career: "Security Analyst, Cyber Defense. Avg Package: ₹15 LPA."
    },
    { 
      id: 5, name: "B.E. Information Science & Engg (ISE)", level: "UG", dept: "CS",
      elig: "10+2 with Physics & Maths.",
      process: "KCET / COMEDK / Management Quota.",
      fee: { "KCET": "₹1.07 Lakhs", "COMEDK": "₹2.6 Lakhs", "Mgmt Quota": "₹10-12 Lakhs" },
      desc: "Similar to CSE but with focus on IT infrastructure and Application Dev.",
      career: "Software Dev, IT Consultant. Avg Package: ₹14 LPA."
    },

    // --- B.E. CIRCUIT BRANCHES ---
    { 
      id: 6, name: "B.E. Electronics & Communication (ECE)", level: "UG", dept: "Circuit",
      elig: "10+2 with Physics & Maths.",
      process: "KCET / COMEDK / Management Quota.",
      fee: { "KCET": "₹1.07 Lakhs", "COMEDK": "₹2.6 Lakhs", "Mgmt Quota": "₹9-11 Lakhs" },
      desc: "VLSI, Embedded Systems, and Communication Networks.",
      career: "Chip Design (Intel, Qualcomm), Core Electronics. Avg Package: ₹12 LPA."
    },
    { 
      id: 7, name: "B.E. Electrical & Electronics (EEE)", level: "UG", dept: "Circuit",
      elig: "10+2 with Physics & Maths.",
      process: "KCET / COMEDK / Management Quota.",
      fee: { "KCET": "₹1.07 Lakhs", "COMEDK": "₹2.6 Lakhs", "Mgmt Quota": "₹5-7 Lakhs" },
      desc: "Power Systems, Control Systems, and EV Technology.",
      career: "Power Grid, Bosch, Schneider Electric. Avg Package: ₹10 LPA."
    },
    { 
      id: 8, name: "B.E. Electronics & Instrumentation", level: "UG", dept: "Circuit",
      elig: "10+2 with Physics & Maths.",
      process: "KCET / COMEDK / Management Quota.",
      fee: { "KCET": "₹1.07 Lakhs", "COMEDK": "₹2.6 Lakhs", "Mgmt Quota": "₹4-6 Lakhs" },
      desc: "Automation, Sensors, and Biomedical Instrumentation.",
      career: "Automation Engineer, Siemens, Honeywell."
    },

    // --- B.E. CORE & SPECIALIZED ---
    { 
      id: 9, name: "B.E. Aerospace Engineering", level: "UG", dept: "Special",
      elig: "10+2 with Physics & Maths.",
      process: "KCET / COMEDK / Management Quota.",
      fee: { "KCET": "₹1.07 Lakhs", "COMEDK": "₹2.6 Lakhs", "Mgmt Quota": "₹7-9 Lakhs" },
      desc: "Avionics, Aerodynamics, and Propulsion Systems.",
      career: "Airbus, Boeing, ISRO, DRDO."
    },
    { 
      id: 10, name: "B.E. Biotechnology", level: "UG", dept: "Special",
      elig: "10+2 with Physics, Maths & Biology.",
      process: "KCET / COMEDK / Management Quota.",
      fee: { "KCET": "₹1.07 Lakhs", "COMEDK": "₹2.6 Lakhs", "Mgmt Quota": "₹6-8 Lakhs" },
      desc: "Genetic Engineering, Bioinformatics, and Pharma.",
      career: "Biocon, GSK, Research Labs."
    },
    { 
      id: 11, name: "B.E. Mechanical Engineering", level: "UG", dept: "Core",
      elig: "10+2 with Physics & Maths.",
      process: "KCET / COMEDK / Management Quota.",
      fee: { "KCET": "₹1.07 Lakhs", "COMEDK": "₹2.6 Lakhs", "Mgmt Quota": "₹5-7 Lakhs" },
      desc: "Thermodynamics, Robotics, and Manufacturing.",
      career: "Mercedes Benz, Tata Motors, General Electric."
    },
    { 
      id: 12, name: "B.E. Civil Engineering", level: "UG", dept: "Core",
      elig: "10+2 with Physics & Maths.",
      process: "KCET / COMEDK / Management Quota.",
      fee: { "KCET": "₹1.07 Lakhs", "COMEDK": "₹2.6 Lakhs", "Mgmt Quota": "₹3-5 Lakhs" },
      desc: "Structural Engg, Construction Mgmt, and Environmental Engg.",
      career: "L&T, Ultratech, Govt Infrastructure."
    },
    { 
      id: 13, name: "B.E. Chemical Engineering", level: "UG", dept: "Core",
      elig: "10+2 with Physics, Maths & Chem.",
      process: "KCET / COMEDK / Management Quota.",
      fee: { "KCET": "₹1.07 Lakhs", "COMEDK": "₹2.6 Lakhs", "Mgmt Quota": "₹3-4 Lakhs" },
      desc: "Process Engineering, Material Science.",
      career: "Reliance, Shell, Asian Paints."
    },

    // --- PG & RESEARCH ---
    { 
      id: 14, name: "Master of Computer Applications (MCA)", level: "PG", dept: "CS",
      elig: "BCA/B.Sc with Maths. PGCET/KMAT Score.",
      process: "PGCET Counseling or Management Quota.",
      fee: { "PGCET": "₹70,000", "Mgmt Quota": "₹5-6 Lakhs (Total)" },
      desc: "2-year program focusing on Application Development.",
      career: "Software Developer, System Analyst. Avg Package: ₹8 LPA."
    },
    { 
      id: 15, name: "M.Tech (CSE / VLSI / Struct / Highway)", level: "PG", dept: "Core",
      elig: "B.E./B.Tech + GATE/PGCET Score.",
      process: "GATE Preferred. PGCET for Karnataka students.",
      fee: { "PGCET": "₹65,000", "Mgmt Quota": "₹1.5 Lakhs" },
      desc: "Specialized Masters in 13+ disciplines including VLSI, Structural, and Product Design.",
      career: "R&D Roles, Senior Engineer, Teaching."
    },
    { 
      id: 16, name: "Ph.D (Doctoral Programs)", level: "PhD", dept: "Research",
      elig: "M.Tech/M.Sc with VTU Eligibility.",
      process: "VTU Entrance Test + Interview.",
      fee: { "Approx": "₹40,000 - ₹60,000 / Year" },
      desc: "Research available in all 15 departments under VTU Research Centre.",
      career: "Professor, Scientist, R&D Head."
    }
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
      
      // Dept Logic
      let matchDept = false;
      if (deptFilter === 'All') matchDept = true;
      else if (deptFilter === 'CS' && (course.dept === 'CS')) matchDept = true;
      else if (deptFilter === 'Circuit' && (course.dept === 'Circuit')) matchDept = true;
      else if (deptFilter === 'Core' && (course.dept === 'Core')) matchDept = true;
      else if (deptFilter === 'Special' && (course.dept === 'Special')) matchDept = true;
      else if (deptFilter === 'Interdisciplinary' && (course.dept === 'Research')) matchDept = true;

      if (matchSearch && matchLevel && matchDept) {
        count++;
        // School Color Class
        let colorClass = 'level-' + course.level;

        const card = `
          <div class="course-card ${colorClass}" style="animation-delay: ${count * 0.05}s">
            <div>
              <span class="c-school">${course.dept} Stream</span>
              <h3 class="c-title">${course.name}</h3>
              <div class="c-meta">
                <span class="c-badge">${course.level}</span>
              </div>
            </div>
            <div class="c-footer">
              <span style="font-size:0.8rem; color:#666;">View Fees & Cutoffs</span>
              <button class="view-btn" onclick="openDetails(${course.id})">Details</button>
            </div>
          </div>
        `;
        grid.innerHTML += card;
      }
    });

    document.getElementById('countDisplay').innerText = count;
  }

  // --- 3. DETAILS MODAL LOGIC ---
  function openDetails(id) {
    const course = courses.find(c => c.id === id);
    if (!course) return;

    document.getElementById('mTitle').innerText = course.name;
    document.getElementById('mOverview').innerText = course.desc;
    document.getElementById('mElig').innerText = course.elig;
    document.getElementById('mSelect').innerText = course.process;
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
