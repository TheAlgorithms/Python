#assignment 23

def count_factors(Number):
    factor_count=0
    for i in range(1,int(Number+1)):
        if Number % i == 0:
            factor_count += 1
    return factor_count
"""Function Ended"""

"""Main program begins here"""
a = int(input("Enter the lower range of number: "))
b = int(input("Enter the Upper range of number(this will be included): "))
print("**************************************************************************")
number_elements = 0
for number in range(a,b+1):
    Number_Factor = count_factors(number)
    if Number_Factor % 2 == 1:
        number_elements += 1

print("Number of elements in given range having odd number of factors are: ",number_elements)