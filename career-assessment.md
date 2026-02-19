---
layout: default
title: "AI Career & Course Assessment 🎯"
permalink: /assessment/
description: "Comprehensive career analysis for Class 10, PUC, UG, and PG students. Discover the right courses and colleges based on your unique abilities."
---

<script src="https://cdnjs.cloudflare.com/ajax/libs/html2pdf.js/0.10.1/html2pdf.bundle.min.js"></script>

<style>
  body { background-color: #f4f7f6; font-family: 'Segoe UI', system-ui, sans-serif; color: #333; }
  
  .assessment-header {
    background: linear-gradient(135deg, #0A2342 0%, #1A5276 100%);
    color: white; padding: 60px 20px; text-align: center; border-radius: 0 0 20px 20px;
    margin-bottom: 40px; box-shadow: 0 4px 15px rgba(0,0,0,0.1);
  }
  .assessment-header h1 { margin: 0 0 10px 0; font-size: 2.5rem; font-weight: 800; }
  .assessment-header p { font-size: 1.1rem; color: #e0e0e0; max-width: 600px; margin: 0 auto; }

  .container { max-width: 900px; margin: 0 auto; padding: 0 20px; }

  /* FORM STYLES */
  .form-card {
    background: white; padding: 40px; border-radius: 12px;
    box-shadow: 0 10px 30px rgba(0,0,0,0.05); margin-bottom: 40px;
  }
  .form-group { margin-bottom: 25px; }
  .form-label { display: block; font-weight: 700; margin-bottom: 10px; color: #0A2342; font-size: 1.1rem; }
  
  .form-select, .form-input {
    width: 100%; padding: 15px; border: 2px solid #e0e6ed; border-radius: 8px;
    font-size: 1rem; color: #444; background: #fcfcfc; transition: all 0.3s;
  }
  .form-select:focus, .form-input:focus { border-color: #1A5276; outline: none; background: white; }

  .btn-submit {
    background: #e65100; color: white; border: none; padding: 15px 30px;
    font-size: 1.1rem; font-weight: bold; border-radius: 50px; cursor: pointer;
    width: 100%; transition: 0.3s; margin-top: 10px;
  }
  .btn-submit:hover { background: #bf360c; transform: translateY(-2px); box-shadow: 0 5px 15px rgba(230,81,0,0.3); }

  /* REPORT STYLES (This section gets converted to PDF) */
  #reportContainer { display: none; }
  
  .report-card {
    background: white; padding: 50px; border-radius: 12px;
    box-shadow: 0 10px 30px rgba(0,0,0,0.08); margin-bottom: 40px; border-top: 8px solid #0A2342;
  }
  .report-header { border-bottom: 2px solid #eee; padding-bottom: 20px; margin-bottom: 30px; }
  .report-header h2 { color: #0A2342; margin: 0 0 5px 0; }
  .report-meta { color: #777; font-size: 0.95rem; }

  .analysis-section { margin-bottom: 30px; }
  .analysis-section h3 { color: #1A5276; font-size: 1.3rem; margin-bottom: 15px; display: flex; align-items: center; gap: 10px;}
  .analysis-text { line-height: 1.7; color: #444; font-size: 1.05rem; background: #f8fafd; padding: 20px; border-radius: 8px; border-left: 4px solid #1A5276; }
  
  .why-not-text { border-left-color: #e74c3c; background: #fdf8f8; }

  .college-recs { display: grid; grid-template-columns: 1fr 1fr; gap: 20px; margin-top: 20px; }
  .rec-card { background: #fff; border: 1px solid #ddd; padding: 20px; border-radius: 8px; box-shadow: 0 4px 10px rgba(0,0,0,0.02); }
  .rec-card h4 { margin: 0 0 10px 0; color: #0A2342; }
  .rec-card p { margin: 0; color: #666; font-size: 0.9rem; }

  .actions { text-align: center; margin-top: 30px; }
  .btn-download {
    background: #0A2342; color: white; border: none; padding: 12px 25px;
    font-size: 1rem; font-weight: bold; border-radius: 50px; cursor: pointer; transition: 0.3s;
  }
  .btn-download:hover { background: #1A5276; }

  /* Print specific styles for PDF */
  @media print {
    body { background: white; }
    .actions, .assessment-header { display: none !important; }
    .report-card { box-shadow: none; border: none; padding: 0; }
  }
</style>

<div class="assessment-header">
  <h1>AI Career & Course Selector</h1>
  <p>Discover your ideal educational path through our comprehensive capability analysis.</p>
</div>

<div class="container">
  
  <div class="form-card" id="assessmentForm">
    <div class="form-group">
      <label class="form-label">Student Name</label>
      <input type="text" id="studentName" class="form-input" placeholder="Enter your full name">
    </div>

    <div class="form-group">
      <label class="form-label">Current Academic Level</label>
      <select id="academicLevel" class="form-select">
        <option value="Class 10">Class 10 (High School)</option>
        <option value="PUC">PUC / 11th-12th</option>
        <option value="UG">Undergraduate (Degree Student)</option>
        <option value="PG">Postgraduate / Master's</option>
      </select>
    </div>

    <div class="form-group">
      <label class="form-label">Primary Interest Area</label>
      <select id="interestArea" class="form-select">
        <option value="technology">Technology, Coding & Logic</option>
        <option value="design">Design, Architecture & Spatial Awareness</option>
        <option value="business">Business, Management & People</option>
        <option value="science">Pure Sciences & Research</option>
      </select>
    </div>

    <div class="form-group">
      <label class="form-label">Preferred Working Style</label>
      <select id="workStyle" class="form-select">
        <option value="hands-on">Hands-on / Practical Application</option>
        <option value="analytical">Analytical / Problem Solving</option>
        <option value="creative">Creative / Out-of-the-box Thinking</option>
      </select>
    </div>

    <button class="btn-submit" onclick="generateReport()">Analyze My Profile ➔</button>
  </div>

  <div id="reportContainer">
    <div class="report-card" id="reportContent">
      
      <div class="report-header">
        <h2>Comprehensive Career Analysis Report</h2>
        <div class="report-meta">
          Prepared for: <strong id="outName">Student</strong> | Level: <strong id="outLevel">Level</strong> | Date: <span id="outDate"></span>
        </div>
      </div>

      <div class="analysis-section">
        <h3>✅ Recommended Path: <span id="outCourse" style="color:#e65100; margin-left: 5px;">Course Name</span></h3>
        <div class="analysis-text" id="outWhyThis">
          </div>
      </div>

      <div class="analysis-section">
        <h3>⚠️ Paths to Reconsider (Why Not Other Options)</h3>
        <div class="analysis-text why-not-text" id="outWhyNot">
          </div>
      </div>

      <div class="analysis-section">
        <h3>🏛️ Top College Matches</h3>
        <p style="color: #666; margin-bottom: 15px;">Based on your profile, here are highly-rated institutions in our database that excel in your recommended field:</p>
        <div class="college-recs" id="outColleges">
          </div>
      </div>
      
      <div style="margin-top: 40px; text-align: center; border-top: 1px solid #eee; padding-top: 20px; font-size: 0.85rem; color: #888;">
        Report generated by The Knowledge Habitat Career Guidance System.
      </div>
    </div>

    <div class="actions">
      <button class="btn-download" onclick="downloadPDF()">📄 Download PDF Report</button>
      <button class="btn-download" style="background: white; color: #0A2342; border: 2px solid #0A2342; margin-left: 10px;" onclick="location.reload()">↺ Start Over</button>
    </div>
  </div>

</div>

<script>
  // 1. MOCK AI LOGIC DATABASE
  // In Phase 2, this data will be generated live by the Gemini AI API via your backend.
  const knowledgeBase = {
    "technology": {
      course: "B.Tech / B.E. in Computer Science or AI",
      whyThis: "Your strong inclination towards logic and analytical problem-solving makes engineering an excellent fit. You thrive in structured environments where you can build systems. A degree in Tech or AI will leverage your analytical mindset to solve complex real-world problems.",
      whyNot: "While you are analytical, a pure Science/Research track might feel too slow-paced for you. You prefer applying logic to create immediate, tangible tools (like software) rather than spending years proving theoretical concepts.",
      colleges: [
        { name: "IIT Roorkee", desc: "Top-tier institution for rigorous engineering and tech placements." },
        { name: "B.M.S. College of Engineering", desc: "Excellent tech programs and placement records in Bangalore." },
        { name: "RV College of Engineering", desc: "Highly reputed for Computer Science and innovation." }
      ]
    },
    "design": {
      course: "Bachelor of Architecture (B.Arch) / Interior Design",
      whyThis: "You possess a unique blend of spatial awareness and creativity. Architecture and Design will allow you to channel your out-of-the-box thinking into tangible, structural realities. This field satisfies your need for both aesthetics and functional application.",
      whyNot: "A standard corporate Management or pure Tech degree may stifle your creativity. Those fields often rely on rigid, pre-existing frameworks, whereas you need an environment that rewards visual and spatial innovation.",
      colleges: [
        { name: "Aditya Academy of Architecture (AAAD)", desc: "Specializes in B.Arch and Interior Design with great studio culture." },
        { name: "Gopalan School of Architecture (GSAP)", desc: "Focuses heavily on sustainable environments and project management." },
        { name: "East West School of Architecture (EWSA)", desc: "Dedicated campus for extensive 5-year B.Arch training." }
      ]
    },
    "business": {
      course: "BBA / MBA / Management Studies",
      whyThis: "Your profile indicates a strong affinity for people, systems, and communication. Management studies will train you to lead teams, optimize resources, and understand market dynamics. Your hands-on approach works perfectly for navigating business challenges.",
      whyNot: "A heavily technical or isolated research role would likely cause burnout. You draw energy from interaction and dynamic environments, making solitary coding or lab work unsuitable for your long-term growth.",
      colleges: [
        { name: "Christ (Deemed to be University)", desc: "Renowned globally for its rigorous Management and BBA/MBA programs." },
        { name: "Jain University", desc: "Strong focus on entrepreneurship and business incubation." },
        { name: "Mount Carmel College", desc: "Excellent commerce and management faculties with a holistic approach." }
      ]
    },
    "science": {
      course: "B.Sc (Research) / Basic Sciences",
      whyThis: "Your deep curiosity and analytical nature make you a natural fit for pure sciences. You are driven by understanding the 'why' behind phenomena. A track in fundamental sciences allows you to engage in long-term research and discovery.",
      whyNot: "Fast-paced corporate degrees (like BBA) or target-driven technical roles might frustrate you. You value deep, thorough understanding over quick, commercial fixes.",
      colleges: [
        { name: "Indian Institute of Science (IISc)", desc: "India's undisputed #1 institute for advanced scientific research." },
        { name: "St. Joseph's University", desc: "Heritage institution with highly respected basic science departments." },
        { name: "IIT Roorkee", desc: "Offers integrated M.Sc programs and advanced laboratories." }
      ]
    }
  };

  // 2. GENERATE REPORT FUNCTION
  function generateReport() {
    // Get user inputs
    const name = document.getElementById('studentName').value || "Student";
    const level = document.getElementById('academicLevel').value;
    const interest = document.getElementById('interestArea').value;
    
    // Fetch mock AI analysis based on interest
    const analysis = knowledgeBase[interest];

    // Populate Report Fields
    document.getElementById('outName').innerText = name;
    document.getElementById('outLevel').innerText = level;
    document.getElementById('outDate').innerText = new Date().toLocaleDateString();
    
    // Adjust course recommendation based on Academic Level
    let recommendedCourse = analysis.course;
    if (level === "PG" && interest === "technology") recommendedCourse = "M.Tech in AI / Data Science";
    if (level === "PG" && interest === "design") recommendedCourse = "M.Arch / Masters in Urban Planning";
    
    document.getElementById('outCourse').innerText = recommendedCourse;
    document.getElementById('outWhyThis').innerText = analysis.whyThis;
    document.getElementById('outWhyNot').innerText = analysis.whyNot;

    // Populate Colleges
    const collegeContainer = document.getElementById('outColleges');
    collegeContainer.innerHTML = ''; // Clear previous
    analysis.colleges.forEach(college => {
      collegeContainer.innerHTML += `
        <div class="rec-card">
          <h4>${college.name}</h4>
          <p>${college.desc}</p>
        </div>
      `;
    });

    // Hide Form, Show Report
    document.getElementById('assessmentForm').style.display = 'none';
    document.getElementById('reportContainer').style.display = 'block';
    
    // Scroll to top of report
    window.scrollTo({ top: 0, behavior: 'smooth' });
  }

  // 3. PDF GENERATION FUNCTION
  function downloadPDF() {
    const element = document.getElementById('reportContent');
    const name = document.getElementById('outName').innerText.replace(/\s+/g, '_');
    
    const opt = {
      margin:       0.5,
      filename:     `Career_Analysis_${name}.pdf`,
      image:        { type: 'jpeg', quality: 0.98 },
      html2canvas:  { scale: 2, useCORS: true },
      jsPDF:        { unit: 'in', format: 'a4', orientation: 'portrait' }
    };

    // New Promise-based usage of html2pdf
    html2pdf().set(opt).from(element).save();
  }
</script>
