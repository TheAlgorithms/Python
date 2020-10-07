
def concatenated_product(factor, upper_limit):
    product_string = ''
    for i in range(1, upper_limit + 1):
        product = i * factor
        product_string += str(product)
    return int(product_string)

def is_pandigital(test_number):
    test_number_string = str(test_number)
    if len(test_number_string) != 9:
        return False
    count_list = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    reduced_number = test_number
    for i in range(9):
        digit = reduced_number % 10
        reduced_number = reduced_number // 10
        count_list[digit] += 1
    for i in range(1, 10):
        if count_list[i] != 1:
            return False
    return True


if __name__ == '__main__':
    n = int(input('Enter upper limit: '))
    test_number = 0
    concat_product = 0
    max_concat_product = 0
    is_too_long = False
    while not is_too_long:
        test_number += 1
        concat_product = concatenated_product(test_number, n)
        print('test number: ' + str(test_number) + ', concatenated product: ' + str(concat_product))
        if len(str(concat_product)) > 9:
            is_too_long = True
        elif is_pandigital(concat_product) and concat_product > max_concat_product:
            max_concat_product = concat_product
    print('Maximum pandigital concatenated product: ' + str(max_concat_product))
