message = "This message is encrypted using RSA"
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz "
p = 53
q = 59
n = p*q
phiN = (p-1) * (q-1)
e = 3
d = 2011

def encrypt(e, message):
    output = []
    for i in message:
        m = alphabet.find(i)
        c = (m**e) % n
        output.append(str(c))

    return ' '.join(output)


def decrypt(d, message):
    output = ''
    ciphertext = message.split(' ')
    for c in ciphertext:
        c = int(c)
        m = (c**d) % n
        output += alphabet[m]

    return output

encryptedMessage = encrypt(e, message)
print(encryptedMessage)

decryptedMessage = decrypt(d, encryptedMessage)
print(decryptedMessage)