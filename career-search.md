---
layout: default
title: Complete Career Roadmap
permalink: /career-search/
---

<style>
  /* 1. FORCE FULL SCREEN (Override Default Layout) */
  .main-content {
    max-width: 100% !important;
    padding: 0 !important;
    margin: 0 !important;
  }
  
  body { overflow-x: hidden; }

  /* 2. MINDMAP CONTAINER */
  .mindmap-wrapper {
    display: flex;
    flex-direction: column;
    align-items: center;
    padding: 60px 40px;
    background: #f4f6f8;
    overflow-x: auto; /* Essential for wide trees */
    min-height: 100vh;
    width: 100%;
    box-sizing: border-box;
  }

  /* 3. NODE STYLING */
  .node {
    border: 2px solid #ccc;
    background: white;
    padding: 12px 15px;
    border-radius: 8px;
    cursor: pointer;
    font-size: 0.85rem;
    font-weight: bold;
    color: #0A2342;
    text-align: center;
    transition: all 0.3s;
    position: relative;
    min-width: 130px;
    max-width: 160px;
    margin: 0 15px;
    z-index: 2;
    box-shadow: 0 2px 5px rgba(0,0,0,0.05);
  }

  .node:hover {
    transform: scale(1.1);
    box-shadow: 0 5px 15px rgba(0,0,0,0.2);
    border-color: #D4AF37;
  }

  /* ACTIVE STATE (Light Up) */
  .node.active {
    border-color: #D4AF37;
    background: #0A2342;
    color: #D4AF37;
    box-shadow: 0 0 20px rgba(212, 175, 55, 0.6);
    transform: scale(1.1);
  }

  /* 4. TREE CONNECTORS (The Lines) */
  .level {
    display: flex;
    justify-content: center;
    padding-top: 50px;
    position: relative;
    width: max-content; /* Allows tree to expand horizontally */
  }

  /* Vertical Line coming down from parent */
  .level::before {
    content: '';
    position: absolute;
    top: 0;
    left: 50%;
    width: 2px;
    height: 25px;
    background: #ccc;
    z-index: 1;
  }
  
  .branch {
    display: flex;
    flex-direction: column;
    align-items: center;
    position: relative;
    padding: 25px 10px 0;
  }

  /* Connector Lines Logic */
  .branch::before {
    content: '';
    position: absolute;
    top: 0;
    left: 50%;
    width: 2px;
    height: 25px;
    background: #ccc;
  }

  .branch::after {
    content: '';
    position: absolute;
    top: 0;
    left: 0;
    width: 50%;
    height: 2px;
    background: #ccc;
  }
  
  /* Fix connectors for first/last children */
  .branch:first-child::after { left: 50%; width: 50%; }
  .branch:last-child::after { left: 0; width: 50%; }
  .branch:only-child::after { display: none; }
  .branch:not(:first-child):not(:last-child)::after { width: 100%; left: 0; }

  /* 5. INFO PANEL (Popup) */
  .info-panel {
    position: fixed;
    bottom: 30px;
    right: 30px;
    width: 320px;
    background: white;
    border-left: 6px solid #D4AF37;
    box-shadow: 0 10px 40px rgba(0,0,0,0.3);
    padding: 25px;
    border-radius: 12px;
    display: none;
    z-index: 1000;
    animation: slideIn 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275);
  }

  @keyframes slideIn {
    from { transform: translateX(120%); opacity: 0; }
    to { transform: translateX(0); opacity: 1; }
  }

  .info-title { font-size: 1.4rem; color: #0A2342; margin-top: 0; border-bottom: 2px solid #eee; padding-bottom: 10px; margin-bottom: 15px; }
  
  /* BACK BUTTON */
  .back-btn {
    position: fixed;
    top: 20px;
    left: 20px;
    background: rgba(10, 35, 66, 0.8);
    color: white;
    padding: 10px 20px;
    border-radius: 50px;
    text-decoration: none;
    font-weight: bold;
    backdrop-filter: blur(5px);
    z-index: 500;
  }
</style>

<a href="{{ '/' | relative_url }}" class="back-btn">← Home</a>

<div style="text-align: center; padding: 60px 20px; background: #0A2342; color: white;">
  <h1 style="font-size: 3rem; margin-bottom: 10px;">The Complete Roadmap</h1>
  <p style="font-size: 1.2rem; opacity: 0.8;">Click any career to trace your path from Class 10.</p>
</div>

<div class="mindmap-wrapper">
  
  <div class="node" id="root" onclick="selectNode('root', null)">Class 10th (Pass)</div>
  
  <div class="level" style="border-top: 2px solid #ccc; min-width: 80%;">
    
    <div class="branch">
      <div class="node" id="pcm" onclick="selectNode('pcm', 'root')">Science (PCM)</div>
      <div class="level">
        <div class="branch">
          <div class="node" id="btech" onclick="selectNode('btech', 'pcm')">B.Tech (Engineering)</div>
          <div class="level">
             <div class="branch"><div class="node" id="cse" onclick="selectNode('cse', 'btech')">Software/IT</div></div>
             <div class="branch"><div class="node" id="mech" onclick="selectNode('mech', 'btech')">Mechanical</div></div>
          </div>
        </div>
        <div class="branch">
          <div class="node" id="barch" onclick="selectNode('barch', 'pcm')">B.Arch</div>
          <div class="level">
             <div class="branch"><div class="node" id="architect" onclick="selectNode('architect', 'barch')">Architect</div></div>
          </div>
        </div>
        <div class="branch">
          <div class="node" id="aviation" onclick="selectNode('aviation', 'pcm')">Aviation / Defense</div>
          <div class="level">
             <div class="branch"><div class="node" id="pilot" onclick="selectNode('pilot', 'aviation')">Commercial Pilot</div></div>
             <div class="branch"><div class="node" id="navy" onclick="selectNode('navy', 'aviation')">Merchant Navy</div></div>
             <div class="branch"><div class="node" id="nda" onclick="selectNode('nda', 'aviation')">Defense (NDA)</div></div>
          </div>
        </div>
      </div>
    </div>

    <div class="branch">
      <div class="node" id="pcb" onclick="selectNode('pcb', 'root')">Science (PCB)</div>
      <div class="level">
        <div class="branch">
          <div class="node" id="mbbs" onclick="selectNode('mbbs', 'pcb')">MBBS / BDS</div>
          <div class="level">
            <div class="branch"><div class="node" id="doctor" onclick="selectNode('doctor', 'mbbs')">Doctor (MD)</div></div>
            <div class="branch"><div class="node" id="dentist" onclick="selectNode('dentist', 'mbbs')">Dentist</div></div>
          </div>
        </div>
        <div class="branch">
          <div class="node" id="ayush" onclick="selectNode('ayush', 'pcb')">AYUSH / Allied</div>
          <div class="level">
            <div class="branch"><div class="node" id="ayurveda" onclick="selectNode('ayurveda', 'ayush')">Ayurveda (BAMS)</div></div>
            <div class="branch"><div class="node" id="physio" onclick="selectNode('physio', 'ayush')">Physiotherapy</div></div>
          </div>
        </div>
        <div class="branch">
          <div class="node" id="bsc_bio" onclick="selectNode('bsc_bio', 'pcb')">B.Sc / Agri</div>
          <div class="level">
            <div class="branch"><div class="node" id="biotech" onclick="selectNode('biotech', 'bsc_bio')">Biotech/Research</div></div>
            <div class="branch"><div class="node" id="agriculture" onclick="selectNode('agriculture', 'bsc_bio')">Agriculture</div></div>
          </div>
        </div>
      </div>
    </div>

    <div class="branch">
      <div class="node" id="comm" onclick="selectNode('comm', 'root')">Commerce</div>
      <div class="level">
        <div class="branch">
          <div class="node" id="prof_courses" onclick="selectNode('prof_courses', 'comm')">Prof. Courses</div>
          <div class="level">
            <div class="branch"><div class="node" id="ca" onclick="selectNode('ca', 'prof_courses')">CA (Chartered Acc)</div></div>
            <div class="branch"><div class="node" id="cs" onclick="selectNode('cs', 'prof_courses')">CS (Company Sec)</div></div>
          </div>
        </div>
        <div class="branch">
          <div class="node" id="bcom" onclick="selectNode('bcom', 'comm')">B.Com / BBA</div>
          <div class="level">
            <div class="branch"><div class="node" id="mba" onclick="selectNode('mba', 'bcom')">MBA (Business)</div></div>
            <div class="branch"><div class="node" id="bank" onclick="selectNode('bank', 'bcom')">Banking/Finance</div></div>
          </div>
        </div>
      </div>
    </div>

    <div class="branch">
      <div class="node" id="arts" onclick="selectNode('arts', 'root')">Arts / Humanities</div>
      <div class="level">
        <div class="branch">
          <div class="node" id="ba" onclick="selectNode('ba', 'arts')">B.A (Pol/Hist)</div>
          <div class="level">
            <div class="branch"><div class="node" id="ias" onclick="selectNode('ias', 'ba')">UPSC (IAS/IPS)</div></div>
            <div class="branch"><div class="node" id="psych" onclick="selectNode('psych', 'ba')">Psychology</div></div>
          </div>
        </div>
        <div class="branch">
          <div class="node" id="creative" onclick="selectNode('creative', 'arts')">Creative / Law</div>
          <div class="level">
            <div class="branch"><div class="node" id="lawyer" onclick="selectNode('lawyer', 'creative')">Law (BA LLB)</div></div>
            <div class="branch"><div class="node" id="design" onclick="selectNode('design', 'creative')">Design (NIFT/NID)</div></div>
            <div class="branch"><div class="node" id="journ" onclick="selectNode('journ', 'creative')">Journalism</div></div>
          </div>
        </div>
      </div>
    </div>

  </div>
</div>

<div id="info-box" class="info-panel">
  <button onclick="closeInfo()" style="float:right; background:none; border:none; font-size:1.5rem; cursor:pointer; color:#999;">&times;</button>
  <h3 id="panel-title" class="info-title">Career Title</h3>
  
  <div style="margin-bottom:15px;">
    <p style="margin:5px 0; font-size:0.9rem;"><strong>⏱️ Duration:</strong> <span id="panel-time"></span></p>
    <p style="margin:5px 0; font-size:0.9rem;"><strong>📝 Key Exams:</strong> <span id="panel-exam" style="color:#D4AF37; font-weight:bold;"></span></p>
  </div>
  
  <p id="panel-desc" style="font-size:0.95rem; line-height:1.6; color:#555;">Description goes here.</p>
  
  <a href="{{ '/book-expert/' | relative_url }}" class="btn" style="background:#0A2342; color:white; padding:12px; font-size:0.9rem; text-decoration:none; display:block; text-align:center; margin-top:20px; border-radius:50px; font-weight:bold;">Talk to an Expert</a>
</div>

<script>
  // --- COMPLETE DATABASE ---
  const careerData = {
    "root": { title: "Class 10th", time: "1 Year", exam: "Board Exams", desc: "The first major milestone. Your stream selection here determines 80% of your future options." },
    
    // LEVEL 1: STREAMS
    "pcm": { title: "Science (PCM)", time: "2 Years", exam: "Min 75% for IITs", desc: "Physics, Chemistry, Maths. Required for Engineering, Architecture, Pilot, and Defense (Navy/Air Force)." },
    "pcb": { title: "Science (PCB)", time: "2 Years", exam: "Min 50% for NEET", desc: "Physics, Chemistry, Biology. Required for Medicine, Dentistry, Ayurveda, and Biotechnology." },
    "comm": { title: "Commerce", time: "2 Years", exam: "Min 60% for Top Colleges", desc: "Accounts, Business, Economics. The path for Finance, Banking, Management, and Corporate Law." },
    "arts": { title: "Arts / Humanities", time: "2 Years", exam: "Varies", desc: "History, Pol Sci, Sociology, Psych. The strongest foundation for UPSC (IAS), Law, and Design." },

    // LEVEL 2: DEGREES/GROUPS
    "btech": { title: "B.Tech / B.E", time: "4 Years", exam: "JEE Mains / Advanced", desc: "The most popular degree. Core engineering options include CS, Mechanical, Civil, and Electrical." },
    "barch": { title: "B.Arch", time: "5 Years", exam: "NATA / JEE Paper 2", desc: "Architecture & Design. Combines artistic skill with engineering physics." },
    "aviation": { title: "Aviation & Defense", time: "Varies", exam: "NDA / DGCA", desc: "Specialized training for Pilots, Merchant Navy officers, and Armed Forces." },
    
    "mbbs": { title: "MBBS / BDS", time: "5.5 Years", exam: "NEET UG", desc: "Bachelor of Medicine/Surgery or Dentistry. Requires intense dedication and hospital internships." },
    "ayush": { title: "AYUSH / Allied Health", time: "4-5 Years", exam: "NEET / CET", desc: "Alternative medicine (Ayurveda, Homeopathy) and Allied fields like Physiotherapy." },
    "bsc_bio": { title: "B.Sc Pure Science", time: "3-4 Years", exam: "CUET", desc: "Research-oriented degrees in Biology, Zoology, Botany, or Agriculture." },

    "prof_courses": { title: "Professional Certifications", time: "3-5 Years", exam: "ICAI / ICSI", desc: "Distance/Correspondence courses that you can do alongside B.Com. Very high value." },
    "bcom": { title: "B.Com / BBA", time: "3-4 Years", exam: "CUET / IPMAT", desc: "General graduation for business roles. BBA is better for management; B.Com for finance." },

    "ba": { title: "Bachelor of Arts", time: "3-4 Years", exam: "CUET", desc: "Degrees in History, Pol Sci, etc. Ideal for Civil Services preparation." },
    "creative": { title: "Creative & Legal", time: "3-5 Years", exam: "CLAT / NIFT", desc: "Specialized degrees for Law (5-Year Integrated) or Design/Fashion." },

    // LEVEL 3: CAREERS
    "cse": { title: "Software Engineer", time: "Job Ready", exam: "Coding Interviews", desc: "Build apps, AI, and websites. Highest starting salaries in the market." },
    "mech": { title: "Mechanical Engineer", time: "Job Ready", exam: "GATE (for PSU)", desc: "Design machines, cars, and robotics. Evergreen field." },
    "architect": { title: "Architect", time: "Professional License", exam: "COA Reg", desc: "Design sustainable buildings and smart cities." },
    "pilot": { title: "Commercial Pilot", time: "18-24 Months", exam: "DGCA CPL", desc: "Fly for airlines like Indigo/Air India. Expensive training (₹40L+) but high ROI." },
    "navy": { title: "Merchant Navy", time: "3-4 Years", exam: "IMU-CET", desc: "Work on cargo ships. Stay at sea for 6 months. Tax-free high salary." },
    "nda": { title: "Defense Officer", time: "3 Years Training", exam: "SSB Interview", desc: "Join Army/Navy/Air Force as an Officer. Ultimate prestige and job security." },

    "doctor": { title: "Doctor (MD/MS)", time: "+3 Years PG", exam: "NEET PG", desc: "Specialist doctor. Requires lifelong learning but offers immense respect." },
    "dentist": { title: "Dentist", time: "Practice Ready", exam: "NEET MDS", desc: "Open your own clinic or work in hospitals. Good work-life balance." },
    "ayurveda": { title: "Ayurvedic Doctor", time: "Practice Ready", exam: "AIAPGET", desc: "Growing field in holistic health and wellness tourism." },
    "physio": { title: "Physiotherapist", time: "4.5 Years", exam: "CET", desc: "Rehab expert for sports injuries and post-surgery recovery." },
    "biotech": { title: "Biotechnologist", time: "Masters/PhD", exam: "GATE / JAM", desc: "Work in pharma companies developing vaccines and medicines." },
    "agriculture": { title: "Agriculture Officer", time: "4 Years", exam: "ICAR AIEEA", desc: "Scientific farming, government research, and agro-business." },

    "ca": { title: "Chartered Accountant", time: "5 Years", exam: "CA Final", desc: "Expert in Audit and Tax. The highest authority in Indian finance." },
    "cs": { title: "Company Secretary", time: "3-4 Years", exam: "CS Professional", desc: "Corporate governance expert. Ensures companies follow legal rules." },
    "mba": { title: "MBA", time: "2 Years", exam: "CAT / GMAT", desc: "Master of Business Admin. Essential for CEO, Marketing Head, and HR roles." },
    "bank": { title: "Investment Banker", time: "High Stress", exam: "CFA / MBA", desc: "Manage mergers, acquisitions, and stock markets. Very high pay." },

    "ias": { title: "IAS / IPS", time: "Prep (1-3 Yrs)", exam: "UPSC CSE", desc: "Run the country's administration or police force. The toughest exam in India." },
    "psych": { title: "Psychologist", time: "MA + M.Phil", exam: "RCI License", desc: "Clinical therapy or corporate HR. Mental health is a booming sector." },
    "lawyer": { title: "Lawyer / Judge", time: "5 Years", exam: "CLAT", desc: "Corporate law (high money) or Litigation (court practice)." },
    "design": { title: "Fashion/Product Design", time: "4 Years", exam: "NIFT / NID", desc: "Design clothes, apps (UX), or cars. For the creatively gifted." },
    "journ": { title: "Journalist / Mass Comm", time: "3 Years", exam: "Media Entrances", desc: "News anchoring, digital content, and PR management." }
  };

  // --- LOGIC ---
  function selectNode(id, parentId) {
    document.querySelectorAll('.node').forEach(n => n.classList.remove('active'));
    
    const current = document.getElementById(id);
    if(current) current.classList.add('active');

    // Trace Backwards
    let pid = parentId;
    while(pid) {
      const pNode = document.getElementById(pid);
      if(pNode) {
        pNode.classList.add('active');
        pid = pNode.getAttribute('onclick').match(/'([^']*)'\)$/)[1]; 
        if(pid === 'null') pid = null;
      } else {
        pid = null;
      }
    }

    // Show Info
    const data = careerData[id];
    if(data) {
      document.getElementById('panel-title').innerText = data.title;
      document.getElementById('panel-time').innerText = data.time;
      document.getElementById('panel-exam').innerText = data.exam;
      document.getElementById('panel-desc').innerText = data.desc;
      document.getElementById('info-box').style.display = 'block';
    }
  }

  function closeInfo() {
    document.getElementById('info-box').style.display = 'none';
  }
</script>
