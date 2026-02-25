---
layout: default
title: "The Ultimate Career Roadmap 🚀"
permalink: /career-search/
---

<style>
  .main-content { max-width: 100% !important; padding: 0 !important; margin: 0 !important; }
  body { background-color: #f8fafc; background-image: radial-gradient(#e2e8f0 1px, transparent 1px); background-size: 20px 20px; font-family: 'Inter', 'Segoe UI', sans-serif; overflow-x: hidden;}

  /* --- HEADER & FILTERS --- */
  .roadmap-header { text-align: center; padding: 80px 20px 40px; background: radial-gradient(circle at top right, #1e293b, #0f172a); color: white; border-bottom: 4px solid #3b82f6;}
  .roadmap-header h1 { margin:0; font-size: 3rem; font-weight: 900; letter-spacing: -1px;}
  .roadmap-header p { font-size: 1.2rem; color: #cbd5e1; margin-top: 10px; font-weight: 300;}

  .filter-container { background: white; padding: 15px 20px; box-shadow: 0 10px 25px rgba(0,0,0,0.05); position: sticky; top: 70px; z-index: 100; border-bottom: 1px solid #e2e8f0;}
  .filter-scroll { display: flex; gap: 10px; overflow-x: auto; padding-bottom: 5px; max-width: 1200px; margin: 0 auto; scrollbar-width: none;}
  .filter-scroll::-webkit-scrollbar { display: none; }
  
  .filter-btn { background: #f1f5f9; border: 1px solid #e2e8f0; color: #475569; padding: 8px 16px; border-radius: 50px; font-size: 0.9rem; font-weight: bold; cursor: pointer; white-space: nowrap; transition: 0.2s; display: flex; align-items: center; gap: 6px;}
  .filter-btn:hover { background: #e2e8f0; }
  .filter-btn.active { background: #3b82f6; color: white; border-color: #3b82f6; box-shadow: 0 4px 10px rgba(59, 130, 246, 0.3);}

  .parent-mode-toggle { background: #fef3c7; color: #d97706; border: 2px solid #f59e0b; padding: 8px 16px; border-radius: 50px; font-weight: 900; cursor: pointer; transition: 0.3s; display: flex; align-items: center; gap: 8px; margin-left: auto; white-space: nowrap;}
  .parent-mode-toggle.active { background: #d97706; color: white; }

  /* --- TREE CSS --- */
  .tree-wrapper { max-width: 1300px; margin: 0 auto; padding: 50px 20px 150px; overflow-x: auto; min-height: 70vh;}
  ul.tree, ul.tree ul { list-style: none; margin: 0; padding: 0; }
  ul.tree ul { margin-left: 45px; position: relative; }
  ul.tree ul:before { content: ""; display: block; width: 0; position: absolute; top: 0; bottom: 0; left: 0; border-left: 3px solid #cbd5e1; }
  ul.tree li { margin: 0; padding: 0 25px; line-height: 4em; position: relative; }
  ul.tree ul li:before { content: ""; display: block; width: 25px; height: 0; border-top: 3px solid #cbd5e1; position: absolute; top: 2em; left: 0; }
  ul.tree ul li:last-child:before { background: #f8fafc; height: auto; top: 2em; bottom: 0; }

  /* --- NODE CARDS --- */
  .node-box { display: inline-flex; align-items: center; padding: 12px 20px; border: none; background: white; border-radius: 12px; font-weight: 700; color: #1e293b; cursor: pointer; transition: all 0.2s cubic-bezier(0.25, 0.8, 0.25, 1); font-size: 0.95rem; position: relative; z-index: 2; box-shadow: 0 4px 6px rgba(0,0,0,0.05), 0 1px 3px rgba(0,0,0,0.05); min-width: 180px; }
  .node-box:hover { transform: translateY(-3px) scale(1.02); box-shadow: 0 10px 20px rgba(0,0,0,0.08); }
  .node-box.active { background: linear-gradient(135deg, #1e293b 0%, #0f172a 100%); color: white; box-shadow: 0 0 0 4px rgba(59, 130, 246, 0.3); border-color: transparent !important;}
  .node-box.filtered-out { opacity: 0.2; pointer-events: none; }

  /* Stream Colors */
  #sci, #sci ~ ul .node-box { border-left: 5px solid #3b82f6; }
  #comm, #comm ~ ul .node-box { border-left: 5px solid #f59e0b; }
  #arts, #arts ~ ul .node-box { border-left: 5px solid #8b5cf6; }
  .node-box.exam-node { background: #f1f5f9; font-size: 0.85rem; border-left: 5px solid #64748b !important; padding: 8px 15px;}
  .node-box.switch { background: #fffaf0; border: 2px dashed #f59e0b !important; border-left: none !important; color: #d97706; }

  /* --- PREMIUM INFO PANEL --- */
  .info-panel { position: fixed; bottom: 30px; right: 30px; width: 400px; background: white; border-top: 6px solid #3b82f6; box-shadow: 0 25px 50px -12px rgba(0,0,0,0.25); padding: 30px; border-radius: 20px; display: none; z-index: 1000; animation: slideIn 0.3s cubic-bezier(0.175, 0.885, 0.32, 1.275); max-height: 85vh; overflow-y: auto; box-sizing: border-box;}
  @keyframes slideIn { from { transform: translateY(100%); opacity: 0; } to { transform: translateY(0); opacity: 1; } }
  
  .panel-header { display: flex; justify-content: space-between; align-items: flex-start; margin-bottom: 20px;}
  .panel-title { margin: 0; font-size: 1.6rem; color: #0f172a; font-weight: 900; line-height: 1.2;}
  
  .meter-box { background: #f8fafc; padding: 15px; border-radius: 12px; margin-bottom: 20px; border: 1px solid #e2e8f0;}
  .meter-row { display: flex; justify-content: space-between; align-items: center; margin-bottom: 8px; font-size: 0.85rem; font-weight: bold;}
  .stars { color: #f59e0b; letter-spacing: 2px; font-size: 1rem;}
  
  .salary-bar-wrap { background: #e2e8f0; height: 10px; border-radius: 5px; margin-top: 5px; overflow: hidden; display: flex;}
  .salary-fresher { background: #93c5fd; height: 100%; width: 30%; }
  .salary-mid { background: #3b82f6; height: 100%; width: 40%; }
  .salary-top { background: #1e3a8a; height: 100%; width: 30%; }
  .salary-labels { display: flex; justify-content: space-between; font-size: 0.7rem; color: #64748b; margin-top: 5px; font-weight: bold;}

  .avoid-box { background: #fef2f2; border: 1px solid #fca5a5; padding: 15px; border-radius: 12px; margin-bottom: 20px;}
  .avoid-box h4 { margin: 0 0 10px 0; color: #dc2626; font-size: 0.9rem;}
  .avoid-box ul { margin: 0; padding-left: 20px; font-size: 0.85rem; color: #7f1d1d;}

  .desc-text { font-size: 0.95rem; color: #475569; line-height: 1.6; margin-bottom: 25px;}
  .parent-warning { display: none; background: #fffbeb; color: #b45309; padding: 10px; border-radius: 8px; font-size: 0.85rem; font-weight: bold; margin-bottom: 15px; border: 1px solid #fde68a;}

  .action-btn { background: #3b82f6; color: white; padding: 14px; text-align: center; border-radius: 12px; font-weight: 800; display: block; text-decoration: none; transition: 0.2s;}
  .action-btn:hover { background: #2563eb; transform: translateY(-2px); box-shadow: 0 10px 20px rgba(59,130,246,0.3);}

  /* Smart Popup */
  .smart-popup { position: fixed; bottom: 30px; left: 30px; background: #0f172a; color: white; padding: 20px 25px; border-radius: 16px; box-shadow: 0 20px 40px rgba(0,0,0,0.3); z-index: 2000; display: none; animation: popUp 0.5s cubic-bezier(0.175, 0.885, 0.32, 1.275); border-left: 5px solid #f59e0b; max-width: 300px;}
  @keyframes popUp { 0% { transform: scale(0.8); opacity: 0; } 100% { transform: scale(1); opacity: 1; } }

  .back-btn { position: absolute; top: 20px; left: 20px; color: white; text-decoration: none; font-weight: bold; background: rgba(255,255,255,0.1); padding: 8px 16px; border-radius: 50px; z-index: 10; }

  /* ==========================================
     MOBILE RESPONSIVE STYLES 
     ========================================== */
  @media (max-width: 768px) {
    .roadmap-header { padding: 90px 15px 30px; }
    .roadmap-header h1 { font-size: 2.2rem; }
    .roadmap-header p { font-size: 1rem; }
    
    .back-btn { top: 15px; left: 15px; padding: 6px 12px; font-size: 0.85rem; }

    /* Filter scroll area tweaks */
    .filter-btn { padding: 6px 12px; font-size: 0.85rem; }
    .parent-mode-toggle { padding: 6px 12px; font-size: 0.85rem; margin-left: 0; }

    /* Make tree nodes fit better on small screens */
    .tree-wrapper { padding: 30px 15px 150px; }
    .node-box { min-width: 140px; padding: 10px 15px; font-size: 0.85rem; }
    ul.tree li { padding: 0 15px; }
    ul.tree ul { margin-left: 30px; }

    /* Convert Info Panel to a Bottom Sheet for Mobile */
    .info-panel {
      width: 100%;
      bottom: 0;
      right: 0;
      left: 0;
      border-radius: 25px 25px 0 0;
      padding: 25px 20px;
      max-height: 85vh;
      border-top-width: 4px;
    }
    .panel-title { font-size: 1.4rem; }
    
    /* Center the Smart Popup on mobile */
    .smart-popup {
      width: 90%;
      left: 5%;
      bottom: 20px;
      max-width: none;
      box-sizing: border-box;
    }
  }
</style>

<div class="roadmap-header">
  <a href="{{ '/' | relative_url }}" class="back-btn">← Home</a>
  <h1>The Career GPS 🧭</h1>
  <p>Stop guessing. Use the filters below to find paths that match your criteria.</p>
</div>

<div class="filter-container">
    <div class="filter-scroll">
        <button class="filter-btn active" onclick="applyFilter('all', this)">All Careers</button>
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
      <span class="node-box" id="root" onclick="selectNode('root', null)" style="border-left: 5px solid #0f172a; background: #0f172a; color: white; font-size:1.1rem;">🎓 Class 10th Base</span>
      <ul>
        
        <li>
          <span class="node-box" id="sci" onclick="selectNode('sci', 'root')" data-tags="high_salary abroad">🧬 Science Stream</span>
          <ul id="sci_tree">
            <li>
              <span class="node-box" id="med_track" onclick="selectNode('med_track', 'sci')" data-tags="high_salary">Medical (PCB)</span>
              <ul>
                <li>
                  <span class="node-box" id="mbbs" onclick="selectNode('mbbs', 'med_track')" data-tags="high_salary no_math">MBBS (Doctor)</span>
                  <ul>
                      <li><span class="node-box exam-node" id="neet" onclick="selectNode('neet', 'mbbs')">📝 Exam: NEET UG</span></li>
                  </ul>
                </li>
                <li><span class="node-box" id="biotech" onclick="selectNode('biotech', 'med_track')" data-tags="abroad low_comp no_math no_neetjee">Biotechnology</span></li>
                <li><span class="node-box" id="forensic" onclick="selectNode('forensic', 'med_track')" data-tags="low_comp no_math no_neetjee">Forensic Science</span></li>
              </ul>
            </li>
            <li>
              <span class="node-box" id="eng_track" onclick="selectNode('eng_track', 'sci')" data-tags="high_salary abroad">Engineering (PCM)</span>
              <ul>
                <li>
                  <span class="node-box" id="btech" onclick="selectNode('btech', 'eng_track')" data-tags="high_salary abroad">B.Tech (CSE/AI)</span>
                  <ul>
                      <li><span class="node-box exam-node" id="jee" onclick="selectNode('jee', 'btech')">📝 Exam: JEE Mains/Adv</span></li>
                      <li><span class="node-box exam-node" id="bits" onclick="selectNode('bits', 'btech')">📝 Exam: BITSAT</span></li>
                  </ul>
                </li>
                <li><span class="node-box" id="space" onclick="selectNode('space', 'eng_track')" data-tags="low_comp">Space Tech (ISRO)</span></li>
                <li><span class="node-box" id="env_sci" onclick="selectNode('env_sci', 'eng_track')" data-tags="abroad low_comp no_neetjee">Environmental Science</span></li>
              </ul>
            </li>
          </ul>
        </li>

        <li>
          <span class="node-box" id="comm" onclick="selectNode('comm', 'root')" data-tags="high_salary no_neetjee">📊 Commerce Stream</span>
          <ul id="comm_tree">
            <li>
              <span class="node-box" id="ca" onclick="selectNode('ca', 'comm')" data-tags="high_salary no_neetjee">Chartered Accountant (CA)</span>
            </li>
            <li><span class="node-box" id="ib" onclick="selectNode('ib', 'comm')" data-tags="high_salary abroad">Investment Banking</span></li>
            <li><span class="node-box" id="actuary" onclick="selectNode('actuary', 'comm')" data-tags="high_salary low_comp abroad">Actuarial Science</span></li>
            <li><span class="node-box" id="fintech" onclick="selectNode('fintech', 'comm')" data-tags="high_salary abroad no_neetjee">FinTech & Analytics</span></li>
          </ul>
        </li>

        <li>
          <span class="node-box" id="arts" onclick="selectNode('arts', 'root')" data-tags="no_math no_neetjee">🎨 Arts / Humanities</span>
          <ul id="arts_tree">
            <li><span class="node-box" id="psych" onclick="selectNode('psych', 'arts')" data-tags="no_math no_neetjee abroad">Clinical Psychology</span></li>
            <li>
                <span class="node-box" id="ux" onclick="selectNode('ux', 'arts')" data-tags="high_salary no_math no_neetjee abroad">UX/UI Design</span>
                <ul>
                    <li><span class="node-box exam-node" id="uceed" onclick="selectNode('uceed', 'ux')">📝 Exam: UCEED / NID</span></li>
                </ul>
            </li>
            <li><span class="node-box" id="policy" onclick="selectNode('policy', 'arts')" data-tags="no_math no_neetjee low_comp">Public Policy / IR</span></li>
            <li>
                <span class="node-box" id="law" onclick="selectNode('law', 'arts')" data-tags="high_salary no_math no_neetjee">Corporate Law (BA LLB)</span>
                <ul>
                    <li><span class="node-box exam-node" id="clat" onclick="selectNode('clat', 'law')">📝 Exam: CLAT / AILET</span></li>
                </ul>
            </li>
          </ul>
        </li>

      </ul>
    </li>
  </ul>
</div>

<div id="info-box" class="info-panel">
  <div class="panel-header">
      <h3 id="panel-title" class="panel-title">Title</h3>
      <button onclick="closeInfo()" style="background:none; border:none; font-size:1.8rem; cursor:pointer; color:#94a3b8; line-height:1;">&times;</button>
  </div>
  
  <div id="parentModeWarning" class="parent-warning">
      👨‍👩‍👧 PARENT MODE ON: Showing stability and long-term security metrics.
  </div>

  <div class="meter-box" id="panel-meters">
      <div class="meter-row"><span>Difficulty:</span> <span id="meter-diff" class="stars">★★★☆☆</span></div>
      <div class="meter-row"><span>Income Potential:</span> <span id="meter-inc" class="stars">★★★★★</span></div>
      <div class="meter-row"><span>Future Growth:</span> <span id="meter-gro" class="stars">★★★★☆</span></div>
      <div class="meter-row"><span>Stress Level:</span> <span id="meter-str" class="stars">★★★★☆</span></div>
      
      <div style="margin-top: 15px;">
          <div class="meter-row" style="margin-bottom:0; color:#0f172a;">Expected Salary Trajectory</div>
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
          <li>People who hate math.</li>
          <li>Students seeking quick money.</li>
      </ul>
  </div>

  <p id="panel-desc" class="desc-text">Description goes here.</p>
  
  <button class="btn-outline" style="width:100%; padding:10px; border-radius:8px; margin-bottom:15px; cursor:pointer; font-weight:bold; border: 2px solid #e2e8f0; color:#475569;">🔄 Compare with another Career</button>
  
  <a href="{{ '/book-expert/' | relative_url }}" class="action-btn">📅 Book Clarity Session</a>
</div>

<div class="smart-popup" id="smartPopup">
    <button onclick="document.getElementById('smartPopup').style.display='none'" style="float:right; background:none; border:none; color:white; cursor:pointer;">&times;</button>
    <h4 style="margin: 0 0 10px 0; color:#f59e0b;">Still Confused?</h4>
    <p style="font-size:0.85rem; margin-bottom:15px; color:#cbd5e1;">You've explored a few options. Want to know exactly which one matches your personality and aptitude?</p>
    <a href="{{ '/assessment/' | relative_url }}" style="color:white; background:#3b82f6; padding:8px 12px; border-radius:6px; text-decoration:none; font-size:0.85rem; font-weight:bold; display:block; text-align:center;">Take Stream Assessment</a>
</div>

<script>
  let clickCount = 0;
  let isParentMode = false;

  // --- DATABASE ---
  const data = {
    "root": { 
        title: "Class 10 Pass", 
        desc: "The foundation. Don't stress — your 10th marks don't decide your life, but your next decision does.",
        p_desc: "This is the most critical junction for your child. A wrong stream here leads to expensive course corrections later. Let's look at stable options.",
        diff: 1, inc: 0, gro: 0, str: 2,
        avoid: ["N/A - Everyone has to pass 10th!"]
    },
    
    // SCIENCE
    "sci": { 
        title: "Science Stream", 
        desc: "The most flexible stream. You can switch to Commerce or Arts later, but it requires high dedication.",
        p_desc: "The safest traditional route. Keeps all competitive exams (UPSC, Banking, MBA) open for your child in the future.",
        diff: 5, inc: 4, gro: 5, str: 5,
        avoid: ["If you struggle heavily with conceptual Math.", "If you are only taking it due to peer pressure."]
    },
    "mbbs": { 
        title: "MBBS (Doctor)", 
        desc: "Highly respected. Involves 5.5 years of intense study followed by specialized residencies.",
        p_desc: "Ultimate job security and social respect. However, be prepared for a long financial gestation period (10+ years before high earning).",
        diff: 5, inc: 5, gro: 5, str: 5,
        avoid: ["If you cannot handle blood or trauma.", "If you want to start earning by age 22.", "If you hate continuous, lifelong studying."]
    },
    "neet": {
        title: "NEET UG Exam",
        desc: "The sole gateway to MBBS/BDS in India. Highly competitive (25 Lakh+ students for ~1 Lakh seats).",
        diff: 5, inc: 0, gro: 0, str: 5,
        avoid: ["If you cannot handle extreme exam anxiety."]
    },
    "biotech": { 
        title: "Biotechnology", 
        desc: "The future of medicine and agriculture. Massive scope abroad (USA/Germany).",
        diff: 4, inc: 4, gro: 5, str: 3,
        avoid: ["If you want a traditional desk job.", "If you don't plan to do a Master's degree."]
    },
    "btech": { 
        title: "B.Tech (CSE / AI)", 
        desc: "The tech route. Software, AI, and Machine Learning are paying record salaries.",
        p_desc: "Excellent ROI if done from top Tier 1/2 colleges. Leads to stable corporate jobs in MNCs.",
        diff: 4, inc: 5, gro: 5, str: 4,
        avoid: ["If you dislike sitting in front of a screen.", "If you hate logic puzzles and coding."]
    },
    "space": { 
        title: "Space Tech (ISRO)", 
        desc: "Aerospace engineering and astrophysics. Highly prestigious government roles.",
        p_desc: "A highly secure central government job with immense prestige and unbeatable perks.",
        diff: 5, inc: 3, gro: 5, str: 3,
        avoid: ["If your primary goal is making massive amounts of money."]
    },

    // COMMERCE
    "comm": { 
        title: "Commerce Stream", 
        desc: "The language of business. Perfect for future entrepreneurs, bankers, and analysts.",
        diff: 3, inc: 5, gro: 4, str: 3,
        avoid: ["If you hate numbers, balance sheets, or corporate environments."]
    },
    "ca": { 
        title: "Chartered Accountant", 
        desc: "The backbone of the economy. Tough exams, but almost zero unemployment.",
        p_desc: "One of the highest ROI degrees in India. Low cost of education with a guaranteed upper-middle-class lifestyle.",
        diff: 5, inc: 5, gro: 4, str: 5,
        avoid: ["If you cannot handle repeated exam failures (low pass %)", "If you dislike auditing and taxation laws."]
    },
    "actuary": { 
        title: "Actuarial Science", 
        desc: "Predicting financial risk using math. Highest paying commerce job you've never heard of.",
        diff: 5, inc: 5, gro: 5, str: 3,
        avoid: ["If you are not exceptionally gifted at advanced Statistics and Probability."]
    },

    // ARTS
    "arts": { 
        title: "Arts / Humanities", 
        desc: "Focuses on human behavior, society, and creativity. Dominates design, policy, and psychology.",
        p_desc: "Excellent base for UPSC/IAS preparation or specialized new-age careers like UX Design.",
        diff: 2, inc: 3, gro: 4, str: 2,
        avoid: ["If you prefer formulas and definitive 'right/wrong' answers over theory."]
    },
    "psych": { 
        title: "Clinical Psychology", 
        desc: "Treating mental health. Massive boom in demand globally and in corporate India.",
        diff: 3, inc: 4, gro: 5, str: 4,
        avoid: ["If you absorb other people's trauma easily (lack emotional boundaries)."]
    },
    "ux": { 
        title: "UX/UI Design", 
        desc: "Designing apps and websites. Tech-level salaries without needing to write code.",
        diff: 3, inc: 5, gro: 5, str: 2,
        avoid: ["If you lack empathy for user problems or have zero visual design sense."]
    },
    "law": { 
        title: "Corporate Law", 
        desc: "Working with massive firms on mergers and patents. Highly lucrative.",
        p_desc: "High prestige. Corporate law from top NLUs guarantees placements in Tier-1 firms.",
        diff: 4, inc: 5, gro: 4, str: 5,
        avoid: ["If you hate extensive reading, drafting, and high-pressure deadlines."]
    }
  };

  // --- LOGIC ---
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
      // Re-render current panel if open
      const activeNode = document.querySelector('.node-box.active');
      if(activeNode) selectNode(activeNode.id, null, true);
  }

  window.selectNode = function(id, parentId, skipScroll = false) {
    clickCount++;
    if(clickCount === 4) {
        setTimeout(() => document.getElementById('smartPopup').style.display = 'block', 1000);
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
      // UI Update
      document.querySelectorAll('.filter-btn').forEach(b => b.classList.remove('active'));
      btnElement.classList.add('active');
      closeInfo();

      // Node Filtering
      const allNodes = document.querySelectorAll('.node-box');
      
      if(filterType === 'all') {
          allNodes.forEach(n => n.classList.remove('filtered-out'));
          return;
      }

      allNodes.forEach(node => {
          if(node.id === 'root') return; // Keep root visible
          const tags = node.getAttribute('data-tags') || "";
          
          if(tags.includes(filterType)) {
              node.classList.remove('filtered-out');
              // Ensure parents are visible
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
