import sys


def merge_sort(alist):
    print("Splitting ", alist)
    if len(alist) > 1:
        mid = len(alist) // 2
        left_half = alist[:mid]
        right_half = alist[mid:]
        merge_sort(left_half)
        merge_sort(right_half)
        i = j = k = 0

        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                alist[k] = left_half[i]
                i += 1
            else:
                alist[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            alist[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            alist[k] = right_half[j]
            j += 1
            k += 1
    print("Merging ", alist)
    return alist


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
        sorted_input = merge_sort(inputs)
        print('\nSorted list (min to max): {}'.format(sorted_input))

if __name__ == '__main__':
    print('==== Merge Sort ====\n')
    main()
