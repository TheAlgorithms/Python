num = 2**1000
sum = 0
while n:
    sum, num = sum + num % 10, num // 10
print(sum)
