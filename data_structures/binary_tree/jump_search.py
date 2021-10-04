import math

def JumpSearch (lst, val): #lst->list, val->value
    length = len(lst)
    jump = int(math.sqrt(length))
    left, right = 0, 0
    while left < length and lst[left] <= val:
        right = min(length - 1, left + jump)
        if lst[left] <= val and lst[right] >= val:
            break
        left += jump;
    if left >= length or lst[left] > val:
        return -1
    right = min(length - 1, right)
    i = left
    while i <= right and lst[i] <= val:
        if lst[i] == val:
            return i
        i += 1
    return -1
