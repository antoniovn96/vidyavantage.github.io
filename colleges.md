---
layout: default
title: Top Colleges & Universities 🎓
permalink: /colleges/
image: "https://images.unsplash.com/photo-1541339907198-e08756dedf3f?w=1200&h=630&fit=crop"
description: "Browse top universities in Bangalore. Get details on courses, fees, and admission processes for IISc, RVCE, PESU, Christ, and St. Joseph's."
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

  /* 2. GRID LAYOUT */
  .college-grid {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(350px, 1fr));
    gap: 30px;
    padding: 0 20px 60px;
    max-width: 1200px;
    margin: 0 auto;
  }

  /* 3. COLLEGE CARD */
  .college-card {
    background: white;
    border-radius: 12px;
    overflow: hidden;
    box-shadow: 0 10px 30px rgba(0,0,0,0.08);
    transition: transform 0.3s, box-shadow 0.3s;
    display: flex;
    flex-direction: column;
    border-top: 5px solid #0A2342;
  }
  
  .college-card:hover { transform: translateY(-5px); box-shadow: 0 15px 40px rgba(0,0,0,0.15); }

  .card-img {
    width: 100%;
    height: 180px;
    object-fit: cover;
  }

  .card-body { padding: 25px; flex-grow: 1; }
  
  .college-name { 
    margin: 0 0 10px; 
    color: #0A2342; 
    font-size: 1.4rem; 
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
</style>

<div class="colleges-hero">
  <h1>Top Colleges & Universities</h1>
  <p>Explore the best institutions for your career path.</p>
</div>

<div class="college-grid">

  <div class="college-card" style="border-top-color: #005a9c;">
    <img src="https://iisc.ac.in/wp-content/uploads/2020/08/main-building.jpg" class="card-img" alt="IISc Bangalore">
    <div class="card-body">
      <h2 class="college-name" style="color: #005a9c;">Indian Institute of Science (IISc)</h2>
      <div class="college-meta">
        <span class="tag">📍 Bengaluru</span>
        <span class="tag">🏆 NIRF Rank #1</span>
      </div>
      <p class="card-desc">
        India's premier institute for advanced scientific and technological research. Offers B.Sc (Research), B.Tech in Mathematics & Computing, M.Tech, and PhD programs.
      </p>
    </div>
    <div class="card-footer">
      <a href="{{ '/colleges/iisc/' | relative_url }}" class="view-btn" style="background: #005a9c; color: white;">
        View Programs ➔
      </a>
    </div>
  </div>

  <div class="college-card" style="border-top-color: #FFC107;">
    <img src="https://rvce.edu.in/sites/default/files/slider/slider1.jpg" class="card-img" alt="RVCE Bangalore">
    <div class="card-body">
      <h2 class="college-name" style="color: #003366;">RV College of Engineering</h2>
      <div class="college-meta">
        <span class="tag">📍 Mysuru Road</span>
        <span class="tag">🏆 Est. 1963</span>
      </div>
      <p class="card-desc">
        Bangalore's most preferred engineering college. Known for high academic rigor, excellent placements in CSE/ISE, and vibrant campus life.
      </p>
    </div>
    <div class="card-footer">
      <a href="{{ '/colleges/rvce/' | relative_url }}" class="view-btn" style="background: #003366; color: #FFC107;">
        View Programs ➔
      </a>
    </div>
  </div>

  <div class="college-card" style="border-top-color: #FF6600;">
    <img src="https://pes.edu/wp-content/uploads/2022/07/PES-University-Banner.jpg" class="card-img" alt="PES University">
    <div class="card-body">
      <h2 class="college-name" style="color: #003366;">PES University</h2>
      <div class="college-meta">
        <span class="tag">📍 Ring Road / EC</span>
        <span class="tag">🏆 Est. 1972</span>
      </div>
      <p class="card-desc">
        A leading private university known for its rigorous academic curriculum and high-tech campus. Famous for CSE placements and the PESSAT entrance exam.
      </p>
    </div>
    <div class="card-footer">
      <a href="{{ '/colleges/pes-university/' | relative_url }}" class="view-btn" style="background: #003366; color: white;">
        View Programs ➔
      </a>
    </div>
  </div>

  <div class="college-card" style="border-top-color: #8b0000;">
    <img src="https://christuniversity.in/images/sharingLogo.jpg" class="card-img" alt="Christ University">
    <div class="card-body">
      <h2 class="college-name" style="color: #8b0000;">Christ (Deemed to be University)</h2>
      <div class="college-meta">
        <span class="tag">📍 Central / Kengeri / BRC</span>
        <span class="tag">🏆 Est. 1969</span>
      </div>
      <p class="card-desc">
        A premier multi-disciplinary university famous for its high academic discipline, vibrant campus culture, and top-tier placements in Management and Law.
      </p>
    </div>
    <div class="card-footer">
      <a href="{{ '/colleges/christ-university/' | relative_url }}" class="view-btn" style="background: #8b0000; color: white;">
        View Courses ➔
      </a>
    </div>
  </div>

  <div class="college-card">
    <img src="https://images.unsplash.com/photo-1562774053-701939374585?w=600&h=300&fit=crop" class="card-img" alt="St Josephs">
    <div class="card-body">
      <h2 class="college-name">St. Joseph's University</h2>
      <div class="college-meta">
        <span class="tag">📍 Bengaluru</span>
        <span class="tag">🏆 Est. 1882</span>
      </div>
      <p class="card-desc">
        One of the oldest and most prestigious institutions in Bangalore. Known for excellence in Commerce, Humanities, and Basic Sciences with a strong focus on holistic development.
      </p>
    </div>
    <div class="card-footer">
      <a href="{{ '/colleges/st-josephs/' | relative_url }}" class="view-btn" style="background: #0A2342; color: #D4AF37;">
        View Courses ➔
      </a>
    </div>
  </div>

</div>
