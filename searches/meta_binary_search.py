def meta_binary_search(arr, target):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1


def main():
    arr = [2, 5, 8, 12, 16, 23, 38, 56, 72, 91]
    target = 23
    result = meta_binary_search(arr, target)
    if result != -1:
        print("Element found at index: ", result)
    else:
        print("Element not found!")


if __name__ == "main":
    main()
