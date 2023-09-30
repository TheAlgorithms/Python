def dictionaryContains(word):
    dictionary = {
        "mobile",
        "samsung",
        "sam",
        "sung",
        "man",
        "mango",
        "icecream",
        "and",
        "go",
        "i",
        "love",
        "ice",
        "cream",
    }
    return word in dictionary


def wordBreak(string):
    wordBreakUtil(string, len(string), "")


def wordBreakUtil(string, n, result):
    for i in range(1, n + 1):
        prefix = string[:i]
        if dictionaryContains(prefix):
            if i == n:
                result += prefix
                print(result)
                return
            wordBreakUtil(string[i:], n - i, result + prefix + " ")


if __name__ == "__main__":
    print("First Test:")
    wordBreak("iloveicecreamandmango")

    print("\nSecond Test:")
    wordBreak("ilovesamsungmobile")
