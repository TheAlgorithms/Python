def fib(n):
    ls = []
    a,b = 0,1
    n += 1
    for i in range(n):
        if (b % 2 == 0):
            ls.append(b)
        else:
            pass
        a,b = b, a+b
    print (sum(ls))
    return None
fib(10)
