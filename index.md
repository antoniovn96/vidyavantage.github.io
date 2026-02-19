---
layout: default
title: Home
---

<style>
  /* --- VARIABLES & RESET --- */
  :root {
    --primary: #2563EB; /* Royal Blue */
    --secondary: #1E40AF; /* Darker Blue */
    --accent: #F59E0B; /* Amber/Gold */
    --text-dark: #1F2937;
    --text-light: #6B7280;
    --bg-light: #F3F4F6;
    --white: #ffffff;
  }
  
  body {
    font-family: 'Inter', system-ui, -apple-system, sans-serif;
    background-color: var(--white);
    color: var(--text-dark);
    margin: 0;
  }

  /* --- 1. MODERN SPLIT HERO SECTION --- */
  .hero-wrapper {
    display: flex;
    align-items: center;
    justify-content: space-between;
    max-width: 1200px;
    margin: 0 auto;
    padding: 80px 20px;
    min-height: 80vh;
  }

  .hero-text {
    flex: 1;
    padding-right: 50px;
    animation: slideInLeft 0.8s ease-out;
  }

  .hero-visual {
    flex: 1;
    position: relative;
    animation: slideInRight 0.8s ease-out;
  }

  .hero-badge {
    display: inline-block;
    background: #DBEAFE;
    color: var(--secondary);
    padding: 6px 15px;
    border-radius: 50px;
    font-size: 0.85rem;
    font-weight: 700;
    margin-bottom: 20px;
    text-transform: uppercase;
    letter-spacing: 0.5px;
  }

  h1.hero-headline {
    font-size: 3.5rem;
    line-height: 1.1;
    font-weight: 800;
    color: #111;
    margin-bottom: 20px;
  }
  
  .hero-headline span { color: var(--primary); }

  .hero-subhead {
    font-size: 1.2rem;
    color: var(--text-light);
    line-height: 1.6;
    margin-bottom: 35px;
    max-width: 90%;
  }

  .cta-group { display: flex; gap: 15px; flex-wrap: wrap; }

  .btn-accent {
    background: var(--accent);
    color: #111;
    padding: 15px 35px;
    border-radius: 8px;
    font-weight: 700;
    text-decoration: none;
    transition: all 0.3s;
    box-shadow: 0 4px 14px rgba(245, 158, 11, 0.3);
  }
  .btn-accent:hover { transform: translateY(-2px); box-shadow: 0 6px 20px rgba(245, 158, 11, 0.4); }

  .btn-primary {
    background: var(--primary);
    color: white;
    padding: 15px 35px;
    border-radius: 8px;
    font-weight: 600;
    text-decoration: none;
    transition: all 0.3s;
    box-shadow: 0 4px 14px rgba(37, 99, 235, 0.3);
  }
  .btn-primary:hover { background: var(--secondary); transform: translateY(-2px); }

  .btn-secondary {
    background: white;
    color: var(--text-dark);
    border: 2px solid #e5e7eb;
    padding: 13px 35px;
    border-radius: 8px;
    font-weight: 600;
    text-decoration: none;
    transition: all 0.3s;
  }
  .btn-secondary:hover { border-color: var(--text-dark); }

  /* Hero Image styling */
  .hero-img-main {
    width: 100%;
    border-radius: 20px;
    box-shadow: 20px 20px 0px var(--bg-light);
    object-fit: cover;
    height: 500px;
  }

  /* --- 2. STATS FLOATING BAR --- */
  .stats-container {
    background: var(--secondary);
    color: white;
    padding: 50px 0;
    margin-top: -40px;
    position: relative;
    z-index: 2;
  }
  .stats-grid {
    max-width: 1200px;
    margin: 0 auto;
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    text-align: center;
    gap: 30px;
  }
  .stat-number { font-size: 3rem; font-weight: 700; margin-bottom: 5px; color: var(--accent); }
  .stat-label { font-size: 1rem; opacity: 0.9; text-transform: uppercase; letter-spacing: 1px; }

  /* --- 3. FEATURE CARDS SECTION --- */
  .features-section {
    padding: 100px 20px;
    background: #fafafa;
  }
  .section-header { text-align: center; max-width: 700px; margin: 0 auto 60px; }
  .section-tag { color: var(--primary); font-weight: 700; text-transform: uppercase; font-size: 0.9rem; }
  .section-title { font-size: 2.5rem; font-weight: 800; margin: 10px 0; color: #111; }

  .cards-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(320px, 1fr));
    gap: 30px;
    max-width: 1200px;
    margin: 0 auto;
  }

  .feature-card {
    background: white;
    border-radius: 16px;
    overflow: hidden;
    box-shadow: 0 10px 40px rgba(0,0,0,0.05);
    transition: transform 0.3s ease;
    text-decoration: none;
    color: inherit;
    display: flex;
    flex-direction: column;
    height: 100%;
  }
  .feature-card:hover { transform: translateY(-10px); }

  .card-image-wrap { height: 200px; overflow: hidden; }
  .card-img { width: 100%; height: 100%; object-fit: cover; transition: transform 0.5s; }
  .feature-card:hover .card-img { transform: scale(1.05); }

  .card-content { padding: 30px; display: flex; flex-direction: column; flex-grow: 1; }
  .card-title { font-size: 1.4rem; font-weight: 700; margin-bottom: 10px; color: #111; }
  .card-desc { color: var(--text-light); line-height: 1.6; margin-bottom: 20px; flex-grow: 1; }
  .card-arrow { color: var(--primary); font-weight: 700; display: flex; align-items: center; gap: 5px; margin-top: auto; }

  /* --- 4. WHY CHOOSE US (Icon Grid) --- */
  .why-section {
    padding: 80px 20px;
    max-width: 1200px;
    margin: 0 auto;
    text-align: center;
  }
  .icon-grid {
    display: flex;
    justify-content: space-around;
    flex-wrap: wrap;
    gap: 40px;
    margin-top: 50px;
  }
  .icon-box { max-width: 300px; }
  .icon-circle {
    width: 70px; height: 70px; background: #DBEAFE; color: var(--primary);
    border-radius: 50%; display: flex; align-items: center; justify-content: center;
    font-size: 1.8rem; margin: 0 auto 20px;
  }
  .icon-title { font-weight: 700; font-size: 1.2rem; margin-bottom: 10px; }
  .icon-text { color: var(--text-light); font-size: 0.95rem; line-height: 1.6; }

  /* RESPONSIVE */
  @media (max-width: 900px) {
    .hero-wrapper { flex-direction: column-reverse; text-align: center; padding-top: 40px; }
    .hero-text { padding-right: 0; margin-top: 40px; }
    .hero-headline { font-size: 2.5rem; }
    .cta-group { justify-content: center; }
    .hero-img-main { height: 300px; }
    .stats-grid { grid-template-columns: 1fr; gap: 30px; }
    .cards-grid { grid-template-columns: 1fr; }
  }

  /* Animations */
  @keyframes slideInLeft { from { opacity: 0; transform: translateX(-30px); } to { opacity: 1; transform: translateX(0); } }
  @keyframes slideInRight { from { opacity: 0; transform: translateX(30px); } to { opacity: 1; transform: translateX(0); } }
</style>

<div class="hero-wrapper">
  <div class="hero-text">
    <span class="hero-badge">🚀 Admissions 2025 Open</span>
    <h1 class="hero-headline">Build Your Future <br><span>Without Limits.</span></h1>
    <p class="hero-subhead">
      Your personalized gateway to top-tier universities and global career opportunities. From Grade 9 counseling to PhD research guidance.
    </p>
    <div class="cta-group">
      <a href="{{ '/assessment/' | relative_url }}" class="btn-accent">Take AI Assessment</a>
      <a href="{{ '/colleges/' | relative_url }}" class="btn-primary">Browse Colleges</a>
      <a href="{{ '/visa/' | relative_url }}" class="btn-secondary">Check Visa Info</a>
    </div>
  </div>
  <div class="hero-visual">
    <img src="https://images.unsplash.com/photo-1523240795612-9a054b0db644?ixlib=rb-4.0.3&auto=format&fit=crop&w=800&q=80" alt="Students" class="hero-img-main">
  </div>
</div>

<div class="stats-container">
  <div class="stats-grid">
    <div>
      <div class="stat-number">8+</div>
      <div class="stat-label">Top Universities</div>
    </div>
    <div>
      <div class="stat-number">10+</div>
      <div class="stat-label">Global Destinations</div>
    </div>
    <div>
      <div class="stat-number">100%</div>
      <div class="stat-label">Verified Data</div>
    </div>
  </div>
</div>

<div class="features-section">
  <div class="section-header">
    <span class="section-tag">Our Services</span>
    <h2 class="section-title">Everything you need to succeed</h2>
    <p style="color:#666; font-size:1.1rem;">We simplify the complex world of admissions, career mapping, and immigration.</p>
  </div>

  <div class="cards-grid">
    
    <a href="{{ '/assessment/' | relative_url }}" class="feature-card">
      <div class="card-image-wrap">
        <img src="https://images.unsplash.com/photo-1454165804606-c3d57bc86b40?ixlib=rb-4.0.3&auto=format&fit=crop&w=800&q=80" class="card-img" alt="AI Career Assessment">
      </div>
      <div class="card-content">
        <h3 class="card-title">AI Career Assessment</h3>
        <p class="card-desc">Not sure which path to take? Take our AI-driven capability analysis to discover your ideal courses and get personalized college matches instantly.</p>
        <div class="card-arrow">Start Assessment ➔</div>
      </div>
    </a>

    <a href="{{ '/colleges/' | relative_url }}" class="feature-card">
      <div class="card-image-wrap">
        <img src="https://images.unsplash.com/photo-1541339907198-e08756dedf3f?ixlib=rb-4.0.3&auto=format&fit=crop&w=800&q=80" class="card-img" alt="Colleges">
      </div>
      <div class="card-content">
        <h3 class="card-title">Top Colleges Directory</h3>
        <p class="card-desc">Comprehensive guides on IISc, IIT Roorkee, BMSCE, and more. Access 2025 fee structures, entrance exams, and placement records.</p>
        <div class="card-arrow">Explore Colleges ➔</div>
      </div>
    </a>

    <a href="{{ '/visa/' | relative_url }}" class="feature-card">
      <div class="card-image-wrap">
        <img src="https://images.unsplash.com/photo-1436491865332-7a61a109cc05?ixlib=rb-4.0.3&auto=format&fit=crop&w=800&q=80" class="card-img" alt="Visa">
      </div>
      <div class="card-content">
        <h3 class="card-title">Global Visa Assistance</h3>
        <p class="card-desc">Planning to study abroad? Get expert checklists for USA (F1), UK (Tier 4), Germany, Australia, and Canada student visas.</p>
        <div class="card-arrow">Check Requirements ➔</div>
      </div>
    </a>
    
  </div>
</div>

<div class="why-section">
  <h2 class="section-title">Why VidyaVantage?</h2>
  <div class="icon-grid">
    
    <div class="icon-box">
      <div class="icon-circle">🎓</div>
      <h3 class="icon-title">Expert Counseling</h3>
      <p class="icon-text">Founded by a School Counselor dedicated to bridging the information gap for students.</p>
    </div>

    <div class="icon-box">
      <div class="icon-circle">📊</div>
      <h3 class="icon-title">Accurate Data</h3>
      <p class="icon-text">Up-to-date 2025 fee structures and admission cutoffs sourced directly from institutions.</p>
    </div>

    <div class="icon-box">
      <div class="icon-circle">🌍</div>
      <h3 class="icon-title">Global Reach</h3>
      <p class="icon-text">From local Bangalore colleges to Ivy League universities, we cover it all.</p>
    </div>

  </div>
</div>
