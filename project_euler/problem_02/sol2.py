def fib(n):
    """
    Returns a list of all the even terms in the Fibonacci sequence that are less than n.
    """
    ls = []
    a, b = 0, 1
    while b < n:
        if b % 2 == 0:
            ls.append(b)
        a, b = b, a+b
    return ls

if __name__ == '__main__':
    n = int(input("Enter max number: ").strip())
    print(sum(fib(n)))
