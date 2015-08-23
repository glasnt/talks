# Life After Death <!-- .slide: class="center" -->
## How to handle abandoned projects
<img src="pictures/footer.svg">



# Hi! <!-- .slide: class="center" -->

Note: This is totally based on a true story. It happened to a friend of a friend of mine.



# &nbsp; <!-- .element: style="margin-bottom: 1em" -->




# "Just fork it!" <!-- .slide: class="center" -->
## Well, it's not that simple <!-- .element: class="fragment" -->



## GitHub Forking <!-- .slide: class="center" -->
## Licencing <!-- .element: class="fragment" -->
## 'Competitor' Code <!-- .element: class="fragment" -->
## Dead Source <!-- .element: class="fragment" -->



# GitHub Forking <!-- .element: style="margin-bottom: 1em" -->
## <img src="pictures/github_forking.gif"> <!-- .element: class="fragment" -->
Note: Github's forking != Traditional Forking




# Limitations <!-- .element: style="margin-bottom: 1em" -->
#  <!-- .element: style="margin-bottom: 1em" -->
## Parent Lock-in <!-- .element: class="fragment" -->
## Default Pull Requests <!-- .element: class="fragment" -->
## No Issue Logging <!-- .element: class="fragment" -->
## Commits Don't Count <!-- .element: class="fragment" -->

Note: Parent - perma link to source
PR - defaults to parent, accidently attempt to merge upstream
Issues - physical limitation on workflow
Commits - you can work your butt off and your green graph doesn't fill up



# Licencing <!-- .element: style="margin-bottom: 1em" -->
# BSD <!-- .element: style="margin-bottom: 1em" -->



# Licencing <!-- .element: style="margin-bottom: 1em" -->
# BSD? <!-- .element: style="margin-bottom: 1em" -->

Note: 
* "Redistribution and use in source and binary forms, with or without modification, are permitted"
 well, yay! I can just have at it! <!-- .element: class="fragment" -->
* "provided that the following conditions are met: "
 ah, the caveats <!-- .element: class="fragment" -->




# BSD3 - Can: <!-- .element: style="margin-bottom: 1em" -->
## Commercially Use <!-- .element: class="fragment" -->
## Modifiy & Distribute <!-- .element: class="fragment" -->
## Sublicence <!-- .element: class="fragment" -->
## Place Warranty <!-- .element: class="fragment" -->
Note: Tldr - yay opensource!



# BSD3 - Cannot: <!-- .element: style="margin-bottom: 1em" -->
## Use Trademark <!-- .element: class="fragment" -->
## Hold Liable <!-- .element: class="fragment" -->
Note: Fair Enough



# BSD3 - Must: <!-- .element: style="margin-bottom: 1em" -->
## Include Copyright <!-- .element: class="fragment" -->
## <img src="pictures/awkward.gif"> <!-- .element: class="fragment" -->
Note: Follows onto the next slide




# 'Competitor' Code <!-- .element: style="margin-bottom: 1em" -->
## &copy; Their Company 2014 <!-- .element: class="fragment" -->
## &copy; Your Company 2015 <!-- .element: class="fragment" -->

Note: having copyrights with other company's copyright is kinda a weird thing, amiright?




# Dead Source <!-- .element: style="margin-bottom: 1em" -->
## <img src="pictures/tumbleweed.gif"> <!-- .element: class="fragment" -->

Note: If the source upstream is dead, then that's an inhibitor of innovation




# So what could you do? <!-- .slide: class="center" -->



# Ask. <!-- .slide: class="center" --> <!-- .element style="font-size: 4em" --> 
Note: This is totally what I did. Because this happened to me. Saddest of Panda



# So what could they do? <!-- .slide: class="center" -->



# Transfer ownership <!-- .slide: class="center" -->



# Transfer ownership <!-- .element: style="margin-bottom: 1em" -->
## Create a new organisation <!-- .element: class="fragment" -->
## Add new admin <!-- .element: class="fragment" -->
## Transfer repo <!-- .element: class="fragment" -->
## Remove new admin <!-- .element: class="fragment" -->

Note: You create a new organisation

Then, you add someone w/transfer rights into your new group, as an admin

Then, they transfer the repo between two organisations that they have the rights to do so with

Then, you remove them, before they can do anything else :)





# Resulting State <!-- .element: style="margin-bottom: 1em" -->
## All the PRs, Issues, Commits stay <!-- .element: class="fragment" -->
## 301 Redirects to new URL <!-- .element: class="fragment" -->
## You get the commit bit :D <!-- .element: class="fragment" -->


Note: the 301 is very nice, it will automatically users to the new repo based on the old URL

This may break if you attempt to overload the old namespace, however.



# So why do you care? <!-- .slide: class="center" -->




# PHP 7 <!-- .slide: class="center" --> <!-- .element style="font-size: 4em" --> 




# So what can you do? <!-- .slide: class="center" -->
## Abandon Responsibly
## Restore Dead Code




# Abandon Responsibly <!-- .element: style="margin-bottom: 1em" -->
## Update your README <!-- .element: class="fragment" -->
## Mark as Inactive <!-- .element: class="fragment" -->
## Link to a better solution <!-- .element: class="fragment" -->
## Assign a New Maintainer <!-- .element: class="fragment" -->





# Restore Dead Code <!-- .element: style="margin-bottom: 1em" -->
## Check their README <!-- .element: class="fragment" -->
## <img src="pictures/notdeadyet.gif"> <!-- .element: class="fragment" -->





# Restore Dead Code <!-- .element: style="margin-bottom: 1em" -->
## Check their README
## Is it inactive? <!-- .element: class="fragment" -->
## Is there a better solution? <!-- .element: class="fragment" -->
## Can you be the new maintainer? <!-- .element: class="fragment" -->