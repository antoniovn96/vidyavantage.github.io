---
layout: default
title: Book an Expert
permalink: /book-expert/
---

<style>
  /* HERO AREA */
  .expert-hero {
    background: #0A2342;
    color: white;
    padding: 60px 20px;
    text-align: center;
    border-radius: 0 0 20px 20px;
    margin-bottom: 40px;
  }

  /* FILTER BUTTONS */
  .filter-bar {
    text-align: center;
    margin-bottom: 40px;
  }
  
  .filter-btn {
    background: white;
    border: 1px solid #ddd;
    padding: 10px 20px;
    margin: 5px;
    border-radius: 50px;
    cursor: pointer;
    font-weight: bold;
    color: #555;
    transition: all 0.3s;
  }

  .filter-btn:hover, .filter-btn.active {
    background: #D4AF37;
    color: #0A2342;
    border-color: #D4AF37;
  }

  /* EXPERT GRID */
  .expert-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
    gap: 30px;
    padding: 0 20px;
    max-width: 1100px;
    margin: 0 auto;
  }

  .expert-card {
    background: white;
    border: 1px solid #eee;
    border-radius: 12px;
    overflow: hidden;
    text-align: center;
    transition: transform 0.3s, box-shadow 0.3s;
    position: relative;
  }

  .expert-card:hover {
    transform: translateY(-5px);
    box-shadow: 0 10px 20px rgba(0,0,0,0.1);
  }

  .expert-header {
    background: #f4f6f8;
    padding: 20px;
    border-bottom: 1px solid #eee;
  }

  .expert-img {
    width: 100px;
    height: 100px;
    border-radius: 50%;
    object-fit: cover;
    border: 3px solid #D4AF37;
    margin-bottom: 10px;
  }

  .expert-body { padding: 20px; }

  .verified-badge {
    background: #e8f5e9;
    color: #2e7d32;
    font-size: 0.75rem;
    padding: 3px 8px;
    border-radius: 4px;
    display: inline-block;
    margin-bottom: 5px;
    font-weight: bold;
  }

  .price-tag {
    font-size: 1.1rem;
    color: #0A2342;
    font-weight: bold;
    margin: 10px 0;
  }

  /* WhatsApp Button Style */
  .btn-whatsapp {
    background-color: #25D366; /* WhatsApp Green */
    color: white;
    padding: 12px 20px;
    border-radius: 50px;
    text-decoration: none;
    display: block;
    width: 100%;
    box-sizing: border-box;
    font-weight: bold;
    font-size: 1rem;
    transition: background 0.3s;
  }
  
  .btn-whatsapp:hover { background-color: #1ebe57; }

</style>

<div class="expert-hero">
  <h1 style="color:white; font-size: 2.5rem;">Connect with Verified Experts.</h1>
  <p style="font-size: 1.1rem; max-width: 600px; margin: 10px auto;">
    Join our exclusive WhatsApp community to book 1-on-1 sessions with Counsellors and Alumni.
  </p>
</div>

<div class="filter-bar">
  <button class="filter-btn active" onclick="filterExperts('all')">All Experts</button>
  <button class="filter-btn" onclick="filterExperts('study-abroad')">✈️ Study Abroad</button>
  <button class="filter-btn" onclick="filterExperts('career-guidance')">🎓 Career Guidance</button>
  <button class="filter-btn" onclick="filterExperts('alumni')">🏛️ Alumni Mentors</button>
</div>

<div class="expert-grid">
  {% for expert in site.data.experts %}
  <div class="expert-card" data-category="{{ expert.category }}">
    
    <div class="expert-header">
      <img src="{{ expert.image }}" alt="{{ expert.name }}" class="expert-img">
      <h3 style="margin: 5px 0; color: #0A2342;">{{ expert.name }}</h3>
      <span class="verified-badge">✓ Verified Expert</span>
    </div>

    <div class="expert-body">
      <p style="color: #666; font-weight: bold; margin-bottom: 5px;">{{ expert.role }}</p>
      <p style="color: #888; font-size: 0.9rem;">Exp: {{ expert.experience }}</p>
      
      <div class="price-tag">{{ expert.price }}</div>
      
      <a href="{{ expert.booking_link }}" class="btn-whatsapp" target="_blank">
        💬 Chat to Book
      </a>
    </div>

  </div>
  {% endfor %}
</div>

<div style="text-align: center; margin-top: 60px; padding: 40px; background: #f9f9f9;">
  <h2 style="color: #0A2342;">How it Works</h2>
  <div style="display: flex; justify-content: center; gap: 40px; flex-wrap: wrap; margin-top: 20px;">
    <div style="max-width: 200px;">
      <h3 style="color: #D4AF37;">1. Join Group</h3>
      <p style="font-size: 0.9rem;">Click "Chat to Book" to join our official WhatsApp group.</p>
    </div>
    <div style="max-width: 200px;">
      <h3 style="color: #D4AF37;">2. Request Expert</h3>
      <p style="font-size: 0.9rem;">Message the admin with the Expert's Name.</p>
    </div>
    <div style="max-width: 200px;">
      <h3 style="color: #D4AF37;">3. Get Slot</h3>
      <p style="font-size: 0.9rem;">We will schedule the session and send you a payment link.</p>
    </div>
  </div>
</div>

<script>
  function filterExperts(cat) {
    const cards = document.querySelectorAll('.expert-card');
    const btns = document.querySelectorAll('.filter-btn');
    
    // Update active button
    btns.forEach(b => {
      b.classList.remove('active');
      if(event.target === b) b.classList.add('active');
    });

    // Filter logic
    cards.forEach(card => {
      if (cat === 'all' || card.getAttribute('data-category') === cat) {
        card.style.display = 'block';
      } else {
        card.style.display = 'none';
      }
    });
  }
</script>
