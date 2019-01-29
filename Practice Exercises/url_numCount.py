from urllib.request import urlopen
from bs4 import BeautifulSoup

# This exercises consists in finding all <span> tags and pulling out the numbers
# out of them.
# http://py4e-data.dr-chuck.net/comments_174835.html
url = input('Enter-',)
html = urlopen(url).read()
soup = BeautifulSoup(html,"html.parser")

# First, scan span tags
sp_tgs = soup('span')
# Prepare counters
Sum = 0
Count = 0
# Iterate over the span tags and calculate the total sum
for sp_tg in sp_tgs:
    Count = Count +  1
    Sum = Sum + int(sp_tg.contents[0])
print('Count',Count)
print('Sum',Sum)
