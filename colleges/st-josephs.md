---
layout: default
title: "St. Joseph's University, Bengaluru 🎓"
permalink: /colleges/st-josephs/
image: "https://images.unsplash.com/photo-1562774053-701939374585?w=1200&h=630&fit=crop"
description: "Complete list of Undergraduate, PG, and Diploma courses at St. Joseph's University with batch timings, fees, and entrance exam details."
---

<style>
  /* 1. LAYOUT RESET */
  .main-content {
    max-width: 100% !important;
    padding: 0 !important;
    margin: 0 !important;
  }
  
  body { background-color: #f8f9fa; font-family: 'Segoe UI', sans-serif; }

  /* 2. HERO SECTION */
  .uni-hero {
    background: linear-gradient(rgba(10, 35, 66, 0.9), rgba(10, 35, 66, 0.8)), url('https://images.unsplash.com/photo-1541339907198-e08756dedf3f?w=1600&auto=format&fit=crop');
    background-size: cover;
    background-position: center;
    color: white;
    text-align: center;
    padding: 100px 20px;
    margin-bottom: 40px;
  }

  .uni-hero h1 { font-size: 3rem; margin: 0; color: white !important; text-shadow: 0 4px 10px rgba(0,0,0,0.5); }
  .uni-hero p { font-size: 1.2rem; color: #ddd !important; margin-top: 10px; }
  
  .visit-btn {
    display: inline-block;
    background: #D4AF37;
    color: #0A2342;
    padding: 10px 25px;
    border-radius: 50px;
    text-decoration: none;
    font-weight: bold;
    margin-top: 20px;
    transition: transform 0.2s;
  }
  .visit-btn:hover { transform: scale(1.05); text-decoration: none; color: #0A2342; }

  /* 3. TABS */
  .level-tabs {
    display: flex;
    justify-content: center;
    gap: 15px;
    margin-bottom: 40px;
    flex-wrap: wrap;
    padding: 0 20px;
  }

  .tab-btn {
    background: white;
    border: 1px solid #ddd;
    padding: 12px 30px;
    border-radius: 50px;
    font-weight: bold;
    color: #555;
    cursor: pointer;
    box-shadow: 0 4px 10px rgba(0,0,0,0.05);
    transition: all 0.3s;
  }

  .tab-btn.active {
    background: #0A2342;
    color: white;
    border-color: #0A2342;
    box-shadow: 0 5px 15px rgba(10, 35, 66, 0.3);
  }

  /* 4. COURSE CARDS */
  .course-container {
    max-width: 1100px;
    margin: 0 auto;
    padding: 0 20px 60px;
    display: none;
    animation: fadeIn 0.5s;
  }
  
  .course-container.active { display: block; }

  @keyframes fadeIn { from { opacity:0; transform:translateY(10px); } to { opacity:1; transform:translateY(0); } }

  .school-card {
    background: white;
    border-radius: 12px;
    box-shadow: 0 5px 20px rgba(0,0,0,0.05);
    margin-bottom: 30px;
    overflow: hidden;
    border-top: 5px solid #0A2342;
  }

  .school-header {
    background: #f8f9fa;
    padding: 20px 30px;
    border-bottom: 1px solid #eee;
  }

  .school-header h2 { margin: 0; color: #0A2342; font-size: 1.5rem; }

  /* TABLE STYLES */
  .course-table {
    width: 100%;
    border-collapse: collapse;
  }

  .course-table th, .course-table td {
    padding: 15px 30px;
    text-align: left;
    border-bottom: 1px solid #eee;
    font-size: 0.95rem;
  }

  .course-table th {
    background: #fff;
    color: #888;
    text-transform: uppercase;
    font-size: 0.8rem;
    font-weight: 700;
    letter-spacing: 1px;
  }

  .course-table tr:last-child td { border-bottom: none; }
  .course-table tr:hover { background: #fdfdfd; }

  .batch-time { color: #555; font-size: 0.9rem; white-space: pre-line; line-height: 1.4; }
  
  /* BADGES & BUTTONS */
  .badge { padding: 5px 10px; border-radius: 4px; font-size: 0.8rem; font-weight: bold; }
  .badge-no { background: #e8f5e9; color: #2e7d32; } /* Green */
  .badge-yes { background: #ffebee; color: #c62828; } /* Red */

  .details-btn {
    background: #0A2342; 
    color: white; 
    border: none; 
    padding: 6px 12px; 
    border-radius: 4px; 
    cursor: pointer; 
    font-size: 0.85rem; 
    margin-left: 10px;
    transition: background 0.2s;
  }
  .details-btn:hover { background: #D4AF37; color: #0A2342; }

  /* MODAL STYLES */
  .modal-overlay {
    display: none; position: fixed; top: 0; left: 0; width: 100%; height: 100%;
    background: rgba(0,0,0,0.6); z-index: 2000; align-items: center; justify-content: center;
    backdrop-filter: blur(3px);
  }
  .modal-content {
    background: white; width: 90%; max-width: 600px; padding: 30px; border-radius: 12px;
    position: relative; animation: slideDown 0.3s; margin: 5% auto;
    max-height: 85vh; overflow-y: auto; box-shadow: 0 10px 30px rgba(0,0,0,0.2);
  }
  .close-btn { position: absolute; top: 15px; right: 20px; font-size: 2rem; cursor: pointer; color: #aaa; line-height: 1; }
  .close-btn:hover { color: #000; }
  
  @keyframes slideDown { from { transform: translateY(-20px); opacity: 0; } to { transform: translateY(0); opacity: 1; } }

  .fee-box { background: #f0f4f8; padding: 15px; border-radius: 8px; margin: 15px 0; border-left: 4px solid #D4AF37; }
  .fee-row { display: flex; justify-content: space-between; margin-bottom: 5px; font-size: 0.95rem; }
  .fee-row strong { color: #555; }

</style>

<div class="uni-hero">
  <h1>St. Joseph's University</h1>
  <p>Bengaluru, Karnataka • Est. 1882</p>
  <a href="https://sju.edu.in" target="_blank" class="visit-btn">Visit Official Website ↗</a>
</div>

<div class="level-tabs">
  <button class="tab-btn active" onclick="openLevel('ug')">🎓 Undergraduate</button>
  <button class="tab-btn" onclick="openLevel('pg')">📜 Postgraduate</button>
  <button class="tab-btn" onclick="openLevel('diploma')">🛠️ PG Diploma</button>
</div>

<div id="ug" class="course-container active">

  <div class="school-card">
    <div class="school-header"><h2>School of Business</h2></div>
    <table class="course-table">
      <thead><tr><th>Course Name</th><th>Batch Timing</th><th>Entrance Test</th></tr></thead>
      <tbody>
        <tr>
          <td><strong>B.Com (Regular)</strong></td>
          <td class="batch-time">Batch 1: 7am-12pm<br>Batch 2: 12pm-4pm<br>Batch 3: 4:45pm-8:45pm</td>
          <td>
            <span class="badge badge-no">No</span>
            <button onclick="openModal('bcom-modal')" class="details-btn">Details ℹ️</button>
          </td>
        </tr>
        
        <tr><td><strong>B.Com (Industry Integrated)</strong></td><td class="batch-time">7:00 AM - 12:00 PM</td><td><span class="badge badge-no">No</span></td></tr>
        <tr><td><strong>B.Com (Intl. Finance & Acc.)</strong></td><td class="batch-time">Batch 1: 7am-12pm<br>Batch 2: 4:45pm-8:45pm</td><td><span class="badge badge-yes">YES</span></td></tr>
        <tr><td><strong>BBA (Regular)</strong></td><td class="batch-time">Batch 1: 7am-12pm<br>Batch 2: 4:45pm-8:45pm</td><td><span class="badge badge-no">No</span></td></tr>
        <tr><td><strong>BBA (Strategic Finance)</strong></td><td class="batch-time">Batch 1: 7am-12pm<br>Batch 2: 4pm-8:45pm</td><td><span class="badge badge-yes">YES</span></td></tr>
        <tr><td><strong>BBA (Branding & Entrep.)</strong></td><td class="batch-time">7:00 AM - 12:00 PM</td><td><span class="badge badge-no">No</span></td></tr>
      </tbody>
    </table>
  </div>

  <div class="school-card">
    <div class="school-header"><h2>School of Information Technology</h2></div>
    <table class="course-table">
      <thead><tr><th>Course Name</th><th>Batch Timing</th><th>Entrance Test</th></tr></thead>
      <tbody>
        <tr><td><strong>Bachelor of Computer Applications (BCA)</strong></td><td class="batch-time">Batch 1: 9am-4pm<br>Batch 2: 4pm-9pm</td><td><span class="badge badge-no">No</span></td></tr>
        <tr><td><strong>BCA (Data Analytics)</strong></td><td class="batch-time">7:00 AM - 1:00 PM</td><td><span class="badge badge-no">No</span></td></tr>
        <tr><td><strong>B.Sc (Comp Sci, Maths, Stats)</strong></td><td class="batch-time">7:00 AM - 1:00 PM</td><td><span class="badge badge-no">No</span></td></tr>
      </tbody>
    </table>
  </div>

  <div class="school-card">
    <div class="school-header"><h2>School of Communication & Media</h2></div>
    <table class="course-table">
      <thead><tr><th>Course Name</th><th>Batch Timing</th><th>Entrance Test</th></tr></thead>
      <tbody>
        <tr><td><strong>B.A. Visual Communication</strong></td><td class="batch-time">7:00 AM - 1:00 PM</td><td><span class="badge badge-yes">YES</span></td></tr>
        <tr><td><strong>B.Voc (Digital Media & Animation)</strong></td><td class="batch-time">7:00 AM - 1:00 PM</td><td><span class="badge badge-yes">YES</span></td></tr>
        <tr><td><strong>B.Voc (Visual Media & Filmmaking)</strong></td><td class="batch-time">7:00 AM - 1:00 PM</td><td><span class="badge badge-yes">YES</span></td></tr>
      </tbody>
    </table>
  </div>

  <div class="school-card">
    <div class="school-header"><h2>School of Humanities & Social Sciences</h2></div>
    <table class="course-table">
      <thead><tr><th>Course Name</th><th>Batch Timing</th><th>Entrance Test</th></tr></thead>
      <tbody>
        <tr><td><strong>B.A. (Econ, Pol Sci, Sociology)</strong></td><td class="batch-time">9:00 AM - 4:00 PM</td><td><span class="badge badge-no">No</span></td></tr>
        <tr><td><strong>B.A. (History, Econ, Pol Sci)</strong></td><td class="batch-time">Batch 1: 9am-4pm<br>Batch 2: 4:45pm-8:45pm</td><td><span class="badge badge-no">No</span></td></tr>
        <tr><td><strong>B.A. (Journalism, Econ, Psych)</strong></td><td class="batch-time">4:00 PM - 9:00 PM</td><td><span class="badge badge-no">No</span></td></tr>
        <tr><td><strong>B.A. (English, Journalism, Psych)</strong></td><td class="batch-time">Batch 1: 7am-1pm<br>Batch 2: 9am-4pm</td><td><span class="badge badge-yes">YES</span></td></tr>
      </tbody>
    </table>
  </div>

  <div class="school-card">
    <div class="school-header"><h2>School of Chemical Sciences</h2></div>
    <table class="course-table">
      <thead><tr><th>Course Name</th><th>Batch Timing</th><th>Entrance Test</th></tr></thead>
      <tbody>
        <tr><td><strong>B.Sc (Chem, Biotech, Bio)</strong></td><td class="batch-time">9:00 AM - 4:00 PM</td><td><span class="badge badge-no">No</span></td></tr>
        <tr><td><strong>B.Sc (Biochem, Micro, Zoo)</strong></td><td class="batch-time">7:00 AM - 1:00 PM</td><td><span class="badge badge-no">No</span></td></tr>
        <tr><td><strong>B.Sc (PCM - Physics, Chem, Math)</strong></td><td class="batch-time">9:00 AM - 4:00 PM</td><td><span class="badge badge-no">No</span></td></tr>
      </tbody>
    </table>
  </div>

</div>

<div id="pg" class="course-container">

  <div class="school-card">
    <div class="school-header"><h2>School of Business</h2></div>
    <table class="course-table">
      <thead><tr><th>Course Name</th><th>Batch Timing</th><th>Entrance Test</th></tr></thead>
      <tbody>
        <tr><td><strong>M.Com</strong></td><td class="batch-time">Batch 1: 7am-11am<br>Batch 2: 4:45pm-8:45pm</td><td><span class="badge badge-no">No</span></td></tr>
      </tbody>
    </table>
  </div>

  <div class="school-card">
    <div class="school-header"><h2>School of Information Technology</h2></div>
    <table class="course-table">
      <thead><tr><th>Course Name</th><th>Batch Timing</th><th>Entrance Test</th></tr></thead>
      <tbody>
        <tr><td><strong>MCA (Master of Computer App)</strong></td><td class="batch-time">1:00 PM - 7:00 PM</td><td><span class="badge badge-yes">YES</span></td></tr>
        <tr><td><strong>M.Sc (Big Data Analytics)</strong></td><td class="batch-time">9:00 AM - 4:00 PM</td><td><span class="badge badge-no">No</span></td></tr>
        <tr><td><strong>M.Sc (Computer Science)</strong></td><td class="batch-time">9:00 AM - 4:00 PM</td><td><span class="badge badge-no">No</span></td></tr>
        <tr><td><strong>M.Sc (Cyber Security & AI)</strong></td><td class="batch-time">7:00 AM - 1:00 PM</td><td><span class="badge badge-no">No</span></td></tr>
      </tbody>
    </table>
  </div>

  <div class="school-card">
    <div class="school-header"><h2>School of Communication</h2></div>
    <table class="course-table">
      <thead><tr><th>Course Name</th><th>Batch Timing</th><th>Entrance Test</th></tr></thead>
      <tbody>
        <tr><td><strong>M.A. (Advertising & PR)</strong></td><td class="batch-time">7:00 AM - 1:00 PM</td><td><span class="badge badge-yes">YES</span></td></tr>
        <tr><td><strong>M.A. (Journalism & Mass Comm)</strong></td><td class="batch-time">7:00 AM - 1:00 PM</td><td><span class="badge badge-yes">YES</span></td></tr>
      </tbody>
    </table>
  </div>

  <div class="school-card">
    <div class="school-header"><h2>School of Chemical & Life Sciences</h2></div>
    <table class="course-table">
      <thead><tr><th>Course Name</th><th>Batch Timing</th><th>Entrance Test</th></tr></thead>
      <tbody>
        <tr><td><strong>M.Sc (Analytical Chemistry)</strong></td><td class="batch-time">9:00 AM - 4:00 PM</td><td><span class="badge badge-no">No</span></td></tr>
        <tr><td><strong>M.Sc (Organic Chemistry)</strong></td><td class="batch-time">7:00 AM - 1:00 PM</td><td><span class="badge badge-no">No</span></td></tr>
        <tr><td><strong>M.Sc (Biotechnology)</strong></td><td class="batch-time">7:00 AM - 1:00 PM</td><td><span class="badge badge-yes">YES</span></td></tr>
        <tr><td><strong>M.Sc (Food Science)</strong></td><td class="batch-time">9:00 AM - 4:00 PM</td><td><span class="badge badge-yes">YES</span></td></tr>
        <tr><td><strong>M.Sc (Microbiology)</strong></td><td class="batch-time">9:00 AM - 4:00 PM</td><td><span class="badge badge-yes">YES</span></td></tr>
      </tbody>
    </table>
  </div>

</div>

<div id="diploma" class="course-container">

  <div class="school-card">
    <div class="school-header"><h2>PG Diploma Programmes</h2></div>
    <table class="course-table">
      <thead><tr><th>Course Name</th><th>Batch Timing</th><th>Entrance Test</th></tr></thead>
      <tbody>
        <tr><td><strong>PG Diploma in Financial Mgmt</strong></td><td class="batch-time">Sat: Offline (9-3)<br>Sun: Online (9-3)</td><td><span class="badge badge-no">No</span></td></tr>
        <tr><td><strong>PG Diploma in HR Management</strong></td><td class="batch-time">Sat: Offline (9-3)<br>Sun: Online (9-3)</td><td><span class="badge badge-no">No</span></td></tr>
        <tr><td><strong>PG Diploma in Cyber Security</strong></td><td class="batch-time">Weekdays: Online (6-9pm)<br>Weekends: Offline</td><td><span class="badge badge-no">No</span></td></tr>
        <tr><td><strong>PG Diploma in Data Analytics</strong></td><td class="batch-time">Weekdays: Online (6-9pm)<br>Weekends: Offline</td><td><span class="badge badge-no">No</span></td></tr>
        <tr><td><strong>Exec. Diploma Digital Media</strong></td><td class="batch-time">Tue/Thu: Online (7:30-8:30pm)<br>Sat: Offline (11:30-1)</td><td><span class="badge badge-no">No</span></td></tr>
      </tbody>
    </table>
  </div>

</div>

<div id="bcom-modal" class="modal-overlay" onclick="closeModal(event, 'bcom-modal')">
  <div class="modal-content">
    <span class="close-btn" onclick="document.getElementById('bcom-modal').style.display='none'">&times;</span>
    
    <h2 style="color:#0A2342; border-bottom:2px solid #D4AF37; padding-bottom:10px; margin-top:0;">Bachelor of Commerce (B.Com)</h2>
    
    <p><strong>Overview:</strong> The regular B.Com. programme facilitates students to acquire specialized knowledge in Accounting, Finance, Taxation, Banking, Insurance, and HR.</p>

    <div class="fee-box">
      <h4 style="margin-top:0; color:#0A2342;">💰 Fee Structure (Per Year)</h4>
      <div class="fee-row"><strong>Karnataka:</strong> <span>₹1,05,000</span></div>
      <div class="fee-row"><strong>Non-Karnataka:</strong> <span>₹1,20,000</span></div>
      <div class="fee-row"><strong>NRI / OCI:</strong> <span>₹1,65,000</span></div>
      <div class="fee-row"><strong>Foreign Nationals:</strong> <span>₹2,05,000 ($2,278)</span></div>
      <hr style="margin:8px 0; border:0; border-top:1px dashed #ccc;">
      <div class="fee-row"><strong>Admission Fee (One-time):</strong> <span>₹5,000</span></div>
    </div>

    <h4 style="color:#0A2342; margin-bottom:5px;">📋 Eligibility</h4>
    <p style="margin-top:0;">Candidates must have completed a 2-year Pre-University programme in Karnataka or equivalent (12th Grade). Study of two languages is mandatory.</p>

    <h4 style="color:#0A2342; margin-bottom:5px;">📅 Selection Process</h4>
    <ul style="margin-top:0; padding-left:20px;">
      <li><strong>Step 1:</strong> Online Application & Document Upload</li>
      <li><strong>Step 2:</strong> Interview (Two Rounds)</li>
      <li><strong>Step 3:</strong> Fee Payment (within 3 days of selection)</li>
    </ul>

    <div style="text-align:center; margin-top:25px;">
      <a href="https://sju.edu.in/courses/st-joseph-university/school-of-business/Department-of-Commerce/bachelor-of-commerce" target="_blank" style="background:#D4AF37; color:#0A2342; padding:12px 25px; text-decoration:none; font-weight:bold; border-radius:50px; box-shadow:0 4px 6px rgba(0,0,0,0.1);">
        Visit Official Page ↗
      </a>
    </div>
  </div>
</div>

<script>
  function openLevel(levelId) {
    // 1. Hide all containers
    const containers = document.querySelectorAll('.course-container');
    containers.forEach(el => el.classList.remove('active'));

    // 2. Reset buttons
    const btns = document.querySelectorAll('.tab-btn');
    btns.forEach(btn => btn.classList.remove('active'));

    // 3. Show selected
    document.getElementById(levelId).classList.add('active');
    event.currentTarget.classList.add('active');
  }

  function openModal(id) {
    document.getElementById(id).style.display = 'flex'; // Changed to flex for centering
  }

  function closeModal(e, id) {
    if(e.target.className === 'modal-overlay') {
      document.getElementById(id).style.display = 'none';
    }
  }
</script>
