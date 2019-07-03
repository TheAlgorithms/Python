from __future__ import print_function
n = 2**1000
r = 0
while n:
    r, n = r + n % 10, n // 10
print(r)
