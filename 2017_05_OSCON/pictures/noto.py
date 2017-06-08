#!/usr/bin/env python

"""
https://github.com/googlei18n/noto-emoji/raw/master/svg/emoji_u1f524.svg
"""
import unicodedata
import sys
import requests


e = sys.argv[1].upper()
print(e)

emoji = ("\N{%s}" % e).decode("unicode_escape") 

print(emoji)

noto = "https://github.com/googlei18n/noto-emoji/raw/master/svg/emoji_u%s.svg" % emoji

print(noto)

