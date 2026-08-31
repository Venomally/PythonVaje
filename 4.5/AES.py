from Crypto.PublicKey import RSA
from Crypto.Cipher import AES, PKCS1_OAEP
from Crypto.Random import get_random_bytes
import binascii
from Crypto.PublicKey import RSA
from Crypto.Cipher import AES, PKCS1_OAEP
#---------------------------------------
# #Naloga

# #Generasan je tajni kljuc od 16 bajtova
# kjuc = get_random_bytes(16)

# #Poruka koja se sifruje
# poruka = "nesto"
# #Kreiramo AES objakt u EAX modu
# cipher = AES.new(kjuc, AES.MODE_EAX)
# #sifria poruku i dobija chiphertext i tag
# chiphertext, tag = cipher.encrypt_and_digest(poruka.encode("utf-8"))
# #uzima nonce iz cipher objekta
# nonce = cipher.nonce
# #snima nonce tag i chiphertext u fajl
# with open("tajna.bin", "wb") as fajl:
#     fajl.write(nonce)
#     fajl.write(tag)
#     fajl.write(chiphertext)

# print("Poruka je uspjesno sifrirana i spremljena u fajl:", binascii.hexlify(nonce).decode('utf-8'))

# #otvara fajl za citanje novih binarnih podataka 
# with open("tajna.bin", "rb") as fajl:
#     ucitani_nonce = fajl.read(16)
#     ucitani_tag = fajl.read(16) 
#     ucitani_chiphertext = fajl.read()

# #kreira novi AES objekat za desifriranje
# cipher_dec = AES.new(kjuc, AES.MODE_EAX, ucitani_nonce)
# #desifrira i ujedno i provjerava integritet pomocu taga

# try:
#     originalna_poruka = cipher_dec.decrypt_and_verify(ucitani_chiphertext, ucitani_tag)
#     print("[INFO] Uspješno dešifrirano!")
#     print("Dešifrirana poruka:", originalna_poruka.decode("utf-8"))
# except ValueError:
#     print("[GREŠKA] Podatci su mijenjani ili je ključ pogrešan! Integritet nije potvrđen.")

#--------------------------------------------

# bits= 2048

# #pravi privatni kljuc i cuva ga u fajl
# key = RSA.generate(bits)
# private_key = key.export_key()
# file_out = open("private.pem", "wb")
# file_out.write(private_key)
# file_out.close()

# #Pravi public key iz privatnog kljuca i cuva ga u fajl
# public_key = key.publickey().export_key()
# file_out = open("public.pem", "wb")
# file_out.write(public_key)
# file_out.close()


# data = "Pronasao sam zabranjeni materijal na internetu i zelim da ga podelim sa tobom. Molim te da ga procitas i da mi kazes sta mislis o tome.".encode("utf-8")
# file_out = open("data.txt", "wb")
# #dobivanje javnog kluca iz fajla
# reception_key = RSA.import_key(open("public.pem").read())
# #dobivanje random session kljuca
# session_key = get_random_bytes(16)
# #encrypt session kljuca sa javnim kljucem
# cipher_rsa = PKCS1_OAEP.new(reception_key)


# enc_session_key = cipher_rsa.encrypt(session_key)
# cipher_aes = AES.new(session_key, AES.MODE_EAX)
# ciphertext, tag = cipher_aes.encrypt_and_digest(data)
# for x in (enc_session_key, cipher_aes.nonce, tag, ciphertext):
#     file_out.write(x)
# file_out.close()

# print("Nonce number (hex):", binascii.hexlify(cipher_aes.nonce).decode('utf-8'))


# file_in = open("data.txt", "rb")
# private_key = RSA.import_key(open("private.pem").read())

# enc_session_key, nonce, tag, ciphertext = \
#    [ file_in.read(x) for x in (private_key.size_in_bytes(), 16, 16, -1) ]
# file_in.close()

# cipher_rsa = PKCS1_OAEP.new(private_key)
# session_key = cipher_rsa.decrypt(enc_session_key)

# cipher_aes = AES.new(session_key, AES.MODE_EAX, nonce)
# data = cipher_aes.decrypt_and_verify(ciphertext, tag)
# print(data.decode("utf-8"))


