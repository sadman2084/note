import socket
client=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
server_address=('127.0.0.1',12345)
try:
    while True:
        msg=input("Enter the filename to request from server: ")
        client.sendto(msg.encode(),server_address)

        reply,addr=client.recvfrom(1024)
        print(addr)
        if not reply:
            break
        print("Reply from server:",reply.decode())
except KeyboardInterrupt:
    print("Client exiting...")
    client.close()
