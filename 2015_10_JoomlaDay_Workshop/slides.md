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
# CVE
## Common<br>Vulnerabilities and Exploits <!-- .element: class="fragment" -->
### Uniquely identified <!-- .element: class="fragment" -->
### <p><code>CVE-YYYY-NNNN</code></p> <!-- .element: class="fragment" -->
### <p><code>+NNN</code></p> <!-- .element: class="fragment" -->
Note: up to 10,000 p/a up until last year
Now 7 N's -> 10,000,000

Only when required in a calendar year

Highest CVE number so far == 76xx-ish
---
# OWASP <!-- .slide: class="center" -->
## <p>Open Web Application<br>Security Project<br><a href="https://owasp.org">oswap.org</a></p> <!-- .element: class="fragment" -->

Note: they make the OWASP Top 10
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
<span class="Y"> Broken Authentication and Session Management</span>
<span class="n"> Cross-Site Scripting (XSS)</span>
<span class="Y"> Insecure Direct Object References</span>
<span class="n"> Security Misconfiguration</span>
<span class="n"> Sensitive Data Exposure</span>
<span class="n"> Missing Function Level Access Control</span>
<span class="n"> Cross-Site Request Forgery (CSRF)</span>
<span class="n"> Using Components with Known Vulnerabilities</span>
<span class="Y"> Unvalidated Redirects and Forwards</span>
</p> 
---
## Poor Authorisation
<p align="left">
<span class="n"> Injection</span>
<span class="n"> Broken Authentication and Session Management</span>
<span class="n"> Cross-Site Scripting (XSS)</span>
<span class="n"> Insecure Direct Object References</span>
<span class="Z"> Security Misconfiguration</span>
<span class="Z"> Sensitive Data Exposure</span>
<span class="Z"> Missing Function Level Access Control</span>
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
<span class="C"> Using Components with Known Vulnerabilities</span>
<span class="n"> Unvalidated Redirects and Forwards</span>
</p> 
---
# CVEs -> Patches <!-- .slide: class="center" -->
## Free fixes!


Note: Applying things like Windows Updates is **super important**
---
# How long has it been since you last patched? <!-- .slide: class="center" -->

Note: in the last month?

year? 

... ever?
---
# In the last 9 months...
## Content Management System CVEs
#### &nbsp;
### Wordpress - ~100* <!-- .element: class="fragment" -->
### Drupal - ~100* <!-- .element: class="fragment" -->
### Magento - 7 <!-- .element: class="fragment" -->
### Joomla - 4 <!-- .element: class="fragment" -->

<span class="dasfoot"><a href="https://cve.mitre.org">cve.mitre.org</a></span>
Note: 
Drupal/Wordpress are ESTIMATES

Wordpress probably include splugins, also Wordpress 4 within the last year, so lots of movement

Drupal the same, but they also have had Drupal 8

---
# But it's not just<br>your CMS <!-- .slide: class="center" -->
---
# In the last 9 months...
## Framework CVEs
#### &nbsp;
### Django - 13 <!-- .element: class="fragment" -->
### Ruby on Rails - 5 <!-- .element: class="fragment" -->
### Symfony - 2 <!-- .element: class="fragment" -->
<span class="dasfoot"><a href="https://cve.mitre.org">cve.mitre.org</a></span>
---
# But it's not just<br>your framework <!-- .slide: class="center" -->
---
# In the last 9 months...
## Language CVEs
#### &nbsp;
### Perl - 6 <!-- .element: class="fragment" -->
### Python - 8 <!-- .element: class="fragment" -->
### Ruby - 2 <!-- .element: class="fragment" -->

<span class="dasfoot"><a href="https://cve.mitre.org">cve.mitre.org</a></span>
---

# PHP <!-- .slide: class="center" -->
## ... <!-- .element: class="fragment" -->
---

 <img src="pictures/PHPChart_NoLabels.png" />
---
 <img src="pictures/PHPChart_Labels.png" />
<span class="dasfoot">Full analysis and caveats - <a href="http://www.coelho.net/php_cve.html">coelho.net/php_cve.html</a></span>
Note: Hard to get an exact number for PHP
At one time, research says it was as high as 25% of all vulns

---
# But it's not just<br>your language <!-- .slide: class="center" -->
---
# In the last 12 months...
## Operating System CVEs
#### &nbsp;
### CVE-2014-6271<br>CVE-2015-0204<br>CVE-2015-3456 <!-- .element: class="fragment" -->
---
# CVE-2014-6271
 <img src="pictures/ghost.png"> <!-- .element: class="fragment" -->
Note: GHOST - 27 JAN 2015 -

gethostbyname() buffer overflow - get IPv4 addr by hostname

Surcuri say PHP vuln. because of gethostbyname wrapped in function “wp_http_validate_url()” et a link


---
# CVE-2015-0204
 <img src="pictures/venom.png"> <!-- .element: class="fragment" -->
Note: VENOM May 2015

QEMU Virt floppy drive vuln for escaping encapsulation


---
# CVE-2015-3456
 <img src="pictures/shellshock.png"> <!-- .element: class="fragment" -->

Note: ShellShock - SEP 2014

Bash issue possibly existing since v1.03 Sept 1989

`() { :;};` - environment variable should never be exec, string tricks system

env x='() { :;}; echo vulnerable' bash -c "echo this is a test"


---
# Logos bring recognition <!-- .slide: class="center" -->
---
# &nbsp; <!-- .slide: class="center" -->
 <img src="pictures/heartbleed.png" />

Note: Bufferoverflow on openSSL
---
# But it's not just<br>your application stack <!-- .slide: class="center" -->
---
# CVEs recorded against:
## &nbsp;
## Nginx
## IIS
## Apache
<span class="dasfoot"><a href="https://cve.mitre.org">cve.mitre.org</a></span>
---
# But it's not just<br>your entire website <!-- .slide: class="center" -->
---
# CVEs recorded against:
## JIRA
## Request Tracker
## Confluence
## SugarCRM
## and many, *many* more...
<span class="dasfoot"><a href="https://cve.mitre.org">cve.mitre.org</a></span>
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
# PHP < 5.0? <!-- .slide: class="center" -->
## Go upgrade. Now. <!-- .element: class="fragment" -->
<span class="dasfootc"><a href="http://php.net/eol">https://php.net/eol</a></span>
Note: 4.4 was EOL 2008
---
# PHP 5.0? <!-- .slide: class="center" -->
## Upgrade. Unmaintained. <!-- .element: class="fragment" -->
<span class="dasfootc"><a href="http://php.net/eol">https://php.net/eol</a></span>
Note: EOL 5 Sep 2005 10 years ago
---
# PHP 5.1? <!-- .slide: class="center" -->
## Upgrade. Unmaintained. <!-- .element: class="fragment" -->
<span class="dasfootc"><a href="http://php.net/eol">https://php.net/eol</a></span>
Note: EOL 24 Aug 2006 9 years, 1 month ago
---
# PHP 5.2? <!-- .slide: class="center" -->
## Upgrade. Unmaintained. <!-- .element: class="fragment" -->
<span class="dasfootc"><a href="http://php.net/eol">https://php.net/eol</a></span>
Note: EOL 6 Jan 2011 4 years, 9 months ago
---
# PHP 5.3? <!-- .slide: class="center" -->
## Upgrade. Unmaintained. <!-- .element: class="fragment" -->
<span class="dasfootc"><a href="http://php.net/eol">https://php.net/eol</a></span>
Note: EOL 14 Aug 2014 1 year, 1 month ago
---
# PHP 5.4? <!-- .slide: class="center" -->
## Upgrade. Unmaintained. <!-- .element: class="fragment" -->
<span class="dasfootc"><a href="http://php.net/eol">https://php.net/eol</a></span>
Note: EOL 3 Sep 2015 1 month ago
---
# PHP 5.5? <!-- .slide: class="center" -->
## Keep your patches up to date. <!-- .element: class="fragment" -->
<span class="dasfootc"><a href="http://php.net/eol">https://php.net/eol</a></span>
---
# PHP 5.6? <!-- .slide: class="center" -->
## Keep your patches up to date. <!-- .element: class="fragment" -->
<span class="dasfootc"><a href="http://php.net/eol">https://php.net/eol</a></span>
---
# PHP 7? <!-- .slide: class="center" -->
## ... <!-- .element: class="fragment" -->
<span class="dasfootc"><a href="http://php.net/eol">https://php.net/eol</a></span>
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

<span class="dasfoot">http://blog.ircmaxell.com/2014/12/php-install-statistics.html
</span> 
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
# Wall Street Journal <!-- .slide: class="center" -->
Note: Advisary note sent to customers 2015-10-08
---
# KMart <!-- .slide: class="center" -->
Note: extracted limited information, exploited a vulnerability
---
# David Jones <!-- .slide: class="center" -->
Note: extracted limited information, exploited a vulnerability
---
# Patreon <!-- .slide: class="center" -->
Note: production data on dev website, open to the internet, with a public debugger
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
Wireless: sqlwireless
Password: none
</h1> 
</section> 