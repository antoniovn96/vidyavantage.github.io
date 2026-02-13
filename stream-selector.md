---
layout: default
title: Stream Selector
permalink: /stream-selector/
---

<style>
  .quiz-container { background: #f4f6f8; padding: 2rem; border-radius: 8px; border-left: 5px solid #D4AF37; }
  .question { display: none; }
  .question.active { display: block; }
  .btn { background: #0A2342; color: white; padding: 10px 20px; border: none; cursor: pointer; margin: 5px; }
  .btn:hover { background: #D4AF37; color: black; }
  .result-box { display: none; background: #e3f2fd; padding: 20px; border: 1px solid #2196F3; }
</style>

<div class="quiz-container">
  <h1>The Reality Check: Grade 10 Stream Selector</h1>
  
  <div id="q1" class="question active">
    <h3>1. How do you feel about Mathematics?</h3>
    <button class="btn" onclick="nextQ('q2a')">I love it / I am good at it</button>
    <button class="btn" onclick="nextQ('q2b')">I struggle with it / I hate it</button>
  </div>

  <div id="q2a" class="question">
    <h3>2. Do you prefer building things (Machines/Code) or understanding nature (Biology/Plants)?</h3>
    <button class="btn" onclick="showResult('Engineering / PCM')">Building Things (Engineering)</button>
    <button class="btn" onclick="showResult('Medical / PCMB')">Nature (Medicine/Research)</button>
  </div>

  <div id="q2b" class="question">
    <h3>2. Are you more interested in Money/Business or Creativity/People?</h3>
    <button class="btn" onclick="showResult('Commerce with Math/IP')">Money & Business</button>
    <button class="btn" onclick="showResult('Humanities / Arts')">Creativity & People</button>
  </div>

  <div id="result" class="result-box">
    <h2 id="result-title"></h2>
    <p>Based on verified data, this stream fits your current profile.</p>
    <a href="/" class="btn">Start Over</a>
  </div>
</div>

<script>
  function nextQ(nextId) {
    // Hide all active questions
    document.querySelectorAll('.question').forEach(el => el.classList.remove('active'));
    // Show the next question
    document.getElementById(nextId).classList.add('active');
  }

  function showResult(stream) {
    document.querySelectorAll('.question').forEach(el => el.classList.remove('active'));
    const resultBox = document.getElementById('result');
    resultBox.style.display = 'block';
    document.getElementById('result-title').innerText = "Recommended Stream: " + stream;
  }
</script>
