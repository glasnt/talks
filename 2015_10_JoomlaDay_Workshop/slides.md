# Main Screen Turn On <!-- .slide: class="center" -->
---
# Hack Yourself First <!-- .slide: class="center" -->
---
# Introductions <!-- .slide: class="center" -->
## Hi! <!-- .element: class="fragment" -->
---
# And what about you? <!-- .slide: class="center" -->
## (not your employer)
---
# What's your flavour? <!-- .slide: class="center" -->
## Joomla, presumably. <!-- .element: class="fragment" -->
## Anything else? <!-- .element: class="fragment" -->

Note: Take note of any other stacks, and adlib appropriately.
---
# What the CVE? <!-- .slide: class="center" -->
---
# CVE <!-- .element: style="margin-bottom: 1em" -->
## Common<br>Vulnerabilities and Exploits <!-- .element: class="fragment" -->
## &nbsp;
### Uniquely identified <!-- .element: class="fragment" -->
### <p><code>CVE-YYYY-NNNN</code></p> <!-- .element: class="fragment" -->
### <p><code>CVE-YYYY-NNNNNNN</code></p> <!-- .element: class="fragment" -->
---
# OWASP <!-- .slide: class="center" -->
## Open Web Application<br>Security Project <!-- .element: class="fragment" -->
## https://www.oswap.org <!-- .element: class="fragment" -->

Note: they made the OWASP Top 10
---
## OWASP Top 10
<p align="left">
<span class="n"> Injection</span>
<span class="n"> Broken Authentication and Session Management</span>
<span class="n"> Cross-Site Scripting (XSS)</span>
<span class="n"> Insecure Direct Object References</span>
<span class="n"> Security Misconfiguration</span>
<span class="n"> Sensitive Data Exposure</span>
<span class="n"> Missing Function Level Access Control</span>
<span class="n"> Cross-Site Request Forgery (CSRF)</span>
<span class="n"> Using Components with Known Vulnerabilities</span>
<span class="n"> Unvalidated Redirects and Forwards</span>
</p> 
---
## The Big Three
<p align="left">
<span class="X"> Injection</span>
<span class="n"> Broken Authentication and Session Management</span>
<span class="X"> Cross-Site Scripting (XSS)</span>
<span class="n"> Insecure Direct Object References</span>
<span class="n"> Security Misconfiguration</span>
<span class="n"> Sensitive Data Exposure</span>
<span class="n"> Missing Function Level Access Control</span>
<span class="X"> Cross-Site Request Forgery (CSRF)</span>
<span class="n"> Using Components with Known Vulnerabilities</span>
<span class="n"> Unvalidated Redirects and Forwards</span>
</p> 
---
## Poor Authentication
<p align="left">
<span class="n"> Injection</span>
<span class="X"> Broken Authentication and Session Management</span>
<span class="n"> Cross-Site Scripting (XSS)</span>
<span class="X"> Insecure Direct Object References</span>
<span class="n"> Security Misconfiguration</span>
<span class="n"> Sensitive Data Exposure</span>
<span class="n"> Missing Function Level Access Control</span>
<span class="n"> Cross-Site Request Forgery (CSRF)</span>
<span class="n"> Using Components with Known Vulnerabilities</span>
<span class="X"> Unvalidated Redirects and Forwards</span>
</p> 
---
## Poor Authorisation
<p align="left">
<span class="n"> Injection</span>
<span class="n"> Broken Authentication and Session Management</span>
<span class="n"> Cross-Site Scripting (XSS)</span>
<span class="n"> Insecure Direct Object References</span>
<span class="X"> Security Misconfiguration</span>
<span class="X"> Sensitive Data Exposure</span>
<span class="X"> Missing Function Level Access Control</span>
<span class="n"> Cross-Site Request Forgery (CSRF)</span>
<span class="n"> Using Components with Known Vulnerabilities</span>
<span class="n"> Unvalidated Redirects and Forwards</span>
</p> 
---
## The cause of much sadness
<p align="left">
<span class="n"> Injection</span>
<span class="n"> Broken Authentication and Session Management</span>
<span class="n"> Cross-Site Scripting (XSS)</span>
<span class="n"> Insecure Direct Object References</span>
<span class="n"> Security Misconfiguration</span>
<span class="n"> Sensitive Data Exposure</span>
<span class="n"> Missing Function Level Access Control</span>
<span class="n"> Cross-Site Request Forgery (CSRF)</span>
<span class="X"> Using Components with Known Vulnerabilities</span>
<span class="n"> Unvalidated Redirects and Forwards</span>
</p> 
---
# CVEs -> Patches <!-- .slide: class="center" -->
## Free fixes!
---
# How long has it been since you last patched? <!-- .slide: class="center" -->
---
# In the last 9 months... <!-- .element: style="margin-bottom: 1em" -->
## Content Management System CVEs
#### &nbsp;
### Drupal - 172 <!-- .element: class="fragment" -->
### Wordpress - 107 <!-- .element: class="fragment" -->
### Magento - 7 <!-- .element: class="fragment" -->
### Joomla - 1 <!-- .element: class="fragment" -->
---
# But it's not just<br>your CMS <!-- .slide: class="center" -->
---
# In the last 9 months... <!-- .element: style="margin-bottom: 1em" -->
## Framework CVEs
#### &nbsp;
### Django - 14 <!-- .element: class="fragment" -->
### Ruby on Rails - 5 <!-- .element: class="fragment" -->
### Symfony - 2 <!-- .element: class="fragment" -->
---
# But it's not just<br>your framework <!-- .slide: class="center" -->
---
# In the last 9 months... <!-- .element: style="margin-bottom: 1em" -->
## Language CVEs
#### &nbsp;
### PHP - 133 <!-- .element: class="fragment" -->
### Perl - 6 <!-- .element: class="fragment" -->
### Python - 4 <!-- .element: class="fragment" -->
### Ruby - 2 <!-- .element: class="fragment" -->
---
# But it's not just<br>your language <!-- .slide: class="center" -->
---
# In the last 12 months... <!-- .element: style="margin-bottom: 1em" -->
## Operating System CVEs
#### &nbsp;
### CVE-2014-6271<br>CVE-2015-0204<br>CVE-2015-3456 <!-- .element: class="fragment" -->
---
# CVE-2014-6271 <!-- .element: style="margin-bottom: 1em" -->
 <img src="pictures/ghost.png" />
---
# CVE-2015-0204 <!-- .element: style="margin-bottom: 1em" -->
 <img src="pictures/venom.png" />
---
# CVE-2015-3456 <!-- .element: style="margin-bottom: 1em" -->
 <img src="pictures/shellshock.png" />
---
# Logos bring recognition <!-- .slide: class="center" -->
---
# &nbsp; <!-- .slide: class="center" -->
 <img src="pictures/heartbleed.png" />
---
# But it's not just<br>your application stack <!-- .slide: class="center" -->
---
# CVEs recorded against: <!-- .element: style="margin-bottom: 1em" -->
## &nbsp;
## Nginx
## IIS
## Apache
---
# But it's not just<br>your entire website <!-- .slide: class="center" -->
---
# CVEs recorded against: <!-- .element: style="margin-bottom: 1em" -->
## JIRA
## Request Tracker
## Confluence
## SugarCRM
## &nbsp;
## and many, *many* more...
---
# But wait! That's not all! <!-- .slide: class="center" -->
---
# Responsible Disclosure <!-- .slide: class="center" -->
Note: All these are things we know about.

Doesn't include bad actors
---
# And *that's* assuming you're up to date! <!-- .slide: class="center" -->
---
# Deprecated Language Versions <!-- .slide: class="center" -->
## Are you running unpatched languages?
---
# PHP <!-- .slide: class="center" -->
## What version are you running? <!-- .element: class="fragment" -->
---
# PHP 5.0? <!-- .slide: class="center" -->
## Upgrade. Unmaintained. <!-- .element: class="fragment" -->
---
# PHP 5.1? <!-- .slide: class="center" -->
## Upgrade. Unmaintained. <!-- .element: class="fragment" -->
---
# PHP 5.2? <!-- .slide: class="center" -->
## Upgrade. Unmaintained. <!-- .element: class="fragment" -->
---
# PHP 5.3? <!-- .slide: class="center" -->
## Upgrade. Unmaintained. <!-- .element: class="fragment" -->
---
# PHP 5.4? <!-- .slide: class="center" -->
## Upgrade. Unmaintained. <!-- .element: class="fragment" -->
---
# PHP 5.5? <!-- .slide: class="center" -->
## Keep your patches up to date. <!-- .element: class="fragment" -->
---
# PHP 5.6? <!-- .slide: class="center" -->
## Keep your patches up to date. <!-- .element: class="fragment" -->
---
# PHP 7? <!-- .slide: class="center" -->
## ... <!-- .element: class="fragment" -->
Note: PHP 7.0.0 RC3 2015-09-17. If in production...
---
# So just how much *don't* we patch? <!-- .slide: class="center" -->
## Surely it's not that bad, right? <!-- .element: class="fragment" -->
---
## PHP <span style="color:black">72</span>%
## Python <span style="color:black">72</span>%
## Perl <span style="color:black">18</span>%
## Drupal <span style="color:black">55</span>%
## Wordpress <span style="color:black">40</span>%
---
## PHP 74%
## Python 22%
## Perl 18%
## Drupal 55%
## Wordpress 40%

<footer> 
<small> 
<br> 
<br> 
<br> 
Data from w3techs correlated by known linux distribution numbers<br>
http://blog.ircmaxell.com/2014/12/php-install-statistics.html 
</small> 
</footer> 
---

# But, but, but... <!-- .slide: class="center" -->
---
# "It's too hard!" <!-- .slide: class="center" -->
## "Upgrades are hard!" <!-- .element: class="fragment" -->
## "Patching is boring!" <!-- .element: class="fragment" -->
---

# No, it's not. <!-- .slide: class="center" -->
## It's easier than losing your business. <!-- .element: class="fragment" -->
---

# "That won't<br>happen to me!" <!-- .slide: class="center" -->
---
# Patreon <!-- .slide: class="center" -->
Note: production data on dev website, open to the internet, with a public debugger
---

# David Jones <!-- .slide: class="center" -->
Note: extracted limited information, exploited a vulnerability
---

# KMart <!-- .slide: class="center" -->
Note: extracted limited information, exploited a vulnerability
---
## ... all within in the past 10 days. <!-- .slide: class="center" -->
---
# "I'm not big enough to be a target" <!-- .slide: class="center" -->
---
# You don't have to be <!-- .slide: class="center" -->
Note: automatic attacks, not even targetted ones

Port scanning
Rainbow Tables

---
# So what can you do? <!-- .slide: class="center" -->
---
# Patch. <!-- .slide: class="center" -->
---
# Update. <!-- .slide: class="center" -->
---
# ... and ... <!-- .slide: class="center" -->
---
# Know your enemy. <!-- .slide: class="center" -->
Note: You need to know what your customisations are doing to your system
---
<section data-background="#ffffff"><h1>
<br> 
<br> 
Let's do some hacking.
<h1></section> 
---
<section data-background="#ffffff"><h1>
<br> 
<br> 
Repeat after me...
</h2></section> 
---
<section data-background="#ffffff"><h2>
<br> 
<br> 
<br> 
I (your name here)
<br>do solemnly and sincerely and truly declare and affirm ...
</h2></section> 
---
<section data-background="#ffffff"><h2>
<br> 
<br> 
<br> 
... to use the following knowledge for good and not evil ...
</h2></section> 
---
<section data-background="#ffffff"><h2>
<br> 
<br> 
<br> 
... for learning and not profit.
And agree that if I break my oath I will ...
</h2></section> 
---
<section data-background="#ffffff"><h2>
<br> 
<br> 
<br> 
... rebuild wordpress.com using nothing but Fortran, HTML tables and transparent GIFs.
</h2></section> 

---
<section data-background="#ffffff"><h1>
<br> 
<br> 
Let's do some hacking!
</h1></section> 
---
<section data-background="#ffffff"><h1>
<br><br> 
PLACEHOLDER<br>Wifi Information ETC</h1></section>