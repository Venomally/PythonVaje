import socket
import sys

# HEADER_LENGTH = 10

# message1 = "Kratko".encode('utf-8')
# message2 = 'Dugooooooooo'.encode('utf-8')


# header1 = f"{len(message1): <{HEADER_LENGTH}}"
# header2 = f"{len(message2)}"

# print(header1,len(header1))
# print(header2, len(header2))

# with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
#     sock.connect(('127.0.0.1', 1235))
#     header1 = f"{len(message1):< {HEADER_LENGTH}}".encode('utf-8')
#     header2 = f"{len(message2):< {HEADER_LENGTH}}".encode('utf-8')

#     sock.sendall(header1+message1+header2+message2)
#     message = sock.recv(1024)
#     print(message.decode())

HEADER_LENGTH = 10

message1 ="Karatko".encode('utf-8')
message2 = "dolgoooooooo".encode('utf-8')
header1 = f"{len(message1):< {HEADER_LENGTH}}"
header2 = f"{len(message2)}"


print(header1,len(header1))
print(header2, len(header2))

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
    sock.connect(('127.0.0.1', 1235))
    header1 = f"{len(message1):< {HEADER_LENGTH}}".encode('utf-8')
    header2 = f"{len(message2):< {HEADER_LENGTH}}".encode("utf-8")

    sock.sendall(header1 + message1 + header2+message2)
    message = sock.recv(1024)
    print(message.decode())

