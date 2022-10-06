import random


def is_sorted(l):
    values = [l[i] <= l[i + 1] for i in range(len(l) - 1)]
    return all(values)


def random_sort(l):
    """
    efficiency? where are we going we don't need that
    """
    while not is_sorted(l):
        random.shuffle(l)
        # print(l)

    return l


if __name__ == "__main__":
    user_input = input("Enter numbers separated by a comma:\n").strip()
    unsorted = [int(item) for item in user_input.split(",")]
    print(random_sort(unsorted))
