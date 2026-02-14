---
layout: default
title: Interactive Career Mindmap
permalink: /career-search/
---

<style>
  /* MINDMAP CONTAINER */
  .mindmap-wrapper {
    display: flex;
    flex-direction: column;
    align-items: center;
    padding: 40px 20px;
    background: #f4f6f8;
    overflow-x: auto; /* Allow scrolling on mobile */
  }

  /* NODE STYLING */
  .node {
    border: 2px solid #ccc;
    background: white;
    padding: 10px 20px;
    border-radius: 8px;
    cursor: pointer;
    font-size: 0.9rem;
    font-weight: bold;
    color: #0A2342;
    text-align: center;
    transition: all 0.3s;
    position: relative;
    min-width: 120px;
    margin: 0 10px;
    z-index: 2;
  }

  .node:hover {
    transform: scale(1.05);
    box-shadow: 0 5px 15px rgba(0,0,0,0.1);
  }

  /* ACTIVE STATE (The "Light Up" Effect) */
  .node.active {
    border-color: #D4AF37;
    background: #0A2342;
    color: #D4AF37;
    box-shadow: 0 0 15px rgba(212, 175, 55, 0.4);
  }

  /* TREE LINES */
  .level {
    display: flex;
    justify-content: center;
    padding-top: 40px;
    position: relative;
  }

  /* Vertical Lines */
  .level::before {
    content: '';
    position: absolute;
    top: 0;
    left: 50%;
    width: 2px;
    height: 20px;
    background: #ccc;
    z-index: 1;
  }
  
  /* Horizontal Connectors handled by JS/Flex logic simplified for CSS tree */
  .branch {
    display: flex;
    flex-direction: column;
    align-items: center;
    position: relative;
    padding: 20px 10px 0;
  }

  /* Lines connecting parent to children */
  .branch::before {
    content: '';
    position: absolute;
    top: 0;
    left: 50%;
    width: 2px;
    height: 20px;
    background: #ccc;
  }

  .branch::after {
    content: '';
    position: absolute;
    top: 0;
    left: 0;
    width: 50%; /* Covers half width to create T shape */
    height: 2px;
    background: #ccc;
  }
  .branch:first-child::after { left: 50%; width: 50%; }
  .branch:last-child::after { left: 0; width: 50%; }
  .branch:only-child::after { display: none; } /* No horizontal line if only 1 child */
  
  /* Remove top horizontal line for middle branches */
  .branch:not(:first-child):not(:last-child)::after {
    width: 100%;
    left: 0;
  }

  /* INFO PANEL (Popup) */
  .info-panel {
    position: fixed;
    bottom: 20px;
    right: 20px;
    width: 300px;
    background: white;
    border-left: 5px solid #D4AF37;
    box-shadow: 0 5px 20px rgba(0,0,0,0.2);
    padding: 20px;
    border-radius: 8px;
    display: none; /* Hidden by default */
    z-index: 100;
    animation: slideIn 0.3s;
  }

  @keyframes slideIn {
    from { transform: translateX(100%); opacity: 0; }
    to { transform: translateX(0); opacity: 1; }
  }

  .info-title { font-size: 1.2rem; color: #0A2342; margin-top: 0; }
  .info-tag { background: #eee; padding: 2px 8px; border-radius: 4px; font-size: 0.8rem; margin-right: 5px; }
  
  /* HIGHLIGHTED PATH LINES (Advanced CSS) */
  .branch.path-active > .node { border-color: #D4AF37; }
  .branch.path-active::before { background: #D4AF37; }
</style>

<div style="text-align: center; padding: 40px 20px; background: #0A2342; color: white;">
  <h1>Interactive Career Roadmap</h1>
  <p>Click on any career (bottom level) to trace your path backward.</p>
</div>

<div class="mindmap-wrapper">
  
  <div class="node" id="root" onclick="selectNode('root', null)">Class 10th (Pass)</div>
  
  <div class="level" style="border-top: 2px solid #ccc; width: 90%;">
    
    <div class="branch">
      <div class="node" id="pcm" onclick="selectNode('pcm', 'root')">Science (PCM)</div>
      <div class="level">
        <div class="branch">
          <div class="node" id="btech" onclick="selectNode('btech', 'pcm')">B.Tech (Engg)</div>
          <div class="level">
            <div class="branch"><div class="node" id="soft_eng" onclick="selectNode('soft_eng', 'btech')">Software Engineer</div></div>
            <div class="branch"><div class="node" id="civil_eng" onclick="selectNode('civil_eng', 'btech')">Civil Engineer</div></div>
          </div>
        </div>
        <div class="branch">
          <div class="node" id="barch" onclick="selectNode('barch', 'pcm')">B.Arch</div>
          <div class="level">
             <div class="branch"><div class="node" id="architect" onclick="selectNode('architect', 'barch')">Architect</div></div>
          </div>
        </div>
      </div>
    </div>

    <div class="branch">
      <div class="node" id="pcb" onclick="selectNode('pcb', 'root')">Science (PCB)</div>
      <div class="level">
        <div class="branch">
          <div class="node" id="mbbs" onclick="selectNode('mbbs', 'pcb')">MBBS</div>
          <div class="level">
            <div class="branch"><div class="node" id="doctor" onclick="selectNode('doctor', 'mbbs')">Doctor (MD)</div></div>
          </div>
        </div>
        <div class="branch">
          <div class="node" id="bsc_bio" onclick="selectNode('bsc_bio', 'pcb')">B.Sc Biology</div>
          <div class="level">
            <div class="branch"><div class="node" id="researcher" onclick="selectNode('researcher', 'bsc_bio')">Researcher</div></div>
          </div>
        </div>
      </div>
    </div>

    <div class="branch">
      <div class="node" id="comm" onclick="selectNode('comm', 'root')">Commerce</div>
      <div class="level">
        <div class="branch">
          <div class="node" id="bcom" onclick="selectNode('bcom', 'comm')">B.Com / BBA</div>
          <div class="level">
            <div class="branch"><div class="node" id="mba" onclick="selectNode('mba', 'bcom')">MBA (Business)</div></div>
            <div class="branch"><div class="node" id="ca" onclick="selectNode('ca', 'bcom')">Chart. Accountant</div></div>
          </div>
        </div>
      </div>
    </div>

    <div class="branch">
      <div class="node" id="arts" onclick="selectNode('arts', 'root')">Arts / Humanities</div>
      <div class="level">
        <div class="branch">
          <div class="node" id="ba" onclick="selectNode('ba', 'arts')">B.A (Pol Sci/Hist)</div>
          <div class="level">
            <div class="branch"><div class="node" id="ias" onclick="selectNode('ias', 'ba')">IAS / IPS (UPSC)</div></div>
            <div class="branch"><div class="node" id="lawyer" onclick="selectNode('lawyer', 'ba')">Lawyer (LLB)</div></div>
          </div>
        </div>
      </div>
    </div>

  </div>
</div>

<div id="info-box" class="info-panel">
  <button onclick="closeInfo()" style="float:right; background:none; border:none; font-size:1.2rem; cursor:pointer;">&times;</button>
  <h3 id="panel-title" class="info-title">Career Title</h3>
  <p><strong>⏱️ Duration:</strong> <span id="panel-time"></span></p>
  <p><strong>📝 Exams/Marks:</strong> <span id="panel-exam"></span></p>
  <hr style="border:0; border-top:1px solid #eee;">
  <p id="panel-desc" style="font-size:0.9rem; color:#555;">Description goes here.</p>
  <a href="{{ '/book-expert/' | relative_url }}" class="btn" style="background:#0A2342; color:white; padding:5px 10px; font-size:0.8rem; text-decoration:none; display:block; text-align:center; margin-top:10px; border-radius:4px;">Get Guidance</a>
</div>

<script>
  // --- DATA DATABASE ---
  const careerData = {
    "root": { title: "Class 10th", time: "1 Year", exam: "Board Exams (min 50%)", desc: "The foundation. Focus on Math and Science if you want Engineering/Medical." },
    
    // STREAMS
    "pcm": { title: "Science (PCM)", time: "2 Years (11th & 12th)", exam: "Min 75% for IITs", desc: "Physics, Chemistry, Maths. The hardest stream, opens Engineering & Architecture." },
    "pcb": { title: "Science (PCB)", time: "2 Years (11th & 12th)", exam: "Min 50% for NEET", desc: "Physics, Chemistry, Biology. The path for Doctors, Dentists, and Zoologists." },
    "comm": { title: "Commerce", time: "2 Years", exam: "Min 60% for Top Colleges", desc: "Business, Accounts, Economics. Good for Finance, Banking, and Management." },
    "arts": { title: "Arts / Humanities", time: "2 Years", exam: "Cutoffs vary", desc: "History, Pol Sci, Psychology. The best foundation for UPSC/Civil Services & Law." },

    // DEGREES
    "btech": { title: "B.Tech / B.E", time: "4 Years", exam: "JEE Mains / Advanced", desc: "Bachelor of Technology. Core engineering degree." },
    "barch": { title: "B.Arch", time: "5 Years", exam: "NATA / JEE Paper 2", desc: "Bachelor of Architecture. Design buildings and spaces." },
    "mbbs": { title: "MBBS", time: "5.5 Years", exam: "NEET UG", desc: "Bachelor of Medicine. Requires intense study and hospital internship." },
    "bsc_bio": { title: "B.Sc", time: "3 Years", exam: "CUET", desc: "Bachelor of Science. Pure science degree for research or teaching." },
    "bcom": { title: "B.Com / BBA", time: "3-4 Years", exam: "CUET / IPMAT", desc: "Bachelor of Commerce or Business Admin. Foundation for corporate jobs." },
    "ba": { title: "Bachelor of Arts", time: "3-4 Years", exam: "CUET", desc: "Undergraduate degree in Humanities subjects." },

    // CAREERS
    "soft_eng": { title: "Software Engineer", time: "Entry Level", exam: "Coding Interviews", desc: "Build apps, websites, and AI systems. High demand globally." },
    "civil_eng": { title: "Civil Engineer", time: "Entry Level", exam: "GATE (for PSU)", desc: "Build bridges, dams, and roads. Government jobs available." },
    "architect": { title: "Licensed Architect", time: "Professional", exam: "COA Registration", desc: "Design homes and corporate offices. Creative + Technical." },
    "doctor": { title: "Doctor (MD/MS)", time: "3 Years (Post MBBS)", exam: "NEET PG", desc: "Specialist doctor (Cardiologist, Surgeon, etc.). High respect." },
    "researcher": { title: "Scientist / Researcher", time: "PhD (3-5 Years)", exam: "NET / JRF", desc: "Work in labs discovering new biology or medicines." },
    "mba": { title: "MBA", time: "2 Years", exam: "CAT / GMAT", desc: "Master of Business Admin. For Management, CEO roles, and Marketing." },
    "ca": { title: "Chartered Accountant", time: "4-5 Years", exam: "ICAI Exams", desc: "Expert in Audit and Tax. Very tough exams, high salary." },
    "ias": { title: "IAS / IPS Officer", time: "Preparation (1-2 Yrs)", exam: "UPSC CSE", desc: "Civil Services. Run the government administration." },
    "lawyer": { title: "Lawyer / Judge", time: "3 Years (LLB)", exam: "CLAT", desc: "Legal practice in courts or corporate firms." }
  };

  // --- LOGIC ---
  function selectNode(id, parentId) {
    // 1. Reset all nodes
    document.querySelectorAll('.node').forEach(n => n.classList.remove('active'));
    
    // 2. Light up current node
    const current = document.getElementById(id);
    if(current) current.classList.add('active');

    // 3. Trace Backwards (The "Light Up" Logic)
    let pid = parentId;
    while(pid) {
      const pNode = document.getElementById(pid);
      if(pNode) {
        pNode.classList.add('active');
        // Find the next parent
        // (This is a simplified lookup since we hardcoded onclicks. 
        // In a dynamic app, we'd use a parent-map)
        pid = pNode.getAttribute('onclick').match(/'([^']*)'\)$/)[1]; 
        if(pid === 'null') pid = null;
      } else {
        pid = null;
      }
    }

    // 4. Show Info Panel
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
