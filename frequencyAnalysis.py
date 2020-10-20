import string, re

ALPHABET = 'abcdefghijklmnopqrstuvwxyz'

def getSingleLetterCount(message):
    message = message.translate(message.maketrans('', '', string.punctuation)).replace(' ', '').upper()
    singleLetterCount = {'A': 0, 'B': 0, 'C': 0, 'D': 0, 'E': 0, 'F': 0, 'G': 0, 'H': 0, 'I': 0, 'J': 0, 'K': 0, 'L': 0,
                     'M': 0, 'N': 0, 'O': 0, 'P': 0, 'Q': 0, 'R': 0, 'S': 0, 'T': 0, 'U': 0, 'V': 0, 'W': 0, 'X': 0,
                     'Y': 0, 'Z': 0}

    # Count each letter frequency in message
    for letter in message:
        if letter in singleLetterCount:
            singleLetterCount[letter] += 1

    # Turn count into percentage
    for letter in singleLetterCount:
        singleLetterCount[letter] = singleLetterCount[letter] / len(message) * 100

    return singleLetterCount

def getDoubleLetterCount(message):
    message = message.translate(message.maketrans('', '', string.punctuation)).replace(' ', '').upper()
    doubleLetterCount = {'A': 0, 'B': 0, 'C': 0, 'D': 0, 'E': 0, 'F': 0, 'G': 0, 'H': 0, 'I': 0, 'J': 0, 'K': 0, 'L': 0,
                     'M': 0, 'N': 0, 'O': 0, 'P': 0, 'Q': 0, 'R': 0, 'S': 0, 'T': 0, 'U': 0, 'V': 0, 'W': 0, 'X': 0,
                     'Y': 0, 'Z': 0}

    # Finds all occurrences of double letters in message and stores the single character in a list
    doubleLetters = re.findall(r"(\w)\1+", message)

    # Count each letter frequency from the doubleLetters List
    for letter in doubleLetters:
        if letter in doubleLetterCount:
            doubleLetterCount[letter] += 1

    # Turn count into percentage
    for letter in doubleLetterCount:
        doubleLetterCount[letter] = doubleLetterCount[letter] / len(message) * 100

    return doubleLetterCount

message = '''There were very many of these, as one could easily believe, looking at the officer's handsome, self-satisfied face, and noting the eager enthusiasm with which he spoke of women. Though all Ramballe's love stories had the sensual character which Frenchmen regard as the special charm and poetry of love, yet he told his story with such sincere conviction that he alone had experienced and known all the charm of love and he described women so alluringly that Pierre listened to him with curiosity. It was plain that l'amour which the Frenchman was so fond of was not that low and simple kind that Pierre had once felt for his wife, nor was it the romantic love stimulated by himself that he experienced for Natasha. (Ramballe despised both these kinds of love equally: the one he considered the "love of clodhoppers" and the other the "love of simpletons.") L'amour which the Frenchman worshiped consisted principally in the unnaturalness of his relation to the woman and in a combination of incongruities giving the chief charm to the feeling. Thus the captain touchingly recounted the story of his love for a fascinating marquise of thirty-five and at the same time for a charming, innocent child of seventeen, daughter of the bewitching marquise. The conflict of magnanimity between the mother and the daughter, ending in the mother's sacrificing herself and offering her daughter in marriage to her lover, even now agitated the captain, though it was the memory of a distant past. Then he recounted an episode in which the husband played the part of the lover, and he- the lover- assumed the role of the husband, as well as several droll incidents from his recollections of Germany, where "shelter" is called Unterkunft and where the husbands eat sauerkraut and the young girls are "too blonde." Finally, the latest episode in Poland still fresh in the captain's memory, and which he narrated with rapid gestures and glowing face, was of how he had saved the life of a Pole (in general, the saving of life continually occurred in the captain's stories) and the Pole had entrusted to him his enchanting wife (parisienne de coeur) while himself entering the French service. The captain was happy, the enchanting Polish lady wished to elope with him, but, prompted by magnanimity, the captain restored the wife to the husband, saying as he did so: "I have saved your life, and I save your honor!" Having repeated these words the captain wiped his eyes and gave himself a shake, as if driving away the weakness which assailed him at this touching recollection. Listening to the captain's tales, Pierre- as often happens late in the evening and under the influence of wine- followed all that was told him, understood it all, and at the same time followed a train of personal memories which, he knew not why, suddenly arose in his mind. While listening to these love stories his own love for Natasha unexpectedly rose to his mind, and going over the pictures of that love in his imagination he mentally compared them with Ramballe's tales. Listening to the story of the struggle between love and duty, Pierre saw before his eyes every minutest detail of his last meeting with the object of his love at the Sukharev water tower. At the time of that meeting it had not produced an effect upon him- he had not even once recalled it. But now it seemed to him that that meeting had had in it something very important and poetic. "Peter Kirilovich, come here! We have recognized you," he now seemed to hear the words she had uttered and to see before him her eyes, her smile, her traveling hood, and a stray lock of her hair... and there seemed to him something pathetic and touching in all this. Having finished his tale about the enchanting Polish lady, the captain asked Pierre if he had ever experienced a similar impulse to sacrifice himself for love and a feeling of envy of the legitimate husband. Challenged by this question Pierre raised his head and felt a need to express the thoughts that filled his mind. He began to explain that he understood love for a women somewhat differently. He said that in all his life he had loved and still loved only one woman, and that she could never be his. Pierre then explained that he had loved this woman from his earliest years, but that he had not dared to think of her because she was too young, and because he had been an illegitimate son without a name. Afterwards when he had received a name and wealth he dared not think of her because he loved her too well, placing her far above everything in the world, and especially therefore above himself. Whether it was the wine he had drunk, or an impulse of frankness, or the thought that this man did not, and never would, know any of those who played a part in his story, or whether it was all these things together, something loosened Pierre's tongue. Speaking thickly and with a faraway look in his shining eyes, he told the whole story of his life: his marriage, Natasha's love for his best friend, her betrayal of him, and all his own simple relations with her. Urged on by Ramballe's questions he also told what he had at first concealed- his own position and even his name. More than anything else in Pierre's story the captain was impressed by the fact that Pierre was very rich, had two mansions in Moscow, and that he had abandoned everything and not left the city, but remained there concealing his name and station. When it was late at night they went out together into the street. The night was warm and light. To the left of the house on the Pokrovka a fire glowed- the first of those that were beginning in Moscow. To the right and high up in the sky was the sickle of the waning moon and opposite to it hung that bright comet which was connected in Pierre's heart with his love. At the gate stood Gerasim, the cook, and two Frenchmen. Their laughter and their mutually incomprehensible remarks in two languages could be heard. They were looking at the glow seen in the town.'''
print(getSingleLetterCount(message))