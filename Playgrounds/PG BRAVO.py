#freeCodeCamp working "webscraper"

import urllib.request, urllib.parse, urllib.error

link = "http://data.pr4e.org/words.txt"

fhand = urllib.request.urlopen(link)

for line in fhand:
    print(line.decode().strip())