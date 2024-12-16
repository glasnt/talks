class: title
# <br>Turning wat into why
## FOSDEM 2025
## 🐘 glasnt@cloudisland.nz

---
class: title
# JavaScript
???

Let's talk about javascript

---
.righthead[JavaScript]
<pre><code class="javascript">> 4 + 2</code></pre>
--
<pre><code class="javascript">6</code></pre>
--
<pre><code class="javascript">> 4 - 2</code></pre>
--
<pre><code class="javascript">2</code></pre>
--
<pre><code class="javascript">> 4 - "2"</code></pre>
--
<pre><code class="javascript">2</code></pre>
--
<pre><code class="javascript">> 4 + "2"</code></pre>
--
<pre><code class="javascript">"42"</code></pre>

---
.righthead[JavaScript]
.footnotes[wait, what? JavaScript?]
<pre><code class="javascript">> 1 == "1"</code></pre>
--
<pre><code class="javascript">true</code></pre>
--
<pre><code class="javascript">> 1 === "1"</code></pre>
--
<pre><code class="javascript">false</code></pre>

---
.righthead[JavaScript]
.footnotes[... thi..this is the Python track, right?]
<pre><code class="javascript">> [] + []</code></pre>
--
<pre><code class="javascript">""</code></pre>
--
<pre><code class="javascript">> [] + {}</code></pre>
--
<pre><code class="javascript">"[object Object]"</code></pre>
--
<pre><code class="javascript">> {} + []</code></pre>
--
<pre><code class="javascript">0</code></pre>
--
<pre><code class="javascript">> {} + {}</code></pre>
--
<pre><code class="javascript">NaN</code></pre>

---
background-image: url("images/wat.png")
.wat[wat]
.wfootnotes[Florentijn Hofman, *Rubber Duck*. Photographer unknown.]
???

Some of you might recognise the last example from Gary Bernhardt's "wat" talk.
That talk, now 12 years old, is part of the original inspiration for this talk.
In his talk, he focuses on the "wat", without explaining much more.
Instead I want to focus on the ...

---
background-image: url("images/wat-river.png")
.wat[.strike[wat]]
.why[why]
.wfootnotes[Florentijn Hofman, *Rubber Duck, Paramatta River, Sydney*. Photo: 564dude (CC BY-SA 3.0)]
???

...why. We're going to focus this talk on learning why these examples work they way they do, and more specifically:

---
background-image: url("images/wat-cobra.png")
.wat[.strike[wat]]
.why[why]
.how[how]
.footnotes[Wild Republic Toys, *Rubber Duck - Cobra*. Product photograph.]
???

How you can learn from these examples as a Python developer. Specifically, if Python has the same issues, and how to avoid them.
So let's cover the examples already shown.

---
class: title
# JavaScript
???

Let's talk about javascript

---
.righthead[JavaScript]
<pre><code class="javascript">> 4 + 2</code></pre>
<pre><code class="javascript">6</code></pre>
<pre><code class="javascript">> 4 - 2</code></pre>
<pre><code class="javascript">2</code></pre>
<pre><code class="javascript">> 4 - "2"</code></pre>
<pre><code class="javascript">2</code></pre>
<pre><code class="javascript">> 4 + "2"</code></pre>
<pre><code class="javascript">"42"</code></pre>
???

Implicit coersion, depending on the operator

---
.righthead[JavaScript]
<pre><code class="javascript">> 4 + 2</code></pre>
<pre><code class="javascript">6</code></pre>
<pre><code class="javascript">> 4 - 2</code></pre>
<pre><code class="javascript">2</code></pre>
<pre><code class="javascript">> 4 .blue[-] "2" // implicit coercion</code></pre>
<pre><code class="javascript">2</code></pre>
<pre><code class="javascript">> 4 + "2"</code></pre>
<pre><code class="javascript">"42"</code></pre>
???
1: subtraction is only defined for numerics, so it coerces the string into a number

---
.righthead[JavaScript]
<pre><code class="javascript">> 4 + 2</code></pre>
<pre><code class="javascript">6</code></pre>
<pre><code class="javascript">> 4 - 2</code></pre>
<pre><code class="javascript">2</code></pre>
<pre><code class="javascript">> 4 .blue[-] "2" // implicit coercion</code></pre>
<pre><code class="javascript">2</code></pre>
<pre><code class="javascript">> 4 .blue[+] "2" // overloaded operator</code></pre>
<pre><code class="javascript">"42"</code></pre>
???
2: the plus is an overloaded operator. It can act as both numeric addition, or in this case, concatenation

---
.righthead[JavaScript]
<pre><code class="javascript">> 1 == "1"</code></pre>
<pre><code class="javascript">true</code></pre>
<pre><code class="javascript">> 1 === "1"</code></pre>
<pre><code class="javascript">false</code></pre>
???

This next example is to do with the difference in the equality operators

---
.righthead[JavaScript]
<pre><code class="javascript">> 1 .blue[==] "1" &nbsp;// with type coercion</code></pre>
<pre><code class="javascript">true</code></pre>
<pre><code class="javascript">> 1 === "1"</code></pre>
<pre><code class="javascript">false</code></pre>

---
.righthead[JavaScript]
<pre><code class="javascript">> 1 .blue[==] "1" &nbsp;// with type coercion</code></pre>
<pre><code class="javascript">true</code></pre>
<pre><code class="javascript">> 1 .blue[===] "1" // without type coercion</code></pre>
<pre><code class="javascript">false</code></pre>

---
.righthead[JavaScript]
<pre><code class="javascript">> [] + []</code></pre>
<pre><code class="javascript">""</code></pre>
<pre><code class="javascript">> [] + {}</code></pre>
<pre><code class="javascript">"[object Object]"</code></pre>
<pre><code class="javascript">> {} + []</code></pre>
<pre><code class="javascript">0</code></pre>
<pre><code class="javascript">> {} + {}</code></pre>
<pre><code class="javascript">NaN</code></pre>
???

but as for this example...

---
.righthead[JavaScript]
<pre><code class="javascript">> [] + []</code></pre>
<pre><code class="javascript">"" .white[..............] // ???</code></pre>
<pre><code class="javascript">> [] + {}</code></pre>
<pre><code class="javascript">"[object Object]" // ???</code></pre>
<pre><code class="javascript">> {} + []</code></pre>
<pre><code class="javascript">0 .white[...............] // ???</code></pre>
<pre><code class="javascript">> {} + {}</code></pre>
<pre><code class="javascript">NaN .white[.............] // ???</code></pre>
???

This one is a bit more complicated.

---
class: title
# +
???

Remember that overloaded operator I mentioned earlier?
I sort of handwaved that.
Let's dive into exactly what this does.

---
class: center
# .ecma[.ecma-header[ECMA-262, 10th edition]]
## .ecma[.ecma-header[ECMAScript® 2019 Language Specification]]
### .ecma[12.8.3 The Addition Operator ( `+` )]
#### &nbsp;
???

TODO(glasnt): update to 2024 deck version.

---
class: center
# .ecma[.ecma-header[ECMA-262, 10th edition]]
## .ecma[.ecma-header[ECMAScript® 2019 Language Specification]]
### .ecma[12.8.3 The Addition Operator ( `+` )]
#### NOTE The addition operator either performs string concatenation or numeric addition.

---
.righthead[ECMAScript]
## .bluef[`a`] `+` .greenf[`b`]
???

Consider two variables, a and b
In order to do the plus operation, we need to work out which operation that is: addition or conccatenation
In order to do that
--.ecma[.bc[Convert .bluef[`a`] and .greenf[`b`] to primatives]]
???

we need to first reduce both sides of the operator to their primative forms
--* .ecma[.bc[that is, `typeof()` in `undefined`, `null`, `boolean`, `number`, `string`]]
???

That is, the type of the variable is undefined, null, bool, number, or string
To do that, we have two options
--* .ecma[First try, .bc[`.valueOf()`], otherwise .bc[`.toString()`]]
???

We have `valueOf`, or `toString`
After both operands are in their primative forms, we then have a choice
--.ecma[Are either .bc[.bluef[`a`]] or .bc[.greenf[`b`]] a string?]
???

If either of the sides are a string,
--.ecma[Yes → .bc[Concatenate `String(`.bluef[`a`]`)` and `String(`.greenf[`b`]`)`]]
???

then we perform a concatenation
--.ecma[No → .bc[Add `Number(`.bluef[`a`]`)` and `Number(`.greenf[`b`]`)`]]
???

otherwise, we convert both sides to a number, and add them.

---
.righthead[ECMAScript]
## .bluef[`[]`] `+` .greenf[`{}`]
--.ecma[.bc[Convert .bluef[`[]`] to primative]]
--* .ecma[.bc[that is, `typeof()` in `undefined`, `null`, `boolean`, `number`, `string`]]
* .ecma[First try, .bc[`.valueOf()`]]
--<pre><code class="javascript">> [].valueOf()</code></pre>
--
<pre><code class="javascript">[]</code></pre>
--
<pre><code class="javascript">> typeof([].valueOf())</code></pre>
--
<pre><code class="javascript">"object"</code></pre>

---
.righthead[ECMAScript]
## .bluef[`[]`] `+` .greenf[`{}`]
.ecma[.bc[Convert .bluef[`[]`] to primative]]
* .ecma[.bc[that is, `typeof()` in `undefined`, `null`, `boolean`, `number`, `string`]]
* .ecma[First try, .bc[`.valueOf()`, else `.toString()`]]
--<pre><code class="javascript">> [].toString()</code></pre>
--
<pre><code class="javascript">""</code></pre>
--
<pre><code class="javascript">> typeof([].toString())</code></pre>
--
<pre><code class="javascript">"string"</code></pre>

---
.righthead[ECMAScript]
## .bluef[`""`] `+` .greenf[`{}`]
--.ecma[.bc[Convert .greenf[`{}`] to primative]]
--* .ecma[.bc[that is, `typeof()` in `undefined`, `null`, `boolean`, `number`, `string`]]
* .ecma[First try, .bc[`.valueOf()`]]
--<pre><code class="javascript">> {}.valueOf()</code></pre>
--
<pre><code class="javascript">{}</code></pre>
--
<pre><code class="javascript">> typeof({}.valueOf())</code></pre>
--
<pre><code class="javascript">"object"</code></pre>

---
.righthead[ECMAScript]
## .bluef[`""`] `+` .greenf[`{}`]
.ecma[.bc[Convert .greenf[`{}`] to primative]]
* .ecma[.bc[that is, `typeof()` in `undefined`, `null`, `boolean`, `number`, `string`]]
* .ecma[First try, .bc[`.valueOf()`, else `.toString()`]]
--<pre><code class="javascript">> {}.toString()</code></pre>
--
<pre><code class="javascript">"[object Object]"</code></pre>
--
<pre><code class="javascript">// ... huh?</code></pre>

---
.righthead[ECMAScript]
.fix-tilt[aside]
<pre><code class="javascript">> String({"a": "b"})</code></pre>
<pre><code class="javascript">"[object Object]"</code></pre>
???
As an aside: the default string representation of a object is the string object object
A lot of other languages have printed representations of dictionaries or objects that are more useful, but not javascript.

---
.righthead[ECMAScript]
.fix-tilt[aside]
<pre><code class="javascript">> String({"a": "b"})</code></pre>
<pre><code class="javascript">"[object Object]"</code></pre>
<br>
<pre><code class="javascript">> JSON.stringify({"a": "b"})</code></pre>
<pre><code class="javascript">'{"a":"b"}'</code></pre>
???
If you do want to get the string representation without altering the functionality of Obejcts, you can use JSON.stringify to natively check
Backwards compatibility

---
.righthead[ECMAScript]
## .bluef[`""`] `+` .greenf[`{}`]
.ecma[.bc[Convert .greenf[`{}`] to primative]]
* .ecma[.bc[that is, `typeof()` in `undefined`, `null`, `boolean`, `number`, `string`]]
* .ecma[First try, .bc[`.valueOf()`, else `.toString()`]]
--<pre><code class="javascript">> {}.toString()</code></pre>
--
<pre><code class="javascript">"[object Object]"</code></pre>
--
<pre><code class="javascript">> typeof({}.toString())</code></pre>
--
<pre><code class="javascript">"string"</code></pre>

---
.righthead[ECMAScript]
## .bluef[`""`] `+` .greenf[`"[object Object]"`]
--.ecma[Are .bc[.bluef[`""`]] or .bc[.greenf[`"[object Object]"`]] a string?]
--.ecma[Yes → .bc[Concatenate `String(`.bluef[`a`]`)` and `String(`.greenf[`b`]`)`]]
--<pre><code class="javascript">> "" + "[object Object]"</code></pre>
--
<pre><code class="javascript">"[object Object]"</code></pre>

---
.righthead[ECMAScript]
.bc[.bluef[`[] → ""`] &nbsp; &nbsp; .greenf[`{} → "[object Object]"`]]
--<pre><code class="javascript">> [] + []</code></pre>
--
.code[.greyf[.bc[`≈ "" + ""`]]]
--<pre><code class="javascript">""</code></pre>
--
<br><br>
<pre><code class="javascript">> [] + {}</code></pre>
--
.code[.greyf[.bc[`≈ "" + "[object Object]"`]]]
--<pre><code class="javascript">"[object Object]"</code></pre>

---
.righthead[ECMAScript]
.bc[.bluef[`[] → ""`] &nbsp; &nbsp; .greenf[`{} → "[object Object]"`]]
--<pre><code class="javascript">> {} + []</code></pre>

---
.righthead[ECMAScript]
.bc[.bluef[`[] → ""`] &nbsp; &nbsp; .greenf[`{} → "[object Object]"`]]
<pre><code class="javascript">> .blue[{}] + [] // empty block</code></pre>
???

Code blocks are ignored, as a no-op
So we can ignore that side, but the other side

---
.righthead[ECMAScript]
.bc[.bluef[`[] → ""`] &nbsp; &nbsp; .greenf[`{} → "[object Object]"`]]
<pre><code class="javascript">> .grey[{}] .green[+ []] // unary addition</code></pre>
???

the other side is a unary addition, which casts the object to number

---
.righthead[ECMAScript]
.bc[.bluef[`[] → ""`] &nbsp; &nbsp; .greenf[`{} → "[object Object]"`]]
<pre><code class="javascript">> {} + []</code></pre>
.code[.greyf[.bc[`≈ ` &nbsp &nbsp`+ ""`]]]
???

this is the equiv of casting the empty string, the primative from earlier, to a number
Which in this case is zero
~~~~~~~~~~~~
--<pre><code class="javascript">0</code></pre>
--
<br><br>
<pre><code class="javascript">> {} + {}</code></pre>
--
.code[.greyf[.bc[`≈ ` &nbsp &nbsp`+ "[object Object]"`]]]
???

unary addition on a string is the same as
casting a string to a number
Which works just about as well as you think
--<pre><code class="javascript">NaN</code></pre>
???

Therefore.

---
.righthead[ECMAScript]
<pre><code class="javascript">> [] + []</code></pre>
--
<pre><code class="javascript">""</code></pre>
--
<pre><code class="javascript">> [] + {}</code></pre>
--
<pre><code class="javascript">"[object Object]"</code></pre>
--
<pre><code class="javascript">> {} + []</code></pre>
--
<pre><code class="javascript">0</code></pre>
--
<pre><code class="javascript">> {} + {}</code></pre>
--
<pre><code class="javascript">NaN</code></pre>

---
.righthead[ECMAScript]
<pre><code class="javascript">> [] + []</code></pre>
<pre><code class="javascript">""</code></pre>
<pre><code class="javascript">> [] + {}</code></pre>
<pre><code class="javascript">"[object Object]"</code></pre>
<pre><code class="javascript">> {} + []</code></pre>
<pre><code class="javascript">0</code></pre>
<pre><code class="javascript">> {} + {}</code></pre>
<pre><code class="javascript">NaN</code></pre>
.fix-notilt[<img src="images/tada.png">]
???

tada

---
.righthead[ECMAScript]
<pre><code class="javascript">> [] + []</code></pre>
<pre><code class="javascript">""</code></pre>
<pre><code class="javascript">> [] + {}</code></pre>
<pre><code class="javascript">"[object Object]"</code></pre>
<pre><code class="javascript">> {} + []</code></pre>
<pre><code class="javascript">0</code></pre>
<pre><code class="javascript">> {} + {}</code></pre>
<pre><code class="javascript">NaN</code></pre>
.fix-notilt[<img src="images/tadoh.png">]
???

but, technically, this isn't completely right
I mean, everything I've just said is accurate, but the problem is that we were using flawed logic.
That code block is only intepreted as a codeblock if it's leading the statement
In these examples, we can't rely on the console interpreting things for us.
We should be using actual IO operations, variables, etc, to replicate what we would get in production code.

---
.righthead[ECMAScript]
.code[`> var` .bluef[.bc[`a`]] ` = []; var` .greenf[.bc[`b`]] ` = {}`]
--.code[.bc[> .bluef[`a`] + .bluef[`a`]]]
--<pre><code class="javascript">""</code></pre>
--
.code[.bc[> .bluef[`a`] + .greenf[`b`]]]
--<pre><code class="javascript">"[object Object]"</code></pre>
--
.code[.bc[> .greenf[`b`] + .bluef[`a`]]]
--<pre><code class="javascript">"[object Object]"</code></pre>
--
.code[.bc[> .greenf[`b`] + .greenf[`b`]]]
--<pre><code class="javascript">NaN</code></pre>

---
.righthead[ECMAScript]
.code[`> var` .bluef[.bc[`a`]] ` = []; var` .greenf[.bc[`b`]] ` = {}`]
.code[.bc[> .bluef[`a`] + .bluef[`a`]]]
<pre><code class="javascript">""</code></pre>
.code[.bc[> .bluef[`a`] + .greenf[`b`]]]
<pre><code class="javascript">"[object Object]"</code></pre>
.code[.bc[> .greenf[`b`] + .bluef[`a`]]]
<pre><code class="javascript">"[object Object]"</code></pre>
.code[.bc[> .greenf[`b`] + .greenf[`b`]]]
<pre><code class="javascript">NaN</code></pre>
.fix-tilt-long[commutative]
.fix-notilt[<img src="images/tada.png">]
???

Commutative - same forwards as is backwards
Pron.: Com-ut-a-tive

---
class: title
# TODO(glasnt): Python Angle

---
class: title
# Java
???

TODO(glasnt): Java Intro

---
.righthead[Java]
<pre><code class="java">java> Integer a = 128</code></pre>
--
<pre><code class="java">java> Integer b = 128</code></pre>
--
<pre><code class="java">java> a <= b</code></pre>
--
<pre><code class="java">true</code></pre>
--
<pre><code class="java">java> a >= b</code></pre>
--
<pre><code class="java">true</code></pre>
--
<pre><code class="java">java> a == b</code></pre>
--
<pre><code class="java">false</code></pre>

---
.righthead[Java]
<pre><code class="java">java> Integer a = 128</code></pre>
<pre><code class="java">java> Integer b = 128</code></pre>
<pre><code class="java">java> a <= b</code></pre>
<pre><code class="java">true</code></pre>
<pre><code class="java">java> a >= b</code></pre>
<pre><code class="java">true</code></pre>
<pre><code class="java">java> a .blue[==] b .grey[/.w[✱] identity .w[✱]/]</code></pre>
<pre><code class="java">false</code></pre>
--.righthead[IntegerCache]
<pre><code class="bash">.white[.............................][-127][-126][...][126][127]</code></pre>
???

---
.righthead[Java]
<pre><code class="java">java> Integer a = 128</code></pre>
<pre><code class="java">java> Integer b = 128</code></pre>
<pre><code class="java">java> a <= b</code></pre>
<pre><code class="java">true</code></pre>
<pre><code class="java">java> a >= b</code></pre>
<pre><code class="java">true</code></pre>
<pre><code class="java">java> a .green[.equals] (b)</code></pre>
<pre><code class="java">true</code></pre>
.fix-tilt[fix #1]

---
.righthead[Java]
<pre><code class="java">java> .green[int] a = 128</code></pre>
<pre><code class="java">java> .green[int] b = 128</code></pre>
<pre><code class="java">java> a <= b</code></pre>
<pre><code class="java">true</code></pre>
<pre><code class="java">java> a >= b</code></pre>
<pre><code class="java">true</code></pre>
<pre><code class="java">java> a == b</code></pre>
<pre><code class="java">true</code></pre>
.fix-tilt[fix #2]

---
class: title
# TODO(glasnt): How does *integer caching* affect Python?
##- Yes.

---
class: title
# Python
???

TODO(glasnt): Python Intro

---
.righthead[Python]
<pre><code class="python">>>> a = 256</code></pre>
--
<pre><code class="python">>>> b = 256</code></pre>
--
<pre><code class="python">>>> a is b</code></pre>
--
<pre><code class="python">True</code></pre>

---
.righthead[Python]
<pre><code class="python">>>> a = 257</code></pre>
--
<pre><code class="python">>>> b = 257</code></pre>
--
<pre><code class="python">>>> a is b</code></pre>
--
<pre><code class="python">False</code></pre>
--
<br>
<pre><code class="python">>>> a = 257; b = 257</code></pre>
--
<pre><code class="python">>>> a is b</code></pre>
--
<pre><code class="python">True</code></pre>

---
.righthead[Terminal]
`~ $ python`
???

In Python, when you load the interpreter, you're probably loading CPython.
--.righthead[CPython]
<pre><code class="python">>>> .white[a=b]</code></pre>
<pre><code class="python">.white[.]</code></pre>
<pre><code class="python">.white[.]</code></pre>
<pre><code class="python">.white[.]</code></pre>
.righthead[CPython Cache]
<pre><code class="bash">&nbsp;</code></pre>
<pre><code class="bash">[ -5 ][ -4 ][...][ 254 ][ 255 ][ 256 ]</code></pre>
???
An optimisation of CPython is to create a list of integers from -5 to 256 for you.

---
.righthead[Terminal]
`~ $ python`
.righthead[CPython]
<pre><code class="python">>>> a = 256</code></pre>
<pre><code class="python">.white[.]</code></pre>
<pre><code class="python">.white[.]</code></pre>
<pre><code class="python">.white[.]</code></pre>
.righthead[CPython Cache]
<pre><code class="bash">&nbsp;</code></pre>
<pre><code class="bash">[ -5 ][ -4 ][...][ 254 ][ 255 ][ 256 ]</code></pre>
<pre><code class="bash">.white[.................................]a</code></pre>
???

so when you assign a variable, it can use one you prepared earlier

---
.righthead[Terminal]
`~ $ python`
.righthead[CPython]
<pre><code class="python">>>> a = 256</code></pre>
<pre><code class="python">>>> b = 256</code></pre>
<pre><code class="python">.white[.]</code></pre>
<pre><code class="python">.white[.]</code></pre>
.righthead[CPython Cache]
<pre><code class="bash">&nbsp;</code></pre>
<pre><code class="bash">[ -5 ][ -4 ][...][ 254 ][ 255 ][ 256 ]</code></pre>
<pre><code class="bash">.white[.................................]a b</code></pre>

---
.righthead[Terminal]
`~ $ python`
.righthead[CPython]
<pre><code class="python">>>> a = 256</code></pre>
<pre><code class="python">>>> b = 256</code></pre>
<pre><code class="python">>>> a is b</code></pre>
<pre><code class="python">.white[.]</code></pre>
.righthead[CPython Cache]
<pre><code class="bash">&nbsp;</code></pre>
<pre><code class="bash">[ -5 ][ -4 ][...][ 254 ][ 255 ][ 256 ]</code></pre>
<pre><code class="bash">.white[.................................]a b</code></pre>
???
So `is` when we talk about "is" here, we're doing an identity check.
Identity is a check to see if two objects are the same

---
.righthead[Terminal]
`~ $ python`
.righthead[CPython]
<pre><code class="python">>>> a = 256</code></pre>
<pre><code class="python">>>> b = 256</code></pre>
<pre><code class="python">>>> a is b</code></pre>
<pre><code class="python">.white[.]</code></pre>
.righthead[CPython Cache]
<pre><code class="bash">&nbsp;</code></pre>
<pre><code class="bash">[ -5 ][ -4 ][...][ 254 ][ 255 ][ .green[256] ]</code></pre>
<pre><code class="bash">.white[.................................]a b</code></pre>
???

Are A and B the same object. Yes!

---
.righthead[Terminal]
`~ $ python`
.righthead[CPython]
<pre><code class="python">>>> a = 256</code></pre>
<pre><code class="python">>>> b = 256</code></pre>
<pre><code class="python">>>> a is b</code></pre>
<pre><code class="python">True</code></pre>
.righthead[CPython Cache]
<pre><code class="bash">&nbsp;</code></pre>
<pre><code class="bash">[ -5 ][ -4 ][...][ 254 ][ 255 ][ .green[256] ]</code></pre>
<pre><code class="bash">.white[.................................]a b</code></pre>
???

Are A and B the same object. Yes!

---
.righthead[Terminal]
`~ $ python`
.righthead[CPython]
<pre><code class="python">>>> .white[a=b]</code></pre>
<pre><code class="python">.white[.]</code></pre>
<pre><code class="python">.white[.]</code></pre>
<pre><code class="python">.white[.]</code></pre>
.righthead[CPython Cache]
<pre><code class="bash">&nbsp;</code></pre>
<pre><code class="bash">[ -5 ][ -4 ][...][ 254 ][ 255 ][ 256 ]</code></pre>
???
But when we use integers outside of our cache, things change

---
.righthead[Terminal]
`~ $ python`
.righthead[CPython]
<pre><code class="python">>>> a = 257</code></pre>
<pre><code class="python">.white[.]</code></pre>
<pre><code class="python">.white[.]</code></pre>
<pre><code class="python">.white[.]</code></pre>
.righthead[CPython Cache]
<pre><code class="bash">&nbsp;</code></pre>
<pre><code class="bash">[ -5 ][ -4 ][...][ 254 ][ 255 ][ 256 ][~][ 257 ]</code></pre>
<pre><code class="bash">.white[............................................]a</code></pre>
???
When we exceed the predeclared array, the value is assigned somewhere else in memory

---
.righthead[Terminal]
`~ $ python`
.righthead[CPython]
<pre><code class="python">>>> a = 257</code></pre>
<pre><code class="python">>>> b = 257</code></pre>
<pre><code class="python">.white[.]</code></pre>
<pre><code class="python">.white[.]</code></pre>
.righthead[CPython Cache]
<pre><code class="bash">&nbsp;</code></pre>
<pre><code class="bash">[ -5 ][ -4 ][...][ 254 ][ 255 ][ 256 ][~][ 257 ][ 257 ]</code></pre>
<pre><code class="bash">.white[............................................]a.white[......]b</code></pre>
???
And when we declare B we also store that as it's own value

---
.righthead[Terminal]
`~ $ python`
.righthead[CPython]
<pre><code class="python">>>> a = 257</code></pre>
<pre><code class="python">>>> b = 257</code></pre>
<pre><code class="python">>>> a is b</code></pre>
<pre><code class="python">.white[.]</code></pre>
.righthead[CPython Cache]
<pre><code class="bash">&nbsp;</code></pre>
<pre><code class="bash">[ -5 ][ -4 ][...][ 254 ][ 255 ][ 256 ][~][ 257 ][ 257 ]</code></pre>
<pre><code class="bash">.white[............................................]a.white[......]b</code></pre>
???
So when we run the check

---
.righthead[Terminal]
`~ $ python`
.righthead[CPython]
<pre><code class="python">>>> a = 257</code></pre>
<pre><code class="python">>>> b = 257</code></pre>
<pre><code class="python">>>> a is b</code></pre>
<pre><code class="python">.white[.]</code></pre>
.righthead[CPython Cache]
<pre><code class="bash">&nbsp;</code></pre>
<pre><code class="bash">[ -5 ][ -4 ][...][ 254 ][ 255 ][ 256 ][~][ .red[257] ][ .red[257] ]</code></pre>
<pre><code class="bash">.white[............................................]a.white[......]b</code></pre>
???
The objects aren't the same

---
.righthead[Terminal]
`~ $ python`
.righthead[CPython]
<pre><code class="python">>>> a = 257</code></pre>
<pre><code class="python">>>> b = 257</code></pre>
<pre><code class="python">>>> a is b</code></pre>
<pre><code class="python">False</code></pre>
.righthead[CPython Cache]
<pre><code class="bash">&nbsp;</code></pre>
<pre><code class="bash">[ -5 ][ -4 ][...][ 254 ][ 255 ][ 256 ][~][ .red[257] ][ .red[257] ]</code></pre>
<pre><code class="bash">.white[............................................]a.white[......]b</code></pre>
???
So the check is false
Even thought he variables have the same value, they aren't the same value, so the identity check fails.

---
.righthead[Terminal]
`~ $ python`
.righthead[CPython]
<pre><code class="python">>>> a = 257; b = 257;</code></pre>
<pre><code class="python">.white[.]</code></pre>
<pre><code class="python">.white[.]</code></pre>
<pre><code class="python">.white[.]</code></pre>
.righthead[CPython Cache]
<pre><code class="bash">&nbsp;</code></pre>
<pre><code class="bash">[ -5 ][ -4 ][...][ 254 ][ 255 ][ 256 ]</code></pre>
???

Here, the one line of code with a semicolon
a quite rare character to see in python code, btw
the interpreter processes this all as one code object

---
.righthead[Terminal]
`~ $ python`
.righthead[CPython]
<pre><code class="python">>>> a = 257; b = 257;</code></pre>
<pre><code class="python">.white[.]</code></pre>
<pre><code class="python">.white[.]</code></pre>
<pre><code class="python">.white[.]</code></pre>
.righthead[CPython Cache]
<pre><code class="bash">&nbsp;</code></pre>
<pre><code class="bash">[ -5 ][ -4 ][...][ 254 ][ 255 ][ 256 ][~][ 257 ]</code></pre>
<pre><code class="bash">.white[...........................................]a b</code></pre>
???

so it's allowed to optimise
and so it only creates one constant

---
.righthead[Terminal]
`~ $ python`
.righthead[CPython]
<pre><code class="python">>>> a = 257; b = 257;</code></pre>
<pre><code class="python">>>> a is b</code></pre>
<pre><code class="python">.white[.]</code></pre>
<pre><code class="python">.white[.]</code></pre>
.righthead[CPython Cache]
<pre><code class="bash">&nbsp;</code></pre>
<pre><code class="bash">[ -5 ][ -4 ][...][ 254 ][ 255 ][ 256 ][~][ 257 ]</code></pre>
<pre><code class="bash">.white[...........................................]a b</code></pre>
???
So when we do our identity check again

---
.righthead[Terminal]
`~ $ python`
.righthead[CPython]
<pre><code class="python">>>> a = 257; b = 257;</code></pre>
<pre><code class="python">>>> a is b</code></pre>
<pre><code class="python">.white[.]</code></pre>
<pre><code class="python">.white[.]</code></pre>
.righthead[CPython Cache]
<pre><code class="bash">&nbsp;</code></pre>
<pre><code class="bash">[ -5 ][ -4 ][...][ 254 ][ 255 ][ 256 ][~][ .green[257] ]</code></pre>
<pre><code class="bash">.white[...........................................]a b</code></pre>
???
The objects are the same

---
.righthead[Terminal]
`~ $ python`
.righthead[CPython]
<pre><code class="python">>>> a = 257; b = 257;</code></pre>
<pre><code class="python">>>> a is b</code></pre>
<pre><code class="python">True</code></pre>
<pre><code class="python">.white[.]</code></pre>
.righthead[CPython Cache]
<pre><code class="bash">&nbsp;</code></pre>
<pre><code class="bash">[ -5 ][ -4 ][...][ 254 ][ 255 ][ 256 ][~][ .green[257] ]</code></pre>
<pre><code class="bash">.white[...........................................]a b</code></pre>
???
So our check succeeds

---
.righthead[CPython]
<pre><code class="python">>>> a = 257</code></pre>
<pre><code class="python">>>> b = 257</code></pre>
<pre><code class="python">>>> a is b</code></pre>
<pre><code class="python">False</code></pre>
???
if what we wanted to do here was an equality check, checking if the values were equal,

---
.righthead[CPython]
<pre><code class="python">>>> a = 257</code></pre>
<pre><code class="python">>>> b = 257</code></pre>
<pre><code class="python">>>> a .green[==] b</code></pre>
<pre><code class="python">True</code></pre>
.fix-tilt[fix]
???
we need to use double equals here instead.

---
class: title
# Python 2
???

TODO(glasnt): Python 2 Intro

---
.righthead[Python 2]
<pre><code class="python">>>> 4 < 2</code></pre>
???

is four less than two. Well, no.
--<pre><code class="python">False</code></pre>
--<pre><code class="python">>>> 4 > 2</code></pre>
???

so 4 is greater than two, right?
--<pre><code class="python">True</code></pre>
???

Yes.
There are no trick questions here.
--<pre><code class="python">>>> 4 > '2'</code></pre>
???

but is four greater than the string 2?
--<pre><code class="python">False</code></pre>
???

no.
--<pre><code class="python">>>> '4' > [2]</code></pre>
???

but what about the string four, is it greater than an array of only 2?
--<pre><code class="python">True</code></pre>
???

yes.
So let's try something here...

---
.righthead[Python 2]
???

let's try and work out if there's some sort of order to this...
--<pre><code class="python">>>> [4] < '4'</code></pre>
--
<pre><code class="python">True</code></pre>
--
<pre><code class="python">>>> 4 < '4'</code></pre>
--
<pre><code class="python">True</code></pre>
--
<pre><code class="python">>>> 4 < [4]</code></pre>
--
<pre><code class="python">True</code></pre>
--
<pre><code class="python">>>> 4 < [4] < '4'</code></pre>
--
<pre><code class="python">True</code></pre>
???
Why is it so? To the Specifications!

---
# .pydocs[Python 2.7.15]
## .pydocs[5.3. Comparisons]
--Objects of different types<sup>1</sup>
never compare equal
.footnotes[[1] except different numeric types and different string types]
???

Okay, this makes sense. In JS we saw that there was implicit casting of types going on. Python doesn't do that. But
--Such objects are ordered consistently but arbitrarily<br>(so that sorting a heterogeneous array yields a consistent result).
???

This also makes sense. Having consistant results is sort of important. But, it doesn't say how they should be ordered. But the docs go on.
--<br>
<br>
**CPython implementation detail**: <br>Objects of different types except numbers are ordered by their type names; [..]
???

Different types of numbers (integers, floats, etc) can be ordered, but otherwise, **(click for highlight)**

---
# .pydocs[Python 2.7.15]
## .pydocs[5.3. Comparisons]
Objects of different types<sup>1</sup>
never compare equal
.footnotes[[1] except different numeric types and different string types]
Such objects are ordered consistently but arbitrarily<br>(so that sorting a heterogeneous array yields a consistent result).
<br>
<br>
**CPython implementation detail**: <br>Objects of different types except numbers .red[are ordered by their type names]; [..]
???

this is specific to cpython, which you're *probably* using.

---
.righthead[Python 2]
<pre><code class="python">>>> 4 < [4] < '4'</code></pre>
<pre><code class="python">True</code></pre>
???

So if we go back to our python2 code, we can see why this statement is true by checking the types of our objects
--<pre><code class="python">>>> type(4); type([4]); type('4')</code></pre>
--
<pre><code class="python">＜type 'int'＞</code></pre>
<pre><code class="python">＜type 'list'＞</code></pre>
<pre><code class="python">＜type 'str'＞</code></pre>
???
int comes before list comes before str, which is the only reason why this works.
.. h **i** j k **l** m n o p q r **S**
--.righthead[Python 3]
<pre><code class="python">>>> 4 < [4] < '4'</code></pre>
???

compare this to the result you get when you try this in python three
--<pre><code class="">TypeError: '＜' not supported between instances of 'int' and 'list'</code></pre>
???
Which is very clearly and error, and it tells you why.
--.pyeol[EOL in -265 weeks]
???

just another reason why you reeeeeallly shouldn't be using Python2
Author note - EOL based on original presentation date.

---
class: title
# All languages have quirks
???
All these things might be first taken to be 'quirks'
But if you have a deep understanding of how a language works
it's not a quirks
it's how the language works

---
class: title
# Perl
???

TODO(glasnt): Perl Intro

---
.righthead[Perl]
<pre><code class="perl">> if ("a" == "b") {</code></pre>
<pre><code class="perl">&nbsp; &nbsp; print "true"</code></pre>
<pre><code class="perl">} else {</code></pre>
<pre><code class="perl">&nbsp; &nbsp; print "false" }</code></pre>
<pre><code class="perl">&nbsp;</code></pre>
--
<pre><code class="perl">true</code></pre>

---
.righthead[Perl]
<pre><code class="perl">> if ("a" .blue[==] "b") { # numeric equality</code></pre>
<pre><code class="perl">&nbsp; &nbsp; print "true"</code></pre>
<pre><code class="perl">} else {</code></pre>
<pre><code class="perl">&nbsp; &nbsp; print "false" }</code></pre>
<pre><code class="perl">&nbsp;</code></pre>
<pre><code class="perl">true</code></pre>

---
.righthead[Perl]
<pre><code class="perl">> if ("a" .green[eq] "b") { # string equality</code></pre>
<pre><code class="perl">&nbsp; &nbsp; print "true"</code></pre>
<pre><code class="perl">} else {</code></pre>
<pre><code class="perl">&nbsp; &nbsp; print "false" }</code></pre>
<pre><code class="perl">&nbsp;</code></pre>
<pre><code class="perl">false</code></pre>
???

note - no perl 6 here, on purpose. outside of scope.

---
class: title
# TODO(glasnt): Python affect.

---
class: title
# Elixir
???

TODO(glasnt): Elixir Intro

---
.righthead[Elixir]
```elixir
iex> Enum.map(1..5, fn(x) -> x*x end)
```
--<pre><code class="elixir">[1, 4, 9, 16, 25]</code></pre>
--
<br>
<pre><code class="elixir">iex> Enum.map(6..10, fn(x) -> x&ast;x end)</code></pre>
--
<pre><code class="elixir">'$1@Qd'</code></pre>

---
.righthead[Elixir]
<pre><code class="elixir">iex> a = Enum.map(6..10, fn(x) -> x*x end)</code></pre>
--
<pre><code class="elixir">iex> Enum.map(a, fn(x) -> IO.puts x end)</code></pre>
--
<pre><code class="elixir">36</code></pre>
<pre><code class="elixir">49</code></pre>
<pre><code class="elixir">64</code></pre>
<pre><code class="elixir">81</code></pre>
<pre><code class="elixir">100</code></pre>
???
If we were to assign our list as a variable
then iterate over each element to print it
we get the list we expected
But why did our first example break and the second one not?
Let's try a different range

---
.righthead[Elixir]
<pre><code class="elixir">iex> Enum.map(65..90, fn(x) -> x end)</code></pre>
???

Let's try say... 65 to 90
No reason
And let's not to anything, just have each element in the range pass through
--<pre><code class="elixir">'ABCDEFGHIJKLMNOPQRSTUVWXYZ'</code></pre>
???
We get a recognisable string.
This is because in ASCII, Capital A starts at sequence 65

---
.righthead[Elixir]
<pre><code class="elixir">iex> Enum.map(65..90, fn(x) -> x end)</code></pre>
<pre><code class="elixir">'ABCDEFGHIJKLMNOPQRSTUVWXYZ'</code></pre>
.fix-tilt[By design]
???

The reason for this:
Elixir was built on top of Erlang, which was created in the 80's, and strings in Erlang are represented as a lists of integers. So, without telling our interpreter any different, it's going to assume that we want to print a string, not a list of numbers
There are flags in erlang to change this, but it's only going to effect our interactive interpreter, not the actual data manipulation

---
class: title
# TODO(glasnt): Python affect.

---
# PowerShell
???

TODO(glasnt): Powershell Intro

---
.righthead[PowerShell]
<br>
<pre><code class="powershell">PS> if (36 > 42) { "true" } else { "false" }</code></pre>
--
<pre><code class="powershell">false</code></pre>
--<br>
<pre><code class="powershell">PS> if (36 < 42) { "true" } else { "false" }</code></pre>
--
<pre><code class="powershell">.ps-error[The '<' operator is reserved for future use.]</code></pre>
???

the problem here is that powershell is a compiler, and an interpreter.
It's a combination compiler and interpreter

---
.righthead[PowerShell]
<br>
<pre><code class="powershell">PS> if (36 .red[>] 42) { "true" } else { "false" }</code></pre>
<pre><code class="">.psg[false] &nbsp;&nbsp; &nbsp; .cc[# file redirection]</code></pre>
<br>
<pre><code class="powershell">PS> if (36 < 42) { "true" } else { "false" }</code></pre>
<pre><code class="powershell">.ps-error[The '<' operator is reserved for future use.]</code></pre>
???

So when you use greater than, it's being interpreted as a file redirection.
--<br>
<pre><code class="powershell">PS> cat 42</code></pre>
--<pre><code class="">36</code></pre>

---
.righthead[PowerShell]
<br>
<pre><code class="powershell">PS> if (36 .red[>] 42) { "true" } else { "false" }</code></pre>
<pre><code class="">.psg[false] &nbsp;&nbsp; &nbsp; .cc[# file redirection]</code></pre>
<br>
<pre><code class="powershell">PS> if (36 .red[<] 42) { "true" } else { "false" }</code></pre>
<pre><code class="powershell">.ps-error[The '<' operator is reserved for future use.]</code></pre>
.fix-tilt[AVOID]
???

You should avoid using greater than, since the complementary less than doesn't exist.

---
.righthead[PowerShell]
<br>
<pre><code class="powershell">PS> if (36 .green[-gt] 42) { "true" } else { "false" }</code></pre>
<pre><code class="powershell">true</code></pre>
<br>
<pre><code class="powershell">PS> if (36 .green[-lt] 42) { "true" } else { "false" }</code></pre>
<pre><code class="powershell">false</code></pre>
.fix-tilt[FIX]
???
It also means you don't hvae to remember which way the crocodile goes

---
&nbsp;
???
INTENTIONALLY BLANK
I've gone through a dozen different programming languages
And shown what could be described in each as a 'wat'
But if you have a deep understanding of how a language works
it's not a wat
it's how the language works

---
class: title
# Turn .wat[wat] into .why[why]
???
When ever you find yourself thinking WAT
turn it into a why
Find out why things are the way they are
Understand the reasoning behind the decision
It will help you get a deeper mastery of the language, and you might just learn something neat along the way

---
class: title
# .inline-img[Learn something ![](images/sparkles.png).new[new]![](images/sparkles.png)]
???
Because these are all examples that I have personally come across. I have been a polyglot developer for *mumble* years now, in every one of these languages, and I use to think
just because I'm a ruby dev, python is terrible
or
I'm doing haskell now, everything that's not functional sucks
But
they're tools
they're tools to manipulate data to solve problems, and each of them has their place
If you are only proficient at Python, that's great. But why not try your hand at something else? You might learn something more and help deeper your understanding of your language of choice along the way

---
class: title
# <br>Thanks!
### References: glasnt.com/wat
![Image](images/footer.svg)
???

thank you for your time
