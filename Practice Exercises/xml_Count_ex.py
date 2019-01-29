import urllib.request,urllib.parse,urllib.error
import xml.etree.ElementTree as ET

# Counting comments in a xml file
#  http://py4e-data.dr-chuck.net/comments_174837.xml
url = input('Enter-')
data = urllib.request.urlopen(url).read()
tree = ET.fromstring(data)
com_count = tree.findall('.//count')
c = 0
co = 0
print('Retrieving',url)
for count in com_count:
    co = co + 1
    c = c + int(count.text)
print('Count',co)
print('Sum',c)
