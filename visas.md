---
layout: default
title: Global Visa Services 🌏
permalink: /visa/
image: "https://images.unsplash.com/photo-1526778548025-fa2f459cd5c1?w=1200&h=630&fit=crop"
description: "Expert Visa Assistance for USA, UK, Canada, Australia, Germany, and more. Student, Tourist, and Work Visas made easy."
---

<style>
  /* HERO SECTION */
  .visa-hero {
    background: linear-gradient(rgba(0,0,0,0.6), rgba(0,0,0,0.6)), url('https://images.unsplash.com/photo-1436491865332-7a61a109cc05?w=1600&fit=crop');
    background-size: cover;
    background-position: center;
    color: white;
    text-align: center;
    padding: 100px 20px;
    margin-bottom: 40px;
  }
  .visa-hero h1 { font-size: 3.5rem; margin: 0; font-weight: 800; }
  .visa-hero p { font-size: 1.2rem; margin-top: 15px; opacity: 0.9; }

  /* COUNTRY GRID */
  .country-grid {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
    gap: 25px;
    padding: 0 20px 60px;
    max-width: 1200px;
    margin: 0 auto;
  }

  /* COUNTRY CARD */
  .country-card {
    background: white;
    border-radius: 12px;
    overflow: hidden;
    box-shadow: 0 5px 15px rgba(0,0,0,0.08);
    transition: transform 0.3s;
    text-decoration: none;
    color: inherit;
    display: flex;
    flex-direction: column;
  }
  .country-card:hover { transform: translateY(-5px); box-shadow: 0 12px 25px rgba(0,0,0,0.15); }

  .card-img-container {
    height: 180px;
    overflow: hidden;
    position: relative;
  }
  .card-img {
    width: 100%;
    height: 100%;
    object-fit: cover;
    transition: transform 0.5s;
  }
  .country-card:hover .card-img { transform: scale(1.1); }

  .flag-badge {
    position: absolute;
    bottom: -20px;
    right: 20px;
    width: 50px;
    height: 50px;
    border-radius: 50%;
    border: 3px solid white;
    background: white;
    object-fit: cover;
    box-shadow: 0 3px 10px rgba(0,0,0,0.2);
  }

  .card-body { padding: 25px 20px 20px; }
  .card-title { font-size: 1.4rem; font-weight: 700; margin: 0 0 10px; color: #2c3e50; }
  .card-text { font-size: 0.95rem; color: #666; line-height: 1.5; }
  .card-link { 
    display: inline-block; 
    margin-top: 15px; 
    color: #007bff; 
    font-weight: 600; 
    font-size: 0.9rem;
  }

  /* Responsive */
  @media (max-width: 768px) {
    .visa-hero h1 { font-size: 2.5rem; }
  }
</style>

<div class="visa-hero">
  <h1>Global Visa Services</h1>
  <p>Your gateway to the world. Simplified visa processing for students and travelers.</p>
</div>

<div class="country-grid">

  <a href="#" class="country-card">
    <div class="card-img-container">
      <img src="https://cdn.pixabay.com/photo/2014/11/22/00/03/new-york-540807_1280.jpg" class="card-img" alt="USA">
      <img src="https://flagcdn.com/w80/us.png" class="flag-badge" alt="USA Flag">
    </div>
    <div class="card-body">
      <h3 class="card-title">USA</h3>
      <p class="card-text">F1 Student Visas, H1B Work Visas, and B1/B2 Tourist Visas assistance.</p>
      <span class="card-link">Learn More &rarr;</span>
    </div>
  </a>

  <a href="#" class="country-card">
    <div class="card-img-container">
      <img src="https://images.unsplash.com/photo-1513635269975-59663e0ac1ad?w=800&q=80" class="card-img" alt="UK">
      <img src="https://flagcdn.com/w80/gb.png" class="flag-badge" alt="UK Flag">
    </div>
    <div class="card-body">
      <h3 class="card-title">United Kingdom</h3>
      <p class="card-text">Tier 4 Student Visas and Skilled Worker Visas guidance.</p>
      <span class="card-link">Learn More &rarr;</span>
    </div>
  </a>

  <a href="#" class="country-card">
    <div class="card-img-container">
      <img src="https://img.freepik.com/free-photo/cityscape-frankfurt-covered-modern-buildings-sunset-germany_181624-15984.jpg" class="card-img" alt="Germany">
      <img src="https://flagcdn.com/w80/de.png" class="flag-badge" alt="Germany Flag">
    </div>
    <div class="card-body">
      <h3 class="card-title">Germany</h3>
      <p class="card-text">Expert help with Student Visas, Job Seeker Visas, and EU Blue Cards.</p>
      <span class="card-link">Learn More &rarr;</span>
    </div>
  </a>

  <a href="#" class="country-card">
    <div class="card-img-container">
      <img src="https://images.unsplash.com/photo-1523482580672-019a2c6b95c9?w=800&q=80" class="card-img" alt="Australia">
      <img src="https://flagcdn.com/w80/au.png" class="flag-badge" alt="Australia Flag">
    </div>
    <div class="card-body">
      <h3 class="card-title">Australia</h3>
      <p class="card-text">Subclass 500 (Student) and PR Visa processing made simple.</p>
      <span class="card-link">Learn More &rarr;</span>
    </div>
  </a>

  <a href="#" class="country-card">
    <div class="card-img-container">
      <img src="https://cdn.pixabay.com/photo/2013/11/03/17/23/killarney-204401_1280.jpg" class="card-img" alt="Ireland">
      <img src="https://flagcdn.com/w80/ie.png" class="flag-badge" alt="Ireland Flag">
    </div>
    <div class="card-body">
      <h3 class="card-title">Ireland</h3>
      <p class="card-text">Study in Ireland with complete support for Stamp 2 Student Visas.</p>
      <span class="card-link">Learn More &rarr;</span>
    </div>
  </a>

  <a href="#" class="country-card">
    <div class="card-img-container">
      <img src="https://images.unsplash.com/photo-1507699622177-f888f14506b8?w=800&q=80" class="card-img" alt="New Zealand">
      <img src="https://flagcdn.com/w80/nz.png" class="flag-badge" alt="New Zealand Flag">
    </div>
    <div class="card-body">
      <h3 class="card-title">New Zealand</h3>
      <p class="card-text">Fee Paying Student Visa and Post-Study Work Visa assistance.</p>
      <span class="card-link">Learn More &rarr;</span>
    </div>
  </a>

  <a href="#" class="country-card">
    <div class="card-img-container">
      <img src="https://images.unsplash.com/photo-1512453979798-5ea90bacbf56?w=800&q=80" class="card-img" alt="UAE">
      <img src="https://flagcdn.com/w80/ae.png" class="flag-badge" alt="UAE Flag">
    </div>
    <div class="card-body">
      <h3 class="card-title">UAE</h3>
      <p class="card-text">Golden Visa, Student Visa, and Work Permit services for Dubai & Abu Dhabi.</p>
      <span class="card-link">Learn More &rarr;</span>
    </div>
  </a>

  <a href="#" class="country-card">
    <div class="card-img-container">
      <img src="https://images.unsplash.com/photo-1503614472-8c93d56e92ce?w=800&q=80" class="card-img" alt="Canada">
      <img src="https://flagcdn.com/w80/ca.png" class="flag-badge" alt="Canada Flag">
    </div>
    <div class="card-body">
      <h3 class="card-title">Canada</h3>
      <p class="card-text">Study Permits, Express Entry, and PNP visa guidance.</p>
      <span class="card-link">Learn More &rarr;</span>
    </div>
  </a>

</div>
