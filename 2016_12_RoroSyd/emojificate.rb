#!/usr/bin/env ruby

require 'gemoji'

def cdn
     "https://twemoji.maxcdn.com/36x36"
end

def emojificate(string)
  string.split("").each do |s|
      e = Emoji.find_by_unicode(s)
      if e then
          u = s.ord.to_s(16)
          d = e.description 
          img = "<img src=\"#{cdn}/#{u}.png\" alt=\"#{s}\" title=\"#{d}\" aria-label=\"Emoji: #{d}\">"
          print img
      else
          print s
      end
  end
end


string = "asdf  💜  sdf"

emojificate(string)
