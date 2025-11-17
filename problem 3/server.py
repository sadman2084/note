import socket
server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind(('127.0.0.1',6000))
server.listen(5)

while True:
    conn,addr=server.accept()
    data=conn.recv(1024).decode()
    num1,operator,num2=data.split()

    if operator=='+':
        result=int(num1)+int(num2)
    elif operator=='-':
        result=int(num1)-int(num2)

    conn.send(str(result).encode())
    print(result)
    conn.close()
