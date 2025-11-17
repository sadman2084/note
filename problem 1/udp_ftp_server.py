import socket
server=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
server.bind(('127.0.0.1',12345))

conn,addr=server.recvfrom(4096)
filename=conn.decode()+"sadman"

with open(filename,'wb') as f:
    while True:
        conn,addr=server.recvfrom(4096)
        if conn== b"END":
            break
        f.write(conn)
print("file receive complete")
server.close()