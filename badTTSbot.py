from playsound import playsound
import time

DICT = {}
PUNCTUATION = "!,.;:?"

def parseDict(file):
    with open(file, encoding="ISO-8859-1") as dictFile:
        for line in dictFile:
            base = line.split("  ")
            english = base[0]
            phonetic = base[1].split()

            DICT[english] = phonetic

def getPhonetics(text):
    phonetics = []
    words = text.split()
    for raw_word in words:
        word = raw_word.upper()
        word_phonetic = []
        if word[-1] in PUNCTUATION:
            word_phonetic.append(word[-1])
            word = word[:-1]
        if word in DICT.keys():
            word_phonetic = DICT[word] + word_phonetic
        elif word[-1] == 's' and word[:-1] + "'s" in DICT.keys():
            word_phonetic = DICT[word[:-1] + "'s"] + word_phonetic
        else:
            letters_phonetic = []
            for letter in word:
                if letter == 'A':
                    letters_phonetic.extend(DICT["A(1)"])
                else:
                    letters_phonetic.extend(DICT[letter])
            word_phonetic = letters_phonetic + word_phonetic
        phonetics.extend(word_phonetic)

    return phonetics

def sayPhonetics(phonetics):
    for phoneme in phonetics:
        if phoneme in PUNCTUATION:
            time.sleep(0.5)
            continue
        elif phoneme[-1] in "012":
            phoneme = phoneme[:-1]
        playsound("audio/{}.wav".format(phoneme))


parseDict("dictionary.txt")
phonetics = getPhonetics(input())
sayPhonetics(phonetics)
