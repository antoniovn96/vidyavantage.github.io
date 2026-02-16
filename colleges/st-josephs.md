---
layout: default
title: "St. Joseph's University, Bengaluru 🎓"
permalink: /colleges/st-josephs/
image: "https://images.unsplash.com/photo-1562774053-701939374585?w=1200&h=630&fit=crop"
description: "Explore Undergraduate, PG, and Diploma courses at St. Joseph's University. Check batch timings (Morning/Evening), fees, and entrance exams."
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
  
  .course-grid {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(350px, 1fr));
    gap: 30px;
  }

  .course-card {
    background: white; border-radius: 15px; overflow: hidden;
    box-shadow: 0 10px 25px rgba(0,0,0,0.05); transition: transform 0.3s;
    display: flex; flex-direction: column; border-top: 5px solid #0A2342;
  }
  .course-card:hover { transform: translateY(-5px); box-shadow: 0 15px 35px rgba(0,0,0,0.1); }

  .card-body { padding: 25px; flex-grow: 1; }
  .school-label { font-size: 0.8rem; color: #888; text-transform: uppercase; letter-spacing: 1px; font-weight: bold; margin-bottom: 5px; display: block;}
  .card-title { font-size: 1.3rem; font-weight: 700; color: #0A2342; margin: 0 0 15px 0; line-height: 1.3; }
  
  /* Batch Timing Badges */
  .batch-badge { 
    display: inline-flex; align-items: center; gap: 5px;
    background: #f0f4f8; padding: 6px 12px; border-radius: 6px; 
    font-size: 0.85rem; font-weight: 600; color: #555; margin-bottom: 8px; width: 100%;
  }
  .batch-icon { font-size: 1rem; }

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
    background: white; width: 95%; max-width: 600px; border-radius: 16px;
    position: relative; animation: slideUp 0.3s; overflow: hidden; display: flex; flex-direction: column;
    max-height: 90vh;
  }
  .modal-header { background: #0A2342; padding: 20px 30px; color: white; display: flex; justify-content: space-between; align-items: center; }
  .modal-header h2 { margin: 0; font-size: 1.3rem; }
  .close-btn { background: none; border: none; color: white; font-size: 2rem; cursor: pointer; }
  
  .modal-body { padding: 30px; overflow-y: auto; }
  
  .info-group { margin-bottom: 25px; }
  .info-title { font-size: 1rem; font-weight: 800; color: #0A2342; margin-bottom: 8px; text-transform: uppercase; letter-spacing: 0.5px; }
  .info-text { color: #555; line-height: 1.6; font-size: 0.95rem; }

  @keyframes slideUp { from { transform: translateY(50px); opacity: 0; } to { transform: translateY(0); opacity: 1; } }
  @keyframes fadeIn { from { opacity: 0; } to { opacity: 1; } }

  /* Responsive */
  @media (max-width: 768px) {
    .uni-hero h1 { font-size: 2.2rem; }
    .course-grid { grid-template-columns: 1fr; }
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
  <div class="course-grid">

    <div class="course-card">
      <div class="card-body">
        <span class="school-label">School of Business</span>
        <h3 class="card-title">Bachelor of Commerce (B.Com)</h3>
        <div class="batch-badge">☀️ Batch 1: 7am - 12pm</div>
        <div class="batch-badge">🌤️ Batch 2: 12pm - 4pm</div>
        <div class="batch-badge">🌇 Batch 3: 4:45pm - 8:45pm</div>
        <p style="margin-top:15px; color:#666; font-size:0.9rem;">Core commerce education focusing on Accounting, Finance, and Taxation.</p>
      </div>
      <div class="card-footer">
        <span style="font-weight:bold; color:#2e7d32;">✅ Merit Based</span>
        <button onclick="openModal('bcom-modal')" class="details-btn">View Details</button>
      </div>
    </div>

    <div class="course-card">
      <div class="card-body">
        <span class="school-label">School of Business</span>
        <h3 class="card-title">Bachelor of Business Admin (BBA)</h3>
        <div class="batch-badge">☀️ Batch 1: 7am - 12pm</div>
        <div class="batch-badge">🌇 Batch 2: 4:45pm - 8:45pm</div>
        <p style="margin-top:15px; color:#666; font-size:0.9rem;">Foundational management course covering Marketing, HR, and Operations.</p>
      </div>
      <div class="card-footer">
        <span style="font-weight:bold; color:#2e7d32;">✅ Merit Based</span>
        <button onclick="openModal('bba-modal')" class="details-btn">View Details</button>
      </div>
    </div>

    <div class="course-card">
      <div class="card-body">
        <span class="school-label">School of IT</span>
        <h3 class="card-title">Bachelor of Computer Applications (BCA)</h3>
        <div class="batch-badge">☀️ Batch 1: 9am - 4pm</div>
        <div class="batch-badge">🌇 Batch 2: 4pm - 9pm</div>
        <p style="margin-top:15px; color:#666; font-size:0.9rem;">Practical software development, programming, and database management.</p>
      </div>
      <div class="card-footer">
        <span style="font-weight:bold; color:#2e7d32;">✅ Merit Based</span>
        <button onclick="openModal('bca-modal')" class="details-btn">View Details</button>
      </div>
    </div>

    <div class="course-card">
      <div class="card-body">
        <span class="school-label">School of Communication</span>
        <h3 class="card-title">B.A. Visual Communication</h3>
        <div class="batch-badge">☀️ 7am - 1pm</div>
        <p style="margin-top:15px; color:#666; font-size:0.9rem;">Design, Photography, and Media studies. Requires portfolio/test.</p>
      </div>
      <div class="card-footer">
        <span style="font-weight:bold; color:#e65100;">⚠️ Entrance Test</span>
        <button onclick="openModal('viscom-modal')" class="details-btn">View Details</button>
      </div>
    </div>

    <div class="course-card">
      <div class="card-body">
        <span class="school-label">School of Sciences</span>
        <h3 class="card-title">B.Sc (PCM / CBZ / MCB)</h3>
        <div class="batch-badge">☀️ 9am - 4pm (General)</div>
        <div class="batch-badge">☀️ 7am - 1pm (Bio/Micro)</div>
        <p style="margin-top:15px; color:#666; font-size:0.9rem;">Multiple combinations available: Physics-Chem-Maths or Chem-Botany-Zoology.</p>
      </div>
      <div class="card-footer">
        <span style="font-weight:bold; color:#2e7d32;">✅ Merit Based</span>
        <button onclick="openModal('bsc-modal')" class="details-btn">View Details</button>
      </div>
    </div>

    <div class="course-card">
      <div class="card-body">
        <span class="school-label">School of Business</span>
        <h3 class="card-title">B.Com (International Finance)</h3>
        <div class="batch-badge">☀️ Batch 1: 7am - 12pm</div>
        <div class="batch-badge">🌇 Batch 2: 4:45pm - 8:45pm</div>
        <p style="margin-top:15px; color:#666; font-size:0.9rem;">Specialized for ACCA/CPA aspirants with global accounting focus.</p>
      </div>
      <div class="card-footer">
        <span style="font-weight:bold; color:#e65100;">⚠️ Entrance Test</span>
        <button onclick="openModal('bcom-intl-modal')" class="details-btn">View Details</button>
      </div>
    </div>

  </div>
</div>

<div id="pg" class="course-container">
  <div class="course-grid">
    
    <div class="course-card">
      <div class="card-body">
        <span class="school-label">School of Business</span>
        <h3 class="card-title">Master of Commerce (M.Com)</h3>
        <div class="batch-badge">☀️ Batch 1: 7am - 11am</div>
        <div class="batch-badge">🌇 Batch 2: 4:45pm - 8:45pm</div>
      </div>
      <div class="card-footer">
        <span style="font-weight:bold; color:#2e7d32;">✅ Merit Based</span>
        <button onclick="openModal('mcom-modal')" class="details-btn">View Details</button>
      </div>
    </div>

    <div class="course-card">
      <div class="card-body">
        <span class="school-label">School of IT</span>
        <h3 class="card-title">Master of Computer Applications (MCA)</h3>
        <div class="batch-badge">🌤️ 1pm - 7pm</div>
      </div>
      <div class="card-footer">
        <span style="font-weight:bold; color:#e65100;">⚠️ Entrance Test</span>
        <button onclick="openModal('mca-modal')" class="details-btn">View Details</button>
      </div>
    </div>

    <div class="course-card">
      <div class="card-body">
        <span class="school-label">School of Languages</span>
        <h3 class="card-title">Master of Arts (English)</h3>
        <div class="batch-badge">☀️ Batch 1: 9am - 4pm</div>
        <div class="batch-badge">🌇 Batch 2: 4:45pm - 8:45pm</div>
      </div>
      <div class="card-footer">
        <span style="font-weight:bold; color:#2e7d32;">✅ Merit Based</span>
        <button onclick="openModal('ma-eng-modal')" class="details-btn">View Details</button>
      </div>
    </div>

  </div>
</div>

<div id="bcom-modal" class="modal-overlay" onclick="closeModal(event, 'bcom-modal')">
  <div class="modal-content">
    <div class="modal-header">
      <h2>Bachelor of Commerce (B.Com)</h2>
      <button class="close-btn" onclick="document.getElementById('bcom-modal').style.display='none'">&times;</button>
    </div>
    <div class="modal-body">
      <div class="info-group">
        <div class="info-title">📋 Eligibility</div>
        <div class="info-text">
          Pass in <strong>Class 12 (PUC)</strong> from Karnataka or equivalent board. Commerce/Arts/Science students can apply, but Commerce background is preferred for easier adaptation.
        </div>
      </div>
      <div class="info-group">
        <div class="info-title">📅 Selection Process</div>
        <div class="info-text">
          1. <strong>Application Review:</strong> Based on 12th Marks.<br>
          2. <strong>Interview:</strong> Two rounds of interview (Subject Knowledge + Personal).<br>
          3. <strong>Fee Payment:</strong> Within 3 days of selection.
        </div>
      </div>
      <div class="info-group">
        <div class="info-title">💰 Fee Structure (Approx/Year)</div>
        <div class="info-text">
          • Karnataka: ₹1,05,000<br>
          • Non-Karnataka: ₹1,20,000<br>
          • NRI: ₹1,65,000
        </div>
      </div>
    </div>
  </div>
</div>

<div id="bba-modal" class="modal-overlay" onclick="closeModal(event, 'bba-modal')">
  <div class="modal-content">
    <div class="modal-header">
      <h2>Bachelor of Business Admin (BBA)</h2>
      <button class="close-btn" onclick="document.getElementById('bba-modal').style.display='none'">&times;</button>
    </div>
    <div class="modal-body">
      <div class="info-group">
        <div class="info-title">📋 Eligibility</div>
        <div class="info-text">
          Pass in <strong>Class 12 (10+2)</strong> with a minimum of 50% aggregate. Students from any stream (Arts/Science/Commerce) are eligible.
        </div>
      </div>
      <div class="info-group">
        <div class="info-title">📅 Selection Process</div>
        <div class="info-text">
          • <strong>Merit Based:</strong> Primarily based on 10th and 11th/12th marks.<br>
          • <strong>Interview:</strong> Focus on communication skills and general awareness.
        </div>
      </div>
    </div>
  </div>
</div>

<div id="bca-modal" class="modal-overlay" onclick="closeModal(event, 'bca-modal')">
  <div class="modal-content">
    <div class="modal-header">
      <h2>Bachelor of Computer Applications (BCA)</h2>
      <button class="close-btn" onclick="document.getElementById('bca-modal').style.display='none'">&times;</button>
    </div>
    <div class="modal-body">
      <div class="info-group">
        <div class="info-title">📋 Eligibility</div>
        <div class="info-text">
          Pass in Class 12. <strong>Mathematics</strong> background is highly recommended and often prioritized. Students without Maths may need to do a bridge course.
        </div>
      </div>
      <div class="info-group">
        <div class="info-title">📅 Selection Process</div>
        <div class="info-text">
          • <strong>Merit + Interview:</strong> High weightage on Maths scores in Class 10/12.
        </div>
      </div>
    </div>
  </div>
</div>

<div id="viscom-modal" class="modal-overlay" onclick="closeModal(event, 'viscom-modal')">
  <div class="modal-content">
    <div class="modal-header">
      <h2>B.A. Visual Communication</h2>
      <button class="close-btn" onclick="document.getElementById('viscom-modal').style.display='none'">&times;</button>
    </div>
    <div class="modal-body">
      <div class="info-group">
        <div class="info-title">📋 Eligibility</div>
        <div class="info-text">
          Pass in Class 12 (any stream). A creative portfolio (drawings, photos, videos) is a huge plus.
        </div>
      </div>
      <div class="info-group">
        <div class="info-title">⚠️ Entrance Test</div>
        <div class="info-text">
          SJU Entrance Test (SJUET) is <strong>Mandatory</strong>. It tests creative aptitude and general knowledge.
        </div>
      </div>
    </div>
  </div>
</div>

<div id="bsc-modal" class="modal-overlay" onclick="closeModal(event, 'bsc-modal')">
  <div class="modal-content">
    <div class="modal-header">
      <h2>Bachelor of Science (B.Sc)</h2>
      <button class="close-btn" onclick="document.getElementById('bsc-modal').style.display='none'">&times;</button>
    </div>
    <div class="modal-body">
      <div class="info-group">
        <div class="info-title">📋 Eligibility</div>
        <div class="info-text">
          Pass in Class 12 (Science Stream).<br>
          • For PCM: Maths is mandatory.<br>
          • For CBZ/Microbiology: Biology/Chemistry is mandatory.
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
