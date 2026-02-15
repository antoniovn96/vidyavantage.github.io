---
layout: default
title: School Partnership Program
permalink: /school-partnership/
---

<style>
  /* HERO SECTION */
  .partner-hero {
    background: linear-gradient(rgba(10, 35, 66, 0.9), rgba(10, 35, 66, 0.8)), url('https://images.unsplash.com/photo-1524178232363-1fb2b075b655?w=1000&auto=format&fit=crop');
    background-size: cover;
    background-position: center;
    color: white;
    padding: 80px 20px;
    text-align: center;
    border-radius: 0 0 20px 20px;
    margin-bottom: 50px;
  }
  
  /* VALUE PROPOSITION GRID */
  .value-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
    gap: 30px;
    max-width: 1000px;
    margin: 0 auto 60px;
    padding: 0 20px;
  }
  
  .value-card {
    background: white;
    border: 1px solid #eee;
    border-radius: 10px;
    padding: 25px;
    text-align: center;
    box-shadow: 0 5px 15px rgba(0,0,0,0.05);
    transition: transform 0.3s;
  }
  
  .value-card:hover { transform: translateY(-5px); border-bottom: 4px solid #D4AF37; }
  .value-icon { font-size: 2.5rem; margin-bottom: 15px; display: block; }
  .value-title { color: #0A2342; font-weight: bold; margin-bottom: 10px; font-size: 1.2rem; }

  /* FORM SECTION */
  .form-wrapper {
    background: #f4f6f8;
    padding: 50px 20px;
    border-top: 1px solid #ddd;
  }
  
  .partner-form-container {
    max-width: 600px;
    margin: 0 auto;
    background: white;
    padding: 40px;
    border-radius: 10px;
    box-shadow: 0 4px 15px rgba(0,0,0,0.1);
    border-top: 5px solid #D4AF37;
  }

  .form-group { margin-bottom: 20px; }
  
  label { display: block; font-weight: bold; margin-bottom: 8px; color: #0A2342; font-size: 0.9rem; }
  
  input, select, textarea {
    width: 100%;
    padding: 12px;
    border: 1px solid #ccc;
    border-radius: 5px;
    font-size: 1rem;
    box-sizing: border-box;
    font-family: inherit;
  }
  
  input:focus, textarea:focus { border-color: #D4AF37; outline: none; box-shadow: 0 0 5px rgba(212, 175, 55, 0.3); }

  .btn-submit {
    background-color: #0A2342;
    color: white;
    border: none;
    padding: 15px 30px;
    font-size: 1.1rem;
    font-weight: bold;
    border-radius: 50px;
    cursor: pointer;
    width: 100%;
    transition: background 0.3s;
  }
  
  .btn-submit:hover { background-color: #D4AF37; color: #0A2342; }
</style>

<div class="partner-hero">
  <h1 style="color:white; font-size: 2.5rem;">Empower Your Students.</h1>
  <p style="font-size: 1.2rem; max-width: 700px; margin: 10px auto;">
    Partner with VidyaVantage to bring verified career intelligence, psychometric testing, and global university access to your campus.
  </p>
</div>

<div style="text-align: center; margin-bottom: 40px;">
  <h2 style="color: #0A2342;">Why Top Schools Choose Us</h2>
  <p style="color: #666;">We don't just give advice. We build careers.</p>
</div>

<div class="value-grid">
  <div class="value-card">
    <span class="value-icon">🧠</span>
    <div class="value-title">Psychometric Testing</div>
    <p>Grade 9 & 10 Stream Selection based on aptitude, not just marks. We use scientific tools to identify student strengths.</p>
  </div>

  <div class="value-card">
    <span class="value-icon">🌏</span>
    <div class="value-title">Study Abroad Desk</div>
    <p>Exclusive access to our database of 500+ universities. We handle profile building, essays, and visa guidance.</p>
  </div>

  <div class="value-card">
    <span class="value-icon">🎤</span>
    <div class="value-title">Alumni Workshops</div>
    <p>We bring real professionals (Pilots, Lawyers, Data Scientists) to your school for interactive "Day in the Life" sessions.</p>
  </div>
</div>

<div class="form-wrapper">
  <div style="text-align: center; margin-bottom: 30px;">
    <h2 style="color: #0A2342;">Request a Proposal</h2>
    <p>Fill in the details below. We typically respond within 24 hours.</p>
  </div>

  <div class="partner-form-container">
    <form action="https://formsubmit.co/partners.vidyavantage@gmail.com" method="POST">
      
      <input type="text" name="_honey" style="display:none">
      <input type="hidden" name="_captcha" value="false">
      <input type="hidden" name="_next" value="https://antoniovn96.github.io/vidyavantage.github.io/partner-success/">
      <input type="hidden" name="_subject" value="New School Partnership Lead!">
      <input type="hidden" name="_cc" value="email"> 

      <div class="form-group">
        <label>School Name</label>
        <input type="text" name="School_Name" required placeholder="e.g. St. Michals's High School">
      </div>

      <div class="form-group">
        <label>City & State</label>
        <input type="text" name="Location" required placeholder="e.g. Bangalore, Karnataka">
      </div>

      <div class="form-group">
        <label>Contact Person</label>
        <input type="text" name="Contact_Person" required placeholder="Name & Designation">
      </div>

      <div class="form-group">
        <label>Official Email Address</label>
        <input type="email" name="email" required placeholder="Where should we send the proposal?">
      </div>

      <div class="form-group">
        <label>Phone Number</label>
        <input type="tel" name="Phone" required>
      </div>

      <div class="form-group">
        <label>I am interested in:</label>
        <select name="Service_Type">
          <option value="Career Counselling Workshops">Career Counselling Workshops</option>
          <option value="Stream Selection Testing">Stream Selection (Grade 10)</option>
          <option value="Study Abroad Guidance">Study Abroad Guidance</option>
          <option value="Full Annual Partnership">Full Annual Partnership</option>
        </select>
      </div>

      <div class="form-group">
        <label>Specific Goals / Message</label>
        <textarea name="Message" rows="4" placeholder="Tell us a bit about your student strength or specific needs..."></textarea>
      </div>

      <button type="submit" class="btn-submit">Send Request</button>
    </form>
  </div>
</div>
