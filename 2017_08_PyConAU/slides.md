###&nbsp; 
# How to handle abandoned projects, Take Two <!-- .slide: class="center" -->
<img src="pictures/footer_new.svg" width="500px">
---
 <img src="pictures/auckland.jpeg" />
 <span class='foot'>SPE Bari, Auckland. MenuLog.co.nz</span>
Note: So I'm in a pub in Auckland, as you do.

It's 2013, and I've just finished attending my first open source software conference. For the first time, the Open Source Developers Conference, or OSDC, has been held outside of Australia.

Paul Fenwick has just given the closing keynote, and a bunch of delegates have retired to the bar. The organisers are rounding up a bunch of people that are all going to see the blockbuster Gravity in the cinema

And I'm next to a guy with dreads.

"This was a pretty good conferece", I say.

"Well, I'm glad you agree", he says.

"I've got some ideas of my own that I might present next year, this little thing I've been working on"

"You should tweet that!"

---
 <div style='margin: 0 auto;'><p align='center'><img src='pictures/eddie_1.png'></p></div>  <!-- .slide: class="center" -->
Note: and so I do, using the slang of the time.

Moments later, I get a notification. "Someone has retweeted your tweet!"
---

 <div style='margin: 0 auto;'><p align='center'><img src='pictures/eddie_2.png'></p></div>  <!-- .slide: class="center" -->
Note: ... Ah.

Turns out the bloke with the dreads was Ben Dechrai.. who sort of.. co-founded OSDC... yeah...

---
 <img src="pictures/brisbane.jpg" />

 <span class='foot'>King George Square, Brisbane. Public Domain</span>

Note: So I'm in a public square in Brisbane, as you do. It's 2015, a wonderful winter's afternoon, and I'm supposed to be giving a talk.

Instead I'm holding someone's ice-cream as they say hello to two gorgeous labradors.

---
 <img src="pictures/hatrack.png" />
 <span class='foot'>PyCon AU 2015, Brisbane. CC-BY 2.0</span>
Note: 
At PyCon AU 2015, my first Python developers conference, I was supposed to give two talks. It wasn't the first time I'd been asked to do this at a conference, so I thought I'd be fine.

The first talk on Sunday was about acknowledging contributions to open source that aren't code, now known as the Hat Rack talk.

---

Note: The second talk never happened.

Thankfully today, two years on, I can give that talk.
---
 <!-- .slide: data-background="#000"-->
## &nbsp;
# How to handle abandoned projects <!-- .slide: class="center" -->
 <img src="pictures/footer_old.svg" />

Note: Hi, I'm Katie, and this is how to handle abandoned projects

---

 <!-- .slide: data-background="#000"-->
# &nbsp;

Note: And this is where I freeze.

What do I say? What can I say? Should I say anything?

Does context matter?

I mean, the talk is clearly about project abandonment, so something must have gone down

Was it burnout? Was it a loss of interest? Was it an unexpected passing of the maintainer?

I could share the tips tricks and configuration suggestions without the context.

Because does it matter? Does context matter?

This is what I had a problem with. All this technology stuff in my talk is solid, current, and repeatable.

Sure as you can see it covers github, but that's the stack I use, so that's the stack of cover.


But a talk just about configuration, without the story, what kind of a talk is that?
---

 <img src="pictures/meetup.jpg" style="margin-top: -50px" />

Note: 

A few weeks after pycon I gave this talk at a local Sydney php user group. I
did the talk, saying the context was that "it happened to a friend of a friend
of mine". But that was bullshit. It was an outright lie, but it let me get past
the context and into the content.

And now I'm here, revisiting this question. Does context matter? Does the human
story around why the tech exists matter? Does anyone care about what happened
to put me in this situation?

Yes. Yes it matters. It matters more than the tech. You can google a bunch of
things around how migrate code and how to make copies and how to do all that
push button get repo stuff. But if by telling my story it helps a single person
going through the same thing I did feel less alone in what was a pretty shit
situation, all things told, then it is absolutely worth it.

---

 <img src="pictures/office.png" />


Note: So I'm in an office in Sydney, as you do. It's early 2015. It's a Tuesday. The month earlier
I'd come back from doing a talk at an international conference about a project
I'd been working on at the company for just over a year at that point

It's a few minutes before standup, and I've just cracked this functionality hack
in elastic search that meant that we could store some complex data within the system
that meant that a function we wanted to implemented was now achievable.

I'm bouncing on my feet at this point, because it was a breakthrough three or four
layers down the stack that meant that we were about to crack production readiness .

Effective immediately,
... 

Just as standup starts, I get called into the CTO's office.

---


 <img src="pictures/office-dark.png" />
Note: 
Effective immediately, I am no longer employed at the company. My role has been made redundant.

A quarter of the department was walked that day. By the end of the year, most of the lucky ones had left of their own accord.

I was shattered.

I'd been working there for four years. It was my first role that had anything at all to do with open source.

I was a poster child for this place. Literally, on posters.

Which is really fun to see your face on a google ad from a place that has just walked you, let me tell you.


---

 <img src="pictures/??" />

Note: I was lucky. I was able to find a new job really quickly. I reached out to a friend and former coworker

and they were able to get me an interview with their employer the next day.

After settling in at that place, I then went back to working out what could be done about the project

---

 <!-- .slide: data-background="#000"-->

Note: 
And thus the original talk content continues

---
 <!-- .slide: data-background="#000"-->
# "Just fork it!" <!-- .slide: class="center" -->
## Well, it's not that simple <!-- .element: class="fragment" -->

Yes, it was a public project on github, but
---

 <!-- .slide: data-background="#000"-->
# GitHub doesn't<br>do "Forking" <!-- .slide: class="center" -->

Note: They don't implement the traditional forking methodology

We'll get to that

---

 <!-- .slide: data-background="#000"-->
# Plus, there's more issues. <!-- .slide: class="center" -->

---

 <!-- .slide: data-background="#000"-->
## GitHub Forking <!-- .slide: class="center" -->
## Licensing <!-- .element: class="fragment" -->
## 'Competitor' Code <!-- .element: class="fragment" -->
## Dead Source <!-- .element: class="fragment" -->


Note: We'll discuss all these things

---

 <!-- .slide: data-background="#000"-->
# GitHub Forking
## <img src="pictures/github_forking.gif"> <!-- .element: class="fragment" -->
Note: Github's forking != Traditional Forking

It's your copy for branches and PR merges.

It's not a full working copy of a code base
---

 <!-- .slide: data-background="#000"-->
# Limitations <!-- .slide: class="center" -->
## Parent Lock-in <!-- .element: class="fragment" -->
## Default Pull Requests <!-- .element: class="fragment" -->
## No Issue Logging by Default <!-- .element: class="fragment" -->
## Commits Don't Count <!-- .element: class="fragment" -->

Note: Parent - perma link to source. Network Graph

PR - defaults to parent, accidently attempt to merge upstream

Issues - CORRECTION - issues are disabled by default on forks, but can be enabled.

Commits - you can work your butt off and your green graph doesn't fill up


---

 <!-- .slide: data-background="#000"-->

# Licensing <!-- .slide: class="center" -->

Note: Licencing is fun, especially because laws around this stuff depend on the country you're in.

It also depends on the site you're on.
---
 <!-- .slide: data-background="#000"-->
### GitHub Code <!-- .slide: class="center" -->
### No LICENCE?
#### -> All Rights Reserved

 <span class='foot'>https://help.github.com/articles/licensing-a-repository/</span>

Note: For code on github, if the repo does not have a licence, no one may reproduce, distribute, or create derivative works from it. At all.

---
 <!-- .slide: data-background="#000"-->
## choosealicense.com <!-- .slide: class="center" -->
## opensource.org/licenses

Note: There are many places where you can get information about what lience to choose

This isn't a licencing talk, so I defer to these resources.

But of note, different websites have different default licence rights

---
 <!-- .slide: data-background="#000"-->
##### <aside> <!-- .slide: class="center" -->
### StackOverflow
### Code? MIT
### Everything else? CC-BY-SA
##### </aside>

 <span class='foot'>[A New Code License: The MIT, this time with Attribution Required, StackOverflow Meta](https://meta.stackexchange.com/questions/272956/a-new-code-license-the-mit-this-time-with-attribution-required?cb=1)</span>

Note: Last year stackoverflow changed their default licencing arragements. For ages it's always been Creative Commons Share Alike. Which means you can share and adapt, but you must attribute.

But as of March 2016, all code is MIT licenced. Which allows you to either keep the MIT licence, or remove it as long as you attribute the original author.

Which can get fun, when you're talking abo
---
 <!-- .slide: data-background="#000"-->
# 'Competitor' Code <!-- .slide: class="center" -->
## &copy; Their Company 2014 <!-- .element: class="fragment" -->
## &copy; Your Company 2015 <!-- .element: class="fragment" -->

Note: having copyrights with other company's copyright is kinda a weird thing, amiright?

---

 <!-- .slide: data-background="#000"-->
# Dead Source <!-- .slide: class="center" -->
## <img src="pictures/tumbleweed.gif"> <!-- .element: class="fragment" -->

Note: If the source upstream is dead, then that's an inhibitor of innovation


No merges ever, no changes. Nerfed fork, very limited play
---

 <!-- .slide: data-background="#000"-->

# So what could you do? <!-- .slide: class="center" -->
---

 <!-- .slide: data-background="#000"-->
# Ask. <!-- .slide: class="center" --> <!-- .slide: class="center" --> <!-- .element style="font-size: 5em" --> 

Note: Ask.
Possible solutions: transfer of ownership, proper copy fork with attribution, many other

---

 <!-- .slide: data-background="#000"-->
# So why should<br>you care? <!-- .slide: class="center" -->

---
 <!-- .slide: data-background="#000"-->
# PHP 7 <!-- .slide: class="center" --> <!-- .slide: class="center" --> <!-- .element style="font-size: 5em" --> 

Note: PHP5 will die. PHP4 shuold already be dead.

When everyone upgrades, the old code needs to come along, or it'll be lost.

Not just PHP

---
 <!-- .slide: data-background="#000"-->
# Ruby 1.8, 1.9.3 EOL <!-- .slide: class="center" -->
## <p> Example: <code>pry-debugger</code></p> <!-- .element: class="fragment" -->

Note: EOL languages. Things have migrated on

pry-debugger - only works with 1.x

Was the go to debugger now not so much

Top of README says: 2.0? use byebug

you shouldn't be using 1.8, 1.9.3 anyway, EOL

---
 <!-- .slide: data-background="#000"-->
# Python 3 <!-- .slide: class="center" -->

## Supported in < 10% of packages <!-- .element: class="fragment" -->

Note: Per PyCon US 2015 Guido keynote

Once 2.7 goes EOL, then projects can't be used any more.

No satisfaction in just porting it

long tail of dependencies prohibit porting

There are automated tools for this

---

 <!-- .slide: data-background="#000"-->
# Non-Language Dependent Factors <!-- .slide: class="center" -->

Note: There's other things that could happen

---

 <!-- .slide: data-background="#000"-->
# Google Code <!-- .slide: class="center" -->
## Read Only <!-- .element: class="fragment" -->

Note: Not accepting new projects as of January.


Read Only as of Aug 24 (Tuesday ish Australia time)

Had a few months, but now anything on there is R/O


---

 <!-- .slide: data-background="#000"-->
# SourceForge <!-- .slide: class="center" -->

Note: VLC binaries 'abandoned', being updated w/out consent, with spyware

Also, small two week outage in there


---

 <!-- .slide: data-background="#000"-->

# Every active project is going to need love <!-- .slide: class="center" -->


Note: 'active' meaning someone's using it, who's moving to the new structure

The maintainer may be off growing grapes

Hostile Forks Don't Help

---

 <!-- .slide: data-background="#000"-->
# So what can you do? <!-- .slide: class="center" -->
## Abandon Responsibly <!-- .element: class="fragment" -->
## Restore Dead Code <!-- .element: class="fragment" -->

Note: If you have a project vs if you see a project

---
 <!-- .slide: data-background="#000"-->

# Abandon Responsibly
## Update your README <!-- .element: class="fragment" -->
## Mark as inactive <!-- .element: class="fragment" -->
## Link to a better solution <!-- .element: class="fragment" -->
## Leave a forwarding address <!-- .element: class="fragment" -->
## Assign a new maintainer <!-- .element: class="fragment" -->

Note: Documentation is your friend

You don't want people coming across your stuff when there's something better

You really don't want people using code that has deps with known vuls

---

 <!-- .slide: data-background="#000"-->
# GitHub Ownership Transfer <!-- .slide: class="center" -->

Note: Create a new/existing organisation

Add the admin from the otehr one in (shared rights)

Transfer 

Remove new admin

---

 <!-- .slide: data-background="#000"-->
# Benefits
## All the PRs, Issues, Commits stay <!-- .element: class="fragment" -->
## 301 Redirects to new URL <!-- .element: class="fragment" -->
## You get the commit bit :D <!-- .element: class="fragment" -->


Note: the 301 is very nice, it will automatically users to the new repo based on the old URL

This may break if you attempt to overload the old namespace, however.

---

 <!-- .slide: data-background="#000"-->

# Restore Dead Code
## Check their README <!-- .element: class="fragment" -->
## <img src="pictures/notdeadyet.gif"> <!-- .element: class="fragment" -->


---
 <!-- .slide: data-background="#000"-->

# Restore Dead Code
## Check their README
## Is it inactive? <!-- .element: class="fragment" -->
## Is there a better solution? <!-- .element: class="fragment" -->
## Can you be the new maintainer? <!-- .element: class="fragment" -->

Note: check the history.

Check if the latest release was stable.

Check if they've mentioned anything in the latest notes

Check if they suggest anything more in their read me

See if they are looking for someone

Do they have an IRC channel? A mailing list?

---

 <!-- .slide: data-background="#000"-->
# There's probably<br>more factors in play <!-- .slide: class="center" -->

Note: It's never just that simple.

Politics 

Friendships 

Pet Projects

---

 <!-- .slide: data-background="#000"-->
# Go to rule:<br>There's nothing wrong<br>with being nice. <!-- .slide: class="center" -->

Note: the ability to openly communicate is one facet of opensource that makes it amazing

They've put in the effort to make a solution that's usefulness is expiring

Help make their solution timeless.

---

 <!-- .slide: data-background="#000"-->
# Thanks! <!-- .slide: class="center" -->
 <img src="pictures/footer_old.svg" />

Note: Thanks! /me mock cheers

---

## &nbsp;

Note: 

---
#### You should totally go see: <!-- .slide: class="center" -->
## Passing the Baton: Succession planning for your project talk
### VM Brasseur
### This afternoon!

Note: If you're interested in this stuff, and around the planning of such things
You really really need to go see VM Brasseur's talk this afternoon.
Like really really need to.
---

 <img src="pictures/brisbane_pycon.jpg" />

Note: I've had two years to try and get this talk right.

Back in Brisbane, I was so stressout that I ended up having a panic attack.

I don't remember a lot of the specifics leading up to the talk, so I've had to
go and ask people who were there how it went down.

That sunday afternoon, I didn't look right. I was stressed out in the break leading up
to the talk, and I was trying to edit my slides at the last minute. Pro-tip, this never ends well

I distinctly remember making my way to the room with the laptop, looking down the corridor, seeing the lecturn, and having the whole dolly zoom effect happen, and hoping NOPE.

And you know what the immediate response was?

Okay. Come over here and sit down.

They'd planned for this. I didn't have to do anything I wasn't comfortable with.

So immediately, waves of relief start washing over me.

And then the reject and anxiety set in.

I'd just let everyone down. They knew I was going to fail. I'm a terrible person. I shouldn't be here. I don't deserve to be here. I want to go home.

Thankfully only a few moments into this sinking whirlpool of emotions, I was asked if I was okay, and if some freshair would be helpful
---

 <img src="pictures/brisbane.jpg" />

Note: it was that trip outside that saved me from a breakdown. I mean, I wasn't okay, but I knew I would be.

What started as 'let's get some freshair' turned into 'let's go into full distraction and self-care mode and go get some icecream'. The amazing puppies we met along the way was only icing on the cake.

I came back to the conference after that. I sat in the back of the room for the end of day lightning talks and closing address... but I came back.

---

 <img src="pictures/brisbane_noodle.jpg" />
 <span class='foot'>[Brisbane Noodle Night Markets, Espresso and Matcha](http://espresso-and-matcha.blogspot.com.au/2015/07/brisbane-noodle-night-markets-southbank.html)</span>

Note: that night, I didn't go home. I went out with a group of people to the noodle markets over in Southbank

My phone was going off by this point. People messaging me asking where I was, if I was okay. There was word that something was wrong. One person heard that I got gastro (erk). It was starting to set me off again

It was suggested that I give my phone to a friend to hold onto so I wouldn't keep getting alerted and distracted. That evening was really nice. I ate.. something, I can't remember. But it was great just to be around people who wanted me to be around.

---

 <img src="pictures/brisbane_day.jpg" />

Note: the next day, I went back. I could have hid, but I didn't. I wanted to be around these amazing people.

The Monday and Tuesday were development sprint days. That was the sprints that I was introduced to BeeWare. And the rest is history.

If I had left, I wouldn't have come back. At all. But I did. And here I am.

---

 <div style='margin: 0 auto;'><p align='center'><img src='pictures/dunedin.jpg'></p></div>  <!-- .slide: class="center" -->

Note: it hasn't been smoothsailing for me since Brisbane.

After that incident, I went through therapy. If you're covered under Medicare,
you can go to your GP and get a Mental Health plan that allows you to get rebates on up
to 10 visits to a mental health professional each year.

Seriously. If you need to talk to someone, please do.

I've been seeing a professional for a few years now, and it's helped me a lot.

But I still get anxious. Especially over talks.

I've had many sleepless nights just trying to work out how to best phrase this one.

Being asked by Richard to keynote was a last minute thing. I wasn't his first choice, but I offered because I knew there were issues there, and I knew I could do it.

Plus, the fact that a talk slot opening up because of a speaker dropping out about a speaker dropping out of a talk... I couldn't help but use this oppurunity to give the talk I couldn't give at this conference two years ago.

It's okay to fail. If you can't give a talk and you have to step away, that's okay. I had to step away, and now I can step in place when the time came.

---

 <div style='margin: 0 auto;'><p align='center'><img src='pictures/selfiesquish.jpg'></p></div>  <!-- .slide: class="center" -->

Note: what has helped me through out all of this is the community. Just having
people who want me around is more helpful than you could ever imagine.

Of note, this particularly lovely group of people here. You may notice a Paul Fenwick in there,
who I mentioned right at the start of this talk.

With his permission, I want to share a small story that shows again just how the little things
can help some feel welcome and included in a community.

I often get the oppurtinuty to go to conferences in communities I'm not a part of,
and one of those was devworld.
---

 <img src="pictures/devworld.jpg" />

Note: So I'm in a pub in Melbourne that has a plane in it, as you do. It's late 2015, and I've found
myself at the speaker dinner for devworld.

The only reason I'm at devworld is because a) i got offered a ticket, and b), after seeing the speaker lineup, I say, and I quote: "OMG OMG OMG Paul Fenwick is keynoting devworld I must go!"

I remember Paul keynoting my first ever open source conference, and I regretted not being able to formally say hi.

I think there may have been a "meeting the queen moment" where we all lined up and shook his hand, but I doubted he remembered me.

So I'm at the dinner, and Paul arrives. And I get the oppurtinity to say hi. And I tell him about how I've seen him speak before, and a major reason why I'm at devworld is to see him.

He later told me that it was my enthusasm for looking forward to hearing him speak that made him feel more at ease in his role at the conference. And this is coming from a long time public speaker.
---

 <img src="pictures/???" />

Note: 
Letting people know that you have been looking forward to seeing them, wishing them luck with their speaking, and actively enjoying their company.. that is what makes a great community.

Going from just an event name that you've heard of before, into an annual pilgramage to see friends
and meet people and gather with your people... that is what makes an amazing community.

Having a group of people that actively help each other, either by activey volunteering
to help run events, and reaching out those in their community that need just a little bit of help, that's what makes an incredible community.

---

 <img src="pictures/??" />

Note: And it doesn't have to be big hugge things, it can be little things that make people feel included.

It might be as simple as quiet room, offering to moderating questions, ensuring a ramp or a lift is available to rooms for wheelchair, or even just making sure someones name spelled correctly.

Having stenographers or sign language intepretors. Having non-alcoholic beverages at dinner. Vege options and kosher meals.

Offering to sit with someone at lunch. Being there if someone needs a hand. Or just being there, actively listening.


Giving back to the community that gave so much to me is something that I've taken to heart, and dedicated a lot of my time to. And for my efforts
---
 <img src="pictures/glassbrick.jpg" />

Note: I got a shiny glass brick. The O'reilly open source award. I was absolutely honoured and humbled by this, so much so that I keep calling it a glass brick.

But it's not about the award. It's about the fact that actively helping people in your community, especially when they're having a bad time, can keep them around, and they have the potential to do great things.

And with that, I want to end this on a high note by sharing some of the things I"ve learnt in these two years.

---

 <img src="pictures/glassbrick.jpg" />

Lucite trophies show up as great big black blocks under xray scanners, so if you have to travel with one, keep it in your carry on, and make sure you take it out for scanning. And don't be surprised if every TSA agent makes the same joke or starts to give an award speech
---

 <img src="pictures/selfiesquish.jpg" />

Note: I don't do selfies, but I've found that if you gather some of your cutest friends and have your face half absured, you may be pleasently surprised by the result.

---

 <img src="pictures/office.jpg" />

Note: projects come and projects go. Companies fold.

---

 <img src="pictures/brisbane_pycon.jpg" />

Note: But the people in your project communities, they are amazing people who can build great things, and you should do everything in your power to help them feel included, and to bring in more amazing peole into your community,
---


 <img src="pictures/brisbane.jpg" />

Note: and sometimes, when everything seems too hard and you can't go on, the best thing to do right then, is to get icecream.
---
<br> 
<br> 
<br> 
<br> 
<img src="pictures/claps.svg" height="100px">

#### glasnt.com/talks

Note: thank you for your time.