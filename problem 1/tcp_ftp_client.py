import socket
TIMEOUT = 2
client = socket.socket()
client.connect(('127.0.0.1', 5000))
client.settimeout(TIMEOUT)
with open('s.txt', 'rb') as f:
    for chunk in iter(lambda: f.read(100), b''):
        while True:
            try:
                client.send(chunk)
                print(f"Sent {len(chunk)} bytes")
                if client.recv(1024) == b'ACK':
                    print("ACK received")
                    break
            except socket.timeout:
                print("Timeout! Retransmitting...")
print("File transfer complete")
client.close()
