---
layout: default
title: Career Blog
permalink: /blog/
---

<style>
  .blog-header { text-align: center; padding: 60px 20px; background: #0A2342; color: white; margin-bottom: 40px; }
  
  /* Filter Buttons */
  .filter-bar { text-align: center; margin-bottom: 40px; }
  .filter-btn { background: white; border: 1px solid #0A2342; color: #0A2342; padding: 10px 20px; margin: 5px; cursor: pointer; border-radius: 50px; font-weight: bold; transition: all 0.3s; }
  .filter-btn.active, .filter-btn:hover { background: #D4AF37; border-color: #D4AF37; color: #0A2342; }
  
  /* Blog Grid */
  .blog-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 30px; }
  
  /* The Card - Now a Link */
  .blog-card { 
    display: block; /* Makes the anchor behave like a box */
    border: 1px solid #ddd; 
    border-radius: 10px; 
    overflow: hidden; 
    transition: transform 0.3s, box-shadow 0.3s; 
    background: white; 
    text-decoration: none !important; /* Removes blue underline */
    color: inherit; /* Keeps text color normal */
  }
  
  .blog-card:hover { transform: translateY(-5px); box-shadow: 0 10px 20px rgba(0,0,0,0.15); }
  
  .blog-img { width: 100%; height: 200px; object-fit: cover; }
  .blog-content { padding: 20px; }
  .blog-tag { background: #e3f2fd; color: #0A2342; padding: 5px 10px; border-radius: 5px; font-size: 0.8rem; font-weight: bold; }
  .blog-title { margin: 15px 0 10px; color: #0A2342; font-size: 1.3rem; font-weight: bold; }
  .read-more { color: #D4AF37; font-weight: bold; margin-top: 10px; display: inline-block; }
</style>

<div class="blog-header">
  <h1>The Career Intel Blog</h1>
  <p>Verified insights on Exams, Visas, and the Future of Work.</p>
</div>

<div class="filter-bar">
  <button class="filter-btn active" onclick="filterPosts('all')">All</button>
  <button class="filter-btn" onclick="filterPosts('study-abroad')">Study Abroad</button>
  <button class="filter-btn" onclick="filterPosts('class-10-12')">Class 10-12</button>
  <button class="filter-btn" onclick="filterPosts('money')">Scholarships & Money</button>
</div>

<div class="blog-grid">
  {% for post in site.posts %}
  <a href="{{ post.url | relative_url }}" class="blog-card" data-category="{{ post.category }}">
    <img src="{{ post.image }}" class="blog-img" alt="{{ post.title }}">
    <div class="blog-content">
      <span class="blog-tag">{{ post.category_label }}</span>
      <h3 class="blog-title">{{ post.title }}</h3>
      <p style="color: #666; font-size: 0.95rem;">{{ post.excerpt | strip_html | truncatewords: 15 }}</p>
      <span class="read-more">Read Article →</span>
    </div>
  </a>
  {% endfor %}
</div>

<script>
  function filterPosts(cat) {
    const cards = document.querySelectorAll('.blog-card');
    const btns = document.querySelectorAll('.filter-btn');
    
    // Update active button visual
    btns.forEach(b => {
        b.classList.remove('active');
        if(event.target === b) b.classList.add('active');
    });

    // Show/Hide cards logic
    cards.forEach(card => {
      if (cat === 'all' || card.getAttribute('data-category') === cat) {
        card.style.display = 'block';
      } else {
        card.style.display = 'none';
      }
    });
  }
</script>
