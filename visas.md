---
layout: default
title: Global Visa Services 🌏
permalink: /visa/
image: "https://images.unsplash.com/photo-1436491865332-7a61a109cc05?ixlib=rb-4.0.3&auto=format&fit=crop&w=1200&q=80"
description: "Expert Visa Assistance for USA, UK, Canada, Australia, Germany, and more. Student, Tourist, and Work Visas made easy."
---

<style>
  /* --- VARIABLES & RESET --- */
  :root {
    --primary: #0A2342; /* Deep Navy */
    --accent: #F39C12; /* Golden/Passport Color */
    --bg-light: #F9FAFB;
    --text-dark: #1F2937;
    --text-muted: #6B7280;
    --card-shadow: 0 10px 30px rgba(0,0,0,0.06);
    --hover-shadow: 0 20px 40px rgba(0,0,0,0.12);
    --success: #10B981;
  }

  body {
    background-color: var(--bg-light);
    font-family: 'Segoe UI', system-ui, sans-serif;
    margin: 0;
  }

  /* --- 1. HERO SECTION --- */
  .visa-hero {
    background: linear-gradient(135deg, rgba(10, 35, 66, 0.95), rgba(10, 35, 66, 0.8)), 
                url('https://images.unsplash.com/photo-1436491865332-7a61a109cc05?ixlib=rb-4.0.3&auto=format&fit=crop&w=1600&q=80');
    background-size: cover;
    background-position: center;
    color: white;
    text-align: center;
    padding: 100px 20px 120px;
    border-radius: 0 0 50% 50% / 40px; 
    margin-bottom: 60px;
  }
  
  .hero-badge {
    display: inline-block;
    background: rgba(255,255,255,0.15);
    backdrop-filter: blur(10px);
    border: 1px solid rgba(255,255,255,0.2);
    padding: 8px 20px;
    border-radius: 50px;
    font-size: 0.9rem;
    font-weight: 600;
    text-transform: uppercase;
    letter-spacing: 1px;
    margin-bottom: 20px;
    color: #F39C12;
  }

  .visa-hero h1 { font-size: 3.5rem; margin: 0 0 15px; font-weight: 800; letter-spacing: -1px; }
  .visa-hero p { font-size: 1.25rem; max-width: 700px; margin: 0 auto; color: #E5E7EB; line-height: 1.6; }

  /* --- 2. PROCESS STEPS (Floating) --- */
  .process-container { max-width: 1000px; margin: -90px auto 80px; padding: 0 20px; position: relative; z-index: 10; }
  .process-card { background: white; border-radius: 16px; padding: 40px; box-shadow: 0 15px 50px rgba(0,0,0,0.1); display: grid; grid-template-columns: repeat(4, 1fr); gap: 20px; text-align: center; }
  .step-item { position: relative; }
  .step-item:not(:last-child)::after { content: '→'; position: absolute; top: 25%; right: -15px; color: #E5E7EB; font-size: 1.5rem; font-weight: 300; }
  .step-icon { width: 60px; height: 60px; background: #EFF6FF; color: var(--primary); border-radius: 50%; display: flex; align-items: center; justify-content: center; font-size: 1.5rem; margin: 0 auto 15px; transition: 0.3s; }
  .step-item:hover .step-icon { background: var(--primary); color: white; transform: scale(1.1); }
  .step-title { font-weight: 700; color: var(--text-dark); margin-bottom: 5px; font-size: 1.1rem; }
  .step-desc { font-size: 0.9rem; color: var(--text-muted); line-height: 1.4; }

  /* --- GLOBAL SHARED STYLES --- */
  .section-wrap { padding: 80px 20px; }
  .section-title { text-align: center; font-size: 2.5rem; font-weight: 800; color: var(--text-dark); margin-bottom: 10px; letter-spacing: -1px;}
  .section-subtitle { text-align: center; color: var(--text-muted); margin-bottom: 50px; font-size: 1.15rem; max-width: 700px; margin-left: auto; margin-right: auto;}
  .alt-bg { background: white; }

  /* --- 3. LEAD CAPTURE FORM --- */
  .lead-container { max-width: 800px; margin: 0 auto; background: white; border-radius: 20px; padding: 40px; box-shadow: var(--card-shadow); border-top: 5px solid var(--accent); }
  .form-grid { display: grid; grid-template-columns: 1fr 1fr; gap: 20px; margin-bottom: 20px;}
  .form-input, .form-select { width: 100%; padding: 14px; border: 2px solid #E5E7EB; border-radius: 8px; font-size: 1rem; box-sizing: border-box; font-family: inherit; transition: 0.3s;}
  .form-input:focus, .form-select:focus { border-color: var(--primary); outline: none;}
  .btn-submit { background: var(--primary); color: white; border: none; width: 100%; padding: 16px; font-size: 1.1rem; font-weight: bold; border-radius: 8px; cursor: pointer; transition: 0.3s;}
  .btn-submit:hover { background: #07182e; transform: translateY(-2px);}

  /* --- 4. WHY CHOOSE US (AUTHORITY) --- */
  .authority-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 20px; max-width: 1000px; margin: 0 auto;}
  .auth-card { background: var(--bg-light); padding: 25px; border-radius: 12px; text-align: center; border: 1px solid #E5E7EB;}
  .auth-icon { font-size: 2.5rem; margin-bottom: 15px; color: var(--accent);}
  .auth-card h4 { margin: 0 0 10px 0; color: var(--primary); font-size: 1.1rem;}

  /* --- 5. THE 100% FREE PACKAGE --- */
  .free-package-box { background: linear-gradient(135deg, var(--primary), #1a365d); color: white; max-width: 1000px; margin: 0 auto; border-radius: 20px; padding: 50px; text-align: center; position: relative; overflow: hidden;}
  .free-badge { background: var(--success); color: white; padding: 8px 20px; border-radius: 50px; font-weight: 900; font-size: 1.1rem; text-transform: uppercase; margin-bottom: 20px; display: inline-block; letter-spacing: 1px;}
  .package-grid { display: grid; grid-template-columns: 1fr 1fr 1fr; gap: 20px; margin-top: 30px;}
  .pkg-item { background: rgba(255,255,255,0.1); padding: 20px; border-radius: 12px; border: 1px solid rgba(255,255,255,0.2);}

  /* --- 6. TIMELINE & COURSES TABLE --- */
  .data-table-wrapper { max-width: 1100px; margin: 0 auto; overflow-x: auto; background: white; border-radius: 16px; box-shadow: var(--card-shadow); border: 1px solid #E5E7EB;}
  .visa-table { width: 100%; border-collapse: collapse; text-align: left; }
  .visa-table th { background: var(--primary); color: white; padding: 18px; font-weight: 600; text-transform: uppercase; font-size: 0.9rem;}
  .visa-table td { padding: 18px; border-bottom: 1px solid #E5E7EB; color: var(--text-dark); font-size: 0.95rem;}
  .visa-table tr:hover { background: #f8fafc; }
  .td-highlight { font-weight: bold; color: var(--primary); }

  /* --- 7. DESTINATIONS GRID --- */
  .country-grid { display: grid; grid-template-columns: repeat(auto-fill, minmax(320px, 1fr)); gap: 30px; max-width: 1200px; margin: 0 auto; }
  .country-card { background: white; border-radius: 16px; overflow: hidden; box-shadow: var(--card-shadow); transition: all 0.4s ease; text-decoration: none; display: flex; flex-direction: column; position: relative; border: 1px solid #f0f0f0; }
  .country-card:hover { transform: translateY(-8px); box-shadow: var(--hover-shadow); border-color: #e0e0e0; }
  .card-img-wrapper { height: 200px; overflow: hidden; position: relative; }
  .card-img { width: 100%; height: 100%; object-fit: cover; transition: transform 0.6s cubic-bezier(0.25, 0.46, 0.45, 0.94); }
  .country-card:hover .card-img { transform: scale(1.1); }
  .flag-badge { position: absolute; bottom: -25px; right: 25px; width: 50px; height: 50px; border-radius: 50%; border: 4px solid white; background: white; object-fit: cover; box-shadow: 0 5px 15px rgba(0,0,0,0.15); z-index: 2; }
  .card-body { padding: 30px 25px 25px; position: relative; }
  .card-title { font-size: 1.5rem; font-weight: 800; color: var(--text-dark); margin: 0 0 10px; display: flex; align-items: center; justify-content: space-between; }
  .visa-tags { display: flex; gap: 8px; flex-wrap: wrap; margin-bottom: 15px; }
  .v-tag { font-size: 0.75rem; padding: 4px 10px; background: #F3F4F6; color: #555; border-radius: 4px; font-weight: 600; }
  .card-text { font-size: 0.95rem; color: var(--text-muted); line-height: 1.6; margin-bottom: 20px; }
  .card-btn { display: block; text-align: center; padding: 10px; border: 1px solid #E5E7EB; border-radius: 8px; color: var(--text-dark); font-weight: 600; transition: 0.2s; font-size: 0.9rem; }
  .country-card:hover .card-btn { background: var(--primary); color: white; border-color: var(--primary); }

  /* --- 8. TESTIMONIALS --- */
  .testimonial-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 30px; max-width: 1000px; margin: 0 auto; }
  .testimonial-card { background: white; padding: 30px; border-radius: 16px; box-shadow: var(--card-shadow); border-top: 4px solid var(--accent); }
  .test-flag { font-size: 1.5rem; margin-bottom: 10px; }
  .test-quote { font-style: italic; color: var(--text-dark); margin-bottom: 20px; font-size: 1.05rem; line-height: 1.6;}
  .test-author { font-weight: bold; color: var(--primary); }
  .test-meta { font-size: 0.8rem; color: var(--text-muted); text-transform: uppercase; }

  /* --- 9. PARENT FAQ --- */
  .faq-container { max-width: 800px; margin: 0 auto; }
  .faq-item { background: white; border: 1px solid var(--border); border-radius: 12px; margin-bottom: 15px; overflow: hidden; transition: 0.3s;}
  .faq-question { padding: 20px; cursor: pointer; font-weight: 700; color: #0f172a; display: flex; justify-content: space-between; align-items: center; font-size: 1.05rem;}
  .faq-answer { padding: 0 20px 20px; color: var(--text-muted); line-height: 1.6; display: none; }
  .faq-item.active .faq-answer { display: block; }
  .faq-item.active { border-color: var(--primary); box-shadow: 0 10px 20px rgba(0,0,0,0.05);}
  
  /* --- 10. LEGAL DISCLAIMER & WHATSAPP --- */
  .legal-footer { text-align: center; padding: 40px 20px; background: #111827; color: #9CA3AF; font-size: 0.85rem; line-height: 1.5; }
  
  .whatsapp-float {
    position: fixed;
    bottom: 30px;
    right: 30px;
    background-color: #25D366;
    color: white;
    border-radius: 50px;
    padding: 12px 20px;
    display: flex;
    align-items: center;
    gap: 10px;
    font-weight: bold;
    text-decoration: none;
    box-shadow: 0 10px 25px rgba(37, 211, 102, 0.4);
    z-index: 1000;
    transition: transform 0.3s;
  }
  .whatsapp-float:hover { transform: scale(1.05); color: white;}
  .whatsapp-float svg { width: 24px; height: 24px; fill: white;}

  /* RESPONSIVE */
  @media (max-width: 900px) {
    .visa-hero { border-radius: 0 0 30px 30px; padding-bottom: 100px; }
    .visa-hero h1 { font-size: 2.5rem; }
    .process-card { grid-template-columns: 1fr; gap: 40px; padding: 30px; }
    .step-item:not(:last-child)::after { content: '↓'; top: auto; bottom: -30px; right: 50%; transform: translateX(50%); }
    .form-grid { grid-template-columns: 1fr; }
    .package-grid { grid-template-columns: 1fr; }
  }
</style>

<div class="visa-hero">
  <span class="hero-badge">✈️ Global Opportunities Await</span>
  <h1>Visa Services & Immigration</h1>
  <p>Simplified visa processing for students, professionals, and tourists. We handle the paperwork so you can focus on the journey.</p>
</div>

<div class="process-container">
  <div class="process-card">
    <div class="step-item">
      <div class="step-icon">📋</div>
      <div class="step-title">Profile Analysis</div>
      <div class="step-desc">We assess your eligibility and choose the right visa category.</div>
    </div>
    <div class="step-item">
      <div class="step-icon">📂</div>
      <div class="step-title">Documentation</div>
      <div class="step-desc">Expert help with SOPs, financials, and application forms.</div>
    </div>
    <div class="step-item">
      <div class="step-icon">🏛️</div>
      <div class="step-title">Embassy Filing</div>
      <div class="step-desc">Error-free submission and interview preparation.</div>
    </div>
    <div class="step-item">
      <div class="step-icon">✈️</div>
      <div class="step-title">Fly High</div>
      <div class="step-desc">Pre-departure briefing and post-landing support.</div>
    </div>
  </div>
</div>

<div class="section-wrap alt-bg" style="padding-top: 0;">
    <div class="section-header" style="margin-bottom: 30px;">
        <h2 class="section-title">Check Your Visa Eligibility</h2>
        <p class="section-subtitle">Fill out the form below for a free, instant profile evaluation by our experts.</p>
    </div>
    <div class="lead-container">
        <form onsubmit="event.preventDefault(); window.open('https://chat.whatsapp.com/JsOIiMJbR5gHTwHxgIDu5O', '_blank');">
            <div class="form-grid">
                <input type="text" class="form-input" placeholder="Full Name" required>
                <input type="tel" class="form-input" placeholder="WhatsApp Number" required>
                <input type="email" class="form-input" placeholder="Email Address" required>
                <select class="form-select" required>
                    <option value="" disabled selected>Target Destination</option>
                    <option value="USA">USA</option>
                    <option value="UK">UK</option>
                    <option value="Canada">Canada</option>
                    <option value="Australia">Australia</option>
                    <option value="Germany">Germany</option>
                    <option value="Other">Other</option>
                </select>
                <select class="form-select" required>
                    <option value="" disabled selected>Visa Type</option>
                    <option value="Student">Student Visa</option>
                    <option value="Work">Work/PR Visa</option>
                    <option value="Tourist">Tourist/Visitor</option>
                </select>
                <select class="form-select">
                    <option value="" disabled selected>Planned Intake</option>
                    <option value="2026">2026</option>
                    <option value="2027">2027</option>
                    <option value="Undecided">Undecided</option>
                </select>
            </div>
            <button type="submit" class="btn-submit">Check My Eligibility Now ➔</button>
            <p style="text-align:center; font-size:0.9rem; color:var(--text-muted); margin-top:15px; font-weight:bold;">
                You will be redirected to our WhatsApp Community. An expert will reach out to you directly!
            </p>
        </form>
    </div>
</div>

<div class="section-wrap">
    <div class="free-package-box">
        <span class="free-badge">Zero Agent Commissions</span>
        <h2 style="font-size: 2.5rem; margin: 0 0 15px 0;">100% Free End-to-End Guidance</h2>
        <p style="font-size: 1.15rem; color: #cbd5e1; max-width: 700px; margin: 0 auto;">
            Unlike traditional agents who push you toward universities that pay them commissions, our platform is built on transparency. We handle your entire journey—from psychometric career matching to visa filing—completely free of service charges.
        </p>
        <div class="package-grid">
            <div class="pkg-item">
                <div style="font-size: 2rem; margin-bottom: 10px;">🧠</div>
                <h4 style="margin: 0 0 5px 0;">Career Assessment</h4>
                <span style="font-size: 0.85rem; color: #9ca3af;">Find your true aptitude</span>
            </div>
            <div class="pkg-item">
                <div style="font-size: 2rem; margin-bottom: 10px;">🏛️</div>
                <h4 style="margin: 0 0 5px 0;">University Selection</h4>
                <span style="font-size: 0.85rem; color: #9ca3af;">Unbiased course mapping</span>
            </div>
            <div class="pkg-item">
                <div style="font-size: 2rem; margin-bottom: 10px;">🛂</div>
                <h4 style="margin: 0 0 5px 0;">Visa Filing Support</h4>
                <span style="font-size: 0.85rem; color: #9ca3af;">Error-free documentation</span>
            </div>
        </div>
    </div>
</div>

<div class="section-wrap alt-bg">
    <div class="section-header">
        <h2 class="section-title">Why Students Trust Our Process</h2>
    </div>
    <div class="authority-grid">
        <div class="auth-card">
            <div class="auth-icon">🎯</div>
            <h4>98% Approval Rate</h4>
            <p style="font-size:0.9rem; color:var(--text-muted); margin:0;">High success due to clinical-level file auditing.</p>
        </div>
        <div class="auth-card">
            <div class="auth-icon">📝</div>
            <h4>SOP Refinement</h4>
            <p style="font-size:0.9rem; color:var(--text-muted); margin:0;">Expert review to make your story embassy-ready.</p>
        </div>
        <div class="auth-card">
            <div class="auth-icon">🎙️</div>
            <h4>Mock Interviews</h4>
            <p style="font-size:0.9rem; color:var(--text-muted); margin:0;">Extensive training to build confidence for the real day.</p>
        </div>
        <div class="auth-card">
            <div class="auth-icon">🛡️</div>
            <h4>Error Audit System</h4>
            <p style="font-size:0.9rem; color:var(--text-muted); margin:0;">Triple-check process prevents stupid rejections.</p>
        </div>
    </div>
</div>

<div class="section-wrap">
    <div class="section-header">
        <h2 class="section-title">Global Snapshot: Timelines & Top Courses</h2>
        <p class="section-subtitle">A quick reference guide for Indian students planning their study abroad journey.</p>
    </div>
    <div class="data-table-wrapper">
        <table class="visa-table">
            <thead>
                <tr>
                    <th>Country</th>
                    <th>Avg. Processing Time</th>
                    <th>Work Rights (Study Visa)</th>
                    <th>Top Synergistic Courses</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td class="td-highlight">🇺🇸 United States</td>
                    <td>4 - 8 Weeks</td>
                    <td>On-Campus Only (20 hrs/wk)</td>
                    <td>Computer Science, Business Analytics, AI</td>
                </tr>
                <tr>
                    <td class="td-highlight">🇬🇧 United Kingdom</td>
                    <td>3 - 5 Weeks</td>
                    <td>20 hrs/week (Term time)</td>
                    <td>Law, Management, FinTech, Humanities</td>
                </tr>
                <tr>
                    <td class="td-highlight">🇨🇦 Canada</td>
                    <td>4 - 10 Weeks (SDS)</td>
                    <td>20 hrs/week (Off-Campus)</td>
                    <td>Data Science, Nursing, Supply Chain</td>
                </tr>
                <tr>
                    <td class="td-highlight">🇩🇪 Germany</td>
                    <td>4 - 8 Weeks</td>
                    <td>120 full days / 240 half days</td>
                    <td>Mechanical Engineering, Automotive, Robotics</td>
                </tr>
                <tr>
                    <td class="td-highlight">🇮🇪 Ireland</td>
                    <td>4 - 6 Weeks</td>
                    <td>20 hrs/week</td>
                    <td>Pharmaceuticals, Cloud Computing, IT</td>
                </tr>
            </tbody>
        </table>
    </div>
</div>

<div class="section-wrap alt-bg">
    <h2 class="section-title">Explore Sub-Pages</h2>
    <p class="section-subtitle">Click to view detailed requirements for each specific region.</p>

    <div class="country-grid">
      <a href="{{ '/visa/usa/' | relative_url }}" class="country-card">
        <div class="card-img-wrapper">
          <img src="https://cdn.pixabay.com/photo/2014/11/22/00/03/new-york-540807_1280.jpg" class="card-img" alt="USA">
          <img src="https://flagcdn.com/w80/us.png" class="flag-badge" alt="USA Flag">
        </div>
        <div class="card-body">
          <h3 class="card-title">United States</h3>
          <div class="visa-tags">
            <span class="v-tag">F1 Student</span>
            <span class="v-tag">H1B Work</span>
            <span class="v-tag">B1/B2 Tourist</span>
          </div>
          <p class="card-text">Navigate the complex US immigration system with expert DS-160 filing and mock interview sessions.</p>
          <span class="card-btn">View USA Details</span>
        </div>
      </a>

      <a href="{{ '/visa/uk/' | relative_url }}" class="country-card">
        <div class="card-img-wrapper">
          <img src="https://images.unsplash.com/photo-1513635269975-59663e0ac1ad?ixlib=rb-4.0.3&auto=format&fit=crop&w=800&q=80" class="card-img" alt="UK">
          <img src="https://flagcdn.com/w80/gb.png" class="flag-badge" alt="UK Flag">
        </div>
        <div class="card-body">
          <h3 class="card-title">United Kingdom</h3>
          <div class="visa-tags">
            <span class="v-tag">Tier 4 Student</span>
            <span class="v-tag">Skilled Worker</span>
          </div>
          <p class="card-text">Study at prestigious UK universities or work with top employers. We assist with CAS and NHS surcharge.</p>
          <span class="card-btn">View UK Details</span>
        </div>
      </a>

      <a href="{{ '/visa/germany/' | relative_url }}" class="country-card">
        <div class="card-img-wrapper">
          <img src="https://images.unsplash.com/photo-1467269204594-9661b134dd2b?ixlib=rb-4.0.3&auto=format&fit=crop&w=800&q=80" class="card-img" alt="Germany">
          <img src="https://flagcdn.com/w80/de.png" class="flag-badge" alt="Germany Flag">
        </div>
        <div class="card-body">
          <h3 class="card-title">Germany</h3>
          <div class="visa-tags">
            <span class="v-tag">Student Visa</span>
            <span class="v-tag">Job Seeker</span>
            <span class="v-tag">Blue Card</span>
          </div>
          <p class="card-text">Unlock free education and engineering careers in Europe's economic powerhouse.</p>
          <span class="card-btn">View Germany Details</span>
        </div>
      </a>

      <a href="{{ '/visa/canada/' | relative_url }}" class="country-card">
        <div class="card-img-wrapper">
          <img src="https://images.unsplash.com/photo-1503614472-8c93d56e92ce?ixlib=rb-4.0.3&auto=format&fit=crop&w=800&q=80" class="card-img" alt="Canada">
          <img src="https://flagcdn.com/w80/ca.png" class="flag-badge" alt="Canada Flag">
        </div>
        <div class="card-body">
          <h3 class="card-title">Canada</h3>
          <div class="visa-tags">
            <span class="v-tag">Study Permit</span>
            <span class="v-tag">Express Entry</span>
          </div>
          <p class="card-text">Expert guidance on SDS/Non-SDS categories and Post-Graduation Work Permits (PGWP).</p>
          <span class="card-btn">View Canada Details</span>
        </div>
      </a>
      
      </div>
</div>

<div class="section-wrap">
    <div class="section-header">
        <h2 class="section-title">Visa Success Stories</h2>
    </div>
    <div class="testimonial-grid">
        <div class="testimonial-card">
            <div class="test-flag">🇨🇦</div>
            <p class="test-quote">"Got my Canada Study Permit under the SDS category in exactly 18 days. The SOP review team was incredibly detailed."</p>
            <div class="test-author">Rahul V.</div>
            <div class="test-meta">Student Visa • Fall Intake</div>
        </div>
        <div class="testimonial-card">
            <div class="test-flag">🇺🇸</div>
            <p class="test-quote">"The mock interviews were lifesavers. They asked me the exact questions the actual embassy officer asked me. Approved!"</p>
            <div class="test-author">Sneha P.</div>
            <div class="test-meta">F1 Visa • Masters in CS</div>
        </div>
        <div class="testimonial-card">
            <div class="test-flag">🇬🇧</div>
            <p class="test-quote">"Navigating the CAS letter and NHS surcharge was confusing, but the team handled the entire backend process smoothly."</p>
            <div class="test-author">Karan M.</div>
            <div class="test-meta">Tier 4 • Business Admin</div>
        </div>
    </div>
</div>

<div class="section-wrap alt-bg">
  <div class="section-header">
    <span class="section-tag">For Parents</span>
    <h2 class="section-title">Parent Advisory Corner</h2>
  </div>
  
  <div class="faq-container">
      <div class="faq-item" onclick="this.classList.toggle('active')">
          <div class="faq-question">Do we need to show the entire 4-year tuition fee in our bank account? <span class="faq-icon">+</span></div>
          <div class="faq-answer">No. Most countries only require you to show liquid funds covering the first year of tuition fees plus 1 year of living expenses. We guide you on acceptable financial formats (FDs, Education Loans, etc.).</div>
      </div>
      <div class="faq-item" onclick="this.classList.toggle('active')">
          <div class="faq-question">What if the visa gets rejected? <span class="faq-icon">+</span></div>
          <div class="faq-answer">While our audit system prevents 99% of basic errors, if a rejection occurs, we analyze the rejection letter (e.g., GCMS notes for Canada) and re-file with strengthened documentation at no extra processing fee.</div>
      </div>
      <div class="faq-item" onclick="this.classList.toggle('active')">
          <div class="faq-question">How does your "100% Free" model actually work? <span class="faq-icon">+</span></div>
          <div class="faq-answer">We are an education-first platform, not a traditional agency. We provide end-to-end guidance as a value-add to our core psychometric career intelligence system, ensuring students make the right choices without financial barriers.</div>
      </div>
  </div>
</div>

<a href="https://wa.me/919035222046?text=Hi!%20I%20would%20like%20to%20check%20my%20visa%20eligibility." target="_blank" class="whatsapp-float">
  <svg viewBox="0 0 24 24"><path d="M12.031 0C5.385 0 0 5.385 0 12.031c0 2.12.553 4.183 1.6 6.002L.156 23.364l5.474-1.436a11.966 11.966 0 006.401 1.834h.004c6.646 0 12.031-5.385 12.031-12.031S18.677 0 12.031 0zm0 21.765h-.003a9.96 9.96 0 01-5.074-1.385l-.364-.216-3.771.99.999-3.676-.237-.377A9.957 9.957 0 012.067 12.03c0-5.503 4.478-9.98 9.964-9.98 5.504 0 9.98 4.477 9.98 9.98s-4.476 9.98-9.98 9.98zm5.47-7.464c-.3-.15-1.774-.875-2.049-.975-.274-.1-.475-.15-.675.15-.2.3-.775.975-.95 1.175-.175.2-.35.225-.65.075-1.488-.737-2.618-1.588-3.606-3.325-.2-.35.225-.325.5-.925.075-.15.038-.288-.038-.438-.075-.15-.675-1.625-.925-2.225-.25-.6-.5-.525-.675-.537-.175-.013-.375-.013-.575-.013s-.525.075-.8.375c-.275.3-1.05 1.025-1.05 2.5s1.075 2.9 1.225 3.1c.15.2 2.1 3.25 5.125 4.55 1.95.838 2.7.775 3.175.7 1.05-.175 1.774-.725 2.024-1.425.25-.7.25-1.3.175-1.425-.075-.125-.275-.2-.575-.35z"/></svg>
  Chat with an Expert
</a>

<footer class="legal-footer">
    <p style="max-width: 800px; margin: 0 auto; font-size: 0.9rem;">
        <strong>Legal Disclaimer:</strong> Career Intelligence System provides documentation guidance, profile evaluation, and application assistance only. We are not an embassy or a government body. The final decision to grant or refuse a visa rests entirely at the discretion of the respective country's embassy or consulate.
    </p>
    <p style="margin-top: 20px; opacity: 0.7;">© 2026 Career Intelligence System. All Rights Reserved.</p>
</footer>
