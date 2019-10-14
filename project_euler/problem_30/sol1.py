#the sum of all the numbers that can be written as the sum of fifth powers of their digits.
#hint: If a number has at least n >= 7 digits, then even if every digit is 9,
# n * 9^5 is still less than the number (which is at least 10^n).
#6*9^5=354294


sum = 0

def fifth_power(string):
    total = 0
    length = len(string)
    for i in range(0,length):
        number = (int(string[i])**5)
        total = total + number
    return total

for j in range(2,354294):
    string = str(j)
    num = fifth_power(string)
    if num==j:
        sum = sum + num

print sum

