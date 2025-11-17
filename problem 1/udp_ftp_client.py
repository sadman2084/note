import socket
client=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
server_address=('127.0.0.1',12345)
filename='s.txt'

client.sendto(filename.encode(),server_address)
with open(filename,'rb') as f:
    while True:
        chunk=f.read(100)
        if not chunk:
            break
        client.sendto(chunk,server_address)

client.sendto(b"END",server_address)
print("File transfer complete")
client.close()


