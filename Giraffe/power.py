def raise_to_power(base_number,pow_number):
    result = 1
    for index in range(pow_number):
        result = result * base_number
    return result
a = int(input("Enter number one: "))
b = int(input(" Enter the number two: "))

x = raise_to_power(a,b)
print("The result is : ",x)
