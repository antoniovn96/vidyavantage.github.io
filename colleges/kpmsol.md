---
layout: default
title: "Kirit P. Mehta School of Law (NMIMS) Course Portal 🎓"
permalink: /colleges/kpmsol/
image: "https://law.nmims.edu/images/banner/law-banner.jpg"
description: "Browse Law programs (BA LLB, BBA LLB, LLM, PhD) at NMIMS Kirit P. Mehta School of Law. Check 2025 Fees, NLAT/CLAT Cutoffs, and Placements."
---

<meta property="og:title" content="NMIMS Kirit P. Mehta School of Law Course Portal 🎓">
<meta property="og:description" content="Access details for BA LLB, BBA LLB, LLM, and PhD. Check Eligibility, Fees, and Career Outcomes.">
<meta property="og:image" content="https://law.nmims.edu/images/banner/law-banner.jpg">

<style>
  /* 1. LAYOUT RESET */
  .main-content { max-width: 100% !important; padding: 0 !important; margin: 0 !important; }
  body { background-color: #f4f6f8; font-family: 'Segoe UI', system-ui, sans-serif; color: #333; }

  /* 2. HERO SECTION */
  .law-hero {
    background: linear-gradient(rgba(44, 62, 80, 0.9), rgba(44, 62, 80, 0.7)), url('https://law.nmims.edu/images/banner/law-banner.jpg');
    background-size: cover;
    background-position: center;
    color: white;
    text-align: center;
    padding: 80px 20px;
    margin-bottom: 0;
  }
  
  .law-hero h1 { font-size: 2.8rem; margin: 0; font-weight: 800; color: #fff !important; }
  .law-hero p { font-size: 1.1rem; color: #ddd !important; margin-top: 10px; max-width: 700px; margin-left: auto; margin-right: auto; }

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
    border-top: 4px solid #c0392b; /* Law Red */
    flex-shrink: 0;
  }

  .filter-group { margin-bottom: 20px; }
  .filter-label { display: block; font-weight: 700; margin-bottom: 8px; color: #c0392b; font-size: 0.9rem; }
  
  .filter-input, .filter-select {
    width: 100%;
    padding: 10px 15px;
    border: 1px solid #ddd;
    border-radius: 8px;
    font-size: 0.95rem;
    outline: none;
    transition: border 0.2s;
  }
  .filter-input:focus, .filter-select:focus { border-color: #c0392b; }

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
  .course-card:hover { transform: translateY(-3px); box-shadow: 0 8px 25px rgba(0,0,0,0.08); border-left-color: #c0392b; }

  /* Level Colors */
  .level-UG { border-left-color: #2980b9; }
  .level-PG { border-left-color: #8e44ad; }
  .level-PhD { border-left-color: #d35400; }

  .c-school { font-size: 0.75rem; text-transform: uppercase; font-weight: 700; color: #888; margin-bottom: 5px; }
  .c-title { font-size: 1.1rem; font-weight: 700; color: #333; margin: 0 0 10px 0; line-height: 1.4; }
  .c-meta { display: flex; gap: 8px; flex-wrap: wrap; margin-bottom: 15px; }
  .c-badge { display: inline-block; background: #f0f2f5; padding: 4px 10px; border-radius: 4px; font-size: 0.75rem; font-weight: 600; color: #555; }
  
  .c-footer { margin-top: auto; display: flex; justify-content: space-between; align-items: center; border-top: 1px solid #f0f0f0; padding-top: 15px; }
  
  .view-btn {
    background: transparent; border: 1px solid #c0392b; color: #c0392b;
    padding: 6px 15px; border-radius: 50px; font-size: 0.85rem; font-weight: 600; cursor: pointer; transition: 0.2s;
  }
  .view-btn:hover { background: #c0392b; color: white; }

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
    background: #c0392b; padding: 20px 25px; color: white; display: flex; justify-content: space-between; align-items: center;
    position: sticky; top: 0; z-index: 10;
  }
  .modal-title { margin: 0; font-size: 1.2rem; font-weight: 700; }
  .close-modal { background: none; border: none; color: white; font-size: 2rem; cursor: pointer; }
  
  .modal-body { padding: 25px; }

  .info-block { margin-bottom: 25px; }
  .info-head { font-size: 0.95rem; font-weight: 700; color: #c0392b; border-bottom: 2px solid #f0f0f0; padding-bottom: 5px; margin-bottom: 10px; display: flex; align-items: center; gap: 8px; }
  .info-content { font-size: 0.95rem; color: #444; line-height: 1.6; }
  
  .fee-table { width: 100%; border-collapse: collapse; margin-top: 10px; font-size: 0.9rem; background: #fdfdfd; }
  .fee-table td { padding: 10px; border-bottom: 1px solid #eee; }
  .fee-table td:first-child { font-weight: 600; color: #555; }
  .fee-table td:last-child { text-align: right; font-weight: bold; color: #c0392b; }

  @keyframes slideUp { from { transform: translateY(50px); opacity: 0; } to { transform: translateY(0); opacity: 1; } }

  /* Mobile */
  @media (max-width: 900px) {
    .app-container { flex-direction: column; }
    .filters-sidebar { width: 100%; position: static; }
  }
</style>

<div class="law-hero">
  <h1>Kirit P. Mehta School of Law</h1>
  <p>Premier Law School of NMIMS (Deemed-to-be University). Approved by Bar Council of India.</p>
</div>

<div class="app-container">

  <aside class="filters-sidebar">
    <div class="filter-group">
      <label class="filter-label">🔍 Search Course</label>
      <input type="text" id="searchInput" class="filter-input" placeholder="e.g. BA LLB, LLM..." onkeyup="renderCourses()">
    </div>
    
    <div class="filter-group">
      <label class="filter-label">🎓 Programme Level</label>
      <select id="levelFilter" class="filter-select" onchange="renderCourses()">
        <option value="All">All Levels</option>
        <option value="UG">Undergraduate (Integrated LLB)</option>
        <option value="PG">Postgraduate (LLM)</option>
        <option value="PhD">Doctoral (PhD)</option>
      </select>
    </div>

    <div class="filter-group">
      <label class="filter-label">⚖️ Specialization</label>
      <select id="specFilter" class="filter-select" onchange="renderCourses()">
        <option value="All">All Areas</option>
        <option value="Corporate">Corporate Law</option>
        <option value="IPR">Intellectual Property</option>
        <option value="Constitutional">Constitutional Law</option>
        <option value="Criminal">Criminal Law</option>
        <option value="General">General/Integrated</option>
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
        <div class="info-head">💰 Fee Structure (Annual)</div>
        <table class="fee-table" id="mFees"></table>
      </div>

      <div class="info-block">
        <div class="info-head">🚀 Career Outcomes</div>
        <div class="info-content" id="mCareers"></div>
      </div>
      
      <div style="text-align:center; margin-top:30px;">
        <a href="https://law.nmims.edu/" target="_blank" style="background:#c0392b; color:white; padding:12px 30px; border-radius:50px; text-decoration:none; font-weight:bold;">Visit Official Site ↗</a>
      </div>

    </div>
  </div>
</div>

<script>
  // --- 1. COURSE DATABASE (KPMSOL) ---
  const courses = [
    // --- UG COURSES (5-Year Integrated) ---
    { 
      id: 1, name: "B.A., LL.B. (Hons.)", level: "UG", spec: "General",
      elig: "10+2 with min 50% aggregate. Valid CLAT / NMIMS-LAT score.",
      process: "Merit list based on CLAT / NMIMS-LAT Score.",
      fee: { "Tuition (Mumbai)": "₹3,25,000", "Tuition (Navi Mumbai)": "₹2,00,000", "Tuition (Bengaluru)": "₹1,75,000" },
      desc: "5-Year Integrated Program. Combines Humanities (Pol Sci, Sociology, History) with Law. Focus on Critical Thinking and Moot Courts.",
      career: "Litigation, Judiciary Services, Corporate Lawyer, Legal Advisor, NGO/Human Rights Advocacy."
    },
    { 
      id: 2, name: "B.B.A., LL.B. (Hons.)", level: "UG", spec: "Corporate",
      elig: "10+2 with min 50% aggregate. Valid CLAT / NMIMS-LAT score.",
      process: "Merit list based on CLAT / NMIMS-LAT Score.",
      fee: { "Tuition (Mumbai)": "₹3,25,000", "Tuition (Navi Mumbai)": "₹2,00,000", "Tuition (Bengaluru)": "₹1,75,000" },
      desc: "5-Year Integrated Program. Combines Management (Marketing, Finance, HR) with Law. Ideal for Corporate Law careers.",
      career: "Corporate Counsel, Merger & Acquisition Specialist, Legal Consultant for MNCs, Banking Law."
    },

    // --- PG COURSES (LLM - 1 Year) ---
    { 
      id: 3, name: "LL.M. in Corporate Law", level: "PG", spec: "Corporate",
      elig: "LL.B. Degree with min 50%.",
      process: "Common Law Admission Test for PG (CLAT PG) / NMIMS Entrance Test + Interview.",
      fee: { "Tuition": "₹2,00,000" },
      desc: "Specialization in Company Law, Mergers, Securities, and Competition Law.",
      career: "Corporate Legal Head, Transactional Lawyer, Legal Compliance Officer."
    },
    { 
      id: 4, name: "LL.M. in Intellectual Property Rights", level: "PG", spec: "IPR",
      elig: "LL.B. Degree with min 50%.",
      process: "CLAT PG / NMIMS Entrance Test + Interview.",
      fee: { "Tuition": "₹2,00,000" },
      desc: "Focus on Patents, Trademarks, Copyrights, and Trade Secrets.",
      career: "IP Attorney, Patent Analyst, Legal Consultant for Tech/Pharma Firms."
    },
    { 
      id: 5, name: "LL.M. in Constitutional Law", level: "PG", spec: "Constitutional",
      elig: "LL.B. Degree with min 50%.",
      process: "CLAT PG / NMIMS Entrance Test + Interview.",
      fee: { "Tuition": "₹2,00,000" },
      desc: "Advanced study of Indian Constitution, Administrative Law, and Judicial Process.",
      career: "Academician, Researcher, Constitutional Lawyer, Government Advisor."
    },
    { 
      id: 6, name: "LL.M. in Financial Regulations", level: "PG", spec: "Corporate",
      elig: "LL.B. Degree with min 50%.",
      process: "CLAT PG / NMIMS Entrance Test + Interview.",
      fee: { "Tuition": "₹2,00,000" },
      desc: "Study of Banking Laws, Capital Markets, Insurance, and Forex Laws.",
      career: "Legal Officer in Banks, Regulatory Bodies (SEBI/RBI), Financial Law Consultant."
    },
    { 
      id: 7, name: "LL.M. in Criminal Laws", level: "PG", spec: "Criminal",
      elig: "LL.B. Degree with min 50%.",
      process: "CLAT PG / NMIMS Entrance Test + Interview.",
      fee: { "Tuition": "₹2,00,000" },
      desc: "Focus on Criminology, Penology, Forensic Science, and Criminal Justice Administration.",
      career: "Criminal Lawyer, Public Prosecutor, Policy Researcher."
    },

    // --- DOCTORAL (PhD) ---
    { 
      id: 8, name: "Ph.D. in Law", level: "PhD", spec: "General",
      elig: "Master's Degree in Law (LLM) with min 55%.",
      process: "NMIMS Written Test + Research Proposal Presentation + Personal Interview.",
      fee: { "Tuition": "₹2,50,000" },
      desc: "Rigorous research program. Scholars expected to contribute original knowledge to the field of law.",
      career: "Professor, Senior Researcher, Legal Think-Tank Analyst, Author."
    }
  ];

  // --- 2. RENDER ENGINE ---
  function renderCourses() {
    const searchText = document.getElementById('searchInput').value.toLowerCase();
    const levelFilter = document.getElementById('levelFilter').value;
    const specFilter = document.getElementById('specFilter').value;
    const grid = document.getElementById('courseGrid');
    
    grid.innerHTML = '';
    let count = 0;

    courses.forEach(course => {
      const matchSearch = course.name.toLowerCase().includes(searchText);
      const matchLevel = levelFilter === 'All' || course.level === levelFilter;
      const matchSpec = specFilter === 'All' || course.spec === specFilter;

      if (matchSearch && matchLevel && matchSpec) {
        count++;
        // Level Color Class
        let colorClass = 'level-' + course.level;

        const card = `
          <div class="course-card ${colorClass}" style="animation-delay: ${count * 0.05}s">
            <div>
              <span class="c-school">School of Law</span>
              <h3 class="c-title">${course.name}</h3>
              <div class="c-meta">
                <span class="c-badge">${course.level}</span>
                <span class="c-badge">${course.spec === 'General' ? 'Integrated' : course.spec}</span>
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
