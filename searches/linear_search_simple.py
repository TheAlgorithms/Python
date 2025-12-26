"""
Linear Search Algorithm

Linear search (also known as sequential search) is a simple searching algorithm
that checks each element in a collection sequentially until it finds the target
value or reaches the end of the collection.

How it works:
1. Start from the first element in the collection
2. Compare the current element with the target value
3. If they match, return the index of the current element
4. If they don't match, move to the next element
5. Repeat steps 2-4 until the target is found or all elements have been checked
6. If the target is not found after checking all elements, return -1

Time Complexity:
- Best case: O(1) - when the target is found at the first position
- Average case: O(n) - where n is the number of elements
- Worst case: O(n) - when the target is at the end or not found

Space Complexity:
- O(1) - only a constant amount of extra space is used (for variables)
"""


from typing import Any, List, Optional


def linear_search(collection: List[Any], target: Any) -> int:
    """
    Perform a linear search to find the target value in the collection.

    Args:
        collection: A list of elements to search through (does not need to be sorted)
        target: The value to search for in the collection

    Returns:
        The index of the target value if found, -1 otherwise

    Examples:
        >>> linear_search([5, 2, 8, 1, 9], 8)
        2
        >>> linear_search([5, 2, 8, 1, 9], 3)
        -1
        >>> linear_search(['apple', 'banana', 'cherry'], 'banana')
        1
    """
    for index, item in enumerate(collection):
        if item == target:
            return index
    return -1


if __name__ == "__main__":
    # Example 1: Searching for a number in a list of integers
    numbers = [64, 34, 25, 12, 22, 11, 90]
    target_number = 22
    result = linear_search(numbers, target_number)
    
    print("Example 1: Searching for a number")
    print(f"Collection: {numbers}")
    print(f"Target: {target_number}")
    if result != -1:
        print(f"Result: Found at index {result}")
    else:
        print("Result: Not found")
    print()

    # Example 2: Searching for a string
    fruits = ["apple", "banana", "cherry", "date", "elderberry"]
    target_fruit = "cherry"
    result = linear_search(fruits, target_fruit)
    
    print("Example 2: Searching for a string")
    print(f"Collection: {fruits}")
    print(f"Target: {target_fruit}")
    if result != -1:
        print(f"Result: Found at index {result}")
    else:
        print("Result: Not found")
    print()

    # Example 3: Target not found
    numbers = [1, 3, 5, 7, 9]
    target_number = 4
    result = linear_search(numbers, target_number)
    
    print("Example 3: Target not found")
    print(f"Collection: {numbers}")
    print(f"Target: {target_number}")
    if result != -1:
        print(f"Result: Found at index {result}")
    else:
        print("Result: Not found")
    print()

    # Example 4: Empty collection
    empty_list: List[int] = []
    result = linear_search(empty_list, 5)
    
    print("Example 4: Empty collection")
    print(f"Collection: {empty_list}")
    print(f"Target: 5")
    if result != -1:
        print(f"Result: Found at index {result}")
    else:
        print("Result: Not found")
