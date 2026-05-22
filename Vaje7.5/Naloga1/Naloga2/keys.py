from Crypto.PublicKey import RSA


bits = 2048

key = RSA.generate(bits)
private_key = key.export_key()
file_out = open("private.pem", "wb")
file_out.write(private_key)
file_out.close()


