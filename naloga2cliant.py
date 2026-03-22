import socket

def napraviHeader(duzina):
    return f"{duzina:<10}".encode()  # 10 bajtova
def posaljiPoruku(sadrzaj1, sadrzaj2):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
         client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(("149.62.71.186", 1235))
