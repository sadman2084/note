import socket
client=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect(('127.0.0.1',12345))
try:
    while True:
        msg=input("Enter the message to send to server: ")
        client.send(msg.encode())

        reply=client.recv(1024).decode()
        if not reply:
            break
        print("Reply from server:",reply)

except KeyboardInterrupt:
    print("Client exiting...")
    client.close()