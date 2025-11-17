import socket
client=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect(('127.0.0.1',6000))

num1=str(12)
operator='+'
num2=str(30)
data=f"{num1} {operator} {num2}"
client.send(data.encode())
result=client.recv(1024).decode()
print("result is",result)
client.close()
