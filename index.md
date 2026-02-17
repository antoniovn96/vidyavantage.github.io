---
layout: default
title: Home
---

<style>
  /* HERO SECTION */
  .home-hero {
    background: linear-gradient(rgba(10, 35, 66, 0.85), rgba(10, 35, 66, 0.7)), url('https://images.unsplash.com/photo-1523050854058-8df90110c9f1?ixlib=rb-4.0.3&auto=format&fit=crop&w=1600&q=80');
    background-size: cover;
    background-position: center;
    color: white;
    text-align: center;
    padding: 120px 20px;
  }
  .home-hero h1 { font-size: 3.5rem; margin: 0; font-weight: 800; letter-spacing: -1px; }
  .home-hero p { font-size: 1.25rem; margin-top: 15px; color: #ddd; max-width: 600px; margin-left: auto; margin-right: auto; }
  
  /* SECTIONS */
  .section-container { max-width: 1100px; margin: 60px auto; padding: 0 20px; }
  .section-title { text-align: center; font-size: 2.5rem; color: #0A2342; margin-bottom: 40px; font-weight: 700; }

  .feature-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(350px, 1fr)); gap: 40px; }
  
  .feature-card {
    background: white; border-radius: 15px; overflow: hidden; box-shadow: 0 10px 30px rgba(0,0,0,0.08);
    transition: transform 0.3s; text-decoration: none; color: inherit; display: block;
  }
  .feature-card:hover { transform: translateY(-8px); box-shadow: 0 20px 40px rgba(0,0,0,0.15); }
  
  .f-img { width: 100%; height: 220px; object-fit: cover; }
  .f-body { padding: 30px; text-align: center; }
  .f-title { font-size: 1.5rem; font-weight: 700; color: #0A2342; margin-bottom: 10px; }
  .f-desc { color: #666; line-height: 1.6; margin-bottom: 20px; }
  .f-btn { color: #007bff; font-weight: 700; text-transform: uppercase; font-size: 0.9rem; }
</style>

<div class="home-hero">
  <h1>Shape Your Future</h1>
  <p>Your one-stop destination for top colleges in Bangalore and global visa assistance.</p>
</div>

<div class="section-container">
  <h2 class="section-title">What are you looking for?</h2>
  
  <div class="feature-grid">
    
    <a href="{{ '/colleges/' | relative_url }}" class="feature-card">
      <img src="https://images.unsplash.com/photo-1562774053-701939374585?ixlib=rb-4.0.3&auto=format&fit=crop&w=800&q=80" class="f-img" alt="Colleges">
      <div class="f-body">
        <h3 class="f-title">Top Colleges</h3>
        <p class="f-desc">Explore premier institutions like IISc, Christ, St. Joseph's, and BMSCE. Get fee structures and admission details.</p>
        <span class="f-btn">Browse Colleges &rarr;</span>
      </div>
    </a>

    <a href="{{ '/visa/' | relative_url }}" class="feature-card">
      <img src="https://images.unsplash.com/photo-1526778548025-fa2f459cd5c1?ixlib=rb-4.0.3&auto=format&fit=crop&w=800&q=80" class="f-img" alt="Visa">
      <div class="f-body">
        <h3 class="f-title">Visa Services</h3>
        <p class="f-desc">Planning to study or work abroad? Get expert guidance for USA, UK, Canada, Germany, and more.</p>
        <span class="f-btn">Check Requirements &rarr;</span>
      </div>
    </a>

  </div>
</div>
