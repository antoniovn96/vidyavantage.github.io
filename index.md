---
layout: default
title: Home
---

<style>
  /* --- VARIABLES & RESET --- */
  :root {
    --primary: #2563EB; /* Royal Blue */
    --secondary: #1E40AF; /* Darker Blue */
    --accent: #F59E0B; /* Amber/Gold */
    --text-dark: #1F2937;
    --text-light: #6B7280;
    --bg-light: #F3F4F6;
    --white: #ffffff;
  }
  
  body {
    font-family: 'Inter', system-ui, -apple-system, sans-serif;
    background-color: var(--white);
    color: var(--text-dark);
    margin: 0;
  }

  /* ==========================================
     HEADER & NAVIGATION
     ========================================== */
  .site-header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 15px 5%;
    background: var(--white);
    border-bottom: 1px solid #e5e7eb;
    position: sticky;
    top: 0;
    z-index: 1000;
    box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.05);
  }

  .site-logo {
    font-size: 1.5rem;
    font-weight: 800;
    color: var(--text-dark);
    text-decoration: none;
    display: flex;
    align-items: center;
    gap: 8px;
    letter-spacing: -0.5px;
  }
  .site-logo span { color: var(--primary); }

  .site-nav {
    display: flex;
    gap: 30px;
    align-items: center;
  }

  .site-nav a {
    text-decoration: none;
    color: var(--text-dark);
    font-weight: 600;
    font-size: 0.95rem;
    transition: color 0.2s;
  }
  .site-nav a:hover { color: var(--primary); }

  .header-login-btn {
    background: var(--bg-light);
    color: var(--text-dark);
    padding: 8px 20px;
    border-radius: 6px;
    border: 1px solid #e5e7eb;
    font-weight: 700;
    cursor: pointer;
    transition: all 0.3s;
    display: flex;
    align-items: center;
    gap: 8px;
  }
  .header-login-btn:hover {
    background: var(--primary);
    color: white;
    border-color: var(--primary);
  }
  .header-login-btn img { width: 16px; height: 16px; }

  /* Mobile Nav Hide (Simple version) */
  @media (max-width: 768px) {
    .site-nav { display: none; }
  }

  /* ==========================================
     1. MODERN SPLIT HERO SECTION 
     ========================================== */
  .hero-wrapper {
    display: flex;
    align-items: center;
    justify-content: space-between;
    max-width: 1200px;
    margin: 0 auto;
    padding: 80px 20px;
    min-height: 80vh;
  }

  .hero-text { flex: 1; padding-right: 50px; animation: slideInLeft 0.8s ease-out; }
  .hero-visual { flex: 1; position: relative; animation: slideInRight 0.8s ease-out; }

  .hero-badge {
    display: inline-block;
    background: #DBEAFE;
    color: var(--secondary);
    padding: 6px 15px;
    border-radius: 50px;
    font-size: 0.85rem;
    font-weight: 700;
    margin-bottom: 20px;
    text-transform: uppercase;
    letter-spacing: 0.5px;
  }

  h1.hero-headline { font-size: 3.5rem; line-height: 1.1; font-weight: 800; color: #111; margin-bottom: 20px; }
  .hero-headline span { color: var(--primary); }
  .hero-subhead { font-size: 1.2rem; color: var(--text-light); line-height: 1.6; margin-bottom: 35px; max-width: 90%; }
  .cta-group { display: flex; gap: 15px; flex-wrap: wrap; align-items: center; }

  /* Google Login Button Styling (Hero) */
  .btn-google {
    background: white;
    color: var(--text-dark);
    padding: 14px 25px;
    border: 1px solid #e5e7eb;
    border-radius: 8px;
    font-size: 1rem;
    font-weight: 700;
    cursor: pointer;
    display: inline-flex;
    align-items: center;
    gap: 12px;
    transition: all 0.3s;
    box-shadow: 0 4px 14px rgba(0, 0, 0, 0.05);
  }
  .btn-google:hover { transform: translateY(-2px); box-shadow: 0 6px 20px rgba(0, 0, 0, 0.1); border-color: var(--primary); }
  .btn-google img { width: 22px; height: 22px; }

  .btn-secondary { background: white; color: var(--text-dark); border: 2px solid #e5e7eb; padding: 13px 35px; border-radius: 8px; font-weight: 600; text-decoration: none; transition: all 0.3s; }
  .btn-secondary:hover { border-color: var(--text-dark); }
  .hero-img-main { width: 100%; border-radius: 20px; box-shadow: 20px 20px 0px var(--bg-light); object-fit: cover; height: 500px; }

  /* ==========================================
     2. STATS & FEATURES 
     ========================================== */
  .stats-container { background: var(--secondary); color: white; padding: 50px 0; margin-top: -40px; position: relative; z-index: 2; }
  .stats-grid { max-width: 1200px; margin: 0 auto; display: grid; grid-template-columns: repeat(3, 1fr); text-align: center; gap: 30px; }
  .stat-number { font-size: 3rem; font-weight: 700; margin-bottom: 5px; color: var(--accent); }
  .stat-label { font-size: 1rem; opacity: 0.9; text-transform: uppercase; letter-spacing: 1px; }

  .features-section { padding: 100px 20px; background: #fafafa; }
  .section-header { text-align: center; max-width: 700px; margin: 0 auto 60px; }
  .section-tag { color: var(--primary); font-weight: 700; text-transform: uppercase; font-size: 0.9rem; }
  .section-title { font-size: 2.5rem; font-weight: 800; margin: 10px 0; color: #111; }
  .cards-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(320px, 1fr)); gap: 30px; max-width: 1200px; margin: 0 auto; }

  .feature-card { background: white; border-radius: 16px; overflow: hidden; box-shadow: 0 10px 40px rgba(0,0,0,0.05); transition: transform 0.3s ease; text-decoration: none; color: inherit; display: flex; flex-direction: column; height: 100%; }
  .feature-card:hover { transform: translateY(-10px); }
  .card-image-wrap { height: 200px; overflow: hidden; }
  .card-img { width: 100%; height: 100%; object-fit: cover; transition: transform 0.5s; }
  .feature-card:hover .card-img { transform: scale(1.05); }
  .card-content { padding: 30px; display: flex; flex-direction: column; flex-grow: 1; }
  .card-title { font-size: 1.4rem; font-weight: 700; margin-bottom: 10px; color: #111; }
  .card-desc { color: var(--text-light); line-height: 1.6; margin-bottom: 20px; flex-grow: 1; }
  .card-arrow { color: var(--primary); font-weight: 700; display: flex; align-items: center; gap: 5px; margin-top: auto; }

  /* ==========================================
     3. WHY CHOOSE US
     ========================================== */
  .why-section { padding: 80px 20px; max-width: 1200px; margin: 0 auto; text-align: center; }
  .icon-grid { display: flex; justify-content: space-around; flex-wrap: wrap; gap: 40px; margin-top: 50px; }
  .icon-box { max-width: 300px; }
  .icon-circle { width: 70px; height: 70px; background: #DBEAFE; color: var(--primary); border-radius: 50%; display: flex; align-items: center; justify-content: center; font-size: 1.8rem; margin: 0 auto 20px; }
  .icon-title { font-weight: 700; font-size: 1.2rem; margin-bottom: 10px; }
  .icon-text { color: var(--text-light); font-size: 0.95rem; line-height: 1.6; }

  /* ==========================================
     FOOTER
     ========================================== */
  .site-footer {
    background: #111827; /* Very dark gray/blue */
    color: #D1D5DB;
    padding: 70px 5% 30px;
    margin-top: 40px;
    border-top: 4px solid var(--primary);
  }
  .footer-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
    gap: 40px;
    max-width: 1200px;
    margin: 0 auto;
    border-bottom: 1px solid #374151;
    padding-bottom: 40px;
  }
  .footer-col h4 { color: white; font-size: 1.2rem; margin-bottom: 20px; font-weight: 700; }
  .footer-col p { line-height: 1.6; font-size: 0.95rem; margin-bottom: 15px; color: #9CA3AF; }
  .footer-links { list-style: none; padding: 0; margin: 0; }
  .footer-links li { margin-bottom: 12px; }
  .footer-links a { color: #9CA3AF; text-decoration: none; transition: color 0.3s; font-size: 0.95rem; }
  .footer-links a:hover { color: var(--accent); }
  .footer-bottom { text-align: center; padding-top: 25px; font-size: 0.9rem; color: #6B7280; }

  /* RESPONSIVE */
  @media (max-width: 900px) {
    .hero-wrapper { flex-direction: column-reverse; text-align: center; padding-top: 40px; }
    .hero-text { padding-right: 0; margin-top: 40px; }
    .hero-headline { font-size: 2.5rem; }
    .cta-group { justify-content: center; }
    .hero-img-main { height: 300px; }
    .stats-grid { grid-template-columns: 1fr; gap: 30px; }
    .cards-grid { grid-template-columns: 1fr; }
  }
  @keyframes slideInLeft { from { opacity: 0; transform: translateX(-30px); } to { opacity: 1; transform: translateX(0); } }
  @keyframes slideInRight { from { opacity: 0; transform: translateX(30px); } to { opacity: 1; transform: translateX(0); } }
</style>

<header class="site-header">
  <a href="/" class="site-logo">
    Vidya<span>Vantage</span>
  </a>
  
  <nav class="site-nav">
    <a href="/">Home</a>
    <a href="{{ '/colleges/' | relative_url }}">Colleges</a>
    <a href="{{ '/visa/' | relative_url }}">Visa Guide</a>
    <a href="{{ '/blog/' | relative_url }}">Blogs & Research</a>
    
    <button class="header-login-btn googleLoginTrigger">
      <img src="https://upload.wikimedia.org/wikipedia/commons/c/c1/Google_%22G%22_logo.svg" alt="Google Logo">
      Portal Login
    </button>
  </nav>
</header>

<div class="hero-wrapper">
  <div class="hero-text">
    <span class="hero-badge">🚀 Platform Access Open</span>
    <h1 class="hero-headline">Build Your Future <br><span>Without Limits.</span></h1>
    <p class="hero-subhead">
      Your personalized gateway to top-tier universities and global career opportunities. Powered by clinical psychometrics and expert counseling.
    </p>
    
    <div class="cta-group">
      <button class="btn-google googleLoginTrigger">
        <img src="https://upload.wikimedia.org/wikipedia/commons/c/c1/Google_%22G%22_logo.svg" alt="Google Logo">
        Access Platform
      </button>
      <a href="{{ '/colleges/' | relative_url }}" class="btn-secondary">Browse Colleges</a>
    </div>
    
    <p id="statusMsg" style="margin-top: 15px; color: var(--primary); font-weight: bold; font-size: 0.95rem; height: 20px;"></p>

  </div>
  <div class="hero-visual">
    <img src="https://images.unsplash.com/photo-1523240795612-9a054b0db644?ixlib=rb-4.0.3&auto=format&fit=crop&w=800&q=80" alt="Students" class="hero-img-main">
  </div>
</div>

<div class="stats-container">
  <div class="stats-grid">
    <div>
      <div class="stat-number">100+</div>
      <div class="stat-label">Top Universities</div>
    </div>
    <div>
      <div class="stat-number">10+</div>
      <div class="stat-label">Global Destinations</div>
    </div>
    <div>
      <div class="stat-number">100%</div>
      <div class="stat-label">Verified Data</div>
    </div>
  </div>
</div>

<div class="features-section">
  <div class="section-header">
    <span class="section-tag">Our Services</span>
    <h2 class="section-title">Everything you need to succeed</h2>
    <p style="color:#666; font-size:1.1rem;">We simplify the complex world of admissions, career mapping, and immigration.</p>
  </div>

  <div class="cards-grid">
    <a href="#" class="feature-card googleLoginTrigger">
      <div class="card-image-wrap">
        <img src="https://images.unsplash.com/photo-1454165804606-c3d57bc86b40?ixlib=rb-4.0.3&auto=format&fit=crop&w=800&q=80" class="card-img" alt="AI Career Assessment">
      </div>
      <div class="card-content">
        <h3 class="card-title">AI Career Assessment</h3>
        <p class="card-desc">Not sure which path to take? Take our AI-driven capability analysis to discover your ideal courses and get personalized college matches instantly.</p>
        <div class="card-arrow">Sign In to Start ➔</div>
      </div>
    </a>

    <a href="{{ '/colleges/' | relative_url }}" class="feature-card">
      <div class="card-image-wrap">
        <img src="https://images.unsplash.com/photo-1541339907198-e08756dedf3f?ixlib=rb-4.0.3&auto=format&fit=crop&w=800&q=80" class="card-img" alt="Colleges">
      </div>
      <div class="card-content">
        <h3 class="card-title">Top Colleges Directory</h3>
        <p class="card-desc">Comprehensive guides on IISc, IIT Roorkee, BMSCE, and more. Access 2025 fee structures, entrance exams, and placement records.</p>
        <div class="card-arrow">Explore Colleges ➔</div>
      </div>
    </a>

    <a href="{{ '/visa/' | relative_url }}" class="feature-card">
      <div class="card-image-wrap">
        <img src="https://images.unsplash.com/photo-1436491865332-7a61a109cc05?ixlib=rb-4.0.3&auto=format&fit=crop&w=800&q=80" class="card-img" alt="Visa">
      </div>
      <div class="card-content">
        <h3 class="card-title">Global Visa Assistance</h3>
        <p class="card-desc">Planning to study abroad? Get expert checklists for USA (F1), UK (Tier 4), Germany, Australia, and Canada student visas.</p>
        <div class="card-arrow">Check Requirements ➔</div>
      </div>
    </a>
  </div>
</div>

<div class="why-section">
  <h2 class="section-title">Why VidyaVantage?</h2>
  <div class="icon-grid">
    <div class="icon-box">
      <div class="icon-circle">🎓</div>
      <h3 class="icon-title">Expert Counseling</h3>
      <p class="icon-text">Founded by a School Counselor dedicated to bridging the information gap for students.</p>
    </div>
    <div class="icon-box">
      <div class="icon-circle">📊</div>
      <h3 class="icon-title">Accurate Data</h3>
      <p class="icon-text">Up-to-date 2025 fee structures and admission cutoffs sourced directly from institutions.</p>
    </div>
    <div class="icon-box">
      <div class="icon-circle">🌍</div>
      <h3 class="icon-title">Global Reach</h3>
      <p class="icon-text">From local Bangalore colleges to Ivy League universities, we cover it all.</p>
    </div>
  </div>
</div>

<footer class="site-footer">
  <div class="footer-grid">
    <div class="footer-col">
      <h4 style="color:var(--primary); font-size:1.5rem; letter-spacing:-0.5px;">VidyaVantage</h4>
      <p>Your personalized gateway to top-tier universities, clinical career assessments, and global opportunities.</p>
    </div>
    
    <div class="footer-col">
      <h4>Platform</h4>
      <ul class="footer-links">
        <li><a href="#" class="googleLoginTrigger">Student Portal</a></li>
        <li><a href="#" class="googleLoginTrigger">Counselor Dashboard</a></li>
        <li><a href="{{ '/colleges/' | relative_url }}">College Directory</a></li>
        <li><a href="{{ '/visa/' | relative_url }}">Immigration & Visa</a></li>
      </ul>
    </div>

    <div class="footer-col">
      <h4>Resources</h4>
      <ul class="footer-links">
        <li><a href="{{ '/blog/' | relative_url }}">Research & Blogs</a></li>
        <li><a href="#">Psychometrics Guide</a></li>
        <li><a href="#">Parent Toolkit</a></li>
        <li><a href="#">Contact Us</a></li>
      </ul>
    </div>
  </div>
  
  <div class="footer-bottom">
    &copy; 2026 VidyaVantage / Career Intelligence. All rights reserved.
  </div>
</footer>

<script type="module">
    import { initializeApp } from "https://www.gstatic.com/firebasejs/10.8.1/firebase-app.js";
    import { getFirestore, doc, getDoc } from "https://www.gstatic.com/firebasejs/10.8.1/firebase-firestore.js";
    import { getAuth, signInWithPopup, GoogleAuthProvider } from "https://www.gstatic.com/firebasejs/10.8.1/firebase-auth.js";

    // ⚠️ YOUR EXACT FIREBASE CONFIG
    const firebaseConfig = {
      apiKey: "AIzaSyBygHYMOSuKueZf9nE5LmSwCyCeZ2dNeD0",
      authDomain: "career-intelligence-system.firebaseapp.com",
      projectId: "career-intelligence-system",
      storageBucket: "career-intelligence-system.firebasestorage.app",
      messagingSenderId: "223785446772",
      appId: "1:223785446772:web:0f9ded4e89a978fc551021",
      measurementId: "G-HGKJJN9KDF"
    };

    const app = initializeApp(firebaseConfig);
    const db = getFirestore(app);
    const auth = getAuth(app);
    const provider = new GoogleAuthProvider();

    // ⚠️ REPLACE THIS WITH YOUR ACTUAL GMAIL ADDRESS FOR MASTER ADMIN ACCESS
    const SUPER_ADMIN_EMAIL = "antonio.antonio.noronha@gmail.com"; 

    // Target ALL elements with the class 'googleLoginTrigger'
    const loginButtons = document.querySelectorAll('.googleLoginTrigger');
    const status = document.getElementById('statusMsg');

    loginButtons.forEach(btn => {
        btn.addEventListener('click', async (e) => {
            e.preventDefault(); // Prevent default link behavior if it's an <a> tag
            
            status.innerText = "Authenticating securely... ⏳";
            
            // Disable all buttons to prevent multiple clicks
            loginButtons.forEach(b => {
                b.style.opacity = "0.7";
                b.style.pointerEvents = "none";
            });
            
            try {
                const result = await signInWithPopup(auth, provider);
                const user = result.user;
                const email = user.email.toLowerCase();
                
                // ROUTE 1: SUPER ADMIN
                if (email === SUPER_ADMIN_EMAIL.toLowerCase()) {
                    status.innerText = "Welcome back! Routing to Master Control Center...";
                    setTimeout(() => window.location.href = "admin.html", 1000);
                    return;
                }

                // ROUTE 2: CHECK VIP PERMISSIONS LIST
                const permsRef = doc(db, "permissions", email);
                const permsSnap = await getDoc(permsRef);

                if (permsSnap.exists()) {
                    const role = permsSnap.data().role;
                    status.innerText = `Authorized as ${role.replace('_', ' ')}. Connecting...`;
                    
                    setTimeout(() => {
                        if (role === "school_admin") window.location.href = "school_dashboard.html";
                        else if (role === "counsellor") window.location.href = "counsellor_dashboard.html";
                    }, 1000);
                    return;
                }

                // ROUTE 3: CHECK IF EXISTING STUDENT
                const studentRef = doc(db, "students", user.uid);
                const studentSnap = await getDoc(studentRef);

                if (studentSnap.exists()) {
                    status.innerText = "Welcome back! Opening Student Portal...";
                    setTimeout(() => window.location.href = "student_portal.html", 1000);
                } else {
                    // ROUTE 4: BRAND NEW STUDENT - SEND TO ONBOARDING
                    status.innerText = "New profile detected! Let's get you registered...";
                    setTimeout(() => window.location.href = "register.html", 1500);
                }

            } catch (error) {
                console.error("Login Error:", error);
                status.innerText = "Authentication failed. Please try again.";
                
                // Re-enable buttons
                loginButtons.forEach(b => {
                    b.style.opacity = "1";
                    b.style.pointerEvents = "auto";
                });
            }
        });
    });
</script>
