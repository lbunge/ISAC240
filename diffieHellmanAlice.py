import socket
import caesarCipher
HOST = '127.0.0.1'
PORT = 17777
generator = 2048
modulo = 199
private_key = 145
public_key = pow(generator, private_key, modulo)
meetingTimeMessage = 'Meet me at dawn'

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))     # Connect to server on host:port
    s.sendall(str(public_key).encode())     # Send UTF-8 encoded public key to server

    server_public_key = s.recv(1024).decode()   # Store UTF-8 decoded server public key that was received
    print('Received server public key:', str(server_public_key))    # Print the server's public key

    shared_secret = pow(int(server_public_key), private_key, modulo)    # Generate shared secret from received pub key
    print('Shared secret:', shared_secret)  # Print shared secret

    encryptedMessage = caesarCipher.caesar(meetingTimeMessage, shared_secret, 'e')    # Call cipher to encrypt text to be sent
    s.sendall(str(encryptedMessage).encode())     # Send all the encrypted text to server
