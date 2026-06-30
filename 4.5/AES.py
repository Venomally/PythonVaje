from Crypto.PublicKey import RSA

bits = 2048

#generate  keys
key = RSA.generate(bits)
#get private key & write it to a .pem file
private_key = key.export_key()
file_out = open("private.pem", "wb")
file_out.write(private_key)
file_out.close()

#get public key & write it to a .pem file
public_key = key.publickey().export_key() 
file_out = open("receiver.pem", "wb")
file_out.write(public_key)
file_out.close()
