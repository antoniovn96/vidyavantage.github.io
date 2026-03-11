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
    --text-dark: #0F172A; 
    --text-muted: #334155; 
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
    </div>

  <div id="noResults">
      <div style="font-size: 4rem; margin-bottom: 15px;">🔍</div>
      <h2>No colleges found matching your criteria.</h2>
      <p>Try adjusting your search terms or expanding your filters.</p>
  </div>

</main>

<script>
  let collegeData = []; 
  const grid = document.getElementById('collegeGrid');
  const noResults = document.getElementById('noResults');

  // 1. Fetch the data from your colleges.json file
  fetch("{{ '/colleges.json' | relative_url }}")
    .then(response => {
      if (!response.ok) {
        throw new Error("Could not load colleges.json. Make sure the file exists in your repository.");
      }
      return response.json();
    })
    .then(data => {
      collegeData = data;
      renderCards(collegeData); // Draw the cards when page loads
    })
    .catch(error => {
      console.error("Database Error:", error);
      grid.innerHTML = `<p style="text-align:center; color: red; grid-column: 1/-1;">Error loading college data. Have you created colleges.json yet?</p>`;
    });

  // 2. The function that builds your HTML cards
  function renderCards(data) {
    grid.innerHTML = ''; 
    
    if (data.length === 0) {
      noResults.style.display = "block";
      return;
    }
    noResults.style.display = "none";

    const cardsHTML = data.map(college => `
      <div class="college-card" style="--theme: ${college.theme || '#1E3A8A'};">
        <img src="${college.image}" class="card-img" alt="${college.name} Campus" width="400" height="200" loading="lazy">
        <div class="card-body">
          <h2 class="college-name">${college.name}</h2>
          <div class="college-meta">
            <span class="tag">📍 ${college.displayLocation}</span>
            <span class="tag tag-theme">🏆 ${college.accreditation}</span>
          </div>
          <p class="card-desc">${college.description}</p>
        </div>
        <div class="card-footer">
          <a href="${college.url}" class="view-btn" aria-label="View Programs at ${college.name}">View Programs ➔</a>
        </div>
      </div>
    `).join('');

    grid.innerHTML = cardsHTML;
  }

  // 3. The completely upgraded Filter Function
  function filterColleges() {
    const searchInput = document.getElementById('searchInput').value.toLowerCase();
    const courseFilter = document.getElementById('courseFilter').value.toLowerCase();
    const locationFilter = document.getElementById('locationFilter').value.toLowerCase();

    const filteredData = collegeData.filter(c => {
      const matchesSearch = c.name.toLowerCase().includes(searchInput) || 
                            c.description.toLowerCase().includes(searchInput);
      
      const matchesCourse = courseFilter === 'all' || 
                           (c.category && c.category.toLowerCase().includes(courseFilter));
                           
      const matchesLocation = locationFilter === 'all' || 
                             (c.location && c.location.toLowerCase().includes(locationFilter));
      
      return matchesSearch && matchesCourse && matchesLocation;
    });

    renderCards(filteredData); 
  }

  // 4. Reset Function
  function resetFilters() {
    document.getElementById('searchInput').value = '';
    document.getElementById('courseFilter').value = 'all';
    document.getElementById('locationFilter').value = 'all';
    renderCards(collegeData); 
  }
</script>
