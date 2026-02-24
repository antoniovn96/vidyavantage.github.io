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
    --border: #e5e7eb;
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
  .site-header { display: flex; justify-content: space-between; align-items: center; padding: 15px 5%; background: var(--white); border-bottom: 1px solid var(--border); position: sticky; top: 0; z-index: 1000; box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.05); }
  .site-logo { font-size: 1.5rem; font-weight: 800; color: var(--text-dark); text-decoration: none; display: flex; align-items: center; gap: 8px; letter-spacing: -0.5px; }
  .site-logo span { color: var(--primary); }
  .site-nav { display: flex; gap: 30px; align-items: center; }
  .site-nav a { text-decoration: none; color: var(--text-dark); font-weight: 600; font-size: 0.95rem; transition: color 0.2s; }
  .site-nav a:hover { color: var(--primary); }
  @media (max-width: 768px) { .site-nav { display: none; } }

  /* ==========================================
     1. MODERN SPLIT HERO SECTION 
     ========================================== */
  .hero-wrapper { display: flex; align-items: center; justify-content: space-between; max-width: 1200px; margin: 0 auto; padding: 80px 20px; min-height: 80vh; }
  .hero-text { flex: 1.2; padding-right: 50px; animation: slideInLeft 0.8s ease-out; }
  .hero-visual { flex: 0.8; position: relative; animation: slideInRight 0.8s ease-out; }

  .hero-badge { display: inline-block; background: #DBEAFE; color: var(--secondary); padding: 6px 15px; border-radius: 50px; font-size: 0.85rem; font-weight: 700; margin-bottom: 20px; text-transform: uppercase; letter-spacing: 0.5px; }
  h1.hero-headline { font-size: 3.5rem; line-height: 1.1; font-weight: 800; color: #111; margin-bottom: 20px; }
  .hero-headline span { color: var(--primary); }
  .hero-subhead { font-size: 1.2rem; color: var(--text-light); line-height: 1.6; margin-bottom: 35px; max-width: 90%; }

  /* --- AUTH BOX (NEW) --- */
  .auth-box { background: white; padding: 30px; border-radius: 16px; border: 1px solid var(--border); box-shadow: 0 20px 40px rgba(0,0,0,0.08); max-width: 400px; margin-top: 20px;}
  .auth-input { width: 100%; padding: 12px 15px; margin-bottom: 15px; border: 2px solid var(--border); border-radius: 8px; font-size: 1rem; box-sizing: border-box; font-family: inherit; transition: 0.3s; }
  .auth-input:focus { border-color: var(--primary); outline: none; }
  
  .auth-buttons { display: flex; gap: 10px; margin-bottom: 20px; }
  .btn-auth { flex: 1; padding: 12px; border: none; border-radius: 8px; font-weight: 700; cursor: pointer; transition: 0.3s; font-size: 1rem; }
  .btn-signin { background: var(--primary); color: white; }
  .btn-signin:hover { background: var(--secondary); transform: translateY(-2px); }
  .btn-signup { background: var(--bg-light); color: var(--text-dark); border: 1px solid var(--border); }
  .btn-signup:hover { background: #e5e7eb; transform: translateY(-2px); }

  .divider { display: flex; align-items: center; text-align: center; color: var(--text-light); font-size: 0.9rem; margin-bottom: 20px; }
  .divider::before, .divider::after { content: ''; flex: 1; border-bottom: 1px solid var(--border); }
  .divider:not(:empty)::before { margin-right: .5em; }
  .divider:not(:empty)::after { margin-left: .5em; }

  .btn-google { width: 100%; background: white; color: var(--text-dark); padding: 12px; border: 2px solid var(--border); border-radius: 8px; font-size: 1rem; font-weight: 700; cursor: pointer; display: flex; align-items: center; justify-content: center; gap: 10px; transition: all 0.3s; }
  .btn-google:hover { border-color: var(--primary); background: #f8fafc; }
  .btn-google img { width: 20px; height: 20px; }

  #statusMsg { margin-top: 15px; color: var(--primary); font-weight: bold; font-size: 0.95rem; text-align: center; min-height: 20px; }

  /* ==========================================
     2. STATS & FEATURES 
     ========================================== */
  .stats-container { background: var(--secondary); color: white; padding: 50px 0; position: relative; z-index: 2; }
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

  /* RESPONSIVE */
  @media (max-width: 900px) {
    .hero-wrapper { flex-direction: column; text-align: center; padding-top: 40px; }
    .hero-text { padding-right: 0; margin-bottom: 40px; }
    .hero-headline { font-size: 2.5rem; }
    .auth-box { margin: 20px auto; text-align: left; }
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
  </nav>
</header>

<div class="hero-wrapper">
  <div class="hero-text">
    <span class="hero-badge">🚀 Platform Access Open</span>
    <h1 class="hero-headline">Build Your Future <br><span>Without Limits.</span></h1>
    <p class="hero-subhead">
      Your personalized gateway to top-tier universities and global career opportunities. Powered by clinical psychometrics and expert counseling.
    </p>
  </div>
  
  <div class="hero-visual">
    <div class="auth-box">
        <h3 style="margin-top:0; color:var(--text-dark);">Secure Portal Access</h3>
        <input type="email" id="emailInput" class="auth-input" placeholder="Email Address">
        <input type="password" id="passwordInput" class="auth-input" placeholder="Password">
        
        <div class="auth-buttons">
            <button class="btn-auth btn-signin" id="emailLoginBtn">Sign In</button>
            <button class="btn-auth btn-signup" id="emailSignUpBtn">Create Account</button>
        </div>
        
        <div class="divider">OR</div>
        
        <button class="btn-google" id="googleLoginBtn">
            <img src="https://upload.wikimedia.org/wikipedia/commons/c/c1/Google_%22G%22_logo.svg" alt="Google Logo">
            Continue with Google
        </button>

        <p id="statusMsg"></p>
    </div>
  </div>
</div>

<div class="stats-container">
  <div class="stats-grid">
    <div><div class="stat-number">100+</div><div class="stat-label">Top Universities</div></div>
    <div><div class="stat-number">10+</div><div class="stat-label">Global Destinations</div></div>
    <div><div class="stat-number">100%</div><div class="stat-label">Verified Data</div></div>
  </div>
</div>

<div class="features-section">
  <div class="section-header">
    <span class="section-tag">Our Services</span>
    <h2 class="section-title">Everything you need to succeed</h2>
    <p style="color:#666; font-size:1.1rem;">We simplify the complex world of admissions, career mapping, and immigration.</p>
  </div>

  <div class="cards-grid">
    <a href="#emailInput" class="feature-card">
      <div class="card-image-wrap">
        <img src="https://images.unsplash.com/photo-1454165804606-c3d57bc86b40?ixlib=rb-4.0.3&auto=format&fit=crop&w=800&q=80" class="card-img" alt="AI Career Assessment">
      </div>
      <div class="card-content">
        <h3 class="card-title">AI Career Assessment</h3>
        <p class="card-desc">Take our clinical analysis to discover your ideal courses and get personalized college matches instantly.</p>
        <div class="card-arrow">Sign In to Start ➔</div>
      </div>
    </a>
    <a href="{{ '/colleges/' | relative_url }}" class="feature-card">
      <div class="card-image-wrap">
        <img src="https://images.unsplash.com/photo-1541339907198-e08756dedf3f?ixlib=rb-4.0.3&auto=format&fit=crop&w=800&q=80" class="card-img" alt="Colleges">
      </div>
      <div class="card-content">
        <h3 class="card-title">Top Colleges Directory</h3>
        <p class="card-desc">Comprehensive guides on top institutions. Access fee structures, entrance exams, and placement records.</p>
        <div class="card-arrow">Explore Colleges ➔</div>
      </div>
    </a>
    <a href="{{ '/visa/' | relative_url }}" class="feature-card">
      <div class="card-image-wrap">
        <img src="https://images.unsplash.com/photo-1436491865332-7a61a109cc05?ixlib=rb-4.0.3&auto=format&fit=crop&w=800&q=80" class="card-img" alt="Visa">
      </div>
      <div class="card-content">
        <h3 class="card-title">Global Visa Assistance</h3>
        <p class="card-desc">Get expert checklists for USA (F1), UK (Tier 4), Germany, Australia, and Canada student visas.</p>
        <div class="card-arrow">Check Requirements ➔</div>
      </div>
    </a>
  </div>
</div>

<script type="module">
    import { initializeApp } from "https://www.gstatic.com/firebasejs/10.8.1/firebase-app.js";
    import { getFirestore, doc, getDoc } from "https://www.gstatic.com/firebasejs/10.8.1/firebase-firestore.js";
    // ⚠️ Note the added Email/Password imports here!
    import { getAuth, signInWithPopup, GoogleAuthProvider, signInWithEmailAndPassword, createUserWithEmailAndPassword } from "https://www.gstatic.com/firebasejs/10.8.1/firebase-auth.js";

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

    // 🚨 REPLACE THIS WITH YOUR ACTUAL GMAIL ADDRESS FOR MASTER ADMIN ACCESS
    const SUPER_ADMIN_EMAIL = "antonio.antonio.noronha@gmail.com"; 

    const status = document.getElementById('statusMsg');
    
    // --- THE MASTER ROUTING ENGINE ---
    // This function runs regardless of HOW the user logged in
    async function processUserRouting(user) {
        const email = user.email.toLowerCase();
        
        try {
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
            console.error("Routing Error:", error);
            status.innerText = "Error analyzing profile permissions.";
            status.style.color = "red";
        }
    }

    // --- 1. GOOGLE LOGIN ---
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

    // --- 2. EMAIL / PASSWORD LOGIN ---
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

    // --- 3. EMAIL / PASSWORD SIGN UP ---
    document.getElementById('emailSignUpBtn').addEventListener('click', async () => {
        const email = document.getElementById('emailInput').value.trim();
        const password = document.getElementById('passwordInput').value;
        if (!email || !password) return alert("Please enter an email and password to register.");
        if (password.length < 6) return alert("Password must be at least 6 characters.");
        
        status.innerText = "Creating secure account... ⏳";
        try {
            const result = await createUserWithEmailAndPassword(auth, email, password);
            // After creating the account, route them (they will naturally go to register.html)
            await processUserRouting(result.user);
        } catch (error) {
            console.error(error);
            status.innerText = error.message.replace("Firebase:", "").trim();
            status.style.color = "red";
        }
    });

</script>
