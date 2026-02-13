---
layout: default
title: Stream Selector
permalink: /stream-selector/
---

<div id="quiz-app" style="max-width: 600px; margin: 0 auto; background: white; padding: 40px; border-radius: 10px; box-shadow: 0 10px 25px rgba(0,0,0,0.1);">
    <h2 id="question-text" style="color: #0A2342;">Loading...</h2>
    <div id="options-container" style="display: flex; flex-direction: column; gap: 10px; margin-top: 20px;"></div>
    <div id="result-container" style="display: none; text-align: center;">
        <h2 style="color: #D4AF37;">Recommended Path:</h2>
        <h1 id="final-result" style="color: #0A2342; font-size: 2.5em;"></h1>
        <p id="final-desc"></p>
        <button onclick="location.reload()" class="btn" style="margin-top: 20px;">Start Over</button>
    </div>
</div>

<script>
    // THE BRAIN: Add as many questions here as you want!
    const questions = {
        "start": {
            text: "Which subject do you enjoy studying the most?",
            options: [
                { text: "Mathematics & Logic", next: "math_path" },
                { text: "Science (Biology/Nature)", next: "bio_path" },
                { text: "History / Social Studies", next: "arts_path" },
                { text: "Money / Business", next: "comm_path" }
            ]
        },
        "math_path": {
            text: "Do you prefer working with computers or physical machines?",
            options: [
                { text: "Computers / Coding", result: "Computer Science (PCM)", desc: "Ideal for Software Engineering, AI, and Data Science." },
                { text: "Physical Machines / Cars", result: "Mechanical Engineering", desc: "Ideal for Robotics, Auto, and Aero industries." }
            ]
        },
        "bio_path": {
            text: "Can you handle blood and hospitals?",
            options: [
                { text: "Yes, I want to save lives", result: "Medicine (MBBS)", desc: "Prepare for NEET. High dedication required." },
                { text: "No, I prefer research/lab work", result: "Biotechnology / Genetics", desc: "Focus on research, pharma, and lab sciences." }
            ]
        },
        "arts_path": {
            text: "Do you like public speaking and debating?",
            options: [
                { text: "Yes, I love arguing points", result: "Law / Humanities", desc: "Great for CLAT, Law School, and Journalism." },
                { text: "No, I prefer writing/designing", result: "Design / Literature", desc: "Look into NIFT, UID, or Mass Comm." }
            ]
        },
        "comm_path": {
            text: "Are you good with numbers and calculations?",
            options: [
                { text: "Yes, I love numbers", result: "Commerce with Math", desc: "Perfect for CA, Investment Banking, and Finance." },
                { text: "No, I prefer management/theory", result: "Commerce without Math", desc: "Good for BBA, Marketing, and HR." }
            ]
        }
    };

    // The Engine (Don't touch this part)
    function loadQuestion(id) {
        const q = questions[id];
        document.getElementById("question-text").innerText = q.text;
        const container = document.getElementById("options-container");
        container.innerHTML = "";

        q.options.forEach(opt => {
            const btn = document.createElement("button");
            btn.className = "btn";
            btn.style.width = "100%";
            btn.innerText = opt.text;
            btn.onclick = () => {
                if (opt.result) showResult(opt.result, opt.desc);
                else loadQuestion(opt.next);
            };
            container.appendChild(btn);
        });
    }

    function showResult(result, desc) {
        document.getElementById("question-text").style.display = "none";
        document.getElementById("options-container").style.display = "none";
        document.getElementById("result-container").style.display = "block";
        document.getElementById("final-result").innerText = result;
        document.getElementById("final-desc").innerText = desc;
    }

    // Start the quiz
    loadQuestion("start");
</script>
