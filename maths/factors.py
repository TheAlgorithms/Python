list1 = []  # declaring an empty list to store the factors after calculation
num = int(input("Enter a positive number: "))  # accepting a number from the user
for i in range(1, num + 1):  # calculating and storing the factors in the list
    if num % i == 0:
        list1.append(i)
print(
    "The factors of the number", num, "are:--\n", list1
)  # displaying the factors of the given number in the form of a list

"""       ---::Output::---
>>> The factors of the number 1 are:--
[1]
>>> The factors of the number 5 are:--
[1, 5]
>>> The factors of the number 24 are:--
[1, 2, 3, 4, 6, 8, 12, 24]
>>> The factors of the number -24 are:--
[]
"""
