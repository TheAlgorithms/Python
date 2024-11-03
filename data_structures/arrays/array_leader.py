"""
Given an array arr[] of size n, the task is to find all the Leaders in the array.
 An element is a Leader if it is greater than all the elements to its right side.

Note: The rightmost element is always a leader.
"""


def array_leader(arr):
    leaders = []
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] < arr[j]:
                break
        else:
            leaders.append(arr[i])

    return " ".join(map(str, leaders))


# Test the function with the provided input
print(array_leader([16, 17, 4, 3, 5, 2]))  # Expected output: 17 5 2
