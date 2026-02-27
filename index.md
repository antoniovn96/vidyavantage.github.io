---
layout: default
title: Home
---

<link rel="preconnect" href="https://www.gstatic.com" crossorigin>

<style>
  /* --- FIX FOR TOP-RIGHT DROPDOWN MENU DISAPPEARING --- */
  /* This forces your master layout header to sit above the homepage hero section */
  header, nav, .navbar, .site-header {
    position: relative;
    z-index: 9999 !important;
  }

  /* --- VARIABLES & RESET --- */
  :root {
    --primary: #2563EB; 
    --secondary: #1E40AF; 
    /* Darkened accent and success colors to pass WCAG AA Contrast Ratios */
    --accent: #D97706; 
    --text-dark: #1F2937;
    --text-light: #4B5563;
    --bg-light: #F8FAFC;
    --white: #ffffff;
    --border: #e2e8f0;
    --success: #059669; 
    --danger: #dc2626;
  }
  
  body {
    font-family: 'Inter', 'Nunito', system-ui, -apple-system, sans-serif;
    background-color: var(--white);
    color: var(--text-dark);
    margin: 0;
    line-height: 1.6;
    text-rendering: optimizeLegibility;
  }

  /* ==========================================
     1. HERO SECTION (VALUE PROP)
     ========================================== */
  .hero-wrapper { display: flex; align-items: center; justify-content: space-between; max-width: 1200px; margin: 0 auto; padding: 80px 20px; min-height: 80vh; gap: 40px; position: relative; z-index: 1;}
  .hero-text { flex: 1.2; animation: slideInLeft 0.8s ease-out; }
  .hero-visual { flex: 0.8; position: relative; animation: slideInRight 0.8s ease-out; min-height: 450px; z-index: 2; }

  .hero-badge { display: inline-block; background: var(--success); color: white; padding: 8px 16px; border-radius: 50px; font-size: 0.85rem; font-weight: 800; margin-bottom: 25px; text-transform: uppercase; letter-spacing: 1px; }
  h1.hero-headline { font-size: 3.5rem; line-height: 1.15; font-weight: 900; color: #0f172a; margin-bottom: 20px; letter-spacing: -1px;}
  .hero-headline span { background: -webkit-linear-gradient(45deg, var(--primary), #3b82f6); -webkit-background-clip: text; -webkit-text-fill-color: transparent; }
  .hero-subhead { font-size: 1.25rem; color: var(--text-light); margin-bottom: 15px; max-width: 90%; font-weight: 500;}
  .hero-location { font-size: 0.95rem; font-weight: 800; color: var(--primary); margin-bottom: 35px; display: flex; align-items: center; gap: 8px;}

  /* --- AUTH & WELCOME BOXES --- */
  .auth-container { min-height: 450px; display: flex; align-items: center; justify-content: center; width: 100%; }
  .auth-box { width: 100%; background: white; padding: 35px; border-radius: 20px; border: 1px solid var(--border); box-shadow: 0 25px 50px -12px rgba(0,0,0,0.1); max-width: 420px; position: relative; overflow: hidden;}
  .auth-box::before { content: ''; position: absolute; top: 0; left: 0; width: 100%; height: 5px; background: linear-gradient(90deg, var(--primary), var(--accent)); }
  
  .auth-input { width: 100%; padding: 14px 15px; margin-bottom: 15px; border: 2px solid var(--border); border-radius: 10px; font-size: 1rem; box-sizing: border-box; font-family: inherit; transition: 0.3s; background: #f8fafc;}
  .auth-input:focus { border-color: var(--primary); outline: none; background: white; box-shadow: 0 0 0 3px rgba(37, 99, 235, 0.1);}
  
  .auth-buttons { display: flex; gap: 10px; margin-bottom: 20px; }
  .btn-auth { flex: 1; padding: 14px; border: none; border-radius: 10px; font-weight: 800; cursor: pointer; transition: 0.3s; font-size: 1rem; text-align: center; touch-action: manipulation; min-height: 48px;}
  .btn-signin { background: var(--primary); color: white; }
  .btn-signin:hover { background: var(--secondary); transform: translateY(-2px); box-shadow: 0 4px 12px rgba(37, 99, 235, 0.2);}
  .btn-signup { background: var(--bg-light); color: var(--text-dark); border: 2px solid var(--border); }
  .btn-signup:hover { background: #e2e8f0; transform: translateY(-2px); }

  .divider { display: flex; align-items: center; text-align: center; color: #94a3b8; font-size: 0.9rem; margin-bottom: 20px; font-weight: bold;}
  .divider::before, .divider::after { content: ''; flex: 1; border-bottom: 1px solid var(--border); }
  .divider:not(:empty)::before { margin-right: .5em; }
  .divider:not(:empty)::after { margin-left: .5em; }

  .btn-google { width: 100%; background: white; color: var(--text-dark); padding: 14px; border: 2px solid var(--border); border-radius: 10px; font-size: 1rem; font-weight: 800; cursor: pointer; display: flex; align-items: center; justify-content: center; gap: 12px; transition: all 0.3s; touch-action: manipulation; min-height: 48px;}
  .btn-google:hover { border-color: var(--primary); background: #f8fafc; }
  
  #statusMsg { margin-top: 15px; color: var(--primary); font-weight: bold; font-size: 0.95rem; text-align: center; min-height: 20px; }

  /* ==========================================
     SHARED SECTION STYLES (Performance Optimized)
     ========================================== */
  .section-wrap { padding: 90px 20px; content-visibility: auto; contain-intrinsic-size: 800px; }
  .section-wrap.alt-bg { background: var(--bg-light); }
  .section-header { text-align: center; max-width: 750px; margin: 0 auto 50px; }
  .section-tag { color: var(--primary); font-weight: 800; text-transform: uppercase; font-size: 0.95rem; letter-spacing: 1px;}
  .section-title { font-size: 2.8rem; font-weight: 900; margin: 15px 0; color: #0f172a; letter-spacing: -1px;}

  /* BUTTON STYLES */
  .btn-outline { border: 2px solid var(--primary); color: var(--primary); background: transparent; transition: all 0.3s; touch-action: manipulation; }
  .btn-outline:hover { background: var(--primary); color: white; }

  /* ==========================================
     2. DYNAMIC SOCIAL PROOF & STATS 
     ========================================== */
  .stats-container { background: var(--secondary); color: white; padding: 60px 20px 40px; position: relative; z-index: 2; }
  .stats-grid { max-width: 1200px; margin: 0 auto; display: grid; grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); text-align: center; gap: 30px; }
  .stat-number { font-size: 3.5rem; font-weight: 900; margin-bottom: 5px; color: #fbbf24; } 
  .stat-label { font-size: 1.1rem; opacity: 0.9; text-transform: uppercase; letter-spacing: 1.5px; font-weight: bold;}
  .live-pulse { display: inline-block; width: 12px; height: 12px; background: #34d399; border-radius: 50%; margin-right: 8px; animation: pulse 2s infinite;}
  .urgency-trigger { text-align: center; margin-top: 30px; font-size: 0.95rem; font-weight: bold; color: #a7f3d0; letter-spacing: 0.5px;}

  /* ==========================================
     3. FOR PARENTS (Micro-Section)
     ========================================== */
  .parents-box { max-width: 800px; margin: 0 auto; background: white; padding: 40px; border-radius: 20px; box-shadow: 0 10px 30px rgba(0,0,0,0.05); text-align: center; border: 1px solid var(--border); }
  .parents-list { list-style: none; padding: 0; margin: 0 0 30px 0; display: flex; flex-direction: column; gap: 15px; font-size: 1.1rem; color: var(--text-dark); font-weight: 600; text-align: left; max-width: 450px; margin-left: auto; margin-right: auto;}
  .parents-list li { display: flex; align-items: center; gap: 10px; }

  /* ==========================================
     4. WHY GUESSWORK FAILS (Comparison)
     ========================================== */
  .comparison-grid { display: grid; grid-template-columns: 1fr 1fr; gap: 30px; max-width: 1000px; margin: 0 auto; }
  .comp-card { background: white; padding: 40px; border-radius: 20px; box-shadow: 0 10px 30px rgba(0,0,0,0.05); }
  .comp-bad { border-top: 5px solid var(--danger); }
  .comp-good { border-top: 5px solid var(--success); }
  .comp-list { list-style: none; padding: 0; margin: 0; }
  .comp-list li { margin-bottom: 20px; font-size: 1.1rem; display: flex; align-items: flex-start; gap: 15px; font-weight: 600; color: var(--text-dark);}
  
  /* ==========================================
     5. REAL TRANSFORMATION & WHO IS THIS FOR
     ========================================== */
  .story-box { max-width: 800px; margin: 0 auto 80px; background: linear-gradient(135deg, var(--bg-light), white); padding: 40px; border-radius: 20px; border: 1px solid var(--border); box-shadow: 0 15px 35px rgba(0,0,0,0.05); position: relative; }
  .story-tag { position: absolute; top: -15px; left: 50%; transform: translateX(-50%); background: var(--secondary); color: white; padding: 6px 18px; border-radius: 50px; font-weight: bold; font-size: 0.85rem; text-transform: uppercase; letter-spacing: 1px;}
  
  .audience-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 20px; max-width: 1000px; margin: 0 auto; text-align: center; }
  .audience-card { background: white; padding: 30px; border-radius: 16px; border: 1px solid var(--border); box-shadow: 0 4px 15px rgba(0,0,0,0.02);}

  /* ==========================================
     6. WHAT HAPPENS NEXT (The Process)
     ========================================== */
  .process-timeline { max-width: 1000px; margin: 0 auto; display: flex; justify-content: space-between; position: relative; gap: 15px; flex-wrap: wrap;}
  .process-timeline::before { content:''; position:absolute; top:40px; left:0; width:100%; height:4px; background:var(--border); z-index:0; }
  .timeline-step { flex: 1; text-align: center; position: relative; z-index: 1; min-width: 150px;}
  .t-icon { width: 80px; height: 80px; background: white; border: 4px solid var(--primary); border-radius: 50%; margin: 0 auto 20px; display: flex; align-items: center; justify-content: center; font-size: 2rem; box-shadow: 0 10px 20px rgba(37,99,235,0.1); transition: 0.3s;}
  .timeline-step:hover .t-icon { transform: scale(1.1); background: var(--primary); color: white;}
  .timeline-step h3 { margin: 0 0 10px; color: #0f172a; font-weight: 800; font-size: 1.1rem;}
  .timeline-step p { font-size: 0.9rem; color: var(--text-light);}
  
  .outcomes-row { max-width: 1000px; margin: 50px auto 0; padding-top: 40px; border-top: 1px solid var(--border); text-align: center; }
  .outcome-pill { display: inline-block; background: white; border: 1px solid var(--border); padding: 10px 22px; border-radius: 50px; font-weight: 800; color: var(--secondary); box-shadow: 0 4px 10px rgba(0,0,0,0.03); margin: 5px;}

  /* ==========================================
     7. ABOUT THE FOUNDER
     ========================================== */
  .founder-wrapper { display: flex; align-items: center; gap: 50px; max-width: 1000px; margin: 0 auto; background: white; padding: 50px; border-radius: 20px; box-shadow: 0 20px 40px rgba(0,0,0,0.05); border: 1px solid var(--border);}
  .founder-photo { width: 250px; height: 250px; border-radius: 20px; background: linear-gradient(135deg, var(--primary), var(--secondary)); display: flex; align-items: center; justify-content: center; font-size: 5rem; color: white; flex-shrink: 0; box-shadow: 0 15px 30px rgba(37,99,235,0.3);}
  .founder-info h2 { font-size: 2rem; margin: 0 0 5px 0; color: #0f172a; font-weight: 900;}
  .founder-info h3 { font-size: 1.1rem; color: var(--primary); margin: 0 0 20px 0; text-transform: uppercase; letter-spacing: 1px;}
  .founder-stats { display: flex; gap: 20px; margin-top: 25px; border-top: 1px solid var(--border); padding-top: 20px;}
  .f-stat strong { display: block; font-size: 1.5rem; color: #0f172a; font-weight: 900;}
  .f-stat span { font-size: 0.85rem; color: var(--text-light); text-transform: uppercase;}

  /* ==========================================
     8. REPORT PREVIEW & SCHOOLS CTA
     ========================================== */
  .preview-box { max-width: 800px; margin: 0 auto; background: white; border-radius: 20px; padding: 40px; box-shadow: 0 20px 50px rgba(0,0,0,0.1); border-top: 8px solid var(--secondary); text-align: center;}
  .school-cta { background: linear-gradient(135deg, #0f172a 0%, #1e1b4b 100%); color: white; padding: 80px 20px; text-align: center; border-radius: 30px; max-width: 1100px; margin: 0 auto; box-shadow: 0 25px 50px -12px rgba(0,0,0,0.2);}

  /* ==========================================
     9. FAQ ACCORDION (Natively Accessible)
     ========================================== */
  .faq-container { max-width: 800px; margin: 0 auto; }
  details.faq-item { background: white; border: 1px solid var(--border); border-radius: 12px; margin-bottom: 15px; overflow: hidden; transition: 0.3s; }
  details.faq-item summary { padding: 24px 25px; font-weight: 800; color: #0f172a; font-size: 1.1rem; cursor: pointer; list-style: none; display: flex; justify-content: space-between; align-items: center; touch-action: manipulation; min-height: 48px; }
  details.faq-item summary::-webkit-details-marker { display: none; }
  details.faq-item summary::after { content: '+'; color: var(--primary); font-size: 1.5rem; font-weight: normal; transition: transform 0.3s; }
  details[open].faq-item summary::after { content: '×'; transform: rotate(45deg); }
  details[open].faq-item { border-color: var(--primary); box-shadow: 0 10px 20px rgba(37,99,235,0.05); }
  .faq-answer { padding: 0 25px 24px; color: var(--text-light); line-height: 1.6; }
  
  .blog-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 30px; max-width: 1200px; margin: 0 auto;}
  .blog-card { background: white; border-radius: 16px; border: 1px solid var(--border); overflow: hidden; transition: 0.3s; cursor: pointer; display: block;}
  .blog-card:hover { transform: translateY(-5px); box-shadow: 0 15px 30px rgba(0,0,0,0.08);}
  .blog-img { height: 200px; background: var(--bg-light); display: flex; align-items: center; justify-content: center; font-size: 3rem;}
  .blog-content { padding: 25px; }
  .blog-content h3 { margin: 0 0 10px 0; font-size: 1.25rem; color: #0f172a;}
  
  /* ==========================================
     10. FOOTER
     ========================================== */
  .trust-footer { background: #0f172a; color: #cbd5e1; padding: 40px 20px; text-align: center; border-top: 1px solid #334155; content-visibility: auto;}
  .trust-badges { display: flex; justify-content: center; gap: 30px; margin-bottom: 20px; flex-wrap: wrap;}
  .t-badge { display: flex; align-items: center; gap: 10px; font-weight: bold; font-size: 0.9rem;}

  @media (max-width: 900px) {
    .hero-wrapper { flex-direction: column; text-align: center; padding-top: 40px; }
    .hero-text { padding-right: 0; margin-bottom: 40px; }
    .hero-headline { font-size: 2.8rem; }
    .hero-location { justify-content: center; }
    .auth-box { margin: 20px auto; text-align: left; }
    .comparison-grid, .founder-wrapper, .audience-grid { flex-direction: column; grid-template-columns: 1fr; text-align: center;}
    .parents-list { align-items: center; text-align: center; }
    .founder-photo { margin: 0 auto; }
    .founder-stats { justify-content: center; }
    .process-timeline::before { display: none; }
  }
</style>

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "LocalBusiness",
  "name": "Vidyavantage Career Intelligence",
  "address": {
    "@type": "PostalAddress",
    "addressLocality": "Bangalore",
    "addressRegion": "Karnataka",
    "addressCountry": "India"
  },
  "areaServed": "India",
  "description": "Professional career counselling and psychometric assessments for students of Class 8 to 12.",
  "founder": {
    "@type": "Person",
    "name": "Antonio Vian Noronha",
    "jobTitle": "Lead School Counsellor"
  }
}
</script>

<main>
    <div class="hero-wrapper">
      <div class="hero-text">
        <span class="hero-badge">Verified Career Intelligence</span>
        
        <h1 class="hero-headline">Career Guidance & Psychometric Assessment for Class 8–12 Students <span>Across India</span></h1>
        
        <p class="hero-subhead">
          End the Confusion. Map Your Future with Clinical Precision. We replace guesswork with science. Get personalized career roadmaps powered by clinical psychometrics and expert 1-on-1 counseling.
        </p>
        <div class="hero-location">
          <span style="font-size: 1.2rem;">📍</span> Serving students Pan-India | Headquartered in Bangalore.
        </div>
      </div>
      
      <div class="hero-visual">
        <div class="auth-container">
            <div class="auth-box" id="loginBoxUI">
                <h2 style="margin-top:0; color:var(--text-dark); font-size: 1.4rem; font-weight: 900;">Access Your Dashboard</h2>
                <p style="color:var(--text-light); font-size:0.9rem; margin-bottom:20px;">Parents, Students, and Counsellors login here.</p>
                
                <input type="email" id="emailInput" class="auth-input" placeholder="Email Address" aria-label="Email Address" autocomplete="username">
                <input type="password" id="passwordInput" class="auth-input" placeholder="Password" aria-label="Password" autocomplete="current-password">
                
                <div class="auth-buttons">
                    <button class="btn-auth btn-signin" id="emailLoginBtn">Sign In</button>
                    <button class="btn-auth btn-signup" id="emailSignUpBtn">Register</button>
                </div>
                
                <div class="divider">OR SECURE LOGIN WITH</div>
                
                <button class="btn-google" id="googleLoginBtn">
                    <svg width="22" height="22" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 48 48"><path fill="#FFC107" d="M43.611,20.083H42V20H24v8h11.303c-1.649,4.657-6.08,8-11.303,8c-6.627,0-12-5.373-12-12c0-6.627,5.373-12,12-12c3.059,0,5.842,1.154,7.961,3.039l5.657-5.657C34.046,6.053,29.268,4,24,4C12.955,4,4,12.955,4,24c0,11.045,8.955,20,20,20c11.045,0,20-8.955,20-20C44,22.659,43.862,21.35,43.611,20.083z"/><path fill="#FF3D00" d="M6.306,14.691l6.571,4.819C14.655,15.108,18.961,12,24,12c3.059,0,5.842,1.154,7.961,3.039l5.657-5.657C34.046,6.053,29.268,4,24,4C16.318,4,9.656,8.337,6.306,14.691z"/><path fill="#4CAF50" d="M24,44c5.166,0,9.86-1.977,13.409-5.192l-6.19-5.238C29.211,35.091,26.715,36,24,36c-5.202,0-9.619-3.317-11.283-7.946l-6.522,5.025C9.505,39.556,16.227,44,24,44z"/><path fill="#1976D2" d="M43.611,20.083H42V20H24v8h11.303c-0.792,2.237-2.231,4.166-4.087,5.571c0.001-0.001,0.002-0.001,0.003-0.002l6.19,5.238C36.971,39.205,44,34,44,24C44,22.659,43.862,21.35,43.611,20.083z"/></svg>
                    Continue with Google
                </button>
                <p id="statusMsg"></p>
            </div>

            <div class="auth-box" id="welcomeBoxUI" style="display: none; text-align: center; padding: 40px 30px;">
                <div style="font-size: 4rem; margin-bottom: 15px; line-height:1;" aria-hidden="true">👋</div>
                <h2 style="margin-top:0; color:var(--text-dark); font-size: 1.8rem; font-weight: 900;">Welcome Back,<br><span id="welcomeNameDisplay" style="color:var(--primary);"></span>!</h2>
                <p style="color:var(--text-light); margin-bottom: 25px; font-size: 1.05rem;">
                    You are securely logged in as:<br>
                    <strong id="loggedInEmailDisplay" style="color:#0f172a;">...</strong>
                </p>
                <button class="btn-auth btn-signin" id="fastTravelBtn" style="width: 100%; padding: 18px; font-size: 1.1rem; box-shadow: 0 10px 20px rgba(37,99,235,0.3); margin-bottom: 15px;">
                    Enter My Portal ➔
                </button>
                <button class="btn-outline" id="homeLogoutBtn" style="width: 100%; padding: 14px; border-radius: 10px; font-size: 1rem; display: block; box-sizing: border-box;">
                    Log Out Securely
                </button>
            </div>
        </div>
      </div>
    </div>

    <div class="stats-container">
      <div class="stats-grid">
        <div><div class="stat-number">5,000+</div><div class="stat-label">Students Mentored</div></div>
        <div><div class="stat-number">75+</div><div class="stat-label">Data Points Analyzed</div></div>
        <div>
            <div class="stat-number">98%</div>
            <div class="stat-label" style="display:flex; align-items:center; justify-content:center;">
                <span class="live-pulse"></span> Clarity Rate
            </div>
        </div>
      </div>
      <div class="urgency-trigger">⚡ 11 students completed their assessment this week.</div>
    </div>

    <div class="section-wrap alt-bg" style="padding-bottom: 60px;">
      <div class="section-header" style="margin-bottom: 40px;">
        <span class="section-tag">For Parents</span>
        <h2 class="section-title">Built for Parents Who Want Clarity — Not Conflict.</h2>
      </div>
      
      <div class="parents-box">
          <ul class="parents-list">
              <li><span style="color: var(--success); font-size: 1.2rem;" aria-hidden="true">✔</span> Scientific, not emotional advice</li>
              <li><span style="color: var(--success); font-size: 1.2rem;" aria-hidden="true">✔</span> Transparent reports parents can easily access</li>
              <li><span style="color: var(--success); font-size: 1.2rem;" aria-hidden="true">✔</span> Conflict-reducing alignment model</li>
          </ul>
          <a href="#loginBoxUI" class="btn-outline" style="display:block; padding: 16px 30px; border-radius: 8px; font-weight: 800; text-decoration: none; max-width: 300px; margin: 0 auto; text-align: center;">See How Parent View Works ➔</a>
      </div>
    </div>

    <div class="section-wrap">
      <div class="section-header">
        <span class="section-tag">Our Career Guidance Services</span>
        <h2 class="section-title">Online Career Counselling & Psychometric Testing Pan-India</h2>
        <p style="color:var(--text-light); font-size:1.15rem;">Choosing a career based on marks or peer pressure leads to burnout.</p>
      </div>

      <div class="comparison-grid">
          <div class="comp-card">
              <h3 style="color:var(--primary); font-size: 1.5rem; margin-top:0;">Career Counselling After 10th</h3>
              <p style="color: var(--text-light); font-size: 1.05rem;">Stream selection guidance (Science, Commerce, Arts) tailored for CBSE and ICSE students to set the right foundation.</p>
          </div>
          <div class="comp-card">
              <h3 style="color:var(--primary); font-size: 1.5rem; margin-top:0;">Career Counselling After 12th</h3>
              <p style="color: var(--text-light); font-size: 1.05rem;">College planning, entrance exam strategy, and course selection to lock in your professional future.</p>
          </div>
          <div class="comp-card">
              <h3 style="color:var(--primary); font-size: 1.5rem; margin-top:0;">Psychometric Career Assessment</h3>
              <p style="color: var(--text-light); font-size: 1.05rem;">RIASEC-based aptitude and personality testing to discover your natural strengths and vulnerability zones.</p>
          </div>
          <div class="comp-card">
              <h3 style="color:var(--primary); font-size: 1.5rem; margin-top:0;">Parent-Student Alignment Sessions</h3>
              <p style="color: var(--text-light); font-size: 1.05rem;">Conflict resolution and a structured career clarity framework to bring families onto the same strategic page.</p>
          </div>
      </div>
    </div>

    <div class="section-wrap alt-bg">
      <div class="story-box">
          <div class="story-tag">Real Transformation</div>
          <div style="display: flex; flex-direction: column; gap: 15px; font-size: 1.15rem; color: var(--text-dark);">
              <div><strong style="color: var(--danger); width: 80px; display:inline-block;">Before:</strong> Wanted Engineering because friends chose it.</div>
              <div><strong style="color: var(--accent); width: 80px; display:inline-block;">After:</strong> Discovered high Artistic + Investigative profile.</div>
              <div><strong style="color: var(--success); width: 80px; display:inline-block;">Now:</strong> Preparing for Architecture with full parental support.</div>
          </div>
          <div style="margin-top: 25px; padding-top: 25px; border-top: 1px dashed var(--border); text-align: center; font-weight: 900; color: var(--secondary); font-size: 1.3rem;">
              Clarity Score Improved: <span style="color: var(--danger);">3</span> ➔ <span style="color: var(--success);">8</span>
          </div>
      </div>

      <div class="section-header" style="margin-bottom: 40px;">
          <span class="section-tag">Target Audience</span>
          <h2 class="section-title">Who Is This For?</h2>
      </div>
      
      <div class="audience-grid">
          <div class="audience-card">
              <div style="font-size: 3rem; margin-bottom: 15px;" aria-hidden="true">👦</div>
              <h3 style="margin: 0 0 5px 0; color: var(--secondary); font-size: 1.4rem;">Class 8–10</h3>
              <p style="margin: 0; color: var(--text-light); font-weight: 600;">Stream Clarity & Foundation</p>
          </div>
          <div class="audience-card">
              <div style="font-size: 3rem; margin-bottom: 15px;" aria-hidden="true">🎓</div>
              <h3 style="margin: 0 0 5px 0; color: var(--secondary); font-size: 1.4rem;">Class 11–12</h3>
              <p style="margin: 0; color: var(--text-light); font-weight: 600;">Career Locking & College Targets</p>
          </div>
          <div class="audience-card">
              <div style="font-size: 3rem; margin-bottom: 15px;" aria-hidden="true">🏫</div>
              <h3 style="margin: 0 0 5px 0; color: var(--secondary); font-size: 1.4rem;">Schools</h3>
              <p style="margin: 0; color: var(--text-light); font-weight: 600;">Institutional Dashboards</p>
          </div>
      </div>
    </div>

    <div class="section-wrap">
      <div class="section-header">
        <span class="section-tag">How It Works</span>
        <h2 class="section-title">The Path to Clarity.</h2>
        <p style="color:var(--text-light); font-size:1.15rem;">A structured 5-step system to lock in your future.</p>
      </div>

      <div class="process-timeline">
          <div class="timeline-step">
              <div class="t-icon" aria-hidden="true">👤</div>
              <h3>1. Create Profile</h3>
              <p>Register and input your academic baseline.</p>
          </div>
          <div class="timeline-step">
              <div class="t-icon" aria-hidden="true">📝</div>
              <h3>2. Assessment</h3>
              <p>Take the 25-min clinical psychometric test.</p>
          </div>
          <div class="timeline-step">
              <div class="t-icon" aria-hidden="true">📊</div>
              <h3>3. Get Score</h3>
              <p>Instantly view your psychological clarity score.</p>
          </div>
          <div class="timeline-step">
              <div class="t-icon" aria-hidden="true">💬</div>
              <h3>4. Meet Expert</h3>
              <p>1-on-1 session to decode your vulnerability zones.</p>
          </div>
          <div class="timeline-step">
              <div class="t-icon" aria-hidden="true">🔒</div>
              <h3>5. Lock Path</h3>
              <p>Generate your 1-year execution roadmap.</p>
          </div>
      </div>

      <div class="outcomes-row">
          <h3 style="color: var(--text-light); margin-bottom: 20px; font-size: 1.1rem; text-transform: uppercase; letter-spacing: 1px;">After Clarity, Students Get:</h3>
          <div style="display: flex; justify-content: center; flex-wrap: wrap;">
              <span class="outcome-pill">🎯 Defined Stream</span>
              <span class="outcome-pill">📚 Target Colleges</span>
              <span class="outcome-pill">📅 1-Year Execution Plan</span>
              <span class="outcome-pill">🧠 Reduced Anxiety</span>
          </div>
      </div>
    </div>

    <div class="section-wrap alt-bg">
        <div class="founder-wrapper">
            <div class="founder-photo" aria-hidden="true">AN</div>
            <div class="founder-info">
                <h2 style="font-size: 2rem; margin: 0 0 5px 0; color: #0f172a; font-weight: 900;">Meet the Career Architect</h2>
                <h3 style="font-size: 1.1rem; color: var(--primary); margin: 0 0 20px 0; text-transform: uppercase; letter-spacing: 1px;">Antonio Vian Noronha | Lead School Counsellor</h3>
                <p style="color:var(--text-light); font-size:1.1rem; line-height: 1.8;">
                    As a professional School Counsellor with an MSW (Medical and Psychiatric Social Work), Antonio has witnessed firsthand the anxiety students face when making blind career choices. He built Career Intelligence to replace dinner-table arguments with clinical precision.
                </p>
                <div class="founder-stats">
                    <div class="f-stat"><strong>MSW</strong><span style="font-size: 0.75rem;">(Medical and Psychiatric Social Work)</span></div>
                    <div class="f-stat"><strong>5k+</strong><span>Students Guided</span></div>
                </div>
            </div>
        </div>
    </div>

    <div class="section-wrap" style="background: linear-gradient(135deg, #0f172a 0%, #1e1b4b 100%); color: white;">
      <div class="section-header">
        <span class="section-tag" style="color:var(--accent);">Inside The Dashboard</span>
        <h2 class="section-title" style="color:white;">Your Personalized Dossier.</h2>
        <p style="color:#cbd5e1; font-size:1.15rem;">Stop guessing. Start executing.</p>
      </div>
      
      <div class="preview-box">
          <h3 style="color:#0f172a; font-size: 1.8rem; margin-top:0;">What's in your report?</h3>
          <div style="display: flex; flex-wrap: wrap; justify-content: center; gap: 15px; margin: 30px 0;">
              <span style="background: var(--bg-light); color: var(--secondary); padding: 8px 16px; border-radius: 8px; font-weight: bold;">🧬 Exact RIASEC Code</span>
              <span style="background: var(--bg-light); color: var(--secondary); padding: 8px 16px; border-radius: 8px; font-weight: bold;">⚠️ Vulnerability Zones</span>
              <span style="background: var(--bg-light); color: var(--secondary); padding: 8px 16px; border-radius: 8px; font-weight: bold;">🎯 Top 5 Career Matches</span>
              <span style="background: var(--bg-light); color: var(--secondary); padding: 8px 16px; border-radius: 8px; font-weight: bold;">📚 Recommended Subjects</span>
          </div>
          <a href="#loginBoxUI" class="btn" style="padding: 16px 40px; font-size: 1.2rem; text-decoration: none; display: inline-block;">Take the Assessment Now</a>
      </div>
    </div>

    <div class="section-wrap">
        <div class="school-cta">
            <span class="hero-badge" style="background: rgba(255,255,255,0.2); color: white; border: none;">B2B Partnerships</span>
            <h2 style="font-size: 3rem; margin: 15px 0; color: #ffffff;">Are You a School Administrator?</h2>
            <p style="font-size: 1.2rem; color: #cbd5e1; max-width: 700px; margin: 0 auto 30px;">
                Empower your institution with a white-labeled career dashboard. Track student clarity metrics, identify high-risk students, and host expert parent workshops.
            </p>
            <a href="mailto:antonio.antonio.noronha@gmail.com?subject=School Partnership Inquiry" class="btn" style="background: white; color: #0f172a; padding: 16px 40px; font-size: 1.1rem; display: inline-block; text-decoration: none;">Request Institutional Demo</a>
        </div>
    </div>

    <div class="section-wrap alt-bg">
      <div class="section-header">
        <h2 class="section-title">Frequently Asked Questions</h2>
      </div>
      
      <div class="faq-container">
          <details class="faq-item">
              <summary>Is this better than a school career test?</summary>
              <div class="faq-answer">Yes. Standard tests often rely on outdated models. Our system dynamically cross-references your psychological traits, academic baseline, and stress resilience to formulate a real-world execution plan.</div>
          </details>
          <details class="faq-item">
              <summary>What if my child changes interests later?</summary>
              <div class="faq-answer">The platform focuses on underlying aptitudes, not just passing interests. However, the system allows for reassessment and roadmap adjustments if significant shifts occur.</div>
          </details>
          <details class="faq-item">
              <summary>Can parents attend the counselling sessions?</summary>
              <div class="faq-answer">Absolutely. We feature a unique "Parent-Student Alignment" model designed specifically to resolve table-side arguments and bring everyone onto the same page using verified data.</div>
          </details>
          <details class="faq-item">
              <summary>Is this suitable for a Class 8 student?</summary>
              <div class="faq-answer">Yes. Early intervention is ideal. For Class 8-10, the focus is purely on stream selection and foundational subject alignment, saving massive stress in 11th grade.</div>
          </details>
      </div>
    </div>

    <div class="section-wrap">
      <div class="section-header">
        <span class="section-tag">Career Insights</span>
        <h2 class="section-title">Latest from the Desk.</h2>
      </div>

      <div class="blog-grid">
          <a href="/career-guidance-after-10th" style="text-decoration: none; color: inherit; display: block;" aria-label="Read our guide on what to do after 10th grade">
              <div class="blog-card">
                  <div class="blog-img" aria-hidden="true">📈</div>
                  <div class="blog-content">
                      <h3>What to Do After 10th? Complete Guide</h3>
                      <p style="color:var(--text-light); font-size:0.95rem;">Stream selection strategy for CBSE & ICSE students facing the Science vs Commerce dilemma.</p>
                  </div>
              </div>
          </a>
          <a href="/best-career-options-after-12th" style="text-decoration: none; color: inherit; display: block;" aria-label="Read about the best career options after 12th science">
              <div class="blog-card">
                  <div class="blog-img" aria-hidden="true">🤖</div>
                  <div class="blog-content">
                      <h3>Best Career Options After 12th Science</h3>
                      <p style="color:var(--text-light); font-size:0.95rem;">Which university majors will survive the automation wave? A clinical breakdown of future-proof degrees.</p>
                  </div>
              </div>
          </a>
          <a href="/tef-vs-tcf-canada-pr-2026" style="text-decoration: none; color: inherit; display: block;" aria-label="Read about TEF vs TCF for Canada PR">
              <div class="blog-card">
                  <div class="blog-img" aria-hidden="true">🇨🇦</div>
                  <div class="blog-content">
                      <h3>TEF vs TCF Canada 2026</h3>
                      <p style="color:var(--text-light); font-size:0.95rem;">The 'Golden Ticket' to Canada PR. How to hit CLB 7 and claim your 50 CRS points.</p>
                  </div>
              </div>
          </a>
      </div>
    </div>
</main>

<footer class="trust-footer">
    <div class="trust-badges">
        <div class="t-badge"><span aria-hidden="true">🔒</span> 256-Bit Data Encryption</div>
        <div class="t-badge"><span aria-hidden="true">🧠</span> Clinical-Grade Psychometrics</div>
        <div class="t-badge"><span aria-hidden="true">🛡️</span> Data Never Sold to 3rd Parties</div>
        <div class="t-badge" style="color: var(--accent);"><span aria-hidden="true">🏆</span> CBSE & ICSE Aligned</div>
    </div>
    
    <div style="margin: 30px 0; font-size: 0.85rem; color: #94a3b8; max-width: 800px; margin-left: auto; margin-right: auto; line-height: 1.6;">
        <p style="margin-bottom: 10px; color: #cbd5e1;">We provide professional online career counselling and psychometric assessments for students of Class 8, 9, 10, 11 and 12 across India. Headquartered in Bangalore, our services help students choose the right stream after 10th and the best career options after 12th using scientific aptitude testing.</p>
        <strong>Our Focus Areas:</strong> Online Career Counselling in India | Best Career Guidance Pan-India | Career Counsellor in Bangalore | Psychometric Career Assessment For Students | Stream Selection After 10th | Career Planning After 12th
    </div>

    <p style="font-size: 0.85rem; opacity: 0.7;">© 2026 Vidyavantage Career Intelligence System. Built by Professional School Counsellors.</p>
</footer>

<script type="module">
    import { initializeApp } from "https://www.gstatic.com/firebasejs/10.8.1/firebase-app.js";
    import { getFirestore, doc, getDoc } from "https://www.gstatic.com/firebasejs/10.8.1/firebase-firestore.js";
    /* 🔥 ADDED signOut TO FIREBASE IMPORTS 🔥 */
    import { getAuth, signInWithPopup, GoogleAuthProvider, signInWithEmailAndPassword, createUserWithEmailAndPassword, onAuthStateChanged, signOut } from "https://www.gstatic.com/firebasejs/10.8.1/firebase-auth.js";

    const firebaseConfig = {
      apiKey: "AIzaSyBygHYMOSuKueZf9nE5LmSwCyCeZ2dNeD0",
      authDomain: "career-intelligence-system.firebaseapp.com",
      projectId: "career-intelligence-system",
      storageBucket: "career-intelligence-system.firebasestorage.app",
      messagingSenderId: "223785446772",
      appId: "1:223785446772:web:0f9ded4e89a978fc551021"
    };

    const app = initializeApp(firebaseConfig);
    const db = getFirestore(app);
    const auth = getAuth(app);
    const provider = new GoogleAuthProvider();

    const status = document.getElementById('statusMsg');
    const loginBoxUI = document.getElementById('loginBoxUI');
    const welcomeBoxUI = document.getElementById('welcomeBoxUI');
    const loggedInEmailDisplay = document.getElementById('loggedInEmailDisplay');
    const welcomeNameDisplay = document.getElementById('welcomeNameDisplay');
    const fastTravelBtn = document.getElementById('fastTravelBtn');
    
    /* 🔥 CAPTURE THE NEW LOGOUT BUTTON 🔥 */
    const homeLogoutBtn = document.getElementById('homeLogoutBtn');
    
    let activeUser = null;

    onAuthStateChanged(auth, (user) => {
        if (user) {
            activeUser = user;
            loginBoxUI.style.display = "none";
            welcomeBoxUI.style.display = "block";
            loggedInEmailDisplay.innerText = user.email;
            const displayName = user.displayName || user.email.split('@')[0];
            welcomeNameDisplay.innerText = displayName;
        } else {
            activeUser = null;
            loginBoxUI.style.display = "block";
            welcomeBoxUI.style.display = "none";
        }
    });
    
    async function processUserRouting(user) {
        const email = user.email.toLowerCase();
        try {
            const permsRef = doc(db, "permissions", email);
            const permsSnap = await getDoc(permsRef);

            if (permsSnap.exists()) {
                const role = permsSnap.data().role;
                if(status) status.innerText = `Authorized as ${role.replace('_', ' ')}. Connecting...`;
                
                setTimeout(() => {
                    if (role === "super_admin") window.location.href = "admin.html";
                    else if (role === "school_admin") window.location.href = "school_dashboard.html";
                    else if (role === "counsellor") window.location.href = "counsellor_dashboard.html";
                    else window.location.href = "student_portal.html"; 
                }, 1000);
                return;
            }

            const studentRef = doc(db, "students", user.uid);
            const studentSnap = await getDoc(studentRef);

            if (studentSnap.exists()) {
                if(status) status.innerText = "Welcome back! Opening Student Portal...";
                setTimeout(() => window.location.href = "student_portal.html", 1000);
            } else {
                if(status) status.innerText = "New profile detected! Let's get you registered...";
                setTimeout(() => window.location.href = "register.html", 1500);
            }
        } catch (error) {
            console.error("Routing Error:", error);
            if(status) { status.innerText = "Error analyzing profile permissions."; status.style.color = "red"; }
            if(fastTravelBtn) fastTravelBtn.innerText = "Connection Error";
        }
    }

    fastTravelBtn.addEventListener('click', () => {
        fastTravelBtn.innerText = "Routing... ⏳";
        if(activeUser) processUserRouting(activeUser);
    });

    /* 🔥 LOGOUT BUTTON CLICK EVENT 🔥 */
    if (homeLogoutBtn) {
        homeLogoutBtn.addEventListener('click', async () => {
            homeLogoutBtn.innerText = "Logging out...";
            try {
                await signOut(auth);
                // The onAuthStateChanged listener above will automatically swap the UI back to the login box!
            } catch (error) {
                console.error("Logout Error:", error);
                homeLogoutBtn.innerText = "Log Out Securely";
            }
        });
    }

    document.getElementById('googleLoginBtn').addEventListener('click', async () => {
        status.innerText = "Authenticating securely... ⏳";
        try {
            const result = await signInWithPopup(auth, provider);
            await processUserRouting(result.user);
        } catch (error) {
            console.error(error);
            status.innerText = "Google Sign-In failed or was cancelled.";
            status.style.color = "red";
        }
    });

    document.getElementById('emailLoginBtn').addEventListener('click', async () => {
        const email = document.getElementById('emailInput').value.trim();
        const password = document.getElementById('passwordInput').value;
        if (!email || !password) return alert("Please enter both email and password.");
        status.innerText = "Verifying credentials... ⏳";
        try {
            const result = await signInWithEmailAndPassword(auth, email, password);
            await processUserRouting(result.user);
        } catch (error) {
            console.error(error);
            status.innerText = "Incorrect email or password.";
            status.style.color = "red";
        }
    });

    document.getElementById('emailSignUpBtn').addEventListener('click', async () => {
        const email = document.getElementById('emailInput').value.trim();
        const password = document.getElementById('passwordInput').value;
        if (!email || !password) return alert("Please enter an email and password to register.");
        if (password.length < 6) return alert("Password must be at least 6 characters.");
        status.innerText = "Creating secure account... ⏳";
        try {
            const result = await createUserWithEmailAndPassword(auth, email, password);
            await processUserRouting(result.user);
        } catch (error) {
            console.error(error);
            status.innerText = error.message.replace("Firebase:", "").trim();
            status.style.color = "red";
        }
    });
</script>
