def product_sum(arr, depth):
    total_sum = 0
    for ele in arr:
        if isinstance(ele, list):
            total_sum += product_sum(ele, depth + 1)
        else:
            total_sum += ele
    return total_sum * depth

def product_sum_array(array):
    return product_sum(array, 1)

if __name__ == "__main__":
    import doctest
    doctest.testmod()
