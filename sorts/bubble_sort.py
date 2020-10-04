def bubble_sort(collection):
    length_num = len(collection)
    for i in range(length_num - 1):
        flag = False
        for j in range(length_num - 1 - i):
            if collection[j] > collection[j + 1]:
                flag = True
                collection[j], collection[j + 1] = collection[j + 1], collection[j]
        if not flag:
            break
    return collection


if __name__ == "__main__":
    import doctest
    import time

    doctest.testmod()

    user_input = input("Enter numbers separated by a space:").strip()
    unsorted = [int(item) for item in user_input.split(" ")]
    start = time.process_time()
    print(*bubble_sort(unsorted), sep=" ")
    print(f"Processing time: {time.process_time() - start}")
