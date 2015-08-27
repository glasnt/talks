# Life After Death <!-- .slide: class="center" -->
## How to handle abandoned projects
<img src="pictures/footer.svg">

Note: Breathe. Slow.

---

# Hi! <!-- .slide: class="center" -->

Note: This is totally based on a true story. It happened to a friend of a friend of mine.

---

# &nbsp; <!-- .element: style="margin-bottom: 1em" -->

Note: Say you have a project

You find a cool widget on GitHub

You want to use it.

But.. 

It hasn't been updated in 4 years

There's cobwebs all over it

It should do what you want

But it needs changes

---


# "Just fork it!" <!-- .slide: class="center" -->
## Well, it's not that simple <!-- .element: class="fragment" -->

---

# GitHub doesn't<br>do "Forking" <!-- .slide: class="center" -->

Note: They don't implement the traditional forking methodology

We'll get to that

---

# Plus, there's more issues. <!-- .slide: class="center" -->

---

## GitHub Forking <!-- .slide: class="center" -->
## Licensing <!-- .element: class="fragment" -->
## 'Competitor' Code <!-- .element: class="fragment" -->
## Dead Source <!-- .element: class="fragment" -->


Note: We'll discuss all these things

---

# GitHub Forking <!-- .element: style="margin-bottom: 1em" -->
## <img src="pictures/github_forking.gif"> <!-- .element: class="fragment" -->
Note: Github's forking != Traditional Forking

It's your copy for branches and PR merges.

It's not a full working copy of a code base
---

# Limitations <!-- .element: style="margin-bottom: 1em" -->
## Parent Lock-in <!-- .element: class="fragment" -->
## Default Pull Requests <!-- .element: class="fragment" -->
## No Issue Logging <!-- .element: class="fragment" -->
## Commits Don't Count <!-- .element: class="fragment" -->

Note: Parent - perma link to source. Network Graph

PR - defaults to parent, accidently attempt to merge upstream

Issues - physical limitation on workflow

Commits - you can work your butt off and your green graph doesn't fill up


---


# Licensing <!-- .element: style="margin-bottom: 1em" -->
# BSD-3 <!-- .element: class="fragment" --> <!-- .element style="font-size: 4em" --> 

Note: Licensing is fun. If you have no licence, it defaults to All Rights Reserved

ARR means you own the copyright, and noone else can have it

So, that's no fun. Let's use BSD as an example

Berkeley Software Distribution 3 Clause License

---
# Licensing <!-- .element: style="margin-bottom: 1em" -->
# BSD-3? <!-- .element style="font-size: 4em" --> 

Note: What does this even mean?

---


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

# What this actually means <!-- .slide: class="center" -->
## (This is not legal advice)

---

# BSD-3 - Can: <!-- .element: style="margin-bottom: 1em" -->
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

# BSD-3 - Cannot: <!-- .element: style="margin-bottom: 1em" -->
## Use Trademark <!-- .element: class="fragment" -->
## Hold Liable <!-- .element: class="fragment" -->

Note: 

Use Trademark

You may not use the names of the original company or its members to endorse derived products.

Hold Liable

Describes the warranty and if the software/license owner can be charged for damages.

---

# BSD-3 - Must: <!-- .element: style="margin-bottom: 1em" -->
## Include License <!-- .element: class="fragment" -->
## Include Copyright <!-- .element: class="fragment" -->
## <img src="pictures/awkward.gif"> <!-- .element: class="fragment" -->


Note: 

Include License

Including the full text of license in source or object code copies.

Include Copyright

Describes whether the original copyright must be retained.

---
# 'Competitor' Code <!-- .element: style="margin-bottom: 1em" -->
## &copy; Their Company 2014 <!-- .element: class="fragment" -->
## &copy; Your Company 2015 <!-- .element: class="fragment" -->

Note: having copyrights with other company's copyright is kinda a weird thing, amiright?

---

# Dead Source <!-- .element: style="margin-bottom: 1em" -->
## <img src="pictures/tumbleweed.gif"> <!-- .element: class="fragment" -->

Note: If the source upstream is dead, then that's an inhibitor of innovation


No merges ever, no changes. Nerfed fork, very limited play
---


# So what could you do? <!-- .slide: class="center" -->
---

# Ask. <!-- .slide: class="center" --> <!-- .element style="font-size: 4em" --> 

Note: This is totally what I did. Because this happened to me. Saddest of Panda


Possible solutions: transfer of ownership, proper copy fork with attribution, many other

---

# So why should<br>you care? <!-- .slide: class="center" -->

---

# PHP 7 <!-- .slide: class="center" --> <!-- .element style="font-size: 4em" --> 

Note: PHP5 will die. PHP4 shuold already be dead.

When everyone upgrades, the old code needs to come along, or it'll be lost.

Not just PHP

---

# Ruby 1.8, 1.9.3 EOL <!-- .slide: class="center" -->
## <p> Example: <code>pry-debugger</code></p> <!-- .element: class="fragment" -->

Note: EOL languages. Things have migrated on

pry-debugger - only works with 1.x

Was the go to debugger now not so much

Top of README says: 2.0? use byebug

you shouldn't be using 1.8, 1.9.3 anyway, EOL

---

# Python 3 <!-- .slide: class="center" -->

## Supported in < 10% of packages <!-- .element: class="fragment" -->

Note: Per PyCon US Guido keynote

Once 2.7 goes EOL, then projects can't be used any more.

No satisfaction in just porting it

long tail of dependencies prohibit porting

There are automated tools for this

---

# Non-Language Dependent Factors <!-- .slide: class="center" -->

Note: There's other things that could happen

---

# Google Code <!-- .slide: class="center" -->
## Read Only <!-- .element: class="fragment" -->

Note: Not accepting new projects as of January.


Read Only as of Aug 24 (Tuesday ish Australia time)

Had a few months, but now anything on there is R/O


---

# SourceForge <!-- .slide: class="center" -->

Note: VLC binaries 'abandoned', being updated w/out consent, with spyware

Also, small two week outage in there


---


# Every active project is going to need love <!-- .slide: class="center" -->


Note: 'active' meaning someone's using it, who's moving to the new structure

The maintainer may be off growing grapes

Hostile Forks Don't Help

---

# So what can you do? <!-- .slide: class="center" -->
## Abandon Responsibly <!-- .element: class="fragment" -->
## Restore Dead Code <!-- .element: class="fragment" -->

Note: If you have a project vs if you see a project

---

# Abandon Responsibly <!-- .element: style="margin-bottom: 1em" -->
## Update your README <!-- .element: class="fragment" -->
## Mark as inactive <!-- .element: class="fragment" -->
## Link to a better solution <!-- .element: class="fragment" -->
## Leave a forwarding address <!-- .element: class="fragment" -->
## Assign a new maintainer <!-- .element: class="fragment" -->

Note: Documentation is your friend

You don't want people coming across your stuff when there's something better

You really don't want people using code that has deps with known vuls

---

# GitHub Ownership Transfer <!-- .slide: class="center" -->

Note: Create a new/existing organisation

Add the admin from the otehr one in (shared rights)

Transfer 

Remove new admin

---

# Benefits <!-- .element: style="margin-bottom: 1em" -->
## All the PRs, Issues, Commits stay <!-- .element: class="fragment" -->
## 301 Redirects to new URL <!-- .element: class="fragment" -->
## You get the commit bit :D <!-- .element: class="fragment" -->


Note: the 301 is very nice, it will automatically users to the new repo based on the old URL

This may break if you attempt to overload the old namespace, however.

---


# Restore Dead Code <!-- .element: style="margin-bottom: 1em" -->
## Check their README <!-- .element: class="fragment" -->
## <img src="pictures/notdeadyet.gif"> <!-- .element: class="fragment" -->


---

# Restore Dead Code <!-- .element: style="margin-bottom: 1em" -->
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

# There's probably<br>more factors in play <!-- .slide: class="center" -->

Note: It's never just that simple.

Politics 

Friendships 

Pet Projects

---

# Go to rule:<br>There's nothing wrong<br>with being nice. <!-- .slide: class="center" -->

Note: the ability to openly communicate is one facet of opensource that makes it amazing

They've put in the effort to make a solution that's usefulness is expiring

Help make their solution timeless.

---

# Thanks! <!-- .slide: class="center" -->

<img src="pictures/footer.svg">


Note: :D