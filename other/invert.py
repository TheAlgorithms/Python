def invert(lst):
    i = 0
    while i < len(lst):
        lst[i] = lst[i] * -1
        i = i + 1
    return lst
