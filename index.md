---
layout: default
title: Home
---

<style>
  /* Reset margins to make it look like a pro website */
  body, .main-content { padding: 0 !important; max-width: 100% !important; margin: 0 !important; }
  
  /* TOP NAVIGATION BAR */
  .top-nav {
    background-color: #0A2342; /* Navy Blue */
    padding: 15px 30px;
    display: flex;
    justify-content: space-between;
    align-items: center;
    position: sticky;
    top: 0;
    z-index: 1000;
    box-shadow: 0 2px 10px rgba(0,0,0,0.3);
  }

  .nav-logo {
    font-family: 'Montserrat', sans-serif;
    font-size: 1.5rem;
    font-weight: bold;
    color: #D4AF37; /* Gold */
    text-decoration: none;
    letter-spacing: 1px;
  }
  
  .nav-links a {
    color: white;
    margin-left: 20px;
    text-decoration: none;
    font-size: 0.9rem;
  }

  /* HERO SECTION */
  .hero-section {
    /* Fallback color if image fails */
    background-color: #0A2342; 
    /* Dark Overlay + Image */
    background-image: linear-gradient(rgba(10, 35, 66, 0.9), rgba(10, 35, 66, 0.8)), url('https://images.unsplash.com/photo-1523050854058-8df90110c9f1?q=80&w=2070&auto=format&fit=crop');
    background-size: cover;
    background-position: center;
    color: white;
    text-align: center;
    padding: 120px 20px 160px 20px; /* Extra padding bottom for the cards */
  }
  
  .hero-title {
    font-size: 3rem;
    font-weight: 700;
    margin-bottom: 15px;
    color: white;
  }
  
  .hero-subtitle {
    font-size: 1.3rem;
    max-width: 800px;
    margin: 0 auto;
    color: #D4AF37; /* Gold Text for visibility */
    font-weight: bold;
    letter-spacing: 0.5px;
  }

  /* THREE DOORS (CARDS) */
  .door-container {
    display: flex;
    justify-content: center;
    gap: 30px;
    padding: 0 20px;
    margin-top: -80px; /* Moves cards UP into the hero */
    flex-wrap: wrap;
    position: relative;
    z-index: 10;
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
    text-decoration: none !important; 
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
    margin: 80px 0 30px; /* More space on top */
    font-weight: bold;
  }
  
  /* VISA SECTION */
  .visa-banner {
    background: #0A2342;
    border-radius: 15px;
    padding: 50px;
    margin: 40px 20px;
    color: white;
    text-align: center;
    border: 2px solid #D4AF37;
  }

  /* RESPONSIVE */
  @media (max-width: 768px) {
    .hero-title { font-size: 2rem; }
    .door-container { margin-top: -40px; }
    .door-card { width: 100%; margin-bottom: 20px; }
    .nav-links { display: none; } /* Hides links on mobile to save space */
  }
</style>

<div class="top-nav">
  <a href="#" class="nav-logo">VIDYAVANTAGE</a>
  <div class="nav-links">
    <a href="./visas/">Global Visas</a>
    <a href="./colleges/">Colleges</a>
    <a href="./book-expert/" style="color: #D4AF37; font-weight: bold;">Book Expert</a>
  </div>
</div>

<div class="hero-section">
  <div class="hero-title">Map Your Future</div>
  <p class="hero-subtitle">"From Grade 9 to Global PhD"</p>
  <p style="color: white; margin-top: 10px;">India’s First Verified Career Intelligence Platform.</p>
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
    <h2 style="color: #D4AF37; margin-bottom: 10px;">The International Wing</h2>
    <p style="font-size: 1.2rem; margin-bottom: 30px;">
      Verified visa rules, exam scores (IELTS/SAT), and cost-of-living data for 
      <strong>USA 🇺🇸, UK 🇬🇧, Germany 🇩🇪, Canada 🇨🇦</strong> and more.
    </p>
    <a href="./visas/" class="btn-gold" style="padding: 15px 30px; font-size: 1rem;">Open Visa Database</a>
</div>

<h2 class="section-title">Verified Mentorship</h2>

<div style="display: flex; justify-content: center; gap: 20px; flex-wrap: wrap; margin-bottom: 60px;">
  <div style="text-align: center; max-width: 300px;">
    <h3 style="font-size: 1.2rem; color: #0A2342;">🏫 School Counsellors</h3>
    <p>For Stream Selection & Board Exams</p>
  </div>
  
  <div style="text-align: center; max-width: 300px;">
    <h3 style="font-size: 1.2rem; color: #0A2342;">✈️ Visa Experts</h3>
    <p>For Immigration & Finance Rules</p>
  </div>

  <div style="text-align: center; max-width: 300px;">
    <h3 style="font-size: 1.2rem; color: #0A2342;">🎓 Alumni Mentors</h3>
    <p>Real students from Ivy League / IITs</p>
  </div>
</div>

<div style="text-align: center; margin-bottom: 60px;">
  <a href="./book-expert/" class="btn-gold" style="padding: 15px 40px;">Book a Session</a>
</div>
<style>
  .site-footer {
    background-color: #0A2342;
    color: white;
    padding: 60px 20px 20px;
    margin-top: 80px;
    border-top: 5px solid #D4AF37;
    font-size: 0.9rem;
  }
  .footer-grid {
    display: flex;
    flex-wrap: wrap;
    justify-content: space-between;
    max-width: 1200px;
    margin: 0 auto;
    gap: 40px;
  }
  .footer-col { flex: 1; min-width: 250px; }
  .footer-heading { color: #D4AF37; font-weight: bold; margin-bottom: 20px; text-transform: uppercase; }
  .footer-links a { display: block; color: #f4f6f8; text-decoration: none; margin-bottom: 10px; transition: color 0.3s; }
  .footer-links a:hover { color: #D4AF37; padding-left: 5px; }
  .copyright { text-align: center; margin-top: 50px; padding-top: 20px; border-top: 1px solid rgba(255,255,255,0.1); color: #888; }
</style>

<footer class="site-footer">
  <div class="footer-grid">
    <div class="footer-col">
      <div class="footer-heading">VidyaVantage</div>
      <p>The only verified career map for Indian students. From Grade 9 stream selection to Global PhD admissions.</p>
    </div>

    <div class="footer-col">
      <div class="footer-heading">Quick Links</div>
      <div class="footer-links">
        <a href="./stream-selector/">Stream Selector</a>
        <a href="./colleges/">College Database</a>
        <a href="./visas/">Visa Rules</a>
        <a href="./blog/">Career Blog</a>
      </div>
    </div>

    <div class="footer-col">
      <div class="footer-heading">Services</div>
      <div class="footer-links">
        <a href="./book-expert/">Book a Counsellor</a>
        <a href="#">School Partnerships</a>
        <a href="#">For Parents</a>
      </div>
    </div>

    <div class="footer-col">
      <div class="footer-heading">Legal</div>
      <div class="footer-links">
        <a href="#">Privacy Policy</a>
        <a href="#">Terms of Use</a>
        <a href="#">Disclaimer</a>
      </div>
    </div>
  </div>

  <div class="copyright">
    © 2026 VidyaVantage. Built with 💙 in Bangalore.
  </div>
</footer>
