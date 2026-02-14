---
layout: default
title: Home
---

<style>
  /* Override main content width for homepage to make it full width */
  .main-content { max-width: 100% !important; padding: 0 !important; }
  
  /* HERO SECTION */
  .hero-section {
    background-color: #0A2342; 
    background-image: linear-gradient(rgba(10, 35, 66, 0.9), rgba(10, 35, 66, 0.8)), url('https://images.unsplash.com/photo-1523050854058-8df90110c9f1?q=80&w=2070&auto=format&fit=crop');
    background-size: cover;
    background-position: center;
    color: white;
    text-align: center;
    padding: 120px 20px 160px 20px;
  }
  
  .hero-title { font-size: 3rem; font-weight: 700; margin-bottom: 15px; color: white; }
  .hero-subtitle { font-size: 1.3rem; max-width: 800px; margin: 0 auto; color: #D4AF37; font-weight: bold; letter-spacing: 0.5px; }

  /* THREE DOORS (CARDS) */
  .door-container { display: flex; justify-content: center; gap: 30px; padding: 0 20px; margin-top: -80px; flex-wrap: wrap; position: relative; z-index: 10; }
  .door-card { background: white; color: #0A2342; padding: 30px; border-radius: 12px; width: 300px; text-align: center; box-shadow: 0 10px 30px rgba(0,0,0,0.15); transition: transform 0.3s ease; border-top: 5px solid #D4AF37; text-decoration: none !important; }
  .door-card:hover { transform: translateY(-10px); }
  .door-icon { font-size: 3rem; margin-bottom: 15px; display: block; }
  .door-title { font-size: 1.5rem; font-weight: bold; margin-bottom: 10px; color: #0A2342; }
  .btn-gold { background-color: #D4AF37; color: #0A2342; padding: 10px 20px; border-radius: 50px; font-weight: bold; text-transform: uppercase; font-size: 0.85rem; display: inline-block; }

  /* SECTIONS */
  .section-title { text-align: center; font-size: 2.2rem; color: #0A2342; margin: 80px 0 30px; font-weight: bold; }
  
  .visa-banner { background: #0A2342; border-radius: 15px; padding: 50px; margin: 40px auto; max-width: 1000px; color: white; text-align: center; border: 2px solid #D4AF37; }
</style>

<div class="hero-section">
  <div class="hero-title">Map Your Future</div>
  <p class="hero-subtitle">"From Grade 9 to Global PhD"</p>
  <p style="color: white; margin-top: 10px;">India’s First Verified Career Intelligence Platform.</p>
</div>

<div class="door-container">
  <a href="{{ '/stream-selector/' | relative_url }}" class="door-card">
    <span class="door-icon">🧭</span>
    <div class="door-title">I am Confused</div>
    <p>Not sure which stream fits you? Take our reality-check quiz.</p>
    <span class="btn-gold">Start Stream Selector</span>
  </a>

  <a href="{{ '/career-search/' | relative_url }}" class="door-card">
    <span class="door-icon">🎯</span>
    <div class="door-title">I have a Goal</div>
    <p>Want to be a Pilot, Doctor, or Engineer? See the verified roadmap.</p>
    <span class="btn-gold">View Roadmaps</span>
  </a>

  <a href="{{ '/skill-search/' | relative_url }}" class="door-card">
    <span class="door-icon">⭐</span>
    <div class="door-title">I have a Talent</div>
    <p>Good at debating or coding? Find jobs that value your skills.</p>
    <span class="btn-gold">Search by Skill</span>
  </a>
</div>

<h2 class="section-title">Global Opportunities</h2>
<div class="visa-banner">
    <h2 style="color: #D4AF37; margin-bottom: 10px;">The International Wing</h2>
    <p style="font-size: 1.2rem; margin-bottom: 30px;">
      Verified visa rules, exam scores (IELTS/SAT), and cost-of-living data for 
      <strong>USA 🇺🇸, UK 🇬🇧, Germany 🇩🇪, Canada 🇨🇦</strong>.
    </p>
    <a href="{{ '/visas/' | relative_url }}" class="btn-gold" style="padding: 15px 30px; font-size: 1rem;">Open Visa Database</a>
</div>

<h2 class="section-title">Verified Mentorship</h2>
<div style="display: flex; justify-content: center; gap: 40px; flex-wrap: wrap; margin-bottom: 60px;">
  <div style="text-align: center; max-width: 300px;">
    <h3 style="font-size: 1.2rem; color: #0A2342;">🏫 School Counsellors</h3>
    <p>For Stream Selection</p>
  </div>
  <div style="text-align: center; max-width: 300px;">
    <h3 style="font-size: 1.2rem; color: #0A2342;">✈️ Visa Experts</h3>
    <p>For Immigration Rules</p>
  </div>
  <div style="text-align: center; max-width: 300px;">
    <h3 style="font-size: 1.2rem; color: #0A2342;">🎓 Alumni Mentors</h3>
    <p>From Ivy League / IITs</p>
  </div>
</div>

<div style="text-align: center; margin-bottom: 60px;">
  <a href="{{ '/book-expert/' | relative_url }}" class="btn-gold" style="padding: 15px 40px;">Book a Session</a>
</div>
