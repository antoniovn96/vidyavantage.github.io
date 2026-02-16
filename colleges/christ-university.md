---
layout: default
title: "Christ (Deemed to be University) 🎓"
permalink: /colleges/christ-university/
image: "https://christuniversity.in/images/sharingLogo.jpg"
description: "Explore Undergraduate, Postgraduate, and PhD programmes at Christ University. Check eligibility, entrance exams, and selection process."
---

<style>
  /* 1. LAYOUT RESET */
  .main-content { max-width: 100% !important; padding: 0 !important; margin: 0 !important; }
  body { background-color: #f0f2f5; font-family: 'Segoe UI', sans-serif; color: #333; }

  /* 2. HERO SECTION */
  .uni-hero {
    background: linear-gradient(rgba(10, 35, 66, 0.9), rgba(10, 35, 66, 0.7)), url('https://images.unsplash.com/photo-1523050854058-8df90110c9f1?w=1600&auto=format&fit=crop');
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
    transition: transform 0.2s, box-shadow 0.2s; box-shadow: 0 4px 10px rgba(212, 175, 55, 0.4);
  }
  .visit-btn:hover { transform: translateY(-3px); color: #0A2342; box-shadow: 0 6px 15px rgba(212, 175, 55, 0.6); }

  /* 3. TABS */
  .level-tabs { display: flex; justify-content: center; gap: 15px; margin-bottom: 40px; flex-wrap: wrap; padding: 0 20px; }
  .tab-btn {
    background: white; border: none; padding: 12px 30px; border-radius: 50px;
    font-weight: 700; color: #555; cursor: pointer; transition: all 0.3s;
    box-shadow: 0 4px 10px rgba(0,0,0,0.05);
  }
  .tab-btn:hover { transform: translateY(-2px); }
  .tab-btn.active { background: #0A2342; color: white; box-shadow: 0 5px 15px rgba(10, 35, 66, 0.3); }

  /* 4. COURSE GRID (THE NEW DESIGN) */
  .course-container { max-width: 1200px; margin: 0 auto; padding: 0 20px 60px; display: none; animation: fadeIn 0.5s; }
  .course-container.active { display: block; }
  
  .course-grid {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(350px, 1fr));
    gap: 30px;
  }

  .course-card {
    background: white; border-radius: 15px; overflow: hidden;
    box-shadow: 0 10px 25px rgba(0,0,0,0.05); transition: transform 0.3s, box-shadow 0.3s;
    display: flex; flex-direction: column; border-top: 5px solid #0A2342;
  }
  .course-card:hover { transform: translateY(-5px); box-shadow: 0 15px 35px rgba(0,0,0,0.1); }

  .card-body { padding: 25px; flex-grow: 1; }
  .card-title { font-size: 1.4rem; font-weight: 700; color: #0A2342; margin: 0 0 10px 0; line-height: 1.3; }
  .card-meta { font-size: 0.9rem; color: #666; margin-bottom: 15px; display: flex; flex-wrap: wrap; gap: 10px; }
  .meta-tag { background: #f0f4f8; padding: 4px 10px; border-radius: 4px; font-weight: 600; color: #555; font-size: 0.8rem; }
  
  .deadline-box { 
    background: #fff3e0; color: #e65100; padding: 10px; border-radius: 8px; 
    font-size: 0.9rem; font-weight: bold; margin-bottom: 20px; display: flex; align-items: center; gap: 8px;
  }

  .card-footer {
    padding: 20px; border-top: 1px solid #eee; background: #fafafa;
    display: flex; justify-content: space-between; align-items: center;
  }
  
  .details-btn {
    background: transparent; border: 2px solid #0A2342; color: #0A2342; 
    padding: 8px 20px; border-radius: 50px; font-weight: bold; cursor: pointer; transition: all 0.2s;
  }
  .details-btn:hover { background: #0A2342; color: white; }

  /* 5. MODAL STYLES */
  .modal-overlay {
    display: none; position: fixed; top: 0; left: 0; width: 100%; height: 100%;
    background: rgba(0,0,0,0.7); z-index: 2000; align-items: center; justify-content: center;
    backdrop-filter: blur(5px);
  }
  .modal-content {
    background: white; width: 95%; max-width: 700px; border-radius: 16px;
    position: relative; animation: slideUp 0.3s; overflow: hidden; display: flex; flex-direction: column;
    max-height: 90vh;
  }
  .modal-header { background: #0A2342; padding: 20px 30px; color: white; display: flex; justify-content: space-between; align-items: center; }
  .modal-header h2 { margin: 0; font-size: 1.5rem; }
  .close-btn { background: none; border: none; color: white; font-size: 2rem; cursor: pointer; }
  
  .modal-body { padding: 30px; overflow-y: auto; }
  
  .info-group { margin-bottom: 25px; }
  .info-title { font-size: 1.1rem; font-weight: 800; color: #0A2342; margin-bottom: 10px; display: flex; align-items: center; gap: 8px; }
  .info-text { color: #555; line-height: 1.6; font-size: 1rem; }

  @keyframes slideUp { from { transform: translateY(50px); opacity: 0; } to { transform: translateY(0); opacity: 1; } }
  @keyframes fadeIn { from { opacity: 0; } to { opacity: 1; } }

  /* Responsive */
  @media (max-width: 768px) {
    .uni-hero h1 { font-size: 2.2rem; }
    .course-grid { grid-template-columns: 1fr; }
  }
</style>

<div class="uni-hero">
  <h1>Christ (Deemed to be University)</h1>
  <p>Excellence and Service • Est. 1969</p>
  <a href="https://christuniversity.in" target="_blank" class="visit-btn">Visit Official Website ↗</a>
</div>

<div class="level-tabs">
  <button class="tab-btn active" onclick="openLevel('ug')">🎓 Undergraduate</button>
  <button class="tab-btn" onclick="openLevel('pg')">📜 Postgraduate</button>
  <button class="tab-btn" onclick="openLevel('phd')">🔬 PhD & Research</button>
</div>

<div id="ug" class="course-container active">
  <div class="course-grid">

    <div class="course-card">
      <div class="card-body">
        <h3 class="card-title">Bachelor of Business Administration (BBA)</h3>
        <div class="card-meta">
          <span class="meta-tag">📍 Central / BRC / Kengeri</span>
          <span class="meta-tag">⚡ Honours Available</span>
        </div>
        <div class="deadline-box">
          📅 Application Closes: 30 Mar 2026
        </div>
        <p style="color:#666; font-size:0.95rem;">One of the top-ranked BBA programs in India. Focuses on holistic management, leadership, and soft skills.</p>
      </div>
      <div class="card-footer">
        <span style="font-weight:bold; color:#2e7d32;">✅ Entrance Required</span>
        <button onclick="openModal('bba-modal')" class="details-btn">View Details</button>
      </div>
    </div>

    <div class="course-card">
      <div class="card-body">
        <h3 class="card-title">B.Com (International Finance)</h3>
        <div class="card-meta">
          <span class="meta-tag">📍 Central Campus</span>
          <span class="meta-tag">⚡ Integrated with CPA</span>
        </div>
        <div class="deadline-box">
          📅 Application Closes: 30 Mar 2026
        </div>
        <p style="color:#666; font-size:0.95rem;">Designed for students aiming for global finance careers. Integrated with US CPA / ACCA curriculum.</p>
      </div>
      <div class="card-footer">
        <span style="font-weight:bold; color:#2e7d32;">✅ Entrance Required</span>
        <button onclick="openModal('bcom-if-modal')" class="details-btn">View Details</button>
      </div>
    </div>

    <div class="course-card">
      <div class="card-body">
        <h3 class="card-title">BA (Psychology, Economics)</h3>
        <div class="card-meta">
          <span class="meta-tag">📍 Central Campus</span>
          <span class="meta-tag">⚡ Dual Major</span>
        </div>
        <div class="deadline-box">
          📅 Application Closes: 05 Apr 2026
        </div>
        <p style="color:#666; font-size:0.95rem;">A rigorous double-major program blending human behavior analysis with economic theory.</p>
      </div>
      <div class="card-footer">
        <span style="font-weight:bold; color:#2e7d32;">✅ Entrance Required</span>
        <button onclick="openModal('ba-psych-modal')" class="details-btn">View Details</button>
      </div>
    </div>

    <div class="course-card">
      <div class="card-body">
        <h3 class="card-title">Bachelor of Computer Applications (BCA)</h3>
        <div class="card-meta">
          <span class="meta-tag">📍 Central Campus</span>
          <span class="meta-tag">⚡ Tech & Code</span>
        </div>
        <div class="deadline-box">
          📅 Application Closes: 30 Mar 2026
        </div>
        <p style="color:#666; font-size:0.95rem;">Best for non-engineering students wanting a career in Software Development, Cloud, and AI.</p>
      </div>
      <div class="card-footer">
        <span style="font-weight:bold; color:#2e7d32;">✅ Entrance Required</span>
        <button onclick="openModal('bca-modal')" class="details-btn">View Details</button>
      </div>
    </div>
    
    <div class="course-card">
      <div class="card-body">
        <h3 class="card-title">BA LLB / BBA LLB (Honours)</h3>
        <div class="card-meta">
          <span class="meta-tag">📍 Central Campus</span>
          <span class="meta-tag">⚡ 5 Years Integrated</span>
        </div>
        <div class="deadline-box">
          📅 Application Closes: 30 Mar 2026
        </div>
        <p style="color:#666; font-size:0.95rem;">Premier legal education with moot court training. Choice between Humanities-Law or Management-Law.</p>
      </div>
      <div class="card-footer">
        <span style="font-weight:bold; color:#2e7d32;">✅ Entrance Required</span>
        <button onclick="openModal('law-modal')" class="details-btn">View Details</button>
      </div>
    </div>

  </div>
</div>

<div id="pg" class="course-container">
  <div class="course-grid">
    
    <div class="course-card">
      <div class="card-body">
        <h3 class="card-title">MBA (Master of Business Admin)</h3>
        <div class="card-meta">
          <span class="meta-tag">📍 Central / Kengeri</span>
          <span class="meta-tag">⚡ Flagship Program</span>
        </div>
        <div class="deadline-box">
          📅 Application Closes: 22 Mar 2026
        </div>
        <p style="color:#666; font-size:0.95rem;">Specializations in Finance, Marketing, HR, and Business Analytics. High placement record.</p>
      </div>
      <div class="card-footer">
        <span style="font-weight:bold; color:#e65100;">⚠️ CAT/MAT + GD/PI</span>
        <button onclick="openModal('mba-modal')" class="details-btn">View Details</button>
      </div>
    </div>

    <div class="course-card">
      <div class="card-body">
        <h3 class="card-title">M.Sc Clinical Psychology</h3>
        <div class="card-meta">
          <span class="meta-tag">📍 Central Campus</span>
          <span class="meta-tag">⚡ High Demand</span>
        </div>
        <div class="deadline-box">
          📅 Application Closes: 22 Mar 2026
        </div>
        <p style="color:#666; font-size:0.95rem;">Rigorous training in clinical assessment and therapy. Includes field work and hospital internships.</p>
      </div>
      <div class="card-footer">
        <span style="font-weight:bold; color:#2e7d32;">✅ Entrance Required</span>
        <button onclick="openModal('msc-psych-modal')" class="details-btn">View Details</button>
      </div>
    </div>

  </div>
</div>

<div id="bba-modal" class="modal-overlay" onclick="closeModal(event, 'bba-modal')">
  <div class="modal-content">
    <div class="modal-header">
      <h2>BBA (Honours)</h2>
      <button class="close-btn" onclick="document.getElementById('bba-modal').style.display='none'">&times;</button>
    </div>
    <div class="modal-body">
      <div class="info-group">
        <div class="info-title">📋 Eligibility</div>
        <div class="info-text">
          Pass in Class 12 (10+2) from any recognized board (Karnataka PUC / ISC / CBSE / State Boards) with a minimum of <strong>55% aggregate</strong>. Students from any stream (Science/Commerce/Arts) can apply.
        </div>
      </div>
      <div class="info-group">
        <div class="info-title">🎯 Selection Process</div>
        <div class="info-text">
          1. <strong>Christ University Entrance Test (CUET):</strong> Tests English, Logic, Data Analysis, and GK.<br>
          2. <strong>Micro Presentation (MP):</strong> Speak for 90 seconds on a given topic.<br>
          3. <strong>Personal Interview (PI):</strong> Assess communication and confidence.
        </div>
      </div>
      <div class="info-group">
        <div class="info-title">💰 Fee Structure (Approx)</div>
        <div class="info-text">
          • Karnataka Students: ₹1,65,000 / Year<br>
          • Other States: ₹1,90,000 / Year<br>
          • NRI: ₹2,40,000 / Year
        </div>
      </div>
    </div>
  </div>
</div>

<div id="bcom-if-modal" class="modal-overlay" onclick="closeModal(event, 'bcom-if-modal')">
  <div class="modal-content">
    <div class="modal-header">
      <h2>B.Com (International Finance)</h2>
      <button class="close-btn" onclick="document.getElementById('bcom-if-modal').style.display='none'">&times;</button>
    </div>
    <div class="modal-body">
      <div class="info-group">
        <div class="info-title">📋 Eligibility</div>
        <div class="info-text">
          Pass in Class 12 (10+2) with minimum <strong>60% aggregate</strong>. Accountancy and Mathematics background is preferred but not strictly mandatory if the student has high aptitude.
        </div>
      </div>
      <div class="info-group">
        <div class="info-title">🎯 Selection Process</div>
        <div class="info-text">
          1. <strong>CUET:</strong> Emphasis on Accountancy, Math, and Reasoning.<br>
          2. <strong>Micro Presentation & Interview:</strong> Focus on global finance awareness.
        </div>
      </div>
    </div>
  </div>
</div>

<div id="bca-modal" class="modal-overlay" onclick="closeModal(event, 'bca-modal')">
  <div class="modal-content">
    <div class="modal-header">
      <h2>Bachelor of Computer Applications</h2>
      <button class="close-btn" onclick="document.getElementById('bca-modal').style.display='none'">&times;</button>
    </div>
    <div class="modal-body">
      <div class="info-group">
        <div class="info-title">📋 Eligibility</div>
        <div class="info-text">
          Pass in Class 12. <strong>Maths / Computer Science / Electronics / Statistics</strong> as one of the subjects is mandatory. Non-math students may struggle or not be eligible.
        </div>
      </div>
    </div>
  </div>
</div>

<div id="mba-modal" class="modal-overlay" onclick="closeModal(event, 'mba-modal')">
  <div class="modal-content">
    <div class="modal-header">
      <h2>MBA (Master of Business Admin)</h2>
      <button class="close-btn" onclick="document.getElementById('mba-modal').style.display='none'">&times;</button>
    </div>
    <div class="modal-body">
      <div class="info-group">
        <div class="info-title">📋 Eligibility</div>
        <div class="info-text">
          50% or above marks in aggregate in the undergraduate examinations. Valid score in MAT / CAT / CMAT / XAT / GMAT / GRE / ATMA.
        </div>
      </div>
      <div class="info-group">
        <div class="info-title">🎯 Selection Process</div>
        <div class="info-text">
          1. <strong>Score Card Verification</strong><br>
          2. <strong>Group Discussion (GD)</strong><br>
          3. <strong>Micro Presentation & PI</strong>
        </div>
      </div>
    </div>
  </div>
</div>

<script>
  // Tab Logic
  function openLevel(levelId) {
    document.querySelectorAll('.course-container').forEach(el => el.classList.remove('active'));
    document.querySelectorAll('.tab-btn').forEach(btn => btn.classList.remove('active'));
    document.getElementById(levelId).classList.add('active');
    event.currentTarget.classList.add('active');
  }

  // Modal Logic
  function openModal(id) { document.getElementById(id).style.display = 'flex'; }
  function closeModal(e, id) { if(e.target.className === 'modal-overlay') document.getElementById(id).style.display = 'none'; }
</script>
