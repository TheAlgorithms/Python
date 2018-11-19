def catalan_rec(n):
    if n == 0:
        return 1
    else:
        b = 0
        for i in range (n):
            b += (catalan_rec(i))*(catalan_rec(n-1-i))
    return b
