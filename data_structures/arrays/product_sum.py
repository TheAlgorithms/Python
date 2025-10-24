def product_sum(arr: list[int | list], depth: int) -> int:
    total_sum = 0
    for ele in arr:
        if isinstance(ele, list):
            total_sum += product_sum(ele, depth + 1)
        else:
            total_sum += ele
    return total_sum * depth

def product_sum_array(array: list[int | list]) -> int:
    return product_sum(array, 1)

if _name_ == "_main_":
    import doctest
    doctest.testmod()
