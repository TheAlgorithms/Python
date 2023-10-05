def anagram(s1, s2):
    if len(s1) != len(s2):
        return False
    if len(s1) == 1:
        return s1 == s2
    for i in range(len(s1)):
        if s1[i] in s2:
            chars = s2[:s2.index(s1[i])]+s2[s2.index(s1[i])+1:]
            if anagram(s1[:i]+s1[i+1:], chars):
                return True
    return False

st1 = input()
st2=input()
print(anagram(st1,st2))
