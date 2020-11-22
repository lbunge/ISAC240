import socket
import caesarCipher
HOST = '127.0.0.1'
PORT = 17778
generator = 2048
modulo = 199
private_key = 123
public_key = pow(generator, private_key, modulo)
meetingTimeMessage = 'Send me the meeting time'

# Server Function
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    # s.close()
    s.bind((HOST, PORT))    # Binding socket to localhost on port
    s.listen()              # Starts listening on bound socket

    conn, addr = s.accept()     # Accept connections and store the address
    print('Connection from', addr)      # Print the Connection to screen

    client_public_key = conn.recv(1024)    # Store the public key up to buffer size 1024
    print('Received client public key:', int(client_public_key))        # Print client pub key to screen

    conn.sendall(str(public_key).encode())      # Send UTF-8 encoded server public key to client
    shared_secret = pow(int(client_public_key), private_key, modulo)    # Generate shared secret
    print('Shared secret=' + str(shared_secret))    # Print shared secret to screen

    message = ''
    while True:
        message += str(conn.recv(1024).decode())    # Decode UTF-8 encoded text received from client and add to message
        if not conn.recv(1024):     # Break connection when no more text is being sent
            break
    print('Received cipher text:', message)     # Print received cipher text message
    decrypted = caesarCipher.caesar(message, shared_secret, 'd')    # Call cipher to decode message with shared secret
    print('Decrypted cipher text:', decrypted)  # Print decrypted text to screen
    s.close()
