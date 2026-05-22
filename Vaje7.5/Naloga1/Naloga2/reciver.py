from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Cipher import PKCS1_OAEP
import binascii
import Crypto.PublicKey.RSA as RSA

import socketserver

HOST,PORT = "localhost", 1234
data = 'Hello World'.encode('utf-8')
file_out = open("data.txt", "wb")
reciption_key = RSA.import_key(open("receiver.pem").read())
sesion_key = get_random_bytes(16)
cipher_rsa = PKCS1_OAEP.new(reciption_key)
enc_session_key = cipher_rsa.encrypt(sesion_key)
cipher_aes = AES.new(sesion_key, AES.MODE_EAX)
ciphertext, tag = cipher_aes.encrypt_and_digest(data)
[ file_out.write(x) for x in (enc_session_key, cipher_aes.nonce, tag, ciphertext) ]
for x in (enc_session_key, cipher_aes.nonce, tag, ciphertext):
    file_out.write(x)
file_out.close()
print("Data encrypted and saved to data.txt")


class MyTCPHandler(socketserver.BaseRequestHandler):
    """ Handle naj sprejme sporočilo, in sporočilo pošlje nazaj"""
    def handle(self):
        self.data = self.request.recv(1024)
        print(f'Dobili smo: {self.data.decode()} od {self.client_address[0]}')
        msg = "Adijo!"
        print(f'Vračamo pozdrav: {msg} na {self.client_address[0]}')
        self.request.sendall(msg.encode('utf-8'))
        

if __name__ == "__main__":
    HOST, PORT = "0.0.0.0", 1234
    with socketserver.TCPServer((HOST, PORT), MyTCPHandler) as server:
        server.serve_forever()
