---
layout: default
title: "Christ (Deemed to be University) Course Portal"
permalink: /colleges/christ-university/
image: "https://christuniversity.in/images/sharingLogo.jpg"
description: "Browse 80+ courses at Christ University (Bangalore, Pune, Delhi). Check 2025 Fees, Entrance Exams, and Eligibility."
---

<meta property="og:title" content="Christ University Course Portal 🎓">
<meta property="og:description" content="Access details for 80+ courses: Eligibility, Fees (2025), Syllabus, and Career Outcomes.">
<meta property="og:image" content="https://christuniversity.in/images/sharingLogo.jpg">

<style>
  /* 1. LAYOUT RESET */
  .main-content { max-width: 100% !important; padding: 0 !important; margin: 0 !important; }
  body { background-color: #f4f6f8; font-family: 'Segoe UI', system-ui, sans-serif; color: #333; }

  /* 2. HERO SECTION */
  .christ-hero {
    background: linear-gradient(rgba(139, 0, 0, 0.9), rgba(20, 20, 20, 0.8)), url('https://christuniversity.in/images/inner-banner-comn.jpg');
    background-size: cover;
    background-position: center;
    color: white;
    text-align: center;
    padding: 80px 20px;
    margin-bottom: 0;
  }
  
  .christ-hero h1 { font-size: 2.8rem; margin: 0; font-weight: 800; color: white !important; }
  .christ-hero p { font-size: 1.1rem; color: #ddd !important; margin-top: 10px; max-width: 700px; margin-left: auto; margin-right: auto; }

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
    border-top: 4px solid #8b0000; /* Christ Red */
    flex-shrink: 0;
  }

  .filter-group { margin-bottom: 20px; }
  .filter-label { display: block; font-weight: 700; margin-bottom: 8px; color: #8b0000; font-size: 0.9rem; }
  
  .filter-input, .filter-select {
    width: 100%;
    padding: 10px 15px;
    border: 1px solid #ddd;
    border-radius: 8px;
    font-size: 0.95rem;
    outline: none;
    transition: border 0.2s;
  }
  .filter-input:focus, .filter-select:focus { border-color: #8b0000; }

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
  .course-card:hover { transform: translateY(-3px); box-shadow: 0 8px 25px rgba(0,0,0,0.08); border-left-color: #8b0000; }

  /* School Colors */
  .school-Business { border-left-color: #e91e63; }
  .school-Law { border-left-color: #795548; }
  .school-Engineering { border-left-color: #2196f3; }
  .school-Science { border-left-color: #4caf50; }
  .school-Humanities { border-left-color: #ff9800; }

  .c-school { font-size: 0.75rem; text-transform: uppercase; font-weight: 700; color: #888; margin-bottom: 5px; }
  .c-title { font-size: 1.1rem; font-weight: 700; color: #333; margin: 0 0 10px 0; line-height: 1.4; }
  .c-meta { display: flex; gap: 8px; flex-wrap: wrap; margin-bottom: 15px; }
  .c-badge { display: inline-block; background: #f0f2f5; padding: 4px 10px; border-radius: 4px; font-size: 0.75rem; font-weight: 600; color: #555; }
  
  .c-footer { margin-top: auto; display: flex; justify-content: space-between; align-items: center; border-top: 1px solid #f0f0f0; padding-top: 15px; }
  
  .view-btn {
    background: transparent; border: 1px solid #8b0000; color: #8b0000;
    padding: 6px 15px; border-radius: 50px; font-size: 0.85rem; font-weight: 600; cursor: pointer; transition: 0.2s;
  }
  .view-btn:hover { background: #8b0000; color: white; }

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
    background: #8b0000; padding: 20px 25px; color: white; display: flex; justify-content: space-between; align-items: center;
    position: sticky; top: 0; z-index: 10;
  }
  .modal-title { margin: 0; font-size: 1.2rem; font-weight: 700; }
  .close-modal { background: none; border: none; color: white; font-size: 2rem; cursor: pointer; }
  
  .modal-body { padding: 25px; }

  .info-block { margin-bottom: 25px; }
  .info-head { font-size: 0.95rem; font-weight: 700; color: #8b0000; border-bottom: 2px solid #f0f0f0; padding-bottom: 5px; margin-bottom: 10px; display: flex; align-items: center; gap: 8px; }
  .info-content { font-size: 0.95rem; color: #444; line-height: 1.6; }
  
  .fee-table { width: 100%; border-collapse: collapse; margin-top: 10px; font-size: 0.9rem; background: #fdfdfd; }
  .fee-table td { padding: 10px; border-bottom: 1px solid #eee; }
  .fee-table td:first-child { font-weight: 600; color: #555; }
  .fee-table td:last-child { text-align: right; font-weight: bold; color: #8b0000; }

  @keyframes slideUp { from { transform: translateY(50px); opacity: 0; } to { transform: translateY(0); opacity: 1; } }

  /* Mobile */
  @media (max-width: 900px) {
    .app-container { flex-direction: column; }
    .filters-sidebar { width: 100%; position: static; }
  }
</style>

<div class="christ-hero">
  <h1>Christ (Deemed to be University)</h1>
  <p>Excellence and Service. Ranked among India's top private universities.</p>
</div>

<div class="app-container">

  <aside class="filters-sidebar">
    <div class="filter-group">
      <label class="filter-label">🔍 Search Course</label>
      <input type="text" id="searchInput" class="filter-input" placeholder="e.g. BBA, Law, Psychology..." onkeyup="renderCourses()">
    </div>
    
    <div class="filter-group">
      <label class="filter-label">🎓 Programme Level</label>
      <select id="levelFilter" class="filter-select" onchange="renderCourses()">
        <option value="All">All Levels</option>
        <option value="UG">Undergraduate (UG)</option>
        <option value="PG">Postgraduate (PG)</option>
        <option value="PhD">Doctoral (PhD)</option>
        <option value="Online">Online Degree</option>
      </select>
    </div>

    <div class="filter-group">
      <label class="filter-label">🏫 Filter by School</label>
      <select id="schoolFilter" class="filter-select" onchange="renderCourses()">
        <option value="All">All Schools</option>
        <option value="Business">Commerce & Management</option>
        <option value="Law">School of Law</option>
        <option value="Engineering">Engineering & Tech</option>
        <option value="Science">Sciences</option>
        <option value="Humanities">Humanities & Social Sci</option>
        <option value="Media">Media & Communication</option>
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
        <div class="info-head">💰 Fee Structure (Approx/Year)</div>
        <table class="fee-table" id="mFees"></table>
      </div>

      <div class="info-block">
        <div class="info-head">🚀 Career Outcomes</div>
        <div class="info-content" id="mCareers"></div>
      </div>
      
      <div style="text-align:center; margin-top:30px;">
        <a href="https://christuniversity.in/apply-online" target="_blank" style="background:#8b0000; color:white; padding:12px 30px; border-radius:50px; text-decoration:none; font-weight:bold;">Apply Now ↗</a>
      </div>

    </div>
  </div>
</div>

<script>
  // --- 1. ROBUST COURSE DATABASE ---
  const courses = [
    // --- BUSINESS & COMMERCE (UG) ---
    { id: 1, name: "Bachelor of Business Administration (BBA)", school: "Business", level: "UG", campus: "Central/Kengeri/BRC", fee: { "Karnataka": "₹2,61,000", "Other States": "₹2,81,000" } },
    { id: 2, name: "BBA (Honours / Research)", school: "Business", level: "UG", campus: "Central", fee: { "Karnataka": "₹2,55,000", "Other States": "₹2,75,000" } },
    { id: 3, name: "BBA (Finance and International Business)", school: "Business", level: "UG", campus: "Bannerghatta", fee: { "Karnataka": "₹2,46,000", "Other States": "₹2,66,000" } },
    { id: 4, name: "BBA (Strategy and Business Analytics)", school: "Business", level: "UG", campus: "Bannerghatta", fee: { "Karnataka": "₹2,39,000", "Other States": "₹2,59,000" } },
    { id: 5, name: "BBA (FinTech Honours)", school: "Business", level: "UG", campus: "Delhi NCR", fee: { "All India": "₹2,95,000" } },
    { id: 6, name: "BBA (Decision Science)", school: "Business", level: "UG", campus: "Central", fee: { "Karnataka": "₹2,70,000", "Other States": "₹2,90,000" } },
    { id: 7, name: "B.Com (Regular)", school: "Business", level: "UG", campus: "Central", fee: { "Karnataka": "₹80,000", "Other States": "₹1,00,000" } },
    { id: 8, name: "B.Com (International Finance)", school: "Business", level: "UG", campus: "Central", fee: { "Karnataka": "₹1,90,000", "Other States": "₹2,10,000" } },
    { id: 9, name: "B.Com (Honours)", school: "Business", level: "UG", campus: "Central", fee: { "Karnataka": "₹1,11,000", "Other States": "₹1,31,000" } },
    { id: 10, name: "B.Com (Strategic Finance Honours)", school: "Business", level: "UG", campus: "Central", fee: { "Karnataka": "₹1,95,000", "Other States": "₹2,15,000" } },
    { id: 11, name: "Bachelor of Hotel Management (BHM)", school: "Business", level: "UG", campus: "Central", fee: { "Karnataka": "₹1,60,000", "Other States": "₹1,80,000" } },

    // --- LAW (UG) ---
    { id: 12, name: "BA LLB (Honours)", school: "Law", level: "UG", campus: "Central/Pune/Delhi", fee: { "Karnataka": "₹2,62,000", "Other States": "₹2,82,000" } },
    { id: 13, name: "BBA LLB (Honours)", school: "Law", level: "UG", campus: "Central/Pune/Delhi", fee: { "Karnataka": "₹2,89,000", "Other States": "₹3,09,000" } },

    // --- ENGINEERING (UG) ---
    { id: 14, name: "B.Tech Computer Science & Engg", school: "Engineering", level: "UG", campus: "Kengeri", fee: { "Karnataka": "₹2,40,000", "Other States": "₹2,60,000" } },
    { id: 15, name: "B.Tech AI & Machine Learning", school: "Engineering", level: "UG", campus: "Kengeri", fee: { "Karnataka": "₹2,65,000", "Other States": "₹2,85,000" } },
    { id: 16, name: "B.Tech Data Science", school: "Engineering", level: "UG", campus: "Kengeri", fee: { "Karnataka": "₹2,50,000", "Other States": "₹2,70,000" } },
    { id: 17, name: "B.Tech Electronics & Comm", school: "Engineering", level: "UG", campus: "Kengeri", fee: { "Karnataka": "₹1,90,000", "Other States": "₹2,10,000" } },
    { id: 18, name: "B.Tech Robotics & Mechatronics", school: "Engineering", level: "UG", campus: "Kengeri", fee: { "Karnataka": "₹1,90,000", "Other States": "₹2,10,000" } },
    { id: 19, name: "B.Tech Automobile Engg", school: "Engineering", level: "UG", campus: "Kengeri", fee: { "Karnataka": "₹1,80,000", "Other States": "₹2,00,000" } },
    { id: 20, name: "B.Tech Civil Engineering", school: "Engineering", level: "UG", campus: "Kengeri", fee: { "Karnataka": "₹1,60,000", "Other States": "₹1,80,000" } },
    { id: 21, name: "Bachelor of Architecture (B.Arch)", school: "Engineering", level: "UG", campus: "Kengeri", fee: { "Karnataka": "₹3,20,000", "Other States": "₹3,40,000" } },

    // --- SCIENCES & IT (UG) ---
    { id: 22, name: "Bachelor of Computer Applications (BCA)", school: "Science", level: "UG", campus: "Central", fee: { "Karnataka": "₹1,87,000", "Other States": "₹2,07,000" } },
    { id: 23, name: "B.Sc Data Science & Maths", school: "Science", level: "UG", campus: "Central", fee: { "Karnataka": "₹1,60,000", "Other States": "₹1,80,000" } },
    { id: 24, name: "B.Sc Economics, Maths, Statistics", school: "Science", level: "UG", campus: "Central", fee: { "Karnataka": "₹1,10,000", "Other States": "₹1,30,000" } },
    { id: 25, name: "B.Sc Psychology (Honours)", school: "Science", level: "UG", campus: "Kengeri/BGR", fee: { "Karnataka": "₹1,50,000", "Other States": "₹1,70,000" } },
    { id: 26, name: "B.Sc Biotechnology, Chemistry", school: "Science", level: "UG", campus: "Central", fee: { "Karnataka": "₹95,000", "Other States": "₹1,15,000" } },

    // --- HUMANITIES & MEDIA (UG) ---
    { id: 27, name: "BA Psychology & Economics", school: "Humanities", level: "UG", campus: "Central", fee: { "Karnataka": "₹1,36,000", "Other States": "₹1,56,000" } },
    { id: 28, name: "BA Journalism & Digital Media", school: "Media", level: "UG", campus: "Central", fee: { "Karnataka": "₹1,60,000", "Other States": "₹1,80,000" } },
    { id: 29, name: "BA Media & Public Affairs", school: "Media", level: "UG", campus: "Central", fee: { "Karnataka": "₹1,86,000", "Other States": "₹2,06,000" } },
    { id: 30, name: "BA Performing Arts / Theatre", school: "Humanities", level: "UG", campus: "Central", fee: { "Karnataka": "₹1,10,000", "Other States": "₹1,30,000" } },
    { id: 31, name: "BA Liberal Arts", school: "Humanities", level: "UG", campus: "BGR Campus", fee: { "Karnataka": "₹1,60,000", "Other States": "₹1,80,000" } },

    // --- PG PROGRAMMES ---
    { id: 32, name: "Master of Business Administration (MBA)", school: "Business", level: "PG", campus: "Central/Kengeri", fee: { "Total (2 Years)": "₹10,60,000" } },
    { id: 33, name: "M.Sc Clinical Psychology", school: "Science", level: "PG", campus: "Central", fee: { "Total (2 Years)": "₹4,20,000" } },
    { id: 34, name: "M.Sc Data Science", school: "Science", level: "PG", campus: "Central/Pune", fee: { "Total (2 Years)": "₹3,80,000" } },
    { id: 35, name: "Master of Computer Applications (MCA)", school: "IT", level: "PG", campus: "Central", fee: { "Total (2 Years)": "₹4,70,000" } },
    { id: 36, name: "LLM (Corporate & Commercial Law)", school: "Law", level: "PG", campus: "Central", fee: { "Total (1 Year)": "₹1,95,000" } },
    { id: 37, name: "M.A. English & Cultural Studies", school: "Humanities", level: "PG", campus: "Central", fee: { "Total (2 Years)": "₹1,80,000" } },
    { id: 38, name: "M.A. Applied Economics", school: "Humanities", level: "PG", campus: "Central", fee: { "Total (2 Years)": "₹2,20,000" } },
    { id: 39, name: "Master of Social Work (MSW)", school: "Humanities", level: "PG", campus: "Central", fee: { "Total (2 Years)": "₹1,90,000" } },

    // --- PHD ---
    { id: 40, name: "PhD in Management", school: "Business", level: "PhD", campus: "Central", fee: { "Per Year": "₹60,000" } },
    { id: 41, name: "PhD in Psychology", school: "Science", level: "PhD", campus: "Central", fee: { "Per Year": "₹60,000" } },
    { id: 42, name: "PhD in Computer Science", school: "IT", level: "PhD", campus: "Central", fee: { "Per Year": "₹60,000" } },
    { id: 43, name: "PhD in Law", school: "Law", level: "PhD", campus: "Central", fee: { "Per Year": "₹60,000" } },
    { id: 44, name: "PhD in Economics", school: "Humanities", level: "PhD", campus: "Central", fee: { "Per Year": "₹60,000" } },

    // --- ONLINE ---
    { id: 45, name: "Online MBA", school: "Business", level: "Online", campus: "Online", fee: { "Total": "₹1,90,000" } },
    { id: 46, name: "Online M.Sc Data Science", school: "Science", level: "Online", campus: "Online", fee: { "Total": "₹2,50,000" } },
    { id: 47, name: "Online B.Com", school: "Business", level: "Online", campus: "Online", fee: { "Total": "₹1,60,000" } },
    { id: 48, name: "Online MA English", school: "Humanities", level: "Online", campus: "Online", fee: { "Total": "₹1,00,000" } }
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
      const matchSchool = schoolFilter === 'All' || getSchoolMapping(course.school) === schoolFilter;
      const matchLevel = levelFilter === 'All' || course.level === levelFilter;

      if (matchSearch && matchSchool && matchLevel) {
        count++;
        // School Color Class
        let colorClass = 'school-Business';
        if (course.school === 'Law') colorClass = 'school-Law';
        if (course.school === 'Engineering') colorClass = 'school-Engineering';
        if (course.school === 'Science') colorClass = 'school-Science';
        if (course.school === 'Humanities') colorClass = 'school-Humanities';

        const card = `
          <div class="course-card ${colorClass}" style="animation-delay: ${count * 0.05}s">
            <div>
              <span class="c-school">${course.school}</span>
              <h3 class="c-title">${course.name}</h3>
              <div class="c-meta">
                <span class="c-badge">${course.level}</span>
                <span class="c-badge">📍 ${course.campus}</span>
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

  // --- 3. HELPER TO MAP SCHOOLS ---
  function getSchoolMapping(school) {
    if (school === "Business") return "Business";
    if (school === "Law") return "Law";
    if (school === "Engineering") return "Engineering";
    if (school === "Science" || school === "IT") return "Science";
    if (school === "Humanities" || school === "Social") return "Humanities";
    if (school === "Media" || school === "Communication") return "Media";
    return "All";
  }

  // --- 4. DETAILS MODAL LOGIC ---
  function openDetails(id) {
    const course = courses.find(c => c.id === id);
    if (!course) return;

    document.getElementById('mTitle').innerText = course.name;
    
    // Auto-Generate Eligibility based on Level/Stream
    let elig = "Class 12 (10+2) with 50% aggregate.";
    if (course.level === "PG") elig = "Bachelor's Degree with 50% marks.";
    if (course.name.includes("B.Tech")) elig = "Class 12 with Physics, Chem, Maths (Min 50%).";
    if (course.name.includes("Law")) elig = "Class 12 with 45% (CLAT/LSAT score accepted).";
    if (course.name.includes("BBA")) elig = "Class 12 (Any stream) with min 55%.";
    if (course.name.includes("BCA") || course.name.includes("Data")) elig = "Class 12 with Maths/Comp Sci/Stats.";
    document.getElementById('mEligibility').innerText = elig;

    // Auto-Generate Selection Process
    let process = "Entrance Test + Micro Presentation + Personal Interview";
    if (course.name.includes("B.Tech")) process = "COMEDK / KCET / Christ Entrance Test";
    if (course.name.includes("MBA")) process = "CAT/MAT/GMAT/XAT score + GD + PI";
    if (course.level === "PhD") process = "Research Proposal + Entrance Test + Interview";
    document.getElementById('mProcess').innerHTML = `<strong>Selection:</strong> ${process}`;

    // Auto-Generate Careers
    let careers = "Corporate, Research, Higher Studies.";
    if (course.name.includes("BBA")) careers = "Management Trainee, HR Executive, Marketing Analyst.";
    if (course.name.includes("Law")) careers = "Corporate Lawyer, Litigator, Legal Advisor, Judiciary.";
    if (course.name.includes("Psychology")) careers = "Counselor, HR Specialist, Clinical Psychologist (after MSc).";
    if (course.name.includes("Tech") || course.name.includes("BCA")) careers = "Software Engineer, Data Analyst, Web Developer.";
    document.getElementById('mCareers').innerText = careers;

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
