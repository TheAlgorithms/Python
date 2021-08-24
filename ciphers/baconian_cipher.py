"""http://easy-ciphers.com/linkous"""

bacon_alpha = {
    "a": "AAAAA",
    "b": "AAAAB",
    "c": "AAABA",
    "d": "AAABB",
    "e": "AABAA",
    "f": "AABAB",
    "g": "AABBA",
    "h": "AABBB",
    "i": "ABAAA",
    "j": "BBBAA",
    "k": "ABAAB",
    "l": "ABABA",
    "m": "ABABB",
    "n": "ABBAA",
    "o": "ABBAB",
    "p": "ABBBA",
    "q": "ABBBB",
    "r": "BAAAA",
    "s": "BAAAB",
    "t": "BAABA",
    "u": "BAABB",
    "v": "BBBAB",
    "w": "BABAA",
    "x": "BABAB",
    "y": "BABBA",
    "z": "BABBB",
}


def encrypt(word: str) -> str:
    """
    Encrypts the argument

    >>> encrypt("linkous")
    'ABABAABAAAABBAAABAABABBABBAABBBAAAB'
    >>> encrypt("rapidum")
    'BAAAAAAAAAABBBAABAAAAAABBBAABBABABB'
    """
    word = word.lower()
    result = []

    for char in word:
        if char == " ":
            result.append(" ")
        else:
            result.append(bacon_alpha[char])

    return "".join(result)


def decrypt(word: str) -> str:
    result = []
    key_list = list(bacon_alpha.keys())
    value_list = list(bacon_alpha.values())

    word = [word[i : i + 5] for i in range(0, len(word), 5)]

    for i in word:
        if i == " ":
            result.append(" ")
        else:
            idx = value_list.index(i)
            result.append(key_list[idx])

    return "".join(result)