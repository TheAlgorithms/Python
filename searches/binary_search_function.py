def binary_search(data, elem):

    start = 0
    end = len(data) - 1

    while start <= end:

        middle = (start + end)//2

        if data[middle] == elem:
            return middle
        elif data[middle] > elem:
            end = middle - 1
        else:
            start = middle + 1

    return -1


print()
list1 = [3, 5, 23, 6, 12, 0, 14, 10]

# ....search must be done in sorted list
result = binary_search(sorted(list1), 10)

if result == -1:
    print("Element not found")
else:
    print("Element found at index " + str(result))
