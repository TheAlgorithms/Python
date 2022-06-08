# Write a program to perform linear search

# function to perform linear search on the list
def linear_search(list_1, size, key):
    for i in range(size):
        if list_1[i] == key:
            return i
    return -1


# scanning the size of the list 
size = int(input("Enter the number of elements to be entered in list: "))   # data type: int

# initialiszing the empty list
list_1 = []     # data type: list

# scanning the elements of the list
print(f"Enter the {size} elements of the list")
for i in range(size):
    print(f"Element {i+1}:", end=" ")
    element = int(input())
    list_1.append(element)

# printing the list
print("Your List:")
print(list_1)

# scanning the key element to find in the list
key = int(input("Enter an element to find in list: "))      # data type: int

# calling the linearSearch() function
result = linear_search(list_1, size, key)

# printing the conclusion
if result == -1:
    print(f"{key} is not found in the list")
else:
    print(f"{key} is found at position {result + 1} in the list")

    
    
# OUTPUT
# Enter the number of elements to be entered in list: 3
# Enter the 3 elements of the list
# Element 1: 1
# Element 2: 5
# Element 3: 9
# Your List:
# [1, 5, 9]
# Enter an element to find in list: 5
# 5 is found at position 2 in the list


# OUTPUT
# Enter the number of elements to be entered in list: 3
# Enter the 3 elements of the list
# Element 1: 1
# Element 2: 5
# Element 3: 9
# Your List:
# [1, 5, 9]
# Enter an element to find in list: 8
# 8 is not found in the list
