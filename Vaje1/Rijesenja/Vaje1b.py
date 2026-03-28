import socketserver

class MyTCPHandler(socketserver.BaseRequestHandler):
    """ Handle naj sprejme sporočilo, in sporočilo pošlje nazaj"""
    def handle(self):
        self.data = self.request.recv(1024)
        print(f'Dobili smo: {self.data.decode()} od {self.client_address[0]}')
        msg = "Zivjeo amer kako si !"
        print(f'Vračamo pozdrav: {msg} na {self.client_address[0]}')
        self.request.sendall(msg.encode('utf-8'))
        

if __name__ == "__main__":
    HOST, PORT = "127.0.0.1", 1234
    with socketserver.TCPServer((HOST, PORT), MyTCPHandler) as server:
        server.serve_forever()
