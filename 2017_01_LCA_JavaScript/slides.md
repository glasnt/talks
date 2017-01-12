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

Note: Hi! Just a little bit of house keeping before we start
---
# Audience<br>Participation <!-- .slide: class="center" -->
Note: There will be a bunch of audience participation in this talk. If I ask a direct question, with my hand up, feel free to shout out an answer.

If my hand isn't up, please dont spoil it for people trying to work out the answer themselves

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


Note: 
There will be some smaller, less important, code in the presentation, like in the bottom section, but this isn't as important.

---
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">> input JavaScript code</code></pre></div>
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">output result</code></pre></div>
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">> input</code></pre></div>
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">output</code></pre></div>
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">> <c>// comments</c></code></pre></div>
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">> "Some <h>highlights</h>"</code></pre></div>
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">> <c>// Assume JavaScript unless</c></code></pre></div>
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">> <c>// otherwise advised</c></code></pre></div>


Note: For the code i'll be presenting, inputs will be prefixed with an input prompt, and output will appear underneath.

Comments will be prefixed with comment syntax

There will be other languages in this talk, but assume JavaScript unless otherwise specified.
---
# Let's get started! <!-- .slide: class="center" -->
---
# Hi! <!-- .slide: class="center" -->
Note: 

Hi! I'm Katie.

If you'll indulge me, I'm going to quote verbatium from my speaker profile

I've worn many hats over the years, but i'm currently a board member fo r Linux Australia[1], core develpoer on the beeware project, operations engineer at Ambiata, public speaker, and conference organiser.

When I"m not doing all those thing, I enjoy cooking, making tapestries and

---

# Global Variables <!-- .slide: class="center" -->
Note: 
Yelling at javascript and it's attempt at global variables.

When I was writing my speaker bio many years ago I was being vexxed by javascript, and it was frustrating.

Let me show you what i mean.
---
<p></p> 
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">> ans</code></pre></div>
Note: 
Say we have a variable, ans
---
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">> ans = "";</code></pre></div>
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">> function question() {<br>> &nbsp; var ans = 42;<br>> &nbsp; return ans;<br>> }</code></pre></div> <!-- .element: class="fragment" -->
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">> console.log(ans);</code></pre></div> <!-- .element: class="fragment" -->
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">""</code></pre></div> <!-- .element: class="fragment" -->
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">> console.log(question());</code></pre></div> <!-- .element: class="fragment" -->
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">42</code></pre></div> <!-- .element: class="fragment" -->
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">> console.log(ans);</code></pre></div> <!-- .element: class="fragment" -->
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">""</code></pre></div> <!-- .element: class="fragment" -->

Note: 
we inialise that variable with an empty string

we then create a funcion that sets the value of answer, and returns it

If we print out, using console.log, the value of ans, we get the epty strhing

if we then output the result of the function, we get 42

But then if we ask for the value of ans again, we get an empty string.

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

Note: If we were to change the scope of declaration of the variable inside the function, by removing `var`, we'd get what we expected, 42.

This exact bug has cost me many hours of my life.
---
# Duck Typing <!-- .slide: class="center" -->
Note: 

but you know what else is fun in JavaScript? Duck Typing

Duck typing is: if it looks like a duck, walks like a duck, and sounds like a duck, then it's a duck.
---
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">> 4 + 2</code></pre></div>
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">6</code></pre></div> <!-- .element: class="fragment" -->
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">> 4 - 2</code></pre></div> <!-- .element: class="fragment" -->
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">2</code></pre></div> <!-- .element: class="fragment" -->
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">> "4" - 2</code></pre></div> <!-- .element: class="fragment" -->
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">2</code></pre></div> <!-- .element: class="fragment" -->
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">> "4" + 2</code></pre></div> <!-- .element: class="fragment" -->
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">"42"</code></pre></div> <!-- .element: class="fragment" -->

Note: 
So: audience participation: what's 4 plus 2?

6 

What's 4 minus 2?

2 

What's the string 4 minus 2?

2 

And of course the string 4 plus 2 is

42 
---
# Equality <!-- .slide: class="center" -->

Note: You think that's fun? Try equality
---
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">> 0 ==&nbsp; false</code></pre></div>
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">true</code></pre></div> <!-- .element: class="fragment" -->
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">> 1 == &nbsp;"1"</code></pre></div> <!-- .element: class="fragment" -->
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">true</code></pre></div> <!-- .element: class="fragment" -->
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">> 0 === false</code></pre></div> <!-- .element: class="fragment" -->
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">false</code></pre></div> <!-- .element: class="fragment" -->
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">> 1 === "1"</code></pre></div> <!-- .element: class="fragment" -->
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">false</code></pre></div> <!-- .element: class="fragment" -->

Note: 



Is this statement true: 0 is equal to false

Yes! True!

What about the number 1? is it equal to the string 1?

True! 

Ah, but we were using double-equals

If we use triple-equals, neither of these things are equals
---
# Arrays and Objects <!-- .slide: class="center" -->
Note: 
And then there's arrays and objects
---
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">> [] + []</code></pre></div>
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">""</code></pre></div> <!-- .element: class="fragment" -->
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">> [] + {}</code></pre></div> <!-- .element: class="fragment" -->
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">[object Object]</code></pre></div> <!-- .element: class="fragment" -->
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">> {} + []</code></pre></div> <!-- .element: class="fragment" -->
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">0</code></pre></div> <!-- .element: class="fragment" -->
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">> {} + {}</code></pre></div> <!-- .element: class="fragment" -->
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">NaN</code></pre></div> <!-- .element: class="fragment" -->

Note: 


What's an empty array plus and empty array?

Yup! Empty string!

An empty array plus an object?

Object. Complete with this wonderful return syntax

What about the reverse, object plus an empty array

Zero! 

And an object plus an object?

It's not a number!
---

 <img src="pictures/wat.jpg" />
<span class="dasfoot"><a href="https://www.destroyallsoftware.com/talks/wat">destroyallsoftware.com</a></span>
Note: 


wat. 

Now, some of you might recognise the last example, and this duck, from Gary Brenhart's 'wat' talk; where he discusses some of the eccentrities of ruby and javascript.

this isn't a "wat" talk
---

 <img src="pictures/mini_wat.jpg" />

<span class="dasfoot"><a href="https://500px.com/photo/140476163/wat-by-edunham">wat, Emily Dunham, CC-BY-SA</a></span>
Note: 
this is 'hidden wat' talk. the sneaky edge cases and eccentries.

---
# Why? <!-- .slide: class="center" -->
Note: more importantly, we're going to discuss why. Why is the language like this?
---

# JavaScript® <!-- .slide: class="center" -->

<span class="bfoot" style="bottom: -280px"><a href="http://tsdr.uspto.gov/#caseNumber=75026640&caseType=SERIAL_NO&searchType=statusSearch">US Trademark &#35;75026640</a></foot>
Note: For starters, JavaScript is a registerd trademark of Oracle

... because it was originally a trademark of Netscape, which got bought by Sun, which then got bought by Oracle.

It also had an extremely fast development cycle of just ten days. ... with no versioning.

---

# ECMAScript <!-- .slide: class="center" -->
### A general purpose, cross-platform programming language

Note: the proper name for the lanague is ECMAScript. This was the working name used during the standardisation, but since there was never a nicer name chosen, we still use JavaScript or ECMAScript.

I'm going to be using the two interchangably.

---

# The most<br>popular language.<br>Ever. <!-- .slide: class="center" -->
Note: Regardless of what you call it, it's the most popular language ever. There are more users of javascript than of any other langauge, and more developers of it.

Since it has so many users, of course it's going to seem that there's more noise about it, both good and bad, than say a less popular language.
---
# wat <!-- .slide: class="center" -->

Note: Anyway, let's go back to those examples from earlier, and show why they are the way they are

---

# Global Variables <!-- .slide: class="center" -->
Note: starting with global variables
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

Note: 
The problem with our global variables example is scope
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

Note: The variable outside the function is implicitly global, whereas the variable inside is local.

this var keyword lessens the scope. The variable inside the function, unless properly declared, can effect the outer variables, which is what tripped me up years ago
---
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%"><c>//ruby</c></code></pre></div>
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%"><h>@</h>ans = 42;</code></pre></div>
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%"></code></pre></div>
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%"><c>//python</c></code></pre></div>
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%"><h>global</h> ans = 42;</code></pre></div>
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%"></code></pre></div>
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%"><c>//java</code></pre></div>
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%"><h>public</h> static ans = 42;</code></pre></div>
Note: especially since in every other language I've developed in, variables are local by default unless declared global by a keyword.
---
# Overloaded<br>`+` operand <!-- .slide: class="center" -->

Note: 
Our duck typing example is because of the overloaded plus operand

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

Note: In the first example, the code sone implicit conversion on the stirng '4' to make it a numeric before actioning, because subtracting from a string doesn't make sense.

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
Note: Using the plus symbol against a string isn't mathematical addition, but string addition, or appending, hence, 42

---

# Equality<br>and<br>Type Coersion <!-- .slide: class="center" -->

Note: we see more of this coersion in the equality example
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

Note: 

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

Note: 

the double equals automatically performs type co-ersion

the triple equals doesn't.

The 'issue' with double-equals was picked up very early on, but because the usage of double-equals was already locked in by the standard, the truple-equals was added

You should always use triple-equals
---
# `parseInt` <!-- .slide: class="center" -->
Note: There are other interesting quirks of javascript

Such as parseInt
---
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">> parseInt("42")</code></pre></div>
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">42</code></pre></div> <!-- .element: class="fragment" -->
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">> parseInt("42 Wallaby Way")</code></pre></div> <!-- .element: class="fragment" -->
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">42</code></pre></div> <!-- .element: class="fragment" -->
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">> parseInt("04")</code></pre></div> <!-- .element: class="fragment" -->
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">4</code></pre></div> <!-- .element: class="fragment" -->
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">> parseInt("08")</code></pre></div> <!-- .element: class="fragment" -->
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">0</code></pre></div> <!-- .element: class="fragment" -->

Note: 



if i wanted to parse the string '42' with parseint, what do you think the result should be?

the integer 42, right

but what about this string? error?

nope, it's 42 as well. The parser stops as soon as it sees a non-numeric charcater in the string. And yes, that includes if you use a comma for thousands.

What about the string "04"?

4 

But what about "08"?

0 
---
<p></p> 
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">> parseInt("42")</code></pre></div>
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">42</code></pre></div>
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">> parseInt("42 Wallaby Way")</code></pre></div>
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">42</code></pre></div>
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">> parseInt("04") <c>// octal</c></code></pre></div>
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">4</code></pre></div>
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">> parseInt("08") <c>// invalid</c></code></pre></div>
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">0</code></pre></div>

Note: 

That's because parseInt makes assumptions about the input

Any number starting with 0 is assumed to be octal, or base 8.

[this is mentioned as fixed later]
---
# `Number` <!-- .slide: class="center" -->
Note: 
Numbers in javacript are just run in general
---
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">> 4 + 2</code></pre></div>
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">6</code></pre></div> <!-- .element: class="fragment" -->
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">> 40 + 20</code></pre></div> <!-- .element: class="fragment" -->
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">60</code></pre></div> <!-- .element: class="fragment" -->
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">> 0.4 + 0.2</code></pre></div> <!-- .element: class="fragment" -->
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">0.6000000000000001</code></pre></div> <!-- .element: class="fragment" -->
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%"><c>// All Number in JavaScript<br>// are IEEE-754 floats</c></code></pre></div> <!-- .element: class="fragment" -->
Note: 
so, 4 plus 2

6 

what about 40 plus 20?

60, right!

but what baout 0.4 plus 0.2?

zero point six zero zero zero zero..... one.

Because all numbers in javascript are floats, and all the fun that comes long with that.
---
# Extended<br>Character Set <!-- .slide: class="center" -->
Note: but it's not just numbers, strings are also fun. More specifically, the extended character set.

---
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">> "abc".split("")</code></pre></div>
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">["a","b","c"]</code></pre></div> <!-- .element: class="fragment" -->
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">> "<img src="pictures/penguin.svg" class="e" style="margin: 0"><img src="pictures/koala.svg" style="margin: 0" class="e">".split("")</code></pre></div> <!-- .element: class="fragment" -->
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">["�","�","�","�"]</code></pre></div> <!-- .element: class="fragment" -->
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">> Array.from("<img src="pictures/penguin.svg" class="e" style="margin: 0"><img src="pictures/koala.svg" style="margin: 0" class="e">")</code></pre></div> <!-- .element: class="fragment" -->
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">["<img src="pictures/penguin.svg" class="e" style="margin: 0">","<img src="pictures/koala.svg" style="margin: 0" class="e">"]</code></pre></div> <!-- .element: class="fragment" -->

Note: 
So, if we want to split the string "abc" into indiviual characters

we get a, b, c

but what if we want to split the string of pengiun emoji, koala emoji

we get nonsense

this is because unicode was developing riht aroudn the time that javascript was, so some native string manipulations make assumptions about variable length encoding. so it doesn't inderstand how to handle characters that use longer encoding

The proper way to handle such character splitting is to use Array from.


---

# This thing <!-- .slide: class="center" -->
## `++[[]][+[]]+[+[]]` <!-- .slide: class="center" -->
Note: Speaking of arrays, this. this is fun.

---
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">> ++[[]][+[]]+[+[]]</code></pre></div>
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">10</code></pre></div> <!-- .element: class="fragment" -->
Note: 
anyone want to hazzard a guess what this evaluates to?

10 

Yes, 10

Let's step through this.

---
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">> []</code></pre></div>
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">""</code></pre></div> <!-- .element: class="fragment" -->
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">> +[] <c>&nbsp; // +""</c></code></pre></div> <!-- .element: class="fragment" -->
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">0</code></pre></div> <!-- .element: class="fragment" -->
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">> [[]] <c> // [""] </c></code></pre></div> <!-- .element: class="fragment" -->
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">""</code></pre></div> <!-- .element: class="fragment" -->
Note: an empty array, like we saw right at the beginning of this talk, is the equivelent of an empty string

if we use a unary addition to cast an array into an integer, because it's an empty string, we get 0

Also, the array of an empty array, or an array of empty string, is just string
---
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">> [[]][+[]] <c> &nbsp;// [""][0]</c></code></pre></div>
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">""</code></pre></div> <!-- .element: class="fragment" -->
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">> +[[]][+[]] <c> // +""</code></pre></div> <!-- .element: class="fragment" -->
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">0</code></pre></div> <!-- .element: class="fragment" -->
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">> ++[[]][+[]] <c>// ++0 </c></code></pre></div> <!-- .element: class="fragment" -->
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">1</code></pre></div> <!-- .element: class="fragment" -->
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">> ++[[]][+[]] <h>+</h> [+[]]</code></pre></div> <!-- .element: class="fragment" -->
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">10</code></pre></div> <!-- .element: class="fragment" -->

Note: 
but 

If we want to get the element at index 0 in an array of an empty string

we get an empty string

however 

that empty string can be cast to an integer

and that integer, can be incremented. so we get a one

so then if we string concatenate the one and the zero

we get 10

we can take this a step further.
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

Note: 
Using only left/right bracket, left-right parenthesis, exclaimation point and plus, we can write anything, and it's valid javascript.

This is valid javascript

It's the string lca2017
---
# `typeof` <!-- .slide: class="center" -->
Note: 
The underlying types of things in javascript is intersting.

By using typeof, we can query thing
---
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">> typeof { a: "b" }</code></pre></div>
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">"object"</code></pre></div> <!-- .element: class="fragment" -->
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">> typeof ["a","b"]</code></pre></div> <!-- .element: class="fragment" -->
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">"object"</code></pre></div> <!-- .element: class="fragment" -->

Note: 
for example: the type of this object

is object

but the type of this array

is object
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
Note: 

The underlying primatives can be tested for what kind of operand a thing is

For example:

Object() is... an object

Following this pattern, typeof Number is

a number

type of string is..

a string!

type of boolean is..

a boolean!

type of null is..

Object. 

[possible giggle here]

So. There is a very important reson for this. And it has to do with the underlying representation of these objects
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

Note: 

The tag prefixed to represent an object is 0, a string 4, and a boolean, 6

However, a null object uses the null pointer.

Which is the same as an object.

you can see where this is going..

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
Note: Here's the source code for typeof. This is C code, taken from JSAPI as it was in 1996

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

Note: it's a big if then else tree

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
Note: starting at the top, we check to see if the value is void

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

Note: 

if not, we check if it's an object

the check for object is to see if the tag on the variable is the same as the object type tag

In this case, a null pointer matches
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
Note: and since it doesn't match the validation for a function

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


Note: it hits the else
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

Note: and the type is an object

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
Note: which we then return out the bottom

yes this is a big.

this is a very old, known bug.
---

# Backwards<br>Compatibility <!-- .slide: class="center" -->

Note: 

the problem here is backwards compatibility

There are no versions of javascript

you write your code in a script tag, marked as type javascript, and it goes from there.

every browser has to implement the same standard

which means that the internet would break if javascript wasn't backwards compatible to day 0.
---

# JavaScript isn't awful <!-- .slide: class="center" -->
Note: Javascript isn't awful,

---
# JavaScript is awe-ful <!-- .slide: class="center" -->
Note: It's awe-ful, full of all.

There's a lot of issues with javascript, and a lot of weird edges around the place
---

# So don't use<br>JavaScript <!-- .slide: class="center" -->
Note: 

so don't use it

you can make a completely function website now days without any javascript at all

advancements in CSS and HTML mean you don't need to use a custom javascript workaround
---

### Image Sliders <!-- .slide: class="center" -->
### Modals
### Light Boxes
### Form Validation
### File Uploads
### ... all with HTML/CSS only.

<span class="bfoot" style="bottom: -100px"><a href="http://youmightnotneedjs.com/">You Might Not Need JavaScript.com</a></span>

Note: image sliders, modals, light boxes; all fancy UI things taht can now be implemented entirely in HTML/CSS

Also, form validation and file uploads!

Sample implementations for all of these are over at youmightnotneedjavascript.com
---

# HTML5 <!-- .slide: class="center" -->

Note: There have also been massive improvements to the web in general with HTML5

With HTML5 a lot of functionality has become native, so you don't need fancy frameworks.
---

### AppCache <!-- .slide: class="center" -->
### Events
### WebSockets
### Service Workers
### Web Storage
### ... all native with HTML5
<span class="bfoot" style="bottom: -100px"><a href="https://medium.com/@aliafshar/vanilla-is-the-best-flavour-c1765729a06a#.9z6s9ubgb">Vanilla is the best flavour, Ali Afshar</a></span>

Note: AppCache, Events, WebSockers, Service Workers, Web Storage

All these improvements to the HTML spec are making a fast improvement ot the web. And yes, some of these aren't available everywhere... yet.

---
# Using JavaScript<br>without JavaScript <!-- .slide: class="center" -->
Note: 

Another way is to use javascript, but dont use javascript

Unfortunately JS is the only language you can use in a browser (thank goodness, otherwise we would have kept ActiveX and Flash).

There are work arounds.
---
# Pick any language <!-- .slide: class="center" -->

<span class="bfoot" style="bottom: -280px"><a href="https://github.com/jashkenas/coffeescript/wiki/list-of-languages-that-compile-to-js">List of languages that compile to JS</a></span>

Note: 

pick any language

that language probably has a way to compile it's code down into javsacript

so you can program in your favourite language, then convert it into javascript, and run that on your browser
---

### Ruby: Opal, Red, .. <!-- .slide: class="center" -->
### PHP: Uniter, phype, .. <!-- .element: class="fragment" -->
### Perl: Perlito, p2js, .. <!-- .element: class="fragment" -->
### Go: GopherJS, .. <!-- .element: class="fragment" -->
### Python: Skulpt, Brython, .. <!-- .element: class="fragment" -->

Note: 
Like Ruby? Try Opal or Red

PHP? Uniter has you

Perl? you have a few choices

Go? You have at least one option in GopherJS

Python? There are a few choices, but I'd like to point out one specifically
---
# Batavia <!-- .slide: class="center" -->
 <img src="pictures/pybee.svg" />

Note: 

Batavia! Batavia does things just a little bit differently.

Batavia is an implementation of the python virtual machine, in javascript. It's part of the BeeWare suite of tools, and if you have a timemachine, or can wait for the recording, Russell Keith-Magee gave a talk on this just a few hours ago in the Wellington room.

But wait, that's not all. There are other languages that can compile down into JS
---
### Haskell: ghcjs, haste, .. <!-- .slide: class="center" -->
### Cobol: CobolScript <!-- .element: class="fragment" -->
### C: Emscripten <!-- .element: class="fragment" -->
Note: 
Haskell? there's ghcjs

Even Cobol has a project called CobolScript

And even C. Now, Emscripten is a wonderful thing. Because; you can convert C programs into javascript. Which means you get stuff like.
---
<video width="720" height="600" controls="controls"><source src="pictures/skifree.mp4" type="video/mp4" /></video>

<span class="bfoot" style="bottom: -20px"><a href="https://archive.org/details/win3_WINSKI">Internet Archive</a></span>
Note: 
This is the Internet Archive. It's wonderful. The amazing people there have been able to take a bunch of vintage software that doesn't run natively on hardware any more and move it up into an easy to access web platform

Here, i'm downloading the metadata and emulater, entirely in javascript

which then launches a dosbox emulator in JS

which then launches Windows 95, in javascript

that tiled background

And then launches the application i asked for, which is skifree.

This is all in javascript

This was achieved by compiling the original C into javascript.

I just think this is amazing.

And yes, due to the fact that clockspeeds are faster now than what they were in 1991, the yeti will always get you.
---

# But <!-- .slide: class="center" -->
---

# Using another language<br>doesn't save you <!-- .slide: class="center" -->

Note: yes, you *could* use another language, but a lot of these cross-compilers generate some knarly javascript.

But the languages themselves also have their own pitfalls.

---
# Other languages<br>have wats <!-- .slide: class="center" -->
Note: 
Other lanugages have 'wats'

Rapid fire time

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
Note: 
Ruby doesn't have the concept of bare words. If you just enter words

you get an error

but, if you declare a special method missing function, you can define what happens when your try and call a funtion that doesn't exist

And thus you can have barewords
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

Note: 
this is how Rails' ActiveRecord worked. Instead of declaring

find by all by last name

or 

find by all by post code

for every possible attribute of a record

this handles all that for you

it also makes debugging extra fun because the definition of your find all by last name method doesn't exist anywhere
---
# <pre>/usr/bin/irb</pre> <!-- .slide: class="center" -->
Note: Let's talk about ruby
---
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">irb> not true && false</code></pre></div>
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">false</code></pre></div> <!-- .element: class="fragment" -->

 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">irb> not true and false</code></pre></div> <!-- .element: class="fragment" -->
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">true</code></pre></div> <!-- .element: class="fragment" -->

<span class="dasfoot"><a href="http://whatthefuckruby.tumblr.com/post/70164947137">whatthef&#45;&#45;&#45;ruby.tumblr.com</a></span>
Note: 
in ruby, we have not and double and operators

so if we have not true double and false, what's the answer going to be?

false 

but, as well as double and we have the word and

so this should be the same, right?

no. 

this is because the order of presidence in ruby goes

double and and double pipe (for or)

not 

and then the words and and or

but i'm not just going to pick on ruby
---

# <pre>/usr/local/bin/ghci</pre> <!-- .slide: class="center" -->
Note: Let's talk about Haskell
---

 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">λ&gt; length [1,2]</code></pre></div>
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">2</code></pre></div> <!-- .element: class="fragment" -->

 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">λ> length (1,2)</code></pre></div> <!-- .element: class="fragment" -->
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">1</code></pre></div> <!-- .element: class="fragment" -->

Note: 
what's the length of the array 1, 2?

two 

what's the length of the of the tuple 1, 2?

1 

this is because of hte way that foldable works in haskell

it's.. complicated.
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
Note: 
in haskell, i can declare the variable a as being the some of 2 and 2

so what does a equal?

4 

but 

I can declare the variable b as being 2 + 2... where 2+2 is 5

which means that the value of b is

5 

this is completely valid haskell

:shrug: 

let's talk about something just slightly different
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



Note: 


In pascall, i can declare a program with a variable x, an integer

between the begin and the end, we manipulate x

what you do expect the output of this program to be?


True 

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

Note: 
because in the 4th line, we're assigning the value, and in the 6th, we're checking equality

which for me, coming from having learnt javascript as my first langauge, was reaally weird, you know, having an actual operand for assigning that's different from equality!

---
# <pre>/bin/bash</pre> <!-- .slide: class="center" -->

Note: Let's talk about bash
---

 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">$ 4 + 2</code></pre></div>
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">bash: 4: command not found</code></pre></div> <!-- .element: class="fragment" -->
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">$ $( 4 + 2 )</code></pre></div> <!-- .element: class="fragment" -->
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">bash: 4: command not found</code></pre></div> <!-- .element: class="fragment" -->
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">$ $(( 4 + 2 ))</code></pre></div> <!-- .element: class="fragment" -->
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">bash: 6: command not found</code></pre></div> <!-- .element: class="fragment" -->
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">$ echo $(( 4 + 2 ))</code></pre></div> <!-- .element: class="fragment" -->
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">6</code></pre></div> <!-- .element: class="fragment" -->

Note: 


let's do some simple arithmatic in bash

what's 4 plus 2?

error 

well, ok then

but about we wrap that around with a subshell, that should evaluate it?

No? 

huh, what about another wrapper

well, the error has our answer..

let's just echo it out

there you go

.. this one tripped me up for ages. yes, you can do arithmatic in bash, it's just... wordy..

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

In elixer, if i want to do a map of a square root like we had earlier, for the range 1 to 5

this works

but if i want to do the same, for say 6 to 10

i get weirdness

this is because somehow elixer is inferring the second as a string, not an range
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

Note: 

what happens if i try and print out this string?

I get get something.. interesting

this is because Cplusplus, specifically c++11 doesn't implement ascii, and the ppipe character doesn't exist

in order to be able to get these special characters, you preface with a double question mark.

these are known as trigraphs, and they are used as a work around in ISO646

---
# <pre>/usr/local/bin python</pre> <!-- .slide: class="center" -->
Note: Let's talk about Python
---
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">>>> a = 256</code></pre></div>
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">>>> b = 256</code></pre></div> <!-- .element: class="fragment" -->
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">>>> a is b</code></pre></div> <!-- .element: class="fragment" -->
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">True</code></pre></div> <!-- .element: class="fragment" -->

<span class="dasfoot"><a href="www.youtube.com/watch?v=sH4XF6pKKmk">Investigating Python Wats</a></span>
Note: 
we declare two varables

a and b, both 256

is a b?

yes 

---
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">>>> a = 257</code></pre></div>
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">>>> b = 257</code></pre></div> <!-- .element: class="fragment" -->
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">>>> a is b</code></pre></div> <!-- .element: class="fragment" -->
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">False</code></pre></div> <!-- .element: class="fragment" -->
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%"><br>>>> a = 257; b = 257</code></pre></div> <!-- .element: class="fragment" -->
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">>>> a is b</code></pre></div> <!-- .element: class="fragment" -->
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">True</code></pre></div> <!-- .element: class="fragment" -->

<span class="dasfoot"><a href="www.youtube.com/watch?v=sH4XF6pKKmk">Investigating Python Wats</a></span>
Note: 
what about if a is 257

and b is 257

is a b?

no 

but if we declare them on he same line

they are
---
# <pre>/usr/local/bin python</pre> <!-- .slide: class="center" -->
Note: Let's talk about Python
---
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">>>> x = bytearray(1)</code></pre></div>
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">>>> y = {}</code></pre></div> <!-- .element: class="fragment" -->
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">>>> x % y</code></pre></div> <!-- .element: class="fragment" -->
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">bytearray(b’’)</code></pre></div> <!-- .element: class="fragment" -->

<span class="bfoot"><a href="http://bugs.python.org/issue29073">Python Issue 29073</a></span>
Note: If we declare x as a byte array of size one

and y as an empty dict

what would a bytearary modulus a dict be?

a bytearray with an empty bytestring
---
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">>>> x = bytearray(1)</code></pre></div>
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">>>> y = {}</code></pre></div>
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">>>> x % y</code></pre></div>
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">bytearray(b’’) <c>&nbsp;&nbsp; &nbsp;# Python 3.5</c></code></pre></div>
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">bytearray(b’\x00’) <c># Python 3.6</c></code></pre></div> <!-- .element: class="fragment" -->
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">>>> x</code></pre></div> <!-- .element: class="fragment" -->
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">bytearray(b'\x00')</code></pre></div> <!-- .element: class="fragment" -->
<span class="bfoot"><a href="http://bugs.python.org/issue29073">Python Issue 29073</a></span>
Note: but this has changed in python 3.6 into the bytearray of a bytestring of a null byte, which is what x is originally

This is the kind of fun we get when we upgrade the python versions in BeeWare components. Because we are reimplementing things, we find all the edge cases.

Our CI makes all the pretty colours :)

Turns out that the Python 3.6 version is right, the Python 3.5 version is wrong, which has been backported and will be fixed in Python 3.5.3

Ah, the things you find when you iterate over every single permutation.
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

Note: 
if i declare an integer a of 1024

and declare b as the same value

then check if a is less than or grater to b

it's true

a is also greater than or equal to b?

yup! 

that means they must be equal, right?

Nope! 

This is due to integer caching, a similar issue to what python has
---
# <pre>/usr/local/bin/scala</pre> <!-- .slide: class="center" -->
Note: Let's talk about scala
---

 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">scala> println({} + "")</code></pre></div>
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">()</code></pre></div> <!-- .element: class="fragment" -->
Note: 
what's the result of this print statement?

... 

yeah, so this is because scala uses punctuation in a completely different way to javascript and other languages; the braces you're seeing is an empty function, and the concatenation of that to an empty string is an empty result

for anyone unfamiliar with the conventions of syntax in scala, like I was when i first started, this can throw you for six


---
# <pre>/usr/bin/xcrun swift</pre> <!-- .slide: class="center" -->
Note: 
let's talk about swift

Now, this one has been fixed, but i'll still mention it anyway
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
Note: 
If we have a large nested list of elements, all statically defined

and all we want to do is return the length of the inner list

we can, and it works

but it takes nearly 14 minutes to compile

This is because there was an issue with the optimiasation of complex objects in swift, which has been fixed.
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
Note: 

say I have this bit of perl code

compare foo and bar, and if they are equal, print true, else print false

so what's the result of this function? is foo equal to bar?

yes! 

wait, what?

this one is because the double-equals in perl is for numeric equality, not string equality; the strings are cast to numerics, and both evaluate to 0, and are thus equal!

---


# <pre>/usr/bin/php -a</pre> <!-- .slide: class="center" -->

Note: Let's talk about PHP
---
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">php> echo (TRUE ?<br>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; "True" : "False");</code></pre></div>
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">True</code></pre></div> <!-- .element: class="fragment" -->
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">php> echo (FALSE ?<br>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; "True" : "False");</code></pre></div> <!-- .element: class="fragment" -->
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">False</code></pre></div> <!-- .element: class="fragment" -->

<span class="dasfoot"><a href="http://phpsadness.com/sad/30">phpsadness.com</a></span>
Note: 

PHP has ternary operators. this means we can have something to execute if a statement is true, and one to execute if a statement is false

so in this example, TRUE is true, so we print

true 

and if we have FALSE, we print

false 

---

 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">php> echo (FALSE ? "one"<br>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;: FALSE ? "two" <br>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;: &nbsp; &nbsp; &nbsp; &nbsp; "three");</code></pre></div>
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">three</code></pre></div> <!-- .element: class="fragment" -->

<span class="dasfoot"><a href="http://phpsadness.com/sad/30">phpsadness.com</a></span>
Note: 
we can also chain these results

so for this example, we expect to fall from the first false to the second and then to the third

which is right
---

 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">php> echo (FALSE ? "one"<br>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;: TRUE &nbsp;? "two" <br>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;: &nbsp; &nbsp; &nbsp; &nbsp; "three");</code></pre></div>
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">two</code></pre></div> <!-- .element: class="fragment" -->

<span class="dasfoot"><a href="http://phpsadness.com/sad/30">phpsadness.com</a></span>
Note: 
but if we have a truth, we'd stop at two, right?

yes 
---
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">php> echo (TRUE &nbsp;? "one"<br>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;: TRUE &nbsp;? "two" <br>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;: &nbsp; &nbsp; &nbsp; &nbsp; "three");</code></pre></div>
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">two</code></pre></div> <!-- .element: class="fragment" -->


<span class="dasfoot"><a href="http://phpsadness.com/sad/30">phpsadness.com</a></span>
Note: 
and if we have a true at the first stage, we stop there, right?

no. 

this is because ternary operators in php are left-associative, different to every other ternary operator
---

# <pre>C:&bsol;> powershell</pre> <!-- .slide: class="center" -->

Note: Let's talk about powershell

---

 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">PS> if (2 > 1) { "true" }<br>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; else { "false" }</code></pre></div>
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">true</code></pre></div> <!-- .element: class="fragment" -->

 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">PS> if (2 < 1) { "true" }<br>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; else { "false" }</code></pre></div> <!-- .element: class="fragment" -->
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">The '<' operator is reserved<br>for future use.</code></pre></div> <!-- .element: class="fragment" -->

<span class="dasfoot"><a href="http://fuckpowershell.tumblr.com/">f&#45;&#45;&#45;powershell.tumblr.com</a></span>
Note: 
if we want to compare is two is bigger than 1, we could write something like this, returning a truth value to test the comparison

so is two bigger than one?

yes, true

what about the other way around? is two less than one

no, because the less than operator is reserved for future use
---
# ... yeah. <!-- .slide: class="center" -->
Note: yeah. I could keep going, but I think you get the idea.
---
# All languages<br>have quirks <!-- .slide: class="center" -->
Note: 

all languages have quirks

some are legitimate bugs in the langauge, some are only 'wats' because we don't know what's going on. And if you don't understand what the language is doing, they can bite you.
---
# JavaScript is<br>awe-ful <!-- .slide: class="center" -->

Note: and javascript is no exception.

However 
---

# JavaScript is<br>evolving <!-- .slide: class="center" -->
---
# JavaScript<br>outside the browser <!-- .slide: class="center" -->
Note: 

But javascript is no longer just for within the browser any more

server side javascript is now a thing

---
# node.js <!-- .slide: class="center" -->

Note: 

Thanks to node.js, which is a runtime environment that allows for serverside js

it's not a framework in itself
---
# V8<br>JavaScript Engine <!-- .slide: class="center" -->
Note: 
it runs on the v8 engine, which is also the engine that powers chromium

it's entirely open source

because it powers both client and serverside javascript, this is where the term "universal" or "isomorphic" javascript comes from

this makes it quite powerful

---
# V8 wat <!-- .slide: class="center" -->
Note: but it's not without it's wats
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

Note: 
Here's a snippet of javascript code

Just ignore the giant comment block

What we're doing is a really big loop. That's it.

It'll take just under 2 seconds to run on a server
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


Note: 
but let's try this again

remember that giant block comment
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

Note: what if we remove the last line

no other changes

it runs in under half the time.

This is because there is an optimization route in V8 that specifically applies to functions under 600 characters long. Including inline comments.

---
# Package<br>Management <!-- .slide: class="center" -->
Note: 
let's step out of security and talk about package management

This one needs some special attention, especially pertaining to javascript the language,
---

# <img src="pictures/npm.png"> <!-- .slide: class="center" -->

Note: 
node package manager, or npm, is not unlike rubygems or the cheeseshop; it's where javascript people can upload and share their packages.

if you're not familiar with them, you may have only heard about them via
---
# left-pad <!-- .slide: class="center" -->

Note: 

left-pad 

[wait for grumbles/giggles]

Now, i'm not bringing up left-pad as a cheap joke. I have a point.

For those that don't know the story, left-pad was removed from npm by it's author for reasons that I won't go into here. It was re-instated by npm because it was a dependency of a major package, which caused a bunch of downstream issues.

What is left-pad?
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

Note: 
an 11 line module that pads a string to the left.

and it handles most of what you'd expect of such a function

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

Note: 
it handles the case if you don't provide a character to pad, using space as the default

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

Note: 

it then works out how many characters you'll need to pad

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

Note: 

and prepends those characters until the length is right.

... 

this implementation is ok

let's take a look at how this might be implemented elsewhere.

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

Note: 
This is the PHP 5.6 standard library implementtaion of the same memethod, written in C, truncated for brevity.

It's got the same parts as the left-pad version

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

Note: 

The default value of space
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

Note: 
working out the length of the padding

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
Note: and
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

Note: 

Looping around until the string is at the right length

The thing is that this is a function within standard PHP.
---

# Work arounds <!-- .slide: class="center" -->
Note: 
left-pad is just one of countless thousands of work arounds that have been implemented due to a lack of unctionality in javascript

Javascript doesn't have a standard library. the functionality a python, ruby or php dev takes for granted isn't ther ein javascript

and so there have been may ways that this has been worked around over the years, including fundamental libraries like jquery

---
# JavaScript<br>is improving <!-- .slide: class="center" -->
Note: 
javascript is improving
---

# ECMAScript 3 <!-- .slide: class="center" -->
## 1999 <!-- .element: class="fragment" -->

<span class="bfoot" style="bottom: -260px"><a href="http://thenewstack.io/whats-new-es2016/">The New Stack</a></span>

Note: 

A lot of what I've been talking about so far has been functionality that's existed in javascript for many years. Most of it is declared in ECMAScript version 3, which dates back to 1999

1999 
---

# ECMAScript 4 <!-- .slide: class="center" -->
## 🏚 <!-- .slide: class="center" -->

Note: updates tried to happen in the form of ECMAScript 4, but for reasons this didn't happen, and it was abandoned.

Now, abandoning an entire version of a language to start again, skipping the number isn't unheard of.

PHP6 was abandoned, and what ever happened to Windows 9?


---
# ECMAScript 5 <!-- .slide: class="center" -->
## 2009, 2011 <!-- .slide: class="center" -->
Note: 

Anyway, it was another 10 years until a new version in the standard was created.

10 years between updates is a long time. between 1999 and 2009 a *LOT* happened on the web.

like, the entire dot com bubble and subsequent comeback.

But with ECMAScript 5, the base language of the web starts improving again.
---
# `isArray` <!-- .slide: class="center" -->
Note: 

For example, isArray!

There's now a native way to check if something is an array, which as we saw earlier, wasn't natively possible in a single call

---
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">ES5> Array.isArray({ a: "b" })</code></pre></div>
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">false</code></pre></div> <!-- .element: class="fragment" -->
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">ES5> Array.isArray(["a","b"])</code></pre></div> <!-- .element: class="fragment" -->
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">true</code></pre></div> <!-- .element: class="fragment" -->
Note: 

I'll be using the ECMAScript version prefixed to the input prompt to show the difference between versions

Now, if you use Array.isArray on an object, it's value

but on an array it's true!
---

# Improved<br>`parseInt` <!-- .slide: class="center" -->
Note: 
Also, there's improvements to existing functions like parseint


---
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">ES3> parseInt("08")</code></pre></div>
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">0</code></pre></div> <!-- .element: class="fragment" -->
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">ES<h>5</h>> parseInt("08")</code></pre></div> <!-- .element: class="fragment" -->
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">8</code></pre></div> <!-- .element: class="fragment" -->
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">ESx> parseInt("08", 10) <h>// radix</h></code></pre></div> <!-- .element: class="fragment" -->
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">8</code></pre></div> <!-- .element: class="fragment" -->
Note: 
Our original example when using parseInt in ECMAScript 3 returns a 0 in error

However, in ECMAScript 5, it works. This is because the default radix is now 10
---
# `map` <!-- .slide: class="center" -->
Note: 
We also get cool new things in ECMAScript 5 like map!
---

 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">ES5> [1, 2, 3].map(Math.sqrt)</code></pre></div>
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">[1, 4, 9]</code></pre></div> <!-- .element: class="fragment" -->
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%"><c>// [Math.sqrt(1)<br>&nbsp; , Math.sqrt(2)<br>&nbsp; , Math.sqrt(3)]</c></code></pre></div> <!-- .element: class="fragment" -->
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">ES5> a = ['10','10','10','10']</code></pre></div> <!-- .element: class="fragment" -->
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">ES5> a.map(parseInt)</code></pre></div> <!-- .element: class="fragment" -->
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">[10, NaN, 2, 3]</code></pre></div> <!-- .element: class="fragment" -->
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%"><h>// Be aware of optional<br>// parameters</h></code></pre></div> <!-- .element: class="fragment" -->
Note: 
For those unfamiliar, map allows you to operate on every element of an array at once, and returnt he result in an array

So for this array, we apply the Square root function over each element, and get the result

However, be careful of what function you're applying.

Remeber how parseInt has a radix?

Yeah, you get some interesting results if you try and apply a function in map that has optional parameters
---
# ECMAScript 6 <!-- .slide: class="center" -->
## 2015 <!-- .slide: class="center" -->
Note: 

we also have ECMASript 6, which was approved 18 months ago in June 2015, so is mostly adopted
---
# `let` <!-- .slide: class="center" -->
Note: 
With ECMAScript 6, we get some extremely nice features

like let

---
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%"><c>// life.js</c></code></pre></div>
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">function question() {<br> &nbsp; var ans = 42; <br> &nbsp; return ans;<br>}</code></pre></div>

Note: 

Before we had a functional which caused us issues because of the ans variable
---
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%"><c>// life.js</c></code></pre></div>
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">function question() {<br> &nbsp; <h>let</h> ans = 42; <br> &nbsp; return ans;<br>}</code></pre></div>

Note: 
now, we can have proper block scoping.


with let, the scope extends only to the block, and we get an error if we try and reclare that variable
---
# `import` <!-- .slide: class="center" -->
Note: 

we also have import, which i'm quite excited about
---
<p></p> 
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%"><c><!&dash;&dash;&dash; old importing --></c></code></pre></div>
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">&lt;html></code></pre></div>
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">&lt;script src="<h>life.js</h>">&lt;/script></code></pre></div>
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">&lt;script src="<h>stuff.js</h>">&lt;/script></code></pre></div>
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">...</code></pre></div>
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">&lt;/html></code></pre></div>
Note: 
You used to have to use script tags to pull in every specific javascript file you wanted to use on page.

---
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%"><c>// life.js</c></code></pre></div>
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%"><h>export</h> function question() {<br> &nbsp; let ans = 42; <br> &nbsp; return ans;<br>}</code></pre></div>
<br> 
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%"><c>// stuff.js</c> <br><h>import</h> { question } from './life'</code></pre></div> <!-- .element: class="fragment" -->
Note: 

But now, for a sufficiently declared exported function

you can import that from another file!

This one isn't quite available yet, but it's now in the candidate stage of the adoption process! Yay!

---

# ECMAScript 7 <!-- .slide: class="center" -->

## "ECMAScript 2016"

<span class="bfoot" style="bottom: -200px"><a href="http://thenewstack.io/whats-new-es2016/">JavaScript Standard Moves to Yearly Release Schedule</a></span>

Note: There's also ECMAScript 7, which while having only some minor features added, is the first annual release of ECMAScript, which is significant because

up until 2016 year the canonical javascript standard document was a "lovingly maintained" Word Document

---

# ECMAScript 8 <!-- .slide: class="center" -->
Note: And there's also a scheduled release for this year which may include such fancy things like decorators, but this is yet to be finalised.

---
# ECMAScript Adoption <!-- .slide: class="center" -->
## kangax.github.io/compat-table/ <!-- .slide: class="center" -->
Note: 

Now, the adoption of these new functions is subject to browsers implementing them
but there's a handy compatibility table for working that out!

Sadly import is only at the candidate stage, but it is being picked up by some of the engines!

If you don't want to look at a big table of adoptions details


---
 <img src="pictures/mariko.png" style="margin-top: -50px" />

<span class="bfoot" style="bottom: 40px"><a href="https://twitter.com/kosamari/status/819066613538373632">Browser Version Update Schedule</span>
Note: Mariko Kosaka has this wonderful drawing

You can see that the dev versions get the twitter activity, but most of the major browsers do update at least once or twice a year, so as long as you RUN YOUR UPDATES then you should get all the new shiny :)


---
# Extending<br>JavaScript <!-- .slide: class="center" -->
Note: However, there is a way of extending javascrpit anyway right now, without having to wait

---
# Polyfill <!-- .slide: class="center" -->
Note: 

by way of polyfills
---
## `padStart` polyfill <!-- .slide: class="center" -->
Note: for example, padStart, a polyfill for leftpad that could be in the ECMA standaard as soon as this year.

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

<span class="bfoot"><a href="https://github.com/tc39/proposal-string-pad-start-end">tc39/proposal-string-pad-start-end</a></span>
Note: 
What we do with a polyfill is go:

if the function doesn't already exist, in this case, an extension to the String primative, add the function

---
## `isArray` polyfill <!-- .slide: class="center" -->
Note: We could also do the same for isArray

---
### &nbsp; <!-- .slide: class="center" -->
<pre style="font-size: 30px"><code>if (!Array.isArray) {
&nbsp; Array.isArray = function(arg) {
&nbsp; &nbsp; return Object.prototype.toString.call(arg)
&nbsp; &nbsp; &nbsp; &nbsp; <h>=== '[object Array]';</h>
&nbsp;}; 
} 
</pre></code> 
Note: 
Which uses the same format, and just returns a truthy value based on matching the output of toString on the object
---
# "Polyfills can<br>create problems" <!-- .slide: class="center" -->

<span class="bfoot" style="bottom: -200px"><a href="https://w3ctag.github.io/polyfills/">Polyfills are part of the web - TAG finding</span>

Note: However, a draft document from the w3c technical architecture group states that while polyfills are a part of the web, they can create problems for standardisation efforts

This includes a bunch of recommendations for developers, which include serving only the polyfills your users need, and considering how to serve all users of your website, including those using slower, less capable devices
---
# JavaScript isn't<br>awful <!-- .slide: class="center" -->
Note: 
So, hopefully I've shown that javascript isn't awful

---
# JavaScript is<br>awe-ful <!-- .slide: class="center" -->
Note: 

it's awe-ful, full of aw

even with all it's edgecases, it's the devil you can't avoid.

you have no alternative in the browser.
---

> "We are not our tools.<br>Discrimination based on tools is just as bad as discrimination based on race or gender"<br>- <a href="https://twitter.com/glasnt/status/613963672046583808">Rachel Nabours</a> <!-- .slide: class="center" -->

Note: 
"We are not our tools. Discrimination based on tools is just as bad as discrimination based on race or gender" - Rachel Nabours
---
<br> 
<br> 
<br> 
<br> 
<img src="pictures/claps.svg" height="100px">

#### glasnt.com/talks

Note: thank you for your time.