a = "123"
n = len(a)
length = 1 << n
hey = []
for i in range(1, length+1):
    b = ""
    for j in range(n):
        if i & (1 << j):
            b += a[j]
    hey.append(b)
print(hey)
