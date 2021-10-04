from random_list import random_list_maker

def sort(l):
    max_val = l[0]

    def add_val(num):
        nonlocal max_val
        max_val = num
        return num

    return [add_val(x) for x in l if x >= max_val]
