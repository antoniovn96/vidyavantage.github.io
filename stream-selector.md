---
layout: default
title: Advanced Stream Selector
permalink: /stream-selector/
---

<style>
  /* Quiz Container Styling */
  .quiz-container {
    max-width: 700px;
    margin: 40px auto;
    background: white;
    padding: 40px;
    border-radius: 15px;
    box-shadow: 0 10px 30px rgba(0,0,0,0.1);
    border-top: 5px solid #D4AF37;
    text-align: center;
  }

  .question-text {
    color: #0A2342;
    font-size: 1.5rem;
    font-weight: bold;
    margin-bottom: 30px;
  }

  .options-grid {
    display: flex;
    flex-direction: column;
    gap: 15px;
  }

  .quiz-btn {
    background: #f4f6f8;
    color: #0A2342;
    border: 1px solid #ddd;
    padding: 15px 20px;
    font-size: 1.1rem;
    cursor: pointer;
    border-radius: 8px;
    transition: all 0.2s;
    text-align: left;
  }

  .quiz-btn:hover {
    background: #0A2342;
    color: #D4AF37;
    transform: translateX(5px);
  }

  /* Result Styling */
  .result-box {
    display: none;
    animation: fadeIn 0.5s;
  }
  
  .result-title {
    color: #D4AF37;
    font-size: 2rem;
    margin-bottom: 10px;
  }
  
  .result-desc {
    font-size: 1.1rem;
    color: #555;
    line-height: 1.6;
    margin-bottom: 30px;
  }

  @keyframes fadeIn {
    from { opacity: 0; transform: translateY(10px); }
    to { opacity: 1; transform: translateY(0); }
  }
</style>

<div class="quiz-container">
  <p id="progress-text" style="color: #888; font-size: 0.9rem; margin-bottom: 20px;">Question 1 of 3</p>

  <div id="quiz-view">
    <h2 id="q-text" class="question-text">Loading...</h2>
    <div id="options-area" class="options-grid"></div>
  </div>

  <div id="result-view" class="result-box">
    <h1 id="r-title" class="result-title"></h1>
    <p id="r-desc" class="result-desc"></p>
    
    <div style="display: flex; justify-content: center; gap: 10px;">
      <button onclick="location.reload()" class="btn" style="background: #eee; color: #333;">Start Over</button>
      <a href="{{ '/book-expert/' | relative_url }}" class="btn" style="background: #0A2342; color: #fff;">Talk to a Counsellor</a>
    </div>
  </div>
</div>

<script>
  // THE COMPLEX BRAIN v2.0
  const questions = {
    "start": {
      text: "What fascinates you the most in the world?",
      step: 1,
      options: [
        { text: "Living things (Humans, Plants, Animals)", next: "bio_branch" },
        { text: "How the Human Mind & Society works", next: "humanities_branch" },
        { text: "Numbers, Logic, and Technology", next: "math_branch" },
        { text: "Business, Money, and Markets", next: "commerce_branch" },
        { text: "Daily Life Science (Food, Textiles, Family)", next: "home_sci_branch" }
      ]
    },

    // --- BIOLOGY BRANCH ---
    "bio_branch": {
      text: "Do you prefer dealing with Humans or Nature?",
      step: 2,
      options: [
        { text: "Humans (Medicine, Disease, Anatomy)", next: "medicine_path" },
        { text: "Nature (Plants, Agriculture, Forests)", next: "botany_path" },
        { text: "Animals & Wildlife", result: "Veterinary Science / Zoology", desc: "You care for animals. Consider B.V.Sc (Vet) or B.Sc Zoology." }
      ]
    },
    "medicine_path": {
      text: "Can you handle blood and high-pressure emergencies?",
      step: 3,
      options: [
        { text: "Yes, I want to be a Doctor", result: "MBBS (Medicine)", desc: "The classic path. Prepare for NEET. High dedication required." },
        { text: "No, I prefer Lab work / Research", result: "Microbiology / Biotechnology", desc: "Focus on research, genetics, and lab sciences without the hospital trauma." }
      ]
    },
    "botany_path": {
      text: "What interests you about plants?",
      step: 3,
      options: [
        { text: "The science of how they grow", result: "B.Sc Botany", desc: "Pure science. You study plant physiology, genetics, and ecology." },
        { text: "Farming and Food Production", result: "B.Sc Agriculture", desc: "A very high-demand field. Focuses on crop science, soil, and modern farming tech." }
      ]
    },

    // --- HUMANITIES / PSYCHOLOGY BRANCH ---
    "humanities_branch": {
      text: "What do you like analyzing the most?",
      step: 2,
      options: [
        { text: "Why people think and behave the way they do", next: "psych_path" },
        { text: "History, Culture, and Past Civilizations", result: "History / Archaeology", desc: "For those who love digging into the past and understanding civilizations." },
        { text: "Laws, Rights, and Arguments", result: "Law (BA LLB)", desc: "Perfect for logical thinkers who want to fight for justice." }
      ]
    },
    "psych_path": {
      text: "How do you want to help people?",
      step: 3,
      options: [
        { text: "Therapy & Mental Health (Clinical)", result: "Clinical Psychology", desc: "You will diagnose and treat mental health issues. Requires MA/M.Phil." },
        { text: "Workplace Behavior & HR", result: "Industrial Psychology / HR", desc: "Apply psychology to companies. Help hire people and improve office culture." }
      ]
    },

    // --- HOME SCIENCE BRANCH ---
    "home_sci_branch": {
      text: "Which aspect of 'Daily Life' interests you?",
      step: 2,
      options: [
        { text: "Food, Diet, and Nutrition", result: "Clinical Nutrition & Dietetics", desc: "Become a Dietician or Nutritionist. Science meets health." },
        { text: "Fashion, Textiles, and Design", result: "Fashion Design / Textile Science", desc: "The science of fabrics and the art of design." },
        { text: "Child Development & Family", result: "B.Sc Home Science", desc: "A holistic degree covering psychology, nutrition, and resource management." }
      ]
    },

    // --- MATH BRANCH ---
    "math_branch": {
      text: "Virtual world or Physical world?",
      step: 2,
      options: [
        { text: "Virtual (Coding, AI, Software)", result: "Computer Science Engineering", desc: "The tech path. Coding, App Dev, and AI." },
        { text: "Physical (Buildings, Machines, Motors)", result: "Mechanical / Civil Engineering", desc: "Build real things. Cars, Bridges, and Robots." },
        { text: "Pure Numbers & Data", result: "Data Science / Statistics", desc: "Analyze data to predict the future. Highly paid." }
      ]
    },

    // --- COMMERCE BRANCH ---
    "commerce_branch": {
      text: "Are you good with Mathematics?",
      step: 2,
      options: [
        { text: "Yes, I love calculations", result: "Chartered Accountancy (CA) / Finance", desc: "The expert path. Auditing, Taxation, and Investment Banking." },
        { text: "No, I prefer Management & Marketing", result: "BBA / Marketing", desc: "Focus on business strategy, sales, and leadership." }
      ]
    }
  };

  // Logic to Render
  function loadQuestion(id) {
    const q = questions[id];
    
    // Update Progress
    if(q.step) document.getElementById("progress-text").innerText = `Question ${q.step} of 3`;

    // Update Text
    document.getElementById("q-text").innerText = q.text;
    const container = document.getElementById("options-area");
    container.innerHTML = "";

    // Create Buttons
    q.options.forEach(opt => {
      const btn = document.createElement("button");
      btn.className = "quiz-btn";
      btn.innerText = opt.text;
      btn.onclick = () => {
        if (opt.result) showResult(opt.result, opt.desc);
        else loadQuestion(opt.next);
      };
      container.appendChild(btn);
    });
  }

  function showResult(title, desc) {
    document.getElementById("quiz-view").style.display = "none";
    document.getElementById("progress-text").style.display = "none";
    document.getElementById("result-view").style.display = "block";
    document.getElementById("r-title").innerText = title;
    document.getElementById("r-desc").innerText = desc;
  }

  // Start
  loadQuestion("start");
</script>
