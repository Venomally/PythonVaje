import socketserver

class MyTCPHanlder(socketserver.BaseRequestHandler):
    def handle(self):
        self.data = self.request.recv(1024)
        print(f'Dobili smo:{self.data.decode()} od {self.client_address[0]}')
        msg = "evo nista ktb"
        print(f'Vracamo pozdrav:{msg} na {self.client_address[0]}')
        self.request.sendall(msg.encode('utf-8'))


if __name__ =="__main__":
    HOST,PORT = "127.0.0.1", 1234
    with socketserver.TCPServer((HOST,PORT), MyTCPHanlder) as server:
        server.serve_forever()

