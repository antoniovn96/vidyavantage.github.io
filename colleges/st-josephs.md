---
layout: default
title: "St. Joseph's University Course Portal"
permalink: /colleges/st-josephs/
image: "https://images.unsplash.com/photo-1541339907198-e08756dedf3f?w=1200&h=630&fit=crop"
description: "Browse 50+ Undergraduate & PG courses at St. Joseph's University, Bengaluru. Check eligibility, fees, and admission details."
---

<meta property="og:title" content="St. Joseph's University Course Portal 🎓">
<meta property="og:description" content="Browse 50+ Undergraduate & PG courses at St. Joseph's University. Check eligibility, fees, and admission details.">
<meta property="og:image" content="https://images.unsplash.com/photo-1541339907198-e08756dedf3f?w=1200&h=630&fit=crop">

<style>
  /* 1. LAYOUT & RESET */
  .main-content { max-width: 100% !important; padding: 0 !important; margin: 0 !important; }
  body { background-color: #f4f6f8; font-family: 'Segoe UI', system-ui, sans-serif; color: #333; }

  /* 2. HERO SECTION */
  .sju-hero {
    background: linear-gradient(rgba(10, 35, 66, 0.9), rgba(10, 35, 66, 0.8)), url('https://images.unsplash.com/photo-1541339907198-e08756dedf3f?w=1600&auto=format&fit=crop');
    background-size: cover;
    background-position: center;
    color: white;
    text-align: center;
    padding: 80px 20px;
    margin-bottom: 0;
  }
  
  .sju-hero h1 { font-size: 3rem; margin: 0; font-weight: 800; color: white !important; }
  .sju-hero p { font-size: 1.2rem; color: #ddd !important; margin-top: 10px; max-width: 700px; margin-left: auto; margin-right: auto; }

  /* 3. INFO STATS STRIP */
  .stats-strip {
    background: white;
    display: flex;
    justify-content: center;
    gap: 40px;
    padding: 20px;
    box-shadow: 0 4px 20px rgba(0,0,0,0.05);
    margin-bottom: 40px;
    flex-wrap: wrap;
  }
  .stat-item { text-align: center; }
  .stat-val { font-size: 1.5rem; font-weight: 800; color: #0A2342; display: block; }
  .stat-label { font-size: 0.85rem; color: #666; text-transform: uppercase; font-weight: 600; letter-spacing: 1px; }

  /* 4. SEARCH & FILTER BAR (STICKY) */
  .filter-bar {
    background: #0A2342;
    padding: 20px;
    position: sticky;
    top: 60px; /* Adjust based on your nav height */
    z-index: 100;
    display: flex;
    justify-content: center;
    gap: 15px;
    flex-wrap: wrap;
    box-shadow: 0 5px 15px rgba(0,0,0,0.2);
  }

  .search-input {
    padding: 12px 20px;
    border-radius: 50px;
    border: none;
    width: 300px;
    font-size: 1rem;
    outline: none;
    background: white;
  }

  .school-select {
    padding: 12px 20px;
    border-radius: 50px;
    border: none;
    font-size: 0.95rem;
    background: #f8f9fa;
    color: #333;
    outline: none;
    cursor: pointer;
  }

  /* 5. TABS */
  .level-tabs { display: flex; justify-content: center; gap: 10px; margin: 30px 0; padding: 0 20px; }
  .tab-btn {
    background: white; border: 1px solid #ddd; padding: 10px 25px; border-radius: 50px;
    font-weight: 600; color: #555; cursor: pointer; transition: 0.3s;
  }
  .tab-btn.active { background: #D4AF37; color: #0A2342; border-color: #D4AF37; font-weight: 800; box-shadow: 0 4px 10px rgba(212, 175, 55, 0.4); }

  /* 6. COURSE LIST (CARD STYLE) */
  .course-container { max-width: 1000px; margin: 0 auto; padding: 0 20px 80px; display: none; }
  .course-container.active { display: block; animation: fadeIn 0.4s; }

  .course-card {
    background: white;
    border-radius: 10px;
    padding: 20px 25px;
    margin-bottom: 20px;
    border-left: 5px solid #0A2342;
    box-shadow: 0 5px 15px rgba(0,0,0,0.03);
    display: flex;
    justify-content: space-between;
    align-items: center;
    transition: transform 0.2s, box-shadow 0.2s;
  }
  .course-card:hover { transform: translateY(-3px); box-shadow: 0 10px 25px rgba(0,0,0,0.08); }

  .c-info h3 { margin: 0 0 5px 0; font-size: 1.2rem; color: #0A2342; }
  .c-meta { font-size: 0.85rem; color: #666; display: flex; gap: 15px; align-items: center; flex-wrap: wrap; }
  .c-badge { background: #e3f2fd; color: #1565c0; padding: 3px 8px; border-radius: 4px; font-weight: 600; }
  .c-school { color: #888; font-weight: 600; font-size: 0.8rem; text-transform: uppercase; }

  .details-btn {
    background: transparent;
    border: 2px solid #0A2342;
    color: #0A2342;
    padding: 8px 18px;
    border-radius: 50px;
    font-weight: bold;
    cursor: pointer;
    transition: all 0.2s;
    white-space: nowrap;
  }
  .details-btn:hover { background: #0A2342; color: white; }

  /* 7. MODAL STYLES */
  .modal-overlay {
    display: none; position: fixed; top: 0; left: 0; width: 100%; height: 100%;
    background: rgba(0,0,0,0.6); z-index: 2000; align-items: center; justify-content: center;
    backdrop-filter: blur(4px);
  }
  .modal-content {
    background: white; width: 90%; max-width: 600px; border-radius: 15px;
    position: relative; animation: slideUp 0.3s; overflow: hidden; display: flex; flex-direction: column;
    max-height: 85vh;
  }
  .modal-header { background: #0A2342; padding: 20px; color: white; display: flex; justify-content: space-between; align-items: center; }
  .modal-header h2 { margin: 0; font-size: 1.3rem; }
  .close-btn { background: none; border: none; color: white; font-size: 2rem; cursor: pointer; }
  .modal-body { padding: 30px; overflow-y: auto; }

  .info-group { margin-bottom: 20px; }
  .info-label { font-size: 0.85rem; color: #888; text-transform: uppercase; font-weight: 700; margin-bottom: 5px; display: block; }
  .info-text { font-size: 1rem; color: #333; line-height: 1.5; }
  
  .fee-table { width: 100%; border-collapse: collapse; margin-top: 10px; font-size: 0.95rem; }
  .fee-table td { padding: 8px 0; border-bottom: 1px dashed #eee; }
  .fee-table td:last-child { text-align: right; font-weight: bold; color: #0A2342; }

  @keyframes slideUp { from { transform: translateY(50px); opacity: 0; } to { transform: translateY(0); opacity: 1; } }
  @keyframes fadeIn { from { opacity: 0; } to { opacity: 1; } }

  /* Mobile Tweaks */
  @media (max-width: 768px) {
    .course-card { flex-direction: column; align-items: flex-start; gap: 15px; }
    .details-btn { width: 100%; }
    .filter-bar { flex-direction: column; }
    .search-input, .school-select { width: 100%; }
    .uni-hero h1 { font-size: 2.5rem; }
  }
</style>

<div class="sju-hero">
  <h1>St. Joseph's University</h1>
  <p>Bengaluru's premier Jesuit university with a legacy of 140+ years.</p>
</div>

<div class="stats-strip">
  <div class="stat-item"><span class="stat-val">A++</span><span class="stat-label">NAAC Grade</span></div>
  <div class="stat-item"><span class="stat-val">1882</span><span class="stat-label">Established</span></div>
  <div class="stat-item"><span class="stat-val">60+</span><span class="stat-label">Courses</span></div>
  <div class="stat-item"><span class="stat-val">Central</span><span class="stat-label">Location</span></div>
</div>

<div class="filter-bar">
  <input type="text" id="courseSearch" class="search-input" placeholder="Search courses (e.g. BBA, Data Science)..." onkeyup="filterCourses()">
  <select id="schoolFilter" class="school-select" onchange="filterCourses()">
    <option value="all">All Schools</option>
    <option value="Business">School of Business</option>
    <option value="Chemical">School of Chemical Sciences</option>
    <option value="Humanities">School of Humanities</option>
    <option value="IT">School of IT</option>
    <option value="Communication">School of Communication</option>
    <option value="Life">School of Life Sciences</option>
    <option value="Physical">School of Physical Sciences</option>
  </select>
</div>

<div class="level-tabs">
  <button class="tab-btn active" onclick="openTab('ug')">Undergraduate</button>
  <button class="tab-btn" onclick="openTab('pg')">Postgraduate</button>
  <button class="tab-btn" onclick="openTab('diploma')">PG Diploma</button>
</div>

<div id="ug" class="course-container active">
  
  <div class="course-card" data-school="Business" data-name="bcom regular commerce">
    <div class="c-info">
      <span class="c-school">School of Business</span>
      <h3>B.Com (Regular)</h3>
      <div class="c-meta"><span class="c-badge">Batch: Morning/Evening</span> <span>Elig: 12th Pass</span></div>
    </div>
    <button class="details-btn" onclick="openDetails('bcom')">View Details</button>
  </div>

  <div class="course-card" data-school="Business" data-name="bcom industry integrated">
    <div class="c-info">
      <span class="c-school">School of Business</span>
      <h3>B.Com (Industry Integrated)</h3>
      <div class="c-meta"><span class="c-badge">Batch: 7am - 12pm</span> <span>Elig: 12th Pass</span></div>
    </div>
    <button class="details-btn" onclick="openDetails('bcom_ind')">View Details</button>
  </div>

  <div class="course-card" data-school="Business" data-name="bcom international finance">
    <div class="c-info">
      <span class="c-school">School of Business</span>
      <h3>B.Com (International Finance & Acc.)</h3>
      <div class="c-meta"><span class="c-badge">Batch: Morning/Evening</span> <span>Elig: 12th (Accounts pref)</span></div>
    </div>
    <button class="details-btn" onclick="openDetails('bcom_intl')">View Details</button>
  </div>

  <div class="course-card" data-school="Business" data-name="bba regular">
    <div class="c-info">
      <span class="c-school">School of Business</span>
      <h3>Bachelor of Business Admin (BBA)</h3>
      <div class="c-meta"><span class="c-badge">Batch: Morning/Evening</span> <span>Elig: 12th Pass</span></div>
    </div>
    <button class="details-btn" onclick="openDetails('bba')">View Details</button>
  </div>

  <div class="course-card" data-school="Business" data-name="bba strategic finance">
    <div class="c-info">
      <span class="c-school">School of Business</span>
      <h3>BBA (Strategic Finance)</h3>
      <div class="c-meta"><span class="c-badge">Batch: Morning/Evening</span> <span>Elig: 12th Pass</span></div>
    </div>
    <button class="details-btn" onclick="openDetails('bba_strat')">View Details</button>
  </div>

  <div class="course-card" data-school="IT" data-name="bca computer applications">
    <div class="c-info">
      <span class="c-school">School of IT</span>
      <h3>Bachelor of Computer Applications (BCA)</h3>
      <div class="c-meta"><span class="c-badge">Batch: 9am-4pm / 4pm-9pm</span> <span>Elig: 12th (Maths/CS)</span></div>
    </div>
    <button class="details-btn" onclick="openDetails('bca')">View Details</button>
  </div>

  <div class="course-card" data-school="IT" data-name="bca data analytics">
    <div class="c-info">
      <span class="c-school">School of IT</span>
      <h3>BCA (Data Analytics)</h3>
      <div class="c-meta"><span class="c-badge">Batch: 7am - 1pm</span> <span>Elig: 12th (Maths)</span></div>
    </div>
    <button class="details-btn" onclick="openDetails('bca_data')">View Details</button>
  </div>

  <div class="course-card" data-school="Physical" data-name="bsc pcm physics chemistry maths">
    <div class="c-info">
      <span class="c-school">School of Physical Sciences</span>
      <h3>B.Sc (Physics, Chem, Maths)</h3>
      <div class="c-meta"><span class="c-badge">Batch: 9am - 4pm</span> <span>Elig: 12th (PCM)</span></div>
    </div>
    <button class="details-btn" onclick="openDetails('bsc_pcm')">View Details</button>
  </div>

  <div class="course-card" data-school="Chemical" data-name="bsc cbz chemistry botany zoology">
    <div class="c-info">
      <span class="c-school">School of Chemical Sciences</span>
      <h3>B.Sc (Chem, Botany, Zoology)</h3>
      <div class="c-meta"><span class="c-badge">Batch: 9am - 4pm</span> <span>Elig: 12th (PCB)</span></div>
    </div>
    <button class="details-btn" onclick="openDetails('bsc_cbz')">View Details</button>
  </div>

  <div class="course-card" data-school="Communication" data-name="ba visual communication">
    <div class="c-info">
      <span class="c-school">School of Communication</span>
      <h3>B.A. Visual Communication</h3>
      <div class="c-meta"><span class="c-badge">Batch: 7am - 1pm</span> <span>Elig: 12th Pass</span></div>
    </div>
    <button class="details-btn" onclick="openDetails('viscom')">View Details</button>
  </div>

</div>

<div id="pg" class="course-container">
  
  <div class="course-card" data-school="Business" data-name="mcom commerce">
    <div class="c-info">
      <span class="c-school">School of Business</span>
      <h3>Master of Commerce (M.Com)</h3>
      <div class="c-meta"><span class="c-badge">Batch: 7am-11am / 4pm-8pm</span> <span>Elig: B.Com/BBA</span></div>
    </div>
    <button class="details-btn" onclick="openDetails('mcom')">View Details</button>
  </div>

  <div class="course-card" data-school="IT" data-name="mca computer applications">
    <div class="c-info">
      <span class="c-school">School of IT</span>
      <h3>Master of Computer Applications (MCA)</h3>
      <div class="c-meta"><span class="c-badge">Batch: 1pm - 7pm</span> <span>Elig: BCA/B.Sc CS</span></div>
    </div>
    <button class="details-btn" onclick="openDetails('mca')">View Details</button>
  </div>

  <div class="course-card" data-school="Communication" data-name="ma advertising public relations">
    <div class="c-info">
      <span class="c-school">School of Communication</span>
      <h3>M.A. Advertising & Public Relations</h3>
      <div class="c-meta"><span class="c-badge">Batch: 7am - 1pm</span> <span>Elig: Any Degree</span></div>
    </div>
    <button class="details-btn" onclick="openDetails('ma_apr')">View Details</button>
  </div>

</div>

<div id="diploma" class="course-container">
  
  <div class="course-card" data-school="Business" data-name="pg diploma financial management">
    <div class="c-info">
      <span class="c-school">School of Business</span>
      <h3>PG Diploma in Financial Management</h3>
      <div class="c-meta"><span class="c-badge">Batch: Weekend</span> <span>Elig: Degree</span></div>
    </div>
    <button class="details-btn" onclick="openDetails('pgd_fm')">View Details</button>
  </div>

  <div class="course-card" data-school="IT" data-name="pg diploma cyber security">
    <div class="c-info">
      <span class="c-school">School of IT</span>
      <h3>PG Diploma in Cyber Security</h3>
      <div class="c-meta"><span class="c-badge">Batch: Weekend</span> <span>Elig: Tech Degree</span></div>
    </div>
    <button class="details-btn" onclick="openDetails('pgd_cs')">View Details</button>
  </div>

</div>

<div id="modal" class="modal-overlay" onclick="closeModal(event)">
  <div class="modal-content">
    <div class="modal-header">
      <h2 id="m-title">Course Title</h2>
      <button class="close-btn" onclick="closeModalBtn()">&times;</button>
    </div>
    <div class="modal-body">
      
      <div class="info-group">
        <span class="info-label">📋 Eligibility</span>
        <div id="m-eligibility" class="info-text"></div>
      </div>

      <div class="info-group">
        <span class="info-label">📚 Syllabus Highlight</span>
        <div id="m-syllabus" class="info-text"></div>
      </div>

      <div class="info-group">
        <span class="info-label">💰 Fee Structure (Per Year)</span>
        <table class="fee-table" id="m-fees"></table>
      </div>

      <div class="info-group">
        <span class="info-label">🚀 Career Outcomes</span>
        <div id="m-careers" class="info-text"></div>
      </div>

      <div style="text-align: center; margin-top: 20px;">
        <a id="m-link" href="#" target="_blank" style="background:#0A2342; color:white; padding:12px 30px; border-radius:50px; text-decoration:none; font-weight:bold;">Visit Official Page ↗</a>
      </div>

    </div>
  </div>
</div>

<script>
  // --- 1. COURSE DATA ---
  const courseDB = {
    'bcom': {
      title: "Bachelor of Commerce (B.Com)",
      elig: "Pass in Class 12 (10+2) or equivalent from a recognized board.",
      syl: "Financial Accounting, Corporate Accounting, Business Law, Taxation, Auditing.",
      fees: { "Karnataka": "₹1,05,000", "Non-Karnataka": "₹1,20,000", "NRI": "₹1,65,000" },
      jobs: "Accountant, Financial Analyst, Tax Consultant, Banker.",
      link: "https://sju.edu.in/courses/st-joseph-university/school-of-business/Department-of-Commerce/bachelor-of-commerce"
    },
    'bcom_ind': {
      title: "B.Com (Industry Integrated)",
      elig: "Pass in Class 12. Designed for immediate industry placement.",
      syl: "BPM (Business Process Management) by TCS, Retail Operations, Corporate Culture.",
      fees: { "Karnataka": "₹1,05,000", "Non-Karnataka": "₹1,20,000", "NRI": "₹1,65,000" },
      jobs: "Process Analyst in TCS/MNCs, Operations Executive.",
      link: "https://sju.edu.in/courses/st-joseph-university/school-of-business/Department-of-Commerce/bachelor-of-commerce-industry-integrated"
    },
    'bcom_intl': {
      title: "B.Com (International Finance & Acc.)",
      elig: "Pass in Class 12. High aptitude for Accounting required.",
      syl: "ACCA Accredited Curriculum: IFRS, Audit & Assurance, Performance Management.",
      fees: { "Karnataka": "₹1,90,000", "Non-Karnataka": "₹2,10,000", "NRI": "₹2,50,000" },
      jobs: "ACCA Certified Professional, Global Auditor, Finance Consultant.",
      link: "https://sju.edu.in/courses/st-joseph-university/school-of-business/Department-of-Commerce/bcom-international-finance-and-accounting"
    },
    'bba': {
      title: "Bachelor of Business Administration (BBA)",
      elig: "Pass in Class 12 (Any stream). Min 50% aggregate suggested.",
      syl: "Management Principles, Marketing, HRM, Organizational Behavior.",
      fees: { "Karnataka": "₹1,40,000", "Non-Karnataka": "₹1,60,000", "NRI": "₹2,10,000" },
      jobs: "HR Executive, Marketing Associate, Manager.",
      link: "https://sju.edu.in/courses/st-joseph-university/school-of-business/department-of-management/batchelor-of-business-administration"
    },
    'bca': {
      title: "Bachelor of Computer Applications (BCA)",
      elig: "Pass in Class 12. Maths/CS/Electronics background mandatory.",
      syl: "Java, Python, Web Dev, DBMS, Software Engineering.",
      fees: { "Karnataka": "₹1,15,000", "Non-Karnataka": "₹1,35,000", "NRI": "₹1,85,000" },
      jobs: "Software Developer, Web Developer, System Analyst.",
      link: "https://sju.edu.in/courses/st-joseph-university/school--of-information-technology/computer-science-and-computer-application/bachelor-of-computer-applications"
    },
    'bca_data': {
      title: "BCA (Data Analytics)",
      elig: "Pass in Class 12 with Maths/Stats.",
      syl: "R Programming, Big Data, Machine Learning, Visualization.",
      fees: { "Karnataka": "₹1,50,000", "Non-Karnataka": "₹1,65,000", "NRI": "₹2,10,000" },
      jobs: "Data Analyst, Junior Data Scientist.",
      link: "https://sju.edu.in/courses/st-joseph-university/school--of-information-technology/advanced-computing/bca-data-analytics"
    },
    'bsc_pcm': {
      title: "B.Sc (Physics, Chemistry, Maths)",
      elig: "Pass in Class 12 Science (PCM).",
      syl: "Thermodynamics, Organic Chemistry, Calculus, Optics.",
      fees: { "Karnataka": "₹50,000", "Non-Karnataka": "₹60,000", "NRI": "₹1,10,000" },
      jobs: "Lab Technician, Researcher, Teacher.",
      link: "https://sju.edu.in/courses/st-joseph-university/school-of-physical-sciences/physics/physics,-mathematics-and-chemistry"
    },
    'viscom': {
      title: "B.A. Visual Communication",
      elig: "Pass in Class 12 (Any Stream). Creative Portfolio required.",
      syl: "Graphic Design, Photography, Videography, Media Laws.",
      fees: { "Karnataka": "₹1,30,000", "Non-Karnataka": "₹1,45,000", "NRI": "₹1,90,000" },
      jobs: "Graphic Designer, Photographer, Film Editor.",
      link: "https://sju.edu.in/courses/st-joseph-university/school-of-communication-and-media-studies/Communication/ba-visual-communication"
    },
    'mcom': {
      title: "Master of Commerce (M.Com)",
      elig: "B.Com/BBA with min 50%.",
      syl: "Advanced Financial Management, Forex, Risk Management.",
      fees: { "Karnataka": "₹1,10,000", "Non-Karnataka": "₹1,25,000", "NRI": "₹1,70,000" },
      jobs: "Senior Accountant, Finance Manager.",
      link: "https://sju.edu.in/courses/st-joseph-university/school-of-business/Department-of-Commerce/mcom"
    }
    // Add more courses as needed mapping to the HTML buttons
  };

  // --- 2. LOGIC ---
  function openTab(tabId) {
    document.querySelectorAll('.course-container').forEach(el => el.classList.remove('active'));
    document.querySelectorAll('.tab-btn').forEach(btn => btn.classList.remove('active'));
    document.getElementById(tabId).classList.add('active');
    event.currentTarget.classList.add('active');
  }

  function filterCourses() {
    const input = document.getElementById('courseSearch').value.toLowerCase();
    const school = document.getElementById('schoolFilter').value;
    const items = document.querySelectorAll('.course-card');

    items.forEach(item => {
      const name = item.getAttribute('data-name');
      const itemSchool = item.getAttribute('data-school');
      
      const matchesSearch = name.includes(input);
      const matchesSchool = school === "all" || itemSchool === school;

      if (matchesSearch && matchesSchool) {
        item.style.display = "flex";
      } else {
        item.style.display = "none";
      }
    });
  }

  function openDetails(key) {
    const data = courseDB[key];
    if (!data) return;

    document.getElementById('m-title').innerText = data.title;
    document.getElementById('m-eligibility').innerText = data.elig;
    document.getElementById('m-syllabus').innerText = data.syl;
    document.getElementById('m-careers').innerText = data.jobs;
    document.getElementById('m-link').href = data.link;

    const table = document.getElementById('m-fees');
    table.innerHTML = "";
    for (const [k, v] of Object.entries(data.fees)) {
      table.innerHTML += `<tr><td>${k}</td><td>${v}</td></tr>`;
    }

    document.getElementById('modal').style.display = 'flex';
  }

  function closeModalBtn() { document.getElementById('modal').style.display = 'none'; }
  function closeModal(e) { if(e.target.className === 'modal-overlay') document.getElementById('modal').style.display = 'none'; }
</script>
