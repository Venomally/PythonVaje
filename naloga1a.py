import socket
import sys

HOST, PORT = "127.0.0.1", 1234
data = "Zivjo Amer"
# Ustvarimo socket
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
    # Povežemo se
    sock.connect((HOST, PORT))

    # Pošljemo sporočilo
    sent = sock.send(data.encode())


    # Sprejmemo sporočilo
    received = sock.recv(1024)


print("Sent:  {}".format(sent))
print("Received: {}".format(received))
