import socket
import caesarCipher
HOST = '127.0.0.1'
server_PORT = 17777
client_PORT = 17778
generator = 2048
modulo = 199
private_key = 28
public_key = pow(generator, private_key, modulo)

#Impersonates Bob and acts as a server for Alice
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as serverSocket:
    ### ESTABLISH CONNECTION WITH ALICE ###
    serverSocket.bind((HOST, server_PORT))
    serverSocket.listen()

    clientConn, addr = serverSocket.accept()
    print('Connection from', addr)

    client_public_key = clientConn.recv(1024)
    print('Received Alice\'s public key:', int(client_public_key))

    clientConn.sendall(str(public_key).encode())
    clientSharedSecret = pow(int(client_public_key), private_key, modulo)
    print('Alice\'s shared secret:', str(clientSharedSecret))

    ### RECEIVE MESSAGE FROM ALICE ###
    clientMessage = ''
    while True:
        clientMessage += str(clientConn.recv(1024).decode())
        if not clientConn.recv(1024):
            break
    print('Received cipher text:', clientMessage)
    serverSocket.close()

### DECRYPT AND MANIPULATE RESPONSE FROM ALICE ###
decryptedClientMessage = caesarCipher.caesar(clientMessage, clientSharedSecret, 'd')
print('Decrypted cipher text:', decryptedClientMessage)
manipulatedMessage = decryptedClientMessage.replace('dawn', 'noon')
print('Manipulated Message:', manipulatedMessage)

# Impersonates Alice and acts as a client for Bob
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as clientSocket:
    ### ESTABLISH CONNECTION WITH BOB ###
    clientSocket.connect((HOST, client_PORT))
    clientSocket.sendall(str(public_key).encode())

    server_public_key = clientSocket.recv(1024).decode()
    print('Received Bob\'s public key:', str(server_public_key))

    serverSharedSecret = pow(int(server_public_key), private_key, modulo)
    print('Bob\'s Shared secret:', serverSharedSecret)

    ### RE-ENCRYPT MANIPULATED MESSAGE AND SEND TO BOB ###
    encryptedClientMessage = caesarCipher.caesar(manipulatedMessage, serverSharedSecret, 'e')
    clientSocket.sendall(str(encryptedClientMessage).encode())
    clientSocket.close()









