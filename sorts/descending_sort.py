def descending_sort(array: list) -> list:
    for i in range(len(array) - 1):
        for j in range(i + 1, len(array)):
            if array[i] < array[j]:
                array[i], array[j] = array[j], array[i]
    return array

def ascending_sort(array: list) -> list:
    for i in range(len(array) - 1):
        for j in range(i + 1, len(array)):
            if array[i] > array[j]:
                array[i], array[j] = array[j], array[i]
    return array


if __name__ == "__main__":
    user_input = input("Enter numbers separated by a comma:\n").strip()
    unsorted = [int(item) for item in user_input.split(",")]
    print(descending_sort(unsorted))
    print(ascending_sort(unsorted))
