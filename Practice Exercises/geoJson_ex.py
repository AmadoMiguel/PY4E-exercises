# This program will prompt for a location, contact a web service and retrieve JSON
# for the web service and parse that data, and retrieve the first place_id from
# the JSON. A place ID is a textual identifier that uniquely identifies a place as
# within Google Maps
import urllib.request, urllib.parse, urllib.error
import json
import ssl
# API endpoint to use: (Uses the same "Address" parameter than the Google API)
service_url = 'http://py4e-data.dr-chuck.net/json?'

while True:
    loc = input('Enter location:')
    if len(loc) < 1: break
    # Append to the endp url, the location specification.
    url = service_url + urllib.parse.urlencode({'address':loc})
    print('Retrieving:',url)
    # Get the handle of the url.
    url_h = urllib.request.urlopen(url)
    # Read and decode the entire information, Probably incoming UTF-8.
    data = url_h.read().decode()
    #print('Retrieved',len(data),'characters')
    print(data)
    try:
        # Returns (if valid data) the dictionary object.
        js = json.loads(data)
    except:
        js = None
