# &nbsp;
# <img style="width: 130px; margin-bottom: 0px" src="pictures/t/lockkey.svg"> + <img style="width: 130px; margin-bottom: 0px" src="pictures/t/imp.svg"> => <img style="width: 130px; margin-bottom: 0px" src="pictures/t/boom.svg"> <!-- .slide: class="center" -->


 <img src="pictures/footer.svg" />

Note: t/down | g/koala | t/sparkles
---

 <div style='width: 50%; margin: 0 auto;'><p align='center'><img height='400px' src='pictures/g/wave.svg'></p></div> <!-- .slide: class="center" -->

Note: Hi! I'm Katie. You may know me as 'glasnt' or That Emoji Girl
---

 <div style='width: 50%; margin: 0 auto;'><p align='center'><img height='400px' src='pictures/t/megaphone.svg'></p></div> <!-- .slide: class="center" -->
Note: 

I've been doing this talk about the place called

---
## The Power and Responsibility <!-- .slide: class="center" -->
##of Unicode Adoption <!-- .slide: class="center" -->
Note: 
"The power and responsibility of UNicode adoption"

I first gave it at this very meetup in March last year.

I know right? It sounds like a proper technical talk, but it's actually me just yelling about emoji and stuff

Thing is, that's not the name
---

## The Power <img style="margin-bottom: 0px" src="pictures/o/bolt.svg" width="50px"> and Responsibility <img style="margin-bottom: 0px" width="50px" src="pictures/g/sweat.svg"> <!-- .slide: class="center" -->
## of Unicode Adoption <img style="margin-bottom: 0px" width="50px" src="pictures/t/sparkles.svg"> <!-- .slide: class="center" -->

Note: this is the name. it has emoji in the title

This has caused me all *sorts* of fun when trying to propose and present at conferences

---

 <img src="pictures/djangoconeu_accept.png" />

Note: For example, some conferences can't get the name right, even when it's been entered into their system

---

 <img src="pictures/easychair.png" />

Note: Some like some characters, but not others

I had to resubmit this one and remove specific characters



---
 <img src="pictures/oscon_talk.png" />

Note: Some won't allow emoji in the talk title, but will in the description (sadface)

---

 <img src="pictures/kiwicon_cfp.png" />

Note: Some just get a little bit corrupted (kiwicon)
---
 <img src="pictures/pyconau_schedule_list.png" />
Note: but sometimes it works!

... on the website
---
 <img src="pictures/pcau_2.jpg" />
Note: but not on the printed schedule
---

 <img src="pictures/pcau_3.jpg" />
Note: or on the AV notes.

Side note, it's REALLY fun when the person introducing you on stage reads that verbatim

---

 <img src="pictures/djeu_5.jpg" />

Note: when you have broken unicode in the middle of glossy printed programs, that's fun

---

 <img src="pictures/djeu_1.jpg" />

Note: but it's not too bad when the schedule poster on the wall just leave them out
---

 <img src="pictures/djeu_1.jpg" />
 <img src="pictures/djeu_2.jpg" />
Note: because they can be corrected

---

 <img src="pictures/pcau_1.jpg" />
Note: But the best part is when the digital boards work

Because I can tell you exactly what operating system this is running. Windows 8

---
# &nbsp;
 <img src="pictures/ms_sweat.png" />

Note: This is the emoji
---
 <img src="pictures/sweat_versions.png" />

Note: 

Different vendors have implemented emoji differently. In this case, the 'sweat drop' face is the most easily recognisable as windows, because it looks like a face with boils all over it or something

(picture of different sweat)

Based on this, we can guess the operating system, down to the version, using just the emoji being displayed.

---

 <div style='width: 50%; margin: 0 auto;'><p align='center'><img height='400px' src='pictures/g/sweat.svg'></p></div> <!-- .slide: class="center" -->

Note: but then sometimes things break completely.

---


 <img src="pictures/mcec_large.png" style="margin-top: -50px" />

Note: Take this signage, from RubyConf just last week in Melbourne
---
 <img src="pictures/mcec.png" style="margin-top: -50px" />

Note: https://twitter.com/robjacoby/status/829474149143769088
Rob Jacoby, twitter

This is what the sign was showing.

---
 <img src="pictures/mcec_a.png" style="margin-top: -50px" />
Note: So what's this gibberish?
---
## &nbsp;
## &nbsp;
# `ud83dude0dnn`
---
## &nbsp;
## &nbsp;
# `\ud83d\ude0dnn`
---
## &nbsp;
## &nbsp;
# `\ud83d \ude0d nn`
---
## &nbsp;
## &nbsp;
# `\u1F60D nn`
---

## &nbsp;
## &nbsp;
# <img src="pictures/g/hearts.png" style="width: 90px; margin-bottom: 0px"> `nn`
---

 <img src="pictures/speaker_tweet.png" style="margin-top: -50px" />
Note: Thanks Rob
---

 <div style='width: 50%; margin: 0 auto;'><p align='center'><img height='400px' src='pictures/e/thinking.svg'></p></div> <!-- .slide: class="center" -->

Note: 


But this is a hacker conf, that's not that interesting

What if we could hack with emoji.

Is it possible?

Well, it depends on your definition of hacking, and emoji



---

 <img src="pictures/not_emoji.png" />

Note: 
These are not emoji

So if, for example, you were to say download an executable claiming to give you an emoji pack for your favourite chat client, that's not hacking. That's you downloading a random executable and getting what's coming to you

What's also not hacking, well, technically, is a Denial of Service attack that was recently fixed by apple.
---

 <div style='width: 100%; margin: 0 auto;'><p align='center'><img height='266px' src='pictures/space.svg'><img height='266px' src='pictures/mobile.png'><img height='266px' src='pictures/space.svg'></p></div> <!-- .slide: class="center" -->

---
 <div style='width: 50%; margin: 0 auto;'><p align='center'><img height='400px' src='pictures/t/rainbow_flag.svg'></p></div> <!-- .slide: class="center" -->
Note: Who is familiar with the Pride Flag emoji that was just added?
---

 <div style='width: 100%; margin: 0 auto;'><p align='center'><img height='266px' src='pictures/t/whiteflag.svg'><img height='266px' src='pictures/zwj.svg'><img height='266px' src='pictures/t/rainbow.svg'></p></div> <!-- .slide: class="center" -->
Note: it's comprised of two existing emoji, the white flag and the rainbow, but with a special character

a Zero Width joiner, between them

You don't normally see this because in your flag picker, you see the end result.

However 

---
 <div style='width: 100%; margin: 0 auto;'><p align='center'><img height='266px' src='pictures/t/whiteflag.svg'><img height='266px' src='pictures/0.svg'><img height='266px' src='pictures/t/rainbow.svg'></p></div> <!-- .slide: class="center" -->

<span class="bfoot" style="bottom: -280px"><a href="http://thehackernews.com/2017/01/crash-iphone-emoji.html">You Can Crash Anyone's iPhone or iPad With A Simple Emoji Text Message (2017)</a></span>
Note: There was a bug where if you sent the two emoji with a number between them, the device would get really confused, and not know what to do
---

 <img src="pictures/iphonecrash.jpeg" />

<span class="bfoot"><a href="https://www.kazoosoft.eu/wp-content/uploads/2015/05/Iphone6Bug2015.jpeg">jazoosoft.eu</a></span>
Note: so it would crash

this isn't the firts time a bug like this has happened
---
 <img src="pictures/effectivepower.jpg" />

<span class="bfoot"><a href="http://s.wsj.net/public/resources/images/BN-IP966_IMESSA_G_20150527143121.jpg">wsj.net</a></span>

Note: This has happened before in what's known as the effective power bug
---


<pre style="font-size: 60px"><code>
effective. 
Power 
لُلُصّبُلُلصّبُررً ॣ ॣh ॣ ॣ
冗 
</code></pre> 
<span class="bfoot" style="bottom: -250px"><a href="https://www.youtube.com/watch?v=hJLMSllzoLA">The Effective Power Bug (2015)</a></span>
Note: how this worked is that the words 'effective power' had no meaning, but the text after it, that's displaying weirdly here, would set it off

When this text appeared in a notification popup, the truncation of that message would happen part way in the stuff on the third line, and the phone would get confused and restart

but that's not hacking.
---

 <div style='width: 50%; margin: 0 auto;'><p align='center'><img height='400px' src='pictures/web.svg'></p></div> <!-- .slide: class="center" -->


---

<img style="margin-top: 100px" src="pictures/o/spoon.ws.svg" height="300px">
---
 <div style='width: 100%; margin: 0 auto;'><p align='center'><img height='114px' src='pictures/g/R.svg'><img height='114px' src='pictures/g/F.svg'><img height='114px' src='pictures/g/C.svg'><img height='114px' src='pictures/e/3.svg'><img height='114px' src='pictures/e/4.svg'><img height='114px' src='pictures/e/9.svg'><img height='114px' src='pictures/e/2.svg'></p></div> <!-- .slide: class="center" -->
---
 <div style='width: 100%; margin: 0 auto;'><p align='center'><img height='160px' src='pictures/space.svg'><img height='160px' src='pictures/space.svg'><img height='160px' src='pictures/o/spoon.svg'><img height='160px' src='pictures/space.svg'><img height='160px' src='pictures/space.svg'></p></div> <!-- .slide: class="center" -->
### `http://xn--9q9h.ws`
Note: that's the domain, but the path...
---

# `?utf8=✓` <!-- .slide: class="center" -->
---
### `google.com`<img src="pictures/t/padlock.svg" style="margin-bottom: 0; width: 60px">`/test/عربي.امارات` <!-- .slide: class="center" -->
<span class="bfoot" style="bottom: -280px"><a href="http://www.rafayhackingarticles.net/2016/08/google-chrome-firefox-address-bar.html">Google Chrome, Firefox Address Bar Spoofing Vulnerability</a></span>

Note: RTL
---
###`عربي.امارات/google.com`<img src="pictures/t/padlock.svg" style="margin-bottom: 0; width: 60px">`/test` <!-- .slide: class="center" -->
<span class="bfoot" style="bottom: -280px"><a href="http://www.rafayhackingarticles.net/2016/08/google-chrome-firefox-address-bar.html">Google Chrome, Firefox Address Bar Spoofing Vulnerability</a></span>
---
 <div style='width: 100%; margin: 0 auto;'><p align='center'><img height='400px' src='pictures/t/world.svg'><img height='400px' src='pictures/t/fire.svg'></p></div> <!-- .slide: class="center" -->

<span class="bfoot" style="bottom: -80px"><a href="https://poststatus.com/the-trojan-emoji/">Anatomy of a Critical Security Bug</a></span>
Note: What is hacking is this wonderful incident I found involving mysql, not-strict tables, and wordpress

With literally a bug that could set the world on fire

---

## `STRICT_ALL_TABLES` <!-- .slide: class="center" -->

Note: This could have all been avoided if STRICT TABLES had been enabled for wordpress

Wordpress core used some of the ... more interesting features of mysql, so they couldn't enable this, and this is why everthing was a fire

---

 <div style='width: 100%; margin: 0 auto;'><p align='center'><img height='266px' src='pictures/space.svg'><img height='266px' src='pictures/g/slightly7.png'><img height='266px' src='pictures/space.svg'></p></div> <!-- .slide: class="center" -->


Note: This character could break everything.
---

 <div style='width: 100%; margin: 0 auto;'><p align='center'><img height='266px' src='pictures/space.svg'><img height='266px' src='pictures/g/smiling1.png'><img height='266px' src='pictures/space.svg'></p></div> <!-- .slide: class="center" -->

Note: But not this one.

---
 <div style='width: 100%; margin: 0 auto;'><p align='center'><img height='400px' src='pictures/g/smiling1.png'><img height='400px' src='pictures/g/slightly7.png'></p></div> <!-- .slide: class="center" -->
## &nbsp;

Note: YOu see, these are two different smiles
---
 <div style='width: 100%; margin: 0 auto;'><p align='center'><img height='400px' src='pictures/g/smiling1.png'><img height='400px' src='pictures/g/slightly7.png'></p></div> <!-- .slide: class="center" -->
## &nbsp; &nbsp; `U+263A`&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; `U+1F642`

Note: one dates back to Unicode 1.1, in 1991, and the latter is a newer emoji.

Hence why the one of the left has a smaller unicode code point
---
 <div style='width: 100%; margin: 0 auto;'><p align='center'><img height='400px' src='pictures/g/smiling1.png'><img height='400px' src='pictures/g/slightly7.png'></p></div> <!-- .slide: class="center" -->
## &nbsp; &nbsp; `E2·98·BA` &nbsp; &nbsp; `F0·9F·98·8A`
Note: 
The emoji the right uses four bytes

And there's a small issue in mysql when strict tables is turned off. If you try and insert an emoji it'll... truncate.

---

## `<q cite="Smile` <img src="pictures/g/slightly7.png" style="width: 50px; margin-bottom: 0px;">`">` <!-- .slide: class="center" -->
## `Be Happy</q>`

Note: So, say if you have a Wordpress blog that allows comments, and citations, and you have something like this, which would pass javascript validation because it's a complete tag

But because Mysql...
---

## `<q cite="Smile` &nbsp;&nbsp; &nbsp; &nbsp; <span style="color: white">.</span> <!-- .slide: class="center" -->
## &nbsp;

Note: It'd drop about here
---

## `script src="hax.ohno">` <!-- .slide: class="center" -->

Note: which means that if your NEXT comment happens to be something like this

because that's not a script tag, there's no opening angle bracket

---
## `<q cite="Smile` <!-- .slide: class="center" -->
## `...` <!-- .slide: class="center" -->
## `script src="hax.ohno">` <!-- .slide: class="center" -->
Note: you'd end up with a very large quote tag, that had a script attribute

sad trombone.

---

 <div style='width: 50%; margin: 0 auto;'><p align='center'><img height='400px' src='pictures/t/boom.svg'></p></div> <!-- .slide: class="center" -->

---

# `CVE-2015-3438` <!-- .slide: class="center" -->
Note: So that's CVE 2015 3 4 3 8

It's been patched as of WordPress 4.2, so please PATCH YOUR THINGS
Wordpress 4.2 introduced emoji natively into the system... and also removed a small issue with it breaking everything

but you get new emoji! you should update your things!
---
# MySQL <!-- .slide: class="center" -->
## `STRICT_ALL_TABLES` <!-- .slide: class="center" -->
Note: also, make sure you enable strict tables, because yowsa.

---

 <div style='width: 50%; margin: 0 auto;'><p align='center'><img height='400px' src='pictures/t/imp.svg'></p></div> <!-- .slide: class="center" -->

Note: this probably isn't the only thing out there, but it's something to watch out for



---
 <div style='width: 50%; margin: 0 auto;'><p align='center'><img height='400px' src='pictures/g/claps.svg'></p></div> <!-- .slide: class="center" -->

### glasnt.com/talks