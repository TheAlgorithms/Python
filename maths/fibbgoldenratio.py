PHI = 1.6180339

f = [ 0, 1, 1, 2, 3, 5 ]

def fib ( n ):
 

    if n < 6:
        return f[n]
    t = 5
    fn = 5
     
    while t < n:
        fn = round(fn * PHI)
        t+=1
     
    return fn
n = 9
print(n, "th Fibonacci Number =", fib(n))
