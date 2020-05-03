---
title: talks
description: in which glasnt says words
layout: page 
header-img: "../img/talking_header.jpg"
---
{% assign talk_total = 0 %}
{% for c in site.data.talks %}
  {% for t in c.conference.talks %}
    {% if t.type != "Podcast" %}
      {% assign talk_total = talk_total | plus: 1 %}
    {% endif %}
  {% endfor %}
{% endfor %}

{% assign talk_num = talk_total %}

{% for c in site.data.talks %} 
<div class="row">&nbsp;</div>
<div class="row">
      {% if c.conference.link %}
      <a href="{{c.conference.link}}">{{c.conference.name}}</a>,
      {% else %}
          {{c.conference.name}}
      {% endif %}

      {% if c.conference.location %}{{c.conference.location}}, {%endif%}
      {{c.conference.date | date: "%b %Y"}}
</div>
  {% for talk in c.conference.talks %} 
  <div class="row">
      {% if talk.type != "Podcast" %}#{{ talk_num }}{%else%}&nbsp;<i class="far fa-podcast">&nbsp;</i>{% endif %}
      {{talk.type | default: "Talk"}}  
      {% if talk.link%}<a href="{{talk.link}}">{{talk.name}}</a>{%else%}"{{talk.name}}"{%endif%}
      &nbsp;
      {% if talk.slides %} <a href="{{talk.slides}}"><i class="far fa-presentation"></i></a>{% endif %}
      {% if talk.video %} <a href="{{talk.video}}"><i class="fab fa-youtube"></i></a>{% endif %}
      {% if talk.twitter %} <a href="{{talk.twitter}}"><i class="fab fa-twitter"></i></a>{% endif %}
      {% if talk.transcript %} <a href="{{talk.transcript}}"><i class="far fa-file-alt"></i></a>{% endif %}
      {% if talk.resources %} <a href="{{talk.resources}}"><i class="far fa-list-alt"></i></a>{% endif %}
      {% if talk.feedback %} <a href="{{talk.feedback}}"><i class="far fa-comments"></i></a>{% endif %}
      {% if talk.article %} <a href="{{talk.article}}"><i class="fas fa-newspaper"></i></a>{% endif %}
      {% if talk.photo %} <a href="{{talk.photo}}"><i class="fas fa-camera"></i></a>{% endif %}

    {% if talk.type != "Podcast" %}
      {% assign talk_num = talk_num | minus: 1 %}
    {% endif %}
  </div>
  {% endfor %}
{% endfor %}
<div class="row">&nbsp;</div>
<div class="row">
<p>Source hosted on <a href="https://github.com/glasnt/talks">GitHub</a>. See also: <a href="http://pyvideo.org/speaker/katie-mclaughlin.html">pyvideo profile</a>, <a href="https://noti.st/glasnt">notist</a>.
</div>
