---
layout: default
title: Global Visa Guide
permalink: /visas/
---

# 🌏 Global Study Visa Guide
**Verified rules for Indian Students (Updated 2026)**

<style>
  .visa-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 20px; }
  .visa-card { border: 1px solid #ddd; border-top: 5px solid #0A2342; padding: 20px; background: white; border-radius: 8px; box-shadow: 0 2px 5px rgba(0,0,0,0.1); }
  .visa-card h3 { color: #0A2342; margin-top: 0; }
  .flag { font-size: 2em; float: right; }
  .tag { background: #e3f2fd; color: #0d47a1; padding: 2px 8px; border-radius: 4px; font-size: 0.9em; }
</style>

<div class="visa-grid">
  {% for visa in site.data.visas %}
  <div class="visa-card">
    <span class="flag">{{ visa.flag }}</span>
    <h3>{{ visa.country }}</h3>
    <p><strong>Visa Type:</strong> {{ visa.visa_type }}</p>
    <hr>
    <p>💰 <strong>Cost:</strong> {{ visa.cost }}</p>
    <p>🏦 <strong>Funds:</strong> {{ visa.proof_of_funds }}</p>
    <p>💼 <strong>Work Rights:</strong> {{ visa.work_rights }}</p>
    <p>🎓 <strong>Post-Study:</strong> {{ visa.post_study_work }}</p>
    <p>📝 <strong>Exams:</strong> 
      {% for exam in visa.exams_needed %}
        <span class="tag">{{ exam }}</span>
      {% endfor %}
    </p>
  </div>
  {% endfor %}
</div>

---
*Disclaimer: Visa rules change frequently. Always verify with the official embassy.*
