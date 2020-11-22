import caesarCipher
import socket

HOST = '127.0.0.1'    # Local IP
PORT = 65432          # Assigned Port
generator = 1024
modulo = 199
private_key = 67
public_key = pow(generator, private_key, modulo)    # Create public key based off power of generator ^ private % modulo

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
  s.bind((HOST, PORT))        # Create socket to assigned IP and port
  s.listen()                  # Begin listening on socket

  conn, addr = s.accept()     # Assign conn and addr variables when socket is reached
  print('Connection from:', addr)   # Print connected host address

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

  decrypted = caesarCipher.caesar(message, shared_secret, 'd')
  print('Decrypted cipher text:', decrypted)

  s.close()