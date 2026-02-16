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

  /* 3. TREE CSS */
  ul.tree, ul.tree ul {
    list-style: none;
    margin: 0;
    padding: 0;
  }

  ul.tree ul {
    margin-left: 30px;
    position: relative;
  }

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
    padding: 0 15px;
    line-height: 2.5em;
    position: relative;
  }

  ul.tree ul li:before {
    content: "";
    display: block;
    width: 25px;
    height: 0;
    border-top: 2px solid #ccc;
    position: absolute;
    top: 1.25em;
    left: 0;
  }

  ul.tree ul li:last-child:before {
    background: #f4f6f8;
    height: auto;
    top: 1.25em;
    bottom: 0;
  }

  /* 4. NODE STYLING */
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

  .node-box.active {
    background: #0A2342;
    color: #D4AF37;
    border-color: #D4AF37;
    box-shadow: 0 0 15px rgba(212, 175, 55, 0.5);
  }

  /* MATHS TAGS */
  .math-tag {
    font-size: 0.7rem;
    background: #e3f2fd;
    color: #1565c0;
    padding: 2px 6px;
    border-radius: 4px;
    margin-left: 5px;
    border: 1px solid #90caf9;
  }

  /* 5. INFO PANEL */
  .info-panel {
    position: fixed;
    bottom: 20px;
    right: 20px;
    width: 320px;
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
          <span class="node-box" id="comm" onclick="selectNode('comm', 'root')">Commerce Stream</span>
          <ul>
            
            <li>
              <span class="node-box" id="fin_track" onclick="selectNode('fin_track', 'comm')">Finance & Accounts</span>
              <ul>
                <li><span class="node-box" id="ca" onclick="selectNode('ca', 'fin_track')">Chartered Accountant (CA)</span></li>
                <li><span class="node-box" id="cs" onclick="selectNode('cs', 'fin_track')">Company Secretary (CS)</span></li>
                <li><span class="node-box" id="cma" onclick="selectNode('cma', 'fin_track')">Cost Mgmt Accountant</span></li>
              </ul>
            </li>

            <li>
              <span class="node-box" id="biz_track" onclick="selectNode('biz_track', 'comm')">Business & MBA</span>
              <ul>
                <li><span class="node-box" id="mba" onclick="selectNode('mba', 'biz_track')">MBA (Finance/HR/Mkt)</span><span class="math-tag">Maths Pref</span></li>
                <li><span class="node-box" id="startup" onclick="selectNode('startup', 'biz_track')">Entrepreneurship</span></li>
                <li><span class="node-box" id="bba" onclick="selectNode('bba', 'biz_track')">BBA / Management</span></li>
              </ul>
            </li>

            <li>
              <span class="node-box" id="new_age" onclick="selectNode('new_age', 'comm')">New-Age / Tech</span>
              <ul>
                <li><span class="node-box" id="data_analyst" onclick="selectNode('data_analyst', 'new_age')">Data Analytics</span><span class="math-tag">Maths Req</span></li>
                <li><span class="node-box" id="fintech" onclick="selectNode('fintech', 'new_age')">FinTech Expert</span></li>
                <li><span class="node-box" id="stock" onclick="selectNode('stock', 'new_age')">Stock Trader / Inv. Banker</span><span class="math-tag">Maths Req</span></li>
                <li><span class="node-box" id="digi_mark" onclick="selectNode('digi_mark', 'new_age')">Digital Marketing</span></li>
              </ul>
            </li>

            <li>
              <span class="node-box" id="govt_track" onclick="selectNode('govt_track', 'comm')">Banking & Govt</span>
              <ul>
                <li><span class="node-box" id="bank_po" onclick="selectNode('bank_po', 'govt_track')">Bank PO / RBI</span></li>
                <li><span class="node-box" id="upsc_comm" onclick="selectNode('upsc_comm', 'govt_track')">UPSC (Civil Services)</span></li>
              </ul>
            </li>

             <li>
              <span class="node-box" id="law_comm" onclick="selectNode('law_comm', 'comm')">Legal Careers</span>
              <ul>
                <li><span class="node-box" id="corp_law" onclick="selectNode('corp_law', 'law_comm')">Corporate Lawyer</span></li>
              </ul>
            </li>

          </ul>
        </li>

        <li>
          <span class="node-box" id="pcm" onclick="selectNode('pcm', 'root')">Science (PCM)</span>
          <ul>
            <li>
              <span class="node-box" id="btech" onclick="selectNode('btech', 'pcm')">Engineering (B.Tech)</span>
              <ul>
                <li><span class="node-box" id="cse" onclick="selectNode('cse', 'btech')">Software/IT</span></li>
                <li><span class="node-box" id="mech" onclick="selectNode('mech', 'btech')">Mechanical</span></li>
              </ul>
            </li>
            <li><span class="node-box" id="barch" onclick="selectNode('barch', 'pcm')">Architecture</span></li>
            <li><span class="node-box" id="pilot" onclick="selectNode('pilot', 'pcm')">Commercial Pilot</span></li>
          </ul>
        </li>

        <li>
          <span class="node-box" id="pcb" onclick="selectNode('pcb', 'root')">Science (PCB)</span>
          <ul>
            <li><span class="node-box" id="mbbs" onclick="selectNode('mbbs', 'pcb')">MBBS (Doctor)</span></li>
            <li><span class="node-box" id="dentist" onclick="selectNode('dentist', 'pcb')">Dentist</span></li>
            <li><span class="node-box" id="biotech" onclick="selectNode('biotech', 'pcb')">Biotechnology</span></li>
          </ul>
        </li>

        <li>
          <span class="node-box" id="arts" onclick="selectNode('arts', 'root')">Arts / Humanities</span>
          <ul>
            <li><span class="node-box" id="ias" onclick="selectNode('ias', 'arts')">UPSC (IAS/IPS)</span></li>
            <li><span class="node-box" id="psych" onclick="selectNode('psych', 'arts')">Psychology</span></li>
            <li><span class="node-box" id="design" onclick="selectNode('design', 'arts')">Design (NIFT)</span></li>
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
  <p><strong>📝 Exams/Stats:</strong> <span id="panel-exam" style="color:#D4AF37; font-weight:bold;"></span></p>
  <hr style="border:0; border-top:1px solid #eee;">
  <p id="panel-desc" style="font-size:0.9rem; color:#555;">Desc</p>
  <a href="{{ '/book-expert/' | relative_url }}" class="btn" style="background:#0A2342; color:white; padding:10px; display:block; text-align:center; text-decoration:none; border-radius:5px; margin-top:15px;">Talk to Counsellor</a>
</div>

<script>
  // --- DATABASE ---
  const data = {
    "root": { title: "Class 10 Pass", time: "1 Year", exam: "Boards", desc: "The foundation. Your choice here defines your future options." },
    
    // COMMERCE STREAM DETAILS
    "comm": { title: "Commerce Stream", time: "2 Years", exam: "Maths vs Non-Maths", desc: "The BIG decision. 'With Maths' opens high-end finance & analytics. 'Without Maths' is great for CA, Law, and Management." },
    
    "fin_track": { title: "Finance & Accounts", time: "Professional", exam: "ICAI / ICSI", desc: "The most popular route. Auditing, Taxes, and Costing." },
    "ca": { title: "Chartered Accountant (CA)", time: "4.5 - 5 Years", exam: "Difficulty: ⭐⭐⭐⭐⭐", desc: "Audit companies & taxes. Salary: ₹8-25 LPA. Requires long study hours & handling pressure." },
    "cs": { title: "Company Secretary (CS)", time: "3 - 4 Years", exam: "Difficulty: ⭐⭐⭐⭐", desc: "Corporate law advisor. More theory/law than maths. Salary: High growth in corporate sector." },
    "cma": { title: "Cost Mgmt Accountant", time: "3 - 4 Years", exam: "Difficulty: ⭐⭐⭐⭐", desc: "Budgeting & Profit Planning. Best for corporate finance roles." },

    "biz_track": { title: "Business & Management", time: "Degree + Masters", exam: "CAT / GMAT", desc: "Leadership, HR, Marketing, and Operations." },
    "mba": { title: "MBA", time: "2 Years (Post Grad)", exam: "CAT / GMAT", desc: "Salary: ₹6-40 LPA. Top colleges prefer Maths background. Leads to CEO/Management roles." },
    "startup": { title: "Entrepreneurship", time: "Anytime", exam: "None", desc: "Start an online business, agency, or trading. Commerce is the BEST background for this." },
    "bba": { title: "BBA", time: "3 Years", exam: "IPMAT / CUET", desc: "Foundation for MBA. Good for students who like presentations and leadership." },

    "new_age": { title: "New-Age Careers", time: "Skill Based", exam: "Portfolio", desc: "Exploding demand in India. Tech + Finance mix." },
    "data_analyst": { title: "Data Analytics", time: "6-12 Months", exam: "Python/SQL Skills", desc: "Requires Maths. Analyze business data using Excel & SQL. Huge demand." },
    "fintech": { title: "FinTech Expert", time: "Varies", exam: "Tech Skills", desc: "Finance + Technology. One of the fastest growing fields globally." },
    "stock": { title: "Stock Trader / Inv. Banker", time: "High Stress", exam: "CFA / NISM", desc: "Portfolio management & trading. Maths/Stats is highly recommended." },
    "digi_mark": { title: "Digital Marketing", time: "3-6 Months", exam: "Certifications", desc: "SEO, Ads, Content Strategy. No Maths required. Great for creative minds." },

    "govt_track": { title: "Banking & Govt", time: "Prep (1-2 Yrs)", exam: "Competitive Exams", desc: "Stable jobs with good perks." },
    "bank_po": { title: "Bank PO / RBI", time: "Prep", exam: "IBPS / SBI PO", desc: "Commerce students do very well here. Manage banking operations." },
    "upsc_comm": { title: "UPSC (Civil Services)", time: "Prep", exam: "CSE", desc: "IAS/IPS/IRS. Commerce is a strong optional subject for Mains." },

    "law_comm": { title: "Legal Careers", time: "5 Years", exam: "CLAT", desc: "Integrated BBA-LLB or B.Com-LLB." },
    "corp_law": { title: "Corporate Lawyer", time: "5 Years", exam: "CLAT", desc: "Legal advisor to companies. Very high salary potential. Maths not required." },

    // SCIENCE & ARTS (Brief for context)
    "pcm": { title: "Science (PCM)", time: "2 Years", exam: "Boards", desc: "Physics, Chem, Math. Hardest stream." },
    "btech": { title: "B.Tech", time: "4 Years", exam: "JEE", desc: "Engineering." },
    "cse": { title: "Software Engineer", time: "Job Ready", exam: "Interviews", desc: "Coding & AI." },
    "mech": { title: "Mechanical Eng", time: "Job Ready", exam: "GATE", desc: "Machines & Robotics." },
    "barch": { title: "Architecture", time: "5 Years", exam: "NATA", desc: "Building Design." },
    "pilot": { title: "Pilot", time: "18 Months", exam: "DGCA", desc: "Aviation." },

    "pcb": { title: "Science (PCB)", time: "2 Years", exam: "Boards", desc: "Physics, Chem, Biology." },
    "mbbs": { title: "MBBS", time: "5.5 Years", exam: "NEET", desc: "Doctor." },
    "dentist": { title: "Dentist", time: "5 Years", exam: "NEET", desc: "Dental Surgery." },
    "biotech": { title: "Biotech", time: "Masters", exam: "GATE", desc: "Research." },

    "arts": { title: "Arts / Humanities", time: "2 Years", exam: "Boards", desc: "History, Pol Sci. For UPSC/Law." },
    "ias": { title: "UPSC (IAS)", time: "Prep", exam: "CSE", desc: "Civil Services." },
    "psych": { title: "Psychology", time: "Masters", exam: "License", desc: "Therapy/HR." },
    "design": { title: "Design", time: "4 Years", exam: "NIFT", desc: "Fashion/Interior." }
  };

  function selectNode(id, parentId) {
    document.querySelectorAll('.node-box').forEach(n => n.classList.remove('active'));
    
    const current = document.getElementById(id);
    if(current) current.classList.add('active');

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
