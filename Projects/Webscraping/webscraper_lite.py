#freeCodeCamp working "webscraper"

import urllib.request, urllib.parse, urllib.error

link = "https://genoplivning.dk/humans.txt"

fhand = urllib.request.urlopen(link)

for line in fhand:
    print(line.decode().strip())