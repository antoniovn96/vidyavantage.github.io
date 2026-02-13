---
layout: default
title: Global College Directory
---

# Verified College Database

Here is our list of verified institutions:

<ul>
  {% for college in site.data.colleges %}
    <li>
      <h3>{{ college.name }}</h3>
      <p>📍 {{ college.location }} | 💰 {{ college.fees }}</p>
      <p>Courses: {{ college.courses | join: ", " }}</p>
      <a href="{{ college.website }}">Visit Website</a>
    </li>
  {% endfor %}
</ul>
