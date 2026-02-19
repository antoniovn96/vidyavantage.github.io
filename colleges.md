---
layout: default
title: Top Colleges & Universities 🎓
permalink: /colleges/
image: "https://images.unsplash.com/photo-1541339907198-e08756dedf3f?w=1200&h=630&fit=crop"
description: "Browse top universities in Bangalore, Chikkamagaluru & Roorkee. Filter by courses, location, and fees for IISc, IIT Roorkee, AIT, BMSCE, Christ, and more."
---

<style>
  /* 1. HERO SECTION */
  .colleges-hero {
    background: linear-gradient(rgba(10, 35, 66, 0.9), rgba(10, 35, 66, 0.8)), url('https://images.unsplash.com/photo-1523050854058-8df90110c9f1?w=1600&auto=format&fit=crop');
    background-size: cover;
    background-position: center;
    color: white;
    text-align: center;
    padding: 80px 20px;
    margin-bottom: 40px;
    box-shadow: 0 4px 10px rgba(0,0,0,0.2);
  }
  .colleges-hero h1 { margin: 0; font-size: 3rem; font-weight: 800; color: white !important; }
  .colleges-hero p { font-size: 1.2rem; color: #ddd !important; margin-top: 10px; }

  /* 2. FILTER BAR */
  .filter-container {
    max-width: 1200px;
    margin: 0 auto 40px;
    padding: 20px;
    background: white;
    border-radius: 12px;
    box-shadow: 0 5px 20px rgba(0,0,0,0.05);
    display: flex;
    gap: 15px;
    justify-content: center;
    flex-wrap: wrap;
    align-items: center;
  }

  .search-input {
    padding: 12px 20px;
    border: 2px solid #eee;
    border-radius: 50px;
    width: 250px;
    font-size: 0.95rem;
    outline: none;
    transition: border 0.3s;
  }
  .search-input:focus { border-color: #0A2342; }

  .filter-select {
    padding: 12px 20px;
    border: 2px solid #eee;
    border-radius: 50px;
    background: white;
    color: #555;
    font-weight: 600;
    cursor: pointer;
    outline: none;
    transition: all 0.3s;
    min-width: 180px;
  }
  .filter-select:hover, .filter-select:focus { border-color: #0A2342; color: #0A2342; }

  .reset-btn {
    padding: 12px 25px;
    background: #e74c3c;
    color: white;
    border: none;
    border-radius: 50px;
    font-weight: bold;
    cursor: pointer;
    transition: 0.2s;
  }
  .reset-btn:hover { background: #c0392b; }

  /* 3. GRID LAYOUT */
  .college-grid {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(350px, 1fr));
    gap: 30px;
    padding: 0 20px 60px;
    max-width: 1200px;
    margin: 0 auto;
  }

  /* 4. COLLEGE CARD */
  .college-card {
    background: white;
    border-radius: 12px;
    overflow: hidden;
    box-shadow: 0 10px 30px rgba(0,0,0,0.08);
    transition: transform 0.3s, box-shadow 0.3s;
    display: flex;
    flex-direction: column;
    border-top: 5px solid #0A2342;
    animation: fadeIn 0.5s ease;
  }
  
  .college-card:hover { transform: translateY(-5px); box-shadow: 0 15px 40px rgba(0,0,0,0.15); }
  .college-card.hidden { display: none; }

  .card-img {
    width: 100%;
    height: 180px;
    object-fit: cover;
  }

  .card-body { padding: 25px; flex-grow: 1; }
  
  .college-name { 
    margin: 0 0 10px; 
    color: #0A2342; 
    font-size: 1.3rem; 
    font-weight: 800; 
  }
  
  .college-meta { font-size: 0.9rem; color: #666; margin-bottom: 15px; }
  
  .tag { 
    display: inline-block; 
    background: #f0f4f8; 
    color: #555; 
    padding: 4px 10px; 
    border-radius: 4px; 
    font-size: 0.8rem; 
    font-weight: 600; 
    margin-right: 5px; 
  }

  .card-desc { color: #555; font-size: 0.95rem; line-height: 1.5; margin-bottom: 20px; }

  .card-footer { padding: 20px; border-top: 1px solid #eee; background: #fafafa; text-align: center; }

  .view-btn {
    display: inline-block;
    padding: 10px 25px;
    border-radius: 50px;
    text-decoration: none;
    font-weight: bold;
    transition: all 0.2s;
  }

  @keyframes fadeIn { from { opacity: 0; transform: translateY(10px); } to { opacity: 1; transform: translateY(0); } }
  
  /* Mobile Responsive */
  @media (max-width: 768px) {
    .filter-container { flex-direction: column; align-items: stretch; }
    .search-input, .filter-select, .reset-btn { width: 100%; }
  }
</style>

<div class="colleges-hero">
  <h1>Top Colleges & Universities</h1>
  <p>Find the best institutions by course and location.</p>
</div>

<div class="filter-container">
  <input type="text" id="searchInput" class="search-input" placeholder="🔍 Search College Name..." onkeyup="filterColleges()">
  
  <select id="courseFilter" class="filter-select" onchange="filterColleges()">
    <option value="all">📚 All Courses</option>
    <option value="engineering">Engineering</option>
    <option value="architecture">Architecture</option>
    <option value="management">Management</option>
    <option value="science">Science & Arts</option>
    <option value="hospitality">Hospitality</option>
    <option value="law">Law</option>
  </select>

  <select id="locationFilter" class="filter-select" onchange="filterColleges()">
    <option value="all">📍 All Locations</option>
    <option value="Bengaluru">Bengaluru (General)</option>
    <option value="Roorkee">Roorkee (IITR)</option>
    <option value="Chikkamagaluru">Chikkamagaluru (AIT)</option>
    <option value="Yelahanka">Yelahanka</option>
    <option value="Whitefield">Whitefield</option>
    <option value="K.R. Puram">K.R. Puram</option>
    <option value="Marathahalli">Marathahalli</option>
    <option value="Basavanagudi">Basavanagudi</option>
    <option value="Malleshwaram">Malleshwaram / Mathikere</option>
    <option value="South">South Bangalore (Jayanagar/Kumaraswamy)</option>
    <option value="West">West Bangalore (Mysore Rd/Kengeri)</option>
  </select>

  <button class="reset-btn" onclick="resetFilters()">Reset</button>
</div>

<div class="college-grid" id="collegeGrid">

  <div class="college-card" data-category="science" data-location="Bengaluru Malleshwaram" style="border-top-color: #005a9c;">
    <img src="https://ioe.iisc.ac.in/wp-content/uploads/2021/04/bg-image-1-500x286.jpg" class="card-img" alt="IISc Bangalore">
    <div class="card-body">
      <h2 class="college-name" style="color: #005a9c;">Indian Institute of Science (IISc)</h2>
      <div class="college-meta">
        <span class="tag">📍 Bengaluru</span>
        <span class="tag">🏆 NIRF Rank #1</span>
      </div>
      <p class="card-desc">
        India's premier institute for advanced scientific research. Known for B.Sc (Research), M.Tech, and PhDs in Science & Engineering.
      </p>
    </div>
    <div class="card-footer">
      <a href="{{ '/colleges/iisc/' | relative_url }}" class="view-btn" style="background: #005a9c; color: white;">View Programs ➔</a>
    </div>
  </div>

  <div class="college-card" data-category="engineering architecture management science" data-location="Roorkee" style="border-top-color: #003366;">
    <img src="https://dynamic-media-cdn.tripadvisor.com/media/photo-o/0c/34/36/84/the-beautiful-main-building.jpg?w=1000&h=600&s=1" class="card-img" alt="IIT Roorkee">
    <div class="card-body">
      <h2 class="college-name" style="color: #003366;">IIT Roorkee</h2>
      <div class="college-meta">
        <span class="tag">📍 Roorkee</span>
        <span class="tag">🏆 NIRF Rank #5</span>
      </div>
      <p class="card-desc">
        Asia's oldest technical institution (formerly Thomason College). Renowned for its Civil Engineering, Architecture, and strong research output.
      </p>
    </div>
    <div class="card-footer">
      <a href="{{ '/colleges/iitr/' | relative_url }}" class="view-btn" style="background: #003366; color: white;">View Programs ➔</a>
    </div>
  </div>

  <div class="college-card" data-category="engineering management" data-location="Chikkamagaluru" style="border-top-color: #16a085;">
    <img src="https://images.jdmagicbox.com/comp/chikmagalur/06/9999pmulblrstd1008006/catalogue/adichunchanagiri-institute-of-technology-jyothinagar-chikmagalur-chikmagalur-colleges-bp76m2q.jpg" class="card-img" alt="Adichunchanagiri Institute of Technology">
    <div class="card-body">
      <h2 class="college-name" style="color: #16a085;">Adichunchanagiri Institute of Technology (AIT)</h2>
      <div class="college-meta">
        <span class="tag">📍 Chikkamagaluru</span>
        <span class="tag">🏆 Est. 1980</span>
      </div>
      <p class="card-desc">
        A premier institute located in the scenic hills of Chikkamagaluru. Known for strong discipline, extensive campus facilities, and specialized Robotics/AI programs.
      </p>
    </div>
    <div class="card-footer">
      <a href="{{ '/colleges/ait/' | relative_url }}" class="view-btn" style="background: #16a085; color: white;">View Programs ➔</a>
    </div>
  </div>

  <div class="college-card" data-category="engineering management science" data-location="Bengaluru V.V. Puram" style="border-top-color: #0033a0;">
    <img src="https://bit-bangalore.edu.in/assets/images/explore/about-bit-1.jpg" class="card-img" alt="BIT Bangalore">
    <div class="card-body">
      <h2 class="college-name" style="color: #0033a0;">Bangalore Institute of Technology (BIT)</h2>
      <div class="college-meta">
        <span class="tag">📍 V.V. Puram</span>
        <span class="tag">🏆 Est. 1979</span>
      </div>
      <p class="card-desc">
        A reputed VTU-affiliated college located in the heart of the city. Known for strong placements in core tech and high-end research centers.
      </p>
    </div>
    <div class="card-footer">
      <a href="{{ '/colleges/bit/' | relative_url }}" class="view-btn" style="background: #0033a0; color: white;">View Programs ➔</a>
    </div>
  </div>

  <div class="college-card" data-category="engineering" data-location="Bengaluru Malleshwaram" style="border-top-color: #800000;">
    <img src="https://msrit-bucket.s3.us-west-2.amazonaws.com/Gallery/rit-1.jpeg" class="card-img" alt="MSRIT Bangalore">
    <div class="card-body">
      <h2 class="college-name" style="color: #800000;">Ramaiah Institute of Technology</h2>
      <div class="college-meta">
        <span class="tag">📍 Mathikere</span>
        <span class="tag">🏆 Est. 1962</span>
      </div>
      <p class="card-desc">
        A premier autonomous engineering institute affiliated to VTU. Renowned for its academic excellence, state-of-the-art infrastructure, and high placement records.
      </p>
    </div>
    <div class="card-footer">
      <a href="{{ '/colleges/msrit/' | relative_url }}" class="view-btn" style="background: #800000; color: white;">View Programs ➔</a>
    </div>
  </div>

  <div class="college-card" data-category="engineering" data-location="Bengaluru South" style="border-top-color: #003366;">
    <img src="https://www.admissionbangalore.com/images/engg_col/dayananda-sagar-college-of-engg.jpg" class="card-img" alt="DSCE Bangalore">
    <div class="card-body">
      <h2 class="college-name" style="color: #003366;">Dayananda Sagar College of Engineering</h2>
      <div class="college-meta">
        <span class="tag">📍 Kumaraswamy Layout</span>
        <span class="tag">🏆 Est. 1979</span>
      </div>
      <p class="card-desc">
        An autonomous institute affiliated to VTU, offering widest range of engineering branches. Known for its huge campus and excellent placements.
      </p>
    </div>
    <div class="card-footer">
      <a href="{{ '/colleges/dsce/' | relative_url }}" class="view-btn" style="background: #003366; color: white;">View Programs ➔</a>
    </div>
  </div>

  <div class="college-card" data-category="engineering" data-location="Bengaluru Marathahalli" style="border-top-color: #1a237e;">
    <img src="https://newhorizoncollegeofengineering.in/wp-content/uploads/2024/03/NHCE-Campus-Temple.webp" class="card-img" alt="NHCE Bangalore">
    <div class="card-body">
      <h2 class="college-name" style="color: #1a237e;">New Horizon College of Engineering</h2>
      <div class="college-meta">
        <span class="tag">📍 Marathahalli</span>
        <span class="tag">🏆 Est. 2001</span>
      </div>
      <p class="card-desc">
        A 'A' Grade NAAC accredited autonomous college in the heart of Bangalore's IT corridor. Famous for high placement records and Minor Degree options.
      </p>
    </div>
    <div class="card-footer">
      <a href="{{ '/colleges/nhce/' | relative_url }}" class="view-btn" style="background: #1a237e; color: white;">View Programs ➔</a>
    </div>
  </div>

  <div class="college-card" data-category="engineering management science" data-location="Bengaluru K.R. Puram" style="border-top-color: #1A5276;">
    <img src="https://engg.cambridge.edu.in/wp-content/uploads/2025/05/College-Photo-2-1024x576.jpg.webp" class="card-img" alt="Cambridge Institute of Technology">
    <div class="card-body">
      <h2 class="college-name" style="color: #1A5276;">Cambridge Institute of Technology (CITech)</h2>
      <div class="college-meta">
        <span class="tag">📍 K.R. Puram</span>
        <span class="tag">🏆 Est. 2007</span>
      </div>
      <p class="card-desc">
        A NAAC A+ accredited institution known for excellent engineering programs, named research centers, and a strong focus on industry-aligned placements.
      </p>
    </div>
    <div class="card-footer">
      <a href="{{ '/colleges/cambridge/' | relative_url }}" class="view-btn" style="background: #1A5276; color: white;">View Programs ➔</a>
    </div>
  </div>

  <div class="college-card" data-category="engineering management" data-location="Bengaluru Yelahanka" style="border-top-color: #2980b9;">
    <img src="https://thecollegesphere.com/wp-content/uploads/2025/08/Brindavan-college.png" class="card-img" alt="Brindavan College of Engineering">
    <div class="card-body">
      <h2 class="college-name" style="color: #2980b9;">Brindavan College of Engineering</h2>
      <div class="college-meta">
        <span class="tag">📍 Yelahanka</span>
        <span class="tag">🏆 Est. 2008</span>
      </div>
      <p class="card-desc">
        A recognized VTU-affiliated college offering specialized programs in AI, Cyber Security, Core Engineering, MBA, MCA, and Polytechnic diplomas.
      </p>
    </div>
    <div class="card-footer">
      <a href="{{ '/colleges/brindavan/' | relative_url }}" class="view-btn" style="background: #2980b9; color: white;">View Programs ➔</a>
    </div>
  </div>

  <div class="college-card" data-category="architecture engineering" data-location="Bengaluru West" style="border-top-color: #2c3e50;">
    <img src="https://www.collegebatch.com/static/clg-gallery/east-west-school-of-architecture-167519.webp" class="card-img" alt="East West School of Architecture">
    <div class="card-body">
      <h2 class="college-name" style="color: #2c3e50;">East West School of Architecture (EWSA)</h2>
      <div class="college-meta">
        <span class="tag">📍 Vishwaneedam Post</span>
        <span class="tag">🏆 COA Approved</span>
      </div>
      <p class="card-desc">
        A dedicated VTU-affiliated architecture institution offering a comprehensive, highly-rated 5-year Bachelor of Architecture (B.Arch) program.
      </p>
    </div>
    <div class="card-footer">
      <a href="{{ '/colleges/ewsa/' | relative_url }}" class="view-btn" style="background: #2c3e50; color: white;">View Programs ➔</a>
    </div>
  </div>

  <div class="college-card" data-category="architecture" data-location="Bengaluru Yelahanka" style="border-top-color: #455A64;">
    <img src="https://aaad.in/wp-content/uploads/2017/03/1_slider-768x432.jpg" class="card-img" alt="Aditya Academy of Architecture and Design">
    <div class="card-body">
      <h2 class="college-name" style="color: #455A64;">Aditya Academy of Architecture & Design</h2>
      <div class="college-meta">
        <span class="tag">📍 Yelahanka</span>
        <span class="tag">🏆 COA Approved</span>
      </div>
      <p class="card-desc">
        A premier design institute under the Aditya Group, specializing in high-quality B.Arch and Interior Design programs with excellent studio facilities.
      </p>
    </div>
    <div class="card-footer">
      <a href="{{ '/colleges/aditya-architecture/' | relative_url }}" class="view-btn" style="background: #455A64; color: white;">View Programs ➔</a>
    </div>
  </div>

  <div class="college-card" data-category="architecture" data-location="Bengaluru Whitefield" style="border-top-color: #c0392b;">
    <img src="https://www.gopalancolleges.com/gsap/images/college-building.jpg" class="card-img" alt="Gopalan School of Architecture and Planning">
    <div class="card-body">
      <h2 class="college-name" style="color: #c0392b;">Gopalan School of Architecture & Planning</h2>
      <div class="college-meta">
        <span class="tag">📍 Whitefield</span>
        <span class="tag">🏆 COA Approved</span>
      </div>
      <p class="card-desc">
        A premium VTU-affiliated architecture institution focused on sustainable design, offering specialized B.Arch and M.Arch (Construction Project Management) degrees.
      </p>
    </div>
    <div class="card-footer">
      <a href="{{ '/colleges/gopalan/' | relative_url }}" class="view-btn" style="background: #c0392b; color: white;">View Programs ➔</a>
    </div>
  </div>

  <div class="college-card" data-category="management hospitality" data-location="Bengaluru" style="border-top-color: #d35400;">
    <img src="https://ihmbangalore.ac.in/wp-content/uploads/2024/06/EDC-3-1536x691.jpg" class="card-img" alt="IHM Bangalore">
    <div class="card-body">
      <h2 class="college-name" style="color: #d35400;">Institute of Hotel Management (IHM)</h2>
      <div class="college-meta">
        <span class="tag">📍 Seshadri Road</span>
        <span class="tag">🏆 Govt. of India</span>
      </div>
      <p class="card-desc">
        A premier public institute offering India's top B.Sc and M.Sc programs in Hospitality Administration, Food Production, and Culinary Arts.
      </p>
    </div>
    <div class="card-footer">
      <a href="{{ '/colleges/ihmb/' | relative_url }}" class="view-btn" style="background: #d35400; color: white;">View Programs ➔</a>
    </div>
  </div>

  <div class="college-card" data-category="science management" data-location="Bengaluru" style="border-top-color: #8b0000;">
    <img src="https://infoadmission.com/wp-content/uploads/2025/05/mount-carmel-college-1-1-1024x570-1.jpg" class="card-img" alt="Mount Carmel College">
    <div class="card-body">
      <h2 class="college-name" style="color: #8b0000;">Mount Carmel College (MCC)</h2>
      <div class="college-meta">
        <span class="tag">📍 Vasanth Nagar</span>
        <span class="tag">🏆 Est. 1948</span>
      </div>
      <p class="card-desc">
        A premier autonomous institution known for holistic education, empowering student culture, and excellence in Science, Commerce & Arts.
      </p>
    </div>
    <div class="card-footer">
      <a href="{{ '/colleges/mcc/' | relative_url }}" class="view-btn" style="background: #8b0000; color: white;">View Programs ➔</a>
    </div>
  </div>

  <div class="college-card" data-category="engineering management" data-location="Bengaluru South" style="border-top-color: #e65100;">
    <img src="https://www.jainuniversity.ac.in/uploads/blog/01eb9e52fb4fbc94a1c18aeca7bab841.jpg" class="card-img" alt="Jain University">
    <div class="card-body">
      <h2 class="college-name" style="color: #e65100;">Jain (Deemed-to-be University)</h2>
      <div class="college-meta">
        <span class="tag">📍 Jayanagar</span>
        <span class="tag">🏆 Est. 1990</span>
      </div>
      <p class="card-desc">
        A top-ranked university known for its emphasis on entrepreneurship, sports, and industry-integrated courses in Engineering & Management.
      </p>
    </div>
    <div class="card-footer">
      <a href="{{ '/colleges/jain-university/' | relative_url }}" class="view-btn" style="background: #e65100; color: white;">View Programs ➔</a>
    </div>
  </div>

  <div class="college-card" data-category="management science law" data-location="Bengaluru West South" style="border-top-color: #8b0000;">
    <img src="https://christuniversity.in/images/chris-building.jpg" class="card-img" alt="Christ University">
    <div class="card-body">
      <h2 class="college-name" style="color: #8b0000;">Christ (Deemed to be University)</h2>
      <div class="college-meta">
        <span class="tag">📍 Central / Kengeri</span>
        <span class="tag">🏆 Est. 1969</span>
      </div>
      <p class="card-desc">
        A multi-disciplinary powerhouse famous for high academic discipline and placements in Management (BBA/MBA), Law, and Humanities.
      </p>
    </div>
    <div class="card-footer">
      <a href="{{ '/colleges/christ-university/' | relative_url }}" class="view-btn" style="background: #8b0000; color: white;">View Programs ➔</a>
    </div>
  </div>

  <div class="college-card" data-category="science management" data-location="Bengaluru" style="border-top-color: #0A2342;">
    <img src="https://www.collegebatch.com/static/clg-gallery/st-josephs-university-bangalore-356425.webp" class="card-img" alt="St Josephs">
    <div class="card-body">
      <h2 class="college-name" style="color: #0A2342;">St. Joseph's University</h2>
      <div class="college-meta">
        <span class="tag">📍 Bengaluru</span>
        <span class="tag">🏆 Est. 1882</span>
      </div>
      <p class="card-desc">
        A heritage institution offering excellent education in Commerce, Arts, and Basic Sciences. Known for its inclusive and holistic approach.
      </p>
    </div>
    <div class="card-footer">
      <a href="{{ '/colleges/st-josephs/' | relative_url }}" class="view-btn" style="background: #0A2342; color: #D4AF37;">View Programs ➔</a>
    </div>
  </div>

  <div class="college-card" data-category="engineering" data-location="Bengaluru Basavanagudi" style="border-top-color: #0056b3;">
    <img src="https://shiksha-tech.com/wp-content/uploads/2025/12/direct_admission_in_bms_college.png" class="card-img" alt="BMSCE Bangalore">
    <div class="card-body">
      <h2 class="college-name" style="color: #0056b3;">B.M.S. College of Engineering</h2>
      <div class="college-meta">
        <span class="tag">📍 Basavanagudi</span>
        <span class="tag">🏆 Est. 1946</span>
      </div>
      <p class="card-desc">
        India's first private engineering college. Top choice for Engineering (BE/M.Tech) with outstanding placements and campus culture.
      </p>
    </div>
    <div class="card-footer">
      <a href="{{ '/colleges/bmsce/' | relative_url }}" class="view-btn" style="background: #0056b3; color: white;">View Programs ➔</a>
    </div>
  </div>

  <div class="college-card" data-category="engineering management" data-location="Bengaluru South West" style="border-top-color: #f39c12;">
    <img src="https://pes.edu/wp-content/uploads/2025/06/PESU-EC-Campus.jpg" class="card-img" alt="PES University">
    <div class="card-body">
      <h2 class="college-name" style="color: #d35400;">PES University</h2>
      <div class="college-meta">
        <span class="tag">📍 Ring Road / EC</span>
        <span class="tag">🏆 Est. 1972</span>
      </div>
      <p class="card-desc">
        Known for the PESSAT exam and rigorous academic standards. Excellent for Computer Science, Design (B.Des), and Architecture.
      </p>
    </div>
    <div class="card-footer">
      <a href="{{ '/colleges/pes-university/' | relative_url }}" class="view-btn" style="background: #d35400; color: white;">View Programs ➔</a>
    </div>
  </div>

  <div class="college-card" data-category="engineering" data-location="Bengaluru West" style="border-top-color: #008080;">
    <img src="https://www.highereducationdigest.com/wp-content/uploads/2019/04/Img-3_800x480-4-768x461.jpg" class="card-img" alt="RVCE">
    <div class="card-body">
      <h2 class="college-name" style="color: #008080;">RV College of Engineering</h2>
      <div class="college-meta">
        <span class="tag">📍 Mysore Road</span>
        <span class="tag">🏆 Est. 1963</span>
      </div>
      <p class="card-desc">
        One of the most preferred engineering colleges under VTU. Famous for its research centers, innovation, and high package placements.
      </p>
    </div>
    <div class="card-footer">
      <a href="{{ '/colleges/rvce/' | relative_url }}" class="view-btn" style="background: #008080; color: white;">View Programs ➔</a>
    </div>
  </div>

  <div class="college-card" data-category="law" data-location="Bengaluru" style="border-top-color: #c0392b;">
    <img src="https://www.lawof.in/wp-content/uploads/2020/07/NMIMS-1-1.jpg" class="card-img" alt="NMIMS Law">
    <div class="card-body">
      <h2 class="college-name" style="color: #c0392b;">Kirit P. Mehta School of Law (NMIMS)</h2>
      <div class="college-meta">
        <span class="tag">📍 Mumbai / Bengaluru</span>
        <span class="tag">🏆 Est. 2013</span>
      </div>
      <p class="card-desc">
        A top-tier private law school known for its rigorous academic curriculum, Moot Court excellence, and integration of Management with Law.
      </p>
    </div>
    <div class="card-footer">
      <a href="{{ '/colleges/kpmsol/' | relative_url }}" class="view-btn" style="background: #c0392b; color: white;">View Programs ➔</a>
    </div>
  </div>

</div>

<script>
  function filterColleges() {
    const searchInput = document.getElementById('searchInput').value.toLowerCase();
    const courseFilter = document.getElementById('courseFilter').value.toLowerCase();
    const locationFilter = document.getElementById('locationFilter').value.toLowerCase();
    
    const cards = document.getElementsByClassName("college-card");

    for (let i = 0; i < cards.length; i++) {
      const card = cards[i];
      const name = card.querySelector('.college-name').innerText.toLowerCase();
      const categories = card.getAttribute('data-category').toLowerCase();
      const locations = card.getAttribute('data-location').toLowerCase();

      // Check Criteria
      const matchesSearch = name.includes(searchInput);
      const matchesCourse = courseFilter === 'all' || categories.includes(courseFilter);
      const matchesLocation = locationFilter === 'all' || locations.includes(locationFilter);

      if (matchesSearch && matchesCourse && matchesLocation) {
        card.classList.remove("hidden");
      } else {
        card.classList.add("hidden");
      }
    }
  }

  function resetFilters() {
    document.getElementById('searchInput').value = '';
    document.getElementById('courseFilter').value = 'all';
    document.getElementById('locationFilter').value = 'all';
    filterColleges();
  }
</script>
