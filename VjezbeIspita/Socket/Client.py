import socket
import sys

HOST, PORT = "127.0.0.1", 1235
data = "Zivjo"
N = len(data)

# Ustvarimo socket
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
    # Povežemo se
    sock.connect((HOST,PORT))

    # Pošljemo sporočilo
    n_bytes = f"{N:<5}".encode()
    sock.sendall(n_bytes)

    for msg in data:
        size_bytes = f"{len(msg.encode()):<5}".encode()
        sock.sendall(size_bytes)
    for msg in data:
        sock.sendall(msg.encode())


    # Sprejmemo sporočilo
    received = str(sock.recv(1024), "utf-8")

print("Sve poruke su supjesno poslane serveru!")
