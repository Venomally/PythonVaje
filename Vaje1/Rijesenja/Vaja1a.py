import socket
import sys

HOST,PORT = "127.0.0.1", 1234
msg = "Hello amer"
encoded = msg.encode('utf-8')
decoded = encoded.decode('utf-8')
print(encoded, decoded)
header = len(encoded)
print(header)

with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as sock:
    sock.connect((HOST,PORT))
    sock.sendall(encoded)
    rec = sock.recv(1024).decode()

    print("sent: {}".format(msg))
    print("Received {}".format(rec))
 