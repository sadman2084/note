import socket
server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind(('127.0.0.1',12345))
server.listen(5)

print("TCP Server listening on port 12345...")
conn,addr=server.accept()
print("Connection from:",addr)
try:
    while True:
        data=conn.recv(1024).decode()
        if not data:
            break
        print("Received from client:",data)
        reply=input("Enter reply to send to client: ")
        conn.send(reply.encode())
except KeyboardInterrupt:
    print("Server exiting...")
    conn.close()
    server.close()