---
layout: default
title: "St. Joseph's University, Bengaluru 🎓"
permalink: /colleges/st-josephs/
image: "https://images.unsplash.com/photo-1562774053-701939374585?w=1200&h=630&fit=crop"
description: "Complete list of Undergraduate, PG, and Diploma courses at St. Joseph's University organized by Schools."
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

  /* 4. COURSE LIST STYLES */
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

  /* MODAL */
  .modal-overlay {
    display: none; position: fixed; top: 0; left: 0; width: 100%; height: 100%;
    background: rgba(0,0,0,0.6); z-index: 2000; align-items: center; justify-content: center; backdrop-filter: blur(3px);
  }
  .modal-content {
    background: white; width: 90%; max-width: 600px; padding: 30px; border-radius: 12px;
    position: relative; animation: slideUp 0.3s; max-height: 85vh; overflow-y: auto;
  }
  .close-btn { position: absolute; top: 15px; right: 20px; font-size: 2rem; cursor: pointer; color: #aaa; }
  
  @keyframes slideUp { from { transform: translateY(50px); opacity: 0; } to { transform: translateY(0); opacity: 1; } }
  @keyframes fadeIn { from { opacity: 0; } to { opacity: 1; } }

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
      <li class="course-item"><span>Bachelor of Commerce (B.Com)</span><div><span class="badge-eligibility">12th Pass</span> <button onclick="openDetails('bcom')" class="details-btn">Details</button></div></li>
      <li class="course-item"><span>B.Com (Industry Integrated)</span><span class="badge-eligibility">12th Pass</span></li>
      <li class="course-item"><span>B.Com (International Finance & Accounting)</span><span class="badge-eligibility">12th Pass</span></li>
      <li class="course-item"><span>Bachelor of Business Administration (BBA)</span><span class="badge-eligibility">12th Pass</span></li>
      <li class="course-item"><span>BBA (Strategic Finance)</span><span class="badge-eligibility">12th Pass</span></li>
      <li class="course-item"><span>BBA (Branding and Entrepreneurship)</span><span class="badge-eligibility">12th Pass</span></li>
    </ul>
  </div>

  <div class="school-block">
    <div class="school-header"><h2>School of Chemical Sciences</h2></div>
    <ul class="course-list">
      <li class="course-item"><span>B.Sc (Chemistry, Biotechnology, Biology)</span><span class="badge-eligibility">12th Science</span></li>
      <li class="course-item"><span>B.Sc (Biochemistry, Microbiology, Zoology)</span><span class="badge-eligibility">12th Science</span></li>
      <li class="course-item"><span>B.Sc (Biochemistry, Biology, Biotechnology)</span><span class="badge-eligibility">12th Science</span></li>
      <li class="course-item"><span>B.Sc (Biochemistry, Biotechnology, Zoology)</span><span class="badge-eligibility">12th Science</span></li>
      <li class="course-item"><span>B.Sc (Chemistry, Botany, Zoology)</span><span class="badge-eligibility">12th Science</span></li>
      <li class="course-item"><span>B.Sc (Physics, Chemistry, Mathematics)</span><span class="badge-eligibility">12th Science</span></li>
      <li class="course-item"><span>B.Sc (Chemistry, Environmental Science, Biology)</span><span class="badge-eligibility">12th Science</span></li>
      <li class="course-item"><span>B.Sc (Chemistry, Microbiology, Biology)</span><span class="badge-eligibility">12th Science</span></li>
      <li class="course-item"><span>B.Sc (Chemistry, Zoology, Biotechnology)</span><span class="badge-eligibility">12th Science</span></li>
      <li class="course-item"><span>B.Sc (Biochemistry, Biology, Microbiology)</span><span class="badge-eligibility">12th Science</span></li>
      <li class="course-item"><span>B.Sc (Biochemistry, Botany, Biotechnology)</span><span class="badge-eligibility">12th Science</span></li>
      <li class="course-item"><span>B.Sc (Chemistry, Microbiology, Biotechnology)</span><span class="badge-eligibility">12th Science</span></li>
    </ul>
  </div>

  <div class="school-block">
    <div class="school-header"><h2>School of Humanities & Social Sciences</h2></div>
    <ul class="course-list">
      <li class="course-item"><span>B.Sc (Economics, Mathematics, Statistics)</span><span class="badge-eligibility">12th (Maths)</span></li>
      <li class="course-item"><span>B.A. (Industrial Relations, Economics, Sociology)</span><span class="badge-eligibility">12th Pass</span></li>
      <li class="course-item"><span>B.A. (Economics, Political Science, Sociology)</span><span class="badge-eligibility">12th Pass</span></li>
      <li class="course-item"><span>B.A. (History, Political Science, Sociology)</span><span class="badge-eligibility">12th Pass</span></li>
      <li class="course-item"><span>B.A. (Intl. Relations, Peace Studies, Journalism & Public Policy)</span><span class="badge-eligibility">12th Pass</span></li>
      <li class="course-item"><span>B.A. (Journalism, Political Science, Sociology)</span><span class="badge-eligibility">12th Pass</span></li>
      <li class="course-item"><span>B.A. (Communicative English, Pol Science, Economics)</span><span class="badge-eligibility">12th Pass</span></li>
      <li class="course-item"><span>B.A. (History, Economics, Political Science)</span><span class="badge-eligibility">12th Pass</span></li>
      <li class="course-item"><span>B.A. (Journalism, Economics, Psychology)</span><span class="badge-eligibility">12th Pass</span></li>
      <li class="course-item"><span>B.A. (Optional English, Journalism, Psychology)</span><span class="badge-eligibility">12th Pass</span></li>
      <li class="course-item"><span>B.A. (Theatre & Performance Studies, Opt. English, Psychology)</span><span class="badge-eligibility">12th Pass</span></li>
    </ul>
  </div>

  <div class="school-block">
    <div class="school-header"><h2>School of Languages & Literatures</h2></div>
    <ul class="course-list">
      <li class="course-item"><span>B.A. (Intl. Relations, Peace Studies, Journalism & Public Policy)</span><span class="badge-eligibility">12th Pass</span></li>
      <li class="course-item"><span>B.A. (Journalism, Political Science, Sociology)</span><span class="badge-eligibility">12th Pass</span></li>
      <li class="course-item"><span>B.A. (Communicative English, Pol Science, Economics)</span><span class="badge-eligibility">12th Pass</span></li>
      <li class="course-item"><span>B.A. (Journalism, Economics, Psychology)</span><span class="badge-eligibility">12th Pass</span></li>
      <li class="course-item"><span>B.A. (Optional English, Journalism, Psychology)</span><span class="badge-eligibility">12th Pass</span></li>
      <li class="course-item"><span>B.A. (Theatre & Performance Studies, Opt. English, Psychology)</span><span class="badge-eligibility">12th Pass</span></li>
    </ul>
  </div>

  <div class="school-block">
    <div class="school-header"><h2>School of Life Sciences</h2></div>
    <ul class="course-list">
      <li class="course-item"><span>B.Sc (Chemistry, Biotechnology, Biology)</span><span class="badge-eligibility">12th Science</span></li>
      <li class="course-item"><span>B.Sc (Biochemistry, Biology, Biotechnology)</span><span class="badge-eligibility">12th Science</span></li>
      <li class="course-item"><span>B.Sc (Biochemistry, Microbiology, Zoology)</span><span class="badge-eligibility">12th Science</span></li>
      <li class="course-item"><span>B.Sc (Biochemistry, Biotechnology, Zoology)</span><span class="badge-eligibility">12th Science</span></li>
      <li class="course-item"><span>B.Sc (Chemistry, Botany, Zoology)</span><span class="badge-eligibility">12th Science</span></li>
      <li class="course-item"><span>B.Sc (Chemistry, Environmental Science, Biology)</span><span class="badge-eligibility">12th Science</span></li>
      <li class="course-item"><span>B.Sc (Chemistry, Microbiology, Biology)</span><span class="badge-eligibility">12th Science</span></li>
      <li class="course-item"><span>B.Sc (Chemistry, Zoology, Biotechnology)</span><span class="badge-eligibility">12th Science</span></li>
      <li class="course-item"><span>B.Sc (Biochemistry, Biology, Microbiology)</span><span class="badge-eligibility">12th Science</span></li>
      <li class="course-item"><span>B.Sc (Biochemistry, Botany, Biotechnology)</span><span class="badge-eligibility">12th Science</span></li>
      <li class="course-item"><span>B.Sc (Botany, Environmental Science, Zoology)</span><span class="badge-eligibility">12th Science</span></li>
      <li class="course-item"><span>B.Sc (Chemistry, Microbiology, Biotechnology)</span><span class="badge-eligibility">12th Science</span></li>
    </ul>
  </div>

  <div class="school-block">
    <div class="school-header"><h2>School of Physical Sciences</h2></div>
    <ul class="course-list">
      <li class="course-item"><span>B.Sc (Physics, Mathematics, Computer Science)</span><span class="badge-eligibility">12th PCM</span></li>
      <li class="course-item"><span>B.Sc (Economics, Mathematics, Statistics)</span><span class="badge-eligibility">12th Maths</span></li>
      <li class="course-item"><span>B.Sc (Physics, Chemistry, Mathematics)</span><span class="badge-eligibility">12th PCM</span></li>
      <li class="course-item"><span>B.Sc (Physics, Electronics, Mathematics)</span><span class="badge-eligibility">12th PCM</span></li>
      <li class="course-item"><span>B.Sc (Computer Science, Mathematics, Statistics)</span><span class="badge-eligibility">12th Maths</span></li>
    </ul>
  </div>

  <div class="school-block">
    <div class="school-header"><h2>School of Social Work</h2></div>
    <ul class="course-list">
      <li class="course-item"><span>Bachelor of Social Work (BSW)</span><span class="badge-eligibility">12th Pass</span></li>
    </ul>
  </div>

  <div class="school-block">
    <div class="school-header"><h2>School of Communication & Media Studies</h2></div>
    <ul class="course-list">
      <li class="course-item"><span>B.A. in Visual Communication</span><span class="badge-eligibility">12th Pass</span></li>
      <li class="course-item"><span>B.Voc in Digital Media and Animation</span><span class="badge-eligibility">12th Pass</span></li>
      <li class="course-item"><span>B.Voc in Visual Media and Film-Making</span><span class="badge-eligibility">12th Pass</span></li>
    </ul>
  </div>

  <div class="school-block">
    <div class="school-header"><h2>School of Information Technology</h2></div>
    <ul class="course-list">
      <li class="course-item"><span>Bachelor of Computer Applications (BCA)</span><span class="badge-eligibility">12th Maths/CS</span></li>
      <li class="course-item"><span>B.Sc (Physics, Mathematics, Computer Science)</span><span class="badge-eligibility">12th PCM</span></li>
      <li class="course-item"><span>BCA in Data Analytics</span><span class="badge-eligibility">12th Maths</span></li>
      <li class="course-item"><span>B.Sc (Computer Science, Mathematics, Statistics)</span><span class="badge-eligibility">12th Maths</span></li>
    </ul>
  </div>

</div>

<div id="pg" class="course-container">

  <div class="school-block">
    <div class="school-header"><h2>School of Business</h2></div>
    <ul class="course-list">
      <li class="course-item"><span>Master of Commerce (M.Com)</span><span class="badge-eligibility">B.Com/BBA</span></li>
    </ul>
  </div>

  <div class="school-block">
    <div class="school-header"><h2>School of Chemical Sciences</h2></div>
    <ul class="course-list">
      <li class="course-item"><span>M.Sc in Analytical Chemistry</span><span class="badge-eligibility">B.Sc Chemistry</span></li>
      <li class="course-item"><span>M.Sc in Organic Chemistry</span><span class="badge-eligibility">B.Sc Chemistry</span></li>
      <li class="course-item"><span>M.Sc in Biochemistry</span><span class="badge-eligibility">B.Sc Biochem</span></li>
    </ul>
  </div>

  <div class="school-block">
    <div class="school-header"><h2>School of Humanities & Social Sciences</h2></div>
    <ul class="course-list">
      <li class="course-item"><span>M.A. in Economics</span><span class="badge-eligibility">BA Economics</span></li>
      <li class="course-item"><span>M.A. in Political Science</span><span class="badge-eligibility">BA Pol Sci</span></li>
      <li class="course-item"><span>M.Sc in Counselling Psychology</span><span class="badge-eligibility">BA/B.Sc Psychology</span></li>
    </ul>
  </div>

  <div class="school-block">
    <div class="school-header"><h2>School of Languages & Literatures</h2></div>
    <ul class="course-list">
      <li class="course-item"><span>M.A. in English</span><span class="badge-eligibility">BA English</span></li>
    </ul>
  </div>

  <div class="school-block">
    <div class="school-header"><h2>School of Life Sciences</h2></div>
    <ul class="course-list">
      <li class="course-item"><span>M.Sc in Biotechnology</span><span class="badge-eligibility">B.Sc Biotech</span></li>
      <li class="course-item"><span>M.Sc in Environmental Science and Sustainability</span><span class="badge-eligibility">B.Sc Science</span></li>
      <li class="course-item"><span>M.Sc in Food Science and Technology</span><span class="badge-eligibility">B.Sc Food Sci</span></li>
      <li class="course-item"><span>M.Sc in Microbiology</span><span class="badge-eligibility">B.Sc Micro</span></li>
      <li class="course-item"><span>M.Sc in Zoology</span><span class="badge-eligibility">B.Sc Zoology</span></li>
    </ul>
  </div>

  <div class="school-block">
    <div class="school-header"><h2>School of Physical Sciences</h2></div>
    <ul class="course-list">
      <li class="course-item"><span>M.Sc in Mathematics</span><span class="badge-eligibility">B.Sc Maths</span></li>
      <li class="course-item"><span>M.Sc in Physics</span><span class="badge-eligibility">B.Sc Physics</span></li>
      <li class="course-item"><span>M.Sc in Statistics</span><span class="badge-eligibility">B.Sc Statistics</span></li>
    </ul>
  </div>

  <div class="school-block">
    <div class="school-header"><h2>School of Social Work</h2></div>
    <ul class="course-list">
      <li class="course-item"><span>Master of Social Work (MSW)</span><span class="badge-eligibility">BSW/Any Degree</span></li>
    </ul>
  </div>

  <div class="school-block">
    <div class="school-header"><h2>School of Communication & Media Studies</h2></div>
    <ul class="course-list">
      <li class="course-item"><span>M.A. in Advertising and Public Relations</span><span class="badge-eligibility">Any Degree</span></li>
      <li class="course-item"><span>M.A. in Journalism and Mass Communication</span><span class="badge-eligibility">Any Degree</span></li>
    </ul>
  </div>

  <div class="school-block">
    <div class="school-header"><h2>School of Information Technology</h2></div>
    <ul class="course-list">
      <li class="course-item"><span>Master of Computer Applications (MCA)</span><span class="badge-eligibility">BCA/B.Sc CS</span></li>
      <li class="course-item"><span>M.Sc in Big Data Analytics</span><span class="badge-eligibility">B.Sc Maths/Stats/CS</span></li>
      <li class="course-item"><span>M.Sc in Computer Science</span><span class="badge-eligibility">B.Sc CS</span></li>
      <li class="course-item"><span>M.Sc in Cyber Security & AI</span><span class="badge-eligibility">B.Sc CS/IT</span></li>
    </ul>
  </div>

</div>

<div id="diploma" class="course-container">

  <div class="school-block">
    <div class="school-header"><h2>School of Business</h2></div>
    <ul class="course-list">
      <li class="course-item"><span>PG Diploma in Financial Management</span><span class="badge-eligibility">Degree</span></li>
      <li class="course-item"><span>PG Diploma in Human Resource Management</span><span class="badge-eligibility">Degree</span></li>
    </ul>
  </div>

  <div class="school-block">
    <div class="school-header"><h2>School of Communication & Media</h2></div>
    <ul class="course-list">
      <li class="course-item"><span>Executive Diploma Digital Media Communications</span><span class="badge-eligibility">Degree/Work Exp</span></li>
    </ul>
  </div>

  <div class="school-block">
    <div class="school-header"><h2>School of Information Technology</h2></div>
    <ul class="course-list">
      <li class="course-item"><span>PG Diploma in Cyber Security</span><span class="badge-eligibility">Tech Degree</span></li>
      <li class="course-item"><span>PG Diploma in Data Analytics</span><span class="badge-eligibility">Tech Degree</span></li>
    </ul>
  </div>

</div>

<div id="bcom-modal" class="modal-overlay" onclick="closeModal(event, 'bcom-modal')">
  <div class="modal-content">
    <span class="close-btn" onclick="document.getElementById('bcom-modal').style.display='none'">&times;</span>
    
    <h2 style="color:#0A2342; border-bottom:2px solid #D4AF37; padding-bottom:10px;">Bachelor of Commerce (B.Com)</h2>
    
    <div style="background:#f9f9f9; padding:15px; border-radius:8px; margin:15px 0;">
      <h4 style="margin-top:0;">💰 Fee Structure (Per Year)</h4>
      <ul style="padding-left:20px; margin-bottom:0;">
        <li><strong>Karnataka:</strong> ₹1,05,000</li>
        <li><strong>Non-Karnataka:</strong> ₹1,20,000</li>
        <li><strong>NRI:</strong> ₹1,65,000</li>
      </ul>
      <p style="font-size:0.85rem; color:#666; margin-top:5px;"><em>*Plus one-time admission fee of ₹5,000.</em></p>
    </div>

    <h4 style="margin-bottom:5px;">📋 Eligibility</h4>
    <p>Completion of 2-year Pre-University (PUC) or 12th Grade equivalent. Study of two languages is mandatory.</p>

    <h4 style="margin-bottom:5px;">📅 Selection Process</h4>
    <p>1. <strong>Application:</strong> Submit online with marks.<br>2. <strong>Interview:</strong> Two rounds (Subject & Personal).<br>3. <strong>Payment:</strong> Within 3 days of selection.</p>

    <div style="text-align:center; margin-top:20px;">
      <a href="https://sju.edu.in/courses/st-joseph-university/school-of-business/Department-of-Commerce/bachelor-of-commerce" target="_blank" style="background:#D4AF37; color:#0A2342; padding:10px 20px; text-decoration:none; font-weight:bold; border-radius:50px;">
        Visit Official Page ↗
      </a>
    </div>
  </div>
</div>

<script>
  function openLevel(levelId) {
    document.querySelectorAll('.course-container').forEach(el => el.classList.remove('active'));
    document.querySelectorAll('.tab-btn').forEach(btn => btn.classList.remove('active'));
    document.getElementById(levelId).classList.add('active');
    event.currentTarget.classList.add('active');
  }

  function openModal(id) { document.getElementById(id).style.display = 'flex'; }
  function closeModal(e, id) { if(e.target.className === 'modal-overlay') document.getElementById(id).style.display = 'none'; }
</script>
