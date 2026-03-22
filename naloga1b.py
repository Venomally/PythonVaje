import socketserver

class MyTCPHandler(socketserver.BaseRequestHandler):
    """ Handle naj sprejme sporočilo, in sporočilo pošlje nazaj"""
    def handle(self):
        data = self.request.recv(1024).strip()

        response = data.upper()

        self.request.sendall(response.encode("utf-8"))

if __name__ == "__main__":
    HOST, PORT = "127.0.0.1", 1234  
    print("I am here")
    
    # Uporabite socketserver.TCPserver, handler MyTCPHandler, in server.serve_forever()
    with socketserver.TCPServer((HOST, PORT), MyTCPHandler) as server:
        server.serve_forever()
