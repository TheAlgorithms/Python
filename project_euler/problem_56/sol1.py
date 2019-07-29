# https://projecteuler.net/problem=56
high = 0
for a in range(1,100):
    for b in range(1,100):
        c = 0
        for k in list(str(a**b)):
            c += int(k)
        if c > high:
            high = c

print(high)
# 972--answer
