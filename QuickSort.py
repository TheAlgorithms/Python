
def quick_sort(A, p, r):
    if p < r:
        q = partition(A, p, r)
        quick_sort(A, p, q - 1)
        quick_sort(A, q + 1, r)
    return A


def partition(A, p, r):
    i = p - 1
    for j in range(p, r):
        if A[j] <= A[r]:
            i += 1
            A[i], A[j] = A[j], A[i]
    A[i + 1], A[r] = A[r], A[i + 1]
    return i + 1


def main():
    try:
        print("Enter numbers separated by spaces")
        s = raw_input()
        inputs = list(map(int, s.split(' ')))
    except Exception as e:
        print(e)
    else:
        sorted_input = quick_sort(inputs, 0, len(inputs) - 1)
        print('\nSorted list (min to max): {}'.format(sorted_input))

if __name__ == '__main__':
    print('==== Quick Sort ====\n')
    main()
