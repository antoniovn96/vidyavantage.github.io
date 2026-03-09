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
            display: flex; 
            flex-direction: column; 
            min-height: 100vh;
        }

        /* --- NAVBAR --- */
        header {
            background: white;
            padding: 20px 50px;
            display: flex;
            justify-content: space-between;
            align-items: center;
            border-bottom: 1px solid var(--border);
            box-shadow: 0 4px 20px rgba(0,0,0,0.02);
            position: fixed;
            width: 100%;
            top: 0;
            box-sizing: border-box;
            z-index: 100;
        }
        .logo { font-size: 1.5rem; font-weight: 900; color: var(--dark); display: flex; align-items: center; gap: 10px;}
        .logo span { background: var(--primary); color: white; padding: 5px 10px; border-radius: 8px; }

        /* --- HERO SECTION --- */
        .hero {
            margin-top: 80px;
            display: flex;
            align-items: center;
            justify-content: center;
            flex: 1;
            padding: 40px 50px;
            background: radial-gradient(circle at top right, rgba(59, 130, 246, 0.1), transparent 50%),
                        radial-gradient(circle at bottom left, rgba(245, 158, 11, 0.05), transparent 50%);
        }
        
        .hero-content { flex: 1; max-width: 600px; padding-right: 50px; }
        .hero-content h1 { font-size: 3.5rem; font-weight: 900; color: var(--dark); line-height: 1.1; margin-bottom: 20px; letter-spacing: -1px;}
        .hero-content p { font-size: 1.2rem; color: var(--text-muted); line-height: 1.6; margin-bottom: 30px;}
        
        .feature-tags { display: flex; gap: 15px; margin-bottom: 40px; flex-wrap: wrap;}
        .tag { background: white; border: 1px solid var(--border); padding: 8px 16px; border-radius: 50px; font-size: 0.9rem; font-weight: 700; color: var(--primary); box-shadow: 0 4px 10px rgba(0,0,0,0.03);}

        /* --- LOGIN CARD --- */
        .login-wrapper { flex: 0.8; max-width: 450px; }
        .login-card {
            background: white;
            padding: 40px;
            border-radius: 20px;
            box-shadow: 0 20px 40px rgba(15, 23, 42, 0.08);
            border: 1px solid rgba(255,255,255,0.5);
        }
        .login-card h2 { margin: 0 0 5px 0; font-size: 1.8rem; color: var(--dark); }
        .login-card p { margin: 0 0 25px 0; color: var(--text-muted); font-size: 0.95rem; }

        .form-group { margin-bottom: 20px; }
        .form-label { display: block; font-weight: 700; margin-bottom: 8px; color: var(--text-muted); font-size: 0.85rem; text-transform: uppercase; letter-spacing: 0.5px;}
        .form-input { width: 100%; padding: 14px; border-radius: 10px; border: 2px solid var(--border); background: #f8fafc; color: var(--dark); box-sizing: border-box; font-family: inherit; font-size: 1rem; transition: 0.3s;}
        .form-input:focus { border-color: var(--primary); outline: none; background: white; box-shadow: 0 0 0 4px rgba(59, 130, 246, 0.1);}

        /* BIG LOGIN BUTTON */
        .btn-large { 
            width: 100%; 
            background: var(--primary); 
            color: white; 
            border: none; 
            padding: 18px; 
            font-size: 1.25rem; 
            font-weight: 900; 
            border-radius: 12px; 
            cursor: pointer; 
            transition: all 0.3s ease; 
            display: inline-flex; 
            align-items: center; 
            justify-content: center; 
            gap: 10px;
            margin-top: 10px;
            box-shadow: 0 8px 20px rgba(59, 130, 246, 0.25);
        }
        .btn-large:hover:not(:disabled) { background: var(--primary-hover); transform: translateY(-3px); box-shadow: 0 12px 25px rgba(59, 130, 246, 0.35);}
        .btn-large:disabled { background: #94a3b8; cursor: not-allowed; transform: none; box-shadow: none;}
        
        /* GOOGLE LOGIN STYLES */
        .divider { display: flex; align-items: center; text-align: center; margin: 20px 0; color: var(--text-muted); font-size: 0.85rem; font-weight: bold; text-transform: uppercase;}
        .divider::before, .divider::after { content: ''; flex: 1; border-bottom: 1px solid var(--border); }
        .divider::before { margin-right: .75em; }
        .divider::after { margin-left: .75em; }
        
        .btn-google {
            width: 100%; 
            background: white; 
            color: var(--text-main); 
            border: 2px solid var(--border); 
            padding: 14px; 
            font-size: 1.05rem; 
            font-weight: 800; 
            border-radius: 12px; 
            cursor: pointer; 
            transition: all 0.3s ease; 
            display: inline-flex; 
            align-items: center; 
            justify-content: center; 
            gap: 10px;
            box-shadow: 0 4px 10px rgba(0,0,0,0.02);
            font-family: 'Nunito', sans-serif;
        }
        .btn-google:hover:not(:disabled) { background: #f8fafc; border-color: #cbd5e1; transform: translateY(-2px); }
        .btn-google:disabled { opacity: 0.7; cursor: not-allowed; }

        .error-msg { color: var(--danger); font-size: 0.85rem; margin-top: 10px; font-weight: 600; text-align: center; display: none;}
        
        /* REGISTER LINK */
        .register-link { text-align: center; margin-top: 25px; font-size: 1.05rem; color: var(--text-muted); }
        .register-link a { color: var(--accent); font-weight: 900; text-decoration: none; border-bottom: 2px solid transparent; transition: 0.2s;}
        .register-link a:hover { border-bottom: 2px solid var(--accent); }

        /* MOBILE RESPONSIVENESS */
        @media (max-width: 900px) {
            .hero { flex-direction: column; padding: 40px 20px; margin-top: 70px; text-align: center;}
            .hero-content { padding-right: 0; margin-bottom: 40px;}
            .feature-tags { justify-content: center; }
            header { padding: 15px 20px; }
            .login-wrapper { width: 100%; max-width: 100%; }
        }
    </style>
</head>
<body>

<header>
    <div class="logo"><span>AI</span> Career Intelligence</div>
    <div style="font-weight: 700; color: var(--text-muted); font-size: 0.9rem;">Student Portal</div>
</header>

<div class="hero">
    <div class="hero-content">
        <h1>Discover Your True Career Path.</h1>
        <p>Take the guesswork out of your future. Combine AI-driven psychometric analysis with human expert counselling to map out your perfect 1-year execution strategy.</p>
        
        <div class="feature-tags">
            <div class="tag">🧠 Psychometric Matching</div>
            <div class="tag">📈 Stream Comparisons</div>
            <div class="tag">🤝 Expert Counselling</div>
        </div>
    </div>

    <div class="login-wrapper">
        <div class="login-card" id="authCardContainer">
            <h2>Student Login</h2>
            <p>Enter your details below to access your dashboard.</p>
            
            <form id="loginForm">
                <div class="form-group">
                    <label class="form-label">Email</label>
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
</div>

<script type="module">
    import { initializeApp } from "https://www.gstatic.com/firebasejs/10.8.1/firebase-app.js";
    import { getAuth, signInWithEmailAndPassword, onAuthStateChanged, GoogleAuthProvider, signInWithPopup, signOut } from "https://www.gstatic.com/firebasejs/10.8.1/firebase-auth.js";
    import { getFirestore, doc, setDoc, getDoc } from "https://www.gstatic.com/firebasejs/10.8.1/firebase-firestore.js";

    // ⚠️ Ensure this matches the config used in student_portal.html
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
    let isProcessingLogin = false;

    // --- SMART LOGGED-IN STATE DETECTION ---
    onAuthStateChanged(auth, (user) => {
        if (user && !isProcessingLogin) {
            // Instead of force-redirecting, we change the UI of the card!
            authCardContainer.innerHTML = `
                <h2>Welcome Back!</h2>
                <p>You are securely logged into Career Intelligence.</p>
                <button onclick="window.location.href='student_portal.html'" class="btn-large" style="margin-top:15px; margin-bottom:10px;">Access Dashboard ➔</button>
                <div style="text-align:center; margin-top:20px;">
                    <button id="quickLogoutBtn" style="background:none; border:none; color:var(--danger); cursor:pointer; font-weight:800; font-size:0.95rem; font-family:inherit;">Sign Out Securely</button>
                </div>
            `;
            
            document.getElementById('quickLogoutBtn').addEventListener('click', () => {
                signOut(auth).then(() => { window.location.reload(); });
            });
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
            googleBtn.disabled = true;
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
                googleBtn.disabled = false;
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
            loginBtn.disabled = true;
            errorMsg.style.display = 'none';

            try {
                const result = await signInWithPopup(auth, provider);
                const user = result.user;

                // Safe check: If this is a completely brand new student using Google, initialize their profile
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
                loginBtn.disabled = false;
                isProcessingLogin = false;
            }
        });
    }
</script>

</body>
</html>
