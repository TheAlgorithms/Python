from typing import List


def radix_sort(list_of_ints: List[int]) -> List[int]:
    """
    radix_sort(range(15)) == sorted(range(15))
    True
    radix_sort(reversed(range(15))) == sorted(range(15))
    True
    """
    RADIX = 10
    placement = 1

    # get the maximum number
    max_digit = max(list_of_ints)

    while placement < max_digit:
        # declare and initialize buckets
        buckets = [list() for _ in range(RADIX)]

        # split list_of_ints between lists
        for i in list_of_ints:
            tmp = int((i / placement) % RADIX)
            buckets[tmp].append(i)

        # empty lists into list_of_ints
        a = 0
        for b in range(RADIX):
            buck = buckets[b]
            for i in buck:
                list_of_ints[a] = i
                a += 1

        # move to next
        placement *= RADIX
    return list_of_ints
