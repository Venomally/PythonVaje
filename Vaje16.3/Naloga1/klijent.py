import socket
import sys 

HOST,PORT = "127.0.0.1", 1234
data = "Zdravo "
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
    sock.connect((HOST,PORT))
    sock.sendall(bytes(data + "\n", "utf-8"))

    received = str(sock.recv(1024), "utf-8")


print("sent: {}".format(data))
print("recived:".format(received))

