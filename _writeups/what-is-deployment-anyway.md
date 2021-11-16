---
layout: writeup
title: "What is deployment, anyway?"
slides: deployment

notes: | 
  The slides below are from the DjangoCon 2021 iteration.

---

<p>
  This talk has been previously presented at:
  
  {% for conf in site.data.talks %}
  {% for talk in conf.conference.talks %}
  {% if talk.name == page.title %}
  <li><a href="{{talk.link}}">{{conf.conference.name}}</a></li>
  {% endif %}
  {% endfor %}
  {% endfor %}