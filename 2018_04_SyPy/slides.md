<br> 
# ORM: The Sequel <!-- .slide: class="center" -->
### SyPy April 2018 <!-- .slide: class="center" -->
 <img src="pictures/footer.svg" />
---
# ⚠️ <!-- .slide: class="center" -->

Note: Before I start a word of warning
---
 <div style='margin: 0 auto;'><p align='center'><img src='pictures/dceu18.png'></p></div>  <!-- .slide: class="center" -->
&nbsp; <!-- .slide: data-background-color="#f58619" -->
<div style="-webkit-transform: rotate(-29deg);color: black;font-size: 124pt;margin-top: -400px; margin-left: 400px;z-index:100;"><b>&nbsp; .</b></div> <!-- .slide: data-background-color="#f58619" -->
Note: 
This talk is being presented next month at DjangoCon Europe

---
 <div style='margin: 0 auto;'><p align='center'><img src='pictures/dceu18.png'></p></div>  <!-- .slide: class="center" -->
&nbsp; <!-- .slide: data-background-color="#f58619" -->
<div style="-webkit-transform: rotate(-29deg);color: red;font-size: 124pt;margin-top: -400px; margin-left: 400px;z-index:100;"><b>DRAFT</b></div> <!-- .slide: data-background-color="#f58619" -->
Note: 

this talk is a work in progress.

If you find any technical errors, or issues, please tell me **after** the talk. I"ll have my twitter and email at the end

Now, with that out of the way

*cough*. :center self:
---
 <div style='width: 50%; margin: 0 auto;'><p align='center'><img height='400px' src='pictures/wave.svg'></p></div> <!-- .slide: class="center" -->

Note: Hi I'm Katie
---
 <div style='margin: 0 auto;'><p align='center'><img src='pictures/djangologo.png'></p></div>  <!-- .slide: class="center" -->

Note: And I do a bunch of things in the Django community
---
 <div style='margin: 0 auto;'><p align='center'><img src='pictures/dceu16.png'></p></div>  <!-- .slide: class="center" -->
&nbsp; <!-- .slide: data-background-color="#302613" -->
Note: I spoke at DjangoCon Europe 16 in Budapest
---
 <div style='margin: 0 auto;'><p align='center'><img src='pictures/dcus17.png'></p></div>  <!-- .slide: class="center" -->
&nbsp; <!-- .slide: data-background-color="#c2eaf4" -->
Note: I was a mentor, and also gave a talk, at DjangoCon US 2017
---
 <!-- .slide: data-background-image="pictures/17_bg.png"-->
 <div style='margin: 0 auto;'><p align='center'><img src='pictures/dcau17.png'></p></div>  <!-- .slide: class="center" -->
Note: I was the organiser of djangocon australia 17
---
 <div style='margin: 0 auto;'><p align='center'><img src='pictures/djangologo.png'></p></div>  <!-- .slide: class="center" -->
Note: I'm currently serving as a Director of the Django Software Foundation
---
# &nbsp; <!-- .slide: class="center" -->

Note: But I'm an absolute novice at django. I have no idea what I'm doing
---
 <div style='margin: 0 auto;'><p align='center'><img src='pictures/djadmin.png'></p></div>  <!-- .slide: class="center" -->
Note: I still see the django admin as

---
 <div style='margin: 0 auto;'><p align='center'><img src='pictures/djadmin_sparkles.png'></p></div>  <!-- .slide: class="center" -->
Note: a magical piece of software development
---
 <div style='margin: 0 auto;'><p align='center'><img src='pictures/djuser_super.png'></p></div>  <!-- .slide: class="center" -->

Note: I mean, the fact that this admin is just generated based on something called models..?

and it just works, it's so cool


---
 <!-- .slide: data-background-image="pictures/macbook.jpg"-->
Note: But just because I'm a novice at django, doesn't mean I'm a novice at tech
---
 <!-- .slide: data-background-image="pictures/thinkpad.jpg"-->
Note: I have over a decade of software development and systems administration behind me.

Before getting into the Python/Django space, I was a ruby dev, working with Rails and Sinatra stacks

But before that, around the time the magic was being removed from Django, I was in my first tech job, and using my first tech stack:

---
 <div style='margin: 0 auto;'><p align='center'><img src='pictures/apexlogo.png'></p></div>  <!-- .slide: class="center" -->
&nbsp; <!-- .slide: data-background-color="#f8f8f8" -->

Note: Was Orale Application Express

Oracle Appplication express, also known as Apex, is a in-database web application creation suite. it comes free with Oracle XE (the free version of the database)
---
<img src="pictures/apex_window.png" style="margin-top: -50px; margin-left: -115px; max-width: 125%">

 <span class='foot'>[StackOverflow](https://stackoverflow.com/questions/48789457/oracle-apex-version-3-2-tabindex-not-working)</span>

Note: Back in 2006, this was the bees knees. An entire web GUI way to build a website based on form submissions and database manpulations. I used this for years
---
 <!-- .slide: data-background-image="pictures/apex32.jpg"-->
Note: So much so, I was a technical reviewer for a technical book on the subject.

Yes, I'm that much of a nerd.
---

# &nbsp; <!-- .slide: class="center" -->

Note: I haven't used APEX for years. But, there's one thing that I have an intrinstic knowledge of

---

 <h1 style="color: white;text-shadow: 1px 1px 6px black, 0 0 136px red, 0 0 51px yellow; font-family: arial; font-size: 200pt">SQL</h1> <!-- .slide: class="center" -->
 <h1 style="color: white;text-shadow: 1px 1px 6px black, 0 0 136px red, 0 0 51px yellow; font-family: arial; font-size:40pt">Structured Query Language</h1> <!-- .slide: class="center" -->

Note: SQL

It's like riding a bike. Left outer joins are always going to be a bit.. fuzzy, but I can't count the amount of times I wished there was an option of throwing a LIKE clause on search results.


---
 <div style='margin: 0 auto;'><p align='center'><img src='pictures/djadmin.png'></p></div>  <!-- .slide: class="center" -->
Note: Getting back to Django.

I'm still getting my head around how Django works

I mean, sure, for a sufficiently setup existing django application, the admin makes things so intuitive.

But if you were to try and tell me how things work underneath

---
 <!-- .slide: data-background-image="pictures/fogofwar.png"-->

Note: I would have some sort of fog of war thing going on. I can't tell what's going on.
---
## > *"Oh, just use the shell!"* <!-- .slide: class="center" -->
Note: Even worse when I'm told "Oh, just use the shell"

It's an empty space. But I've been told that this is where the actual Django magic lives
---
 <h1 style="color: white;text-shadow: 1px 1px 6px black, 0 0 136px blue, 0 0 51px green; font-family: arial; font-size: 200pt">ORM</h1> <!-- .slide: class="center" -->

 <h1 style="color: white;text-shadow: 1px 1px 6px black, 0 0 136px blue, 0 0 51px green; font-family: arial; font-size: 40pt">Object Relational Mapper</h1> <!-- .slide: class="center" -->
Note: The ORM

The Object relational mapper

The engine that makes django go

But without context, what does that even mean?
---
# Context <!-- .slide: class="center" -->

Note: Context is important.

So for the purposes of this, let's break away from the normal.

A number of tutorials start with a clean slate, and assume you have little to know dev experience. DjangoGirls is great for complete beginners to development

But it's not so helpful for developers who come into the space with prior knowledge

It's also not helpful for the way that I came into Django; trying to fix an existing project

So for the purposes of this, we're going to use an existing project
---
 <!-- .slide: data-background-image="pictures/hunterbird.jpg"-->

Note: 

We're going to be a noisy myna, and go bughunting.

We're going to find outselves an existing project, in this case, a field of kale, and hunt about trying to find some delicious bugs. We may not find any, but we can poke around and see what we find.
---
# Context <!-- .slide: class="center" -->

Note: so, our context today isn't going to be the standard blog site or news portal.

It's going to be about something near and dear to my heart
---
# ✨ <!-- .slide: class="center" -->
Note: emoji
---
 <img src="pictures/unicodex_index.png" style="margin-top: -50px" />

Note: 

If you've seen my {DjangoCon EU 2016 talk,emoji talks before}

this website would be sort of familiar to you.

I call it.. Unicodex. It's a django-backed database of different emoji from different platforms

On the home page there's a bunch of emoji and if you click on one

---

 <img src="pictures/unicodex_sparkles.png" style="margin-top: -50px" />

Note: it shows you the emoji from different vendors and the versions.

So given this website exists, we can start poking around in the shell
---
## "Just use the shell" <!-- .slide: class="center" -->
Note: what they mean here is the django shell
---
 <div class="shell-wrap"><p class="shell-top-bar">bash</p><p class="shell-body">
 <ps>myrtle</ps> <dr>~ $</dr> 
cd project<br>
 <ps>myrtle</ps> <dr>~/project $</dr> 
 ./manage.py shell<w>&nbsp;</w>

Note: which is available using the manage.py shell command
---
 <div class="shell-wrap"><p class="shell-top-bar">python3.6</p><p class="shell-body">
 <ps>myrtle</ps> <dr>~ $</dr> 
cd project<br>
 <ps>myrtle</ps> <dr>~/project $</dr> 
./manage.py shell<br>
Python 3.6.3 (default, Nov 9 2017, 15:58:30)<br>
[GCC 4.2.1 Compatible Apple LLVM 9.0.0 (clang-900.0.38)] on darwin<br>
Type "help", "copyright", "credits" or "license" for more information.<br>
(InteractiveConsole)<br> 
 &gt;&gt;&gt;&nbsp;<w>&nbsp;</w>

Note: 

Here, we're presented with an interactive console

All shell is is a python environment where the django environment path has been loaded.

From here you can interact with your django projet directly.

---
## "But, how do I use the shell?" <!-- .slide: class="center" -->
## *"..."* <!-- .element: class="fragment" -->

Note: but how do I use the shell

First things first. For an SQL dev, the first thing they normally do in a foreign system is
---
## Finding all tables <!-- .slide: class="center" -->
---
<pre><code><c>&dash;&dash; MySQL</c>
show tables

<c>&dash;&dash; PostgreSQL</c>
\dt 

<c>&dash;&dash; Oracle</c>
<r>SELECT * <br>&nbsp; FROM</r> <l>dba</l>.<l>tables</l>
</code></pre> 

Note: depending on which flavour of database is most familiar to you, you'd try and issue one of these commands

For mysql, for postgres, for oracle

But we're not in a database console, we're in the django shell. We need to use ORM codes.


---
<pre><code><c>&num; ORM</c>
<c>&num; ...</c>

Note: SO! To list all the tables in a project in the django shell!...

there's no real good way.

In order to start querying model objects, you need to import the models

In django, a project has multiple applications, or apps, and an app can have one or many models.

The model code is the powerhouse of django. the ORM manipulates models. A lot of the logic for a django project is going to be in the model.py of it's various applications.
But without looking at the model code, and understanding what you're looking at in order to generate the import statement, you can be at a complete loss.

Thankfully, django is clever and has helpful methods you can call to generate a list of imports for all the models in the project
---
<pre><code><c># Generate import statements</c>
<r>from</r> django.apps <r>import</r> apps
&nbsp; 
<r>for</r> app_config <r>in</r> apps.get_app_configs():
&nbsp; l <r>=</r> app_config.label
&nbsp; <r>for</r> model <r>in</r> app_config.get_models():
&nbsp; &nbsp; n <r>=</r> model._meta.object_name
&nbsp; &nbsp; <l>print</l>(<d>f'from</d> <l>{</l>l<l>}</l><d>.models import </d><l>{</l>n<l>}</l>')
</code></pre> 

Note: here's some I prepared earlier

We're going to import the django apps

And iterate over all the apps that django knows about

For each of those, we're going to get all the models

and print an import statement for each

---
 <div class="shell-wrap"><p class="shell-top-bar">python3.6</p><p class="shell-body">
 <ps>myrtle</ps> <dr>~/project $</dr> 
./manage.py shell<br>
Python 3.6.3 (default, Nov 9 2017, 15:58:30)<br>
[GCC 4.2.1 Compatible Apple LLVM 9.0.0 (clang-900.0.38)] on darwin<br>
Type "help", "copyright", "credits" or "license" for more information.<br>
(InteractiveConsole)<br> 
 &gt;&gt;&gt;&nbsp;<w>&nbsp;</w>

Note: Going back to our shell
---
 <div class="shell-wrap"><p class="shell-top-bar">python3.6</p><p class="shell-body">
 <ps>myrtle</ps> <dr>~/project $</dr> 
./manage.py shell<br>
Python 3.6.3 (default, Nov 9 2017, 15:58:30)<br>
[GCC 4.2.1 Compatible Apple LLVM 9.0.0 (clang-900.0.38)] on darwin<br>
Type "help", "copyright", "credits" or "license" for more information.<br>
(InteractiveConsole)<br> 
&gt;&gt;&gt; from django.apps import apps<br>
&gt;&gt;&gt; for app_config in apps.get_app_configs():<br>
...&nbsp; l = app_config.label<br>
...&nbsp; for model in app_config.get_models():<br>
...&nbsp; &nbsp; n = model._meta.object_name<br>
...&nbsp; &nbsp; print(f'from {l}.models import {n}')<br>
 ...&nbsp;<w>&nbsp;</w>

Note: for now, we're just going to dump in that code and run it
---
 <div class="shell-wrap"><p class="shell-top-bar">python3.6</p><p class="shell-body">
...&nbsp; l = app_config.label<br>
...&nbsp; for model in app_config.get_models():<br>
...&nbsp; &nbsp; n = model._meta.object_name<br>
...&nbsp; &nbsp; print(f'from {l}.models import {n}')<br>
...&nbsp;<br> 
from auth.models import Permission<br>
from auth.models import Group<br>
from auth.models import User<br>
from contenttypes.models import ContentType<br>
from sessions.models import Session<br>
from sites.models import Site<br>
from aldryn_sso.models import AldrynCloudUser<br>
from admin.models import LogEntry<br>
from unicodex.models import Codepoint<br>
from unicodex.models import Vendor<br>
from unicodex.models import VendorVersion<br>
from unicodex.models import Design<br>
 &gt;&gt;&gt;&nbsp;<w>&nbsp;</w>

Note: and what we get back is some generated import statements about

This output will have similarities across django projects

the first few in this list are pretty standard fair; authentication, sessions, sites, admin

But what we're looking for is, in a lovely happenstance, the models that match the name of the website we saw earlier -- unicodex.
---

## Finding the table for a model <!-- .slide: class="center" -->
---
<pre><code> 
<c># ORM</c>
Codepoint._meta.db_table 
</code></pre> 
---
 <div class="shell-wrap"><p class="shell-top-bar">python3.6</p><p class="shell-body">
 <ps>myrtle</ps> <dr>~/project $</dr> 
./manage.py shell<br>
Python 3.6.3 (default, Nov 9 2017, 15:58:30)<br>
[GCC 4.2.1 Compatible Apple LLVM 9.0.0 (clang-900.0.38)] on darwin<br>
Type "help", "copyright", "credits" or "license" for more information.<br>
(InteractiveConsole)<br> 
 &gt;&gt;&gt; <w>&nbsp;</w>
---
 <div class="shell-wrap"><p class="shell-top-bar">python3.6</p><p class="shell-body">
 <ps>myrtle</ps> <dr>~/project $</dr> 
./manage.py shell<br>
Python 3.6.3 (default, Nov 9 2017, 15:58:30)<br>
[GCC 4.2.1 Compatible Apple LLVM 9.0.0 (clang-900.0.38)] on darwin<br>
Type "help", "copyright", "credits" or "license" for more information.<br>
(InteractiveConsole)<br> 
 &gt;&gt;&gt; from unicodex.models import Codepoint<w>&nbsp;</w>
---
 <div class="shell-wrap"><p class="shell-top-bar">python3.6</p><p class="shell-body">
 <ps>myrtle</ps> <dr>~/project $</dr> 
./manage.py shell<br>
Python 3.6.3 (default, Nov 9 2017, 15:58:30)<br>
[GCC 4.2.1 Compatible Apple LLVM 9.0.0 (clang-900.0.38)] on darwin<br>
Type "help", "copyright", "credits" or "license" for more information.<br>
(InteractiveConsole)<br> 
 &gt;&gt;&gt; from unicodex.models import Codepoint<br>
 &gt;&gt;&gt; <w>&nbsp;</w>
---
 <div class="shell-wrap"><p class="shell-top-bar">python3.6</p><p class="shell-body">
 <ps>myrtle</ps> <dr>~/project $</dr> 
./manage.py shell<br>
Python 3.6.3 (default, Nov 9 2017, 15:58:30)<br>
[GCC 4.2.1 Compatible Apple LLVM 9.0.0 (clang-900.0.38)] on darwin<br>
Type "help", "copyright", "credits" or "license" for more information.<br>
(InteractiveConsole)<br> 
 &gt;&gt;&gt; from unicodex.models import Codepoint<br>
 &gt;&gt;&gt; Codepoint._meta.db_table<w>&nbsp;</w>
---
 <div class="shell-wrap"><p class="shell-top-bar">python3.6</p><p class="shell-body">
 <ps>myrtle</ps> <dr>~/project $</dr> 
./manage.py shell<br>
Python 3.6.3 (default, Nov 9 2017, 15:58:30)<br>
[GCC 4.2.1 Compatible Apple LLVM 9.0.0 (clang-900.0.38)] on darwin<br>
Type "help", "copyright", "credits" or "license" for more information.<br>
(InteractiveConsole)<br> 
 &gt;&gt;&gt; from unicodex.models import Codepoint<br>
 &gt;&gt;&gt; Codepoint._meta.db_table<br>
'unicodex_codepoint'<br> 
 &gt;&gt;&gt; <w>&nbsp;</w>
---
## Showing all table columns <!-- .slide: class="center" -->
---
<pre><code><br><c># ORM</c><br>Codepoint._meta.get_fields()
---
 <div class="shell-wrap"><p class="shell-top-bar">python3.6</p><p class="shell-body">
 <ps>myrtle</ps> <dr>~/project $</dr> 
./manage.py shell<br>
Python 3.6.3 (default, Nov 9 2017, 15:58:30)<br>
[GCC 4.2.1 Compatible Apple LLVM 9.0.0 (clang-900.0.38)] on darwin<br>
Type "help", "copyright", "credits" or "license" for more information.<br>
(InteractiveConsole)<br> 
 &gt;&gt;&gt; from unicodex.models import Codepoint<br>
 &gt;&gt;&gt; Codepoint._meta.db_table<br>
'unicodex_codepoint'<br> 
 &gt;&gt;&gt; Codepoint._meta.get_fields()<w>&nbsp;</w>
---
 <div class="shell-wrap"><p class="shell-top-bar">python3.6</p><p class="shell-body">
 <ps>myrtle</ps> <dr>~/project $</dr> 
./manage.py shell<br>
Python 3.6.3 (default, Nov 9 2017, 15:58:30)<br>
[GCC 4.2.1 Compatible Apple LLVM 9.0.0 (clang-900.0.38)] on darwin<br>
Type "help", "copyright", "credits" or "license" for more information.<br>
(InteractiveConsole)<br> 
 &gt;&gt;&gt; from unicodex.models import Codepoint<br>
 &gt;&gt;&gt; Codepoint._meta.db_table<br>
'unicodex_codepoint'<br> 
 &gt;&gt;&gt; Codepoint._meta.get_fields()<br>
(&lt;ManyToOneRel: unicodex.design>, <br>
&lt;django.db.models.fields.AutoField: id>, <br>
&lt;django.db.models.fields.CharField: name>, <br>
&lt;django.db.models.fields.TextField: description>,<br>
&lt;django.db.models.fields.CharField: codepoint>)<br>
 &gt;&gt;&gt; <w>&nbsp;</w>
---
## Finding all tables <!-- .slide: class="center" -->
### via the database

Note: We can find all this information directly via the database,

and django provides an easy way to get there
---
 <div class="shell-wrap"><p class="shell-top-bar">bash</p><p class="shell-body">
 <ps>myrtle</ps> <dr>~/project $</dr> 
 ./manage.py dbshell<w>&nbsp;</w>

Note: back in our terminal, instead of running manage.py shell, we run DB shell
---
 <div class="shell-wrap"><p class="shell-top-bar">psql</p><p class="shell-body">
 <ps>myrtle</ps> <dr>~/project $</dr> 
./manage.py dbshell<br>
psql (9.6.5, server 9.6.8)<br>
Type "help" for help.<br>
<br> 
 db=#&nbsp;<w>&nbsp;</w>

Note: and we get an output that will be familiar to postgres devs in the audience

This particular project has a postgres backend
---
 <div class="shell-wrap"><p class="shell-top-bar">psql</p><p class="shell-body">
 <ps>myrtle</ps> <dr>~/project $</dr> 
./manage.py dbshell<br>
psql (9.6.5, server 9.6.8)<br>
Type "help" for help.<br>
<br> 
 db=# \dt<w>&nbsp;</w>

Note: given we know it's postgres, we cna issue the postgres list table command, and get back
---
 <div class="shell-wrap"><p class="shell-top-bar">psql</p><p class="shell-body">
&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; List of relations<br>
&nbsp;Schema |&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; Name&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; | Type&nbsp; |&nbsp; Owner<br>
&dash;&dash;&dash;&dash;&dash;&dash;&dash;&dash;+&dash;&dash;&dash;&dash;&dash;&dash;&dash;&dash;&dash;&dash;&dash;&dash;&dash;&dash;&dash;&dash;&dash;&dash;&dash;&dash;&dash;&dash;&dash;&dash;&dash;&dash;&dash;&dash;+&dash;&dash;&dash;&dash;&dash;&dash;&dash;+&dash;&dash;&dash;&dash;&dash;&dash;&dash;&dash;&dash;&dash;<br> 
&nbsp;public | aldryn_sso_aldrynclouduser | table | postgres<br>
&nbsp;public | auth_group&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;&nbsp; | table | postgres<br>
&nbsp;public | auth_group_permissions&nbsp; &nbsp; &nbsp;| table | postgres<br>
&nbsp;public | auth_permission&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; | table | postgres<br>
&nbsp;public | auth_user&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; | table | postgres<br>
&nbsp;public | auth_user_groups&nbsp; &nbsp; &nbsp; &nbsp;&nbsp; &nbsp; | table | postgres<br>
&nbsp;public | auth_user_user_permissions | table | postgres<br>
&nbsp;public | django_admin_log&nbsp; &nbsp;&nbsp; &nbsp; &nbsp; &nbsp; | table | postgres<br>
&nbsp;public | django_content_type&nbsp; &nbsp; &nbsp; &nbsp; | table | postgres<br>
&nbsp;public&nbsp;|&nbsp;django_migrations&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|&nbsp;table&nbsp;|&nbsp;postgres<br. 
&nbsp;public&nbsp;|&nbsp;django_session&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|&nbsp;table&nbsp;|&nbsp;postgres<br> 
&nbsp;public&nbsp;|&nbsp;django_site&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|&nbsp;table&nbsp;|&nbsp;postgres<br> 
&nbsp;public&nbsp;|&nbsp;unicodex_codepoint&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|&nbsp;table&nbsp;|&nbsp;postgres<br> 
&nbsp;public&nbsp;|&nbsp;unicodex_design&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|&nbsp;table&nbsp;|&nbsp;postgres<br> 
&nbsp;public&nbsp;|&nbsp;unicodex_vendor&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|&nbsp;table&nbsp;|&nbsp;postgres<br> 
&dash;&dash;More&dash;&dash; 

Note: all our tables. Note the usual suspects from earlier, auth, content, sites
---
 <div class="shell-wrap"><p class="shell-top-bar">psql</p><p class="shell-body">
&nbsp;public | aldryn_sso_aldrynclouduser | table | postgres<br>
&nbsp;public | auth_group&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;&nbsp; | table | postgres<br>
&nbsp;public | auth_group_permissions&nbsp; &nbsp; &nbsp;| table | postgres<br>
&nbsp;public | auth_permission&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; | table | postgres<br>
&nbsp;public | auth_user&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; | table | postgres<br>
&nbsp;public | auth_user_groups&nbsp; &nbsp; &nbsp; &nbsp;&nbsp; &nbsp; | table | postgres<br>
&nbsp;public | auth_user_user_permissions | table | postgres<br>
&nbsp;public | django_admin_log&nbsp; &nbsp;&nbsp; &nbsp; &nbsp; &nbsp; | table | postgres<br>
&nbsp;public | django_content_type&nbsp; &nbsp; &nbsp; &nbsp; | table | postgres<br>
&nbsp;public&nbsp;|&nbsp;django_migrations&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|&nbsp;table&nbsp;|&nbsp;postgres<br. 
&nbsp;public&nbsp;|&nbsp;django_session&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|&nbsp;table&nbsp;|&nbsp;postgres<br> 
&nbsp;public&nbsp;|&nbsp;django_site&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|&nbsp;table&nbsp;|&nbsp;postgres<br> 
&nbsp;public&nbsp;|&nbsp;unicodex_codepoint&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|&nbsp;table&nbsp;|&nbsp;postgres<br> 
&nbsp;public&nbsp;|&nbsp;unicodex_design&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|&nbsp;table&nbsp;|&nbsp;postgres<br> 
&nbsp;public&nbsp;|&nbsp;unicodex_vendor&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|&nbsp;table&nbsp;|&nbsp;postgres<br> 
&nbsp;public&nbsp;|&nbsp;unicodex_vendorversion&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|&nbsp;table&nbsp;|&nbsp;postgres<br> 
(16 rows)<br>
<br> 
 db=#&nbsp;<w>&nbsp;</w>

Note: but also, our own project's tables

We'll take note of these for later.
---
## Show all table contents <!-- .slide: class="center" -->

Note: so now that we know there are tables, we'd like to see what's inside them
---
<pre><code> 
<c>&dash;&dash; SQL</c>
<r>SELECT * <br>&nbsp; FROM</r> <l>unicodex_codepoint;</l>
<br><br> 
</code></pre> 

Note: in SQL, this would be your standard select star from table
---
<pre><code> 
<c>&dash;&dash; SQL</c>
<r>SELECT * <br>&nbsp; FROM</r> <l>unicodex_codepoint;</l>

<c>&num; ORM</c>
Codepoint.objects.all() 
</code></pre> 

Note: in the oRM, this maps to Codepoint, the model, dot objects dot all

Just list all of them
---
 <div class="shell-wrap"><p class="shell-top-bar">python3.6</p><p class="shell-body">
 <ps>myrtle</ps> <dr>~/project $</dr> 
./manage.py shell<br>
Python 3.6.3 (default, Nov 9 2017, 15:58:30)<br>
[GCC 4.2.1 Compatible Apple LLVM 9.0.0 (clang-900.0.38)] on darwin<br>
Type "help", "copyright", "credits" or "license" for more information.<br>
(InteractiveConsole)<br> 
 &gt;&gt;&gt; <w>&nbsp;</w>
Note: back over in our console, before we can call Codepoint, we need to use that import statement we generated earlier
---
 <div class="shell-wrap"><p class="shell-top-bar">python3.6</p><p class="shell-body">
 <ps>myrtle</ps> <dr>~/project $</dr> 
./manage.py shell<br>
Python 3.6.3 (default, Nov 9 2017, 15:58:30)<br>
[GCC 4.2.1 Compatible Apple LLVM 9.0.0 (clang-900.0.38)] on darwin<br>
Type "help", "copyright", "credits" or "license" for more information.<br>
(InteractiveConsole)<br> 
 &gt;&gt;&gt; from unicodex.models import Codepoint<w>&nbsp;</w>

Note: from unicodex dot models import codepoint
---
 <div class="shell-wrap"><p class="shell-top-bar">python3.6</p><p class="shell-body">
 <ps>myrtle</ps> <dr>~/project $</dr> 
./manage.py shell<br>
Python 3.6.3 (default, Nov 9 2017, 15:58:30)<br>
[GCC 4.2.1 Compatible Apple LLVM 9.0.0 (clang-900.0.38)] on darwin<br>
Type "help", "copyright", "credits" or "license" for more information.<br>
(InteractiveConsole)<br> 
 &gt;&gt;&gt; from unicodex.models import Codepoint<br>
 &gt;&gt;&gt; <w>&nbsp;</w>

Note: after we hit enter, we'll get no output, which is good, because this was successfully imported.
---
 <div class="shell-wrap"><p class="shell-top-bar">python3.6</p><p class="shell-body">
 <ps>myrtle</ps> <dr>~/project $</dr> 
./manage.py shell<br>
Python 3.6.3 (default, Nov 9 2017, 15:58:30)<br>
[GCC 4.2.1 Compatible Apple LLVM 9.0.0 (clang-900.0.38)] on darwin<br>
Type "help", "copyright", "credits" or "license" for more information.<br>
(InteractiveConsole)<br> 
 &gt;&gt;&gt; from unicodex.models import Codepoint<br>
 &gt;&gt;&gt; Codepoint.objects.all()<w>&nbsp;</w>

Note: then we make our codepoint dot objects dot all call
---
 <div class="shell-wrap"><p class="shell-top-bar">python3.6</p><p class="shell-body">
 <ps>myrtle</ps> <dr>~/project $</dr> 
./manage.py shell<br>
Python 3.6.3 (default, Nov 9 2017, 15:58:30)<br>
[GCC 4.2.1 Compatible Apple LLVM 9.0.0 (clang-900.0.38)] on darwin<br>
Type "help", "copyright", "credits" or "license" for more information.<br>
(InteractiveConsole)<br> 
 &gt;&gt;&gt; from unicodex.models import Codepoint<br>
 &gt;&gt;&gt; Codepoint.objects.all()<br>
&lt;QuerySet [&lt;Codepoint: Sparkles>, &lt;Codepoint: Unicorn>, &lt;Codepoint: Two Hearts>]><br>
 &gt;&gt;&gt; <w>&nbsp;</w>

Note: and we get back a queryset of objects

We remember from earlier that there were sparkles, unicorns and hearts on our page, so we're getting the right data!

The return value here is known as a queryset, an unordered objects. QuerySets can be enacted upon further, which we'll see later.


**Query set is not a list**

---
## Show specific table contents <!-- .slide: class="center" -->

Note: now that we can see all the things, how about just some of the things
---
<pre><code> 
<c>&dash;&dash; SQL</c>
<r>SELECT * <br>&nbsp; FROM</r> <l>unicodex_codepoint c</l><br>&nbsp;<r>WHERE</r> <l>c</l>.<l>name</l> <r>=</r> 'Sparkles';
<br><br> 
</code></pre> 

Note: the SQL would be familiar

Adding a where clause for, say, sparkles
---
<pre><code> 
<c>&dash;&dash; SQL</c>
<r>SELECT * <br>&nbsp; FROM</r> <l>unicodex_codepoint c</l><br>&nbsp;<r>WHERE</r> <l>c</l>.<l>name</l> <r>&equals;</r> 'Sparkles';

<c>&num; ORM</c>
Codepoint.objects.filter(<o>name&equals;</o>'Sparkles') 
</code></pre> 

Note: this maps to the ORM as filter. where the name column is a keyword argument of filter.


---
 <div class="shell-wrap"><p class="shell-top-bar">python3.6</p><p class="shell-body">
 &gt;&gt;&gt; from unicodex.models import Codepoint<br>
 &gt;&gt;&gt; Codepoint.objects.filter(name='Sparkles')<w>&nbsp;</w>

Note: so in our fresh terminal, we import Codepoint

Then run our filter
---
 <div class="shell-wrap"><p class="shell-top-bar">python3.6</p><p class="shell-body">
 &gt;&gt;&gt; from unicodex.models import Codepoint<br>
 &gt;&gt;&gt; Codepoint.objects.filter(name='Sparkles')<br>
&lt;QuerySet [&lt;Codepoint: Sparkles>]><br>
 &gt;&gt;&gt; <w>&nbsp;</w>
Note: and we get back a queryset with a single object: sparkles
---
## Get specific record <!-- .slide: class="center" -->

Note: we can also just return one specific record, instead of a queryset
---
 <div class="shell-wrap"><p class="shell-top-bar">python3.6</p><p class="shell-body">
 &gt;&gt;&gt; from unicodex.models import Codepoint<br>
 &gt;&gt;&gt; Codepoint.objects.filter(name='Sparkles')<br>
&lt;QuerySet [&lt;Codepoint: Sparkles>]><br>
 &gt;&gt;&gt; Codepoint.objects.get(name='Sparkles')<w>&nbsp;</w>
Note: so where last time we used filter

This time we use get
---
 <div class="shell-wrap"><p class="shell-top-bar">python3.6</p><p class="shell-body">
 &gt;&gt;&gt; from unicodex.models import Codepoint<br>
 &gt;&gt;&gt; Codepoint.objects.filter(name='Sparkles')<br>
&lt;QuerySet [&lt;Codepoint: Sparkles>]><br>
 &gt;&gt;&gt; Codepoint.objects.get(name='Sparkles')<br>
&lt;Codepoint: Sparkles><br>
 &gt;&gt;&gt; <w>&nbsp;</w>

Note: and we get a single object
---
 <div class="shell-wrap"><p class="shell-top-bar">python3.6</p><p class="shell-body">
 &gt;&gt;&gt; from unicodex.models import Codepoint<br>
 &gt;&gt;&gt; Codepoint.objects.filter(name='Sparkles')<br>
&lt;QuerySet [&lt;Codepoint: Sparkles>]><br>
 &gt;&gt;&gt; Codepoint.objects.get(name='Sparkles')<br>
&lt;Codepoint: Sparkles><br>
 &gt;&gt;&gt; Codepoint.objects.get()<w>&nbsp;</w>

Note: a thing to note about get

Get will always return one and only one object

THERE CAN BE ONLY ONE

So if you try and run get, say, without any limiatations
---
 <div class="shell-wrap"><p class="shell-top-bar">python3.6</p><p class="shell-body">
 &gt;&gt;&gt; from unicodex.models import Codepoint<br>
 &gt;&gt;&gt; Codepoint.objects.filter(name='Sparkles')<br>
&lt;QuerySet [&lt;Codepoint: Sparkles>]><br>
 &gt;&gt;&gt; Codepoint.objects.get(name='Sparkles')<br>
&lt;Codepoint: Sparkles><br>
 &gt;&gt;&gt; Codepoint.objects.get()<br>
Traceback (most recent call last):<br>
&nbsp; File "&lt;console>", line 1, in &lt;module><br>
&nbsp; File "/usr/local/lib/python3.6/site-packages/django/db/models/manager.p y", line 85, in manager_method<br>
&nbsp; &nbsp; return getattr(self.get_queryset(), name)(&#42;args, &#42;&#42;kwargs)<br>
&nbsp; File "/usr/local/lib/python3.6/site-packages/django/db/models/query.py" , line 384, in get<br>
&nbsp; &nbsp; (self.model._meta.object_name, num)<br>
unicodex.models.MultipleObjectsReturned: get() returned more than one Codepoint -- it returned 3!<br>
 &gt;&gt;&gt; <w>&nbsp;</w>

Note: we get a MultipleObjectsReturned error

which tells us that it would have returned three Codepoint objects, which is just far too much for get to handle.
---
## Joins <!-- .slide: class="center" -->

Note: So now we come to the fun bit. Joins

Anyone who's worked with SQL for long enough will know the venn diagrams for inner joins, outer joins, left joins, right joins, and it can get a bit confusing

Thankfully, especially for someone like me who has forgotten so much SQL, the ORM makes joins a joy.
---
<pre><code><c>&dash;&dash; SQL</c><br><r>SELECT * <br>&nbsp; FROM</r> <l>unicodex_codepoint c,<br>&nbsp; &nbsp; &nbsp; &nbsp;unicodex_design d</l><br>&nbsp;<r>WHERE</r> <l>c</l>.<l>name</l> <r>&equals;</r> 'Sparkles'<BR><r>&nbsp; &nbsp;AND</r> d.codepoint_id = c.id;
Note: say we want to join our design and codepoint tables

A codepoint has multiple designs. Sparkles has an image that shows up in Android, Apple, Facebook, etc

So we want to join on the codepoint_id on the designs table to the primary codepoint id

This is a good chunk of SQL

So what does the ORM equivelent look like?
---
<pre><code><c>&dash;&dash; SQL</c><br><r>SELECT * <br>&nbsp; FROM</r> <l>unicodex_codepoint c,<br>&nbsp; &nbsp; &nbsp; &nbsp;unicodex_design d</l><br>&nbsp;<r>WHERE</r> <l>c</l>.<l>name</l> <r>&equals;</r> 'Sparkles'<BR><r>&nbsp; &nbsp;AND</r> d.codepoint_id = c.id;<br><br><c>&num; ORM</c>
Design.objects.filter(<o><br>&nbsp;&nbsp;&nbsp;codepoint&#95;&#95;name&equals;</o>'Sparkles') 
</code></pre> 
Note: Design dot objects dot filter codepoint dunder name equals sparkles.

I know right? so simple!
---
<pre><code><c>&dash;&dash; SQL</c>
<r>SELECT * <br>&nbsp; FROM</r> <l>unicodex_codepoint c,<br>&nbsp; &nbsp; &nbsp; &nbsp;unicodex_design d</l><br>&nbsp;<r>WHERE</r> <l>c</l>.<l>name</l> <r>&equals;</r> 'Sparkles'<BR><r>&nbsp; &nbsp;AND</r> d.codepoint_id = c.id;

<c>&num; ORM</c>
Design.objects.filter(<o><br>&nbsp;&nbsp;&nbsp;codepoint&#95;&#95;name&equals;</o>'Sparkles') 
&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; <c>^^</c>
</code></pre> 

Note: this doubleunderscore here is doing a lot of powerful things behind the scenes

which I'll explain more in a moment.

---
 <div class="shell-wrap"><p class="shell-top-bar">python3.6</p><p class="shell-body">
 &gt;&gt;&gt; from unicodex.models import Design<br>
 &gt;&gt;&gt; <w>&nbsp;</w>

Note: back to our terminal again, to execute this elegant little code snippet

We import the design model this time
---
 <div class="shell-wrap"><p class="shell-top-bar">python3.6</p><p class="shell-body">
 &gt;&gt;&gt; from unicodex.models import Design<br>
 &gt;&gt;&gt; Design.objects.filter(codepoint&#95;&#95;name='Sparkles')<w>&nbsp;</w>
Note: and we run our filter
---
 <div class="shell-wrap"><p class="shell-top-bar">python3.6</p><p class="shell-body">
 &gt;&gt;&gt; from unicodex.models import Design<br>
 &gt;&gt;&gt; Design.objects.filter(codepoint&#95;&#95;name='Sparkles')<br>
&lt;QuerySet [&lt;Design: Sparkles Microsoft - Windows 10>, &lt;Design: Sparkles Microsoft - Windows 8.1>, &lt;Design: Sparkles Microsoft - Windows 8.0>, &lt;Design: Sparkles Facebook - 2.2>, &lt;Design: Sparkles Facebook - 1.0>, &lt;Design: Sparkles Messenger - 1.0>, &lt;Design: Sparkles Twitter - 1.0>, &lt;Design: Sparkles EmojiOne - 3.0>, &lt;Design: Sparkles EmojiOne - 2.0>, &lt;Design: Sparkles EmojiOne - 1.0>, '...(remaining elements truncated)...']><br>
 &gt;&gt;&gt; <w>&nbsp;</w>

Note: And we get back a reeeeeeally long queryset.

But, the resuts are truncated for us

This is so incredibly useful

Data is still there, if you iterate over the list, but the print representation specificalyl doesn't flood your terminal

(this was implemented because of a very real bug at Lawrance Journal World, where they had servers keep crashing, because the debug page was trying to be helpful and show all the data... a million objects worth..)
---
<pre><code><c>&num; ORM</c>
Design.objects.filter(<o><br>&nbsp;&nbsp;&nbsp;codepoint&#95;&#95;name&equals;</o>'Sparkles') 

<c>&num; field, field, field... lookup</c>

Note: what we have here is one or more fields and then a lookup, all separated by double underscores

A lookup as an operation on that field

If you remember back when we looked up the fields on a model, we know what options we have here.
---
 <div class="shell-wrap"><p class="shell-top-bar">python3.6</p><p class="shell-body">
 &gt;&gt;&gt; from unicodex.models import Design<br>
 &gt;&gt;&gt; Design._meta.get_fields()<w>&nbsp;</w>
---
 <div class="shell-wrap"><p class="shell-top-bar">python3.6</p><p class="shell-body">
 &gt;&gt;&gt; from unicodex.models import Design<br>
 &gt;&gt;&gt; Design._meta.get_fields()<br>
(&lt;django.db.models.fields.AutoField: id>,<br>
&lt;django.db.models.fields.related.ForeignKey: vendorversion>, <br>
&lt;django.db.models.fields.related.ForeignKey: codepoint>, <br>
&lt;django.db.models.fields.files.FileField: image>)<br>
 &gt;&gt;&gt; <w>&nbsp;</w>

Note: we have four fields - a unique id, two foreign keys off to other models, and image

but name isn't there. That came from codepoint

---
 <div class="shell-wrap"><p class="shell-top-bar">python3.6</p><p class="shell-body">
 &gt;&gt;&gt; from unicodex.models import Design<br>
 &gt;&gt;&gt; Design._meta.get_fields()<br>
(&lt;django.db.models.fields.AutoField: id>,<br>
&lt;django.db.models.fields.related.ForeignKey: vendorversion>, <br>
&lt;django.db.models.fields.related.ForeignKey: codepoint>, <br>
&lt;django.db.models.fields.files.FileField: image>)<br>
 &gt;&gt;&gt; Codepoint._meta.get_fields()<w>&nbsp;</w>

Note: so if we inspect Codepoint

---
 <div class="shell-wrap"><p class="shell-top-bar">python3.6</p><p class="shell-body">
 &gt;&gt;&gt; from unicodex.models import Design<br>
 &gt;&gt;&gt; Design._meta.get_fields()<br>
(&lt;django.db.models.fields.AutoField: id>,<br>
&lt;django.db.models.fields.related.ForeignKey: vendorversion>, <br>
&lt;django.db.models.fields.related.ForeignKey: codepoint>, <br>
&lt;django.db.models.fields.files.FileField: image>)<br>
 &gt;&gt;&gt; Codepoint._meta.get_fields()<br>
(&lt;ManyToOneRel: unicodex.design>, <br>
&lt;django.db.models.fields.AutoField: id>,<br>
&lt;django.db.models.fields.CharField: name>, <br>
&lt;django.db.models.fields.TextField: description>,<br>
&lt;django.db.models.fields.CharField: codepoint>)<br>
 &gt;&gt;&gt; <w>&nbsp;</w>

Note: WE see that codepoint has the name field
---
<pre><code><c>&num; ORM</c>
Design.objects.filter(<o><br>&nbsp;&nbsp;&nbsp;codepoint&#95;&#95;name&equals;</o>'Sparkles')<br><br><c>&num; field, field, field... lookup</c>

Note: You'll also note in our example that we end on a field.

By default the look up is an exact match on the string. So effectively, name equals sparkles
---
<pre><code><c>&num; ORM</c>
Design.objects.filter(<o><br>&nbsp;&nbsp;&nbsp;codepoint&#95;&#95;name&equals;</o>'Sparkles')<br><br><c>&num; field, field, field... lookup</c>
<br><c>&num; ORM</c>
Design.objects.filter(<o><br>&nbsp;&nbsp;&nbsp;codepoint&#95;&#95;name&#95;&#95;exact&equals;</o>'Sparkles') 

Note: so by default what we're calling is codepoint name equals
---
# Aside <!-- .slide: class="center" -->

Note: as aside, did you know that this is how those awesome admin filters work? it's true!
---
 <img src="pictures/djuser_super.png" style="margin-top: -50px" />
Note: if we go back to that admin page we saw right at the start
---
 <img src="pictures/djuser_super_h.png" style="margin-top: -50px" />
Note: 

Look at the URL

It's our filters

the admin uses field lookups in it's UI

and to some extent, you can handcode this URL to do some basic filtering, even if there isn't any filters on the right hand side panel

---
 <div class="shell-wrap"><p class="shell-top-bar">python3.6</p><p class="shell-body">
 &gt;&gt;&gt; from unicodex.models import Design<br>
 &gt;&gt;&gt; Design._meta.get_fields()<br>
(&lt;django.db.models.fields.AutoField: id>,<br>
&lt;django.db.models.fields.related.ForeignKey: vendorversion>, <br>
&lt;django.db.models.fields.related.ForeignKey: codepoint>, <br>
&lt;django.db.models.fields.files.FileField: image>)<br>
 &gt;&gt;&gt; Codepoint._meta.get_fields()<br>
(&lt;ManyToOneRel: unicodex.design>, <br>
&lt;django.db.models.fields.AutoField: id>,<br>
&lt;django.db.models.fields.CharField: name>, <br>
&lt;django.db.models.fields.TextField: description>,<br>
&lt;django.db.models.fields.CharField: codepoint>)<br>
 &gt;&gt;&gt; <w>&nbsp;</w>

Note: 

back to our terminal

We can also forge a path down a different series of foreign keys

See the vendorversion there? Let's see what that contains
---

 <div class="shell-wrap"><p class="shell-top-bar">python3.6</p><p class="shell-body">
 &gt;&gt;&gt; <w>&nbsp;</w>
---
 <div class="shell-wrap"><p class="shell-top-bar">python3.6</p><p class="shell-body">
 &gt;&gt;&gt; from unicodex.models import VendorVersion<w>&nbsp;</w>
---

 <div class="shell-wrap"><p class="shell-top-bar">python3.6</p><p class="shell-body">
 &gt;&gt;&gt; from unicodex.models import VendorVersion<br>
 &gt;&gt;&gt; <w>&nbsp;</w>
---
 <div class="shell-wrap"><p class="shell-top-bar">python3.6</p><p class="shell-body">
 &gt;&gt;&gt; from unicodex.models import VendorVersion<br>
 &gt;&gt;&gt; VendorVersion._meta.get_fields()<w>&nbsp;</w>


Note: let's refresh our terminal and inspect VendorVersion

---
 <div class="shell-wrap"><p class="shell-top-bar">python3.6</p><p class="shell-body">
 &gt;&gt;&gt; from unicodex.models import VendorVersion<br>
 &gt;&gt;&gt; VendorVersion._meta.get_fields()<br>
(&lt;ManyToOneRel: unicodex.design>,<br>
&lt;django.db.models.fields.AutoField: id>, <br>
&lt;django.db.models.fields.CharField: name>, <br>
&lt;django.db.models.fields.related.ForeignKey: vendor>)<br>
 &gt;&gt;&gt; <w>&nbsp;</w>

Note: Okay, so a vendorversion has many designs, an ID, a name, and a Vendor FK

What about Vendor?
---
 <div class="shell-wrap"><p class="shell-top-bar">python3.6</p><p class="shell-body">
 &gt;&gt;&gt; from unicodex.models import VendorVersion<br>
 &gt;&gt;&gt; VendorVersion._meta.get_fields()<br>
(&lt;ManyToOneRel: unicodex.design>,<br>
&lt;django.db.models.fields.AutoField: id>, <br>
&lt;django.db.models.fields.CharField: name>, <br>
&lt;django.db.models.fields.related.ForeignKey: vendor>)<br>
 &gt;&gt;&gt; from unicodex.models import Vendor<w>&nbsp;</w>

---
 <div class="shell-wrap"><p class="shell-top-bar">python3.6</p><p class="shell-body">
 &gt;&gt;&gt; from unicodex.models import VendorVersion<br>
 &gt;&gt;&gt; VendorVersion._meta.get_fields()<br>
(&lt;ManyToOneRel: unicodex.design>,<br>
&lt;django.db.models.fields.AutoField: id>, <br>
&lt;django.db.models.fields.CharField: name>, <br>
&lt;django.db.models.fields.related.ForeignKey: vendor>)<br>
 &gt;&gt;&gt; from unicodex.models import Vendor<br>
 &gt;&gt;&gt; <w>&nbsp;</w>
---
 <div class="shell-wrap"><p class="shell-top-bar">python3.6</p><p class="shell-body">
 &gt;&gt;&gt; from unicodex.models import VendorVersion<br>
 &gt;&gt;&gt; VendorVersion._meta.get_fields()<br>
(&lt;ManyToOneRel: unicodex.design>,<br>
&lt;django.db.models.fields.AutoField: id>, <br>
&lt;django.db.models.fields.CharField: name>, <br>
&lt;django.db.models.fields.related.ForeignKey: vendor>)<br>
 &gt;&gt;&gt; from unicodex.models import Vendor<br>
 &gt;&gt;&gt; Vendor._meta.get_fields()<w>&nbsp;</w>


Note: clear our terminal, import Vendor, and check

---
 <div class="shell-wrap"><p class="shell-top-bar">python3.6</p><p class="shell-body">
 &gt;&gt;&gt; from unicodex.models import VendorVersion<br>
 &gt;&gt;&gt; VendorVersion._meta.get_fields()<br>
(&lt;ManyToOneRel: unicodex.design>,<br>
&lt;django.db.models.fields.AutoField: id>, <br>
&lt;django.db.models.fields.CharField: name>, <br>
&lt;django.db.models.fields.related.ForeignKey: vendor>)<br>
 &gt;&gt;&gt; from unicodex.models import Vendor<br>
 &gt;&gt;&gt; Vendor._meta.get_fields()<br>
(&lt;ManyToOneRel: unicodex.vendorversion>, <br>
&lt;django.db.models.fields.AutoField: id>, <br>
&lt;django.db.models.fields.CharField: name>) <br>
 &gt;&gt;&gt; <w>&nbsp;</w>

Note: so vendor has a relationship with vendorversion, an id and a name too

And thus, we have exhausted our search, and we could build up a UML diagram showing the relationships between all the tables in this app

But I woldn't do that too you.

Back to what we were doing, showing filter walks

---

 <div class="shell-wrap"><p class="shell-top-bar">python3.6</p><p class="shell-body">
 &gt;&gt;&gt; <w>&nbsp;</w>

Note: clearing our terminal again with Control L
---
 <div class="shell-wrap"><p class="shell-top-bar">python3.6</p><p class="shell-body">
 &gt;&gt;&gt; Design.objects.filter(<w>&nbsp;</w>

Note: we have a number of options here. Let's build the longest chain we can...

---
 <div class="shell-wrap"><p class="shell-top-bar">python3.6</p><p class="shell-body">
 &gt;&gt;&gt; Design.objects.filter(vendorversion<w>&nbsp;</w>

Note: Let's filter design objects where... the linked vendor version

---

 <div class="shell-wrap"><p class="shell-top-bar">python3.6</p><p class="shell-body">
 &gt;&gt;&gt; Design.objects.filter(vendorversion&#95;&#95;vendor<w>&nbsp;</w>


Note: and the vendor linked to that....

---
 <div class="shell-wrap"><p class="shell-top-bar">python3.6</p><p class="shell-body">
 &gt;&gt;&gt; Design.objects.filter(vendorversion&#95;&#95;vendor&#95;&#95;name<w>&nbsp;</w>

Note: the name of that vendor

---


 <div class="shell-wrap"><p class="shell-top-bar">python3.6</p><p class="shell-body">
 &gt;&gt;&gt; Design.objects.filter(vendorversion&#95;&#95;vendor&#95;&#95;name&#95;&#95;contains=<w>&nbsp;</w>

Note: contains...
---

 <div class="shell-wrap"><p class="shell-top-bar">python3.6</p><p class="shell-body">
 &gt;&gt;&gt; Design.objects.filter(vendorversion&#95;&#95;vendor&#95;&#95;name&#95;&#95;contains="Micro")<w>&nbsp;</w>

Note: the string Micro
---

 <div class="shell-wrap"><p class="shell-top-bar">python3.6</p><p class="shell-body">
 &gt;&gt;&gt; Design.objects.filter(vendorversion&#95;&#95;vendor&#95;&#95;name&#95;&#95;contains="Micro")<br>
&lt;QuerySet [&lt;Design: Sparkles Microsoft - Windows 8.0>, &lt;Design: Two Hearts Microsoft - Windows 8.0>, &lt;Design: Sparkles Microsoft - Windows 8.1>, &lt;Design: Two Hearts Microsoft - Windows 8.1>, &lt;Design: Sparkles Microsoft - Windows 10>, &lt;Design: Two Hearts Microsoft - Windows 10>]><br>
 &gt;&gt;&gt; <w>&nbsp;</w>

Note: And thus, we get a of all designs where the name of the linked vendor contains Micro

---
<pre><code><c>&num; Field Lookups</c><table>
<tr><td><l>contains</l></td><td><o>LIKE "%?%"</o></td></tr>
<tr><td><l>startswith</l></td><td><o>LIKE "%?"</o></td></tr>
<tr><td><l>endswith</l></td><td><o>LIKE "?%"</o></td></tr>
<tr><td><l>in</l></td><td><o>IN (?, ?, ?, ...)</o></td></tr>
<tr><td><l>lt, le, gt, ge</l></td><td><o>&lt;, &lt;=, &gt;, &gt;=</o></td></tr>
<tr><td><l>range</l></td><td><o>BETWEEN</o></td></tr> 
<tr><td><l>isnull</l></td><td><o>NULL</o></td></tr></table><c>&num; ... and many more!</c>
<span class="bfoot" style="margin-bottom: -270px"><fl>[docs - querysets field lookups](https://docs.djangoproject.com/en/2.0/ref/models/querysets/#field-lookups)</fl></span>

Note: There are other field lookups we can use for a number of differnt things.

We're also not just limited to one filter, we can have more than one
---

 <div class="shell-wrap"><p class="shell-top-bar">python3.6</p><p class="shell-body">
 &gt;&gt;&gt; Design.objects.filter(vendorversion&#95;&#95;vendor&#95;&#95;name&#95;&#95;contains="Micro"<w>&nbsp;</w>

Note: instead of just filtering on Micro, we could alos
---
 <div class="shell-wrap"><p class="shell-top-bar">python3.6</p><p class="shell-body">
 &gt;&gt;&gt; Design.objects.filter(vendorversion&#95;&#95;vendor&#95;&#95;name&#95;&#95;contains="Micro",<br>
 ... &nbsp;&nbsp;<w>&nbsp;</w><br>
---
 <div class="shell-wrap"><p class="shell-top-bar">python3.6</p><p class="shell-body">
 &gt;&gt;&gt; Design.objects.filter(vendorversion&#95;&#95;vendor&#95;&#95;name&#95;&#95;contains="Micro",<br>
 ... &nbsp; codepoint<w>&nbsp;</w><br>

---
 <div class="shell-wrap"><p class="shell-top-bar">python3.6</p><p class="shell-body">
 &gt;&gt;&gt; Design.objects.filter(vendorversion&#95;&#95;vendor&#95;&#95;name&#95;&#95;contains="Micro",<br>
 ... &nbsp; codepoint&#95;&#95;name<w>&nbsp;</w><br>


---
 <div class="shell-wrap"><p class="shell-top-bar">python3.6</p><p class="shell-body">
 &gt;&gt;&gt; Design.objects.filter(vendorversion&#95;&#95;vendor&#95;&#95;name&#95;&#95;contains="Micro",<br>
 ... &nbsp; codepoint&#95;&#95;name&#95;&#95;endswith<w>&nbsp;</w><br>

---
 <div class="shell-wrap"><p class="shell-top-bar">python3.6</p><p class="shell-body">
 &gt;&gt;&gt; Design.objects.filter(vendorversion&#95;&#95;vendor&#95;&#95;name&#95;&#95;contains="Micro",<br>
 ... &nbsp; codepoint&#95;&#95;name&#95;&#95;endswith="Hearts")<w>&nbsp;</w><br>


---
 <div class="shell-wrap"><p class="shell-top-bar">python3.6</p><p class="shell-body">
 &gt;&gt;&gt; Design.objects.filter(vendorversion&#95;&#95;vendor&#95;&#95;name&#95;&#95;contains="Micro",<br>
 ... &nbsp; codepoint&#95;&#95;name&#95;&#95;endswith="Hearts")<br>
&lt;QuerySet [&lt;Design: Two Hearts Microsoft - Windows 10>, &lt;Design: Two Hearts Microsoft - Windows 8.1>, &lt;Design: Two Hearts Microsoft - Windows 8.0>]><br>
 &gt;&gt;&gt; <w>&nbsp;</w>

Note: we get list of designs both from a vendor
---
## ... `AND`? <!-- .slide: class="center" -->
Note: 

So far we've dealt with single or chained filters, which will AND together

name equals sparkles AND image ends with png AND AND AND

If we want to start using OR, we need to get a bit fancy
---
# `Q` <!-- .slide: class="center" -->

Note: This is where Q comes in

No, not the race from the great Star Trek sequel, The Next Generation,

Q and in Query

With Q, we can build up AND, OR, and NOT statements in our where clause when filtering objects

So, let's start some comparisons...
---
<pre><code><c>&num; ORM</c>
Codepoint.objects.filter( 
&nbsp; <o>name=</o>'Sparkles',
&nbsp; <o>description=</o>'Shiny!'
) 


Note: instead of using our super long chaining filter, let's use a simpler example here
this query would give us codepoints named sparkles with the description shiny

---
<pre><code><c>&num; ORM</c>
Codepoint.objects.filter( 
&nbsp; <o>name=</o>'Sparkles',
&nbsp; <o>description=</o>'Shiny!'
)<br><br><c>&dash;&dash; SQL</c><br><r>SELECT *
&nbsp; FROM</r> <l>unicodex_codepoint c </l><br><r>&nbsp;WHERE</r> <l>c</l>.<l>name</l> <r>=</r> 'Sparkles'<br><r>&nbsp; &nbsp;AND</r> <l>c</l>.<l>description</l> <r>=</r> 'Shiny!'

Note: this would be the equvilent SQL
---
<pre><code><c>&num; ORM</c>
Codepoint.objects.filter( 
&nbsp; <o>name&#95;&#95;exact=</o>'Sparkles',
&nbsp; <o>description&#95;&#95;exact=</o>'Shiny!'
)<br><br><c>&dash;&dash; SQL</c><br><r>SELECT *
&nbsp; FROM</r> <l>unicodex_codepoint c </l><br><r>&nbsp;WHERE</r> <l>c</l>.<l>name</l> <r>=</r> 'Sparkles'<br><r>&nbsp; &nbsp;AND</r> <l>c</l>.<l>description</l> <r>=</r> 'Shiny!'

Note: And we learnt earlier that unless there's a field lookup defined, we assume exact

This is the same SQL

We can also express this same statement using Q
---

<pre><code><c>&num; ORM</c>
Codepoint.objects.filter( 
&nbsp; <o>name=</o>'Sparkles',
&nbsp; <o>description=</o>'Shiny!'
)<br><br><c>&dash;&dash; SQL</c><br><r>SELECT *
&nbsp; FROM</r> <l>unicodex_codepoint c </l><br><r>&nbsp;WHERE</r> <l>c</l>.<l>name</l> <r>=</r> 'Sparkles'<br><r>&nbsp; &nbsp;AND</r> <l>c</l>.<l>description</l> <r>=</r> 'Shiny!'

Note: so going back to our first example,
---
<pre><code><c>&num; ORM</c>
Codepoint.objects.filter( 
&nbsp; <o>name=</o>'Sparkles').filter(
&nbsp; <o>description=</o>'Shiny!'
)<br><br><c>&dash;&dash; SQL</c><br><r>SELECT *
&nbsp; FROM</r> <l>unicodex_codepoint c </l><br><r>&nbsp;WHERE</r> <l>c</l>.<l>name</l> <r>=</r> 'Sparkles'<br><r>&nbsp; &nbsp;AND</r> <l>c</l>.<l>description</l> <r>=</r> 'Shiny!'

Note: we could also have two separate filter clauses.
---
<pre><code><c>&num; ORM</c>
Codepoint.objects.filter( 
&nbsp; <o>name=</o>'Sparkles',
&nbsp; <o>description=</o>'Shiny!'
)<br><br><c>&dash;&dash; SQL</c><br><r>SELECT *
&nbsp; FROM</r> <l>unicodex_codepoint c </l><br><r>&nbsp;WHERE</r> <l>c</l>.<l>name</l> <r>=</r> 'Sparkles'<br><r>&nbsp; &nbsp;AND</r> <l>c</l>.<l>description</l> <r>=</r> 'Shiny!'

Note: we could also

---
<pre><code><c>&num; ORM</c>
Codepoint.objects.filter( 
&nbsp; Q(<o>name=</o>'Sparkles'),
&nbsp; Q(<o>description=</o>'Shiny!')
)<br><br><c>&dash;&dash; SQL</c><br><r>SELECT *
&nbsp; FROM</r> <l>unicodex_codepoint c </l><br><r>&nbsp;WHERE</r> <l>c</l>.<l>name</l> <r>=</r> 'Sparkles'<br><r>&nbsp; &nbsp;AND</r> <l>c</l>.<l>description</l> <r>=</r> 'Shiny!'

Note: wrap our two filter parameters in Q

This provides the same result

Notice in all of this, the equivelent SQL hasn't changed.

With our comma here, we're implying we're using AND here. We can be explicit

---
<pre><code><c>&num; ORM</c>
Codepoint.objects.filter( 
&nbsp; Q(<o>name=</o>'Sparkles') <r>&</r>
&nbsp; Q(<o>description=</o>'Shiny!')
)<br><br><c>&dash;&dash; SQL</c><br><r>SELECT *
&nbsp; FROM</r> <l>unicodex_codepoint c </l><br><r>&nbsp;WHERE</r> <l>c</l>.<l>name</l> <r>=</r> 'Sparkles'<br><r>&nbsp; &nbsp;AND</r> <l>c</l>.<l>description</l> <r>=</r> 'Shiny!'

Note: 

But, since we have Q objects, we can do operations on them

Here, we're saying filter by this Query, and this Query

And we're using AND here explitictly

We don't have to wrap both in Q, either
---
<pre><code><c>&num; ORM</c>
Codepoint.objects.filter( 
&nbsp; Q(<o>name=</o>'Sparkles'),</r>
&nbsp; Q(<o>description=</o>'Shiny!')
)<br><br><c>&dash;&dash; SQL</c><br><r>SELECT *
&nbsp; FROM</r> <l>unicodex_codepoint c </l><br><r>&nbsp;WHERE</r> <l>c</l>.<l>name</l> <r>=</r> 'Sparkles'<br><r>&nbsp; &nbsp;AND</r> <l>c</l>.<l>description</l> <r>=</r> 'Shiny!'

Note: going back to our changed example
---
<pre><code><c>&num; ORM</c>
Codepoint.objects.filter( 
&nbsp; Q(<o>name=</o>'Sparkles'),
&nbsp; <o>description=</o>'Shiny!'
)<br><br><c>&dash;&dash; SQL</c><br><r>SELECT *
&nbsp; FROM</r> <l>unicodex_codepoint c </l><br><r>&nbsp;WHERE</r> <l>c</l>.<l>name</l> <r>=</r> 'Sparkles'<br><r>&nbsp; &nbsp;AND</r> <l>c</l>.<l>description</l> <r>=</r> 'Shiny!'


Note: we can change our queries with comman, and just wrap the first one and leave thther. Same result
---
<pre><code><c>&num; ORM</c>
Codepoint.objects.filter( 
&nbsp; <o>name=</o>'Sparkles',
&nbsp; <o>description=</o>'Shiny!'
)<br><br><c>&dash;&dash; SQL</c><br><r>SELECT *
&nbsp; FROM</r> <l>unicodex_codepoint c </l><br><r>&nbsp;WHERE</r> <l>c</l>.<l>name</l> <r>=</r> 'Sparkles'<br><r>&nbsp; &nbsp;AND</r> <l>c</l>.<l>description</l> <r>=</r> 'Shiny!'


Note: and we don't have to wrap either. But what if we wrap just the second
So, we could just wrap the second one, and leave the first one alone, right?


---
<pre><code><c>&num; ORM</c>
Codepoint.objects.filter( 
&nbsp; <o>name=</o>'Sparkles',
&nbsp; Q(<o>description=</o>'Shiny!')
)<br><br><r>SyntaxError: positional argument follows keyword argument</r>

Note: well no, we get an error.

The error here is insightful: Syntax Error, positioal argument follows keyword argument

The reasoning behind this is that in all the code we've been doing here, we've been giving arguments to the filter function

And in python, you have to declare positional argumnet before keyword argumnets

Remembering that even in these new Django concepts, we're still using Python, so python rules still apply.
---

<pre><code><c>&num; ORM</c>
Codepoint.objects.filter( 
&nbsp; <o>name=</o>'Sparkles',
&nbsp; <o>description=</o>'Shiny!'
)<br><br><c>&dash;&dash; SQL</c><br><r>SELECT *
&nbsp; FROM</r> <l>unicodex_codepoint c </l><br><r>&nbsp;WHERE</r> <l>c</l>.<l>name</l> <r>=</r> 'Sparkles'<br><r>&nbsp; &nbsp;AND</r> <l>c</l>.<l>description</l> <r>=</r> 'Shiny!'

Note: Another example of this. Let's put our code back working, and try changing that description

Say we want to search for sparkles and unicorns

So we search for name equals sparkles and name equals unicorns and
---
<pre><code><c>&num; ORM</c>
Codepoint.objects.filter( 
&nbsp; <o>name=</o>'Sparkles',
&nbsp; <o>name=</o>'Unicorn'
)<br><br><r>SyntaxError: keyword argument repeated</r>

Note: oh. There's an error.

This is agan, because Python. You can't repeat keyword aguments. But, you can get around this.
Just wrap it in Q

---
<pre><code><c>&num; ORM</c>
Codepoint.objects.filter( 
&nbsp; Q(<o>name=</o>'Sparkles'),
&nbsp; Q(<o>name=</o>'Unicorn')
)<br><br><c>&dash;&dash; SQL</c><br><r>SELECT *
&nbsp; FROM</r> <l>unicodex_codepoint c </l><br><r>&nbsp;WHERE</r> <l>c</l>.<l>name</l> <r>=</r> 'Sparkles'<br><r>&nbsp; &nbsp;AND</r> <l>c</l>.<l>name</l> <r>=</r> 'Unicorn'

Note: now, this code is valid python, but it isn't useful, because it will never return any results.

We're asking for exact string matches on the same column, twice. It'll always be an empty set.

But what we can do is change this from an and, to an OR

---
<pre><code><c>&num; ORM</c>
Codepoint.objects.filter( 
&nbsp; Q(<o>name=</o>'Sparkles') &
&nbsp; Q(<o>name=</o>'Unicorn')
)<br><br><c>&dash;&dash; SQL</c><br><r>SELECT *
&nbsp; FROM</r> <l>unicodex_codepoint c </l><br><r>&nbsp;WHERE</r> <l>c</l>.<l>name</l> <r>=</r> 'Sparkles'<br><r>&nbsp; &nbsp;AND</r> <l>c</l>.<l>name</l> <r>=</r> 'Unicorn'

Note: Using the comma is equiv to this AND, but with the comma we're giving filter two arguments. Here, we're giving it one. We'll get back to this, because it's really cool

So, to take our AND to and OR, we change the ampersand

---
<pre><code><c>&num; ORM</c>
Codepoint.objects.filter( 
&nbsp; Q(<o>name=</o>'Sparkles') |
&nbsp; Q(<o>name=</o>'Unicorn')
)<br><br><c>&dash;&dash; SQL</c><br><r>SELECT *
&nbsp; FROM</r> <l>unicodex_codepoint c </l><br><r>&nbsp;WHERE</r> <l>c</l>.<l>name</l> <r>=</r> 'Sparkles'<br><r> &nbsp; &nbsp;OR</r> <l>c</l>.<l>name</l> <r>=</r> 'Unicorn'

Note: to a pipe.

This is an or operation

You may have only seen these operators before in bitmasking

---
 <div class="shell-wrap"><p class="shell-top-bar">python3.6</p><p class="shell-body">
 &gt;&gt;&gt; <w>&nbsp;</w>
---
 <div class="shell-wrap"><p class="shell-top-bar">python3.6</p><p class="shell-body">
 &gt;&gt;&gt; x = 0b10101010<w>&nbsp;</w>

Note: if we have X as a binary string of one zero one zero

---
 <div class="shell-wrap"><p class="shell-top-bar">python3.6</p><p class="shell-body">
 &gt;&gt;&gt; x = 0b10101010<br>
 &gt;&gt;&gt; <w>&nbsp;</w>

---
 <div class="shell-wrap"><p class="shell-top-bar">python3.6</p><p class="shell-body">
 &gt;&gt;&gt; x = 0b10101010<br>
 &gt;&gt;&gt; y = 0b11110000<w>&nbsp;</w>

Note: and we have y as one one one zero zero zero zero

we can do something called bit masking

---
 <div class="shell-wrap"><p class="shell-top-bar">python3.6</p><p class="shell-body">
 &gt;&gt;&gt; x = 0b10101010<br>
 &gt;&gt;&gt; y = 0b11110000<br>
 &gt;&gt;&gt; <w>&nbsp;</w>

---
 <div class="shell-wrap"><p class="shell-top-bar">python3.6</p><p class="shell-body">
 &gt;&gt;&gt; x = 0b10101010<br>
 &gt;&gt;&gt; y = 0b11110000<br>
 &gt;&gt;&gt; bin(x & y)<w>&nbsp;</w>

Note: if we ask for x AND y

---
 <div class="shell-wrap"><p class="shell-top-bar">python3.6</p><p class="shell-body">
 &gt;&gt;&gt; x = 0b10101010<br>
 &gt;&gt;&gt; y = 0b11110000<br>
 &gt;&gt;&gt; bin(x & y)<br>
'0b10100000'<br> 
 &gt;&gt;&gt; <w>&nbsp;</w>

Note: we get 10100000

For each bit, we only return 1 if both are 1

---
 <div class="shell-wrap"><p class="shell-top-bar">python3.6</p><p class="shell-body">
 &gt;&gt;&gt; x = 0b10101010<br>
 &gt;&gt;&gt; y = 0b11110000<br>
 &gt;&gt;&gt; bin(x & y)<br>
'0b10100000'<br> 
 &gt;&gt;&gt; bin(x | y)<w>&nbsp;</w>

Note: conversely, if we ask for x OR y

---
 <div class="shell-wrap"><p class="shell-top-bar">python3.6</p><p class="shell-body">
 &gt;&gt;&gt; x = 0b10101010<br>
 &gt;&gt;&gt; y = 0b11110000<br>
 &gt;&gt;&gt; bin(x & y)<br>
'0b10100000'<br> 
 &gt;&gt;&gt; bin(x | y)<br>
'0b11110101' 

Note: we get all ones at the start, then our stripes

That's because we return one is either or are 1


That's how binary ANDs and binary ORs work

This is very similar to what we do in SQL.

For each row of a table, we want to return it in our result set if BOTH conditions are true on and, or if either are true on and OR

---
<pre><code><c>&num; ORM</c>
Codepoint.objects.filter( 
&nbsp; Q(<o>name=</o>'Sparkles') |
&nbsp; Q(<o>name=</o>'Unicorn')
)<br><br><c>&dash;&dash; SQL</c><br><r>SELECT *
&nbsp; FROM</r> <l>unicodex_codepoint c </l><br><r>&nbsp;WHERE</r> <l>c</l>.<l>name</l> <r>=</r> 'Sparkles'<br><r> &nbsp; &nbsp;OR</r> <l>c</l>.<l>name</l> <r>=</r> 'Unicorn'


Note: so, using the and or operators here makes sense, because those are the actions we are performing

But, we're doing these operations on Query objects, not binary. Do how does that work?

What's happening here is metaprogramming. Sometimes confused for magic, it's a funcitonlaity of python that makes it really powerful.

I'm going to show you a small snippet of django source code. It won't be scary, don't worry.

---
<pre><code style="font-size: 24pt !important"><r>class</r> <g>Q</g>(<g>tree</g>.<g>Node</g>):
<c>"""<br>Encapsulate filters as objects that can<br>then be combined logically (using `&` and `|`).<br>"""</c>
&nbsp; ...<br<br>>
&nbsp; <r>def</r> <l>&#95;&#95;or&#95;&#95;</l>(self, other):
&nbsp; &nbsp; <r>return</r> <l>self</l>._combine(other, <l>self.OR</l>)

&nbsp; <r>def</r> <l>&#95;&#95;and&#95;&#95;</l>(self, other):
&nbsp; &nbsp; <r>return</r> <l>self</l>._combine(other, <l>self.AND</l>)
</code></pre> 

 <span class='foot'>[django db/models/utils.py](https://github.com/django/django/blame/5256a805ff1c31e4d5112627846291e91c5dc65d/django/db/models/query_utils.py#L142)</span>

Note: django literally overloads the operations that happens when you try and do bitwise operations on the Q class in order for Q to have a logical response to bitwise operations

and it means you can do bitwise operations on Q obecjts and it's compeltely valid python

it's composble, it's functional, and it's intuative.

and it's been in Django for over 10 years

---
<pre><code><c>&num; ORM</c>
Codepoint.objects.filter( 
&nbsp; Q(<o>name=</o>'Sparkles') |
&nbsp; Q(<o>name=</o>'Unicorn')
)<br><br><c>&dash;&dash; SQL</c><br><r>SELECT *
&nbsp; FROM</r> <l>unicodex_codepoint c </l><br><r>&nbsp;WHERE</r> <l>c</l>.<l>name</l> <r>=</r> 'Sparkles'<br><r> &nbsp; &nbsp;OR</r> <l>c</l>.<l>name</l> <r>=</r> 'Unicorn'

Note: as well as AND or OR, we can also do NOT

So with our code above

---
<pre><code><c>&num; ORM</c>
Codepoint.objects.filter( 
&nbsp; Q(<o>name=</o>'Sparkles') |
&nbsp; ~Q(<o>name=</o>'Unicorn')
)<br><br><c>&dash;&dash; SQL</c><br><r>SELECT *
&nbsp; FROM</r> <l>unicodex_codepoint c </l><br><r>&nbsp;WHERE</r> <l>c</l>.<l>name</l> <r>=</r> 'Sparkles'<br><r> &nbsp; &nbsp;OR NOT</r> <l>c</l>.<l>name</l> <r>=</r> 'Unicorn'


Note: we can and a tilda negation to invert that part of the query, and add a NOT to our SQL

Using our field lookups and these operations, we can do a lot of things. But are some limitations

Firstly, you need to understand how the joins happen in order avoid confusion

---
<pre><code><c>&num; ORM</c>
Codepoint.objects.filter( 
&nbsp; <o>design&#95;&#95;image&#95;&#95;contains=</o>"png",
&nbsp; <o>design&#95;&#95;image&#95;&#95;startswith=</o>"design")

Note: Consider the following we want codepoints where their design iages have png and start with design

THis is based on the filename I'm using for the iages uploaded to my models

Okay. Let's run that and see what happens

---
 <div class="shell-wrap"><p class="shell-top-bar">python3.6</p><p class="shell-body">
 <ps>myrtle</ps> <dr>~/project $</dr> 
./manage.py shell<br>
Python 3.6.3 (default, Nov 9 2017, 15:58:30)<br>
[GCC 4.2.1 Compatible Apple LLVM 9.0.0 (clang-900.0.38)] on darwin<br>
Type "help", "copyright", "credits" or "license" for more information.<br>
(InteractiveConsole)<br> 
 &gt;&gt;&gt; <w>&nbsp;</w>

Note: so in our terminal

---
 <div class="shell-wrap"><p class="shell-top-bar">python3.6</p><p class="shell-body">
 <ps>myrtle</ps> <dr>~/project $</dr> 
./manage.py shell<br>
Python 3.6.3 (default, Nov 9 2017, 15:58:30)<br>
[GCC 4.2.1 Compatible Apple LLVM 9.0.0 (clang-900.0.38)] on darwin<br>
Type "help", "copyright", "credits" or "license" for more information.<br>
(InteractiveConsole)<br> 
 &gt;&gt;&gt; from unicodex.models import Codepoint<w>&nbsp;</w>

---
 <div class="shell-wrap"><p class="shell-top-bar">python3.6</p><p class="shell-body">
 <ps>myrtle</ps> <dr>~/project $</dr> 
./manage.py shell<br>
Python 3.6.3 (default, Nov 9 2017, 15:58:30)<br>
[GCC 4.2.1 Compatible Apple LLVM 9.0.0 (clang-900.0.38)] on darwin<br>
Type "help", "copyright", "credits" or "license" for more information.<br>
(InteractiveConsole)<br> 
 &gt;&gt;&gt; from unicodex.models import Codepoint<br>
 &gt;&gt;&gt; <w>&nbsp;</w>

Note: remembering to import our model

---
 <div class="shell-wrap"><p class="shell-top-bar">python3.6</p><p class="shell-body">
 <ps>myrtle</ps> <dr>~/project $</dr> 
./manage.py shell<br>
Python 3.6.3 (default, Nov 9 2017, 15:58:30)<br>
[GCC 4.2.1 Compatible Apple LLVM 9.0.0 (clang-900.0.38)] on darwin<br>
Type "help", "copyright", "credits" or "license" for more information.<br>
(InteractiveConsole)<br> 
 &gt;&gt;&gt; from unicodex.models import Codepoint<br>
 &gt;&gt;&gt; Codepoint.objects.filter(design&#95;&#95;image&#95;&#95;contains="png", design&#95;&#95;image&#95;&#95;startswith="design")<w>&nbsp;</w>

Note: we add our code

---
 <div class="shell-wrap"><p class="shell-top-bar">python3.6</p><p class="shell-body">
 <ps>myrtle</ps> <dr>~/project $</dr> 
./manage.py shell<br>
Python 3.6.3 (default, Nov 9 2017, 15:58:30)<br>
[GCC 4.2.1 Compatible Apple LLVM 9.0.0 (clang-900.0.38)] on darwin<br>
Type "help", "copyright", "credits" or "license" for more information.<br>
(InteractiveConsole)<br> 
 &gt;&gt;&gt; from unicodex.models import Codepoint<br>
 &gt;&gt;&gt; Codepoint.objects.filter(design&#95;&#95;image&#95;&#95;contains="png", design&#95;&#95;image&#95;&#95;startswith="design")<br>
&lt;QuerySet [&lt;Codepoint: Sparkles>, &lt;Codepoint: Sparkles>, &lt;Codepoint: Sparkles>, &lt;Codepoint: Sparkles>, &lt;Codepoint: Sparkles>, &lt;Codepoint: Sparkles>, &lt;Codepoint: Sparkles>, &lt;Codepoint: Sparkles>, &lt;Codepoint: Sparkles>, &lt;Codepoint: Sparkles>, &lt;Codepoint: Sparkles>, &lt;Codepoint: Unicorn>, &lt;Codepoint: Unicorn>, &lt;Codepoint: Unicorn>, &lt;Codepoint: Unicorn>, &lt;Codepoint: Unicorn>, &lt;Codepoint: Unicorn>, &lt;Codepoint: Unicorn>, &lt;Codepoint: Two Hearts>, &lt;Codepoint: Two Hearts>, '...(remaining elements truncated)...']><br>
 &gt;&gt;&gt; <w>&nbsp;</w>


Note: our results are truncated here, so let's get the count of this

---
 <div class="shell-wrap"><p class="shell-top-bar">python3.6</p><p class="shell-body">
 <ps>myrtle</ps> <dr>~/project $</dr> 
./manage.py shell<br>
Python 3.6.3 (default, Nov 9 2017, 15:58:30)<br>
[GCC 4.2.1 Compatible Apple LLVM 9.0.0 (clang-900.0.38)] on darwin<br>
Type "help", "copyright", "credits" or "license" for more information.<br>
(InteractiveConsole)<br> 
 &gt;&gt;&gt; from unicodex.models import Codepoint<br>
 &gt;&gt;&gt; Codepoint.objects.filter(design&#95;&#95;image&#95;&#95;contains="png", design&#95;&#95;image&#95;&#95;startswith="design")<w>&nbsp;</w>


Note: rewind a step

---
 <div class="shell-wrap"><p class="shell-top-bar">python3.6</p><p class="shell-body">
 <ps>myrtle</ps> <dr>~/project $</dr> 
./manage.py shell<br>
Python 3.6.3 (default, Nov 9 2017, 15:58:30)<br>
[GCC 4.2.1 Compatible Apple LLVM 9.0.0 (clang-900.0.38)] on darwin<br>
Type "help", "copyright", "credits" or "license" for more information.<br>
(InteractiveConsole)<br> 
 &gt;&gt;&gt; from unicodex.models import Codepoint<br>
 &gt;&gt;&gt; Codepoint.objects.filter(design&#95;&#95;image&#95;&#95;contains="png", design&#95;&#95;image&#95;&#95;startswith="design").count()<w>&nbsp;</w>

Note: add a count function on the end

---
 <div class="shell-wrap"><p class="shell-top-bar">python3.6</p><p class="shell-body">
 <ps>myrtle</ps> <dr>~/project $</dr> 
./manage.py shell<br>
Python 3.6.3 (default, Nov 9 2017, 15:58:30)<br>
[GCC 4.2.1 Compatible Apple LLVM 9.0.0 (clang-900.0.38)] on darwin<br>
Type "help", "copyright", "credits" or "license" for more information.<br>
(InteractiveConsole)<br> 
 &gt;&gt;&gt; from unicodex.models import Codepoint<br>
 &gt;&gt;&gt; Codepoint.objects.filter(design&#95;&#95;image&#95;&#95;contains="png", design&#95;&#95;image&#95;&#95;startswith="design").count()<br>
37<br> 
 &gt;&gt;&gt; <w>&nbsp;</w>

Note: 37 results

---
<pre><code><c>&num; ORM</c>
Codepoint.objects.filter( 
&nbsp; <o>design&#95;&#95;image&#95;&#95;contains=</o>"png",
&nbsp; <o>design&#95;&#95;image&#95;&#95;startswith=</o>"design").count()

---
<pre><code><c>&num; ORM</c>
Codepoint.objects.filter( 
&nbsp; <o>design&#95;&#95;image&#95;&#95;contains=</o>"png",
&nbsp; <o>design&#95;&#95;image&#95;&#95;startswith=</o>"design").count()<br><br><c>&dash;&dash; SQL</c><br><c>&dash;&dash; ?? </c>


Note: But what code was run?

We have the ability to check this
---
<pre><code><c>&num; ORM</c>
Codepoint.objects.filter( 
&nbsp; <o>design&#95;&#95;image&#95;&#95;contains=</o>"png",
&nbsp; <o>design&#95;&#95;image&#95;&#95;startswith=</o>"design").count()<br><br><c>&dash;&dash; SQL</c><br><c>&dash;&dash; ?? </c><br><br><c>&num; ORM</c><br><r>from</r> django.db <r>import</r> connection<br>connection.queries
</code></pre> 
---
 <div class="shell-wrap"><p class="shell-top-bar">python3.6</p><p class="shell-body">
 <ps>myrtle</ps> <dr>~/project $</dr> 
./manage.py shell<br>
Python 3.6.3 (default, Nov 9 2017, 15:58:30)<br>
[GCC 4.2.1 Compatible Apple LLVM 9.0.0 (clang-900.0.38)] on darwin<br>
Type "help", "copyright", "credits" or "license" for more information.<br>
(InteractiveConsole)<br> 
 &gt;&gt;&gt; from unicodex.models import Codepoint<br>
 &gt;&gt;&gt; Codepoint.objects.filter(design&#95;&#95;image&#95;&#95;contains="png", design&#95;&#95;image&#95;&#95;startswith="design").count()<br>
37<br> 
 &gt;&gt;&gt; <w>&nbsp;</w>
---

 <div class="shell-wrap"><p class="shell-top-bar">python3.6</p><p class="shell-body">
 <ps>myrtle</ps> <dr>~/project $</dr> 
./manage.py shell<br>
Python 3.6.3 (default, Nov 9 2017, 15:58:30)<br>
[GCC 4.2.1 Compatible Apple LLVM 9.0.0 (clang-900.0.38)] on darwin<br>
Type "help", "copyright", "credits" or "license" for more information.<br>
(InteractiveConsole)<br> 
 &gt;&gt;&gt; from unicodex.models import Codepoint<br>
 &gt;&gt;&gt; Codepoint.objects.filter(design&#95;&#95;image&#95;&#95;contains="png", design&#95;&#95;image&#95;&#95;startswith="design").count()<br>
37<br> 
 &gt;&gt;&gt; from django.db import connection<w>&nbsp;</w>

Note: we can import the django database connection modele
---

 <div class="shell-wrap"><p class="shell-top-bar">python3.6</p><p class="shell-body">
 <ps>myrtle</ps> <dr>~/project $</dr> 
./manage.py shell<br>
Python 3.6.3 (default, Nov 9 2017, 15:58:30)<br>
[GCC 4.2.1 Compatible Apple LLVM 9.0.0 (clang-900.0.38)] on darwin<br>
Type "help", "copyright", "credits" or "license" for more information.<br>
(InteractiveConsole)<br> 
 &gt;&gt;&gt; from unicodex.models import Codepoint<br>
 &gt;&gt;&gt; Codepoint.objects.filter(design&#95;&#95;image&#95;&#95;contains="png", design&#95;&#95;image&#95;&#95;startswith="design").count()<br>
37<br> 
 &gt;&gt;&gt; from django.db import connection<br>
 &gt;&gt;&gt; <w>&nbsp;</w>
---

 <div class="shell-wrap"><p class="shell-top-bar">python3.6</p><p class="shell-body">
 <ps>myrtle</ps> <dr>~/project $</dr> 
./manage.py shell<br>
Python 3.6.3 (default, Nov 9 2017, 15:58:30)<br>
[GCC 4.2.1 Compatible Apple LLVM 9.0.0 (clang-900.0.38)] on darwin<br>
Type "help", "copyright", "credits" or "license" for more information.<br>
(InteractiveConsole)<br> 
 &gt;&gt;&gt; from unicodex.models import Codepoint<br>
 &gt;&gt;&gt; Codepoint.objects.filter(design&#95;&#95;image&#95;&#95;contains="png", design&#95;&#95;image&#95;&#95;startswith="design").count()<br>
37<br> 
 &gt;&gt;&gt; from django.db import connection<br>
 &gt;&gt;&gt; connection.queries[-1]<w>&nbsp;</w>

Note: and inspect the last query run against our databse


---
 <div class="shell-wrap"><p class="shell-top-bar">python3.6</p><p class="shell-body">
 <ps>myrtle</ps> <dr>~/project $</dr> 
./manage.py shell<br>
Python 3.6.3 (default, Nov 9 2017, 15:58:30)<br>
[GCC 4.2.1 Compatible Apple LLVM 9.0.0 (clang-900.0.38)] on darwin<br>
Type "help", "copyright", "credits" or "license" for more information.<br>
(InteractiveConsole)<br> 
 &gt;&gt;&gt; from unicodex.models import Codepoint<br>
 &gt;&gt;&gt; Codepoint.objects.filter(design&#95;&#95;image&#95;&#95;contains="png", design&#95;&#95;image&#95;&#95;startswith="design").count()<br>
37<br> 
 &gt;&gt;&gt; from django.db import connection<br>
 &gt;&gt;&gt; connection.queries[-1]<br>
{'sql': 'SELECT COUNT(&#42;) AS "&#95;&#95;count" FROM "unicodex_codepoint" INNER JOIN "unicodex_design" ON ("unicodex_codepoint"."id" = "unicodex_design"."codepoint_id") WHERE ("unicodex_design"."image"::text LIKE \'%png%\' AND "unicodex_design"."image"::text LIKE \'design%\')', 'time': '0.001'}<br>
 &gt;&gt;&gt; <w>&nbsp;</w>
---
<pre><code><c>&num; ORM</c>
Codepoint.objects.filter( 
&nbsp; <o>design&#95;&#95;image&#95;&#95;contains=</o>"png",
&nbsp; <o>design&#95;&#95;image&#95;&#95;startswith=</o>"design").count()<br><br><c>&dash;&dash; SQL</c><br><r>SELECT</r> <l>count</l>(<r>*</r>)
&nbsp; <r>FROM</r> from unicodex_codepoint C<br><r>&nbsp;INNER JOIN</r> unicodex_design D <r>ON</r> (<l>C</l>.<l>id <r>=</r> D</l>.<l>id</l>)<br><r>&nbsp;WHERE</r> (<l>D</l>.<l>image</l> <r>LIKE</r> '%png%'
&nbsp; &nbsp; <r>AND</r> <l>D</l>.<l>image</l> <r>LIKE</r> 'design%')

---

<pre><code><c>&num; ORM</c>
Codepoint.objects.filter( 
&nbsp; <o>design&#95;&#95;image&#95;&#95;contains=</o>"png").filter(
&nbsp; <o>design&#95;&#95;image&#95;&#95;startswith=</o>"design").count()<br><br><c>&dash;&dash; SQL</c><br><c>&dash;&dash; ??

---
 <div class="shell-wrap"><p class="shell-top-bar">python3.6</p><p class="shell-body">
 &gt;&gt;&gt; from unicodex.models import Codepoint<br>
 &gt;&gt;&gt; Codepoint.objects.filter(design&#95;&#95;image&#95;&#95;contains="png", design&#95;&#95;image&#95;&#95;startswith="design").count()<br>
37<br> 
 &gt;&gt;&gt; from django.db import connection<br>
 &gt;&gt;&gt; connection.queries[-1]<br>
{'sql': 'SELECT COUNT(&#42;) AS "&#95;&#95;count" FROM "unicodex&#95;codepoint" INNER JOIN "unicodex&#95;design" ON ("unicodex&#95;codepoint"."id" = "unicodex&#95;design"."codepoint&#95;id") WHERE ("unicodex&#95;design"."image"::text LIKE \'%png%\' AND "unicodex&#95;design"."image"::text LIKE \'design%\')', 'time': '0.001'}<br>
 &gt;&gt;&gt; <w>&nbsp;</w>
---
 <div class="shell-wrap"><p class="shell-top-bar">python3.6</p><p class="shell-body">
 &gt;&gt;&gt; from unicodex.models import Codepoint<br>
 &gt;&gt;&gt; Codepoint.objects.filter(design&#95;&#95;image&#95;&#95;contains="png", design&#95;&#95;image&#95;&#95;startswith="design").count()<br>
37<br> 
 &gt;&gt;&gt; from django.db import connection<br>
 &gt;&gt;&gt; connection.queries[-1]<br>
{'sql': 'SELECT COUNT(&#42;) AS "&#95;&#95;count" FROM "unicodex&#95;codepoint" INNER JOIN "unicodex&#95;design" ON ("unicodex&#95;codepoint"."id" = "unicodex&#95;design"."codepoint&#95;id") WHERE ("unicodex&#95;design"."image"::text LIKE \'%png%\' AND "unicodex&#95;design"."image"::text LIKE \'design%\')', 'time': '0.001'}<br>
 &gt;&gt;&gt; Codepoint.objects.filter(design&#95;&#95;image&#95;&#95;contains="png").filter(<br>
 ... design&#95;&#95;image&#95;&#95;startswith="design").count()<w>&nbsp;</w><br>

---
 <div class="shell-wrap"><p class="shell-top-bar">python3.6</p><p class="shell-body">
 &gt;&gt;&gt; from unicodex.models import Codepoint<br>
 &gt;&gt;&gt; Codepoint.objects.filter(design&#95;&#95;image&#95;&#95;contains="png", design&#95;&#95;image&#95;&#95;startswith="design").count()<br>
37<br> 
 &gt;&gt;&gt; from django.db import connection<br>
 &gt;&gt;&gt; connection.queries[-1]<br>
{'sql': 'SELECT COUNT(&#42;) AS "&#95;&#95;count" FROM "unicodex&#95;codepoint" INNER JOIN "unicodex&#95;design" ON ("unicodex&#95;codepoint"."id" = "unicodex&#95;design"."codepoint&#95;id") WHERE ("unicodex&#95;design"."image"::text LIKE \'%png%\' AND "unicodex&#95;design"."image"::text LIKE \'design%\')', 'time': '0.001'}<br>
 &gt;&gt;&gt; Codepoint.objects.filter(design&#95;&#95;image&#95;&#95;contains="png").filter(<br>
 ... design&#95;&#95;image&#95;&#95;startswith="design").count()<br>
501<br> 
 &gt;&gt;&gt; <w>&nbsp;</w>

Note: wait, what??

---
 <div class="shell-wrap"><p class="shell-top-bar">python3.6</p><p class="shell-body">
 &gt;&gt;&gt; from unicodex.models import Codepoint<br>
 &gt;&gt;&gt; Codepoint.objects.filter(design&#95;&#95;image&#95;&#95;contains="png", design&#95;&#95;image&#95;&#95;startswith="design").count()<br>
37<br> 
 &gt;&gt;&gt; from django.db import connection<br>
 &gt;&gt;&gt; connection.queries[-1]<br>
{'sql': 'SELECT COUNT(&#42;) AS "&#95;&#95;count" FROM "unicodex&#95;codepoint" INNER JOIN "unicodex&#95;design" ON ("unicodex&#95;codepoint"."id" = "unicodex&#95;design"."codepoint&#95;id") WHERE ("unicodex&#95;design"."image"::text LIKE \'%png%\' AND "unicodex&#95;design"."image"::text LIKE \'design%\')', 'time': '0.001'}<br>
 &gt;&gt;&gt; Codepoint.objects.filter(design&#95;&#95;image&#95;&#95;contains="png").filter(<br>
 ... design&#95;&#95;image&#95;&#95;startswith="design").count()<br>
501<br> 
 &gt;&gt;&gt; connection.queries[-1]<w>&nbsp;</w>

Note: let's check



---
 <div class="shell-wrap"><p class="shell-top-bar">python3.6</p><p class="shell-body">
 &gt;&gt;&gt; from django.db import connection<br>
 &gt;&gt;&gt; connection.queries[-1]<br>
{'sql': 'SELECT COUNT(&#42;) AS "&#95;&#95;count" FROM "unicodex&#95;codepoint" INNER JOIN "unicodex&#95;design" ON ("unicodex&#95;codepoint"."id" = "unicodex&#95;design"."codepoint&#95;id") WHERE ("unicodex&#95;design"."image"::text LIKE \'%png%\' AND "unicodex&#95;design"."image"::text LIKE \'design%\')', 'time': '0.001'}<br>
 &gt;&gt;&gt; Codepoint.objects.filter(design&#95;&#95;image&#95;&#95;contains="png").filter(<br>
 ... design&#95;&#95;image&#95;&#95;startswith="design").count()<br>
501<br> 
 &gt;&gt;&gt; connection.queries[-1]<br>
{'sql': 'SELECT COUNT(&#42;) AS "&#95;&#95;count" FROM "unicodex&#95;codepoint" INNER JOIN "unicodex&#95;design" ON ("unicodex&#95;codepoint"."id" = "unicodex&#95;design"."codepoint&#95;id") INNER JOIN "unicodex&#95;design" T3 ON ("unicodex&#95;codepoint"."id" = T3."codepoint&#95;id") WHERE ("unicodex&#95;design"."image"::text LIKE \'%png%\' AND T3."image"::text LIKE \'design%\')', 'time': '0.002'}<br>
 &gt;&gt;&gt; <w>&nbsp;</w>

Note: well, we can tell it's a different SQL statement than before based on the length of the output.. but let's format itnicely and see what's going on
---
<pre><code><c>&num; ORM</c>
Codepoint.objects.filter( 
&nbsp; <o>design&#95;&#95;image&#95;&#95;contains=</o>"png").filter(
&nbsp; <o>design&#95;&#95;image&#95;&#95;startswith=</o>"design").count()<br><br><c>&dash;&dash; SQL</c><br><r>SELECT</r> <l>count</l>(<r>&#42;</r>)
&nbsp; <r>FROM</r> from unicodex_codepoint C<br><r>&nbsp;INNER JOIN</r> unicodex_design D <r>ON</r> (<l>C</l>.<l>id <r>=</r> D</l>.<l>id</l>)<br><r>&nbsp;INNER JOIN</r> unicodex_design E <r>ON</r> (<l>C</l>.<l>id <r>=</r> E</l>.<l>id</l>)<br><r>&nbsp;WHERE</r> (<l>D</l>.<l>image</l> <r>LIKE</r> '%png%'
&nbsp; &nbsp; <r>AND</r> <l>E</l>.<l>image</l> <r>LIKE</r> 'design%')

Note: Ah.

We have TWO joins happening here

Every time there is a separate filter, it's another join. Which can absolutely be useful, but not when you're matching on the same associated table in both filters, as you can't join those references together.

To do that, put them both in the same filter call. Django will be able to work it out, then.
---
## So, what if the ORM doesn't do it? <!-- .slide: class="center" -->

Note: but what if you have something reeeeeally complex, that you can't easily represent in the ORM?

---
## `raw` <!-- .slide: class="center" -->
Note: If you really really really need to, you can drop down to raw SQL CODE
---
# ⚠️ <!-- .slide: class="center" -->
Note: but

but but but

You need to be careful

If you look up the docs about how to do this

---
<div class="left"><span style="font-family: Roboto">Performing raw SQL queries</span><br><br>
<rr>The raw() manager ...</rr><br/>
<br>⚠️ <rb>You should be very careful whenever you write.</rb><br>
<br>`Abc.objects.raw('SELECT * FROM myapp_abc')`<br><br>
🗒 <rr>Where did the name of the Person table come from in that example?</rr>
<br>⚠️ <rb>No checking is done on the SQL statement that is passed in to .raw().</rb>
<br>⚠️ <rb>If you are performing queries on MySQL, note that MySQL’s silent type coercion may cause unexpected results when mixing types.</rb>
<br>⚠️ <rb>While a RawQuerySet instance can be iterated over like a normal QuerySet, RawQuerySet doesn’t implement </rb><br></div>

Note: you'll see it is FULL of warnings and notes and conditions

There are specific sections in the docs about how to give raw parameterised arguments to help prevent potential SQL injection, but you should still understand how this functionality works before you try using it.

You also break the ability for your app to be used by multiple databases. Because of the differences in SQL between databases, your postgres flavoured code probably will break if someone wants to run it on an sqlite database

---
## Sometimes, the sequels are better. <!-- .slide: class="center" -->

Note: But sometimes, SQL is better

the whole point of the ORM is in the name: the Object Relational Mapper. It's all about mapping objects to relations

the ORM can do 80% of things, but if there's stuff that's easier to do in RAW self, instead of wrangling the ORM, do that instead.

---
## Discover more yourself <!-- .slide: class="center" -->
Note: I've only touched the surface of the power of the ORM

If I've caught your interest in the power of this part of django, you can learn more yourself
---
## Creating objects <!-- .slide: class="center" -->
## Field Types
## Field Relationships

Note: How to create objects, including from raw SQL

Field types - things like email fields and image fields

And more field relations, ways that you can call both codepoint attributes on a design object, and design attributes on a codepoint
---
## <fl>docs.djangoproject.com</fl> <!-- .slide: class="center" -->

Note: seriously, the docs are wonderful. Now that you know some of the general terms of this bit of software, you should be able to find more interesting ways to make the ORM work for you
---
# ☝️ <!-- .slide: class="center" -->
## <span style="color: white">`.`</span> <!-- .slide: class="center" -->
Note: Oh, and just one more note before I go
If you really want to make the ORM work well for you when developing
---

# ☝️ <!-- .slide: class="center" -->
## `echo "ipython" >> Pipfile` <!-- .slide: class="center" -->
Note: add ipython as a dev requirement in your Pipfile, or requirements.txt or whereever all good python package managers store their requirements.
---
 <div class="shell-wrap"><p class="shell-top-bar">python3.6</p><p class="shell-body">
 <ps>myrtle</ps> <dr>~/project $</dr> 
./manage.py shell<br>
Python 3.6.3 (default, Nov 9 2017, 15:58:30)<br>
[GCC 4.2.1 Compatible Apple LLVM 9.0.0 (clang-900.0.38)] on darwin<br>
Type "help", "copyright", "credits" or "license" for more information.<br>
(InteractiveConsole)<br> 
 &gt;&gt;&gt; <w>&nbsp;</w>

Note: it will turn your shell from this old and busted
---
 <div class="shell-wrap"><p class="shell-top-bar">python3.6</p><p class="shell-body">
 <ps>myrtle</ps> <dr>~/project $</dr> 
./manage.py shell<br>
Python 3.6.3 (default, Nov 9 2017, 15:58:30)<br>
Type 'copyright', 'credits' or 'license' for more information<br>
IPython 6.3.1 -- An enhanced Interactive Python. Type '?' for help.<br><br>
 <tg>In [</tg><ty>1</ty><tg>]:&nbsp;<w>&nbsp;</w>
Note: to the new hotness

This is an ipython powered shell, which means
---
 <div class="shell-wrap"><p class="shell-top-bar">python3.6</p><p class="shell-body">
 <ps>myrtle</ps> <dr>~/project $</dr> 
./manage.py shell<br>
Python 3.6.3 (default, Nov 9 2017, 15:58:30)<br>
Type 'copyright', 'credits' or 'license' for more information<br>
IPython 6.3.1 -- An enhanced Interactive Python. Type '?' for help.<br>
<br><tg>In [</tg><ty>1</ty><tg>]: from </tg><tb>uni</tb><w>&nbsp;</w>
Note: you start typing something, press tab, and
---
 <div class="shell-wrap"><p class="shell-top-bar">python3.6</p><p class="shell-body">
 <ps>myrtle</ps> <dr>~/project $</dr> 
./manage.py shell<br>
Python 3.6.3 (default, Nov 9 2017, 15:58:30)<br>
Type 'copyright', 'credits' or 'license' for more information<br>
IPython 6.3.1 -- An enhanced Interactive Python. Type '?' for help.<br>
<br><tg>In [</tg><ty>1</ty><tg>]: from </tg><tb>uni</tb><w>&nbsp;</w>
<br>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; <ww>unicodedata</ww>
<br>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; <ww>unicodex&nbsp; &nbsp;</ww>
<br>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; <ww>unittest&nbsp; &nbsp;</ww>
Note: you get autocompleted suggestions.

So cool
---

 <!-- .slide: data-background-image="pictures/hunterfound.jpg"-->


Note: 

So that's all I had. Hopefully with these tips and tricks about how to use the ORM to interact your project, you can start finding those pesky bugs you've been tasked to find.

It might be a new stack to you, it might be old school, but I find the utmost dorkish joy in finding that odd little thing in a technology stack that just a short time ago I had no idea about, and then being able to harness that power.

And being able to use your skills gained from other technology sets in new fields is really fun, sometimes a bit interesting, but always great.

---
<br> 
 <div style='width: 100%; margin: 0 auto;'><p align='center'><img height='160px' src='pictures/space.svg'><img height='160px' src='pictures/space.svg'><img height='160px' src='pictures/claps.svg'><img height='160px' src='pictures/space.svg'><img height='160px' src='pictures/space.svg'></p></div> <!-- .slide: class="center" -->
 <img src="pictures/footer.svg" />
 <span class='foot'>Some images: [WOCinTech Chat](https://www.flickr.com/photos/wocintechchat/albums)</span>

Note: thank you for your time
---
 <!-- .slide: data-background-image="pictures/pyconau18.png"-->
<h2 style="color: white; margin-top: 256px">Call for Proposals Now Open</h2>
<br><br><br> 
<h2 style="color: white; margin-top: 65px">pycon-au.org</h2>

Note: PS PyCon AU is a thing that's happening