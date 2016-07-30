import sys


def simple_bubble_sort(int_list):
    count = len(int_list)
    swapped = True
    while (swapped):
        swapped = False
        for j in range(count - 1):
            if (int_list[j] > int_list[j + 1]):
                int_list[j], int_list[j + 1] = int_list[j + 1], int_list[j]
                swapped = True
    return int_list


def main():
    # Python 2's `raw_input` has been renamed to `input` in Python 3
    if sys.version_info.major < 3:
        input_function = raw_input
    else:
        input_function = input

    try:
        print("Enter numbers separated by spaces:")
        s = input_function()
        inputs = list(map(int, s.split(' ')))
        if len(inputs) < 2:
            print('No Enough values to sort!')
            raise Exception

    except Exception as e:
        print(e)
    else:
        sorted_input = simple_bubble_sort(inputs)
        print('\nSorted list (min to max): {}'.format(sorted_input))

if __name__ == '__main__':
    print('==== Bubble Sort ====\n')
    main()
