## &nbsp;
<div style='width: 100%; margin: 0 auto;'><p align='center'><img height='260px' src='pictures/o/bolt.svg'><img height='260px' src='pictures/g/sweat.svg'><img height='260px' src='pictures/t/sparkle.svg'></p></div> <!-- .slide: class="center" -->
 <img src="pictures/footer.svg" />
---
 <div style='width: 100%; margin: 0 auto;'><p align='center'><img height='400px' src='pictures/g/wave.svg'><img height='400px' src='pictures/g/koala.svg'></p></div> <!-- .slide: class="center" -->
Note: I'm from australia
---
 <div style='width: 100%; margin: 0 auto;'><p align='center'><img height='266px' src='pictures/t/guitar.svg'><img height='266px' src='pictures/e/no.svg'><img height='266px' src='pictures/e/sad.svg'></p></div> <!-- .slide: class="center" -->
Note: And i'm not a django dev. I don't use django
---
 <div style='width: 100%; margin: 0 auto;'><p align='center'><img height='266px' src='pictures/g/snake.svg'><img height='266px' src='pictures/t/laptop.svg'><img height='266px' src='pictures/g/thumbsup.svg'></p></div> <!-- .slide: class="center" -->
Note: but I am a python dev
---
 <div style='width: 100%; margin: 0 auto;'><p align='center'><img height='200px' src='pictures/g/red_gem.svg'><img height='200px' src='pictures/g/coffee.svg'><img height='200px' src='pictures/g/elephant.svg'><img height='200px' src='pictures/t/camel1.svg'></p></div> <!-- .slide: class="center" -->
 <div style='width: 100%; margin: 0 auto;'><p align='center'><img height='200px' src='pictures/g/snake.svg'><img height='200px' src='pictures/e/web.svg'><img height='200px' src='pictures/g/shell.svg'><img height='200px' src='pictures/e/burrito.svg'></p></div> <!-- .slide: class="center" -->
Note: I code in a lot of things
---
 <div style='width: 50%; margin: 0 auto;'><p align='center'><img height='400px' src='pictures/t/purple_heart.svg'></p></div> <!-- .slide: class="center" -->
Note: and I love emoji
---
 <div style='width: 50%; margin: 0 auto;'><p align='center'><img height='400px' src='pictures/o/broken.svg'></p></div> <!-- .slide: class="center" -->
Note: and I love how broken emoji is

Now let me explain. I'm a polyglot programmer.

windows apple linux
many languea
---
 <div style='width: 100%; margin: 0 auto;'><p align='center'><img height='266px' src='pictures/g/bug.svg'><img height='266px' src='pictures/g/bug.svg'><img height='266px' src='pictures/g/bug.svg'></p></div> <!-- .slide: class="center" -->
Note: And given that, I notice a lot of bugs and other inconscitancies
---
 <div style='width: 100%; margin: 0 auto;'><p align='center'><img height='266px' src='pictures/o/bolt.svg'><img height='266px' src='pictures/g/sweat.svg'><img height='266px' src='pictures/t/sparkle.svg'></p></div> <!-- .slide: class="center" -->
Note: now, this talk is called Power Responsibily of Unicode Adoption
---
 <div style='width: 50%; margin: 0 auto;'><p align='center'><img height='400px' src='pictures/t/no.svg'></p></div> <!-- .slide: class="center" -->

Note: But it contains absolutely no emoji.

I'm running Ubuntu, and nothing would work if I did that
---

 <div style='width: 100%; margin: 0 auto;'><p align='center'><img height='266px' src='pictures/t/blue_bird.svg'><img height='266px' src='pictures/t/bee.svg'><img height='266px' src='pictures/t/shiny.svg'></p></div> <!-- .slide: class="center" -->
Note: I ran a poll on twitter asking me to do this in entirely emoji, but i can't

Russell also suggested this might be a bit of fun

So, let's get started with a bit about how uniode got started

the birds and the bees, if you will. *BOOM BOOM *
---

Note: Unicode History
---
  <!-- .element: class="fragment" -->
 <div style='width: 100%; margin: 0 auto;'><p align='center'><img height='400px' src='pictures/t/chicken.svg'><img height='400px' src='pictures/g/hot_bath.svg'></p></div> <!-- .slide: class="center" -->
Note: We're here in hungary. I don't think I need to explain how you most definiately need to be using unicode compatible systems

---
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">$ python</code></pre></div>
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">>>> Sophia = "fantastic"</code></pre></div>
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">>>> Sophia</code></pre></div>
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">'fantastic'</code></pre></div>

 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">$ python <br>>>> Zsófia = “fantasztikus"<br> File "<stdin>", line 1<br> &nbsp; Zsófia = “fantasztikus"<br> &nbsp; &nbsp;&nbsp;^<br>SyntaxError: invalid syntax</code></pre></div> <!-- .element: class="fragment" -->

Note: if you wanted to do unicode in python, it won't work for things like variable names with non-ascii characters

---

 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">$ python</code></pre></div>
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">>>> Sophia = "fantastic"</code></pre></div>
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">>>> Sophia</code></pre></div>
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">'fantastic'</code></pre></div>

 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">$ python3<br>>>> Zsófia = "fantasztikus"<br>>>> Zsófia<br> 'fantasztikus'</code></pre></div> <!-- .element: class="fragment" -->
---

 <div style='width: 50%; margin: 0 auto;'><p align='center'><img height='400px' src='pictures/t/thumb_up.svg'></p></div> <!-- .slide: class="center" -->
  <!-- .element: class="fragment" -->
 <div style='width: 50%; margin: 0 auto;'><p align='center'><img height='400px' src='pictures/g/thinking.svg'></p></div> <!-- .slide: class="center" -->
Note: But what about emoji?

---
 <div style='width: 100%; margin: 0 auto;'><p align='center'><img height='800px' src='pictures/t/japan.svg'></p></div> <!-- .slide: class="center" -->
Note: japanese history
---
Note: emoticon vs emoji

---
Note: web and wing dings
---
Note: msn, yahoo
---

---
 <div style='width: 100%; margin: 0 auto;'><p align='center'><img height='400px' src='pictures/g/hairy_heart.png'><img height='400px' src='pictures/g/yellow_heart.svg'></p></div> <!-- .slide: class="center" -->
---
 <div style='width: 100%; margin: 0 auto;'><p align='center'><img height='400px' src='pictures/t/camel1.svg'><img height='400px' src='pictures/t/camel2.svg'></p></div> <!-- .slide: class="center" -->
---
 <div style='width: 100%; margin: 0 auto;'><p align='center'><img height='400px' src='pictures/t/grinning.svg'><img height='400px' src='pictures/t/grimice.svg'></p></div> <!-- .slide: class="center" -->
Note: Grinning vs Grimace
---