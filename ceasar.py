alphabet = 'abcdefghijklmnopqrstuvwxyz0123456789!@#$%/.'

message = 'Xvzcvb x3.2zb 3c v di.z 90 v cewcd3ded398 x3.2zb 9b 7989v6.2vwzd3x x3.2zb g2zbz zfzbi 6zddzb 38 d2z 7zccv1z 3c bz.6vxzy wi c97z 9d2zb 6zddzb 03hzy 8e7wzb 90 .9c3d398c y9g8 d2z v6.2vwzdu D2z 8e7wzb 90 c230d .9c3d398c 3c d2z 5zi'

def ceasar(input, key, mode):
    output = ''
    for p in input:
        if p == ' ':
            output = output + p
            continue
        pIndex = alphabet.find(p.lower())
        if mode == 'e':
            cIndex = (pIndex + key) % len(alphabet)
        elif mode == 'd':
            cIndex = (pIndex - key) % len(alphabet)
        else:
            print("Please input acceptable mode (e|d)")
        output = output + alphabet[cIndex]
        
    return output

print(ceasar(message, 21, 'd'))