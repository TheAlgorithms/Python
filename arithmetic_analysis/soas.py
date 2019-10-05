#python program for sum of arithmetic series

def sum_of_arithmetic(a, d, n):
    sum = 0
    i = 0
    while i < n:
        sum = sum + a 
        i = i + 1
        a = a + d   
    return sum
print(sum_of_arithmetic(1, 3, 10))

