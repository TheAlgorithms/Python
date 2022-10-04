import doctest


def find_anagrams(_list: list):
    emptyDict = dict()
    emptylist = []
    for word in _list:
        if "".join(sorted(word)) in emptyDict:
            if emptyDict.get("".join(sorted(word))) != word:
                emptyDict.update(
                    {
                        "NA".join(sorted(word)): emptyDict.get("".join(sorted(word)))
                        + ","
                        + word
                    }
                )
        else:
            emptyDict.update({"".join(sorted(word)): word})
    for key, value in emptyDict.items():
        listword = value.split(",")
        if len(listword) > 1:
            emptylist.append(listword)
    return emptylist


if __name__ == "__main__":
    input = [
        "could",
        "cloud",
        "areas",
        "arena",
        "artsy",
        "grips",
        "hello",
        "parts",
        "prigs",
        "strap",
        "traps",
    ]
    doctest.testfile("group_anagram.txt")
    find_anagrams(input)
