---
layout: default
title: Home
---

<style>
  /* --- VARIABLES & RESET --- */
  :root {
    --primary: #2563EB; 
    --secondary: #1E40AF; 
    --accent: #F59E0B; 
    --text-dark: #1F2937;
    --text-light: #4B5563;
    --bg-light: #F8FAFC;
    --white: #ffffff;
    --border: #e2e8f0;
  }
  
  body {
    font-family: 'Inter', 'Nunito', sans-serif;
    background-color: var(--white);
    color: var(--text-dark);
    margin: 0;
  }

  /* ==========================================
     1. HERO SECTION (VALUE PROP)
     ========================================== */
  .hero-wrapper { display: flex; align-items: center; justify-content: space-between; max-width: 1200px; margin: 0 auto; padding: 80px 20px; min-height: 80vh; }
  .hero-text { flex: 1.2; padding-right: 50px; animation: slideInLeft 0.8s ease-out; }
  .hero-visual { flex: 0.8; position: relative; animation: slideInRight 0.8s ease-out; }

  .hero-badge { display: inline-block; background: #dbeafe; color: var(--secondary); padding: 8px 16px; border-radius: 50px; font-size: 0.85rem; font-weight: 800; margin-bottom: 25px; text-transform: uppercase; letter-spacing: 1px; }
  h1.hero-headline { font-size: 3.5rem; line-height: 1.15; font-weight: 900; color: #0f172a; margin-bottom: 20px; letter-spacing: -1px;}
  .hero-headline span { background: -webkit-linear-gradient(45deg, var(--primary), #60a5fa); -webkit-background-clip: text; -webkit-text-fill-color: transparent; }
  .hero-subhead { font-size: 1.25rem; color: var(--text-light); line-height: 1.6; margin-bottom: 35px; max-width: 90%; font-weight: 500;}

  /* --- AUTH & WELCOME BOXES --- */
  .auth-box { background: white; padding: 35px; border-radius: 20px; border: 1px solid var(--border); box-shadow: 0 25px 50px -12px rgba(0,0,0,0.1); max-width: 420px; margin-top: 20px; position: relative; overflow: hidden;}
  .auth-box::before { content: ''; position: absolute; top: 0; left: 0; width: 100%; height: 5px; background: linear-gradient(90deg, var(--primary), var(--accent)); }
  
  .auth-input { width: 100%; padding: 14px 15px; margin-bottom: 15px; border: 2px solid var(--border); border-radius: 10px; font-size: 1rem; box-sizing: border-box; font-family: inherit; transition: 0.3s; background: #f8fafc;}
  .auth-input:focus { border-color: var(--primary); outline: none; background: white; box-shadow: 0 0 0 3px rgba(37, 99, 235, 0.1);}
  
  .auth-buttons { display: flex; gap: 10px; margin-bottom: 20px; }
  .btn-auth { flex: 1; padding: 14px; border: none; border-radius: 10px; font-weight: 800; cursor: pointer; transition: 0.3s; font-size: 1rem; }
  .btn-signin { background: var(--primary); color: white; }
  .btn-signin:hover { background: var(--secondary); transform: translateY(-2px); box-shadow: 0 4px 12px rgba(37, 99, 235, 0.2);}
  .btn-signup { background: var(--bg-light); color: var(--text-dark); border: 2px solid var(--border); }
  .btn-signup:hover { background: #e2e8f0; transform: translateY(-2px); }

  .divider { display: flex; align-items: center; text-align: center; color: #94a3b8; font-size: 0.9rem; margin-bottom: 20px; font-weight: bold;}
  .divider::before, .divider::after { content: ''; flex: 1; border-bottom: 1px solid var(--border); }
  .divider:not(:empty)::before { margin-right: .5em; }
  .divider:not(:empty)::after { margin-left: .5em; }

  .btn-google { width: 100%; background: white; color: var(--text-dark); padding: 14px; border: 2px solid var(--border); border-radius: 10px; font-size: 1rem; font-weight: 800; cursor: pointer; display: flex; align-items: center; justify-content: center; gap: 12px; transition: all 0.3s; }
  .btn-google:hover { border-color: var(--primary); background: #f8fafc; }
  .btn-google img { width: 22px; height: 22px; }

  #statusMsg { margin-top: 15px; color: var(--primary); font-weight: bold; font-size: 0.95rem; text-align: center; min-height: 20px; }

  /* ==========================================
     2. TRUST STATS 
     ========================================== */
  .stats-container { background: var(--secondary); color: white; padding: 60px 0; position: relative; z-index: 2; }
  .stats-grid { max-width: 1200px; margin: 0 auto; display: grid; grid-template-columns: repeat(3, 1fr); text-align: center; gap: 30px; }
  .stat-number { font-size: 3.5rem; font-weight: 900; margin-bottom: 5px; color: var(--accent); }
  .stat-label { font-size: 1.1rem; opacity: 0.9; text-transform: uppercase; letter-spacing: 1.5px; font-weight: bold;}

  /* ==========================================
     3. WHO WE HELP SECTION
     ========================================== */
  .section-wrap { padding: 100px 20px; }
  .section-wrap.alt-bg { background: var(--bg-light); }
  .section-header { text-align: center; max-width: 700px; margin: 0 auto 60px; }
  .section-tag { color: var(--primary); font-weight: 800; text-transform: uppercase; font-size: 0.95rem; letter-spacing: 1px;}
  .section-title { font-size: 2.8rem; font-weight: 900; margin: 15px 0; color: #0f172a; letter-spacing: -1px;}
  
  .target-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 30px; max-width: 1200px; margin: 0 auto; }
  .target-card { background: white; padding: 40px 30px; border-radius: 20px; box-shadow: 0 10px 30px rgba(0,0,0,0.04); border: 1px solid var(--border); text-align: center;}
  .target-icon { font-size: 3rem; margin-bottom: 20px; }
  .target-card h3 { font-size: 1.5rem; font-weight: 800; color: #0f172a; margin-bottom: 15px; }
  .target-card p { color: var(--text-light); line-height: 1.6; }

  /* ==========================================
     4. METHODOLOGY (THE PROCESS)
     ========================================== */
  .process-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(320px, 1fr)); gap: 40px; max-width: 1200px; margin: 0 auto; position: relative;}
  .step-card { background: white; border-radius: 20px; padding: 40px; border: 1px solid var(--border); position: relative; transition: 0.3s; z-index: 2;}
  .step-card:hover { transform: translateY(-10px); box-shadow: 0 20px 40px rgba(0,0,0,0.08); border-color: var(--primary);}
  .step-number { position: absolute; top: -20px; left: -20px; width: 50px; height: 50px; background: var(--accent); color: white; display: flex; align-items: center; justify-content: center; font-size: 1.5rem; font-weight: 900; border-radius: 50%; box-shadow: 0 10px 20px rgba(245, 158, 11, 0.3);}
  .step-card h3 { font-size: 1.5rem; font-weight: 800; color: #0f172a; margin-bottom: 15px; margin-top: 10px;}
  .step-card p { color: var(--text-light); line-height: 1.7; font-size: 1.05rem; margin-bottom: 20px;}
  .step-link { color: var(--primary); font-weight: 800; text-decoration: none; display: inline-flex; align-items: center; gap: 5px; cursor: pointer;}
  .step-link:hover { text-decoration: underline; }

  /* ==========================================
     5. TESTIMONIALS
     ========================================== */
  .testimonial-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(400px, 1fr)); gap: 30px; max-width: 1000px; margin: 0 auto; }
  .testimonial-card { background: white; padding: 40px; border-radius: 20px; box-shadow: 0 10px 30px rgba(0,0,0,0.05); position: relative; border-left: 5px solid var(--primary);}
  .quote-mark { position: absolute; top: 20px; right: 20px; font-size: 4rem; color: rgba(37, 99, 235, 0.1); font-family: Georgia, serif; line-height: 1;}
  .testimonial-text { font-size: 1.15rem; color: #0f172a; line-height: 1.7; font-style: italic; margin-bottom: 25px; position: relative; z-index: 2;}
  .testimonial-author { display: flex; align-items: center; gap: 15px; }
  .author-avatar { width: 50px; height: 50px; border-radius: 50%; background: var(--bg-light); display: flex; align-items: center; justify-content: center; font-weight: bold; color: var(--primary); font-size: 1.2rem;}
  .author-info h4 { margin: 0; font-size: 1rem; font-weight: 800; color: #0f172a;}
  .author-info span { font-size: 0.85rem; color: var(--text-light); text-transform: uppercase; font-weight: bold;}

  /* RESPONSIVE */
  @media (max-width: 900px) {
    .hero-wrapper { flex-direction: column; text-align: center; padding-top: 40px; }
    .hero-text { padding-right: 0; margin-bottom: 40px; }
    .hero-headline { font-size: 2.5rem; }
    .auth-box { margin: 20px auto; text-align: left; }
    .stats-grid { grid-template-columns: 1fr; gap: 30px; }
    .testimonial-grid { grid-template-columns: 1fr; }
  }
  @keyframes slideInLeft { from { opacity: 0; transform: translateX(-30px); } to { opacity: 1; transform: translateX(0); } }
  @keyframes slideInRight { from { opacity: 0; transform: translateX(30px); } to { opacity: 1; transform: translateX(0); } }
</style>

<div class="hero-wrapper">
  <div class="hero-text">
    <span class="hero-badge">Verified Career Intelligence</span>
    <h1 class="hero-headline">End the Confusion. <br>Map Your Future with <span>Clinical Precision.</span></h1>
    <p class="hero-subhead">
      We replace guesswork with science. Get personalized career roadmaps powered by clinical psychometrics and expert 1-on-1 counseling for students in Class 8 to 12.
    </p>
  </div>
  
  <div class="hero-visual">
    <div class="auth-box" id="loginBoxUI">
        <h3 style="margin-top:0; color:var(--text-dark); font-size: 1.4rem; font-weight: 900;">Access Your Dashboard</h3>
        <p style="color:var(--text-light); font-size:0.9rem; margin-bottom:20px;">Parents, Students, and Counsellors login here.</p>
        
        <input type="email" id="emailInput" class="auth-input" placeholder="Email Address">
        <input type="password" id="passwordInput" class="auth-input" placeholder="Password">
        
        <div class="auth-buttons">
            <button class="btn-auth btn-signin" id="emailLoginBtn">Sign In</button>
            <button class="btn-auth btn-signup" id="emailSignUpBtn">Register</button>
        </div>
        
        <div class="divider">OR SECURE LOGIN WITH</div>
        
        <button class="btn-google" id="googleLoginBtn">
            <img src="https://upload.wikimedia.org/wikipedia/commons/c/c1/Google_%22G%22_logo.svg" alt="Google Logo">
            Continue with Google
        </button>

        <p id="statusMsg"></p>
    </div>

    <div class="auth-box" id="welcomeBoxUI" style="display: none; text-align: center; padding: 50px 30px;">
        <div style="font-size: 4rem; margin-bottom: 15px; line-height:1;">👋</div>
        <h3 style="margin-top:0; color:var(--text-dark); font-size: 1.8rem; font-weight: 900;">Welcome Back,<br><span id="welcomeNameDisplay" style="color:var(--primary);"></span>!</h3>
        <p style="color:var(--text-light); margin-bottom: 30px; font-size: 1.05rem;">
            You are securely logged in as:<br>
            <strong id="loggedInEmailDisplay" style="color:#0f172a;">...</strong>
        </p>
        <button class="btn-auth btn-signin" id="fastTravelBtn" style="width: 100%; padding: 18px; font-size: 1.1rem; box-shadow: 0 10px 20px rgba(37,99,235,0.3);">
            Enter My Portal ➔
        </button>
    </div>
  </div>
</div>

<div class="stats-container">
  <div class="stats-grid">
    <div><div class="stat-number">5,000+</div><div class="stat-label">Students Mentored</div></div>
    <div><div class="stat-number">75+</div><div class="stat-label">Data Points Analyzed</div></div>
    <div><div class="stat-number">98%</div><div class="stat-label">Clarity Rate</div></div>
  </div>
</div>

<div class="section-wrap alt-bg">
  <div class="section-header">
    <span class="section-tag">Who We Help</span>
    <h2 class="section-title">Guidance for every stage.</h2>
    <p style="color:var(--text-light); font-size:1.15rem;">Whether you are choosing a stream or fighting over colleges, we bring clarity to the table.</p>
  </div>

  <div class="target-grid">
    <div class="target-card">
      <div class="target-icon">🎒</div>
      <h3>Class 8 to 12 Students</h3>
      <p>Discover your true aptitude. We help you choose the right stream (Science, Commerce, Arts) without the stress of peer pressure.</p>
    </div>
    <div class="target-card" style="border-top: 5px solid var(--accent);">
      <div class="target-icon">🎓</div>
      <h3>College & Graduates</h3>
      <p>Stuck in the wrong degree? We help undergrads pivot their careers, build strong portfolios, and target global Master's programs.</p>
    </div>
    <div class="target-card" style="border-top: 5px solid var(--success);">
      <div class="target-icon">👨‍👩‍👧</div>
      <h3>Anxious Parents</h3>
      <p>End the dining table arguments. Get verified, unbiased data on what career path actually suits your child's personality and market trends.</p>
    </div>
  </div>
</div>

<div class="section-wrap">
  <div class="section-header">
    <span class="section-tag">Our Methodology</span>
    <h2 class="section-title">How we find your path.</h2>
    <p style="color:var(--text-light); font-size:1.15rem;">A scientific, 3-step approach to career intelligence.</p>
  </div>

  <div class="process-grid">
    <div class="step-card">
      <div class="step-number">1</div>
      <h3>Clinical Assessment</h3>
      <p>Students take our proprietary 75-point psychometric test evaluating RIASEC traits, inherent aptitudes, and emotional resilience.</p>
      <a onclick="window.scrollTo({top:0, behavior:'smooth'})" class="step-link">Take the Test ➔</a>
    </div>
    <div class="step-card">
      <div class="step-number">2</div>
      <h3>Expert Counselling</h3>
      <p>Sit down (online or offline) with a certified clinical career psychologist to decode the report, resolve parent-student conflicts, and answer questions.</p>
      <a href="https://github.com/antoniovn96" target="_blank" class="step-link">Meet the Experts ➔</a>
    </div>
    <div class="step-card">
      <div class="step-number">3</div>
      <h3>Execution Roadmap</h3>
      <p>Walk away with a concrete action plan. Know exactly which stream to pick, which exams to prepare for, and what skills to build this year.</p>
      <a onclick="window.scrollTo({top:0, behavior:'smooth'})" class="step-link">View Sample Plan ➔</a>
    </div>
  </div>
</div>

<div class="section-wrap alt-bg">
    <div class="section-header">
      <span class="section-tag">Success Stories</span>
      <h2 class="section-title">Don't just take our word for it.</h2>
    </div>

    <div class="testimonial-grid">
        <div class="testimonial-card">
            <div class="quote-mark">"</div>
            <p class="testimonial-text">"Before Career Intel, we were constantly fighting about my son taking PCM. The clinical assessment proved his aptitude was actually in Financial Analytics. It saved us years of frustration."</p>
            <div class="testimonial-author">
                <div class="author-avatar">R</div>
                <div class="author-info">
                    <h4>Rajesh Sharma</h4>
                    <span>Parent of Grade 10 Student</span>
                </div>
            </div>
        </div>

        <div class="testimonial-card" style="border-left-color: var(--accent);">
            <div class="quote-mark">"</div>
            <p class="testimonial-text">"I thought I wanted to do engineering because my friends were doing it. The counselling session opened my eyes to Product Design. Now I actually enjoy studying for my entrance exams."</p>
            <div class="testimonial-author">
                <div class="author-avatar" style="color: var(--accent);">A</div>
                <div class="author-info">
                    <h4>Ananya V.</h4>
                    <span>Grade 12 Student</span>
                </div>
            </div>
        </div>
    </div>
</div>

<script type="module">
    import { initializeApp } from "https://www.gstatic.com/firebasejs/10.8.1/firebase-app.js";
    import { getFirestore, doc, getDoc } from "https://www.gstatic.com/firebasejs/10.8.1/firebase-firestore.js";
    import { getAuth, signInWithPopup, GoogleAuthProvider, signInWithEmailAndPassword, createUserWithEmailAndPassword, onAuthStateChanged } from "https://www.gstatic.com/firebasejs/10.8.1/firebase-auth.js";

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

    const SUPER_ADMIN_EMAIL = "antonio.antonio.noronha@gmail.com"; 

    const status = document.getElementById('statusMsg');
    const loginBoxUI = document.getElementById('loginBoxUI');
    const welcomeBoxUI = document.getElementById('welcomeBoxUI');
    const loggedInEmailDisplay = document.getElementById('loggedInEmailDisplay');
    const welcomeNameDisplay = document.getElementById('welcomeNameDisplay');
    const fastTravelBtn = document.getElementById('fastTravelBtn');
    
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
            if (email === SUPER_ADMIN_EMAIL.toLowerCase()) {
                if(status) status.innerText = "Welcome back! Routing to Master Control Center...";
                setTimeout(() => window.location.href = "admin.html", 1000);
                return;
            }

            const permsRef = doc(db, "permissions", email);
            const permsSnap = await getDoc(permsRef);

            if (permsSnap.exists()) {
                const role = permsSnap.data().role;
                if(status) status.innerText = `Authorized as ${role.replace('_', ' ')}. Connecting...`;
                setTimeout(() => {
                    if (role === "school_admin") window.location.href = "school_dashboard.html";
                    else if (role === "counsellor") window.location.href = "counsellor_dashboard.html";
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
