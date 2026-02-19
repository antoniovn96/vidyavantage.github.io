---
layout: default
title: Top Colleges & Universities 🎓
permalink: /colleges/
image: "https://images.unsplash.com/photo-1541339907198-e08756dedf3f?w=1200&h=630&fit=crop"
description: "Browse top universities in Bangalore. Get details on courses, fees, and admission processes for IISc, BIT, Jain, Christ, BMSCE, MSRIT, DSCE, NHCE, MCC, IHM Bangalore, Brindavan College and more."
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
    padding: 0 20px;
    display: flex;
    gap: 15px;
    justify-content: center;
    flex-wrap: wrap;
  }

  .filter-btn {
    padding: 10px 20px;
    border: 2px solid #ddd;
    background: white;
    border-radius: 50px;
    font-weight: 600;
    color: #555;
    cursor: pointer;
    transition: 0.2s;
    font-size: 0.95rem;
  }

  .filter-btn:hover, .filter-btn.active {
    background: #0A2342;
    color: white;
    border-color: #0A2342;
  }

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
  }
  
  .college-card:hover { transform: translateY(-5px); box-shadow: 0 15px 40px rgba(0,0,0,0.15); }
  
  /* Hide cards that don't match filter */
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
</style>

<div class="colleges-hero">
  <h1>Top Colleges & Universities</h1>
  <p>Explore the best institutions for your career path.</p>
</div>

<div class="filter-container">
  <button class="filter-btn active" onclick="filterSelection('all')">All</button>
  <button class="filter-btn" onclick="filterSelection('engineering')">Engineering</button>
  <button class="filter-btn" onclick="filterSelection('management')">Management</button>
  <button class="filter-btn" onclick="filterSelection('science')">Science & Arts</button>
  <button class="filter-btn" onclick="filterSelection('hospitality')">Hospitality</button>
  <button class="filter-btn" onclick="filterSelection('law')">Law</button>
</div>

<div class="college-grid">

  <div class="college-card category-science" style="border-top-color: #005a9c;">
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
      <a href="{{ '/colleges/iisc/' | relative_url }}" class="view-btn" style="background: #005a9c; color: white;">
        View Programs ➔
      </a>
    </div>
  </div>

  <div class="college-card category-engineering category-management category-science" style="border-top-color: #0033a0;">
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
      <a href="{{ '/colleges/bit/' | relative_url }}" class="view-btn" style="background: #0033a0; color: white;">
        View Programs ➔
      </a>
    </div>
  </div>

  <div class="college-card category-engineering" style="border-top-color: #800000;">
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
      <a href="{{ '/colleges/msrit/' | relative_url }}" class="view-btn" style="background: #800000; color: white;">
        View Programs ➔
      </a>
    </div>
  </div>

  <div class="college-card category-engineering" style="border-top-color: #003366;">
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
      <a href="{{ '/colleges/dsce/' | relative_url }}" class="view-btn" style="background: #003366; color: white;">
        View Programs ➔
      </a>
    </div>
  </div>

  <div class="college-card category-engineering" style="border-top-color: #1a237e;">
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
      <a href="{{ '/colleges/nhce/' | relative_url }}" class="view-btn" style="background: #1a237e; color: white;">
        View Programs ➔
      </a>
    </div>
  </div>

  <div class="college-card category-engineering category-management" style="border-top-color: #2980b9;">
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
      <a href="{{ '/colleges/brindavan/' | relative_url }}" class="view-btn" style="background: #2980b9; color: white;">
        View Programs ➔
      </a>
    </div>
  </div>

  <div class="college-card category-management category-hospitality" style="border-top-color: #d35400;">
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
      <a href="{{ '/colleges/ihmb/' | relative_url }}" class="view-btn" style="background: #d35400; color: white;">
        View Programs ➔
      </a>
    </div>
  </div>

  <div class="college-card category-science category-management" style="border-top-color: #8b0000;">
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
      <a href="{{ '/colleges/mcc/' | relative_url }}" class="view-btn" style="background: #8b0000; color: white;">
        View Programs ➔
      </a>
    </div>
  </div>

  <div class="college-card category-engineering category-management" style="border-top-color: #e65100;">
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
      <a href="{{ '/colleges/jain-university/' | relative_url }}" class="view-btn" style="background: #e65100; color: white;">
        View Programs ➔
      </a>
    </div>
  </div>

  <div class="college-card category-management category-science category-law" style="border-top-color: #8b0000;">
    <img src="https://christuniversity.in/images/chris-building.jpg" class="card-img" alt="Christ University">
    <div class="card-body">
      <h2 class="college-name" style="color: #8b0000;">Christ (Deemed to be University)</h2>
      <div class="college-meta">
        <span class="tag">📍 Central / Kengeri / BRC</span>
        <span class="tag">🏆 Est. 1969</span>
      </div>
      <p class="card-desc">
        A multi-disciplinary powerhouse famous for high academic discipline and placements in Management (BBA/MBA), Law, and Humanities.
      </p>
    </div>
    <div class="card-footer">
      <a href="{{ '/colleges/christ-university/' | relative_url }}" class="view-btn" style="background: #8b0000; color: white;">
        View Programs ➔
      </a>
    </div>
  </div>

  <div class="college-card category-science category-management" style="border-top-color: #0A2342;">
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
      <a href="{{ '/colleges/st-josephs/' | relative_url }}" class="view-btn" style="background: #0A2342; color: #D4AF37;">
        View Programs ➔
      </a>
    </div>
  </div>

  <div class="college-card category-engineering" style="border-top-color: #0056b3;">
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
      <a href="{{ '/colleges/bmsce/' | relative_url }}" class="view-btn" style="background: #0056b3; color: white;">
        View Programs ➔
      </a>
    </div>
  </div>

  <div class="college-card category-engineering category-management" style="border-top-color: #f39c12;">
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
      <a href="{{ '/colleges/pes-university/' | relative_url }}" class="view-btn" style="background: #d35400; color: white;">
        View Programs ➔
      </a>
    </div>
  </div>

  <div class="college-card category-engineering" style="border-top-color: #008080;">
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
      <a href="{{ '/colleges/rvce/' | relative_url }}" class="view-btn" style="background: #008080; color: white;">
        View Programs ➔
      </a>
    </div>
  </div>

  <div class="college-card category-law" style="border-top-color: #c0392b;">
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
      <a href="{{ '/colleges/kpmsol/' | relative_url }}" class="view-btn" style="background: #c0392b; color: white;">
        View Programs ➔
      </a>
    </div>
  </div>

</div>

<script>
  function filterSelection(c) {
    var x, i;
    x = document.getElementsByClassName("college-card");
    
    // Buttons Active State
    var btns = document.getElementsByClassName("filter-btn");
    for (i = 0; i < btns.length; i++) {
      btns[i].classList.remove("active");
      if(btns[i].innerText.toLowerCase().includes(c) || (c === 'all' && btns[i].innerText === 'All')) {
         btns[i].classList.add("active");
      }
    }

    if (c == "all") c = "";
    
    for (i = 0; i < x.length; i++) {
      removeClass(x[i], "hidden");
      if (x[i].className.indexOf(c) == -1 && c !== "") {
        addClass(x[i], "hidden");
      }
    }
  }

  function addClass(element, name) {
    var arr1, arr2;
    arr1 = element.className.split(" ");
    arr2 = name.split(" ");
    for (var i = 0; i < arr2.length; i++) {
      if (arr1.indexOf(arr2[i]) == -1) {element.className += " " + arr2[i];}
    }
  }

  function removeClass(element, name) {
    var arr1, arr2;
    arr1 = element.className.split(" ");
    arr2 = name.split(" ");
    for (var i = 0; i < arr2.length; i++) {
      while (arr1.indexOf(arr2[i]) > -1) {
        arr1.splice(arr1.indexOf(arr2[i]), 1);     
      }
    }
    element.className = arr1.join(" ");
  }
</script>
