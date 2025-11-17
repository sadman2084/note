import socket,threading,os
def handle(conn):
    f=conn.recv(1024).decode()
    if os.path.exists(f):
        conn.send(b"OK")
        with open(f,"rb") as file:
            for chunk in iter(lambda:file.read(1000),b""):conn.send(chunk)
    else:
        conn.send(b"ERROR")
    conn.close()
server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind(('127.0.0.1',6000))
server.listen(5)
while True:
    conn,addr=server.accept()
    threading.Thread(target=handle,args=(conn,)).start()


