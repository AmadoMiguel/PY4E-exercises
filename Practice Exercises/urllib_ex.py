import urllib.request,urllib.parse,urllib.error
# Request for the given url using urllib
fhand = urllib.request.urlopen('http://data.pr4e.org')
# Prepare to count the overall number of characters
char = 0
for line in fhand:
    if len(line) < 1:
        print('No more info to show\n')
        break
    # Even more precise
    words = line.split()
    for word in words:
        # Finish condition
        if char >= 3000 or char + len(word) > 3000:
            break
        # Decodes incoming bytes and delets endlines
        print(word.decode())
        # Counts number of displayed characters
        char = char + len(word)
print('\n\nTotal displayed characters:',char)
