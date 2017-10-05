#!/usr/bin/env python
import socket

SERVER_IP = '192.168.0.4'
SERVER_PORT = 13012
BUFFER_SIZE = 512
MESSGAE = 'Hola server!'

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((SERVER_IP, SERVER_PORT))
sock.send(MESSGAE)
data_recv = ''
try:
    data_recv = sock.recv(BUFFER_SIZE)
except KeyboardInterrupt:
    sock.close()
sock.close()

print("Recibi: ", data_recv)
