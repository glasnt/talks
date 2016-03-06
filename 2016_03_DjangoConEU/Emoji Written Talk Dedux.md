*Italics are comments. Adlibbing aside, this should be fairly on topic*

*Section: Intro*

*DjangoCon US: *Hi! I’m not a Django Dev but this isn’t my first rodeo -- er, Djangocon. 

I get to use Python in my day job, and that’s pretty cool, but I don’t self-identify as a Python developer

*DevOpsDays Sydney: *Hi!  [http://www.meetup.com/devops-sydney/events/221906379/]

I’m a polyglot programmer. I use *so* many languages in production it’s not funny. I also use a lot of different operating systems, frameworks and platforms. 

(python, ruby, perl, php, shell, web, javascript, haskell, scala… )

So, I’ve seen a lot of stuff in production and in the wild. And all in all, I love emoji. 

I love just how *broken* it is.

Let me explain. I had a poll on twitter where I asked if I should do this entire talk in emoji. There was an overwhelming amount of positive response. But, this talk has no emoji in it. 

I’m running (Apple OSX Yosemite | Ubuntu 14.10 LTS). There’s only so much emoji compatibility on this operating system. Plus, I’m using Chrome, which has less emoji compatibility. My presentation would be full little rectangles

Also, if I used the system native emoji, I couldn’t show you any comparisons between the.. more interesting interpretations of emoji between different platforms. 

Is that a good enough excuse? Good!

So, let’s start with a bit of recap.

## ASCII

Everything in a computer is ones and zeros. A single one or zero is a bit. 8 of these make your typical byte. 

The Americans were really smart. They worked out they could fit a lot of things in just 7 bits.They developed a character standard known as ASCII

A 01000001 65 |  B 01000010 66

etc

And it’s really nice because the lower case ones are

a 01100001 97 | b 01100010 98

All nice and human readable..ish

This is known as the 7-bit ASCII table. Everything an American needed!

This worked perfectly fine, because the English alphabet only has 26 characters, and a few general punctuation marks. But, they had a while 127 characters to play with, that should be fine!

That is until they realised that they needed more. Then we get Extended ASCII - 8 bits to represent a whole 254 characters! should be enough, right?

While the Americans had ASCII, there were many *many* other encodings about the place from countries that aren’t america. And here’s the thing about computers in the 80’s, they started to be networked together. Computers? Talking to each other? Could you even imagine!

And thus the problem: if you want to send a document that’s encoded in ASCII from America to Japanese Industrial Standard where they use a different encoding set? What do you do?

If you send a character, there’s no guarantee that it’ll turn out right at the other end. Without the right encoding, everything gets garbled. 

And so, the unification of encodings was required. And the Unicode Consortium was created. And it was good. 

And a whole lot of character sets were added into Unicode, and there was much rejoicing. Greek, Cyrillic, Armenian Thai, Lao  were in 1.0, and many more characters sets were added later versions, and continue to be added today.

## Encoding of Unicode

TODO UTF-8, 16, 32 encoding summary

A code point, of as many bytes as required

Abstract reference to a code chart

https://www.branah.com/unicode-converter

… 

\u2c22

-> GLAGOLITIC SMALL LETTER SPIDERY HA

![image alt text](image_0.png)

So everyone is having fun with unicode, new character sets are being added from other languages over the years… Until the Japanese members ask: "Can we have emoji in there?"

# Unicode 

Here’s where it gets complicated

There have been pictures in Unicode for a long time. Heck, there has been the ability to use pictures and symbols in fonts for nearly 40 years. The Japanese emoji were only included quite late in the game

So, I’m going to try and create a running timeline. 

US == USA, or Amercias, or Europe (basically, not JP)

JP == Japan

UC == Unicode

US	1978		Zapf Dingbats

UC	1989 - 1991	1.0 Released, incl. Dingbats

US 	1990		Microsoft Wingdings, Windows 3.1

US	1997		Microsoft Webdings, Windows 98

JP	~1998/99	Docomo Kurita Kaomoji

US	~1998/99	Microsoft MSN Messenger, Yahoo Messenger

UC	2000		Proposal to incorporate Docomo -- failed

JP	2006		Japanese Telco Emoji consolidation (w/Google help)

UC	2007		Proposal/Dev for Emoji 

JP	2008		Apple iPhone (JP only) iOS 2.0, Emoji in private space

UC 	2010 		6.0 Released, incl. Emoji

US 	2011		Apple iPhone iOS 5, implementing Unicode 6.0

US	2012		Android Jellybean B/W Unicode 6.0

US	2012		Microsoft Windows 8, B/W Unicode 6.0

US 	2013		Android KitKat Colour Unicode 6.0

US	2013		Microsoft Windows 8.1, Colour Unicode 6.0

UC	2014		7.0 Released, incl Wingdings and Webdings

*Riffs Pending. Will be very stylish and such.*

### Additional Encoding requirements of Emoji

Descriptions, sample picture for reference only. etc.

So for example, \u1F44F is a pair of hands clapping, which is standardised as "CLAPPING HANDS SIGN", and might look a little something like http://www.fileformat.info/info/unicode/char/1f44f/clapping_hands_sign.png, as a suggestion.

## Misinterpretation

There are currently 1624 emoji http://www.latimes.com/business/technology/la-fi-tn-emoji-q-and-a-20160125-htmlstory.html

It’s my belief that a lot of the issues you’re about to see are based on the race to adopt these cool new pictures. Anyone trying to play catchup with Apple had to be fast. And because of this sheer speed.. I think sometimes there’s a bit of … "misinterpretation" of the unicode standard, shall we say. 

### Image misinterprets Reality

Clapping Hands (Microsoft, specifically)

Hugging

Blonde

Hairy Heart (later fixed)

1F5A4 Black Heart

### Images look too similar

Flushed, Pouting, Blushing

Ram vs Sheep

Rat vs Mouse

Ox vs Cow vs Water Buffalo

disappointed-but-relieved-face vs face-with-cold-sweat vs /face-with-open-mouth-and-cold-sweat/

Weary vs Tired vs Sleeping

Grinning vs Grimace

### Cultural Additions

Information Desk, Bowing, No Good, OK

Bowing on Apple looks like a highfive (ref fixes)

Many many MANY Japanese food

### Deprecated

Trackball mouse

Minidisc

Business Card dividers

Fax icon

Floppy Disk x 3 

Tape Cartridge

### Cute ones

Two different camels - One hump or two

SO MANY SPARKLES

### Questionable - Why?

Levitating Business Man - Webdings compatibility

NO PIRACY

### Questionable - Decency

Eggplant

Playboy Bunny

Love Hotel

No over 18

Pile of Poo!

### Missing Emoji

Yak

Spoon

Egg

## How Emoji are Selected

### **_Factors for Inclusion_**

1. [Compatibility](http://www.unicode.org/emoji/selection.html#Selection_Factors_Compatibility).* Are these needed for compatibility with high-use emoji in existing systems, such as Gmail?*

2. [Expected usage level](http://www.unicode.org/emoji/selection.html#Selection_Factors_Usage). *(See questions below)* Measures that can be presented as evidence include the following:

    * Frequency*.*

    * Multiple usages*. *

3. [Image distinctiveness](http://www.unicode.org/emoji/selection.html#Selection_Factors_Distinctive). 

4. [Completeness](http://www.unicode.org/emoji/selection.html#Selection_Factors_Completeness). *Does the proposed pictograph fill a gap in existing types of emoji?*

5. [Frequently requested](http://www.unicode.org/emoji/selection.html#Selection_Factors_Requested). *Is it often requested of the Unicode Consortium, or of Unicode member companies?*

### **_Factors for Exclusion_**

1. [Overly specific](http://www.unicode.org/emoji/selection.html#Specific). *Is the proposed character overly specific?*

2. [Open-ended](http://www.unicode.org/emoji/selection.html#Selection_Factors_Open). *Is it just one of many, with no special reason to favor it over others of that type?*

3. [Already Representable](http://www.unicode.org/emoji/selection.html#Selection_Factors_Representable). *Can the concept be represented by another emoji or sequence?*

4. [Logos, brands, UI icons, signage, specific people, deities](http://www.unicode.org/emoji/selection.html#Selection_Factors_Inappropriate). *Are the images unsuitable for encoding as characters?*

    * Images such as company logos, or those showing company brands as part or all of the image, or images of products strongly associated with a particular brand.

    * UI icons such as [Material Design Icons](https://github.com/google/material-design-icons#material-design-icons), [Winjs Icons](https://github.com/winjs/winjs/tree/master/src/fonts#symbolsttf), or [Font Awesome Icons](https://github.com/FortAwesome/Font-Awesome#font-awesome-v420), which are often discarded or modified to meet evolving UI needs

    * Signage such as See also Slate’s *[The Big Red Word vs. the Little Green Ma*n](http://www.slate.com/articles/life/signs/2010/03/the_big_red_word_vs_the_little_green_man.html)

    * Specific people, whether historic or living

    * Deities

5. [Transient](http://www.unicode.org/emoji/selection.html#Transient).* Is the expected level of usage likely to continue into the future, or would it just be a fad?*

    * Transient or faddish symbols are poor candidates for encoding.

[http://www.unicode.org/emoji/charts/emoji-candidates.html](http://www.unicode.org/emoji/charts/emoji-candidates.html)

### Example Proposal

TODO 

[http://www.unicode.org/L2/L2014/14298-whisky-emoji.pdf](http://www.unicode.org/L2/L2014/14298-whisky-emoji.pdf)

Marketing campain , [https://www.youtube.com/watch?v=84pgoFC-Yrw](https://www.youtube.com/watch?v=84pgoFC-Yrw)

Also, when considering emoji, the ratio of mentions of a new emoji are sometimes related to the ratio of mentions of a hamburger.

A hamburger is now a unit of measurement!

### Edge Case - Corporate Branding Sneaky

Although there’s explicit branding exclusions, it doesn’t stop people from styling things just so

Apple **watch** looks like a watch

apple **headphone** looks like an ipod earbud

**desktop computer** --- iMac

**Personal computer** -- backbook pro

**video Game** in Windows looks like an xbox controller

**mobile phone** - apple == iphone, google == android, microsofts looks like an old numpad one

## Mojibake

New emoji are being added all the time, but the adoption rates across platforms is sparse haphazard.

[http://unicode.org/emoji/charts/emoji-released.html](http://unicode.org/emoji/charts/emoji-released.html)

There’s a term for when you see the diamond and question mark, or a rectangle --- mojibake

diamond and ? == Replacement Character  \uFFFD

Some platforms just have invisible space --- NOT GOOD

some keep the content but rendered into two rows of three as the content -- helpful for working out the base, but not highly readable.

TODO - confirm exactly what the standard says. 

### Emoji Input

So, you have all these characters available, just how can you get at them?

Apple are all in for emoji in their systems.

* they have a keyboard shortcut to show a nice searchable pane of emoji. Command - Control - Space. 

* RKM Addition: This shortcut exists, but strangely, it doesn't work in every app. Twitter OS X, for example (At least, it doesn't work for me)

* You can have usernames or SSIDs as emoji (REF Zac Holman’s article)

As far as I know, for desktop OSs, noone else has any kinda nice input like this.

For mobiles, emoji-enabled keyboards are the key. The smiley face under the enter key takes you to the screen. 

I’ve not seen one with search, but once you get your head around the categorisation, it’s not too hard. I use SwiftKey myself, and their Most Recent and pagination works really well.

… on a web platform level, the implementations greatly vary

FB - there are 20 smiles and one thumbs up hidden away on the web. Messenger has more

Gmail - hidden on the bar. 

* interestingly enough - they enter and look like emoji, and they send as emoji, but while in draft, they actually alt to nonsense characters.

Twitter - three smiles, a party popper, and a love heart are the only entries

### Shortcodes

Hipchat - kicks off when you type openbracket technically not emoji

Github - kicks off when you type colon

Slack - full, with search.

The Slack implementation is kinda awesome: 

* a fully searchable base

* shortcodes (shortcake). meh TODO confirm shortcodes are defacto standard (pretty sure they are)

* but, emoji entered default back into shortcodes. that’s nice. accessible for everyone, the stnadard set of emoji across app, web and mobile

* There is an application that does this for django called [https://github.com/gaqzi/django-emoji](https://github.com/gaqzi/django-emoji). It looks like it implements the Slack model

Personally, I’m not a fan of shortcodes. I mean, yes they have a place, but once you breach the boundary of that particular app, they don’t make sense

I see people all the time using the ‘wrong’ shortcode in different places. e.g. slack/github shortcodes in hipchat

NEW: Slack engineers using codes in Medium posts: https://slack.engineering/distributed-security-alerting-c89414c992d6#.4u9lpew5k
Hipchat codes in Github, Github codes in Hipchat


Also, why is :cake: shortcake? why isn’t it brithdaycake? 

Some platforms take it too far, and try and reverse from emoticons to emoji, but fail

* e.g. :$ for me has always been embarrassed. Google talk likes to make it money-mouth

* or :# which autocorrects in hipchat

* `if (x and y):` get REALLY SAD

You might also know this phenominom from the Microsoft J

## Reading Emoji

Apart from being able to enter your emoji in a nice way, you have to be able to read them back again. 

For Apple or Android, anything you enter can be read back again using the system level emoji ok. 

On the web side, it’s fun...

A lot will just let the system level handle things. Which is fine for earlier versions of emoji that everyone has

Slack, GitHub, Hipchat, the ones that have :shortcodes: parse out, which is nice

But I think Twitter does the best at this:

You can see really clearly if you send a single emoji via a direct message: 

* I paste a codepoint, and it might not look quite right, as it’s rendering as the system emoji on the input form

* once I send it, it gets converted. the actual HTML on the page has the following attributes

* the image is replaced with a twitter platform standard. This is visible to the recipient regardless of the platofrm they’re on, because it’s an image. 

* The alt-text on the image is the codepoint itself. So, you can copy-paste it as you would text, and it copes properly

* It has a title of the description, so if you mouse over it, you get a description!

* And the thing I really like: if you sent emoji via DM, it MAKES THEM BIGGER. THis works if you send between 1 and 10 emoji with no other characters, and it makes them SUPER readable!

* (I believe Facebook also does this now) 

One of the major problems with the Twitter model: it doesn’t map the mobile apps

* if someone sends me an new emoji, it shows on web

* if i open the same message on android, mojibake :(

(insert DS test on OSX 9.2.1 vs Android 5.5.1)

## Accessibility

RKM addition: I presume this is where you're going to hit the "need good eyes to tell the difference between different smiles" point? Color contrast is part of that - can you see a 3 px blue tear on a yellow face?

You may not think this is a problem, but think about Accessibility

* alt text is super important yo

* ARIA is important

* and everyone is learning how to emoji, and having the ablity to mouse over and query is good

*Section: what I’d like*

* Context searchable data entry

* Failover graphic, alt-text the codepoint, title the description
* SVGS FOR THE LOVE OF GOD
So, a combination of the apple/slack search, and twitter failover.

Turns out, this is what the UC also want :D

*TODO - Crib description from the below in a nice flowy way*

## **TR51- - 8 ****[Longer Term Solution**s](http://unicode.org/reports/tr51/#Longer_Term)

The longer-term goal for implementations should be to support embedded graphics, in addition to the emoji characters. Embedded graphics allow arbitrary emoji symbols, and are not dependent on additional Unicode encoding. Some examples of this are found in Skype and LINE—see the [emoji press page](http://unicode.org/press/emoji.html) for more examples.

However, to be as effective and simple to use as emoji characters, a full solution requires significant infrastructure changes to allow simple, reliable input and transport of images (stickers) in texting, chat, mobile phones, email programs, virtual and mobile keyboards, and so on. (Even so, such images will never interchange in environments that only support plain text, such as email addresses.) Until that time, many implementations will need to use Unicode emoji instead.

For example, mobile keyboards need to be enhanced. Enabling embedded graphics would involve adding an additional custom mechanism for users to add in their own graphics or purchase additional sets, such as a sign to add an image to the palette above. This would prompt the user to paste or otherwise select a graphic, and add annotations for dictionary selection.

With such an enhanced mobile keyboard, the user could then select those graphics in the same way as selecting the Unicode emoji. If users started adding many custom graphics, the mobile keyboard might even be enhanced to allow ordering or organization of those graphics so that they can be quickly accessed. The extra graphics would need to be disabled if the target of the mobile keyboard (such as an email header line) would only accept text.

Other features required to make embedded graphics work well include the ability of images to scale with font size, inclusion of embedded images in more transport protocols, switching services and applications to use protocols that do permit inclusion of embedded images (eg, MMS versus SMS for text messages). There will always, however, be places where embedded graphics can’t be used—such as email headers, SMS messages, or file names. There are also privacy aspects to implementations of embedded graphics: if the graphic itself is not packaged with the text, but instead is just a reference to an image on a server, then that server could track usage.

## Emoji Hardware

But of course, the best solution is just to create a keyboard that has *ALL* the emoji

Which has been done, of course.

(tom Scott emoji keyboard)

This was done by a person that also co-created an emoji only network. 

That was a thing that existed. 

Hearing a Q&A they did about the *fun* they had with things like push notifications, postgres databases, cross-platform compiling.. There’s a reason it doesn’t exist anymore

## Emoji Future

### Approved New Glyphs

http://unicode.org/emoji/charts/emoji-released.html

New Western Food~ TODO NEW

### Emoji under consideration

[http://www.unicode.org/emoji/charts/emoji-candidates.html](http://www.unicode.org/emoji/charts/emoji-candidates.html)

Also ongoing work to ensure all the MSN /Yahoo emoticons are linked

[http://www.shervinafshar.name/emoji-drafts/charts/yahoo.html](http://www.shervinafshar.name/emoji-drafts/charts/yahoo.html)

[http://www.unicode.org/L2/L2015/15058-emoji-im-msn.pdf](http://www.unicode.org/L2/L2015/15058-emoji-im-msn.pdf)

[http://www.unicode.org/L2/L2015/15059-emoji-im-yahoo.pdf](http://www.unicode.org/L2/L2015/15059-emoji-im-yahoo.pdf)

[http://www.unicode.org/L2/L2015/15054r4-emoji-tranche5.pdf](http://www.unicode.org/L2/L2015/15054r4-emoji-tranche5.pdf) (compatibility)

FIXING THE BASE EMOJI RECOMMENDED

[http://www.unicode.org/L2/L2015/15141-pri294-emoji-image-background.html](http://www.unicode.org/L2/L2015/15141-pri294-emoji-image-background.html)

Specifically:

	playboy bunny removal

	highfive/bowing change

### Incoming Proposals

Dark Beer (to match light beer) http://www.unicode.org/L2/L2015/15221-cerveza-indio-letter.pdf

### Android 6.0.1

They keep changing thigns!

4.4 ![image alt text](image_1.png)

[http://emojipedia-us.s3.amazonaws.com/cache/9f/11/9f116097f5ab364936ae5683cdec69ff.png](http://emojipedia-us.s3.amazonaws.com/cache/9f/11/9f116097f5ab364936ae5683cdec69ff.png)

5.0 ![image alt text](image_2.png)

[http://emojipedia-us.s3.amazonaws.com/cache/30/86/30860d158ec35c26b3f14a4fcc8637dd.png](http://emojipedia-us.s3.amazonaws.com/cache/30/86/30860d158ec35c26b3f14a4fcc8637dd.png)

http://emojipedia.org/google/android-5.0/nose/

6.0![image alt text](image_3.png)

http://emojipedia.org/google/android-6.0.1/nose/

MORE http://blog.emojipedia.org/android-6-0-1-emoji-changelog/

The android poo emoji is getting eyes [http://emojipedia.org/google/android-6.0.1/pile-of-poo/](http://emojipedia.org/google/android-6.0.1/pile-of-poo/)

[https://en.wikipedia.org/wiki/Android_version_history#/media/File:Android_historical_version_distribution_-_vector.svg](https://en.wikipedia.org/wiki/Android_version_history#/media/File:Android_historical_version_distribution_-_vector.svg)

The versions of android mean there’s many people using the old versions

### Advanced Features

#### Fitzpatrick Modifier

TODO

#### Zero Width Character

For groupings

Technical issues [http://www.unicode.org/L2/L2015/15319-emoji-zwj-seq-harmful.pdf](http://www.unicode.org/L2/L2015/15319-emoji-zwj-seq-harmful.pdf)

Social issues http://time.com/4218922/indonesia-facebook-whatsapp-gay-lgbt-emoji-stickers/

#### Better Gender fixing

http://www.unicode.org/review/pri321/

Underpublic review
http://blog.emojipedia.org/custom-emoji-a-summary/

## TLDR

Use emoji with caution

Implement better accessibility and access

Have a bit of fun! 

## MORE RESOURCE

[http://www.unicode.org/versions/Unicode8.0.0/UnicodeStandard-8.0.pdf](http://www.unicode.org/versions/Unicode8.0.0/UnicodeStandard-8.0.pdf)

