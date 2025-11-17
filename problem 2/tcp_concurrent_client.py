import socket

c = socket.socket()
c.connect(('127.0.0.1',6000))

f = 's.txt'
c.send(f.encode())

if c.recv(1024) == b'OK':
    with open("downloaded_"+f,'wb') as file:
        for chunk in iter(lambda:c.recv(1000), b''): file.write(chunk)
    print("Downloaded:", "downloaded_"+f)
else:
    print("File not found")

c.close()
