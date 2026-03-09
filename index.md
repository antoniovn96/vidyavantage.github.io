<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Career Intelligence | AI-Powered Discovery</title>
    <style>
        :root {
            --bg: #f8fafc;
            --primary: #3b82f6;
            --primary-hover: #2563eb;
            --secondary: #10b981;
            --accent: #f59e0b;
            --dark: #0f172a;
            --text-main: #334155;
            --text-muted: #64748b;
            --border: #e2e8f0;
            --danger: #ef4444;
        }
        
        body { 
            background-color: var(--bg); 
            font-family: 'Nunito', sans-serif; 
            color: var(--text-main); 
            margin: 0; 
            line-height: 1.6;
            overflow-x: hidden;
        }

        /* --- GLOBAL LAYOUT --- */
        .container { max-width: 1200px; margin: 0 auto; padding: 0 20px; }
        .section { padding: 80px 0; }
        .section-title { text-align: center; font-size: 2.5rem; color: var(--dark); font-weight: 900; margin-bottom: 15px; letter-spacing: -0.5px;}
        .section-subtitle { text-align: center; color: var(--text-muted); font-size: 1.1rem; max-width: 600px; margin: 0 auto 50px;}

        /* --- NAVBAR --- */
        header {
            background: rgba(255, 255, 255, 0.95);
            backdrop-filter: blur(10px);
            padding: 15px 0;
            border-bottom: 1px solid var(--border);
            position: fixed;
            width: 100%;
            top: 0;
            z-index: 1000;
        }
        .nav-inner { display: flex; justify-content: space-between; align-items: center; max-width: 1200px; margin: 0 auto; padding: 0 20px;}
        .logo { font-size: 1.4rem; font-weight: 900; color: var(--dark); display: flex; align-items: center; gap: 10px; text-decoration: none;}
        .logo span { background: var(--primary); color: white; padding: 4px 8px; border-radius: 8px; font-size: 1.1rem;}
        .btn-nav { background: var(--primary); color: white; padding: 10px 20px; border-radius: 8px; text-decoration: none; font-weight: 700; transition: 0.3s;}
        .btn-nav:hover { background: var(--primary-hover); transform: translateY(-2px); box-shadow: 0 4px 10px rgba(59,130,246,0.3);}

        /* --- HERO SECTION --- */
        .hero { padding: 160px 0 100px; background: radial-gradient(circle at top right, rgba(59, 130, 246, 0.08), transparent 40%), radial-gradient(circle at bottom left, rgba(245, 158, 11, 0.05), transparent 40%); text-align: center;}
        .hero-tag { display: inline-block; background: rgba(59,130,246,0.1); color: var(--primary); font-weight: 800; padding: 6px 16px; border-radius: 50px; font-size: 0.9rem; margin-bottom: 20px;}
        .hero h1 { font-size: 4rem; font-weight: 900; color: var(--dark); line-height: 1.1; margin-bottom: 20px; letter-spacing: -1.5px; max-width: 900px; margin-left: auto; margin-right: auto;}
        .hero p { font-size: 1.25rem; color: var(--text-muted); max-width: 700px; margin: 0 auto 40px;}
        .hero-buttons { display: flex; justify-content: center; gap: 15px; }
        .btn-large { background: var(--primary); color: white; border: none; padding: 16px 32px; font-size: 1.1rem; font-weight: 800; border-radius: 12px; cursor: pointer; transition: 0.3s; text-decoration: none; display: inline-block; box-shadow: 0 10px 25px rgba(59, 130, 246, 0.3);}
        .btn-large:hover { background: var(--primary-hover); transform: translateY(-3px); box-shadow: 0 15px 35px rgba(59, 130, 246, 0.4);}
        .btn-outline { background: white; color: var(--text-main); border: 2px solid var(--border); box-shadow: none;}
        .btn-outline:hover { border-color: var(--primary); color: var(--primary); transform: translateY(-3px);}

        /* --- TRUST STRIP --- */
        .trust-strip { background: white; border-top: 1px solid var(--border); border-bottom: 1px solid var(--border); padding: 40px 0;}
        .trust-grid { display: grid; grid-template-columns: repeat(4, 1fr); gap: 20px; text-align: center;}
        .trust-item h3 { font-size: 2.2rem; color: var(--primary); margin: 0 0 5px; font-weight: 900;}
        .trust-item p { margin: 0; color: var(--text-muted); font-weight: 700; font-size: 0.95rem; text-transform: uppercase;}

        /* --- PROBLEM SECTION --- */
        .problem-section { background: #fff; }
        .problem-card { background: #fff1f2; border: 1px solid #fecdd3; padding: 30px; border-radius: 16px; margin-bottom: 20px;}
        .problem-list { list-style: none; padding: 0; font-size: 1.1rem; color: var(--text-main);}
        .problem-list li { margin-bottom: 15px; display: flex; align-items: center; gap: 10px; font-weight: 600;}
        .problem-list li::before { content: '❌'; font-size: 1.2rem;}
        .problem-conclusion { background: var(--primary); color: white; padding: 25px; border-radius: 16px; text-align: center; font-size: 1.2rem; font-weight: 700; box-shadow: 0 10px 30px rgba(59,130,246,0.2);}

        /* --- SYSTEM / HOW IT WORKS --- */
        .steps-grid { display: grid; grid-template-columns: repeat(5, 1fr); gap: 20px; position: relative; }
        .step-card { background: white; padding: 30px 20px; border-radius: 16px; text-align: center; border: 1px solid var(--border); box-shadow: 0 10px 30px rgba(0,0,0,0.02); transition: 0.3s; position: relative; z-index: 2;}
        .step-card:hover { transform: translateY(-5px); border-color: var(--primary); box-shadow: 0 15px 40px rgba(59,130,246,0.1);}
        .step-num { width: 40px; height: 40px; background: var(--primary); color: white; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-weight: 900; font-size: 1.2rem; margin: 0 auto 15px;}
        .step-card h4 { margin: 0 0 10px; font-size: 1.1rem; color: var(--dark);}

        /* --- PARENT SECTION --- */
        .parent-section { background: var(--dark); color: white; text-align: center;}
        .parent-section .section-title { color: white; }
        .parent-section .section-subtitle { color: #94a3b8; }
        .parent-grid { display: grid; grid-template-columns: repeat(3, 1fr); gap: 30px; margin-top: 40px;}
        .parent-card { background: rgba(255,255,255,0.05); padding: 30px; border-radius: 16px; border: 1px solid rgba(255,255,255,0.1);}
        .parent-card h4 { color: var(--secondary); font-size: 1.2rem; margin: 0 0 10px;}

        /* --- STORY & REPORT SECTION --- */
        .split-grid { display: grid; grid-template-columns: 1fr 1fr; gap: 50px; align-items: center;}
        .story-card { background: white; padding: 40px; border-radius: 20px; border: 1px solid var(--border); box-shadow: 0 20px 40px rgba(0,0,0,0.05);}
        .badge { display: inline-block; padding: 4px 12px; border-radius: 50px; font-size: 0.8rem; font-weight: 800; text-transform: uppercase;}
        .badge-before { background: #fee2e2; color: #ef4444; }
        .badge-after { background: #d1fae5; color: #059669; }

        /* --- DASHBOARD PREVIEW --- */
        .dash-mockup { background: white; border-radius: 16px; border: 1px solid var(--border); box-shadow: 0 25px 50px rgba(0,0,0,0.1); overflow: hidden; display: flex; height: 400px; max-width: 900px; margin: 0 auto;}
        .mock-sidebar { width: 200px; background: var(--dark); padding: 20px;}
        .mock-line { height: 12px; background: rgba(255,255,255,0.1); border-radius: 6px; margin-bottom: 15px;}
        .mock-content { flex: 1; padding: 30px; background: #f8fafc;}
        .mock-header { height: 30px; width: 40%; background: #e2e8f0; border-radius: 8px; margin-bottom: 30px;}
        .mock-grid { display: grid; grid-template-columns: 1fr 1fr 1fr; gap: 20px;}
        .mock-card { height: 100px; background: white; border-radius: 12px; border: 1px solid #e2e8f0;}

        /* --- FAQ --- */
        details.faq-item { background: white; border: 1px solid var(--border); border-radius: 12px; margin-bottom: 15px; overflow: hidden; transition: 0.3s;}
        details.faq-item summary { padding: 20px; font-weight: 800; font-size: 1.1rem; color: var(--dark); cursor: pointer; display: flex; justify-content: space-between; align-items: center; list-style: none; outline: none; }
        details.faq-item summary::-webkit-details-marker { display: none; }
        details.faq-item summary::after { content: '+'; color: var(--primary); font-size: 1.5rem;}
        details.faq-item[open] summary::after { content: '×'; color: var(--danger);}
        details.faq-item[open] summary { border-bottom: 1px solid var(--border); }
        .faq-body { padding: 20px; background: #f8fafc; color: var(--text-main); font-size: 1rem; line-height: 1.6;}

        /* --- LOGIN SECTION (BOTTOM) --- */
        .login-section { background: var(--bg); border-top: 1px solid var(--border); padding: 80px 0; }
        .login-card-container { max-width: 450px; margin: 0 auto; background: white; padding: 40px; border-radius: 20px; box-shadow: 0 20px 50px rgba(15, 23, 42, 0.08); border: 1px solid rgba(255,255,255,0.5);}
        .form-group { margin-bottom: 20px; }
        .form-label { display: block; font-weight: 700; margin-bottom: 8px; color: var(--text-muted); font-size: 0.85rem; text-transform: uppercase;}
        .form-input { width: 100%; padding: 14px; border-radius: 10px; border: 2px solid var(--border); background: #f8fafc; color: var(--dark); box-sizing: border-box; font-family: inherit; font-size: 1rem; transition: 0.3s;}
        .form-input:focus { border-color: var(--primary); outline: none; background: white;}
        .divider { display: flex; align-items: center; text-align: center; margin: 20px 0; color: var(--text-muted); font-size: 0.85rem; font-weight: bold; text-transform: uppercase;}
        .divider::before, .divider::after { content: ''; flex: 1; border-bottom: 1px solid var(--border); }
        .divider::before { margin-right: .75em; }
        .divider::after { margin-left: .75em; }
        .btn-google { width: 100%; background: white; color: var(--text-main); border: 2px solid var(--border); padding: 14px; font-size: 1.05rem; font-weight: 800; border-radius: 12px; cursor: pointer; transition: 0.3s; display: inline-flex; align-items: center; justify-content: center; gap: 10px;}
        .btn-google:hover { background: #f8fafc; border-color: #cbd5e1;}
        .error-msg { color: var(--danger); font-size: 0.85rem; margin-top: 10px; font-weight: 600; text-align: center; display: none;}

        footer { background: var(--dark); color: #64748b; text-align: center; padding: 30px; font-size: 0.9rem;}

        /* --- MOBILE RESPONSIVENESS --- */
        @media (max-width: 900px) {
            .hero h1 { font-size: 2.8rem; }
            .hero-buttons { flex-direction: column; }
            .trust-grid, .steps-grid, .parent-grid, .split-grid { grid-template-columns: 1fr; }
            .step-card { margin-bottom: 10px; }
            .dash-mockup { display: none; /* hide mockup on mobile for space */ }
        }
    </style>
</head>
<body>

<header>
    <div class="nav-inner">
        <a href="#" class="logo"><span>AI</span> Career Intelligence</a>
        <div id="nav-auth-container">
            <a href="#loginArea" style="color:var(--text-main); text-decoration:none; font-weight:800; margin-right:20px;">Login</a>
            <a href="register.html" class="btn-nav">Register</a>
        </div>
    </div>
</header>

<section class="hero">
    <div class="container">
        <span class="hero-tag">Class 8th - 12th & Undergraduates</span>
        <h1>Confused About Science, Commerce or Arts?</h1>
        <p>Discover the Right Career Path Before It’s Too Late. AI-powered psychometric testing combined with expert human counsellors to help you make confident, data-driven career decisions.</p>
        <div class="hero-buttons">
            <a href="register.html" class="btn-large">Take Career Assessment →</a>
            <a href="#howItWorks" class="btn-large btn-outline">See How It Works</a>
        </div>
    </div>
</section>

<section class="trust-strip">
    <div class="container trust-grid">
        <div class="trust-item"><h3>5000+</h3><p>Students Guided</p></div>
        <div class="trust-item"><h3>98%</h3><p>Clarity Improvement</p></div>
        <div class="trust-item"><h3>75+</h3><p>Data Points Analyzed</p></div>
        <div class="trust-item"><h3>100%</h3><p>Scientific Method</p></div>
    </div>
</section>

<section class="section problem-section">
    <div class="container split-grid">
        <div>
            <h2 class="section-title" style="text-align: left;">Why Most Students Choose the Wrong Career</h2>
            <p style="font-size: 1.1rem; color: var(--text-muted); margin-bottom: 30px;">Every year, millions of students make life-altering stream and college choices based on flawed metrics. Are you making these common mistakes?</p>
            <ul class="problem-list">
                <li>Choosing Science just because you got good marks.</li>
                <li>Following the exact same path as your friends.</li>
                <li>Succumbing to pressure from relatives and society.</li>
                <li>Discovering you hate the subjects only after 12th grade.</li>
            </ul>
        </div>
        <div class="problem-conclusion">
            "Career decisions should be based on natural aptitude, inherent personality, and long-term strengths — not guesswork."
        </div>
    </div>
</section>

<section class="section" id="howItWorks">
    <div class="container">
        <h2 class="section-title">How Our Intelligence System Works</h2>
        <p class="section-subtitle">A simple, 5-step scientific approach to completely eliminate career confusion.</p>
        
        <div class="steps-grid">
            <div class="step-card">
                <div class="step-num">1</div>
                <h4>Create Profile</h4>
                <p style="font-size:0.85rem; color:var(--text-muted); margin:0;">Log your academic history, hobbies, and interests.</p>
            </div>
            <div class="step-card">
                <div class="step-num">2</div>
                <h4>Take Assessment</h4>
                <p style="font-size:0.85rem; color:var(--text-muted); margin:0;">Complete the 25-minute AI Psychometric Test.</p>
            </div>
            <div class="step-card">
                <div class="step-num">3</div>
                <h4>Get Matches</h4>
                <p style="font-size:0.85rem; color:var(--text-muted); margin:0;">Review your RIASEC code and top career pathways.</p>
            </div>
            <div class="step-card">
                <div class="step-num">4</div>
                <h4>Meet Expert</h4>
                <p style="font-size:0.85rem; color:var(--text-muted); margin:0;">Discuss your results 1-on-1 with a certified counselor.</p>
            </div>
            <div class="step-card" style="border-color: var(--primary); background: rgba(59,130,246,0.05);">
                <div class="step-num" style="background: var(--accent);">5</div>
                <h4 style="color:var(--primary);">Get Roadmap</h4>
                <p style="font-size:0.85rem; color:var(--text-muted); margin:0;">Lock your path and receive a 1-year execution strategy.</p>
            </div>
        </div>
    </div>
</section>

<section class="section" style="background: white;">
    <div class="container split-grid">
        <div class="story-card">
            <h3 style="margin-top:0; color:var(--dark);">Real Student Transformation</h3>
            <div style="margin-bottom: 20px;">
                <span class="badge badge-before">Before Assessment</span>
                <p style="margin:5px 0 0; color:var(--text-muted); font-style:italic;">"Wanted to do Engineering because my friends chose it. I hated math but felt I had no choice."</p>
            </div>
            <div style="margin-bottom: 20px;">
                <span class="badge" style="background: #e0e7ff; color: #1e40af;">AI Discovery</span>
                <p style="margin:5px 0 0; color:var(--text-muted); font-weight:bold;">High Artistic + Investigative profile discovered. Strong aptitude for design logic.</p>
            </div>
            <div>
                <span class="badge badge-after">Now (Clarity Score: 9/10)</span>
                <p style="margin:5px 0 0; color:var(--dark); font-weight:bold; font-size:1.1rem;">Successfully preparing for Architecture (B.Arch) with high confidence.</p>
            </div>
        </div>
        
        <div>
            <h2 class="section-title" style="text-align: left;">Your Career Intelligence Report Includes:</h2>
            <ul class="problem-list" style="margin-top:20px;">
                <li style="color:var(--dark);">✅ Detailed RIASEC Personality Code Breakdown</li>
                <li style="color:var(--dark);">✅ Top 5 Career Matches (Ranked by Compatibility %)</li>
                <li style="color:var(--dark);">✅ Optimal Stream & Subject Recommendations</li>
                <li style="color:var(--dark);">✅ Vulnerability Zones (Careers leading to burnout)</li>
                <li style="color:var(--dark);">✅ 1-Year Career Execution & Study Plan</li>
            </ul>
        </div>
    </div>
</section>

<section class="section parent-section">
    <div class="container">
        <h2 class="section-title">Built for Parents Who Want Clarity — Not Conflict</h2>
        <p class="section-subtitle">We bridge the gap between student aspirations and parental expectations using hard data.</p>
        
        <div class="parent-grid">
            <div class="parent-card">
                <h4>📊 Scientific Decisions</h4>
                <p style="font-size:0.95rem; margin:0; opacity:0.8;">Remove the emotional bias. We use proven psychometric science to identify what your child is naturally built for.</p>
            </div>
            <div class="parent-card">
                <h4>👁️ Transparent Tracking</h4>
                <p style="font-size:0.95rem; margin:0; opacity:0.8;">Our dedicated "Parent View" allows you to log into the dashboard to review reports and track execution progress.</p>
            </div>
            <div class="parent-card">
                <h4>🤝 Family Alignment</h4>
                <p style="font-size:0.95rem; margin:0; opacity:0.8;">Our expert counsellors mediate sessions to ensure both parents and students are excited about the final career path.</p>
            </div>
        </div>
    </div>
</section>

<section class="section">
    <div class="container">
        <h2 class="section-title">Inside Your Career Dashboard</h2>
        <p class="section-subtitle">A premium digital workspace designed to keep students motivated, structured, and on track.</p>
        
        <div class="dash-mockup">
            <div class="mock-sidebar">
                <div class="mock-line" style="width: 80%; background:var(--primary); margin-bottom: 30px;"></div>
                <div class="mock-line" style="width: 100%;"></div>
                <div class="mock-line" style="width: 90%;"></div>
                <div class="mock-line" style="width: 95%;"></div>
            </div>
            <div class="mock-content">
                <div class="mock-header"></div>
                <div class="mock-grid">
                    <div class="mock-card" style="border-top: 4px solid var(--primary);"></div>
                    <div class="mock-card" style="border-top: 4px solid var(--secondary);"></div>
                    <div class="mock-card" style="border-top: 4px solid var(--accent);"></div>
                </div>
                <div style="margin-top:20px; height: 150px; background: white; border-radius: 12px; border: 1px solid #e2e8f0; display:flex; align-items:center; justify-content:center; color: #cbd5e1; font-weight:bold;">
                    Interactive Career Explorer Engine
                </div>
            </div>
        </div>
    </div>
</section>

<section class="section" style="background: white;">
    <div class="container" style="max-width: 800px;">
        <h2 class="section-title">Frequently Asked Questions</h2>
        
        <details class="faq-item" open>
            <summary>When is the right time to take a career assessment?</summary>
            <div class="faq-body">The ideal time is between Class 9 and Class 11. Testing in Class 9 or 10 helps you choose the correct stream (Science/Commerce/Arts). Testing in Class 11 or 12 helps you narrow down specific degrees and entrance exams. However, undergraduate students can also take it to pivot their majors.</div>
        </details>
        <details class="faq-item">
            <summary>How accurate are the psychometric tests?</summary>
            <div class="faq-body">Our system is based on the globally recognized Holland Code (RIASEC) theory, combined with modern cognitive pattern analysis. It boasts a 92%+ accuracy rate in identifying natural aptitudes when answered honestly by the student.</div>
        </details>
        <details class="faq-item">
            <summary>Can parents attend the expert counselling session?</summary>
            <div class="faq-body">Absolutely. We strongly encourage at least one parent to be present during the final roadmap session to ensure family alignment and proper execution of the plan.</div>
        </details>
    </div>
</section>

<section class="login-section" id="loginArea">
    <div class="container">
        <h2 class="section-title" style="margin-bottom: 5px;">Stop Guessing Your Future.</h2>
        <p class="section-subtitle">25 minutes could save you years of academic confusion. Sign in or register below to begin.</p>

        <div class="login-card-container" id="authCardContainer">
            <h2 style="margin: 0 0 5px 0; font-size: 1.8rem; color: var(--dark); text-align:center;">Student Login</h2>
            <p style="margin: 0 0 25px 0; color: var(--text-muted); font-size: 0.95rem; text-align:center;">Enter your details to access your dashboard.</p>
            
            <form id="loginForm">
                <div class="form-group">
                    <label class="form-label">Email Address</label>
                    <input type="email" id="email" class="form-input" placeholder="student@school.com" required>
                </div>

                <div class="form-group" style="margin-bottom: 10px;">
                    <label class="form-label">Password</label>
                    <input type="password" id="password" class="form-input" placeholder="••••••••" required>
                </div>
                
                <div class="error-msg" id="errorMsg">Invalid email or password.</div>
                
                <button type="submit" class="btn-large" id="loginBtn">Secure Sign In</button>
            </form>

            <div class="divider"><span>OR</span></div>
            
            <button type="button" class="btn-google" id="googleBtn">
                <img src="https://www.svgrepo.com/show/475656/google-color.svg" alt="Google" style="width: 22px; height: 22px;">
                Sign in with Google
            </button>

            <div class="register-link">
                New to the Platform?<br><br>
                <a href="register.html">Click here to create an account.</a>
            </div>
        </div>
    </div>
</section>

<footer>
    <div class="container">
        &copy; 2026 Career Intelligence System. All rights reserved. Designed to empower students.
    </div>
</footer>

<script type="module">
    import { initializeApp } from "https://www.gstatic.com/firebasejs/10.8.1/firebase-app.js";
    import { getAuth, signInWithEmailAndPassword, onAuthStateChanged, GoogleAuthProvider, signInWithPopup, signOut } from "https://www.gstatic.com/firebasejs/10.8.1/firebase-auth.js";
    import { getFirestore, doc, setDoc, getDoc } from "https://www.gstatic.com/firebasejs/10.8.1/firebase-firestore.js";

    // ⚠️ REPLACE WITH YOUR FIREBASE CONFIG
    const firebaseConfig = {
      apiKey: "AIzaSyBygHYMOSuKueZf9nE5LmSwCyCeZ2dNeD0",
      authDomain: "career-intelligence-system.firebaseapp.com",
      projectId: "career-intelligence-system",
      storageBucket: "career-intelligence-system.firebasestorage.app",
      messagingSenderId: "223785446772",
      appId: "1:223785446772:web:0f9ded4e89a978fc551021"
    };

    const app = initializeApp(firebaseConfig);
    const auth = getAuth(app);
    const db = getFirestore(app);
    const provider = new GoogleAuthProvider();

    const authCardContainer = document.getElementById('authCardContainer');
    const navAuthContainer = document.getElementById('nav-auth-container');
    let isProcessingLogin = false;

    // --- SMART LOGGED-IN STATE DETECTION ---
    onAuthStateChanged(auth, (user) => {
        // Stop forcing redirect! Let them read the homepage if they want to.
        // Instead, we dynamically change the Login UI to a "Go to Dashboard" button.
        if (user && !isProcessingLogin) {
            
            // 1. Update Navbar
            if(navAuthContainer) {
                navAuthContainer.innerHTML = `<a href="student_portal.html" class="btn-nav">Dashboard ➔</a>`;
            }

            // 2. Update bottom Login Card to a Welcome Card
            if(authCardContainer) {
                authCardContainer.innerHTML = `
                    <div style="text-align:center;">
                        <div style="font-size: 3rem; margin-bottom: 10px;">👋</div>
                        <h2 style="color:var(--dark); margin:0 0 10px 0;">Welcome Back!</h2>
                        <p style="color:var(--text-muted); margin-bottom:25px;">You are already securely authenticated.</p>
                        <button onclick="window.location.href='student_portal.html'" class="btn-large" style="margin-bottom:15px;">Enter My Dashboard ➔</button>
                        <br>
                        <button id="quickLogoutBtn" style="background:none; border:none; color:var(--danger); cursor:pointer; font-weight:800; font-size:0.95rem; font-family:inherit; text-decoration:underline;">Sign Out</button>
                    </div>
                `;
                
                document.getElementById('quickLogoutBtn').addEventListener('click', () => {
                    signOut(auth).then(() => { window.location.reload(); });
                });
            }
        }
    });

    // 1. STANDARD EMAIL / PASSWORD LOGIN
    const loginForm = document.getElementById('loginForm');
    if (loginForm) {
        loginForm.addEventListener('submit', async (e) => {
            e.preventDefault();
            isProcessingLogin = true; 

            const email = document.getElementById('email').value.trim();
            const password = document.getElementById('password').value.trim();
            const loginBtn = document.getElementById('loginBtn');
            const googleBtn = document.getElementById('googleBtn');
            const errorMsg = document.getElementById('errorMsg');

            loginBtn.innerText = "Authenticating... ⏳";
            loginBtn.disabled = true;
            if(googleBtn) googleBtn.disabled = true;
            errorMsg.style.display = 'none';

            try {
                await signInWithEmailAndPassword(auth, email, password);
                window.location.href = "student_portal.html";
            } catch (error) {
                console.error("Login Error:", error.message);
                errorMsg.innerText = "Invalid email or password. Please verify your credentials.";
                errorMsg.style.display = 'block';
                loginBtn.innerText = "Secure Sign In";
                loginBtn.disabled = false;
                if(googleBtn) googleBtn.disabled = false;
                isProcessingLogin = false;
            }
        });
    }

    // 2. GOOGLE LOGIN
    const googleBtn = document.getElementById('googleBtn');
    if(googleBtn) {
        googleBtn.addEventListener('click', async () => {
            isProcessingLogin = true;
            const loginBtn = document.getElementById('loginBtn');
            const errorMsg = document.getElementById('errorMsg');

            googleBtn.innerText = "Connecting... ⏳";
            googleBtn.disabled = true;
            if(loginBtn) loginBtn.disabled = true;
            errorMsg.style.display = 'none';

            try {
                const result = await signInWithPopup(auth, provider);
                const user = result.user;

                // Safe check: If this is a brand new student using Google, initialize their empty profile
                const docRef = doc(db, "students", user.uid);
                const docSnap = await getDoc(docRef);
                
                if (!docSnap.exists()) {
                    await setDoc(docRef, {
                        name: user.displayName || "Student",
                        email: user.email,
                        schoolId: "GENERAL",
                        joinedAt: new Date().toISOString(),
                        assessmentCompleted: false,
                        sessionsHad: 0,
                        careerLocked: false,
                        academic: {}
                    }, { merge: true });
                }

                window.location.href = "student_portal.html";

            } catch (error) {
                console.error("Google Login Error:", error.message);
                errorMsg.innerText = "Google Sign-In failed or was cancelled.";
                errorMsg.style.display = 'block';
                googleBtn.innerHTML = `<img src="https://www.svgrepo.com/show/475656/google-color.svg" alt="Google" style="width: 22px; height: 22px;"> Sign in with Google`;
                googleBtn.disabled = false;
                if(loginBtn) loginBtn.disabled = false;
                isProcessingLogin = false;
            }
        });
    }
</script>

</body>
</html>
