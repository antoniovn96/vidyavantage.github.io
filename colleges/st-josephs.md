---
layout: default
title: "St. Joseph's University Course Portal"
permalink: /colleges/st-josephs/
image: "https://images.unsplash.com/photo-1562774053-701939374585?w=1200&h=630&fit=crop"
description: "Browse 100+ Undergraduate, PG & Diploma courses at St. Joseph's University. Check eligibility, fees, syllabus, and admission details."
---

<meta property="og:title" content="St. Joseph's University Course Portal 🎓">
<meta property="og:description" content="Access details for 100+ courses: Eligibility, Fees, Syllabus, and Career Outcomes.">
<meta property="og:image" content="https://images.unsplash.com/photo-1562774053-701939374585?w=1200&h=630&fit=crop">

<style>
  /* 1. LAYOUT RESET */
  .main-content { max-width: 100% !important; padding: 0 !important; margin: 0 !important; }
  body { background-color: #f0f2f5; font-family: 'Segoe UI', system-ui, sans-serif; color: #333; }

  /* 2. HERO SECTION */
  .sju-hero {
    background: linear-gradient(rgba(10, 35, 66, 0.9), rgba(10, 35, 66, 0.8)), url('https://images.unsplash.com/photo-1541339907198-e08756dedf3f?w=1600&auto=format&fit=crop');
    background-size: cover;
    background-position: center;
    color: white;
    text-align: center;
    padding: 60px 20px;
    margin-bottom: 0;
  }
  .sju-hero h1 { font-size: 2.8rem; margin: 0; font-weight: 800; color: white !important; }
  .sju-hero p { font-size: 1.1rem; color: #ddd !important; margin-top: 10px; max-width: 700px; margin-left: auto; margin-right: auto; }

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
    border-top: 4px solid #0A2342;
    flex-shrink: 0;
  }

  .filter-group { margin-bottom: 20px; }
  .filter-label { display: block; font-weight: 700; margin-bottom: 8px; color: #0A2342; font-size: 0.9rem; }
  
  .filter-input, .filter-select {
    width: 100%;
    padding: 10px 15px;
    border: 1px solid #ddd;
    border-radius: 8px;
    font-size: 0.95rem;
    outline: none;
    transition: border 0.2s;
  }
  .filter-input:focus, .filter-select:focus { border-color: #D4AF37; }

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
  .course-card:hover { transform: translateY(-3px); box-shadow: 0 8px 25px rgba(0,0,0,0.08); border-left-color: #D4AF37; }

  /* School Colors */
  .school-Business { border-left-color: #e91e63; }
  .school-IT { border-left-color: #2196f3; }
  .school-Science { border-left-color: #4caf50; }
  .school-Humanities { border-left-color: #ff9800; }

  .c-school { font-size: 0.75rem; text-transform: uppercase; font-weight: 700; color: #888; margin-bottom: 5px; }
  .c-title { font-size: 1.1rem; font-weight: 700; color: #333; margin: 0 0 10px 0; line-height: 1.4; }
  .c-level { display: inline-block; background: #f0f2f5; padding: 4px 10px; border-radius: 4px; font-size: 0.8rem; font-weight: 600; color: #555; }
  
  .c-footer { margin-top: 15px; display: flex; justify-content: space-between; align-items: center; }
  
  .view-btn {
    background: transparent; border: 1px solid #0A2342; color: #0A2342;
    padding: 6px 15px; border-radius: 50px; font-size: 0.85rem; font-weight: 600; cursor: pointer; transition: 0.2s;
  }
  .view-btn:hover { background: #0A2342; color: white; }

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
    background: #0A2342; padding: 20px 25px; color: white; display: flex; justify-content: space-between; align-items: center;
    position: sticky; top: 0; z-index: 10;
  }
  .modal-title { margin: 0; font-size: 1.2rem; font-weight: 700; }
  .close-modal { background: none; border: none; color: white; font-size: 2rem; cursor: pointer; }
  
  .modal-body { padding: 25px; }

  .info-block { margin-bottom: 25px; }
  .info-head { font-size: 0.95rem; font-weight: 700; color: #0A2342; border-bottom: 2px solid #f0f0f0; padding-bottom: 5px; margin-bottom: 10px; display: flex; align-items: center; gap: 8px; }
  .info-content { font-size: 0.95rem; color: #444; line-height: 1.6; }
  
  .tag-bubble { display: inline-block; background: #e3f2fd; color: #1565c0; padding: 4px 10px; border-radius: 20px; font-size: 0.85rem; margin: 0 5px 5px 0; }

  @keyframes slideUp { from { transform: translateY(50px); opacity: 0; } to { transform: translateY(0); opacity: 1; } }

  /* Mobile */
  @media (max-width: 900px) {
    .app-container { flex-direction: column; }
    .filters-sidebar { width: 100%; position: static; }
  }
</style>

<div class="sju-hero">
  <h1>St. Joseph's University Course Portal</h1>
  <p>Find your perfect course. Filter by School, Level, or Subject.</p>
</div>

<div class="app-container">

  <aside class="filters-sidebar">
    <div class="filter-group">
      <label class="filter-label">🔍 Search Course</label>
      <input type="text" id="searchInput" class="filter-input" placeholder="e.g. Psychology, BCA..." onkeyup="renderCourses()">
    </div>
    
    <div class="filter-group">
      <label class="filter-label">🏫 Filter by School</label>
      <select id="schoolFilter" class="filter-select" onchange="renderCourses()">
        <option value="All">All Schools</option>
        <option value="Business">School of Business</option>
        <option value="IT">School of IT</option>
        <option value="Communication">School of Communication</option>
        <option value="Humanities">School of Humanities</option>
        <option value="Chemical">School of Chemical Sciences</option>
        <option value="Physical">School of Physical Sciences</option>
        <option value="Life">School of Life Sciences</option>
        <option value="Languages">School of Languages</option>
        <option value="Social">School of Social Work</option>
      </select>
    </div>

    <div class="filter-group">
      <label class="filter-label">🎓 Programme Level</label>
      <select id="levelFilter" class="filter-select" onchange="renderCourses()">
        <option value="All">All Levels</option>
        <option value="UG">Undergraduate (UG)</option>
        <option value="PG">Postgraduate (PG)</option>
        <option value="Diploma">PG Diploma</option>
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
        <div class="info-head">📋 Programme Details</div>
        <div class="info-content" id="mDetails"></div>
      </div>

      <div class="info-block">
        <div class="info-head">✅ Eligibility Criteria</div>
        <div class="info-content" id="mEligibility"></div>
      </div>

      <div class="info-block">
        <div class="info-head">📝 Admission & Selection</div>
        <div class="info-content">
          <p><strong>Process:</strong> <span id="mProcess"></span></p>
          <p><strong>Entrance Test:</strong> <span id="mTest"></span></p>
        </div>
      </div>

      <div class="info-block">
        <div class="info-head">💰 Fee Structure (Approx/Year)</div>
        <div class="info-content" id="mFees" style="background:#f9f9f9; padding:10px; border-radius:5px;"></div>
      </div>

      <div class="info-block">
        <div class="info-head">🚀 Potential Career Outcomes</div>
        <div class="info-content" id="mCareers"></div>
      </div>
      
      <div style="text-align:center; margin-top:30px;">
        <a href="https://sju.edu.in/" target="_blank" style="background:#D4AF37; color:#0A2342; padding:12px 30px; text-decoration:none; font-weight:bold; border-radius:50px;">Apply on Official Website ↗</a>
      </div>

    </div>
  </div>
</div>

<script>
  // --- 1. MASTER DATABASE (ALL COURSES) ---
  const allCourses = [
    // --- BUSINESS (UG) ---
    { id: 1, name: "Bachelor of Commerce (B.Com)", school: "Business", level: "UG", elig: "12th Pass (Commerce/Science)", fee: "₹1.05L - ₹1.65L" },
    { id: 2, name: "B.Com (Industry Integrated)", school: "Business", level: "UG", elig: "12th Pass", fee: "₹1.05L - ₹1.65L" },
    { id: 3, name: "B.Com (International Finance & Acc.)", school: "Business", level: "UG", elig: "12th Pass (Accounts pref)", fee: "₹1.9L - ₹2.5L" },
    { id: 4, name: "Bachelor of Business Admin (BBA)", school: "Business", level: "UG", elig: "12th Pass (Any Stream)", fee: "₹1.4L - ₹2.1L" },
    { id: 5, name: "BBA (Strategic Finance)", school: "Business", level: "UG", elig: "12th Pass", fee: "₹2.0L - ₹2.6L" },
    { id: 6, name: "BBA (Branding & Entrepreneurship)", school: "Business", level: "UG", elig: "12th Pass", fee: "₹1.9L - ₹2.5L" },
    
    // --- CHEMICAL SCIENCES (UG) ---
    { id: 7, name: "B.Sc (Chemistry, Biotech, Biology)", school: "Chemical", level: "UG", elig: "12th Science (Bio)", fee: "₹50k - ₹1L" },
    { id: 8, name: "B.Sc (Biochem, Micro, Zoology)", school: "Chemical", level: "UG", elig: "12th Science (Bio)", fee: "₹50k - ₹1L" },
    { id: 9, name: "B.Sc (Biochem, Biology, Biotech)", school: "Chemical", level: "UG", elig: "12th Science (Bio)", fee: "₹50k - ₹1L" },
    { id: 10, name: "B.Sc (Biochem, Biotech, Zoology)", school: "Chemical", level: "UG", elig: "12th Science (Bio)", fee: "₹50k - ₹1L" },
    { id: 11, name: "B.Sc (Chemistry, Botany, Zoology)", school: "Chemical", level: "UG", elig: "12th Science (Bio)", fee: "₹50k - ₹1L" },
    { id: 12, name: "B.Sc (Physics, Chemistry, Maths)", school: "Chemical", level: "UG", elig: "12th Science (PCM)", fee: "₹50k - ₹1L" },
    { id: 13, name: "B.Sc (Chem, Env Science, Biology)", school: "Chemical", level: "UG", elig: "12th Science", fee: "₹50k - ₹1L" },
    
    // --- HUMANITIES (UG) ---
    { id: 14, name: "B.Sc (Econ, Maths, Statistics)", school: "Humanities", level: "UG", elig: "12th with Maths", fee: "₹90k - ₹1.5L" },
    { id: 15, name: "B.A. (Ind. Relations, Econ, Sociology)", school: "Humanities", level: "UG", elig: "12th Pass", fee: "₹40k - ₹90k" },
    { id: 16, name: "B.A. (Econ, Pol Sci, Sociology)", school: "Humanities", level: "UG", elig: "12th Pass", fee: "₹40k - ₹90k" },
    { id: 17, name: "B.A. (History, Pol Sci, Sociology)", school: "Humanities", level: "UG", elig: "12th Pass", fee: "₹40k - ₹90k" },
    { id: 18, name: "B.A. (Intl Relations, Peace, Journ)", school: "Humanities", level: "UG", elig: "12th Pass", fee: "₹60k - ₹1.2L" },
    { id: 19, name: "B.A. (Journalism, Pol Sci, Soc)", school: "Humanities", level: "UG", elig: "12th Pass", fee: "₹60k - ₹1.2L" },
    { id: 20, name: "B.A. (Comm English, Pol Sci, Econ)", school: "Humanities", level: "UG", elig: "12th Pass", fee: "₹60k - ₹1.2L" },
    { id: 21, name: "B.A. (Journalism, Econ, Psychology)", school: "Humanities", level: "UG", elig: "12th Pass", fee: "₹60k - ₹1.2L" },
    
    // --- LANGUAGES (UG) ---
    { id: 22, name: "B.A. (Opt English, Journ, Psych)", school: "Languages", level: "UG", elig: "12th Pass", fee: "₹60k - ₹1.2L" },
    { id: 23, name: "B.A. (Theatre, Opt English, Psych)", school: "Languages", level: "UG", elig: "12th Pass", fee: "₹60k - ₹1.2L" },

    // --- LIFE SCIENCES (UG) ---
    { id: 24, name: "B.Sc (Botany, Env Sci, Zoology)", school: "Life", level: "UG", elig: "12th Science", fee: "₹50k - ₹1L" },
    { id: 25, name: "B.Sc (Biochem, Botany, Biotech)", school: "Life", level: "UG", elig: "12th Science", fee: "₹50k - ₹1L" },

    // --- PHYSICAL SCIENCES (UG) ---
    { id: 26, name: "B.Sc (Physics, Maths, Comp Sci)", school: "Physical", level: "UG", elig: "12th PCM", fee: "₹90k - ₹1.5L" },
    { id: 27, name: "B.Sc (Physics, Electronics, Maths)", school: "Physical", level: "UG", elig: "12th PCM", fee: "₹50k - ₹1L" },
    { id: 28, name: "B.Sc (Comp Sci, Maths, Stats)", school: "Physical", level: "UG", elig: "12th Maths", fee: "₹90k - ₹1.5L" },

    // --- SOCIAL WORK (UG) ---
    { id: 29, name: "Bachelor of Social Work (BSW)", school: "Social", level: "UG", elig: "12th Pass", fee: "₹40k - ₹80k" },

    // --- COMMUNICATION (UG) ---
    { id: 30, name: "B.A. Visual Communication", school: "Communication", level: "UG", elig: "12th Pass + Portfolio", fee: "₹1.3L - ₹1.9L" },
    { id: 31, name: "B.Voc Digital Media & Animation", school: "Communication", level: "UG", elig: "12th Pass", fee: "₹1.1L - ₹1.7L" },
    { id: 32, name: "B.Voc Visual Media & Filmmaking", school: "Communication", level: "UG", elig: "12th Pass", fee: "₹1.1L - ₹1.7L" },

    // --- IT (UG) ---
    { id: 33, name: "Bachelor of Computer Applications (BCA)", school: "IT", level: "UG", elig: "12th Maths/CS/Elec", fee: "₹1.15L - ₹1.85L" },
    { id: 34, name: "BCA (Data Analytics)", school: "IT", level: "UG", elig: "12th Maths/Stats", fee: "₹1.5L - ₹2.1L" },

    // --- PG COURSES ---
    { id: 35, name: "Master of Commerce (M.Com)", school: "Business", level: "PG", elig: "B.Com/BBA", fee: "₹1.1L - ₹1.7L" },
    { id: 36, name: "M.Sc Analytical Chemistry", school: "Chemical", level: "PG", elig: "B.Sc Chemistry", fee: "₹80k - ₹1.5L" },
    { id: 37, name: "M.Sc Organic Chemistry", school: "Chemical", level: "PG", elig: "B.Sc Chemistry", fee: "₹80k - ₹1.5L" },
    { id: 38, name: "M.Sc Biochemistry", school: "Chemical", level: "PG", elig: "B.Sc Biochem", fee: "₹80k - ₹1.5L" },
    { id: 39, name: "M.A. Economics", school: "Humanities", level: "PG", elig: "BA Economics", fee: "₹80k - ₹1.5L" },
    { id: 40, name: "M.A. Political Science", school: "Humanities", level: "PG", elig: "BA Pol Sci", fee: "₹80k - ₹1.5L" },
    { id: 41, name: "M.Sc Counselling Psychology", school: "Humanities", level: "PG", elig: "BA/B.Sc Psych", fee: "₹1.2L - ₹2L" },
    { id: 42, name: "M.A. English", school: "Languages", level: "PG", elig: "BA English", fee: "₹80k - ₹1.5L" },
    { id: 43, name: "M.Sc Biotechnology", school: "Life", level: "PG", elig: "B.Sc Biotech", fee: "₹1L - ₹1.8L" },
    { id: 44, name: "M.Sc Mathematics", school: "Physical", level: "PG", elig: "B.Sc Maths", fee: "₹80k - ₹1.5L" },
    { id: 45, name: "M.Sc Physics", school: "Physical", level: "PG", elig: "B.Sc Physics", fee: "₹80k - ₹1.5L" },
    { id: 46, name: "Master of Social Work (MSW)", school: "Social", level: "PG", elig: "Any Degree", fee: "₹80k - ₹1.5L" },
    { id: 47, name: "M.A. Advertising & PR", school: "Communication", level: "PG", elig: "Any Degree", fee: "₹1.4L - ₹2L" },
    { id: 48, name: "M.A. Journalism & Mass Comm", school: "Communication", level: "PG", elig: "Any Degree", fee: "₹1.4L - ₹2L" },
    { id: 49, name: "Master of Computer Applications (MCA)", school: "IT", level: "PG", elig: "BCA/B.Sc CS", fee: "₹1.75L - ₹2.35L" },
    { id: 50, name: "M.Sc Big Data Analytics", school: "IT", level: "PG", elig: "B.Sc Maths/CS", fee: "₹1.75L - ₹2.35L" },
    { id: 51, name: "M.Sc Cyber Security & AI", school: "IT", level: "PG", elig: "B.Sc CS/IT", fee: "₹1.75L - ₹2.35L" },

    // --- DIPLOMA ---
    { id: 52, name: "PG Diploma in Financial Mgmt", school: "Business", level: "Diploma", elig: "Degree", fee: "Contact Office" },
    { id: 53, name: "PG Diploma in HR Management", school: "Business", level: "Diploma", elig: "Degree", fee: "Contact Office" },
    { id: 54, name: "PG Diploma in Cyber Security", school: "IT", level: "Diploma", elig: "Tech Degree", fee: "Contact Office" },
    { id: 55, name: "PG Diploma in Data Analytics", school: "IT", level: "Diploma", elig: "Tech Degree", fee: "Contact Office" },
    { id: 56, name: "Exec. Diploma Digital Media", school: "Communication", level: "Diploma", elig: "Degree/Exp", fee: "Contact Office" }
  ];

  // --- 2. RENDER FUNCTIONS ---
  function renderCourses() {
    const searchText = document.getElementById('searchInput').value.toLowerCase();
    const schoolFilter = document.getElementById('schoolFilter').value;
    const levelFilter = document.getElementById('levelFilter').value;
    const grid = document.getElementById('courseGrid');
    
    grid.innerHTML = '';
    let count = 0;

    allCourses.forEach(course => {
      // Logic for Filtering
      const matchesSearch = course.name.toLowerCase().includes(searchText);
      const matchesSchool = schoolFilter === 'All' || course.school === schoolFilter;
      const matchesLevel = levelFilter === 'All' || course.level === levelFilter;

      if (matchesSearch && matchesSchool && matchesLevel) {
        count++;
        // Generate Card HTML
        const card = `
          <div class="course-card school-${course.school}">
            <div class="c-info">
              <span class="c-school">School of ${course.school}</span>
              <h3 class="c-title">${course.name}</h3>
              <div class="c-meta">
                <span class="c-level">${course.level}</span>
                <span class="c-badge">Elig: ${course.elig}</span>
              </div>
            </div>
            <div class="c-footer">
              <button class="view-btn" onclick="openModal(${course.id})">View Details</button>
            </div>
          </div>
        `;
        grid.innerHTML += card;
      }
    });

    document.getElementById('countDisplay').innerText = count;
  }

  // --- 3. MODAL LOGIC ---
  function openModal(id) {
    const course = allCourses.find(c => c.id === id);
    if (!course) return;

    document.getElementById('mTitle').innerText = course.name;
    document.getElementById('mFees').innerText = course.fee;
    document.getElementById('mEligibility').innerText = course.elig;
    
    // Dynamic Content Gen based on course Keywords
    let careers = "Specialist roles in the field, Research, Higher Education (PhD/Masters).";
    if (course.name.includes("BCA") || course.name.includes("Computer")) careers = "Software Engineer, Web Developer, System Analyst, Data Scientist.";
    if (course.name.includes("Commerce") || course.name.includes("BBA")) careers = "Accountant, Financial Analyst, HR Executive, Marketing Manager.";
    if (course.name.includes("Visual") || course.name.includes("Media")) careers = "Graphic Designer, Content Creator, Film Editor, PR Specialist.";
    if (course.name.includes("Chemistry") || course.name.includes("Physics")) careers = "Lab Scientist, Researcher, Lecturer, Industrial R&D.";

    document.getElementById('mCareers').innerText = careers;
    
    // Syllabus & Process
    document.getElementById('mDetails').innerText = "This programme offers in-depth knowledge in " + course.school + " with a focus on holistic development and practical skills.";
    document.getElementById('mProcess').innerText = "Online Application -> Entrance Test (for select courses) -> Personal Interview.";
    document.getElementById('mTest').innerText = course.name.includes("B.A.") || course.name.includes("B.Sc") ? "Merit Based (Interview)" : "SJUET Entrance Test (Check Official Site)";

    document.getElementById('courseModal').style.display = 'flex';
  }

  function closeModalBtn() { document.getElementById('courseModal').style.display = 'none'; }
  function closeModal(e) { if(e.target.className === 'modal-overlay') document.getElementById('courseModal').style.display = 'none'; }

  // Initial Load
  renderCourses();
</script>

<br>

Here is a video from YouTube that might be helpful:
[St. Joseph's University, Bangalore - Admission Process 2023, List of Courses etc](https://www.youtube.com/watch?v=u60gE02OyII)

This video provides a comprehensive overview of the admission process, course list, and fee structure for St. Joseph's University, Bangalore, which complements the information on the updated webpage.
