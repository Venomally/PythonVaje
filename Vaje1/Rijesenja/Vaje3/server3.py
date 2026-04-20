import socket
import select

HEADER_LENGTH = 10

IP = "127.0.0.1"
PORT = 1234

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) # omogoča ponovno uporabo naslova]

server_socket.bind((IP, PORT))

server_socket.listen()

sockets_list = [server_socket]
print(sockets_list)

clients = {}    

def receive_message(client_socket):
    try:
        message_header = client_socket.recv(HEADER_LENGTH)

        if not len(message_header):
            return False
        
        message_length = int(message_header.decode("utf-8").strip())

        return {"header": message_header, "data": client_socket.recv(message_length)}
    except:
        return False

print(f'Listening for connections on {IP}:{PORT}...')
while True:
    read_sockets, _, _ = select.select(sockets_list, [], sockets_list)

    for notification_socket in read_sockets:
        if notification_socket == server_socket:
            client_socket, client_address = server_socket.accept()

            user = receive_message(client_socket)

            if user is False:
                continue

            sockets_list.append(client_socket)

            clients[client_socket] = user

            print(f'New connection from {client_address[0]}:{client_address[1]} username: {user["data"].decode("utf-8")}')
        
        else:
            message = receive_message(notification_socket)

            if message is False:
                print(f'Closed connection from: {clients[notification_socket]["data"].decode("utf-8")}')
                sockets_list.remove(notification_socket)
                del clients[notification_socket]
                continue
            
            user = clients[notification_socket]

            print(f'Received message from {user["data"].decode("utf-8")}: {message["data"].decode("utf-8")}')

            for socket in clients:
                if socket != notification_socket:
                    socket.send(user["header"] + user["data"] + message["header"] + message["data"])
