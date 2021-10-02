n=0
def fibonacci(n):
    if n <= 1:
        return n
    else:
        return int(fibonacci(n - 1) + fibonacci(n - 2))

for i in range (2,10):
    print(fibonacci(i))