x = input("Enter Card Number : ")
list_of_digits = [i for i in x]
list_1 = []
sum1 = 0
for i in range(len(x) - 2, -1, -2):
    a = str(2 * (int(list_of_digits[i])))
    list_1.append(a)
    for j in range(len(a)):
        sum1 += int(a[j])
sum2 = sum1
for i in range(len(x) - 1, -1, -2):
    sum2 += int(list_of_digits[i])
if (sum2) % 10 == 0:
    if len(x) == 15:
        print("AMEX")
    elif (len(x) == 16 or len(x) == 13) and x[0] == '4':
        print("VISA")
    else:
        print("MASTERCARD")
else:
    print("INVALID")
