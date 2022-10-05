import doctest


def find_anagrams(_list: list):
    empty_dict: dict[str, str] = {}
    empty_list = []
    for word in _list:
        check_key = "".join(sorted(word))
        if check_key in empty_dict:
            if empty_dict.get(check_key) != word:
                empty_dict.update(
                    {check_key: empty_dict.get(check_key) + "," + word}
                )
        else:
            empty_dict.update({check_key: word})
    for key, value in empty_dict.items():
        list_word = value.split(",")
        if len(list_word) > 1:
            empty_list.append(list_word)
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
