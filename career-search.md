---
layout: default
title: "The Ultimate Career Roadmap: From Class 10 to Your Dream Job 🚀"
permalink: /career-search/
image: "https://images.unsplash.com/photo-1454165804606-c3d57bc86b40?w=1200&h=630&fit=crop"
description: "Confused after Class 10? Explore the complete interactive roadmap for Science, Commerce, Arts, and Teaching careers. Check exams, salaries, and real advice."
---

<style>
  /* 1. LAYOUT RESET */
  .main-content {
    max-width: 100% !important;
    padding: 0 !important;
    margin: 0 !important;
  }
  
  body { background-color: #f4f6f8; }

  /* 2. QUOTES CAROUSEL */
  .quote-container {
    background: #0A2342;
    color: #FFD700;
    padding: 20px;
    text-align: center;
    position: relative;
    overflow: hidden;
    height: 60px;
    display: flex;
    align-items: center;
    justify-content: center;
    border-bottom: 1px solid rgba(255,255,255,0.1);
  }

  .quote-slide {
    font-size: 1.1rem;
    font-style: italic;
    font-weight: 500;
    opacity: 0;
    position: absolute;
    transition: opacity 1s ease-in-out;
    width: 90%;
  }

  .quote-slide.active { opacity: 1; }

  /* 3. VERTICAL TREE CONTAINER */
  .tree-wrapper {
    max-width: 900px;
    margin: 0 auto;
    padding: 40px 20px 80px;
    font-family: 'Open Sans', sans-serif;
  }

  /* 4. TREE CSS */
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

  /* 5. NODE STYLING */
  .node-box {
    display: inline-block;
    padding: 8px 15px;
    border: 2px solid #ccc;
    background: white;
    border-radius: 4px;
    font-weight: 600;
    color: #0A2342;
    cursor: pointer;
    transition: all 0.2s;
    font-size: 0.95rem;
    position: relative;
    z-index: 2;
  }

  /* Special Style for Switch Nodes */
  .node-box.switch {
    border-color: #ff9800;
    color: #e65100;
    background: #fff3e0;
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

  /* 6. INFO PANEL */
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
    color: white !important;
    padding: 8px 20px;
    border-radius: 20px;
    text-decoration: none;
    font-weight: bold;
    z-index: 500;
    font-size: 0.9rem;
    box-shadow: 0 2px 5px rgba(0,0,0,0.3);
  }
</style>

<a href="{{ '/' | relative_url }}" class="back-btn">Back to Home</a>

<div style="text-align: center; padding: 100px 20px 40px; background: #0A2342;">
  <h1 style="margin:0; color: #ffffff !important; font-size: 2.5rem; text-shadow: 0 2px 4px rgba(0,0,0,0.5);">The Ultimate Career Roadmap 🚀</h1>
  <p style="color: #e0e0e0 !important; font-size: 1.2rem; margin-top: 10px;">Click any career box to see subjects, exams, and advice.</p>
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
  <div class="quote-slide">"Believe you can and you're halfway there." — Theodore Roosevelt</div>
  <div class="quote-slide">"The best way to predict the future is to create it." — Peter Drucker</div>
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
              <span class="node-box switch" id="sci_switch" onclick="selectNode('sci_switch', 'sci')">🔀 Switch from Science</span>
              <ul>
                <li><span class="node-box" id="sci_mba" onclick="selectNode('sci_mba', 'sci_switch')">MBA (Business)</span></li>
                <li><span class="node-box" id="sci_law" onclick="selectNode('sci_law', 'sci_switch')">Law (5-Year Integrated)</span></li>
                <li><span class="node-box" id="sci_design" onclick="selectNode('sci_design', 'sci_switch')">Design / Fashion</span></li>
                <li><span class="node-box" id="sci_upsc" onclick="selectNode('sci_upsc', 'sci_switch')">UPSC (IAS/IPS)</span></li>
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
              </ul>
            </li>
            <li>
              <span class="node-box switch" id="comm_switch" onclick="selectNode('comm_switch', 'comm')">🔀 Switch from Commerce</span>
              <ul>
                <li><span class="node-box" id="comm_law" onclick="selectNode('comm_law', 'comm_switch')">Law (CLAT)</span></li>
                <li><span class="node-box" id="comm_design" onclick="selectNode('comm_design', 'comm_switch')">Design (NIFT)</span></li>
                <li><span class="node-box" id="comm_teach" onclick="selectNode('comm_teach', 'comm_switch')">Teaching (B.Ed)</span></li>
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
              <span class="node-box" id="teach_track" onclick="selectNode('teach_track', 'arts')">Teaching & Education</span>
              <ul>
                <li><span class="node-box" id="teacher" onclick="selectNode('teacher', 'teach_track')">School Teacher (B.Ed)</span></li>
                <li><span class="node-box" id="special_ed" onclick="selectNode('special_ed', 'teach_track')">Special Educator</span></li>
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
          <span class="node-box" id="diploma" onclick="selectNode('diploma', 'root')">4. Diploma (Skip +2)</span>
          <ul>
            <li>
              <span class="node-box" id="tech_dip" onclick="selectNode('tech_dip', 'diploma')">Technical Diploma</span>
              <ul>
                <li><span class="node-box" id="mech_dip" onclick="selectNode('mech_dip', 'tech_dip')">Mech / Civil / Elec</span></li>
              </ul>
            </li>
            <li>
              <span class="node-box" id="voc_dip" onclick="selectNode('voc_dip', 'diploma')">Vocational</span>
              <ul>
                <li><span class="node-box" id="hotel" onclick="selectNode('hotel', 'voc_dip')">Hotel Management</span></li>
                <li><span class="node-box" id="fashion" onclick="selectNode('fashion', 'voc_dip')">Fashion / Animation</span></li>
              </ul>
            </li>
            <li>
              <span class="node-box switch" id="dip_switch" onclick="selectNode('dip_switch', 'diploma')">🔀 Switch from Diploma</span>
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
  <button onclick
