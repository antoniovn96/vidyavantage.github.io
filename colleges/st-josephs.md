---
layout: default
title: "St. Joseph's University, Bengaluru 🎓"
permalink: /colleges/st-josephs/
image: "https://images.unsplash.com/photo-1562774053-701939374585?w=1200&h=630&fit=crop"
description: "Complete list of Undergraduate, PG, and Diploma courses at St. Joseph's University with batch timings, fees, and entrance exam details."
---

<style>
  /* 1. GLOBAL LAYOUT */
  .main-content { max-width: 100% !important; padding: 0 !important; margin: 0 !important; }
  body { background-color: #f4f7f6; font-family: 'Segoe UI', sans-serif; color: #333; }

  /* 2. HERO SECTION */
  .uni-hero {
    background: linear-gradient(rgba(10, 35, 66, 0.9), rgba(10, 35, 66, 0.7)), url('https://images.unsplash.com/photo-1541339907198-e08756dedf3f?w=1600&auto=format&fit=crop');
    background-size: cover;
    background-position: center;
    color: white;
    text-align: center;
    padding: 100px 20px;
    margin-bottom: 40px;
    box-shadow: 0 4px 20px rgba(0,0,0,0.1);
  }
  .uni-hero h1 { font-size: 3.5rem; margin: 0; color: white !important; font-weight: 800; text-shadow: 0 4px 15px rgba(0,0,0,0.5); }
  .uni-hero p { font-size: 1.3rem; color: #e0e0e0 !important; margin-top: 15px; font-weight: 500; }
  
  .visit-btn {
    display: inline-block; background: #D4AF37; color: #0A2342; padding: 12px 30px; 
    border-radius: 50px; text-decoration: none; font-weight: bold; margin-top: 25px; 
    transition: transform 0.2s; box-shadow: 0 4px 10px rgba(212, 175, 55, 0.4);
  }
  .visit-btn:hover { transform: translateY(-3px); color: #0A2342; }

  /* 3. TABS */
  .level-tabs { display: flex; justify-content: center; gap: 15px; margin-bottom: 40px; flex-wrap: wrap; padding: 0 20px; }
  .tab-btn {
    background: white; border: none; padding: 12px 30px; border-radius: 50px;
    font-weight: 700; color: #555; cursor: pointer; transition: all 0.3s;
    box-shadow: 0 4px 10px rgba(0,0,0,0.05);
  }
  .tab-btn.active { background: #0A2342; color: white; box-shadow: 0 5px 15px rgba(10, 35, 66, 0.3); }

  /* 4. COURSE CARDS GRID */
  .course-container { max-width: 1200px; margin: 0 auto; padding: 0 20px 60px; display: none; animation: fadeIn 0.5s; }
  .course-container.active { display: block; }
  
  .school-block {
    background: white; border-radius: 12px; box-shadow: 0 5px 20px rgba(0,0,0,0.05);
    margin-bottom: 30px; overflow: hidden; border-top: 5px solid #0A2342;
  }
  .school-header { background: #f8f9fa; padding: 20px 30px; border-bottom: 1px solid #eee; }
  .school-header h2 { margin: 0; color: #0A2342; font-size: 1.5rem; }

  .course-list { list-style: none; padding: 0; margin: 0; }
  .course-item {
    padding: 15px 30px; border-bottom: 1px solid #eee; display: flex; justify-content: space-between; align-items: center;
    font-size: 0.95rem; color: #444; transition: background 0.2s;
  }
  .course-item:last-child { border-bottom: none; }
  .course-item:hover { background: #fdfdfd; }
  
  .details-btn {
    background: #0A2342; color: white; border: none; padding: 6px 15px; 
    border-radius: 4px; cursor: pointer; font-size: 0.85rem; font-weight: 600;
  }
  .details-btn:hover { background: #D4AF37; color: #0A2342; }

  .badge-eligibility {
    display: inline-block; background: #e3f2fd; color: #1565c0; padding: 4px 8px;
    border-radius: 4px; font-size: 0.8rem; margin-right: 10px; font-weight: 600;
  }

  /* 5. MODAL STYLES */
  .modal-overlay {
    display: none; position: fixed; top: 0; left: 0; width: 100%; height: 100%;
    background: rgba(0,0,0,0.7); z-index: 2000; align-items: center; justify-content: center;
    backdrop-filter: blur(5px);
  }
  .modal-content {
    background: white; width: 95%; max-width: 650px; border-radius: 16px;
    position: relative; animation: slideUp 0.3s; overflow: hidden; display: flex; flex-direction: column;
    max-height: 90vh;
  }
  .modal-header { background: #0A2342; padding: 20px 30px; color: white; display: flex; justify-content: space-between; align-items: center; }
  .modal-header h2 { margin: 0; font-size: 1.3rem; }
  .close-btn { background: none; border: none; color: white; font-size: 2rem; cursor: pointer; }
  
  .modal-body { padding: 30px; overflow-y: auto; }
  
  .info-group { margin-bottom: 25px; border-bottom: 1px dashed #eee; padding-bottom: 15px; }
  .info-group:last-child { border-bottom: none; }
  .info-title { font-size: 1rem; font-weight: 800; color: #0A2342; margin-bottom: 8px; text-transform: uppercase; letter-spacing: 0.5px; display: flex; align-items: center; gap: 8px; }
  .info-text { color: #555; line-height: 1.6; font-size: 0.95rem; }
  
  /* Fee Table in Modal */
  .fee-table { width: 100%; border-collapse: collapse; margin-top: 10px; font-size: 0.9rem; }
  .fee-table td { padding: 8px; border-bottom: 1px solid #eee; }
  .fee-table td:first-child { font-weight: 600; color: #444; }
  .fee-table td:last-child { text-align: right; color: #0A2342; font-weight: bold; }

  @keyframes slideUp { from { transform: translateY(50px); opacity: 0; } to { transform: translateY(0); opacity: 1; } }

  /* Responsive */
  @media (max-width: 768px) {
    .uni-hero h1 { font-size: 2.2rem; }
    .course-item { flex-direction: column; align-items: flex-start; gap: 10px; }
  }
</style>

<div class="uni-hero">
  <h1>St. Joseph's University</h1>
  <p>Faith and Toil • Est. 1882</p>
  <a href="https://sju.edu.in" target="_blank" class="visit-btn">Visit Official Website ↗</a>
</div>

<div class="level-tabs">
  <button class="tab-btn active" onclick="openLevel('ug')">🎓 Undergraduate</button>
  <button class="tab-btn" onclick="openLevel('pg')">📜 Postgraduate</button>
  <button class="tab-btn" onclick="openLevel('diploma')">🛠️ PG Diploma</button>
</div>

<div id="ug" class="course-container active">

  <div class="school-block">
    <div class="school-header"><h2>School of Business</h2></div>
    <ul class="course-list">
      <li class="course-item">
        <span>Bachelor of Commerce (B.Com)</span>
        <div><span class="badge-eligibility">12th (Comm/Sci)</span> <button onclick="openDetails('bcom')" class="details-btn">Details</button></div>
      </li>
      <li class="course-item">
        <span>B.Com (Industry Integrated)</span>
        <div><span class="badge-eligibility">12th Pass</span> <button onclick="openDetails('bcom_ind')" class="details-btn">Details</button></div>
      </li>
      <li class="course-item">
        <span>B.Com (International Finance & Acc.)</span>
        <div><span class="badge-eligibility">12th Pass</span> <button onclick="openDetails('bcom_intl')" class="details-btn">Details</button></div>
      </li>
      <li class="course-item">
        <span>Bachelor of Business Admin (BBA)</span>
        <div><span class="badge-eligibility">12th Pass</span> <button onclick="openDetails('bba')" class="details-btn">Details</button></div>
      </li>
      <li class="course-item">
        <span>BBA (Strategic Finance)</span>
        <div><span class="badge-eligibility">12th Pass</span> <button onclick="openDetails('bba_strat')" class="details-btn">Details</button></div>
      </li>
      <li class="course-item">
        <span>BBA (Branding and Entrepreneurship)</span>
        <div><span class="badge-eligibility">12th Pass</span> <button onclick="openDetails('bba_brand')" class="details-btn">Details</button></div>
      </li>
    </ul>
  </div>

  <div class="school-block">
    <div class="school-header"><h2>School of Chemical Sciences</h2></div>
    <ul class="course-list">
      <li class="course-item"><span>B.Sc (Chemistry, Biotech, Biology)</span><div><span class="badge-eligibility">12th Science</span> <button onclick="openDetails('bsc_bio')" class="details-btn">Details</button></div></li>
      <li class="course-item"><span>B.Sc (Biochem, Micro, Zoology)</span><div><span class="badge-eligibility">12th Science</span> <button onclick="openDetails('bsc_bio')" class="details-btn">Details</button></div></li>
      <li class="course-item"><span>B.Sc (Chemistry, Botany, Zoology)</span><div><span class="badge-eligibility">12th Science</span> <button onclick="openDetails('bsc_bio')" class="details-btn">Details</button></div></li>
      <li class="course-item"><span>B.Sc (Chemistry, Env Science, Biology)</span><div><span class="badge-eligibility">12th Science</span> <button onclick="openDetails('bsc_bio')" class="details-btn">Details</button></div></li>
    </ul>
  </div>

  <div class="school-block">
    <div class="school-header"><h2>School of Humanities & Social Sciences</h2></div>
    <ul class="course-list">
      <li class="course-item"><span>B.A. (Economics, Pol Sci, Sociology)</span><div><span class="badge-eligibility">12th Pass</span> <button onclick="openDetails('ba_eps')" class="details-btn">Details</button></div></li>
      <li class="course-item"><span>B.A. (Industrial Relations, Econ, Soc)</span><div><span class="badge-eligibility">12th Pass</span> <button onclick="openDetails('ba_eps')" class="details-btn">Details</button></div></li>
      <li class="course-item"><span>B.A. (History, Pol Sci, Sociology)</span><div><span class="badge-eligibility">12th Pass</span> <button onclick="openDetails('ba_eps')" class="details-btn">Details</button></div></li>
      <li class="course-item"><span>B.A. (Journalism, Econ, Psych)</span><div><span class="badge-eligibility">12th Pass</span> <button onclick="openDetails('ba_eps')" class="details-btn">Details</button></div></li>
      <li class="course-item"><span>B.A. (Optional English, Journ, Psych)</span><div><span class="badge-eligibility">12th Pass</span> <button onclick="openDetails('ba_eps')" class="details-btn">Details</button></div></li>
    </ul>
  </div>

  <div class="school-block">
    <div class="school-header"><h2>School of Physical Sciences</h2></div>
    <ul class="course-list">
      <li class="course-item"><span>B.Sc (Physics, Maths, Comp Sci)</span><div><span class="badge-eligibility">12th PCM</span> <button onclick="openDetails('bsc_pmc')" class="details-btn">Details</button></div></li>
      <li class="course-item"><span>B.Sc (Economics, Maths, Stats)</span><div><span class="badge-eligibility">12th Maths</span> <button onclick="openDetails('bsc_ems')" class="details-btn">Details</button></div></li>
      <li class="course-item"><span>B.Sc (Physics, Chem, Maths)</span><div><span class="badge-eligibility">12th PCM</span> <button onclick="openDetails('bsc_pcm')" class="details-btn">Details</button></div></li>
      <li class="course-item"><span>B.Sc (Physics, Electronics, Maths)</span><div><span class="badge-eligibility">12th PCM</span> <button onclick="openDetails('bsc_pem')" class="details-btn">Details</button></div></li>
    </ul>
  </div>

  <div class="school-block">
    <div class="school-header"><h2>School of Communication & Media</h2></div>
    <ul class="course-list">
      <li class="course-item"><span>B.A. in Visual Communication</span><div><span class="badge-eligibility">12th Pass</span> <button onclick="openDetails('ba_viscom')" class="details-btn">Details</button></div></li>
      <li class="course-item"><span>B.Voc (Digital Media & Animation)</span><div><span class="badge-eligibility">12th Pass</span> <button onclick="openDetails('bvoc')" class="details-btn">Details</button></div></li>
      <li class="course-item"><span>B.Voc (Visual Media & Filmmaking)</span><div><span class="badge-eligibility">12th Pass</span> <button onclick="openDetails('bvoc')" class="details-btn">Details</button></div></li>
    </ul>
  </div>

  <div class="school-block">
    <div class="school-header"><h2>School of Information Technology</h2></div>
    <ul class="course-list">
      <li class="course-item"><span>Bachelor of Computer Applications (BCA)</span><div><span class="badge-eligibility">12th Maths/CS</span> <button onclick="openDetails('bca')" class="details-btn">Details</button></div></li>
      <li class="course-item"><span>BCA in Data Analytics</span><div><span class="badge-eligibility">12th Maths</span> <button onclick="openDetails('bca_data')" class="details-btn">Details</button></div></li>
    </ul>
  </div>

</div>

<div id="pg" class="course-container">

  <div class="school-block">
    <div class="school-header"><h2>School of Business</h2></div>
    <ul class="course-list">
      <li class="course-item"><span>Master of Commerce (M.Com)</span><div><span class="badge-eligibility">B.Com/BBA</span> <button onclick="openDetails('mcom')" class="details-btn">Details</button></div></li>
    </ul>
  </div>

  <div class="school-block">
    <div class="school-header"><h2>School of Information Technology</h2></div>
    <ul class="course-list">
      <li class="course-item"><span>Master of Computer Applications (MCA)</span><div><span class="badge-eligibility">BCA/B.Sc CS</span> <button onclick="openDetails('mca')" class="details-btn">Details</button></div></li>
      <li class="course-item"><span>M.Sc in Big Data Analytics</span><div><span class="badge-eligibility">B.Sc Maths/CS</span> <button onclick="openDetails('msc_data')" class="details-btn">Details</button></div></li>
    </ul>
  </div>

  <div class="school-block">
    <div class="school-header"><h2>School of Communication</h2></div>
    <ul class="course-list">
      <li class="course-item"><span>M.A. in Advertising and Public Relations</span><div><span class="badge-eligibility">Any Degree</span> <button onclick="openDetails('ma_comm')" class="details-btn">Details</button></div></li>
      <li class="course-item"><span>M.A. in Journalism and Mass Communication</span><div><span class="badge-eligibility">Any Degree</span> <button onclick="openDetails('ma_comm')" class="details-btn">Details</button></div></li>
    </ul>
  </div>

</div>

<div id="course-modal" class="modal-overlay" onclick="closeModal(event)">
  <div class="modal-content">
    <div class="modal-header">
      <h2 id="modal-title">Course Name</h2>
      <button class="close-btn" onclick="closeModalBtn()">&times;</button>
    </div>
    <div class="modal-body">
      
      <div class="info-group">
        <div class="info-title">📋 Eligibility</div>
        <div class="info-text" id="modal-eligibility"></div>
      </div>

      <div class="info-group">
        <div class="info-title">📚 Syllabus Overview</div>
        <div class="info-text" id="modal-syllabus"></div>
      </div>

      <div class="info-group">
        <div class="info-title">💰 Fee Structure (Approx/Year)</div>
        <table class="fee-table" id="modal-fees">
          </table>
      </div>

      <div class="info-group">
        <div class="info-title">🚀 Potential Career Outcomes</div>
        <div class="info-text" id="modal-careers"></div>
      </div>

    </div>
  </div>
</div>

<script>
  // --- 1. COURSE DATA REPOSITORY ---
  const courseData = {
    // BUSINESS
    'bcom': {
      title: "Bachelor of Commerce (B.Com)",
      eligibility: "Pass in Class 12 (10+2) or equivalent from a recognized board. Commerce or Science stream preferred.",
      syllabus: "Core subjects: Financial Accounting, Corporate Accounting, Business Law, Taxation, Auditing, and Cost Management.",
      fees: { "Karnataka": "₹1,05,000", "Non-Karnataka": "₹1,20,000", "NRI": "₹1,65,000" },
      careers: "Accountant, Financial Analyst, Tax Consultant, Banker, or higher studies like M.Com/MBA/CA."
    },
    'bcom_ind': {
      title: "B.Com (Industry Integrated)",
      eligibility: "Pass in Class 12 (10+2). Designed for students seeking immediate industry placement.",
      syllabus: "Integrated with BPM (Business Process Management) concepts from TCS. Practical approach to commerce.",
      fees: { "Karnataka": "₹1,05,000", "Non-Karnataka": "₹1,20,000", "NRI": "₹1,65,000" },
      careers: "Process Analyst, Operations Executive in MNCs, Corporate Finance roles."
    },
    'bcom_intl': {
      title: "B.Com (International Finance & Accounting)",
      eligibility: "Pass in Class 12 (10+2). High aptitude for Accounting required.",
      syllabus: "Accredited by ACCA (UK). Covers International Financial Reporting, Audit & Assurance, and Performance Management.",
      fees: { "Karnataka": "₹1,90,000", "Non-Karnataka": "₹2,10,000", "NRI": "₹2,50,000" },
      careers: "ACCA Certified Professional, Global Auditor, International Financial Consultant."
    },
    'bba': {
      title: "Bachelor of Business Administration (BBA)",
      eligibility: "Pass in Class 12 (10+2) from any stream. Minimum 50% aggregate suggested.",
      syllabus: "Management Principles, Marketing Management, HRM, Organizational Behavior, Business Analytics basics.",
      fees: { "Karnataka": "₹1,40,000", "Non-Karnataka": "₹1,60,000", "NRI": "₹2,10,000" },
      careers: "HR Executive, Marketing Associate, Business Development Manager, Entrepreneur."
    },
    'bba_strat': {
      title: "BBA (Strategic Finance)",
      eligibility: "Pass in Class 12 (10+2). Integrated with CMA (USA) curriculum.",
      syllabus: "US CMA aligned: Financial Planning, Performance & Analytics, Strategic Financial Management.",
      fees: { "Karnataka": "₹2,00,000", "Non-Karnataka": "₹2,25,000", "NRI": "₹2,60,000" },
      careers: "Management Accountant, Financial Strategist, Corporate Controller."
    },
    'bba_brand': {
      title: "BBA (Branding and Entrepreneurship)",
      eligibility: "Pass in Class 12 (10+2). Ideal for students with family business background or startup ideas.",
      syllabus: "Brand Management, Digital Marketing, Venture Creation, Family Business Dynamics, Innovation.",
      fees: { "Karnataka": "₹1,90,000", "Non-Karnataka": "₹2,10,000", "NRI": "₹2,50,000" },
      careers: "Brand Manager, Entrepreneur, Digital Marketing Strategist, Product Manager."
    },

    // IT
    'bca': {
      title: "Bachelor of Computer Applications (BCA)",
      eligibility: "Pass in Class 12. Mathematics/Computer Science/Electronics/Stats background is mandatory.",
      syllabus: "C++, Java, Python, Web Dev, DBMS, Software Engineering, Cloud Computing.",
      fees: { "Karnataka": "₹1,15,000", "Non-Karnataka": "₹1,35,000", "NRI": "₹1,85,000" },
      careers: "Software Developer, Web Developer, System Analyst, IT Support."
    },
    'bca_data': {
      title: "BCA (Data Analytics)",
      eligibility: "Pass in Class 12 with Mathematics or Statistics. Strong analytical bent of mind.",
      syllabus: "Data Structures, R Programming, Big Data basics, Machine Learning concepts, Visualization tools.",
      fees: { "Karnataka": "₹1,50,000", "Non-Karnataka": "₹1,65,000", "NRI": "₹2,10,000" },
      careers: "Data Analyst, Junior Data Scientist, Business Intelligence Analyst."
    },

    // SCIENCE
    'bsc_pmc': {
      title: "B.Sc (Physics, Mathematics, Computer Science)",
      eligibility: "Pass in Class 12 Science (PCM).",
      syllabus: "Classical Mechanics, Calculus, Programming in C/Python, Data Structures, Quantum Physics basics.",
      fees: { "Karnataka": "₹90,000", "Non-Karnataka": "₹1,05,000", "NRI": "₹1,50,000" },
      careers: "Software Engineer, Research Assistant, Technical Analyst, Teacher."
    },
    'bsc_pcm': {
      title: "B.Sc (Physics, Chemistry, Mathematics)",
      eligibility: "Pass in Class 12 Science (PCM).",
      syllabus: "Thermodynamics, Organic/Inorganic Chemistry, Calculus, Algebra, Optics.",
      fees: { "Karnataka": "₹50,000", "Non-Karnataka": "₹56,000", "NRI": "₹1,10,000" },
      careers: "Lab Technician, Researcher, Lecturer, Govt Jobs (Scientific)."
    },
    'bsc_bio': {
      title: "B.Sc Life Sciences (General)",
      eligibility: "Pass in Class 12 Science (Biology required).",
      syllabus: "Microbiology, Genetics, Plant Physiology, Animal Diversity, Biochemistry.",
      fees: { "Karnataka": "₹55,000", "Non-Karnataka": "₹65,000", "NRI": "₹1,10,000" },
      careers: "Lab Technician, Clinical Researcher, Pharma Industry, Conservationist."
    },
    'bsc_ems': {
      title: "B.Sc (Economics, Mathematics, Statistics)",
      eligibility: "Pass in Class 12 with Mathematics.",
      syllabus: "Micro/Macro Economics, Econometrics, Probability Theory, Calculus, Statistical Methods.",
      fees: { "Karnataka": "₹90,000", "Non-Karnataka": "₹1,05,000", "NRI": "₹1,50,000" },
      careers: "Actuary, Economic Analyst, Statistician, Data Analyst."
    },

    // HUMANITIES / ARTS / MEDIA
    'ba_eps': {
      title: "B.A. (Economics, Political Science, Sociology)",
      eligibility: "Pass in Class 12 (Any stream).",
      syllabus: "Indian Economy, Political Theory, Social Structures, Public Administration.",
      fees: { "Karnataka": "₹42,000", "Non-Karnataka": "₹47,000", "NRI": "₹1,02,000" },
      careers: "Civil Services (UPSC), NGO Sector, Policy Analyst, Journalism."
    },
    'ba_viscom': {
      title: "B.A. Visual Communication",
      eligibility: "Pass in Class 12 (Any stream). Creative portfolio/Entrance test required.",
      syllabus: "Graphic Design, Photography, Videography, Media Laws, Animation basics.",
      fees: { "Karnataka": "₹1,30,000", "Non-Karnataka": "₹1,45,000", "NRI": "₹1,90,000" },
      careers: "Graphic Designer, Photographer, Film Editor, Advertising Professional."
    },
    'bvoc': {
      title: "B.Voc (Digital Media / Filmmaking)",
      eligibility: "Pass in Class 12. Skill-based admission.",
      syllabus: "Practical training in Camera, Lighting, Editing Suites, Sound Design, VFX.",
      fees: { "Karnataka": "₹1,10,000", "Non-Karnataka": "₹1,25,000", "NRI": "₹1,70,000" },
      careers: "Cinematographer, Video Editor, Animator, Media Production."
    },

    // PG
    'mcom': {
      title: "Master of Commerce (M.Com)",
      eligibility: "B.Com/BBA with min 50%.",
      syllabus: "Advanced Financial Management, Forex, Risk Management, Corporate Governance.",
      fees: { "Karnataka": "₹1,10,000", "Non-Karnataka": "₹1,25,000", "NRI": "₹1,70,000" },
      careers: "Senior Accountant, Finance Manager, Lecturer, Auditor."
    },
    'mca': {
      title: "Master of Computer Applications (MCA)",
      eligibility: "BCA/B.Sc CS with 50% + Maths at 10+2 level. Entrance Test (PGCET/KMAT) required.",
      syllabus: "Advanced Java, Python, AI/ML, Cloud Computing, Full Stack Dev.",
      fees: { "Karnataka": "₹1,75,000", "Non-Karnataka": "₹1,95,000", "NRI": "₹2,35,000" },
      careers: "Software Engineer, System Architect, Data Engineer."
    },
    'msc_data': {
      title: "M.Sc Big Data Analytics",
      eligibility: "Graduation with Maths/Stats/CS (50%). Entrance Test required.",
      syllabus: "Hadoop, Spark, Predictive Analytics, Neural Networks, NoSQL Databases.",
      fees: { "Karnataka": "₹1,75,000", "Non-Karnataka": "₹1,95,000", "NRI": "₹2,35,000" },
      careers: "Big Data Engineer, Machine Learning Specialist, Data Scientist."
    },
    'ma_comm': {
      title: "M.A. Journalism / Advertising",
      eligibility: "Graduation in any discipline (50%). Entrance test + Portfolio.",
      syllabus: "Media Research, PR Strategies, Corporate Comm, Digital Journalism.",
      fees: { "Karnataka": "₹1,40,000", "Non-Karnataka": "₹1,55,000", "NRI": "₹2,00,000" },
      careers: "PR Manager, Journalist, Content Strategist, Corp Comm Lead."
    }
  };

  // --- 2. OPEN TAB LOGIC ---
  function openLevel(levelId) {
    document.querySelectorAll('.course-container').forEach(el => el.classList.remove('active'));
    document.querySelectorAll('.tab-btn').forEach(btn => btn.classList.remove('active'));
    document.getElementById(levelId).classList.add('active');
    event.currentTarget.classList.add('active');
  }

  // --- 3. MODAL LOGIC ---
  function openDetails(courseKey) {
    const data = courseData[courseKey];
    if (!data) return; // Safety check

    // Populate Modal
    document.getElementById('modal-title').innerText = data.title;
    document.getElementById('modal-eligibility').innerText = data.eligibility;
    document.getElementById('modal-syllabus').innerText = data.syllabus;
    document.getElementById('modal-careers').innerText = data.careers;

    // Populate Fees
    const feeTable = document.getElementById('modal-fees');
    feeTable.innerHTML = ''; // Clear previous
    for (const [category, amount] of Object.entries(data.fees)) {
      const row = `<tr><td>${category}</td><td>${amount}</td></tr>`;
      feeTable.innerHTML += row;
    }

    // Show Modal
    document.getElementById('course-modal').style.display = 'flex';
  }

  function closeModalBtn() {
    document.getElementById('course-modal').style.display = 'none';
  }

  function closeModal(e) {
    if(e.target.className === 'modal-overlay') {
      document.getElementById('course-modal').style.display = 'none';
    }
  }
</script>
