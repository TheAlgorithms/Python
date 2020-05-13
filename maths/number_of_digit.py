number = int(input("Enter number"))
count=0
digits=[]

while number != 0:
    digits.append(num%10)
    number = number//10 #alternatively number = int(number/10)
    count = count +1

print("Number of Digits is", count)
digit = digits[::-1]
print("digits are",digit)
