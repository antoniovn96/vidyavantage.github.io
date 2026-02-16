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

  /* 5. INFO PANEL */
  .info-panel {
    position: fixed;
    bottom: 20px;
    right: 20px;
    width: 340px;
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
  <p style="opacity:0.8;">Click any career to see details. <br>10th doesn't decide your life, but it decides your next path.</p>
</div>

<div class="tree-wrapper">
  <ul class="tree">
    
    <li>
      <span class="node-box" id="root" onclick="selectNode('root', null)">Class 10th (Pass)</span>
      
      <ul>
        
        <li>
          <span class="node-box" id="sci" onclick="selectNode('sci', 'root')">1. Science Stream</span>
          <ul>
            
            <li>
              <span class="node-box" id="med_track" onclick="selectNode('med_track', 'sci')">🔬 Medical (PCB)</span>
              <ul>
                <li><span class="node-box" id="mbbs" onclick="selectNode('mbbs', 'med_track')">MBBS (Doctor)</span></li>
                <li><span class="node-box" id="dentist" onclick="selectNode('dentist', 'med_track')">Dentist (BDS)</span></li>
                <li><span class="node-box" id="allied" onclick="selectNode('allied', 'med_track')">Physio / Nursing / Pharma</span></li>
                <li><span class="node-box" id="vet" onclick="selectNode('vet', 'med_track')">Veterinary Doctor</span></li>
                <li><span class="node-box" id="nutrition" onclick="selectNode('nutrition', 'med_track')">Nutritionist / Psych</span></li>
              </ul>
            </li>

            <li>
              <span class="node-box" id="eng_track" onclick="selectNode('eng_track', 'sci')">⚙️ Engineering (PCM)</span>
              <ul>
                <li><span class="node-box" id="btech" onclick="selectNode('btech', 'eng_track')">B.Tech (CSE / Mech / Civil)</span></li>
                <li><span class="node-box" id="arch" onclick="selectNode('arch', 'eng_track')">Architecture</span></li>
                <li><span class="node-box" id="aviation" onclick="selectNode('aviation', 'eng_track')">Aviation / Merchant Navy</span></li>
                <li><span class="node-box" id="tech_new" onclick="selectNode('tech_new', 'eng_track')">Data Science / Game Dev</span></li>
              </ul>
            </li>

            <li>
              <span class="node-box" id="research_track" onclick="selectNode('research_track', 'sci')">🧠 Research / New-Age</span>
              <ul>
                <li><span class="node-box" id="scientist" onclick="selectNode('scientist', 'research_track')">Scientist / ISRO</span></li>
                <li><span class="node-box" id="forensic" onclick="selectNode('forensic', 'research_track')">Forensic Science</span></li>
                <li><span class="node-box" id="genetics" onclick="selectNode('genetics', 'research_track')">Genetics / Neuro</span></li>
                <li><span class="node-box" id="robotics" onclick="selectNode('robotics', 'research_track')">AI & Robotics</span></li>
              </ul>
            </li>

          </ul>
        </li>

        <li>
          <span class="node-box" id="comm" onclick="selectNode('comm', 'root')">2. Commerce Stream</span>
          <ul>
            <li>
              <span class="node-box" id="fin_track" onclick="selectNode('fin_track', 'comm')">Finance & Accounts</span>
              <ul>
                <li><span class="node-box" id="ca" onclick="selectNode('ca', 'fin_track')">Chartered Accountant (CA)</span></li>
                <li><span class="node-box" id="cs" onclick="selectNode('cs', 'fin_track')">Company Secretary (CS)</span></li>
                <li><span class="node-box" id="bank_job" onclick="selectNode('bank_job', 'fin_track')">Banking / Stock Market</span></li>
              </ul>
            </li>
            <li>
              <span class="node-box" id="biz_track" onclick="selectNode('biz_track', 'comm')">Business & Mgmt</span>
              <ul>
                <li><span class="node-box" id="mba" onclick="selectNode('mba', 'biz_track')">MBA / Entrepreneur</span></li>
                <li><span class="node-box" id="digital" onclick="selectNode('digital', 'biz_track')">Digital Marketing</span></li>
                <li><span class="node-box" id="logistics" onclick="selectNode('logistics', 'biz_track')">Logistics / Supply Chain</span></li>
              </ul>
            </li>
          </ul>
        </li>

        <li>
          <span class="node-box" id="arts" onclick="selectNode('arts', 'root')">3. Arts / Humanities</span>
          <ul>
            <li>
              <span class="node-box" id="govt_track" onclick="selectNode('govt_track', 'arts')">Govt / Law</span>
              <ul>
                <li><span class="node-box" id="ias" onclick="selectNode('ias', 'govt_track')">UPSC (IAS / IPS)</span></li>
                <li><span class="node-box" id="lawyer" onclick="selectNode('lawyer', 'govt_track')">Lawyer / Judge</span></li>
              </ul>
            </li>
            <li>
              <span class="node-box" id="creative_track" onclick="selectNode('creative_track', 'arts')">Creative / Social</span>
              <ul>
                <li><span class="node-box" id="psych" onclick="selectNode('psych', 'creative_track')">Psychologist</span></li>
                <li><span class="node-box" id="journ" onclick="selectNode('journ', 'creative_track')">Journalist / Media</span></li>
                <li><span class="node-box" id="design" onclick="selectNode('design', 'creative_track')">Designer / Teacher</span></li>
              </ul>
            </li>
          </ul>
        </li>

        <li>
          <span class="node-box" id="diploma" onclick="selectNode('diploma', 'root')">4. Diploma (Skip +2)</span>
          <ul>
            <li>
              <span class="node-box" id="tech_dip" onclick="selectNode('tech_dip', 'diploma')">Technical Diploma</span>
              <ul>
                <li><span class="node-box" id="mech_dip" onclick="selectNode('mech_dip', 'tech_dip')">Mech / Civil / Elec</span></li>
                <li><span class="node-box" id="auto_dip" onclick="selectNode('auto_dip', 'tech_dip')">Automobile / Comp</span></li>
              </ul>
            </li>
            <li>
              <span class="node-box" id="voc_dip" onclick="selectNode('voc_dip', 'diploma')">Vocational</span>
              <ul>
                <li><span class="node-box" id="hotel" onclick="selectNode('hotel', 'voc_dip')">Hotel Management</span></li>
                <li><span class="node-box" id="fashion" onclick="selectNode('fashion', 'voc_dip')">Fashion / Animation</span></li>
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
  <div id="panel-tags" style="margin-bottom:10px;"></div>
  <p><strong>👉 Good if:</strong> <span id="panel-good" style="color:#D4AF37; font-weight:bold;"></span></p>
  <hr style="border:0; border-top:1px solid #eee;">
  <p id="panel-desc" style="font-size:0.9rem; color:#555; line-height:1.5;">Desc</p>
  <a href="{{ '/book-expert/' | relative_url }}" class="btn" style="background:#0A2342; color:white; padding:10px; display:block; text-align:center; text-decoration:none; border-radius:5px; margin-top:15px;">Talk to Counsellor</a>
</div>

<script>
  // --- DATABASE ---
  const data = {
    // ROOT
    "root": { title: "Class 10 Pass", good: "You are ready to choose your path", desc: "10th doesn't decide your life — it only decides your next path. You have 4 major routes." },
    
    // --- 1. SCIENCE ---
    "sci": { 
      title: "Science Stream", 
      good: "You are decent in Maths/Science OR want max options", 
      desc: "Subjects: Physics, Chem, Maths/Bio. Big Advantage: You can switch to Commerce/Arts later, but they cannot switch to Science." 
    },
    "med_track": { title: "Medical Line (PCB)", good: "You like Biology or helping people", desc: "Focus on PCB. Leads to NEET exam." },
    "mbbs": { title: "MBBS (Doctor)", good: "You can study hard for 5+ years", desc: "Top medical degree. Treat patients, surgery, hospitals." },
    "dentist": { title: "Dentist (BDS)", good: "You want medical field with work-life balance", desc: "Dental surgery and care." },
    "allied": { title: "Allied Health", good: "You want shorter courses", desc: "Nursing, Pharmacy, Physiotherapy. Very high demand." },
    "vet": { title: "Veterinary Doctor", good: "You love animals", desc: "Treating animals. Requires NEET." },
    "nutrition": { title: "Nutritionist / Psych", good: "You like health & mind", desc: "Diet planning or Mental health therapy." },

    "eng_track": { title: "Engineering Line (PCM)", good: "You like Maths, Machines, or Logic", desc: "Focus on PCM. Leads to JEE/CET exams." },
    "btech": { title: "B.Tech / B.E", good: "Problem Solving", desc: "Mechanical, Civil, ECE, CSE. Build things and software." },
    "arch": { title: "Architecture", good: "Drawing + Logic", desc: "Design buildings. Requires NATA exam." },
    "aviation": { title: "Aviation / Navy", good: "Adventure & Travel", desc: "Pilot or Merchant Navy. High pay, high discipline." },
    "tech_new": { title: "New-Age Tech", good: "Coding & Data", desc: "Data Science, Game Dev, AI. The future of tech." },

    "research_track": { title: "Research & New-Age", good: "You are curious & innovative", desc: "For scientists and inventors." },
    "scientist": { title: "Scientist (ISRO/DRDO)", good: "Deep thinking", desc: "Space science, Physics research." },
    "forensic": { title: "Forensic Science", good: "Investigation", desc: "Crime scene analysis and lab work." },
    "genetics": { title: "Genetics / Neuro", good: "Biology Research", desc: "Study of genes and brain science." },
    "robotics": { title: "AI & Robotics", good: "Building Bots", desc: "Creating intelligent machines." },

    // --- 2. COMMERCE ---
    "comm": { 
      title: "Commerce Stream", 
      good: "You handle numbers/logic but dislike heavy science", 
      desc: "Subjects: Accounts, Econ, Business. High earning potential with less academic stress than Science." 
    },
    "fin_track": { title: "Finance & Accounts", good: "You love money management", desc: "Core finance careers." },
    "ca": { title: "Chartered Accountant", good: "Hard work & Numbers", desc: "Audit and Tax expert. Tough exam but high respect." },
    "cs": { title: "Company Secretary", good: "Law & Corporate Rules", desc: "Legal compliance for companies." },
    "bank_job": { title: "Banking / Stock Mkt", good: "Fast calculations", desc: "Investment banker, Stock trader, Bank PO." },

    "biz_track": { title: "Business & Mgmt", good: "Leadership & Strategy", desc: "Running companies and teams." },
    "mba": { title: "MBA / Entrepreneur", good: "Starting businesses", desc: "Master of Business Admin. CEO roles." },
    "digital": { title: "Digital Marketing", good: "Creativity + Data", desc: "Social media, SEO, Ads." },
    "logistics": { title: "Logistics", good: "Organization", desc: "Supply chain management. Moving goods globally." },

    // --- 3. ARTS ---
    "arts": { 
      title: "Arts / Humanities", 
      good: "Creativity, Social Understanding, Debating", 
      desc: "Subjects: Psych, History, Pol Sci. Underrated but powerful for Govt jobs and Creativity." 
    },
    "govt_track": { title: "Govt & Law", good: "Service & Arguments", desc: "Serving the nation or fighting for justice." },
    "ias": { title: "UPSC (IAS/IPS)", good: "Power & Responsibility", desc: "Civil Services. Arts is the best base for this." },
    "lawyer": { title: "Lawyer / Judge", good: "Logic & Speaking", desc: "Legal practice. Corporate or Criminal law." },

    "creative_track": { title: "Creative & Social", good: "Understanding People", desc: "Helping society and expression." },
    "psych": { title: "Psychologist", good: "Empathy", desc: "Therapy and mental health." },
    "journ": { title: "Journalist / Media", good: "Storytelling", desc: "News, Reporting, Media production." },
    "design": { title: "Designer / Teacher", good: "Artistic Skill", desc: "Fashion, Interior, or Professor." },

    // --- 4. DIPLOMA ---
    "diploma": { 
      title: "Diploma (Polytechnic)", 
      good: "You hate theory & want hands-on work", 
      desc: "Skip 11th/12th. 3-Year practical course. Direct entry to Engineering 2nd year later." 
    },
    "tech_dip": { title: "Technical Diploma", good: "Machines & Tools", desc: "Mechanical, Civil, Electrical." },
    "mech_dip": { title: "Mech/Civil/Elec", good: "Fixing things", desc: "Core technical jobs early in career." },
    "auto_dip": { title: "Auto / Computer", good: "Cars or Code", desc: "Automobile repair or basic coding." },
    
    "voc_dip": { title: "Vocational", good: "Specific Skills", desc: "Non-technical practical careers." },
    "hotel": { title: "Hotel Management", good: "Hospitality", desc: "Chefs, Hotel operations." },
    "fashion": { title: "Fashion / Animation", good: "Visual Art", desc: "Designing clothes or VFX/Movies." }
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
      document.getElementById('panel-good').innerText = info.good;
      document.getElementById('panel-desc').innerText = info.desc;
      document.getElementById('info-box').style.display = 'block';
    }
  }

  function closeInfo() {
    document.getElementById('info-box').style.display = 'none';
  }
</script>
