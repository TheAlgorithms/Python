power = int(input("Enter the power of 2: "))
num = 2**power
string_num = str(num)
sum_of_num = sum([int(i) for i in string_num])
print("2 ^",power,"=",num)
print("Sum of the digits is:",sum_of_num)
