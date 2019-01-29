from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl
import re

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

#  http://www.dr-chuck.com/page1.htm
url = input('Enter url - ')
# Another way to write the urlopen function, but directly
html = urlopen(url, context=ctx).read()
soup = BeautifulSoup(html,"html.parser")

# Scan for paragraph tags
parags = soup('p')
c = 0 # Prepare to count the paragraphs
for parag in parags:
    c = c + 1
    print(parag)
    # Combining re.findall() and tag.find_all() to print the string
    # representation of the urls.
    print('\nurl(s) in paragraph',c,'are:\n')
    for tag in parag.find_all('a'):
        # First, decode the found anchor tag
        dec_tag = tag.decode()
        # Next, extract the url only (greedy)
        tag_url = re.findall('<a href="(.\S*)"',dec_tag)
        # Finally, print it
        # In case there's more than one
        for url in tag_url:
            # Avoid unwanted newline characters
            url = url.strip()
            print(url)
    print('\n')
