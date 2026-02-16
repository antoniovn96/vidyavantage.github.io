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

  /* 5. CARD HEADER (FIXED VISIBILITY) */
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

  /* Gradient Overlay for Text Readability */
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

  /* 6. COLLAPSIBLE SECTIONS (ACCORDION) */
  details {
    border-bottom: 1px solid #eee;
    transition: all 0.3s;
  }

  details[open] {
    background: #fdfdfd;
    border-left: 5px solid #D4AF37; /* Gold highlight when open */
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
    list-style: none; /* Hides default triangle */
  }

  summary:hover { background: #f8f9fa; }

  /* Custom + Icon */
  summary:after {
    content: '+'; 
    font-size: 1.5rem;
    color: #D4AF37;
    font-weight: bold;
  }
  
  details[open] summary:after { content: '-'; }

  /* The Content Inside */
  .details-content {
    padding: 0 25px 25px 25px;
    color: #555;
    line-height: 1.6;
    animation: fadeIn 0.3s;
  }

  /* Data Boxes inside accordion */
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

  /* Warning Box Style */
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
    <button class="tab-btn active" onclick="openCountry('usa')">USA</button>
    <button class="tab-btn" onclick="openCountry('canada')">Canada</button>
    <button class="tab-btn" onclick="openCountry('uk')">UK</button>
    <button class="tab-btn" onclick="openCountry('australia')">Australia</button>
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

  <div id="usa" class="visa-card active">
    <div class="vc-header">
      <img src="https://images.unsplash.com/photo-1534270804882-6b5048b1c1fc?w=1000&auto=format&fit=crop" class="vc-bg-img">
      <div class="vc-overlay">
        <span class="vc-tag">Highest Salaries</span>
        <div class="vc-title"><h2>United States</h2></div>
      </div>
    </div>

    <details open>
      <summary>🏁 1. Visa Success Rate</summary>
      <div class="details-content">
        <div class="data-box">
          <span class="data-label">Approval Chance</span>
          <span class="data-value">80% (Interview Based)</span>
        </div>
        <div class="data-box">
          <span class="data-label">2025 Update</span>
          <span class="data-value">Mandatory In-Person Interview. No waivers.</span>
        </div>
        <div class="data-box">
          <span class="data-label">Exams Needed</span>
          <span class="data-value">TOEFL 90+ / IELTS 6.5</span>
        </div>
      </div>
    </details>

    <details>
      <summary>💰 2. Total Cost Calculator</summary>
      <div class="details-content">
        <div class="data-box">
          <span class="data-label">Tuition Fee</span>
          <span class="data-value">₹25 - 50 Lakhs / Year</span>
        </div>
        <div class="data-box">
          <span class="data-label">Living Expenses</span>
          <span class="data-value">₹12 - 18 Lakhs / Year</span>
        </div>
        <p><strong>Total Realistic Budget:</strong> ₹37 - 68 Lakhs / Year</p>
      </div>
    </details>

    <details>
      <summary>💼 3. Work Rules & PSW</summary>
      <div class="details-content">
        <div class="data-box">
          <span class="data-label">Part-Time Work</span>
          <span class="data-value">20 Hrs/Week (Strictly On-Campus)</span>
        </div>
        <div class="data-box">
          <span class="data-label">Post Study Work (OPT)</span>
          <span class="data-value">3 Years (For STEM Degrees)</span>
        </div>
        <p><em>Warning: Off-campus work is illegal without permission.</em></p>
      </div>
    </details>

    <details>
      <summary>🛂 4. PR & Settlement</summary>
      <div class="details-content">
        <div class="data-box">
          <span class="data-label">Difficulty</span>
          <span class="data-value">Very Hard (10+ Years)</span>
        </div>
        <p>You need the H1B Visa (Lottery System). Do not go to the USA if your only goal is quick citizenship.</p>
      </div>
    </details>

    <details>
      <summary>⚠️ 5. Who Should AVOID?</summary>
      <div class="details-content">
        <div class="warning-msg">
          Do not choose USA if you have a weak financial background or fear interviews. Rejection rates for non-STEM courses are higher.
        </div>
        <a href="{{ '/book-expert/' | relative_url }}" class="eligibility-btn">Check Eligibility Now</a>
      </div>
    </details>
  </div>

  <div id="canada" class="visa-card">
    <div class="vc-header">
      <img src="https://images.unsplash.com/photo-1517935706615-2717063c2225?w=1000&auto=format&fit=crop" class="vc-bg-img">
      <div class="vc-overlay">
        <span class="vc-tag">PR Friendly</span>
        <div class="vc-title"><h2>Canada</h2></div>
      </div>
    </div>

    <details open>
      <summary>🏁 1. Visa Success Rate</summary>
      <div class="details-content">
        <div class="data-box">
          <span class="data-label">Approval Chance</span>
          <span class="data-value">60-70% (SDS Category)</span>
        </div>
        <div class="data-box">
          <span class="data-label">Key Requirement</span>
          <span class="data-value">IELTS 6.0 Overall (Strict for SDS)</span>
        </div>
      </div>
    </details>

    <details>
      <summary>💰 2. Total Cost Calculator</summary>
      <div class="details-content">
        <div class="data-box">
          <span class="data-label">Tuition Fee</span>
          <span class="data-value">₹15 - 25 Lakhs / Year</span>
        </div>
        <div class="data-box">
          <span class="data-label">Living (GIC)</span>
          <span class="data-value">₹13 Lakhs (Mandatory Deposit)</span>
        </div>
        <p><strong>Total Realistic Budget:</strong> ₹28 - 38 Lakhs / Year</p>
      </div>
    </details>

    <details>
      <summary>💼 3. Work Rules & PSW</summary>
      <div class="details-content">
        <div class="data-box">
          <span class="data-label">Part-Time Work</span>
          <span class="data-value">20 Hrs/Week (Off-campus allowed)</span>
        </div>
        <div class="data-box">
          <span class="data-label">Stay Back (PGWP)</span>
          <span class="data-value">Up to 3 Years</span>
        </div>
      </div>
    </details>

    <details>
      <summary>🛂 4. PR & Settlement</summary>
      <div class="details-content">
        <div class="data-box">
          <span class="data-label">Difficulty</span>
          <span class="data-value">Moderate (Points System)</span>
        </div>
        <p>Best country for PR. You can get it within 3-4 years via Express Entry.</p>
      </div>
    </details>

    <details>
      <summary>⚠️ 5. Who Should AVOID?</summary>
      <div class="details-content">
        <div class="warning-msg">
          Avoid if you hate extreme cold (-20°C). Housing in Toronto/Vancouver is very expensive right now.
        </div>
        <a href="{{ '/book-expert/' | relative_url }}" class="eligibility-btn">Check Eligibility Now</a>
      </div>
    </details>
  </div>

  <div id="uk" class="visa-card">
    <div class="vc-header">
      <img src="https://images.unsplash.com/photo-1486299267070-83823f5448dd?w=1000&auto=format&fit=crop" class="vc-bg-img">
      <div class="vc-overlay">
        <span class="vc-tag">1-Year Masters</span>
        <div class="vc-title"><h2>United Kingdom</h2></div>
      </div>
    </div>

    <details open>
      <summary>🏁 1. Visa Success Rate</summary>
      <div class="details-content">
        <div class="data-box">
          <span class="data-label">Approval Chance</span>
          <span class="data-value">95% (Very High)</span>
        </div>
        <div class="data-box">
          <span class="data-label">Exams</span>
          <span class="data-value">IELTS 6.5 (Often waived)</span>
        </div>
      </div>
    </details>

    <details>
      <summary>💰 2. Total Cost Calculator</summary>
      <div class="details-content">
        <div class="data-box">
          <span class="data-label">Tuition Fee</span>
          <span class="data-value">₹20 - 30 Lakhs (Total for 1 Year)</span>
        </div>
        <div class="data-box">
          <span class="data-label">Living</span>
          <span class="data-value">₹12 - 15 Lakhs</span>
        </div>
      </div>
    </details>

    <details>
      <summary>💼 3. Work Rules & PSW</summary>
      <div class="details-content">
        <div class="data-box">
          <span class="data-label">Stay Back Visa</span>
          <span class="data-value">2 Years (Graduate Route)</span>
        </div>
        <p>You can work in ANY job (even non-field jobs) for 2 years after graduating.</p>
      </div>
    </details>

    <details>
      <summary>⚠️ 4. Who Should AVOID?</summary>
      <div class="details-content">
        <div class="warning-msg">
          Avoid if you need PR quickly. Settling in the UK takes 5+ years of sponsored work, which is hard to find.
        </div>
        <a href="{{ '/book-expert/' | relative_url }}" class="eligibility-btn">Check Eligibility Now</a>
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
      <summary>🏁 1. Visa Success Rate</summary>
      <div class="details-content">
        <div class="data-box">
          <span class="data-label">Approval Chance</span>
          <span class="data-value">High (If university admits you)</span>
        </div>
      </div>
    </details>

    <details>
      <summary>💰 2. Total Cost Calculator</summary>
      <div class="details-content">
        <div class="data-box">
          <span class="data-label">Tuition (Public)</span>
          <span class="data-value">ZERO (Free)</span>
        </div>
        <div class="data-box">
          <span class="data-label">Living (Blocked Acc)</span>
          <span class="data-value">₹11 Lakhs / Year</span>
        </div>
      </div>
    </details>

    <details>
      <summary>⚠️ 3. Who Should AVOID?</summary>
      <div class="details-content">
        <div class="warning-msg">
          Avoid if you are not willing to learn German. English works in class, but not for jobs or daily life.
        </div>
      </div>
    </details>
  </div>

  <div id="australia" class="visa-card">
    <div class="vc-header">
      <img src="https://images.unsplash.com/photo-1523482580672-01e6f2eb6056?w=1000&auto=format&fit=crop" class="vc-bg-img">
      <div class="vc-overlay">
        <span class="vc-tag">High Wages</span>
        <div class="vc-title"><h2>Australia</h2></div>
      </div>
    </div>

    <details open>
      <summary>🏁 1. Visa Success Rate</summary>
      <div class="details-content">
        <div class="data-box">
          <span class="data-label">Approval Chance</span>
          <span class="data-value">80% (Strict GTE Check)</span>
        </div>
      </div>
    </details>

    <details>
      <summary>💰 2. Total Cost Calculator</summary>
      <div class="details-content">
        <div class="data-box">
          <span class="data-label">Tuition Fee</span>
          <span class="data-value">₹25 - 40 Lakhs / Year</span>
        </div>
        <div class="data-box">
          <span class="data-label">Living</span>
          <span class="data-value">₹15 - 18 Lakhs / Year</span>
        </div>
      </div>
    </details>

    <details>
      <summary>💼 3. Work Rules</summary>
      <div class="details-content">
        <div class="data-box">
          <span class="data-label">Part-Time Wage</span>
          <span class="data-value">Highest in the world (~AUD 23/hr)</span>
        </div>
        <div class="data-box">
          <span class="data-label">Post Study Work</span>
          <span class="data-value">2 - 4 Years</span>
        </div>
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
      <summary>🏁 1. Visa Success Rate</summary>
      <div class="details-content">
        <div class="data-box">
          <span class="data-label">Process</span>
          <span class="data-value">Campus France Interview Mandatory</span>
        </div>
      </div>
    </details>

    <details>
      <summary>💼 2. Special Benefits</summary>
      <div class="details-content">
        <div class="data-box">
          <span class="data-label">For Indian Masters</span>
          <span class="data-value">5-Year Post Study Work Visa</span>
        </div>
        <p>This is a special diplomatic rule for Indian students completing a Masters in France.</p>
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
      <summary>🏁 1. Visa Success Rate</summary>
      <div class="details-content">
        <div class="data-box">
          <span class="data-label">Scrutiny</span>
          <span class="data-value">High Financial Check (Funds must be 6 months old)</span>
        </div>
      </div>
    </details>

    <details>
      <summary>💼 2. Work Rules</summary>
      <div class="details-content">
        <div class="data-box">
          <span class="data-label">Part-Time</span>
          <span class="data-value">30 Hours/Week (Allowed for some courses)</span>
        </div>
        <div class="data-box">
          <span class="data-label">Post Study Work</span>
          <span class="data-value">Up to 3 Years</span>
        </div>
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
      <summary>🏁 1. Visa Success Rate</summary>
      <div class="details-content">
        <div class="data-box"><span class="data-label">Approval</span><span class="data-value">95%</span></div>
        <div class="data-box"><span class="data-label">Critical Skills</span><span class="data-value">Work Permit for Tech/Pharma roles</span></div>
      </div>
    </details>
    <details>
      <summary>💰 2. Costs & Companies</summary>
      <div class="details-content">
        <div class="data-box"><span class="data-label">Tuition</span><span class="data-value">€15,000 - €20,000</span></div>
        <div class="data-box"><span class="data-label">Top Employers</span><span class="data-value">Google, Meta, Pfizer, Apple (Euro HQs)</span></div>
      </div>
    </details>
  </div>

  <div id="uae" class="visa-card">
    <div class="vc-header">
      <img src="https://images.unsplash.com/photo-1512453979798-5ea904ac6605?w=1000&auto=format&fit=crop" class="vc-bg-img">
      <div class="vc-overlay">
        <span class="vc-tag">Tax Free & Safe</span>
        <div class="vc-title"><h2>UAE (Dubai)</h2></div>
      </div>
    </div>
    <details open>
      <summary>🏁 1. Visa & Benefits</summary>
      <div class="details-content">
        <div class="data-box"><span class="data-label">Success Rate</span><span class="data-value">99% (University Sponsored)</span></div>
        <div class="data-box"><span class="data-label">Golden Visa</span><span class="data-value">10-Year Residency for Toppers (GPA 3.8+)</span></div>
      </div>
    </details>
    <details>
      <summary>💰 2. Cost & Lifestyle</summary>
      <div class="details-content">
        <div class="data-box"><span class="data-label">Tuition</span><span class="data-value">40k - 70k AED / Year</span></div>
        <div class="data-box"><span class="data-label">Income Tax</span><span class="data-value">0% (Keep 100% of your salary)</span></div>
        <div class="data-box"><span class="data-label">Safety</span><span class="data-value">Ranked #1 Safest City Globally</span></div>
      </div>
    </details>
    <details>
      <summary>⚠️ 3. Warning</summary>
      <div class="details-content">
        <div class="warning-msg">No Citizenship possible. Good for earning money, not settling permanently.</div>
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
