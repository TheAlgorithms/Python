def sleep_sort(element: int):
    from time import sleep

    sleep(element)
    global collection
    collection.append(element)


if __name__ == "__main__":
    import doctest
    import _thread
    import time
    from time import sleep

    doctest.testmod()

    user_input = input("Enter numbers separated by a comma:").strip()
    unsorted_input = [int(item) for item in user_input.split(",")]
    start = time.process_time()
    collection = []
    for i in unsorted_input:
        _thread.start_new_thread(sleep_sort, (i,))
    # sleep for time == max value + 1 second for operations to take place
    sleep(max(unsorted_input) + 1)
    print(*collection, sep=",")
    print(f"Processing time: {time.process_time() - start}")

# for information regarding sleep sort :
# https://www.geeksforgeeks.org/sleep-sort-king-laziness-sorting-sleeping
