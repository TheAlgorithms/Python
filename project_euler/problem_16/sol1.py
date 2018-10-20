power = int(input("Enter the power of 2: "))
num = 2**power

string_num = str(num)

list_num = list(string_num)

sum_of_num = 0

print("2 ^",power,"=",num)

for i in list_num:
    sum_of_num += int(i)

print("Sum of the digits are:",sum_of_num)
