---
layout: default
title: "Global Visa Intelligence Hub 🌏"
permalink: /visas/
image: "/assets/images/visa-preview.png"
description: "Compare student visas for USA, UK, Canada, Germany, and Australia. Check costs, work rights, and PR rules for Indian students."
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
  .visa-hero {
    background: linear-gradient(135deg, #0A2342 0%, #16365f 100%);
    color: white;
    text-align: center;
    padding: 80px 20px 40px;
    border-bottom: 5px solid #D4AF37;
  }
  
  .visa-hero h1 { font-size: 3rem; margin: 0; text-shadow: 0 4px 10px rgba(0,0,0,0.3); }
  .visa-hero p { font-size: 1.2rem; color: #cbd5e0; margin-top: 10px; }

  /* 3. COUNTRY SELECTOR (Tabs) */
  .country-tabs {
    display: flex;
    justify-content: center;
    gap: 15px;
    flex-wrap: wrap;
    margin-top: -30px; /* Overlap hero */
    padding: 0 20px;
  }

  .tab-btn {
    background: white;
    border: none;
    padding: 15px 30px;
    border-radius: 50px;
    font-size: 1.1rem;
    font-weight: bold;
    color: #555;
    cursor: pointer;
    box-shadow: 0 5px 15px rgba(0,0,0,0.1);
    transition: all 0.3s;
    display: flex;
    align-items: center;
    gap: 10px;
  }

  .tab-btn:hover { transform: translateY(-3px); }
  
  .tab-btn.active {
    background: #D4AF37;
    color: #0A2342;
    transform: scale(1.05);
    box-shadow: 0 0 20px rgba(212, 175, 55, 0.4);
  }

  /* 4. CONTENT DISPLAY AREA */
  .country-content {
    max-width: 1000px;
    margin: 40px auto;
    padding: 20px;
  }

  .visa-card {
    background: white;
    border-radius: 20px;
    box-shadow: 0 10px 30px rgba(0,0,0,0.05);
    overflow: hidden;
    display: none; /* Hidden by default */
    animation: fadeIn 0.5s;
  }
  
  .visa-card.active { display: block; }

  @keyframes fadeIn {
    from { opacity: 0; transform: translateY(20px); }
    to { opacity: 1; transform: translateY(0); }
  }

  /* Card Header */
  .vc-header {
    background: #0A2342;
    color: white;
    padding: 30px;
    display: flex;
    justify-content: space-between;
    align-items: center;
    flex-wrap: wrap;
  }

  .vc-title h2 { margin: 0; font-size: 2.5rem; }
  .vc-tag { background: #D4AF37; color: #0A2342; padding: 5px 15px; border-radius: 4px; font-weight: bold; font-size: 0.9rem; margin-top: 5px; display: inline-block; }

  /* Data Grid */
  .vc-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
    gap: 30px;
    padding: 40px;
    background: white;
  }

  .data-point h4 { color: #888; font-size: 0.9rem; text-transform: uppercase; margin: 0 0 5px; }
  .data-point p { color: #0A2342; font-size: 1.3rem; font-weight: bold; margin: 0; }

  /* Verdict Section */
  .vc-verdict {
    background: #f1f5f9;
    padding: 30px 40px;
    border-top: 1px solid #e2e8f0;
  }

  .verdict-box {
    border-left: 5px solid #D4AF37;
    padding-left: 20px;
  }

  /* 5. ROADMAP STEPS */
  .roadmap-steps {
    max-width: 1000px;
    margin: 60px auto;
    padding: 20px;
  }
  
  .step-container {
    display: flex;
    justify-content: space-between;
    flex-wrap: wrap;
    gap: 20px;
  }

  .step-card {
    flex: 1;
    min-width: 180px;
    background: white;
    padding: 20px;
    border-radius: 10px;
    text-align: center;
    box-shadow: 0 5px 15px rgba(0,0,0,0.05);
    position: relative;
  }

  .step-num {
    background: #0A2342;
    color: white;
    width: 30px;
    height: 30px;
    border-radius: 50%;
    display: flex;
    align-items: center;
    justify-content: center;
    margin: 0 auto 10px;
    font-weight: bold;
  }

</style>

<div class="visa-hero">
  <h1>Your Ticket to the World ✈️</h1>
  <p>Verified Intelligence on Costs, Visas, and PR Rules for Indian Students.</p>
</div>

<div class="country-tabs">
  <button class="tab-btn active" onclick="openCountry('usa')">🇺🇸 USA</button>
  <button class="tab-btn" onclick="openCountry('uk')">🇬🇧 UK</button>
  <button class="tab-btn" onclick="openCountry('canada')">🇨🇦 Canada</button>
  <button class="tab-btn" onclick="openCountry('germany')">🇩🇪 Germany</button>
  <button class="tab-btn" onclick="openCountry('australia')">🇦🇺 Australia</button>
  <button class="tab-btn" onclick="openCountry('ireland')">🇮🇪 Ireland</button>
</div>

<div class="country-content">

  <div id="usa" class="visa-card active">
    <div class="vc-header">
      <div class="vc-title">
        <h2>United States</h2>
        <span class="vc-tag">Top Choice for Tech & STEM</span>
      </div>
      <div style="font-size: 3rem;">🗽</div>
    </div>
    <div class="vc-grid">
      <div class="data-point">
        <h4> Avg Tuition (Year)</h4>
        <p>₹25 - 50 Lakhs</p>
      </div>
      <div class="data-point">
        <h4>Living Cost (Year)</h4>
        <p>₹12 - 18 Lakhs</p>
      </div>
      <div class="data-point">
        <h4>Post-Study Visa</h4>
        <p>1 Year (General)<br>3 Years (STEM)</p>
      </div>
      <div class="data-point">
        <h4>Part-Time Work</h4>
        <p>20 Hrs/Week<br>(On-Campus Only)</p>
      </div>
      <div class="data-point">
        <h4>Key Exams</h4>
        <p>GRE / SAT / TOEFL</p>
      </div>
      <div class="data-point">
        <h4>Intakes</h4>
        <p>Fall (Aug) / Spring (Jan)</p>
      </div>
    </div>
    <div class="vc-verdict">
      <div class="verdict-box">
        <h3 style="margin-top:0; color:#0A2342;">The VidyaVantage Verdict:</h3>
        <p><strong>✅ Pros:</strong> Highest salaries in the world. Best for CS/IT engineers. 3-year stay back for STEM is a huge advantage.</p>
        <p><strong>⚠️ Cons:</strong> The H1B Visa (Work Visa) is a lottery system. Getting a Green Card can take 10+ years. High upfront cost.</p>
      </div>
    </div>
  </div>

  <div id="uk" class="visa-card">
    <div class="vc-header">
      <div class="vc-title">
        <h2>United Kingdom</h2>
        <span class="vc-tag">Best for Masters (1 Year)</span>
      </div>
      <div style="font-size: 3rem;">💂</div>
    </div>
    <div class="vc-grid">
      <div class="data-point">
        <h4>Avg Tuition (Year)</h4>
        <p>₹20 - 35 Lakhs</p>
      </div>
      <div class="data-point">
        <h4>Living Cost (Year)</h4>
        <p>₹12 - 15 Lakhs</p>
      </div>
      <div class="data-point">
        <h4>Post-Study Visa</h4>
        <p>2 Years (Graduate Route)</p>
      </div>
      <div class="data-point">
        <h4>Part-Time Work</h4>
        <p>20 Hrs/Week<br>(Off-Campus Allowed)</p>
      </div>
      <div class="data-point">
        <h4>Key Exams</h4>
        <p>IELTS / PTE (No GRE usually)</p>
      </div>
      <div class="data-point">
        <h4>Intakes</h4>
        <p>Sep (Major) / Jan</p>
      </div>
    </div>
    <div class="vc-verdict">
      <div class="verdict-box">
        <h3 style="margin-top:0; color:#0A2342;">The VidyaVantage Verdict:</h3>
        <p><strong>✅ Pros:</strong> Masters is only 1 year (saves time & money). "Graduate Route" visa guarantees 2 years to look for a job.</p>
        <p><strong>⚠️ Cons:</strong> Job market is tighter than USA. Dependent visas are now restricted for most courses.</p>
      </div>
    </div>
  </div>

  <div id="canada" class="visa-card">
    <div class="vc-header">
      <div class="vc-title">
        <h2>Canada</h2>
        <span class="vc-tag">The PR Pathway</span>
      </div>
      <div style="font-size: 3rem;">🍁</div>
    </div>
    <div class="vc-grid">
      <div class="data-point">
        <h4>Avg Tuition (Year)</h4>
        <p>₹15 - 30 Lakhs</p>
      </div>
      <div class="data-point">
        <h4>Living Cost (Year)</h4>
        <p>₹10 - 12 Lakhs (GIC)</p>
      </div>
      <div class="data-point">
        <h4>Post-Study Visa</h4>
        <p>Up to 3 Years (PGWP)</p>
      </div>
      <div class="data-point">
        <h4>Part-Time Work</h4>
        <p>20 Hrs/Week</p>
      </div>
      <div class="data-point">
        <h4>Key Exams</h4>
        <p>IELTS (Academic)</p>
      </div>
      <div class="data-point">
        <h4>Intakes</h4>
        <p>Sep / Jan / May</p>
      </div>
    </div>
    <div class="vc-verdict">
      <div class="verdict-box">
        <h3 style="margin-top:0; color:#0A2342;">The VidyaVantage Verdict:</h3>
        <p><strong>✅ Pros:</strong> Easiest route to Permanent Residency (PR). Community colleges offer cheaper, practical diplomas.</p>
        <p><strong>⚠️ Cons:</strong> Severe housing crisis in Toronto/Vancouver. Winters are brutal (-20°C). Recent caps on student visas.</p>
      </div>
    </div>
  </div>

  <div id="germany" class="visa-card">
    <div class="vc-header">
      <div class="vc-title">
        <h2>Germany</h2>
        <span class="vc-tag">Free Education (Public)</span>
      </div>
      <div style="font-size: 3rem;">🍺</div>
    </div>
    <div class="vc-grid">
      <div class="data-point">
        <h4>Avg Tuition (Year)</h4>
        <p>Almost ZERO (Public)</p>
      </div>
      <div class="data-point">
        <h4>Living Cost (Year)</h4>
        <p>~₹11 Lakhs (Blocked Acc)</p>
      </div>
      <div class="data-point">
        <h4>Post-Study Visa</h4>
        <p>18 Months</p>
      </div>
      <div class="data-point">
        <h4>Part-Time Work</h4>
        <p>20 Hrs/Week</p>
      </div>
      <div class="data-point">
        <h4>Key Exams</h4>
        <p>IELTS + Basic German (A1/A2)</p>
      </div>
      <div class="data-point">
        <h4>Intakes</h4>
        <p>Winter (Sep) / Summer (Mar)</p>
      </div>
    </div>
    <div class="vc-verdict">
      <div class="verdict-box">
        <h3 style="margin-top:0; color:#0A2342;">The VidyaVantage Verdict:</h3>
        <p><strong>✅ Pros:</strong> Tuition is free in public universities! Strongest economy in Europe for Automobile/Mechanical jobs.</p>
        <p><strong>⚠️ Cons:</strong> You MUST learn German to survive socially and get good jobs. University entry is very strict academically.</p>
      </div>
    </div>
  </div>

  <div id="australia" class="visa-card">
    <div class="vc-header">
      <div class="vc-title">
        <h2>Australia</h2>
        <span class="vc-tag">Lifestyle & Quality</span>
      </div>
      <div style="font-size: 3rem;">🦘</div>
    </div>
    <div class="vc-grid">
      <div class="data-point">
        <h4>Avg Tuition (Year)</h4>
        <p>₹25 - 40 Lakhs</p>
      </div>
      <div class="data-point">
        <h4>Living Cost (Year)</h4>
        <p>₹15 - 20 Lakhs</p>
      </div>
      <div class="data-point">
        <h4>Post-Study Visa</h4>
        <p>2 - 4 Years</p>
      </div>
      <div class="data-point">
        <h4>Part-Time Work</h4>
        <p>24 Hrs/Week (Increased)</p>
      </div>
      <div class="data-point">
        <h4>Key Exams</h4>
        <p>IELTS / PTE</p>
      </div>
      <div class="data-point">
        <h4>Intakes</h4>
        <p>Feb / July</p>
      </div>
    </div>
    <div class="vc-verdict">
      <div class="verdict-box">
        <h3 style="margin-top:0; color:#0A2342;">The VidyaVantage Verdict:</h3>
        <p><strong>✅ Pros:</strong> Amazing weather and quality of life. High minimum wage for part-time jobs. 3+ year stay back for regional areas.</p>
        <p><strong>⚠️ Cons:</strong> Very expensive. Visa rejection rates for Indians have increased recently. High cost of living in Sydney/Melbourne.</p>
      </div>
    </div>
  </div>

  <div id="ireland" class="visa-card">
    <div class="vc-header">
      <div class="vc-title">
        <h2>Ireland</h2>
        <span class="vc-tag">The Silicon Valley of Europe</span>
      </div>
      <div style="font-size: 3rem;">☘️</div>
    </div>
    <div class="vc-grid">
      <div class="data-point">
        <h4>Avg Tuition (Year)</h4>
        <p>₹12 - 25 Lakhs</p>
      </div>
      <div class="data-point">
        <h4>Living Cost (Year)</h4>
        <p>₹10 - 14 Lakhs</p>
      </div>
      <div class="data-point">
        <h4>Post-Study Visa</h4>
        <p>2 Years</p>
      </div>
      <div class="data-point">
        <h4>Part-Time Work</h4>
        <p>20 Hrs/Week</p>
      </div>
      <div class="data-point">
        <h4>Key Exams</h4>
        <p>IELTS / PTE</p>
      </div>
      <div class="data-point">
        <h4>Intakes</h4>
        <p>Sep / Jan</p>
      </div>
    </div>
    <div class="vc-verdict">
      <div class="verdict-box">
        <h3 style="margin-top:0; color:#0A2342;">The VidyaVantage Verdict:</h3>
        <p><strong>✅ Pros:</strong> English-speaking country in EU. Home to Google, Meta, Apple HQs (great tech jobs). Friendly locals.</p>
        <p><strong>⚠️ Cons:</strong> Smaller job market than UK/USA. Housing crisis in Dublin is severe.</p>
      </div>
    </div>
  </div>

</div>

<div class="roadmap-steps">
  <h2 style="text-align:center; color:#0A2342; margin-bottom:40px;">Your 5-Step Application Roadmap</h2>
  <div class="step-container">
    <div class="step-card">
      <div class="step-num">1</div>
      <h3>Profile Evaluation</h3>
      <p style="font-size:0.9rem; color:#666;">Check GPA & Budget. Choose Country.</p>
    </div>
    <div class="step-card">
      <div class="step-num">2</div>
      <h3>Tests Prep</h3>
      <p style="font-size:0.9rem; color:#666;">Prepare for IELTS/GRE. (3-4 Months)</p>
    </div>
    <div class="step-card">
      <div class="step-num">3</div>
      <h3>Applications</h3>
      <p style="font-size:0.9rem; color:#666;">Shortlist Universities & Apply.</p>
    </div>
    <div class="step-card">
      <div class="step-num">4</div>
      <h3>Finances & Visa</h3>
      <p style="font-size:0.9rem; color:#666;">Secure Loan, Pay Fees, Book Interview.</p>
    </div>
    <div class="step-card">
      <div class="step-num">5</div>
      <h3>Fly!</h3>
      <p style="font-size:0.9rem; color:#666;">Book tickets & housing. Start Dream.</p>
    </div>
  </div>
</div>

<div style="text-align: center; margin-bottom: 80px;">
  <p style="font-size:1.2rem; color:#555;">Confused by the rules? Don't risk a rejection.</p>
  <a href="{{ '/book-expert/' | relative_url }}" style="background: #0A2342; color: white; padding: 15px 40px; border-radius: 50px; text-decoration: none; font-weight: bold; font-size: 1.1rem; box-shadow: 0 4px 15px rgba(0,0,0,0.2);">Talk to a Visa Expert</a>
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
