---
layout: default
title: "B.M.S. College of Engineering Course Portal 🎓"
permalink: /colleges/bmsce/
image: "https://bmsce.ac.in/assets/images/banner/bmsce-banner-1.jpg"
description: "Browse Undergraduate (BE), Postgraduate (M.Tech, MBA, MCA), and PhD courses at BMSCE. Check 2025 Fees, Cutoffs, and Placements."
---

<meta property="og:title" content="BMSCE Course Portal 🎓">
<meta property="og:description" content="Access details for 20+ Engineering & Management courses: Eligibility, Fees, Cutoffs, and Placement Stats.">
<meta property="og:image" content="https://bmsce.ac.in/assets/images/banner/bmsce-banner-1.jpg">

<style>
  /* 1. LAYOUT RESET */
  .main-content { max-width: 100% !important; padding: 0 !important; margin: 0 !important; }
  body { background-color: #f0f2f5; font-family: 'Segoe UI', system-ui, sans-serif; color: #333; }

  /* 2. HERO SECTION */
  .bmsce-hero {
    background: linear-gradient(rgba(10, 35, 66, 0.9), rgba(10, 35, 66, 0.7)), url('https://bmsce.ac.in/assets/images/banner/bmsce-banner-1.jpg');
    background-size: cover;
    background-position: center;
    color: white;
    text-align: center;
    padding: 60px 20px;
    margin-bottom: 0;
  }
  .bmsce-hero h1 { font-size: 2.8rem; margin: 0; font-weight: 800; color: white !important; }
  .bmsce-hero p { font-size: 1.1rem; color: #ddd !important; margin-top: 10px; max-width: 700px; margin-left: auto; margin-right: auto; }

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
    border-top: 4px solid #0056b3; /* BMSCE Blue */
    flex-shrink: 0;
  }

  .filter-group { margin-bottom: 20px; }
  .filter-label { display: block; font-weight: 700; margin-bottom: 8px; color: #0056b3; font-size: 0.9rem; }
  
  .filter-input, .filter-select {
    width: 100%;
    padding: 10px 15px;
    border: 1px solid #ddd;
    border-radius: 8px;
    font-size: 0.95rem;
    outline: none;
    transition: border 0.2s;
  }
  .filter-input:focus, .filter-select:focus { border-color: #0056b3; }

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
  .course-card:hover { transform: translateY(-3px); box-shadow: 0 8px 25px rgba(0,0,0,0.08); border-left-color: #0056b3; }

  /* Department Colors */
  .dept-Engineering { border-left-color: #007bff; }
  .dept-CSE { border-left-color: #17a2b8; }
  .dept-Management { border-left-color: #e83e8c; }
  .dept-Science { border-left-color: #28a745; }

  .c-dept { font-size: 0.75rem; text-transform: uppercase; font-weight: 700; color: #888; margin-bottom: 5px; }
  .c-title { font-size: 1.1rem; font-weight: 700; color: #333; margin: 0 0 10px 0; line-height: 1.4; }
  .c-level { display: inline-block; background: #f0f2f5; padding: 4px 10px; border-radius: 4px; font-size: 0.8rem; font-weight: 600; color: #555; }
  
  .c-footer { margin-top: 15px; display: flex; justify-content: space-between; align-items: center; }
  
  .view-btn {
    background: transparent; border: 1px solid #0056b3; color: #0056b3;
    padding: 6px 15px; border-radius: 50px; font-size: 0.85rem; font-weight: 600; cursor: pointer; transition: 0.2s;
  }
  .view-btn:hover { background: #0056b3; color: white; }

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
    background: #0056b3; padding: 20px 25px; color: white; display: flex; justify-content: space-between; align-items: center;
    position: sticky; top: 0; z-index: 10;
  }
  .modal-title { margin: 0; font-size: 1.2rem; font-weight: 700; }
  .close-modal { background: none; border: none; color: white; font-size: 2rem; cursor: pointer; }
  
  .modal-body { padding: 25px; }

  .info-block { margin-bottom: 25px; }
  .info-head { font-size: 0.95rem; font-weight: 700; color: #0056b3; border-bottom: 2px solid #f0f0f0; padding-bottom: 5px; margin-bottom: 10px; display: flex; align-items: center; gap: 8px; }
  .info-content { font-size: 0.95rem; color: #444; line-height: 1.6; }
  
  .fee-table { width: 100%; border-collapse: collapse; margin-top: 10px; font-size: 0.9rem; background: #fdfdfd; }
  .fee-table td { padding: 10px; border-bottom: 1px solid #eee; }
  .fee-table td:first-child { font-weight: 600; color: #555; }
  .fee-table td:last-child { text-align: right; font-weight: bold; color: #0056b3; }

  @keyframes slideUp { from { transform: translateY(50px); opacity: 0; } to { transform: translateY(0); opacity: 1; } }

  /* Mobile */
  @media (max-width: 900px) {
    .app-container { flex-direction: column; }
    .filters-sidebar { width: 100%; position: static; }
  }
</style>

<div class="bmsce-hero">
  <h1>B.M.S. College of Engineering</h1>
  <p>First private engineering college in India. Established 1946. Autonomous Institute under VTU.</p>
</div>

<div class="app-container">

  <aside class="filters-sidebar">
    <div class="filter-group">
      <label class="filter-label">🔍 Search Course</label>
      <input type="text" id="searchInput" class="filter-input" placeholder="e.g. Computer Science, MBA..." onkeyup="renderCourses()">
    </div>
    
    <div class="filter-group">
      <label class="filter-label">🎓 Programme Level</label>
      <select id="levelFilter" class="filter-select" onchange="renderCourses()">
        <option value="All">All Levels</option>
        <option value="UG">Undergraduate (BE)</option>
        <option value="PG">Postgraduate (M.Tech/MBA/MCA)</option>
        <option value="PhD">Doctoral (PhD/M.Sc Engg)</option>
      </select>
    </div>

    <div class="filter-group">
      <label class="filter-label">🏫 Department</label>
      <select id="deptFilter" class="filter-select" onchange="renderCourses()">
        <option value="All">All Departments</option>
        <option value="Engineering">Core Engineering</option>
        <option value="CSE">Computer Science & AI</option>
        <option value="Management">Management & MBA</option>
        <option value="Science">Basic Sciences</option>
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
        <div class="info-content" id="mEligibility"></div>
      </div>

      <div class="info-block">
        <div class="info-head">📝 Admission Process</div>
        <div class="info-content" id="mProcess"></div>
      </div>

      <div class="info-block">
        <div class="info-head">💰 Fee Structure (Annual)</div>
        <table class="fee-table" id="mFees"></table>
      </div>

      <div class="info-block">
        <div class="info-head">🚀 Career Outcomes</div>
        <div class="info-content" id="mCareers"></div>
      </div>
      
      <div style="text-align:center; margin-top:30px;">
        <a href="https://bmsce.ac.in/home/Admission" target="_blank" style="background:#0056b3; color:white; padding:12px 30px; border-radius:50px; text-decoration:none; font-weight:bold;">Visit Official Page ↗</a>
      </div>

    </div>
  </div>
</div>

<script>
  // --- 1. COURSE DATABASE (Derived from BMSCE Website & Search Results) ---
  const courses = [
    // --- UG (B.E.) ---
    { 
      id: 1, name: "Civil Engineering", level: "UG", dept: "Engineering",
      elig: "Passed 10+2 with Physics & Math as compulsory subjects along with Chem/Bio/CS/Elec. Min 45% aggregate (40% for SC/ST/OBC).",
      process: "KCET (Govt Quota) or COMEDK (Pvt Quota) or Management Quota.",
      fee: { "KCET": "₹1,07,470", "COMEDK": "₹2,64,000", "Mgmt Quota": "₹3.5 Lakhs" },
      career: "Structural Engineer, Construction Manager, Govt Sector (PWD/NHAI), Higher Studies."
    },
    { 
      id: 2, name: "Mechanical Engineering", level: "UG", dept: "Engineering",
      elig: "Passed 10+2 with Physics & Math. Min 45% aggregate.",
      process: "KCET / COMEDK / Management Quota.",
      fee: { "KCET": "₹1,07,470", "COMEDK": "₹2,64,000", "Mgmt Quota": "₹4.0 Lakhs" },
      career: "Automotive Engineer, Robotics, Manufacturing, Aerospace, Design Engineer."
    },
    { 
      id: 3, name: "Electrical & Electronics Engg", level: "UG", dept: "Engineering",
      elig: "Passed 10+2 with Physics & Math. Min 45% aggregate.",
      process: "KCET / COMEDK / Management Quota.",
      fee: { "KCET": "₹1,07,470", "COMEDK": "₹2,64,000", "Mgmt Quota": "₹4.5 Lakhs" },
      career: "Power Systems Engineer, Control Systems, EV Technology, Electronics Design."
    },
    { 
      id: 4, name: "Electronics & Communication Engg", level: "UG", dept: "Engineering",
      elig: "Passed 10+2 with Physics & Math. Min 45% aggregate.",
      process: "KCET / COMEDK / Management Quota.",
      fee: { "KCET": "₹1,07,470", "COMEDK": "₹2,64,000", "Mgmt Quota": "₹6.0 Lakhs" },
      career: "VLSI Design, Embedded Systems, Telecom, Signal Processing, Software Roles."
    },
    { 
      id: 5, name: "Industrial Engg & Management", level: "UG", dept: "Engineering",
      elig: "Passed 10+2 with Physics & Math. Min 45% aggregate.",
      process: "KCET / COMEDK / Management Quota.",
      fee: { "KCET": "₹1,07,470", "COMEDK": "₹2,64,000", "Mgmt Quota": "₹4.5 Lakhs" },
      career: "Operations Manager, Supply Chain Analyst, Quality Assurance, Industrial Consultant."
    },
    { 
      id: 6, name: "Computer Science & Engineering", level: "UG", dept: "CSE",
      elig: "Passed 10+2 with Physics & Math. Min 45% aggregate. High demand course.",
      process: "KCET / COMEDK / Management Quota.",
      fee: { "KCET": "₹1,07,470", "COMEDK": "₹2,64,000", "Mgmt Quota": "₹10.0 Lakhs" },
      career: "Software Developer, Data Scientist, System Architect. Highest Placement Pkg: ₹50 LPA."
    },
    { 
      id: 7, name: "Information Science & Engg", level: "UG", dept: "CSE",
      elig: "Passed 10+2 with Physics & Math. Min 45% aggregate.",
      process: "KCET / COMEDK / Management Quota.",
      fee: { "KCET": "₹1,07,470", "COMEDK": "₹2,64,000", "Mgmt Quota": "₹7.5 Lakhs" },
      career: "IT Consultant, Web Developer, Database Admin, Network Engineer."
    },
    { 
      id: 8, name: "Bio Technology", level: "UG", dept: "Engineering",
      elig: "Passed 10+2 with Physics & Math. Biology optional subject.",
      process: "KCET / COMEDK / Management Quota.",
      fee: { "KCET": "₹1,07,470", "COMEDK": "₹2,64,000", "Mgmt Quota": "₹4.5 Lakhs" },
      career: "Biotech Research, Pharma Industry, Bioinformatics, Food Technology."
    },
    { 
      id: 9, name: "Chemical Engineering", level: "UG", dept: "Engineering",
      elig: "Passed 10+2 with Physics & Math. Chemistry optional subject.",
      process: "KCET / COMEDK / Management Quota.",
      fee: { "KCET": "₹1,07,470", "COMEDK": "₹2,64,000", "Mgmt Quota": "₹2.5 Lakhs" },
      career: "Chemical Process Engineer, Petrochemical Industry, Environmental Engineer."
    },
    { 
      id: 10, name: "Aerospace Engineering", level: "UG", dept: "Engineering",
      elig: "Passed 10+2 with Physics & Math. Min 45% aggregate.",
      process: "KCET / COMEDK / Management Quota.",
      fee: { "KCET": "₹1,07,470", "COMEDK": "₹2,64,000", "Mgmt Quota": "₹4.0 Lakhs" },
      career: "Aerodynamics Engineer, Propulsion Systems, Aircraft Design, Defense Sector."
    },
    { 
      id: 11, name: "AI & Machine Learning", level: "UG", dept: "CSE",
      elig: "Passed 10+2 with Physics & Math. Min 45% aggregate.",
      process: "KCET / COMEDK / Management Quota.",
      fee: { "KCET": "₹1,07,470", "COMEDK": "₹2,64,000", "Mgmt Quota": "₹8.5 Lakhs" },
      career: "AI Engineer, ML Specialist, Data Analyst, Research Scientist."
    },
    { 
      id: 12, name: "CSE (Data Science)", level: "UG", dept: "CSE",
      elig: "Passed 10+2 with Physics & Math. Min 45% aggregate.",
      process: "KCET / COMEDK / Management Quota.",
      fee: { "KCET": "₹1,07,470", "COMEDK": "₹2,64,000", "Mgmt Quota": "₹8.5 Lakhs" },
      career: "Data Scientist, Big Data Engineer, Business Intelligence Analyst."
    },
    { 
      id: 13, name: "CSE (IoT & Cyber Security)", level: "UG", dept: "CSE",
      elig: "Passed 10+2 with Physics & Math. Min 45% aggregate.",
      process: "KCET / COMEDK / Management Quota.",
      fee: { "KCET": "₹1,07,470", "COMEDK": "₹2,64,000", "Mgmt Quota": "₹8.5 Lakhs" },
      career: "Cyber Security Analyst, IoT Developer, Blockchain Developer, Network Security."
    },
    { 
      id: 14, name: "AI & Data Science", level: "UG", dept: "CSE",
      elig: "Passed 10+2 with Physics & Math. Min 45% aggregate.",
      process: "KCET / COMEDK / Management Quota.",
      fee: { "KCET": "₹1,07,470", "COMEDK": "₹2,64,000", "Mgmt Quota": "₹8.0 Lakhs" },
      career: "AI Research, Data Mining, Predictive Analytics, Software Development."
    },
     { 
      id: 15, name: "Computer Science & Business Systems", level: "UG", dept: "CSE",
      elig: "Passed 10+2 with Physics & Math. Min 45% aggregate.",
      process: "KCET / COMEDK / Management Quota.",
      fee: { "KCET": "₹1,07,470", "COMEDK": "₹2,64,000", "Mgmt Quota": "₹12.0 Lakhs (Est)" }, /* Note: Verify Mgmt fee */
      career: "Business Analyst, IT Consultant, Techno-Functional Roles."
    },

    // --- PG (M.Tech/MBA/MCA) ---
    { 
      id: 16, name: "Master of Computer Applications (MCA)", level: "PG", dept: "CSE",
      elig: "Bachelor's Degree with 50% agg. Maths/Stats/CS/Business Maths at 10+2 or Degree level.",
      process: "PGCET / KMAT / Management Quota.",
      fee: { "PGCET": "Govt Fixed", "Mgmt Quota": "₹3.5 Lakhs" },
      career: "Software Engineer, Web Developer, System Analyst, App Developer."
    },
    { 
      id: 17, name: "Master of Business Administration (MBA)", level: "PG", dept: "Management",
      elig: "Bachelor's Degree (min 3 years) with 50% agg (45% for SC/ST).",
      process: "PGCET / KMAT / CMAT / MAT / Management Quota.",
      fee: { "PGCET": "Govt Fixed", "Mgmt Quota": "₹4.5 Lakhs" },
      career: "HR Manager, Marketing Manager, Financial Analyst, Operations Lead."
    },
    { 
      id: 18, name: "M.Tech Computer Networking", level: "PG", dept: "CSE",
      elig: "BE/B.Tech in CS/IS/EC/TE with 50% agg. Valid GATE or PGCET score.",
      process: "GATE / PGCET / Management Quota.",
      fee: { "PGCET": "Govt Fixed", "Mgmt Quota": "₹1.5 Lakhs" },
      career: "Network Architect, Security Specialist, System Admin."
    },
    { 
      id: 19, name: "M.Tech Transportation Engg & Mgmt", level: "PG", dept: "Engineering",
      elig: "BE/B.Tech in Civil with 50% agg. Valid GATE or PGCET score.",
      process: "GATE / PGCET / Management Quota.",
      fee: { "PGCET": "Govt Fixed", "Mgmt Quota": "₹1.5 Lakhs" },
      career: "Transportation Planner, Highway Engineer, Project Manager."
    },
    { 
      id: 20, name: "M.Tech VLSI Design & Embedded Systems", level: "PG", dept: "Engineering",
      elig: "BE/B.Tech in EC/TE/IT/CS with 50% agg. Valid GATE or PGCET score.",
      process: "GATE / PGCET / Management Quota.",
      fee: { "PGCET": "Govt Fixed", "Mgmt Quota": "₹4.0 Lakhs" },
      career: "VLSI Design Engineer, Verification Engineer, Embedded Software Engineer."
    },
    { 
      id: 21, name: "M.Tech Construction Technology", level: "PG", dept: "Engineering",
      elig: "BE/B.Tech in Civil with 50% agg. Valid GATE or PGCET score.",
      process: "GATE / PGCET.",
      fee: { "PGCET": "Govt Fixed", "Mgmt Quota": "Contact College" },
      career: "Construction Project Manager, Site Engineer, Consultant."
    },
    { 
      id: 22, name: "M.Tech Environmental Engineering", level: "PG", dept: "Engineering",
      elig: "BE/B.Tech in Civil/Chemical/Env Engg with 50% agg.",
      process: "GATE / PGCET.",
      fee: { "PGCET": "Govt Fixed", "Mgmt Quota": "Contact College" },
      career: "Environmental Consultant, Water Treatment Engineer, Pollution Control."
    },
    { 
      id: 23, name: "M.Tech Machine Design", level: "PG", dept: "Engineering",
      elig: "BE/B.Tech in Mechanical/Auto/Aero with 50% agg.",
      process: "GATE / PGCET.",
      fee: { "PGCET": "Govt Fixed", "Mgmt Quota": "Contact College" },
      career: "Design Engineer, R&D in Auto/Aero, CAD Specialist."
    },
    { 
      id: 24, name: "M.Tech Power Electronics", level: "PG", dept: "Engineering",
      elig: "BE/B.Tech in EE/EC with 50% agg.",
      process: "GATE / PGCET.",
      fee: { "PGCET": "Govt Fixed", "Mgmt Quota": "Contact College" },
      career: "Power Electronics Engineer, EV Systems Engineer, R&D."
    },
    { 
      id: 25, name: "M.Tech Digital Communication", level: "PG", dept: "Engineering",
      elig: "BE/B.Tech in EC/TE with 50% agg.",
      process: "GATE / PGCET.",
      fee: { "PGCET": "Govt Fixed", "Mgmt Quota": "Contact College" },
      career: "Communication Systems Engineer, Network Planner, R&D."
    },

    // --- PHD ---
    { 
      id: 26, name: "PhD / M.Sc (Engg) by Research", level: "PhD", dept: "Science",
      elig: "Master's Degree (M.Tech/MBA/MCA/M.Sc) in relevant discipline. B.E/B.Tech with valid GATE for M.Sc (Engg).",
      process: "VTU Eligibility Test / GATE / NET followed by Interview.",
      fee: { "Tuition": "As per VTU Norms" },
      desc: "Research programs available in Civil, Mech, EEE, ECE, IEM, Chemical, MBA, Maths, Biotech, CSE, ISE, Physics, Chemistry, Telecom, and MCA.",
      career: "Research Scientist, Professor, R&D Head."
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
      const matchLevel = levelFilter === 'All' || course.level.startsWith(levelFilter); // Handles PG_Course etc.
      const matchDept = deptFilter === 'All' || course.dept === deptFilter;

      if (matchSearch && matchLevel && matchDept) {
        count++;
        // Department Color Class
        let colorClass = 'dept-' + course.dept;
        
        // Handle "Engineering" as a catch-all if needed or specific mapping
        if (course.dept === 'CSE') colorClass = 'dept-CSE';

        const card = `
          <div class="course-card ${colorClass}" style="animation-delay: ${count * 0.05}s">
            <div>
              <span class="c-dept">${course.dept} Dept</span>
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

  // --- 3. DETAILS MODAL LOGIC ---
  function openDetails(id) {
    const course = courses.find(c => c.id === id);
    if (!course) return;

    document.getElementById('mTitle').innerText = course.name;
    document.getElementById('mEligibility').innerText = course.elig;
    document.getElementById('mProcess').innerText = course.process;
    document.getElementById('mCareers').innerText = course.career || (course.desc ? course.desc + " -> Research/Academic Roles" : "Core Industry Roles, R&D, Higher Studies.");

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

<br>

Here is a video from YouTube that might be helpful:
[BMS College of Engineering - Admission, Fees, Placement, Campus Tour - Bangalore](https://www.youtube.com/watch?v=sS68rJ5729w)

This video provides a detailed overview of BMS College of Engineering, covering admission processes, fee structures, placement statistics, and a tour of the campus, which complements the course information provided above.
