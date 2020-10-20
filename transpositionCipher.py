import math

def encrypt(message, key):
    # Error Checking
    if key == 1 or key > len(message) / 2:
        return "Invalid key"

    # Initialize the cipher text output to have as many columns as the key
    cipherText = [''] * key

    for column in range(key):
        currentIndex = column

        while currentIndex < len(message):
            cipherText[column] += message[currentIndex]
            currentIndex += key

    return ''.join(cipherText)

def decrypt(message, key):
    numOfColumns = int(math.ceil(len(message) / float(key)))
    numOfRows = key
    numOfShadedBoxes = (numOfColumns * numOfRows) - len(message)
    plaintext = [''] * numOfColumns
    column = 0
    row = 0

    for symbol in message:
        plaintext[column] += symbol
        column += 1

        if (column == numOfColumns) or (column == numOfColumns - 1 and row >= numOfRows - numOfShadedBoxes):
            column = 0
            row += 1

    return ''.join(plaintext)

message = "Having run through different yards and side streets, Pierre got back with his little burden to the Gruzinski garden at the corner of the Povarskoy. He did not at first recognize the place from which he had set out to look for the child, so crowded was it now with people and goods that had been dragged out of the houses. Besides Russian families who had taken refuge here from the fire with their belongings, there were several French soldiers in a variety of clothing. Pierre took no notice of them. He hurried to find the family of that civil servant in order to restore the daughter to her mother and go to save someone else. Pierre felt that he had still much to do and to do quickly. Glowing with the heat and from running, he felt at that moment more strongly than ever the sense of youth, animation, and determination that had come on him when he ran to save the child. She had now become quiet and, clinging with her little hands to Pierre's coat, sat on his arm gazing about her like some little wild animal. He glanced at her occasionally with a slight smile. He fancied he saw something pathetically innocent in that frightened, sickly little face."
key = 156

print(decrypt(encrypt(message, key),key))