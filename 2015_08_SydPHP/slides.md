# Life After Death <!-- .slide: class="center" -->
## How to handle abandoned projects
<img src="pictures/footer.svg">

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
## Licencing <!-- .element: class="fragment" -->
## 'Competitor' Code <!-- .element: class="fragment" -->
## Dead Source <!-- .element: class="fragment" -->

---

# GitHub Forking <!-- .element: style="margin-bottom: 1em" -->
## <img src="pictures/github_forking.gif"> <!-- .element: class="fragment" -->
Note: Github's forking != Traditional Forking

---

# Limitations <!-- .element: style="margin-bottom: 1em" -->
## Parent Lock-in <!-- .element: class="fragment" -->
## Default Pull Requests <!-- .element: class="fragment" -->
## No Issue Logging <!-- .element: class="fragment" -->
## Commits Don't Count <!-- .element: class="fragment" -->

Note: Parent - perma link to source

PR - defaults to parent, accidently attempt to merge upstream

Issues - physical limitation on workflow

Commits - you can work your butt off and your green graph doesn't fill up


---


# Licencing <!-- .element: style="margin-bottom: 1em" -->
# BSD <!-- .element: class="fragment" --> <!-- .element style="font-size: 4em" --> 


---
# Licencing <!-- .element: style="margin-bottom: 1em" -->
# BSD? <!-- .element style="font-size: 4em" --> 

Note: 

"Redistribution and use in source and binary forms, with or without modification, are permitted"

well, yay! I can just have at it!

"provided that the following conditions are met: "

ah, the caveats

---

# BSD3 - Can: <!-- .element: style="margin-bottom: 1em" -->
## Commercially Use <!-- .element: class="fragment" -->
## Modifiy & Distribute <!-- .element: class="fragment" -->
## Sublicence <!-- .element: class="fragment" -->
## Place Warranty <!-- .element: class="fragment" -->
Note: Tldr - yay opensource!

---

# BSD3 - Cannot: <!-- .element: style="margin-bottom: 1em" -->
## Use Trademark <!-- .element: class="fragment" -->
## Hold Liable <!-- .element: class="fragment" -->
Note: Fair Enough

---

# BSD3 - Must: <!-- .element: style="margin-bottom: 1em" -->
## Include Copyright <!-- .element: class="fragment" -->
## <img src="pictures/awkward.gif"> <!-- .element: class="fragment" -->

---
# 'Competitor' Code <!-- .element: style="margin-bottom: 1em" -->
## &copy; Their Company 2014 <!-- .element: class="fragment" -->
## &copy; Your Company 2015 <!-- .element: class="fragment" -->

Note: having copyrights with other company's copyright is kinda a weird thing, amiright?

---

# Dead Source <!-- .element: style="margin-bottom: 1em" -->
## <img src="pictures/tumbleweed.gif"> <!-- .element: class="fragment" -->

Note: If the source upstream is dead, then that's an inhibitor of innovation

---


# So what could you do? <!-- .slide: class="center" -->
---

# Ask. <!-- .slide: class="center" --> <!-- .element style="font-size: 4em" --> 

Note: This is totally what I did. Because this happened to me. Saddest of Panda

---

# So why do you care? <!-- .slide: class="center" -->

---

# PHP 7 <!-- .slide: class="center" --> <!-- .element style="font-size: 4em" --> 

Note: PHP5 will die. PHP4 shuold already be dead.

When everyone upgrades, the old code needs to come along, or it'll be lost.



---

# Also <!-- .slide: class="center" -->

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

# Source Forge <!-- .slide: class="center" -->

Note: VLC binaries 'abandoned', being updated w/out concent, with spyware

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
## Mark as Inactive <!-- .element: class="fragment" -->
## Link to a better solution <!-- .element: class="fragment" -->
## Leave a forwarding address <!-- .element: class="fragment" -->
## Assign a New Maintainer <!-- .element: class="fragment" -->

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

---

# There's probably more factors in play <!-- .slide: class="center" -->

Note: It's never just that simple.

Politics 

Friendships 

Pet Projects

---

# Go to rule: There's nothing wrong with being nice. <!-- .slide: class="center" -->

Note: the ability to openly communicate is one facet of opensource that makes it amazing

They've put in the effort to make a solution that's usefulness is expiring

Help make their solution timeless.

---

# Thanks! <!-- .slide: class="center" -->

<img src="pictures/footer.svg">