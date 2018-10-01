from __future__ import print_function
def binary_search(lst, item, start, end):
    if start == end:
        if lst[start] > item:
            return start
        else:
            return start + 1
    if start > end:
        return start

    mid = (start + end) // 2
    if lst[mid] < item:
        return binary_search(lst, item, mid + 1, end)
    elif lst[mid] > item:
        return binary_search(lst, item, start, mid - 1)
    else:
        return mid


def insertion_sort(lst):
    length = len(lst)

    for index in range(1, length):
        value = lst[index]
        pos = binary_search(lst, value, 0, index - 1)
        lst = lst[:pos] + [value] + lst[pos:index] + lst[index+1:]

    return lst


def merge(left, right):
    if not left:
        return right

    if not right:
        return left

    if left[0] < right[0]:
        return [left[0]] + merge(left[1:], right)

    return [right[0]] + merge(left, right[1:])


def timsort(lst):
    runs, sorted_runs = [], []
    length = len(lst)
    new_run = [lst[0]]
    sorted_array = []

    for i in range(1, length):
        if i == length - 1:
            new_run.append(lst[i])
            runs.append(new_run)
            break

        if lst[i] < lst[i - 1]:
            if not new_run:
                runs.append([lst[i - 1]])
                new_run.append(lst[i])
            else:
                runs.append(new_run)
                new_run = []
        else:
            new_run.append(lst[i])

    for run in runs:
        sorted_runs.append(insertion_sort(run))

    for run in sorted_runs:
        sorted_array = merge(sorted_array, run)

    return sorted_array


def main():

    lst = [5,9,10,3,-4,5,178,92,46,-18,0,7]
    sorted_lst = timsort(lst)
    print(sorted_lst)

if __name__ == '__main__':
    main()
