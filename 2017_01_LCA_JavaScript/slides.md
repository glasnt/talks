 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%"><c>// If you can read this, yay!</code></pre></div>
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%"><s>123456789 123456789 123456789 12</s></code></pre></div>
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">> console.log("Hello World");</code></pre></div>
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">Hello World</code></pre></div>
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%"><h>!#/usr/bin/env ruby</h></code></pre></div>
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">> (0..3).each {|c| puts c}</code></pre></div>
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">0</code></pre></div>
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">1</code></pre></div>
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">2</code></pre></div>
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">3</code></pre></div>
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">=> 0..3 <c>// Console is 11x32 </c></code></pre></div>
---

<br> 
<br> 
# JavaScript is Awe-ful
<br> 
 <img src="pictures/footer.svg" />
---
# House Keeping <!-- .slide: class="center" -->

Note: Before we get started, I want to do a bit of house keeping.
---
# Audience<br>Participation <!-- .slide: class="center" -->

Note: During this talk, there will be some audience participation segments. If
my hand is raised, or I ask a direct question, feel free to call out the
answer. 

If my hand isn't raised, don't call out. We don't want to spoil the answers for
anyone else who is playing along.
---
<br><br> 
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%"><c>// This is the size most of the</code></pre></div>
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%"><c>// code will be shown in</c></code></pre></div>
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%"><h>// If you cannot read this,</code></pre></div>
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%"><h>// please change seats</h></code></pre></div>
<br> 
<pre><code> 
Some less important code will be shown in this size
It's optimal you can also read this, but this is not a requirement<br>
</pre></code> 

Note: If you can read this code OK, then you're sitting in the right place. We will be going over quite a bit of code in this talk, from multiple languages, so it's essential you can view it properly.

The slides are already online, and I'll link to where they are available at the end.
---
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">> input JavaScript code</code></pre></div>
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">output result</code></pre></div>
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">> input</code></pre></div>
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">output</code></pre></div>
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">> <c>// comments</c></code></pre></div>
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">> "Some <h>highlights</h>"</code></pre></div>
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">> <c>// Assume JavaScript unless</c></code></pre></div>
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">> <c>// otherwise advised</c></code></pre></div>

Note: As per this slide, while there are many languages that will be referenced, unless otherwise stated, assume JavaScript.

Input will be prefaced with an input prompt, output will not.

---
# Let's get started! <!-- .slide: class="center" -->
---
# Hi! <!-- .slide: class="center" -->
Note: Hi, I'm Katie. If you've read my speaker bio it says that when I'm not changing the world, I enjoy making tapestries, cooking, and...
---

# Global Variables <!-- .slide: class="center" -->
Note: yelling at javascript and it's attempts at global variables.

This is because, when I was making my speaker bio many years ago, I was getting frustrated with my own code and my inability to remember how these worked in JavaScript.
---
<p></p> 
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">> ans</code></pre></div>

Note: So, say we have a variable called answer.

Remember, this is our input prompt.
---
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">> ans = "";</code></pre></div>
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">> function question() {<br>> &nbsp; var ans = 42;<br>> &nbsp; return ans;<br>> }</code></pre></div> <!-- .element: class="fragment" -->
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">> console.log(ans);</code></pre></div> <!-- .element: class="fragment" -->
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">""</code></pre></div> <!-- .element: class="fragment" -->
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">> console.log(question());</code></pre></div> <!-- .element: class="fragment" -->
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">42</code></pre></div> <!-- .element: class="fragment" -->
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">> console.log(ans);</code></pre></div> <!-- .element: class="fragment" -->
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">""</code></pre></div> <!-- .element: class="fragment" -->

Note: we assign answer to the empty string

We then create a function, queestion, which assigns a variable answer to 42. If we output the value of the variable answer, we get the empty string

If we output the value of the function question we get 42

If we then output the value of ans again, we get the empty string.
---
<p></p> 
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">> ans = "";</code></pre></div>
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">> function question() {<br>> &nbsp; <s>var</s> ans = 42; <br>> &nbsp; return ans;<br>> }</code></pre></div>
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">> console.log(ans);</code></pre></div>
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">""</code></pre></div>
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">> console.log(question());</code></pre></div>
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">42</code></pre></div>
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">> console.log(ans);</code></pre></div>
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">42</code></pre></div>

Note: the problem is that we weren't declaring our two ans variables with the same scope. if we remove the 'var', then we get the expected output, 42
---
# Duck Typing <!-- .slide: class="center" -->
Note: You know what's also frustrating? Duck typing.


if it looks like a duck and sounds like a duck, it's a duck.
---
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">> 4 + 2</code></pre></div>
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">6</code></pre></div> <!-- .element: class="fragment" -->
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">> 4 - 2</code></pre></div> <!-- .element: class="fragment" -->
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">2</code></pre></div> <!-- .element: class="fragment" -->
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">> "4" - 2</code></pre></div> <!-- .element: class="fragment" -->
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">2</code></pre></div> <!-- .element: class="fragment" -->
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">> "4" + 2</code></pre></div> <!-- .element: class="fragment" -->
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">"42"</code></pre></div> <!-- .element: class="fragment" -->

Note: (audience partipation with outputs)
---
# Equality <!-- .slide: class="center" -->
---
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">> 0 ==&nbsp; false</code></pre></div>
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">true</code></pre></div> <!-- .element: class="fragment" -->
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">> 1 == &nbsp;"1"</code></pre></div> <!-- .element: class="fragment" -->
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">true</code></pre></div> <!-- .element: class="fragment" -->
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">> 0 === false</code></pre></div> <!-- .element: class="fragment" -->
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">false</code></pre></div> <!-- .element: class="fragment" -->
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">> 1 === "1"</code></pre></div> <!-- .element: class="fragment" -->
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">false</code></pre></div> <!-- .element: class="fragment" -->
---
# Commutative Law <!-- .slide: class="center" -->

Note: This law refers to how some operands can happen in reverse order and their output isn't changed. For example, 2 + 3 is the same as 3 + 2
---
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">> {} || {}</code></pre></div>
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">{}</code></pre></div> <!-- .element: class="fragment" -->
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">> null || {}</code></pre></div> <!-- .element: class="fragment" -->
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">{}</code></pre></div> <!-- .element: class="fragment" -->
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">> {} || null</code></pre></div> <!-- .element: class="fragment" -->
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">Unexpected token ||</code></pre></div> <!-- .element: class="fragment" -->


Note: (audience partipation with outputs)
---
# Arrays and Objects <!-- .slide: class="center" -->
---
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">> [] + []</code></pre></div>
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">""</code></pre></div> <!-- .element: class="fragment" -->
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">> [] + {}</code></pre></div> <!-- .element: class="fragment" -->
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">[object Object]</code></pre></div> <!-- .element: class="fragment" -->
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">> {} + []</code></pre></div> <!-- .element: class="fragment" -->
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">0</code></pre></div> <!-- .element: class="fragment" -->
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">> {} + {}</code></pre></div> <!-- .element: class="fragment" -->
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">NaN</code></pre></div> <!-- .element: class="fragment" -->

Note: (audience partipation with outputs)
---

 <img src="pictures/wat.jpg" />
<span class="dasfoot"><a href="https://www.destroyallsoftware.com/talks/wat">destroyallsoftware.com</a></span>
Note: wat.


For those of you familiar with Gary Bernhardt's 'wat' talk, this isn't that talk.
---

 <img src="pictures/mini_wat.jpg" />

<span class="dasfoot"><a href="https://500px.com/photo/140476163/wat-by-edunham">wat, Emily Dunham, CC-BY-SA</a></span>
Note: what this is, is a talk that describes some of the hidden wats in javascript, and more specifically
---
# Why? <!-- .slide: class="center" -->
Note: Why. Why are these basic language constructs so illogical?
---

# JavaScript History<br>in 30 words or less <!-- .slide: class="center" -->
Note: I don't have time to tell the entire history of javascript

Check out the YUI Theatre series

For more, see "Crockford on JavaScript"

---

### In 1995, JavaScript was developed in 10 days <!-- .slide: class="center" -->
### by Brendan Eich for Netscape
### to offer a lightweight version of Java
### in order to compete for users with Microsoft.

Note: Let's step through that
---


### In 1995, JavaScript was developed in 10 days <!-- .slide: class="center" -->
### &nbsp;
### &nbsp;
### &nbsp;
Note: awfully short development time

just by that alone could explain things.
---
### In 1995, JavaScript was developed in 10 days <!-- .slide: class="center" -->
### by Brendan Eich for Netscape
### &nbsp;
### &nbsp;
Note: 
Eich originally wanted to make scheme

Sure, they said

Oh wait, that's scheme, that's gross, don't do that.
---
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">> (define hello-world</code></pre></div>
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">>&nbsp; (lambda ()</code></pre></div>
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">>&nbsp; &nbsp; (begin</code></pre></div>
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">>&nbsp; &nbsp; &nbsp; (write ‘Hello-World)</code></pre></div>
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">>&nbsp; &nbsp; )</code></pre></div>
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">>&nbsp; )</code></pre></div>
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">> )</code></pre></div>
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">></code></pre></div>
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">> (hello-world)</code></pre></div>
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">Hello-World</code></pre></div>
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%"></code></pre></div>
Note: We could have written in the browser like this
---
### In 1995, JavaScript was developed in 10 days <!-- .slide: class="center" -->
### by Brendan Eich for Netscape
### &nbsp;
### &nbsp;

Note: For user adoption, maybe it wasn't the best
---

### In 1995, JavaScript was developed in 10 days <!-- .slide: class="center" -->
### by Brendan Eich for Netscape
### to offer a lightweight version of Java
### &nbsp;


Note: so Eich made it look like Java, basing it a bit on Scheme and Self as well

Originally called LiveScript. Changed to JavaScript because it was kinda based on int

But Sun owned the trademark, so Sun owned the JavaScript trademark

Which is now owned by Oracle


Java could have been the language of the web

Java Applets

---

### In 1995, JavaScript was developed in 10 days <!-- .slide: class="center" -->
### by Brendan Eich for Netscape
### to offer a lightweight version of Java
### in order to compete for users with Microsoft.

Note: Mosaic split into NetScape in SpyGlass

Netscape says: "we're going to wipe out MS!"

MS says: "whoops, buying spyglass"

race was on to develop the scriting language to make the web better

Because trademark, MS reverse engineered JS, called it JScript

---

# JavaScript™ <!-- .slide: class="center" -->

<span class="bfoot" style="bottom: -280px"><a href="http://tsdr.uspto.gov/#caseNumber=75026640&caseType=SERIAL_NO&searchType=statusSearch">US Trademark &#35;75026640</a></foot>
Note: Yes, it's trademarked.

---

# ECMAScript <!-- .slide: class="center" -->
### A general purpose, cross-platform programming language

Note: Because of some fun issues, Tim Berners Lee and W3C wouldn't do the standard

TBL was apparently upset that Netscape took his simple design and made it silly

with things like images and formatting



They ended up at the

European Computer Manufacturers Association

They couldn't think of a better name

Working title: ECMA Script (ecc-ma)


---

# The most<br>popular language.<br>Ever. <!-- .slide: class="center" -->
Note: what percentage of the world uses the internet?

I posit that there are more uses of JS than any other lanaguage ever

What percentage of the internet uses JS?

Given this user base, there are more developers of JS than any other language

Butt-loads of complaints

It may also be the most complained about language
But not without some reason

---
# wat <!-- .slide: class="center" -->

Note: 

aka footguns

Things you can shoot yourself with in the foot

---

# Global Variables <!-- .slide: class="center" -->
Note: Incidently, first listing in The Good Parts - Appendix A - The Awful Parts
---

<p></p> 
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">> ans = "";</code></pre></div>
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">> function question() {<br>> &nbsp; var ans = 42; <br>> &nbsp; return ans;<br>> }</code></pre></div>
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">> console.log(ans);</code></pre></div>
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">""</code></pre></div>
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">> console.log(question());</code></pre></div>
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">42</code></pre></div>
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">> console.log(ans);</code></pre></div>
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">""</code></pre></div>
---
<p></p> 
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">> ans = ""; <c>// global</code></pre></div>
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">> function question() {<br>> &nbsp; var ans = 42; <c> // local</c> <br>> &nbsp; return ans;<br>> }</code></pre></div>
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">> console.log(ans);</code></pre></div>
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">""</code></pre></div>
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">> console.log(question());</code></pre></div>
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">42</code></pre></div>
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">> console.log(ans);</code></pre></div>
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">""</code></pre></div>
---
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%"><c>//ruby</c></code></pre></div>
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%"><h>@</h>ans = 42;</code></pre></div>
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%"></code></pre></div>
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%"><c>//python</c></code></pre></div>
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%"><h>global</h> ans = 42;</code></pre></div>
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%"></code></pre></div>
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%"><c>//java</code></pre></div>
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%"><h>public</h> static ans = 42;</code></pre></div>
Note: Because every other language has locals by default
---
# Overloaded<br>`+` operand <!-- .slide: class="center" -->
---
<p></p> 
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">> 4 + 2</code></pre></div>
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">6</code></pre></div>
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">> 4 - 2</code></pre></div>
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">2</code></pre></div>
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">> "4" - 2</code></pre></div>
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">2</code></pre></div>
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">> "4" + 2</code></pre></div>
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">"42"</code></pre></div>
---
<p></p> 
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">> 4 + 2</code></pre></div>
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">6</code></pre></div>
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">> 4 - 2</code></pre></div>
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">2</code></pre></div>
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">> "4" - 2</code></pre></div>
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">2 <c>&nbsp;&nbsp; // type → integer</c></code></pre></div>
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">> "4" + 2</code></pre></div>
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">"42"<c> // type → string</c></code></pre></div>
Note: `+` for both additon and concatenation
---

# Equality<br>and<br>Type Coersion <!-- .slide: class="center" -->
---
<p></p> 
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">> 0 ==&nbsp; false</code></pre></div>
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">true</code></pre></div>
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">> 0 === false</code></pre></div>
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">false</code></pre></div>
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">> 1 == &nbsp;"1"</code></pre></div>
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">true</code></pre></div>
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">> 1 === "1"</code></pre></div>
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">false</code></pre></div>
---
<p></p> 
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">> 0 ==&nbsp; false</code></pre></div>
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">true</code></pre></div>
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">> 0 === false</code></pre></div>
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">false</code></pre></div>
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">> 1 == &nbsp;"1" <c>// equality</code></pre></div>
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">true</code></pre></div>
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">> 1 === "1" <c>// equality without</c></code></pre></div>
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">false &nbsp; &nbsp; &nbsp; <c>// type coersion</c></code></pre></div>
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%"><h>// always use ===</h></code></pre></div> <!-- .element: class="fragment" -->

Note: This was picked up v. early by Brendan Eich

But because legacy, the standards committee didn't accept the change to `==`

forced creation of `===`
---
# `NaN` <!-- .slide: class="center" -->
Note: More gotchas, Combination of original 'Bad Parts', 'Awful Parts', and some new Fun
---
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">> typeof NaN</code></pre></div>
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">"number"</code></pre></div>
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">> NaN === NaN</code></pre></div> <!-- .element: class="fragment" -->
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">false</code></pre></div> <!-- .element: class="fragment" -->
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">> NaN !== NaN</code></pre></div> <!-- .element: class="fragment" -->
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">true</code></pre></div> <!-- .element: class="fragment" -->
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">> isFinite(NaN)</code></pre></div> <!-- .element: class="fragment" -->
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">false</code></pre></div> <!-- .element: class="fragment" -->
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%"><h>// if typeof a === "number" <br> &nbsp; &nbsp;&nbsp; && isFinite(a)</h></code></pre></div> <!-- .element: class="fragment" -->
---
# `parseInt` <!-- .slide: class="center" -->
---
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">> parseInt("42")</code></pre></div>
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">42</code></pre></div> <!-- .element: class="fragment" -->
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">> parseInt("42 Wallaby Way")</code></pre></div> <!-- .element: class="fragment" -->
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">42</code></pre></div> <!-- .element: class="fragment" -->
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">> parseInt("04")</code></pre></div> <!-- .element: class="fragment" -->
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">4</code></pre></div> <!-- .element: class="fragment" -->
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">> parseInt("08")</code></pre></div> <!-- .element: class="fragment" -->
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">0</code></pre></div> <!-- .element: class="fragment" -->
---
<p></p> 
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">> parseInt("42")</code></pre></div>
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">42</code></pre></div>
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">> parseInt("42 Wallaby Way")</code></pre></div>
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">42</code></pre></div>
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">> parseInt("04") <c>// radix 10</c></code></pre></div>
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">4</code></pre></div>
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">> parseInt("08") <c>// octal</c></code></pre></div>
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">0</code></pre></div>
---
# `Number` <!-- .slide: class="center" -->
---
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">> 4 + 2</code></pre></div>
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">6</code></pre></div> <!-- .element: class="fragment" -->
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">> 40 + 20</code></pre></div> <!-- .element: class="fragment" -->
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">60</code></pre></div> <!-- .element: class="fragment" -->
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">> 0.4 + 0.2</code></pre></div> <!-- .element: class="fragment" -->
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">0.6000000000000001</code></pre></div> <!-- .element: class="fragment" -->
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%"><c>// All Number in JavaScript<br>// are IEEE-754 floats</c></code></pre></div> <!-- .element: class="fragment" -->
Note: All numbers are IEEE 754 floats

Fix this by dealing with 'round' numbers. Money - work in cents
---
# Extended<br>Character Set <!-- .slide: class="center" -->
---
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">> "abc".split("")</code></pre></div>
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">["a","b","c"]</code></pre></div> <!-- .element: class="fragment" -->
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">> "<img src="pictures/penguin.svg" class="e" style="margin: 0"><img src="pictures/koala.svg" style="margin: 0" class="e">".split("")</code></pre></div> <!-- .element: class="fragment" -->
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">["�","�","�","�"]</code></pre></div> <!-- .element: class="fragment" -->
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">> Array.from("<img src="pictures/penguin.svg" class="e" style="margin: 0"><img src="pictures/koala.svg" style="margin: 0" class="e">")</code></pre></div> <!-- .element: class="fragment" -->
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">["<img src="pictures/penguin.svg" class="e" style="margin: 0">","<img src="pictures/koala.svg" style="margin: 0" class="e">"]</code></pre></div> <!-- .element: class="fragment" -->

Note: Unicode extended characterset

Javascript was created before unicode was super popular, so some parts don't understand extended characters

---

# This thing <!-- .slide: class="center" -->
## `++[[]][+[]]+[+[]]` <!-- .slide: class="center" -->
Note: audience participation -- guess
---
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">> ++[[]][+[]]+[+[]]</code></pre></div>
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">10</code></pre></div> <!-- .element: class="fragment" -->

---
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">> []</code></pre></div>
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">""</code></pre></div> <!-- .element: class="fragment" -->
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">> +[] <c>&nbsp; // +""</c></code></pre></div> <!-- .element: class="fragment" -->
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">0</code></pre></div> <!-- .element: class="fragment" -->
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">> [[]] <c> // [""] </c></code></pre></div> <!-- .element: class="fragment" -->
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">""</code></pre></div> <!-- .element: class="fragment" -->
---
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">> [[]][+[]] <c> &nbsp;// [""][0]</c></code></pre></div>
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">""</code></pre></div> <!-- .element: class="fragment" -->
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">> +[[]][+[]] <c> // +""</code></pre></div> <!-- .element: class="fragment" -->
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">0</code></pre></div> <!-- .element: class="fragment" -->
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">> ++[[]][+[]] <c>// ++0 </c></code></pre></div> <!-- .element: class="fragment" -->
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">1</code></pre></div> <!-- .element: class="fragment" -->
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">> ++[[]][+[]] <h>+</h> [+[]]</code></pre></div> <!-- .element: class="fragment" -->
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">10</code></pre></div> <!-- .element: class="fragment" -->

Note: pre-increment only works on some objects, not directly on number literals
---

<pre><code> 
[][(![]+[])[+[]]+([![]]+[][[]])[+!+[]+[+[]]]+(![]+[])[!+[]+!+[]]+( 
!![]+[])[+[]]+(!![]+[])[!+[]+!+[]+!+[]]+(!![]+[])[+!+[]]][([][(![] 
+[])[+[]]+([![]]+[][[]])[+!+[]+[+[]]]+(![]+[])[!+[]+!+[]]+(!![]+[] 
)[+[]]+(!![]+[])[!+[]+!+[]+!+[]]+(!![]+[])[+!+[]]]+[])[!+[]+!+[]+! 
+[]]+(!![]+[][(![]+[])[+[]]+([![]]+[][[]])[+!+[]+[+[]]]+(![]+[])[! 
+[]+!+[]]+(!![]+[])[+[]]+(!![]+[])[!+[]+!+[]+!+[]]+(!![]+[])[+!+[] 
]])[+!+[]+[+[]]]+([][[]]+[])[+!+[]]+(![]+[])[!+[]+!+[]+!+[]]+(!![] 
+[])[+[]]+(!![]+[])[+!+[]]+([][[]]+[])[+[]]+([][(![]+[])[+[]]+([![ 
]]+[][[]])[+!+[]+[+[]]]+(![]+[])[!+[]+!+[]]+(!![]+[])[+[]]+(!![]+[ 
])[!+[]+!+[]+!+[]]+(!![]+[])[+!+[]]]+[])[!+[]+!+[]+!+[]]+(!![]+[]) 
[+[]]+(!![]+[][(![]+[])[+[]]+([![]]+[][[]])[+!+[]+[+[]]]+(![]+[])[ 
!+[]+!+[]]+(!![]+[])[+[]]+(!![]+[])[!+[]+!+[]+!+[]]+(!![]+[])[+!+[ 
]]])[+!+[]+[+[]]]+(!![]+[])[+!+[]]]((![]+[])[!+[]+!+[]]+([][(![]+[ 
])[+[]]+([![]]+[][[]])[+!+[]+[+[]]]+(![]+[])[!+[]+!+[]]+(!![]+[])[ 
+[]]+(!![]+[])[!+[]+!+[]+!+[]]+(!![]+[])[+!+[]]]+[])[!+[]+!+[]+!+[ 
]]+(![]+[])[+!+[]]+[!+[]+!+[]]+[+[]]+[+!+[]]+[!+[]+!+[]+!+[]+!+[]+ 
!+[]+!+[]+!+[]])() 
</code></pre> 

 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">lca2017</code></pre></div> <!-- .element: class="fragment" -->

<span class="dasfoot"><a href="http://www.jsfuck.com/">esoteric javascript, @aemkei</a></span>
---
# Arrays are Objects <!-- .slide: class="center" -->
## Kinda.

Note: they are special, with integer keys and special sugar.
See eariler partial working of addressing array keys
---

 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">> typeof { a: "b" }</code></pre></div>
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">"object"</code></pre></div> <!-- .element: class="fragment" -->
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">> typeof ["a","b"]</code></pre></div> <!-- .element: class="fragment" -->
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">"object"</code></pre></div> <!-- .element: class="fragment" -->
---
# `typeof` <!-- .slide: class="center" -->
Note: Big typeof
---
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">> typeof Object()</code></pre></div>
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">"object"</code></pre></div> <!-- .element: class="fragment" -->
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">> typeof Number()</code></pre></div> <!-- .element: class="fragment" -->
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">"number"</code></pre></div> <!-- .element: class="fragment" -->
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">> typeof String()</code></pre></div> <!-- .element: class="fragment" -->
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">"string"</code></pre></div> <!-- .element: class="fragment" -->
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">> typeof Boolean()</code></pre></div> <!-- .element: class="fragment" -->
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">"boolean"</code></pre></div> <!-- .element: class="fragment" -->
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">> typeof null</code></pre></div> <!-- .element: class="fragment" -->
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">"object"</code></pre></div> <!-- .element: class="fragment" -->
Note: even JScript dutifully reverse engineered this error

It's a bug
---
<p></p> 
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">> typeof Object()</code></pre></div>
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">"object" <h> // JSVAL_OBJECT &nbsp; 0x0</h></code></pre></div>
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">> typeof Number()</code></pre></div>
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">"number"</code></pre></div>
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">> typeof String()</code></pre></div>
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">"string" <h> // JSVAL_STRING &nbsp; 0x4</h></code></pre></div>
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">> typeof Boolean()</code></pre></div>
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">"boolean" <h>// JSVAL_BOOLEAN &nbsp;0x6</h></code></pre></div>
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">> typeof null</code></pre></div>
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">"object"&nbsp; <c>// 0x00 pointer </c></code></pre></div>

---
<pre><code><c>// source/js/src/jsapi.c</c><br>
JS_TypeOfValue(JSContext *cx, jsval v) {
&nbsp; &nbsp; if (JSVAL_IS_VOID(v)) {
&nbsp; &nbsp; &nbsp; &nbsp; type = JSTYPE_VOID;
&nbsp; &nbsp; } else if (JSVAL_IS_OBJECT(v)) {
&nbsp; &nbsp; &nbsp; &nbsp; if (...) {
&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; type = JSTYPE_FUNCTION;
&nbsp; &nbsp; &nbsp; &nbsp; } else {
&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; type = JSTYPE_OBJECT;
&nbsp; &nbsp; &nbsp; &nbsp; }
&nbsp; &nbsp; } else if (JSVAL_IS_NUMBER(v)) {
&nbsp; &nbsp; &nbsp; &nbsp; type = JSTYPE_NUMBER;
&nbsp; &nbsp; } else if (JSVAL_IS_STRING(v)) {
&nbsp; &nbsp; &nbsp; &nbsp; type = JSTYPE_STRING;
&nbsp; &nbsp; } else if (JSVAL_IS_BOOLEAN(v)) {
&nbsp; &nbsp; &nbsp; &nbsp; type = JSTYPE_BOOLEAN;
&nbsp; &nbsp; }
&nbsp; &nbsp; return type;
} 
</pre></code> 


<span class="dasfoot"><a href="http://mxr.mozilla.org/classic/source/js/src/jsapi.h">jsapi from October 1996</a></span>
---
<pre><code><c>// source/js/src/jsapi.c</c><br>
JS_TypeOfValue(JSContext *cx, jsval v) {
&nbsp; &nbsp; <h>if</h> (JSVAL_IS_VOID(v)) {
&nbsp; &nbsp; &nbsp; &nbsp; type = JSTYPE_VOID;
&nbsp; &nbsp; } <h>else if</h> (JSVAL_IS_OBJECT(v)) {
&nbsp; &nbsp; &nbsp; &nbsp; <h>if</h> (...) {
&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; type = JSTYPE_FUNCTION;
&nbsp; &nbsp; &nbsp; &nbsp; } <h>else</h> {
&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; type = JSTYPE_OBJECT;
&nbsp; &nbsp; &nbsp; &nbsp; }
&nbsp; &nbsp; } <h>else if</h> (JSVAL_IS_NUMBER(v)) {
&nbsp; &nbsp; &nbsp; &nbsp; type = JSTYPE_NUMBER;
&nbsp; &nbsp; } <h>else if</h> (JSVAL_IS_STRING(v)) {
&nbsp; &nbsp; &nbsp; &nbsp; type = JSTYPE_STRING;
&nbsp; &nbsp; } <h>else if</h> (JSVAL_IS_BOOLEAN(v)) {
&nbsp; &nbsp; &nbsp; &nbsp; type = JSTYPE_BOOLEAN;
&nbsp; &nbsp; }
&nbsp; &nbsp; return type;
} 
</pre></code> 


<span class="dasfoot"><a href="http://mxr.mozilla.org/classic/source/js/src/jsapi.h">jsapi from October 1996</a></span>
---
<pre><code><c>// source/js/src/jsapi.c</c><br>
JS_TypeOfValue(JSContext *cx, jsval v) {
&nbsp; &nbsp; if (<h>JSVAL_IS_VOID(v)</h>) { <c>// v == JSVAL_VOID</c>
&nbsp; &nbsp; &nbsp; &nbsp; type = JSTYPE_VOID;
&nbsp; &nbsp; } else if (JSVAL_IS_OBJECT(v)) {
&nbsp; &nbsp; &nbsp; &nbsp; if (...) {
&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; type = JSTYPE_FUNCTION;
&nbsp; &nbsp; &nbsp; &nbsp; } else {
&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; type = JSTYPE_OBJECT;
&nbsp; &nbsp; &nbsp; &nbsp; }
&nbsp; &nbsp; } else if (JSVAL_IS_NUMBER(v)) {
&nbsp; &nbsp; &nbsp; &nbsp; type = JSTYPE_NUMBER;
&nbsp; &nbsp; } else if (JSVAL_IS_STRING(v)) {
&nbsp; &nbsp; &nbsp; &nbsp; type = JSTYPE_STRING;
&nbsp; &nbsp; } else if (JSVAL_IS_BOOLEAN(v)) {
&nbsp; &nbsp; &nbsp; &nbsp; type = JSTYPE_BOOLEAN;
&nbsp; &nbsp; }
&nbsp; &nbsp; return type;
} 
</pre></code> 
<span class="dasfoot"><a href="http://mxr.mozilla.org/classic/source/js/src/jsapi.h">jsapi from October 1996</a></span>
---
<pre><code><c>// source/js/src/jsapi.c</c><br>
JS_TypeOfValue(JSContext *cx, jsval v) {
&nbsp; &nbsp; if (JSVAL_IS_VOID(v)) {
&nbsp; &nbsp; &nbsp; &nbsp; type = JSTYPE_VOID;
&nbsp; &nbsp; } else if (<h>JSVAL_IS_OBJECT(v)</h>) { <c>// JSVAL_TAG(v) == JSVAL_OBJECT</c>
&nbsp; &nbsp; &nbsp; &nbsp; if (...) {
&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; type = JSTYPE_FUNCTION;
&nbsp; &nbsp; &nbsp; &nbsp; } else {
&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; type = JSTYPE_OBJECT;
&nbsp; &nbsp; &nbsp; &nbsp; }
&nbsp; &nbsp; } else if (JSVAL_IS_NUMBER(v)) {
&nbsp; &nbsp; &nbsp; &nbsp; type = JSTYPE_NUMBER;
&nbsp; &nbsp; } else if (JSVAL_IS_STRING(v)) {
&nbsp; &nbsp; &nbsp; &nbsp; type = JSTYPE_STRING;
&nbsp; &nbsp; } else if (JSVAL_IS_BOOLEAN(v)) {
&nbsp; &nbsp; &nbsp; &nbsp; type = JSTYPE_BOOLEAN;
&nbsp; &nbsp; }
&nbsp; &nbsp; return type;
} 
</pre></code> 


<span class="dasfoot"><a href="http://mxr.mozilla.org/classic/source/js/src/jsapi.h">jsapi from October 1996</a></span>
---
<pre><code><c>// source/js/src/jsapi.c</c><br>
JS_TypeOfValue(JSContext *cx, jsval v) {
&nbsp; &nbsp; if (JSVAL_IS_VOID(v)) {
&nbsp; &nbsp; &nbsp; &nbsp; type = JSTYPE_VOID;
&nbsp; &nbsp; } else if (JSVAL_IS_OBJECT(v)) {
&nbsp; &nbsp; &nbsp; &nbsp; if (...) { <c>// Excuse me, are you a function?</c>
&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; type = JSTYPE_FUNCTION;
&nbsp; &nbsp; &nbsp; &nbsp; } else {
&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; type = JSTYPE_OBJECT;
&nbsp; &nbsp; &nbsp; &nbsp; }
&nbsp; &nbsp; } else if (JSVAL_IS_NUMBER(v)) {
&nbsp; &nbsp; &nbsp; &nbsp; type = JSTYPE_NUMBER;
&nbsp; &nbsp; } else if (JSVAL_IS_STRING(v)) {
&nbsp; &nbsp; &nbsp; &nbsp; type = JSTYPE_STRING;
&nbsp; &nbsp; } else if (JSVAL_IS_BOOLEAN(v)) {
&nbsp; &nbsp; &nbsp; &nbsp; type = JSTYPE_BOOLEAN;
&nbsp; &nbsp; }
&nbsp; &nbsp; return type;
} 
</pre></code> 


<span class="dasfoot"><a href="http://mxr.mozilla.org/classic/source/js/src/jsapi.h">jsapi from October 1996</a></span>
---
<pre><code><c>// source/js/src/jsapi.c</c><br>
JS_TypeOfValue(JSContext *cx, jsval v) {
&nbsp; &nbsp; if (JSVAL_IS_VOID(v)) {
&nbsp; &nbsp; &nbsp; &nbsp; type = JSTYPE_VOID;
&nbsp; &nbsp; } else if (JSVAL_IS_OBJECT(v)) {
&nbsp; &nbsp; &nbsp; &nbsp; if (...) {
&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; type = JSTYPE_FUNCTION;
&nbsp; &nbsp; &nbsp; &nbsp; } <h>else</h> {
&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; type = JSTYPE_OBJECT;
&nbsp; &nbsp; &nbsp; &nbsp; }
&nbsp; &nbsp; } else if (JSVAL_IS_NUMBER(v)) {
&nbsp; &nbsp; &nbsp; &nbsp; type = JSTYPE_NUMBER;
&nbsp; &nbsp; } else if (JSVAL_IS_STRING(v)) {
&nbsp; &nbsp; &nbsp; &nbsp; type = JSTYPE_STRING;
&nbsp; &nbsp; } else if (JSVAL_IS_BOOLEAN(v)) {
&nbsp; &nbsp; &nbsp; &nbsp; type = JSTYPE_BOOLEAN;
&nbsp; &nbsp; }
&nbsp; &nbsp; return type;
} 
</pre></code> 


<span class="dasfoot"><a href="http://mxr.mozilla.org/classic/source/js/src/jsapi.h">jsapi from October 1996</a></span>
---
<pre><code><c>// source/js/src/jsapi.c</c><br>
JS_TypeOfValue(JSContext *cx, jsval v) {
&nbsp; &nbsp; if (JSVAL_IS_VOID(v)) {
&nbsp; &nbsp; &nbsp; &nbsp; type = JSTYPE_VOID;
&nbsp; &nbsp; } else if (JSVAL_IS_OBJECT(v)) {
&nbsp; &nbsp; &nbsp; &nbsp; if (...) {
&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; type = JSTYPE_FUNCTION;
&nbsp; &nbsp; &nbsp; &nbsp; } else {
&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; <h>type = JSTYPE_OBJECT</h>;
&nbsp; &nbsp; &nbsp; &nbsp; }
&nbsp; &nbsp; } else if (JSVAL_IS_NUMBER(v)) {
&nbsp; &nbsp; &nbsp; &nbsp; type = JSTYPE_NUMBER;
&nbsp; &nbsp; } else if (JSVAL_IS_STRING(v)) {
&nbsp; &nbsp; &nbsp; &nbsp; type = JSTYPE_STRING;
&nbsp; &nbsp; } else if (JSVAL_IS_BOOLEAN(v)) {
&nbsp; &nbsp; &nbsp; &nbsp; type = JSTYPE_BOOLEAN;
&nbsp; &nbsp; }
&nbsp; &nbsp; return type;
} 
</pre></code> 


<span class="dasfoot"><a href="http://mxr.mozilla.org/classic/source/js/src/jsapi.h">jsapi from October 1996</a></span>

---
<pre><code><c>// source/js/src/jsapi.c</c><br>
JS_TypeOfValue(JSContext *cx, jsval v) {
&nbsp; &nbsp; if (JSVAL_IS_VOID(v)) {
&nbsp; &nbsp; &nbsp; &nbsp; type = JSTYPE_VOID;
&nbsp; &nbsp; } else if (JSVAL_IS_OBJECT(v)) {
&nbsp; &nbsp; &nbsp; &nbsp; if (...) {
&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; type = JSTYPE_FUNCTION;
&nbsp; &nbsp; &nbsp; &nbsp; } else {
&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; type = JSTYPE_OBJECT;
&nbsp; &nbsp; &nbsp; &nbsp; }
&nbsp; &nbsp; } else if (JSVAL_IS_NUMBER(v)) {
&nbsp; &nbsp; &nbsp; &nbsp; type = JSTYPE_NUMBER;
&nbsp; &nbsp; } else if (JSVAL_IS_STRING(v)) {
&nbsp; &nbsp; &nbsp; &nbsp; type = JSTYPE_STRING;
&nbsp; &nbsp; } else if (JSVAL_IS_BOOLEAN(v)) {
&nbsp; &nbsp; &nbsp; &nbsp; type = JSTYPE_BOOLEAN;
&nbsp; &nbsp; }
&nbsp; &nbsp; <h>return type</h>;
} 
</pre></code> 
<span class="dasfoot"><a href="http://mxr.mozilla.org/classic/source/js/src/jsapi.h">jsapi from October 1996</a></span>
---
## Yes, this is a bug. <!-- .slide: class="center" -->
## This is a old, known bug. <!-- .element: class="fragment" -->
---
# Backwards<br>Compatibility <!-- .slide: class="center" -->

Note: 


JS has no versioning. You can't specify a specific version, like Python, etc.

JS = most popular language

Most users

Most impact

Biggest user base *ever*. Backward compatibility is not optional

The internet would *break*

And if that's not enough, we have to think about more things

---
# Security <!-- .slide: class="center" -->
Note: on top of the things you know JS does

you have to worry about the things that you *really* don't want it to do
---

## Cross Site Scripting <!-- .slide: class="center" -->
### XSS <!-- .slide: class="center" -->

Note: this is one of the big players in the OWASP Top 10. It poses an enourmous security risk
---

## Cross Site Request Forgery <!-- .slide: class="center" -->
### CSRF <!-- .slide: class="center" -->

Note: within scope, but not strictly JS
---

### `document.execCommand('copy');` <!-- .slide: class="center" -->

<span class="bfoot" style="bottom: -280px"><a href="https://github.com/dxa4481/Pastejacking/blob/master/index.html">dxa4481/pastejacking</a></span>
Note: New line in a terminal will auto execute
---
# `eval` <!-- .slide: class="center" -->

Note: executing arbitary code.

Because what could possibly go wrong

---
<br><br> 
<pre><code style="overflow: hidden; width: 100%; white-space: pre-wrap"><h>eval(</h>function(p,a,c,k,e,d){e&#61;function(c){return c.toString(36)};if(!''.replace(/^/,String)){while(c--){d[c.toString(a)]&#61;k[c]||c.toString(a)}k&#61;[function(e){return d[e]}];e&#61;function(){return'\\w+'};c&#61;1};while(c--){if(k[c]){p&#61;p.replace(new RegExp('\\b'+e(c)+'\\b','g'),k[c])}}return p}('8 3&#61;["\\7\\1\\6\\4\\2\\1\\2\\5\\9\\a\\4\\2\\b\\1\\d"]c(3[0])',14,14,<br>'|x61|x20|_0xfb59|x65|x6E|x76|x48|var|x69|x63|x64|alert|x79'<br>.split('|'),0,{})<h>)</h>
</pre></code> 

 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">alert("Have a nice day")</code></pre></div> <!-- .element: class="fragment" -->
Note: Would anyone where want to have this code on their systems>

(postreveal) see? nothing malicious, right?
---
# 😢 <!-- .slide: class="center" -->
Note: 
so, that's what javascript can do. it's powerful, and scary. what if you say
---

# So don't use<br>JavaScript <!-- .slide: class="center" -->
---

### Image Sliders <!-- .slide: class="center" -->
### Modals
### Light Boxes
### Form Validation
### File Uploads
### ... all with HTML/CSS only.

<span class="bfoot" style="bottom: -100px"><a href="http://youmightnotneedjs.com/">You Might Not Need JavaScript.com</a></span>
---
# Using JavaScript<br>without JavaScript <!-- .slide: class="center" -->
---
# Pick any language <!-- .slide: class="center" -->

<span class="bfoot" style="bottom: -280px"><a href="https://github.com/jashkenas/coffeescript/wiki/list-of-languages-that-compile-to-js">List of languages that compile to JS</a></span>
---

### Ruby: Opal, Red, .. <!-- .slide: class="center" -->
### PHP: Uniter, phype, .. <!-- .element: class="fragment" -->
### Perl: Perlito, p2js, .. <!-- .element: class="fragment" -->
### Go: GopherJS, .. <!-- .element: class="fragment" -->
### Python: Skulpt, Brython, .. <!-- .element: class="fragment" -->
---
# Batavia <!-- .slide: class="center" -->
 <img src="pictures/pybee.svg" />

Note: throwback
---
### Haskell: ghcjs, haste, .. <!-- .slide: class="center" -->
### Cobol: CobolScript <!-- .element: class="fragment" -->
### C: Emscripten <!-- .element: class="fragment" -->
---
<video width="720" height="600" controls="controls"><source src="pictures/skifree.mp4" type="video/mp4" /></video>

<span class="bfoot" style="bottom: -20px"><a href="https://archive.org/details/win3_WINSKI">Internet Archive</a></span>
Note: Yes, that's windows 95 running in my browser
---
# JavaScript<br>outside the browser <!-- .slide: class="center" -->
---
# node.js <!-- .slide: class="center" -->
Note: serverside js

runtime environment, not a framework

runs on the V8 engine (next slide)
---

# V8<br>JavaScript Engine <!-- .slide: class="center" -->
Note: 

Chromium Browser engine.


Open source

'Isomorphic JavaScript' slash 'Universal javascript'
---
# V8 wat <!-- .slide: class="center" -->
Note: but even this implementation isn't without it's issue. Consider the following
---
<pre><code>'use strict';

function add(x, y) {
<c style="font-weight:normal">&nbsp; // I am the very model of a modern Major-General
&nbsp; // I've information vegetable, animal, and mineral
&nbsp; // I know the kings of England, and I quote the fights historical
&nbsp; // From Marathon to Waterloo, in order categorical
&nbsp; // I'm very well acquainted, too, with matters mathematical
&nbsp; // I understand equations, both the simple and quadratical
&nbsp; // About binomial theorem I'm teeming with a lot o' news
&nbsp; // With many cheerful facts about the square of the hypotenuse
&nbsp; // I'm very good at integral and differential calculus
&nbsp; // I know the scientific names of beings animalculous
</c> 
&nbsp; return(x + y);
} 

for (let i = 0; i < 500000000; i++) {
&nbsp; if (add(i, i++) < 5) { <c>/* */</c> }
} 
</code></pre> 

 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">$ time -p node general.js<br>real 1.91</code></pre></div> <!-- .element: class="fragment" -->

<span class="bfoot"><a href="https://top.fse.guru/nodejs-a-quick-optimization-advice-7353b820c92e">top.fse.guru</a></span>

Note: A function that runs a loop for a specific amount of time.

Note the massive comment block.
---
<pre><code>'use strict';

function add(x, y) {
<c style="font-weight:normal">&nbsp; // I am the very model of a modern Major-General
&nbsp; // I've information vegetable, animal, and mineral
&nbsp; // I know the kings of England, and I quote the fights historical
&nbsp; // From Marathon to Waterloo, in order categorical
&nbsp; // I'm very well acquainted, too, with matters mathematical
&nbsp; // I understand equations, both the simple and quadratical
&nbsp; // About binomial theorem I'm teeming with a lot o' news
&nbsp; // With many cheerful facts about the square of the hypotenuse
&nbsp; // I'm very good at integral and differential calculus
&nbsp; // I know the scientific names of beings animalculous
</c> 
&nbsp; return(x + y);
} 

for (let i = 0; i < 500000000; i++) {
&nbsp; if (add(i, i++) < 5) { <c>/* */</c> }
} 
</code></pre> 

<span class="bfoot" style="bottom: -135px"><a href="https://top.fse.guru/nodejs-a-quick-optimization-advice-7353b820c92e">top.fse.guru</a></span>


Note: (slide intentionally blank for flicking to the next one)
---
<pre><code>'use strict';

function add(x, y) {
<c style="font-weight:normal">&nbsp; // I am the very model of a modern Major-General
&nbsp; // I've information vegetable, animal, and mineral
&nbsp; // I know the kings of England, and I quote the fights historical
&nbsp; // From Marathon to Waterloo, in order categorical
&nbsp; // I'm very well acquainted, too, with matters mathematical
&nbsp; // I understand equations, both the simple and quadratical
&nbsp; // About binomial theorem I'm teeming with a lot o' news
&nbsp; // With many cheerful facts about the square of the hypotenuse
&nbsp; // I'm very good at integral and differential calculus
&nbsp; 
</c> 
&nbsp; return(x + y);
} 

for (let i = 0; i < 500000000; i++) {
&nbsp; if (add(i, i++) < 5) { <c>/* */</c> }
} 
</code></pre> 

 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">$ time -p node general.js<br>real 0.77<c> &nbsp;# vs 1.91</c></code></pre></div> <!-- .element: class="fragment" -->


<span class="bfoot"><a href="https://top.fse.guru/nodejs-a-quick-optimization-advice-7353b820c92e">top.fse.guru</a></span>

Note: What's going to happen? any change?



More than twice as fast


v8 optimisation handles functions differently if they are under 600 characters

INCLUDING COMMENTS
---
# Server Side Security <!-- .slide: class="center" -->
Note: 
---

## "The Little Doctor" <!-- .slide: class="center" -->
### Cross-platform XSS worm framework

<span class="dasfoot"><a href="https://github.com/infosec-au/little-doctor/">Source Code, GitHub</a> <a href="https://www.youtube.com/watch?v=jMKmPW99TFQ">Video</a></span>
Note: Demo'd at KiwiCon X

Rocket Chat is all made in Javascript frames in the mobile and desktop app

So the same vulnerability of being able to run the code....

---
# Package<br>Management <!-- .slide: class="center" -->
---

# <img src="pictures/npm.png"> <!-- .slide: class="center" -->
---

# <img src="pictures/wdu.png"> <!-- .slide: class="center" -->
Note: Wombat Developers Union
---
# <img src="pictures/wombatlogo.png"> <!-- .slide: class="center" -->
---
 <img src="pictures/WOMBAT.png" style="margin-top: -50px" />
Note: wombats are awesome.
---

# <img src="pictures/npm.png"> <!-- .slide: class="center" -->

Note: Node package manager

---
# left-pad <!-- .slide: class="center" -->

Note: Note well. This is not a cheap joke. I'm mentioning this specifically for a reason.
---
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%"><c>//stevemao/left-pad:index.js</c></code></pre></div>
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">module.exports = leftpad;</code></pre></div>
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">function leftpad (str, len, ch){</code></pre></div>
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">&nbsp; str = String(str);</code></pre></div>
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">&nbsp; var i = -1;</code></pre></div>
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">&nbsp; if (!ch && ch !== 0) ch = ' ';</code></pre></div>
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">&nbsp; len = len - str.length;</code></pre></div>
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">&nbsp; while (++i < len) {</code></pre></div>
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">&nbsp; &nbsp; &nbsp; str = ch + str; }</code></pre></div>
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">&nbsp; return str;</code></pre></div>
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">}</code></pre></div>

---
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%"><c>//stevemao/left-pad:index.js</c></code></pre></div>
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">module.exports = leftpad;</code></pre></div>
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">function leftpad (str, len, ch){</code></pre></div>
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">&nbsp; str = String(str);</code></pre></div>
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">&nbsp; var i = -1;</code></pre></div>
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">&nbsp; if (<h>!ch && ch !== 0</h>) <h>ch = ' '</h>;</code></pre></div>
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">&nbsp; len = len - str.length;</code></pre></div>
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">&nbsp; while (++i < len) {</code></pre></div>
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">&nbsp; &nbsp; &nbsp; str = ch + str; }</code></pre></div>
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">&nbsp; return str;</code></pre></div>
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">}</code></pre></div>

---
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%"><c>//stevemao/left-pad:index.js</c></code></pre></div>
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">module.exports = leftpad;</code></pre></div>
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">function leftpad (str, len, ch){</code></pre></div>
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">&nbsp; str = String(str);</code></pre></div>
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">&nbsp; var i = -1;</code></pre></div>
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">&nbsp; if (!ch && ch !== 0) ch = ' ';</code></pre></div>
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">&nbsp; len = <h>len - str.length</h>;</code></pre></div>
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">&nbsp; while (++i < len) {</code></pre></div>
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">&nbsp; &nbsp; &nbsp; str = ch + str; }</code></pre></div>
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">&nbsp; return str;</code></pre></div>
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">}</code></pre></div>
---
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%"><c>//stevemao/left-pad:index.js</c></code></pre></div>
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">module.exports = leftpad;</code></pre></div>
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">function leftpad (str, len, ch){</code></pre></div>
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">&nbsp; str = String(str);</code></pre></div>
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">&nbsp; var i = -1;</code></pre></div>
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">&nbsp; if (!ch && ch !== 0) ch = ' ';</code></pre></div>
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">&nbsp; len = len - str.length;</code></pre></div>
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">&nbsp; while <h>(++i < len)</h> {</code></pre></div>
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">&nbsp; &nbsp; &nbsp; str = ch + str; }</code></pre></div>
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">&nbsp; return str;</code></pre></div>
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">}</code></pre></div>

---
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">PHP_FUNCTION(str_pad) {</code></pre></div>
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">&nbsp; char &ast;input;</code></pre></div>
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">&nbsp; int input_len;</code></pre></div>
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">&nbsp; long &nbsp;pad_length;</code></pre></div>
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">&nbsp; char &ast;pad_str_val = " ";</code></pre></div>
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">&nbsp; <c>/&ast; ... &ast;/</c></code></pre></div>
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">&nbsp; num_pad_chars =</code></pre></div>
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">&nbsp; &nbsp; &nbsp;pad_length - input_len;</code></pre></div>
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">&nbsp; <c>/&ast; ... &ast;/</c></code></pre></div>

<span class="dasfoot"><a href="https://github.com/php/php-src/blob/PHP-5.6/ext/standard/string.c">php 5.6 - ext/standard/string.c</a></span>
---
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">PHP_FUNCTION(str_pad) {</code></pre></div>
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">&nbsp; char &ast;input;</code></pre></div>
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">&nbsp; int input_len;</code></pre></div>
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">&nbsp; long &nbsp;pad_length;</code></pre></div>
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">&nbsp; char <h>&ast;pad_str_val = " ";</h></code></pre></div>
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">&nbsp; <c>/&ast; ... &ast;/</c></code></pre></div>
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">&nbsp; num_pad_chars =</code></pre></div>
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">&nbsp; &nbsp; &nbsp;pad_length - input_len;</code></pre></div>
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">&nbsp; <c>/&ast; ... &ast;/</c></code></pre></div>

<span class="dasfoot"><a href="https://github.com/php/php-src/blob/PHP-5.6/ext/standard/string.c">php 5.6 - ext/standard/string.c</a></span>
---
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">PHP_FUNCTION(str_pad) {</code></pre></div>
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">&nbsp; char &ast;input;</code></pre></div>
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">&nbsp; int input_len;</code></pre></div>
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">&nbsp; long &nbsp;pad_length;</code></pre></div>
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">&nbsp; char &ast;pad_str_val = " ";</code></pre></div>
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">&nbsp; <c>/&ast; ... &ast;/</c></code></pre></div>
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">&nbsp; num_pad_chars =</code></pre></div>
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">&nbsp; &nbsp; &nbsp;<h>pad_length - input_len;</h></code></pre></div>
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">&nbsp; <c>/&ast; ... &ast;/</c></code></pre></div>

<span class="dasfoot"><a href="https://github.com/php/php-src/blob/PHP-5.6/ext/standard/string.c">php 5.6 - ext/standard/string.c</a></span>
---
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">&nbsp; <c>/&ast; cont. &ast;/</c></code></pre></div>
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">&nbsp;</code></pre></div>
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">&nbsp; <c>/&ast; ... &ast;/</c></code></pre></div>
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">&nbsp; for (i = 0; i < left_pad; i++)</code></pre></div>
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">&nbsp; &nbsp; result[result_len++]</code></pre></div>
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">&nbsp; &nbsp; &nbsp; = pad_str_val[i];</code></pre></div>
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">&nbsp; <c>/&ast; ... &ast;/</c></code></pre></div>
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">&nbsp; return result;</code></pre></div>
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">}</code></pre></div>

<span class="dasfoot"><a href="https://github.com/php/php-src/blob/PHP-5.6/ext/standard/string.c">php 5.6 - ext/standard/string.c</a></span>
---
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">&nbsp; <c>/&ast; cont. &ast;/</c></code></pre></div>
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">&nbsp;</code></pre></div>
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">&nbsp; <c>/&ast; ... &ast;/</c></code></pre></div>
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">&nbsp; <h>for (i = 0; i < left_pad; i++)</h></code></pre></div>
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">&nbsp; &nbsp; result[result_len++]</code></pre></div>
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">&nbsp; &nbsp; &nbsp; = pad_str_val[i];</code></pre></div>
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">&nbsp; <c>/&ast; ... &ast;/</c></code></pre></div>
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">&nbsp; return result;</code></pre></div>
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">}</code></pre></div>

<span class="dasfoot"><a href="https://github.com/php/php-src/blob/PHP-5.6/ext/standard/string.c">php 5.6 - ext/standard/string.c</a></span>
---

# User-land<br>"standard library" <!-- .slide: class="center" -->
Note: jquery

left-pad 
---
# Design by<br>Committee <!-- .slide: class="center" -->
Note: same loveingly maintained word document from version one.

15, 20 yaers, one word doc

over head
---
# However <!-- .slide: class="center" -->

---
# JavaScript<br>is improving <!-- .slide: class="center" -->
---

# ECMAScript 5 <!-- .slide: class="center" -->
Note: std intro'd in 2009

Mostly adpoted
---
# `isArray` <!-- .slide: class="center" -->
---
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">ES5> Array.isArray({ a: "b" })</code></pre></div>
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">false</code></pre></div> <!-- .element: class="fragment" -->
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">ES5> Array.isArray(["a","b"])</code></pre></div> <!-- .element: class="fragment" -->
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">true</code></pre></div> <!-- .element: class="fragment" -->
---

# Improved<br>`parseInt` <!-- .slide: class="center" -->

---
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">ES3> parseInt("08")</code></pre></div>
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">0</code></pre></div> <!-- .element: class="fragment" -->
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">ES<h>5</h>> parseInt("08")</code></pre></div> <!-- .element: class="fragment" -->
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">8</code></pre></div> <!-- .element: class="fragment" -->
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">ESx> parseInt("08", 10) <h>// radix</h></code></pre></div> <!-- .element: class="fragment" -->
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">8</code></pre></div> <!-- .element: class="fragment" -->
Note: assumed to be octal unless you have ECMAScript 5.
Supply radix to be cross compatible.
---
# `map` <!-- .slide: class="center" -->
---

 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">ES5> [1, 2, 3].map(Math.sqrt)</code></pre></div>
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">[1, 4, 9]</code></pre></div> <!-- .element: class="fragment" -->
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%"><c>// [Math.sqrt(1)<br>&nbsp; , Math.sqrt(2)<br>&nbsp; , Math.sqrt(3)]</c></code></pre></div> <!-- .element: class="fragment" -->
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">ES5> a = ['10','10','10','10']</code></pre></div> <!-- .element: class="fragment" -->
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">ES5> a.map(parseInt)</code></pre></div> <!-- .element: class="fragment" -->
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">[10, NaN, 2, 3]</code></pre></div> <!-- .element: class="fragment" -->
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%"><h>// Be aware of optional<br>// parameters</h></code></pre></div> <!-- .element: class="fragment" -->
---
# ECMAScript 6 <!-- .slide: class="center" -->
Note: approved in June 2015 (a few months ago)

Still very much not adpoted.
---
# `let` <!-- .slide: class="center" -->
---

 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%"><c>// life.js</c></code></pre></div>
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">function ans() {<br> &nbsp; var answer = 42; <br> &nbsp; return answer;<br>}</code></pre></div>
---
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%"><c>// life.js</c></code></pre></div>
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">function ans() {<br> &nbsp; <h>let</h> answer = 42; <br> &nbsp; return answer;<br>}</code></pre></div>

Note: proper block scope
Re-declarations are in error
---
# `import` <!-- .slide: class="center" -->
---
<p></p> 
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%"><c><!&dash;&dash;&dash; old importing --></c></code></pre></div>
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">&lt;html></code></pre></div>
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">&lt;script src="<h>life.js</h>">&lt;/script></code></pre></div>
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">&lt;script src="<h>stuff.js</h>">&lt;/script></code></pre></div>
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">...</code></pre></div>
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">&lt;/html></code></pre></div>
---
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%"><c>// life.js</c></code></pre></div>
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%"><h>export</h> function ans() {<br> &nbsp; let answer = 42; <br> &nbsp; return answer;<br>}</code></pre></div>
<br> 
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%"><c>// stuff.js</c> <br><h>import</h> { ans } from './life';</code></pre></div> <!-- .element: class="fragment" -->
---
# ECMAScript 5/6 Adoption <!-- .slide: class="center" -->
---
## kangax.github.io/compat-table/es5/ <!-- .slide: class="center" -->
## kangax.github.io/compat-table/es6/ <!-- .slide: class="center" -->
---
# Non-standard 'Standards' <!-- .slide: class="center" -->
---
# `console.log` <!-- .slide: class="center" -->
Note: Not actually a standard :D
---
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">> console.log("a string")</code></pre></div>
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">"a string"</code></pre></div> <!-- .element: class="fragment" -->

 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">> a = 42</code></pre></div> <!-- .element: class="fragment" -->
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">> console.log("a is: " + a);</code></pre></div> <!-- .element: class="fragment" -->
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">"a is 42"</code></pre></div> <!-- .element: class="fragment" -->
Note: basics
---
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">> console.time("Process")</code></pre></div>
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">> <c>// ... do the thing</c></code></pre></div> <!-- .element: class="fragment" -->
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">> console.timeEnd("Process")</code></pre></div> <!-- .element: class="fragment" -->
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">"Process: 1337ms"</code></pre></div> <!-- .element: class="fragment" -->

 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">> console.log("%cHello world!",<br>&nbsp;"color: red; font-size: 40px");</code></pre></div> <!-- .element: class="fragment" -->
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%"><span style="color: red; font-size: 70px">Hello world!</span></code></pre></div> <!-- .element: class="fragment" -->
Note: fancy extensions

try autocompleting for more, including grouping
---
<br><br> 
 <img src="pictures/facebook.png" />
Note: from console on facebook


OK I LIE
---

# `console.log` <!-- .slide: class="center" -->
## github.com/whatwg/console <!-- .slide: class="center" -->
Note: It's slowing getting standardaised :D

... by Web Hypertext Application Technology Working Group


their markup parser for standards doc createion is called...

bikeshed 

---
# Extending<br>JavaScript <!-- .slide: class="center" -->
---
# Polyfill <!-- .slide: class="center" -->
Note: Adding new funcionality in JS to JS by adding more JS
---
## `padStart` polyfill <!-- .slide: class="center" -->
---
<pre><code>if (!String.prototype.padStart) {
&nbsp; &nbsp; String.prototype.padStart = function padStart(maxLength,
&nbsp; &nbsp; &nbsp; fillString = ' ') {
&nbsp; &nbsp; &nbsp; &nbsp; const O = RequireObjectCoercible(this);
&nbsp; &nbsp; &nbsp; &nbsp; const S = String(O);
&nbsp; &nbsp; &nbsp; &nbsp; const intMaxLength = ToLength(maxLength);
&nbsp; &nbsp; &nbsp; &nbsp; const stringLength = ToLength(S.length);
&nbsp; &nbsp; &nbsp; &nbsp; if (intMaxLength <= stringLength) { return S; }
&nbsp; &nbsp; &nbsp; &nbsp; let filler = typeof fillString === 'undefined' ?
&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; ' ' : String(fillString);
&nbsp; &nbsp; &nbsp; &nbsp; if (filler === '') { return S; }
&nbsp; &nbsp; &nbsp; &nbsp; const fillLen = intMaxLength - stringLength;
&nbsp; &nbsp; &nbsp; &nbsp; while (filler.length < fillLen) {
&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; const fLen = filler.length;
&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; const remainingCodeUnits = fillLen - fLen;
&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; if (fLen > remainingCodeUnits) {
&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; filler += filler.slice(0, remainingCodeUnits);
&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; } else {
&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; filler += filler;
&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; }
&nbsp; &nbsp; &nbsp; &nbsp; }
&nbsp; &nbsp; &nbsp; &nbsp; const truncatedStringFiller = filler.slice(0, fillLen);
&nbsp; &nbsp; &nbsp; &nbsp; return truncatedStringFiller + S;
&nbsp; &nbsp; };
} 
</pre></code> 
---
## `isArray` polyfill <!-- .slide: class="center" -->
Note: you can also polyfill things that exist in ES5 but might not be available
---
### &nbsp; <!-- .slide: class="center" -->
<pre style="font-size: 30px"><code>if (!Array.isArray) {
&nbsp; Array.isArray = function(arg) {
&nbsp; &nbsp; return Object.prototype.toString.call(arg)
&nbsp; &nbsp; &nbsp; &nbsp; <h>=== '[object Array]';</h>
&nbsp;}; 
} 
</pre></code> 
Note: Can also polyfil things that may not exist in your browser. but specifically only define it if it's not already defined
---
## `console.log` polyfill <!-- .slide: class="center" -->
---
### &nbsp; <!-- .slide: class="center" -->
<pre style="font-size: 30px"><code>window.console =
&nbsp; &nbsp; typeof window.console === 'undefined' ? {
&nbsp; &nbsp; &nbsp; &nbsp; log: function(str) {
&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; alert(str)
&nbsp; &nbsp; &nbsp; &nbsp; }
&nbsp; &nbsp; } : window.console;</pre></code>

 <pre style="font-size: 30px"><code> <!-- .element: class="fragment" -->
console.log("Viva la Alert-based Debugging");
&nbsp;</pre></code> 
---
# JavaScript isn't awful <!-- .slide: class="center" -->
---
# JavaScript is awe-ful <!-- .slide: class="center" -->
Note: 
Full of Awe

It's amazing that we can take something so broken and made so much

The devil you know
---

> When that's the glue<br>of the modern day web, it's a minor miracle that society even functions<br> - <a href="https://twitter.com/NamTaf/status/590790154991702016">Adam Jones</a> <!-- .slide: class="center" -->
---
> ... JavaScript is no more weird or broken than any other scripting language<br> - <a href="https://twitter.com/seldo/status/728686963868344320">Laurie Voss, npm</a> <!-- .slide: class="center" -->
---
## Other languages have wats <!-- .slide: class="center" -->
---
# <pre>/usr/bin/irb</pre> <!-- .slide: class="center" -->
Note: Let's talk about ruby
---
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">irb> ruby bare words</code></pre></div>
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">NameError: undefined local<br>variable or method `words'</code></pre></div> <!-- .element: class="fragment" -->

 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">irb> def method_missing(@args)<br> &nbsp; &nbsp; &nbsp; args.join(" ")<br> &nbsp; &nbsp; end</code></pre></div> <!-- .element: class="fragment" -->
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">irb> ruby bare words</code></pre></div> <!-- .element: class="fragment" -->
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">"ruby bare words"</code></pre></div> <!-- .element: class="fragment" -->
<span class="dasfoot"><a href="https://www.destroyallsoftware.com/talks/wat">destroyallsoftware.com</a></span>
Note: Method Missing is evil monkey patching

This is how Rails used to work

find_customer_by_id substring
---
<pre><code><c># Customer.find&lowbar;all&lowbar;by&lowbar;last_name(last_name)</c>
def method&lowbar;missing(method&lowbar;id, &ast;arguments)
&nbsp; if match = /^<h>find&lowbar;</h>(<h>all&lowbar;by</h>|by)<h>&lowbar;</h>(<h>[&lowbar;a-zA-Z]\w*</h>)$/
&nbsp; &nbsp;&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; .match(method&lowbar;id.to&lowbar;s)
&nbsp; &nbsp; &nbsp; <c># ...</c>
&nbsp; &nbsp; &nbsp; self.class_eval %{
&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; def self.#{method_id}(*args)
&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; <c># ...</c>
&nbsp; &nbsp; &nbsp; }, __FILE__, __LINE__
&nbsp; 
&nbsp; &nbsp; &nbsp; send(method_id, *arguments)
&nbsp; 
&nbsp; elsif match = /^find_or_(initialize|create)_by_([_a-zA-Z]\w*)$/
&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; .match(method&lowbar;id.to&lowbar;s)
&nbsp; &nbsp; &nbsp; <c># ...</c>
&nbsp; &nbsp; &nbsp; send(method_id, *arguments)
&nbsp; else
&nbsp; &nbsp; &nbsp;super
&nbsp; end
end 
</code></pre> 

<span class="dasfoot"><a href="http://apidock.com/rails/v2.0.0/ActiveRecord/Base/method_missing/class">Rails 2.0.0 ActiveRecord/Base/method_missing</a></span>
---
# <pre>/usr/bin/irb</pre> <!-- .slide: class="center" -->
Note: Let's talk about ruby
---
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">irb> not true && false</code></pre></div>
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">false</code></pre></div> <!-- .element: class="fragment" -->

 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">irb> not true and false</code></pre></div> <!-- .element: class="fragment" -->
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">true</code></pre></div> <!-- .element: class="fragment" -->

<span class="dasfoot"><a href="http://whatthefuckruby.tumblr.com/post/70164947137">whatthef&#45;&#45;&#45;ruby.tumblr.com</a></span>
Note: order of presidence

&& ||
not 
and or
---

# <pre>/usr/local/bin/ghci</pre> <!-- .slide: class="center" -->
Note: Let's talk about Haskell
---

 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">λ&gt; length [1,2]</code></pre></div>
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">2</code></pre></div> <!-- .element: class="fragment" -->

 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">λ> length (1,2)</code></pre></div> <!-- .element: class="fragment" -->
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">1</code></pre></div> <!-- .element: class="fragment" -->

Note: because foldable, fMap fun
---
# <pre>/usr/local/bin/ghci</pre> <!-- .slide: class="center" -->
Note: Let's talk about Haskell
---
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">λ> let a = 2 + 2</code></pre></div>
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">λ> a</code></pre></div> <!-- .element: class="fragment" -->
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">4</code></pre></div> <!-- .element: class="fragment" -->

 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">λ> let b = 2 + 2 where 2 + 2 = 5</code></pre></div> <!-- .element: class="fragment" -->
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">λ> b</code></pre></div> <!-- .element: class="fragment" -->
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">5</code></pre></div> <!-- .element: class="fragment" -->
Note: Because haskell
---
# <pre>/usr/bin/local/pascal</pre> <!-- .slide: class="center" -->
Note: Let's talk about pascal
---

 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">Program boop(output);</code></pre></div>
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">VAR x: INTEGER;</code></pre></div>
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">begin</code></pre></div>
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">&nbsp; x := 41;</code></pre></div>
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">&nbsp; x += 1;</code></pre></div>
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">&nbsp; writeln(x = 42);</code></pre></div>
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">end.</code></pre></div>
<br> 
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">TRUE</code></pre></div> <!-- .element: class="fragment" -->



Note: that's all I wanted to point out

an assignment operator that doesn't look like equality; bliss
---

<p></p> 
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">Program boop(output);</code></pre></div>
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">VAR x: INTEGER;</code></pre></div>
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">begin</code></pre></div>
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">&nbsp; x <c>:=</c> 41; <c> // assignment</c></code></pre></div>
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">&nbsp; x += 1;</code></pre></div>
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">&nbsp; writeln(x <c>=</c> 42); <c> // equality </c></code></pre></div>
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">end.</code></pre></div>
<br> 
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">TRUE</code></pre></div>

Note: Let's talk about something completely different
---
# <pre>/bin/bash</pre> <!-- .slide: class="center" -->

Note: Let's talk about bash
---

 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">$ 4 + 2</code></pre></div>
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">bash: 4: command not found</code></pre></div> <!-- .element: class="fragment" -->
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">$ $(( 4 + 2 ))</code></pre></div> <!-- .element: class="fragment" -->
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">bash: 6: command not found</code></pre></div> <!-- .element: class="fragment" -->
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">$ echo $(( 4 + 2 ))</code></pre></div> <!-- .element: class="fragment" -->
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">6</code></pre></div> <!-- .element: class="fragment" -->

Note: let's do some simple arithmatic in bash

I'm just used to a repl that understands integers

shrug 
---

# <pre>/usr/local/bin/iex</pre> <!-- .slide: class="center" -->

Note: Let's talk about Elixir

---

 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">iex> Enum.map(1..5,<br>&nbsp; &nbsp; &nbsp; &nbsp; fn(x) -> x*x end )</code></pre></div>
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">[1, 4, 9, 16, 25]</code></pre></div> <!-- .element: class="fragment" -->

 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">iex> Enum.map(6..10,<br>&nbsp; &nbsp; &nbsp; &nbsp; fn(x) -> x*x end )</code></pre></div> <!-- .element: class="fragment" -->
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">'$1@Qd'</code></pre></div> <!-- .element: class="fragment" -->

<span class="dasfoot"><a href="http://www.cursingthedarkness.com/2015/10/the-definitive-all-dancing-all-complete.html">cursingthedarkness.com</a></span>
Note: 

Elixir is erlang

Strings in erlang are list of integers

and somewhow, elixir is inferring the second is string, not a list of numbers
---

# <pre>/usr/bin/cpp</pre> <!-- .slide: class="center" -->

Note: lets talk about c plus plus
---
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">> printf("wat??!")</code></pre></div>
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">wat|</code></pre></div> <!-- .element: class="fragment" -->
<br> 
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%"><h>// ??! → |<br>// ??< → {<br>// ??> → }<br>// ??= → #</h></code></pre></div> <!-- .element: class="fragment" -->
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%"><c>// "Trigraphs"<br>// ISO 646</c></code></pre></div> <!-- .element: class="fragment" -->


<span class="dasfoot"><a href="http://stackoverflow.com/questions/1234582/purpose-of-trigraph-sequences-in-c">Stack Overflow</a></span>

Note: disabled in gcc, works in c++11

Trigraphs - used as a work around for a lack of special symbols in ISO 646

ISO 646 nearly identical to ASCII
---
# <pre>/usr/local/bin python</pre> <!-- .slide: class="center" -->
Note: Let's talk about Python
---
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">>>> a = 256</code></pre></div>
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">>>> b = 256</code></pre></div> <!-- .element: class="fragment" -->
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">>>> a is b</code></pre></div> <!-- .element: class="fragment" -->
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">True</code></pre></div> <!-- .element: class="fragment" -->

<span class="dasfoot"><a href="www.youtube.com/watch?v=sH4XF6pKKmk">Investigating Python Wats</a></span>
---
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">>>> a = 257</code></pre></div>
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">>>> b = 257</code></pre></div> <!-- .element: class="fragment" -->
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">>>> a is b</code></pre></div> <!-- .element: class="fragment" -->
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">False</code></pre></div> <!-- .element: class="fragment" -->
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%"><br>>>> a = 257; b = 257</code></pre></div> <!-- .element: class="fragment" -->
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">>>> a is b</code></pre></div> <!-- .element: class="fragment" -->
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">True</code></pre></div> <!-- .element: class="fragment" -->

<span class="dasfoot"><a href="www.youtube.com/watch?v=sH4XF6pKKmk">Investigating Python Wats</a></span>
---

# <pre>#!/usr/bin/env java</pre> <!-- .slide: class="center" -->

Note: let's talk about java
---

 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">java> Integer a = 1024;</code></pre></div>
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">java> Integer b = 1024;</code></pre></div> <!-- .element: class="fragment" -->
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">java> a <= b</code></pre></div> <!-- .element: class="fragment" -->
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">true</code></pre></div> <!-- .element: class="fragment" -->
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">java> a >= b</code></pre></div> <!-- .element: class="fragment" -->
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">true</code></pre></div> <!-- .element: class="fragment" -->
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">java> a == b</code></pre></div> <!-- .element: class="fragment" -->
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">false</code></pre></div> <!-- .element: class="fragment" -->

<span class="dasfoot"><a href="http://stackoverflow.com/a/2001861/124019">Stack Overflow</a></span>

Note: integer caching. different objects.

Similar to python, but different.
---
# <pre>/usr/local/bin/scala</pre> <!-- .slide: class="center" -->
Note: Let's talk about scala
---

 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">scala> println({} + "")</code></pre></div>
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">()</code></pre></div> <!-- .element: class="fragment" -->
Note: unlike type concatenation issues, just like JavaScript

---
# <pre>/usr/bin/xcrun swift</pre> <!-- .slide: class="center" -->
Note: Let's talk about Swift
---
<pre><code>let cat_cafe = [
&nbsp;"cats": [
&nbsp; &nbsp;"01": ["nyan": "mew"],
&nbsp; &nbsp;"02": ["nyan": "mew"],
&nbsp; &nbsp;"03": ["nyan": "mew"],
&nbsp; &nbsp;"04": ["nyan": "mew"],
&nbsp; &nbsp;"05": ["nyan": "mew"],
&nbsp; &nbsp;"06": ["nyan": "mew"],
&nbsp; &nbsp;"07": ["nyan": "mew"],
&nbsp; &nbsp;"08": ["nyan": "mew"],
&nbsp; &nbsp;"09": ["nyan": "mew"],
&nbsp; &nbsp;"10": ["nyan": "mew"],
&nbsp; &nbsp;"11": ["nyan": "mew"],
&nbsp; &nbsp;"12": ["nyan": "mew"],
&nbsp; &nbsp;"13": ["nyan": "mew"],
&nbsp; &nbsp;"14": ["nyan": "mew"],
&nbsp; &nbsp;"15": ["nyan": "mew"]
&nbsp;] 
]</code></pre> 
 <pre style="margin-top: -20px;"><code>print("Cat count: " + String(cat_cafe["cats"]!.count))</code></pre> <!-- .element: class="fragment" -->
 <pre><code>$ time -p xcrun swift cats.swift</code></pre> <!-- .element: class="fragment" -->
 <pre style="margin-top: -20px;"><code>Cat count: 15</code></pre> <!-- .element: class="fragment" -->
 <pre style="margin-top: -20px;"><code>real 828.78</code></pre> <!-- .element: class="fragment" -->


<span class="dasfoot"><a href="https://bugs.swift.org/browse/SR-305">SR-305</a> <a href="https://spin.atomicobject.com/2016/04/26/swift-long-compile-time/">(atomicobject.com)</a></span>
Note: Swift

Wat isn't the strint dict int concat

Original version of this is 20 iterations, taking 20 - 55 *HOURS*

Dics of Dics of Dicts of strings compiler inefficency

Type inference issue

Fixed late April, in dev Snapshot May 9
just missed 2.2.1, may get into 2.2.2?
---
# <pre>/usr/bin/env perl -de1</pre> <!-- .slide: class="center" -->
Note: Let's talk about Perl

---

 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">> if ("foo" == "bar") {</code></pre></div>
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">> &nbsp; &nbsp; print "true"</code></pre></div>
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">> } else {</code></pre></div>
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">> &nbsp; &nbsp; print "false"</code></pre></div>
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">> }</code></pre></div>

 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">true</code></pre></div> <!-- .element: class="fragment" -->
<span class="dasfoot"><a href="http://stackoverflow.com/a/14046720/124019">Stack Overflow</a></span>
Note: Reason is `==` is for number comparing

eq is for string comparing

a new programmer won't know this.
---


# <pre>/usr/bin/php -a</pre> <!-- .slide: class="center" -->

Note: Let's talk about PHP
---
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">php> echo (TRUE ?<br>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; "True" : "False");</code></pre></div>
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">True</code></pre></div> <!-- .element: class="fragment" -->
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">php> echo (FALSE ?<br>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; "True" : "False");</code></pre></div> <!-- .element: class="fragment" -->
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">False</code></pre></div> <!-- .element: class="fragment" -->

<span class="dasfoot"><a href="http://phpsadness.com/sad/30">phpsadness.com</a></span>
Note: short hand for if else if else if
---

 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">php> echo (FALSE ? "one"<br>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;: FALSE ? "two" <br>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;: &nbsp; &nbsp; &nbsp; &nbsp; "three");</code></pre></div>
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">three</code></pre></div> <!-- .element: class="fragment" -->

<span class="dasfoot"><a href="http://phpsadness.com/sad/30">phpsadness.com</a></span>
---

 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">php> echo (FALSE ? "one"<br>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;: TRUE &nbsp;? "two" <br>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;: &nbsp; &nbsp; &nbsp; &nbsp; "three");</code></pre></div>
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">two</code></pre></div> <!-- .element: class="fragment" -->

<span class="dasfoot"><a href="http://phpsadness.com/sad/30">phpsadness.com</a></span>
---
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">php> echo (TRUE &nbsp;? "one"<br>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;: TRUE &nbsp;? "two" <br>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;: &nbsp; &nbsp; &nbsp; &nbsp; "three");</code></pre></div>
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">two</code></pre></div> <!-- .element: class="fragment" -->


<span class="dasfoot"><a href="http://phpsadness.com/sad/30">phpsadness.com</a></span>
Note: WRONG
---

# <pre>C:&bsol;> powershell</pre> <!-- .slide: class="center" -->

Note: Let's talk about powershell

---

 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">PS> if (2 > 1) { "true" }<br>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; else { "false" }</code></pre></div>
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">true</code></pre></div> <!-- .element: class="fragment" -->

 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">PS> if (2 < 1) { "true" }<br>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; else { "false" }</code></pre></div> <!-- .element: class="fragment" -->
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">The '<' operator is reserved<br>for future use.</code></pre></div> <!-- .element: class="fragment" -->

<span class="dasfoot"><a href="http://fuckpowershell.tumblr.com/">f&#45;&#45;&#45;powershell.tumblr.com</a></span>
---
# My point is... <!-- .slide: class="center" -->
---
# All languages<br>have quirks <!-- .slide: class="center" -->
Note: 
Yes some have more than others. Some have reasons why they can't be fixed

But that doesn't mean we have to critise those that use them

"We are not our tools. Discrimination based on tools is just as bad as discrimination based on race or gender" - Rachel Nabours

Hopefully I've shown just how good JS can be. And it might make someone reconsider before I see the next awful tirade on twitter
---

# &nbsp; <!-- .slide: class="center" -->
### glasnt.com/talks
---
# Resources
### &nbsp;
#### Check footnotes throughout the slide deck

### &nbsp;
### Online Interative Development Environments:
#### <a href="https://repl.it/">repl.it</a>
#### <a href="http://www.tutorialspoint.com/codingground.htm">TutorialsPoint.com</a>