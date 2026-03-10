---
layout: default
title: "NITTE University Course Portal 🎓"
permalink: /colleges/nitte/
image: "https://nitte.edu.in/img/nitte-university-mangalore.jpg"
description: "Browse all UG, PG, Diploma, Fellowship, and PhD programs at NITTE University across Mangaluru, Bengaluru, and Nitte campuses."
---

<meta property="og:title" content="NITTE University Course Portal 🎓">
<meta property="og:description" content="Access details for Engineering, Medicine, Management, and Sciences at NITTE. Check eligibility and specializations.">
<meta property="og:image" content="https://nitte.edu.in/img/nitte-university-mangalore.jpg">

<style>
  /* --- 1. LAYOUT & RESET --- */
  .main-content { max-width: 100% !important; padding: 0 !important; margin: 0 !important; }
  *, *::before, *::after { box-sizing: border-box; }
  html, body { max-width: 100vw; overflow-x: hidden; }
  body { background-color: #F4F7FB; font-family: 'Nunito', sans-serif; color: #0F172A; margin: 0; }
  p, h1, h2, h3, span { word-wrap: break-word; overflow-wrap: break-word; }

  /* --- 2. HERO SECTION --- */
  .nitte-hero {
    background: linear-gradient(rgba(15, 23, 42, 0.85), rgba(30, 58, 138, 0.9)), url('https://nitte.edu.in/img/nitte-university-mangalore.jpg');
    background-size: cover;
    background-position: center;
    color: white;
    text-align: center;
    padding: 80px 20px;
    margin-bottom: 0;
  }
  .nitte-hero h1 { font-family: 'Outfit', sans-serif; font-size: 3.2rem; margin: 0; font-weight: 900; color: #fff !important; letter-spacing: -1px;}
  .nitte-hero p { font-size: 1.15rem; color: #e2e8f0 !important; margin-top: 15px; max-width: 800px; margin-left: auto; margin-right: auto; line-height: 1.6; font-weight: 600;}

  /* --- 3. APP CONTAINER & SIDEBAR --- */
  .app-container {
    max-width: 1400px;
    margin: 0 auto;
    display: flex;
    gap: 30px;
    padding: 40px 20px;
    align-items: flex-start;
  }

  .filters-sidebar {
    width: 300px;
    background: white;
    padding: 30px 25px;
    border-radius: 16px;
    box-shadow: 0 10px 30px rgba(0,0,0,0.03);
    position: sticky;
    top: 90px;
    border-top: 5px solid #1E3A8A; /* NITTE Deep Blue */
    flex-shrink: 0;
  }

  .filter-group { margin-bottom: 25px; }
  .filter-label { display: block; font-weight: 800; margin-bottom: 8px; color: #1E3A8A; font-size: 0.85rem; text-transform: uppercase; letter-spacing: 0.5px; font-family: 'Outfit', sans-serif;}
  
  .filter-input, .filter-select {
    width: 100%;
    padding: 14px 15px;
    border: 2px solid #E2E8F0;
    border-radius: 10px;
    font-size: 0.95rem;
    font-weight: 600;
    color: #334155;
    outline: none;
    transition: all 0.3s ease;
    background: #F8FAFC;
    font-family: 'Nunito', sans-serif;
  }
  .filter-input:focus, .filter-select:focus { border-color: #1E3A8A; background: white; box-shadow: 0 0 0 4px rgba(30, 58, 138, 0.1);}

  /* --- 4. COURSE GRID --- */
  .results-area { flex-grow: 1; min-width: 0;}
  
  .course-grid {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(320px, 1fr));
    gap: 25px;
  }

  .course-card {
    background: white;
    border-radius: 16px;
    padding: 25px;
    border-left: 6px solid #ddd;
    box-shadow: 0 4px 15px rgba(0,0,0,0.02);
    transition: transform 0.3s ease, box-shadow 0.3s ease;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    min-width: 0;
  }
  .course-card:hover { transform: translateY(-5px); box-shadow: 0 15px 35px rgba(0,0,0,0.06); }

  /* Dynamic Level Colors */
  .level-UG { border-left-color: #3B82F6; }
  .level-PG { border-left-color: #8B5CF6; }
  .level-PhD { border-left-color: #EF4444; }
  .level-Diploma { border-left-color: #F59E0B; }
  .level-Fellowship { border-left-color: #10B981; }
  .level-Certificate { border-left-color: #64748B; }

  .c-dept { font-size: 0.75rem; text-transform: uppercase; font-weight: 800; color: #64748B; margin-bottom: 8px; letter-spacing: 0.5px;}
  .c-title { font-family: 'Outfit', sans-serif; font-size: 1.25rem; font-weight: 800; color: #0F172A; margin: 0 0 15px 0; line-height: 1.3; }
  
  .c-meta { display: flex; gap: 8px; flex-wrap: wrap; margin-bottom: 15px; }
  .c-badge { display: inline-flex; align-items: center; gap: 5px; background: #EEF2FF; padding: 6px 12px; border-radius: 8px; font-size: 0.8rem; font-weight: 800; color: #4338CA;}
  .c-badge-loc { display: inline-flex; align-items: center; gap: 5px; background: #FFFBEB; padding: 6px 12px; border-radius: 8px; font-size: 0.8rem; font-weight: 800; color: #B45309;}
  
  .c-inst { font-size: 0.9rem; color: #475569; font-weight: 600; margin: 0 0 20px 0; display: flex; align-items: flex-start; gap: 8px; line-height: 1.4;}
  
  .c-footer { margin-top: auto; border-top: 1px solid #F1F5F9; padding-top: 20px; }
  
  .view-btn {
    display: block; width: 100%; text-align: center;
    background: #F8FAFC; border: 2px solid #E2E8F0; color: #1E3A8A;
    padding: 12px 20px; border-radius: 12px; font-size: 0.95rem; font-weight: 800; cursor: pointer; transition: 0.3s;
    text-decoration: none; font-family: 'Outfit', sans-serif;
  }
  .view-btn:hover { background: #1E3A8A; color: white; border-color: #1E3A8A; box-shadow: 0 4px 15px rgba(30, 58, 138, 0.2);}

  /* Mobile */
  @media (max-width: 900px) {
    .app-container { flex-direction: column; padding: 30px 15px;}
    .filters-sidebar { width: 100%; position: static; padding: 20px;}
    .nitte-hero h1 { font-size: 2.2rem; }
  }
</style>

<div class="nitte-hero">
  <h1>NITTE University Portal</h1>
  <p>Explore all elite Undergraduate, Postgraduate, Fellowship, and Doctoral programs across our Mangaluru, Bengaluru, and Nitte campuses.</p>
</div>

<div class="app-container">

  <aside class="filters-sidebar">
    <div class="filter-group">
      <label class="filter-label">🔍 Search Course</label>
      <input type="text" id="searchInput" class="filter-input" placeholder="e.g. Artificial Intelligence, MBBS..." onkeyup="renderCourses()">
    </div>

    <div class="filter-group">
      <label class="filter-label">📍 Campus Location</label>
      <select id="campusFilter" class="filter-select" onchange="renderCourses()">
        <option value="All">All Campuses</option>
        <option value="Mangaluru">Mangaluru</option>
        <option value="Bengaluru">Bengaluru</option>
        <option value="Nitte">Nitte</option>
      </select>
    </div>
    
    <div class="filter-group">
      <label class="filter-label">🎓 Academic Level</label>
      <select id="levelFilter" class="filter-select" onchange="renderCourses()">
        <option value="All">All Levels</option>
        <option value="UG">Undergraduate (UG)</option>
        <option value="PG">Postgraduate (PG)</option>
        <option value="PhD">Doctoral (PhD)</option>
        <option value="Diploma">Diploma / Post Basic</option>
        <option value="Fellowship">Fellowship</option>
        <option value="Certificate">Certificate Courses</option>
      </select>
    </div>

    <div class="filter-group" style="margin-bottom:0;">
      <label class="filter-label">🏫 Faculty / Domain</label>
      <select id="deptFilter" class="filter-select" onchange="renderCourses()">
        <option value="All">All Faculties</option>
        <option value="Engineering">Engineering & Tech</option>
        <option value="Medicine">Medicine & Surgery</option>
        <option value="Dentistry">Dentistry</option>
        <option value="Allied">Allied Health Sciences</option>
        <option value="Nursing">Nursing</option>
        <option value="Pharmacy">Pharmacy</option>
        <option value="Physiotherapy">Physiotherapy</option>
        <option value="BioScience">Biological Sciences</option>
        <option value="Commerce">Commerce & Management</option>
        <option value="Architecture">Architecture & Design</option>
        <option value="Hospitality">Hospitality & Aviation</option>
        <option value="Audiology">Speech & Hearing</option>
        <option value="Communication">Media & Communication</option>
      </select>
    </div>

    <div style="margin-top:25px; font-size:0.9rem; color:#64748b; font-weight: 700; text-align:center; padding-top:15px; border-top: 1px dashed #cbd5e1;">
      Showing <span id="countDisplay" style="color: #1E3A8A; font-size:1.1rem; font-weight:900;">0</span> active programs
    </div>
  </aside>

  <div class="results-area">
    <div id="courseGrid" class="course-grid">
      </div>
  </div>

</div>

<script>
  // --- 1. MASSIVE NITTE COURSE DATABASE ---
  const courses = [
    // --- ENGINEERING (UG) ---
    { name: "BTech Artificial Intelligence & Data Science", campus: "Nitte", dept: "Engineering", level: "UG", dur: "4 Years", link: "https://nitte.edu.in/nmamit/department-AI&DS.php", inst: "NMAM Institute of Technology" },
    { name: "BTech Computer Science (Cyber Security)", campus: "Nitte", dept: "Engineering", level: "UG", dur: "4 Years", link: "https://nitte.edu.in/nmamit/department-CyberSecurity.php", inst: "NMAM Institute of Technology" },
    { name: "BTech Electronics (VLSI Design & Technology)", campus: "Nitte", dept: "Engineering", level: "UG", dur: "4 Years", link: "https://nitte.edu.in/nmamit/department-VLSI.php", inst: "NMAM Institute of Technology" },
    { name: "BTech Electronics & Communication (ACT)", campus: "Nitte", dept: "Engineering", level: "UG", dur: "4 Years", link: "https://nitte.edu.in/nmamit/department-Communication.php", inst: "NMAM Institute of Technology" },
    { name: "BTech Artificial Intelligence & Machine Learning", campus: "Nitte", dept: "Engineering", level: "UG", dur: "4 Years", link: "https://nitte.edu.in/nmamit/department-AI&ML.php", inst: "NMAM Institute of Technology" },
    { name: "BTech Biotechnology", campus: "Nitte", dept: "Engineering", level: "UG", dur: "4 Years", link: "https://nitte.edu.in/nmamit/department-biotechnology.php", inst: "NMAM Institute of Technology" },
    { name: "BTech Civil Engineering", campus: "Nitte", dept: "Engineering", level: "UG", dur: "4 Years", link: "https://nitte.edu.in/nmamit/department-civil.php", inst: "NMAM Institute of Technology" },
    { name: "BTech Computer & Communication Engineering", campus: "Nitte", dept: "Engineering", level: "UG", dur: "4 Years", link: "https://nitte.edu.in/nmamit/department-CCE.php", inst: "NMAM Institute of Technology" },
    { name: "BTech Computer Science", campus: "Nitte", dept: "Engineering", level: "UG", dur: "4 Years", link: "https://nitte.edu.in/nmamit/department-computer-science.php", inst: "NMAM Institute of Technology" },
    { name: "BTech Electrical & Electronics", campus: "Nitte", dept: "Engineering", level: "UG", dur: "4 Years", link: "https://nitte.edu.in/nmamit/department-electrical-electronics.php", inst: "NMAM Institute of Technology" },
    { name: "BTech Electronics & Communication", campus: "Nitte", dept: "Engineering", level: "UG", dur: "4 Years", link: "https://nitte.edu.in/nmamit/department-electronics-communication.php", inst: "NMAM Institute of Technology" },
    { name: "BTech Information Science", campus: "Nitte", dept: "Engineering", level: "UG", dur: "4 Years", link: "https://nitte.edu.in/nmamit/department-information-science.php", inst: "NMAM Institute of Technology" },
    { name: "BTech Robotics & Artificial Intelligence", campus: "Nitte", dept: "Engineering", level: "UG", dur: "4 Years", link: "https://nitte.edu.in/nmamit/department-robotics.php", inst: "NMAM Institute of Technology" },
    { name: "BTech Mechanical Engineering", campus: "Nitte", dept: "Engineering", level: "UG", dur: "4 Years", link: "https://nitte.edu.in/nmamit/department-mechanical.php", inst: "NMAM Institute of Technology" },
    { name: "BTech International Dual Degree Program", campus: "Nitte", dept: "Engineering", level: "UG", dur: "4 Years", link: "https://nitte.edu.in/nmamit/DualDegree.php", inst: "NMAM Institute of Technology" },
    
    { name: "BTech Artificial Intelligence & Data Science", campus: "Bengaluru", dept: "Engineering", level: "UG", dur: "4 Years", link: "https://nitte.edu.in/nmit/btech-in-artificialintelligence-and-datascience.php", inst: "Nitte Meenakshi Institute of Technology" },
    { name: "BTech Aeronautical", campus: "Bengaluru", dept: "Engineering", level: "UG", dur: "4 Years", link: "https://nitte.edu.in/nmit/btech-aeronautical-engineering.php", inst: "Nitte Meenakshi Institute of Technology" },
    { name: "BTech Artificial Intelligence & Machine Learning", campus: "Bengaluru", dept: "Engineering", level: "UG", dur: "4 Years", link: "https://nitte.edu.in/nmit/btech-in-artificialintelligence-and-machinelearning.php", inst: "Nitte Meenakshi Institute of Technology" },
    { name: "BTech Robotics & Artificial Intelligence", campus: "Bengaluru", dept: "Engineering", level: "UG", dur: "4 Years", link: "https://nitte.edu.in/nmit/btech-robotics-and-artificial-intelligence.php", inst: "Nitte Meenakshi Institute of Technology" },
    { name: "BTech Civil Engineering", campus: "Bengaluru", dept: "Engineering", level: "UG", dur: "4 Years", link: "https://nitte.edu.in/nmit/btech-civil-engineering.php", inst: "Nitte Meenakshi Institute of Technology" },
    { name: "BTech Computer Science & Business Systems", campus: "Bengaluru", dept: "Engineering", level: "UG", dur: "4 Years", link: "https://nitte.edu.in/nmit/btech-computer-science-and-business-systems.php", inst: "Nitte Meenakshi Institute of Technology" },
    { name: "BTech Computer Science Engineering", campus: "Bengaluru", dept: "Engineering", level: "UG", dur: "4 Years", link: "https://nitte.edu.in/nmit/btech-computer-science-engineering.php", inst: "Nitte Meenakshi Institute of Technology" },
    { name: "BTech Electrical & Electronics", campus: "Bengaluru", dept: "Engineering", level: "UG", dur: "4 Years", link: "https://nitte.edu.in/nmit/btech-electrical-and-electronics-engineering.php", inst: "Nitte Meenakshi Institute of Technology" },
    { name: "BTech Electronics & Communication", campus: "Bengaluru", dept: "Engineering", level: "UG", dur: "4 Years", link: "https://nitte.edu.in/nmit/btech-electronics-and-communication-engineering.php", inst: "Nitte Meenakshi Institute of Technology" },
    { name: "BTech Electronics (VLSI Design)", campus: "Bengaluru", dept: "Engineering", level: "UG", dur: "4 Years", link: "https://nitte.edu.in/nmit/btech-in-electronics-engineering-vlsi.php", inst: "Nitte Meenakshi Institute of Technology" },
    { name: "BTech Information Science", campus: "Bengaluru", dept: "Engineering", level: "UG", dur: "4 Years", link: "https://nitte.edu.in/nmit/btech-information-science-and-engineering.php", inst: "Nitte Meenakshi Institute of Technology" },
    { name: "BTech Mechanical Engineering", campus: "Bengaluru", dept: "Engineering", level: "UG", dur: "4 Years", link: "https://nitte.edu.in/nmit/btech-mechanical-engineering.php", inst: "Nitte Meenakshi Institute of Technology" },

    // --- ENGINEERING (PG) ---
    { name: "MTech Computer Science & Engineering", campus: "Nitte", dept: "Engineering", level: "PG", dur: "2 Years", link: "https://nitte.edu.in/nmamit/department-computer-science.php#program", inst: "NMAM Institute of Technology" },
    { name: "MTech Cyber Security", campus: "Nitte", dept: "Engineering", level: "PG", dur: "2 Years", link: "https://nitte.edu.in/nmamit/department-computer-science.php#program", inst: "NMAM Institute of Technology" },
    { name: "MTech Structural Engineering", campus: "Nitte", dept: "Engineering", level: "PG", dur: "2 Years", link: "https://nitte.edu.in/nmamit/department-civil.php#program", inst: "NMAM Institute of Technology" },
    { name: "MTech VLSI Design & Embedded Systems", campus: "Nitte", dept: "Engineering", level: "PG", dur: "2 Years", link: "https://nitte.edu.in/nmamit/department-electronics-communication.php#program", inst: "NMAM Institute of Technology" },
    { name: "MTech Mechatronics", campus: "Nitte", dept: "Engineering", level: "PG", dur: "2 Years", link: "https://nitte.edu.in/nmamit/MTech-Mechatronics.php", inst: "NMAM Institute of Technology" },
    { name: "MCA (Master of Computer Applications)", campus: "Nitte", dept: "Engineering", level: "PG", dur: "2 Years", link: "https://nitte.edu.in/nmamit/department-mca.php", inst: "NMAM Institute of Technology" },
    { name: "MTech Defence Technology", campus: "Bengaluru", dept: "Engineering", level: "PG", dur: "2 Years", link: "https://nitte.edu.in/nmit/mtech-in-defence-technology.php", inst: "Nitte Meenakshi Institute of Technology" },
    { name: "MTech Robotics and Artificial Intelligence", campus: "Bengaluru", dept: "Engineering", level: "PG", dur: "2 Years", link: "https://nitte.edu.in/nmit/mtech-in-robotics-ai.php", inst: "Nitte Meenakshi Institute of Technology" },
    { name: "MTech Structural Engineering", campus: "Bengaluru", dept: "Engineering", level: "PG", dur: "2 Years", link: "https://nitte.edu.in/nmit/mtech-in-structural-engineering.php", inst: "Nitte Meenakshi Institute of Technology" },
    { name: "MTech Electric Vehicle Technology", campus: "Bengaluru", dept: "Engineering", level: "PG", dur: "2 Years", link: "https://nitte.edu.in/nmit/mtech-in-electric-vehicle-technology.php", inst: "Nitte Meenakshi Institute of Technology" },
    { name: "MCA (Master of Computer Applications)", campus: "Bengaluru", dept: "Engineering", level: "PG", dur: "2 Years", link: "https://nitte.edu.in/nmit/MCA.php", inst: "Nitte Meenakshi Institute of Technology" },

    // --- MEDICINE (KSHEMA) UG & PG ---
    { name: "MBBS (Bachelor of Medicine & Surgery)", campus: "Mangaluru", dept: "Medicine", level: "UG", dur: "5.5 Years", link: "https://nitte.edu.in/kshema/admission-mbbs.php", inst: "K S Hegde Medical Academy" },
    { name: "MD Anatomy", campus: "Mangaluru", dept: "Medicine", level: "PG", dur: "3 Years", link: "https://nitte.edu.in/kshema/admission-md-anatomy.php", inst: "K S Hegde Medical Academy" },
    { name: "MD Anesthesiology", campus: "Mangaluru", dept: "Medicine", level: "PG", dur: "3 Years", link: "https://nitte.edu.in/kshema/admission-md-anesthesiology.php", inst: "K S Hegde Medical Academy" },
    { name: "MD Biochemistry", campus: "Mangaluru", dept: "Medicine", level: "PG", dur: "3 Years", link: "https://nitte.edu.in/kshema/admission-md-biochemistry.php", inst: "K S Hegde Medical Academy" },
    { name: "MD Community Medicine", campus: "Mangaluru", dept: "Medicine", level: "PG", dur: "3 Years", link: "https://nitte.edu.in/kshema/admission-md-community-medicine.php", inst: "K S Hegde Medical Academy" },
    { name: "MD Dermatology", campus: "Mangaluru", dept: "Medicine", level: "PG", dur: "3 Years", link: "https://nitte.edu.in/kshema/admission-dermatology-venereology.php", inst: "K S Hegde Medical Academy" },
    { name: "MD Forensic Medicine", campus: "Mangaluru", dept: "Medicine", level: "PG", dur: "3 Years", link: "https://nitte.edu.in/kshema/admission-md-forensic-medicine.php", inst: "K S Hegde Medical Academy" },
    { name: "MD General Medicine", campus: "Mangaluru", dept: "Medicine", level: "PG", dur: "3 Years", link: "https://nitte.edu.in/kshema/admission-md-general-medicine.php", inst: "K S Hegde Medical Academy" },
    { name: "MD Microbiology", campus: "Mangaluru", dept: "Medicine", level: "PG", dur: "3 Years", link: "https://nitte.edu.in/kshema/admission-md-microbiology.php", inst: "K S Hegde Medical Academy" },
    { name: "MD Paediatrics", campus: "Mangaluru", dept: "Medicine", level: "PG", dur: "3 Years", link: "https://nitte.edu.in/kshema/admission-md-paediatrics.php", inst: "K S Hegde Medical Academy" },
    { name: "MD Pathology", campus: "Mangaluru", dept: "Medicine", level: "PG", dur: "3 Years", link: "https://nitte.edu.in/kshema/admission-md-pathology.php", inst: "K S Hegde Medical Academy" },
    { name: "MD Pharmacology", campus: "Mangaluru", dept: "Medicine", level: "PG", dur: "3 Years", link: "https://nitte.edu.in/kshema/admission-md-pharmacology.php", inst: "K S Hegde Medical Academy" },
    { name: "MD Physiology", campus: "Mangaluru", dept: "Medicine", level: "PG", dur: "3 Years", link: "https://nitte.edu.in/kshema/admission-md-physiology.php", inst: "K S Hegde Medical Academy" },
    { name: "MD Psychiatry", campus: "Mangaluru", dept: "Medicine", level: "PG", dur: "3 Years", link: "https://nitte.edu.in/kshema/admission-md-psychiatry.php", inst: "K S Hegde Medical Academy" },
    { name: "MD Pulmonary Medicine", campus: "Mangaluru", dept: "Medicine", level: "PG", dur: "3 Years", link: "https://nitte.edu.in/kshema/admission-md-pulmonary-medicine.php", inst: "K S Hegde Medical Academy" },
    { name: "MD Radiodiagnosis", campus: "Mangaluru", dept: "Medicine", level: "PG", dur: "3 Years", link: "https://nitte.edu.in/kshema/admission-md-radiodiagnosis.php", inst: "K S Hegde Medical Academy" },
    { name: "MS General Surgery", campus: "Mangaluru", dept: "Medicine", level: "PG", dur: "3 Years", link: "https://nitte.edu.in/kshema/admission-ms-general-surgery.php", inst: "K S Hegde Medical Academy" },
    { name: "MS Obstetrics & Gynaecology", campus: "Mangaluru", dept: "Medicine", level: "PG", dur: "3 Years", link: "https://nitte.edu.in/kshema/admission-ms-obstetrics-gynaecology.php", inst: "K S Hegde Medical Academy" },
    { name: "MS Ophthalmology", campus: "Mangaluru", dept: "Medicine", level: "PG", dur: "3 Years", link: "https://nitte.edu.in/kshema/admission-ms-opthalmology.php", inst: "K S Hegde Medical Academy" },
    { name: "MS Orthopaedics", campus: "Mangaluru", dept: "Medicine", level: "PG", dur: "3 Years", link: "https://nitte.edu.in/kshema/admission-ms-orthopaedics.php", inst: "K S Hegde Medical Academy" },
    { name: "MS Otorhinolaryngology (ENT)", campus: "Mangaluru", dept: "Medicine", level: "PG", dur: "3 Years", link: "https://nitte.edu.in/kshema/admission-ms-otorhinolaryngology.php", inst: "K S Hegde Medical Academy" },
    { name: "MCh Urology", campus: "Mangaluru", dept: "Medicine", level: "PG", dur: "3 Years", link: "https://nitte.edu.in/kshema/admission-mch.php", inst: "K S Hegde Medical Academy" },
    { name: "Fellowship in Interventional Pulmonology", campus: "Mangaluru", dept: "Medicine", level: "Fellowship", dur: "1 Year", link: "https://nitte.edu.in/kshema/", inst: "K S Hegde Medical Academy" },
    { name: "Fellowship in Neuroimmunology", campus: "Mangaluru", dept: "Medicine", level: "Fellowship", dur: "1 Year", link: "https://nitte.edu.in/kshema/neuroimmunology.php", inst: "K S Hegde Medical Academy" },
    { name: "Care of Critically Ill Surgical Patients (CCrISP)", campus: "Mangaluru", dept: "Medicine", level: "Certificate", dur: "Short Term", link: "https://nitte.edu.in/admissions.php", inst: "K S Hegde Medical Academy" },

    // --- DENTISTRY (ABSMIDS) ---
    { name: "BDS (Bachelor of Dental Surgery)", campus: "Mangaluru", dept: "Dentistry", level: "UG", dur: "5 Years", link: "https://nitte.edu.in/absmids/admission-bds.php", inst: "A B Shetty Memorial Institute of Dental Sciences" },
    { name: "MDS Oral & Maxillofacial Pathology", campus: "Mangaluru", dept: "Dentistry", level: "PG", dur: "3 Years", link: "https://nitte.edu.in/absmids/admission-mds-maxillofacial-pathology-microbiology.php", inst: "A B Shetty Memorial Institute of Dental Sciences" },
    { name: "MDS Conservative Dentistry & Endodontics", campus: "Mangaluru", dept: "Dentistry", level: "PG", dur: "3 Years", link: "https://nitte.edu.in/absmids/admission-mds-conservative-dentistry-endodontics.php", inst: "A B Shetty Memorial Institute of Dental Sciences" },
    { name: "MDS Oral & Maxillofacial Surgery", campus: "Mangaluru", dept: "Dentistry", level: "PG", dur: "3 Years", link: "https://nitte.edu.in/absmids/admission-mds-oral-maxillofacial-surgery.php", inst: "A B Shetty Memorial Institute of Dental Sciences" },
    { name: "MDS Oral Medicine & Radiology", campus: "Mangaluru", dept: "Dentistry", level: "PG", dur: "3 Years", link: "https://nitte.edu.in/absmids/admission-mds-oral-medicine-radiology.php", inst: "A B Shetty Memorial Institute of Dental Sciences" },
    { name: "MDS Orthodontics & Dentofacial Ortho", campus: "Mangaluru", dept: "Dentistry", level: "PG", dur: "3 Years", link: "https://nitte.edu.in/absmids/admission-mds-orthodontics-dentofacial-orthopaedics.php", inst: "A B Shetty Memorial Institute of Dental Sciences" },
    { name: "MDS Paediatric & Preventive Dentistry", campus: "Mangaluru", dept: "Dentistry", level: "PG", dur: "3 Years", link: "https://nitte.edu.in/absmids/admission-mds-paediatric-preventive-dentistry.php", inst: "A B Shetty Memorial Institute of Dental Sciences" },
    { name: "MDS Periodontology", campus: "Mangaluru", dept: "Dentistry", level: "PG", dur: "3 Years", link: "https://nitte.edu.in/absmids/admission-mds-periodontology.php", inst: "A B Shetty Memorial Institute of Dental Sciences" },
    { name: "MDS Prosthodontics & Crown & Bridge", campus: "Mangaluru", dept: "Dentistry", level: "PG", dur: "3 Years", link: "https://nitte.edu.in/absmids/admission-mds-prosthodontics-crown-bridge.php", inst: "A B Shetty Memorial Institute of Dental Sciences" },
    { name: "Fellowship in Oral Implantology", campus: "Mangaluru", dept: "Dentistry", level: "Fellowship", dur: "1 Year", link: "https://nitte.edu.in/admissions.php", inst: "A B Shetty Memorial Institute of Dental Sciences" },

    // --- ALLIED HEALTH SCIENCES (NIAHS) ---
    { name: "BSc Medical Radiology & Imaging Tech", campus: "Mangaluru", dept: "Allied", level: "UG", dur: "4 Years", link: "https://nitte.edu.in/niahs/admission-bsc-mit.php", inst: "Nitte Institute of Allied Health Sciences" },
    { name: "BSc Anaesthesia & Operation Theatre Tech", campus: "Mangaluru", dept: "Allied", level: "UG", dur: "4 Years", link: "https://nitte.edu.in/niahs/admission-bsc-OT.php", inst: "Nitte Institute of Allied Health Sciences" },
    { name: "BSc Medical Laboratory Science", campus: "Mangaluru", dept: "Allied", level: "UG", dur: "4 Years", link: "https://nitte.edu.in/niahs/admission-bsc-mlt.php", inst: "Nitte Institute of Allied Health Sciences" },
    { name: "BSc Respiratory Technology", campus: "Mangaluru", dept: "Allied", level: "UG", dur: "4 Years", link: "https://nitte.edu.in/niahs/admission-bsc-rt.php", inst: "Nitte Institute of Allied Health Sciences" },
    { name: "BSc Radiation Therapy Technology", campus: "Mangaluru", dept: "Allied", level: "UG", dur: "4 Years", link: "https://nitte.edu.in/niahs/admission-bsc-rtt.php", inst: "Nitte Institute of Allied Health Sciences" },
    { name: "BSc Dialysis Therapy Technology", campus: "Mangaluru", dept: "Allied", level: "UG", dur: "4 Years", link: "https://nitte.edu.in/niahs/admission-bsc-rdt.php", inst: "Nitte Institute of Allied Health Sciences" },
    { name: "Master in Medical Radiology & Imaging", campus: "Mangaluru", dept: "Allied", level: "PG", dur: "2 Years", link: "https://nitte.edu.in/niahs/admission-msc-mit.php", inst: "Nitte Institute of Allied Health Sciences" },
    { name: "Master in Anaesthesia & OT Tech", campus: "Mangaluru", dept: "Allied", level: "PG", dur: "2 Years", link: "https://nitte.edu.in/niahs/admission-A&OTT.php", inst: "Nitte Institute of Allied Health Sciences" },
    { name: "Master of Medical Laboratory Science", campus: "Mangaluru", dept: "Allied", level: "PG", dur: "2 Years", link: "https://nitte.edu.in/niahs/admission-msc-mlt.php", inst: "Nitte Institute of Allied Health Sciences" },
    { name: "Master of Respiratory Technology", campus: "Mangaluru", dept: "Allied", level: "PG", dur: "2 Years", link: "https://nitte.edu.in/niahs/admission-msc-rt.php", inst: "Nitte Institute of Allied Health Sciences" },
    { name: "MSc Clinical Embryology", campus: "Mangaluru", dept: "Allied", level: "PG", dur: "2 Years", link: "https://nitte.edu.in/niahs/admission-msc-clinicalembryology.php", inst: "Nitte Institute of Allied Health Sciences" },
    { name: "MPH (Public Health)", campus: "Mangaluru", dept: "Allied", level: "PG", dur: "2 Years", link: "https://nitte.edu.in/niahs/admission-mph.php", inst: "Nitte Institute of Allied Health Sciences" },
    { name: "MHA (Hospital Administration)", campus: "Mangaluru", dept: "Allied", level: "PG", dur: "2 Years", link: "https://nitte.edu.in/niahs/admission-mhahsm.php", inst: "Nitte Institute of Allied Health Sciences" },
    { name: "PG Diploma Computed Tomography Tech", campus: "Mangaluru", dept: "Allied", level: "Diploma", dur: "1 Year", link: "https://nitte.edu.in/niahs/admission-ctt.php", inst: "Nitte Institute of Allied Health Sciences" },
    { name: "PG Diploma Magnetic Resonance Imaging", campus: "Mangaluru", dept: "Allied", level: "Diploma", dur: "1 Year", link: "https://nitte.edu.in/niahs/admission-mri.php", inst: "Nitte Institute of Allied Health Sciences" },

    // --- PHARMACY (NGSMIPS & NCOPS) ---
    { name: "BPharm", campus: "Mangaluru", dept: "Pharmacy", level: "UG", dur: "4 Years", link: "https://nitte.edu.in/ngsmips/bpharm.php", inst: "NGSM Institute of Pharmaceutical Sciences" },
    { name: "PharmD", campus: "Mangaluru", dept: "Pharmacy", level: "UG", dur: "6 Years", link: "https://nitte.edu.in/ngsmips/pharmd.php", inst: "NGSM Institute of Pharmaceutical Sciences" },
    { name: "PharmD (Post Baccalaureate)", campus: "Mangaluru", dept: "Pharmacy", level: "PG", dur: "3 Years", link: "https://nitte.edu.in/ngsmips/pharmdpb.php", inst: "NGSM Institute of Pharmaceutical Sciences" },
    { name: "MPharm (Pharmaceutics/Chemistry/Practice/Pharmacology)", campus: "Mangaluru", dept: "Pharmacy", level: "PG", dur: "2 Years", link: "https://nitte.edu.in/ngsmips/mpharm.php", inst: "NGSM Institute of Pharmaceutical Sciences" },
    { name: "BPharm", campus: "Bengaluru", dept: "Pharmacy", level: "UG", dur: "4 Years", link: "https://ncops.ac.in/bachelor-in-pharmacy.php", inst: "Nitte College of Pharmaceutical Sciences" },
    { name: "BPharm (Lateral Entry)", campus: "Bengaluru", dept: "Pharmacy", level: "UG", dur: "3 Years", link: "https://ncops.ac.in/bachelor-in-pharmacy.php", inst: "Nitte College of Pharmaceutical Sciences" },
    { name: "MPharm", campus: "Bengaluru", dept: "Pharmacy", level: "PG", dur: "2 Years", link: "https://ncops.ac.in/masters-in-pharmacy.php", inst: "Nitte College of Pharmaceutical Sciences" },

    // --- PHYSIOTHERAPY (NIPT) ---
    { name: "Bachelor of Physiotherapy (BPT)", campus: "Mangaluru", dept: "Physiotherapy", level: "UG", dur: "5 Years", link: "https://nitte.edu.in/nipt/bachelor-of-physiotherapy.php", inst: "Nitte Institute of Physiotherapy" },
    { name: "Master of Physiotherapy (MPT)", campus: "Mangaluru", dept: "Physiotherapy", level: "PG", dur: "2 Years", link: "https://nitte.edu.in/nipt/master-of-physiotherapy.php", inst: "Nitte Institute of Physiotherapy" },

    // --- NURSING (NUINS) ---
    { name: "BSc Nursing", campus: "Mangaluru", dept: "Nursing", level: "UG", dur: "4 Years", link: "https://nitte.edu.in/nuins/bachelor-of-science-bsc-nursing.php", inst: "Nitte Usha Institute of Nursing Sciences" },
    { name: "Post Basic BSc Nursing", campus: "Mangaluru", dept: "Nursing", level: "Diploma", dur: "2 Years", link: "https://nitte.edu.in/nuins/post-basic-bachelor-of-science-pbbsc-nursing.php", inst: "Nitte Usha Institute of Nursing Sciences" },
    { name: "MSc Nursing (Medical Surgical/Child Health/Mental Health)", campus: "Mangaluru", dept: "Nursing", level: "PG", dur: "2 Years", link: "https://nitte.edu.in/nuins/master-of-science-msc-nursing.php", inst: "Nitte Usha Institute of Nursing Sciences" },
    { name: "Post Basic Diploma in Dialysis Nursing", campus: "Mangaluru", dept: "Nursing", level: "Diploma", dur: "1 Year", link: "https://nitte.edu.in/admissions.php", inst: "Nitte Usha Institute of Nursing Sciences" },

    // --- BIOLOGICAL SCIENCES (NUCSER) ---
    { name: "BSc (Hons) Biomedical Science", campus: "Mangaluru", dept: "BioScience", level: "UG", dur: "4 Years", link: "https://nitte.edu.in/nucser/bachelor-of-science-bsc-hons-biomedical-sciences.php", inst: "Nitte University Centre for Science Edu" },
    { name: "MSc Biomedical Science", campus: "Mangaluru", dept: "BioScience", level: "PG", dur: "2 Years", link: "https://nitte.edu.in/nucser/master-of-science-msc-biomedical-science.php", inst: "Nitte University Centre for Science Edu" },
    { name: "MSc Food Science & Technology", campus: "Mangaluru", dept: "BioScience", level: "PG", dur: "2 Years", link: "https://nitte.edu.in/nucser/master-of-science-msc-food-safety-and-biotechnology.php", inst: "Nitte University Centre for Science Edu" },
    { name: "MSc Biotechnology", campus: "Mangaluru", dept: "BioScience", level: "PG", dur: "2 Years", link: "https://nitte.edu.in/nucser/master-of-science-msc-biotechnology.php", inst: "Nitte University Centre for Science Edu" },
    { name: "MSc Bioinformatics", campus: "Mangaluru", dept: "BioScience", level: "PG", dur: "2 Years", link: "https://nitte.edu.in/nucser/master-of-science-bioinformatics.php", inst: "Nitte University Centre for Science Edu" },
    { name: "MSc Microbiology", campus: "Mangaluru", dept: "BioScience", level: "PG", dur: "2 Years", link: "https://nitte.edu.in/nucser/master-of-science-msc-microbiology.php", inst: "Nitte University Centre for Science Edu" },
    { name: "MSc Cancer Biology", campus: "Mangaluru", dept: "BioScience", level: "PG", dur: "2 Years", link: "https://nitte.edu.in/nucser/master-of-cancer-biology.php", inst: "Nitte University Centre for Science Edu" },
    { name: "MSc Marine Biotechnology", campus: "Mangaluru", dept: "BioScience", level: "PG", dur: "2 Years", link: "https://nitte.edu.in/nucser/master-of-science-msc-marine-biotechnology.php", inst: "Nitte University Centre for Science Edu" },
    { name: "One Year MSc (Biological Science)", campus: "Mangaluru", dept: "BioScience", level: "PG", dur: "1 Year", link: "https://nitte.edu.in/nucser/one-year-program-msc.php", inst: "Nitte University Centre for Science Edu" },

    // --- SPEECH & HEARING (NISH) ---
    { name: "B.ASLP (Audiology & Speech Pathology)", campus: "Mangaluru", dept: "Audiology", level: "UG", dur: "4 Years", link: "https://nitte.edu.in/nish/bachelor-of-audiology-speech-language-pathology-baslp.php", inst: "Nitte Institute of Speech & Hearing" },
    { name: "MSc Speech-Language Pathology", campus: "Mangaluru", dept: "Audiology", level: "PG", dur: "2 Years", link: "https://nitte.edu.in/nish/admissions.php", inst: "Nitte Institute of Speech & Hearing" },
    { name: "MSc Audiology", campus: "Mangaluru", dept: "Audiology", level: "PG", dur: "2 Years", link: "https://nitte.edu.in/nish/master_of_science_in_audiology.php", inst: "Nitte Institute of Speech & Hearing" },

    // --- COMMERCE & MANAGEMENT ---
    { name: "BBA (Honors) General", campus: "Nitte", dept: "Commerce", level: "UG", dur: "4 Years", link: "https://nitte.edu.in/nsamfgcn/BBA-BBM-colleges-in-karnataka.php", inst: "NSAM First Grade College" },
    { name: "BBA (Honors) General", campus: "Bengaluru", dept: "Commerce", level: "UG", dur: "4 Years", link: "https://nitte.edu.in/nsamfgcb/BBA-regular-program.php", inst: "Dr. NSAM First Grade College" },
    { name: "BBA (Honors) Professional", campus: "Mangaluru", dept: "Commerce", level: "UG", dur: "4 Years", link: "https://nitte.edu.in/nipe/Bachelor_of_Business_Administration.php", inst: "Nitte Institute of Professional Edu" },
    { name: "BBA (Honors) Aviation Management", campus: "Bengaluru", dept: "Commerce", level: "UG", dur: "4 Years", link: "https://nitte.edu.in/nsamfgcb/BBA-aviation-management.php", inst: "Dr. NSAM First Grade College" },
    { name: "BCom (Honors) General", campus: "Nitte", dept: "Commerce", level: "UG", dur: "4 Years", link: "https://nitte.edu.in/nsamfgcn/Bcom-colleges-in-karnataka.php", inst: "NSAM First Grade College" },
    { name: "BCom (Honors) Professional", campus: "Nitte", dept: "Commerce", level: "UG", dur: "4 Years", link: "https://nitte.edu.in/nsamfgcn/Bcom-colleges-in-karnataka.php", inst: "NSAM First Grade College" },
    { name: "BCom (Honors) Professional", campus: "Mangaluru", dept: "Commerce", level: "UG", dur: "4 Years", link: "https://nitte.edu.in/nipe/Bachelor_of_commerce.php", inst: "Nitte Institute of Professional Edu" },
    { name: "BCom (Honors) Professional", campus: "Bengaluru", dept: "Commerce", level: "UG", dur: "4 Years", link: "https://nitte.edu.in/nsamfgcb/Bcom-professional.php", inst: "Dr. NSAM First Grade College" },
    { name: "BCom (Honors) Business Data Analytics", campus: "Bengaluru", dept: "Commerce", level: "UG", dur: "4 Years", link: "https://nitte.edu.in/nsamfgcb/Bcom-business-data-analytics.php", inst: "Dr. NSAM First Grade College" },
    { name: "BCA (Honors) Computer Applications", campus: "Nitte", dept: "Commerce", level: "UG", dur: "4 Years", link: "https://nitte.edu.in/nsamfgcn/bca.php", inst: "NSAM First Grade College" },
    { name: "BCA (Honors) Computer Applications", campus: "Mangaluru", dept: "Commerce", level: "UG", dur: "4 Years", link: "https://nitte.edu.in/nipe/Bachelor%20of%20Computer%20Applications.php", inst: "Nitte Institute of Professional Edu" },
    { name: "BCA (Honors) Computer Applications", campus: "Bengaluru", dept: "Commerce", level: "UG", dur: "4 Years", link: "https://nitte.edu.in/nsamfgcb/Bca-regular-colleges-in-bangalore.php", inst: "Dr. NSAM First Grade College" },
    { name: "BSc (Data Analytics)", campus: "Nitte", dept: "Commerce", level: "UG", dur: "3 Years", link: "https://nitte.edu.in/admissions.php", inst: "NSAM First Grade College" },
    { name: "MBA (Finance, Mktg, HR, SCM, Fintech, AI)", campus: "Mangaluru", dept: "Commerce", level: "PG", dur: "2 Years", link: "https://nitte.edu.in/jkshim/admissions.php", inst: "Justice KS Hegde Institute of Mgmt" },
    { name: "MBA", campus: "Bengaluru", dept: "Commerce", level: "PG", dur: "2 Years", link: "https://nitte.edu.in/nmit/MBA.php", inst: "Nitte Meenakshi Institute of Technology" },
    { name: "MBA", campus: "Nitte", dept: "Commerce", level: "PG", dur: "2 Years", link: "https://nitte.edu.in/admissions.php", inst: "Justice KS Hegde Institute of Mgmt" },

    // --- HOSPITALITY & AVIATION (NIHS) ---
    { name: "BSc (Honors) Hotel Management", campus: "Mangaluru", dept: "Hospitality", level: "UG", dur: "4 Years", link: "https://nitte.edu.in/nihs/hotel_management.php", inst: "Nitte Institute of Hospitality Services" },
    { name: "BSc (Honors) Culinary Arts & Management", campus: "Mangaluru", dept: "Hospitality", level: "UG", dur: "4 Years", link: "https://nitte.edu.in/nihs/bsc_hons_culinary_arts_management.php", inst: "Nitte Institute of Hospitality Services" },
    { name: "BSc (Honors) Airlines, Tourism & Hospitality", campus: "Mangaluru", dept: "Hospitality", level: "UG", dur: "4 Years", link: "https://nitte.edu.in/nihs/bsc_hons_airlines_tourism.php", inst: "Nitte Institute of Hospitality Services" },
    { name: "BSc (Honors) Hotel Management (Industry-integrated)", campus: "Mangaluru", dept: "Hospitality", level: "UG", dur: "4 Years", link: "https://nitte.edu.in/nihs/bsc-hotel-management-industry-integrated.php", inst: "Nitte Institute of Hospitality Services" },
    { name: "BSc (Honors) Civil Aviation Pilot Training", campus: "Bengaluru", dept: "Hospitality", level: "UG", dur: "4 Years", link: "https://nitte.edu.in/nmit/bsc-civil-aviation-pilot-training.php", inst: "Nitte Meenakshi Institute of Technology" },
    { name: "BSc (Honors) Civil Aviation Flight Dispatcher", campus: "Bengaluru", dept: "Hospitality", level: "UG", dur: "4 Years", link: "https://nitte.edu.in/nmit/bsc-civil-aviation-flight-dispatchers.php", inst: "Nitte Meenakshi Institute of Technology" },
    { name: "Certificate Course in Commi Chef", campus: "Mangaluru", dept: "Hospitality", level: "Certificate", dur: "Short Term", link: "https://nitte.edu.in/admissions.php", inst: "Nitte Institute of Hospitality Services" },

    // --- ARCHITECTURE & DESIGN ---
    { name: "BArch", campus: "Mangaluru", dept: "Architecture", level: "UG", dur: "5 Years", link: "https://nitte.edu.in/nia/arch.php", inst: "Nitte Institute of Architecture" },
    { name: "BArch", campus: "Bengaluru", dept: "Architecture", level: "UG", dur: "5 Years", link: "https://nitte.edu.in/nsapd/bachelor-of-architecture.php", inst: "Nitte School of Architecture & Design" },
    { name: "BPlan", campus: "Bengaluru", dept: "Architecture", level: "UG", dur: "4 Years", link: "https://nitte.edu.in/nsapd/bachelor-of-planning.php", inst: "Nitte School of Architecture & Design" },
    { name: "BDes (UI/UX | Product | Communication)", campus: "Bengaluru", dept: "Architecture", level: "UG", dur: "4 Years", link: "https://nitte.edu.in/nsapd/bachelor-of-design.php", inst: "Nitte School of Architecture & Design" },
    { name: "BDes (Fashion Design)", campus: "Bengaluru", dept: "Architecture", level: "UG", dur: "4 Years", link: "https://nitte.edu.in/nsftid/bdes-in-fashion-technology.php", inst: "Nitte School of Fashion & Interior Design" },
    { name: "BDes (Interior Design)", campus: "Bengaluru", dept: "Architecture", level: "UG", dur: "4 Years", link: "https://nitte.edu.in/nsftid/bdes-in-interior-design.php", inst: "Nitte School of Fashion & Interior Design" },
    { name: "MPlan (Urban & Regional Planning)", campus: "Bengaluru", dept: "Architecture", level: "PG", dur: "2 Years", link: "https://nitte.edu.in/nsapd/mplan-murp.php", inst: "Nitte School of Architecture & Design" },
    { name: "MDes (Fashion Design)", campus: "Bengaluru", dept: "Architecture", level: "PG", dur: "2 Years", link: "https://nitte.edu.in/nsftid/mdes-in-fashion-design.php", inst: "Nitte School of Fashion & Interior Design" },
    { name: "MDes (Interior Design)", campus: "Bengaluru", dept: "Architecture", level: "PG", dur: "2 Years", link: "https://nitte.edu.in/nsftid/mdes-in-interior-design.php", inst: "Nitte School of Fashion & Interior Design" },

    // --- MEDIA & COMMUNICATION ---
    { name: "BA (Hons) Media & Communication", campus: "Mangaluru", dept: "Communication", level: "UG", dur: "4 Years", link: "https://nitte.edu.in/nico/ba-hons-media-communication.php", inst: "Nitte Institute of Communication" },
    { name: "MA (Photography & Filmmaking)", campus: "Mangaluru", dept: "Communication", level: "PG", dur: "2 Years", link: "https://nitte.edu.in/nico/ma-in-photography-filmmaking.php", inst: "Nitte Institute of Communication" },

    // --- PHD PROGRAMS ---
    { name: "PhD in Engineering (All Branches)", campus: "Bengaluru", dept: "Engineering", level: "PhD", dur: "3+ Years", link: "https://nitte.edu.in/phd.php", inst: "NITTE Deemed University" },
    { name: "PhD in Engineering (All Branches)", campus: "Nitte", dept: "Engineering", level: "PhD", dur: "3+ Years", link: "https://nitte.edu.in/phd.php", inst: "NITTE Deemed University" },
    { name: "PhD in Medicine & Allied Health", campus: "Mangaluru", dept: "Medicine", level: "PhD", dur: "3+ Years", link: "https://nitte.edu.in/phd.php", inst: "NITTE Deemed University" },
    { name: "PhD in Dentistry", campus: "Mangaluru", dept: "Dentistry", level: "PhD", dur: "3+ Years", link: "https://nitte.edu.in/phd.php", inst: "NITTE Deemed University" },
    { name: "PhD in Biological Sciences", campus: "Mangaluru", dept: "BioScience", level: "PhD", dur: "3+ Years", link: "https://nitte.edu.in/phd.php", inst: "NITTE Deemed University" },
    { name: "PhD in Pharmacy", campus: "Mangaluru", dept: "Pharmacy", level: "PhD", dur: "3+ Years", link: "https://nitte.edu.in/phd.php", inst: "NITTE Deemed University" },
    { name: "PhD in Nursing", campus: "Mangaluru", dept: "Nursing", level: "PhD", dur: "3+ Years", link: "https://nitte.edu.in/phd.php", inst: "NITTE Deemed University" },
    { name: "PhD in Physiotherapy", campus: "Mangaluru", dept: "Physiotherapy", level: "PhD", dur: "3+ Years", link: "https://nitte.edu.in/phd.php", inst: "NITTE Deemed University" },
    { name: "PhD in Speech & Hearing", campus: "Mangaluru", dept: "Audiology", level: "PhD", dur: "3+ Years", link: "https://nitte.edu.in/phd.php", inst: "NITTE Deemed University" },
    { name: "PhD in Business Administration", campus: "Mangaluru", dept: "Commerce", level: "PhD", dur: "3+ Years", link: "https://nitte.edu.in/phd.php", inst: "NITTE Deemed University" },
    { name: "PhD in Commerce", campus: "Mangaluru", dept: "Commerce", level: "PhD", dur: "3+ Years", link: "https://nitte.edu.in/phd.php", inst: "NITTE Deemed University" },
    { name: "PhD in Humanities & Languages", campus: "Mangaluru", dept: "Communication", level: "PhD", dur: "3+ Years", link: "https://nitte.edu.in/phd.php", inst: "NITTE Deemed University" },
    { name: "PhD in Media & Communication", campus: "Mangaluru", dept: "Communication", level: "PhD", dur: "3+ Years", link: "https://nitte.edu.in/phd.php", inst: "NITTE Deemed University" },
    { name: "PhD in Fashion Design", campus: "Bengaluru", dept: "Architecture", level: "PhD", dur: "3+ Years", link: "https://nitte.edu.in/phd.php", inst: "NITTE Deemed University" },
    { name: "PhD in Interior Design", campus: "Bengaluru", dept: "Architecture", level: "PhD", dur: "3+ Years", link: "https://nitte.edu.in/phd.php", inst: "NITTE Deemed University" }
  ];

  // --- 2. HIGH PERFORMANCE RENDER ENGINE ---
  function renderCourses() {
    const searchText = document.getElementById('searchInput').value.toLowerCase();
    const campusFilter = document.getElementById('campusFilter').value;
    const levelFilter = document.getElementById('levelFilter').value;
    const deptFilter = document.getElementById('deptFilter').value;
    const grid = document.getElementById('courseGrid');
    
    // Clear Grid
    grid.innerHTML = '';
    let count = 0;
    let htmlBuffer = '';

    courses.forEach(course => {
      // Filter Logic
      const matchSearch = course.name.toLowerCase().includes(searchText) || course.inst.toLowerCase().includes(searchText);
      const matchCampus = campusFilter === 'All' || course.campus === campusFilter;
      const matchLevel = levelFilter === 'All' || course.level === levelFilter;
      const matchDept = deptFilter === 'All' || course.dept === deptFilter;

      if (matchSearch && matchCampus && matchLevel && matchDept) {
        count++;
        
        let colorClass = 'level-' + course.level; 
        let campusIcon = course.campus === 'Bengaluru' ? '🏙️' : course.campus === 'Mangaluru' ? '🌊' : '🌳';
        let levelIcon = course.level === 'UG' ? '🎓' : course.level === 'PG' ? '🔬' : course.level === 'PhD' ? '📜' : '🔖';

        htmlBuffer += `
          <div class="course-card ${colorClass}" style="animation-delay: ${(count % 10) * 0.05}s">
            <div>
              <div style="display:flex; justify-content:space-between;">
                  <span class="c-dept">${course.dept}</span>
              </div>
              <h3 class="c-title">${course.name}</h3>
              <div class="c-meta">
                <span class="c-badge">${levelIcon} ${course.level} • ${course.dur}</span>
                <span class="c-badge-loc">${campusIcon} ${course.campus}</span>
              </div>
              <div class="c-inst">
                  <span style="font-size:1.1rem; margin-top:-2px;">🏫</span>
                  <span>${course.inst}</span>
              </div>
            </div>
            <div class="c-footer">
              <a href="${course.link}" target="_blank" class="view-btn">View Full Details ➔</a>
            </div>
          </div>
        `;
      }
    });

    // Inject HTML in one batch for maximum performance
    grid.innerHTML = htmlBuffer;
    document.getElementById('countDisplay').innerText = count;
    
    // If no results
    if(count === 0) {
        grid.innerHTML = `
            <div style="grid-column: 1 / -1; text-align:center; padding: 50px; background:white; border-radius:12px; color:#64748b;">
                <div style="font-size:3rem; margin-bottom:10px;">🔍</div>
                <h3>No courses found matching your criteria.</h3>
                <p>Try adjusting your search filters or resetting them.</p>
                <button onclick="resetFilters()" style="background:#1E3A8A; color:white; padding:10px 20px; border:none; border-radius:50px; cursor:pointer; font-weight:bold; margin-top:10px;">Reset Filters</button>
            </div>
        `;
    }
  }

  function resetFilters() {
    document.getElementById('searchInput').value = '';
    document.getElementById('campusFilter').value = 'All';
    document.getElementById('levelFilter').value = 'All';
    document.getElementById('deptFilter').value = 'All';
    renderCourses();
  }

  // Initial Render on page load
  document.addEventListener('DOMContentLoaded', renderCourses);
</script>
