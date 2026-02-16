---
layout: default
title: "Indian Institute of Science (IISc) Course Portal 🎓"
permalink: /colleges/iisc/
image: "https://iisc.ac.in/wp-content/uploads/2020/08/main-building.jpg"
description: "Browse Undergraduate (B.Sc, B.Tech), Masters (M.Tech, M.Des, M.Mgt), and PhD programs at IISc. Check eligibility, fees, and GATE/JEE cutoffs."
---

<meta property="og:title" content="IISc Bangalore Course Portal 🎓">
<meta property="og:description" content="Access details for B.Sc (Research), B.Tech (Math & Computing), M.Tech, and PhD programs. Check fees, eligibility, and selection process.">
<meta property="og:image" content="https://iisc.ac.in/wp-content/uploads/2020/08/main-building.jpg">

<style>
  /* 1. LAYOUT RESET */
  .main-content { max-width: 100% !important; padding: 0 !important; margin: 0 !important; }
  body { background-color: #f4f6f8; font-family: 'Segoe UI', system-ui, sans-serif; color: #333; }

  /* 2. HERO SECTION */
  .iisc-hero {
    background: linear-gradient(rgba(0, 40, 85, 0.9), rgba(0, 40, 85, 0.7)), url('https://iisc.ac.in/wp-content/uploads/2020/08/main-building.jpg');
    background-size: cover;
    background-position: center;
    color: white;
    text-align: center;
    padding: 80px 20px;
    margin-bottom: 0;
  }
  
  .iisc-hero h1 { font-size: 2.8rem; margin: 0; font-weight: 800; color: #fff !important; }
  .iisc-hero p { font-size: 1.1rem; color: #ddd !important; margin-top: 10px; max-width: 700px; margin-left: auto; margin-right: auto; }

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
    border-top: 4px solid #005a9c; /* IISc Blue */
    flex-shrink: 0;
  }

  .filter-group { margin-bottom: 20px; }
  .filter-label { display: block; font-weight: 700; margin-bottom: 8px; color: #005a9c; font-size: 0.9rem; }
  
  .filter-input, .filter-select {
    width: 100%;
    padding: 10px 15px;
    border: 1px solid #ddd;
    border-radius: 8px;
    font-size: 0.95rem;
    outline: none;
    transition: border 0.2s;
  }
  .filter-input:focus, .filter-select:focus { border-color: #005a9c; }

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
  .course-card:hover { transform: translateY(-3px); box-shadow: 0 8px 25px rgba(0,0,0,0.08); border-left-color: #f1c40f; }

  /* Level Colors */
  .level-UG { border-left-color: #2196f3; }
  .level-PG { border-left-color: #9c27b0; }
  .level-Research { border-left-color: #ff9800; }
  .level-PhD { border-left-color: #f44336; }

  .c-school { font-size: 0.75rem; text-transform: uppercase; font-weight: 700; color: #888; margin-bottom: 5px; }
  .c-title { font-size: 1.1rem; font-weight: 700; color: #333; margin: 0 0 10px 0; line-height: 1.4; }
  .c-meta { display: flex; gap: 8px; flex-wrap: wrap; margin-bottom: 15px; }
  .c-badge { display: inline-block; background: #f0f2f5; padding: 4px 10px; border-radius: 4px; font-size: 0.75rem; font-weight: 600; color: #555; }
  
  .c-footer { margin-top: auto; display: flex; justify-content: space-between; align-items: center; border-top: 1px solid #f0f0f0; padding-top: 15px; }
  
  .view-btn {
    background: transparent; border: 1px solid #005a9c; color: #005a9c;
    padding: 6px 15px; border-radius: 50px; font-size: 0.85rem; font-weight: 600; cursor: pointer; transition: 0.2s;
  }
  .view-btn:hover { background: #005a9c; color: white; }

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
    background: #005a9c; padding: 20px 25px; color: white; display: flex; justify-content: space-between; align-items: center;
    position: sticky; top: 0; z-index: 10;
  }
  .modal-title { margin: 0; font-size: 1.2rem; font-weight: 700; }
  .close-modal { background: none; border: none; color: white; font-size: 2rem; cursor: pointer; }
  
  .modal-body { padding: 25px; }

  .info-block { margin-bottom: 25px; }
  .info-head { font-size: 0.95rem; font-weight: 700; color: #005a9c; border-bottom: 2px solid #f0f0f0; padding-bottom: 5px; margin-bottom: 10px; display: flex; align-items: center; gap: 8px; }
  .info-content { font-size: 0.95rem; color: #444; line-height: 1.6; }
  
  .fee-table { width: 100%; border-collapse: collapse; margin-top: 10px; font-size: 0.9rem; background: #fdfdfd; }
  .fee-table td { padding: 10px; border-bottom: 1px solid #eee; }
  .fee-table td:first-child { font-weight: 600; color: #555; }
  .fee-table td:last-child { text-align: right; font-weight: bold; color: #005a9c; }

  @keyframes slideUp { from { transform: translateY(50px); opacity: 0; } to { transform: translateY(0); opacity: 1; } }

  /* Mobile */
  @media (max-width: 900px) {
    .app-container { flex-direction: column; }
    .filters-sidebar { width: 100%; position: static; }
  }
</style>

<div class="iisc-hero">
  <h1>Indian Institute of Science (IISc)</h1>
  <p>India's #1 Ranked University for Scientific Research & Advanced Engineering.</p>
</div>

<div class="app-container">

  <aside class="filters-sidebar">
    <div class="filter-group">
      <label class="filter-label">🔍 Search Course</label>
      <input type="text" id="searchInput" class="filter-input" placeholder="e.g. Data Science, Aerospace..." onkeyup="renderCourses()">
    </div>
    
    <div class="filter-group">
      <label class="filter-label">🎓 Programme Level</label>
      <select id="levelFilter" class="filter-select" onchange="renderCourses()">
        <option value="All">All Levels</option>
        <option value="UG">Undergraduate (UG)</option>
        <option value="PG_Course">PG (M.Tech/M.Des/M.Mgt)</option>
        <option value="PG_Res">PG Research (M.Tech Res)</option>
        <option value="PhD">Doctoral (PhD)</option>
        <option value="Online">Online Degree</option>
      </select>
    </div>

    <div class="filter-group">
      <label class="filter-label">🏫 Department/Div</label>
      <select id="deptFilter" class="filter-select" onchange="renderCourses()">
        <option value="All">All Divisions</option>
        <option value="Science">Division of Sciences</option>
        <option value="Engineering">Division of Engineering</option>
        <option value="Interdisciplinary">Interdisciplinary</option>
        <option value="Management">Management Studies</option>
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
          <p><strong>Selection:</strong> <span id="mSelect"></span></p>
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
        <a href="https://iisc.ac.in/admissions/" target="_blank" style="background:#005a9c; color:white; padding:12px 30px; border-radius:50px; text-decoration:none; font-weight:bold;">Official Admissions Page ↗</a>
      </div>

    </div>
  </div>
</div>

<script>
  // --- 1. COURSE DATABASE (Based on Handbook 2025) ---
  const courses = [
    // --- UG ---
    { 
      id: 1, name: "Bachelor of Science (Research)", level: "UG", dept: "Science",
      elig: "12th Std (PCM) with 60%. Exams: JEE Main/Advanced, NEET-UG, or IAT.",
      process: "Merit list based on National Entrance Exams.",
      fee: { "Tuition": "₹10,000", "Total (GN/OBC)": "₹15,800", "SC/ST": "Fully Waived" },
      desc: "A 4-year interdisciplinary research program. Majors: Biology, Chemistry, Earth & Env Sci, Materials, Math, Physics.",
      career: "Top-tier PhDs abroad, R&D in Pharma/Tech, Scientific Officer."
    },
    { 
      id: 2, name: "B.Tech in Mathematics & Computing", level: "UG", dept: "Interdisciplinary",
      elig: "12th Std (PCM). Selection via JEE Advanced Rank.",
      process: "100% based on JEE Advanced Rank.",
      fee: { "Tuition": "₹2,00,000", "Total (GN/OBC)": "₹2,05,800" },
      desc: "Combines Math, CS, and Data Science. Focus on AI, ML, Quantum Computing, and Finance Tech.",
      career: "Data Scientist, Quant Analyst, AI Researcher, Software Engineer (FAANG)."
    },

    // --- PG COURSE (M.Tech) ---
    { 
      id: 3, name: "M.Tech in Aerospace Engineering", level: "PG_Course", dept: "Engineering",
      elig: "BE/B.Tech or equivalent. Valid GATE Score.",
      process: "100% GATE Score (Paper: AE/CE/ME/EC/EE).",
      fee: { "Tuition": "₹9,000", "Total (GN/OBC)": "₹14,800" },
      desc: "Specializations in Aerodynamics, Propulsion, Structures, and Guidance & Control.",
      career: "ISRO, DRDO, Airbus, Boeing, Rolls-Royce, PhD."
    },
    { 
      id: 4, name: "M.Tech in Artificial Intelligence", level: "PG_Course", dept: "Interdisciplinary",
      elig: "BE/B.Tech/M.Sc with CS/IT/Elec background.",
      process: "70% GATE Score + 30% Written Test/Interview.",
      fee: { "Tuition": "₹9,000", "Total (GN/OBC)": "₹14,800" },
      desc: "Cutting-edge AI, Deep Learning, Computer Vision, and Robotics offered by CSA/ECE/EE depts.",
      career: "AI Research Scientist, ML Engineer, Data Scientist (Google, Microsoft, Meta)."
    },
    { 
      id: 5, name: "M.Tech in Computer Science & Engg", level: "PG_Course", dept: "Engineering",
      elig: "BE/B.Tech or equivalent. Valid GATE (CS) Score.",
      process: "100% GATE Score (CS paper).",
      fee: { "Tuition": "₹9,000", "Total (GN/OBC)": "₹14,800" },
      desc: "Rigorous coursework in Systems, Theory, and Intelligent Systems.",
      career: "System Architect, Senior Dev, R&D Labs, PhD."
    },
    { 
      id: 6, name: "M.Tech in Electronics & Comm (ECE)", level: "PG_Course", dept: "Engineering",
      elig: "BE/B.Tech. Valid GATE (EC) Score.",
      process: "70% GATE Score + 30% Interview.",
      fee: { "Tuition": "₹9,000", "Total (GN/OBC)": "₹14,800" },
      desc: "Focus on Comm Networks, Signal Processing, and High-Frequency Circuits.",
      career: "Qualcomm, Intel, TI, 5G/6G R&D."
    },
     { 
      id: 7, name: "M.Tech in Mechanical Engineering", level: "PG_Course", dept: "Engineering",
      elig: "BE/B.Tech (Mech/Aero/Auto). Valid GATE (ME) Score.",
      process: "70% GATE Score + 30% Interview.",
      fee: { "Tuition": "₹9,000", "Total (GN/OBC)": "₹14,800" },
      desc: "Fluid Mechanics, Solid Mechanics, Design, Vibrations, and Thermal Sciences.",
      career: "General Electric, Tata Motors, Shell, PhD."
    },

    // --- OTHER MASTERS ---
    { 
      id: 8, name: "Master of Design (M.Des)", level: "PG_Course", dept: "Engineering",
      elig: "BE/B.Tech/B.Des/B.Arch. Valid GATE/CEED Score.",
      process: "70% GATE/CEED + 30% Design Aptitude Test & Interview.",
      fee: { "Tuition": "₹9,000", "Total (GN/OBC)": "₹14,800" },
      desc: "Product Design and Engineering. Fusion of technology, aesthetics, and ergonomics.",
      career: "Product Designer, UX Researcher, Innovation Lead."
    },
    { 
      id: 9, name: "Master of Management (M.Mgt)", level: "PG_Course", dept: "Management",
      elig: "BE/B.Tech with First Class. Valid GATE/CAT/GMAT.",
      process: "Group Discussion + Personal Interview.",
      fee: { "Tuition": "₹1,70,000", "Total (GN/OBC)": "₹2,52,100" },
      desc: "Business Analytics and Technology Management focus. Not a generic MBA.",
      career: "Business Analyst, Tech Consultant, Product Manager (Citigroup, Walmart, Cisco)."
    },
    { 
      id: 10, name: "M.Sc in Life Sciences", level: "PG_Course", dept: "Science",
      elig: "B.Sc or equivalent (Bio/Chem/Phy).",
      process: "100% based on JAM (Joint Admission Test) Score.",
      fee: { "Tuition": "₹16,000", "Total (GN/OBC)": "₹1,06,800" },
      desc: "Advanced research training in Biology, Genetics, and Biochemistry.",
      career: "PhD in Ivy Leagues, Biotech R&D (Biocon, Syngene)."
    },

    // --- RESEARCH ---
    { 
      id: 11, name: "M.Tech (Research)", level: "PG_Res", dept: "Engineering",
      elig: "BE/B.Tech/M.Sc. Valid GATE/NET Score.",
      process: "Interview (High weightage on research aptitude).",
      fee: { "Tuition": "₹9,000", "Total (GN/OBC)": "₹14,800" },
      desc: "Formerly M.Sc (Engg). 1-2 years of research thesis + minimal coursework.",
      career: "Perfect stepping stone to PhD or specialized R&D roles."
    },
    { 
      id: 12, name: "Doctor of Philosophy (PhD) - Science", level: "PhD", dept: "Science",
      elig: "M.Sc/BE/B.Tech. Valid GATE/JRF/NET/Inspire.",
      process: " rigorous Interview. Direct PhD available for CFIs top rankers.",
      fee: { "Tuition": "₹15,000", "Total (GN/OBC)": "₹20,800" },
      desc: "World-class research in Physics, Chem, Math, Bio, Earth Science.",
      career: "Professor (IIT/IISER), Scientist (NASA/CERN/Max Planck), Industry R&D."
    },
    { 
      id: 13, name: "Doctor of Philosophy (PhD) - Engineering", level: "PhD", dept: "Engineering",
      elig: "ME/M.Tech/BE/B.Tech. Valid GATE/NET.",
      process: "Rigorous Interview.",
      fee: { "Tuition": "₹15,000", "Total (GN/OBC)": "₹20,800" },
      desc: "Research in Aero, Civil, CS, EE, Mech, Materials, Nano, etc.",
      career: "R&D Head, Faculty, Entrepreneur, Deep-Tech Startups."
    },
    { 
      id: 14, name: "Integrated PhD (Int. PhD)", level: "PhD", dept: "Science",
      elig: "B.Sc / BE / B.Tech. Valid JAM/JEST Score.",
      process: "Interview.",
      fee: { "Tuition": "₹9,000", "Total (GN/OBC)": "₹14,800" },
      desc: "Fast-track PhD for brilliant undergraduates. Available in Bio, Chem, Math, Physics.",
      career: "Academic Research, Post-Doc fellowships."
    },

    // --- ONLINE ---
    { 
      id: 15, name: "M.Tech (Online) - AI / Data Science / ECE", level: "Online", dept: "Interdisciplinary",
      elig: "BE/B.Tech with 2 years industry experience. Sponsored by Company.",
      process: "Nomination by Company + Institute Selection.",
      fee: { "Course Credit": "₹22,500/credit", "Total": "~₹8-10 Lakhs" },
      desc: "Degree equivalent to regular M.Tech. Designed for working professionals.",
      career: "Senior Architect, Principal Engineer, Data Lead."
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
      const matchDept = deptFilter === 'All' || course.dept === deptFilter;

      if (matchSearch && matchLevel && matchDept) {
        count++;
        // School Color Class
        let colorClass = 'level-' + course.level.split('_')[0]; // Simple color map

        const card = `
          <div class="course-card ${colorClass}" style="animation-delay: ${count * 0.05}s">
            <div>
              <span class="c-school">${course.dept} Division</span>
              <h3 class="c-title">${course.name}</h3>
              <div class="c-meta">
                <span class="c-badge">${course.level.replace('_', ' ')}</span>
              </div>
            </div>
            <div class="c-footer">
              <span style="font-size:0.8rem; color:#666;">View Fees & Elig</span>
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
