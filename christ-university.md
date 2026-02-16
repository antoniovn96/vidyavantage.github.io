---
layout: default
title: "Christ (Deemed to be University) 🎓"
permalink: /colleges/christ-university/
image: "https://christuniversity.in/images/sharingLogo.jpg"
description: "Explore Undergraduate, Postgraduate, PhD, and Online programmes at Christ University. Check entrance exams, timings, and eligibility."
---

<style>
  /* 1. LAYOUT RESET */
  .main-content { max-width: 100% !important; padding: 0 !important; margin: 0 !important; }
  body { background-color: #f8f9fa; font-family: 'Segoe UI', sans-serif; }

  /* 2. HERO SECTION */
  .uni-hero {
    background: linear-gradient(rgba(139, 0, 0, 0.85), rgba(20, 20, 20, 0.8)), url('https://christuniversity.in/images/inner-banner-comn.jpg');
    background-size: cover;
    background-position: center;
    color: white;
    text-align: center;
    padding: 100px 20px;
    margin-bottom: 40px;
    border-bottom: 5px solid #D4AF37;
  }
  .uni-hero h1 { font-size: 3rem; margin: 0; color: white !important; text-shadow: 0 4px 10px rgba(0,0,0,0.5); }
  .uni-hero p { font-size: 1.2rem; color: #ddd !important; margin-top: 10px; }

  /* 3. TABS */
  .level-tabs { display: flex; justify-content: center; gap: 10px; margin-bottom: 40px; flex-wrap: wrap; padding: 0 20px; }
  .tab-btn {
    background: white; border: 1px solid #ddd; padding: 12px 25px; border-radius: 50px;
    font-weight: bold; color: #555; cursor: pointer; transition: 0.3s;
  }
  .tab-btn.active { background: #8b0000; color: white; border-color: #8b0000; box-shadow: 0 5px 15px rgba(139, 0, 0, 0.3); }

  /* 4. CONTENT CARDS */
  .course-container { max-width: 1100px; margin: 0 auto; padding: 0 20px 60px; display: none; animation: fadeIn 0.5s; }
  .course-container.active { display: block; }
  @keyframes fadeIn { from { opacity:0; transform:translateY(10px); } to { opacity:1; transform:translateY(0); } }

  .school-card { background: white; border-radius: 12px; box-shadow: 0 5px 20px rgba(0,0,0,0.05); margin-bottom: 30px; overflow: hidden; border-top: 5px solid #8b0000; }
  .school-header { background: #fffcfc; padding: 20px 30px; border-bottom: 1px solid #eee; }
  .school-header h2 { margin: 0; color: #8b0000; font-size: 1.5rem; }

  .course-table { width: 100%; border-collapse: collapse; }
  .course-table th, .course-table td { padding: 15px 30px; text-align: left; border-bottom: 1px solid #eee; }
  .course-table th { color: #888; text-transform: uppercase; font-size: 0.8rem; font-weight: 700; }
  .course-table tr:hover { background: #fff8f8; }

  .badge { padding: 5px 10px; border-radius: 4px; font-size: 0.8rem; font-weight: bold; }
  .badge-no { background: #e8f5e9; color: #2e7d32; }
  .badge-yes { background: #ffebee; color: #c62828; }
</style>

<div class="uni-hero">
  <h1>Christ (Deemed to be University)</h1>
  <p>Bangalore • Delhi NCR • Pune Lavasa</p>
  <a href="https://christuniversity.in" target="_blank" style="color:#D4AF37; font-weight:bold; text-decoration:none;">Visit Official Portal ➔</a>
</div>

<div class="level-tabs">
  <button class="tab-btn active" onclick="openLevel('ug')">UG Programs</button>
  <button class="tab-btn" onclick="openLevel('pg')">PG Programs</button>
  <button class="tab-btn" onclick="openLevel('phd')">Doctoral (PhD)</button>
  <button class="tab-btn" onclick="openLevel('online')">Online Degrees</button>
</div>

<div id="ug" class="course-container active">
  <div class="school-card">
    <div class="school-header"><h2>Professional & Commerce</h2></div>
    <table class="course-table">
      <thead><tr><th>Programme</th><th>Entrance Test</th><th>Last Date</th></tr></thead>
      <tbody>
        <tr><td><strong>BBA (Honours/Research)</strong></td><td><span class="badge badge-yes">YES</span></td><td>30-Mar-2026</td></tr>
        <tr><td><strong>B.Com (International Finance)</strong></td><td><span class="badge badge-yes">YES</span></td><td>30-Mar-2026</td></tr>
        <tr><td><strong>BHM (Hotel Management)</strong></td><td><span class="badge badge-yes">YES</span></td><td>30-Mar-2026</td></tr>
        <tr><td><strong>BA LLB / BBA LLB (Honours)</strong></td><td><span class="badge badge-yes">YES</span></td><td>30-Mar-2026</td></tr>
      </tbody>
    </table>
  </div>
</div>

<div id="pg" class="course-container">
  <div class="school-card">
    <div class="school-header"><h2>Postgraduate Studies</h2></div>
    <table class="course-table">
      <thead><tr><th>Programme</th><th>Selection Mode</th><th>Open Until</th></tr></thead>
      <tbody>
        <tr><td><strong>MBA (Flagship)</strong></td><td>CAT/MAT/GMAT + GD/PI</td><td>22-Mar-2026</td></tr>
        <tr><td><strong>M.Sc Psychology (Clinical)</strong></td><td>Entrance Test + PI</td><td>22-Mar-2026</td></tr>
        <tr><td><strong>MA English / Economics</strong></td><td>Merit + Interview</td><td>22-Mar-2026</td></tr>
        <tr><td><strong>MCA / M.Sc Data Science</strong></td><td>Entrance Test</td><td>22-Mar-2026</td></tr>
      </tbody>
    </table>
  </div>
</div>

<div id="phd" class="course-container">
  <div class="school-card">
    <div class="school-header"><h2>Doctoral Research</h2></div>
    <div style="padding: 30px; line-height: 1.6;">
      <p><strong>Eligibility:</strong> Master’s degree with minimum 55% aggregate.</p>
      <p><strong>Exemption:</strong> Students with UGC-NET/JRF, GATE, or M.Phil are exempt from the written entrance test.</p>
      <p><strong>Fee Structure:</strong><br>• Full-Time: ~₹60,000/year<br>• Part-Time: ~₹80,000/year</p>
    </div>
  </div>
</div>

<div id="online" class="course-container">
  <div class="school-card">
    <div class="school-header"><h2>UGC Recognized Online Degrees</h2></div>
    <table class="course-table">
      <thead><tr><th>Degree</th><th>Duration</th><th>Total Fee (Approx)</th></tr></thead>
      <tbody>
        <tr><td><strong>Online MBA</strong></td><td>2 Years</td><td>₹1,90,000</td></tr>
        <tr><td><strong>Online M.Sc Data Science</strong></td><td>2 Years</td><td>₹2,50,000</td></tr>
        <tr><td><strong>Online BCA / B.Com</strong></td><td>3 Years</td><td>₹1,60,000</td></tr>
      </tbody>
    </table>
  </div>
</div>

<script>
  function openLevel(levelId) {
    document.querySelectorAll('.course-container').forEach(el => el.classList.remove('active'));
    document.querySelectorAll('.tab-btn').forEach(btn => btn.classList.remove('active'));
    document.getElementById(levelId).classList.add('active');
    event.currentTarget.classList.add('active');
  }
</script>
