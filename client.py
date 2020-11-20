import caesarCipher
import socket

HOST = '127.0.0.1'
PORT = 65432
generator = 127
modulo = 199
private_key = 14
public_key = pow(generator, private_key, modulo)
message = 'This message is encrypted using Caesar cipher.'

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
  s.connect((HOST, PORT))
  s.sendall(str(public_key).encode())
  server_public_key = s.recv(1024).decode()
  print('Received server public key:', str(server_public_key))
  shared_secret = pow(int(server_public_key), private_key, modulo)
  print('Shared secret:', shared_secret)
  cipher = caesarCipher(message, shared_secret, 'd')
  s.sendall(str(cipher).encode())
  s.close()