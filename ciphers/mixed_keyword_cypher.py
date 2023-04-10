import string

"""This function takes two parameters: a string variable named
    'key' (with a default value of 'college') and a string variable
     named 'pt' (with a default value of 'UNIVERSITY').
     The function returns a string that is a transformation of the 'pt' argument
      based on a key-shift cipher"""


def mixed_keyword(key: str = "college", pt: str = "UNIVERSITY") -> str:
    """

    For key:hello

    H E L O
    A B C D
    F G I J
    K M N P
    Q R S T
    U V W X
    Y Z
    and map vertically

    >>> mixed_keyword("college", "UNIVERSITY")  # doctest: +NORMALIZE_WHITESPACE
    {'A': 'C', 'B': 'A', 'C': 'I', 'D': 'P', 'E': 'U', 'F': 'Z', 'G': 'O', 'H': 'B',
     'I': 'J', 'J': 'Q', 'K': 'V', 'L': 'L', 'M': 'D', 'N': 'K', 'O': 'R', 'P': 'W',
     'Q': 'E', 'R': 'F', 'S': 'M', 'T': 'S', 'U': 'X', 'V': 'G', 'W': 'H', 'X': 'N',
     'Y': 'T', 'Z': 'Y'}
    'XKJGUFMJST'
    """
    key = key.upper()
    pt = pt.upper()
    ## changed below lines added sets functionality and remove for loops to get unique elemnt in list
    temp = list(set(key))
    len_temp = len(temp)
    # print(temp)
    # string module can used to generate alphabets list instead of using loops
    alpha = list(string.ascii_uppercase)
    modalpha = []
    for j in alpha:
        if j not in temp:
            temp.append(j)

    # print(temp)
    r = int(26 / 4)
    print(r)
    print(len_temp)
    # for i in range(r*len_temp):
    #     s = [temp[i] for _ in range(len_temp) if i < 26]
    #     modalpha.append(s)

    k = 0
    """These lines of code creates a dictionary by iterating over the list of
    lists. Each letter in the alphabets list is mapped to a letter in a row of
     the "modalpha" list. The mappings are stored in the dictionary with the
     indices of the alphabets list as keys and the values fromthe corresponding modalpha lists as values"""
    for _ in range(r):
        s = []
        for _ in range(len_temp):
            s.append(temp[k])
            if k >= 25:
                break
            k += 1
        modalpha.append(s)
    # print(modalpha)
    d = {}
    j = 0
    k = 0
    for j in range(len_temp):
        for m in modalpha:
            if not len(m) - 1 >= j:
                break
            d[alpha[k]] = m[j]
            if not k < 25:
                break
            k += 1
    print(d)
    cypher = "".join(d[c] for c in pt)
    # cypher = ""
    # for i in pt:
    #     cypher += d[i]
    return cypher


print(mixed_keyword("college", "UNIVERSITY"))
