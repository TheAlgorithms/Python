def fib(n):
    a, b, s = 0, 1, 0
    while b < n:
        if b % 2 == 0 and b < n: s += b
        a, b = b, a+b
    ls.append(s)

T = int(input().strip())
ls = []
for _ in range(T):
    fib(int(input().strip()))
print(*ls, sep = '\n')
