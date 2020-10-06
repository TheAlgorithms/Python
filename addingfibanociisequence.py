def fib(n):
    '''
    uses generater to return fibonacci sequence 
    up to given # n dynamically
    '''
    a,b = 1,1

    for _ in range(0,n):
        yield a
        a,b = b,a+b

    return a
