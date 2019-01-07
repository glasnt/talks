class: bottom left
background-image: url("images/moon.jpg")
# .uber[Being kind to 3am you]
## .stpad[Katie McLaughlin<br>Docs Down Under, LCA 2019]

???

Words of encouragement here.

Hi! I'm Katie

---
class: bottom right
background-image: url("images/sleeping.jpeg")
???

And I like sleep. No really, getting a good night sleep is the best.

You know what's also really great?

Waking up when my body is done, my batteries are at 100% charged, and I can get going with the best possible start to my day.

I can get up, do a bit of exercise, get my coffee, and start my day.

I can operate to the best of my ability.

I can be productive and happy and get things done.

but when I'm tired. Oh when I'm tired..
---
class: bottom right
background-image: url("images/tired.jpeg")

???

I don't operate well when I'm tired.

Being unable to focus or see properly or think straight really inhibits my ability to be productive.

So when I get paged, especially at night, I'm tired. I'm not operating at my best.

I'm not going to be 100% there, I'm not going to be as quick thinking.

But if I'm paged, stuff be broken, yo, so I have to get it fixed.

So what I need to do is to set myself up for to be the best I can be when, not if, when, the pager goes off at 3am.


---
class: bottom right
background-image: url("images/bedlaptop.jpeg")

???

Because the 3am pager will probably happen.

Sure, you can be lucky enough to be in a place with Follow the Sun (explain, possibly with maps?)

But you probably won't be, if you're on a small team.

And it might not be an actual "3am pager", but it would be the apocryphl 3am pager.

Something is going to come by which means you'll not at your best, when you're sick, or not with it, or tired.

So these tips and tricks can help you when you're not 100%, but also you can use the time you are 100% to feedback into this system.

---
background-image: url("images/triple.jpg")

# Essentials, Next Steps, Feedback

???

I'll be splitting this up into three sections

Essentials, Next Steps, and Feedback

(Each with their own clever visuals :) )

---

class: bottom left
background-image: url("images/basics.jpg")
# The Essentials
???

so, the essential documentation.

Not yet what you need to write down, but where to write it.

You could go whole hog and do a full knowledge base and documentation management system, but that all requires buy-in and resources. Sometime, you can't get that.

And what you really want is a good night's sleep.

You just want to throw some notes down.

Places you could do this include: the wiki on your github pages, or say under your username on your Confluence page.

But, where you put these notes needs to have some important features.

---
background-image: url("images/basics.jpg")
### .big[Editable]

???

It needs to be editable. Yes, sure, but editable means something important here.

Whereever you're storing this stuff, it needs to be able to be edited easily.

You need to be able to readily add new information, and remove out of date information.

This might seem obvious, but it's such an important feature that if you are stuck with, say, having a

"documentation repo" that needs to have content approved before it can be merged, it's a huge blocker.

---
background-image: url("images/basics.jpg")
### .big[Searchable]
???

it needs to be searchable.

Paper doesn't work here. You need to have something you can Control-F at 3am, where ever you are in the world.

This is especially useful for those road warriors.

What I've also found super useful is creating a Custom Search Engine here.

Having a keyword I can throw into a new tab of by browser to search my notes wiki is so helpful.

I personally have custom search keywords for a number of services like wikipedia or twitter,

but also a keyword for my company wiki, and also one for the code store.

If I come across something new across something and it's not in one of those two places, then probably something third party and I just have to search the public internet, or worse: knowledge is either trapped inside someone's head. At 3am, this is the worst.

---
background-image: url("images/basics.jpg")
### .big[Discoverable]

???

And this is where the third tier comes in. Discoverability.

This is where the wiki excels here. Having the system being web based means that your coworkers can see it to.

And they can also use your custom search engines to find your notes, and perhaps CoLlAbOrAtE?!


But the question is, what do you write down? What do you want to be able to discover at 3am?


---
class: bottom left
background-image: url("images/knife.jpg")
# Your tools

???

Well, this is really going to depend on your environment.

Are you working in a Docker shop? Kubernetes? Lots of networking?

What would be super useful for 3am is sharpened tools. Commands with all those strange flags, more esotric actions, or inspection scripts.

Things that aren't aliased (though having these in your docs in case you forget what you have around is superuseful)

Having A copy-pastable command that does something like: show me all the loadbalancers that have high memory usage, display the docker containers with high CPU, show me the pod balance across the region.

---
class: bottom left
background-image: url("images/knife.jpg")
# Your tools

???
It really depends on your environment, but having sharpened tools are really useful.

And also remembering that when you're storing these, ensuring they're easily copy-pasteable. There's nothing worse than having those leading dollar signs or non-obvious environment variables in your stored commands that means you have to think about editing them.

And also, making sure these commands are safe. Don't put any descructive commands in these caches unless they're clearly marked as such, have big red warning signs.
---
class: bottom left
background-image: url("images/basics.jpg")
# The Essentials

???

So now that you have the initial basics, you need to think about their evolution

---
class: bottom left
background-image: url("images/step.jpg")
# Stepping Up
???

Stepping up this repository of useful hints, how can you make it work for you?

Again, your milage may vary, but I can offer advice for what I've seen work.

---
background-image: url("images/step.jpg")
### .big[Integration]

???

Integration is a big step. And so so useful.

Having your cache end up being moved into an "SRE Tips" page that appears on the home page for your rota information. Having it linked up in the channel topic of your firehouse chat channel.

Making it available and useful.

---
background-image: url("images/step.jpg")
### .bigx[Contextual Integration]

???

Another big bonus is not just linking to the cache, but having it contexual

One fleet I maintained had a lot of different machines across different operating systems and virtualisation types. Physical machines, VMware, KVM, Xen; Linux, Windows, different versions of those in between.

And depending on the service on the server that was having the issue there would be a link on the nagios alert to that particular service or server.

Which meant having a Swap alert on a Linux box would immediately show the sysadmin on call a link to the basic debugging for that service.

Or, if I'm recalling the setup properly, if there was a listing for the service specifically for that **server**, that would be shown instead. This was incredibly useful for those pesky machines that were notorious for having memory leaks or other bugbear issues.

Which brings me to another important point

---
background-image: url("images/step.jpg")

### .big[Post Mortem]

???

Post Mortems

When there is an issue, integrating some of the debugging steps that were used into the useful tips docs.

This could be something as simple as saving a copy of a santised bash history somewhere, but is so very very useful when a senior SRE can show which of those sharpened tools they used so that a junior might learn.

Which, in itself, brings me to the third major point.

---
class: bottom left
background-image: url("images/laptop-angle-small.jpg")
# Feedback Loop

???

the feedback loop.

These caches don't just appear overnight. They evolve over time, as they are used, and are useful, for those on call .

Having a cache of the flags on an essoteric CLI is one thing, but having a well oiled bag of tricks is another.


---
background-image: url("images/laptop-angle-small.jpg")
### .big[Recurring Issues]

???
Especially with recurring issues.

Now, this is different from one off things, and I want to focus on this for a moment.

In an ideal world, no issue should happen more than once, because, hey, all problems are immediately fixed by the on-call engineer and will never happen again, right?

For anyone whos done ops or any period of time (or dev, for that matter_, you know there's always a compromise between work arounds and fixes.

That server that keeps alerting due to critical disk space usage? Is it easier to occasionally clean up the old webserver logs, or setup a scheduled task that archives logs older than a week? Or also deletes those older than a month?

The engineering time to create such a script that's appropriate for the environment is non-trivial if it doesn't already exist, especially when considerations like data retention or GDPR come involved that affect the implementation.

So, sometimes it's easier to, say, change monitoring to soft-alert at, say, a 10% diskspace free level so an engineer can cleanup things during the day, as opposed to waking up the engineer at 3am with a critical 5% free alert that would have the same action.

Tuning alerts and actions for recurring events is absolutely valid, even in cases where "Yes, we'll fix that Soon".


---
background-image: url("images/laptop-angle-small.jpg")
### .big[Automation]

???

You can even start applying automations to these manual functions.

Something simple like adding a for loop to the start of a command to apply it to many servers.

Or making that for loop smarter by turning it into an ansible playbook that can check for things on the servers before applying commands.

Taking the commands in your bag of tricks and turning them into cronjobs, or such.


Again, it's going to depend on your environment, both machine and people.

But in all of this, the biggest thing that I can suggest -
---
background-image: url("images/laptop-angle-small.jpg")

### .big[Learning]

???

turn this into a learning oppourtinuty for the members of your team.

This feeds back into the discoverability and feedback loop steps, but making sure that juniors or other team members "learn the weather".

I'm the first speaker today, so there are other talks in this miniconf that will deal with this, so I'll just handwave here.

Again, depending on your setup, if you have a junior that's starting to shadow, showing them the iffy machines; giving them a chance to debug things themselves, but working with them to solve issues in a timely manner.


But making sure that any of those "We'll fix that soon" are noted. This is so so important so that people know what to expect.

And when you finally get to fixing things, please make sure you communicate this.

---
background-image: url("images/laptop-angle-small.jpg")

### .big[Flag change]

???

While it might be great that things finally get fixed, that those alerts go away, I've been here long enough to know it's not always that simple.

Infra changes almost always cause other issues down the line. Make sure you communicate these with your team, and in your cache.

Especailly if any of your cool scripts get deprecated.

And, bonus points: especailly if you're lucky enough to be on a distributed team, if you're going to be personally make big changes that might have the slightest change of raising alerts, please take the pager.

Especially if it's your workday, and you're not already on call.

---
class: bottom right
background-image: url("images/empathy.jpg")
# Empathy

???

And a small sidenote here:

Showing empathy for your fellow engineer who is going to be thankful for that full night sleep is paid back in kind.

Showing self-care by giving yourself the tools to help you get your job done so you can go back to counting sheep.

Making sure your junior or new on call engineers don't freak out in the middle of the night because you left them a note about that upgrade, so those new errors they're seeing are totally okay (well, not okay, but not unexpected)

Working in a team is hard, but as soon as you start expecting work out of hours, especially when on-call is involved, practicing explicit empathy makes things so much easier for everyone involved.

---
class: bottom right
background-image: url("images/blank-small.jpg")
# Get started now

???

you're not your best when you're tired, but you'll do your future self a favour and starting your bag of tricks today.

A bashhistory, an odd command here and there, just start somewhere. Evolve it, and it'll help you on those early morning calls so you can get back to sleep.


---
class: bottom left
background-image: url("images/moon.jpg")
class: title
# <br><br>Thanks!

.footnotes[Images from: Unsplash, WOCinTech]
???

thank you for your time