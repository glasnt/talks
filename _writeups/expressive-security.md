---
layout: writeup
title: "Expressive Security: Vulnerabilities with Emoji"
slides: expressivesecurity
notes: | 
  The slides below are from the SeaGL 2021 iteration. 
  <br><br>
  <b>Note</! I had already recorded my SeaGL talk when <a href="https://nvd.nist.gov/vuln/detail/CVE-2021-42574">CVE-2021-42574</a>/<a href="https://trojansource.codes/">Trojan Source</a> was released, but this latest development just re-emphasises that yes, Unicode issues will continue. Read more: <a href="https://confluence.atlassian.com/security/multiple-products-security-advisory-unrendered-unicode-bidirectional-override-characters-cve-2021-42574-1086419475.html">Atlassian Advisory</a>, <a href="https://blog.rust-lang.org/2021/11/01/cve-2021-42574.html">rustc Advisory</a>.

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
</p><p>
Other Emoji Security Talks:
<ul>
{% for conf in site.data.talks %}
{% for talk in conf.conference.talks %}
{% if talk.name == "Protect yourself against the bees 🐝" %}<li><a href="{{talk.link}}">{{talk.name}}, {{conf.conference.name}}</a></li>{% endif %}
{% if talk.name == "🔐 + 😈 => 💥" %}<li><a href="{{talk.link}}">{{talk.name}}, {{conf.conference.name}}</a></li>{% endif %}
{% endfor %}
{% endfor %}
</ul></p><p>
See also "The Power ⚡️ and Responsibility 😓 of Unicode Adoption ✨", previously presented at:
{% for conf in site.data.talks %}
{% for talk in conf.conference.talks %}
{% if talk.name == "The Power and Responsibility of Unicode Adoption" %}<a href="{{talk.link}}">{{conf.conference.name}}, </a>{% endif %}
{% if talk.name == "The Power ⚡️ and Responsibility 😓 of Unicode Adoption ✨" %}<a href="{{talk.link}}">{{conf.conference.name}}, </a>{% endif %}
{% endfor %}
{% endfor %}
just to name a few.
</p>
