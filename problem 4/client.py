import socket

HOST, PORT = '127.0.0.1', 8000
BUFFER_SIZE = 10000

c = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
fname = "video.mp4"
out = f"streaming_{fname}"

c.sendto(fname.encode(), (HOST, PORT))
if c.recvfrom(1024)[0] != b'OK':
    print("File not found"); exit()

print("Streaming started...")
bytes_received = 0
with open(out,'wb') as f:
    while True:
        c.settimeout(2)
        try:
            data, _ = c.recvfrom(2048)
            if data==b'EOF': break
            f.write(data); bytes_received+=len(data)
            print(f"Received: {bytes_received} bytes", end='\r')
        except socket.timeout:
            print("\nStream timeout"); break

print(f"\nFile saved as: {out}")
c.close()
