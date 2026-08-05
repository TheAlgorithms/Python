def meta_binary_search(arr, target):
    """Meta Binary Search using bit manipulation."""
    n = len(arr)
    pos = -1
    for i in reversed(range(n.bit_length())):
        new_pos = pos + (1 << i)
        if new_pos < n and arr[new_pos] <= target:
            pos = new_pos
    if pos != -1 and arr[pos] == target:
        return pos
    return -1


if __name__ == "__main__":
    arr = [2, 5, 7, 9, 14, 18, 21, 25]
    target = 18
    result = meta_binary_search(arr, target)
    print(
        f"Element {target} found at index: {result}"
        if result != -1
        else "Element not found."
    )
