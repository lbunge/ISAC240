import socket

HOST = '127.0.0.1'
PORT = 65432
privateKey = 5
modulus = 677

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
  s.bind((HOST, PORT))
  s.listen()
  conn, addr = s.accept()
  with conn:
    print('Connected by', addr)
    while True:
      clientPublic = conn.recv(1024)
      if not clientPublic:
        break
      print(clientPublic)
      publicKey = (7  privateKey) % modulus
      conn.sendall(str(publicKey).encode())
      break
    sharedSecret = (int(clientPublic.decode())  privateKey) % modulus
    print('Shared Secret=' + str(sharedSecret))
