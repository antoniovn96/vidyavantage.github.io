---
layout: default
title: Global Visa Services 🌏
permalink: /visa/
image: "https://images.unsplash.com/photo-1436491865332-7a61a109cc05?ixlib=rb-4.0.3&auto=format&fit=crop&w=1200&q=80"
description: "Expert Visa Assistance for USA, UK, Canada, Australia, Germany, and more. Student, Tourist, and Work Visas made easy."
---

<style>
  /* --- VARIABLES & RESET --- */
  :root {
    --primary: #0A2342; /* Deep Navy */
    --accent: #F39C12; /* Golden/Passport Color */
    --bg-light: #F9FAFB;
    --text-dark: #1F2937;
    --text-muted: #6B7280;
    --card-shadow: 0 10px 30px rgba(0,0,0,0.06);
    --hover-shadow: 0 20px 40px rgba(0,0,0,0.12);
  }

  body {
    background-color: var(--bg-light);
    font-family: 'Segoe UI', system-ui, sans-serif;
  }

  /* --- 1. HERO SECTION --- */
  .visa-hero {
    background: linear-gradient(135deg, rgba(10, 35, 66, 0.95), rgba(10, 35, 66, 0.8)), 
                url('https://images.unsplash.com/photo-1436491865332-7a61a109cc05?ixlib=rb-4.0.3&auto=format&fit=crop&w=1600&q=80');
    background-size: cover;
    background-position: center;
    color: white;
    text-align: center;
    padding: 100px 20px 120px;
    border-radius: 0 0 50% 50% / 40px; /* Curved bottom */
    margin-bottom: 60px;
  }
  
  .hero-badge {
    display: inline-block;
    background: rgba(255,255,255,0.15);
    backdrop-filter: blur(10px);
    border: 1px solid rgba(255,255,255,0.2);
    padding: 8px 20px;
    border-radius: 50px;
    font-size: 0.9rem;
    font-weight: 600;
    text-transform: uppercase;
    letter-spacing: 1px;
    margin-bottom: 20px;
    color: #F39C12;
  }

  .visa-hero h1 { 
    font-size: 3.5rem; 
    margin: 0 0 15px; 
    font-weight: 800; 
    letter-spacing: -1px;
  }
  
  .visa-hero p { 
    font-size: 1.25rem; 
    max-width: 700px; 
    margin: 0 auto; 
    color: #E5E7EB; 
    line-height: 1.6;
  }

  /* --- 2. PROCESS STEPS (Floating) --- */
  .process-container {
    max-width: 1000px;
    margin: -90px auto 80px;
    padding: 0 20px;
    position: relative;
    z-index: 10;
  }
  
  .process-card {
    background: white;
    border-radius: 16px;
    padding: 40px;
    box-shadow: 0 15px 50px rgba(0,0,0,0.1);
    display: grid;
    grid-template-columns: repeat(4, 1fr);
    gap: 20px;
    text-align: center;
  }

  .step-item { position: relative; }
  .step-item:not(:last-child)::after {
    content: '→';
    position: absolute;
    top: 25%;
    right: -15px;
    color: #E5E7EB;
    font-size: 1.5rem;
    font-weight: 300;
  }

  .step-icon {
    width: 60px; height: 60px;
    background: #EFF6FF;
    color: var(--primary);
    border-radius: 50%;
    display: flex; align-items: center; justify-content: center;
    font-size: 1.5rem;
    margin: 0 auto 15px;
    transition: 0.3s;
  }
  .step-item:hover .step-icon { background: var(--primary); color: white; transform: scale(1.1); }
  
  .step-title { font-weight: 700; color: var(--text-dark); margin-bottom: 5px; font-size: 1.1rem; }
  .step-desc { font-size: 0.9rem; color: var(--text-muted); line-height: 1.4; }

  /* --- 3. DESTINATIONS GRID --- */
  .section-title {
    text-align: center;
    font-size: 2.2rem;
    font-weight: 800;
    color: var(--text-dark);
    margin-bottom: 10px;
  }
  .section-subtitle {
    text-align: center;
    color: var(--text-muted);
    margin-bottom: 50px;
    font-size: 1.1rem;
  }

  .country-grid {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(320px, 1fr));
    gap: 30px;
    padding: 0 20px 80px;
    max-width: 1200px;
    margin: 0 auto;
  }

  .country-card {
    background: white;
    border-radius: 16px;
    overflow: hidden;
    box-shadow: var(--card-shadow);
    transition: all 0.4s ease;
    text-decoration: none;
    display: flex;
    flex-direction: column;
    position: relative;
    border: 1px solid #f0f0f0;
  }
  .country-card:hover { 
    transform: translateY(-8px); 
    box-shadow: var(--hover-shadow); 
    border-color: #e0e0e0;
  }

  .card-img-wrapper {
    height: 200px;
    overflow: hidden;
    position: relative;
  }
  .card-img {
    width: 100%;
    height: 100%;
    object-fit: cover;
    transition: transform 0.6s cubic-bezier(0.25, 0.46, 0.45, 0.94);
  }
  .country-card:hover .card-img { transform: scale(1.1); }

  .flag-badge {
    position: absolute;
    bottom: -25px;
    right: 25px;
    width: 50px;
    height: 50px;
    border-radius: 50%;
    border: 4px solid white;
    background: white;
    object-fit: cover;
    box-shadow: 0 5px 15px rgba(0,0,0,0.15);
    z-index: 2;
  }

  .card-body { padding: 30px 25px 25px; position: relative; }
  
  .card-title { 
    font-size: 1.5rem; 
    font-weight: 800; 
    color: var(--text-dark); 
    margin: 0 0 10px;
    display: flex;
    align-items: center;
    justify-content: space-between;
  }
  
  .visa-tags {
    display: flex;
    gap: 8px;
    flex-wrap: wrap;
    margin-bottom: 15px;
  }
  .v-tag {
    font-size: 0.75rem;
    padding: 4px 10px;
    background: #F3F4F6;
    color: #555;
    border-radius: 4px;
    font-weight: 600;
  }

  .card-text { 
    font-size: 0.95rem; 
    color: var(--text-muted); 
    line-height: 1.6; 
    margin-bottom: 20px;
  }

  .card-btn {
    display: block;
    text-align: center;
    padding: 10px;
    border: 1px solid #E5E7EB;
    border-radius: 8px;
    color: var(--text-dark);
    font-weight: 600;
    transition: 0.2s;
    font-size: 0.9rem;
  }
  .country-card:hover .card-btn {
    background: var(--primary);
    color: white;
    border-color: var(--primary);
  }

  /* RESPONSIVE */
  @media (max-width: 900px) {
    .visa-hero { border-radius: 0 0 30px 30px; padding-bottom: 100px; }
    .visa-hero h1 { font-size: 2.5rem; }
    .process-card { grid-template-columns: 1fr; gap: 40px; padding: 30px; }
    .step-item:not(:last-child)::after { content: '↓'; top: auto; bottom: -30px; right: 50%; transform: translateX(50%); }
  }
</style>

<div class="visa-hero">
  <span class="hero-badge">✈️ Global Opportunities Await</span>
  <h1>Visa Services & Immigration</h1>
  <p>Simplified visa processing for students, professionals, and tourists. We handle the paperwork so you can focus on the journey.</p>
</div>

<div class="process-container">
  <div class="process-card">
    <div class="step-item">
      <div class="step-icon">📋</div>
      <div class="step-title">Profile Analysis</div>
      <div class="step-desc">We assess your eligibility and choose the right visa category.</div>
    </div>
    <div class="step-item">
      <div class="step-icon">📂</div>
      <div class="step-title">Documentation</div>
      <div class="step-desc">Expert help with SOPs, financials, and application forms.</div>
    </div>
    <div class="step-item">
      <div class="step-icon">🏛️</div>
      <div class="step-title">Embassy Filing</div>
      <div class="step-desc">Error-free submission and interview preparation.</div>
    </div>
    <div class="step-item">
      <div class="step-icon">✈️</div>
      <div class="step-title">Fly High</div>
      <div class="step-desc">Pre-departure briefing and post-landing support.</div>
    </div>
  </div>
</div>

<h2 class="section-title">Choose Your Destination</h2>
<p class="section-subtitle">We provide specialized support for these top destinations.</p>

<div class="country-grid">

  <a href="#" class="country-card">
    <div class="card-img-wrapper">
      <img src="https://cdn.pixabay.com/photo/2014/11/22/00/03/new-york-540807_1280.jpg" class="card-img" alt="USA">
      <img src="https://flagcdn.com/w80/us.png" class="flag-badge" alt="USA Flag">
    </div>
    <div class="card-body">
      <h3 class="card-title">United States</h3>
      <div class="visa-tags">
        <span class="v-tag">F1 Student</span>
        <span class="v-tag">H1B Work</span>
        <span class="v-tag">B1/B2 Tourist</span>
      </div>
      <p class="card-text">Navigate the complex US immigration system with expert DS-160 filing and mock interview sessions.</p>
      <span class="card-btn">Check Requirements</span>
    </div>
  </a>

  <a href="#" class="country-card">
    <div class="card-img-wrapper">
      <img src="https://images.unsplash.com/photo-1513635269975-59663e0ac1ad?ixlib=rb-4.0.3&auto=format&fit=crop&w=800&q=80" class="card-img" alt="UK">
      <img src="https://flagcdn.com/w80/gb.png" class="flag-badge" alt="UK Flag">
    </div>
    <div class="card-body">
      <h3 class="card-title">United Kingdom</h3>
      <div class="visa-tags">
        <span class="v-tag">Tier 4 Student</span>
        <span class="v-tag">Skilled Worker</span>
      </div>
      <p class="card-text">Study at prestigious UK universities or work with top employers. We assist with CAS and NHS surcharge.</p>
      <span class="card-btn">Check Requirements</span>
    </div>
  </a>

  <a href="#" class="country-card">
    <div class="card-img-wrapper">
      <img src="https://images.unsplash.com/photo-1467269204594-9661b134dd2b?ixlib=rb-4.0.3&auto=format&fit=crop&w=800&q=80" class="card-img" alt="Germany">
      <img src="https://flagcdn.com/w80/de.png" class="flag-badge" alt="Germany Flag">
    </div>
    <div class="card-body">
      <h3 class="card-title">Germany</h3>
      <div class="visa-tags">
        <span class="v-tag">Student Visa</span>
        <span class="v-tag">Job Seeker</span>
        <span class="v-tag">Blue Card</span>
      </div>
      <p class="card-text">Unlock free education and engineering careers in Europe's economic powerhouse.</p>
      <span class="card-btn">Check Requirements</span>
    </div>
  </a>

  <a href="#" class="country-card">
    <div class="card-img-wrapper">
      <img src="https://images.unsplash.com/photo-1523482580672-019a2c6b95c9?ixlib=rb-4.0.3&auto=format&fit=crop&w=800&q=80" class="card-img" alt="Australia">
      <img src="https://flagcdn.com/w80/au.png" class="flag-badge" alt="Australia Flag">
    </div>
    <div class="card-body">
      <h3 class="card-title">Australia</h3>
      <div class="visa-tags">
        <span class="v-tag">Subclass 500</span>
        <span class="v-tag">PR Visa</span>
      </div>
      <p class="card-text">Simplified processing for GTE requirements and health insurance (OSHC) for Down Under.</p>
      <span class="card-btn">Check Requirements</span>
    </div>
  </a>

  <a href="#" class="country-card">
    <div class="card-img-wrapper">
      <img src="https://images.unsplash.com/photo-1503614472-8c93d56e92ce?ixlib=rb-4.0.3&auto=format&fit=crop&w=800&q=80" class="card-img" alt="Canada">
      <img src="https://flagcdn.com/w80/ca.png" class="flag-badge" alt="Canada Flag">
    </div>
    <div class="card-body">
      <h3 class="card-title">Canada</h3>
      <div class="visa-tags">
        <span class="v-tag">Study Permit</span>
        <span class="v-tag">Express Entry</span>
      </div>
      <p class="card-text">Expert guidance on SDS/Non-SDS categories and Post-Graduation Work Permits (PGWP).</p>
      <span class="card-btn">Check Requirements</span>
    </div>
  </a>

  <a href="#" class="country-card">
    <div class="card-img-wrapper">
      <img src="https://cdn.pixabay.com/photo/2013/11/03/17/23/killarney-204401_1280.jpg" class="card-img" alt="Ireland">
      <img src="https://flagcdn.com/w80/ie.png" class="flag-badge" alt="Ireland Flag">
    </div>
    <div class="card-body">
      <h3 class="card-title">Ireland</h3>
      <div class="visa-tags">
        <span class="v-tag">Stamp 2 Student</span>
        <span class="v-tag">Work Permit</span>
      </div>
      <p class="card-text">Experience the "Emerald Isle" with our end-to-end support for Irish study visas.</p>
      <span class="card-btn">Check Requirements</span>
    </div>
  </a>

  <a href="#" class="country-card">
    <div class="card-img-wrapper">
      <img src="https://images.unsplash.com/photo-1507699622177-f888f14506b8?ixlib=rb-4.0.3&auto=format&fit=crop&w=800&q=80" class="card-img" alt="New Zealand">
      <img src="https://flagcdn.com/w80/nz.png" class="flag-badge" alt="New Zealand Flag">
    </div>
    <div class="card-body">
      <h3 class="card-title">New Zealand</h3>
      <div class="visa-tags">
        <span class="v-tag">Fee Paying Student</span>
        <span class="v-tag">Post-Study Work</span>
      </div>
      <p class="card-text">Comprehensive assistance for Level 7/8/9 courses and pathway student visas.</p>
      <span class="card-btn">Check Requirements</span>
    </div>
  </a>

  <a href="#" class="country-card">
    <div class="card-img-wrapper">
      <img src="https://images.unsplash.com/photo-1512453979798-5ea90bacbf56?ixlib=rb-4.0.3&auto=format&fit=crop&w=800&q=80" class="card-img" alt="UAE">
      <img src="https://flagcdn.com/w80/ae.png" class="flag-badge" alt="UAE Flag">
    </div>
    <div class="card-body">
      <h3 class="card-title">UAE</h3>
      <div class="visa-tags">
        <span class="v-tag">Golden Visa</span>
        <span class="v-tag">Student Visa</span>
      </div>
      <p class="card-text">Fast-track your visa for Dubai, Abu Dhabi, and Sharjah education hubs.</p>
      <span class="card-btn">Check Requirements</span>
    </div>
  </a>

</div>
