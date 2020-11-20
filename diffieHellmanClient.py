import socket

HOST = '127.0.0.1'
PORT = 65432
privateKey = 6
modulus = 677

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
  s.connect((HOST, PORT))
  while True:
    publicKey = (7privateKey) % modulus
    s.sendall(str(publicKey).encode())
    data = s.recv(1024)
    print('Received', data.decode())
    break
  sharedSecret = (int(data.decode())  privateKey) % modulus
  print('Shared Secret=' + str(sharedSecret))