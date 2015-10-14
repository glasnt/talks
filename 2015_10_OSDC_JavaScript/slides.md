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

# JavaScript is Awe-ful <!-- .slide: class="center" -->
 <img src="pictures/footer.svg" />
---

 <img src="pictures/javascript_book.png" style="margin-top: -50px" />

Note: Tapestry and Cooking and Yelling

---

# Global Variables <!-- .slide: class="center" -->
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
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">> ans = ""; <c>//global</c></code></pre></div>
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">> function question() {<br>> &nbsp; var ans = 42; <c>//local</c><br>> &nbsp; return ans;<br>> }</code></pre></div>
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">> console.log(ans);</code></pre></div>
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">""</code></pre></div>
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">> console.log(question());</code></pre></div>
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">42</code></pre></div>
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">> console.log(ans);</code></pre></div>
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">""</code></pre></div>
---
<p></p> 
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">> ans = ""; <c>//global</c></code></pre></div>
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">> function question() {<br>> &nbsp; <s>var</s> ans = 42; <c>//global</c><br>> &nbsp; return ans;<br>> }</code></pre></div>
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">> console.log(ans);</code></pre></div>
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">""</code></pre></div>
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">> console.log(question());</code></pre></div>
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">42</code></pre></div>
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">> console.log(ans);</code></pre></div>
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">42</code></pre></div>
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
# Duck Typing <!-- .slide: class="center" -->
### Quack <!-- .element: class="fragment" -->

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
<p></p> 
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">> 4 + 2</code></pre></div>
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">6</code></pre></div>
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">> 4 - 2</code></pre></div>
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">2</code></pre></div>
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">> "4" - 2</code></pre></div>
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">2 <c>&nbsp;&nbsp; // type -> integer</c></code></pre></div>
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">> "4" + 2</code></pre></div>
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">"42"<c> // type -> string</c></code></pre></div>

Note: Automatic Type Co-ersion

Higher order type wins
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

Note: Associativity? Pfft!
---
<p></p> 
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">> [] + []</code></pre></div>
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">""</code></pre></div>
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">> [] + {}</code></pre></div>
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">[object Object]</code></pre></div>
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">> {} + []</code></pre></div>
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">0</code></pre></div>
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">> {} + {}</code></pre></div>
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">NaN <c>// wat</c></code></pre></div>
---
# Arrays != Objects <!-- .slide: class="center" -->
---
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">> var arr = ['a', 'b', 'c']</code></pre></div>
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">> arr</code></pre></div> <!-- .element: class="fragment" -->
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">["a", "b", "c"]</code></pre></div> <!-- .element: class="fragment" -->
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">> arr.hello = "world"</code></pre></div> <!-- .element: class="fragment" -->
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">"world"</code></pre></div> <!-- .element: class="fragment" -->
---
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">> arr</code></pre></div>
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">["a", "b", "c"]</code></pre></div> <!-- .element: class="fragment" -->
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">> for (var k in arr) {<br>>&nbsp;&nbsp; console.log(k);<br>> }</code></pre></div> <!-- .element: class="fragment" -->
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">0<br>1<br>2<br>hello</code></pre></div> <!-- .element: class="fragment" -->
---
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">> arr.push("append")</code></pre></div>
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">4</code></pre></div> <!-- .element: class="fragment" -->
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">> c = 0</code></pre></div> <!-- .element: class="fragment" -->
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">> for(var k in arr){ c++ }</code></pre></div> <!-- .element: class="fragment" -->
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">> c</code></pre></div> <!-- .element: class="fragment" -->
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">5</code></pre></div> <!-- .element: class="fragment" -->
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">> arr.length</code></pre></div> <!-- .element: class="fragment" -->
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">4</code></pre></div> <!-- .element: class="fragment" -->
---
# Equality <!-- .slide: class="center" -->
---
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">> 0 ==&nbsp; false</code></pre></div>
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">true</code></pre></div> <!-- .element: class="fragment" -->
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">> 0 === false</code></pre></div> <!-- .element: class="fragment" -->
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">false</code></pre></div> <!-- .element: class="fragment" -->
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">> 1 == &nbsp;"1"</code></pre></div> <!-- .element: class="fragment" -->
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">true</code></pre></div> <!-- .element: class="fragment" -->
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">> 1 === "1"</code></pre></div> <!-- .element: class="fragment" -->
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">false</code></pre></div> <!-- .element: class="fragment" -->
---
<p></p> 
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">> 0 ==&nbsp; false</code></pre></div>
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">true</code></pre></div>
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">> 0 === false</code></pre></div>
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">false</code></pre></div>
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">> 1 == &nbsp;"1" <c> // equality</c></code></pre></div>
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">true</code></pre></div>
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">> 1 === "1" <c>// equality without</c></code></pre></div>
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">false &nbsp; &nbsp; &nbsp; <c>// type co-ersion</c></code></pre></div>
---

<br><br> 
> The fact that === exists in languages like PHP and JavaScript is a sign that those languages are ridiculously broken.
> 
> -- @TheColonial

---

# Why is<br>JavaScript<br>so awful? <!-- .slide: class="center" -->
---

## ~~ wavey time passing lines ~~ <!-- .slide: class="center" -->
---

# 1995 <!-- .slide: class="center" -->
---
 <img src="pictures/needanimage.png" />

Note: The year is 1995. The documentary Hackers has been released, and people are burning through the data with their 28.8K BAUD modems

---

 <img src="pictures/needanimage.png" />
Note: Brendan Eich wanted to do fancy things

Made JavaScript in 10 days

Only took 6 to create the world

Waterfall software development cycle estimages

---

 <img src="pictures/needanimage.png" />

Note: Netscape view of javascript

Features: marquee title text

(only include the basic stuff)

---
 <img src="pictures/needanimage.png" />

Note: Lock-in. what could we do

Applets 

Flash 
---

<p></p> 
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">alert("My value = " + value);</code></pre></div>
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">// alert based debugging</code></pre></div>

 <img src="pictures/consolealert.png" />

---

# ~~ fast forward ~~ <!-- .slide: class="center" -->
---

# 2000 <!-- .slide: class="center" -->

---

 <img src="pictures/image.png" />

Note: big names in dotcomboom etc

---

 <img src="pictures/bubbleburst.png" />

Note: pop

---
# ~~ fast forward ~~ <!-- .slide: class="center" -->
---
# 2005 <!-- .slide: class="center" -->
---

 <img src="pictures/needanimage.png" />

Note: Things getting back together again

---

# 2006 <!-- .slide: class="center" -->
---

 <img src="pictures/firebug.png" />

Note: FIREBUG OMG
---

 <img src="pictures/mootools.png" />
---

 <img src="pictures/jquery.png" />
---

 <img src="pictures/rise of the framworks.png" />

Note: Why write javascript when you can use nice things that other people have written?
---

# 2009 <!-- .slide: class="center" -->
---

 <img src="pictures/node.js" />

---

## But I don't want to write<br>JavaScript<br>;_; <!-- .slide: class="center" -->

---

 <img src="pictures/coffeescirpt.png" />
## Not-shite JS -> JavaScript
---

 <img src="pictures/typescript.png" />
## Functional* -> JavaScript

---

 <img src="pictures/batavia.png" />
## Python -> JavaScript

---

## But I don't want to write<br>anything *other* than<br>JavaScript <!-- .slide: class="center" -->
---

Note: crosscompilers

---
# JavaScript isn't awful <!-- .slide: class="center" -->
---
# JavaScript is awe-ful <!-- .slide: class="center" -->
Note: It's amazing that we can take something so broken and made so much

The devil you know
---

# R.I.P<br>Java Applets <!-- .slide: class="center" -->
### &nbsp;
---
# R.I.P<br>Flash <!-- .slide: class="center" -->
### (mostly)
---
# JavaScript is awesome. <!-- .slide: class="center" -->
---
# But just remember... <!-- .slide: class="center" -->
## other languages have wats <!-- .slide: class="center" -->
---

# <pre>#!/usr/bin/env java</pre> <!-- .slide: class="center" -->

Note: Let's about about Java

---
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">/&#42;&#42; read from a file &#42;&#42;/</code></pre></div>
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">filename = "myfile.txt"</code></pre></div> <!-- .element: class="fragment" -->
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">f = new FileInputStream(filename);</code></pre></div> <!-- .element: class="fragment" -->
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">i = new InputStreamReader(fis);</code></pre></div> <!-- .element: class="fragment" -->
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">r = new BufferedReader(isr);</code></pre></div> <!-- .element: class="fragment" -->
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">String line = rdr.readLine();</code></pre></div> <!-- .element: class="fragment" -->
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">while(line != null){<br>&nbsp;&nbsp;/&#42; stuff &#42;/<br>&nbsp;&nbsp;line = rdr.readLine();<br>}</code></pre></div> <!-- .element: class="fragment" -->

---
# <pre>#!/usr/bin/env python</pre> <!-- .slide: class="center" -->
Note: Let's talk about Python
---
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">>>> ans = 42</code></pre></div>
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">>>> def question():</code></pre></div> <!-- .element: class="fragment" -->
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">... &nbsp; &nbsp; return ans</code></pre></div> <!-- .element: class="fragment" -->
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">>>> question()</code></pre></div> <!-- .element: class="fragment" -->
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">???</code></pre></div> <!-- .element: class="fragment" -->
---
<p></p> 
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">>>> ans = 42</code></pre></div>
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">>>> def question():</code></pre></div>
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">... &nbsp; &nbsp; return ans</code></pre></div>
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">>>> question()</code></pre></div>
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">42</code></pre></div>

Note: undefined answer within scope of the function

but it still works

---
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">>>> ans = 42</code></pre></div>
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">>>> def question():</code></pre></div> <!-- .element: class="fragment" -->
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">... &nbsp; &nbsp; ans += 1</code></pre></div> <!-- .element: class="fragment" -->
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">... &nbsp; &nbsp; return ans</code></pre></div> <!-- .element: class="fragment" -->
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">>>> question()</code></pre></div> <!-- .element: class="fragment" -->
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">???</code></pre></div> <!-- .element: class="fragment" -->
---
<p></p> 
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">>>> ans = 42</code></pre></div>
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">>>> def question():</code></pre></div>
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">... &nbsp; &nbsp; ans += 1</code></pre></div>
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">... &nbsp; &nbsp; return ans</code></pre></div>
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">>>> question()</code></pre></div>
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">Traceback (most recent call last):<br> &nbsp;File "<stdin>", line 1, in <module><br> &nbsp;File "<stdin>", line 2, in question<br> UnboundLocalError: local variable 'ans' referenced before assignment</code></pre></div>

Note: manipulation of variable within the scope
---
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">>>> a = 256</code></pre></div>
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">>>> b = 256</code></pre></div> <!-- .element: class="fragment" -->
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">>>> a **is** b</code></pre></div> <!-- .element: class="fragment" -->
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">???</code></pre></div> <!-- .element: class="fragment" -->
---
<p></p> 
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">>>> a = 256</code></pre></div>
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">>>> b = 256</code></pre></div>
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">>>> a **is** b</code></pre></div>
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">True</code></pre></div>

---
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">>>> a = 257</code></pre></div>
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">>>> b = 257</code></pre></div> <!-- .element: class="fragment" -->
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">>>> a **is** b</code></pre></div> <!-- .element: class="fragment" -->
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">???</code></pre></div> <!-- .element: class="fragment" -->
---
<p></p> 
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">>>> a = 257</code></pre></div>
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">>>> b = 257</code></pre></div>
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">>>> a **is** b</code></pre></div>
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">False</code></pre></div>
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%"><br>>>> a = 257; b = 257</code></pre></div> <!-- .element: class="fragment" -->
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">>>> a **is** b</code></pre></div> <!-- .element: class="fragment" -->
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">???</code></pre></div> <!-- .element: class="fragment" -->
---
<p></p> 
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">>>> a = 257</code></pre></div>
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">>>> b = 257</code></pre></div>
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">>>> a **is** b</code></pre></div>
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">False</code></pre></div>
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%"><br>>>> a = 257; b = 257</code></pre></div>
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">>>> a **is** b</code></pre></div>
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">True</code></pre></div>

---
# wat <!-- .slide: class="center" -->

---
### Wat - Gary Bernhardt, CodeMash 2012
### Investigating Python Wats - Amy Hanlon, Python 2015