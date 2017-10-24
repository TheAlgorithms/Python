import pprint, time

def getWordPattern(word):
    word = word.upper()
    nextNum = 0
    letterNums = {}
    wordPattern = []

    for letter in word:
        if letter not in letterNums:
            letterNums[letter] = str(nextNum)
            nextNum += 1
        wordPattern.append(letterNums[letter])
    return '.'.join(wordPattern)

def main():
    startTime = time.time()
    allPatterns = {}

    with open('Dictionary.txt') as fo:
        wordList = fo.read().split('\n')

    for word in wordList:
        pattern = getWordPattern(word)

        if pattern not in allPatterns:
            allPatterns[pattern] = [word]
        else:
            allPatterns[pattern].append(word)

    with open('Word Patterns.txt', 'w') as fo:
        fo.write(pprint.pformat(allPatterns))

    totalTime = round(time.time() - startTime, 2)
    print('Done! [', totalTime, 'seconds ]')

if __name__ == '__main__':
    main()
