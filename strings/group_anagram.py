import doctest


def find_anagrams(_list: list):
    emptyDict = {}
    emptylist = []
    for word in _list:
        if "".join(sorted(word)) in emptyDict.keys():
            if emptyDict.get("".join(sorted(word))) == word:
                pass
            else:
                emptyDict.update(
                    {
                        ''.join(sorted(word)): emptyDict.get("".join(sorted(word)))
                        + ","
                        + word
                    }
                )
        else:
            emptyDict.update({''.join(sorted(word)): word})
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
    # doctest.testfile("group_anagram.txt")
    print(find_anagrams(input))
