---
layout: default
title: Career Blog
permalink: /blog/
---

<style>
  /* --- GLOBAL RESETS & BACKGROUND --- */
  body {
    background-color: #f8fafc; 
    font-family: 'Inter', 'Nunito', system-ui, -apple-system, sans-serif;
    text-rendering: optimizeLegibility;
    color: #1F2937;
    margin: 0;
  }

  /* --- PREMIUM PAGE HEADER --- */
  .blog-header { 
    text-align: center; 
    padding: 100px 20px; 
    background: radial-gradient(circle at top right, #1e1b4b, #0f172a); 
    color: #ffffff; 
    margin-bottom: 60px;
    position: relative;
    overflow: hidden;
    border-bottom: 4px solid #3b82f6;
    box-shadow: 0 10px 30px rgba(0,0,0,0.1);
  }
  
  .blog-header::before {
    content: '';
    position: absolute;
    top: 0; left: 0; right: 0; bottom: 0;
    background-image: radial-gradient(rgba(255,255,255,0.1) 1px, transparent 1px);
    background-size: 20px 20px;
    opacity: 0.5;
    pointer-events: none;
  }

  .blog-header h1 { 
    font-size: 3.5rem; 
    font-weight: 900; 
    margin: 0 0 15px 0; 
    position: relative;
    z-index: 1;
    background: -webkit-linear-gradient(45deg, #60a5fa, #ffffff);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    color: white; /* Fallback */
    letter-spacing: -1px;
  }
  
  .blog-header p { 
    font-size: 1.25rem; 
    color: #cbd5e1; 
    max-width: 650px; 
    margin: 0 auto; 
    position: relative;
    z-index: 1;
    line-height: 1.6;
  }

  /* --- MAIN LAYOUT (Two Column) --- */
  .blog-layout { 
    display: grid; 
    grid-template-columns: 300px 1fr; 
    gap: 40px; 
    max-width: 1250px; 
    margin: 0 auto; 
    padding: 0 20px 80px; 
  }

  /* --- FLOATING SIDEBAR (Left Side) --- */
  .blog-sidebar { 
    position: sticky; 
    top: 100px; 
    height: max-content; 
    background: white;
    padding: 30px;
    border-radius: 20px;
    box-shadow: 0 15px 35px rgba(0,0,0,0.05);
    border: 1px solid #f1f5f9;
  }
  
  .sidebar-section-title { 
    font-size: 0.95rem; 
    color: #4B5563; /* Darkened for Contrast */
    font-weight: 800; 
    text-transform: uppercase; 
    letter-spacing: 1px;
    margin-top: 0;
    margin-bottom: 15px;
  }

  /* Modern Pill Search Bar */
  .search-container { margin-bottom: 40px; position: relative;}
  .search-input { 
    width: 100%; 
    padding: 15px 20px 15px 45px; 
    border: 2px solid #e2e8f0; 
    border-radius: 50px; /* Pill shape */
    font-size: 1rem; 
    box-sizing: border-box; 
    transition: all 0.3s ease; 
    background: #f8fafc;
    min-height: 48px; /* Touch Target Fix */
    color: #1F2937;
  }
  .search-input:focus { 
    background: white;
    border-color: #3b82f6; 
    outline: none; 
    box-shadow: 0 0 0 4px rgba(59, 130, 246, 0.1); 
  }
  .search-icon { position: absolute; left: 18px; top: 16px; color: #64748b; font-size: 1.2rem; }

  /* Premium Filter Buttons */
  .filter-list { display: flex; flex-direction: column; gap: 8px; }
  .filter-btn { 
    background: transparent; 
    border: none; 
    color: #374151; /* Perfect Contrast */
    padding: 12px 20px; 
    cursor: pointer; 
    border-radius: 12px; 
    font-weight: 700; 
    transition: all 0.2s; 
    text-align: left; 
    font-size: 1rem;
    display: flex;
    justify-content: space-between;
    align-items: center;
    min-height: 48px; /* Touch Target Fix */
    touch-action: manipulation;
  }
  .filter-btn:hover, .filter-btn:focus { background: #f1f5f9; color: #0f172a; transform: translateX(5px); outline: none;}
  
  .filter-btn.active { 
    background: #eff6ff; 
    color: #1d4ed8; /* Darker blue for contrast */
  }
  .filter-btn.active::after { 
    content: '●'; 
    color: #2563eb; 
    font-size: 0.8rem;
  }

  /* --- BLOG GRID (Right Side) --- */
  .blog-grid { 
    display: grid; 
    grid-template-columns: repeat(auto-fill, minmax(320px, 1fr)); 
    gap: 30px; 
    align-items: start; 
  }
  
  .blog-card { 
    display: flex; flex-direction: column;
    border: 1px solid #e2e8f0; 
    border-radius: 20px; 
    overflow: hidden; 
    transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275); /* Bouncy transition */
    background: white; 
    text-decoration: none !important; 
    color: inherit; 
    height: 100%;
    box-shadow: 0 4px 15px rgba(0,0,0,0.03);
    content-visibility: auto; /* Performance Optimization */
  }
  
  .blog-card:hover { 
    transform: translateY(-10px); 
    box-shadow: 0 25px 50px rgba(0,0,0,0.1); 
    border-color: #cbd5e1;
  }
  
  /* CLS Fix: Strict Aspect Ratio */
  .card-img-wrapper { 
    overflow: hidden; 
    aspect-ratio: 3/2; 
    background: #f1f5f9; /* Skeleton load color */
  }
  .blog-img { width: 100%; height: 100%; object-fit: cover; transition: transform 0.5s ease; }
  .blog-card:hover .blog-img { transform: scale(1.08); } /* Image zoom on hover */

  .blog-content { padding: 30px; display: flex; flex-direction: column; flex-grow: 1;}
  
  .blog-tag { 
    align-self: flex-start; 
    background: rgba(59, 130, 246, 0.1); 
    color: #1d4ed8; /* Contrast Fix */
    padding: 6px 14px; 
    border-radius: 50px; 
    font-size: 0.75rem; 
    font-weight: 800; 
    text-transform: uppercase; 
    margin-bottom: 15px; 
  }
  
  .blog-title { margin: 0 0 15px 0; color: #0f172a; font-size: 1.3rem; font-weight: 900; line-height: 1.4;}
  .blog-excerpt { color: #4B5563; font-size: 1rem; line-height: 1.6; flex-grow: 1; margin: 0 0 25px 0;} /* Contrast Fix */
  
  .read-more { 
    color: #D97706; /* Accessible Amber */
    font-weight: 800; 
    display: inline-flex; 
    align-items: center; 
    gap: 5px; 
    font-size: 0.95rem;
    transition: 0.2s;
  }
  .blog-card:hover .read-more { gap: 10px; color: #b45309;}

  /* Empty State */
  .no-results { 
    grid-column: 1 / -1; 
    text-align: center; 
    padding: 60px 20px; 
    color: #4B5563; 
    font-size: 1.2rem; 
    display: none; 
    background: white; 
    border-radius: 20px; 
    box-shadow: 0 10px 25px rgba(0,0,0,0.05);
    border: 1px solid #e2e8f0;
  }

  /* RESPONSIVE */
  @media (max-width: 900px) {
    .blog-layout { grid-template-columns: 1fr; }
    .blog-sidebar { position: static; margin-bottom: 20px; z-index: 10;}
    .filter-list { flex-direction: row; flex-wrap: wrap; }
    .filter-btn { flex: 1 1 calc(50% - 10px); justify-content: center;}
  }
  @media (max-width: 500px) {
    .filter-btn { flex: 1 1 100%; }
    .blog-header h1 { font-size: 2.5rem; }
  }
</style>

<main>
  <header class="blog-header">
    <h1>The Career Intel Blog</h1>
    <p>Verified clinical insights on career paths, institutional data, and the psychology of student success.</p>
  </header>

  <div class="blog-layout">
    
    <aside class="blog-sidebar">
      <div class="search-container">
        <h2 class="sidebar-section-title">Search Library</h2>
        <span class="search-icon" aria-hidden="true">🔍</span>
        <input type="text" id="searchInput" class="search-input" placeholder="Keywords, topics..." aria-label="Search blog posts">
      </div>

      <div class="filter-container">
        <h2 class="sidebar-section-title">Categories</h2>
        <div class="filter-list" role="tablist">
          <button class="filter-btn active" onclick="setCategory('all', this)" role="tab" aria-selected="true">All Research</button>
          
          <button class="filter-btn" onclick="setCategory('career-guidance', this)" role="tab" aria-selected="false">Career Guidance</button>
          
          <button class="filter-btn" onclick="setCategory('study-abroad', this)" role="tab" aria-selected="false">Study Abroad & Visas</button>
          <button class="filter-btn" onclick="setCategory('psychology', this)" role="tab" aria-selected="false">Student Psychology</button>
          <button class="filter-btn" onclick="setCategory('admissions', this)" role="tab" aria-selected="false">Admissions & Exams</button>
        </div>
      </div>
    </aside>

    <section class="blog-main">
      <div class="blog-grid" id="blogGrid">
        
        {% for post in site.posts %}
        <a href="{{ post.url | relative_url }}" class="blog-card" data-category="{{ post.category }}" aria-label="Read article: {{ post.title }}">
          
          <div class="card-img-wrapper">
              {% if post.image %}
              <img src="{{ post.image }}" class="blog-img" alt="{{ post.title }}" width="600" height="400" loading="lazy" decoding="async">
              {% else %}
              <img src="https://images.unsplash.com/photo-1454165804606-c3d57bc86b40?auto=format&fit=crop&w=600&q=80" class="blog-img" alt="Blog Image" width="600" height="400" loading="lazy" decoding="async">
              {% endif %}
          </div>
          
          <div class="blog-content">
            <span class="blog-tag">{{ post.category_label | default: post.category }}</span>
            <h3 class="blog-title">{{ post.title }}</h3>
            <p class="blog-excerpt">{{ post.excerpt | strip_html | truncatewords: 18 }}</p>
            <span class="read-more" aria-hidden="true">Read Full Article <span style="font-size:1.2em;">→</span></span>
          </div>
        </a>
        {% endfor %}

        <div class="no-results" id="noResultsMsg" aria-live="polite">
          <div style="font-size: 3rem; margin-bottom: 15px;" aria-hidden="true">🕵️‍♂️</div>
          <strong>No articles found.</strong><br>Try adjusting your search terms or selecting a different category.
        </div>

      </div>
    </section>

  </div>
</main>

<script>
  // State variables to track both search and category
  let currentCategory = 'all';
  let currentSearchTerm = '';

  // 1. Handle Category Clicks
  function setCategory(cat, btnElement) {
    currentCategory = cat;
    
    // Update active button styles and ARIA states
    document.querySelectorAll('.filter-btn').forEach(b => {
      b.classList.remove('active');
      b.setAttribute('aria-selected', 'false');
    });
    btnElement.classList.add('active');
    btnElement.setAttribute('aria-selected', 'true');
    
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
