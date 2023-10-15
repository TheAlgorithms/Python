def combination_util(arr, n, r, index, data, i, result):
    if index == r:
        result.append(tuple(data[:r]))  # Append the combination to the result list
        return
    if i >= n:
        return
    data[index] = arr[i]
    combination_util(arr, n, r, index + 1, data, i + 1, result)
    combination_util(arr, n, r, index, data, i + 1, result)


def print_combination(arr, n, r):
    data = [0] * r
    result = []  # Initialize an empty list to store the combinations
    combination_util(arr, n, r, 0, data, 0, result)
    return result  # Return the list of tuples


if __name__ == "__main__":
    arr = [10, 20, 30, 40, 50]
    combinations = print_combination(arr, len(arr), 3)
    for combo in combinations:
        print(combo)
