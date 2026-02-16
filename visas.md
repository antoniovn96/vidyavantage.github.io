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
  
  body { background-color: #f0f2f5; font-family: 'Segoe UI', sans-serif; }

  /* 2. HERO SECTION */
  .visa-hero {
    background: linear-gradient(rgba(10, 35, 66, 0.9), rgba(10, 35, 66, 0.9)), url('https://images.unsplash.com/photo-1524813686514-a57563d77965?w=1200&auto=format&fit=crop');
    background-size: cover;
    background-position: center;
    color: white;
    text-align: center;
    padding: 100px 20px 60px;
    border-bottom: 5px solid #D4AF37;
  }
  
  /* FIXED: Title Visibility */
  .visa-hero h1 { 
    font-size: 3.5rem; 
    margin: 0; 
    color: #ffffff !important; 
    text-shadow: 0 4px 15px rgba(0,0,0,0.5); 
    font-weight: 800;
  }
  
  .visa-hero p { 
    font-size: 1.3rem; 
    color: #e0e0e0 !important; 
    margin-top: 15px; 
    font-weight: 500;
  }

  /* 3. COUNTRY SELECTOR (Tabs) */
  .country-tabs {
    display: flex;
    justify-content: center;
    gap: 15px;
    flex-wrap: wrap;
    margin-top: -35px;
    padding: 0 20px;
  }

  .tab-btn {
    background: white;
    border: none;
    padding: 15px 35px;
    border-radius: 50px;
    font-size: 1.1rem;
    font-weight: bold;
    color: #555;
    cursor: pointer;
    box-shadow: 0 10px 20px rgba(0,0,0,0.1);
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
    box-shadow: 0 0 25px rgba(212, 175, 55, 0.5);
  }

  /* 4. CONTENT DISPLAY AREA */
  .country-content {
    max-width: 1100px;
    margin: 50px auto;
    padding: 20px;
  }

  .visa-card {
    background: white;
    border-radius: 20px;
    box-shadow: 0 15px 40px rgba(0,0,0,0.1);
    overflow: hidden;
    display: none;
    animation: fadeIn 0.5s ease-out;
  }
  
  .visa-card.active { display: block; }

  @keyframes fadeIn {
    from { opacity: 0; transform: translateY(20px); }
    to { opacity: 1; transform: translateY(0); }
  }

  /* Card Header with IMAGE */
  .vc-header {
    height: 200px;
    position: relative;
    color: white;
    overflow: hidden;
  }

  .vc-bg-img {
    width: 100%;
    height: 100%;
    object-fit: cover;
    filter: brightness(0.6);
  }

  .vc-title-overlay {
    position: absolute;
    bottom: 20px;
    left: 30px;
    z-index: 2;
  }

  .vc-title-overlay h2 { margin: 0; font-size: 3rem; text-shadow: 0 2px 10px rgba(0,0,0,0.5); }
  .vc-tag { background: #D4AF37; color: #0A2342; padding: 5px 15px; border-radius: 4px; font-weight: bold; font-size: 1rem; display: inline-block; margin-top: 5px; }

  /* Data Grid */
  .vc-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
    gap: 30px;
    padding: 40px;
    background: white;
  }

  .data-point h4 { color: #888; font-size: 0.85rem; text-transform: uppercase; margin: 0 0 8px; letter-spacing: 1px; }
  .data-point p { color: #0A2342; font-size: 1.25rem; font-weight: bold; margin: 0; }

  /* NEW: EXAM SECTION */
  .exam-section {
    background: #f8f9fa;
    padding: 30px 40px;
    border-top: 1px solid #eee;
  }
  
  .exam-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
    gap: 20px;
    margin-top: 15px;
  }

  .exam-box {
    background: white;
    padding: 15px;
    border-radius: 8px;
    border-left: 4px solid #0A2342;
    box-shadow: 0 2px 5px rgba(0,0,0,0.05);
  }

  /* Verdict Section */
  .vc-verdict {
    background: #fff;
    padding: 30px 40px;
    border-top: 1px solid #eee;
  }

  .verdict-box {
    border-left: 5px solid #D4AF37;
    padding-left: 20px;
    background: #fffcf0;
    padding: 20px;
    border-radius: 0 10px 10px 0;
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
    padding: 25px 20px;
    border-radius: 15px;
    text-align: center;
    box-shadow: 0 5px 15px rgba(0,0,0,0.05);
    position: relative;
    border-bottom: 4px solid transparent;
    transition: all 0.3s;
  }

  .step-card:hover { transform: translateY(-5px); border-bottom-color: #D4AF37; }

  .step-num {
    background: #0A2342;
    color: white;
    width: 35px;
    height: 35px;
    border-radius: 50%;
    display: flex;
    align-items: center;
    justify-content: center;
    margin: 0 auto 15px;
    font-weight: bold;
    font-size: 1.1rem;
  }

</style>

<div class="visa-hero">
  <h1>Your Ticket to the World ✈️</h1>
  <p>Verified Intelligence on Costs, Visas, and Exams for Indian Students.</p>
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
      <img src="https://images.unsplash.com/photo-1550951298-5c7b95a66b6a?w=1000&auto=format&fit=crop" class="vc-bg-img">
      <div class="vc-title-overlay">
        <h2>United States</h2>
        <span class="vc-tag">#1 for Tech & Research</span>
      </div>
    </div>
    
    <div class="vc-grid">
      <div class="data-point"><h4>Avg Tuition (Year)</h4><p>₹25 - 50 Lakhs</p></div>
      <div class="data-point"><h4>Living Cost (Year)</h4><p>₹12 - 18 Lakhs</p></div>
      <div class="data-point"><h4>Stay Back Visa</h4><p>3 Years (STEM)</p></div>
      <div class="data-point"><h4>Part-Time Work</h4><p>20 Hrs (On-Campus)</p></div>
    </div>

    <div class="exam-section">
      <h3 style="margin-top:0; color:#0A2342;">📚 Required Exams & Scores</h3>
      <div class="exam-grid">
        <div class="exam-box">
          <strong>GRE (Graduate Record Exam)</strong>
          <p style="margin:5px 0; font-size:0.9rem; color:#666;">Essential for MS/PhD.</p>
          <div style="color:#2e7d32; font-weight:bold;">Target: 310+ / 340</div>
        </div>
        <div class="exam-box">
          <strong>TOEFL / IELTS</strong>
          <p style="margin:5px 0; font-size:0.9rem; color:#666;">English Proficiency.</p>
          <div style="color:#2e7d32; font-weight:bold;">Target: 90+ (TOEFL) or 6.5+ (IELTS)</div>
        </div>
        <div class="exam-box">
          <strong>SAT (Undergrad Only)</strong>
          <p style="margin:5px 0; font-size:0.9rem; color:#666;">For Bachelors degree.</p>
          <div style="color:#2e7d32; font-weight:bold;">Target: 1300+ / 1600</div>
        </div>
      </div>
    </div>

    <div class="vc-verdict">
      <div class="verdict-box">
        <h3 style="margin-top:0; color:#0A2342;">The VidyaVantage Verdict:</h3>
        <p><strong>✅ Pros:</strong> Highest salaries globally. OPT (Stay back) allows you to recover cost quickly.</p>
        <p><strong>⚠️ Cons:</strong> H1B Visa is a lottery. Strict interview process.</p>
      </div>
    </div>
  </div>

  <div id="uk" class="visa-card">
    <div class="vc-header">
      <img src="https://images.unsplash.com/photo-1513635269975-59663e0ac1ad?w=1000&auto=format&fit=crop" class="vc-bg-img">
      <div class="vc-title-overlay">
        <h2>United Kingdom</h2>
        <span class="vc-tag">Best for 1-Year Masters</span>
      </div>
    </div>
    
    <div class="vc-grid">
      <div class="data-point"><h4>Avg Tuition (Year)</h4><p>₹20 - 35 Lakhs</p></div>
      <div class="data-point"><h4>Living Cost (Year)</h4><p>₹12 - 15 Lakhs</p></div>
      <div class="data-point"><h4>Stay Back Visa</h4><p>2 Years (Graduate Route)</p></div>
      <div class="data-point"><h4>Part-Time Work</h4><p>20 Hrs (Off-Campus OK)</p></div>
    </div>

    <div class="exam-section">
      <h3 style="margin-top:0; color:#0A2342;">📚 Required Exams & Scores</h3>
      <div class="exam-grid">
        <div class="exam-box">
          <strong>IELTS Academic</strong>
          <p style="margin:5px 0; font-size:0.9rem; color:#666;">Mandatory for Visa.</p>
          <div style="color:#2e7d32; font-weight:bold;">Target: 6.5 (No Band < 6.0)</div>
        </div>
        <div class="exam-box">
          <strong>No GRE Required</strong>
          <p style="margin:5px 0; font-size:0.9rem; color:#666;">Most UK Universities do not ask for GRE.</p>
          <div style="color:#2e7d32; font-weight:bold;">Focus on GPA</div>
        </div>
      </div>
    </div>

    <div class="vc-verdict">
      <div class="verdict-box">
        <h3 style="margin-top:0; color:#0A2342;">The VidyaVantage Verdict:</h3>
        <p><strong>✅ Pros:</strong> Short duration (1 Year Masters). 2 Year guaranteed work search visa.</p>
        <p><strong>⚠️ Cons:</strong> Job market is competitive. High rent in London.</p>
      </div>
    </div>
  </div>

  <div id="canada" class="visa-card">
    <div class="vc-header">
      <img src="https://images.unsplash.com/photo-1517935706615-2717063c2225?w=1000&auto=format&fit=crop" class="vc-bg-img">
      <div class="vc-title-overlay">
        <h2>Canada</h2>
        <span class="vc-tag">The PR Pathway</span>
      </div>
    </div>
    
    <div class="vc-grid">
      <div class="data-point"><h4>Avg Tuition (Year)</h4><p>₹15 - 30 Lakhs</p></div>
      <div class="data-point"><h4>Living Cost (Year)</h4><p>₹20 Lakhs (GIC)</p></div>
      <div class="data-point"><h4>Stay Back Visa</h4><p>Up to 3 Years (PGWP)</p></div>
      <div class="data-point"><h4>Part-Time Work</h4><p>24 Hrs/Week</p></div>
    </div>

    <div class="exam-section">
      <h3 style="margin-top:0; color:#0A2342;">📚 Required Exams & Scores</h3>
      <div class="exam-grid">
        <div class="exam-box">
          <strong>IELTS Academic</strong>
          <p style="margin:5px 0; font-size:0.9rem; color:#666;">Strict requirement for SDS Visa.</p>
          <div style="color:#2e7d32; font-weight:bold;">Target: 6.0 in each band</div>
        </div>
        <div class="exam-box">
          <strong>PTE Academic</strong>
          <p style="margin:5px 0; font-size:0.9rem; color:#666;">Accepted by most colleges.</p>
          <div style="color:#2e7d32; font-weight:bold;">Target: 60+</div>
        </div>
      </div>
    </div>

    <div class="vc-verdict">
      <div class="verdict-box">
        <h3 style="margin-top:0; color:#0A2342;">The VidyaVantage Verdict:</h3>
        <p><strong>✅ Pros:</strong> Clear path to Permanent Residency (PR). Friendly to immigrants.</p>
        <p><strong>⚠️ Cons:</strong> Housing crisis in major cities. Extreme winter weather.</p>
      </div>
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
    
    <div class="vc-grid">
      <div class="data-point"><h4>Avg Tuition (Year)</h4><p>ZERO (Public)</p></div>
      <div class="data-point"><h4>Living Cost (Year)</h4><p>₹11 Lakhs (Blocked Acc)</p></div>
      <div class="data-point"><h4>Stay Back Visa</h4><p>18 Months</p></div>
      <div class="data-point"><h4>Part-Time Work</h4><p>20 Hrs/Week</p></div>
    </div>

    <div class="exam-section">
      <h3 style="margin-top:0; color:#0A2342;">📚 Required Exams & Scores</h3>
      <div class="exam-grid">
        <div class="exam-box">
          <strong>IELTS / TOEFL</strong>
          <p style="margin:5px 0; font-size:0.9rem; color:#666;">For English-taught programs.</p>
          <div style="color:#2e7d32; font-weight:bold;">Target: 6.5 Bands</div>
        </div>
        <div class="exam-box">
          <strong>German Language (Goethe)</strong>
          <p style="margin:5px 0; font-size:0.9rem; color:#666;">Highly recommended for jobs.</p>
          <div style="color:#2e7d32; font-weight:bold;">Level: A1/A2 (Basics)</div>
        </div>
        <div class="exam-box">
          <strong>GRE</strong>
          <p style="margin:5px 0; font-size:0.9rem; color:#666;">Required by top TU9 Universities.</p>
          <div style="color:#2e7d32; font-weight:bold;">Target: 315+</div>
        </div>
      </div>
    </div>

    <div class="vc-verdict">
      <div class="verdict-box">
        <h3 style="margin-top:0; color:#0A2342;">The VidyaVantage Verdict:</h3>
        <p><strong>✅ Pros:</strong> No tuition fees (save ₹30 Lakhs!). Strongest economy in Europe.</p>
        <p><strong>⚠️ Cons:</strong> Language barrier is real. Academic entry is very strict.</p>
      </div>
    </div>
  </div>

  <div id="australia" class="visa-card">
    <div class="vc-header">
      <img src="https://images.unsplash.com/photo-1506973035872-a4ec16b8e8d9?w=1000&auto=format&fit=crop" class="vc-bg-img">
      <div class="vc-title-overlay">
        <h2>Australia</h2>
        <span class="vc-tag">Lifestyle & Quality</span>
      </div>
    </div>
    
    <div class="vc-grid">
      <div class="data-point"><h4>Avg Tuition (Year)</h4><p>₹25 - 40 Lakhs</p></div>
      <div class="data-point"><h4>Living Cost (Year)</h4><p>₹15 - 20 Lakhs</p></div>
      <div class="data-point"><h4>Stay Back Visa</h4><p>2 - 4 Years</p></div>
      <div class="data-point"><h4>Part-Time Work</h4><p>24 Hrs/Week</p></div>
    </div>

    <div class="exam-section">
      <h3 style="margin-top:0; color:#0A2342;">📚 Required Exams & Scores</h3>
      <div class="exam-grid">
        <div class="exam-box">
          <strong>IELTS / PTE</strong>
          <p style="margin:5px 0; font-size:0.9rem; color:#666;">Strict Visa Requirement.</p>
          <div style="color:#2e7d32; font-weight:bold;">Target: 6.5 (No Band < 6.0)</div>
        </div>
      </div>
    </div>

    <div class="vc-verdict">
      <div class="verdict-box">
        <h3 style="margin-top:0; color:#0A2342;">The VidyaVantage Verdict:</h3>
        <p><strong>✅ Pros:</strong> High minimum wage. Great weather. Extra stay back for regional areas.</p>
        <p><strong>⚠️ Cons:</strong> Very expensive. Visa rejection rates for Indians are high currently.</p>
      </div>
    </div>
  </div>

  <div id="ireland" class="visa-card">
    <div class="vc-header">
      <img src="https://images.unsplash.com/photo-1590089415225-401cd6f9ad5d?w=1000&auto=format&fit=crop" class="vc-bg-img">
      <div class="vc-title-overlay">
        <h2>Ireland</h2>
        <span class="vc-tag">Silicon Valley of Europe</span>
      </div>
    </div>
    
    <div class="vc-grid">
      <div class="data-point"><h4>Avg Tuition (Year)</h4><p>₹12 - 25 Lakhs</p></div>
      <div class="data-point"><h4>Living Cost (Year)</h4><p>₹12 - 15 Lakhs</p></div>
      <div class="data-point"><h4>Stay Back Visa</h4><p>2 Years</p></div>
      <div class="data-point"><h4>Part-Time Work</h4><p>20 Hrs/Week</p></div>
    </div>

    <div class="exam-section">
      <h3 style="margin-top:0; color:#0A2342;">📚 Required Exams & Scores</h3>
      <div class="exam-grid">
        <div class="exam-box">
          <strong>IELTS / PTE</strong>
          <p style="margin:5px 0; font-size:0.9rem; color:#666;">Accepted by all colleges.</p>
          <div style="color:#2e7d32; font-weight:bold;">Target: 6.5 Bands</div>
        </div>
      </div>
    </div>

    <div class="vc-verdict">
      <div class="verdict-box">
        <h3 style="margin-top:0; color:#0A2342;">The VidyaVantage Verdict:</h3>
        <p><strong>✅ Pros:</strong> English speaking EU country. Home to Google/Meta HQs (Tech Jobs).</p>
        <p><strong>⚠️ Cons:</strong> Smaller job market than UK/US. Housing shortage in Dublin.</p>
      </div>
    </div>
  </div>

</div>

<div class="roadmap-steps">
  <h2 style="text-align:center; color:#0A2342; margin-bottom:40px;">Your 5-Step Application Roadmap</h2>
  <div class="step-container">
    <div class="step-card">
      <div class="step-num">1</div>
      <h3>Profile Check</h3>
      <p style="font-size:0.9rem; color:#666;">GPA & Budget Analysis.</p>
    </div>
    <div class="step-card">
      <div class="step-num">2</div>
      <h3>Tests Prep</h3>
      <p style="font-size:0.9rem; color:#666;">IELTS/GRE (3 Months).</p>
    </div>
    <div class="step-card">
      <div class="step-num">3</div>
      <h3>Apply</h3>
      <p style="font-size:0.9rem; color:#666;">Shortlist & Send Docs.</p>
    </div>
    <div class="step-card">
      <div class="step-num">4</div>
      <h3>Visa</h3>
      <p style="font-size:0.9rem; color:#666;">Loan & Embassy Interview.</p>
    </div>
    <div class="step-card">
      <div class="step-num">5</div>
      <h3>Fly!</h3>
      <p style="font-size:0.9rem; color:#666;">Housing & Travel.</p>
    </div>
  </div>
</div>

<div style="text-align: center; margin-bottom: 80px;">
  <p style="font-size:1.2rem; color:#555;">Don't let a small mistake reject your visa.</p>
  <a href="{{ '/book-expert/' | relative_url }}" style="background: #0A2342; color: white; padding: 15px 40px; border-radius: 50px; text-decoration: none; font-weight: bold; font-size: 1.1rem; box-shadow: 0 4px 15px rgba(0,0,0,0.2); transition: transform 0.2s;">Talk to a Visa Expert</a>
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
