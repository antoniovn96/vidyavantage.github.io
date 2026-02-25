---
layout: default
title: "The Ultimate Career Roadmap 🚀"
permalink: /career-search/
---

<style>
  /* --- GLOBAL RESETS --- */
  .main-content { max-width: 100% !important; padding: 0 !important; margin: 0 !important; }
  body { 
    background-color: #f8fafc; 
    background-image: radial-gradient(#cbd5e1 1px, transparent 1px); 
    background-size: 30px 30px; 
    font-family: 'Inter', 'Segoe UI', sans-serif; 
    overflow-x: hidden;
  }

  /* --- HEADER (Fixed Visibility & Vibrant Premium Look) --- */
  .roadmap-header { 
    text-align: center; 
    padding: 90px 20px 50px; 
    background: linear-gradient(135deg, #1e3a8a 0%, #3b82f6 100%); 
    color: #ffffff !important; 
    position: relative;
    box-shadow: 0 10px 30px rgba(59, 130, 246, 0.2);
  }
  .roadmap-header h1 { 
    margin: 0; 
    font-size: 3.2rem; 
    font-weight: 900; 
    letter-spacing: -1px;
    color: #ffffff !important; 
    text-shadow: 0 2px 10px rgba(0,0,0,0.2);
  }
  .roadmap-header p { 
    font-size: 1.2rem; 
    color: #e0f2fe !important; 
    margin-top: 15px; 
    font-weight: 400;
  }
  .back-btn { 
    position: absolute; 
    top: 20px; 
    left: 20px; 
    color: white !important; 
    text-decoration: none; 
    font-weight: bold; 
    background: rgba(255,255,255,0.2); 
    padding: 8px 20px; 
    border-radius: 50px; 
    z-index: 10; 
    backdrop-filter: blur(5px);
    transition: 0.2s;
  }
  .back-btn:hover { background: rgba(255,255,255,0.3); transform: translateX(-5px); }

  /* --- SMART FILTERS (Glassmorphism) --- */
  .filter-container { 
    background: rgba(255, 255, 255, 0.85); 
    backdrop-filter: blur(12px);
    padding: 15px 20px; 
    box-shadow: 0 4px 20px rgba(0,0,0,0.05); 
    position: sticky; 
    top: 70px; 
    z-index: 100; 
    border-bottom: 1px solid rgba(255,255,255,0.5);
  }
  .filter-scroll { display: flex; gap: 12px; overflow-x: auto; padding-bottom: 5px; max-width: 1300px; margin: 0 auto; scrollbar-width: none;}
  .filter-scroll::-webkit-scrollbar { display: none; }
  
  .filter-btn { background: #f1f5f9; border: 1px solid #e2e8f0; color: #475569; padding: 10px 20px; border-radius: 50px; font-size: 0.9rem; font-weight: 700; cursor: pointer; white-space: nowrap; transition: 0.2s; display: flex; align-items: center; gap: 6px;}
  .filter-btn:hover { background: #e2e8f0; transform: translateY(-2px);}
  .filter-btn.active { background: #1e293b; color: white; border-color: #1e293b; box-shadow: 0 4px 10px rgba(15, 23, 42, 0.3);}

  .parent-mode-toggle { background: #fef3c7; color: #d97706; border: 2px solid #f59e0b; padding: 10px 20px; border-radius: 50px; font-weight: 900; cursor: pointer; transition: 0.3s; display: flex; align-items: center; gap: 8px; margin-left: auto; white-space: nowrap;}
  .parent-mode-toggle.active { background: #d97706; color: white; box-shadow: 0 4px 10px rgba(217, 119, 6, 0.3);}

  /* --- INTERACTIVE TREE CSS (Blueprint Style) --- */
  .tree-wrapper { max-width: 1400px; margin: 0 auto; padding: 50px 20px 150px; overflow-x: auto; min-height: 70vh;}
  ul.tree, ul.tree ul { list-style: none; margin: 0; padding: 0; }
  ul.tree ul { margin-left: 50px; position: relative; }
  /* Dashed vertical connector */
  ul.tree ul:before { content: ""; display: block; width: 0; position: absolute; top: 0; bottom: 0; left: 0; border-left: 2px dashed #94a3b8; }
  ul.tree li { margin: 0; padding: 0 25px; line-height: 4.5em; position: relative; }
  /* Dashed horizontal connector */
  ul.tree ul li:before { content: ""; display: block; width: 25px; height: 0; border-top: 2px dashed #94a3b8; position: absolute; top: 2.25em; left: 0; }
  ul.tree ul li:last-child:before { background: #f8fafc; height: auto; top: 2.25em; bottom: 0; }

  /* --- NODE CARDS (Premium UI) --- */
  .node-box { 
    display: inline-flex; 
    align-items: center; 
    padding: 12px 24px; 
    border: none; 
    background: white; 
    border-radius: 12px; 
    font-weight: 800; 
    color: #1e293b; 
    cursor: pointer; 
    transition: all 0.2s cubic-bezier(0.25, 0.8, 0.25, 1); 
    font-size: 0.95rem; 
    position: relative; 
    z-index: 2; 
    box-shadow: 0 4px 10px rgba(0,0,0,0.06); 
    min-width: 200px; 
  }
  .node-box:hover { transform: translateY(-4px) scale(1.02); box-shadow: 0 15px 25px rgba(0,0,0,0.1); }
  
  .node-box.active { 
    background: linear-gradient(135deg, #1e293b 0%, #0f172a 100%); 
    color: white; 
    box-shadow: 0 0 0 5px rgba(59, 130, 246, 0.3); 
    border-color: transparent !important;
  }
  .node-box.filtered-out { opacity: 0.2; pointer-events: none; filter: grayscale(100%);}

  /* Beautiful Color Coding */
  #sci, #sci ~ ul .node-box { border-left: 6px solid #3b82f6; } /* Science Blue */
  #comm, #comm ~ ul .node-box { border-left: 6px solid #10b981; } /* Commerce Green */
  #arts, #arts ~ ul .node-box { border-left: 6px solid #8b5cf6; } /* Arts Purple */
  #def, #def ~ ul .node-box { border-left: 6px solid #f59e0b; } /* Defense Orange */
  
  .node-box.exam-node { background: #f1f5f9; font-size: 0.85rem; border-left: 6px solid #64748b !important; padding: 8px 18px; font-weight: 600;}
  .node-box.switch { background: #fffaf0; border: 2px dashed #f59e0b !important; border-left: none !important; color: #d97706; }

  /* --- PREMIUM INFO PANEL --- */
  .info-panel { position: fixed; bottom: 30px; right: 30px; width: 420px; background: white; border-top: 6px solid #3b82f6; box-shadow: 0 25px 50px -12px rgba(0,0,0,0.3); padding: 30px; border-radius: 20px; display: none; z-index: 1000; animation: slideIn 0.3s cubic-bezier(0.175, 0.885, 0.32, 1.275); max-height: 85vh; overflow-y: auto; box-sizing: border-box;}
  @keyframes slideIn { from { transform: translateY(100%); opacity: 0; } to { transform: translateY(0); opacity: 1; } }
  
  .panel-header { display: flex; justify-content: space-between; align-items: flex-start; margin-bottom: 20px;}
  .panel-title { margin: 0; font-size: 1.6rem; color: #0f172a; font-weight: 900; line-height: 1.2;}
  
  .meter-box { background: #f8fafc; padding: 18px; border-radius: 12px; margin-bottom: 20px; border: 1px solid #e2e8f0;}
  .meter-row { display: flex; justify-content: space-between; align-items: center; margin-bottom: 8px; font-size: 0.85rem; font-weight: bold; color: #334155;}
  .stars { color: #f59e0b; letter-spacing: 2px; font-size: 1.1rem;}
  
  .salary-bar-wrap { background: #e2e8f0; height: 12px; border-radius: 6px; margin-top: 5px; overflow: hidden; display: flex;}
  .salary-fresher { background: #93c5fd; height: 100%; width: 30%; }
  .salary-mid { background: #3b82f6; height: 100%; width: 40%; }
  .salary-top { background: #1e3a8a; height: 100%; width: 30%; }
  .salary-labels { display: flex; justify-content: space-between; font-size: 0.75rem; color: #64748b; margin-top: 5px; font-weight: 800;}

  .avoid-box { background: #fef2f2; border: 1px solid #fca5a5; padding: 15px; border-radius: 12px; margin-bottom: 20px;}
  .avoid-box h4 { margin: 0 0 10px 0; color: #dc2626; font-size: 0.95rem; font-weight: 800;}
  .avoid-box ul { margin: 0; padding-left: 20px; font-size: 0.9rem; color: #7f1d1d; line-height: 1.5;}

  .desc-text { font-size: 1rem; color: #475569; line-height: 1.6; margin-bottom: 25px;}
  .parent-warning { display: none; background: #fffbeb; color: #b45309; padding: 12px; border-radius: 8px; font-size: 0.9rem; font-weight: bold; margin-bottom: 15px; border: 1px solid #fde68a;}

  .action-btn { background: #3b82f6; color: white; padding: 15px; text-align: center; border-radius: 12px; font-weight: 900; display: block; text-decoration: none; transition: 0.2s; font-size: 1.05rem;}
  .action-btn:hover { background: #1d4ed8; transform: translateY(-2px); box-shadow: 0 10px 20px rgba(37,99,235,0.3);}
  .btn-outline { background: transparent; border: 2px solid #cbd5e1; color: #475569; width: 100%; padding: 12px; border-radius: 12px; margin-bottom: 15px; cursor: pointer; font-weight: bold; transition: 0.2s;}
  .btn-outline:hover { background: #f1f5f9; border-color: #94a3b8; color: #0f172a;}

  /* Smart Popup */
  .smart-popup { position: fixed; bottom: 30px; left: 30px; background: #0f172a; color: white; padding: 20px 25px; border-radius: 16px; box-shadow: 0 20px 40px rgba(0,0,0,0.3); z-index: 2000; display: none; animation: popUp 0.5s cubic-bezier(0.175, 0.885, 0.32, 1.275); border-left: 5px solid #f59e0b; max-width: 320px;}
  @keyframes popUp { 0% { transform: scale(0.8); opacity: 0; } 100% { transform: scale(1); opacity: 1; } }

  /* ==========================================
     MOBILE RESPONSIVE STYLES 
     ========================================== */
  @media (max-width: 768px) {
    .roadmap-header { padding: 90px 15px 40px; }
    .roadmap-header h1 { font-size: 2.2rem; }
    .roadmap-header p { font-size: 1rem; }
    
    .back-btn { top: 15px; left: 15px; padding: 6px 15px; font-size: 0.85rem; }

    .filter-container { padding: 10px; }
    .filter-btn { padding: 8px 14px; font-size: 0.85rem; }
    .parent-mode-toggle { padding: 8px 14px; font-size: 0.85rem; margin-left: 0; }

    .tree-wrapper { padding: 30px 10px 150px; }
    .node-box { min-width: 150px; padding: 10px 16px; font-size: 0.85rem; }
    ul.tree li { padding: 0 15px; }
    ul.tree ul { margin-left: 30px; }

    /* Bottom Sheet Info Panel */
    .info-panel {
      width: 100%;
      bottom: 0;
      right: 0;
      left: 0;
      border-radius: 25px 25px 0 0;
      padding: 25px 20px;
      max-height: 85vh;
    }
    .panel-title { font-size: 1.4rem; }
    
    .smart-popup { width: 90%; left: 5%; bottom: 20px; max-width: none; box-sizing: border-box; }
  }
</style>

<div class="roadmap-header">
  <a href="{{ '/' | relative_url }}" class="back-btn">← Home</a>
  <h1>The Career GPS 🧭</h1>
  <p>Stop guessing. Click the filters below to instantly reveal the best paths for you.</p>
</div>

<div class="filter-container">
    <div class="filter-scroll">
        <button class="filter-btn active" onclick="applyFilter('all', this)">Show All</button>
        <button class="filter-btn" onclick="applyFilter('high_salary', this)">💰 High Salary First</button>
        <button class="filter-btn" onclick="applyFilter('low_comp', this)">🧠 Low Competition</button>
        <button class="filter-btn" onclick="applyFilter('no_math', this)">📚 Without Maths</button>
        <button class="filter-btn" onclick="applyFilter('no_neetjee', this)">🚫 Without NEET/JEE</button>
        <button class="filter-btn" onclick="applyFilter('abroad', this)">🌍 Study Abroad Friendly</button>
        
        <button class="parent-mode-toggle" id="parentModeBtn" onclick="toggleParentMode()">👨‍👩‍👧 Parent Mode: OFF</button>
    </div>
</div>

<div class="tree-wrapper">
  <ul class="tree">
    <li>
      <span class="node-box" id="root" onclick="selectNode('root', null)" style="border-left: 6px solid #0f172a; background: #0f172a; color: white; font-size:1.1rem; padding: 15px 30px;">🎓 Class 10th Base</span>
      <ul>
        
        <li>
          <span class="node-box" id="sci" onclick="selectNode('sci', 'root')" data-tags="high_salary abroad">🔬 Science Stream</span>
          <ul id="sci_tree">
            <li>
              <span class="node-box" id="med_track" onclick="selectNode('med_track', 'sci')" data-tags="high_salary no_math">🩺 Medical (PCB)</span>
              <ul>
                <li>
                  <span class="node-box" id="mbbs" onclick="selectNode('mbbs', 'med_track')" data-tags="high_salary no_math">👨‍⚕️ MBBS (Doctor)</span>
                  <ul><li><span class="node-box exam-node" id="neet" onclick="selectNode('neet', 'mbbs')">📝 Gateway: NEET UG</span></li></ul>
                </li>
                <li><span class="node-box" id="biotech" onclick="selectNode('biotech', 'med_track')" data-tags="abroad low_comp no_math no_neetjee">🧬 Biotechnology</span></li>
                <li><span class="node-box" id="forensic" onclick="selectNode('forensic', 'med_track')" data-tags="low_comp no_math no_neetjee">🔍 Forensic Science</span></li>
                <li><span class="node-box" id="marine" onclick="selectNode('marine', 'med_track')" data-tags="low_comp no_math no_neetjee abroad">🐋 Marine Biology</span></li>
              </ul>
            </li>
            
            <li>
              <span class="node-box" id="eng_track" onclick="selectNode('eng_track', 'sci')" data-tags="high_salary abroad">⚙️ Engineering (PCM)</span>
              <ul>
                <li>
                  <span class="node-box" id="btech" onclick="selectNode('btech', 'eng_track')" data-tags="high_salary abroad">💻 B.Tech (CSE/AI)</span>
                  <ul>
                      <li><span class="node-box exam-node" id="jee" onclick="selectNode('jee', 'btech')">📝 Exam: JEE Mains/Adv</span></li>
                      <li><span class="node-box exam-node" id="bits" onclick="selectNode('bits', 'btech')">📝 Exam: BITSAT</span></li>
                  </ul>
                </li>
                <li><span class="node-box" id="cyber" onclick="selectNode('cyber', 'eng_track')" data-tags="high_salary low_comp abroad">🛡️ Cyber Security</span></li>
                <li><span class="node-box" id="space" onclick="selectNode('space', 'eng_track')" data-tags="low_comp">🚀 Space Tech (ISRO)</span></li>
                <li><span class="node-box" id="aviation" onclick="selectNode('aviation', 'eng_track')" data-tags="high_salary low_comp abroad">✈️ Commercial Pilot</span></li>
                <li><span class="node-box" id="arch" onclick="selectNode('arch', 'eng_track')" data-tags="no_neetjee abroad">🏛️ Architecture (B.Arch)</span></li>
              </ul>
            </li>
          </ul>
        </li>

        <li>
          <span class="node-box" id="comm" onclick="selectNode('comm', 'root')" data-tags="high_salary no_neetjee">📈 Commerce Stream</span>
          <ul id="comm_tree">
            <li>
              <span class="node-box" id="ca" onclick="selectNode('ca', 'comm')" data-tags="high_salary no_neetjee">📊 Chartered Accountant (CA)</span>
            </li>
            <li><span class="node-box" id="acca" onclick="selectNode('acca', 'comm')" data-tags="high_salary no_neetjee abroad">🌍 ACCA (Global CA)</span></li>
            <li><span class="node-box" id="ib" onclick="selectNode('ib', 'comm')" data-tags="high_salary abroad">🏦 Investment Banking</span></li>
            <li><span class="node-box" id="actuary" onclick="selectNode('actuary', 'comm')" data-tags="high_salary low_comp abroad">📉 Actuarial Science</span></li>
            <li><span class="node-box" id="supply" onclick="selectNode('supply', 'comm')" data-tags="low_comp abroad no_neetjee no_math">📦 Supply Chain Management</span></li>
            <li><span class="node-box" id="fintech" onclick="selectNode('fintech', 'comm')" data-tags="high_salary abroad no_neetjee">💳 FinTech & Analytics</span></li>
          </ul>
        </li>

        <li>
          <span class="node-box" id="arts" onclick="selectNode('arts', 'root')" data-tags="no_math no_neetjee">🎨 Arts / Humanities</span>
          <ul id="arts_tree">
            <li><span class="node-box" id="psych" onclick="selectNode('psych', 'arts')" data-tags="no_math no_neetjee abroad">🧠 Clinical Psychology</span></li>
            <li>
                <span class="node-box" id="ux" onclick="selectNode('ux', 'arts')" data-tags="high_salary no_math no_neetjee abroad">📱 UX/UI Design</span>
                <ul><li><span class="node-box exam-node" id="uceed" onclick="selectNode('uceed', 'ux')">📝 Exam: UCEED / NID</span></li></ul>
            </li>
            <li><span class="node-box" id="law" onclick="selectNode('law', 'arts')" data-tags="high_salary no_math no_neetjee">⚖️ Corporate Law (BA LLB)</span></li>
            <li><span class="node-box" id="masscomm" onclick="selectNode('masscomm', 'arts')" data-tags="no_math no_neetjee">🎥 Journalism & Mass Comm</span></li>
            <li><span class="node-box" id="fashion" onclick="selectNode('fashion', 'arts')" data-tags="no_math no_neetjee abroad">👗 Fashion Design (NIFT)</span></li>
            <li><span class="node-box" id="anim" onclick="selectNode('anim', 'arts')" data-tags="high_salary no_math no_neetjee abroad">🎮 Animation & VFX</span></li>
            <li><span class="node-box" id="policy" onclick="selectNode('policy', 'arts')" data-tags="no_math no_neetjee low_comp">🏛️ Public Policy / IR</span></li>
          </ul>
        </li>

        <li>
          <span class="node-box" id="def" onclick="selectNode('def', 'root')" data-tags="low_comp no_neetjee">🎖️ Defense (NDA)</span>
          <ul id="def_tree">
            <li><span class="node-box" id="army" onclick="selectNode('army', 'def')" data-tags="low_comp no_neetjee no_math">🪖 Indian Army</span></li>
            <li><span class="node-box" id="navy" onclick="selectNode('navy', 'def')" data-tags="low_comp no_neetjee">⚓ Indian Navy (Needs PCM)</span></li>
            <li><span class="node-box" id="airforce" onclick="selectNode('airforce', 'def')" data-tags="low_comp no_neetjee">✈️ Air Force (Needs PCM)</span></li>
          </ul>
        </li>

      </ul>
    </li>
  </ul>
</div>

<div id="info-box" class="info-panel">
  <div class="panel-header">
      <h3 id="panel-title" class="panel-title">Title</h3>
      <button onclick="closeInfo()" style="background:none; border:none; font-size:1.8rem; cursor:pointer; color:#94a3b8; line-height:1; padding:0;">&times;</button>
  </div>
  
  <div id="parentModeWarning" class="parent-warning">
      👨‍👩‍👧 PARENT MODE ON: Showing stability, safety, and long-term security metrics.
  </div>

  <div class="meter-box" id="panel-meters">
      <div class="meter-row"><span>Difficulty to Enter:</span> <span id="meter-diff" class="stars">★★★☆☆</span></div>
      <div class="meter-row"><span>Income Potential:</span> <span id="meter-inc" class="stars">★★★★★</span></div>
      <div class="meter-row"><span>Future Growth (AI Risk):</span> <span id="meter-gro" class="stars">★★★★☆</span></div>
      <div class="meter-row"><span>Job Stress Level:</span> <span id="meter-str" class="stars">★★★★☆</span></div>
      
      <div style="margin-top: 18px; padding-top: 15px; border-top: 1px dashed #cbd5e1;">
          <div class="meter-row" style="margin-bottom:5px; color:#0f172a;">Expected Salary Trajectory</div>
          <div class="salary-bar-wrap">
              <div class="salary-fresher"></div>
              <div class="salary-mid"></div>
              <div class="salary-top"></div>
          </div>
          <div class="salary-labels">
              <span>Fresher (₹4L)</span>
              <span>Mid (₹12L)</span>
              <span>Peak (₹30L+)</span>
          </div>
      </div>
  </div>

  <div class="avoid-box" id="panel-avoid">
      <h4>❌ Who Should Avoid This:</h4>
      <ul id="avoid-list">
          <li>Loading...</li>
      </ul>
  </div>

  <p id="panel-desc" class="desc-text">Description goes here.</p>
  
  <button class="btn-outline">🔄 Compare with another Career</button>
  <a href="{{ '/book-expert/' | relative_url }}" class="action-btn">📅 Book Clarity Session</a>
</div>

<div class="smart-popup" id="smartPopup">
    <button onclick="document.getElementById('smartPopup').style.display='none'" style="float:right; background:none; border:none; color:white; cursor:pointer; font-size:1.2rem;">&times;</button>
    <h4 style="margin: 0 0 10px 0; color:#f59e0b; font-size:1.1rem;">Still Confused? 🤔</h4>
    <p style="font-size:0.9rem; margin-bottom:15px; color:#cbd5e1; line-height: 1.5;">You've explored a few options. Want to know exactly which one matches your personality and true aptitude?</p>
    <a href="{{ '/assessment/' | relative_url }}" style="color:#0f172a; background:#f59e0b; padding:10px 15px; border-radius:8px; text-decoration:none; font-size:0.9rem; font-weight:900; display:block; text-align:center;">Take Stream Assessment ➔</a>
</div>

<script>
  let clickCount = 0;
  let isParentMode = false;

  // --- COMPREHENSIVE CAREER DATABASE ---
  const data = {
    "root": { 
        title: "Class 10 Pass", 
        desc: "The foundation block. Don't stress — your 10th marks do not dictate your life, but your next stream choice does.",
        p_desc: "This is the most critical junction for your child. A wrong stream here leads to expensive course corrections later. Let's look at stable options.",
        diff: 1, inc: 0, gro: 0, str: 1,
        avoid: ["N/A - Everyone has to pass 10th!"]
    },
    
    // --- SCIENCE TRACK ---
    "sci": { 
        title: "Science Stream", 
        desc: "The most flexible stream. You can switch to Commerce or Arts later, but it requires high dedication and study hours.",
        p_desc: "The safest traditional route. Keeps all competitive exams (UPSC, Banking, MBA) open for your child in the future.",
        diff: 5, inc: 4, gro: 5, str: 5,
        avoid: ["If you struggle heavily with conceptual Math and Physics.", "If you are only taking it due to peer/parental pressure."]
    },
    "mbbs": { 
        title: "MBBS (Doctor)", 
        desc: "Highly respected. Involves 5.5 years of intense study followed by specialized residencies and long working hours.",
        p_desc: "Ultimate job security and social respect. However, be prepared for a long financial gestation period (10+ years before high earning).",
        diff: 5, inc: 5, gro: 5, str: 5,
        avoid: ["If you cannot handle blood, trauma, or high-stress emergencies.", "If you want to start earning a high salary by age 22.", "If you hate continuous, lifelong studying."]
    },
    "neet": {
        title: "NEET UG Exam",
        desc: "The sole gateway to MBBS/BDS in India. Highly competitive (25 Lakh+ students fight for ~1 Lakh seats). Requires intense coaching.",
        diff: 5, inc: 0, gro: 0, str: 5,
        avoid: ["If you suffer from extreme test anxiety.", "If you cannot commit to 10-12 hours of daily study for 2 years."]
    },
    "biotech": { 
        title: "Biotechnology", 
        desc: "The future of medicine, genetics, and agriculture. Massive scope abroad (USA/Germany/UK) for research and pharma roles.",
        diff: 4, inc: 4, gro: 5, str: 3,
        avoid: ["If you want a traditional desk job.", "If you don't plan to do a Master's degree (B.Sc alone pays very little)."]
    },
    "forensic": { 
        title: "Forensic Science", 
        desc: "Working with law enforcement to solve crimes using biology and chemistry. Fascinating but niche job market in India.",
        diff: 3, inc: 3, gro: 4, str: 4,
        avoid: ["If you are squeamish about crime scenes.", "If you expect a massive corporate salary."]
    },
    "marine": { 
        title: "Marine Biology", 
        desc: "Study of ocean ecosystems. Heavy fieldwork, traveling, and conservation efforts. Highly rewarding globally.",
        diff: 4, inc: 3, gro: 4, str: 2,
        avoid: ["If you get seasick.", "If you want to stay in a bustling city your whole life."]
    },
    "btech": { 
        title: "B.Tech (CSE / AI)", 
        desc: "The premier tech route. Software, Artificial Intelligence, and Machine Learning are paying record-breaking global salaries.",
        p_desc: "Excellent ROI if done from top Tier 1/2 colleges. Leads to highly stable, high-paying corporate jobs in global MNCs.",
        diff: 4, inc: 5, gro: 5, str: 4,
        avoid: ["If you dislike sitting in front of a screen for 8 hours.", "If you hate logic puzzles and coding."]
    },
    "cyber": { 
        title: "Cyber Security", 
        desc: "Protecting companies and governments from hackers. One of the few tech jobs completely immune to AI replacement.",
        diff: 4, inc: 5, gro: 5, str: 4,
        avoid: ["If you lack extreme attention to detail.", "If you want a highly creative/artistic job."]
    },
    "space": { 
        title: "Space Tech (ISRO)", 
        desc: "Aerospace engineering and astrophysics. Highly prestigious government and private space roles.",
        p_desc: "A highly secure central government job (ISRO) with immense prestige and unbeatable lifelong perks.",
        diff: 5, inc: 3, gro: 5, str: 3,
        avoid: ["If your primary goal is making massive amounts of money quickly."]
    },
    "aviation": { 
        title: "Commercial Pilot", 
        desc: "Flying commercial airlines globally. Highly glamorous, massive salary, but very expensive initial training.",
        diff: 3, inc: 5, gro: 4, str: 4,
        avoid: ["If you cannot pass strict medical and vision tests.", "If you have a fear of flying or heights."]
    },

    // --- COMMERCE TRACK ---
    "comm": { 
        title: "Commerce Stream", 
        desc: "The language of global business. Perfect for future entrepreneurs, bankers, accountants, and market analysts.",
        diff: 3, inc: 5, gro: 4, str: 3,
        avoid: ["If you hate working with numbers, balance sheets, or corporate environments."]
    },
    "ca": { 
        title: "Chartered Accountant", 
        desc: "The backbone of the economy. Extremely tough exams (low pass rate), but almost zero unemployment once cleared.",
        p_desc: "One of the highest ROI degrees in India. Low cost of education with a guaranteed upper-middle-class lifestyle and absolute job security.",
        diff: 5, inc: 5, gro: 4, str: 5,
        avoid: ["If you cannot handle repeated exam failures.", "If you dislike auditing, taxation, and heavy rulebooks."]
    },
    "acca": { 
        title: "ACCA (Global CA)", 
        desc: "The UK equivalent of CA, recognized in 180+ countries. Faster to clear than Indian CA and highly prized by Big 4 firms.",
        diff: 4, inc: 5, gro: 4, str: 4,
        avoid: ["If you plan to set up your own individual tax practice strictly inside India (Indian CA is better for that)."]
    },
    "ib": { 
        title: "Investment Banking", 
        desc: "Helping corporations raise money and merge. The highest-paying jobs in the world, but famous for 80-hour work weeks.",
        diff: 5, inc: 5, gro: 4, str: 5,
        avoid: ["If you value work-life balance.", "If you cannot handle extreme, relentless pressure."]
    },
    "actuary": { 
        title: "Actuarial Science", 
        desc: "Predicting financial risk using heavy math for insurance companies. The highest paying commerce job you've never heard of.",
        diff: 5, inc: 5, gro: 5, str: 3,
        avoid: ["If you are not exceptionally gifted at advanced Statistics, Calculus, and Probability."]
    },
    "supply": { 
        title: "Supply Chain Mgmt", 
        desc: "Managing how goods get from factories to consumers (like Amazon logistics). A booming, low-competition industry.",
        diff: 3, inc: 4, gro: 5, str: 3,
        avoid: ["If you dislike operations, coordination, and handling logistical crises."]
    },
    "fintech": { 
        title: "FinTech & Analytics", 
        desc: "Where finance meets technology. Building payment gateways, crypto apps, and analyzing financial big data.",
        diff: 4, inc: 5, gro: 5, str: 3,
        avoid: ["If you refuse to learn basic coding/SQL alongside your finance degree."]
    },

    // --- ARTS/HUMANITIES TRACK ---
    "arts": { 
        title: "Arts / Humanities", 
        desc: "Focuses on human behavior, society, and creativity. Dominates the fields of design, public policy, media, and psychology.",
        p_desc: "An excellent, low-stress base for UPSC/IAS preparation or transitioning into highly paid new-age careers like UX Design.",
        diff: 2, inc: 3, gro: 4, str: 2,
        avoid: ["If you prefer strict formulas and definitive 'right/wrong' answers over abstract theory."]
    },
    "psych": { 
        title: "Clinical Psychology", 
        desc: "Treating mental health and behavior. Experiencing a massive boom in demand globally and in corporate India.",
        diff: 3, inc: 4, gro: 5, str: 4,
        avoid: ["If you easily absorb other people's trauma (lack emotional boundaries).", "If you are highly impatient."]
    },
    "ux": { 
        title: "UX/UI Design", 
        desc: "Designing how apps and websites look and feel. Tech-level salaries without needing to write a single line of code.",
        diff: 3, inc: 5, gro: 5, str: 2,
        avoid: ["If you lack empathy for user problems.", "If you have absolutely zero visual/aesthetic design sense."]
    },
    "law": { 
        title: "Corporate Law", 
        desc: "Working with massive firms on corporate mergers, contracts, and patents. Highly lucrative and prestigious.",
        p_desc: "High prestige and stability. Doing corporate law from top National Law Universities (NLUs) guarantees high Tier-1 placements.",
        diff: 4, inc: 5, gro: 4, str: 5,
        avoid: ["If you hate extensive reading, drafting documents, and high-pressure deadlines."]
    },
    "masscomm": { 
        title: "Journalism & Media", 
        desc: "News broadcasting, digital media, PR, and content creation. Fast-paced and highly visible.",
        diff: 2, inc: 3, gro: 4, str: 4,
        avoid: ["If you are highly introverted.", "If you want a 9-to-5 desk job (news never sleeps)."]
    },
    "anim": { 
        title: "Animation & VFX", 
        desc: "Creating visual effects for movies and gaming. A booming industry with massive remote-work potential.",
        diff: 3, inc: 4, gro: 5, str: 3,
        avoid: ["If you are unwilling to spend hours perfecting a single frame of video on a computer."]
    },

    // --- DEFENSE TRACK ---
    "def": { 
        title: "Defense (NDA)", 
        desc: "Joining the armed forces as an officer right after 12th grade. Unmatched pride, discipline, and national service.",
        p_desc: "The ultimate secure government career. Full medical coverage, lifetime pension, respect, and early financial independence.",
        diff: 5, inc: 3, gro: 3, str: 5,
        avoid: ["If you lack physical fitness or discipline.", "If you cannot follow strict hierarchies."]
    }
  };

  // --- UI LOGIC ---
  function getStars(num) {
      if(num === 0) return "N/A";
      return '★'.repeat(num) + '☆'.repeat(5-num);
  }

  function toggleParentMode() {
      isParentMode = !isParentMode;
      const btn = document.getElementById('parentModeBtn');
      if(isParentMode) {
          btn.classList.add('active');
          btn.innerText = "👨‍👩‍👧 Parent Mode: ON";
          document.getElementById('parentModeWarning').style.display = 'block';
      } else {
          btn.classList.remove('active');
          btn.innerText = "👨‍👩‍👧 Parent Mode: OFF";
          document.getElementById('parentModeWarning').style.display = 'none';
      }
      
      const activeNode = document.querySelector('.node-box.active');
      if(activeNode) selectNode(activeNode.id, null, true);
  }

  window.selectNode = function(id, parentId, skipScroll = false) {
    clickCount++;
    if(clickCount === 4) {
        setTimeout(() => document.getElementById('smartPopup').style.display = 'block', 1200);
    }

    document.querySelectorAll('.node-box').forEach(n => n.classList.remove('active'));
    
    const current = document.getElementById(id);
    if(current) current.classList.add('active');

    // Highlight path logic
    let pid = parentId;
    while(pid) {
      const pNode = document.getElementById(pid);
      if(pNode) {
        pNode.classList.add('active');
        const match = pNode.getAttribute('onclick').match(/'([^']*)'\)$/);
        pid = match && match[1] !== 'null' ? match[1] : null;
      } else {
        pid = null;
      }
    }

    const info = data[id] || { title: "Explore Path", desc: "Select a specific node to see details.", diff:0, inc:0, gro:0, str:0, avoid:[]};
    
    document.getElementById('panel-title').innerText = info.title;
    document.getElementById('panel-desc').innerText = (isParentMode && info.p_desc) ? info.p_desc : info.desc;
    
    // Update Meters
    document.getElementById('meter-diff').innerText = getStars(info.diff);
    document.getElementById('meter-inc').innerText = getStars(info.inc);
    document.getElementById('meter-gro').innerText = getStars(info.gro);
    document.getElementById('meter-str').innerText = getStars(info.str);

    // Update Avoid List
    const avoidUl = document.getElementById('avoid-list');
    avoidUl.innerHTML = "";
    if(info.avoid && info.avoid.length > 0) {
        info.avoid.forEach(item => {
            avoidUl.innerHTML += `<li>${item}</li>`;
        });
        document.getElementById('panel-avoid').style.display = 'block';
    } else {
        document.getElementById('panel-avoid').style.display = 'none';
    }

    document.getElementById('info-box').style.display = 'block';
  }

  window.closeInfo = function() {
    document.getElementById('info-box').style.display = 'none';
    document.querySelectorAll('.node-box').forEach(n => n.classList.remove('active'));
  }

  // --- FILTERING LOGIC ---
  window.applyFilter = function(filterType, btnElement) {
      document.querySelectorAll('.filter-btn').forEach(b => b.classList.remove('active'));
      btnElement.classList.add('active');
      closeInfo();

      const allNodes = document.querySelectorAll('.node-box');
      
      if(filterType === 'all') {
          allNodes.forEach(n => n.classList.remove('filtered-out'));
          return;
      }

      allNodes.forEach(node => {
          if(node.id === 'root') return; 
          const tags = node.getAttribute('data-tags') || "";
          
          if(tags.includes(filterType)) {
              node.classList.remove('filtered-out');
              let parentNode = node.closest('ul').previousElementSibling;
              while(parentNode && parentNode.classList.contains('node-box')) {
                  parentNode.classList.remove('filtered-out');
                  parentNode = parentNode.closest('ul').previousElementSibling;
              }
          } else {
              node.classList.add('filtered-out');
          }
      });
  }
</script>
