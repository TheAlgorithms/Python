n = int(input())
v = fat = n
for e in range(n - 1):
    v -= 1
    fat = fat * v
print(fat)
