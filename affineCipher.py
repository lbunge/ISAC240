message = '''''When the mutton and an omelet had been served and a samovar and vodka brought, with some wine which the French had taken from a Russian cellar and brought with them, Ramballe invited Pierre to share his dinner, and himself began to eat greedily and quickly like a healthy and hungry man, munching his food rapidly with his strong teeth, continually smacking his lips, and repeating- "Excellent! Delicious!" His face grew red and was covered with perspiration. Pierre was hungry and shared the dinner with pleasure. Morel, the orderly, brought some hot water in a saucepan and placed a bottle of claret in it. He also brought a bottle of kvass, taken from the kitchen for them to try. That beverage was already known to the French and had been given a special name. They called it limonade de cochon (pig's lemonade), and Morel spoke well of the limonade de cochon he had found in the kitchen. But as the captain had the wine they had taken while passing through Moscow, he left the kvass to Morel and applied himself to the bottle of Bordeaux. He wrapped the bottle up to its neck in a table napkin and poured out wine for himself and for Pierre. The satisfaction of his hunger and the wine rendered the captain still more lively and he chatted incessantly all through dinner'''
abc = 'abcdefghijklmnopqrstuvwxyz'
key1 = 11
key2 = 3

def gcd(a, b):
  while a != 0:
    a, b = b % a, a
  return b

def findModInverse(a, m):
  if gcd(a, m) != 1:
    return None
  u1, u2, u3 = 1, 0, a
  v1, v2, v3 = 0, 1, m
  while v3 != 0:
    q = u3 // v3
    v1, v2, v3, u1, u2, u3 = (u1 - q * v1), (u2 - q * v2), (u3 - q * v3), v1, v2, v3
  return u1 % m

def affine(message, key1, key2, mode):
    output = ''
    if mode == 'e':
        for i in message:
            if i not in abc:
                output += i
                continue
            lindex = abc.find(i.lower())
            cindex = (lindex * key1 + key2) % len(abc)
            if i.isupper():
                output += abc[cindex].upper()
            else:
                output += abc[cindex]
    if mode == 'd':
        for i in message:
            if i not in abc:
                output += i
                continue
            cindex = abc.find(i.lower())
            pindex = ((cindex - key2) * findModInverse(key1, len(abc))) % len(abc)
            if i.isupper():
                output += abc[pindex].upper()
            else:
                output += abc[pindex]

    return output

print(affine(message, key1, key2, 'e'))
#print(affine(ciphertext, key1, key2, 'd'))