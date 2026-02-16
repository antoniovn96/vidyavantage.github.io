---
layout: default
title: "Global Visa Intelligence Hub"
permalink: /visas/
image: "/assets/images/visa-preview.png"
description: "Compare student visas for USA, UK, Canada, Germany, Australia, and UAE. Check costs, work rights, and PR rules for Indian students."
---

<style>
  /* 1. GLOBAL RESET & FONTS */
  .main-content {
    max-width: 100% !important;
    padding: 0 !important;
    margin: 0 !important;
  }
  
  body { 
    background-color: #f4f7f6; 
    font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif;
    color: #333;
  }

  /* 2. HERO SECTION */
  .visa-hero {
    background: linear-gradient(rgba(10, 35, 66, 0.95), rgba(10, 35, 66, 0.9)), url('https://images.unsplash.com/photo-1451187580459-43490279c0fa?w=1600&auto=format&fit=crop');
    background-size: cover;
    background-position: center;
    color: white;
    text-align: center;
    padding: 100px 20px 80px;
    border-bottom: 4px solid #D4AF37;
  }
  
  .visa-hero h1 { 
    font-size: 3rem; 
    margin: 0 0 15px 0; 
    color: #ffffff !important; 
    text-shadow: 0 2px 10px rgba(0,0,0,0.5); 
    font-weight: 700;
    letter-spacing: 1px;
  }
  
  .visa-hero p { 
    font-size: 1.2rem; 
    color: #e0e0e0 !important; 
    max-width: 800px;
    margin: 0 auto;
    line-height: 1.6;
  }

  /* 3. TIER NAVIGATION */
  .tier-nav {
    background: white;
    padding: 20px;
    box-shadow: 0 4px 20px rgba(0,0,0,0.05);
    position: sticky;
    top: 0;
    z-index: 100;
    text-align: center;
  }

  .tier-label {
    display: block;
    font-size: 0.85rem;
    text-transform: uppercase;
    color: #888;
    margin-bottom: 10px;
    font-weight: bold;
    letter-spacing: 1px;
  }

  .country-tabs {
    display: flex;
    justify-content: center;
    gap: 10px;
    flex-wrap: wrap;
  }

  .tab-btn {
    background: #f8f9fa;
    border: 1px solid #e9ecef;
    padding: 10px 20px;
    border-radius: 4px;
    font-size: 0.95rem;
    font-weight: 600;
    color: #555;
    cursor: pointer;
    transition: all 0.2s;
  }

  .tab-btn:hover { background: #e9ecef; }
  
  .tab-btn.active {
    background: #0A2342;
    color: white;
    border-color: #0A2342;
  }

  /* 4. COUNTRY CONTENT CARD */
  .country-content {
    max-width: 1000px;
    margin: 40px auto;
    padding: 0 20px;
  }

  .visa-card {
    background: white;
    border-radius: 8px;
    box-shadow: 0 5px 25px rgba(0,0,0,0.08);
    overflow: hidden;
    display: none;
    margin-bottom: 40px;
    border: 1px solid #e0e0e0;
  }
  
  .visa-card.active { display: block; }

  /* Card Header Image */
  .vc-header {
    height: 250px;
    position: relative;
    color: white;
  }

  .vc-bg-img {
    width: 100%;
    height: 100%;
    object-fit: cover;
    filter: brightness(0.5);
  }

  .vc-title-overlay {
    position: absolute;
    bottom: 30px;
    left: 40px;
    z-index: 2;
  }

  .vc-title-overlay h2 { 
    margin: 0; 
    font-size: 3rem; 
    font-weight: 700; 
    text-shadow: 0 2px 10px rgba(0,0,0,0.5);
  }
  
  .vc-tag { 
    background: #D4AF37; 
    color: #0A2342; 
    padding: 6px 12px; 
    font-weight: bold; 
    font-size: 0.9rem; 
    display: inline-block; 
    margin-top: 10px;
    text-transform: uppercase;
    letter-spacing: 0.5px;
  }

  /* 5. DATA GRID (8 SECTIONS) */
  .vc-section {
    padding: 40px;
    border-bottom: 1px solid #eee;
  }

  .section-title {
    color: #0A2342;
    font-size: 1.4rem;
    margin: 0 0 20px 0;
    border-left: 4px solid #D4AF37;
    padding-left: 15px;
    font-weight: 700;
  }

  /* Quick Facts Table */
  .facts-table {
    width: 100%;
    border-collapse: collapse;
    margin-bottom: 20px;
  }
  
  .facts-table td {
    padding: 12px;
    border-bottom: 1px solid #eee;
    font-size: 1rem;
  }
  
  .facts-table td:first-child {
    font-weight: bold;
    color: #555;
    width: 40%;
  }

  .facts-table td:last-child {
    color: #0A2342;
    font-weight: 600;
  }

  /* Cost Calculator Box */
  .cost-box {
    background: #f8f9fa;
    padding: 25px;
    border-radius: 8px;
    border: 1px solid #eee;
  }

  .cost-row {
    display: flex;
    justify-content: space-between;
    margin-bottom: 10px;
    font-size: 1rem;
  }

  .cost-total {
    border-top: 2px solid #ccc;
    padding-top: 10px;
    margin-top: 10px;
    font-weight: bold;
    font-size: 1.2rem;
    color: #0A2342;
  }

  /* Eligibility Badge */
  .eligibility-check {
    background: #e3f2fd;
    color: #0d47a1;
    padding: 15px;
    text-align: center;
    border-radius: 4px;
    font-weight: bold;
    margin-top: 20px;
    cursor: pointer;
    border: 1px solid #bbdefb;
    transition: background 0.2s;
  }
  
  .eligibility-check:hover { background: #bbdefb; }

  /* Warning Box */
  .warning-box {
    background: #fff3e0;
    border-left: 4px solid #ff9800;
    padding: 20px;
    color: #e65100;
  }

  /* 6. CTA BOTTOM */
  .cta-section {
    text-align: center;
    margin-bottom: 80px;
    padding: 40px;
    background: white;
    box-shadow: 0 5px 20px rgba(0,0,0,0.05);
  }

</style>

<div class="visa-hero">
  <h1>Global Visa Intelligence Hub</h1>
  <p>Verified data on Visa Success, Total Costs, and PR Chances for Indian Students.</p>
</div>

<div class="tier-nav">
  <span class="tier-label">Tier 1: Most Popular</span>
  <div class="country-tabs">
    <button class="tab-btn active" onclick="openCountry('canada')">Canada</button>
    <button class="tab-btn" onclick="openCountry('australia')">Australia</button>
    <button class="tab-btn" onclick="openCountry('uk')">UK</button>
    <button class="tab-btn" onclick="openCountry('usa')">USA</button>
    <button class="tab-btn" onclick="openCountry('germany')">Germany</button>
  </div>
  
  <div style="margin-top:15px;">
    <span class="tier-label">Tier 2: Fast Growing</span>
    <div class="country-tabs">
      <button class="tab-btn" onclick="openCountry('ireland')">Ireland</button>
      <button class="tab-btn" onclick="openCountry('uae')">UAE (Dubai)</button>
      <button class="tab-btn" onclick="openCountry('france')">France</button>
      <button class="tab-btn" onclick="openCountry('nz')">New Zealand</button>
    </div>
  </div>
</div>

<div class="country-content">

  <div id="canada" class="visa-card active">
    <div class="vc-header">
      <img src="https://images.unsplash.com/photo-1517935706615-2717063c2225?w=1000&auto=format&fit=crop" class="vc-bg-img">
      <div class="vc-title-overlay">
        <h2>Canada</h2>
        <span class="vc-tag">PR Friendly Destination</span>
      </div>
    </div>

    <div class="vc-section">
      <h3 class="section-title">1. Visa Success Rate</h3>
      <table class="facts-table">
        <tr><td>Approval Chance</td><td>60-70% (SDS Category)</td></tr>
        <tr><td>Main Rejection Reason</td><td>Weak Financial Proof / Course Mismatch</td></tr>
        <tr><td>English Requirement</td><td>IELTS 6.0 Overall (SDS Rule)</td></tr>
        <tr><td>Backlogs Accepted</td><td>Up to 5-6 (varies by college)</td></tr>
      </table>
    </div>

    <div class="vc-section">
      <h3 class="section-title">2. Total Annual Cost</h3>
      <div class="cost-box">
        <div class="cost-row"><span>Average Tuition</span><span>15 - 25 Lakhs</span></div>
        <div class="cost-row"><span>Living Expenses (GIC)</span><span>12 - 13 Lakhs</span></div>
        <div class="cost-total"><div class="cost-row"><span>REALISTIC BUDGET</span><span>27 - 38 Lakhs / Year</span></div></div>
        <p style="font-size:0.9rem; color:#666; margin-top:10px;">*GIC amount is mandatory to show in advance.</p>
      </div>
    </div>

    <div class="vc-section">
      <h3 class="section-title">3. Part-Time Work Rules</h3>
      <p><strong>Hours:</strong> 20 Hours per week (Off-campus allowed).</p>
      <p><strong>During Breaks:</strong> Full-time work allowed.</p>
      <p><strong>Minimum Wage:</strong> approx CAD 15-17 per hour.</p>
    </div>

    <div class="vc-section">
      <h3 class="section-title">4. Post Study Work (PGWP)</h3>
      <p><strong>Duration:</strong> Up to 3 Years.</p>
      <p><strong>Rule:</strong> Course must be 2+ years for a 3-year permit. Shorter courses get shorter permits.</p>
    </div>

    <div class="vc-section">
      <h3 class="section-title">5. PR & Settlement</h3>
      <p><strong>Difficulty:</strong> Moderate.</p>
      <p><strong>Pathway:</strong> Canadian Experience Class (CEC) via Express Entry.</p>
      <p><strong>Timeline:</strong> Possible within 3-5 years if you secure a skilled job.</p>
    </div>

    <div class="vc-section">
      <h3 class="section-title">6. Intakes & Processing</h3>
      <p><strong>Primary Intake:</strong> September (Fall).</p>
      <p><strong>Secondary Intake:</strong> January (Winter).</p>
      <p><strong>Processing Time:</strong> 4 - 8 Weeks (SDS).</p>
    </div>

    <div class="vc-section">
      <h3 class="section-title">7. High Demand Courses</h3>
      <ul style="line-height:1.8;">
        <li>Health Administration</li>
        <li>Computer Science & IT</li>
        <li>Supply Chain Management</li>
        <li>Engineering Management</li>
      </ul>
    </div>

    <div class="vc-section" style="border-bottom:none;">
      <h3 class="section-title">8. Who Should NOT Choose Canada?</h3>
      <div class="warning-box">
        Do not choose Canada if you cannot handle extreme cold weather (-20C) or if you are looking for immediate PR without skilled work experience. The housing market in Toronto/Vancouver is currently very expensive.
      </div>
      <a href="{{ '/book-expert/' | relative_url }}" class="eligibility-check">Check Your Canada Eligibility in 30 Seconds</a>
    </div>
  </div>

  <div id="australia" class="visa-card">
    <div class="vc-header">
      <img src="https://images.unsplash.com/photo-1506973035872-a4ec16b8e8d9?w=1000&auto=format&fit=crop" class="vc-bg-img">
      <div class="vc-title-overlay">
        <h2>Australia</h2>
        <span class="vc-tag">High Lifestyle & Wages</span>
      </div>
    </div>

    <div class="vc-section">
      <h3 class="section-title">1. Visa Success Rate</h3>
      <table class="facts-table">
        <tr><td>Approval Chance</td><td>80-90% (Level 1 Universities)</td></tr>
        <tr><td>Main Rejection Reason</td><td>Non-Genuine Temporary Entrant (GTE)</td></tr>
        <tr><td>English Requirement</td><td>IELTS 6.5 Overall</td></tr>
        <tr><td>Gap Accepted</td><td>Strictly scrutinized</td></tr>
      </table>
    </div>

    <div class="vc-section">
      <h3 class="section-title">2. Total Annual Cost</h3>
      <div class="cost-box">
        <div class="cost-row"><span>Average Tuition</span><span>25 - 40 Lakhs</span></div>
        <div class="cost-row"><span>Living Expenses</span><span>15 - 18 Lakhs</span></div>
        <div class="cost-total"><div class="cost-row"><span>REALISTIC BUDGET</span><span>40 - 58 Lakhs / Year</span></div></div>
      </div>
    </div>

    <div class="vc-section">
      <h3 class="section-title">3. Part-Time Work Rules</h3>
      <p><strong>Hours:</strong> 48 Hours per fortnight (24 hrs/week).</p>
      <p><strong>Wage:</strong> Highest in the world (approx AUD 23/hour).</p>
    </div>

    <div class="vc-section">
      <h3 class="section-title">4. Post Study Work</h3>
      <p><strong>Duration:</strong> 2 to 4 Years.</p>
      <p><strong>Bonus:</strong> Extra years granted for studying in Regional Areas (Perth, Adelaide, Gold Coast).</p>
    </div>

    <div class="vc-section">
      <h3 class="section-title">5. PR & Settlement</h3>
      <p><strong>Difficulty:</strong> Hard (Points Based).</p>
      <p><strong>Pathway:</strong> General Skilled Migration (189/190 Visas).</p>
      <p><strong>Tip:</strong> Nursing, Teaching, and IT have higher PR chances.</p>
    </div>

    <div class="vc-section">
      <h3 class="section-title">6. Intakes & Processing</h3>
      <p><strong>Major Intakes:</strong> February and July.</p>
      <p><strong>Processing Time:</strong> 4 - 12 Weeks.</p>
    </div>

    <div class="vc-section">
      <h3 class="section-title">7. High Demand Courses</h3>
      <ul style="line-height:1.8;">
        <li>Nursing & Public Health</li>
        <li>Data Science</li>
        <li>Engineering (Civil/Mining)</li>
      </ul>
    </div>

    <div class="vc-section" style="border-bottom:none;">
      <h3 class="section-title">8. Who Should NOT Choose Australia?</h3>
      <div class="warning-box">
        Do not choose Australia if you are on a tight budget. Tuition and rent are very high. Also avoid if you have a large unexplained study gap.
      </div>
      <a href="{{ '/book-expert/' | relative_url }}" class="eligibility-check">Check Your Australia Eligibility in 30 Seconds</a>
    </div>
  </div>

  <div id="uk" class="visa-card">
    <div class="vc-header">
      <img src="https://images.unsplash.com/photo-1513635269975-59663e0ac1ad?w=1000&auto=format&fit=crop" class="vc-bg-img">
      <div class="vc-title-overlay">
        <h2>United Kingdom</h2>
        <span class="vc-tag">1-Year Masters</span>
      </div>
    </div>

    <div class="vc-section">
      <h3 class="section-title">1. Visa Success Rate</h3>
      <table class="facts-table">
        <tr><td>Approval Chance</td><td>95% (Very High)</td></tr>
        <tr><td>Main Rejection Reason</td><td>Credibility Interview Fail</td></tr>
        <tr><td>English Requirement</td><td>IELTS 6.5 (Waiver possible)</td></tr>
      </table>
    </div>

    <div class="vc-section">
      <h3 class="section-title">2. Total Annual Cost</h3>
      <div class="cost-box">
        <div class="cost-row"><span>Average Tuition</span><span>20 - 30 Lakhs</span></div>
        <div class="cost-row"><span>Living Expenses</span><span>12 - 15 Lakhs</span></div>
        <div class="cost-total"><div class="cost-row"><span>REALISTIC BUDGET</span><span>32 - 45 Lakhs (Total)</span></div></div>
        <p style="font-size:0.9rem; color:#666;">*Note: Masters is only 1 year, so this is the total cost.</p>
      </div>
    </div>

    <div class="vc-section">
      <h3 class="section-title">4. Post Study Work (Graduate Route)</h3>
      <p><strong>Duration:</strong> 2 Years flat.</p>
      <p><strong>Rule:</strong> You can work in any job (even cashier/driver) during these 2 years to recover costs.</p>
    </div>

    <div class="vc-section" style="border-bottom:none;">
      <h3 class="section-title">8. Who Should NOT Choose UK?</h3>
      <div class="warning-box">
        Do not choose UK if your primary goal is permanent settlement (PR). The PR route takes 5+ years of sponsored work, which is difficult to secure.
      </div>
      <a href="{{ '/book-expert/' | relative_url }}" class="eligibility-check">Check Your UK Eligibility in 30 Seconds</a>
    </div>
  </div>

  <div id="usa" class="visa-card">
    <div class="vc-header">
      <img src="https://images.unsplash.com/photo-1550951298-5c7b95a66b6a?w=1000&auto=format&fit=crop" class="vc-bg-img">
      <div class="vc-title-overlay">
        <h2>USA</h2>
        <span class="vc-tag">Highest Salaries</span>
      </div>
    </div>

    <div class="vc-section">
      <h3 class="section-title">1. Visa Success Rate</h3>
      <table class="facts-table">
        <tr><td>Approval Chance</td><td>80% (Interview Based)</td></tr>
        <tr><td>Main Rejection Reason</td><td>Applying to low-tier colleges</td></tr>
        <tr><td>English Requirement</td><td>TOEFL 90+ / IELTS 6.5</td></tr>
      </table>
    </div>

    <div class="vc-section">
      <h3 class="section-title">4. Post Study Work (OPT)</h3>
      <p><strong>STEM Degrees:</strong> 3 Years work permit.</p>
      <p><strong>Non-STEM:</strong> 1 Year work permit.</p>
    </div>

    <div class="vc-section" style="border-bottom:none;">
      <h3 class="section-title">8. Who Should NOT Choose USA?</h3>
      <div class="warning-box">
        Do not choose USA if you fear interviews. The visa depends entirely on a 2-minute interview officer's mood. Also avoid if doing non-STEM courses (only 1 year stay back).
      </div>
      <a href="{{ '/book-expert/' | relative_url }}" class="eligibility-check">Check Your USA Eligibility in 30 Seconds</a>
    </div>
  </div>

  <div id="germany" class="visa-card">
    <div class="vc-header">
      <img src="https://images.unsplash.com/photo-1564426544976-559d80d28222?w=1000&auto=format&fit=crop" class="vc-bg-img">
      <div class="vc-title-overlay">
        <h2>Germany</h2>
        <span class="vc-tag">Free Education</span>
      </div>
    </div>

    <div class="vc-section">
      <h3 class="section-title">2. Total Annual Cost</h3>
      <div class="cost-box">
        <div class="cost-row"><span>Tuition (Public)</span><span>ZERO</span></div>
        <div class="cost-row"><span>Living (Blocked Acc)</span><span>11 - 12 Lakhs</span></div>
        <div class="cost-total"><div class="cost-row"><span>REALISTIC BUDGET</span><span>12 Lakhs / Year</span></div></div>
      </div>
    </div>

    <div class="vc-section" style="border-bottom:none;">
      <h3 class="section-title">8. Who Should NOT Choose Germany?</h3>
      <div class="warning-box">
        Do not choose Germany if you are unwilling to learn the German language. While courses are in English, daily life and jobs require German skills.
      </div>
      <a href="{{ '/book-expert/' | relative_url }}" class="eligibility-check">Check Your Germany Eligibility in 30 Seconds</a>
    </div>
  </div>

  <div id="uae" class="visa-card">
    <div class="vc-header">
      <img src="https://images.unsplash.com/photo-1512453979798-5ea904ac6605?w=1000&auto=format&fit=crop" class="vc-bg-img">
      <div class="vc-title-overlay">
        <h2>UAE (Dubai)</h2>
        <span class="vc-tag">Luxury & Safety</span>
      </div>
    </div>

    <div class="vc-section">
      <h3 class="section-title">1. Visa Success Rate</h3>
      <table class="facts-table">
        <tr><td>Approval Chance</td><td>99% (Easiest)</td></tr>
        <tr><td>Processing Time</td><td>2-3 Weeks</td></tr>
        <tr><td>Sponsor</td><td>University sponsors Visa</td></tr>
      </table>
    </div>

    <div class="vc-section">
      <h3 class="section-title">4. Post Study Work</h3>
      <p><strong>Golden Visa:</strong> Outstanding students (GPA 3.8+) get a 5-10 year visa.</p>
      <p><strong>Standard:</strong> 1 Year renewable job-seeker visa.</p>
    </div>

    <div class="vc-section" style="border-bottom:none;">
      <h3 class="section-title">8. Who Should NOT Choose UAE?</h3>
      <div class="warning-box">
        Do not choose UAE if you want "Citizenship". You will likely never get a passport here. It is great for making money tax-free, but not for permanent immigration.
      </div>
      <a href="{{ '/book-expert/' | relative_url }}" class="eligibility-check">Check Your Dubai Eligibility in 30 Seconds</a>
    </div>
  </div>

  <div id="ireland" class="visa-card">
    <div class="vc-header">
      <img src="https://images.unsplash.com/photo-1590089415225-401cd6f9ad5d?w=1000&auto=format&fit=crop" class="vc-bg-img">
      <div class="vc-title-overlay">
        <h2>Ireland</h2>
        <span class="vc-tag">Europe's Tech Hub</span>
      </div>
    </div>

    <div class="vc-section">
      <h3 class="section-title">1. Visa Success Rate</h3>
      <table class="facts-table">
        <tr><td>Approval Chance</td><td>90-95%</td></tr>
        <tr><td>Main Requirement</td><td>Paid Fees + Finance Proof</td></tr>
      </table>
    </div>

    <div class="vc-section">
      <h3 class="section-title">4. Post Study Work</h3>
      <p><strong>Masters:</strong> 2 Years stay back.</p>
      <p><strong>Bachelors:</strong> 1 Year stay back.</p>
    </div>

    <div class="vc-section" style="border-bottom:none;">
      <h3 class="section-title">8. Who Should NOT Choose Ireland?</h3>
      <div class="warning-box">
        Do not choose Ireland if you are in a niche non-tech field. The market is small compared to UK/Germany. Housing in Dublin is notoriously difficult to find.
      </div>
      <a href="{{ '/book-expert/' | relative_url }}" class="eligibility-check">Check Your Ireland Eligibility in 30 Seconds</a>
    </div>
  </div>

</div>

<div class="cta-section">
  <h2>Confused by the Options?</h2>
  <p>Don't guess with your future. Get a verified profile evaluation.</p>
  <a href="{{ '/book-expert/' | relative_url }}" style="background: #0A2342; color: white; padding: 15px 40px; border-radius: 50px; text-decoration: none; font-weight: bold; font-size: 1.1rem; display:inline-block; margin-top:10px;">Talk to a Visa Expert</a>
</div>

<script>
  function openCountry(countryId) {
    // 1. Hide all cards
    const cards = document.querySelectorAll('.visa-card');
    cards.forEach(card => card.classList.remove('active'));

    // 2. Remove active class from all buttons
    const btns = document.querySelectorAll('.tab-btn');
    btns.forEach(btn => btn.classList.remove('active'));

    // 3. Show selected card
    document.getElementById(countryId).classList.add('active');
    
    // 4. Highlight clicked button
    event.currentTarget.classList.add('active');
  }
</script>
