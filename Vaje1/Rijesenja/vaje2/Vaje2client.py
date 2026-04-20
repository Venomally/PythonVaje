import socket

HEADER_SIZE = 10

message1 = 'Hello'.encode('utf-8')
message2 = 'Dolgoooooooooooo'.encode('utf-8')

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
    sock.connect(('localhost', 9999))  # enak naslov in port kot server

    header1 = f"{len(message1):<{HEADER_SIZE}}".encode('utf-8')
    header2 = f"{len(message2):<{HEADER_SIZE}}".encode('utf-8')

    sock.sendall(header1 + message1 + header2 + message2)

    message = sock.recv(1024)
    print(message.decode())
