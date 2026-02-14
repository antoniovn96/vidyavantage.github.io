---
layout: default
title: Career Blog
permalink: /blog/
---

<style>
  .blog-header { text-align: center; padding: 60px 20px; background: #0A2342; color: white; margin-bottom: 40px; }
  .filter-bar { text-align: center; margin-bottom: 40px; }
  .filter-btn { background: white; border: 1px solid #0A2342; color: #0A2342; padding: 10px 20px; margin: 5px; cursor: pointer; border-radius: 50px; font-weight: bold; }
  .filter-btn.active, .filter-btn:hover { background: #D4AF37; border-color: #D4AF37; }
  
  .blog-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 30px; }
  .blog-card { border: 1px solid #ddd; border-radius: 10px; overflow: hidden; transition: transform 0.3s; background: white; }
  .blog-card:hover { transform: translateY(-5px); box-shadow: 0 10px 20px rgba(0,0,0,0.1); }
  .blog-img { width: 100%; height: 200px; object-fit: cover; }
  .blog-content { padding: 20px; }
  .blog-tag { background: #e3f2fd; color: #0A2342; padding: 5px 10px; border-radius: 5px; font-size: 0.8rem; font-weight: bold; }
  .blog-title { margin: 10px 0; color: #0A2342; font-size: 1.2rem; }
  .read-more { color: #D4AF37; font-weight: bold; text-decoration: none; }
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
  <div class="blog-card" data-category="{{ post.category }}">
    <img src="{{ post.image }}" class="blog-img">
    <div class="blog-content">
      <span class="blog-tag">{{ post.category_label }}</span>
      <h3 class="blog-title">{{ post.title }}</h3>
      <p>{{ post.excerpt | strip_html | truncatewords: 15 }}</p>
      <a href="{{ post.url }}" class="read-more">Read Article →</a>
    </div>
  </div>
  {% endfor %}
</div>

<script>
  function filterPosts(cat) {
    const cards = document.querySelectorAll('.blog-card');
    const btns = document.querySelectorAll('.filter-btn');
    
    // Update active button
    btns.forEach(b => b.classList.remove('active'));
    event.target.classList.add('active');

    // Show/Hide cards
    cards.forEach(card => {
      if (cat === 'all' || card.getAttribute('data-category') === cat) {
        card.style.display = 'block';
      } else {
        card.style.display = 'none';
      }
    });
  }
</script>
