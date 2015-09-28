# Main Screen Turn On <!-- .slide: class="center" -->
---
# Hack the Planet <!-- .slide: class="center" -->
---
# Introductions <!-- .slide: class="center" -->
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
## **C**ommon **V**ulnerabilities and **E**xploits
## Uniquely identified <!-- .element: class="fragment" -->
## <p><code>CVE-YYYY-NNNN</code></p> <!-- .element: class="fragment" -->
## <p><code>CVE-YYYY-NNNNNNN</code></p> <!-- .element: class="fragment" -->
---
# OWASP <!-- .slide: class="center" -->
## **O**pen **W**eb **A**pplication **S**ecurity **P**roject
## https://www.oswap.org
## OWASP Top 10<br>Most common attack vectors for the web <!-- .element: class="fragment" -->
---
## &nbsp;
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
# With CVEs come patches <!-- .slide: class="center" -->
## Free fixes!
---
# How long has it been since you last patched? <!-- .slide: class="center" -->
---
# In the last 9 months... <!-- .element: style="margin-bottom: 1em" -->
## Content Management System CVEs
### Drupal 172
### Wordpress 107
### Magento 7
### Joomla 1 <!-- .element: class="fragment" -->
---
# But it's not just your CMS <!-- .slide: class="center" -->
---
# In the last 9 months... <!-- .element: style="margin-bottom: 1em" -->
## Framework CVEs
### Django 14
### Ruby on Rails 5
### Symfony 2
---
# But it's not just your framework <!-- .slide: class="center" -->
---
# In the last 9 months... <!-- .element: style="margin-bottom: 1em" -->
## Language CVEs
### PHP 133
### Perl 6
### Python 4
### Ruby 2
---
# But it's not just your language <!-- .slide: class="center" -->
---
# In the last 12 months... <!-- .element: style="margin-bottom: 1em" -->
## Operating System CVEs
### CVE-2014-6271
### CVE-2015-0204
### CVE-2015-3456
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
 <img src="pictures/heartbleed.png" />
---
# Don't forget your web servers! <!-- .slide: class="center" -->
---
## CVEs recorded against:
### Nginx
### IIS
### Apache
---
# But it's not just your application stack <!-- .slide: class="center" -->
---
## CVEs recorded against:
### JRA
### Request Tracker
### Confluence
### SugarCRM
### &nbsp;
### and many, *many* more...
---
# But wait! That's not all! <!-- .slide: class="center" -->
---
# Responsible Disclosure <!-- .slide: class="center" -->
---
# And *that's* assuming you're up to date! <!-- .slide: class="center" -->
---
# Deprecated Language Versions <!-- .slide: class="center" -->
## Are you running unpatched languages
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
# So just how much *dont* we patch <!-- .slide: class="center" -->
## Surely it's not that bad, right? <!-- .element: class="fragment" -->
---
# Estimated Insecure Installations <!-- .slide: class="center" -->
## PHP
## Python
## Perl
## &nbsp;
## Drupal
## Wordpress
---
# Estimated Insecure Installations <!-- .slide: class="center" -->
## PHP 74%
## Python 22%
## Perl 18%
## &nbsp;
## Drupal 55%
## Wordpress 40%

### Data from w3techs correlated by known linux distribution numbers
### http://blog.ircmaxell.com/2014/12/php-install-statistics.html

---

# But, but, but... <!-- .slide: class="center" -->
---
# "It's too hard!" <!-- .slide: class="center" -->
## "Upgrades are hard!"
## "Patching is boring!"
---

# No, it's not. <!-- .slide: class="center" -->
## It's easier than losing your business. <!-- .element: class="fragment" -->
---

# "That won't happen to me!" <!-- .slide: class="center" -->
---

## eBay
## Sony
## Apple iCloud
## tinder
## snapchat
## microsoft
## The United States Department of Personnel Management <!-- .element: class="fragment" -->
---
# "I'm not big enough to be a target" <!-- .slide: class="center" -->
---
# You don't have to be. <!-- .slide: class="center" -->
Note: automatic attacks, not even targetted ones
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
---
# Let's do some hacking. <!-- .slide: class="center" -->
---
# Repeat after me... <!-- .slide: class="center" -->
---
# I ______ do solemnly and sincerely and truly declare and affirm... <!-- .slide: class="center" -->
---
# ... to use the following knowledge for good and not evil ... <!-- .slide: class="center" -->
---
# … for learning and not profit. <!-- .slide: class="center" -->

And agree that if I break my oath
I will…

---
# … rebuild wordpress.com using nothing but Fortran, HTML tables and transparent GIFs. <!-- .slide: class="center" -->

---
# Let's do some hacking! <!-- .slide: class="center" -->