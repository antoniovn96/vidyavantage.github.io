---
layout: default
title: "NITTE University Course Portal 🎓"
permalink: /colleges/nitte/
image: "https://nitte.edu.in/img/nitte-university-mangalore.jpg"
description: "Browse UG, PG, and PhD programs at NITTE University across Mangaluru, Bengaluru, and Nitte campuses."
---

<meta property="og:title" content="NITTE University Course Portal 🎓">
<meta property="og:description" content="Access details for Engineering, Medicine, Management, and Sciences at NITTE. Check eligibility and specializations.">
<meta property="og:image" content="https://nitte.edu.in/img/nitte-university-mangalore.jpg">

<style>
  /* 1. LAYOUT RESET */
  .main-content { max-width: 100% !important; padding: 0 !important; margin: 0 !important; }
  body { background-color: #f8f9fa; font-family: 'Segoe UI', system-ui, sans-serif; color: #333; }

  /* 2. HERO SECTION */
  .nitte-hero {
    background: linear-gradient(rgba(18, 52, 86, 0.85), rgba(10, 35, 66, 0.9)), url('https://nitte.edu.in/img/nitte-university-mangalore.jpg');
    background-size: cover;
    background-position: center;
    color: white;
    text-align: center;
    padding: 100px 20px;
    margin-bottom: 0;
  }
  
  .nitte-hero h1 { font-size: 3rem; margin: 0; font-weight: 900; color: #fff !important; letter-spacing: -0.5px;}
  .nitte-hero p { font-size: 1.15rem; color: #e2e8f0 !important; margin-top: 15px; max-width: 800px; margin-left: auto; margin-right: auto; line-height: 1.6;}

  /* 3. APP CONTAINER */
  .app-container {
    max-width: 1400px;
    margin: 0 auto;
    display: flex;
    gap: 30px;
    padding: 40px 20px;
    align-items: flex-start;
  }

  /* 4. SIDEBAR FILTERS */
  .filters-sidebar {
    width: 280px;
    background: white;
    padding: 25px;
    border-radius: 12px;
    box-shadow: 0 10px 30px rgba(0,0,0,0.05);
    position: sticky;
    top: 90px;
    border-top: 4px solid #123456; /* NITTE Blue */
    flex-shrink: 0;
  }

  .filter-group { margin-bottom: 20px; }
  .filter-label { display: block; font-weight: 700; margin-bottom: 8px; color: #123456; font-size: 0.9rem; text-transform: uppercase; letter-spacing: 0.5px;}
  
  .filter-input, .filter-select {
    width: 100%;
    padding: 12px 15px;
    border: 1px solid #cbd5e1;
    border-radius: 8px;
    font-size: 0.95rem;
    outline: none;
    transition: border 0.2s, box-shadow 0.2s;
    background: #f8fafc;
  }
  .filter-input:focus, .filter-select:focus { border-color: #123456; box-shadow: 0 0 0 3px rgba(18, 52, 86, 0.1); background: white;}

  /* 5. COURSE GRID */
  .results-area { flex-grow: 1; }
  
  .course-grid {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(320px, 1fr));
    gap: 25px;
  }

  .course-card {
    background: white;
    border-radius: 12px;
    padding: 25px;
    border-left: 5px solid #ddd;
    box-shadow: 0 4px 15px rgba(0,0,0,0.03);
    transition: transform 0.2s, box-shadow 0.2s;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
  }
  .course-card:hover { transform: translateY(-5px); box-shadow: 0 12px 30px rgba(0,0,0,0.08); }

  /* Level Colors */
  .level-UG { border-left-color: #2980b9; }
  .level-PG { border-left-color: #8e44ad; }
  .level-PhD { border-left-color: #c0392b; }
  .level-Diploma { border-left-color: #f39c12; }
  .level-Fellowship { border-left-color: #16a085; }

  .c-school { font-size: 0.75rem; text-transform: uppercase; font-weight: 800; color: #64748b; margin-bottom: 8px; letter-spacing: 0.5px;}
  .c-title { font-size: 1.2rem; font-weight: 800; color: #0f172a; margin: 0 0 10px 0; line-height: 1.4; }
  .c-meta { display: flex; gap: 8px; flex-wrap: wrap; margin-bottom: 20px; }
  .c-badge { display: inline-block; background: #EEF2FF; padding: 6px 12px; border-radius: 6px; font-size: 0.8rem; font-weight: 700; color: #4338CA; border: 1px solid #C7D2FE;}
  .c-badge-loc { display: inline-block; background: #FFFBEB; padding: 6px 12px; border-radius: 6px; font-size: 0.8rem; font-weight: 700; color: #B45309; border: 1px solid #FDE68A;}
  
  .c-footer { margin-top: auto; display: flex; justify-content: space-between; align-items: center; border-top: 1px solid #f1f5f9; padding-top: 20px; }
  
  .view-btn {
    background: #f8fafc; border: 1px solid #123456; color: #123456;
    padding: 8px 20px; border-radius: 50px; font-size: 0.9rem; font-weight: 700; cursor: pointer; transition: 0.3s;
    text-decoration: none;
    display: inline-block;
  }
  .view-btn:hover { background: #123456; color: white; box-shadow: 0 4px 10px rgba(18, 52, 86, 0.2);}

  /* Mobile */
  @media (max-width: 900px) {
    .app-container { flex-direction: column; }
    .filters-sidebar { width: 100%; position: static; }
  }
</style>

<div class="nitte-hero">
  <h1>NITTE University</h1>
  <p>Deemed-to-be University (NAAC A+ Grade). Discover world-class programs across Medicine, Engineering, Management, and Sciences in Mangaluru, Bengaluru, and Nitte.</p>
</div>

<div class="app-container">

  <aside class="filters-sidebar">
    <div class="filter-group">
      <label class="filter-label">🔍 Search Course</label>
      <input type="text" id="searchInput" class="filter-input" placeholder="e.g. BTech, Medicine..." onkeyup="renderCourses()">
    </div>

    <div class="filter-group">
      <label class="filter-label">📍 Campus Location</label>
      <select id="campusFilter" class="filter-select" onchange="renderCourses()">
        <option value="All">All Campuses</option>
        <option value="Mangaluru">Mangaluru</option>
        <option value="Bangalore">Bengaluru</option>
        <option value="Nitte">Nitte</option>
      </select>
    </div>
    
    <div class="filter-group">
      <label class="filter-label">🎓 Programme Level</label>
      <select id="levelFilter" class="filter-select" onchange="renderCourses()">
        <option value="All">All Levels</option>
        <option value="UG">Undergraduate (UG)</option>
        <option value="PG">Postgraduate (PG)</option>
        <option value="PhD">Doctoral (PhD)</option>
        <option value="Diploma">Diploma</option>
        <option value="Fellowship">Fellowship</option>
      </select>
    </div>

    <div class="filter-group">
      <label class="filter-label">🏫 Faculty</label>
      <select id="deptFilter" class="filter-select" onchange="renderCourses()">
        <option value="All">All Faculties</option>
        <option value="Engineering">Engineering & Tech</option>
        <option value="Medicine">Medicine & Allied Health</option>
        <option value="Dentistry">Dentistry</option>
        <option value="Commerce-Management">Commerce & Management</option>
        <option value="Pharmacy">Pharmacy</option>
        <option value="BioScience">Biological Sciences</option>
        <option value="Architecture">Architecture & Design</option>
        <option value="Communication">Media & Communication</option>
      </select>
    </div>

    <div style="margin-top:20px; font-size:0.85rem; color:#64748b; font-weight: 600;">
      Showing <strong id="countDisplay" style="color: #0f172a;">0</strong> courses
    </div>
  </aside>

  <div class="results-area">
    <div id="courseGrid" class="course-grid">
      </div>
  </div>

</div>

<script>
  // --- 1. COURSE DATABASE ---
  const courses = [
    // ENGINEERING - NITTE CAMPUS
    { name: "BTech Artificial Intelligence & Data Science", campus: "Nitte", dept: "Engineering", level: "UG", dur: "4 Years", link: "https://nitte.edu.in/nmamit/department-AI&DS.php", inst: "NMAM Institute of Technology" },
    { name: "BTech Computer Science (Cyber Security)", campus: "Nitte", dept: "Engineering", level: "UG", dur: "4 Years", link: "https://nitte.edu.in/nmamit/department-CyberSecurity.php", inst: "NMAM Institute of Technology" },
    { name: "BTech Electronics (VLSI Design & Technology)", campus: "Nitte", dept: "Engineering", level: "UG", dur: "4 Years", link: "https://nitte.edu.in/nmamit/department-VLSI.php", inst: "NMAM Institute of Technology" },
    { name: "BTech Artificial Intelligence & Machine Learning", campus: "Nitte", dept: "Engineering", level: "UG", dur: "4 Years", link: "https://nitte.edu.in/nmamit/department-AI&ML.php", inst: "NMAM Institute of Technology" },
    { name: "BTech Biotechnology", campus: "Nitte", dept: "Engineering", level: "UG", dur: "4 Years", link: "https://nitte.edu.in/nmamit/department-biotechnology.php", inst: "NMAM Institute of Technology" },
    { name: "BTech Computer Science", campus: "Nitte", dept: "Engineering", level: "UG", dur: "4 Years", link: "https://nitte.edu.in/nmamit/department-computer-science.php", inst: "NMAM Institute of Technology" },
    { name: "BTech Robotics & Artificial Intelligence", campus: "Nitte", dept: "Engineering", level: "UG", dur: "4 Years", link: "https://nitte.edu.in/nmamit/department-robotics.php", inst: "NMAM Institute of Technology" },
    { name: "MTech Computer Science & Engineering", campus: "Nitte", dept: "Engineering", level: "PG", dur: "2 Years", link: "https://nitte.edu.in/nmamit/department-computer-science.php#program", inst: "NMAM Institute of Technology" },
    { name: "MTech VLSI Design & Embedded Systems", campus: "Nitte", dept: "Engineering", level: "PG", dur: "2 Years", link: "https://nitte.edu.in/nmamit/department-electronics-communication.php#program", inst: "NMAM Institute of Technology" },
    { name: "MCA (Master of Computer Applications)", campus: "Nitte", dept: "Engineering", level: "PG", dur: "2 Years", link: "https://nitte.edu.in/nmamit/department-mca.php", inst: "NMAM Institute of Technology" },

    // ENGINEERING - BANGALORE CAMPUS
    { name: "BTech Artificial Intelligence & Data Science", campus: "Bangalore", dept: "Engineering", level: "UG", dur: "4 Years", link: "https://nitte.edu.in/nmit/btech-in-artificialintelligence-and-datascience.php", inst: "Nitte Meenakshi Institute of Technology" },
    { name: "BTech Aeronautical", campus: "Bangalore", dept: "Engineering", level: "UG", dur: "4 Years", link: "https://nitte.edu.in/nmit/btech-aeronautical-engineering.php", inst: "Nitte Meenakshi Institute of Technology" },
    { name: "BTech Computer Science & Business Systems", campus: "Bangalore", dept: "Engineering", level: "UG", dur: "4 Years", link: "https://nitte.edu.in/nmit/btech-computer-science-and-business-systems.php", inst: "Nitte Meenakshi Institute of Technology" },
    { name: "MTech Defence Technology", campus: "Bangalore", dept: "Engineering", level: "PG", dur: "2 Years", link: "https://nitte.edu.in/nmit/mtech-in-defence-technology.php", inst: "Nitte Meenakshi Institute of Technology" },
    { name: "MTech Electric Vehicle Technology", campus: "Bangalore", dept: "Engineering", level: "PG", dur: "2 Years", link: "https://nitte.edu.in/nmit/mtech-in-electric-vehicle-technology.php", inst: "Nitte Meenakshi Institute of Technology" },

    // MEDICINE & ALLIED HEALTH - MANGALURU
    { name: "MBBS (Bachelor of Medicine, Bachelor of Surgery)", campus: "Mangaluru", dept: "Medicine", level: "UG", dur: "5.5 Years", link: "https://nitte.edu.in/kshema/admission-mbbs.php", inst: "K S Hegde Medical Academy" },
    { name: "Bachelor in Medical Radiology & Imaging Technology", campus: "Mangaluru", dept: "Medicine", level: "UG", dur: "4 Years", link: "https://nitte.edu.in/niahs/admission-bsc-mit.php", inst: "Nitte Institute of Allied Health Sciences" },
    { name: "Bachelor in Anaesthesia & Operation Theatre Tech", campus: "Mangaluru", dept: "Medicine", level: "UG", dur: "4 Years", link: "https://nitte.edu.in/niahs/admission-bsc-OT.php", inst: "Nitte Institute of Allied Health Sciences" },
    { name: "BSc Nursing", campus: "Mangaluru", dept: "Medicine", level: "UG", dur: "4 Years", link: "https://nitte.edu.in/nuins/bachelor-of-science-bsc-nursing.php", inst: "Nitte Usha Institute of Nursing Sciences" },
    { name: "Bachelor of Physiotherapy (BPT)", campus: "Mangaluru", dept: "Medicine", level: "UG", dur: "5 Years", link: "https://nitte.edu.in/nipt/bachelor-of-physiotherapy.php", inst: "Nitte Institute of Physiotherapy" },
    { name: "MD (General Medicine)", campus: "Mangaluru", dept: "Medicine", level: "PG", dur: "3 Years", link: "https://nitte.edu.in/kshema/admission-md-general-medicine.php", inst: "K S Hegde Medical Academy" },
    { name: "MS (General Surgery)", campus: "Mangaluru", dept: "Medicine", level: "PG", dur: "3 Years", link: "https://nitte.edu.in/kshema/admission-ms-general-surgery.php", inst: "K S Hegde Medical Academy" },
    { name: "MPH (Public Health)", campus: "Mangaluru", dept: "Medicine", level: "PG", dur: "2 Years", link: "https://nitte.edu.in/niahs/admission-mph.php", inst: "Nitte Institute of Allied Health Sciences" },
    { name: "MHA (Hospital Administration)", campus: "Mangaluru", dept: "Medicine", level: "PG", dur: "2 Years", link: "https://nitte.edu.in/niahs/admission-mhahsm.php", inst: "Nitte Institute of Allied Health Sciences" },

    // DENTISTRY - MANGALURU
    { name: "BDS (Bachelor of Dental Surgery)", campus: "Mangaluru", dept: "Dentistry", level: "UG", dur: "5 Years", link: "https://nitte.edu.in/absmids/admission-bds.php", inst: "A B Shetty Memorial Institute of Dental Sciences" },
    { name: "MDS Oral & Maxillofacial Surgery", campus: "Mangaluru", dept: "Dentistry", level: "PG", dur: "3 Years", link: "https://nitte.edu.in/absmids/admission-mds-oral-maxillofacial-surgery.php", inst: "A B Shetty Memorial Institute of Dental Sciences" },
    { name: "MDS Conservative Dentistry & Endodontics", campus: "Mangaluru", dept: "Dentistry", level: "PG", dur: "3 Years", link: "https://nitte.edu.in/absmids/admission-mds-conservative-dentistry-endodontics.php", inst: "A B Shetty Memorial Institute of Dental Sciences" },

    // PHARMACY
    { name: "BPharm", campus: "Mangaluru", dept: "Pharmacy", level: "UG", dur: "4 Years", link: "https://nitte.edu.in/ngsmips/bpharm.php", inst: "NGSM Institute of Pharmaceutical Sciences" },
    { name: "PharmD", campus: "Mangaluru", dept: "Pharmacy", level: "UG", dur: "6 Years", link: "https://nitte.edu.in/ngsmips/pharmd.php", inst: "NGSM Institute of Pharmaceutical Sciences" },
    { name: "BPharm", campus: "Bangalore", dept: "Pharmacy", level: "UG", dur: "4 Years", link: "https://ncops.ac.in/bachelor-in-pharmacy.php", inst: "Nitte College of Pharmaceutical Sciences" },

    // BIOSCIENCES
    { name: "BSc (Honors) Biomedical Science", campus: "Mangaluru", dept: "BioScience", level: "UG", dur: "4 Years", link: "https://nitte.edu.in/nucser/bachelor-of-science-bsc-hons-biomedical-sciences.php", inst: "Nitte University Centre for Science Education" },
    { name: "MSc Food Science & Technology", campus: "Mangaluru", dept: "BioScience", level: "PG", dur: "2 Years", link: "https://nitte.edu.in/nucser/master-of-science-msc-food-safety-and-biotechnology.php", inst: "Nitte University Centre for Science Education" },

    // COMMERCE & MANAGEMENT
    { name: "BBA (Honors) Aviation Management", campus: "Bangalore", dept: "Commerce-Management", level: "UG", dur: "4 Years", link: "https://nitte.edu.in/nsamfgcb/BBA-aviation-management.php", inst: "Dr. NSAM First Grade College" },
    { name: "BCom (Honors) Business Data Analytics", campus: "Bangalore", dept: "Commerce-Management", level: "UG", dur: "4 Years", link: "https://nitte.edu.in/nsamfgcb/Bcom-business-data-analytics.php", inst: "Dr. NSAM First Grade College" },
    { name: "MBA (Finance, Marketing, HR, AI)", campus: "Mangaluru", dept: "Commerce-Management", level: "PG", dur: "2 Years", link: "https://nitte.edu.in/jkshim/admissions.php", inst: "Justice K S Hegde Institute of Management" },
    { name: "MBA", campus: "Bangalore", dept: "Commerce-Management", level: "PG", dur: "2 Years", link: "https://nitte.edu.in/nmit/MBA.php", inst: "Nitte Meenakshi Institute of Technology" },

    // ARCHITECTURE & DESIGN
    { name: "BArch", campus: "Bangalore", dept: "Architecture", level: "UG", dur: "5 Years", link: "https://nitte.edu.in/nsapd/bachelor-of-architecture.php", inst: "Nitte School of Architecture, Planning & Design" },
    { name: "BDes (UI/UX | Product | Communication)", campus: "Bangalore", dept: "Architecture", level: "UG", dur: "4 Years", link: "https://nitte.edu.in/nsapd/bachelor-of-design.php", inst: "Nitte School of Architecture, Planning & Design" },
    { name: "BDes (Fashion Design)", campus: "Bangalore", dept: "Architecture", level: "UG", dur: "4 Years", link: "https://nitte.edu.in/nsftid/bdes-in-fashion-technology.php", inst: "Nitte School of Fashion Technology" },

    // COMMUNICATION
    { name: "BA (Honors) Media & Communication", campus: "Mangaluru", dept: "Communication", level: "UG", dur: "4 Years", link: "https://nitte.edu.in/nico/ba-hons-media-communication.php", inst: "Nitte Institute of Communication" },
    
    // PhD PROGRAMS
    { name: "PhD Programs (All Faculties)", campus: "All", dept: "All", level: "PhD", dur: "Variable", link: "https://nitte.edu.in/phd.php", inst: "NITTE University (Deemed)" }
  ];

  // --- 2. RENDER ENGINE ---
  function renderCourses() {
    const searchText = document.getElementById('searchInput').value.toLowerCase();
    const campusFilter = document.getElementById('campusFilter').value;
    const levelFilter = document.getElementById('levelFilter').value;
    const deptFilter = document.getElementById('deptFilter').value;
    const grid = document.getElementById('courseGrid');
    
    grid.innerHTML = '';
    let count = 0;

    courses.forEach(course => {
      const matchSearch = course.name.toLowerCase().includes(searchText) || course.inst.toLowerCase().includes(searchText);
      const matchCampus = campusFilter === 'All' || course.campus === campusFilter || course.campus === 'All';
      const matchLevel = levelFilter === 'All' || course.level === levelFilter || course.level === 'All';
      const matchDept = deptFilter === 'All' || course.dept === deptFilter || course.dept === 'All';

      if (matchSearch && matchCampus && matchLevel && matchDept) {
        count++;
        let colorClass = 'level-' + course.level; 

        const card = `
          <div class="course-card ${colorClass}" style="animation-delay: ${count * 0.05}s">
            <div>
              <span class="c-school">${course.dept}</span>
              <h3 class="c-title">${course.name}</h3>
              <div class="c-meta">
                <span class="c-badge">${course.level} • ${course.dur}</span>
                <span class="c-badge-loc">📍 ${course.campus}</span>
              </div>
              <p style="font-size:0.85rem; color:#64748b; margin:0 0 15px 0;">🏫 ${course.inst}</p>
            </div>
            <div class="c-footer">
              <a href="${course.link}" target="_blank" class="view-btn">View Details ➔</a>
            </div>
          </div>
        `;
        grid.innerHTML += card;
      }
    });

    document.getElementById('countDisplay').innerText = count;
  }

  // Initial Render
  renderCourses();
</script>
