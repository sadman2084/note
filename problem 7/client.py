import socket, struct, threading

GROUP = '224.1.1.1'
PORT = 5007

def recv_msg(sock):
    while True:
        try:
            data, addr = sock.recvfrom(1024)
            # print(f"\n[{addr[0]}] {data.decode()}\nYou: ", end='')
        except:
            break

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
sock.bind(('', PORT))

mreq = struct.pack("4sl", socket.inet_aton(GROUP), socket.INADDR_ANY)
sock.setsockopt(socket.IPPROTO_IP, socket.IP_ADD_MEMBERSHIP, mreq)

threading.Thread(target=recv_msg, args=(sock,), daemon=True).start()

print(f"Multicast Chat on {GROUP}:{PORT}\n")

try:
    while True:
        msg = input("You: ")
        sock.sendto(msg.encode(), (GROUP, PORT))
except KeyboardInterrupt:
    print("\nChat Closed")

sock.close()
