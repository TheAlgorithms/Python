import doctest


def find_anagrams(_list: list):
    empty_dict = {}  # Python names variables using snake_case.
    empty_list = []
    for word in _list:
        if "".join(sorted(word)) in empty_dict:
            if empty_dict.get("".join(sorted(word))) != word:
                empty_dict.update(
                    {
                        "".join(sorted(word)): empty_dict.get("".join(sorted(word)))
                        + ","
                        + word
                    }
                )
        else:
            empty_dict.update({"".join(sorted(word)): word})
    for key, value in empty_dict.items():
        listword = value.split(",")
        if len(listword) > 1:
            empty_list.append(listword)
    return empty_list


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
