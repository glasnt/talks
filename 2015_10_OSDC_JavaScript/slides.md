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

 <img src="pictures/javascript_book.png" style="margin-top: -50px" />

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
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">> arr.push("append");</code></pre></div>
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">4</code></pre></div> <!-- .element: class="fragment" -->
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">> c = 0;</code></pre></div> <!-- .element: class="fragment" -->
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">> for (var k in arr) {<br>>&nbsp; &nbsp; c = c + 1; <br>> }</code></pre></div> <!-- .element: class="fragment" -->
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
# But, why? <!-- .slide: class="center" -->
Note: why is javascript so awful
---

## ~~ wavey time passing lines ~~ <!-- .slide: class="center" -->
---

# 1993 <!-- .slide: class="center" -->
---
<br><br> 
<pre><code> 
&nbsp; Hypertext Markup Language (HTML)&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; Tim Berners-Lee, CERN
&nbsp; Internet Draft&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; Daniel Connolly, Atrium
&nbsp; IIIR Working Group&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; June 1993


&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; Hypertext Markup Language (HTML)

&nbsp; &nbsp; &nbsp; A Representation of Textual Information and MetaInformation
&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; for Retrieval and Interchange
</pre></code> 

<span class="dasfoot"><a href="http://www.w3.org/MarkUp/draft-ietf-iiir-html-01.txt">http://www.w3.org/MarkUp/draft-ietf-iiir-html-01.txt</a></span>
---
## The Original HTML
<br> 
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">&lt;HTML></code></pre></div>
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">&lt;TITLE>My Page&lt;/TITLE></code></pre></div>
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">&lt;BODY></code></pre></div>
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">&nbsp; &nbsp; &lt;P>Hello World Wide Web&lt;/P></code></pre></div>
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">&lt;/BODY></code></pre></div>
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">&lt;/HTML></code></pre></div>

Note: YELLING TAGS
---
## Anchor Tags <!-- .slide: class="center" -->
<br> 
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">&lt;<h>A</h> HREF="index.html">My Page&lt;/<h>A</h>></code></pre></div> <!-- .element: class="fragment" -->
---
## Glossary or Definition List <!-- .slide: class="center" -->
<pre><code> 
&nbsp; &lt;H1>Dictionary&lt;/H1>
&nbsp; <h>&lt;DT></h>pun<h>&lt;/DT></h>
&nbsp; <h>&lt;DD></h>a joke exploiting the different possible meanings of
&nbsp; a word or the fact that there are words that sound alike
&nbsp; but have different meanings. <h>&lt;/DD></h><br>
</code></pre> 
 <img src="pictures/dt.png" width="60%"> <!-- .element: class="fragment" -->
---
<br> 
# <img src="pictures/static.jpg"> <!-- .slide: class="center" -->
---
# ~~ wavey lines ~~ <!-- .slide: class="center" -->
---
# 1995 <!-- .slide: class="center" -->
Note: The year is 1995. The documentary Hackers has been released, and people are burning through the data with their 28.8K BAUD modems

---

# <img src="pictures/netscape-navigator.jpg" width="40%"> <!-- .slide: class="center" -->

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
</pre></code> 

---
# <img src="pictures/javascript_1995.png" width="40%"> <!-- .slide: class="center" -->

Note: Brendan Eich wanted to do fancy things

Made JavaScript in 10 days

Only took 6 to create the world

Waterfall software development cycle estimages

---
<p></p> 
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">// alert based debugging</code></pre></div>
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">alert(my_date);</code></pre></div>

# <img src="pictures/alert-debugging.gif" width="40%"> <!-- .slide: class="center" -->

---

# ~~ fast forward ~~ <!-- .slide: class="center" -->
---

# 2000 <!-- .slide: class="center" -->

---

@ image.png <!-- .slide: class="center" -->

Note: big names in dotcomboom etc

---

@ bubbleburst.png <!-- .slide: class="center" -->

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

@ firebug.png <!-- .slide: class="center" -->

Note: FIREBUG OMG
---

@ mootools.png <!-- .slide: class="center" -->
---

@ jquery.png <!-- .slide: class="center" -->
---

@ rise of the framworks.png <!-- .slide: class="center" -->

Note: Why write javascript when you can use nice things that other people have written?
---

# 2009 <!-- .slide: class="center" -->
---

@ node.js <!-- .slide: class="center" -->

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

@ crosscompiler.png <!-- .slide: class="center" -->
Note: crosscompilers



---

## Debugging
# 
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">console.log()</code></pre></div>


---

 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">window.console = typeof window.console === 'undefined'</code></pre></div>
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">&nbsp; &nbsp; ? {log:function(str){ alert(str) }}</code></pre></div>
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">&nbsp; &nbsp; : window.console;</code></pre></div>
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%"><br>console.log("oh good god.");</code></pre></div>


Note: console.log isn't defined in any ECMA standard, therefore it doesn't have to exist.

---

facebook console css


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
<br><br> 
> ... when that's the glue of the modern day web it's minor miracle that society even functions
> 
> -- @NamTaf
---
# But just remember... <!-- .slide: class="center" -->
## other languages have wats <!-- .element: class="fragment" -->
---

# <pre>#!/usr/bin/env java</pre> <!-- .slide: class="center" -->

Note: Let's about about Java

---
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%"><c>/&#42;&#42; read from a file &#42;&#42;/</c></code></pre></div>
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">filename = "myfile.txt"</code></pre></div> <!-- .element: class="fragment" -->
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">f = new FileInputStream(filename);</code></pre></div> <!-- .element: class="fragment" -->
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">i = new InputStreamReader(fis);</code></pre></div> <!-- .element: class="fragment" -->
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">r = new BufferedReader(isr);</code></pre></div> <!-- .element: class="fragment" -->
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">String line = rdr.readLine();</code></pre></div> <!-- .element: class="fragment" -->
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">while(line != null){<br>&nbsp;&nbsp;<c>/&#42; actual processing &#42;/</c><br>&nbsp;&nbsp;line = rdr.readLine();<br>}</code></pre></div> <!-- .element: class="fragment" -->

---
# <pre>#!/usr/bin/env ruby</pre> <!-- .slide: class="center" -->
Note: Let's talk about ruby
---
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">BAR = "outer"</code></pre></div>
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">module A</code></pre></div>
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">&nbsp; FOO = nil; BAR = "inner"</code></pre></div>
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">&nbsp; module B</code></pre></div>
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">&nbsp; &nbsp; puts A::FOO::BAR</code></pre></div>
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">&nbsp; end</code></pre></div>
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">end</code></pre></div>
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">puts A::FOO::BAR</code></pre></div>
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%"><br>???</code></pre></div> <!-- .element: class="fragment" -->

Note: https://twitter.com/charliesome/status/654190206547968000
---
<p></p> 
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">BAR = "outer"</code></pre></div>
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">module A</code></pre></div>
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">&nbsp; FOO = nil; BAR = "inner"</code></pre></div>
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">&nbsp; module B</code></pre></div>
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">&nbsp; &nbsp; puts A::FOO::BAR</code></pre></div>
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">&nbsp; end</code></pre></div>
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">end</code></pre></div>
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">puts A::FOO::BAR</code></pre></div>
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%"><br>inner</code></pre></div>
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">outer</code></pre></div>
---
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">TODO Barewords</code></pre></div>
Note: Method Missing
---

# <pre>ghci</pre> <!-- .slide: class="center" -->
Note: Let's talk about Haskell
---

 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">λ&gt; length []</code></pre></div>
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">0</code></pre></div> <!-- .element: class="fragment" -->
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">λ&gt; length [1]</code></pre></div> <!-- .element: class="fragment" -->
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">1</code></pre></div> <!-- .element: class="fragment" -->
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">λ&gt; length [1,2]</code></pre></div> <!-- .element: class="fragment" -->
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">2</code></pre></div> <!-- .element: class="fragment" -->
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">λ> :type [1,2]</code></pre></div> <!-- .element: class="fragment" -->
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">[1,2] :: Num t => [t]</code></pre></div> <!-- .element: class="fragment" -->

Note: Type of List
---

 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">λ> :type (1,2)</code></pre></div>
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">(1,2) :: (Num t, Num t1)=>(t, t1)</code></pre></div> <!-- .element: class="fragment" -->
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">λ> length (1,2)</code></pre></div> <!-- .element: class="fragment" -->
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">1</code></pre></div> <!-- .element: class="fragment" -->

Note: because foldable, fMap fun
---

 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">λ> length (Left 0)</code></pre></div>
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">0</code></pre></div> <!-- .element: class="fragment" -->
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">λ> length (Right 0)</code></pre></div> <!-- .element: class="fragment" -->
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">1</code></pre></div> <!-- .element: class="fragment" -->

---
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">λ> let a = 2 + 2</code></pre></div>
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">λ> a</code></pre></div> <!-- .element: class="fragment" -->
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">4</code></pre></div> <!-- .element: class="fragment" -->
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">λ> let b = 2 + 2 where 2 + 2 = 5</code></pre></div> <!-- .element: class="fragment" -->
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">λ> wat</code></pre></div> <!-- .element: class="fragment" -->
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">5</code></pre></div> <!-- .element: class="fragment" -->

---
# <pre>#!/usr/bin/env python</pre> <!-- .slide: class="center" -->
Note: Let's talk about Python
---
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">>>> ans = 42</code></pre></div>
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">>>> def question(): <br>... &nbsp; &nbsp; return ans</code></pre></div> <!-- .element: class="fragment" -->
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">>>> question()</code></pre></div> <!-- .element: class="fragment" -->
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">42</code></pre></div> <!-- .element: class="fragment" -->

Note: undefined answer within scope of the function

but it still works

---
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">>>> ans = 42</code></pre></div>
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">>>> def question():</code></pre></div> <!-- .element: class="fragment" -->
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">... &nbsp; &nbsp; ans += 1</code></pre></div> <!-- .element: class="fragment" -->
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">... &nbsp; &nbsp; return ans</code></pre></div> <!-- .element: class="fragment" -->
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">>>> question()</code></pre></div> <!-- .element: class="fragment" -->
 <div style='margin-bottom:0px; font-size: 80px'><pre style='margin-bottom:0px;margin-top:0px'><code style="font: 'monospace' 150%">Traceback (most recent call last):<br> &nbsp;File "<stdin>", line 1, in <module><br> &nbsp;File "<stdin>", line 2, in question<br> UnboundLocalError: local variable 'ans' referenced before assignment</code></pre></div> <!-- .element: class="fragment" -->

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
<br><br> 
<br><br> 
<br><br> 
<h4>Sources of some wats</h4>
<h4> Wat - Gary Bernhardt, CodeMash 2012</h4>
https://github.com/puffnfresh/wat-collection 
<h4> Investigating Python Wats - Amy Hanlon, Python 2015 </h4>