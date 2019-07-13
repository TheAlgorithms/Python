"""
this algorithm tries to find the pattern from every position of
the mainString if pattern is found from position i it add it to
the answer and does the same for position i+1

Complexity : O(n*m)
    n=length of main string
    m=length of pattern string
"""


def naivePatternSearch(mainString, pattern):
    patLen = len(pattern)
    strLen = len(mainString)
    position = []
    if patLen > strLen:
        return position
    for i in range(strLen - patLen + 1):
        if mainString[i : i + patLen] == pattern:
            position.append(i)
    return position


mainString = "ABAAABCDBBABCDDEBCABC"
pattern = "ABC"
position = naivePatternSearch(mainString, pattern)
print("Pattern found in position ")
for x in position:
    print(x)

