import os

UPPERLETTERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
LETTERS_AND_SPACE = UPPERLETTERS + UPPERLETTERS.lower() + " \t\n"


def loadDictionary() -> dict:
    path = os.path.split(os.path.realpath(__file__))
    englishWords: dict = {}
    with open(path[0] + "/dictionary.txt") as dictionaryFile:
        for word in dictionaryFile.read().split("\n"):
            englishWords[word] = None
    return englishWords


ENGLISH_WORDS = loadDictionary()


def getEnglishCount(message: str) -> float:
    message = message.upper()
    message = removeNonLetters(message)
    possibleWords = message.split()

    if possibleWords == []:
        return 0.0

    matches = 0
    for word in possibleWords:
        if word in ENGLISH_WORDS:
            matches += 1

    return float(matches) / len(possibleWords)


def removeNonLetters(message: str) -> str:
    lettersOnly = []
    for symbol in message:
        if symbol in LETTERS_AND_SPACE:
            lettersOnly.append(symbol)
    return "".join(lettersOnly)


def isEnglish(message: str, wordPercentage: int =20, letterPercentage: int =85) -> bool:
    """
    >>> isEnglish('Hello World')
    True

    >>> isEnglish('llold HorWd')
    False
    """
    wordsMatch = getEnglishCount(message) * 100 >= wordPercentage
    numLetters = len(removeNonLetters(message))
    messageLettersPercentage = (float(numLetters) / len(message)) * 100
    lettersMatch = messageLettersPercentage >= letterPercentage
    return wordsMatch and lettersMatch


if __name__ == "__main__":
    import doctest

    doctest.testmod()
