---
layout: writeup
title: "Present like a pro"

slides: present-like-a-pro
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
</p>

## Resources


* Lara Hogan [Demystifying public speaking](https://larahogan.me/speaking/)
* Damien Conway [Instantly Better Presentations](https://www.youtube.com/watch?v=W_i_DrWic88) 
* VM Brasseur [Public Speaking Resources](https://github.com/vmbrasseur/Public_Speaking#writing-presentations)
* William Brown [The History of - History and Politics - William Brown](https://www.youtube.com/watch?v=q2VmIUaOS9o&t=3623s) ([context](https://www.youtube.com/watch?v=AJqcxEzRdSY&t=1119s))
* Zach Holman [speaking.io](https://speaking.io) 
* PyCon AU 2021 [Speaking Guide](https://2021.pycon.org.au/speak/)


PyCon AU specific: [Guide to PyCon AU 2023 CFP from DjangoCon AU CFP Workshop](../2023-05-djangoconau-cfp-workshop/)
