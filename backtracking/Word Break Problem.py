def dictionarycontains(word):
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


def wordbreak(string):
    wordbreakutil(string, len(string), "")


def wordbreakutil(string, n, result):
    for i in range(1, n + 1):
        prefix = string[:i]
        if dictionarycontains(prefix):
            if i == n:
                result += prefix
                print(result)
                return
            wordbreakutil(string[i:], n - i, result + prefix + " ")


if __name__ == "__main__":
    print("First Test:")
    wordbreak("iloveicecreamandmango")

    print("\nSecond Test:")
    wordbreak("ilovesamsungmobile")
