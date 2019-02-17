import urllib2
import re
a = raw_input('DWSE URL')
response = urllib2.urlopen(a)
html = response.read()
linechange = len(re.findall("<br>", html)) + len(re.findall("</p>", html))
syndesmoi = len(re.findall("<a href", html))
print("VRETHIKAN ", syndesmoi, "SYNDESMOI KAI ", linechange, "ALLAGES GRAMMIS")
