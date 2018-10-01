def radixsort(lst):
    if len(lst) < 1:
        return

    RADIX = 10
    maxLength = False
    tmp, placement = -1, 1

    while not maxLength:
        maxLength = True
        # declare and initialize buckets
        buckets = [list() for _ in range(RADIX)]

        # split lst between lists
        for i in lst:
            tmp = int((i / placement) % RADIX)
            buckets[tmp].append(i)

            if maxLength and tmp > 0:
                maxLength = False

        # empty lists into lst array
        a = 0
        for b in range(RADIX):
            buck = buckets[b]
            for i in buck:
                lst[a] = i
                a += 1

        # move to next
        placement *= RADIX


if __name__ == '__main__':
    try:
        raw_input          # Python 2
    except NameError:
        raw_input = input  # Python 3

    user_input = raw_input('Enter numbers separated by a comma:\n').strip()
    unsorted = [int(item) for item in user_input.split(',')]
    radixsort(unsorted)
    print(unsorted)
