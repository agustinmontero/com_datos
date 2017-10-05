import socket

UDP_IP = "192.168.0.4"
UDP_PORT = 13012
BUFFER_SIZE = 512

sock = socket.socket(socket.AF_INET,  # Internet
                     socket.SOCK_DGRAM)  # UDP
sock.bind((UDP_IP, UDP_PORT))

while True:
    try:
        data, addr = sock.recvfrom(BUFFER_SIZE)
        print("received message:", data)
        sock.sendto(data, addr)  # eco
    except (KeyboardInterrupt, OSError):
        print("Finalizando...")
        sock.close()
