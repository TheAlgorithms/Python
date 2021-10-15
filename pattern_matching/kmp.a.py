"""
KMP - Knuth Morris Pratt Algorithm
It helps to find a given string inside a big string. Or maximum similarities in between 2 different string.
The time complexity of KMP algorithm is O(n) in the worst case.

pat -> the string we are finding
text ->where we are trying to find the pat string
F -> Failure Function
"""

# find the Failure Function of in a string with respect to itself


def failfunc(s) -> None:
    F = [0 for _ in s]
    i, j = 1, 0
    while i < len(s):
        if s[i] == s[j]:
            j += 1
            F[i] = j
            i += 1
        else:
            if j == 0:
                F[i], i = 0, i+1
            else:
                j = F[j-1]
    return F

# Find the position of the string


def find(F, txt, patt) -> str:
    i, j = 0, 0
    while i < len(txt):
        if txt[i] == patt[j]:
            i, j = i+1, j+1
        if j == len(patt):
            return i-len(patt)
        elif i < len(txt) and txt[i] != patt[j]:
            if j == 0:
                i += 1
            else:
                j = F[j-1]
    return None


pat, text = 'lkdma', 'asdlkaslkdmaklsndknsadasnd'
F = failfunc(pat)
print(find(F, text, pat))
