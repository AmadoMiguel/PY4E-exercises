from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

# Exercise that consists on following url for 7 times, till the last name is
# found and printed out.
url = 'http://py4e-data.dr-chuck.net/known_by_Kaelum.html'
html = urlopen(url).read()
soup = BeautifulSoup(html,"html.parser")

# Scan for anchor tags
anchs = soup('a')
# General counter
c = 0
while c < 7:
    # Find 18th url.
    anch_18 = str(anchs[17])
    tag_url = (re.findall('<a href="(.\S*)"',anch_18))
    url = tag_url[0]
    print(url)
    # Follow that link and repeat the process.
    html = urlopen(url).read()
    soup = BeautifulSoup(html,"html.parser")
    anchs = soup('a')
    c = c + 1
# Extract the last name. The first letter 'E' was given as a hint.
last_name = re.findall('(E.+).html',url)
print(last_name[0])
