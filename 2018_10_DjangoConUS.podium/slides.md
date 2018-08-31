<br>
#ORM: The Sequel
###DjangoCon Europe 2018
![Image](images/footer.svg)
---
class: middle, center
![Image](images/wave.svg)


???

Hi I'm Katie

---
class: middle, center, image
![Image](images/djangologo.png)


???

And I do a bunch of things in the Django community

---
class: middle, center, image
![Image](images/dceu16.png)

???

I spoke at DjangoCon Europe 16 in Budapest

---
class: middle, center, image
![Image](images/dcus17.png)

???

I was a mentor, and also gave a talk, at DjangoCon US 2017

---
class: middle, center, image
![Image](images/dcau17.png)
<style>background-image: url("images/17_bg.png");</style>

???

I was the organiser of djangocon australia 17

---

class: middle, center, image
![Image](images/divio-logo.png)


???

I'm a site reliability engineer at Divio, the company behind django-cms

---
class: middle, center, image
![Image](images/djangologo.png)

???

I'm currently serving as a Director of the Django Software Foundation

---


???

But I don't know django.


Yet.

I'man absolute novice. I have no idea what I'm doing
---
class: middle, center, image
![Image](images/djadmin.png)

???

I still see the django admin as


---
class: middle, center, image
![Image](images/djadmin_sparkles.png)

???

a magical piece of software development

---
class: middle, center, image
![Image](images/djuser_super.png)


???

I mean, the fact that this admin is just generated based on something called models..?


andit just works, it's so cool


---
<style>background-image: url("images/macbook.jpg");</style>
<span class='foot'>[WOCinTech](https://www.flickr.com/photos/wocintechchat/albums)</span>

???

But just because I'm a novice at django, doesn't mean I'm a novice at tech

---
<style>background-image: url("images/thinkpad.jpg");</style>
<span class='foot'><a href="https://www.flickr.com/photos/wocintechchat/albums" style="color:white !important">WOCinTech</a></span>


???

I have over a decade of software development and systems administration behind me.


Beforegetting into the Python/Django space, I was a ruby dev, working with Rails and Sinatra stacks

Butbefore that, around the time the magic was being removed from Django, I was in my first tech job, and using my first tech stack:

---
class: middle, center, image
![Image](images/apexlogo.png)
&nbsp;<!-- .slide: data-background-color="#f8f8f8" -->


???

Was Orale Application Express


OracleAppplication express, also known as Apex, is a in-database web application creation suite. it comes free with Oracle XE (the free version of the database)
---
<imgsrc="pictures/apex_window.png" style="margin-top: -50px; margin-left: -115px; max-width: 125%">

<span class='foot'>[StackOverflow](https://stackoverflow.com/questions/48789457/oracle-apex-version-3-2-tabindex-not-working)</span>


???

Back in 2006, this was the bees knees. An entire web GUI way to build a website based on form submissions and database manpulations. I used this for years

---
<style>background-image: url("images/apex32.jpg");</style>

???

So much so, I was a technical reviewer for a technical book on the subject.


Yes,I'm that much of a nerd.
---

#&nbsp;


???

I haven't used APEX for years. But, there's one thing that I have an intrinstic knowledge of


---

<h1 style="color: white;text-shadow: 1px 1px 6px black, 0 0 136px red, 0 0 51px yellow; font-family: arial; font-size: 200pt">SQL</h1>
<h1 style="color: white;text-shadow: 1px 1px 6px black, 0 0 136px red, 0 0 51px yellow; font-family: arial; font-size:40pt">Structured Query Language</h1>


???

SQL


It'slike riding a bike. Left outer joins are always going to be a bit.. fuzzy, but I can't count the amount of times I wished there was an option of throwing a LIKE clause on search results.


---
class: middle, center, image
![Image](images/djadmin.png)

???

Getting back to Django.


I'mstill getting my head around how Django works

Imean, sure, for a sufficiently setup existing django application, the admin makes things so intuitive.

Butif you were to try and tell me how things work underneath

---
<style>background-image: url("images/fogofwar.png");</style>


???

I would have some sort of fog of war thing going on. I can't tell what's going on.

---
##> *"Oh, just use the shell!"*

???

Even worse when I'm told "Oh, just use the shell"


It'san empty space. But I've been told that this is where the actual Django magic lives
---
<h1 style="color: white;text-shadow: 1px 1px 6px black, 0 0 136px blue, 0 0 51px green; font-family: arial; font-size: 200pt">ORM</h1>

<h1 style="color: white;text-shadow: 1px 1px 6px black, 0 0 136px blue, 0 0 51px green; font-family: arial; font-size: 40pt">Object Relational Mapper</h1>

???

The ORM


TheObject relational mapper

Theengine that makes django go

Butwithout context, what does that even mean?
---
#Context


???

Context is important.


Sofor the purposes of this, let's break away from the normal.

Anumber of tutorials start with a clean slate, and assume you have little to know dev experience. DjangoGirls is great for complete beginners to development

Butit's not so helpful for developers who come into the space with prior knowledge

It'salso not helpful for the way that I came into Django; trying to fix an existing project

Sofor the purposes of this, we're going to use an existing project
---
<style>background-image: url("images/hunterbird.jpg");</style>


???




We'regoing to be a noisy myna, and go bughunting.

We'regoing to find outselves an existing project, in this case, a field of kale, and hunt about trying to find some delicious bugs.

Thefield may look daunting, endless complexities that seem impossible to understand, but we'll get there.

---
#Context


???

so, our context today isn't going to be the standard blog site or news portal.


It'sgoing to be about something near and dear to my heart
---
#✨

???

emoji

---
class: top, image
![Image](images/unicodex_index.png)


???




Ifyou've seen my {DjangoCon EU 2016 talk,emoji talks before}

thiswebsite would be sort of familiar to you.

Icall it.. Unicodex. It's a django-backed database of different emoji from different platforms

Onthe home page there's a bunch of emoji and if you click on one

---

class: top, image
![Image](images/unicodex_sparkles_bug.png)


???

it shows you the emoji from different vendors and the versions.


Sogiven this website exists, we can start poking around in the shell
---
##"Just use the shell"

???

what they mean here is the django shell

---
<div class="shell-wrap"><p class="shell-top-bar">bash</p><p class="shell-body">
<ps>myrtle</ps> <dr>~ $</dr> 
cdproject<br>
<ps>myrtle</ps> <dr>~/project $</dr> 
./manage.py shell<w>&nbsp;</w>


???

which is available using the manage.py shell command

---
<div class="shell-wrap"><p class="shell-top-bar">python3.6</p><p class="shell-body">
<ps>myrtle</ps> <dr>~ $</dr> 
cdproject<br>
<ps>myrtle</ps> <dr>~/project $</dr> 
./manage.pyshell<br>
Python3.6.3 (default, Nov 9 2017, 15:58:30)<br>
[GCC4.2.1 Compatible Apple LLVM 9.0.0 (clang-900.0.38)] on darwin<br>
Type"help", "copyright", "credits" or "license" for more information.<br>
(InteractiveConsole)<br>
&gt;&gt;&gt;&nbsp;<w>&nbsp;</w>


???




Here,we're presented with an interactive console

Allshell is is a python environment where the django environment path has been loaded.

Fromhere you can interact with your django projet directly.

---
##"But, how do I use the shell?"
##*"..."* <!-- .element: class="fragment" -->


???

but how do I use the shell


Firstthings first. For an SQL dev, the first thing they normally do in a foreign system is
---
##Finding all tables
---
<pre><code><c>&dash;&dash;MySQL</c>
showtables

<c>&dash;&dash;PostgreSQL</c>
\dt

<c>&dash;&dash;Oracle</c>
<r>SELECT* <br>&nbsp; FROM</r> dba.tables;
</code></pre>


???

depending on which flavour of database is most familiar to you, you'd try and issue one of these commands


Formysql, for postgres, for oracle

Butwe're not in a database console, we're in the django shell. We need to use ORM codes.


---
<pre><code><c>&num;ORM</c>
<c>&num;...</c>


???

SO! To list all the tables in a project in the django shell!...


there'sno real good way.

Inorder to start querying model objects, you need to import the models

Indjango, a project has multiple applications, or apps, and an app can have one or many models.

Themodel code is the powerhouse of django. the ORM manipulates models. A lot of the logic for a django project is going to be in the model.py of it's various applications.
Butwithout looking at the model code, and understanding what you're looking at in order to generate the import statement, you can be at a complete loss.

Thankfully,django is clever and has helpful methods you can call to generate a list of imports for all the models in the project
---
<pre><code><c>#Generate import statements</c>
<r>from</r>django.apps <r>import</r> apps
&nbsp;
<r>for</r>app_config <r>in</r> apps.get_app_configs():
&nbsp;l <r>=</r> app_config.name
&nbsp;<r>for</r> model <r>in</r> app_config.get_models():
&nbsp;&nbsp; n <r>=</r> model._meta.object_name
&nbsp;&nbsp; <l>print</l>(<d>f'from</d> <l>{</l>l<l>}</l><d>.models import </d><l>{</l>n<l>}</l>')
</code></pre>


???

here's some I prepared earlier


We'regoing to import the django apps

Anditerate over all the apps that django knows about

Foreach of those, we're going to get all the models

andprint an import statement for each

---
<div class="shell-wrap"><p class="shell-top-bar">python3.6</p><p class="shell-body">
<ps>myrtle</ps> <dr>~/project $</dr> 
./manage.pyshell<br>
Python3.6.3 (default, Nov 9 2017, 15:58:30)<br>
[GCC4.2.1 Compatible Apple LLVM 9.0.0 (clang-900.0.38)] on darwin<br>
Type"help", "copyright", "credits" or "license" for more information.<br>
(InteractiveConsole)<br>
&gt;&gt;&gt;&nbsp;<w>&nbsp;</w>


???

Going back to our shell

---
<div class="shell-wrap"><p class="shell-top-bar">python3.6</p><p class="shell-body">
<ps>myrtle</ps> <dr>~/project $</dr> 
./manage.pyshell<br>
Python3.6.3 (default, Nov 9 2017, 15:58:30)<br>
[GCC4.2.1 Compatible Apple LLVM 9.0.0 (clang-900.0.38)] on darwin<br>
Type"help", "copyright", "credits" or "license" for more information.<br>
(InteractiveConsole)<br>
&gt;&gt;&gt;from django.apps import apps<br>
&gt;&gt;&gt;for app_config in apps.get_app_configs():<br>
...&nbsp;l = app_config.name<br>
...&nbsp;for model in app_config.get_models():<br>
...&nbsp;&nbsp; n = model._meta.object_name<br>
...&nbsp;&nbsp; print(f'from {l}.models import {n}')<br>
...&nbsp;<w>&nbsp;</w>


???

for now, we're just going to dump in that code and run it

---
<div class="shell-wrap"><p class="shell-top-bar">python3.6</p><p class="shell-body">
...&nbsp;l = app_config.name<br>
...&nbsp;for model in app_config.get_models():<br>
...&nbsp;&nbsp; n = model._meta.object_name<br>
...&nbsp;&nbsp; print(f'from {l}.models import {n}')<br>
...&nbsp;<br>
fromdjango.contrib.auth.models import Permission<br>
fromdjango.contrib.auth.models import Group<br>
fromdjango.contrib.auth.models import User<br>
fromdjango.contrib.contenttypes.models import ContentType<br>
fromdjango.contrib.sessions.models import Session<br>
fromdjango.contrib.sites.models import Site<br>
fromaldryn_sso.models import AldrynCloudUser<br>
fromdjango.contrib.admin.models import LogEntry<br>
fromunicodex.models import Codepoint<br>
fromunicodex.models import Vendor<br>
fromunicodex.models import VendorVersion<br>
fromunicodex.models import Design<br>
&gt;&gt;&gt;&nbsp;<w>&nbsp;</w>


???

and what we get back is some generated import statements about


Thisoutput will have similarities across django projects

thefirst few in this list are pretty standard fair; authentication, sessions, sites, admin

There'salso one in there called aldryn_sso. this is because I've hosted this on divio cloud. We're holding a workshop during the sprints on it, come see me afterwards!

Butwhat we're looking for is, in a lovely happenstance, the models that match the name of the website we saw earlier -- unicodex.
---

##Finding the table for a model
---
<pre><code>
<c>#ORM</c>
Codepoint._meta.db_table
</code></pre>
---
<div class="shell-wrap"><p class="shell-top-bar">python3.6</p><p class="shell-body">
<ps>myrtle</ps> <dr>~/project $</dr> 
./manage.pyshell<br>
Python3.6.3 (default, Nov 9 2017, 15:58:30)<br>
[GCC4.2.1 Compatible Apple LLVM 9.0.0 (clang-900.0.38)] on darwin<br>
Type"help", "copyright", "credits" or "license" for more information.<br>
(InteractiveConsole)<br>
&gt;&gt;&gt; <w>&nbsp;</w>
---
<div class="shell-wrap"><p class="shell-top-bar">python3.6</p><p class="shell-body">
<ps>myrtle</ps> <dr>~/project $</dr> 
./manage.pyshell<br>
Python3.6.3 (default, Nov 9 2017, 15:58:30)<br>
[GCC4.2.1 Compatible Apple LLVM 9.0.0 (clang-900.0.38)] on darwin<br>
Type"help", "copyright", "credits" or "license" for more information.<br>
(InteractiveConsole)<br>
&gt;&gt;&gt; from unicodex.models import Codepoint<w>&nbsp;</w>
---
<div class="shell-wrap"><p class="shell-top-bar">python3.6</p><p class="shell-body">
<ps>myrtle</ps> <dr>~/project $</dr> 
./manage.pyshell<br>
Python3.6.3 (default, Nov 9 2017, 15:58:30)<br>
[GCC4.2.1 Compatible Apple LLVM 9.0.0 (clang-900.0.38)] on darwin<br>
Type"help", "copyright", "credits" or "license" for more information.<br>
(InteractiveConsole)<br>
&gt;&gt;&gt; from unicodex.models import Codepoint<br>
&gt;&gt;&gt; <w>&nbsp;</w>
---
<div class="shell-wrap"><p class="shell-top-bar">python3.6</p><p class="shell-body">
<ps>myrtle</ps> <dr>~/project $</dr> 
./manage.pyshell<br>
Python3.6.3 (default, Nov 9 2017, 15:58:30)<br>
[GCC4.2.1 Compatible Apple LLVM 9.0.0 (clang-900.0.38)] on darwin<br>
Type"help", "copyright", "credits" or "license" for more information.<br>
(InteractiveConsole)<br>
&gt;&gt;&gt; from unicodex.models import Codepoint<br>
&gt;&gt;&gt; Codepoint._meta.db_table<w>&nbsp;</w>
---
<div class="shell-wrap"><p class="shell-top-bar">python3.6</p><p class="shell-body">
<ps>myrtle</ps> <dr>~/project $</dr> 
./manage.pyshell<br>
Python3.6.3 (default, Nov 9 2017, 15:58:30)<br>
[GCC4.2.1 Compatible Apple LLVM 9.0.0 (clang-900.0.38)] on darwin<br>
Type"help", "copyright", "credits" or "license" for more information.<br>
(InteractiveConsole)<br>
&gt;&gt;&gt; from unicodex.models import Codepoint<br>
&gt;&gt;&gt; Codepoint._meta.db_table<br>
'unicodex_codepoint'<br>
&gt;&gt;&gt; <w>&nbsp;</w>
---
##Showing all table columns
---
<pre><code><br><c>#ORM</c><br>Codepoint._meta.get_fields()
---
<div class="shell-wrap"><p class="shell-top-bar">python3.6</p><p class="shell-body">
<ps>myrtle</ps> <dr>~/project $</dr> 
./manage.pyshell<br>
Python3.6.3 (default, Nov 9 2017, 15:58:30)<br>
[GCC4.2.1 Compatible Apple LLVM 9.0.0 (clang-900.0.38)] on darwin<br>
Type"help", "copyright", "credits" or "license" for more information.<br>
(InteractiveConsole)<br>
&gt;&gt;&gt; from unicodex.models import Codepoint<br>
&gt;&gt;&gt; Codepoint._meta.db_table<br>
'unicodex_codepoint'<br>
&gt;&gt;&gt; <w>&nbsp;</w>
---
<div class="shell-wrap"><p class="shell-top-bar">python3.6</p><p class="shell-body">
<ps>myrtle</ps> <dr>~/project $</dr> 
./manage.pyshell<br>
Python3.6.3 (default, Nov 9 2017, 15:58:30)<br>
[GCC4.2.1 Compatible Apple LLVM 9.0.0 (clang-900.0.38)] on darwin<br>
Type"help", "copyright", "credits" or "license" for more information.<br>
(InteractiveConsole)<br>
&gt;&gt;&gt; from unicodex.models import Codepoint<br>
&gt;&gt;&gt; Codepoint._meta.db_table<br>
'unicodex_codepoint'<br>
&gt;&gt;&gt; Codepoint._meta.get_fields()<w>&nbsp;</w>
---
<div class="shell-wrap"><p class="shell-top-bar">python3.6</p><p class="shell-body">
<ps>myrtle</ps> <dr>~/project $</dr> 
./manage.pyshell<br>
Python3.6.3 (default, Nov 9 2017, 15:58:30)<br>
[GCC4.2.1 Compatible Apple LLVM 9.0.0 (clang-900.0.38)] on darwin<br>
Type"help", "copyright", "credits" or "license" for more information.<br>
(InteractiveConsole)<br>
&gt;&gt;&gt; from unicodex.models import Codepoint<br>
&gt;&gt;&gt; Codepoint._meta.db_table<br>
'unicodex_codepoint'<br>
&gt;&gt;&gt; Codepoint._meta.get_fields()<br>
(&lt;ManyToOneRel:unicodex.design>, <br>
&lt;django.db.models.fields.AutoField:id>, <br>
&lt;django.db.models.fields.CharField:name>, <br>
&lt;django.db.models.fields.TextField:description>,<br>
&lt;django.db.models.fields.CharField:codepoint>)<br>
&gt;&gt;&gt; <w>&nbsp;</w>
---
##Finding all tables
###via the database


???

We can find all this information directly via the database,


anddjango provides an easy way to get there
---
<div class="shell-wrap"><p class="shell-top-bar">bash</p><p class="shell-body">
<ps>myrtle</ps> <dr>~/project $</dr> 
./manage.py dbshell<w>&nbsp;</w>


???

back in our terminal, instead of running manage.py shell, we run DB shell

---
<div class="shell-wrap"><p class="shell-top-bar">psql</p><p class="shell-body">
<ps>myrtle</ps> <dr>~/project $</dr> 
./manage.pydbshell<br>
psql(9.6.5, server 9.6.8)<br>
Type"help" for help.<br>
<br>
db=#&nbsp;<w>&nbsp;</w>


???

and we get an output that will be familiar to postgres devs in the audience


Thisparticular project has a postgres backend
---
<div class="shell-wrap"><p class="shell-top-bar">psql</p><p class="shell-body">
<ps>myrtle</ps> <dr>~/project $</dr> 
./manage.pydbshell<br>
psql(9.6.5, server 9.6.8)<br>
Type"help" for help.<br>
<br>
db=# \dt<w>&nbsp;</w>


???

given we know it's postgres, we cna issue the postgres list table command, and get back

---
<div class="shell-wrap"><p class="shell-top-bar">psql</p><p class="shell-body">
&nbsp;&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; List of relations<br>
&nbsp;Schema|&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; Name&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; | Type&nbsp; |&nbsp; Owner<br>
&dash;&dash;&dash;&dash;&dash;&dash;&dash;&dash;+&dash;&dash;&dash;&dash;&dash;&dash;&dash;&dash;&dash;&dash;&dash;&dash;&dash;&dash;&dash;&dash;&dash;&dash;&dash;&dash;&dash;&dash;&dash;&dash;&dash;&dash;&dash;&dash;+&dash;&dash;&dash;&dash;&dash;&dash;&dash;+&dash;&dash;&dash;&dash;&dash;&dash;&dash;&dash;&dash;&dash;<br>
&nbsp;public| aldryn_sso_aldrynclouduser | table | postgres<br>
&nbsp;public| auth_group&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;&nbsp; | table | postgres<br>
&nbsp;public| auth_group_permissions&nbsp; &nbsp; &nbsp;| table | postgres<br>
&nbsp;public| auth_permission&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; | table | postgres<br>
&nbsp;public| auth_user&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; | table | postgres<br>
&nbsp;public| auth_user_groups&nbsp; &nbsp; &nbsp; &nbsp;&nbsp; &nbsp; | table | postgres<br>
&nbsp;public| auth_user_user_permissions | table | postgres<br>
&nbsp;public| django_admin_log&nbsp; &nbsp;&nbsp; &nbsp; &nbsp; &nbsp; | table | postgres<br>
&nbsp;public| django_content_type&nbsp; &nbsp; &nbsp; &nbsp; | table | postgres<br>
&nbsp;public&nbsp;|&nbsp;django_migrations&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|&nbsp;table&nbsp;|&nbsp;postgres<br.
&nbsp;public&nbsp;|&nbsp;django_session&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|&nbsp;table&nbsp;|&nbsp;postgres<br>
&nbsp;public&nbsp;|&nbsp;django_site&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|&nbsp;table&nbsp;|&nbsp;postgres<br>
&nbsp;public&nbsp;|&nbsp;unicodex_codepoint&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|&nbsp;table&nbsp;|&nbsp;postgres<br>
&nbsp;public&nbsp;|&nbsp;unicodex_design&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|&nbsp;table&nbsp;|&nbsp;postgres<br>
&nbsp;public&nbsp;|&nbsp;unicodex_vendor&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|&nbsp;table&nbsp;|&nbsp;postgres<br>
&dash;&dash;More&dash;&dash;


???

all our tables. Note the usual suspects from earlier, auth, content, sites

---
<div class="shell-wrap"><p class="shell-top-bar">psql</p><p class="shell-body">
&nbsp;public| aldryn_sso_aldrynclouduser | table | postgres<br>
&nbsp;public| auth_group&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;&nbsp; | table | postgres<br>
&nbsp;public| auth_group_permissions&nbsp; &nbsp; &nbsp;| table | postgres<br>
&nbsp;public| auth_permission&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; | table | postgres<br>
&nbsp;public| auth_user&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; | table | postgres<br>
&nbsp;public| auth_user_groups&nbsp; &nbsp; &nbsp; &nbsp;&nbsp; &nbsp; | table | postgres<br>
&nbsp;public| auth_user_user_permissions | table | postgres<br>
&nbsp;public| django_admin_log&nbsp; &nbsp;&nbsp; &nbsp; &nbsp; &nbsp; | table | postgres<br>
&nbsp;public| django_content_type&nbsp; &nbsp; &nbsp; &nbsp; | table | postgres<br>
&nbsp;public&nbsp;|&nbsp;django_migrations&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|&nbsp;table&nbsp;|&nbsp;postgres<br.
&nbsp;public&nbsp;|&nbsp;django_session&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|&nbsp;table&nbsp;|&nbsp;postgres<br>
&nbsp;public&nbsp;|&nbsp;django_site&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|&nbsp;table&nbsp;|&nbsp;postgres<br>
&nbsp;public&nbsp;|&nbsp;unicodex_codepoint&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|&nbsp;table&nbsp;|&nbsp;postgres<br>
&nbsp;public&nbsp;|&nbsp;unicodex_design&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|&nbsp;table&nbsp;|&nbsp;postgres<br>
&nbsp;public&nbsp;|&nbsp;unicodex_vendor&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|&nbsp;table&nbsp;|&nbsp;postgres<br>
&nbsp;public&nbsp;|&nbsp;unicodex_vendorversion&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|&nbsp;table&nbsp;|&nbsp;postgres<br>
(16rows)<br>
<br>
db=#&nbsp;<w>&nbsp;</w>


???

but also, our own project's tables


We'lltake note of these for later.
---
##Show all table contents


???

so now that we know there are tables, we'd like to see what's inside them

---
<pre><code>
<c>&dash;&dash;SQL</c>
<r>SELECT* <br>&nbsp; FROM</r> unicodex_codepoint;
<br><br>
</code></pre>


???

in SQL, this would be your standard select star from table

---
<pre><code>
<c>&dash;&dash;SQL</c>
<r>SELECT* <br>&nbsp; FROM</r> unicodex_codepoint;

<c>&num;ORM</c>
Codepoint.objects.all()
</code></pre>


???

in the ORM, this maps to Codepoint, the model, dot objects dot all


Justlist all of them
---
<div class="shell-wrap"><p class="shell-top-bar">python3.6</p><p class="shell-body">
<ps>myrtle</ps> <dr>~/project $</dr> 
./manage.pyshell<br>
Python3.6.3 (default, Nov 9 2017, 15:58:30)<br>
[GCC4.2.1 Compatible Apple LLVM 9.0.0 (clang-900.0.38)] on darwin<br>
Type"help", "copyright", "credits" or "license" for more information.<br>
(InteractiveConsole)<br>
&gt;&gt;&gt; <w>&nbsp;</w>

???

back over in our console, before we can call Codepoint, we need to use that import statement we generated earlier

---
<div class="shell-wrap"><p class="shell-top-bar">python3.6</p><p class="shell-body">
<ps>myrtle</ps> <dr>~/project $</dr> 
./manage.pyshell<br>
Python3.6.3 (default, Nov 9 2017, 15:58:30)<br>
[GCC4.2.1 Compatible Apple LLVM 9.0.0 (clang-900.0.38)] on darwin<br>
Type"help", "copyright", "credits" or "license" for more information.<br>
(InteractiveConsole)<br>
&gt;&gt;&gt; from unicodex.models import Codepoint<w>&nbsp;</w>


???

from unicodex dot models import codepoint

---
<div class="shell-wrap"><p class="shell-top-bar">python3.6</p><p class="shell-body">
<ps>myrtle</ps> <dr>~/project $</dr> 
./manage.pyshell<br>
Python3.6.3 (default, Nov 9 2017, 15:58:30)<br>
[GCC4.2.1 Compatible Apple LLVM 9.0.0 (clang-900.0.38)] on darwin<br>
Type"help", "copyright", "credits" or "license" for more information.<br>
(InteractiveConsole)<br>
&gt;&gt;&gt; from unicodex.models import Codepoint<br>
&gt;&gt;&gt; <w>&nbsp;</w>


???

after we hit enter, we'll get no output, which is good, because this was successfully imported.

---
<div class="shell-wrap"><p class="shell-top-bar">python3.6</p><p class="shell-body">
<ps>myrtle</ps> <dr>~/project $</dr> 
./manage.pyshell<br>
Python3.6.3 (default, Nov 9 2017, 15:58:30)<br>
[GCC4.2.1 Compatible Apple LLVM 9.0.0 (clang-900.0.38)] on darwin<br>
Type"help", "copyright", "credits" or "license" for more information.<br>
(InteractiveConsole)<br>
&gt;&gt;&gt; from unicodex.models import Codepoint<br>
&gt;&gt;&gt; Codepoint.objects.all()<w>&nbsp;</w>


???

then we make our codepoint dot objects dot all call

---
<div class="shell-wrap"><p class="shell-top-bar">python3.6</p><p class="shell-body">
<ps>myrtle</ps> <dr>~/project $</dr> 
./manage.pyshell<br>
Python3.6.3 (default, Nov 9 2017, 15:58:30)<br>
[GCC4.2.1 Compatible Apple LLVM 9.0.0 (clang-900.0.38)] on darwin<br>
Type"help", "copyright", "credits" or "license" for more information.<br>
(InteractiveConsole)<br>
&gt;&gt;&gt; from unicodex.models import Codepoint<br>
&gt;&gt;&gt; Codepoint.objects.all()<br>
&lt;QuerySet[&lt;Codepoint: Sparkles>, &lt;Codepoint: Unicorn>, &lt;Codepoint: Castle>]><br>
&gt;&gt;&gt; <w>&nbsp;</w>


???

and we get back a queryset of objects


Weremember from earlier that there were sparkles, unicorns and hearts on our page, so we're getting the right data!

Thereturn value here is known as a queryset, an unordered objects. QuerySets can be enacted upon further, which we'll see later.


**Queryset is not a list**

---
##Show specific table contents


???

now that we can see all the things, how about just some of the things

---
<pre><code>
<c>&dash;&dash;SQL</c>
<r>SELECT* <br>&nbsp; FROM</r> unicodex_codepoint c<br>&nbsp;<r>WHERE</r> <l>c</l>.<l>name</l> <r>=</r> <d>'Sparkles'</d>;
<br><br>
</code></pre>


???

the SQL would be familiar


Addinga where clause for, say, sparkles
---
<pre><code>
<c>&dash;&dash;SQL</c>
<r>SELECT* <br>&nbsp; FROM</r> unicodex_codepoint c<br>&nbsp;<r>WHERE</r> <l>c</l>.<l>name</l> <r>&equals;</r> <d>'Sparkles'</d>;

<c>&num;ORM</c>
Codepoint.objects.filter(<o>name&equals;</o>'Sparkles')
</code></pre>


???

this maps to the ORM as filter. where the name column is a keyword argument of filter.



---
<div class="shell-wrap"><p class="shell-top-bar">python3.6</p><p class="shell-body">
&gt;&gt;&gt; from unicodex.models import Codepoint<br>
&gt;&gt;&gt; Codepoint.objects.filter(name='Sparkles')<w>&nbsp;</w>


???

so in our fresh terminal, we import Codepoint


Thenrun our filter
---
<div class="shell-wrap"><p class="shell-top-bar">python3.6</p><p class="shell-body">
&gt;&gt;&gt; from unicodex.models import Codepoint<br>
&gt;&gt;&gt; Codepoint.objects.filter(name='Sparkles')<br>
&lt;QuerySet[&lt;Codepoint: Sparkles>]><br>
&gt;&gt;&gt; <w>&nbsp;</w>

???

and we get back a queryset with a single object: sparkles

---
##Get specific record


???

we can also just return one specific record, instead of a queryset

---
<div class="shell-wrap"><p class="shell-top-bar">python3.6</p><p class="shell-body">
&gt;&gt;&gt; from unicodex.models import Codepoint<br>
&gt;&gt;&gt; Codepoint.objects.filter(name='Sparkles')<br>
&lt;QuerySet[&lt;Codepoint: Sparkles>]><br>
&gt;&gt;&gt; Codepoint.objects.get(name='Sparkles')<w>&nbsp;</w>

???

so where last time we used filter


Thistime we use get
---
<div class="shell-wrap"><p class="shell-top-bar">python3.6</p><p class="shell-body">
&gt;&gt;&gt; from unicodex.models import Codepoint<br>
&gt;&gt;&gt; Codepoint.objects.filter(name='Sparkles')<br>
&lt;QuerySet[&lt;Codepoint: Sparkles>]><br>
&gt;&gt;&gt; Codepoint.objects.get(name='Sparkles')<br>
&lt;Codepoint:Sparkles><br>
&gt;&gt;&gt; <w>&nbsp;</w>


???

and we get a single object

---
<div class="shell-wrap"><p class="shell-top-bar">python3.6</p><p class="shell-body">
&gt;&gt;&gt; from unicodex.models import Codepoint<br>
&gt;&gt;&gt; Codepoint.objects.filter(name='Sparkles')<br>
&lt;QuerySet[&lt;Codepoint: Sparkles>]><br>
&gt;&gt;&gt; Codepoint.objects.get(name='Sparkles')<br>
&lt;Codepoint:Sparkles><br>
&gt;&gt;&gt; Codepoint.objects.get()<w>&nbsp;</w>


???

a thing to note about get


Getwill always return one and only one object

THERECAN BE ONLY ONE

Soif you try and run get, say, without any limiatations
---
<div class="shell-wrap"><p class="shell-top-bar">python3.6</p><p class="shell-body">
&gt;&gt;&gt; from unicodex.models import Codepoint<br>
&gt;&gt;&gt; Codepoint.objects.filter(name='Sparkles')<br>
&lt;QuerySet[&lt;Codepoint: Sparkles>]><br>
&gt;&gt;&gt; Codepoint.objects.get(name='Sparkles')<br>
&lt;Codepoint:Sparkles><br>
&gt;&gt;&gt; Codepoint.objects.get()<br>
Traceback(most recent call last):<br>
&nbsp;File "&lt;console>", line 1, in &lt;module><br>
&nbsp;File "/usr/local/lib/python3.6/site-packages/django/db/models/manager.p y", line 85, in manager_method<br>
&nbsp;&nbsp; return getattr(self.get_queryset(), name)(&#42;args, &#42;&#42;kwargs)<br>
&nbsp;File "/usr/local/lib/python3.6/site-packages/django/db/models/query.py" , line 384, in get<br>
&nbsp;&nbsp; (self.model._meta.object_name, num)<br>
unicodex.models.MultipleObjectsReturned:get() returned more than one Codepoint -- it returned 3!<br>
&gt;&gt;&gt; <w>&nbsp;</w>


???

we get a MultipleObjectsReturned error


whichtells us that it would have returned three Codepoint objects, which is just far too much for get to handle.
---
##Joins


???

So now we come to the fun bit. Joins


Anyonewho's worked with SQL for long enough will know the venn diagrams for inner joins, outer joins, left joins, right joins, and it can get a bit confusing

Thankfully,especially for someone like me who has forgotten so much SQL, the ORM makes joins a joy.
---
<pre><code><c>&dash;&dash;SQL</c><br><r>SELECT</r> d.<r>*</r> <br>&nbsp; <r>FROM</r> unicodex_codepoint c,<br>&nbsp; &nbsp; &nbsp; &nbsp;unicodex_design d<br>&nbsp;<r>WHERE</r> <l>c</l>.<l>name</l> <r>&equals;</r> <d>'Sparkles'</d><BR><r>&nbsp; &nbsp;AND</r> <l>d</l>.<l>codepoint_id</l> <r>=</r> <l>c</l>.<l>id</l>;

???

say we want to join our design and codepoint tables


Acodepoint has multiple designs. Sparkles has an image that shows up in Android, Apple, Facebook, etc

Sowe want to join on the codepoint_id on the designs table to the primary codepoint id

Thisis a good chunk of SQL

Sowhat does the ORM equivelent look like?
---
<pre><code><c>&dash;&dash;SQL</c><br><r>SELECT</r> d.<r>*</r> <br>&nbsp; <r>FROM</r> unicodex_codepoint c,<br>&nbsp; &nbsp; &nbsp; &nbsp;unicodex_design d<br>&nbsp;<r>WHERE</r> <l>c</l>.<l>name</l> <r>&equals;</r> <d>'Sparkles'</d><BR><r>&nbsp; &nbsp;AND</r> <l>d</l>.<l>codepoint_id</l> <r>=</r> <l>c</l>.<l>id</l>;<br><br><c>&num; ORM</c>
Design.objects.filter(<o>codepoint&#95;&#95;name&equals;</o>'Sparkles')
</code></pre>

???

Design dot objects dot filter codepoint dunder name equals sparkles.


Iknow right? so simple!
---
<pre><code><c>&dash;&dash;SQL</c><br><r>SELECT</r> d.<r>*</r> <br>&nbsp; <r>FROM</r> unicodex_codepoint c,<br>&nbsp; &nbsp; &nbsp; &nbsp;unicodex_design d<br>&nbsp;<r>WHERE</r> <l>c</l>.<l>name</l> <r>&equals;</r> <d>'Sparkles'</d><BR><r>&nbsp; &nbsp;AND</r> <l>d</l>.<l>codepoint_id</l> <r>=</r> <l>c</l>.<l>id</l>;<br><br><c>&num; ORM</c>
Design.objects.filter(<o>codepoint&#95;&#95;name&equals;</o>'Sparkles')
&nbsp;&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; <c>^^</c>
</code></pre>


???

this doubleunderscore here is doing a lot of powerful things behind the scenes


whichI'll explain more in a moment.

---
<div class="shell-wrap"><p class="shell-top-bar">python3.6</p><p class="shell-body">
&gt;&gt;&gt; <w>&nbsp;</w>


???

back to our terminal again, to execute this elegant little code snippet


Weimport the design model this time
---
<div class="shell-wrap"><p class="shell-top-bar">python3.6</p><p class="shell-body">
&gt;&gt;&gt; from unicodex.models import Design<w>&nbsp;</w>
---
<div class="shell-wrap"><p class="shell-top-bar">python3.6</p><p class="shell-body">
&gt;&gt;&gt; from unicodex.models import Design<br>
&gt;&gt;&gt; <w>&nbsp;</w>
---

<div class="shell-wrap"><p class="shell-top-bar">python3.6</p><p class="shell-body">
&gt;&gt;&gt; from unicodex.models import Design<br>
&gt;&gt;&gt; Design.objects.filter(codepoint&#95;&#95;name='Sparkles')<w>&nbsp;</w>

???

and we run our filter

---
<div class="shell-wrap"><p class="shell-top-bar">python3.6</p><p class="shell-body">
&gt;&gt;&gt; from unicodex.models import Design<br>
&gt;&gt;&gt; Design.objects.filter(codepoint&#95;&#95;name='Sparkles')<br>
&lt;QuerySet[&lt;Design: Sparkles Apple iOS 10.2>, &lt;Design: Sparkles Apple iOS 6.0>, &lt;Design: Sparkles Android 8.1>, &lt;Design: Sparkles Android 4.4>, &lt;Design: Sparkles Android 4.3>, &lt;Design: Sparkles Microsoft Windows 10>, &lt;Design: Sparkles Microsoft Windows 8.0>, &lt;Design: Sparkles Microsoft Windows 8.1>, &lt;Design: Sparkles Twitter 2.4>, &lt;Design: Sparkles EmojiOne 3.0>, &lt;Design: Sparkles EmojiOne 2.0>, &lt;Design: Sparkles EmojiOne 1.0>, &lt;Design: Sparkles Facebook 2.2>, &lt;Design: Sparkles Facebook 1.0>, &lt;Design: Sparkles Messenger 1.0>, &lt;Design: Sparkles WhatsApp 2.17>, &lt;Design: Sparkles Mozilla Firefox OS 2.5>, &lt;Design: Sparkles Twitter 1.0>]><br>
&gt;&gt;&gt; <w>&nbsp;</w>



???




---
<pre><code><c>&num;ORM</c>
Design.objects.filter(<o>codepoint&#95;&#95;name&equals;</o>'Sparkles')

<c>&num;field, field, field... lookup</c>


???

what we have here is one or more fields and then a lookup, all separated by double underscores


Alookup as an operation on that field

Ifyou remember back when we looked up the fields on a model, we know what options we have here.
---
<div class="shell-wrap"><p class="shell-top-bar">python3.6</p><p class="shell-body">
&gt;&gt;&gt; from unicodex.models import Design<br>
&gt;&gt;&gt; Design._meta.get_fields()<w>&nbsp;</w>
---
<div class="shell-wrap"><p class="shell-top-bar">python3.6</p><p class="shell-body">
&gt;&gt;&gt; from unicodex.models import Design<br>
&gt;&gt;&gt; Design._meta.get_fields()<br>
(&lt;django.db.models.fields.AutoField:id>,<br>
&lt;django.db.models.fields.related.ForeignKey:vendorversion>, <br>
&lt;django.db.models.fields.related.ForeignKey:codepoint>, <br>
&lt;django.db.models.fields.files.FileField:image>)<br>
&gt;&gt;&gt; <w>&nbsp;</w>


???

we have four fields - a unique id, two foreign keys off to other models, and image


butname isn't there. That came from codepoint

---
<div class="shell-wrap"><p class="shell-top-bar">python3.6</p><p class="shell-body">
&gt;&gt;&gt; from unicodex.models import Design<br>
&gt;&gt;&gt; Design._meta.get_fields()<br>
(&lt;django.db.models.fields.AutoField:id>,<br>
&lt;django.db.models.fields.related.ForeignKey:vendorversion>, <br>
&lt;django.db.models.fields.related.ForeignKey:codepoint>, <br>
&lt;django.db.models.fields.files.FileField:image>)<br>
&gt;&gt;&gt; Codepoint._meta.get_fields()<w>&nbsp;</w>


???

so if we inspect Codepoint


---
<div class="shell-wrap"><p class="shell-top-bar">python3.6</p><p class="shell-body">
&gt;&gt;&gt; from unicodex.models import Design<br>
&gt;&gt;&gt; Design._meta.get_fields()<br>
(&lt;django.db.models.fields.AutoField:id>,<br>
&lt;django.db.models.fields.related.ForeignKey:vendorversion>, <br>
&lt;django.db.models.fields.related.ForeignKey:codepoint>, <br>
&lt;django.db.models.fields.files.FileField:image>)<br>
&gt;&gt;&gt; Codepoint._meta.get_fields()<br>
(&lt;ManyToOneRel:unicodex.design>, <br>
&lt;django.db.models.fields.AutoField:id>,<br>
&lt;django.db.models.fields.CharField:name>, <br>
&lt;django.db.models.fields.TextField:description>,<br>
&lt;django.db.models.fields.CharField:codepoint>)<br>
&gt;&gt;&gt; <w>&nbsp;</w>


???

WE see that codepoint has the name field

---
<pre><code><c>&num;ORM</c>
Design.objects.filter(<o>codepoint&#95;&#95;name&equals;</o>'Sparkles')<br><br><c>&num;field, field, field... lookup</c>


???

You'll also note in our example that we end on a field.


Bydefault the look up is an exact match on the string. So effectively, name equals sparkles
---
<pre><code><c>&num;ORM</c>
Design.objects.filter(<o>codepoint&#95;&#95;name&equals;</o>'Sparkles')<br><br><c>&num;field, field, field... lookup</c>
<br><c>&num;ORM</c>
Design.objects.filter(<o>codepoint&#95;&#95;name&#95;&#95;exact&equals;</o>'Sparkles')


???

so by default what we're calling is codepoint name equals

---
#Aside


???

as aside, did you know that this is how those awesome admin filters work? it's true!

---
class: top, image
![Image](images/djuser_super.png)

???

if we go back to that admin page we saw right at the start

---
class: top, image
![Image](images/djuser_super_h.png)

???




Lookat the URL

It'sour filters

theadmin uses field lookups in it's UI

andto some extent, you can handcode this URL to do some basic filtering, even if there isn't any filters on the right hand side panel

---
<div class="shell-wrap"><p class="shell-top-bar">python3.6</p><p class="shell-body">
&gt;&gt;&gt; from unicodex.models import Design<br>
&gt;&gt;&gt; Design._meta.get_fields()<br>
(&lt;django.db.models.fields.AutoField:id>,<br>
&lt;django.db.models.fields.related.ForeignKey:vendorversion>, <br>
&lt;django.db.models.fields.related.ForeignKey:codepoint>, <br>
&lt;django.db.models.fields.files.FileField:image>)<br>
&gt;&gt;&gt; Codepoint._meta.get_fields()<br>
(&lt;ManyToOneRel:unicodex.design>, <br>
&lt;django.db.models.fields.AutoField:id>,<br>
&lt;django.db.models.fields.CharField:name>, <br>
&lt;django.db.models.fields.TextField:description>,<br>
&lt;django.db.models.fields.CharField:codepoint>)<br>
&gt;&gt;&gt; <w>&nbsp;</w>


???




backto our terminal

Wecan also forge a path down a different series of foreign keys

Seethe vendorversion there? Let's see what that contains
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



???

let's refresh our terminal and inspect VendorVersion


---
<div class="shell-wrap"><p class="shell-top-bar">python3.6</p><p class="shell-body">
&gt;&gt;&gt; from unicodex.models import VendorVersion<br>
&gt;&gt;&gt; VendorVersion._meta.get_fields()<br>
(&lt;ManyToOneRel:unicodex.design>,<br>
&lt;django.db.models.fields.AutoField:id>, <br>
&lt;django.db.models.fields.CharField:name>, <br>
&lt;django.db.models.fields.related.ForeignKey:vendor>)<br>
&gt;&gt;&gt; <w>&nbsp;</w>


???

Okay, so a vendorversion has many designs, an ID, a name, and a Vendor FK


Whatabout Vendor?
---
<div class="shell-wrap"><p class="shell-top-bar">python3.6</p><p class="shell-body">
&gt;&gt;&gt; from unicodex.models import VendorVersion<br>
&gt;&gt;&gt; VendorVersion._meta.get_fields()<br>
(&lt;ManyToOneRel:unicodex.design>,<br>
&lt;django.db.models.fields.AutoField:id>, <br>
&lt;django.db.models.fields.CharField:name>, <br>
&lt;django.db.models.fields.related.ForeignKey:vendor>)<br>
&gt;&gt;&gt; from unicodex.models import Vendor<w>&nbsp;</w>

---
<div class="shell-wrap"><p class="shell-top-bar">python3.6</p><p class="shell-body">
&gt;&gt;&gt; from unicodex.models import VendorVersion<br>
&gt;&gt;&gt; VendorVersion._meta.get_fields()<br>
(&lt;ManyToOneRel:unicodex.design>,<br>
&lt;django.db.models.fields.AutoField:id>, <br>
&lt;django.db.models.fields.CharField:name>, <br>
&lt;django.db.models.fields.related.ForeignKey:vendor>)<br>
&gt;&gt;&gt; from unicodex.models import Vendor<br>
&gt;&gt;&gt; <w>&nbsp;</w>
---
<div class="shell-wrap"><p class="shell-top-bar">python3.6</p><p class="shell-body">
&gt;&gt;&gt; from unicodex.models import VendorVersion<br>
&gt;&gt;&gt; VendorVersion._meta.get_fields()<br>
(&lt;ManyToOneRel:unicodex.design>,<br>
&lt;django.db.models.fields.AutoField:id>, <br>
&lt;django.db.models.fields.CharField:name>, <br>
&lt;django.db.models.fields.related.ForeignKey:vendor>)<br>
&gt;&gt;&gt; from unicodex.models import Vendor<br>
&gt;&gt;&gt; Vendor._meta.get_fields()<w>&nbsp;</w>



???

clear our terminal, import Vendor, and check


---
<div class="shell-wrap"><p class="shell-top-bar">python3.6</p><p class="shell-body">
&gt;&gt;&gt; from unicodex.models import VendorVersion<br>
&gt;&gt;&gt; VendorVersion._meta.get_fields()<br>
(&lt;ManyToOneRel:unicodex.design>,<br>
&lt;django.db.models.fields.AutoField:id>, <br>
&lt;django.db.models.fields.CharField:name>, <br>
&lt;django.db.models.fields.related.ForeignKey:vendor>)<br>
&gt;&gt;&gt; from unicodex.models import Vendor<br>
&gt;&gt;&gt; Vendor._meta.get_fields()<br>
(&lt;ManyToOneRel:unicodex.vendorversion>, <br>
&lt;django.db.models.fields.AutoField:id>, <br>
&lt;django.db.models.fields.CharField:name>) <br>
&gt;&gt;&gt; <w>&nbsp;</w>


???

so vendor has a relationship with vendorversion, an id and a name too


Andthus, we have exhausted our search, and we could build up a UML diagram showing the relationships between all the tables in this app

ButI woldn't do that too you.

Backto what we were doing, showing filter walks

---

<div class="shell-wrap"><p class="shell-top-bar">python3.6</p><p class="shell-body">
&gt;&gt;&gt; <w>&nbsp;</w>


???

clearing our terminal again with Control L

---
<div class="shell-wrap"><p class="shell-top-bar">python3.6</p><p class="shell-body">
&gt;&gt;&gt; Design.objects.filter(<w>&nbsp;</w>


???

we have a number of options here. Let's build the longest chain we can...


---
<div class="shell-wrap"><p class="shell-top-bar">python3.6</p><p class="shell-body">
&gt;&gt;&gt; Design.objects.filter(vendorversion<w>&nbsp;</w>


???

Let's filter design objects where... the linked vendor version


---

<div class="shell-wrap"><p class="shell-top-bar">python3.6</p><p class="shell-body">
&gt;&gt;&gt; Design.objects.filter(vendorversion&#95;&#95;vendor<w>&nbsp;</w>



???

and the vendor linked to that....


---
<div class="shell-wrap"><p class="shell-top-bar">python3.6</p><p class="shell-body">
&gt;&gt;&gt; Design.objects.filter(vendorversion&#95;&#95;vendor&#95;&#95;name<w>&nbsp;</w>


???

the name of that vendor


---


<div class="shell-wrap"><p class="shell-top-bar">python3.6</p><p class="shell-body">
&gt;&gt;&gt; Design.objects.filter(vendorversion&#95;&#95;vendor&#95;&#95;name&#95;&#95;contains=<w>&nbsp;</w>


???

contains...

---

<div class="shell-wrap"><p class="shell-top-bar">python3.6</p><p class="shell-body">
&gt;&gt;&gt; Design.objects.filter(vendorversion&#95;&#95;vendor&#95;&#95;name&#95;&#95;contains="Micro")<w>&nbsp;</w>


???

the string Micro

---

<div class="shell-wrap"><p class="shell-top-bar">python3.6</p><p class="shell-body">
&gt;&gt;&gt; Design.objects.filter(vendorversion&#95;&#95;vendor&#95;&#95;name&#95;&#95;contains="Micro")<br>
&lt;QuerySet[&lt;Design: Sparkles Microsoft Windows 8.0>, &lt;Design: Castle Microsoft Windows 8.0>, &lt;Design: Sparkles Microsoft Windows 8.1>, &lt;Design: Castle Microsoft Windows 8.1>, &lt;Design: Sparkles Microsoft Windows 10>, &lt;Design: Unicorn Microsoft Windows 10>, &lt;Design: Castle Microsoft Windows 10>]><br>
&gt;&gt;&gt; <w>&nbsp;</w>


???

And thus, we get a of all designs where the name of the linked vendor contains Micro


---
<pre><code><c>&num;Field Lookups</c><table>
<tr><td><l>contains</l></td><td><o>LIKE"%?%"</o></td></tr>
<tr><td><l>startswith</l></td><td><o>LIKE"?%"</o></td></tr>
<tr><td><l>endswith</l></td><td><o>LIKE"%?"</o></td></tr>
<tr><td><l>in</l></td><td><o>IN(?, ?, ?, ...)</o></td></tr>
<tr><td><l>lt,le, gt, ge</l></td><td><o>&lt;, &lt;=, &gt;, &gt;=</o></td></tr>
<tr><td><l>range</l></td><td><o>BETWEEN</o></td></tr>
<tr><td><l>isnull</l></td><td><o>NULL</o></td></tr></table><c>&num;... and many more!</c>
<spanclass="bfoot" style="margin-bottom: -270px"><fl>[docs - querysets field lookups](https://docs.djangoproject.com/en/2.0/ref/models/querysets/#field-lookups)</fl></span>


???

There are other field lookups we can use for a number of differnt things.


We'realso not just limited to one filter, we can have more than one
---

<div class="shell-wrap"><p class="shell-top-bar">python3.6</p><p class="shell-body">
&gt;&gt;&gt; Design.objects.filter(vendorversion&#95;&#95;vendor&#95;&#95;name&#95;&#95;contains="Micro"<w>&nbsp;</w>


???

instead of just filtering on Micro, we could alos

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
... &nbsp; codepoint&#95;&#95;name&#95;&#95;endswith="corn")<w>&nbsp;</w><br>


---
<div class="shell-wrap"><p class="shell-top-bar">python3.6</p><p class="shell-body">
&gt;&gt;&gt; Design.objects.filter(vendorversion&#95;&#95;vendor&#95;&#95;name&#95;&#95;contains="Micro",<br>
... &nbsp; codepoint&#95;&#95;name&#95;&#95;endswith="corn")<br>
&lt;QuerySet[&lt;Design: Unicorn Microsoft Windows 10>]><br>
&gt;&gt;&gt; <w>&nbsp;</w>


???

we get list of designs both from a vendor

---
##... `AND`?

???




Sofar we've dealt with single or chained filters, which will AND together

nameequals sparkles AND image ends with png AND AND AND

Ifwe want to start using OR, we need to get a bit fancy
---
#`Q`


???

This is where Q comes in


No,not the race from the great Star Trek sequel, The Next Generation,

Qand in Query

WithQ, we can build up AND, OR, and NOT statements in our where clause when filtering objects

So,let's start some comparisons...
---
<pre><code><c>&num;ORM</c>
Codepoint.objects.filter(
&nbsp;<o>name=</o>'Sparkles',
&nbsp;<o>description=</o>'Shiny!'
)



???

instead of using our super long chaining filter, let's use a simpler example here

thisquery would give us codepoints named sparkles with the description shiny

---
<pre><code><c>&num;ORM</c>
Codepoint.objects.filter(
&nbsp;<o>name=</o>'Sparkles',
&nbsp;<o>description=</o>'Shiny!'
)<br><br><c>&dash;&dash;SQL</c><br><r>SELECT *
&nbsp;FROM</r> unicodex_codepoint c <br><r>&nbsp;WHERE</r> <l>c</l>.<l>name</l> <r>=</r> <d>'Sparkles'</d><br><r>&nbsp; &nbsp;AND</r> <l>c</l>.<l>description</l> <r>=</r> <d>'Shiny!'</d>


???

this would be the equvilent SQL

---
<pre><code><c>&num;ORM</c>
Codepoint.objects.filter(
&nbsp;<o>name&#95;&#95;exact=</o>'Sparkles',
&nbsp;<o>description&#95;&#95;exact=</o>'Shiny!'
)<br><br><c>&dash;&dash;SQL</c><br><r>SELECT *
&nbsp;FROM</r> unicodex_codepoint c <br><r>&nbsp;WHERE</r> <l>c</l>.<l>name</l> <r>=</r> <d>'Sparkles'</d><br><r>&nbsp; &nbsp;AND</r> <l>c</l>.<l>description</l> <r>=</r> <d>'Shiny!'</d>


???

And we learnt earlier that unless there's a field lookup defined, we assume exact


Thisis the same SQL

Wecan also express this same statement using Q
---

<pre><code><c>&num;ORM</c>
Codepoint.objects.filter(
&nbsp;<o>name=</o>'Sparkles',
&nbsp;<o>description=</o>'Shiny!'
)<br><br><c>&dash;&dash;SQL</c><br><r>SELECT *
&nbsp;FROM</r> unicodex_codepoint c <br><r>&nbsp;WHERE</r> <l>c</l>.<l>name</l> <r>=</r> <d>'Sparkles'</d><br><r>&nbsp; &nbsp;AND</r> <l>c</l>.<l>description</l> <r>=</r> <d>'Shiny!'</d>


???

so going back to our first example,

---
<pre><code><c>&num;ORM</c>
Codepoint.objects.filter(
&nbsp;<o>name=</o>'Sparkles').filter(
&nbsp;<o>description=</o>'Shiny!'
)<br><br><c>&dash;&dash;SQL</c><br><r>SELECT *
&nbsp;FROM</r> unicodex_codepoint c <br><r>&nbsp;WHERE</r> <l>c</l>.<l>name</l> <r>=</r> <d>'Sparkles'</d><br><r>&nbsp; &nbsp;AND</r> <l>c</l>.<l>description</l> <r>=</r> <d>'Shiny!'</d>


???

we could also have two separate filter clauses.

---
<pre><code><c>&num;ORM</c>
Codepoint.objects.filter(
&nbsp;<o>name=</o>'Sparkles',
&nbsp;<o>description=</o>'Shiny!'
)<br><br><c>&dash;&dash;SQL</c><br><r>SELECT *
&nbsp;FROM</r> unicodex_codepoint c <br><r>&nbsp;WHERE</r> <l>c</l>.<l>name</l> <r>=</r> <d>'Sparkles'</d><br><r>&nbsp; &nbsp;AND</r> <l>c</l>.<l>description</l> <r>=</r> <d>'Shiny!'</d>


???

we could also


---
<pre><code><c>&num;ORM</c>
Codepoint.objects.filter(
&nbsp;Q(<o>name=</o>'Sparkles'),
&nbsp;Q(<o>description=</o>'Shiny!')
)<br><br><c>&dash;&dash;SQL</c><br><r>SELECT *
&nbsp;FROM</r> unicodex_codepoint c <br><r>&nbsp;WHERE</r> <l>c</l>.<l>name</l> <r>=</r> <d>'Sparkles'</d><br><r>&nbsp; &nbsp;AND</r> <l>c</l>.<l>description</l> <r>=</r> <d>'Shiny!'</d>


???

wrap our two filter parameters in Q


Thisprovides the same result

Noticein all of this, the equivelent SQL hasn't changed.

Withour comma here, we're implying we're using AND here. We can be explicit

---
<pre><code><c>&num;ORM</c>
Codepoint.objects.filter(
&nbsp;Q(<o>name=</o>'Sparkles') <r>&</r>
&nbsp;Q(<o>description=</o>'Shiny!')
)<br><br><c>&dash;&dash;SQL</c><br><r>SELECT *
&nbsp;FROM</r> unicodex_codepoint c <br><r>&nbsp;WHERE</r> <l>c</l>.<l>name</l> <r>=</r> <d>'Sparkles'</d><br><r>&nbsp; &nbsp;AND</r> <l>c</l>.<l>description</l> <r>=</r> <d>'Shiny!'</d>


???




But,since we have Q objects, we can do operations on them

Here,we're saying filter by this Query, and this Query

Andwe're using AND here explitictly

Wedon't have to wrap both in Q, either
---
<pre><code><c>&num;ORM</c>
Codepoint.objects.filter(
&nbsp;Q(<o>name=</o>'Sparkles'),</r>
&nbsp;Q(<o>description=</o>'Shiny!')
)<br><br><c>&dash;&dash;SQL</c><br><r>SELECT *
&nbsp;FROM</r> unicodex_codepoint c <br><r>&nbsp;WHERE</r> <l>c</l>.<l>name</l> <r>=</r> <d>'Sparkles'</d><br><r>&nbsp; &nbsp;AND</r> <l>c</l>.<l>description</l> <r>=</r> <d>'Shiny!'</d>


???

going back to our changed example

---
<pre><code><c>&num;ORM</c>
Codepoint.objects.filter(
&nbsp;Q(<o>name=</o>'Sparkles'),
&nbsp;<o>description=</o>'Shiny!'
)<br><br><c>&dash;&dash;SQL</c><br><r>SELECT *
&nbsp;FROM</r> unicodex_codepoint c <br><r>&nbsp;WHERE</r> <l>c</l>.<l>name</l> <r>=</r> <d>'Sparkles'</d><br><r>&nbsp; &nbsp;AND</r> <l>c</l>.<l>description</l> <r>=</r> <d>'Shiny!'</d>



???

we can change our queries with comman, and just wrap the first one and leave thther. Same result

---
<pre><code><c>&num;ORM</c>
Codepoint.objects.filter(
&nbsp;<o>name=</o>'Sparkles',
&nbsp;<o>description=</o>'Shiny!'
)<br><br><c>&dash;&dash;SQL</c><br><r>SELECT *
&nbsp;FROM</r> unicodex_codepoint c <br><r>&nbsp;WHERE</r> <l>c</l>.<l>name</l> <r>=</r> <d>'Sparkles'</d><br><r>&nbsp; &nbsp;AND</r> <l>c</l>.<l>description</l> <r>=</r> <d>'Shiny!'</d>



???

and we don't have to wrap either. But what if we wrap just the second

So,we could just wrap the second one, and leave the first one alone, right?


---
<pre><code><c>&num;ORM</c>
Codepoint.objects.filter(
&nbsp;<o>name=</o>'Sparkles',
&nbsp;Q(<o>description=</o>'Shiny!')
)<br><br><r>SyntaxError:positional argument follows keyword argument</r>


???

well no, we get an error.


Theerror here is insightful: Syntax Error, positioal argument follows keyword argument

Thereasoning behind this is that in all the code we've been doing here, we've been giving arguments to the filter function

Andin python, you have to declare positional argumnet before keyword argumnets

Rememberingthat even in these new Django concepts, we're still using Python, so python rules still apply.
---

<pre><code><c>&num;ORM</c>
Codepoint.objects.filter(
&nbsp;<o>name=</o>'Sparkles',
&nbsp;<o>description=</o>'Shiny!'
)<br><br><c>&dash;&dash;SQL</c><br><r>SELECT *
&nbsp;FROM</r> unicodex_codepoint c <br><r>&nbsp;WHERE</r> <l>c</l>.<l>name</l> <r>=</r> <d>'Sparkles'</d><br><r>&nbsp; &nbsp;AND</r> <l>c</l>.<l>description</l> <r>=</r> <d>'Shiny!'</d>


???

Another example of this. Let's put our code back working, and try changing that description


Saywe want to search for sparkles and unicorns

Sowe search for name equals sparkles and name equals unicorns and
---
<pre><code><c>&num;ORM</c>
Codepoint.objects.filter(
&nbsp;<o>name=</o>'Sparkles',
&nbsp;<o>name=</o>'Unicorn'
)<br><br><r>SyntaxError:keyword argument repeated</r>


???

oh. There's an error.


Thisis agan, because Python. You can't repeat keyword aguments. But, you can get around this.
Justwrap it in Q

---
<pre><code><c>&num;ORM</c>
Codepoint.objects.filter(
&nbsp;Q(<o>name=</o>'Sparkles'),
&nbsp;Q(<o>name=</o>'Unicorn')
)<br><br><c>&dash;&dash;SQL</c><br><r>SELECT *
&nbsp;FROM</r> unicodex_codepoint c <br><r>&nbsp;WHERE</r> <l>c</l>.<l>name</l> <r>=</r> <d>'Sparkles'</d><br><r>&nbsp; &nbsp;AND</r> <l>c</l>.<l>name</l> <r>=</r> <d>'Unicorn'</d>


???

now, this code is valid python, but it isn't useful, because it will never return any results.


We'reasking for exact string matches on the same column, twice. It'll always be an empty set.

Butwhat we can do is change this from an and, to an OR

---
<pre><code><c>&num;ORM</c>
Codepoint.objects.filter(
&nbsp;Q(<o>name=</o>'Sparkles') &
&nbsp;Q(<o>name=</o>'Unicorn')
)<br><br><c>&dash;&dash;SQL</c><br><r>SELECT *
&nbsp;FROM</r> unicodex_codepoint c <br><r>&nbsp;WHERE</r> <l>c</l>.<l>name</l> <r>=</r> <d>'Sparkles'</d><br><r>&nbsp; &nbsp;AND</r> <l>c</l>.<l>name</l> <r>=</r> <d>'Unicorn'</d>


???

Using the comma is equiv to this AND, but with the comma we're giving filter two arguments. Here, we're giving it one. We'll get back to this, because it's really cool


So,to take our AND to and OR, we change the ampersand

---
<pre><code><c>&num;ORM</c>
Codepoint.objects.filter(
&nbsp;Q(<o>name=</o>'Sparkles') |
&nbsp;Q(<o>name=</o>'Unicorn')
)<br><br><c>&dash;&dash;SQL</c><br><r>SELECT *
&nbsp;FROM</r> unicodex_codepoint c <br><r>&nbsp;WHERE</r> <l>c</l>.<l>name</l> <r>=</r> <d>'Sparkles'</d><br><r>&nbsp; &nbsp; OR</r> <l>c</l>.<l>name</l> <r>=</r> <d>'Unicorn'</d>


???

to a pipe.


Thisis an or operation

Youmay have only seen these operators before in bitmasking

---
<div class="shell-wrap"><p class="shell-top-bar">python3.6</p><p class="shell-body">
&gt;&gt;&gt; <w>&nbsp;</w>
---
<div class="shell-wrap"><p class="shell-top-bar">python3.6</p><p class="shell-body">
&gt;&gt;&gt; x = 0b10101010<w>&nbsp;</w>


???

if we have X as a binary string of one zero one zero


---
<div class="shell-wrap"><p class="shell-top-bar">python3.6</p><p class="shell-body">
&gt;&gt;&gt; x = 0b10101010<br>
&gt;&gt;&gt; <w>&nbsp;</w>

---
<div class="shell-wrap"><p class="shell-top-bar">python3.6</p><p class="shell-body">
&gt;&gt;&gt; x = 0b10101010<br>
&gt;&gt;&gt; y = 0b11110000<w>&nbsp;</w>


???

and we have y as one one one zero zero zero zero


wecan do something called bit masking

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


???

if we ask for x AND y


---
<div class="shell-wrap"><p class="shell-top-bar">python3.6</p><p class="shell-body">
&gt;&gt;&gt; x = 0b10101010<br>
&gt;&gt;&gt; y = 0b11110000<br>
&gt;&gt;&gt; bin(x & y)<br>
'0b10100000'<br>
&gt;&gt;&gt; <w>&nbsp;</w>


???

we get 10100000


Foreach bit, we only return 1 if both are 1

---
<div class="shell-wrap"><p class="shell-top-bar">python3.6</p><p class="shell-body">
&gt;&gt;&gt; x = 0b10101010<br>
&gt;&gt;&gt; y = 0b11110000<br>
&gt;&gt;&gt; bin(x & y)<br>
'0b10100000'<br>
&gt;&gt;&gt; bin(x | y)<w>&nbsp;</w>


???

conversely, if we ask for x OR y


---
<div class="shell-wrap"><p class="shell-top-bar">python3.6</p><p class="shell-body">
&gt;&gt;&gt; x = 0b10101010<br>
&gt;&gt;&gt; y = 0b11110000<br>
&gt;&gt;&gt; bin(x & y)<br>
'0b10100000'<br>
&gt;&gt;&gt; bin(x | y)<br>
'0b11110101'


???

we get all ones at the start, then our stripes


That'sbecause we return one is either or are 1


That'show binary ANDs and binary ORs work

Thisis very similar to what we do in SQL.

Foreach row of a table, we want to return it in our result set if BOTH conditions are true on and, or if either are true on and OR

---
<pre><code><c>&num;ORM</c>
Codepoint.objects.filter(
&nbsp;Q(<o>name=</o>'Sparkles') |
&nbsp;Q(<o>name=</o>'Unicorn')
)<br><br><c>&dash;&dash;SQL</c><br><r>SELECT *
&nbsp;FROM</r> unicodex_codepoint c <br><r>&nbsp;WHERE</r> <l>c</l>.<l>name</l> <r>=</r> <d>'Sparkles'</d><br><r>&nbsp; &nbsp; OR</r> <l>c</l>.<l>name</l> <r>=</r> <d>'Unicorn'</d>



???

so, using the and or operators here makes sense, because those are the actions we are performing


But,we're doing these operations on Query objects, not binary. Do how does that work?

What'shappening here is metaprogramming. Sometimes confused for magic, it's a funcitonlaity of python that makes it really powerful.

I'mgoing to show you a small snippet of django source code. It won't be scary, don't worry.

---
<pre><codestyle="font-size: 24pt !important"><r>class</r> <g>Q</g>(<g>tree</g>.<g>Node</g>):
<c>"""<br>Encapsulatefilters as objects that can<br>then be combined logically (using `&` and `|`).<br>"""</c>
&nbsp;...<br><br>
&nbsp;<r>def</r> <l>&#95;&#95;or&#95;&#95;</l>(self, other):
&nbsp;&nbsp; <r>return</r> <l>self</l>._combine(other, <l>self.OR</l>)

&nbsp;<r>def</r> <l>&#95;&#95;and&#95;&#95;</l>(self, other):
&nbsp;&nbsp; <r>return</r> <l>self</l>._combine(other, <l>self.AND</l>)
</code></pre>

<span class='foot'>[django db/models/utils.py](https://github.com/django/django/blame/5256a805ff1c31e4d5112627846291e91c5dc65d/django/db/models/query_utils.py#L142)</span>


???

django literally overloads the operations that happens when you try and do bitwise operations on the Q class in order for Q to have a logical response to bitwise operations


andit means you can do bitwise operations on Q obecjts and it's compeltely valid python

it'scomposble, it's functional, and it's intuative.

andit's been in Django for over 10 years

---
<pre><code><c>&num;ORM</c>
Codepoint.objects.filter(
&nbsp;Q(<o>name=</o>'Sparkles') |
&nbsp;Q(<o>name=</o>'Unicorn')
)<br><br><c>&dash;&dash;SQL</c><br><r>SELECT *
&nbsp;FROM</r> unicodex_codepoint c <br><r>&nbsp;WHERE</r> <l>c</l>.<l>name</l> <r>=</r> <d>'Sparkles'</d><br><r>&nbsp; &nbsp; OR</r> <l>c</l>.<l>name</l> <r>=</r> <d>'Unicorn'</d>


???

as well as AND or OR, we can also do NOT


Sowith our code above

---
<pre><code><c>&num;ORM</c>
Codepoint.objects.filter(
&nbsp;Q(<o>name=</o>'Sparkles') |
&nbsp;~Q(<o>name=</o>'Unicorn')
)<br><br><c>&dash;&dash;SQL</c><br><r>SELECT *
&nbsp;FROM</r> unicodex_codepoint c <br><r>&nbsp;WHERE</r> <l>c</l>.<l>name</l> <r>=</r> <d>'Sparkles'</d><br><r> &nbsp; &nbsp;OR NOT</r> <l>c</l>.<l>name</l> <r>=</r> <d>'Unicorn'</d>



???

we can and a tilda negation to invert that part of the query, and add a NOT to our SQL


Usingour field lookups and these operations, we can do a lot of things. But are some limitations

Firstly,you need to understand how the joins happen in order avoid confusion

---
<pre><code><c>&num;ORM</c>
Codepoint.objects.filter(
&nbsp;<o>design&#95;&#95;image&#95;&#95;contains=</o>"png",
&nbsp;<o>design&#95;&#95;image&#95;&#95;startswith=</o>"design")


???

Consider the following we want codepoints where their design iages have png and start with design


THisis based on the filename I'm using for the iages uploaded to my models

Okay.Let's run that and see what happens

---
<div class="shell-wrap"><p class="shell-top-bar">python3.6</p><p class="shell-body">
<ps>myrtle</ps> <dr>~/project $</dr> 
./manage.pyshell<br>
Python3.6.3 (default, Nov 9 2017, 15:58:30)<br>
[GCC4.2.1 Compatible Apple LLVM 9.0.0 (clang-900.0.38)] on darwin<br>
Type"help", "copyright", "credits" or "license" for more information.<br>
(InteractiveConsole)<br>
&gt;&gt;&gt; <w>&nbsp;</w>


???

so in our terminal


---
<div class="shell-wrap"><p class="shell-top-bar">python3.6</p><p class="shell-body">
<ps>myrtle</ps> <dr>~/project $</dr> 
./manage.pyshell<br>
Python3.6.3 (default, Nov 9 2017, 15:58:30)<br>
[GCC4.2.1 Compatible Apple LLVM 9.0.0 (clang-900.0.38)] on darwin<br>
Type"help", "copyright", "credits" or "license" for more information.<br>
(InteractiveConsole)<br>
&gt;&gt;&gt; from unicodex.models import Codepoint<w>&nbsp;</w>

---
<div class="shell-wrap"><p class="shell-top-bar">python3.6</p><p class="shell-body">
<ps>myrtle</ps> <dr>~/project $</dr> 
./manage.pyshell<br>
Python3.6.3 (default, Nov 9 2017, 15:58:30)<br>
[GCC4.2.1 Compatible Apple LLVM 9.0.0 (clang-900.0.38)] on darwin<br>
Type"help", "copyright", "credits" or "license" for more information.<br>
(InteractiveConsole)<br>
&gt;&gt;&gt; from unicodex.models import Codepoint<br>
&gt;&gt;&gt; <w>&nbsp;</w>


???

remembering to import our model


---
<div class="shell-wrap"><p class="shell-top-bar">python3.6</p><p class="shell-body">
<ps>myrtle</ps> <dr>~/project $</dr> 
./manage.pyshell<br>
Python3.6.3 (default, Nov 9 2017, 15:58:30)<br>
[GCC4.2.1 Compatible Apple LLVM 9.0.0 (clang-900.0.38)] on darwin<br>
Type"help", "copyright", "credits" or "license" for more information.<br>
(InteractiveConsole)<br>
&gt;&gt;&gt; from unicodex.models import Codepoint<br>
&gt;&gt;&gt; Codepoint.objects.filter(design&#95;&#95;image&#95;&#95;contains="png", design&#95;&#95;image&#95;&#95;startswith="design")<w>&nbsp;</w>


???

we add our code


---
<div class="shell-wrap"><p class="shell-top-bar">python3.6</p><p class="shell-body">
<ps>myrtle</ps> <dr>~/project $</dr> 
./manage.pyshell<br>
Python3.6.3 (default, Nov 9 2017, 15:58:30)<br>
[GCC4.2.1 Compatible Apple LLVM 9.0.0 (clang-900.0.38)] on darwin<br>
Type"help", "copyright", "credits" or "license" for more information.<br>
(InteractiveConsole)<br>
&gt;&gt;&gt; from unicodex.models import Codepoint<br>
&gt;&gt;&gt; Codepoint.objects.filter(design&#95;&#95;image&#95;&#95;contains="png", design&#95;&#95;image&#95;&#95;startswith="design")<br>
&lt;QuerySet[&lt;Codepoint: Sparkles>, &lt;Codepoint: Sparkles>, &lt;Codepoint: Sparkles>, &lt;Codepoint: Sparkles>, &lt;Codepoint: Sparkles>, &lt;Codepoint: Sparkles>, &lt;Codepoint: Sparkles>, &lt;Codepoint: Sparkles>, &lt;Codepoint: Sparkles>, &lt;Codepoint: Sparkles>, &lt;Codepoint: Sparkles>, &lt;Codepoint: Unicorn>, &lt;Codepoint: Unicorn>, &lt;Codepoint: Unicorn>, &lt;Codepoint: Unicorn>, &lt;Codepoint: Unicorn>, &lt;Codepoint: Unicorn>, &lt;Codepoint: Unicorn>, &lt;Codepoint: Castle>, &lt;Codepoint: Castle>, '...(remaining elements truncated)...']><br>
&gt;&gt;&gt; <w>&nbsp;</w>



???




Andwe get back a reeeeeeally long queryset.

But,the resuts are truncated for us

Thisis so incredibly useful

Datais still there, if you iterate over the list, but the print representation specificalyl doesn't flood your terminal

(thiswas implemented because of a very real bug at Lawrance Journal World, where they had servers keep crashing, because the debug page was trying to be helpful and show all the data... a million objects worth..)

---
<div class="shell-wrap"><p class="shell-top-bar">python3.6</p><p class="shell-body">
<ps>myrtle</ps> <dr>~/project $</dr> 
./manage.pyshell<br>
Python3.6.3 (default, Nov 9 2017, 15:58:30)<br>
[GCC4.2.1 Compatible Apple LLVM 9.0.0 (clang-900.0.38)] on darwin<br>
Type"help", "copyright", "credits" or "license" for more information.<br>
(InteractiveConsole)<br>
&gt;&gt;&gt; from unicodex.models import Codepoint<br>
&gt;&gt;&gt; Codepoint.objects.filter(design&#95;&#95;image&#95;&#95;contains="png", design&#95;&#95;image&#95;&#95;startswith="design")<w>&nbsp;</w>



???

rewind a step


---
<div class="shell-wrap"><p class="shell-top-bar">python3.6</p><p class="shell-body">
<ps>myrtle</ps> <dr>~/project $</dr> 
./manage.pyshell<br>
Python3.6.3 (default, Nov 9 2017, 15:58:30)<br>
[GCC4.2.1 Compatible Apple LLVM 9.0.0 (clang-900.0.38)] on darwin<br>
Type"help", "copyright", "credits" or "license" for more information.<br>
(InteractiveConsole)<br>
&gt;&gt;&gt; from unicodex.models import Codepoint<br>
&gt;&gt;&gt; Codepoint.objects.filter(design&#95;&#95;image&#95;&#95;contains="png", design&#95;&#95;image&#95;&#95;startswith="design").count()<w>&nbsp;</w>


???

add a count function on the end


---
<div class="shell-wrap"><p class="shell-top-bar">python3.6</p><p class="shell-body">
<ps>myrtle</ps> <dr>~/project $</dr> 
./manage.pyshell<br>
Python3.6.3 (default, Nov 9 2017, 15:58:30)<br>
[GCC4.2.1 Compatible Apple LLVM 9.0.0 (clang-900.0.38)] on darwin<br>
Type"help", "copyright", "credits" or "license" for more information.<br>
(InteractiveConsole)<br>
&gt;&gt;&gt; from unicodex.models import Codepoint<br>
&gt;&gt;&gt; Codepoint.objects.filter(design&#95;&#95;image&#95;&#95;contains="png", design&#95;&#95;image&#95;&#95;startswith="design").count()<br>
44<br>
&gt;&gt;&gt; <w>&nbsp;</w>


???

44 results


---
<pre><code><c>&num;ORM</c>
Codepoint.objects.filter(
&nbsp;<o>design&#95;&#95;image&#95;&#95;contains=</o>"png",
&nbsp;<o>design&#95;&#95;image&#95;&#95;startswith=</o>"design").count()

---
<pre><code><c>&num;ORM</c>
Codepoint.objects.filter(
&nbsp;<o>design&#95;&#95;image&#95;&#95;contains=</o>"png",
&nbsp;<o>design&#95;&#95;image&#95;&#95;startswith=</o>"design").count()<br><br><c>&dash;&dash; SQL</c><br><c>&dash;&dash; ?? </c>



???

But what code was run?


Wehave the ability to check this
---
<pre><code><c>&num;ORM</c>
Codepoint.objects.filter(
&nbsp;<o>design&#95;&#95;image&#95;&#95;contains=</o>"png",
&nbsp;<o>design&#95;&#95;image&#95;&#95;startswith=</o>"design").count()<br><br><c>&dash;&dash; SQL</c><br><c>&dash;&dash; ?? </c><br><br><c>&num; ORM</c><br><r>from</r> django.db <r>import</r> connection<br>connection.queries
</code></pre>
---
<div class="shell-wrap"><p class="shell-top-bar">python3.6</p><p class="shell-body">
<ps>myrtle</ps> <dr>~/project $</dr> 
./manage.pyshell<br>
Python3.6.3 (default, Nov 9 2017, 15:58:30)<br>
[GCC4.2.1 Compatible Apple LLVM 9.0.0 (clang-900.0.38)] on darwin<br>
Type"help", "copyright", "credits" or "license" for more information.<br>
(InteractiveConsole)<br>
&gt;&gt;&gt; from unicodex.models import Codepoint<br>
&gt;&gt;&gt; Codepoint.objects.filter(design&#95;&#95;image&#95;&#95;contains="png", design&#95;&#95;image&#95;&#95;startswith="design").count()<br>
44<br>
&gt;&gt;&gt; <w>&nbsp;</w>
---

<div class="shell-wrap"><p class="shell-top-bar">python3.6</p><p class="shell-body">
<ps>myrtle</ps> <dr>~/project $</dr> 
./manage.pyshell<br>
Python3.6.3 (default, Nov 9 2017, 15:58:30)<br>
[GCC4.2.1 Compatible Apple LLVM 9.0.0 (clang-900.0.38)] on darwin<br>
Type"help", "copyright", "credits" or "license" for more information.<br>
(InteractiveConsole)<br>
&gt;&gt;&gt; from unicodex.models import Codepoint<br>
&gt;&gt;&gt; Codepoint.objects.filter(design&#95;&#95;image&#95;&#95;contains="png", design&#95;&#95;image&#95;&#95;startswith="design").count()<br>
44<br>
&gt;&gt;&gt; from django.db import connection<w>&nbsp;</w>


???

we can import the django database connection modele

---

<div class="shell-wrap"><p class="shell-top-bar">python3.6</p><p class="shell-body">
<ps>myrtle</ps> <dr>~/project $</dr> 
./manage.pyshell<br>
Python3.6.3 (default, Nov 9 2017, 15:58:30)<br>
[GCC4.2.1 Compatible Apple LLVM 9.0.0 (clang-900.0.38)] on darwin<br>
Type"help", "copyright", "credits" or "license" for more information.<br>
(InteractiveConsole)<br>
&gt;&gt;&gt; from unicodex.models import Codepoint<br>
&gt;&gt;&gt; Codepoint.objects.filter(design&#95;&#95;image&#95;&#95;contains="png", design&#95;&#95;image&#95;&#95;startswith="design").count()<br>
44<br>
&gt;&gt;&gt; from django.db import connection<br>
&gt;&gt;&gt; <w>&nbsp;</w>
---

<div class="shell-wrap"><p class="shell-top-bar">python3.6</p><p class="shell-body">
<ps>myrtle</ps> <dr>~/project $</dr> 
./manage.pyshell<br>
Python3.6.3 (default, Nov 9 2017, 15:58:30)<br>
[GCC4.2.1 Compatible Apple LLVM 9.0.0 (clang-900.0.38)] on darwin<br>
Type"help", "copyright", "credits" or "license" for more information.<br>
(InteractiveConsole)<br>
&gt;&gt;&gt; from unicodex.models import Codepoint<br>
&gt;&gt;&gt; Codepoint.objects.filter(design&#95;&#95;image&#95;&#95;contains="png", design&#95;&#95;image&#95;&#95;startswith="design").count()<br>
44<br>
&gt;&gt;&gt; from django.db import connection<br>
&gt;&gt;&gt; connection.queries[-1]<w>&nbsp;</w>


???

and inspect the last query run against our databse



---
<div class="shell-wrap"><p class="shell-top-bar">python3.6</p><p class="shell-body">
<ps>myrtle</ps> <dr>~/project $</dr> 
./manage.pyshell<br>
Python3.6.3 (default, Nov 9 2017, 15:58:30)<br>
[GCC4.2.1 Compatible Apple LLVM 9.0.0 (clang-900.0.38)] on darwin<br>
Type"help", "copyright", "credits" or "license" for more information.<br>
(InteractiveConsole)<br>
&gt;&gt;&gt; from unicodex.models import Codepoint<br>
&gt;&gt;&gt; Codepoint.objects.filter(design&#95;&#95;image&#95;&#95;contains="png", design&#95;&#95;image&#95;&#95;startswith="design").count()<br>
44<br>
&gt;&gt;&gt; from django.db import connection<br>
&gt;&gt;&gt; connection.queries[-1]<br>
{'sql':'SELECT COUNT(&#42;) AS "&#95;&#95;count" FROM "unicodex_codepoint" INNER JOIN "unicodex_design" ON ("unicodex_codepoint"."id" = "unicodex_design"."codepoint_id") WHERE ("unicodex_design"."image"::text LIKE \'%png%\' AND "unicodex_design"."image"::text LIKE \'design%\')', 'time': '0.001'}<br>
&gt;&gt;&gt; <w>&nbsp;</w>
---
<pre><code><c>&num;ORM</c>
Codepoint.objects.filter(
&nbsp;<o>design&#95;&#95;image&#95;&#95;contains=</o>"png",
&nbsp;<o>design&#95;&#95;image&#95;&#95;startswith=</o>"design").count()<br><br><c>&dash;&dash; SQL</c><br><r>SELECT</r> <l>count</l>(<r>*</r>)
&nbsp;<r>FROM</r> unicodex_codepoint C<br><r>&nbsp;INNER JOIN</r> unicodex_design D <r>ON</r> (<l>C</l>.<l>id <r>=</r> D</l>.<l>id</l>)<br><r>&nbsp;WHERE</r> (<l>D</l>.<l>image</l> <r>LIKE</r> <d>'%png%'</d>
&nbsp;&nbsp; <r>AND</r> <l>D</l>.<l>image</l> <r>LIKE</r> <d>'design%'</d>)

---

<pre><code><c>&num;ORM</c>
Codepoint.objects.filter(
&nbsp;<o>design&#95;&#95;image&#95;&#95;contains=</o>"png").filter(
&nbsp;<o>design&#95;&#95;image&#95;&#95;startswith=</o>"design").count()<br><br><c>&dash;&dash; SQL</c><br><c>&dash;&dash; ??

---
<div class="shell-wrap"><p class="shell-top-bar">python3.6</p><p class="shell-body">
&gt;&gt;&gt; from unicodex.models import Codepoint<br>
&gt;&gt;&gt; Codepoint.objects.filter(design&#95;&#95;image&#95;&#95;contains="png", design&#95;&#95;image&#95;&#95;startswith="design").count()<br>
44<br>
&gt;&gt;&gt; from django.db import connection<br>
&gt;&gt;&gt; connection.queries[-1]<br>
{'sql':'SELECT COUNT(&#42;) AS "&#95;&#95;count" FROM "unicodex&#95;codepoint" INNER JOIN "unicodex&#95;design" ON ("unicodex&#95;codepoint"."id" = "unicodex&#95;design"."codepoint&#95;id") WHERE ("unicodex&#95;design"."image"::text LIKE \'%png%\' AND "unicodex&#95;design"."image"::text LIKE \'design%\')', 'time': '0.001'}<br>
&gt;&gt;&gt; <w>&nbsp;</w>
---
<div class="shell-wrap"><p class="shell-top-bar">python3.6</p><p class="shell-body">
&gt;&gt;&gt; from unicodex.models import Codepoint<br>
&gt;&gt;&gt; Codepoint.objects.filter(design&#95;&#95;image&#95;&#95;contains="png", design&#95;&#95;image&#95;&#95;startswith="design").count()<br>
44<br>
&gt;&gt;&gt; from django.db import connection<br>
&gt;&gt;&gt; connection.queries[-1]<br>
{'sql':'SELECT COUNT(&#42;) AS "&#95;&#95;count" FROM "unicodex&#95;codepoint" INNER JOIN "unicodex&#95;design" ON ("unicodex&#95;codepoint"."id" = "unicodex&#95;design"."codepoint&#95;id") WHERE ("unicodex&#95;design"."image"::text LIKE \'%png%\' AND "unicodex&#95;design"."image"::text LIKE \'design%\')', 'time': '0.001'}<br>
&gt;&gt;&gt; Codepoint.objects.filter(design&#95;&#95;image&#95;&#95;contains="png").filter(<br>
... design&#95;&#95;image&#95;&#95;startswith="design").count()<w>&nbsp;</w><br>

---
<div class="shell-wrap"><p class="shell-top-bar">python3.6</p><p class="shell-body">
&gt;&gt;&gt; from unicodex.models import Codepoint<br>
&gt;&gt;&gt; Codepoint.objects.filter(design&#95;&#95;image&#95;&#95;contains="png", design&#95;&#95;image&#95;&#95;startswith="design").count()<br>
44<br>
&gt;&gt;&gt; from django.db import connection<br>
&gt;&gt;&gt; connection.queries[-1]<br>
{'sql':'SELECT COUNT(&#42;) AS "&#95;&#95;count" FROM "unicodex&#95;codepoint" INNER JOIN "unicodex&#95;design" ON ("unicodex&#95;codepoint"."id" = "unicodex&#95;design"."codepoint&#95;id") WHERE ("unicodex&#95;design"."image"::text LIKE \'%png%\' AND "unicodex&#95;design"."image"::text LIKE \'design%\')', 'time': '0.001'}<br>
&gt;&gt;&gt; Codepoint.objects.filter(design&#95;&#95;image&#95;&#95;contains="png").filter(<br>
... design&#95;&#95;image&#95;&#95;startswith="design").count()<br>
712<br>
&gt;&gt;&gt; <w>&nbsp;</w>


???

wait, what??


---
<div class="shell-wrap"><p class="shell-top-bar">python3.6</p><p class="shell-body">
&gt;&gt;&gt; from unicodex.models import Codepoint<br>
&gt;&gt;&gt; Codepoint.objects.filter(design&#95;&#95;image&#95;&#95;contains="png", design&#95;&#95;image&#95;&#95;startswith="design").count()<br>
44<br>
&gt;&gt;&gt; from django.db import connection<br>
&gt;&gt;&gt; connection.queries[-1]<br>
{'sql':'SELECT COUNT(&#42;) AS "&#95;&#95;count" FROM "unicodex&#95;codepoint" INNER JOIN "unicodex&#95;design" ON ("unicodex&#95;codepoint"."id" = "unicodex&#95;design"."codepoint&#95;id") WHERE ("unicodex&#95;design"."image"::text LIKE \'%png%\' AND "unicodex&#95;design"."image"::text LIKE \'design%\')', 'time': '0.001'}<br>
&gt;&gt;&gt; Codepoint.objects.filter(design&#95;&#95;image&#95;&#95;contains="png").filter(<br>
... design&#95;&#95;image&#95;&#95;startswith="design").count()<br>
712<br>
&gt;&gt;&gt; connection.queries[-1]<w>&nbsp;</w>


???

let's check




---
<div class="shell-wrap"><p class="shell-top-bar">python3.6</p><p class="shell-body">
&gt;&gt;&gt; connection.queries[-1]<br>
{'sql':'SELECT COUNT(&#42;) AS "&#95;&#95;count" FROM "unicodex&#95;codepoint" INNER JOIN "unicodex&#95;design" ON ("unicodex&#95;codepoint"."id" = "unicodex&#95;design"."codepoint&#95;id") WHERE ("unicodex&#95;design"."image"::text LIKE \'%png%\' AND "unicodex&#95;design"."image"::text LIKE \'design%\')', 'time': '0.001'}<br>
&gt;&gt;&gt; Codepoint.objects.filter(design&#95;&#95;image&#95;&#95;contains="png").filter(<br>
... design&#95;&#95;image&#95;&#95;startswith="design").count()<br>
712<br>
&gt;&gt;&gt; connection.queries[-1]<br>
{'sql':'SELECT COUNT(&#42;) AS "&#95;&#95;count" FROM "unicodex&#95;codepoint" INNER JOIN "unicodex&#95;design" ON ("unicodex&#95;codepoint"."id" = "unicodex&#95;design"."codepoint&#95;id") INNER JOIN "unicodex&#95;design" T3 ON ("unicodex&#95;codepoint"."id" = T3."codepoint&#95;id") WHERE ("unicodex&#95;design"."image"::text LIKE \'%png%\' AND T3."image"::text LIKE \'design%\')', 'time': '0.002'}<br>
&gt;&gt;&gt; <w>&nbsp;</w>


???

well, we can tell it's a different SQL statement than before based on the length of the output.. but let's format itnicely and see what's going on

---
<pre><code><c>&num;ORM</c>
Codepoint.objects.filter(
&nbsp;<o>design&#95;&#95;image&#95;&#95;contains=</o>"png").filter(
&nbsp;<o>design&#95;&#95;image&#95;&#95;startswith=</o>"design").count()<br><br><c>&dash;&dash; SQL</c><br><r>SELECT</r> <l>count</l>(<r>&#42;</r>)
&nbsp;<r>FROM</r> from unicodex_codepoint C<br><r>&nbsp;INNER JOIN</r> unicodex_design D <r>ON</r> (<l>C</l>.<l>id <r>=</r> D</l>.<l>id</l>)<br><r>&nbsp;INNER JOIN</r> unicodex_design E <r>ON</r> (<l>C</l>.<l>id <r>=</r> E</l>.<l>id</l>)<br><r>&nbsp;WHERE</r> (<l>D</l>.<l>image</l> <r>LIKE</r> <d>'%png%'</d>
&nbsp;&nbsp; <r>AND</r> <l>E</l>.<l>image</l> <r>LIKE</r> <d>'design%'</d>)


???

Ah.


Wehave TWO joins happening here

Everytime there is a separate filter, it's another join. Which can absolutely be useful, but not when you're matching on the same associated table in both filters, as you can't join those references together.

Todo that, put them both in the same filter call. Django will be able to work it out, then.
---

<style>background-image: url("images/hunterbird.jpg");</style>


???

so now that we know how to hunt let's find that bug


---

class: top, image
![Image](images/unicodex_sparkles_bug.png)


???

we have a broken image somewhere. We can tell by the page that it's probably the image associated to the with the Twitter 1.0 Sparkle design.


Solet's find that.

Option:'shout it out'

---
<div class="shell-wrap"><p class="shell-top-bar">bash</p><p class="shell-body">
<ps>myrtle</ps> <dr>~ $</dr> 
cdproject<br>
<ps>myrtle</ps> <dr>~/project $</dr> 
./manage.py shell<w>&nbsp;</w>

---
<div class="shell-wrap"><p class="shell-top-bar">python3.6</p><p class="shell-body">
<ps>myrtle</ps> <dr>~ $</dr> 
cdproject<br>
<ps>myrtle</ps> <dr>~/project $</dr> 
./manage.pyshell<br>
Python3.6.3 (default, Nov 9 2017, 15:58:30)<br>
[GCC4.2.1 Compatible Apple LLVM 9.0.0 (clang-900.0.38)] on darwin<br>
Type"help", "copyright", "credits" or "license" for more information.<br>
(InteractiveConsole)<br>
&gt;&gt;&gt; <w>&nbsp;</w>
---
<div class="shell-wrap"><p class="shell-top-bar">python3.6</p><p class="shell-body">
<ps>myrtle</ps> <dr>~ $</dr> 
cdproject<br>
<ps>myrtle</ps> <dr>~/project $</dr> 
./manage.pyshell<br>
Python3.6.3 (default, Nov 9 2017, 15:58:30)<br>
[GCC4.2.1 Compatible Apple LLVM 9.0.0 (clang-900.0.38)] on darwin<br>
Type"help", "copyright", "credits" or "license" for more information.<br>
(InteractiveConsole)<br>
&gt;&gt;&gt; from unicodex.objects import<w>&nbsp;</w>
---
<div class="shell-wrap"><p class="shell-top-bar">python3.6</p><p class="shell-body">
<ps>myrtle</ps> <dr>~ $</dr> 
cdproject<br>
<ps>myrtle</ps> <dr>~/project $</dr> 
./manage.pyshell<br>
Python3.6.3 (default, Nov 9 2017, 15:58:30)<br>
[GCC4.2.1 Compatible Apple LLVM 9.0.0 (clang-900.0.38)] on darwin<br>
Type"help", "copyright", "credits" or "license" for more information.<br>
(InteractiveConsole)<br>
&gt;&gt;&gt; from unicodex.objects import *<w>&nbsp;</w>
---
<div class="shell-wrap"><p class="shell-top-bar">python3.6</p><p class="shell-body">
<ps>myrtle</ps> <dr>~ $</dr> 
cdproject<br>
<ps>myrtle</ps> <dr>~/project $</dr> 
./manage.pyshell<br>
Python3.6.3 (default, Nov 9 2017, 15:58:30)<br>
[GCC4.2.1 Compatible Apple LLVM 9.0.0 (clang-900.0.38)] on darwin<br>
Type"help", "copyright", "credits" or "license" for more information.<br>
(InteractiveConsole)<br>
&gt;&gt;&gt; from unicodex.objects import *<br>
&gt;&gt;&gt; <w>&nbsp;</w>
---
<div class="shell-wrap"><p class="shell-top-bar">python3.6</p><p class="shell-body">
<ps>myrtle</ps> <dr>~ $</dr> 
cdproject<br>
<ps>myrtle</ps> <dr>~/project $</dr> 
./manage.pyshell<br>
Python3.6.3 (default, Nov 9 2017, 15:58:30)<br>
[GCC4.2.1 Compatible Apple LLVM 9.0.0 (clang-900.0.38)] on darwin<br>
Type"help", "copyright", "credits" or "license" for more information.<br>
(InteractiveConsole)<br>
&gt;&gt;&gt; from unicodex.objects import *<br>
&gt;&gt;&gt; Design.objects.filter(<w>&nbsp;</w>
---
<div class="shell-wrap"><p class="shell-top-bar">python3.6</p><p class="shell-body">
<ps>myrtle</ps> <dr>~ $</dr> 
cdproject<br>
<ps>myrtle</ps> <dr>~/project $</dr> 
./manage.pyshell<br>
Python3.6.3 (default, Nov 9 2017, 15:58:30)<br>
[GCC4.2.1 Compatible Apple LLVM 9.0.0 (clang-900.0.38)] on darwin<br>
Type"help", "copyright", "credits" or "license" for more information.<br>
(InteractiveConsole)<br>
&gt;&gt;&gt; from unicodex.objects import *<br>
&gt;&gt;&gt; Design.objects.filter(codepoint&#95;&#95;name="Sparkles"<w>&nbsp;</w>
---
<div class="shell-wrap"><p class="shell-top-bar">python3.6</p><p class="shell-body">
<ps>myrtle</ps> <dr>~ $</dr> 
cdproject<br>
<ps>myrtle</ps> <dr>~/project $</dr> 
./manage.pyshell<br>
Python3.6.3 (default, Nov 9 2017, 15:58:30)<br>
[GCC4.2.1 Compatible Apple LLVM 9.0.0 (clang-900.0.38)] on darwin<br>
Type"help", "copyright", "credits" or "license" for more information.<br>
(InteractiveConsole)<br>
&gt;&gt;&gt; from unicodex.objects import *<br>
&gt;&gt;&gt; Design.objects.filter(codepoint&#95;&#95;name="Sparkles",<br>
... <w>&nbsp;</w><br>
---
<div class="shell-wrap"><p class="shell-top-bar">python3.6</p><p class="shell-body">
<ps>myrtle</ps> <dr>~ $</dr> 
cdproject<br>
<ps>myrtle</ps> <dr>~/project $</dr> 
./manage.pyshell<br>
Python3.6.3 (default, Nov 9 2017, 15:58:30)<br>
[GCC4.2.1 Compatible Apple LLVM 9.0.0 (clang-900.0.38)] on darwin<br>
Type"help", "copyright", "credits" or "license" for more information.<br>
(InteractiveConsole)<br>
&gt;&gt;&gt; from unicodex.objects import *<br>
&gt;&gt;&gt; Design.objects.filter(codepoint&#95;&#95;name="Sparkles",<br>
... vendorversion<w>&nbsp;</w><br>
---
<div class="shell-wrap"><p class="shell-top-bar">python3.6</p><p class="shell-body">
<ps>myrtle</ps> <dr>~ $</dr> 
cdproject<br>
<ps>myrtle</ps> <dr>~/project $</dr> 
./manage.pyshell<br>
Python3.6.3 (default, Nov 9 2017, 15:58:30)<br>
[GCC4.2.1 Compatible Apple LLVM 9.0.0 (clang-900.0.38)] on darwin<br>
Type"help", "copyright", "credits" or "license" for more information.<br>
(InteractiveConsole)<br>
&gt;&gt;&gt; from unicodex.objects import *<br>
&gt;&gt;&gt; Design.objects.filter(codepoint&#95;&#95;name="Sparkles",<br>
... vendorversion&#95;&#95;vendor<w>&nbsp;</w><br>
---
<div class="shell-wrap"><p class="shell-top-bar">python3.6</p><p class="shell-body">
<ps>myrtle</ps> <dr>~ $</dr> 
cdproject<br>
<ps>myrtle</ps> <dr>~/project $</dr> 
./manage.pyshell<br>
Python3.6.3 (default, Nov 9 2017, 15:58:30)<br>
[GCC4.2.1 Compatible Apple LLVM 9.0.0 (clang-900.0.38)] on darwin<br>
Type"help", "copyright", "credits" or "license" for more information.<br>
(InteractiveConsole)<br>
&gt;&gt;&gt; from unicodex.objects import *<br>
&gt;&gt;&gt; Design.objects.filter(codepoint&#95;&#95;name="Sparkles",<br>
... vendorversion&#95;&#95;vendor&#95;&#95;name<w>&nbsp;</w><br>
---
<div class="shell-wrap"><p class="shell-top-bar">python3.6</p><p class="shell-body">
<ps>myrtle</ps> <dr>~ $</dr> 
cdproject<br>
<ps>myrtle</ps> <dr>~/project $</dr> 
./manage.pyshell<br>
Python3.6.3 (default, Nov 9 2017, 15:58:30)<br>
[GCC4.2.1 Compatible Apple LLVM 9.0.0 (clang-900.0.38)] on darwin<br>
Type"help", "copyright", "credits" or "license" for more information.<br>
(InteractiveConsole)<br>
&gt;&gt;&gt; from unicodex.objects import *<br>
&gt;&gt;&gt; Design.objects.filter(codepoint&#95;&#95;name="Sparkles",<br>
... vendorversion&#95;&#95;vendor&#95;&#95;name="Twitter")<w>&nbsp;</w><br>
---
<div class="shell-wrap"><p class="shell-top-bar">python3.6</p><p class="shell-body">
<ps>myrtle</ps> <dr>~ $</dr> 
cdproject<br>
<ps>myrtle</ps> <dr>~/project $</dr> 
./manage.pyshell<br>
Python3.6.3 (default, Nov 9 2017, 15:58:30)<br>
[GCC4.2.1 Compatible Apple LLVM 9.0.0 (clang-900.0.38)] on darwin<br>
Type"help", "copyright", "credits" or "license" for more information.<br>
(InteractiveConsole)<br>
&gt;&gt;&gt; from unicodex.objects import *<br>
&gt;&gt;&gt; Design.objects.filter(codepoint&#95;&#95;name="Sparkles",<br>
... vendorversion&#95;&#95;vendor&#95;&#95;name="Twitter")<br>
&lt;QuerySet[&lt;Design: Sparkles Twitter 1.0>, &lt;Design: Sparkles Twitter 2.4>]><br>
&gt;&gt;&gt; <w>&nbsp;</w>
---
<div class="shell-wrap"><p class="shell-top-bar">python3.6</p><p class="shell-body">
<ps>myrtle</ps> <dr>~ $</dr> 
cdproject<br>
<ps>myrtle</ps> <dr>~/project $</dr> 
./manage.pyshell<br>
Python3.6.3 (default, Nov 9 2017, 15:58:30)<br>
[GCC4.2.1 Compatible Apple LLVM 9.0.0 (clang-900.0.38)] on darwin<br>
Type"help", "copyright", "credits" or "license" for more information.<br>
(InteractiveConsole)<br>
&gt;&gt;&gt; from unicodex.objects import *<br>
&gt;&gt;&gt; Design.objects.filter(codepoint&#95;&#95;name="Sparkles",<br>
... vendorversion&#95;&#95;vendor&#95;&#95;name="Twitter")<br>
&lt;QuerySet[&lt;Design: Sparkles Twitter 1.0>, &lt;Design: Sparkles Twitter 2.4>]><br>
&gt;&gt;&gt; Design.objects.filter(codepoint&#95;&#95;name="Sparkles",<br>
... vendorversion&#95;&#95;vendor&#95;&#95;name="Twitter")<w>&nbsp;</w><br>


???

press up to replay the line

---
<div class="shell-wrap"><p class="shell-top-bar">python3.6</p><p class="shell-body">
<ps>myrtle</ps> <dr>~ $</dr> 
cdproject<br>
<ps>myrtle</ps> <dr>~/project $</dr> 
./manage.pyshell<br>
Python3.6.3 (default, Nov 9 2017, 15:58:30)<br>
[GCC4.2.1 Compatible Apple LLVM 9.0.0 (clang-900.0.38)] on darwin<br>
Type"help", "copyright", "credits" or "license" for more information.<br>
(InteractiveConsole)<br>
&gt;&gt;&gt; from unicodex.objects import *<br>
&gt;&gt;&gt; Design.objects.filter(codepoint&#95;&#95;name="Sparkles",<br>
... vendorversion&#95;&#95;vendor&#95;&#95;name="Twitter")<br>
&lt;QuerySet[&lt;Design: Sparkles Twitter 1.0>, &lt;Design: Sparkles Twitter 2.4>]><br>
&gt;&gt;&gt; <w>D</w>esign.objects.filter(codepoint&#95;&#95;name="Sparkles",<br>
... vendorversion&#95;&#95;vendor&#95;&#95;name="Twitter")<br>

---
<div class="shell-wrap"><p class="shell-top-bar">python3.6</p><p class="shell-body">
<ps>myrtle</ps> <dr>~ $</dr> 
cdproject<br>
<ps>myrtle</ps> <dr>~/project $</dr> 
./manage.pyshell<br>
Python3.6.3 (default, Nov 9 2017, 15:58:30)<br>
[GCC4.2.1 Compatible Apple LLVM 9.0.0 (clang-900.0.38)] on darwin<br>
Type"help", "copyright", "credits" or "license" for more information.<br>
(InteractiveConsole)<br>
&gt;&gt;&gt; from unicodex.objects import *<br>
&gt;&gt;&gt; Design.objects.filter(codepoint&#95;&#95;name="Sparkles",<br>
... vendorversion&#95;&#95;vendor&#95;&#95;name="Twitter")<br>
&lt;QuerySet[&lt;Design: Sparkles Twitter 1.0>, &lt;Design: Sparkles Twitter 2.4>]><br>
&gt;&gt;&gt; d =<w>&nbsp;</w>Design.objects.filter(codepoint&#95;&#95;name="Sparkles",<br>
... vendorversion&#95;&#95;vendor&#95;&#95;name="Twitter")<br>

---
<div class="shell-wrap"><p class="shell-top-bar">python3.6</p><p class="shell-body">
<ps>myrtle</ps> <dr>~ $</dr> 
cdproject<br>
<ps>myrtle</ps> <dr>~/project $</dr> 
./manage.pyshell<br>
Python3.6.3 (default, Nov 9 2017, 15:58:30)<br>
[GCC4.2.1 Compatible Apple LLVM 9.0.0 (clang-900.0.38)] on darwin<br>
Type"help", "copyright", "credits" or "license" for more information.<br>
(InteractiveConsole)<br>
&gt;&gt;&gt; from unicodex.objects import *<br>
&gt;&gt;&gt; Design.objects.filter(codepoint&#95;&#95;name="Sparkles",<br>
... vendorversion&#95;&#95;vendor&#95;&#95;name="Twitter")<br>
&lt;QuerySet[&lt;Design: Sparkles Twitter 1.0>, &lt;Design: Sparkles Twitter 2.4>]><br>
&gt;&gt;&gt; d = Design.objects.filter(codepoint&#95;&#95;name="Sparkles",<br>
... vendorversion&#95;&#95;vendor&#95;&#95;name="Twitter")<br>
&gt;&gt;&gt; <w>&nbsp;</w>


???

now we have our value saved

---
<div class="shell-wrap"><p class="shell-top-bar">python3.6</p><p class="shell-body">
&gt;&gt;&gt; <w>&nbsp;</w>


???

clear terminal

---
<div class="shell-wrap"><p class="shell-top-bar">python3.6</p><p class="shell-body">
&gt;&gt;&gt; d<w>&nbsp;</w>
---
<div class="shell-wrap"><p class="shell-top-bar">python3.6</p><p class="shell-body">
&gt;&gt;&gt; d<br>
&lt;QuerySet[&lt;Design: Sparkles Twitter 1.0>, &lt;Design: Sparkles Twitter 2.4>]><br>
&gt;&gt;&gt; <w>&nbsp;</w>


???

now, we can filter more.

---

<div class="shell-wrap"><p class="shell-top-bar">python3.6</p><p class="shell-body">
&gt;&gt;&gt; d<br>
&lt;QuerySet[&lt;Design: Sparkles Twitter 1.0>, &lt;Design: Sparkles Twitter 2.4>]><br>
&gt;&gt;&gt; d[0]<w>&nbsp;</w>


???

we could absolutely just return the first value of this array


That'scompletely valid
---
<div class="shell-wrap"><p class="shell-top-bar">python3.6</p><p class="shell-body">
&gt;&gt;&gt; d<br>
&lt;QuerySet[&lt;Design: Sparkles Twitter 1.0>, &lt;Design: Sparkles Twitter 2.4>]><br>
&gt;&gt;&gt; d<w>&nbsp;</w>


???

but let's keep filtering, instead


---
<div class="shell-wrap"><p class="shell-top-bar">python3.6</p><p class="shell-body">
&gt;&gt;&gt; d<br>
&lt;QuerySet[&lt;Design: Sparkles Twitter 1.0>, &lt;Design: Sparkles Twitter 2.4>]><br>
&gt;&gt;&gt; d.filter(<w>&nbsp;</w>


???

we can chain filters on querysets, remember?


---
<div class="shell-wrap"><p class="shell-top-bar">python3.6</p><p class="shell-body">
&gt;&gt;&gt; d<br>
&lt;QuerySet[&lt;Design: Sparkles Twitter 1.0>, &lt;Design: Sparkles Twitter 2.4>]><br>
&gt;&gt;&gt; d.filter(vendorversion<w>&nbsp;</w>
---
<div class="shell-wrap"><p class="shell-top-bar">python3.6</p><p class="shell-body">
&gt;&gt;&gt; d<br>
&lt;QuerySet[&lt;Design: Sparkles Twitter 1.0>, &lt;Design: Sparkles Twitter 2.4>]><br>
&gt;&gt;&gt; d.filter(vendorversion&#95;&#95;name<w>&nbsp;</w>
---
<div class="shell-wrap"><p class="shell-top-bar">python3.6</p><p class="shell-body">
&gt;&gt;&gt; d<br>
&lt;QuerySet[&lt;Design: Sparkles Twitter 1.0>, &lt;Design: Sparkles Twitter 2.4>]><br>
&gt;&gt;&gt; d.filter(vendorversion&#95;&#95;name&#95;&#95;contains<w>&nbsp;</w>


???

contains here, to be save. We know the string will have 1.0 in it, but we aren't 100% sure where

---
<div class="shell-wrap"><p class="shell-top-bar">python3.6</p><p class="shell-body">
&gt;&gt;&gt; d<br>
&lt;QuerySet[&lt;Design: Sparkles Twitter 1.0>, &lt;Design: Sparkles Twitter 2.4>]><br>
&gt;&gt;&gt; d.filter(vendorversion&#95;&#95;name&#95;&#95;contains="1.0")<w>&nbsp;</w>
---
<div class="shell-wrap"><p class="shell-top-bar">python3.6</p><p class="shell-body">
&gt;&gt;&gt; d<br>
&lt;QuerySet[&lt;Design: Sparkles Twitter 1.0>, &lt;Design: Sparkles Twitter 2.4>]><br>
&gt;&gt;&gt; d.filter(vendorversion&#95;&#95;name&#95;&#95;contains="1.0")<br>
&lt;QuerySet[&lt;Design: Sparkles Twitter 1.0>]><br>
&gt;&gt;&gt; <w>&nbsp;</w>


???

woo!

---
<div class="shell-wrap"><p class="shell-top-bar">python3.6</p><p class="shell-body">
&gt;&gt;&gt; d<br>
&lt;QuerySet[&lt;Design: Sparkles Twitter 1.0>, &lt;Design: Sparkles Twitter 2.4>]><br>
&gt;&gt;&gt; d.filter(vendorversion&#95;&#95;name&#95;&#95;contains="1.0")<br>
&lt;QuerySet[&lt;Design: Sparkles Twitter 1.0>]><br>
&gt;&gt;&gt; d.filter(vendorversion&#95;&#95;name&#95;&#95;contains="1.0")<w>&nbsp;</w>
---
<div class="shell-wrap"><p class="shell-top-bar">python3.6</p><p class="shell-body">
&gt;&gt;&gt; d<br>
&lt;QuerySet[&lt;Design: Sparkles Twitter 1.0>, &lt;Design: Sparkles Twitter 2.4>]><br>
&gt;&gt;&gt; d.filter(vendorversion&#95;&#95;name&#95;&#95;contains="1.0")<br>
&lt;QuerySet[&lt;Design: Sparkles Twitter 1.0>]><br>
&gt;&gt;&gt; <w>d</w>.filter(vendorversion&#95;&#95;name&#95;&#95;contains="1.0")<br>
---
<div class="shell-wrap"><p class="shell-top-bar">python3.6</p><p class="shell-body">
&gt;&gt;&gt; d<br>
&lt;QuerySet[&lt;Design: Sparkles Twitter 1.0>, &lt;Design: Sparkles Twitter 2.4>]><br>
&gt;&gt;&gt; d.filter(vendorversion&#95;&#95;name&#95;&#95;contains="1.0")<br>
&lt;QuerySet[&lt;Design: Sparkles Twitter 1.0>]><br>
&gt;&gt;&gt; d.filte<w>r</w>(vendorversion&#95;&#95;name&#95;&#95;contains="1.0")<br>

---
<div class="shell-wrap"><p class="shell-top-bar">python3.6</p><p class="shell-body">
&gt;&gt;&gt; d<br>
&lt;QuerySet[&lt;Design: Sparkles Twitter 1.0>, &lt;Design: Sparkles Twitter 2.4>]><br>
&gt;&gt;&gt; d.filter(vendorversion&#95;&#95;name&#95;&#95;contains="1.0")<br>
&lt;QuerySet[&lt;Design: Sparkles Twitter 1.0>]><br>
&gt;&gt;&gt; d.<w>(</w>vendorversion&#95;&#95;name&#95;&#95;contains="1.0")<br>
---
<div class="shell-wrap"><p class="shell-top-bar">python3.6</p><p class="shell-body">
&gt;&gt;&gt; d<br>
&lt;QuerySet[&lt;Design: Sparkles Twitter 1.0>, &lt;Design: Sparkles Twitter 2.4>]><br>
&gt;&gt;&gt; d.filter(vendorversion&#95;&#95;name&#95;&#95;contains="1.0")<br>
&lt;QuerySet[&lt;Design: Sparkles Twitter 1.0>]><br>
&gt;&gt;&gt; d.get<w>(</w>vendorversion&#95;&#95;name&#95;&#95;contains="1.0")<br>
---
<div class="shell-wrap"><p class="shell-top-bar">python3.6</p><p class="shell-body">
&gt;&gt;&gt; d<br>
&lt;QuerySet[&lt;Design: Sparkles Twitter 1.0>, &lt;Design: Sparkles Twitter 2.4>]><br>
&gt;&gt;&gt; d.filter(vendorversion&#95;&#95;name&#95;&#95;contains="1.0")<br>
&lt;QuerySet[&lt;Design: Sparkles Twitter 1.0>]><br>
&gt;&gt;&gt; d.get(vendorversion&#95;&#95;name&#95;&#95;contains="1.0")<br>
&lt;Design:Sparkles Twitter 1.0><br>
&gt;&gt;&gt; <w>&nbsp;</w>
---
<div class="shell-wrap"><p class="shell-top-bar">python3.6</p><p class="shell-body">
&gt;&gt;&gt; d<br>
&lt;QuerySet[&lt;Design: Sparkles Twitter 1.0>, &lt;Design: Sparkles Twitter 2.4>]><br>
&gt;&gt;&gt; d.filter(vendorversion&#95;&#95;name&#95;&#95;contains="1.0")<br>
&lt;QuerySet[&lt;Design: Sparkles Twitter 1.0>]><br>
&gt;&gt;&gt; d.get(vendorversion&#95;&#95;name&#95;&#95;contains="1.0")<br>
&lt;Design:Sparkles Twitter 1.0><br>
&gt;&gt;&gt; d.get(vendorversion&#95;&#95;name&#95;&#95;contains="1.0")<w>&nbsp;</w>

---
<div class="shell-wrap"><p class="shell-top-bar">python3.6</p><p class="shell-body">
&gt;&gt;&gt; d<br>
&lt;QuerySet[&lt;Design: Sparkles Twitter 1.0>, &lt;Design: Sparkles Twitter 2.4>]><br>
&gt;&gt;&gt; d.filter(vendorversion&#95;&#95;name&#95;&#95;contains="1.0")<br>
&lt;QuerySet[&lt;Design: Sparkles Twitter 1.0>]><br>
&gt;&gt;&gt; d.get(vendorversion&#95;&#95;name&#95;&#95;contains="1.0")<br>
&lt;Design:Sparkles Twitter 1.0><br>
&gt;&gt;&gt; d.get(vendorversion&#95;&#95;name&#95;&#95;contains="1.0")._meta.get_fields()<w>&nbsp;</w>

---
<div class="shell-wrap"><p class="shell-top-bar">python3.6</p><p class="shell-body">
&gt;&gt;&gt; d<br>
&lt;QuerySet[&lt;Design: Sparkles Twitter 1.0>, &lt;Design: Sparkles Twitter 2.4>]><br>
&gt;&gt;&gt; d.filter(vendorversion&#95;&#95;name&#95;&#95;contains="1.0")<br>
&lt;QuerySet[&lt;Design: Sparkles Twitter 1.0>]><br>
&gt;&gt;&gt; d.get(vendorversion&#95;&#95;name&#95;&#95;contains="1.0")<br>
&lt;Design:Sparkles Twitter 1.0><br>
&gt;&gt;&gt; d.get(vendorversion&#95;&#95;name&#95;&#95;contains="1.0")._meta.get_fields()<br>
(&lt;django.db.models.fields.AutoField:id>,<br>
&lt;django.db.models.fields.related.ForeignKey:vendorversion>, </br>
&lt;django.db.models.fields.related.ForeignKey:codepoint>, <br>
&lt;django.db.models.fields.files.FileField:image>)<br>
&gt;&gt;&gt; <w>&nbsp;</w>
---
<div class="shell-wrap"><p class="shell-top-bar">python3.6</p><p class="shell-body">
&gt;&gt;&gt; d<br>
&lt;QuerySet[&lt;Design: Sparkles Twitter 1.0>, &lt;Design: Sparkles Twitter 2.4>]><br>
&gt;&gt;&gt; d.filter(vendorversion&#95;&#95;name&#95;&#95;contains="1.0")<br>
&lt;QuerySet[&lt;Design: Sparkles Twitter 1.0>]><br>
&gt;&gt;&gt; d.get(vendorversion&#95;&#95;name&#95;&#95;contains="1.0")<br>
&lt;Design:Sparkles Twitter 1.0><br>
&gt;&gt;&gt; d.get(vendorversion&#95;&#95;name&#95;&#95;contains="1.0")._meta.get_fields()<br>
(&lt;django.db.models.fields.AutoField:id>,<br>
&lt;django.db.models.fields.related.ForeignKey:vendorversion>, </br>
&lt;django.db.models.fields.related.ForeignKey:codepoint>, <br>
&lt;django.db.models.fields.files.FileField:image>)<br>
&gt;&gt;&gt; d.get(vendorversion&#95;&#95;name&#95;&#95;contains="1.0")._meta.get_fields()<w>&nbsp;</w>
---
<div class="shell-wrap"><p class="shell-top-bar">python3.6</p><p class="shell-body">
&gt;&gt;&gt; d<br>
&lt;QuerySet[&lt;Design: Sparkles Twitter 1.0>, &lt;Design: Sparkles Twitter 2.4>]><br>
&gt;&gt;&gt; d.filter(vendorversion&#95;&#95;name&#95;&#95;contains="1.0")<br>
&lt;QuerySet[&lt;Design: Sparkles Twitter 1.0>]><br>
&gt;&gt;&gt; d.get(vendorversion&#95;&#95;name&#95;&#95;contains="1.0")<br>
&lt;Design:Sparkles Twitter 1.0><br>
&gt;&gt;&gt; d.get(vendorversion&#95;&#95;name&#95;&#95;contains="1.0")._meta.get_fields()<br>
(&lt;django.db.models.fields.AutoField:id>,<br>
&lt;django.db.models.fields.related.ForeignKey:vendorversion>, </br>
&lt;django.db.models.fields.related.ForeignKey:codepoint>, <br>
&lt;django.db.models.fields.files.FileField:image>)<br>
&gt;&gt;&gt; d.get(vendorversion&#95;&#95;name&#95;&#95;contains="1.0")<w>&nbsp;</w>

---
<div class="shell-wrap"><p class="shell-top-bar">python3.6</p><p class="shell-body">
&gt;&gt;&gt; d<br>
&lt;QuerySet[&lt;Design: Sparkles Twitter 1.0>, &lt;Design: Sparkles Twitter 2.4>]><br>
&gt;&gt;&gt; d.filter(vendorversion&#95;&#95;name&#95;&#95;contains="1.0")<br>
&lt;QuerySet[&lt;Design: Sparkles Twitter 1.0>]><br>
&gt;&gt;&gt; d.get(vendorversion&#95;&#95;name&#95;&#95;contains="1.0")<br>
&lt;Design:Sparkles Twitter 1.0><br>
&gt;&gt;&gt; d.get(vendorversion&#95;&#95;name&#95;&#95;contains="1.0")._meta.get_fields()<br>
(&lt;django.db.models.fields.AutoField:id>,<br>
&lt;django.db.models.fields.related.ForeignKey:vendorversion>, </br>
&lt;django.db.models.fields.related.ForeignKey:codepoint>, <br>
&lt;django.db.models.fields.files.FileField:image>)<br>
&gt;&gt;&gt; d.get(vendorversion&#95;&#95;name&#95;&#95;contains="1.0").image<w>&nbsp;</w>
---
<div class="shell-wrap"><p class="shell-top-bar">python3.6</p><p class="shell-body">
&gt;&gt;&gt; d<br>
&lt;QuerySet[&lt;Design: Sparkles Twitter 1.0>, &lt;Design: Sparkles Twitter 2.4>]><br>
&gt;&gt;&gt; d.filter(vendorversion&#95;&#95;name&#95;&#95;contains="1.0")<br>
&lt;QuerySet[&lt;Design: Sparkles Twitter 1.0>]><br>
&gt;&gt;&gt; d.get(vendorversion&#95;&#95;name&#95;&#95;contains="1.0")<br>
&lt;Design:Sparkles Twitter 1.0><br>
&gt;&gt;&gt; d.get(vendorversion&#95;&#95;name&#95;&#95;contains="1.0")._meta.get_fields()<br>
(&lt;django.db.models.fields.AutoField:id>,<br>
&lt;django.db.models.fields.related.ForeignKey:vendorversion>, </br>
&lt;django.db.models.fields.related.ForeignKey:codepoint>, <br>
&lt;django.db.models.fields.files.FileField:image>)<br>
&gt;&gt;&gt; d.get(vendorversion&#95;&#95;name&#95;&#95;contains="1.0").image<br>
&lt;FieldFile:designs/downloads/2728_twitter_twemoji-1.0.png🐛><br>
&gt;&gt;&gt; <w>&nbsp;</w>
---

##`..twemoji-1.0.png🐛"`


???

there's my bug!


Gotcha!

Ireally should fix that.. meh, after my talk.


---
##So


???

So, the ORM is demonstratably great and all, but what if you have something reeeeeally complex, that you can't easily represent in the ORM?

---

##So, what if the ORM doesn't do it?


---
##`raw`

???

If you really really really need to, you can drop down to raw SQL CODE

---
#⚠️

???

but


butbut but

Youneed to be careful

Ifyou look up the docs about how to do this

---
<divclass="left"><span style="font-family: Roboto">Performing raw SQL queries</span><br><br>
<rr>Theraw() manager ...</rr><br/>
<br>⚠️<rb>You should be very careful whenever you write.</rb><br>
<br>`Abc.objects.raw('SELECT* FROM myapp_abc')`<br><br>
🗒<rr>Where did the name of the Person table come from in that example?</rr>
<br>⚠️<rb>No checking is done on the SQL statement that is passed in to .raw().</rb>
<br>⚠️<rb>If you are performing queries on MySQL, note that MySQL’s silent type coercion may cause unexpected results when mixing types.</rb>
<br>⚠️<rb>While a RawQuerySet instance can be iterated over like a normal QuerySet, RawQuerySet doesn’t implement </rb><br></div>


???

you'll see it is FULL of warnings and notes and conditions


Thereare specific sections in the docs about how to give raw parameterised arguments to help prevent potential SQL injection, but you should still understand how this functionality works before you try using it.

Youalso break the ability for your app to be used by multiple databases. Because of the differences in SQL between databases, your postgres flavoured code probably will break if someone wants to run it on an sqlite database

---
##Sometimes, the sequels are better.


???

But sometimes, SQL is better


thewhole point of the ORM is in the name: the Object Relational Mapper. It's all about mapping objects to relations

theORM can do 80% of things, but if there's stuff that's easier to do in RAW self, instead of wrangling the ORM, do that instead.

---
##Discover more yourself

???

I've only touched the surface of the power of the ORM


IfI've caught your interest in the power of this part of django, you can learn more yourself
---
##Creating objects
##Field Types
##Field Relationships


???

How to create objects, including from raw SQL


Fieldtypes - things like email fields and image fields

Andmore field relations, ways that you can call both codepoint attributes on a design object, and design attributes on a codepoint
---
##<fl>docs.djangoproject.com</fl>


???

seriously, the docs are wonderful. Now that you know some of the general terms of this bit of software, you should be able to find more interesting ways to make the ORM work for you

---
#☝️
##<span style="color: white">`.`</span>

???

Oh, and just one more note before I go

Ifyou really want to make the ORM work well for you when developing
---

#☝️
##`echo "ipython" >> Pipfile`

???

add ipython as a dev requirement in your Pipfile, or requirements.txt or whereever all good python package managers store their requirements.

---
<div class="shell-wrap"><p class="shell-top-bar">python3.6</p><p class="shell-body">
<ps>myrtle</ps> <dr>~/project $</dr> 
./manage.pyshell<br>
Python3.6.3 (default, Nov 9 2017, 15:58:30)<br>
[GCC4.2.1 Compatible Apple LLVM 9.0.0 (clang-900.0.38)] on darwin<br>
Type"help", "copyright", "credits" or "license" for more information.<br>
(InteractiveConsole)<br>
&gt;&gt;&gt; <w>&nbsp;</w>


???

it will turn your shell from this old and busted

---
<div class="shell-wrap"><p class="shell-top-bar">python3.6</p><p class="shell-body">
<ps>myrtle</ps> <dr>~/project $</dr> 
./manage.pyshell<br>
Python3.6.3 (default, Nov 9 2017, 15:58:30)<br>
Type'copyright', 'credits' or 'license' for more information<br>
IPython6.3.1 -- An enhanced Interactive Python. Type '?' for help.<br><br>
<tg>In [</tg><ty>1</ty><tg>]:&nbsp;<w>&nbsp;</w>

???

to the new hotness


Thisis an ipython powered shell, which means
---
<div class="shell-wrap"><p class="shell-top-bar">python3.6</p><p class="shell-body">
<ps>myrtle</ps> <dr>~/project $</dr> 
./manage.pyshell<br>
Python3.6.3 (default, Nov 9 2017, 15:58:30)<br>
Type'copyright', 'credits' or 'license' for more information<br>
IPython6.3.1 -- An enhanced Interactive Python. Type '?' for help.<br>
<br><tg>In[</tg><ty>1</ty><tg>]: from </tg><tb>uni</tb><w>&nbsp;</w>

???

you start typing something, press tab, and

---
<div class="shell-wrap"><p class="shell-top-bar">python3.6</p><p class="shell-body">
<ps>myrtle</ps> <dr>~/project $</dr> 
./manage.pyshell<br>
Python3.6.3 (default, Nov 9 2017, 15:58:30)<br>
Type'copyright', 'credits' or 'license' for more information<br>
IPython6.3.1 -- An enhanced Interactive Python. Type '?' for help.<br>
<br><tg>In[</tg><ty>1</ty><tg>]: from </tg><tb>uni</tb><w>&nbsp;</w>
<br>&nbsp;&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; <ww>unicodedata</ww>
<br>&nbsp;&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; <ww>unicodex&nbsp; &nbsp;</ww>
<br>&nbsp;&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; <ww>unittest&nbsp; &nbsp;</ww>

???

you get autocompleted suggestions.


Socool
---

<style>background-image: url("images/hunterfound.jpg");</style>



???




Sothat's all I had. Hopefully with these tips and tricks about how to use the ORM to interact your project, you can start finding those pesky bugs you've been tasked to find.

Itmight be a new stack to you, it might be old school, but I find the utmost dorkish joy in finding that odd little thing in a technology stack that just a short time ago I had no idea about, and then being able to harness that power.

Andbeing able to use your skills gained from other technology sets in new fields is really fun, sometimes a bit interesting, but always great.

---
<br>
<div style='width: 100%; margin: 0 auto;'><p align='center'><img height='160px' src='images/space.svg'><img height='160px' src='images/space.svg'><img height='160px' src='images/claps.svg'><img height='160px' src='images/space.svg'><img height='160px' src='images/space.svg'></p></div>
![Image](images/footer.svg)
<span class='foot'>Technical reviewers: James Bennett, Russell Keith-Magee</span>


???

thank you for your time

---
<style>background-image: url("images/pyconau18.png");</style>
<divstyle="-webkit-transform: rotate(-29deg);color: lightgreen;font-size: 64pt;margin-top: 230px;font-family: 'DTLProkyonST', regular;margin-left: 600px;z-index: 999;width: 500px;"><b>Includes<br>DjangoCon AU</b></div>

???

PS PyCon AU is a thing that's happening
