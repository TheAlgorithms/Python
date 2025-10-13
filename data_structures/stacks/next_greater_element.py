"""
Next Greater Element
--------------------
Given an array, find the next greater element for each element in the array.
The next greater element for an element x is the first greater element on the
right side of x in the array. If no such element exists, output -1.
"""

def next_greater_elements(arr):
    stack = []
    result = [-1] * len(arr)

    # Traverse from right to left
    for i in range(len(arr) - 1, -1, -1):
        while stack and stack[-1] <= arr[i]:
            stack.pop()
        if stack:
            result[i] = stack[-1]
        stack.append(arr[i])
    return result


if __name__ == "__main__":
    sample = [4, 5, 2, 25]
    print("Input:", sample)
    print("Next Greater Elements:", next_greater_elements(sample))
    # Output: [5, 25, 25, -1]
