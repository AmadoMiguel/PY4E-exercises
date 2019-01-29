# Import the socket library
import socket
# Create the socket object, suitable across the INTERNET
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Data 'Phone Call' (Only Host name)
mysock.connect(('data.pr4e.org', 80))
# Create the request
cmd = 'GET http://data.pr4e.org/intro-short.txt HTTP/1.0\r\n\r\n'.encode()
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
cmd = 'GET http://data.pr4e.org/intro-short.txt HTTP/1.0\r\n\r\n'.encode()
mysock.send(cmd)
while True:
    data = mysock.recv(100)
    if len(data) < 1:
        break
    # Asks for headers ending's index.
    if re.search('\r\n\r\n',data.decode()):
        ind = data.decode().index('\r\n\r\n')
        print(data.decode().strip()[ind:])
        while True:
            data = mysock.recv(100)
            print(data.decode().strip())
            if len(data) < 1:
                break
mysock.close()
