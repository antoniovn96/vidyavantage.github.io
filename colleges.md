---
layout: default
title: Top Colleges & Universities 🎓
permalink: /colleges/
image: "https://images.unsplash.com/photo-1541339907198-e08756dedf3f?w=1200&h=630&fit=crop"
description: "Browse top universities in Bangalore, Roorkee, Delhi NCR & Chikkamagaluru. Filter by courses, location, and fees for IISc, IIT Roorkee, JGU, NITTE, IHM Pusa, and more."
---

<link rel="preload" as="image" href="https://images.unsplash.com/photo-1523050854058-8df90110c9f1?w=1600&auto=format&fit=crop">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Nunito:wght@400;600;700;800&family=Outfit:wght@500;700;800;900&display=swap" rel="stylesheet">

<style>
  :root {
    --bg-main: #F4F7FB;
    --text-dark: #0F172A; /* Very high contrast for headings */
    --text-muted: #334155; /* High contrast for body */
    --border-color: #CBD5E1;
    --white: #FFFFFF;
    --focus-ring: #4338CA;
  }

  /* --- 1. GLOBAL LAYOUT & ACCESSIBILITY --- */
  *, *::before, *::after { box-sizing: border-box; }
  body { background-color: var(--bg-main); font-family: 'Nunito', sans-serif; color: var(--text-muted); margin: 0; }
  h1, h2, h3, h4 { font-family: 'Outfit', sans-serif; color: var(--text-dark); margin-top: 0; letter-spacing: -0.5px; }
  p, span { line-height: 1.6; word-wrap: break-word; }

  *:focus-visible { outline: 3px solid var(--focus-ring); outline-offset: 3px; border-radius: 4px; }

  /* --- 2. HERO SECTION --- */
  .colleges-hero {
    background: linear-gradient(rgba(15, 23, 42, 0.85), rgba(15, 23, 42, 0.95)), url('https://images.unsplash.com/photo-1523050854058-8df90110c9f1?w=1600&auto=format&fit=crop');
    background-size: cover;
    background-position: center;
    color: var(--white);
    text-align: center;
    padding: 100px 20px;
    margin-bottom: 0;
  }
  .colleges-hero h1 { font-size: 3.5rem; font-weight: 900; color: var(--white); margin-bottom: 15px; }
  .colleges-hero p { font-size: 1.25rem; color: #E2E8F0; max-width: 700px; margin: 0 auto; font-weight: 600; }

  /* --- 3. FILTER COMMAND CENTER --- */
  .filter-wrapper {
    background: var(--bg-main);
    padding: 0 20px;
    position: relative;
    top: -30px;
    z-index: 10;
  }
  .filter-container {
    max-width: 1100px;
    margin: 0 auto;
    padding: 25px;
    background: var(--white);
    border-radius: 20px;
    box-shadow: 0 15px 35px rgba(0,0,0,0.06);
    display: flex;
    gap: 15px;
    justify-content: center;
    flex-wrap: wrap;
    align-items: center;
    border: 1px solid rgba(0,0,0,0.05);
  }

  .filter-input, .filter-select {
    padding: 14px 20px;
    border: 2px solid var(--border-color);
    border-radius: 12px;
    font-size: 1rem;
    font-family: 'Nunito', sans-serif;
    font-weight: 700;
    color: var(--text-dark);
    background: #F8FAFC;
    outline: none;
    transition: all 0.3s ease;
    min-height: 52px;
  }
  .filter-input { width: 300px; flex-grow: 1; max-width: 400px; }
  .filter-select { min-width: 200px; cursor: pointer; flex-grow: 1; max-width: 250px;}
  
  .filter-input:focus, .filter-select:focus, .filter-select:hover { 
    border-color: var(--focus-ring); 
    background: var(--white); 
    box-shadow: 0 0 0 4px rgba(67, 56, 202, 0.1); 
  }

  .reset-btn {
    padding: 14px 30px;
    background: #EF4444; 
    color: var(--white);
    border: none;
    border-radius: 12px;
    font-size: 1rem;
    font-family: 'Outfit', sans-serif;
    font-weight: 800;
    cursor: pointer;
    transition: 0.2s;
    min-height: 52px;
  }
  .reset-btn:hover { background: #B91C1C; transform: translateY(-2px); box-shadow: 0 4px 12px rgba(239, 68, 68, 0.3); }

  /* --- 4. GRID & CARDS --- */
  .college-grid {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(340px, 1fr));
    gap: 35px;
    padding: 20px 20px 80px;
    max-width: 1300px;
    margin: 0 auto;
  }

  /* Notice the --theme variable used below for dynamic styling */
  .college-card {
    background: var(--white);
    border-radius: 20px;
    overflow: hidden;
    box-shadow: 0 10px 30px rgba(0,0,0,0.04);
    transition: transform 0.3s ease, box-shadow 0.3s ease;
    display: flex;
    flex-direction: column;
    border: 1px solid var(--border-color);
    position: relative;
  }
  
  .college-card:hover { 
    transform: translateY(-8px); 
    box-shadow: 0 20px 40px rgba(0,0,0,0.08), 0 0 0 3px var(--theme); 
    border-color: transparent;
  }
  .college-card.hidden { display: none; }

  .card-img {
    width: 100%;
    height: 200px;
    object-fit: cover;
    background: #E2E8F0;
    border-bottom: 1px solid var(--border-color);
  }

  .card-body { padding: 30px 25px 20px; flex-grow: 1; display: flex; flex-direction: column;}
  
  .college-name { 
    margin: 0 0 15px; 
    color: var(--text-dark); 
    font-size: 1.4rem; 
    line-height: 1.3;
  }
  
  .college-meta { display: flex; flex-wrap: wrap; gap: 8px; margin-bottom: 15px; }
  
  .tag { 
    display: inline-flex; 
    align-items: center;
    background: #F1F5F9;
    color: var(--text-dark);
    padding: 6px 12px; 
    border-radius: 8px; 
    font-size: 0.85rem; 
    font-weight: 800; 
    border: 1px solid var(--border-color);
  }
  .tag-theme { background: var(--white); color: var(--theme); border-color: var(--theme); }

  .card-desc { color: var(--text-muted); font-size: 1rem; line-height: 1.6; margin-bottom: 20px; font-weight: 500; flex-grow: 1;}

  .card-footer { padding: 0 25px 30px; margin-top: auto; }

  .view-btn {
    display: block;
    width: 100%;
    text-align: center;
    padding: 14px 20px;
    border-radius: 12px;
    text-decoration: none;
    font-family: 'Outfit', sans-serif;
    font-weight: 800;
    font-size: 1.05rem;
    color: var(--white);
    background: var(--theme);
    transition: all 0.3s;
    box-shadow: 0 4px 15px rgba(0,0,0,0.1);
  }
  .view-btn:hover { opacity: 0.9; transform: translateY(-2px); box-shadow: 0 8px 20px rgba(0,0,0,0.15); }

  /* NO RESULTS STATE */
  #noResults {
    grid-column: 1 / -1;
    text-align: center;
    padding: 60px 20px;
    background: var(--white);
    border-radius: 20px;
    border: 2px dashed var(--border-color);
    display: none;
  }
  #noResults h2 { color: var(--text-dark); font-size: 1.8rem; margin-bottom: 10px;}
  #noResults p { color: var(--text-muted); font-size: 1.1rem; font-weight: 600;}

  /* Mobile Responsive */
  @media (max-width: 768px) {
    .filter-container { flex-direction: column; align-items: stretch; padding: 20px; }
    .search-input, .filter-select, .reset-btn { width: 100%; max-width: 100%; }
    .colleges-hero { padding: 60px 20px 80px; }
    .colleges-hero h1 { font-size: 2.5rem; }
    .college-grid { grid-template-columns: 1fr; }
  }
</style>

<main>
  <div class="colleges-hero">
    <h1>Top Colleges & Universities</h1>
    <p>Discover premier institutions. Filter by your targeted career path and preferred location.</p>
  </div>

  <div class="filter-wrapper">
      <div class="filter-container">
        <input type="text" id="searchInput" class="search-input" placeholder="🔍 Search College Name..." aria-label="Search College Name" onkeyup="filterColleges()">
        
        <select id="courseFilter" class="filter-select" aria-label="Filter by Course" onchange="filterColleges()">
          <option value="all">📚 All Courses</option>
          <option value="engineering">Engineering & Tech</option>
          <option value="architecture">Architecture & Design</option>
          <option value="management">Commerce & Management</option>
          <option value="science">Sciences</option>
          <option value="medicine">Medicine & Pharma</option>
          <option value="hospitality">Hospitality & Culinary</option>
          <option value="law">Law</option>
        </select>

        <select id="locationFilter" class="filter-select" aria-label="Filter by Location" onchange="filterColleges()">
          <option value="all">📍 All Locations</option>
          <option value="Bengaluru">Bengaluru (General)</option>
          <option value="New Delhi">New Delhi / NCR</option>
          <option value="Roorkee">Roorkee</option>
          <option value="Mangaluru">Mangaluru</option>
          <option value="Chikkamagaluru">Chikkamagaluru</option>
        </select>

        <button class="reset-btn" aria-label="Reset Filters" onclick="resetFilters()">Reset</button>
      </div>
  </div>

  <div class="college-grid" id="collegeGrid">

    <div class="college-card" data-category="engineering management science architecture medicine pharmacy law" data-location="Mangaluru Bengaluru Yelahanka Nitte" style="--theme: #1E3A8A;">
      <img src="https://daijiworld.ap-south-1.linodeobjects.com/Linode/images3/nitte_230224_1.jpg" class="card-img" alt="NITTE University Campus" width="400" height="200" loading="lazy" decoding="async">
      <div class="card-body">
        <h2 class="college-name">NITTE (Deemed to be University)</h2>
        <div class="college-meta">
          <span class="tag">📍 Mangaluru / Bengaluru</span>
          <span class="tag tag-theme">🏆 NAAC A+ Grade</span>
        </div>
        <p class="card-desc">
          A premier Deemed-to-be University offering 160+ elite programs across Medicine, Engineering, Management, Architecture, Pharmacy, and Sciences.
        </p>
      </div>
      <div class="card-footer">
        <a href="{{ '/colleges/nitte/' | relative_url }}" class="view-btn" aria-label="View Programs at NITTE">View Programs ➔</a>
      </div>
    </div>

    <div class="college-card" data-category="management law science" data-location="Sonipat New Delhi NCR" style="--theme: #0B2B5E;">
      <img src="https://jgu.edu.in/blog/wp-content/uploads/2020/04/CUSM-FINAL_APP8758_ACAD_AP-2048x1195.jpg" class="card-img" alt="O.P. Jindal Global University Campus" width="400" height="200" loading="lazy" decoding="async">
      <div class="card-body">
        <h2 class="college-name">O.P. Jindal Global University (JGU)</h2>
        <div class="college-meta">
          <span class="tag">📍 Sonipat (NCR)</span>
          <span class="tag tag-theme">🏆 Inst. of Eminence</span>
        </div>
        <p class="card-desc">
          India's #1 Ranked Private University. Recognized globally for its interdisciplinary approach and world-class programs in Law, Business, and Humanities.
        </p>
      </div>
      <div class="card-footer">
        <a href="{{ '/colleges/jgu-online/' | relative_url }}" class="view-btn" aria-label="View Programs at JGU">View Programs ➔</a>
      </div>
    </div>

    <div class="college-card" data-category="management hospitality" data-location="New Delhi Bengaluru" style="--theme: #00509E;">
      <img src="https://www.ciiih.com/images/about.jpg" class="card-img" alt="CII Institute of Hospitality" width="400" height="200" loading="lazy" decoding="async">
      <div class="card-body">
        <h2 class="college-name">CII Institute of Hospitality</h2>
        <div class="college-meta">
          <span class="tag">📍 Pan India</span>
          <span class="tag tag-theme">🇨🇭 Swiss Curriculum</span>
        </div>
        <p class="card-desc">
          An industry-led hospitality institute by the Confederation of Indian Industry. Offers the prestigious VET by EHL Swiss Professional Hospitality Diploma.
        </p>
      </div>
      <div class="card-footer">
        <a href="{{ '/colleges/cii-ih/' | relative_url }}" class="view-btn" aria-label="View Programs at CII IH">View Programs ➔</a>
      </div>
    </div>

    <div class="college-card" data-category="management hospitality" data-location="New Delhi" style="--theme: #B91C1C;">
      <img src="https://www.collegebatch.com/static/clg-gallery/institute-of-hotel-management-catering-nutrition-pusa-new-delhi-322357.webp" class="card-img" alt="IHM Pusa Campus Building" width="400" height="200" loading="lazy" decoding="async">
      <div class="card-body">
        <h2 class="college-name">Institute of Hotel Management (IHM) Pusa</h2>
        <div class="college-meta">
          <span class="tag">📍 New Delhi</span>
          <span class="tag tag-theme">🏆 Govt. of India</span>
        </div>
        <p class="card-desc">
          India's premier institute for Hospitality Education and Culinary Arts. Renowned for its globally recognized B.Sc, M.Sc, and specialized diploma programs.
        </p>
      </div>
      <div class="card-footer">
        <a href="{{ '/colleges/ihm-pusa/' | relative_url }}" class="view-btn" aria-label="View Programs at IHM Pusa">View Programs ➔</a>
      </div>
    </div>

    <div class="college-card" data-category="science engineering" data-location="Bengaluru Malleshwaram" style="--theme: #0369A1;">
      <img src="https://ioe.iisc.ac.in/wp-content/uploads/2021/04/bg-image-1-500x286.jpg" class="card-img" alt="IISc Bangalore Campus Building" width="400" height="200" loading="lazy" decoding="async">
      <div class="card-body">
        <h2 class="college-name">Indian Institute of Science (IISc)</h2>
        <div class="college-meta">
          <span class="tag">📍 Bengaluru</span>
          <span class="tag tag-theme">🏆 NIRF Rank #1</span>
        </div>
        <p class="card-desc">
          India's premier institute for advanced scientific research. Known for B.Sc (Research), M.Tech, and PhDs in Science & Engineering.
        </p>
      </div>
      <div class="card-footer">
        <a href="{{ '/colleges/iisc/' | relative_url }}" class="view-btn" aria-label="View Programs at IISc Bangalore">View Programs ➔</a>
      </div>
    </div>

    <div class="college-card" data-category="engineering architecture management science" data-location="Roorkee" style="--theme: #0F766E;">
      <img src="https://dynamic-media-cdn.tripadvisor.com/media/photo-o/0c/34/36/84/the-beautiful-main-building.jpg?w=1000&h=600&s=1" class="card-img" alt="IIT Roorkee Main Building" width="400" height="200" loading="lazy" decoding="async">
      <div class="card-body">
        <h2 class="college-name">IIT Roorkee</h2>
        <div class="college-meta">
          <span class="tag">📍 Roorkee</span>
          <span class="tag tag-theme">🏆 NIRF Rank #5</span>
        </div>
        <p class="card-desc">
          Asia's oldest technical institution (formerly Thomason College). Renowned for its Civil Engineering, Architecture, and strong research output.
        </p>
      </div>
      <div class="card-footer">
        <a href="{{ '/colleges/iitr/' | relative_url }}" class="view-btn" aria-label="View Programs at IIT Roorkee">View Programs ➔</a>
      </div>
    </div>

    <div class="college-card" data-category="engineering management" data-location="Chikkamagaluru" style="--theme: #047857;">
      <img src="https://images.jdmagicbox.com/comp/chikmagalur/06/9999pmulblrstd1008006/catalogue/adichunchanagiri-institute-of-technology-jyothinagar-chikmagalur-chikmagalur-colleges-bp76m2q.jpg" class="card-img" alt="Adichunchanagiri Institute of Technology Campus" width="400" height="200" loading="lazy" decoding="async">
      <div class="card-body">
        <h2 class="college-name">Adichunchanagiri Institute of Technology (AIT)</h2>
        <div class="college-meta">
          <span class="tag">📍 Chikkamagaluru</span>
          <span class="tag tag-theme">🏆 Est. 1980</span>
        </div>
        <p class="card-desc">
          A premier institute located in the scenic hills. Known for strong discipline, extensive campus facilities, and specialized Robotics/AI programs.
        </p>
      </div>
      <div class="card-footer">
        <a href="{{ '/colleges/ait/' | relative_url }}" class="view-btn" aria-label="View Programs at AIT">View Programs ➔</a>
      </div>
    </div>

    <div class="college-card" data-category="engineering management science" data-location="Bengaluru V.V. Puram" style="--theme: #1D4ED8;">
      <img src="https://bit-bangalore.edu.in/assets/images/explore/about-bit-1.jpg" class="card-img" alt="BIT Bangalore Campus" width="400" height="200" loading="lazy" decoding="async">
      <div class="card-body">
        <h2 class="college-name">Bangalore Institute of Technology (BIT)</h2>
        <div class="college-meta">
          <span class="tag">📍 V.V. Puram</span>
          <span class="tag tag-theme">🏆 Est. 1979</span>
        </div>
        <p class="card-desc">
          A reputed VTU-affiliated college located in the heart of the city. Known for strong placements in core tech and high-end research centers.
        </p>
      </div>
      <div class="card-footer">
        <a href="{{ '/colleges/bit/' | relative_url }}" class="view-btn" aria-label="View Programs at BIT">View Programs ➔</a>
      </div>
    </div>

    <div class="college-card" data-category="engineering" data-location="Bengaluru Malleshwaram" style="--theme: #991B1B;">
      <img src="https://msrit-bucket.s3.us-west-2.amazonaws.com/Gallery/rit-1.jpeg" class="card-img" alt="MSRIT Bangalore Campus" width="400" height="200" loading="lazy" decoding="async">
      <div class="card-body">
        <h2 class="college-name">Ramaiah Institute of Technology</h2>
        <div class="college-meta">
          <span class="tag">📍 Mathikere</span>
          <span class="tag tag-theme">🏆 Est. 1962</span>
        </div>
        <p class="card-desc">
          A premier autonomous engineering institute affiliated to VTU. Renowned for its academic excellence, infrastructure, and high placement records.
        </p>
      </div>
      <div class="card-footer">
        <a href="{{ '/colleges/msrit/' | relative_url }}" class="view-btn" aria-label="View Programs at MSRIT">View Programs ➔</a>
      </div>
    </div>

    <div class="college-card" data-category="engineering" data-location="Bengaluru South" style="--theme: #1E40AF;">
      <img src="https://www.admissionbangalore.com/images/engg_col/dayananda-sagar-college-of-engg.jpg" class="card-img" alt="DSCE Bangalore Campus" width="400" height="200" loading="lazy" decoding="async">
      <div class="card-body">
        <h2 class="college-name">Dayananda Sagar College of Engineering</h2>
        <div class="college-meta">
          <span class="tag">📍 South Bengaluru</span>
          <span class="tag tag-theme">🏆 Est. 1979</span>
        </div>
        <p class="card-desc">
          An autonomous institute offering the widest range of engineering branches. Known for its huge campus and excellent core placements.
        </p>
      </div>
      <div class="card-footer">
        <a href="{{ '/colleges/dsce/' | relative_url }}" class="view-btn" aria-label="View Programs at DSCE">View Programs ➔</a>
      </div>
    </div>

    <div class="college-card" data-category="engineering management" data-location="Bengaluru Marathahalli" style="--theme: #4338CA;">
      <img src="https://newhorizoncollegeofengineering.in/wp-content/uploads/2024/03/NHCE-Campus-Temple.webp" class="card-img" alt="NHCE Bangalore Campus" width="400" height="200" loading="lazy" decoding="async">
      <div class="card-body">
        <h2 class="college-name">New Horizon College of Engineering</h2>
        <div class="college-meta">
          <span class="tag">📍 Marathahalli</span>
          <span class="tag tag-theme">🏆 NAAC A Grade</span>
        </div>
        <p class="card-desc">
          An autonomous college in the heart of Bangalore's IT corridor. Famous for high placement records and integrated Minor Degree options.
        </p>
      </div>
      <div class="card-footer">
        <a href="{{ '/colleges/nhce/' | relative_url }}" class="view-btn" aria-label="View Programs at NHCE">View Programs ➔</a>
      </div>
    </div>

    <div class="college-card" data-category="engineering management science" data-location="Bengaluru K.R. Puram" style="--theme: #0369A1;">
      <img src="https://engg.cambridge.edu.in/wp-content/uploads/2025/05/College-Photo-2-1024x576.jpg.webp" class="card-img" alt="Cambridge Institute of Technology Campus" width="400" height="200" loading="lazy" decoding="async">
      <div class="card-body">
        <h2 class="college-name">Cambridge Institute of Technology (CITech)</h2>
        <div class="college-meta">
          <span class="tag">📍 K.R. Puram</span>
          <span class="tag tag-theme">🏆 NAAC A+ Grade</span>
        </div>
        <p class="card-desc">
          A highly accredited institution known for excellent engineering programs, specialized research centers, and a strong focus on industry alignment.
        </p>
      </div>
      <div class="card-footer">
        <a href="{{ '/colleges/cambridge/' | relative_url }}" class="view-btn" aria-label="View Programs at CITech">View Programs ➔</a>
      </div>
    </div>

    <div class="college-card" data-category="architecture engineering" data-location="Bengaluru West" style="--theme: #334155;">
      <img src="https://www.collegebatch.com/static/clg-gallery/east-west-school-of-architecture-167519.webp" class="card-img" alt="East West School of Architecture" width="400" height="200" loading="lazy" decoding="async">
      <div class="card-body">
        <h2 class="college-name">East West School of Architecture (EWSA)</h2>
        <div class="college-meta">
          <span class="tag">📍 West Bengaluru</span>
          <span class="tag tag-theme">🏆 COA Approved</span>
        </div>
        <p class="card-desc">
          A dedicated VTU-affiliated architecture institution offering a comprehensive, highly-rated 5-year Bachelor of Architecture (B.Arch) program.
        </p>
      </div>
      <div class="card-footer">
        <a href="{{ '/colleges/ewsa/' | relative_url }}" class="view-btn" aria-label="View Programs at EWSA">View Programs ➔</a>
      </div>
    </div>

    <div class="college-card" data-category="management hospitality" data-location="Bengaluru" style="--theme: #C2410C;">
      <img src="https://ihmbangalore.ac.in/wp-content/uploads/2024/06/EDC-3-1536x691.jpg" class="card-img" alt="IHM Bangalore" width="400" height="200" loading="lazy" decoding="async">
      <div class="card-body">
        <h2 class="college-name">Institute of Hotel Management (IHM)</h2>
        <div class="college-meta">
          <span class="tag">📍 Central Bengaluru</span>
          <span class="tag tag-theme">🏆 Govt. of India</span>
        </div>
        <p class="card-desc">
          A premier public institute offering India's top B.Sc and M.Sc programs in Hospitality Administration, Food Production, and Culinary Arts.
        </p>
      </div>
      <div class="card-footer">
        <a href="{{ '/colleges/ihmb/' | relative_url }}" class="view-btn" aria-label="View Programs at IHM Bangalore">View Programs ➔</a>
      </div>
    </div>

    <div class="college-card" data-category="science management" data-location="Bengaluru" style="--theme: #BE123C;">
      <img src="https://infoadmission.com/wp-content/uploads/2025/05/mount-carmel-college-1-1-1024x570-1.jpg" class="card-img" alt="Mount Carmel College" width="400" height="200" loading="lazy" decoding="async">
      <div class="card-body">
        <h2 class="college-name">Mount Carmel College (MCC)</h2>
        <div class="college-meta">
          <span class="tag">📍 Vasanth Nagar</span>
          <span class="tag tag-theme">🏆 Est. 1948</span>
        </div>
        <p class="card-desc">
          A premier autonomous institution known for holistic education, empowering student culture, and absolute excellence in Science, Commerce & Arts.
        </p>
      </div>
      <div class="card-footer">
        <a href="{{ '/colleges/mcc/' | relative_url }}" class="view-btn" aria-label="View Programs at Mount Carmel College">View Programs ➔</a>
      </div>
    </div>

    <div class="college-card" data-category="engineering management" data-location="Bengaluru South" style="--theme: #EA580C;">
      <img src="https://www.jainuniversity.ac.in/uploads/blog/01eb9e52fb4fbc94a1c18aeca7bab841.jpg" class="card-img" alt="Jain University" width="400" height="200" loading="lazy" decoding="async">
      <div class="card-body">
        <h2 class="college-name">Jain (Deemed-to-be University)</h2>
        <div class="college-meta">
          <span class="tag">📍 Jayanagar / Kanakapura</span>
          <span class="tag tag-theme">🏆 NAAC A++ Grade</span>
        </div>
        <p class="card-desc">
          A top-ranked university known for its massive emphasis on entrepreneurship, national sports, and industry-integrated modern courses.
        </p>
      </div>
      <div class="card-footer">
        <a href="{{ '/colleges/jain-university/' | relative_url }}" class="view-btn" aria-label="View Programs at Jain University">View Programs ➔</a>
      </div>
    </div>

    <div class="college-card" data-category="management science law" data-location="Bengaluru West South" style="--theme: #9F1239;">
      <img src="https://christuniversity.in/images/chris-building.jpg" class="card-img" alt="Christ University" width="400" height="200" loading="lazy" decoding="async">
      <div class="card-body">
        <h2 class="college-name">Christ (Deemed to be University)</h2>
        <div class="college-meta">
          <span class="tag">📍 Central / Kengeri</span>
          <span class="tag tag-theme">🏆 Est. 1969</span>
        </div>
        <p class="card-desc">
          A multi-disciplinary powerhouse famous for high academic discipline and elite placements in Management (BBA/MBA), Law, and Humanities.
        </p>
      </div>
      <div class="card-footer">
        <a href="{{ '/colleges/christ-university/' | relative_url }}" class="view-btn" aria-label="View Programs at Christ University">View Programs ➔</a>
      </div>
    </div>

  </div>

  <div id="noResults">
      <div style="font-size: 4rem; margin-bottom: 15px;">🔍</div>
      <h2>No colleges found matching your criteria.</h2>
      <p>Try adjusting your search terms or expanding your filters.</p>
  </div>

</main>

<script>
  function filterColleges() {
    const searchInput = document.getElementById('searchInput').value.toLowerCase();
    const courseFilter = document.getElementById('courseFilter').value.toLowerCase();
    const locationFilter = document.getElementById('locationFilter').value.toLowerCase();
    
    const cards = document.getElementsByClassName("college-card");
    const noResults = document.getElementById('noResults');
    let visibleCount = 0;

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
        visibleCount++;
      } else {
        card.classList.add("hidden");
      }
    }

    // Toggle No Results Message
    if (visibleCount === 0) {
        noResults.style.display = "block";
    } else {
        noResults.style.display = "none";
    }
  }

  function resetFilters() {
    document.getElementById('searchInput').value = '';
    document.getElementById('courseFilter').value = 'all';
    document.getElementById('locationFilter').value = 'all';
    filterColleges();
  }
</script>
