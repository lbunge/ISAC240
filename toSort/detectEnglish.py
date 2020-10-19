ALPHABET = 'abcdefghijklmnopqrstuvwxyz'
LETTERS_AND_SPACE = ALPHABET + ALPHABET.upper() + ' \t\n'

# Reads txt file containing dictionary words and returns a dictionary object containing the words {<WORD> : None}
def loadDictionary():
    dictionaryFile = open('dictionary.txt')
    englishWords = {}
    for word in dictionaryFile.read().split('\n'):
        englishWords[word] = None
    dictionaryFile.close()
    return englishWords

# Constant containing the dictionary words
ENGLISH_WORDS = loadDictionary()


# Accepts a message and returns a float result (# of english words / # of possible words)
def getEnglishCount(message):
    message = message.upper()
    message = removeNonLetters(message)
    possibleWords = message.split()

    if possibleWords == []:
        return 0.0  # No words, return float 0

    matches = 0
    for word in possibleWords:
        if word in ENGLISH_WORDS:
            matches += 1
    return float(matches) / len(possibleWords)


# Accepts a message and returns only letters from the alphabet along with spaces, tabs, and new lines
def removeNonLetters(message):
    lettersOnly = []
    for symbol in message:
        if symbol in LETTERS_AND_SPACE:
            lettersOnly.append(symbol)
    return ''.join(lettersOnly)


# Accepts a message and a number criteria for word percentage and letter percentage.
# Returns True if both percentages are true, otherwise false
# By default, 20% of the words must exist in the dictionary file, and
# 85% of all the characters in the message must be letters or spaces
# (not punctuation or numbers).
def isEnglish(message, wordPercentage=20, letterPercentage=85):
   wordsMatch = getEnglishCount(message) * 100 >= wordPercentage
    numLetters = len(removeNonLetters(message))
    messageLettersPercentage = float(numLetters) / len(message) * 100
    lettersMatch = messageLettersPercentage >= letterPercentage
    return wordsMatch and lettersMatch