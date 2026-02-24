---
layout: default
title: Career Blog
permalink: /blog/
---

<style>
  /* --- PAGE HEADER --- */
  .blog-header { text-align: center; padding: 80px 20px; background: #0A2342; color: white; margin-bottom: 40px; }
  .blog-header h1 { font-size: 2.8rem; margin: 0 0 10px 0; }
  .blog-header p { font-size: 1.2rem; color: #e3f2fd; max-width: 600px; margin: 0 auto; }

  /* --- MAIN LAYOUT (Two Column) --- */
  .blog-layout { display: grid; grid-template-columns: 280px 1fr; gap: 40px; max-width: 1200px; margin: 0 auto; padding: 0 20px 60px; }

  /* --- SIDEBAR (Left Side) --- */
  .blog-sidebar { position: sticky; top: 100px; height: max-content; }
  
  .sidebar-section-title { font-size: 1.1rem; color: #0A2342; font-weight: 800; border-bottom: 2px solid #eee; padding-bottom: 10px; margin-bottom: 20px; text-transform: uppercase; letter-spacing: 0.5px;}

  /* Search Bar */
  .search-container { margin-bottom: 40px; position: relative;}
  .search-input { width: 100%; padding: 14px 15px 14px 40px; border: 2px solid #ddd; border-radius: 8px; font-size: 1rem; box-sizing: border-box; font-family: inherit; transition: 0.3s; background: white;}
  .search-input:focus { border-color: #0A2342; outline: none; box-shadow: 0 0 0 3px rgba(10, 35, 66, 0.1); }
  .search-icon { position: absolute; left: 12px; top: 15px; color: #999; font-size: 1.2rem; }

  /* Filter Buttons (Stacked) */
  .filter-list { display: flex; flex-direction: column; gap: 10px; }
  .filter-btn { background: #f8fafc; border: 1px solid #e2e8f0; color: #334155; padding: 12px 20px; cursor: pointer; border-radius: 8px; font-weight: bold; transition: all 0.2s; text-align: left; display: flex; justify-content: space-between; align-items: center;}
  .filter-btn:hover { background: #e2e8f0; }
  .filter-btn.active { background: #0A2342; border-color: #0A2342; color: white; }
  .filter-btn.active::after { content: '✓'; color: #D4AF37; }

  /* --- BLOG GRID (Right Side) --- */
  .blog-grid { display: grid; grid-template-columns: repeat(auto-fill, minmax(280px, 1fr)); gap: 30px; align-items: start; }
  
  .blog-card { 
    display: flex; flex-direction: column;
    border: 1px solid #e2e8f0; 
    border-radius: 12px; 
    overflow: hidden; 
    transition: transform 0.3s, box-shadow 0.3s; 
    background: white; 
    text-decoration: none !important; 
    color: inherit; 
    height: 100%;
  }
  .blog-card:hover { transform: translateY(-5px); box-shadow: 0 15px 30px rgba(0,0,0,0.1); border-color: #cbd5e1;}
  
  .blog-img { width: 100%; height: 200px; object-fit: cover; border-bottom: 1px solid #e2e8f0; }
  .blog-content { padding: 25px; display: flex; flex-direction: column; flex-grow: 1;}
  .blog-tag { align-self: flex-start; background: #e3f2fd; color: #0A2342; padding: 5px 12px; border-radius: 6px; font-size: 0.75rem; font-weight: 800; text-transform: uppercase; margin-bottom: 15px; }
  .blog-title { margin: 0 0 10px 0; color: #0A2342; font-size: 1.25rem; font-weight: 800; line-height: 1.4;}
  .blog-excerpt { color: #64748b; font-size: 0.95rem; line-height: 1.6; flex-grow: 1; margin: 0 0 20px 0;}
  .read-more { color: #D4AF37; font-weight: 800; display: inline-flex; align-items: center; gap: 5px; font-size: 0.9rem;}

  /* Empty State */
  .no-results { grid-column: 1 / -1; text-align: center; padding: 50px 20px; color: #64748b; font-size: 1.2rem; display: none; background: #f8fafc; border-radius: 12px; border: 2px dashed #cbd5e1;}

  /* RESPONSIVE */
  @media (max-width: 900px) {
    .blog-layout { grid-template-columns: 1fr; }
    .blog-sidebar { position: static; margin-bottom: 20px; }
    .filter-list { flex-direction: row; flex-wrap: wrap; }
    .filter-btn { flex: 1 1 calc(50% - 10px); }
  }
  @media (max-width: 500px) {
    .filter-btn { flex: 1 1 100%; }
  }
</style>

<div class="blog-header">
  <h1>The Career Intel Blog</h1>
  <p>Verified clinical insights on career paths, institutional data, and the psychology of student success.</p>
</div>

<div class="blog-layout">
  
  <aside class="blog-sidebar">
    <div class="search-container">
      <h3 class="sidebar-section-title">Search</h3>
      <span class="search-icon">🔍</span>
      <input type="text" id="searchInput" class="search-input" placeholder="Search keywords, topics...">
    </div>

    <div class="filter-container">
      <h3 class="sidebar-section-title">Categories</h3>
      <div class="filter-list">
        <button class="filter-btn active" onclick="setCategory('all', this)">All Research</button>
        <button class="filter-btn" onclick="setCategory('study-abroad', this)">Study Abroad & Visas</button>
        <button class="filter-btn" onclick="setCategory('psychology', this)">Student Psychology</button>
        <button class="filter-btn" onclick="setCategory('admissions', this)">Admissions & Exams</button>
      </div>
    </div>
  </aside>

  <main class="blog-main">
    <div class="blog-grid" id="blogGrid">
      
      {% for post in site.posts %}
      <a href="{{ post.url | relative_url }}" class="blog-card" data-category="{{ post.category }}">
        {% if post.image %}
        <img src="{{ post.image }}" class="blog-img" alt="{{ post.title }}">
        {% else %}
        <img src="https://images.unsplash.com/photo-1454165804606-c3d57bc86b40?auto=format&fit=crop&w=600&q=80" class="blog-img" alt="Blog Image">
        {% endif %}
        
        <div class="blog-content">
          <span class="blog-tag">{{ post.category_label | default: post.category }}</span>
          <h3 class="blog-title">{{ post.title }}</h3>
          <p class="blog-excerpt">{{ post.excerpt | strip_html | truncatewords: 18 }}</p>
          <span class="read-more">Read Full Article →</span>
        </div>
      </a>
      {% endfor %}

      <div class="no-results" id="noResultsMsg">
        No articles found matching your criteria. Try adjusting your search!
      </div>

    </div>
  </main>

</div>

<script>
  // State variables to track both search and category
  let currentCategory = 'all';
  let currentSearchTerm = '';

  // 1. Handle Category Clicks
  function setCategory(cat, btnElement) {
    currentCategory = cat;
    
    // Update active button styles
    document.querySelectorAll('.filter-btn').forEach(b => b.classList.remove('active'));
    btnElement.classList.add('active');
    
    applyFilters();
  }

  // 2. Handle Search Bar Typing
  document.getElementById('searchInput').addEventListener('input', function(e) {
    currentSearchTerm = e.target.value.toLowerCase().trim();
    applyFilters();
  });

  // 3. The Master Filter Engine
  function applyFilters() {
    const cards = document.querySelectorAll('.blog-card');
    let visibleCount = 0;

    cards.forEach(card => {
      // Get data from the card
      const cardCat = card.getAttribute('data-category');
      const titleText = card.querySelector('.blog-title').innerText.toLowerCase();
      const excerptText = card.querySelector('.blog-excerpt').innerText.toLowerCase();

      // Check Category Match
      const matchesCategory = (currentCategory === 'all' || cardCat === currentCategory);
      
      // Check Search Match
      const matchesSearch = (titleText.includes(currentSearchTerm) || excerptText.includes(currentSearchTerm));

      // Show/Hide Logic
      if (matchesCategory && matchesSearch) {
        card.style.display = 'flex'; // Use flex to maintain the card layout
        visibleCount++;
      } else {
        card.style.display = 'none';
      }
    });

    // Show or hide the "No Results" message
    const noResults = document.getElementById('noResultsMsg');
    if (visibleCount === 0) {
      noResults.style.display = 'block';
    } else {
      noResults.style.display = 'none';
    }
  }
</script>
