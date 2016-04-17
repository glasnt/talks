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
# JavaScript is Awe-ful <!-- .element: style="margin-bottom: 1em" -->
<br> 
 <img src="pictures/footer.svg" />
---

 <img src="pictures/javascript_book.png" style="margin-top: -50px" />
Note: Good parts written by Douglas Crockford
---

# Hi! <!-- .slide: class="center" -->
Note: Tapestry and Cooking and Yelling
---

# Global Variables <!-- .slide: class="center" -->
---
<p></p> 
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">> ans</code></pre></div>
---
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">> ans = "";</code></pre></div>
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">> function question() {<br>> &nbsp; var ans = 42;<br>> &nbsp; return ans;<br>> }</code></pre></div> <!-- .element: class="fragment" -->
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">> console.log(ans);</code></pre></div> <!-- .element: class="fragment" -->
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">""</code></pre></div> <!-- .element: class="fragment" -->
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">> console.log(question());</code></pre></div> <!-- .element: class="fragment" -->
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">42</code></pre></div> <!-- .element: class="fragment" -->
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">> console.log(ans);</code></pre></div> <!-- .element: class="fragment" -->
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">""</code></pre></div> <!-- .element: class="fragment" -->
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
---
# Duck Typing <!-- .slide: class="center" -->
Note: if it looks like a duck and sounds like a duck, it's a duck.
---
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">> 4 + 2</code></pre></div>
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">6</code></pre></div> <!-- .element: class="fragment" -->
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">> 4 - 2</code></pre></div> <!-- .element: class="fragment" -->
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">2</code></pre></div> <!-- .element: class="fragment" -->
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">> "4" - 2</code></pre></div> <!-- .element: class="fragment" -->
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">2</code></pre></div> <!-- .element: class="fragment" -->
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">> "4" + 2</code></pre></div> <!-- .element: class="fragment" -->
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">"42"</code></pre></div> <!-- .element: class="fragment" -->
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

Note: Associativity? Pfft! Transativity? Hahahah
---

# Arrays != Objects <!-- .slide: class="center" -->
---
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">> var arr = ['a', 'b', 'c']</code></pre></div>
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">> arr</code></pre></div> <!-- .element: class="fragment" -->
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">["a", "b", "c"]</code></pre></div> <!-- .element: class="fragment" -->
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">> arr.hello = "world"</code></pre></div> <!-- .element: class="fragment" -->
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">"world"</code></pre></div> <!-- .element: class="fragment" -->
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">> arr</code></pre></div> <!-- .element: class="fragment" -->
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">["a", "b", "c"]</code></pre></div> <!-- .element: class="fragment" -->
---
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">> for (var k in arr) {<br>>&nbsp;&nbsp; console.log(k);<br>> }</code></pre></div>
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">0<br>1<br>2<br>hello</code></pre></div> <!-- .element: class="fragment" -->
---
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">> arr.push("append");</code></pre></div>
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">4</code></pre></div> <!-- .element: class="fragment" -->
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">> c = 0;<br>> for (var k in arr) {<br>>&nbsp; &nbsp; c = c + 1; <br>> }<br>> c</code></pre></div> <!-- .element: class="fragment" -->
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">5</code></pre></div> <!-- .element: class="fragment" -->
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">> arr.length</code></pre></div> <!-- .element: class="fragment" -->
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">4</code></pre></div> <!-- .element: class="fragment" -->
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
# Developers can get<br>just a little bit<br>upset at JavaScript <!-- .slide: class="center" -->
---
> "[A]: Please don't hire me<br>for my JS abilities.<br>I'm proficient enough to loath the language intensely" <!-- .slide: class="center" -->
Note: experienced developers get frustrated with it
---

> "[B]: I have been around [A]<br>when they hack JS.<br>Let's just say<br>Satan himself would blush." <!-- .slide: class="center" -->
Note: people near to javascript developers hear them swear. A lot.
---

> "[C]: Have to modify some JavaScript<br>I did over a year ago. <!-- .slide: class="center" -->
> 
> 'What is this?'<br>
> 'Why did I ...?'<br>
> 'What sort of name is that!'"

Note: confusing syntax, hard to come back to

---

> "[D]: 'I hate writing JavaScript.<br> <!-- .slide: class="center" -->
> I know, I'll write some JavaScript<br>to fix it.'
> 
> This is how Angular happens."

Note: Pot shots at the Language
---
# ... <!-- .slide: class="center" -->
---
# Why? <!-- .slide: class="center" -->
Note: why is javascript so awful
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

<span class="dasfoot"><a href="http://tsdr.uspto.gov/#caseNumber=75026640&caseType=SERIAL_NO&searchType=statusSearch">US Trademark &#35;75026640</a></span>
Note: 

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


---
# Billions of users <!-- .slide: class="center" -->

Note: What percentage of the internet uses JS?

---
# Millions of developers <!-- .slide: class="center" -->
Note: Given this user base, there are more developers of JS than any other language
---
# Butt-loads of complaints <!-- .slide: class="center" -->

Note: It may also be the most complained about language
But not without some reason

---
# Foot Guns <!-- .slide: class="center" -->

Note: Things you can shoot yourself with in the foot

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
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">2 <c>&nbsp;&nbsp; // type -> integer</c></code></pre></div>
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">> "4" + 2</code></pre></div>
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">"42"<c> // type -> string</c></code></pre></div>
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
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">> parseInt("123")</code></pre></div>
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">123</code></pre></div> <!-- .element: class="fragment" -->
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">> parseInt("123 bunnies")</code></pre></div> <!-- .element: class="fragment" -->
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">123</code></pre></div> <!-- .element: class="fragment" -->
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">> parseInt("04")</code></pre></div> <!-- .element: class="fragment" -->
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">4</code></pre></div> <!-- .element: class="fragment" -->
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">> parseInt("08")</code></pre></div> <!-- .element: class="fragment" -->
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">0</code></pre></div> <!-- .element: class="fragment" -->
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
# Extended Character Set <!-- .slide: class="center" -->
---
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">> "abc".split("")</code></pre></div>
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">["a","b","c"]</code></pre></div> <!-- .element: class="fragment" -->
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">> "<img src="pictures/rabbit.svg" class="e" style="margin: 0"><img src="pictures/cat.svg" style="margin: 0" class="e">".split("")</code></pre></div> <!-- .element: class="fragment" -->
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">["�","�","�","�"]</code></pre></div> <!-- .element: class="fragment" -->
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">> Array.from("<img src="pictures/rabbit.svg" class="e" style="margin: 0"><img src="pictures/cat.svg" style="margin: 0" class="e">")</code></pre></div> <!-- .element: class="fragment" -->
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">["<img src="pictures/rabbit.svg" class="e" style="margin: 0">","<img src="pictures/cat.svg" style="margin: 0" class="e">"]</code></pre></div> <!-- .element: class="fragment" -->

Note: Unicode extended characterset

Javascript was created before unicode was super popular, so some parts don't understand extended characters

split doesn't but array.from does (polyfill?)
---

# This thing <!-- .slide: class="center" -->
## `++[[]][+[]]+[+[]]` <!-- .slide: class="center" -->

---
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">> ++[[]][+[]]+[+[]]</code></pre></div>
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">10</code></pre></div> <!-- .element: class="fragment" -->
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">> []</code></pre></div> <!-- .element: class="fragment" -->
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">""</code></pre></div> <!-- .element: class="fragment" -->
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">> +[] <c>// +""</c></code></pre></div> <!-- .element: class="fragment" -->
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">0</code></pre></div> <!-- .element: class="fragment" -->
Note: uniary operand casts to number
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

# Arrays are Objects <!-- .slide: class="center" -->
## Kinda. <!-- .element: class="fragment" -->

Note: they are special, with integer keys and special sugar.
See eariler partial working of addressing array keys
---

 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">> typeof { a: "b"}</code></pre></div>
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
&nbsp; &nbsp; if (<h>JSVAL_IS_VOID(v)</h>) { <h>// v == JSVAL_VOID</h>
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
&nbsp; &nbsp; } else if (<h>JSVAL_IS_OBJECT(v)</h>) { <h>// JSVAL_TAG(v) == JSVAL_OBJECT</h>
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
&nbsp; &nbsp; &nbsp; &nbsp; if (...) { <h>// Excuse me, are you a function?</h>
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

Note: JS = most popular language

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

# Cross Site Scripting <!-- .slide: class="center" -->
# XSS <!-- .slide: class="center" -->

Note: Javascript can be used for other evil things

Can take data from your site onto others and other such fun:
---

# `eval` <!-- .slide: class="center" -->

Note: executing arbitary code.

We can create not easily readable code

If you were in Ben's Virus talk, this is havoc in PHP. JS no different
---
<br><br> 
<pre><code style="overflow: hidden; width: 100%; white-space: pre-wrap"><h>eval(</h>function(p,a,c,k,e,d){e&equals;function(c){return c.toString(36)};if(!''.replace(/^/,String)){while(c--){d[c.toString(a)]&equals;k[c]||c.toString(a)}k&equals;[function(e){return
d[e]}];e&equals;function(){return'\\\\w+'};c&equals;1};while(c--){if(k[c]){p&equals;p.replace(new RegExp('\\\\b'+e(c)+'\\\\b','g'),k[c])}}return p}('f a&equals;["\\\\e\\\\1\\\\7\\\\4\\\\2\\\\3\\\\1\\\\2\\\\3\\\\6\\\\4\\\\2\\\\d\\\\8\\\\c\\\\9\\\\2\\\\3\\\\6\\\\4\\\\2" +"\\\\g\\\\h\\\\8\\\\k\\\\4\\\\3\\\\2\\\\b\\\\1\\\\5\\\\9\\\\l\\\\6\\\\1\\\\i\\\\2\\\\3\\\\1\\\\7\\\\1\\\\5" +"\\\\5\\\\1\\\\b"];j(a[0]);',22,22,'|x6F|x20|x74|x65|x72|x68|x6D|x61|x6B|'<br>+'_0|x77|x63|x48|x43|var|x50|x6C|x70|alert|x6E|x73'.split('|'),0,{})<h>)</h>
</pre></code> 

 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">alert("Come to the <br> &nbsp; &nbsp; &nbsp; Hack the Planet workshop<br> &nbsp; &nbsp; &nbsp; tomorrow")</code></pre></code></pre></div> <!-- .element: class="fragment" -->
Note: base64_encode in php is similar
---
# ... <!-- .slide: class="center" -->
Note: so, that's what javascript can do. it's powerful, and scary. what if you say

---
## (╯°□°）╯︵ sʇɐʍ ʎɔɐƃǝl <!-- .slide: class="center" -->
Note: I dont want to deal with all that stuff
---

# Frameworks <!-- .slide: class="center" -->
Note: pre rolled goodness and wrappers and and and
---

# MooTools <!-- .slide: class="center" -->
# jQuery <!-- .slide: class="center" -->
# Bootstrap <!-- .slide: class="center" -->
Note: MooTools was a really good thing back in the day

I've only come across it when I tasked to remove it

... 

JQuery so much extension


at one point ~90% of websites had it

... 
more than JS; CSS, HTML
Adding more functionality so you dont have to worry about responsive websites

But you can spot a bootstraped wbesite from a mile away
---
# Meteor <!-- .slide: class="center" -->
# React <!-- .slide: class="center" -->
# Angular <!-- .slide: class="center" -->
---
# ... <!-- .slide: class="center" -->
Note: but what if you sasy
---
## (╯°□°）╯︵ ʇdᴉɹɔsɐʌɐɾ <!-- .slide: class="center" -->
Note: stuff javascript all together
---

# CoffeeScript <!-- .slide: class="center" -->
# TypeScript <!-- .slide: class="center" -->
# PureScript <!-- .slide: class="center" -->
Note: CoffeeScript is a little language that compiles into JavaScript. Underneath that awkward Java-esque patina, JavaScript has always had a gorgeous heart.

TypeScript lets you write JavaScript the way you really want to. TypeScript is a typed superset of JavaScript that compiles to plain JavaScript

See Typehints in JS talk from PyCon AU 2015
---
# ... <!-- .slide: class="center" -->
---
## (╯°□°）╯︵ ƃuᴉuɹɐǝl <!-- .slide: class="center" -->
Note: I want to work in my favourite language, and still work in the browser
---
## Pick a language. <!-- .slide: class="center" -->
## Any language. <!-- .slide: class="center" -->

---
### github.com/jashkenas/coffeescript/wiki/<br>List-of-languages-that-compile-to-JS <!-- .slide: class="center" -->
Note: Haskell - GHCJS
Python - pyjamas
Ruby - Opal

Listings for perl, erlang, java, scala, c#, f#, lisp, smalltalk, pascal, go, php, sql
---
# Some of my favourites <!-- .slide: class="center" -->
---
# Batavia <!-- .slide: class="center" -->
 <img src="pictures/pybee.svg" />
Note: Python Bytecode being run by the Jacascript VM
---
# asm.js <!-- .slide: class="center" -->
# emscripten <!-- .slide: class="center" -->
Note: C into JS

Faster than Light Osmos - Humble Bundle Mozilla

Unreal Tornament

DosBox 
---
 <img src="pictures/win95.png"> <!-- .slide: class="center" -->
Note: Yes, that's windows 95 running in my browser from 1995
---
# ... <!-- .slide: class="center" -->
---
## ┬javascript┬ ノ( ゜-゜ノ) <!-- .slide: class="center" -->
Note: OK, JS is pretty freaking neat, I want some of that.
But what about it's other uses

---
# JavaScript<br>outside the browser <!-- .slide: class="center" -->
---
# node.js <!-- .slide: class="center" -->
Note: serverside js

---
# Electron <!-- .slide: class="center" -->
Note: 

GitHub's framework. Atom. Github Desktop
not the first time JS has been used on the desktop
---
# Google Gadgets <!-- .slide: class="center" -->
Note: iGoogle and Google Desktop widget - scripting by javascript on the desktop
---
 <img src="pictures/google_gadgets.jpg" />
---
<br><br> 
 <img src="pictures/igoogle.png" />
---
# As a scripting language <!-- .slide: class="center" -->
Note: NginScript, Cinnamon
---

# More Gotchas <!-- .slide: class="center" -->
---

# V8 Function<br>Optimisation <!-- .slide: class="center" -->
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

for(let i = 0; i < 500000000; i++) {
&nbsp; if (add(i, i++) < 5) {
&nbsp; &nbsp; <c>//</c>
&nbsp; }
} 
</code></pre> 

 <pre><code>$ time -p node general.js<br>real 1.91</code></pre> <!-- .element: class="fragment" -->
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

for(let i = 0; i < 500000000; i++) {
&nbsp; if (add(i, i++) < 5) {
&nbsp; &nbsp; <c>//</c>
&nbsp; }
} 
</code></pre> 

Note: blank for flicking

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
&nbsp; //
</c> 
&nbsp; return(x + y);
} 

for(let i = 0; i < 500000000; i++) {
&nbsp; if (add(i, i++) < 5) {
&nbsp; &nbsp; <c>//</c>
&nbsp; }
} 
</code></pre> 

 <pre><code>$ time -p node general.js<br>real 0.77</code></pre> <!-- .element: class="fragment" -->
Note: What's going to happen? any change?

More than twice as fast
---
# JavaScript<br>is improving <!-- .slide: class="center" -->
---

# ECMAScript 5 <!-- .slide: class="center" -->
Note: std intro'd in 2009

Mostly adpoted
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
# `isArray` <!-- .slide: class="center" -->
---
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">> Array.isArray({ a: "b" })</code></pre></div>
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">false</code></pre></div> <!-- .element: class="fragment" -->
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">> Array.isArray(["a","b"])</code></pre></div> <!-- .element: class="fragment" -->
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">true</code></pre></div> <!-- .element: class="fragment" -->
---
# `trim` <!-- .slide: class="center" -->

Note: JS didn't ahve a trim command til ES5
it had a `trimLeft` and a `trimRight`

---

 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">> " Hello ".trimLeft()</code></pre></div>
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">"Hello "</code></pre></div> <!-- .element: class="fragment" -->
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">> " Hello ".trimRight()</code></pre></div> <!-- .element: class="fragment" -->
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">" Hello"</code></pre></div> <!-- .element: class="fragment" -->
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">ES<h>5</h>> " Hello ".trim()</code></pre></div> <!-- .element: class="fragment" -->
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">"Hello"</code></pre></div> <!-- .element: class="fragment" -->
---
# ECMAScript 6 <!-- .slide: class="center" -->
Note: approved in June 2015 (a few months ago)

Still very much not adpoted.
---
# `let` <!-- .slide: class="center" -->
---

 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">> ans = "";</code></pre></div>
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">> function quest() {<br>> &nbsp; var ans = 42; <br>> &nbsp; return ans;<br>> }</code></pre></div>
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">> quest()</code></pre></div>
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">> console.log(ans);</code></pre></div>
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">> ""</code></pre></div>
---
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">> ans = "";</code></pre></div>
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">> function quest() {<br>> &nbsp; <h>let</h> ans = 42; <br>> &nbsp; return ans;<br>> }</code></pre></div>
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">> quest()</code></pre></div>
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">> console.log(ans);</code></pre></div>
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">> ""</code></pre></div>

Note: proper block scope
Re-declarations are in error
---
# `import` <!-- .slide: class="center" -->
---
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%"><c>// life.js</c></code></pre></div>
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%"><h>export</h> function quest() {</code></pre></div>
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%"><c> /&ast; ... &ast;/</c></code></pre></div>
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">}</code></pre></div>
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%"><c>// script.js</c> <br><h>import</h> { quest } from './life';</code></pre></div> <!-- .element: class="fragment" -->
---
# Spread <!-- .slide: class="center" -->
---
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">function add(<h>...</h>vals) {</code></pre></div>
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">&nbsp; let sum = 0;</code></pre></div>
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">&nbsp; for (var v of vals) {</code></pre></div>
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">&nbsp; &nbsp; &nbsp; sum += v;</code></pre></div>
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">&nbsp; }</code></pre></div>
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">&nbsp; return sum;</code></pre></div>
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">}</code></pre></div>
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%"><br>> add(10, 14, 9, 7, 2)</code></pre></div> <!-- .element: class="fragment" -->
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">42</code></pre></div> <!-- .element: class="fragment" -->

---
# ECMAScript 5/6 Adpotion <!-- .slide: class="center" -->
---
## kangax.github.io/compat-table/es5/ <!-- .slide: class="center" -->
## kangax.github.io/compat-table/es6/ <!-- .slide: class="center" -->
---
# Non-standard 'Standards' <!-- .slide: class="center" -->
---
# `console.log` <!-- .slide: class="center" -->
Note: Not actually a standard :D
---
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">> a = 42</code></pre></div>
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">> console.log("a is: " + a);</code></pre></div> <!-- .element: class="fragment" -->
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">"a is 42"</code></pre></div> <!-- .element: class="fragment" -->
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">> console.time("Process")</code></pre></div> <!-- .element: class="fragment" -->
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">> <c>// ... do the thing</c></code></pre></div> <!-- .element: class="fragment" -->
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">> console.timeEnd("Process")</code></pre></div> <!-- .element: class="fragment" -->
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">"Process: 1337ms"</code></pre></div> <!-- .element: class="fragment" -->
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">> console.log("%cHello world!",<br>&nbsp;"color: red; font-size: 40px");</code></pre></div> <!-- .element: class="fragment" -->
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%"><span style="color: red; font-size: 70px">Hello world!</span></code></pre></div> <!-- .element: class="fragment" -->
Note: try autocompleting for more, including grouping
---
<br><br> 
 <img src="pictures/facebook.png" />
Note: from console on facebook
---
# Extending JavaScript <!-- .slide: class="center" -->
---
# Polyfill <!-- .slide: class="center" -->
Note: Adding new funcionality in JS to JS by adding more JS
---
# `supplant` <!-- .slide: class="center" -->
Note: allows for native templating
---
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">> s = "{greet} there {name}!"</code></pre></div>
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">> t = { greet: "Oh hello",<br>&nbsp; &nbsp; &nbsp; &nbsp; name: &nbsp;"Katie" }</code></pre></div> <!-- .element: class="fragment" -->
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">> s.supplant(t)</code></pre></div> <!-- .element: class="fragment" -->
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">"Oh, hello there Katie!"</code></pre></div> <!-- .element: class="fragment" -->
Note: Supplant didn't get into ES6. But you can still polyfill it
---

## `supplant` polyfill <!-- .slide: class="center" -->
 <pre><code> <!-- .element: class="fragment" -->
if (!String.prototype.supplant) {
&nbsp; String.prototype.supplant = function (o) {
&nbsp; &nbsp; return this.replace(<h>/\{([^{}]*)\}/</h>g,
&nbsp; &nbsp; &nbsp; function (a, b) {
&nbsp; &nbsp; &nbsp; &nbsp; var r = o[b];
&nbsp; &nbsp; &nbsp; &nbsp; return typeof r === 'string' ||
&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;typeof r === 'number' ? r : a;
&nbsp; &nbsp; &nbsp; }
&nbsp; &nbsp; );
&nbsp; };
} 
</code></pre> 
Note: Create function if it doesn't exist

Doesn't handle multiple-level definitions

Didn't make it into es6, but totes useful
---
## `isArray` polyfill <!-- .slide: class="center" -->

 <pre><code> <!-- .element: class="fragment" -->
if (!Array.isArray) {
&nbsp; Array.isArray = function(arg) {
&nbsp; &nbsp; return Object.prototype.toString.call(arg) === '[object Array]';
&nbsp;}; 
} 
</pre></code> 
Note: Can also polyfil things that may not exist in your browser. but specifically only define it if it's not already defined
---
## `console.log` polyfill <!-- .slide: class="center" -->
 <pre><code> <!-- .element: class="fragment" -->
window.console =
&nbsp; &nbsp; typeof window.console === 'undefined' ? {
&nbsp; &nbsp; &nbsp; &nbsp; log: function(str) {
&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; alert(str)
&nbsp; &nbsp; &nbsp; &nbsp; }
&nbsp; &nbsp; } : window.console;
&nbsp;</pre></code> 
 <pre><code> <!-- .element: class="fragment" -->
console.log("oh goodness.");
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
> When that's the glue<br>of the modern day web,<br>it's a minor miracle<br>that society even functions <!-- .slide: class="center" -->
---
## Just keep in mind... <!-- .slide: class="center" -->
---
## Other languages have wats <!-- .slide: class="center" -->
---

# <pre>#!/usr/bin/env java</pre> <!-- .slide: class="center" -->

Note: Let's about about Java

---
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%"><c>/&#42;&#42; read from a file &#42;&#42;/</c></code></pre></div>
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">filename = "myfile.txt"</code></pre></div> <!-- .element: class="fragment" -->
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">BufferedReader reader = <br>&nbsp; &nbsp; &nbsp; new BufferedReader( <br>&nbsp; &nbsp; &nbsp; &nbsp; new InputStreamReader( <br>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; new FileInputStream(<br>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; filename<br>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; )<br>&nbsp; &nbsp; &nbsp; &nbsp; )<br>&nbsp; &nbsp; &nbsp; );<br>&nbsp;</code></pre></div> <!-- .element: class="fragment" -->
---
# <pre>/usr/bin/irb</pre> <!-- .slide: class="center" -->
Note: Let's talk about ruby
---
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">irb> open source rocks</code></pre></div>
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">NameError: undefined local<br>variable or method `rocks'</code></pre></div> <!-- .element: class="fragment" -->
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">irb> def method_missing(@args)<br> &nbsp; &nbsp; &nbsp; args.join(" ")<br> &nbsp; &nbsp; end</code></pre></div> <!-- .element: class="fragment" -->
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">irb> open source rocks</code></pre></div> <!-- .element: class="fragment" -->
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">"open source rocks"</code></pre></div> <!-- .element: class="fragment" -->
Note: Method Missing is evil monkey patching
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

# <pre>/usr/bin/env perl -de1</pre> <!-- .slide: class="center" -->
Note: Let's talk about Perl

---

 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">DB&lt;1> if ("foo" == "bar") <br> &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; { print "true" }<br> &nbsp;&nbsp; &nbsp; else { print "false" }</code></pre></div>
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">true</code></pre></div> <!-- .element: class="fragment" -->
<span class="dasfoot"><a href="http://stackoverflow.com/a/14046720/124019">http://stackoverflow.com/a/14046720/124019</a></span>
Note: Reason is `==` is for number comparing

eq is for string comparing

a new programmer won't know this.
---


# <pre>/usr/bin/php -a</pre> <!-- .slide: class="center" -->

Note: Let's talk about PHP
---
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">php> $a = INF;</code></pre></div>
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">php> $b = array();</code></pre></div> <!-- .element: class="fragment" -->
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">php> $c = (object)array();</code></pre></div> <!-- .element: class="fragment" -->
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">php> var_dump( $a < $b );</code></pre></div> <!-- .element: class="fragment" -->
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">true</code></pre></div> <!-- .element: class="fragment" -->
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">php> var_dump( $b < $c );</code></pre></div> <!-- .element: class="fragment" -->
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">true</code></pre></div> <!-- .element: class="fragment" -->
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">php> var_dump( $c < $a );</code></pre></div> <!-- .element: class="fragment" -->
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">true</code></pre></div> <!-- .element: class="fragment" -->

<span class="dasfoot"><a href="http://phpsadness.com/sad/52">http://phpsadness.com/sad/52</a></span>
Note: cyclic truthiness. Totally a thing.

---

# <pre>C:&bsol;> powershell</pre> <!-- .slide: class="center" -->

Note: Let's talk about powershell

---

 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">PS> if (2 > 1) { "true" }<br>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; else { "false" }</code></pre></div>
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">true</code></pre></div> <!-- .element: class="fragment" -->
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%"><br>PS> if (2 < 1) { "true" }<br>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; else { "false" }</code></pre></div> <!-- .element: class="fragment" -->
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
<br><br> 
# Cheers! <!-- .slide: class="center" -->
<br><br> 
### <3 feedback - joind.in/15903 <!-- .slide: class="center" -->
 <img src="pictures/footer.svg" />