# talks

This repo contains all of my talks. 

For a webview, go to [glasnt.com/talks](http://glasnt.com/talks)

## Technical overview

These talks use a few different formats. 

Most recently, they are [Podium](https://github.com/pybee/podium) decks.

For talks not in a `.podium`, they use [reveal.js](http://lab.hakim.se/reveal-js/#/), while some earlier versions use a system called [projection](https://github.com/afcowie/projection), but there are some Keynote and PDFs in there. 

In all circumstances, they should all be visible by clicking on the **Slides** link on [glasnt.com/talks](https://glasnt.com/talks)

The talk listing itself is [jekyll](https://jekyllrb.com/), [myrtle](https://github.com/glasnt/myrtle) theme.

### Running locally

For reveal.js and projection.js: 
   
```
   cd TALK_NAME
   python -m http.server -p 1337
   open http://localhost:1337
```

If you are running Python 2.7 (which you [really shouldn't](https://pythonclock.org/)), run `python -m SimpleHTTPServer 1337` instead. 

Speaker notes can be viewed by pressing `[s]`. I use the notes mostly for reminders, and should not be assumed to be of any use to anyone wanting a general review of the talk. 


## Talk writeups

If you want to get a TLDR on any of my talks, if there is an associated write-up, it'll be linked on the main [talks](http://glasnt.com/talks) page as "Resource".  

