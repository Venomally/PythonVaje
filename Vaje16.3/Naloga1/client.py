import socket
import sys

HOST, PORT = "127.0.0.1",1234
msg = 'Sta ima kako si'

encoded = msg.encode('utf-8')
decode = encoded.decode('utf-8')
print(encoded,"\n",decode)
header = len(encoded)
print(header)


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock: 
    sock.connect((HOST,PORT))
    sock.sendall(encoded)
    rec = sock.recv(1024).decode()

print("sent: {}\n".format(msg))
print("Received {}".format(rec))


