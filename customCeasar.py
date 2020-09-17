# A custom Caesar cipher who's key is different based on odd/even index (+2 on even)

alphabet = 'abcdefghijklmnopqrstuvwxyz0123456789.$%/!@#'
message = 'j  n332zvp  4p03rzw  zo  4qp  lln3j2  ltysn2  5tuw  wz2  xjvn  4qp  lpj3n2  ltysn2  jy7 3nn32n   zwnn   4qp   j42llvn2   otwo   x52   lkz34   2sn   yn7   ltysn2   33ryp   2n6n21p nyptwpn2ryp lwo l2702lwlu91t1'

# Function takes some message, a key, and whether or not you want to decrypt or encrypt the message
# Key gets 2 added on even index
def ceasar(input, key, mode):
    output = ''
    loop = 1
    for p in input:
        if p == ' ':
            output = output + p
            continue
        pIndex = alphabet.find(p.lower())
        if mode == 'e':
            if loop % 2 == 0:
               cIndex = (pIndex + (key + 2)) % len(alphabet)
            else:
                cIndex = (pIndex + key) % len(alphabet)
        elif mode == 'd':
            if loop % 2 == 0:
                cIndex = (pIndex - (key + 2)) % len(alphabet)
            else:
                cIndex = (pIndex - key) % len(alphabet)
        else:
            print("Please input acceptable mode (e|d)")
        output = output + alphabet[cIndex]
        loop += 1
        
    return output

print(ceasar(message, 9, 'd'))