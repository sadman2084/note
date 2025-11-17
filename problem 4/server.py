import socket, os, random, time

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(('127.0.0.1', 8000))
print("Streaming Server ready...")

while True:
    data, addr = s.recvfrom(1024)
    f = data.decode()

    if not os.path.exists(f):
        s.sendto(b'ERROR', addr)
        continue

    s.sendto(b'OK', addr)
    time.sleep(0.1)

    with open(f,'rb') as file:
        for chunk in iter(lambda:file.read(random.randint(1000,2000)), b''):
            s.sendto(chunk, addr)
            time.sleep(0.05)

    s.sendto(b'EOF', addr)
