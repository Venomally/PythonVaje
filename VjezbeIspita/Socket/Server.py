import socketserver

class MyTCPHandler(socketserver.BaseRequestHandler):
    def handle(self):
        print(f"[{self.client_address}] Klijent se spojio. Pocetak primanja"
              "Protokola....."
              )
        #Prima pet bajtova obavjestilo o broju poruka
        raw_n = self.request.recv(5)
        if not raw_n:
            return
        n_messages = int(raw_n.decode().strip())
        print(f"Broj poruka koje klinet salje (N): {n_messages}")

        size = []
        for i in range(n_messages): 
            raw_size = self.request.recv(5)
            msg_size = int(raw_size.decode().strip())
            size.append(msg_size)

        print(f"Velicina poruka koje dolaze: {size}")

        for i in range(n_messages):
            package_size = size[i]
            data = self.request.recv(package_size)
            poruka = data.decode()
            print(f"Primljena poruka #{i+1}: {poruka}")


if __name__ == "__main__":
    HOST, PORT = "127.0.0.1", 1235
    with socketserver.TCPServer((HOST, PORT), MyTCPHandler) as server:
        print(f"Server pokrenut na {HOST}:{PORT}. Ceka klijenta....")
        server.serve_forever()
