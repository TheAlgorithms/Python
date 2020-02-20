def mixed_keyword(key="college", pt="UNIVERSITY"):
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
    temp = []
    for i in key:
        if i not in temp:
            temp.append(i)
    l = len(temp)
    # print(temp)
    alpha = []
    modalpha = []
    for i in range(65, 91):
        t = chr(i)
        alpha.append(t)
        if t not in temp:
            temp.append(t)
    # print(temp)
    r = int(26 / 4)
    # print(r)
    k = 0
    for i in range(r):
        t = []
        for j in range(l):
            t.append(temp[k])
            if not (k < 25):
                break
            k += 1
        modalpha.append(t)
    # print(modalpha)
    d = dict()
    j = 0
    k = 0
    for j in range(l):
        for i in modalpha:
            if not (len(i) - 1 >= j):
                break
            d[alpha[k]] = i[j]
            if not k < 25:
                break
            k += 1
    print(d)
    cypher = ""
    for i in pt:
        cypher += d[i]
    return cypher


print(mixed_keyword("college", "UNIVERSITY"))
