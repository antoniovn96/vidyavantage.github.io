---
layout: default
title: "Global Visa Intelligence Hub"
permalink: /visas/
image: "https://images.unsplash.com/photo-1544256277-c93d8b377b30?w=1200&h=630&fit=crop"
description: "Compare student visas for USA, UK, Canada, Germany, France, New Zealand, and UAE. Check costs, work rights, and PR rules for Indian students."
---

<meta property="og:title" content="Global Visa Intelligence Hub - VidyaVantage" />
<meta property="og:description" content="Verified data on Visa Success, Total Costs, and PR Chances for Indian Students. Compare USA, UK, Canada, France & NZ." />
<meta property="og:image" content="https://images.unsplash.com/photo-1544256277-c93d8b377b30?w=1200&h=630&fit=crop" />
<meta property="twitter:card" content="summary_large_image" />

<style>
  /* 1. GLOBAL RESET */
  .main-content {
    max-width: 100% !important;
    padding: 0 !important;
    margin: 0 !important;
  }
  
  body { 
    background-color: #f4f7f6; 
    font-family: 'Segoe UI', Helvetica, Arial, sans-serif;
    color: #333;
  }

  /* 2. HERO SECTION */
  .visa-hero {
    background: linear-gradient(rgba(10, 35, 66, 0.9), rgba(10, 35, 66, 0.8)), url('https://images.unsplash.com/photo-1436491865332-7a61a109cc05?w=1600&auto=format&fit=crop');
    background-size: cover;
    background-position: center;
    color: white;
    text-align: center;
    padding: 100px 20px 80px;
    border-bottom: 4px solid #D4AF37;
  }
  
  .visa-hero h1 { 
    font-size: 3.5rem; 
    margin: 0 0 15px 0; 
    color: #ffffff !important; 
    text-shadow: 0 4px 15px rgba(0,0,0,0.6); 
    font-weight: 800;
  }
  
  .visa-hero p { 
    font-size: 1.2rem; 
    color: #ddd !important; 
    max-width: 700px;
    margin: 0 auto;
  }

  /* 3. TIER NAVIGATION (Tabs) */
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
    gap: 12px;
    flex-wrap: wrap;
  }

  .tab-btn {
    background: #f8f9fa;
    border: 1px solid #e9ecef;
    padding: 12px 25px;
    border-radius: 50px;
    font-size: 0.95rem;
    font-weight: 700;
    color: #555;
    cursor: pointer;
    transition: all 0.2s;
  }

  .tab-btn:hover { background: #e9ecef; transform: translateY(-2px); }
  
  .tab-btn.active {
    background: #0A2342;
    color: white;
    border-color: #0A2342;
    box-shadow: 0 4px 10px rgba(10, 35, 66, 0.3);
  }

  /* 4. CARD CONTAINER */
  .country-content {
    max-width: 900px;
    margin: 40px auto;
    padding: 0 20px;
  }

  .visa-card {
    background: white;
    border-radius: 16px;
    box-shadow: 0 10px 30px rgba(0,0,0,0.08);
    overflow: hidden;
    display: none; /* Hidden by default */
    margin-bottom: 60px;
  }
  
  .visa-card.active { display: block; animation: slideUp 0.4s ease-out; }

  @keyframes slideUp {
    from { opacity: 0; transform: translateY(20px); }
    to { opacity: 1; transform: translateY(0); }
  }

  /* 5. CARD HEADER */
  .vc-header {
    height: 250px;
    position: relative;
    color: white;
    overflow: hidden;
  }

  .vc-bg-img {
    width: 100%;
    height: 100%;
    object-fit: cover;
    transition: transform 0.5s;
  }
  
  .visa-card:hover .vc-bg-img {
    transform: scale(1.05);
  }

  .vc-overlay {
    position: absolute;
    top: 0; left: 0; right: 0; bottom: 0;
    background: linear-gradient(to top, rgba(10, 35, 66, 0.9) 0%, rgba(10, 35, 66, 0.1) 70%);
    padding: 30px;
    display: flex;
    flex-direction: column;
    justify-content: flex-end;
  }

  .vc-title h2 { 
    margin: 0; 
    font-size: 3rem; 
    font-weight: 800; 
    color: white !important;
    text-shadow: 0 2px 10px rgba(0,0,0,0.5);
  }
  
  .vc-tag { 
    background: #D4AF37; 
    color: #0A2342; 
    padding: 5px 12px; 
    font-weight: bold; 
    font-size: 0.9rem; 
    display: inline-block; 
    margin-bottom: 10px;
    border-radius: 4px;
    text-transform: uppercase;
  }

  /* 6. COLLAPSIBLE SECTIONS */
  details {
    border-bottom: 1px solid #eee;
    transition: all 0.3s;
  }

  details[open] {
    background: #fdfdfd;
    border-left: 5px solid #D4AF37;
  }

  summary {
    padding: 20px 25px;
    cursor: pointer;
    font-weight: bold;
    font-size: 1.1rem;
    color: #0A2342;
    display: flex;
    justify-content: space-between;
    align-items: center;
    list-style: none;
  }

  summary:hover { background: #f8f9fa; }

  summary:after {
    content: '+'; 
    font-size: 1.5rem;
    color: #D4AF37;
    font-weight: bold;
  }
  
  details[open] summary:after { content: '-'; }

  .details-content {
    padding: 0 25px 25px 25px;
    color: #555;
    line-height: 1.6;
    animation: fadeIn 0.3s;
  }

  /* Quick Facts Table */
  .facts-table {
    width: 100%;
    border-collapse: collapse;
    margin-bottom: 15px;
  }
  
  .facts-table td {
    padding: 12px 5px;
    border-bottom: 1px solid #eee;
    font-size: 1rem;
  }
  
  .facts-table td:first-child {
    font-weight: 600;
    color: #666;
    width: 40%;
  }

  .facts-table td:last-child {
    color: #0A2342;
    font-weight: 700;
  }

  /* Data Boxes */
  .data-box {
    background: white;
    border: 1px solid #e0e0e0;
    padding: 15px;
    border-radius: 8px;
    margin-bottom: 10px;
  }

  .data-label {
    font-size: 0.85rem;
    color: #888;
    text-transform: uppercase;
    letter-spacing: 0.5px;
    display: block;
    margin-bottom: 5px;
  }
  
  .data-value {
    font-size: 1.1rem;
    color: #0A2342;
    font-weight: bold;
  }

  .content-list {
    list-style: none;
    padding: 0;
  }
  .content-list li {
    padding: 8px 0;
    border-bottom: 1px solid #f0f0f0;
  }
  .content-list li:last-child { border-bottom: none; }

  .warning-msg {
    background: #fff3e0;
    color: #e65100;
    padding: 15px;
    border-radius: 6px;
    border-left: 4px solid #ff9800;
    font-weight: 500;
  }

  /* 7. CTA BUTTONS */
  .eligibility-btn {
    display: block;
    width: 100%;
    text-align: center;
    background: #e3f2fd;
    color: #0d47a1;
    padding: 15px;
    font-weight: bold;
    text-decoration: none;
    margin-top: 15px;
    border-radius: 8px;
    transition: background 0.2s;
  }
  .eligibility-btn:hover { background: #bbdefb; }

</style>

<div class="visa-hero">
  <h1>Global Visa Intelligence Hub</h1>
  <p>Verified data on Visa Success, Costs, and PR. <br>Click a country below to start.</p>
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
      <button class="tab-btn" onclick="openCountry('france')">France</button>
      <button class="tab-btn" onclick="openCountry('nz')">New Zealand</button>
      <button class="tab-btn" onclick="openCountry('ireland')">Ireland</button>
      <button class="tab-btn" onclick="openCountry('uae')">UAE</button>
    </div>
  </div>
</div>

<div class="country-content">

  <div id="canada" class="visa-card active">
    <div class="vc-header">
      <img src="https://images.unsplash.com/photo-1517935706615-2717063c2225?w=1000&auto=format&fit=crop" class="vc-bg-img">
      <div class="vc-overlay">
        <span class="vc-tag">#1 Choice for PR</span>
        <div class="vc-title"><h2>Canada</h2></div>
      </div>
    </div>

    <details open>
      <summary>📊 1. Quick Facts (At a Glance)</summary>
      <div class="details-content">
        <table class="facts-table">
          <tr><td>Intakes</td><td>Sep (Major), Jan, May</td></tr>
          <tr><td>IELTS Requirement</td><td>6.0 - 6.5 Overall</td></tr>
          <tr><td>Visa Success</td><td>High (if finances clear)</td></tr>
          <tr><td>Processing Time</td><td>4-8 Weeks</td></tr>
        </table>
      </div>
    </details>

    <details>
      <summary>💰 2. Total Cost to Study</summary>
      <div class="details-content">
        <div class="data-box">
          <span class="data-label">Tuition Fees (Per Year)</span>
          <ul class="content-list">
            <li><strong>Diploma:</strong> CAD 14,000 - 18,000</li>
            <li><strong>Bachelors:</strong> CAD 17,000 - 25,000</li>
            <li><strong>Masters:</strong> CAD 18,000 - 30,000</li>
          </ul>
        </div>
        <div class="data-box">
          <span class="data-label">Bank Balance Required</span>
          <span class="data-value">CAD 20,635 (GIC) + Tuition</span>
        </div>
        <div class="data-box" style="background:#e8f5e9; border-color:#c8e6c9;">
          <span class="data-label">Average Yearly Budget</span>
          <span class="data-value">₹18 - ₹28 Lakhs</span>
        </div>
      </div>
    </details>

    <details>
      <summary>💼 3. Part-Time Work Rules</summary>
      <div class="details-content">
        <div class="data-box">
          <span class="data-label">Allowed Hours</span>
          <span class="data-value">24 Hours / Week</span>
        </div>
        <div class="data-box">
          <span class="data-label">Minimum Wage</span>
          <span class="data-value">CAD 15 - 18 / Hour</span>
        </div>
        <div class="data-box">
          <span class="data-label">Monthly Earning</span>
          <span class="data-value">CAD 900 - 1,400 (Approx)</span>
        </div>
        <p><strong>Note:</strong> Spouse can work full-time in most programs.</p>
      </div>
    </details>

    <details>
      <summary>🎓 4. Post-Study Work Permit (PGWP)</summary>
      <div class="details-content">
        <table class="facts-table">
          <tr><td>1 Year Course</td><td>1 Year Work Permit</td></tr>
          <tr><td>2 Year Course</td><td>3 Year Work Permit</td></tr>
        </table>
        <p>This work experience is critical for applying for PR later.</p>
      </div>
    </details>

    <details>
      <summary>🏠 5. Permanent Residency (PR)</summary>
      <div class="details-content">
        <p>Canada is famous for settlement options. Most common routes:</p>
        <ul class="content-list">
          <li>Express Entry</li>
          <li>Provincial Nominee Program (PNP)</li>
          <li>Canadian Experience Class</li>
        </ul>
        <p><strong>Success Rate:</strong> Many students become PR within 2-4 years.</p>
      </div>
    </details>

    <details>
      <summary>🧠 6. High Demand Courses</summary>
      <div class="details-content">
        <ul class="content-list">
          <li>Healthcare & Nursing</li>
          <li>IT & Software / Data Analytics</li>
          <li>Construction & Civil</li>
          <li>Business & Supply Chain</li>
          <li>Early Childhood Education</li>
        </ul>
      </div>
    </details>

    <details>
      <summary>📅 7. Intakes & Timeline</summary>
      <div class="details-content">
        <table class="facts-table">
          <tr><td>September Intake</td><td>Apply by Jan - March</td></tr>
          <tr><td>January Intake</td><td>Apply by June - August</td></tr>
          <tr><td>May Intake</td><td>Apply by Oct - Nov</td></tr>
        </table>
      </div>
    </details>

    <details>
      <summary>⚠️ 8. Who Should / Should Not</summary>
      <div class="details-content">
        <div class="data-box">
          <span class="data-label">Good Profiles</span>
          <p>Moderate budget, Planning for PR, Willing to work part-time.</p>
        </div>
        <div class="warning-msg">
          <strong>Not Ideal For:</strong> Students with very low IELTS (below 6), no financial documents, or those who cannot handle cold weather.
        </div>
        <a href="{{ '/book-expert/' | relative_url }}" class="eligibility-btn">Check Free Eligibility for Canada</a>
      </div>
    </details>
  </div>

  <div id="australia" class="visa-card">
    <div class="vc-header">
      <img src="https://images.unsplash.com/photo-1523482580672-01e6f2eb6056?w=1000&auto=format&fit=crop" class="vc-bg-img">
      <div class="vc-overlay">
        <span class="vc-tag">High Salary & Job Market</span>
        <div class="vc-title"><h2>Australia</h2></div>
      </div>
    </div>

    <details open>
      <summary>📊 1. Quick Facts</summary>
      <div class="details-content">
        <table class="facts-table">
          <tr><td>Intakes</td><td>Feb (Major), July, Nov</td></tr>
          <tr><td>IELTS Requirement</td><td>6.0 - 6.5 Overall</td></tr>
          <tr><td>Processing Time</td><td>3 - 6 Weeks</td></tr>
          <tr><td>Work While Studying</td><td>24 Hours / Week</td></tr>
        </table>
      </div>
    </details>

    <details>
      <summary>💰 2. Total Cost to Study</summary>
      <div class="details-content">
        <div class="data-box">
          <span class="data-label">Tuition Fees (Per Year)</span>
          <ul class="content-list">
            <li><strong>Diploma:</strong> AUD 12,000 - 18,000</li>
            <li><strong>Bachelors:</strong> AUD 20,000 - 35,000</li>
            <li><strong>Masters:</strong> AUD 22,000 - 40,000</li>
          </ul>
        </div>
        <div class="data-box">
          <span class="data-label">Living & Funds</span>
          <span class="data-value">AUD 29,710/Year (Funds Required)</span>
        </div>
        <div class="data-box" style="background:#e8f5e9; border-color:#c8e6c9;">
          <span class="data-label">Average Yearly Budget</span>
          <span class="data-value">₹22 - ₹35 Lakhs</span>
        </div>
      </div>
    </details>

    <details>
      <summary>💼 3. Part-Time Work</summary>
      <div class="details-content">
        <div class="data-box">
          <span class="data-label">Hourly Wage</span>
          <span class="data-value">AUD 23+ (Highest Globally)</span>
        </div>
        <div class="data-box">
          <span class="data-label">Monthly Earning</span>
          <span class="data-value">AUD 1,500 - 2,200 Approx</span>
        </div>
        <p><strong>Spouse:</strong> Can work full-time if partner is in Masters.</p>
      </div>
    </details>

    <details>
      <summary>🎓 4. Post-Study Work (Subclass 485)</summary>
      <div class="details-content">
        <table class="facts-table">
          <tr><td>Diploma</td><td>18 Months</td></tr>
          <tr><td>Bachelors</td><td>2 - 3 Years</td></tr>
          <tr><td>Masters</td><td>3 - 5 Years</td></tr>
        </table>
      </div>
    </details>

    <details>
      <summary>🏠 5. Permanent Residency (PR)</summary>
      <div class="details-content">
        <p>PR is points-based. Easier if your course is on the Skill Shortage List.</p>
        <p><strong>Common Routes:</strong> 189/190 Visa or Employer Sponsorship.</p>
        <p><strong>Timeline:</strong> Possible in 3-6 years.</p>
      </div>
    </details>

    <details>
      <summary>🧠 6. High Demand Courses</summary>
      <div class="details-content">
        <ul class="content-list">
          <li>Nursing & Healthcare</li>
          <li>Social Work</li>
          <li>Engineering (Civil/Mech)</li>
          <li>IT & Cybersecurity</li>
          <li>Early Childhood Education</li>
        </ul>
      </div>
    </details>

    <details>
      <summary>📅 7. Intakes & Timeline</summary>
      <div class="details-content">
        <table class="facts-table">
          <tr><td>February Intake</td><td>Apply by Aug - Oct</td></tr>
          <tr><td>July Intake</td><td>Apply by Feb - April</td></tr>
          <tr><td>November Intake</td><td>Apply by May - June</td></tr>
        </table>
      </div>
    </details>

    <details>
      <summary>⚠️ 8. Who Should / Should Not</summary>
      <div class="details-content">
        <div class="data-box">
          <span class="data-label">Good Profiles</span>
          <p>Students wanting high salary, ready to work hard, and skilled professionals.</p>
        </div>
        <div class="warning-msg">
          <strong>Not Ideal For:</strong> Very low budget students or those with low English scores.
        </div>
        <a href="{{ '/book-expert/' | relative_url }}" class="eligibility-btn">Check Free Eligibility for Australia</a>
      </div>
    </details>
  </div>

  <div id="uk" class="visa-card">
    <div class="vc-header">
      <img src="https://images.unsplash.com/photo-1486299267070-83823f5448dd?w=1000&auto=format&fit=crop" class="vc-bg-img">
      <div class="vc-overlay">
        <span class="vc-tag">Fast Degree (1 Year)</span>
        <div class="vc-title"><h2>United Kingdom</h2></div>
      </div>
    </div>

    <details open>
      <summary>📊 1. Quick Facts</summary>
      <div class="details-content">
        <table class="facts-table">
          <tr><td>Intakes</td><td>Sep (Major), Jan, May</td></tr>
          <tr><td>IELTS Requirement</td><td>6.0 - 6.5</td></tr>
          <tr><td>Processing Time</td><td>~3 Weeks</td></tr>
          <tr><td>Work While Studying</td><td>20 Hours / Week</td></tr>
        </table>
      </div>
    </details>

    <details>
      <summary>💰 2. Total Cost to Study</summary>
      <div class="details-content">
        <div class="data-box">
          <span class="data-label">Tuition Fees</span>
          <ul class="content-list">
            <li><strong>Bachelors:</strong> £12,000 - 18,000 / Year</li>
            <li><strong>Masters:</strong> £14,000 - 22,000 (Total)</li>
          </ul>
        </div>
        <div class="data-box">
          <span class="data-label">Living Expenses</span>
          <span class="data-value">£800 - 1,200 / Month</span>
        </div>
        <div class="data-box" style="background:#e8f5e9; border-color:#c8e6c9;">
          <span class="data-label">Average Total Budget (Masters)</span>
          <span class="data-value">₹20 - ₹30 Lakhs (Complete)</span>
        </div>
      </div>
    </details>

    <details>
      <summary>💼 3. Part-Time Work</summary>
      <div class="details-content">
        <div class="data-box">
          <span class="data-label">Hourly Wage</span>
          <span class="data-value">£10 - £12 / Hour</span>
        </div>
        <div class="data-box">
          <span class="data-label">Monthly Earning</span>
          <span class="data-value">£700 - £1,000 Approx</span>
        </div>
        <p><strong>Spouse:</strong> Allowed mainly for PhD/Research students.</p>
      </div>
    </details>

    <details>
      <summary>🎓 4. Post-Study Work (Graduate Route)</summary>
      <div class="details-content">
        <table class="facts-table">
          <tr><td>Bachelors / Masters</td><td>2 Years</td></tr>
          <tr><td>PhD</td><td>3 Years</td></tr>
        </table>
        <p>No job offer is needed to stay during this period.</p>
      </div>
    </details>

    <details>
      <summary>🏠 5. PR & Settlement</summary>
      <div class="details-content">
        <p>Possible after obtaining a long-term work visa (Skilled Worker Route).</p>
        <p><strong>Timeline:</strong> About 5 years of working in the UK.</p>
      </div>
    </details>

    <details>
      <summary>🧠 6. High Demand Courses</summary>
      <div class="details-content">
        <ul class="content-list">
          <li>Business & Management</li>
          <li>Finance & Accounting</li>
          <li>Data Science / AI</li>
          <li>Healthcare & Public Health</li>
          <li>Law</li>
        </ul>
      </div>
    </details>

    <details>
      <summary>📅 7. Intakes & Timeline</summary>
      <div class="details-content">
        <table class="facts-table">
          <tr><td>September Intake</td><td>Apply by Jan - May</td></tr>
          <tr><td>January Intake</td><td>Apply by July - Sept</td></tr>
          <tr><td>May Intake</td><td>Apply by Oct - Nov</td></tr>
        </table>
      </div>
    </details>

    <details>
      <summary>⚠️ 8. Who Should / Should Not</summary>
      <div class="details-content">
        <div class="data-box">
          <span class="data-label">Good Profiles</span>
          <p>Students wanting a fast Master's (1 year) and career-focused individuals.</p>
        </div>
        <div class="warning-msg">
          <strong>Not Ideal For:</strong> Students only targeting PR without skills, or those with very low budgets.
        </div>
        <a href="{{ '/book-expert/' | relative_url }}" class="eligibility-btn">Check Free Eligibility for UK</a>
      </div>
    </details>
  </div>

  <div id="usa" class="visa-card">
    <div class="vc-header">
      <img src="https://images.unsplash.com/photo-1550951298-5c7b95a66b6a?w=1000&auto=format&fit=crop" class="vc-bg-img">
      <div class="vc-overlay">
        <span class="vc-tag">Highest Salaries</span>
        <div class="vc-title"><h2>United States</h2></div>
      </div>
    </div>
    <details open>
      <summary>🏁 1. Visa Success Rate</summary>
      <div class="details-content">
        <div class="data-box"><span class="data-label">Approval Chance</span><span class="data-value">80% (Interview Based)</span></div>
        <div class="data-box"><span class="data-label">Update</span><span class="data-value">Mandatory In-Person Interview</span></div>
      </div>
    </details>
    <details>
      <summary>💰 2. Total Cost Calculator</summary>
      <div class="details-content">
        <div class="data-box"><span class="data-label">Tuition</span><span class="data-value">₹25 - 50 Lakhs</span></div>
        <div class="data-box"><span class="data-label">Living</span><span class="data-value">₹12 - 18 Lakhs</span></div>
        <p><strong>Total Realistic Budget:</strong> ₹37 - 68 Lakhs / Year</p>
      </div>
    </details>
    <details>
      <summary>💼 3. Work Rules & PSW</summary>
      <div class="details-content">
        <div class="data-box"><span class="data-label">Part-Time</span><span class="data-value">20 Hrs (On-Campus Only)</span></div>
        <div class="data-box"><span class="data-label">OPT (Stay Back)</span><span class="data-value">3 Years (STEM Degrees)</span></div>
      </div>
    </details>
  </div>

  <div id="germany" class="visa-card">
    <div class="vc-header">
      <img src="https://images.unsplash.com/photo-1599946347371-88a312a783a1?w=1000&auto=format&fit=crop" class="vc-bg-img">
      <div class="vc-overlay">
        <span class="vc-tag">Free Education</span>
        <div class="vc-title"><h2>Germany</h2></div>
      </div>
    </div>
    <details open>
      <summary>💰 1. Total Cost</summary>
      <div class="details-content">
        <div class="data-box"><span class="data-label">Tuition (Public)</span><span class="data-value">ZERO</span></div>
        <div class="data-box"><span class="data-label">Living</span><span class="data-value">₹11 Lakhs / Year</span></div>
      </div>
    </details>
    <details>
      <summary>⚠️ 2. Warning</summary>
      <div class="details-content">
        <div class="warning-msg">Avoid if you won't learn German.</div>
      </div>
    </details>
  </div>

  <div id="france" class="visa-card">
    <div class="vc-header">
      <img src="https://images.unsplash.com/photo-1502602898657-3e91760cbb34?w=1000&auto=format&fit=crop" class="vc-bg-img">
      <div class="vc-overlay">
        <span class="vc-tag">5-Year Visa</span>
        <div class="vc-title"><h2>France</h2></div>
      </div>
    </div>
    <details open>
      <summary>💼 1. Special Benefits</summary>
      <div class="details-content">
        <div class="data-box"><span class="data-label">For Indian Masters</span><span class="data-value">5-Year Post Study Visa</span></div>
      </div>
    </details>
  </div>

  <div id="nz" class="visa-card">
    <div class="vc-header">
      <img src="https://images.unsplash.com/photo-1507699622177-388894d7023c?w=1000&auto=format&fit=crop" class="vc-bg-img">
      <div class="vc-overlay">
        <span class="vc-tag">Peaceful</span>
        <div class="vc-title"><h2>New Zealand</h2></div>
      </div>
    </div>
    <details open>
      <summary>💼 1. Work Rules</summary>
      <div class="details-content">
        <div class="data-box"><span class="data-label">Part-Time</span><span class="data-value">30 Hours/Week (Specific Courses)</span></div>
      </div>
    </details>
  </div>

  <div id="ireland" class="visa-card">
    <div class="vc-header">
      <img src="https://images.unsplash.com/photo-1590089415225-401cd6f9ad5d?w=1000&auto=format&fit=crop" class="vc-bg-img">
      <div class="vc-overlay">
        <span class="vc-tag">Europe's Tech Hub</span>
        <div class="vc-title"><h2>Ireland</h2></div>
      </div>
    </div>
    <details open>
      <summary>🏁 1. Visa Success</summary>
      <div class="details-content">
        <div class="data-box"><span class="data-label">Approval</span><span class="data-value">95%</span></div>
      </div>
    </details>
    <details>
      <summary>💰 2. Costs</summary>
      <div class="details-content">
        <div class="data-box"><span class="data-label">Tuition</span><span class="data-value">€15,000 - €20,000</span></div>
        <div class="data-box"><span class="data-label">Top Employers</span><span class="data-value">Google, Meta, Pfizer (Euro HQs)</span></div>
      </div>
    </details>
  </div>

  <div id="uae" class="visa-card">
    <div class="vc-header">
      <img src="https://images.unsplash.com/photo-1512453979798-5ea904ac6605?w=1000&auto=format&fit=crop" class="vc-bg-img">
      <div class="vc-overlay">
        <span class="vc-tag">Tax Free</span>
        <div class="vc-title"><h2>UAE (Dubai)</h2></div>
      </div>
    </div>
    <details open>
      <summary>🏁 1. Visa & Benefits</summary>
      <div class="details-content">
        <div class="data-box"><span class="data-label">Golden Visa</span><span class="data-value">10-Year Residency for Toppers</span></div>
        <div class="data-box"><span class="data-label">Income Tax</span><span class="data-value">0% (Tax Free Salary)</span></div>
      </div>
    </details>
  </div>

</div>

<div style="text-align: center; margin-bottom: 80px;">
  <p style="font-size:1.2rem; color:#555;">Don't guess with your future. Get a verified profile evaluation.</p>
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
