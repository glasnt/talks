---
layout: writeup
title: "Expressive Security: Vulnerabilities with Emoji"
slides: expressivesecurity
notes: | 
  The slides below are from the SeaGL 2021 iteration.
---

<p>
Other Emoji Security Talks:

{% for conf in site.data.talks %}
{% for talk in conf.conference.talks %}
{% if talk.name == "Protect yourself against the bees 🐝" %}<li><a href="{{talk.link}}">{{talk.name}}, {{conf.conference.name}}</a></li>{% endif %}
{% if talk.name == "🔐 + 😈 => 💥" %}<li><a href="{{talk.link}}">{{talk.name}}, {{conf.conference.name}}</a></li>{% endif %}
{% endfor %}
{% endfor %}
</p><p>
See also "The Power ⚡️ and Responsibility 😓 of Unicode Adoption ✨", previously presented at:
{% for conf in site.data.talks %}
{% for talk in conf.conference.talks %}
{% if talk.name == "The Power and Responsibility of Unicode Adoption" %}<a href="{{talk.link}}">{{conf.conference.name}}, </a>{% endif %}
{% if talk.name == "The Power ⚡️ and Responsibility 😓 of Unicode Adoption ✨" %}<a href="{{talk.link}}">{{conf.conference.name}}, </a>{% endif %}
{% endfor %}
{% endfor %}
just to name a few.
</p>