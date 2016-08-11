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

    fo = open('Dictionary.txt')
    wordList = fo.read().split('\n')
    fo.close()

    for word in wordList:
        pattern = getWordPattern(word)

        if pattern not in allPatterns:
            allPatterns[pattern] = [word]
        else:
            allPatterns[pattern].append(word)

    fo = open('Word Patterns.txt', 'w')
    fo.write(pprint.pformat(allPatterns))
    fo.close()
    totalTime = round(time.time() - startTime, 2)
    print('Done! [', totalTime, 'seconds ]')

if __name__ == '__main__':
    main()
