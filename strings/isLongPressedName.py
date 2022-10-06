def isLongPressedName(name: str, typed: str):
        i, j, m, n = 0, 0, len(name), len(typed)
        if n < m: return False
        while i < m and j < n:
            if name[i] == typed[j]:
                i += 1
                j += 1
            elif j == 0 or typed[j] != typed[j - 1]: return False
            else:
                j += 1
        return i == m and typed[j:] == typed[j - 1] * (n - j)

str="sourav"
str1="sssouravvvvv"
ans=isLongPressedName(str,str1)
print(ans)
