from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

# Exercises that consists on following url for 7 times, till the last name is
# found and printed out.
url = 'http://py4e-data.dr-chuck.net/known_by_Kaelum.html'
html = urlopen(url).read()
soup = BeautifulSoup(html,"html.parser")

# Scan for anchor tags
anchs = soup('a')
c = 0
tag_url = []
while c < 7:
    for anch in anchs:
        tag_url.append(re.findall('<a href="(.\S*)"',anch.decode()))
    # Find the link at position 18
    url = tag_url[18][0]
    # Follow that link and repeat the process.
    html = urlopen(url).read()
    soup = BeautifulSoup(html,"html.parser")
    anchs = soup('a')
    c = c + 1
# Extract the last name. The first letter 'E' was given as a hint.
last_name = re.findall('(E.+).html',url)
print(last_name[0])
