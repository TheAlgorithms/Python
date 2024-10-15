def find_floor(arr, n, x):
    low = 0
    high = n - 1
    ans = -1

    while low <= high:
        mid = (low + high) // 2
        # maybe an answer
        if arr[mid] <= x:
            ans = arr[mid]
            # look for smaller index on the left
            low = mid + 1
        else:
            high = mid - 1  # look on the right

    return ans


def find_ceil(arr, n, x):
    low = 0
    high = n - 1
    ans = -1

    while low <= high:
        mid = (low + high) // 2
        # maybe an answer
        if arr[mid] >= x:
            ans = arr[mid]
            # look for smaller index on the left
            high = mid - 1
        else:
            low = mid + 1  # look on the right

    return ans


def get_floor_and_ceil(arr, n, x):
    f = find_floor(arr, n, x)
    c = find_ceil(arr, n, x)
    return (f, c)


# sample test cas
# arr = [3, 4, 4, 7, 8, 10]
# n = 6
# x = 5
# ans = get_floor_and_ceil(arr, n, x)
# print("The floor and ceil are:", ans[0], ans[1])
