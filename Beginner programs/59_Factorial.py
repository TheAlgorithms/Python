'''n=5
factorial=1
for i in range(n):
    factorial=factorial * (i+1)

print(factorial)'''

def factorial_iter(n):
    factorial=1
    for i in range(n):
        factorial=factorial * (i+1)
    return factorial

def factorial_recursive(n):
    if(n==1) or (n==0):
        return 1
    else:
        return (n*factorial_recursive(n-1))

f=factorial_iter(5)
print(f)

f=factorial_recursive(4)
print(f)