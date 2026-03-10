---
layout: default
title: "O.P. Jindal Global University (JGU Online) Course Portal 🎓"
permalink: /colleges/jgu-online/
image: "https://images.unsplash.com/photo-1523050854058-8df90110c9f1?w=1600&auto=format&fit=crop"
description: "Browse 100% online Undergraduate (BBA, B.Sc, B.Com) and Masters (MBA, M.A., M.Sc, M.Des) programs at JGU Online. Check eligibility, fees, and career outcomes."
---

<meta property="og:title" content="JGU Online Course Portal 🎓">
<meta property="og:description" content="Access details for Online MBA, M.A. in Public Policy, BBA, M.Sc in AI, and more. Check fees, eligibility, and selection process.">
<meta property="og:image" content="https://images.unsplash.com/photo-1523050854058-8df90110c9f1?w=1600&auto=format&fit=crop">

<style>
  /* 1. LAYOUT RESET */
  .main-content { max-width: 100% !important; padding: 0 !important; margin: 0 !important; }
  body { background-color: #f4f6f8; font-family: 'Segoe UI', system-ui, sans-serif; color: #333; }

  /* 2. HERO SECTION */
  .jgu-hero {
    background: linear-gradient(rgba(11, 43, 94, 0.95), rgba(11, 43, 94, 0.85)), url('https://images.unsplash.com/photo-1523050854058-8df90110c9f1?w=1600&auto=format&fit=crop');
    background-size: cover;
    background-position: center;
    color: white;
    text-align: center;
    padding: 80px 20px;
    margin-bottom: 0;
  }
  
  .jgu-hero h1 { font-size: 2.8rem; margin: 0; font-weight: 800; color: #fff !important; }
  .jgu-hero p { font-size: 1.1rem; color: #D4AF37 !important; margin-top: 10px; max-width: 700px; margin-left: auto; margin-right: auto; font-weight: 600; }

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
    border-top: 4px solid #0B2B5E; /* JGU Navy Blue */
    flex-shrink: 0;
  }

  .filter-group { margin-bottom: 20px; }
  .filter-label { display: block; font-weight: 700; margin-bottom: 8px; color: #0B2B5E; font-size: 0.9rem; }
  
  .filter-input, .filter-select {
    width: 100%;
    padding: 10px 15px;
    border: 1px solid #ddd;
    border-radius: 8px;
    font-size: 0.95rem;
    outline: none;
    transition: border 0.2s;
  }
  .filter-input:focus, .filter-select:focus { border-color: #0B2B5E; }

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

  /* Level Colors */
  .level-UG { border-left-color: #2196f3; }
  .level-PG { border-left-color: #0B2B5E; }

  .c-school { font-size: 0.75rem; text-transform: uppercase; font-weight: 700; color: #888; margin-bottom: 5px; }
  .c-title { font-size: 1.1rem; font-weight: 700; color: #333; margin: 0 0 10px 0; line-height: 1.4; }
  .c-meta { display: flex; gap: 8px; flex-wrap: wrap; margin-bottom: 15px; }
  .c-badge { display: inline-block; background: #f0f2f5; padding: 4px 10px; border-radius: 4px; font-size: 0.75rem; font-weight: 600; color: #555; }
  
  .c-footer { margin-top: auto; display: flex; justify-content: space-between; align-items: center; border-top: 1px solid #f0f0f0; padding-top: 15px; }
  
  .view-btn {
    background: transparent; border: 1px solid #0B2B5E; color: #0B2B5E;
    padding: 6px 15px; border-radius: 50px; font-size: 0.85rem; font-weight: 600; cursor: pointer; transition: 0.2s;
  }
  .view-btn:hover { background: #0B2B5E; color: white; }

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
    background: #0B2B5E; padding: 20px 25px; color: white; display: flex; justify-content: space-between; align-items: center;
    position: sticky; top: 0; z-index: 10;
  }
  .modal-title { margin: 0; font-size: 1.2rem; font-weight: 700; }
  .close-modal { background: none; border: none; color: white; font-size: 2rem; cursor: pointer; }
  
  .modal-body { padding: 25px; }

  .info-block { margin-bottom: 25px; }
  .info-head { font-size: 0.95rem; font-weight: 700; color: #0B2B5E; border-bottom: 2px solid #f0f0f0; padding-bottom: 5px; margin-bottom: 10px; display: flex; align-items: center; gap: 8px; }
  .info-content { font-size: 0.95rem; color: #444; line-height: 1.6; }
  
  .fee-table { width: 100%; border-collapse: collapse; margin-top: 10px; font-size: 0.9rem; background: #fdfdfd; }
  .fee-table td { padding: 10px; border-bottom: 1px solid #eee; }
  .fee-table td:first-child { font-weight: 600; color: #555; }
  .fee-table td:last-child { text-align: right; font-weight: bold; color: #0B2B5E; }

  @keyframes slideUp { from { transform: translateY(50px); opacity: 0; } to { transform: translateY(0); opacity: 1; } }

  /* Mobile */
  @media (max-width: 900px) {
    .app-container { flex-direction: column; }
    .filters-sidebar { width: 100%; position: static; }
  }
</style>

<div class="jgu-hero">
  <h1>O.P. Jindal Global University (Online)</h1>
  <p>Institution of Eminence & India's #1 Ranked Private University</p>
</div>

<div class="app-container">

  <aside class="filters-sidebar">
    <div class="filter-group">
      <label class="filter-label">🔍 Search Course</label>
      <input type="text" id="searchInput" class="filter-input" placeholder="e.g. Analytics, Public Policy..." onkeyup="renderCourses()">
    </div>
    
    <div class="filter-group">
      <label class="filter-label">🎓 Programme Level</label>
      <select id="levelFilter" class="filter-select" onchange="renderCourses()">
        <option value="All">All Levels</option>
        <option value="UG">Undergraduate (UG)</option>
        <option value="PG">Postgraduate (Masters)</option>
      </select>
    </div>

    <div class="filter-group">
      <label class="filter-label">🏫 Domain</label>
      <select id="deptFilter" class="filter-select" onchange="renderCourses()">
        <option value="All">All Domains</option>
        <option value="Business">Business & Management</option>
        <option value="Finance">Finance & Accounting</option>
        <option value="Public Policy">Public Policy & IR</option>
        <option value="Humanities">Humanities & Social Sciences</option>
        <option value="Science">Science & Technology</option>
        <option value="Education">Education</option>
        <option value="Design">Design & Innovation</option>
        <option value="Law">Law & Governance</option>
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
        <div class="info-head">💰 Fee Structure</div>
        <table class="fee-table" id="mFees"></table>
      </div>

      <div class="info-block">
        <div class="info-head">🚀 Career Outcomes</div>
        <div class="info-content" id="mCareers"></div>
      </div>
      
      <div style="text-align:center; margin-top:30px;">
        <a href="https://jguonline.edu.in/" target="_blank" style="background:#0B2B5E; color:white; padding:12px 30px; border-radius:50px; text-decoration:none; font-weight:bold;">Official Website ↗</a>
      </div>

    </div>
  </div>
</div>

<script>
  // --- 1. COURSE DATABASE ---
  const courses = [
    // --- UG PROGRAMS ---
    { 
      id: 1, name: "Online Bachelor of Business Administration (BBA)", level: "UG", dept: "Business",
      elig: "12th Std with 50% aggregate.", process: "JSAT / SAT / ACT / CUET or Profile Review.",
      fee: { "Total Tuition": "₹1,80,000 - ₹2,00,000" },
      desc: "A 3-year comprehensive online BBA offering 4 specializations: Finance, Marketing, HR, and Operations.", career: "Business Strategist, Marketing Lead, Operations Manager."
    },
    { 
      id: 2, name: "B.Sc. in Risk Management", level: "UG", dept: "Finance",
      elig: "12th Std with 50% (Maths/Stats/IT preferred).", process: "Application Screening + JSAT / SAT / ACT.",
      fee: { "Total Tuition": "₹3,00,000" },
      desc: "A 3-year globally recognized undergraduate program aligned with IRM's Enterprise Risk Management framework.", career: "Risk Analyst, Compliance Officer, Credit Risk Manager."
    },
    { 
      id: 3, name: "B.Com in International Accounting and Finance", level: "UG", dept: "Finance",
      elig: "12th Std with 50% aggregate in Commerce/Maths.", process: "Academic Transcript Review.",
      fee: { "Total Tuition": "₹2,50,000" },
      desc: "A globally focused B.Com designed for students aiming for international accounting standards and global finance roles.", career: "Financial Accountant, Auditor, Tax Consultant."
    },
    { 
      id: 4, name: "B.Sc. in Psychology (Blended)", level: "UG", dept: "Humanities",
      elig: "12th Std with 50% aggregate.", process: "Application Review & Interview.",
      fee: { "Total Tuition": "₹2,50,000" },
      desc: "A blended learning program focusing on cognitive, developmental, and clinical psychology fundamentals.", career: "Behavioral Analyst, HR Consultant, Mental Health Advocate."
    },

    // --- PG BUSINESS & MANAGEMENT ---
    { 
      id: 5, name: "Online MBA (7 Specializations)", level: "PG", dept: "Business",
      elig: "Bachelor's degree with minimum 50%.", process: "JMAT Exam OR valid CAT/MAT/GMAT + Profile Review.",
      fee: { "Total Tuition": "₹1,80,000" },
      desc: "A 1-year accelerated online MBA with specializations in Finance, Marketing, HR, AI for Business, and more. AACSB Accredited.", career: "Management Consultant, HR Manager, Brand Strategist."
    },
    { 
      id: 6, name: "MBA in Business Analytics", level: "PG", dept: "Business",
      elig: "Bachelor's degree with 50%.", process: "Transcript Review + SOP.",
      fee: { "Total Tuition": "₹1,65,000 - ₹2,00,000" },
      desc: "A data-driven MBA program focusing on tools like Python, Tableau, SQL, and Machine Learning.", career: "Business Analyst, Management Consultant, Data Strategist."
    },
    { 
      id: 7, name: "MBA in Business and Law", level: "PG", dept: "Business",
      elig: "Bachelor's degree with minimum 50%.", process: "Profile Review & SOP.",
      fee: { "Total Tuition": "₹2,00,000" },
      desc: "Bridges the gap between corporate management and legal compliance, tailored for future corporate leaders.", career: "Corporate Strategist, Compliance Director, Business Consultant."
    },
    { 
      id: 8, name: "M.Sc. in Family Business", level: "PG", dept: "Business",
      elig: "Bachelor's degree with 50%.", process: "Application Review.",
      fee: { "Total Tuition": "₹2,50,000" },
      desc: "Equips the next generation of family business leaders with modern management tools while preserving family legacies.", career: "Family Business Leader, Entrepreneur, Wealth Manager."
    },

    // --- PG FINANCE & ACCOUNTING ---
    { 
      id: 9, name: "M.Sc. in Global Risk Management", level: "PG", dept: "Finance",
      elig: "Undergraduate degree with 50%.", process: "SOP Review + JSAT/Interview.",
      fee: { "Total Tuition": "₹2,75,000" },
      desc: "Master risk analysis, financial modeling, and global regulatory frameworks over a flexible 12-month curriculum.", career: "Risk Manager, Fintech Consultant, Financial Operations Lead."
    },
    { 
      id: 10, name: "Master’s Degree in International Accounting and Finance (Integrated with ACCA)", level: "PG", dept: "Finance",
      elig: "Bachelor's degree in Commerce/Finance.", process: "Application Review.",
      fee: { "Total Tuition": "₹3,50,000" },
      desc: "An integrated master's program embedding ACCA professional level curriculum for global accounting careers.", career: "Global Auditor, Chief Financial Officer, International Tax Advisor."
    },
    { 
      id: 11, name: "Masters of Science in Artificial Intelligence Finance", level: "PG", dept: "Finance",
      elig: "Bachelor's degree with 50%.", process: "Profile Review & SOP.",
      fee: { "Total Tuition": "₹3,00,000" },
      desc: "Combines cutting-edge AI and machine learning techniques with complex financial modeling and quant analysis.", career: "Quant Analyst, Algorithmic Trader, Fintech Product Manager."
    },

    // --- PG PUBLIC POLICY & IR ---
    { 
      id: 12, name: "Master in Public Policy (M.A.)", level: "PG", dept: "Public Policy",
      elig: "Undergraduate degree in any discipline.", process: "SOP (800 words) + Profile Review.",
      fee: { "Total Tuition": "₹3,00,000" },
      desc: "A 1-year master's program hosted on Coursera. Features tracks in Data Analytics and Policy Design.", career: "Policy Analyst, Governance Consultant, NGO Leader."
    },
    { 
      id: 13, name: "M.A. in International Relations, Security and Strategy", level: "PG", dept: "Public Policy",
      elig: "Undergraduate degree in any discipline.", process: "Application Review + SOP.",
      fee: { "Total Tuition": "₹2,75,000" },
      desc: "Analyzes global geopolitics, national security challenges, and grand strategy in a multipolar world.", career: "Diplomat, Intelligence Analyst, Risk Consultant."
    },
    { 
      id: 14, name: "M.Sc. in Global Health and Human Development", level: "PG", dept: "Public Policy",
      elig: "Bachelor's degree with 50%.", process: "Application Review.",
      fee: { "Total Tuition": "₹2,50,000" },
      desc: "Explores the intersection of health policy, economics, and international development.", career: "Global Health Consultant, Policy Advisor, NGO Director."
    },
    { 
      id: 15, name: "M.Sc. in Development Studies", level: "PG", dept: "Public Policy",
      elig: "Undergraduate degree with 50%.", process: "Profile Review & Interview.",
      fee: { "Total Tuition": "₹2,50,000" },
      desc: "A multidisciplinary approach to understanding global inequalities, sustainable development, and poverty alleviation.", career: "Development Consultant, UN Policy Maker, Research Analyst."
    },
    { 
      id: 16, name: "M.A. in Electoral Analysis and Management", level: "PG", dept: "Public Policy",
      elig: "Undergraduate degree.", process: "Application Review.",
      fee: { "Total Tuition": "₹2,50,000" },
      desc: "Specialized training in psephology, election management, voting behavior, and campaign strategy.", career: "Political Strategist, Psephologist, Campaign Manager."
    },

    // --- PG HUMANITIES & SOCIAL SCIENCES ---
    { 
      id: 17, name: "M.A. in Political Communication", level: "PG", dept: "Humanities",
      elig: "Undergraduate degree in any discipline.", process: "Application Review + SOP.",
      fee: { "Total Tuition": "₹2,75,000" },
      desc: "Combines political science, journalism, and digital media to shape modern political narratives and campaigns.", career: "Political Strategist, Campaign Manager, Media Consultant."
    },
    { 
      id: 18, name: "M.A. in Museology & Cultural Heritage", level: "PG", dept: "Humanities",
      elig: "Bachelor's degree in any discipline.", process: "Application and SOP Review.",
      fee: { "Total Tuition": "₹2,50,000" },
      desc: "An interdisciplinary program connecting art, history, culture, and tech, including a hands-on Museum immersion.", career: "Museum Curator, Cultural Heritage Manager, Archival Specialist."
    },
    { 
      id: 19, name: "M.A. in India Studies", level: "PG", dept: "Humanities",
      elig: "Undergraduate degree.", process: "SOP Review.",
      fee: { "Total Tuition": "₹2,00,000" },
      desc: "An in-depth exploration of Indian history, culture, philosophy, and contemporary society.", career: "Cultural Consultant, Academic Researcher, Diplomatic Attaché."
    },
    { 
      id: 20, name: "M.A. in American Studies", level: "PG", dept: "Humanities",
      elig: "Undergraduate degree.", process: "Application Review.",
      fee: { "Total Tuition": "₹2,00,000" },
      desc: "Comprehensive study of US history, politics, literature, and its role in global affairs.", career: "Foreign Policy Analyst, International Educator, Researcher."
    },
    { 
      id: 21, name: "M.Sc. in Strategic Communications", level: "PG", dept: "Humanities",
      elig: "Undergraduate degree with 50%.", process: "Profile Review.",
      fee: { "Total Tuition": "₹2,50,000" },
      desc: "Focuses on corporate communications, PR, crisis management, and digital brand strategy.", career: "PR Director, Corporate Comm Lead, Media Strategist."
    },

    // --- PG EDUCATION ---
    { 
      id: 22, name: "M.A. in Teaching English to Speakers of Other Languages (TESOL)", level: "PG", dept: "Education",
      elig: "Undergraduate degree.", process: "Application Review.",
      fee: { "Total Tuition": "₹2,50,000" },
      desc: "Advanced pedagogical training for teaching English globally, focusing on linguistics and classroom methodology.", career: "ESL Instructor, Curriculum Developer, Educational Consultant."
    },
    { 
      id: 23, name: "M.A. in Educational Leadership & Governance", level: "PG", dept: "Education",
      elig: "Undergraduate degree.", process: "Application and SOP Review.",
      fee: { "Total Tuition": "₹2,50,000" },
      desc: "Prepares educators and administrators to lead schools, shape education policy, and manage academic institutions.", career: "School Principal, Education Policy Advisor, EdTech Leader."
    },

    // --- PG SCIENCE & TECHNOLOGY ---
    { 
      id: 24, name: "Master’s Degree in Artificial Intelligence and Data Science", level: "PG", dept: "Science",
      elig: "Undergraduate degree in STEM or related field.", process: "Technical Profile Review.",
      fee: { "Total Tuition": "₹3,00,000" },
      desc: "Deep dive into machine learning, neural networks, big data infrastructure, and ethical AI applications.", career: "AI Engineer, Data Scientist, ML Architect."
    },
    { 
      id: 25, name: "M.Sc. in Environmental Change & Sustainability", level: "PG", dept: "Science",
      elig: "Undergraduate degree.", process: "Profile Review & SOP.",
      fee: { "Total Tuition": "₹2,50,000" },
      desc: "Focuses on climate change mitigation, sustainable resource management, and corporate ESG (Environmental, Social, Governance) reporting.", career: "Sustainability Consultant, ESG Analyst, Environmental Policy Advisor."
    },

    // --- PG DESIGN & INNOVATION ---
    { 
      id: 26, name: "Master of Design in User Experience (UX)", level: "PG", dept: "Design",
      elig: "Undergraduate degree in any discipline.", process: "Portfolio Submission & Interview.",
      fee: { "Total Tuition": "₹3,50,000" },
      desc: "Human-centered design program covering UX research, interaction design, prototyping, and usability testing.", career: "UX Researcher, Lead Product Designer, UI/UX Specialist."
    },
    { 
      id: 27, name: "M.Sc. in Design Thinking and Innovation", level: "PG", dept: "Design",
      elig: "Undergraduate degree.", process: "Application Review.",
      fee: { "Total Tuition": "₹2,75,000" },
      desc: "Trains professionals to solve complex business and social problems using creative, empathetic design frameworks.", career: "Innovation Strategist, Product Manager, Design Consultant."
    },

    // --- PG LAW & GOVERNANCE ---
    { 
      id: 28, name: "Master Of Arts (M.A.) Legislative Drafting", level: "PG", dept: "Law",
      elig: "Undergraduate degree (Law preferred but not mandatory).", process: "Application & SOP.",
      fee: { "Total Tuition": "₹2,50,000" },
      desc: "A niche program teaching the technical skills required to draft clear, effective legislation and corporate policies.", career: "Legislative Drafter, Legal Policy Consultant, Parliamentary Advisor."
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
        let colorClass = 'level-' + course.level.split('_')[0];

        const card = `
          <div class="course-card ${colorClass}" style="animation-delay: ${count * 0.05}s">
            <div>
              <span class="c-school">${course.dept}</span>
              <h3 class="c-title">${course.name}</h3>
              <div class="c-meta">
                <span class="c-badge">${course.level.replace('_', ' ')} Online</span>
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
