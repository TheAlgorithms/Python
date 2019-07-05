a = 3
result = 0
while a < 1000:
    if(a % 3 == 0 or a % 5 == 0):
        result += a
    elif(a % 15 == 0):
        result -= a
    a += 1
print(result)
