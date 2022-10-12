def karatsuba(x, y):
    n = len(x)
    if n < 2:
        return int(x) * int(y)
    else:
        n = n // 2
        al = x[:n]
        ar = x[n:]
        bl = y[:n]
        br = y[n:]
        a = karatsuba(al, bl)
        b = karatsuba(ar, br)
        c = karatsuba(str(int(al) + int(ar)), str(int(bl) + int(br))) - a - b
        prod = (a * (10 ** (n * 2))) + (c * (10**n)) + b
        return prod


num1 = input("Enter the first number: ")
num2 = input("Enter the second number: ")
xlen = len(num1)
ylen = len(num2)
ma = max(len(num1), len(num2))
num1.zfill(ma)
num2.zfill(ma)
result = karatsuba(num1, num2)
print(result)
print(int(num1) * int(num2))
