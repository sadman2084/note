import socket
server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind(('127.0.0.1',12345))
server.listen(5)
print("server is listening")
conn,addr=server.accept()
with open('sample.txt','wb') as f:
    while True:
        data=conn.recv(100)
        if not data:
            break
        f.write(data)
        conn.send(b'ACK')

print("file transfer complete")
conn.close()
server.close()