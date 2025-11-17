import socket
server=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
server.bind(('127.0.0.1',12345))

try:
    while True:
        conn,addr=server.recvfrom(1024)
        print("Connection from:",addr)
        print("Received from client:",conn.decode())
        reply=input("Enter reply to send to client: ")
        server.sendto(reply.encode(),addr)
except KeyboardInterrupt:
    print("Server exiting...")
    server.close()