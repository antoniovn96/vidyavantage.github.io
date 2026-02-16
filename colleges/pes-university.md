---
layout: default
title: "PES University Course Portal 🎓"
permalink: /colleges/pes-university/
image: "https://pes.edu/wp-content/uploads/2022/07/PES-University-Banner.jpg"
description: "Explore 60+ courses at PES University (Ring Road, EC Campus, Hanumauth Nagar). Check PESSAT 2025 details, fees, and eligibility."
---

<meta property="og:title" content="PES University Course Portal 🎓">
<meta property="og:description" content="Browse B.Tech, BBA, B.Des, MBBS, and M.Tech programs. Check PESSAT/KCET/JEE eligibility and fees.">
<meta property="og:image" content="https://pes.edu/wp-content/uploads/2022/07/PES-University-Banner.jpg">

<style>
  /* 1. LAYOUT RESET */
  .main-content { max-width: 100% !important; padding: 0 !important; margin: 0 !important; }
  body { background-color: #f4f6f8; font-family: 'Segoe UI', system-ui, sans-serif; color: #333; }

  /* 2. HERO SECTION */
  .pes-hero {
    background: linear-gradient(rgba(0, 51, 102, 0.9), rgba(0, 51, 102, 0.8)), url('https://pes.edu/wp-content/uploads/2022/07/PES-University-Banner.jpg');
    background-size: cover;
    background-position: center;
    color: white;
    text-align: center;
    padding: 80px 20px;
    margin-bottom: 0;
    border-bottom: 5px solid #FF6600; /* PES Orange */
  }
  
  .pes-hero h1 { font-size: 2.8rem; margin: 0; font-weight: 800; color: #fff !important; }
  .pes-hero p { font-size: 1.1rem; color: #ddd !important; margin-top: 10px; max-width: 700px; margin-left: auto; margin-right: auto; }

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
  .filter-input:focus, .filter-select:focus { border-color: #FF6600; }

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
  .course-card:hover { transform: translateY(-3px); box-shadow: 0 8px 25px rgba(0,0,0,0.08); border-left-color: #FF6600; }

  /* School Colors */
  .school-Engineering { border-left-color: #2196f3; }
  .school-Management { border-left-color: #e91e63; }
  .school-Design { border-left-color: #9c27b0; }
  .school-Health { border-left-color: #4caf50; }
  .school-Law { border-left-color: #795548; }

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

<div class="pes-hero">
  <h1>PES University</h1>
  <p>Education for the Real World. Ring Road | Electronic City | Hanumanth Nagar</p>
</div>

<div class="app-container">

  <aside class="filters-sidebar">
    <div class="filter-group">
      <label class="filter-label">🔍 Search Course</label>
      <input type="text" id="searchInput" class="filter-input" placeholder="e.g. CSE, BBA, Design..." onkeyup="renderCourses()">
    </div>
    
    <div class="filter-group">
      <label class="filter-label">🎓 Programme Level</label>
      <select id="levelFilter" class="filter-select" onchange="renderCourses()">
        <option value="All">All Levels</option>
        <option value="UG">Undergraduate (UG)</option>
        <option value="PG">Postgraduate (PG)</option>
        <option value="Research">Research (PhD/M.Tech Res)</option>
      </select>
    </div>

    <div class="filter-group">
      <label class="filter-label">🏫 Institute/Faculty</label>
      <select id="schoolFilter" class="filter-select" onchange="renderCourses()">
        <option value="All">All Institutes</option>
        <option value="Engineering">Engineering & Tech</option>
        <option value="Management">Management & Commerce</option>
        <option value="Design">Design & Architecture</option>
        <option value="Health">Medical & Allied Health</option>
        <option value="Law">Law & Legal Studies</option>
        <option value="Science">Sciences & Pharma</option>
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
        <a href="https://pessat.com/" target="_blank" style="background:#FF6600; color:white; padding:12px 30px; border-radius:50px; text-decoration:none; font-weight:bold;">Register for PESSAT ↗</a>
      </div>

    </div>
  </div>
</div>

<script>
  // --- 1. COURSE DATABASE (PESU 2025) ---
  const courses = [
    // --- ENGINEERING (UG) ---
    { 
      id: 1, name: "B.Tech Computer Science & Engg (CSE)", level: "UG", school: "Engineering", 
      elig: "10+2 with Physics & Maths (Min 50%). PESSAT/KCET/JEE Score.",
      process: "PESSAT (60% seats) / KCET (40%).",
      fee: { "PESSAT Quota": "₹4,80,000", "KCET Quota": "₹1,07,000", "NRI/Higher": "Contact Office" },
      desc: "Flagship program at RR & EC Campus. Focus on AI, Systems, Cloud.",
      career: "Software Engineer, Data Scientist. Top Recruiters: Microsoft, Amazon, Cisco."
    },
    { 
      id: 2, name: "B.Tech AI & Machine Learning", level: "UG", school: "Engineering", 
      elig: "10+2 with Physics & Maths. PESSAT Rank.",
      process: "PESSAT / KCET.",
      fee: { "PESSAT Quota": "₹4,80,000", "KCET": "₹1,07,000" },
      desc: "Specialized CSE stream focusing on Neural Networks, Deep Learning, and Robotics.",
      career: "ML Engineer, AI Researcher, Data Analyst."
    },
    { 
      id: 3, name: "B.Tech Electronics & Comm (ECE)", level: "UG", school: "Engineering", 
      elig: "10+2 with Physics & Maths.",
      process: "PESSAT / KCET.",
      fee: { "PESSAT Quota": "₹4,20,000", "KCET": "₹1,07,000" },
      desc: "VLSI Design, Communication Networks, Signal Processing.",
      career: "Chip Design (Intel, Qualcomm), Embedded Systems Engineer."
    },
    { 
      id: 4, name: "B.Tech Mechanical Engineering", level: "UG", school: "Engineering", 
      elig: "10+2 with Physics & Maths.",
      process: "PESSAT / KCET.",
      fee: { "PESSAT Quota": "₹2,60,000", "KCET": "₹1,07,000" },
      desc: "Thermodynamics, Automotive, Robotics and Automation.",
      career: "Automotive Engineer (Tesla, Mercedes), Manufacturing, Robotics."
    },
    { 
      id: 5, name: "B.Tech Biotechnology", level: "UG", school: "Engineering", 
      elig: "10+2 with Physics, Chem, Bio/Maths.",
      process: "PESSAT / KCET.",
      fee: { "PESSAT Quota": "₹2,60,000", "KCET": "₹1,07,000" },
      desc: "Genetic Engineering, Bioinformatics, Computational Biology.",
      career: "Biotech R&D, Pharma, Clinical Research."
    },

    // --- MANAGEMENT & COMMERCE (UG) ---
    { 
      id: 6, name: "BBA (General / Honours)", level: "UG", school: "Management", 
      elig: "10+2 from any stream.",
      process: "PESSAT Interview.",
      fee: { "Regular": "₹2,40,000", "Honours": "₹2,40,000" },
      desc: "Foundational management course. Covers Marketing, HR, Finance.",
      career: "Business Analyst, HR Executive, Marketing Manager."
    },
    { 
      id: 7, name: "BBA (Business Analytics)", level: "UG", school: "Management", 
      elig: "10+2 with Math/Stats preferred.",
      process: "PESSAT Interview.",
      fee: { "Per Year": "₹2,60,000" },
      desc: "Data-driven management. Tools like Python, R, Tableau included.",
      career: "Data Analyst, Business Intelligence, Consultant."
    },
    { 
      id: 8, name: "BBA (Sports Management)", level: "UG", school: "Management", 
      elig: "10+2 any stream. Interest in Sports.",
      process: "PESSAT Interview.",
      fee: { "Per Year": "₹2,40,000" },
      desc: "Combines business principles with sports administration and marketing.",
      career: "Sports Manager, Team Admin, Event Coordinator."
    },
    { 
      id: 9, name: "B.Com (ACCA Accredited)", level: "UG", school: "Management", 
      elig: "10+2 Commerce/Science.",
      process: "PESSAT Interview.",
      fee: { "Per Year": "₹2,20,000" },
      desc: "Integrated with ACCA curriculum (UK). Exemption for certain papers.",
      career: "Certified Accountant, Auditor, Financial Consultant."
    },
    { 
      id: 10, name: "B.Com (Honours with CA)", level: "UG", school: "Management", 
      elig: "10+2 Commerce.",
      process: "PESSAT Interview.",
      fee: { "Per Year": "₹2,20,000" },
      desc: "Aligned with ICAI syllabus for CA aspirants.",
      career: "Chartered Accountant, Tax Consultant."
    },

    // --- DESIGN & ARCHITECTURE (UG) ---
    { 
      id: 11, name: "Bachelor of Design (B.Des)", level: "UG", school: "Design", 
      elig: "10+2 (Any stream) + PESSAT/UCEED score.",
      process: "PESSAT Design Test + Portfolio Review.",
      fee: { "Per Year": "₹3,80,000" },
      desc: "Product Design, Interaction Design, Visual Communication.",
      career: "UX/UI Designer, Product Designer, Creative Director."
    },
    { 
      id: 12, name: "Bachelor of Architecture (B.Arch)", level: "UG", school: "Design", 
      elig: "10+2 with Maths. NATA Score Mandatory.",
      process: "Based on NATA Score + 12th Marks.",
      fee: { "CET Quota": "Govt Fee", "Mgmt Quota": "Contact Office" },
      desc: "5-Year program. Urban planning, sustainable architecture.",
      career: "Architect, Urban Planner, Interior Designer."
    },

    // --- MEDICAL & ALLIED HEALTH (UG) ---
    { 
      id: 13, name: "MBBS (Bachelor of Medicine)", level: "UG", school: "Health", 
      elig: "10+2 PCB + NEET UG Qualified.",
      process: "KEA Counseling based on NEET Rank.",
      fee: { "Govt Quota": "₹1.4L", "Private": "₹11L", "NRI": "₹40L+" },
      desc: "Offered at PES Institute of Medical Sciences (Kuppam/Bangalore).",
      career: "Doctor, Surgeon, Medical Researcher."
    },
    { 
      id: 14, name: "B.Sc Medical Laboratory Tech", level: "UG", school: "Health", 
      elig: "10+2 Science (PCB).",
      process: "PESSAT / Marks Merit.",
      fee: { "Per Year": "₹1,20,000" },
      desc: "Diagnostic analysis, pathology lab management.",
      career: "Lab Technologist, Hospital Admin."
    },
    { 
      id: 15, name: "Bachelor of Pharmacy (B.Pharm)", level: "UG", school: "Science", 
      elig: "10+2 Science (PCB/M).",
      process: "PESSAT / KCET.",
      fee: { "Per Year": "₹1,60,000" },
      desc: "Drug formulation, pharmacology, clinical practice.",
      career: "Pharmacist, R&D Scientist, Drug Inspector."
    },

    // --- LAW (UG) ---
    { 
      id: 16, name: "BA LLB / BBA LLB (Honours)", level: "UG", school: "Law", 
      elig: "10+2 with 45%. CLAT/LSAT/PESSAT.",
      process: "PESSAT Law Test / CLAT Score.",
      fee: { "Per Year": "₹2,20,000" },
      desc: "5-Year Integrated. Moot courts, corporate law focus.",
      career: "Corporate Lawyer, Litigator, Legal Advisor."
    },

    // --- POSTGRADUATE (PG) ---
    { 
      id: 17, name: "Master of Business Admin (MBA)", level: "PG", school: "Management", 
      elig: "Degree with 50%. PESSAT/MAT/CAT/CMAT.",
      process: "GD + Personal Interview.",
      fee: { "Per Year": "₹6,00,000" },
      desc: "Dual specialization options. High ROI program.",
      career: "Manager, Consultant, Entrepreneur."
    },
    { 
      id: 18, name: "Master of Computer Applications (MCA)", level: "PG", school: "Engineering", 
      elig: "BCA/B.Sc with Maths. PESSAT/PGCET.",
      process: "PESSAT Rank.",
      fee: { "Per Year": "₹2,60,000" },
      desc: "Full stack development, cloud computing focus.",
      career: "Software Engineer, System Architect."
    },
    { 
      id: 19, name: "M.Tech (CSE / Data Science / VLSI)", level: "PG", school: "Engineering", 
      elig: "BE/B.Tech with 50%. PESSAT/GATE.",
      process: "PESSAT/GATE Score.",
      fee: { "Per Year": "₹2,60,000" },
      desc: "Advanced specialization. Scholarship for GATE qualified.",
      career: "R&D Engineer, Senior Developer, Specialist."
    },
    { 
      id: 20, name: "M.Sc Psychology", level: "PG", school: "Science", 
      elig: "BA/B.Sc Psychology.",
      process: "PESSAT Interview.",
      fee: { "Per Year": "₹1,60,000" },
      desc: "Clinical and Industrial psychology tracks.",
      career: "Psychologist, HR Specialist, Counselor."
    },

    // --- RESEARCH ---
    { 
      id: 21, name: "Ph.D (Doctoral Programs)", level: "Research", school: "Engineering", 
      elig: "Masters Degree. PESSAT Research Selection.",
      process: "Entrance Test + Interview.",
      fee: { "Per Year": "₹80,000" },
      desc: "Available in all Engineering, Science, and Management domains.",
      career: "Professor, Scientist, Chief Researcher."
    }
  ];

  // --- 2. RENDER ENGINE ---
  function renderCourses() {
    const searchText = document.getElementById('searchInput').value.toLowerCase();
    const schoolFilter = document.getElementById('schoolFilter').value;
    const levelFilter = document.getElementById('levelFilter').value;
    const grid = document.getElementById('courseGrid');
    
    grid.innerHTML = '';
    let count = 0;

    courses.forEach(course => {
      const matchSearch = course.name.toLowerCase().includes(searchText);
      const matchSchool = schoolFilter === 'All' || course.school === schoolFilter;
      const matchLevel = levelFilter === 'All' || course.level === levelFilter;

      if (matchSearch && matchSchool && matchLevel) {
        count++;
        // Color Class
        let colorClass = 'school-Engineering';
        if (course.school === 'Management') colorClass = 'school-Management';
        if (course.school === 'Design') colorClass = 'school-Design';
        if (course.school === 'Health') colorClass = 'school-Health';
        if (course.school === 'Law') colorClass = 'school-Law';

        const card = `
          <div class="course-card ${colorClass}" style="animation-delay: ${count * 0.05}s">
            <div>
              <span class="c-school">Institute of ${course.school}</span>
              <h3 class="c-title">${course.name}</h3>
              <div class="c-meta">
                <span class="c-badge">${course.level}</span>
              </div>
            </div>
            <div class="c-footer">
              <span style="font-size:0.8rem; color:#666;">View Eligibility & Fees</span>
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
