""" 
Exponential search is also known as doubling or galloping search.
Exponential search involves two steps:  

1. Find range where element is present
2. Perform Binary Search in above found range.

You can read more about it here - https://en.wikipedia.org/wiki/Exponential_search
"""


def BinarySearch(lys, val):
    first = 0
    last = len(lys)-1
    index = -1
    while (first <= last) and (index == -1):
        mid = (first+last)//2
        if lys[mid] == val:
            index = mid
        else:
            if val<lys[mid]:
                last = mid -1
            else:
                first = mid +1
    return index

def exponentialSearch(lst, val):
    if lst[0] == val:
        return 0
    index = 1
    while index < len(lst) and lst[index] <= val:
        index = index * 2
    return BinarySearch( arr[:min(index, len(lst))], val)

#driver code
if __name__ == "__main__":
    user_input = input("Enter numbers separated by a comma (in ascending order):\n").strip()
    arr = [int(item) for item in user_input.split(",")]
    print(arr)
    x = int(input("Enter the number to be searched:\n"))
    res = exponentialSearch(arr, x)
    if res == -1:
        print("Number not found!")
    else:
        print(f"Number {x} is at index {res}. (Index starts from 0)")
