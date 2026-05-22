from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Cipher import PKCS1_OAEP
import binascii
import Crypto.PublicKey.RSA as RSA


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
