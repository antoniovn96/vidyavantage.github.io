---
layout: default
title: Home
---

<style>
  /* GLOBAL RESET & FONTS */
  body { font-family: 'Segoe UI', system-ui, -apple-system, sans-serif; background-color: #f8f9fa; }

  /* 1. HERO SECTION */
  .hero-section {
    position: relative;
    height: 85vh;
    min-height: 500px;
    background: linear-gradient(135deg, rgba(10, 35, 66, 0.9), rgba(0, 0, 0, 0.6)), url('https://images.unsplash.com/photo-1523050854058-8df90110c9f1?ixlib=rb-4.0.3&auto=format&fit=crop&w=1920&q=80');
    background-size: cover;
    background-position: center;
    background-attachment: fixed; /* Parallax effect */
    display: flex;
    align-items: center;
    justify-content: center;
    text-align: center;
    color: white;
    padding: 20px;
    margin-top: -50px; /* Pull up to cover any default spacing */
  }

  .hero-content { max-width: 900px; animation: fadeInUp 1s ease-out; }
  .hero-title { font-size: 4rem; font-weight: 800; margin-bottom: 20px; line-height: 1.1; letter-spacing: -1px; text-shadow: 0 2px 10px rgba(0,0,0,0.3); }
  .hero-subtitle { font-size: 1.5rem; color: #e0e0e0; margin-bottom: 40px; font-weight: 300; }
  
  .hero-btn {
    display: inline-block;
    background: #F39C12; /* Accent Color */
    color: #0A2342;
    padding: 15px 40px;
    font-size: 1.1rem;
    font-weight: 700;
    text-transform: uppercase;
    border-radius: 50px;
    text-decoration: none;
    transition: transform 0.3s, box-shadow 0.3s;
    box-shadow: 0 4px 15px rgba(243, 156, 18, 0.4);
  }
  .hero-btn:hover { transform: translateY(-3px); box-shadow: 0 8px 25px rgba(243, 156, 18, 0.6); color: #0A2342; background: white; }

  /* 2. STATS / VALUE BAR */
  .stats-bar {
    background: white;
    box-shadow: 0 10px 30px rgba(0,0,0,0.05);
    border-radius: 15px;
    margin: -50px auto 60px;
    position: relative;
    max-width: 1100px;
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    padding: 40px 20px;
    text-align: center;
    z-index: 10;
  }
  .stat-item h3 { font-size: 2.5rem; color: #0A2342; margin: 0; font-weight: 800; }
  .stat-item p { color: #666; margin: 5px 0 0; font-weight: 600; text-transform: uppercase; font-size: 0.9rem; letter-spacing: 1px; }

  /* 3. MAIN SERVICES GRID */
  .section-container { max-width: 1200px; margin: 0 auto 80px; padding: 0 20px; }
  .section-header { text-align: center; margin-bottom: 50px; }
  .section-title { font-size: 2.5rem; color: #0A2342; font-weight: 800; margin-bottom: 15px; }
  .section-desc { font-size: 1.1rem; color: #666; max-width: 600px; margin: 0 auto; }

  .services-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(400px, 1fr)); gap: 40px; }

  .service-card {
    background: white;
    border-radius: 20px;
    overflow: hidden;
    box-shadow: 0 10px 30px rgba(0,0,0,0.05);
    transition: all 0.4s ease;
    text-decoration: none;
    color: inherit;
    position: relative;
    display: flex;
    flex-direction: column;
  }
  .service-card:hover { transform: translateY(-10px); box-shadow: 0 20px 50px rgba(0,0,0,0.15); }
  
  .img-wrapper { height: 250px; overflow: hidden; position: relative; }
  .service-img { width: 100%; height: 100%; object-fit: cover; transition: transform 0.5s; }
  .service-card:hover .service-img { transform: scale(1.1); }
  
  .service-content { padding: 35px; flex-grow: 1; display: flex; flex-direction: column; justify-content: center; }
  .service-title { font-size: 1.8rem; font-weight: 800; margin-bottom: 15px; color: #0A2342; }
  .service-text { color: #555; line-height: 1.6; margin-bottom: 25px; font-size: 1.05rem; }
  .service-link { color: #F39C12; font-weight: 700; text-transform: uppercase; letter-spacing: 1px; font-size: 0.9rem; display: flex; align-items: center; gap: 10px; }
  .service-link::after { content: '→'; font-size: 1.2rem; transition: transform 0.3s; }
  .service-card:hover .service-link::after { transform: translateX(5px); }

  /* 4. ABOUT / MISSION SECTION */
  .mission-section {
    background: #0A2342;
    color: white;
    padding: 80px 20px;
    text-align: center;
    border-radius: 20px;
    margin: 0 20px 80px;
  }
  .mission-content { max-width: 800px; margin: 0 auto; }
  .mission-title { font-size: 2.2rem; margin-bottom: 20px; font-weight: 700; }
  .mission-text { font-size: 1.1rem; line-height: 1.8; color: #ccc; margin-bottom: 30px; }
  .mission-btn {
    border: 2px solid #F39C12;
    color: #F39C12;
    padding: 12px 30px;
    border-radius: 50px;
    text-decoration: none;
    font-weight: 700;
    transition: 0.3s;
  }
  .mission-btn:hover { background: #F39C12; color: #0A2342; }

  /* RESPONSIVE */
  @media (max-width: 768px) {
    .hero-title { font-size: 2.5rem; }
    .hero-section { height: 70vh; }
    .stats-bar { grid-template-columns: 1fr; gap: 30px; margin-top: 0; }
    .services-grid { grid-template-columns: 1fr; }
  }

  /* Animation */
  @keyframes fadeInUp {
    from { opacity: 0; transform: translateY(30px); }
    to { opacity: 1; transform: translateY(0); }
  }
</style>

<section class="hero-section">
  <div class="hero-content">
    <h1 class="hero-title">From Grade 9 to Global PhD.</h1>
    <p class="hero-subtitle">Your personalized roadmap to the world's best universities and careers.</p>
    <a href="#explore" class="hero-btn">Start Your Journey</a>
  </div>
</section>

<div class="stats-bar">
  <div class="stat-item">
    <h3>150+</h3>
    <p>Universities Analyzed</p>
  </div>
  <div class="stat-item">
    <h3>50+</h3>
    <p>Career Paths</p>
  </div>
  <div class="stat-item">
    <h3>100%</h3>
    <p>Personalized Guidance</p>
  </div>
</div>

<div id="explore" class="section-container">
  <div class="section-header">
    <h2 class="section-title">Explore Opportunities</h2>
    <p class="section-desc">We bridge the gap between ambition and reality. Choose your path below.</p>
  </div>

  <div class="services-grid">
    
    <a href="{{ '/colleges/' | relative_url }}" class="service-card">
      <div class="img-wrapper">
        <img src="https://images.unsplash.com/photo-1562774053-701939374585?ixlib=rb-4.0.3&auto=format&fit=crop&w=800&q=80" class="service-img" alt="Colleges">
      </div>
      <div class="service-content">
        <h3 class="service-title">College Admissions</h3>
        <p class="service-text">Detailed guides on IISc, Christ, St. Joseph's, and other top institutes. Access fee structures, entrance exams, and placement data.</p>
        <span class="service-link">Find Colleges</span>
      </div>
    </a>

    <a href="{{ '/visa/' | relative_url }}" class="service-card">
      <div class="img-wrapper">
        <img src="https://images.unsplash.com/photo-1526778548025-fa2f459cd5c1?ixlib=rb-4.0.3&auto=format&fit=crop&w=800&q=80" class="service-img" alt="Visa">
      </div>
      <div class="service-content">
        <h3 class="service-title">Global Visa Services</h3>
        <p class="service-text">Navigate the complexities of international travel. Expert support for Student, Work, and Tourist visas for USA, UK, Germany, and more.</p>
        <span class="service-link">View Visa Guides</span>
      </div>
    </a>

  </div>
</div>

<div class="mission-section">
  <div class="mission-content">
    <h2 class="mission-title">Expert Guidance by Antonio</h2>
    <p class="mission-text">
      "My mission is to democratize access to education. Whether you are in Grade 9 exploring options or a postgraduate looking for research opportunities, I am here to guide you."
    </p>
    <a href="https://github.com/antoniovn96" target="_blank" class="mission-btn">Connect on GitHub</a>
  </div>
</div>
