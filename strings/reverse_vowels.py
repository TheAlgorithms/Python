
def reverseVowels( s):
    chars = list(s)
    idx = []
    v = []

    for i in range(len(chars)):
        if chars[i] in ['a','e','i','o','u']:
            v.append(chars[i])
            idx.append(i)

    v = v[::-1]
    final = []

    ind = 0
    for i in range(len(chars)):
        if i in idx:
            final.append(v[ind])
            ind += 1
        else:
            final.append(chars[i])

    str1 = ""
    return str1.join(final)


s=input()
print(reverseVowels(s))