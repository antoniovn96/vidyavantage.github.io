---
layout: default
title: Complete Career Roadmap
permalink: /career-search/
---

<style>
  /* 1. LAYOUT RESET */
  .main-content {
    max-width: 100% !important;
    padding: 0 !important;
    margin: 0 !important;
  }
  
  body { background-color: #f4f6f8; }

  /* 2. VERTICAL TREE CONTAINER */
  .tree-wrapper {
    max-width: 900px;
    margin: 0 auto;
    padding: 60px 20px;
    font-family: 'Open Sans', sans-serif;
  }

  /* 3. TREE CSS (The Magic Part) */
  ul.tree, ul.tree ul {
    list-style: none;
    margin: 0;
    padding: 0;
  }

  ul.tree ul {
    margin-left: 30px; /* Indent children */
    position: relative;
  }

  /* The Vertical Line (Left Border) */
  ul.tree ul:before {
    content: "";
    display: block;
    width: 0;
    position: absolute;
    top: 0;
    bottom: 0;
    left: 0;
    border-left: 2px solid #ccc;
  }

  ul.tree li {
    margin: 0;
    padding: 0 15px; /* Space for the horizontal connector */
    line-height: 2.5em; /* Spacing between rows */
    position: relative;
  }

  /* The Horizontal Connector Line */
  ul.tree ul li:before {
    content: "";
    display: block;
    width: 25px; /* Length of connector */
    height: 0;
    border-top: 2px solid #ccc;
    position: absolute;
    top: 1.25em; /* Middle of the line height */
    left: 0;
  }

  /* Remove vertical line for last child to prevent overhang */
  ul.tree ul li:last-child:before {
    background: #f4f6f8; /* Hide overlap */
    height: auto;
    top: 1.25em;
    bottom: 0;
  }

  /* 4. NODE STYLING (The Boxes) */
  .node-box {
    display: inline-block;
    padding: 8px 15px;
    border: 2px solid #ccc;
    background: white;
    border-radius: 50px;
    font-weight: bold;
    color: #0A2342;
    cursor: pointer;
    transition: all 0.2s;
    font-size: 0.95rem;
    position: relative;
    z-index: 2;
  }

  .node-box:hover {
    transform: translateX(5px);
    border-color: #D4AF37;
    box-shadow: 0 4px 10px rgba(0,0,0,0.1);
  }

  /* ACTIVE STATE (Gold Highlight) */
  .node-box.active {
    background: #0A2342;
    color: #D4AF37;
    border-color: #D4AF37;
    box-shadow: 0 0 15px rgba(212, 175, 55, 0.5);
  }

  /* Highlight Lines (Advanced CSS trick) */
  .highlight-line {
    border-color: #D4AF37 !important;
  }

  /* 5. INFO PANEL (Popup) */
  .info-panel {
    position: fixed;
    bottom: 20px;
    right: 20px;
    width: 300px;
    background: white;
    border-left: 5px solid #D4AF37;
    box-shadow: 0 10px 30px rgba(0,0,0,0.2);
    padding: 20px;
    border-radius: 8px;
    display: none;
    z-index: 1000;
    animation: slideUp 0.3s ease-out;
  }

  @keyframes slideUp {
    from { transform: translateY(100%); opacity: 0; }
    to { transform: translateY(0); opacity: 1; }
  }

  .back-btn {
    position: fixed;
    top: 20px;
    left: 20px;
    background: #0A2342;
    color: white;
    padding: 8px 20px;
    border-radius: 20px;
    text-decoration: none;
    font-weight: bold;
    z-index: 500;
  }
</style>

<a href="{{ '/' | relative_url }}" class="back-btn">← Home</a>

<div style="text-align: center; padding: 80px 20px 40px; background: #0A2342; color: white;">
  <h1 style="margin:0;">Interactive Career Tree</h1>
  <p style="opacity:0.8;">Click any career to trace your path from Class 10.</p>
</div>

<div class="tree-wrapper">
  <ul class="tree">
    
    <li>
      <span class="node-box" id="root" onclick="selectNode('root', null)">Class 10th (Pass)</span>
      
      <ul>
        <li>
          <span class="node-box" id="pcm" onclick="selectNode('pcm', 'root')">Science (PCM)</span>
          <ul>
            <li>
              <span class="node-box" id="btech" onclick="selectNode('btech', 'pcm')">B.Tech (Engineering)</span>
              <ul>
                <li><span class="node-box" id="cse" onclick="selectNode('cse', 'btech')">Software/IT Engineer</span></li>
                <li><span class="node-box" id="mech" onclick="selectNode('mech', 'btech')">Mechanical Engineer</span></li>
                <li><span class="node-box" id="civil" onclick="selectNode('civil', 'btech')">Civil Engineer</span></li>
              </ul>
            </li>
            <li>
              <span class="node-box" id="barch" onclick="selectNode('barch', 'pcm')">Architecture (B.Arch)</span>
              <ul>
                <li><span class="node-box" id="architect" onclick="selectNode('architect', 'barch')">Licensed Architect</span></li>
              </ul>
            </li>
            <li>
              <span class="node-box" id="aviation" onclick="selectNode('aviation', 'pcm')">Aviation / Defense</span>
              <ul>
                <li><span class="node-box" id="pilot" onclick="selectNode('pilot', 'aviation')">Commercial Pilot</span></li>
                <li><span class="node-box" id="navy" onclick="selectNode('navy', 'aviation')">Merchant Navy</span></li>
                <li><span class="node-box" id="nda" onclick="selectNode('nda', 'aviation')">Defense Officer (NDA)</span></li>
              </ul>
            </li>
          </ul>
        </li>

        <li>
          <span class="node-box" id="pcb" onclick="selectNode('pcb', 'root')">Science (PCB)</span>
          <ul>
            <li>
              <span class="node-box" id="mbbs" onclick="selectNode('mbbs', 'pcb')">MBBS / BDS</span>
              <ul>
                <li><span class="node-box" id="doctor" onclick="selectNode('doctor', 'mbbs')">Doctor (MD/MS)</span></li>
                <li><span class="node-box" id="dentist" onclick="selectNode('dentist', 'mbbs')">Dentist</span></li>
              </ul>
            </li>
            <li>
              <span class="node-box" id="allied" onclick="selectNode('allied', 'pcb')">Allied Health</span>
              <ul>
                <li><span class="node-box" id="ayurveda" onclick="selectNode('ayurveda', 'allied')">Ayurveda (BAMS)</span></li>
                <li><span class="node-box" id="physio" onclick="selectNode('physio', 'allied')">Physiotherapy</span></li>
                <li><span class="node-box" id="pharma" onclick="selectNode('pharma', 'allied')">Pharmacy (B.Pharm)</span></li>
              </ul>
            </li>
            <li>
              <span class="node-box" id="bsc_bio" onclick="selectNode('bsc_bio', 'pcb')">B.Sc Science</span>
              <ul>
                <li><span class="node-box" id="biotech" onclick="selectNode('biotech', 'bsc_bio')">Biotechnology</span></li>
                <li><span class="node-box" id="agri" onclick="selectNode('agri', 'bsc_bio')">B.Sc Agriculture</span></li>
                <li><span class="node-box" id="forensic" onclick="selectNode('forensic', 'bsc_bio')">Forensic Science</span></li>
              </ul>
            </li>
          </ul>
        </li>

        <li>
          <span class="node-box" id="comm" onclick="selectNode('comm', 'root')">Commerce</span>
          <ul>
            <li>
              <span class="node-box" id="ca_track" onclick="selectNode('ca_track', 'comm')">Professional Certs</span>
              <ul>
                <li><span class="node-box" id="ca" onclick="selectNode('ca', 'ca_track')">Chartered Accountant (CA)</span></li>
                <li><span class="node-box" id="cs" onclick="selectNode('cs', 'ca_track')">Company Secretary (CS)</span></li>
                <li><span class="node-box" id="cma" onclick="selectNode('cma', 'ca_track')">Cost Accountant (CMA)</span></li>
              </ul>
            </li>
            <li>
              <span class="node-box" id="bcom" onclick="selectNode('bcom', 'comm')">B.Com / BBA</span>
              <ul>
                <li><span class="node-box" id="mba" onclick="selectNode('mba', 'bcom')">MBA (Management)</span></li>
                <li><span class="node-box" id="bank" onclick="selectNode('bank', 'bcom')">Inv. Banker / CFA</span></li>
                <li><span class="node-box" id="digital" onclick="selectNode('digital', 'bcom')">Digital Marketing</span></li>
              </ul>
            </li>
          </ul>
        </li>

        <li>
          <span class="node-box" id="arts" onclick="selectNode('arts', 'root')">Arts / Humanities</span>
          <ul>
            <li>
              <span class="node-box" id="ba" onclick="selectNode('ba', 'arts')">B.A (Pol/Hist)</span>
              <ul>
                <li><span class="node-box" id="ias" onclick="selectNode('ias', 'ba')">UPSC (IAS/IPS)</span></li>
                <li><span class="node-box" id="prof" onclick="selectNode('prof', 'ba')">Professor / Teaching</span></li>
              </ul>
            </li>
            <li>
              <span class="node-box" id="law_track" onclick="selectNode('law_track', 'arts')">Legal & Creative</span>
              <ul>
                <li><span class="node-box" id="lawyer" onclick="selectNode('lawyer', 'law_track')">Lawyer (BA LLB)</span></li>
                <li><span class="node-box" id="psych" onclick="selectNode('psych', 'law_track')">Psychologist</span></li>
                <li><span class="node-box" id="design" onclick="selectNode('design', 'law_track')">Fashion/Interior Design</span></li>
                <li><span class="node-box" id="journ" onclick="selectNode('journ', 'law_track')">Journalism / Media</span></li>
              </ul>
            </li>
          </ul>
        </li>

      </ul>
    </li>
  </ul>
</div>

<div id="info-box" class="info-panel">
  <button onclick="closeInfo()" style="float:right; background:none; border:none; font-size:1.5rem; cursor:pointer; color:#999;">&times;</button>
  <h3 id="panel-title" style="color:#0A2342; margin-top:0;">Title</h3>
  <p><strong>⏱️ Duration:</strong> <span id="panel-time"></span></p>
  <p><strong>📝 Exams:</strong> <span id="panel-exam" style="color:#D4AF37; font-weight:bold;"></span></p>
  <hr style="border:0; border-top:1px solid #eee;">
  <p id="panel-desc" style="font-size:0.9rem; color:#555;">Desc</p>
  <a href="{{ '/book-expert/' | relative_url }}" class="btn" style="background:#0A2342; color:white; padding:10px; display:block; text-align:center; text-decoration:none; border-radius:5px; margin-top:15px;">Talk to Counsellor</a>
</div>

<script>
  // --- DATABASE ---
  const data = {
    // ROOT
    "root": { title: "Class 10 Pass", time: "1 Year", exam: "Boards", desc: "The foundation of your career." },
    
    // LEVEL 1
    "pcm": { title: "Science (PCM)", time: "2 Years", exam: "Boards", desc: "Physics, Chem, Math. Hardest stream." },
    "pcb": { title: "Science (PCB)", time: "2 Years", exam: "Boards", desc: "Physics, Chem, Biology. For medical." },
    "comm": { title: "Commerce", time: "2 Years", exam: "Boards", desc: "Business, Accounts. For finance/mgmt." },
    "arts": { title: "Arts / Humanities", time: "2 Years", exam: "Boards", desc: "History, Pol Sci. For UPSC/Law." },

    // LEVEL 2
    "btech": { title: "B.Tech (Engineering)", time: "4 Years", exam: "JEE Mains/Adv", desc: "Most popular degree in India." },
    "barch": { title: "B.Arch", time: "5 Years", exam: "NATA", desc: "Architecture & Design." },
    "aviation": { title: "Aviation/Defense", time: "Varies", exam: "NDA/DGCA", desc: "Pilot or Armed Forces." },
    
    "mbbs": { title: "MBBS", time: "5.5 Years", exam: "NEET", desc: "Bachelor of Medicine." },
    "allied": { title: "Allied Health", time: "3-4 Years", exam: "CET", desc: "Supportive healthcare roles." },
    "bsc_bio": { title: "B.Sc Pure Science", time: "3 Years", exam: "CUET", desc: "Research focused." },

    "ca_track": { title: "Professional Certs", time: "3-5 Years", exam: "ICAI/ICSI", desc: "Correspondence courses." },
    "bcom": { title: "B.Com / BBA", time: "3 Years", exam: "CUET", desc: "General business degrees." },

    "ba": { title: "Bachelor of Arts", time: "3 Years", exam: "CUET", desc: "Humanities degrees." },
    "law_track": { title: "Legal & Creative", time: "3-5 Years", exam: "CLAT/NIFT", desc: "Specialized fields." },

    // LEVEL 3 (CAREERS)
    "cse": { title: "Software Engineer", time: "Job Ready", exam: "Interviews", desc: "Coding, AI, App Dev." },
    "mech": { title: "Mechanical Engineer", time: "Job Ready", exam: "GATE", desc: "Machines & Robotics." },
    "civil": { title: "Civil Engineer", time: "Job Ready", exam: "GATE", desc: "Construction & Infrastructure." },
    "architect": { title: "Architect", time: "Licensed", exam: "COA", desc: "Building design." },
    "pilot": { title: "Commercial Pilot", time: "18 Months", exam: "CPL", desc: "Fly airlines. High cost, high pay." },
    "navy": { title: "Merchant Navy", time: "3 Years", exam: "IMU-CET", desc: "Work on cargo ships." },
    "nda": { title: "Defense Officer", time: "Training", exam: "SSB", desc: "Army/Navy/Air Force." },

    "doctor": { title: "Doctor", time: "MD/MS", exam: "NEET PG", desc: "Specialist medical practitioner." },
    "dentist": { title: "Dentist", time: "Practice", exam: "NEET MDS", desc: "Dental surgery." },
    "ayurveda": { title: "Ayurvedic Doctor", time: "Practice", exam: "AIAPGET", desc: "Holistic medicine." },
    "physio": { title: "Physiotherapist", time: "4.5 Years", exam: "CET", desc: "Physical rehabilitation." },
    "pharma": { title: "Pharmacist", time: "4 Years", exam: "CET", desc: "Medicine manufacturing." },
    "biotech": { title: "Biotechnologist", time: "Masters", exam: "GATE", desc: "Lab research & vaccines." },
    "agri": { title: "Agriculture Officer", time: "4 Years", exam: "ICAR", desc: "Scientific farming." },
    "forensic": { title: "Forensic Scientist", time: "Masters", exam: "Entrance", desc: "Crime scene analysis." },

    "ca": { title: "Chartered Accountant", time: "5 Years", exam: "Finals", desc: "Audit, Tax, Finance expert." },
    "cs": { title: "Company Secretary", time: "3 Years", exam: "Finals", desc: "Corporate law compliance." },
    "cma": { title: "Cost Accountant", time: "3 Years", exam: "Finals", desc: "Cost management & budgeting." },
    "mba": { title: "MBA", time: "2 Years", exam: "CAT", desc: "Business Management." },
    "bank": { title: "Investment Banker", time: "High Stress", exam: "CFA", desc: "Stock market & mergers." },
    "digital": { title: "Digital Marketer", time: "Job Ready", exam: "None", desc: "Online ads & SEO." },

    "ias": { title: "IAS / IPS", time: "Prep", exam: "UPSC", desc: "Civil Services." },
    "prof": { title: "Professor", time: "PhD", exam: "NET", desc: "University teaching." },
    "lawyer": { title: "Lawyer", time: "Practice", exam: "Bar Council", desc: "Legal practice." },
    "psych": { title: "Psychologist", time: "Masters", exam: "License", desc: "Mental health therapy." },
    "design": { title: "Designer", time: "4 Years", exam: "NIFT/NID", desc: "Fashion or Interior design." },
    "journ": { title: "Journalist", time: "3 Years", exam: "Entrance", desc: "News & Media." }
  };

  function selectNode(id, parentId) {
    // Reset
    document.querySelectorAll('.node-box').forEach(n => n.classList.remove('active'));
    
    // Highlight Current
    const current = document.getElementById(id);
    if(current) current.classList.add('active');

    // Trace Backwards
    let pid = parentId;
    while(pid) {
      const pNode = document.getElementById(pid);
      if(pNode) {
        pNode.classList.add('active');
        // Extract parent ID from onclick attribute
        const match = pNode.getAttribute('onclick').match(/'([^']*)'\)$/);
        pid = match && match[1] !== 'null' ? match[1] : null;
      } else {
        pid = null;
      }
    }

    // Info Panel
    const info = data[id];
    if(info) {
      document.getElementById('panel-title').innerText = info.title;
      document.getElementById('panel-time').innerText = info.time;
      document.getElementById('panel-exam').innerText = info.exam;
      document.getElementById('panel-desc').innerText = info.desc;
      document.getElementById('info-box').style.display = 'block';
    }
  }

  function closeInfo() {
    document.getElementById('info-box').style.display = 'none';
  }
</script>
