import caesarCipher
import socket

HOST = '127.0.0.1'
PORT = 65432
generator = 127
modulo = 199
private_key = 198
public_key = pow(generator, private_key, modulo)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
  s.bind((HOST, PORT))
  s.listen()
  conn, addr = s.accept()
  print('Connection from:', addr)
  client_public_key = conn.recv(1024)
  print('Received client public key:', int(client_public_key))
  conn.sendall(str(public_key).encode())
  shared_secret = pow(int(client_public_key), private_key, modulo)
  print('Shared secret:', str(shared_secret))
  message = ''
  while True:
    message += str(conn.recv(1024).decode())
    if not conn.recv(1024):
      break
  print('Received cipher text:', message)
  decrypted = caesarCipher(message, shared_secret, 'd')
  print('Decrypted cipher text:', decrypted)
  s.close()