---
layout: default
title: Book an Expert
permalink: /book-expert/
---

# 🤝 Book a Verified Expert
**Don't guess with your future. Get 1-on-1 advice.**

<style>
  .expert-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 20px; margin-top: 30px; }
  .expert-card { background: white; border: 1px solid #ddd; border-radius: 8px; padding: 20px; text-align: center; box-shadow: 0 4px 6px rgba(0,0,0,0.1); transition: transform 0.2s; }
  .expert-card:hover { transform: translateY(-5px); border-color: #D4AF37; }
  .expert-img { width: 100px; height: 100px; border-radius: 50%; object-fit: cover; border: 3px solid #0A2342; margin-bottom: 15px; }
  .price-tag { background: #e3f2fd; color: #0A2342; padding: 5px 10px; border-radius: 15px; font-weight: bold; font-size: 0.9em; }
</style>

<div class="expert-grid">
  {% for expert in site.data.experts %}
  <div class="expert-card">
    <img src="{{ expert.image }}" alt="{{ expert.name }}" class="expert-img">
    <h3>{{ expert.name }}</h3>
    <p style="color: #666; margin-bottom: 5px;">{{ expert.role }}</p>
    <p><small>Exp: {{ expert.experience }}</small></p>
    <p class="price-tag">{{ expert.price }}</p>
    <br>
    <a href="{{ expert.booking_link }}" class="btn" target="_blank">Book Now</a>
  </div>
  {% endfor %}
</div>
