# Import the socket library
import socket
# Create the socket object, suitable across the INTERNET
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Data 'Phone Call'
mysock.connect(('data.pr4e.org', 80))
# Create the request
cmd = 'GET http://data.pr4e.org HTTP/1.0\r\n\r\n'.encode()
# Send the request
mysock.send(cmd)
# Receive data iteratively
char = 0
# Avoids printing more than 3000 characters
while char < 3000:
    data = mysock.recv(1000)
    if len(data) < 1 or char + len(data) > 3000:
        break
    print(data.decode(),end='')
    char = char + len(data)
print('\n\nTotal displayed characters:',char)
mysock.close()

# Now, the program will be changed so it only shows data if headers and
# blank lines are received.
import re
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('data.pr4e.org', 80))
cmd = 'GET http://data.pr4e.org HTTP/1.0\r\n\r\n'.encode()
mysock.send(cmd)
while True:
    data = mysock.recv(80)
    if len(data) < 1:
        break
    # Searches for the beginning of a header
    if re.search('<',data.decode()):
        # Stores the header's beginning index
        ind = data.decode().index('<')
        # Searches for an endline in the same received bytes
        if re.search('\n',data.decode()):
            # Stores the index as well and prints the info between found indexes
            ind2 = data.decode().index('\n')
            prnt = data.decode()[ind:ind2]
            print(prnt,'\n')
mysock.close()
