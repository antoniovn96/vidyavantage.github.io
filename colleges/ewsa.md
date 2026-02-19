---
layout: default
title: "East West School of Architecture (EWSA) Course Portal 🎓"
permalink: /colleges/ewsa/
image: "https://images.unsplash.com/photo-1503387762-592deb58ef4e?ixlib=rb-4.0.3&auto=format&fit=crop&w=1600&q=80"
description: "Explore the NATA-approved Bachelor of Architecture (B.Arch) program at East West School of Architecture, Bangalore."
---

<meta property="og:title" content="EWSA Bangalore Course Portal 🎓">
<meta property="og:description" content="Access details for the B.Arch program at East West School of Architecture. Check 2025/2026 Fees, NATA Eligibility, and Admission details.">
<meta property="og:image" content="https://images.unsplash.com/photo-1503387762-592deb58ef4e?ixlib=rb-4.0.3&auto=format&fit=crop&w=1600&q=80">

<style>
  /* 1. LAYOUT RESET */
  .main-content { max-width: 100% !important; padding: 0 !important; margin: 0 !important; }
  body { background-color: #f4f6f8; font-family: 'Segoe UI', system-ui, sans-serif; color: #333; }

  /* 2. HERO SECTION */
  .ewsa-hero {
    background: linear-gradient(rgba(44, 62, 80, 0.85), rgba(0, 0, 0, 0.7)), url('https://images.unsplash.com/photo-1503387762-592deb58ef4e?ixlib=rb-4.0.3&auto=format&fit=crop&w=1600&q=80');
    background-size: cover;
    background-position: center;
    color: white;
    text-align: center;
    padding: 80px 20px;
    margin-bottom: 0;
  }
  
  .ewsa-hero h1 { font-size: 2.8rem; margin: 0; font-weight: 800; color: white !important; }
  .ewsa-hero p { font-size: 1.1rem; color: #f0f0f0 !important; margin-top: 10px; max-width: 700px; margin-left: auto; margin-right: auto; }

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
    border-top: 4px solid #2c3e50; /* Slate Grey for Architecture */
    flex-shrink: 0;
  }

  .filter-group { margin-bottom: 20px; }
  .filter-label { display: block; font-weight: 700; margin-bottom: 8px; color: #2c3e50; font-size: 0.9rem; }
  
  .filter-input, .filter-select {
    width: 100%;
    padding: 10px 15px;
    border: 1px solid #ddd;
    border-radius: 8px;
    font-size: 0.95rem;
    outline: none;
    transition: border 0.2s;
  }
  .filter-input:focus, .filter-select:focus { border-color: #2c3e50; }

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
  .course-card:hover { transform: translateY(-3px); box-shadow: 0 8px 25px rgba(0,0,0,0.08); border-left-color: #2c3e50; }

  /* Department Colors */
  .dept-Arch { border-left-color: #2c3e50; } /* Slate Grey */

  .c-dept { font-size: 0.75rem; text-transform: uppercase; font-weight: 700; color: #888; margin-bottom: 5px; }
  .c-title { font-size: 1.1rem; font-weight: 700; color: #333; margin: 0 0 10px 0; line-height: 1.4; }
  .c-meta { display: flex; gap: 8px; flex-wrap: wrap; margin-bottom: 15px; }
  .c-badge { display: inline-block; background: #f0f2f5; padding: 4px 10px; border-radius: 4px; font-size: 0.75rem; font-weight: 600; color: #555; }
  
  .c-footer { margin-top: auto; display: flex; justify-content: space-between; align-items: center; border-top: 1px solid #f0f0f0; padding-top: 15px; }
  
  .view-btn {
    background: transparent; border: 1px solid #2c3e50; color: #2c3e50;
    padding: 6px 15px; border-radius: 50px; font-size: 0.85rem; font-weight: 600; cursor: pointer; transition: 0.2s;
  }
  .view-btn:hover { background: #2c3e50; color: white; }

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
    background: #2c3e50; padding: 20px 25px; color: white; display: flex; justify-content: space-between; align-items: center;
    position: sticky; top: 0; z-index: 10;
  }
  .modal-title { margin: 0; font-size: 1.2rem; font-weight: 700; }
  .close-modal { background: none; border: none; color: white; font-size: 2rem; cursor: pointer; }
  
  .modal-body { padding: 25px; }

  .info-block { margin-bottom: 25px; }
  .info-head { font-size: 0.95rem; font-weight: 700; color: #2c3e50; border-bottom: 2px solid #f0f0f0; padding-bottom: 5px; margin-bottom: 10px; display: flex; align-items: center; gap: 8px; }
  .info-content { font-size: 0.95rem; color: #444; line-height: 1.6; }
  
  .fee-table { width: 100%; border-collapse: collapse; margin-top: 10px; font-size: 0.9rem; background: #fdfdfd; }
  .fee-table td { padding: 10px; border-bottom: 1px solid #eee; }
  .fee-table td:first-child { font-weight: 600; color: #555; }
  .fee-table td:last-child { text-align: right; font-weight: bold; color: #2c3e50; }

  @keyframes slideUp { from { transform: translateY(50px); opacity: 0; } to { transform: translateY(0); opacity: 1; } }

  /* Mobile */
  @media (max-width: 900px) {
    .app-container { flex-direction: column; }
    .filters-sidebar { width: 100%; position: static; }
  }
</style>

<div class="ewsa-hero">
  <h1>East West School of Architecture (EWSA)</h1>
  <p>Approved by Council of Architecture (COA) | Affiliated to VTU | Govt. of Karnataka Recognized</p>
</div>

<div class="app-container">

  <aside class="filters-sidebar">
    <div class="filter-group">
      <label class="filter-label">🔍 Search Course</label>
      <input type="text" id="searchInput" class="filter-input" placeholder="e.g. Architecture..." onkeyup="renderCourses()">
    </div>
    
    <div class="filter-group">
      <label class="filter-label">🎓 Programme Level</label>
      <select id="levelFilter" class="filter-select" onchange="renderCourses()">
        <option value="All">All Levels</option>
        <option value="UG">Undergraduate (B.Arch)</option>
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
        <a href="https://ewsa.edu.in/" target="_blank" style="background:#2c3e50; color:white; padding:12px 30px; border-radius:50px; text-decoration:none; font-weight:bold;">Official Website ↗</a>
      </div>

    </div>
  </div>
</div>

<script>
  // --- 1. COURSE DATABASE (EWSA) ---
  const courses = [
    // --- UNDERGRADUATE (B.ARCH) ---
    { 
      id: 1, 
      name: "Bachelor of Architecture (B.Arch)", 
      dept: "Arch", 
      level: "UG", 
      fee: { 
        "CET Quota": "₹90,000 - ₹1,10,000 / year", 
        "COMEDK Quota": "₹2,50,000+ / year", 
        "Management Quota": "₹3.0 - 4.5 Lakhs / year" 
      }, 
      elig: "Passed 10+2 (PUC/CBSE/ISC) with Physics, Chemistry, and Mathematics (Min 50% aggregate) OR 10+3 Diploma with Mathematics. MUST qualify NATA or JEE Main (Paper 2).", 
      career: "Licensed Architect, Urban Designer, Interior Architect, Landscape Architect, Sustainable Design Consultant." 
    }
  ];

  // --- 2. RENDER ENGINE ---
  function renderCourses() {
    const searchText = document.getElementById('searchInput').value.toLowerCase();
    const levelFilter = document.getElementById('levelFilter').value;
    const grid = document.getElementById('courseGrid');
    
    grid.innerHTML = '';
    let count = 0;

    courses.forEach(course => {
      const matchSearch = course.name.toLowerCase().includes(searchText);
      const matchLevel = levelFilter === 'All' || course.level === levelFilter;

      if (matchSearch && matchLevel) {
        count++;
        let colorClass = 'dept-' + course.dept;

        const card = `
          <div class="course-card ${colorClass}" style="animation-delay: ${count * 0.05}s">
            <div>
              <span class="c-dept">Architecture (COA Approved)</span>
              <h3 class="c-title">${course.name}</h3>
              <div class="c-meta">
                <span class="c-badge">5 Years (10 Semesters)</span>
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

  // --- 3. DETAILS MODAL LOGIC ---
  function openDetails(id) {
    const course = courses.find(c => c.id === id);
    if (!course) return;

    document.getElementById('mTitle').innerText = course.name;
    document.getElementById('mElig').innerText = course.elig;
    
    document.getElementById('mProcess').innerText = "Admission is strictly based on valid NATA or JEE Main (Paper 2) scores. Seats are allocated through KCET/COMEDK counselling or direct Management Quota.";
    
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
