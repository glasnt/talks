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

This is based on a true story, it happened to a friend of a friend of mine.

---

 <!-- .slide: data-background="#000"-->
# &nbsp;

Note: Say you have a project

You find a cool widget on GitHub

You want to use it.

But.. 

It hasn't been updated in 4 years

There's cobwebs all over it

It should do what you want

But it needs changes

---


 <!-- .slide: data-background="#000"-->
# "Just fork it!" <!-- .slide: class="center" -->
## Well, it's not that simple <!-- .element: class="fragment" -->

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
# Limitations
## Parent Lock-in <!-- .element: class="fragment" -->
## Default Pull Requests <!-- .element: class="fragment" -->
## No Issue Logging by Default <!-- .element: class="fragment" -->
## Commits Don't Count <!-- .element: class="fragment" -->

Note: Parent - perma link to source. Network Graph

PR - defaults to parent, accidently attempt to merge upstream


Issues - CORRECTION - issues are disabled by default, but can be enabled.

Commits - you can work your butt off and your green graph doesn't fill up


---

 <!-- .slide: data-background="#000"-->

# Licensing
# BSD-3 <!-- .element: class="fragment" --> <!-- .slide: class="center" --> <!-- .element style="font-size: 5em" --> 

Note: Licensing is fun. If you have no licence, it defaults to All Rights Reserved

ARR means you own the copyright, and noone else can have it

So, that's no fun. Let's use BSD as an example

Berkeley Software Distribution 3 Clause License

---
 <!-- .slide: data-background="#000"-->
# Licensing
# BSD-3? <!-- .slide: class="center" --> <!-- .element style="font-size: 5em" --> 

Note: What does this even mean?

---

 <!-- .slide: data-background="#000"-->

<pre style="top: -20px">
Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions
are met:

* Redistributions of source code must retain the above copyright
notice, this list of conditions and the following disclaimer.

* Redistributions in binary form must reproduce the above copyright
notice, this list of conditions and the following disclaimer in the
documentation and/or other materials provided with the distribution.

* Neither the name of the organization nor the names of its
contributors may be used to endorse or promote products derived
from this software without specific prior written permission.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
"AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS
FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE
COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT,
INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
(INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION)
HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT,
STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED
OF THE POSSIBILITY OF SUCH DAMAGE.
</pre> 

Note: Holy Wall Of Text, BatMan!

---

 <!-- .slide: data-background="#000"-->
# What this actually means <!-- .slide: class="center" -->
## (This is not legal advice)

---

 <!-- .slide: data-background="#000"-->
# BSD-3 - Can:
## Commercially Use <!-- .element: class="fragment" -->
## Modifiy <!-- .element: class="fragment" -->
## Distribute <!-- .element: class="fragment" -->
## Place Warranty <!-- .element: class="fragment" -->


Note: 

From https://tldrlegal.com/


Commercial Use, can use software for

Modify the software and create derivatives.

Distribute original or modified (derivative) works.

Place Warranty on the software licensed.

---

 <!-- .slide: data-background="#000"-->
# BSD-3 - Cannot:
## Use Trademark <!-- .element: class="fragment" -->
## Hold Liable <!-- .element: class="fragment" -->

Note: 

Use Trademark

You may not use the names of the original company or its members to endorse derived products.

Hold Liable

Describes the warranty and if the software/license owner can be charged for damages.

---

 <!-- .slide: data-background="#000"-->
# BSD-3 - Must:
## Include License <!-- .element: class="fragment" -->
## Include Copyright <!-- .element: class="fragment" -->
## <img src="pictures/awkward.gif"> <!-- .element: class="fragment" -->


Note: 

Include License

Including the full text of license in source or object code copies.

Include Copyright

Describes whether the original copyright must be retained.

---
 <!-- .slide: data-background="#000"-->
# 'Competitor' Code
## &copy; Their Company 2014 <!-- .element: class="fragment" -->
## &copy; Your Company 2015 <!-- .element: class="fragment" -->

Note: having copyrights with other company's copyright is kinda a weird thing, amiright?

---

 <!-- .slide: data-background="#000"-->
# Dead Source
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
Note: A lot of things have happened since that talk .

For one, Python 3 support has improved!

For another, I learnt not to use gifs in slides.



---
#### You should totally go see: <!-- .slide: class="center" -->
## Passing the Baton: Succession planning for your project talk
### VM Brasseur
### This afternoon!

---
<br> 
<br> 
<br> 
<br> 
<img src="pictures/claps.svg" height="100px">

#### glasnt.com/talks

Note: thank you for your time.