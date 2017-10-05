#!/usr/bin/env python

import socket

TCP_IP = '192.168.0.4'
TCP_PORT = 13012
BUFFER_SIZE = 512

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((TCP_IP, TCP_PORT))
s.listen(1)

conn, addr = s.accept()
print('Connection address:', addr)
while True:
    try:
        data = conn.recv(BUFFER_SIZE)
        if not data:
            break
        print("received data:", data)
        conn.send(data)  # echo
    except (KeyboardInterrupt, OSError):
        conn.close()
conn.close()
