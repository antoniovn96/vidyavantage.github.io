---
layout: default
title: "The Ultimate Career Roadmap 🚀"
permalink: /career-search/
image: "/assets/images/roadmap-preview.png"
description: "Confused after Class 10? Explore the complete interactive roadmap for Science, Commerce, Arts, and Teaching careers. Check exams, salaries, and real advice."
---

<style>
  /* 1. LAYOUT & BACKGROUND */
  .main-content {
    max-width: 100% !important;
    padding: 0 !important;
    margin: 0 !important;
  }
  
  body { 
    background-color: #f0f4f8; 
    background-image: radial-gradient(#e1e8ed 1px, transparent 1px);
    background-size: 20px 20px;
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
  }

  /* 2. QUOTES CAROUSEL (Modern Glass Style) */
  .quote-container {
    background: linear-gradient(135deg, #0A2342, #1C3B70);
    color: #FFD700;
    padding: 25px;
    text-align: center;
    position: relative;
    overflow: hidden;
    height: 70px;
    display: flex;
    align-items: center;
    justify-content: center;
    box-shadow: 0 4px 15px rgba(0,0,0,0.2);
    margin-bottom: 20px;
  }

  .quote-slide {
    font-size: 1.2rem;
    font-style: italic;
    font-weight: 500;
    opacity: 0;
    position: absolute;
    transition: opacity 1s ease-in-out, transform 1s ease;
    width: 80%;
    transform: translateY(20px);
  }

  .quote-slide.active { opacity: 1; transform: translateY(0); }

  /* 3. TREE CONTAINER */
  .tree-wrapper {
    max-width: 1100px;
    margin: 0 auto;
    padding: 40px 20px 100px;
    overflow-x: auto;
  }

  /* 4. TREE CSS (Connectors) */
  ul.tree, ul.tree ul {
    list-style: none;
    margin: 0;
    padding: 0;
  }

  ul.tree ul {
    margin-left: 40px; /* More spacing */
    position: relative;
  }

  /* Vertical Line */
  ul.tree ul:before {
    content: "";
    display: block;
    width: 0;
    position: absolute;
    top: 0;
    bottom: 0;
    left: 0;
    border-left: 3px solid #cbd5e0; /* Thicker, softer gray */
    transition: border-color 0.3s;
  }

  ul.tree li {
    margin: 0;
    padding: 0 20px;
    line-height: 3.5em; /* More vertical breathing room */
    position: relative;
  }

  /* Horizontal Line */
  ul.tree ul li:before {
    content: "";
    display: block;
    width: 30px;
    height: 0;
    border-top: 3px solid #cbd5e0;
    position: absolute;
    top: 1.75em;
    left: 0;
    transition: border-color 0.3s;
  }

  ul.tree ul li:last-child:before {
    background: #f0f4f8; /* Match body bg */
    height: auto;
    top: 1.75em;
    bottom: 0;
  }

  /* 5. NODE STYLING (The Beautiful Cards) */
  .node-box {
    display: inline-flex;
    align-items: center;
    padding: 12px 20px;
    border: none;
    background: white;
    border-radius: 12px;
    font-weight: 600;
    color: #2d3748;
    cursor: pointer;
    transition: all 0.3s cubic-bezier(0.25, 0.8, 0.25, 1);
    font-size: 1rem;
    position: relative;
    z-index: 2;
    box-shadow: 0 4px 6px rgba(50, 50, 93, 0.11), 0 1px 3px rgba(0, 0, 0, 0.08);
    min-width: 180px;
  }

  .node-box:hover {
    transform: translateY(-3px) scale(1.02);
    box-shadow: 0 7px 14px rgba(50, 50, 93, 0.1), 0 3px 6px rgba(0, 0, 0, 0.08);
  }

  /* Active/Selected State */
  .node-box.active {
    background: linear-gradient(135deg, #0A2342 0%, #2a4365 100%);
    color: #FFD700;
    box-shadow: 0 0 0 3px rgba(10, 35, 66, 0.2);
  }

  /* Stream Specific Colors (Left Borders) */
  #sci, #sci ~ ul .node-box { border-left: 5px solid #3182ce; } /* Blue */
  #comm, #comm ~ ul .node-box { border-left: 5px solid #d69e2e; } /* Gold */
  #arts, #arts ~ ul .node-box { border-left: 5px solid #805ad5; } /* Purple */
  #diploma, #diploma ~ ul .node-box { border-left: 5px solid #38a169; } /* Green */

  /* Switch Nodes Styling */
  .node-box.switch {
    background: #fffaf0;
    border: 2px dashed #ed8936 !important;
    border-left: none !important;
    color: #c05621;
  }
  .node-box.switch:hover {
    background: #feebc8;
  }

  /* 6. INFO PANEL (Floating Card) */
  .info-panel {
    position: fixed;
    bottom: 30px;
    right: 30px;
    width: 350px;
    background: rgba(255, 255, 255, 0.95);
    backdrop-filter: blur(10px);
    border-top: 6px solid #D4AF37;
    box-shadow: 0 20px 40px rgba(0,0,0,0.2);
    padding: 25px;
    border-radius: 15px;
    display: none;
    z-index: 1000;
    animation: slideIn 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275);
    font-family: 'Open Sans', sans-serif;
  }

  @keyframes slideIn {
    from { transform: translateY(100%); opacity: 0; }
    to { transform: translateY(0); opacity: 1; }
  }

  .back-btn {
    position: fixed;
    top: 20px;
    left: 20px;
    background: white;
    color: #0A2342 !important;
    padding: 10px 25px;
    border-radius: 50px;
    text-decoration: none;
    font-weight: bold;
    z-index: 500;
    font-size: 0.95rem;
    box-shadow: 0 4px 10px rgba(0,0,0,0.15);
    transition: transform 0.2s;
  }
  .back-btn:hover { transform: scale(1.05); }

</style>

<a href="{{ '/' | relative_url }}" class="back-btn">← Back to Home</a>

<div style="text-align: center; padding: 80px 20px 20px; background: #0A2342; border-bottom: 5px solid #D4AF37;">
  <h1 style="margin:0; color: #ffffff !important; font-size: 3rem; font-weight: 800; text-shadow: 0 4px 10px rgba(0,0,0,0.3);">Your Career Roadmap 🧭</h1>
  <p style="color: #cbd5e0 !important; font-size: 1.3rem; margin-top: 15px; font-weight: 300;">Interactive. Verified. Complete.</p>
</div>

<div class="quote-container">
  <div class="quote-slide active">"The future belongs to those who believe in the beauty of their dreams." — Eleanor Roosevelt</div>
  <div class="quote-slide">"Choose a job you love, and you will never have to work a day in your life." — Confucius</div>
  <div class="quote-slide">"Education is the passport to the future." — Malcolm X</div>
  <div class="quote-slide">"Don't watch the clock; do what it does. Keep going." — Sam Levenson</div>
  <div class="quote-slide">"Your time is limited, so don't waste it living someone else's life." — Steve Jobs</div>
  <div class="quote-slide">"Opportunities don't happen. You create them." — Chris Grosser</div>
  <div class="quote-slide">"Success is not the key to happiness. Happiness is the key to success." — Albert Schweitzer</div>
  <div class="quote-slide">"The only way to do great work is to love what you do." — Steve Jobs</div>
</div>

<div class="tree-wrapper">
  <ul class="tree">
    
    <li>
      <span class="node-box" id="root" onclick="selectNode('root', null)" style="border-left: 5px solid #2d3748; background: #2d3748; color: white;">🎓 Class 10th (Pass)</span>
      
      <ul>
        
        <li>
          <span class="node-box" id="sci" onclick="selectNode('sci', 'root')">🧬 Science Stream</span>
          <ul>
            <li>
              <span class="node-box" id="med_track" onclick="selectNode('med_track', 'sci')">Medical (PCB)</span>
              <ul>
                <li><span class="node-box" id="mbbs" onclick="selectNode('mbbs', 'med_track')">MBBS (Doctor)</span></li>
                <li><span class="node-box" id="dentist" onclick="selectNode('dentist', 'med_track')">Dentist (BDS)</span></li>
                <li><span class="node-box" id="allied" onclick="selectNode('allied', 'med_track')">Physio / Nursing / Pharma</span></li>
                <li><span class="node-box" id="vet" onclick="selectNode('vet', 'med_track')">Veterinary Doctor</span></li>
              </ul>
            </li>

            <li>
              <span class="node-box" id="eng_track" onclick="selectNode('eng_track', 'sci')">Engineering (PCM)</span>
              <ul>
                <li><span class="node-box" id="btech" onclick="selectNode('btech', 'eng_track')">B.Tech (CSE / Mech / Civil)</span></li>
                <li><span class="node-box" id="arch" onclick="selectNode('arch', 'eng_track')">Architecture</span></li>
                <li><span class="node-box" id="aviation" onclick="selectNode('aviation', 'eng_track')">Aviation / Merchant Navy</span></li>
                <li><span class="node-box" id="tech_new" onclick="selectNode('tech_new', 'eng_track')">Data Science / Game Dev</span></li>
              </ul>
            </li>

            <li>
              <span class="node-box" id="research_track" onclick="selectNode('research_track', 'sci')">Research & Innovation</span>
              <ul>
                <li><span class="node-box" id="scientist" onclick="selectNode('scientist', 'research_track')">Scientist / ISRO</span></li>
                <li><span class="node-box" id="robotics" onclick="selectNode('robotics', 'research_track')">AI & Robotics</span></li>
              </ul>
            </li>

            <li>
              <span class="node-box switch" id="sci_switch" onclick="selectNode('sci_switch', 'sci')">🔀 Switch from Science</span>
              <ul>
                <li><span class="node-box" id="sci_arts" onclick="selectNode('sci_arts', 'sci_switch')">B.A. (Psych/History)</span></li>
                <li><span class="node-box" id="sci_law" onclick="selectNode('sci_law', 'sci_switch')">Law (Integrated)</span></li>
                <li><span class="node-box" id="sci_mba" onclick="selectNode('sci_mba', 'sci_switch')">MBA (Business)</span></li>
                <li><span class="node-box" id="sci_upsc" onclick="selectNode('sci_upsc', 'sci_switch')">UPSC (IAS/IPS)</span></li>
              </ul>
            </li>
          </ul>
        </li>

        <li>
          <span class="node-box" id="comm" onclick="selectNode('comm', 'root')">📊 Commerce Stream</span>
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
              </ul>
            </li>
            <li>
              <span class="node-box switch" id="comm_switch" onclick="selectNode('comm_switch', 'comm')">🔀 Switch from Commerce</span>
              <ul>
                <li><span class="node-box" id="comm_arts" onclick="selectNode('comm_arts', 'comm_switch')">B.A. (Mass Comm/Psych)</span></li>
                <li><span class="node-box" id="comm_law" onclick="selectNode('comm_law', 'comm_switch')">Law (CLAT)</span></li>
                <li><span class="node-box" id="comm_teach" onclick="selectNode('comm_teach', 'comm_switch')">Teaching (B.Ed)</span></li>
              </ul>
            </li>
          </ul>
        </li>

        <li>
          <span class="node-box" id="arts" onclick="selectNode('arts', 'root')">🎨 Arts / Humanities</span>
          <ul>
            <li>
              <span class="node-box" id="govt_track" onclick="selectNode('govt_track', 'arts')">Govt / Law</span>
              <ul>
                <li><span class="node-box" id="ias" onclick="selectNode('ias', 'govt_track')">UPSC (IAS / IPS)</span></li>
                <li><span class="node-box" id="lawyer" onclick="selectNode('lawyer', 'govt_track')">Lawyer / Judge</span></li>
              </ul>
            </li>
            
            <li>
              <span class="node-box" id="teach_track" onclick="selectNode('teach_track', 'arts')">Teaching & Education</span>
              <ul>
                <li><span class="node-box" id="teacher" onclick="selectNode('teacher', 'teach_track')">School Teacher (B.Ed)</span></li>
                <li><span class="node-box" id="prof" onclick="selectNode('prof', 'teach_track')">Professor / Lecturer</span></li>
              </ul>
            </li>
            
            <li>
              <span class="node-box switch" id="arts_switch" onclick="selectNode('arts_switch', 'arts')">🔀 Switch from Arts</span>
              <ul>
                <li><span class="node-box" id="arts_mba" onclick="selectNode('arts_mba', 'arts_switch')">MBA (Business)</span></li>
                <li><span class="node-box" id="arts_hotel" onclick="selectNode('arts_hotel', 'arts_switch')">Hotel Management</span></li>
              </ul>
            </li>
          </ul>
        </li>

        <li>
          <span class="node-box" id="diploma" onclick="selectNode('diploma', 'root')">🛠️ Diploma (Skip +2)</span>
          <ul>
            <li><span class="node-box" id="tech_dip" onclick="selectNode('tech_dip', 'diploma')">Engineering Diploma</span></li>
            <li><span class="node-box" id="voc_dip" onclick="selectNode('voc_dip', 'diploma')">Hotel Mgmt / Fashion</span></li>
            <li>
              <span class="node-box switch" id="dip_switch" onclick="selectNode('dip_switch', 'diploma')">🔀 Switch to Degree</span>
              <ul>
                <li><span class="node-box" id="dip_btech" onclick="selectNode('dip_btech', 'dip_switch')">B.Tech (Lateral Entry)</span></li>
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
  <h3 id="panel-title" style="color:#0A2342; margin-top:0; font-size:1.5rem;">Title</h3>
  <div style="background:#f7fafc; padding:10px; border-radius:8px; margin:15px 0;">
    <p style="margin:5px 0;"><strong>🔑 Key Path/Exam:</strong> <span id="panel-good" style="color:#d69e2e; font-weight:bold;"></span></p>
  </div>
  <p id="panel-desc" style="font-size:1rem; color:#4a5568; line-height:1.6;">Desc</p>
  <a href="{{ '/book-expert/' | relative_url }}" class="btn" style="background:#0A2342; color:white; padding:12px 20px; display:block; text-align:center; text-decoration:none; border-radius:50px; margin-top:20px; font-weight:bold; box-shadow:0 4px 6px rgba(0,0,0,0.1);">📅 Book Expert Counsellor</a>
</div>

<script>
  // --- CAROUSEL LOGIC ---
  let slideIndex = 0;
  const slides = document.querySelectorAll(".quote-slide");
  
  function showSlides() {
    for (let i = 0; i < slides.length; i++) {
      slides[i].classList.remove("active");
    }
    slideIndex++;
    if (slideIndex > slides.length) {slideIndex = 1}
    slides[slideIndex-1].classList.add("active");
    setTimeout(showSlides, 4000); 
  }
  showSlides();

  // --- DATABASE ---
  const data = {
    "root": { title: "Class 10 Pass", good: "Choose wisely", desc: "10th doesn't decide your life — it only decides your next path. You have 4 major routes." },
    
    // --- SCIENCE ---
    "sci": { title: "Science Stream", good: "Maths/Science Aptitude", desc: "Subjects: Physics, Chem, Maths/Bio. Big Advantage: You can switch to Commerce/Arts later." },
    "sci_switch": { title: "Switching from Science", good: "Explore Options", desc: "60% of Science students eventually switch to Management, Law, or Arts." },
    "sci_arts": { title: "Switch to Arts", good: "CUET / Direct", desc: "Switch to Psychology, English Lit, or Sociology." },
    "sci_mba": { title: "MBA (Business)", good: "CAT / GMAT", desc: "Complete B.Tech/B.Sc, then write CAT. IIMs love engineers." },
    "sci_law": { title: "Law (Integrated)", good: "CLAT / AILET", desc: "5-Year B.Sc LLB or B.Tech LLB. Patent Law is huge." },
    "sci_upsc": { title: "UPSC (IAS/IPS)", good: "UPSC CSE", desc: "Science students often choose Maths/Physics as optional." },
    "med_track": { title: "Medical Line (PCB)", good: "NEET", desc: "Focus on PCB. Leads to Doctor, Dentist, or Allied Health." },
    "mbbs": { title: "MBBS (Doctor)", good: "NEET UG", desc: "Top medical degree. Treat patients, surgery, hospitals." },
    "dentist": { title: "Dentist (BDS)", good: "NEET UG", desc: "Dental surgery and care." },
    "allied": { title: "Allied Health", good: "CET / NEET", desc: "Nursing, Pharmacy, Physiotherapy. Very high demand." },
    "vet": { title: "Veterinary Doctor", good: "NEET UG", desc: "Treating animals." },
    "eng_track": { title: "Engineering Line (PCM)", good: "JEE / KCET", desc: "Focus on PCM. Leads to Technical careers." },
    "btech": { title: "B.Tech / B.E", good: "JEE Mains/Adv", desc: "Mechanical, Civil, ECE, CSE. Build things and software." },
    "arch": { title: "Architecture", good: "NATA", desc: "Design buildings." },
    "aviation": { title: "Aviation", good: "DGCA / NDA", desc: "Pilot or Merchant Navy." },
    "tech_new": { title: "New-Age Tech", good: "Portfolio / Skills", desc: "Data Science, Game Dev, AI." },
    "research_track": { title: "Research", good: "IISER / NEST", desc: "For scientists and inventors." },
    "scientist": { title: "Scientist", good: "GATE / NET", desc: "Space science, Physics research." },
    "robotics": { title: "Robotics", good: "JEE (Mechatronics)", desc: "Creating intelligent machines." },

    // --- COMMERCE ---
    "comm": { title: "Commerce Stream", good: "Numbers & Logic", desc: "High earning potential with less academic stress than Science." },
    "comm_switch": { title: "Switching from Commerce", good: "Explore Options", desc: "Commerce students make excellent Lawyers, Journalists, and Teachers." },
    "comm_arts": { title: "Switch to Arts", good: "CUET / Direct", desc: "Move into Journalism, Mass Comm, or Psychology." },
    "comm_law": { title: "Law", good: "CLAT", desc: "B.Com LLB is a very powerful degree for Corporate Law." },
    "comm_teach": { title: "Teaching", good: "B.Ed", desc: "Become a Commerce teacher for 11th/12th grade." },
    "fin_track": { title: "Finance & Accounts", good: "ICAI Exams", desc: "Core finance careers." },
    "ca": { title: "Chartered Accountant", good: "CA Foundation", desc: "Audit and Tax expert. Tough exam but high respect." },
    "cs": { title: "Company Secretary", good: "CSEET", desc: "Legal compliance for companies." },
    "bank_job": { title: "Banking", good: "IBPS PO / SBI PO", desc: "Investment banker, Stock trader, Bank PO." },
    "biz_track": { title: "Business", good: "CAT (Later)", desc: "Running companies and teams." },
    "mba": { title: "MBA", good: "CAT / GMAT", desc: "Master of Business Admin. CEO roles." },
    "digital": { title: "Digital Marketing", good: "Certifications", desc: "Social media, SEO, Ads." },

    // --- ARTS ---
    "arts": { title: "Arts / Humanities", good: "Creativity & Social", desc: "Underrated but powerful for Govt jobs and Creativity." },
    "arts_switch": { title: "Switching from Arts", good: "Explore Options", desc: "Yes! Arts students CAN do an MBA or Hotel Mgmt." },
    "arts_mba": { title: "MBA", good: "CAT / MAT", desc: "Marketing, HR, and Media Management are perfect for Arts grads." },
    "arts_hotel": { title: "Hotel Mgmt", good: "NCHMCT JEE", desc: "Top hotels hire based on communication skills." },
    "govt_track": { title: "Govt & Law", good: "UPSC / CLAT", desc: "Serving the nation or fighting for justice." },
    "ias": { title: "UPSC (IAS/IPS)", good: "UPSC CSE", desc: "Civil Services. Arts is the best base for this." },
    "lawyer": { title: "Lawyer", good: "CLAT", desc: "Legal practice. B.A LLB." },
    "teach_track": { title: "Teaching", good: "B.Ed", desc: "Patience & Knowledge sharing." },
    "teacher": { title: "School Teacher", good: "B.Ed / TET", desc: "Mentoring Kids. Stable job." },
    "prof": { title: "Professor", good: "NET / PhD", desc: "College level teaching." },

    // --- DIPLOMA ---
    "diploma": { title: "Diploma", good: "Hands-on Skills", desc: "Skip 11th/12th. 3-Year practical course." },
    "dip_switch": { title: "Switch to Degree", good: "Lateral Entry", desc: "Move from Diploma to Degree." },
    "dip_btech": { title: "B.Tech (Lateral)", good: "DCET / ECET", desc: "Join directly in 2nd Year of Engineering." },
    "tech_dip": { title: "Technical Diploma", good: "Polytechnic Exam", desc: "Mechanical, Civil, Electrical." },
    "voc_dip": { title: "Vocational", good: "Direct Admission", desc: "Hotel Management, Fashion." }
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
