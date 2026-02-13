---
layout: default
title: Home
---

<style>
  /* Reset some default Jekyll margins */
  .main-content { max-width: 100%; padding: 0; }
  
  /* HERO SECTION */
  .hero-section {
    background: linear-gradient(rgba(10, 35, 66, 0.85), rgba(10, 35, 66, 0.7)), url('https://images.unsplash.com/photo-1523050854058-8df90110c9f1?q=80&w=2070&auto=format&fit=crop');
    background-size: cover;
    background-position: center;
    color: white;
    text-align: center;
    padding: 100px 20px;
    margin-bottom: 40px;
  }
  
  .hero-title {
    font-size: 3.5rem;
    font-weight: 700;
    margin-bottom: 10px;
    color: #D4AF37; /* Gold */
    text-shadow: 2px 2px 4px rgba(0,0,0,0.5);
  }
  
  .hero-subtitle {
    font-size: 1.4rem;
    max-width: 800px;
    margin: 0 auto;
    color: #f4f6f8;
  }

  /* THREE DOORS (CARDS) */
  .door-container {
    display: flex;
    justify-content: center;
    gap: 30px;
    padding: 0 20px;
    margin-top: -50px; /* Overlap effect */
    flex-wrap: wrap;
  }

  .door-card {
    background: white;
    color: #0A2342;
    padding: 30px;
    border-radius: 12px;
    width: 300px;
    text-align: center;
    box-shadow: 0 10px 30px rgba(0,0,0,0.15);
    transition: transform 0.3s ease, box-shadow 0.3s ease;
    border-top: 5px solid #D4AF37;
    text-decoration: none !important; /* Remove underline from links */
  }

  .door-card:hover {
    transform: translateY(-10px);
    box-shadow: 0 20px 40px rgba(0,0,0,0.2);
  }

  .door-icon { font-size: 3rem; margin-bottom: 15px; display: block; }
  .door-title { font-size: 1.5rem; font-weight: bold; margin-bottom: 10px; color: #0A2342; }
  .door-desc { font-size: 0.95rem; color: #666; margin-bottom: 20px; line-height: 1.5; }
  
  .btn-gold {
    background-color: #D4AF37;
    color: #0A2342;
    padding: 10px 20px;
    border-radius: 50px;
    font-weight: bold;
    text-transform: uppercase;
    font-size: 0.85rem;
    display: inline-block;
  }

  /* SECTIONS */
  .section-title {
    text-align: center;
    font-size: 2.2rem;
    color: #0A2342;
    margin: 60px 0 20px;
    font-weight: bold;
  }
  
  /* VISA SECTION */
  .visa-banner {
    background: url('https://images.unsplash.com/photo-1524850011238-e3d235c7d4c9?q=80&w=2064&auto=format&fit=crop');
    background-size: cover;
    background-position: center;
    border-radius: 15px;
    padding: 60px;
    margin: 40px 20px;
    color: white;
    text-align: center;
    position: relative;
    overflow: hidden;
  }
  
  .visa-overlay {
    background: rgba(10, 35, 66, 0.8);
    position: absolute;
    top: 0; left: 0; right: 0; bottom: 0;
  }
  
  .visa-content { position: relative; z-index: 2; }

  /* RESPONSIVE */
  @media (max-width: 768px) {
    .hero-title { font-size: 2rem; }
    .door-container { margin-top: 20px; }
    .door-card { width: 100%; }
  }
</style>

<div class="hero-section">
  <div class="hero-title">VidyaVantage</div>
  <p class="hero-subtitle">India’s First Verified Career Intelligence Platform.<br>From Grade 9 Choices to Global PhDs.</p>
</div>

<div class="door-container">
  <a href="./stream-selector/" class="door-card">
    <span class="door-icon">🧭</span>
    <div class="door-title">I am Confused</div>
    <div class="door-desc">Not sure which stream or career fits you? Take our reality-check quiz.</div>
    <span class="btn-gold">Start Stream Selector</span>
  </a>

  <a href="./career-search/" class="door-card">
    <span class="door-icon">🎯</span>
    <div class="door-title">I have a Goal</div>
    <div class="door-desc">Want to be a Pilot, Doctor, or Engineer? See the verified roadmap.</div>
    <span class="btn-gold">View Roadmaps</span>
  </a>

  <a href="./skill-search/" class="door-card">
    <span class="door-icon">⭐</span>
    <div class="door-title">I have a Talent</div>
    <div class="door-desc">Good at debating or coding? Find jobs that value your skills.</div>
    <span class="btn-gold">Search by Skill</span>
  </a>
</div>

<h2 class="section-title">Global Opportunities</h2>

<div class="visa-banner">
  <div class="visa-overlay"></div>
  <div class="visa-content">
    <h2 style="color: #D4AF37; margin-bottom: 10px;">The International Wing</h2>
    <p style="font-size: 1.2rem; margin-bottom: 30px;">
      Verified visa rules, exam scores (IELTS/SAT), and cost-of-living data for 
      <strong>USA 🇺🇸, UK 🇬🇧, Germany 🇩🇪, Canada 🇨🇦</strong> and more.
    </p>
    <a href="./visas/" class="btn-gold" style="padding: 15px 30px; font-size: 1rem;">Open Visa Database</a>
  </div>
</div>

<h2 class="section-title">Verified Mentorship</h2>

<div style="display: flex; justify-content: center; gap: 20px; flex-wrap: wrap; margin-bottom: 60px;">
  <div style="text-align: center; max-width: 300px;">
    <img src="https://images.unsplash.com/photo-1573496359142-b8d87734a5a2?q=80&w=688&auto=format&fit=crop" style="width: 100px; height: 100px; border-radius: 50%; object-fit: cover; border: 3px solid #0A2342; margin-bottom: 15px;">
    <h3 style="font-size: 1.2rem; color: #0A2342;">School Counsellors</h3>
    <p>For Stream Selection & Board Exams</p>
  </div>
  
  <div style="text-align: center; max-width: 300px;">
    <img src="https://images.unsplash.com/photo-1560250097-0b93528c311a?q=80&w=687&auto=format&fit=crop" style="width: 100px; height: 100px; border-radius: 50%; object-fit: cover; border: 3px solid #0A2342; margin-bottom: 15px;">
    <h3 style="font-size: 1.2rem; color: #0A2342;">Visa Experts</h3>
    <p>For Immigration & Finance Rules</p>
  </div>

  <div style="text-align: center; max-width: 300px;">
    <img src="https://images.unsplash.com/photo-1519085360753-af0119f7cbe7?q=80&w=687&auto=format&fit=crop" style="width: 100px; height: 100px; border-radius: 50%; object-fit: cover; border: 3px solid #0A2342; margin-bottom: 15px;">
    <h3 style="font-size: 1.2rem; color: #0A2342;">Alumni Mentors</h3>
    <p>Real students from Ivy League / IITs</p>
  </div>
</div>

<div style="text-align: center; margin-bottom: 60px;">
  <a href="./book-expert/" class="btn-gold" style="padding: 15px 40px;">Book a Session</a>
</div>
