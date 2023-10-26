# 5 Fibonacci series
n = int(input("Number of terms in Fibonacci series : "))
a, b = 0, 1
count = 0
# check if the number of terms is valid
if n <= 0:
    print("Please enter a positive integer")
elif n == 1:
    print("Fibonacci series upto", n, "terms is :", a)
# generate fibonacci sequence
else:
    print("Fibonacci series upto ", n, " terms is :")
    while count < n:
        print(a, end=" ")
        c = a + b
        a = b
        b = c
        count += 1
