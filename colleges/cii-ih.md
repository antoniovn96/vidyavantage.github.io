---
layout: default
title: "CII Institute of Hospitality Course Portal 🏨"
permalink: /colleges/cii-ih/
image: "https://www.ciiih.com/images/about.jpg"
description: "Browse VET by EHL Swiss Professional Hospitality Diplomas at CII Institute of Hospitality. Check eligibility, structure, and career outcomes."
---

<meta property="og:title" content="CII Institute of Hospitality Course Portal 🏨">
<meta property="og:description" content="Access details for VET by EHL Swiss Professional Diplomas in Culinary, F&B, and Rooms. Check curriculum, eligibility, and selection process.">
<meta property="og:image" content="https://www.ciiih.com/images/about.jpg">

<style>
  /* 1. LAYOUT RESET */
  .main-content { max-width: 100% !important; padding: 0 !important; margin: 0 !important; }
  body { background-color: #f8f9fa; font-family: 'Segoe UI', system-ui, sans-serif; color: #333; }

  /* 2. HERO SECTION */
  .cii-hero {
    background: linear-gradient(rgba(0, 33, 71, 0.85), rgba(10, 35, 66, 0.9)), url('https://www.ciiih.com/images/about.jpg');
    background-size: cover;
    background-position: center;
    color: white;
    text-align: center;
    padding: 100px 20px;
    margin-bottom: 0;
  }
  
  .cii-hero h1 { font-size: 3rem; margin: 0; font-weight: 900; color: #fff !important; letter-spacing: -0.5px;}
  .cii-hero p { font-size: 1.15rem; color: #e2e8f0 !important; margin-top: 15px; max-width: 800px; margin-left: auto; margin-right: auto; line-height: 1.6;}

  /* 3. APP CONTAINER */
  .app-container {
    max-width: 1300px;
    margin: 0 auto;
    display: flex;
    gap: 30px;
    padding: 40px 20px;
    align-items: flex-start;
  }

  /* 4. SIDEBAR FILTERS */
  .filters-sidebar {
    width: 280px;
    background: white;
    padding: 25px;
    border-radius: 12px;
    box-shadow: 0 10px 30px rgba(0,0,0,0.05);
    position: sticky;
    top: 90px;
    border-top: 4px solid #00509E; /* CII Blue */
    flex-shrink: 0;
  }

  .filter-group { margin-bottom: 20px; }
  .filter-label { display: block; font-weight: 700; margin-bottom: 8px; color: #00509E; font-size: 0.9rem; text-transform: uppercase; letter-spacing: 0.5px;}
  
  .filter-input, .filter-select {
    width: 100%;
    padding: 12px 15px;
    border: 1px solid #cbd5e1;
    border-radius: 8px;
    font-size: 0.95rem;
    outline: none;
    transition: border 0.2s, box-shadow 0.2s;
    background: #f8fafc;
  }
  .filter-input:focus, .filter-select:focus { border-color: #00509E; box-shadow: 0 0 0 3px rgba(0, 80, 158, 0.1); background: white;}

  /* 5. COURSE GRID */
  .results-area { flex-grow: 1; }
  
  .course-grid {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(320px, 1fr));
    gap: 25px;
  }

  .course-card {
    background: white;
    border-radius: 12px;
    padding: 25px;
    border-left: 5px solid #ddd;
    box-shadow: 0 4px 15px rgba(0,0,0,0.03);
    transition: transform 0.2s, box-shadow 0.2s;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
  }
  .course-card:hover { transform: translateY(-5px); box-shadow: 0 12px 30px rgba(0,0,0,0.08); border-left-color: #D4AF37; }

  /* Level Colors */
  .level-VET_Diploma { border-left-color: #00509E; }

  .c-school { font-size: 0.8rem; text-transform: uppercase; font-weight: 800; color: #64748b; margin-bottom: 8px; letter-spacing: 0.5px;}
  .c-title { font-size: 1.25rem; font-weight: 800; color: #0f172a; margin: 0 0 15px 0; line-height: 1.4; }
  .c-meta { display: flex; gap: 8px; flex-wrap: wrap; margin-bottom: 20px; }
  .c-badge { display: inline-block; background: #EEF2FF; padding: 6px 12px; border-radius: 6px; font-size: 0.8rem; font-weight: 700; color: #4338CA; border: 1px solid #C7D2FE;}
  
  .c-footer { margin-top: auto; display: flex; justify-content: space-between; align-items: center; border-top: 1px solid #f1f5f9; padding-top: 20px; }
  
  .view-btn {
    background: #f8fafc; border: 1px solid #00509E; color: #00509E;
    padding: 8px 20px; border-radius: 50px; font-size: 0.9rem; font-weight: 700; cursor: pointer; transition: 0.3s;
  }
  .view-btn:hover { background: #00509E; color: white; box-shadow: 0 4px 10px rgba(0, 80, 158, 0.2);}

  /* 6. MODAL */
  .modal-overlay {
    display: none; position: fixed; top: 0; left: 0; width: 100%; height: 100%;
    background: rgba(15, 23, 42, 0.8); z-index: 2000; align-items: center; justify-content: center; backdrop-filter: blur(5px);
  }
  .modal-box {
    background: white; width: 95%; max-width: 750px; max-height: 90vh; overflow-y: auto;
    border-radius: 16px; position: relative; animation: slideUp 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275);
    box-shadow: 0 25px 50px rgba(0,0,0,0.25);
  }
  .modal-header {
    background: #00509E; padding: 25px 30px; color: white; display: flex; justify-content: space-between; align-items: center;
    position: sticky; top: 0; z-index: 10; border-bottom: 4px solid #D4AF37;
  }
  .modal-title { margin: 0; font-size: 1.4rem; font-weight: 800; }
  .close-modal { background: none; border: none; color: white; font-size: 2rem; cursor: pointer; transition: 0.2s;}
  .close-modal:hover { color: #fca5a5; transform: scale(1.1);}
  
  .modal-body { padding: 30px; }

  .info-block { margin-bottom: 30px; background: #f8fafc; padding: 20px; border-radius: 12px; border: 1px solid #e2e8f0;}
  .info-head { font-size: 1.05rem; font-weight: 800; color: #00509E; border-bottom: 2px solid #cbd5e1; padding-bottom: 8px; margin-bottom: 15px; display: flex; align-items: center; gap: 10px; text-transform: uppercase; letter-spacing: 0.5px;}
  .info-content { font-size: 1rem; color: #334155; line-height: 1.7; font-weight: 500;}
  
  .fee-table { width: 100%; border-collapse: collapse; margin-top: 10px; font-size: 0.95rem; background: white; border-radius: 8px; overflow: hidden;}
  .fee-table td { padding: 12px 15px; border-bottom: 1px solid #f1f5f9; }
  .fee-table td:first-child { font-weight: 700; color: #475569; }
  .fee-table td:last-child { text-align: right; font-weight: 800; color: #00509E; }

  @keyframes slideUp { from { transform: translateY(50px); opacity: 0; } to { transform: translateY(0); opacity: 1; } }

  /* Mobile */
  @media (max-width: 900px) {
    .app-container { flex-direction: column; }
    .filters-sidebar { width: 100%; position: static; }
  }
</style>

<div class="cii-hero">
  <h1>CII Institute of Hospitality</h1>
  <p>Deliver excellence with the prestigious VET by EHL Swiss Professional Hospitality Diploma. An advanced Swiss curriculum highly respected and sought after by the global industry.</p>
</div>

<div class="app-container">

  <aside class="filters-sidebar">
    <div class="filter-group">
      <label class="filter-label">🔍 Search Course</label>
      <input type="text" id="searchInput" class="filter-input" placeholder="e.g. Culinary, Food..." onkeyup="renderCourses()">
    </div>
    
    <div class="filter-group">
      <label class="filter-label">🎓 Programme Level</label>
      <select id="levelFilter" class="filter-select" onchange="renderCourses()">
        <option value="All">All Levels</option>
        <option value="VET_Diploma">VET by EHL Diploma</option>
      </select>
    </div>

    <div class="filter-group">
      <label class="filter-label">🏫 Specialization</label>
      <select id="deptFilter" class="filter-select" onchange="renderCourses()">
        <option value="All">All Specializations</option>
        <option value="Culinary">Culinary Arts</option>
        <option value="F&B">Food & Beverage Service</option>
        <option value="Rooms">Rooms Division</option>
      </select>
    </div>

    <div style="margin-top:20px; font-size:0.85rem; color:#64748b; font-weight: 600;">
      Showing <strong id="countDisplay" style="color: #0f172a;">0</strong> courses
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
      <button class="close-modal" onclick="closeModalBtn()" aria-label="Close">&times;</button>
    </div>
    <div class="modal-body">
      
      <div class="info-block" style="background: #FFFBEB; border-color: #FDE68A;">
        <div class="info-head" style="color: #B45309; border-color: #FCD34D;">🇨🇭 VET by EHL Framework</div>
        <div class="info-content">
          <p style="margin-top:0;">This course comprises three internationally recognized certificates leading to the final diploma:</p>
          <ul style="margin-bottom:0;">
            <li><strong>Foundation Certificate</strong> (Level 1)</li>
            <li><strong>Intermediate Certificate</strong> (Level 2)</li>
            <li><strong>Advanced Certificate</strong> (Level 3)</li>
          </ul>
        </div>
      </div>

      <div class="info-block">
        <div class="info-head">📋 Programme Overview</div>
        <div class="info-content" id="mOverview"></div>
      </div>

      <div class="info-block">
        <div class="info-head">✅ Eligibility & Admission</div>
        <div class="info-content">
          <p style="margin-top:0;"><strong>Criteria:</strong> <span id="mElig"></span></p>
          <p style="margin-bottom:0;"><strong>Selection:</strong> <span id="mSelect"></span></p>
        </div>
      </div>

      <div class="info-block">
        <div class="info-head">🚀 Career Outcomes</div>
        <div class="info-content" id="mCareers"></div>
      </div>
      
      <div style="text-align:center; margin-top:40px; margin-bottom: 10px;">
        <a href="https://www.ciiih.com/" target="_blank" style="background:#00509E; color:white; padding:15px 40px; border-radius:50px; text-decoration:none; font-weight:800; font-size: 1.1rem; display: inline-block; box-shadow: 0 10px 20px rgba(0, 80, 158, 0.2); transition: 0.3s;">Visit Official CII IH Website ➔</a>
      </div>

    </div>
  </div>
</div>

<script>
  // --- 1. COURSE DATABASE ---
  const courses = [
    { 
      id: 1, 
      name: "Culinary Professional Diploma Program", 
      level: "VET_Diploma", 
      dept: "Culinary",
      elig: "Successful completion of 10+2 system of Senior Secondary Examination or its equivalent.",
      process: "Direct Admission / Personal Interview by the Institute.",
      desc: "An advanced Swiss curriculum, highly respected and sought after by the Industry. The program focuses heavily on international culinary techniques, kitchen management, hygiene, menu planning, and food production standards.",
      career: "Commis Chef, Chef de Partie, Executive Chef, Culinary Entrepreneur, Food Stylist in top-tier international hotel chains and premium standalone restaurants."
    },
    { 
      id: 2, 
      name: "F&B Service Professional Diploma Program", 
      level: "VET_Diploma", 
      dept: "F&B",
      elig: "Successful completion of 10+2 system of Senior Secondary Examination or its equivalent.",
      process: "Direct Admission / Personal Interview by the Institute.",
      desc: "An advanced Swiss curriculum, highly respected and sought after by the Industry. This program trains students in the fine arts of food and beverage service, mixology, banquet operations, and guest experience management.",
      career: "F&B Supervisor, Sommelier, Banquet Manager, Restaurant Manager, Guest Relations Executive in luxury hospitality sectors."
    },
    { 
      id: 3, 
      name: "Rooms Professional Diploma Program", 
      level: "VET_Diploma", 
      dept: "Rooms",
      elig: "Successful completion of 10+2 system of Senior Secondary Examination or its equivalent.",
      process: "Direct Admission / Personal Interview by the Institute.",
      desc: "An advanced Swiss curriculum, highly respected and sought after by the Industry. This comprehensive program covers the core operations of a hotel including Front Office management, Housekeeping operations, revenue management, and hospitality administration.",
      career: "Front Office Manager, Executive Housekeeper, Rooms Division Manager, Reservation Manager, Hospitality Administrator."
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
        let colorClass = 'level-' + course.level; 

        const card = `
          <div class="course-card ${colorClass}" style="animation-delay: ${count * 0.05}s">
            <div>
              <span class="c-school">${course.dept} SPECIALIZATION</span>
              <h3 class="c-title">${course.name}</h3>
              <div class="c-meta">
                <span class="c-badge">🇨🇭 VET by EHL Swiss Curriculum</span>
              </div>
            </div>
            <div class="c-footer">
              <span style="font-size:0.85rem; color:#64748b; font-weight:600;">View Swiss Certificates</span>
              <button class="view-btn" onclick="openDetails(${course.id})">Details ➔</button>
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

    document.getElementById('courseModal').style.display = 'flex';
  }

  function closeModalBtn() { document.getElementById('courseModal').style.display = 'none'; }
  function closeModal(e) { if(e.target.className === 'modal-overlay') document.getElementById('courseModal').style.display = 'none'; }

  // Initial Render
  renderCourses();
</script>
