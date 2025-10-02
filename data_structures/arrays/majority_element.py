def majority_element(arr: list[int]) -> int | None:
    """
    Find the majority element in an array using the Boyer-Moore Voting Algorithm
    The majority element is the element that appears more than n/2 times (n is the size of the array)

    Args:
        arr(list[int]): The input array
    
    Returns:
        int | None: The majority element if it exists
    
    Examples:
        >>> majority_element([3, 3, 4, 2, 4, 4, 2, 4, 4])
        4
        >>> majority_element([2, 2, 1, 1, 1, 2, 2])
        2
        >>> majority_element([1, 2, 3])
        None
        >>> majority_element([])
        None
    """

    count = 0
    majority = None

    for num in arr:
        if count == 0:
            majority = num
            count = 1
        elif num == majority:
            count += 1
        else:
            count -= 1
    
    if majority is not None and arr.count(majority) > len(arr) // 2:
        return majority
    return None


if __name__ == "__main__":
    arr = [3, 3, 4, 2, 4, 4, 2, 4, 4]
    print("Majority element: ", majority_element(arr))