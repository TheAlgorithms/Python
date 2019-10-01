def levenshtein(a, b):
    """Levenshtein Distance.

    "...the Levenshtein distance is a string metric for measuring the
        difference between two sequences."
        https://en.wikipedia.org/wiki/Levenshtein_distance

    Example:
    >>> levenshtein("everything", "anything")
    >>> 4
    """

    m = len(a)
    n = len(b)
    s = []

    for x in range(m+1):
        s.append([])
        for y in range(n+1):
            s[x].append(0)

    for i in range(0, m+1):
        s[i][0] = i

    for j in range(0, n+1):
        s[0][j] = j

    for x in range(1, m+1):
        for y in range(1, n+1):
            if a[x - 1] == b[y - 1]:
                cost = 0
            else:
                cost = 1

            s[x][y] = min((s[x-1][y-1] + cost,
                           s[x-1][y] + 1,
                           s[x][y-1] + 1,))

    return s[m][n]
