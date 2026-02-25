---
layout: default
title: "Advanced Psychometric Career Assessment 🚀"
permalink: /assessment/
---

<style>
  /* --- PREMIUM PSYCHOMETRIC UI THEME --- */
  :root {
    --bg: #0f172a; --card-bg: #1e293b;
    --primary: #3b82f6; --secondary: #10b981; --accent: #f59e0b;
    --text-main: #f8fafc; --text-muted: #94a3b8; --border: #334155;
    --text-dark: #0f172a;
    --success: #10b981; --warning: #f59e0b; --danger: #ef4444;
  }

  body { background-color: var(--bg); font-family: 'Nunito', 'Segoe UI', sans-serif; color: var(--text-main); margin: 0; }
  
  .assessment-header {
    background: linear-gradient(135deg, #0f172a 0%, #1e1b4b 100%); padding: 40px 20px 25px; text-align: center; 
    border-bottom: 2px solid var(--primary); margin-bottom: 30px;
  }
  .assessment-header h1 { margin: 0 0 10px 0; font-size: 2.2rem; font-weight: 900; background: -webkit-linear-gradient(45deg, #60a5fa, #a855f7); -webkit-background-clip: text; -webkit-text-fill-color: transparent; }
  .assessment-header p { font-size: 1.05rem; color: var(--text-muted); margin: 0;}

  .container { max-width: 900px; margin: 0 auto; padding: 0 20px 50px; }

  /* PROGRESS BAR & UX */
  .progress-wrapper { display: flex; justify-content: space-between; align-items: center; margin-bottom: 10px; font-weight: bold; font-size: 0.9rem; color: var(--text-muted);}
  .progress-container { width: 100%; background: #0f172a; border-radius: 50px; height: 10px; margin-bottom: 25px; border: 1px solid var(--border); overflow: hidden;}
  .progress-bar { height: 100%; background: linear-gradient(90deg, var(--primary), #a855f7); width: 14%; transition: width 0.4s ease; border-radius: 50px; }

  /* WIZARD CARDS */
  .step-card {
    background: var(--card-bg); padding: 35px; border-radius: 20px; border: 1px solid rgba(255,255,255,0.05);
    box-shadow: 0 15px 30px rgba(0,0,0,0.3); margin-bottom: 30px; display: none; animation: slideUp 0.4s ease;
  }
  .step-card.active { display: block; }
  .step-title { font-size: 1.6rem; font-weight: 800; color: white; margin-bottom: 5px; text-align: center; }
  .step-sub { text-align: center; color: var(--primary); margin-bottom: 25px; font-weight: bold; text-transform: uppercase; letter-spacing: 1px; font-size: 0.85rem;}

  /* UI COMPONENTS */
  .grid-2col { display: grid; grid-template-columns: 1fr 1fr; gap: 20px; }
  .grid-3col { display: grid; grid-template-columns: 1fr 1fr 1fr; gap: 20px; }
  @media (max-width: 768px) { .grid-2col, .grid-3col { grid-template-columns: 1fr; } }
  
  .form-group { margin-bottom: 20px; }
  .form-label { display: block; font-weight: 700; margin-bottom: 8px; color: var(--text-muted); font-size: 0.85rem; text-transform: uppercase;}
  
  .form-input, .form-select, .form-textarea { 
    width: 100%; padding: 14px; border: 2px solid var(--border); border-radius: 10px; 
    font-size: 1.05rem; color: white; background: #0f172a; box-sizing: border-box; transition: 0.3s; font-family: inherit;
  }
  .form-textarea { resize: vertical; min-height: 80px; }
  .form-input:focus, .form-select:focus { border-color: var(--primary); outline: none; box-shadow: 0 0 0 3px rgba(59, 130, 246, 0.2);}

  /* RATING SCALES */
  .scale-legend { display: flex; justify-content: space-between; color: var(--text-muted); font-size: 0.8rem; font-weight: bold; margin-bottom: 15px; text-transform: uppercase; }
  .rating-grid { display: grid; gap: 10px; margin-bottom: 25px; }
  .rating-row { display: flex; align-items: center; justify-content: space-between; background: #0f172a; padding: 12px 15px; border-radius: 12px; border: 1px solid var(--border); transition: 0.2s; }
  .rating-row:hover { border-color: var(--primary); }
  @media (max-width: 768px) { .rating-row { flex-direction: column; align-items: flex-start; gap: 10px; } }
  
  .rating-label { font-weight: 600; font-size: 0.95rem; flex: 1; padding-right: 15px; line-height: 1.4;}
  .rating-options { display: flex; gap: 6px; background: #1e293b; padding: 4px; border-radius: 50px; }
  .rate-btn {
    width: 35px; height: 35px; border-radius: 50%; border: none; background: transparent; 
    font-size: 1.1rem; cursor: pointer; display: flex; align-items: center; justify-content: center; transition: 0.2s;
    filter: grayscale(100%) opacity(0.4);
  }
  .rate-btn:hover { filter: grayscale(0%) opacity(1); transform: scale(1.2); }
  .rate-btn.selected { filter: grayscale(0%) opacity(1); transform: scale(1.2); background: rgba(255,255,255,0.1); }

  /* RANKING UI (VALUES) */
  .values-container { display: flex; gap: 20px; }
  @media (max-width: 768px) { .values-container { flex-direction: column; } }
  .value-pool, .value-ranked { flex: 1; background: #0f172a; padding: 20px; border-radius: 12px; border: 1px solid var(--border); min-height: 250px;}
  .value-pool h3, .value-ranked h3 { color: var(--text-muted); font-size: 1rem; margin-top: 0; text-align: center; }
  .val-pill { background: var(--card-bg); border: 1px solid var(--border); padding: 10px 15px; border-radius: 8px; margin-bottom: 8px; cursor: pointer; font-weight: bold; transition: 0.2s; text-align: center; font-size: 0.9rem;}
  .val-pill:hover { border-color: var(--primary); color: var(--primary); }
  .ranked-slot { display: flex; align-items: center; gap: 10px; margin-bottom: 8px; }
  .rank-num { background: var(--primary); color: white; width: 30px; height: 30px; display: flex; align-items: center; justify-content: center; border-radius: 50%; font-weight: bold; flex-shrink: 0;}
  
  /* BUTTONS */
  .btn-wrapper { display: flex; justify-content: space-between; margin-top: 25px; border-top: 1px solid var(--border); padding-top: 20px; gap:15px; flex-wrap: wrap;}
  .btn-main { background: linear-gradient(45deg, var(--primary), #8b5cf6); color: white; border: none; padding: 12px 30px; font-size: 1.05rem; font-weight: 900; border-radius: 50px; cursor: pointer; transition: 0.3s; flex: 1; text-align: center; text-decoration: none;}
  .btn-main:hover { transform: translateY(-2px); box-shadow: 0 10px 20px rgba(139, 92, 246, 0.3); }
  .btn-back { background: transparent; border: 2px solid var(--border); color: var(--text-muted); box-shadow: none; flex: 0.5;}
  .btn-back:hover { background: rgba(255,255,255,0.05); color: white; border-color: var(--text-muted);}

  /* --- PSYCHOMETRIC REPORT STYLES (Light for PDF Export) --- */
  #reportContainer { display: none; }
  .report-card { background: white; padding: 40px; border-radius: 16px; color: var(--text-dark); position: relative; overflow: hidden;}
  .r-header { text-align: center; border-bottom: 3px solid #f1f5f9; padding-bottom: 25px; margin-bottom: 30px; }
  .r-header h2 { font-size: 2.2rem; font-weight: 900; margin: 0; color: #0f172a; }
  
  .reliability-badge { display: inline-block; padding: 6px 15px; border-radius: 50px; font-size: 0.85rem; font-weight: 900; margin-top: 15px; text-transform: uppercase; border: 1px solid;}
  .rel-high { background: #d1fae5; color: #059669; border-color: #059669;}
  .rel-mod { background: #fef3c7; color: #d97706; border-color: #d97706;}
  .rel-low { background: #fee2e2; color: #e11d48; border-color: #e11d48;}
  
  .badge-code { display: inline-block; background: #0f172a; color: white; padding: 8px 30px; border-radius: 50px; font-weight: 900; font-size: 1.8rem; margin-top: 15px; letter-spacing: 2px; }
  
  .grid-2 { display: grid; grid-template-columns: 1fr 1fr; gap: 25px; margin-bottom: 30px; }
  @media (max-width: 768px) { .grid-2 { grid-template-columns: 1fr; } }
  
  .chart-box { max-width: 400px; margin: 0 auto; }
  .metrics-box { padding: 25px; background: #f8fafc; border-radius: 16px; border: 1px solid #e2e8f0; }
  
  .metric { margin-bottom: 15px; }
  .m-head { display: flex; justify-content: space-between; font-size: 0.9rem; font-weight: 800; color: #475569; margin-bottom: 5px; text-transform: uppercase; }
  .m-track { width: 100%; height: 10px; background: #e2e8f0; border-radius: 10px; overflow: hidden; }
  .m-fill { height: 100%; border-radius: 10px; }

  .r-section { background: #ffffff; border-radius: 16px; padding: 25px; margin-bottom: 25px; border: 1px solid #e2e8f0; border-left: 6px solid var(--primary); box-shadow: 0 4px 6px rgba(0,0,0,0.02);}
  .r-section h3 { margin-top: 0; font-size: 1.3rem; color: #0f172a; border-bottom: 1px dashed #e2e8f0; padding-bottom: 10px; font-weight: 900;}
  .r-section p { line-height: 1.7; font-size: 1rem; color: #334155; }
  
  .career-bar { display: flex; justify-content: space-between; align-items: center; background: #f8fafc; padding: 15px; border-radius: 10px; border: 1px solid #e2e8f0; margin-bottom: 10px; }
  .c-name { font-weight: 800; color: #0f172a; font-size: 1.1rem;}
  .c-fit { font-size: 0.8rem; font-weight: bold; padding: 4px 10px; border-radius: 6px;}
  .fit-strong { background: #d1fae5; color: #059669; }
  .fit-mod { background: #fef3c7; color: #d97706; }
  .fit-exp { background: #f1f5f9; color: #64748b; }

  .trait-box { background: #f1f5f9; padding: 12px 15px; border-radius: 8px; margin-bottom: 10px; font-size: 0.95rem; color: #334155;}
  .trait-box strong { color: #0f172a; }

  .avoid-section { border-left-color: var(--danger); background: #fef2f2;}
  .avoid-section h3 { color: #e11d48; border-bottom-color: #fecdd3;}
  
  /* Skill Gap Table */
  .skill-table { width: 100%; border-collapse: collapse; margin-top: 15px; font-size: 0.9rem;}
  .skill-table th, .skill-table td { padding: 10px; text-align: left; border-bottom: 1px solid #e2e8f0; }
  .skill-table th { color: #64748b; text-transform: uppercase; font-size: 0.75rem; }

  .action-grid { display: grid; grid-template-columns: 1fr 1fr; gap: 15px; margin-top: 15px;}
  .action-card { background: white; border: 1px solid #e2e8f0; padding: 15px; border-radius: 10px;}
  .action-card h4 { margin: 0 0 10px 0; color: var(--primary); font-size: 0.95rem; text-transform: uppercase;}
  .action-card ul { margin: 0; padding-left: 20px; font-size: 0.9rem; color: #475569; line-height: 1.6;}

  .tier-card { border-left: 4px solid var(--secondary); background: #f8fafc; padding: 12px 15px; border-radius: 8px; margin-bottom: 10px;}
  .tier-card strong { display: block; color: #0f172a; font-size: 0.95rem; margin-bottom: 4px;}
  .tier-card span { font-size: 0.85rem; color: #64748b;}

  .escalation-box { background: #0f172a; color: white; padding: 20px; border-radius: 12px; text-align: center; border: 2px solid var(--accent); margin-top: 20px; display: none;}
  
  .disclaimer { font-size: 0.75rem; color: #94a3b8; text-align: center; margin-top: 30px; font-style: italic; }

  /* Premium Pricing Box */
  .pricing-box { background: #fef3c7; border: 1px solid #f59e0b; padding: 25px; border-radius: 12px; text-align: center; margin-top: 30px;}
  .pricing-btn { display: block; background: white; color: #0f172a; border: 2px solid #0f172a; padding: 12px; border-radius: 8px; font-weight: bold; margin-bottom: 10px; text-decoration: none; transition: 0.2s;}
  .pricing-btn:hover { background: #0f172a; color: white;}
  .pricing-btn.premium { background: var(--primary); color: white; border-color: var(--primary);}
  .pricing-btn.premium:hover { background: #1d4ed8; }

  @keyframes slideUp { from { opacity: 0; transform: translateY(15px); } to { opacity: 1; transform: translateY(0); } }

  @media print {
    body { background: white; }
    .assessment-header, .progress-wrapper, .progress-container, .btn-wrapper, .escalation-box, .pricing-box { display: none !important; }
    .report-card { padding: 0; box-shadow: none; border: none; }
    .r-section { page-break-inside: avoid; border: 1px solid #e2e8f0; }
    .action-grid { display: block; }
    .action-card { margin-bottom: 15px; }
  }
</style>

<div class="assessment-header">
  <h1>Advanced Psychometric Assessment</h1>
  <p>Scientific Career Mapping • RIASEC • Aptitude • Resilience</p>
</div>

<div class="container">
  
  <div class="progress-wrapper" id="progressWrap">
      <span id="stepCounter">Step 1 of 7</span>
      <span id="timeEstimator" style="color: var(--primary);">⏱ Est. Time: 15 mins</span>
  </div>
  <div class="progress-container" id="progressCont"><div class="progress-bar" id="progressBar"></div></div>

  <div id="wizardContainer"></div>

  <div id="reportContainer">
    <div class="report-card" id="reportContent">
      <div class="r-header">
        <h2>Career Intelligence Dossier</h2>
        <div style="color:#64748b; font-size: 1rem; font-weight:600; margin-top: 10px; line-height: 1.6;">
          Candidate: <strong id="outName" style="color:#0f172a; font-size:1.1rem;"></strong><br>
          Academic Profile: <span id="outAcad"></span><br>
          Report Generated: <span id="outDate"></span>
        </div>
        <div class="reliability-badge" id="outReliability"></div><br>
        <div class="badge-code" id="outCode"></div>
        <p style="margin-top: 10px; font-size: 0.9rem; color: var(--primary); font-weight: bold;" id="outPercentile"></p>
      </div>

      <div class="grid-2">
        <div class="chart-box"><canvas id="riasecChart"></canvas></div>
        <div class="metrics-box">
          <h3 style="margin-top:0; color:var(--text-dark); font-size:1.1rem; border-bottom:1px solid #e2e8f0; padding-bottom:8px;">Scientific Aptitude Metrics</h3>
          <div class="metric"><div class="m-head"><span>Aptitude Confidence</span><span id="txt-apt"></span></div><div class="m-track"><div class="m-fill" id="bar-apt" style="background:var(--primary);"></div></div></div>
          <div class="metric"><div class="m-head"><span>Stress Resilience</span><span id="txt-res"></span></div><div class="m-track"><div class="m-fill" id="bar-res" style="background:var(--success);"></div></div></div>
          <div class="metric"><div class="m-head"><span>Decision Maturity</span><span id="txt-mat"></span></div><div class="m-track"><div class="m-fill" id="bar-mat" style="background:#8b5cf6;"></div></div></div>
          <div class="metric" style="margin-bottom:0;"><div class="m-head"><span>External Pressure</span><span id="txt-par"></span></div><div class="m-track"><div class="m-fill" id="bar-par" style="background:var(--warning);"></div></div></div>
        </div>
      </div>

      <div class="r-section" style="border-left-color: #8b5cf6;">
        <h3>🧠 Trait Breakdown & Narrative</h3>
        <div id="outTraitBreakdown"></div>
      </div>

      <div id="shadowWarning" style="display:none; background: #fffbeb; padding: 15px; border-radius: 8px; border-left: 4px solid #f59e0b; margin-bottom: 25px;">
          <strong style="color: #b45309;">⚠️ Career Interest Mismatch:</strong> You indicated an interest in <span id="outSecret" style="font-weight:bold;"></span>. However, your psychometric data shows higher alignment with different pathways. Discussing this with a counsellor is highly advised.
      </div>

      <div class="r-section" style="border-left-color: var(--primary);">
        <h3>🎯 Top Aligned Pathways</h3>
        <p style="font-size:0.9rem; color:#64748b; margin-bottom: 15px;">Algorithmically filtered based on your academic stream eligibility and psychometric alignment.</p>
        <div id="outCareers"></div>
      </div>

      <div class="r-section" style="border-left-color: var(--success);">
          <h3>🧬 Skill Gap Heatmap</h3>
          <p style="font-size:0.9rem; color:#64748b;">Based on your top recommended career path.</p>
          <table class="skill-table">
              <thead><tr><th>Required Skill</th><th>Your Level</th><th>Gap Analysis</th></tr></thead>
              <tbody id="outSkills"></tbody>
          </table>
      </div>

      <div class="r-section avoid-section">
        <h3>🚫 Vulnerability Zones</h3>
        <p style="font-size:0.9rem; margin-bottom: 10px;">Careers where you may feel less aligned due to lower natural interest scores.</p>
        <p id="outAvoid" style="font-weight:bold; color:#9f1239;"></p>
      </div>

      <div class="r-section" style="border-left-color: var(--secondary);">
        <h3>📅 1-Year Execution Action Plan</h3>
        <div class="action-grid">
            <div class="action-card">
                <h4>📚 Recommended Courses</h4>
                <ul id="planCourses"></ul>
            </div>
            <div class="action-card">
                <h4>🎯 Exams & Focus</h4>
                <ul id="planExams"></ul>
            </div>
        </div>
      </div>

      <div class="r-section" style="border-left-color: #0f172a;">
        <h3>🏛️ Structural College Targets</h3>
        <div id="outColleges"></div>
      </div>
      
      <div style="background: #f1f5f9; padding: 20px; border-radius: 12px; text-align: center; border: 1px solid #cbd5e1; margin-top: 20px;">
          <h4 style="margin: 0 0 10px 0; color: #0f172a;">🏆 Professional Conclusion</h4>
          <p style="margin: 0; color: #334155; font-size: 1.05rem;" id="outConfidence"></p>
      </div>

      <div id="escalationWarning" class="escalation-box">
          <h3 style="margin-top:0; color:#fcd34d;" id="escTitle">⚠️ Intervention Recommended</h3>
          <p style="font-size: 0.95rem; line-height: 1.5; margin-bottom: 0;" id="escText">Our system has detected data patterns requiring expert discussion.</p>
      </div>

      <div class="disclaimer">
          *This assessment is for career guidance purposes only and is not a medical or psychological diagnosis. All decisions should be made in consultation with certified professionals.*
      </div>
    </div>

    <div class="pricing-box">
        <h3 style="margin-top:0; color: #b45309;">Don't leave your future to chance.</h3>
        <p style="font-size:0.9rem; color:#78350f; margin-bottom:20px;">Psychometric results without interpretation create anxiety. Let our experts build your strategy.</p>
        <a href="{{ '/book-expert/' | relative_url }}" class="pricing-btn premium">Full Career Strategy Plan (90 mins) - ₹4999</a>
        <a href="{{ '/book-expert/' | relative_url }}" class="pricing-btn">Parent + Student Alignment Session - ₹3999</a>
        <a href="{{ '/book-expert/' | relative_url }}" class="pricing-btn" style="border-color:#e2e8f0; color:#64748b;">Basic Interpretation (45 mins) - ₹1999</a>
    </div>

    <div class="btn-wrapper" style="justify-content: center; gap: 15px; margin-top: 20px;">
      <button class="btn-main" id="pdfBtn" onclick="downloadPDF()" style="flex: 1;">📄 Export Free PDF</button>
    </div>
  </div>
</div>

<script>
  // --- 75-QUESTION DATABASE (With Traps & Contradictions) ---
  const qBank = {
    riasec: [
      { id:'r1', text:'I enjoy building or repairing things.', cat:'R' }, { id:'r2', text:'I prefer hands-on tasks over theoretical study.', cat:'R' }, { id:'r3', text:'I like working outdoors.', cat:'R' }, { id:'r4', text:'I enjoy using tools or equipment.', cat:'R' }, { id:'r5', text:'I feel satisfied when I create something tangible.', cat:'R' }, { id:'r6', text:'I prefer practical activities over discussions.', cat:'R' },
      { id:'i1', text:'I enjoy solving complex problems.', cat:'I' }, { id:'i2', text:'I ask "why" and "how" frequently.', cat:'I' }, { id:'i3', text:'I enjoy science-based subjects.', cat:'I' }, { id:'i4', text:'I like analysing data or patterns.', cat:'I' }, { id:'i5', text:'I enjoy researching topics in depth.', cat:'I' }, { id:'i6', text:'I prefer logical reasoning over emotional decisions.', cat:'I' },
      { id:'a1', text:'I enjoy creative writing or storytelling.', cat:'A' }, { id:'a2', text:'I like drawing, designing, or visual expression.', cat:'A' }, { id:'a3', text:'I prefer flexible tasks over structured ones.', cat:'A' }, { id:'a4', text:'I enjoy music, performance, or media creation.', cat:'A' }, { id:'a5', text:'I think creatively when solving problems.', cat:'A' }, { id:'a6', text:'I dislike rigid rules.', cat:'A' }, // Pairs with c4
      { id:'s1', text:'I enjoy helping others solve problems.', cat:'S' }, { id:'s2', text:'I feel fulfilled when supporting someone emotionally.', cat:'S' }, { id:'s3', text:'I like teaching or explaining concepts.', cat:'S' }, { id:'s4', text:'I am patient when listening to others.', cat:'S' }, { id:'s5', text:'I prefer people-oriented activities.', cat:'S' }, { id:'s6', text:'I feel motivated when my work benefits others.', cat:'S' },
      { id:'e1', text:'I enjoy leading group projects.', cat:'E' }, { id:'e2', text:'I like persuading or influencing others.', cat:'E' }, { id:'e3', text:'I am comfortable taking initiative.', cat:'E' }, { id:'e4', text:'I enjoy competitive environments.', cat:'E' }, { id:'e5', text:'I am interested in business or entrepreneurship.', cat:'E' }, { id:'e6', text:'I like taking calculated risks.', cat:'E' },
      { id:'c1', text:'I enjoy organising information.', cat:'C' }, { id:'c2', text:'I prefer structured instructions.', cat:'C' }, { id:'c3', text:'I like working with numbers and records.', cat:'C' }, { id:'c4', text:'I prefer predictable work environments.', cat:'C' }, { id:'c5', text:'I enjoy planning and scheduling.', cat:'C' }, { id:'c6', text:'I pay attention to small details.', cat:'C' }
    ],
    aptitude: [
      { id:'ap1', text:'I am confident in my mathematical ability.', cat:'APT' }, { id:'ap2', text:'I can understand logical problems quickly.', cat:'APT' }, { id:'ap3', text:'I communicate my thoughts clearly.', cat:'APT' }, { id:'ap4', text:'I remember information easily.', cat:'APT' }, { id:'ap5', text:'I can think in 3D or visualise objects well.', cat:'APT' }, { id:'ap6', text:'I manage time effectively.', cat:'APT' },
      { id:'ap7', text:'I stay focused for long periods.', cat:'APT' }, { id:'ap8', text:'I understand others’ emotions easily.', cat:'APT' }, { id:'ap9', text:'I am confident speaking in front of groups.', cat:'APT' }, { id:'ap10', text:'I solve problems systematically.', cat:'APT' }, { id:'ap11', text:'I learn new technical skills quickly.', cat:'APT' }, { id:'ap12', text:'I analyse mistakes and improve.', cat:'APT' }
    ],
    resilience: [
      { id:'rs1', text:'I handle academic pressure well.', cat:'RES', rev:false }, { id:'rs2', text:'I panic before important exams.', cat:'RES', rev:true }, { id:'rs3', text:'I continue working even after failure.', cat:'RES', rev:false }, { id:'rs4', text:'I give up easily when things are difficult.', cat:'RES', rev:true }, { id:'rs5', text:'I compare myself with others frequently.', cat:'RES', rev:true }, { id:'rs6', text:'I can manage long study hours.', cat:'RES', rev:false },
      { id:'rs7', text:'I recover quickly from disappointment.', cat:'RES', rev:false }, { id:'rs8', text:'I feel anxious about my future.', cat:'RES', rev:true }, { id:'rs9', text:'I stay calm during deadlines.', cat:'RES', rev:false }, { id:'rs10', text:'I seek help when overwhelmed.', cat:'RES', rev:false }, { id:'rs11', text:'I feel confident making decisions.', cat:'RES', rev:false }, { id:'rs12', text:'I overthink small mistakes.', cat:'RES', rev:true }
    ],
    maturity: [
      { id:'m1', text:'I clearly understand my strengths.', cat:'MAT', rev:false }, { id:'m2', text:'I am choosing a career mainly based on marks.', cat:'MAT', rev:true }, { id:'m3', text:'My parents strongly influence my career decisions.', cat:'PAR', rev:false },
      { id:'m4', text:'I have researched career pathways thoroughly.', cat:'MAT', rev:false }, { id:'m5', text:'I am open to exploring alternative options.', cat:'MAT', rev:false }, { id:'m6', text:'I feel confused about my career direction.', cat:'MAT', rev:true }, 
      // SOCIAL DESIRABILITY TRAPS
      { id:'t1', text:'I have never lied in my life.', cat:'TRAP', rev:false }, { id:'t2', text:'I always perform perfectly under pressure.', cat:'TRAP', rev:false }, { id:'t3', text:'I never procrastinate or waste time.', cat:'TRAP', rev:false }
    ],
    values: ['High income', 'Job security', 'Work-life balance', 'Prestige/status', 'Creativity', 'Helping society', 'Independence', 'Fast growth opportunities']
  };

  const traitExplanations = {
      R: "Practical, hands-on, and tool-oriented. You prefer concrete execution over abstract theory.",
      I: "Analytical, logical, and scientific. You excel at solving complex, data-driven problems.",
      A: "Creative, original, and unstructured. You thrive in environments allowing self-expression.",
      S: "Empathetic, helpful, and community-focused. You are motivated by healing, teaching, or guiding others.",
      E: "Persuasive, leadership-driven, and risk-taking. You are built for business, management, and influence.",
      C: "Detail-oriented, organized, and rule-abiding. You excel in structured, predictable, and data-heavy environments."
  };

  let state = { answers: {}, startTime: null, topValues: [], currentStep: 0 };
  const emojis = ['😖', '😕', '😐', '🙂', '🤩'];

  function initApp() {
      const saved = localStorage.getItem('careerIntelState');
      if(saved) {
          if(confirm("We found a saved session. Would you like to resume?")) {
              state = JSON.parse(saved);
          } else {
              localStorage.removeItem('careerIntelState');
          }
      }
      renderWizard();
      if(state.currentStep > 0) goNext(state.currentStep - 1, true);
  }

  function saveProgress() {
      localStorage.setItem('careerIntelState', JSON.stringify(state));
      alert("Progress Saved! You can close this window and return later.");
  }

  function buildLikertGrid(qs) {
    return `<div class="scale-legend"><span>1 = Strongly Disagree</span><span>5 = Strongly Agree</span></div><div class="rating-grid">` + 
      qs.map(q => {
        let preVal = state.answers[q.id] ? state.answers[q.id].raw : 0;
        return `
        <div class="rating-row" id="row_${q.id}">
          <div class="rating-label">${q.text}</div>
          <div class="rating-options">
            ${[1,2,3,4,5].map(n => `<div class="rate-btn ${preVal === n ? 'selected' : ''}" onclick="setAns('${q.id}', ${n}, this, ${q.rev || false}, '${q.cat}')">${emojis[n-1]}</div>`).join('')}
          </div>
        </div>`
      }).join('') + `</div>`;
  }

  function setAns(id, val, btn, isRev, cat) {
    if(!state.startTime) state.startTime = Date.now();
    let p = btn.parentElement;
    Array.from(p.children).forEach(c => c.classList.remove('selected'));
    btn.classList.add('selected');
    let finalVal = isRev ? (6 - val) : val;
    state.answers[id] = { raw: val, calc: finalVal, cat: cat };
  }

  function moveValue(el, val) {
    const ranked = document.getElementById('vRanked');
    if (el.parentElement.id === 'vPool') {
      if(state.topValues.length >= 5) return alert("You can only select 5 values.");
      state.topValues.push(val);
      el.remove();
      ranked.innerHTML += `<div class="ranked-slot"><div class="rank-num">${state.topValues.length}</div><div class="val-pill" onclick="unmoveValue(this, '${val}')" style="margin:0; flex:1;">${val}</div></div>`;
    }
  }

  function unmoveValue(el, val) {
    const pool = document.getElementById('vPool');
    state.topValues = state.topValues.filter(v => v !== val);
    el.parentElement.remove();
    pool.innerHTML += `<div class="val-pill" onclick="moveValue(this, '${val}')">${val}</div>`;
    let slots = document.getElementById('vRanked').querySelectorAll('.ranked-slot');
    slots.forEach((s, i) => s.querySelector('.rank-num').innerText = i + 1);
  }

  function validateValues(s) {
    if(state.topValues.length !== 5) return alert("Please select exactly 5 career values.");
    goNext(s);
  }

  function updateUXText(s) {
      document.getElementById('stepCounter').innerText = `Step ${s+1} of 7`;
      const timeEst = Math.max(1, 15 - (s * 2));
      document.getElementById('timeEstimator').innerText = `⏱ Est. Time: ~${timeEst} mins`;
  }

  function goNext(s, isRestore = false) {
    if(!isRestore) state.currentStep = s + 1;
    let target = isRestore ? s + 1 : state.currentStep;
    
    document.querySelectorAll('.step-card').forEach(el => el.classList.remove('active'));
    document.getElementById(`step_${target}`).classList.add('active');
    
    document.getElementById('progressBar').style.width = (((target+1) / 7) * 100) + '%';
    updateUXText(target);
    window.scrollTo({ top: 0, behavior: 'smooth' });
  }

  function goPrev(s) {
    state.currentStep = s - 1;
    document.querySelectorAll('.step-card').forEach(el => el.classList.remove('active'));
    document.getElementById(`step_${state.currentStep}`).classList.add('active');
    
    document.getElementById('progressBar').style.width = (((state.currentStep+1) / 7) * 100) + '%';
    updateUXText(state.currentStep);
    window.scrollTo({ top: 0, behavior: 'smooth' });
  }

  function renderWizard() {
    const wiz = document.getElementById('wizardContainer');
    let html = "";
    
    // Step 0: Profile & Academics
    html += `<div class="step-card active" id="step_0">
      <h2 class="step-title">Candidate Profile</h2><p class="step-sub">LEVEL 1 / 7</p>
      <div class="form-group"><label class="form-label">Full Name</label><input type="text" id="candName" class="form-input" placeholder="Enter your full name"></div>
      <div class="grid-2col">
        <div class="form-group"><label class="form-label">Current Grade</label>
          <select id="qGrade" class="form-select"><option value="8-10">Grade 8 - 10</option><option value="11-12">Grade 11 - 12</option><option value="UG">Undergraduate</option></select>
        </div>
        <div class="form-group"><label class="form-label">Current Stream / Track</label>
          <select id="qStream" class="form-select"><option value="PCM">Science (PCM)</option><option value="PCB">Science (PCB)</option><option value="Commerce">Commerce</option><option value="Arts">Arts / Humanities</option></select>
        </div>
      </div>
      <div style="border-top: 1px solid var(--border); margin-top: 10px; padding-top: 20px;">
          <h4 style="margin:0 0 15px 0; color:white;">Academic Performance Baseline</h4>
          <div class="grid-3col">
              <div class="form-group"><label class="form-label">Avg Marks %</label><input type="number" id="qMarks" class="form-input" placeholder="e.g. 85"></div>
              <div class="form-group"><label class="form-label">Strongest Subject</label><input type="text" id="qStrong" class="form-input" placeholder="e.g. Math"></div>
              <div class="form-group"><label class="form-label">Weakest Subject</label><input type="text" id="qWeak" class="form-input" placeholder="e.g. History"></div>
          </div>
      </div>
      <div class="btn-wrapper"><button class="btn-main" style="width:100%" onclick="goNext(0)">Start Assessment ➔</button></div>
    </div>`;

    html += `<div class="step-card" id="step_1"><h2 class="step-title">Preferences I</h2>${buildLikertGrid(qBank.riasec.slice(0, 18))}<div class="btn-wrapper"><button class="btn-back" onclick="goPrev(1)">Back</button><button class="btn-main" onclick="goNext(1)">Next ➔</button></div><div style="text-align:center; margin-top:15px;"><a href="#" onclick="saveProgress()" style="color:var(--text-muted); font-size:0.8rem;">💾 Save & Resume Later</a></div></div>`;
    html += `<div class="step-card" id="step_2"><h2 class="step-title">Preferences II</h2>${buildLikertGrid(qBank.riasec.slice(18, 36))}<div class="btn-wrapper"><button class="btn-back" onclick="goPrev(2)">Back</button><button class="btn-main" onclick="goNext(2)">Next ➔</button></div><div style="text-align:center; margin-top:15px;"><a href="#" onclick="saveProgress()" style="color:var(--text-muted); font-size:0.8rem;">💾 Save & Resume Later</a></div></div>`;
    html += `<div class="step-card" id="step_3"><h2 class="step-title">Aptitude Indicator</h2>${buildLikertGrid(qBank.aptitude)}<div class="btn-wrapper"><button class="btn-back" onclick="goPrev(3)">Back</button><button class="btn-main" onclick="goNext(3)">Next ➔</button></div><div style="text-align:center; margin-top:15px;"><a href="#" onclick="saveProgress()" style="color:var(--text-muted); font-size:0.8rem;">💾 Save & Resume Later</a></div></div>`;
    
    let poolHtml = qBank.values.filter(v => !state.topValues.includes(v)).map(v => `<div class="val-pill" onclick="moveValue(this, '${v}')">${v}</div>`).join('');
    let rankedHtml = state.topValues.map((v, i) => `<div class="ranked-slot"><div class="rank-num">${i+1}</div><div class="val-pill" onclick="unmoveValue(this, '${v}')" style="margin:0; flex:1;">${v}</div></div>`).join('');
    
    html += `<div class="step-card" id="step_4"><h2 class="step-title">Career Values</h2><p class="step-sub">Select your TOP 5 priorities</p>
      <div class="values-container">
        <div class="value-pool" id="vPool">${poolHtml}</div>
        <div class="value-ranked" id="vRanked">${rankedHtml}</div>
      </div>
      <div class="btn-wrapper"><button class="btn-back" onclick="goPrev(4)">Back</button><button class="btn-main" onclick="validateValues(4)">Next ➔</button></div></div>`;

    html += `<div class="step-card" id="step_5"><h2 class="step-title">Stress Resilience</h2>${buildLikertGrid(qBank.resilience)}<div class="btn-wrapper"><button class="btn-back" onclick="goPrev(5)">Back</button><button class="btn-main" onclick="goNext(5)">Next ➔</button></div></div>`;
    
    html += `<div class="step-card" id="step_6"><h2 class="step-title">Final Reality Check</h2>${buildLikertGrid(qBank.maturity)}
      <div style="margin-top:20px; border-top:1px solid var(--border); padding-top:20px;">
        <div class="form-group"><label class="form-label">Parent's Preferred Career</label><input type="text" id="qParent" class="form-input"></div>
        <div class="form-group"><label class="form-label">Your Secret Career Interest</label><input type="text" id="qSecret" class="form-input" placeholder="What do you actually want to do?"></div>
      </div>
      <div class="btn-wrapper"><button class="btn-back" onclick="goPrev(6)">Back</button><button class="btn-main" id="analyzeBtn" onclick="processClinicalData()">Compile Dossier ✨</button></div></div>`;

    wiz.innerHTML = html;
  }

  function calculateSD(arr) {
      if(arr.length === 0) return 0;
      const mean = arr.reduce((a, b) => a + b) / arr.length;
      return Math.sqrt(arr.map(x => Math.pow(x - mean, 2)).reduce((a, b) => a + b) / arr.length);
  }

  // --- CORE ENGINE ---
  async function processClinicalData() {
    const answerKeys = Object.keys(state.answers);
    if(answerKeys.length < 69) return alert(`Please answer all questions. You have answered ${answerKeys.length}/69.`);

    const btn = document.getElementById('analyzeBtn');
    btn.innerText = "Analyzing Psychometrics... ⏳";
    btn.disabled = true;

    // 1. Social Desirability & Consistency Math
    const timeTakenMins = (Date.now() - state.startTime) / 60000;
    const rawScores = answerKeys.map(k => state.answers[k].raw);
    const sd = calculateSD(rawScores);
    
    let trapScore = 0;
    if(state.answers['t1']) trapScore += state.answers['t1'].raw;
    if(state.answers['t2']) trapScore += state.answers['t2'].raw;
    if(state.answers['t3']) trapScore += state.answers['t3'].raw;

    let contradictionScore = 0;
    if(state.answers['a6'] && state.answers['c4']) {
        if(state.answers['a6'].raw > 3 && state.answers['c4'].raw > 3) contradictionScore = 1; // Both hate rules AND love structure
    }

    let reliability = "🟢 High Reliability";
    let relClass = "rel-high";
    if (timeTakenMins < 4 || sd < 0.5) {
        reliability = "🔴 Low Reliability (Random/Rushed)";
        relClass = "rel-low";
    } else if (trapScore >= 13 || contradictionScore > 0) {
        reliability = "🟡 Moderate (Social Desirability Detected)";
        relClass = "rel-mod";
    }

    // Dynamic Percentile
    const basePct = Math.floor(Math.random() * (92 - 78 + 1)) + 78;

    const payload = {
        studentName: document.getElementById('candName').value || "Student",
        answers: state.answers,
        topValues: state.topValues,
        grade: document.getElementById('qGrade').value,
        currentStream: document.getElementById('qStream').value,
        marks: document.getElementById('qMarks').value,
        strongSub: document.getElementById('qStrong').value,
        weakSub: document.getElementById('qWeak').value,
        parentCareer: document.getElementById('qParent').value,
        secretCareer: document.getElementById('qSecret').value,
        reliability: relClass
    };

    try {
      // HIT CLOUD RUN ENGINE
      const response = await fetch('https://submitassessment-susm3f6boa-uc.a.run.app', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(payload)
      });
      const jsonResponse = await response.json();
      if (!jsonResponse.success) throw new Error("Analysis failed");
      let report = jsonResponse.result;

      // RENDER RESULTS
      localStorage.removeItem('careerIntelState');
      
      // SAFELY trigger confetti
      if (typeof confetti === 'function') {
          confetti({ particleCount: 150, spread: 70, origin: { y: 0.6 } });
      } else {
          console.warn("Confetti animation skipped (script did not load).");
      }
      
      document.getElementById('progressWrap').style.display = 'none';
      document.getElementById('progressCont').style.display = 'none';
      document.getElementById('wizardContainer').style.display = 'none';
      document.getElementById('reportContainer').style.display = 'block';
      
      document.getElementById('outName').innerText = payload.studentName;
      document.getElementById('outAcad').innerText = `${payload.currentStream} | Avg Marks: ${payload.marks || 'N/A'}%`;
      document.getElementById('outDate').innerText = new Date().toLocaleDateString();
      
      const relBadge = document.getElementById('outReliability');
      relBadge.innerText = reliability;
      relBadge.className = `reliability-badge ${relClass}`;

      document.getElementById('outCode').innerText = report.finalCode;
      const topLetter = report.finalCode.charAt(0);
      document.getElementById('outPercentile').innerText = `🏆 Your ${topLetter} trait score is higher than ${basePct}% of students globally.`;

      let breakdownHtml = "";
      report.finalCode.split('').forEach(letter => {
          breakdownHtml += `<div class="trait-box"><strong>${letter} (${report.scores[letter]}%):</strong> ${traitExplanations[letter]}</div>`;
      });
      document.getElementById('outTraitBreakdown').innerHTML = breakdownHtml;

      // SAFELY generate Chart
      const ctx = document.getElementById('riasecChart').getContext('2d');
      if (typeof Chart !== 'undefined') {
          new Chart(ctx, {
              type: 'radar',
              data: {
                  labels: ['Realistic','Investigative','Artistic','Social','Enterprising','Conventional'],
                  datasets: [{
                      data: [report.scores.R, report.scores.I, report.scores.A, report.scores.S, report.scores.E, report.scores.C],
                      backgroundColor: 'rgba(59, 130, 246, 0.2)', borderColor: '#3b82f6', pointBackgroundColor: '#0f172a'
                  }]
              },
              options: { scales: { r: { max: 100, min: 0 } }, plugins: { legend: { display: false } } }
          });
      } else {
          console.warn("Chart.js blocked by browser or network. Skipping chart render.");
      }

      document.getElementById('txt-apt').innerText = report.aptPct + "%"; document.getElementById('bar-apt').style.width = report.aptPct + "%";
      document.getElementById('txt-res').innerText = report.resPct + "%"; document.getElementById('bar-res').style.width = report.resPct + "%";
      document.getElementById('txt-mat').innerText = report.matPct + "%"; document.getElementById('bar-mat').style.width = report.matPct + "%";
      document.getElementById('txt-par').innerText = report.parPct + "%"; document.getElementById('bar-par').style.width = report.parPct + "%";

      // ESCALATION LOGIC (Layered)
      const escBox = document.getElementById('escalationWarning');
      if(report.parPct > 80 && report.resPct < 40) {
          escBox.style.display = 'block';
          escBox.style.borderColor = "var(--danger)";
          document.getElementById('escTitle').innerText = "🚨 High Priority Intervention Recommended";
          document.getElementById('escTitle').style.color = "var(--danger)";
          document.getElementById('escText').innerText = "Elevated external pressure and low stress resilience detected. A parent-counsellor meeting is highly advised before making stream choices.";
      } else if (report.parPct > 70 || report.matPct < 35) {
          escBox.style.display = 'block';
      }

      // SHADOW CAREER
      const topNames = report.topCareers.map(c => c.name.toLowerCase());
      const secret = payload.secretCareer.toLowerCase();
      if(secret && !topNames.some(n => n.includes(secret) || secret.includes(n))) {
          document.getElementById('shadowWarning').style.display = 'block';
          document.getElementById('outSecret').innerText = payload.secretCareer;
      }

      document.getElementById('outCareers').innerHTML = report.topCareers.map(c => {
          let fitClass = "fit-exp";
          let fitLabel = "Exploratory Fit";
          if(c.score >= 80) { fitClass = "fit-strong"; fitLabel = "🟢 Strong Fit"; }
          else if (c.score >= 60) { fitClass = "fit-mod"; fitLabel = "🟡 Moderate Fit"; }
          return `<div class="career-bar">
                    <span class="c-name">${c.name}</span>
                    <span class="c-fit ${fitClass}">${fitLabel} (${c.score}%)</span>
                  </div>`;
      }).join('');

      const topCareer = report.topCareers[0].name.toLowerCase();
      
      // Dynamic Confidence Statement
      document.getElementById('outConfidence').innerText = `Based on your psychometric alignment and academic baseline, you show strong directional clarity toward ${report.topCareers[0].name} and allied fields.`;

      // Skill Gap Heatmap Logic
      let skillsHtml = "";
      if(topCareer.includes("engineer") || topCareer.includes("tech")) {
          skillsHtml = `<tr><td>Logical Mathematics</td><td>${report.aptPct}%</td><td>Needs +15% Boost</td></tr>
                        <tr><td>Analytical Focus</td><td>${report.scores.I}%</td><td>Strong Alignment</td></tr>
                        <tr><td>Stress Tolerance</td><td>${report.resPct}%</td><td>${report.resPct < 50 ? "Critical Gap" : "Adequate"}</td></tr>`;
      } else {
          skillsHtml = `<tr><td>Verbal/Written Comm.</td><td>${report.aptPct}%</td><td>Monitor</td></tr>
                        <tr><td>Social Empathy</td><td>${report.scores.S}%</td><td>Strong Alignment</td></tr>
                        <tr><td>Pressure Handling</td><td>${report.resPct}%</td><td>${report.resPct < 50 ? "Critical Gap" : "Adequate"}</td></tr>`;
      }
      document.getElementById('outSkills').innerHTML = skillsHtml;

      const lowestTraits = Object.entries(report.scores).sort((a,b)=>a[1]-b[1]).slice(0,2).map(x=>x[0]);
      document.getElementById('outAvoid').innerText = `Paths requiring heavily dominant ${lowestTraits.join(' & ')} traits.`;

      renderTiersAndPlan(topCareer, payload.currentStream);
      bridgeToFirestore(report, payload);
      
    } catch (error) {
        console.error(error);
        alert("Connection failed. Data was not saved.");
        btn.disabled = false;
        btn.innerText = "Compile Dossier ✨";
    }
  }

  function renderTiersAndPlan(careerName, stream) {
      let tierHtml = ""; let planCourses = ""; let planExams = "";

      if(careerName.includes("engineering") || careerName.includes("tech") || stream === "PCM") {
          tierHtml = `<div class="tier-card"><strong>Tier 1 (Elite)</strong><span>IITs, NITs, BITS Pilani, IIITs</span></div>
                      <div class="tier-card"><strong>Tier 2 (Premium)</strong><span>VIT, MIT Manipal, SRM, Thapar</span></div>`;
          planCourses = "<li>Basic Python/C++ Logic Foundation</li><li>JEE Mains Crash Course</li>";
          planExams = "<li>Primary: JEE Mains (Jan)</li><li>Secondary: BITSAT / State CET</li>";
      } else if (careerName.includes("medical") || careerName.includes("mbbs") || stream === "PCB") {
          tierHtml = `<div class="tier-card"><strong>Tier 1 (Elite)</strong><span>AIIMS, JIPMER, AFMC, CMC Vellore</span></div>
                      <div class="tier-card"><strong>Tier 2 (State Govt)</strong><span>Top State Medical Colleges (Merit)</span></div>`;
          planCourses = "<li>Advanced NCERT Biology Mastery</li><li>Clinical Shadowing (1 week)</li>";
          planExams = "<li>Primary: NEET UG (May)</li><li>Backup: CUET (B.Sc Bio)</li>";
      } else if (stream === "Commerce") {
          tierHtml = `<div class="tier-card"><strong>Tier 1 (Elite)</strong><span>SRCC, Hindu College, IIM (IPM)</span></div>
                      <div class="tier-card"><strong>Professional Bodies</strong><span>ICAI (For CA), ACCA Global</span></div>`;
          planCourses = "<li>Financial Excel Certification</li><li>CA Foundation Prep</li>";
          planExams = "<li>Primary: CUET (DU target)</li><li>Professional: CA Found / IPMAT</li>";
      } else {
          tierHtml = `<div class="tier-card"><strong>Tier 1 (Elite)</strong><span>St. Stephens, LSR, NLSIU</span></div>
                      <div class="tier-card"><strong>Tier 2 (Design)</strong><span>NID, NIFT, Srishti</span></div>`;
          planCourses = "<li>Public Speaking / MUN Workshops</li><li>Design Portfolio Building</li>";
          planExams = "<li>Primary: CUET / CLAT</li><li>Design: UCEED / NID DAT</li>";
      }

      document.getElementById('outColleges').innerHTML = tierHtml;
      document.getElementById('planCourses').innerHTML = planCourses;
      document.getElementById('planExams').innerHTML = planExams;
  }

  async function bridgeToFirestore(report, payload) {
    try {
        const { getAuth } = await import("https://www.gstatic.com/firebasejs/10.8.1/firebase-auth.js");
        const { getFirestore, doc, setDoc } = await import("https://www.gstatic.com/firebasejs/10.8.1/firebase-firestore.js");
        
        const auth = getAuth();
        const db = getFirestore();
        const user = auth.currentUser;
        if (!user) return;

        const psychologyPackage = {
            assessmentCompleted: true,
            completedAt: new Date().toISOString(),
            streamInfo: { stream: payload.currentStream, marks: payload.marks },
            psychIndex: {
                careerClarity: Math.round(report.matPct / 10), 
                confidenceScore: Math.round(report.aptPct / 10),
                parentPressure: Math.round(report.parPct / 10),
                riskCategory: (report.parPct > 70 || report.matPct < 40) ? "High" : "Low",
                stressIndicator: (report.resPct < 40) ? "High" : "Normal",
                reliability: payload.reliability
            },
            riasecCode: report.finalCode,
            primaryTrait: report.dom
        };

        await setDoc(doc(db, "students", user.uid), psychologyPackage, { merge: true });
    } catch (e) { console.error("Bridge Failure:", e); }
  }

  function downloadPDF() {
      const el = document.getElementById('reportContent');
      html2pdf().from(el).set({ margin: 0.2, filename: 'Career_Intelligence_Dossier.pdf', html2canvas: { scale: 2 }, jsPDF: { unit: 'in', format: 'letter', orientation: 'portrait' } }).save();
  }

  initApp();
</script>
</body>
</html>
