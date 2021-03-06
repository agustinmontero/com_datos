import socket

UDP_IP = "192.168.0.4"
UDP_PORT = 13012
BUFFER_SIZE = 512
MESSAGE = 'Hola server!'

sock = socket.socket(socket.AF_INET,  # Internet
                     socket.SOCK_DGRAM)  # UDP
sock.sendto(MESSAGE.encode(), (UDP_IP, UDP_PORT))
data_rec = ''
try:
    data_rec = sock.recvfrom(BUFFER_SIZE)
except KeyboardInterrupt:
    sock.close()
print("Recibi del servidor: ", data_rec[0].decode('utf-8'))
sock.close()
