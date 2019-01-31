import urllib.request
import json
# This exercise consists in counting comments inside a json file, by parsing
# and iterating over it.

# http://py4e-data.dr-chuck.net/comments_174838.json
url = input('Enter location:')
print('Retrieving',url)
# Read the whole file
url_han = urllib.request.urlopen(url).read()
print('Retrieved',len(url_han),'characters')
# Get the dictionary
data = json.loads(url_han)

# Iterate over the 'comments' key and get the total counts of comments.
c = 0
Sum = 0
for com in data['comments']:
    c = c + 1
    # Convert to int the string number inside the 'count' key.
    Sum = Sum + int(com['count'])
print('Count:',c)
print('Sum:',Sum)
