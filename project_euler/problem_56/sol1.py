def maximum_digital_sum(a,b):
    '''
    Considering natural numbers of the form, a**b, where a, b < 100,
    what is the maximum digital sum?
    :param a:
    :param b:
    :return:
    '''
    # RETURN the MAXIMUM from the list of SUMs of the list of INT converted from STR of BASE raised to the POWER
    return max([sum([int(x) for x in str(base**power)]) for base in range(a) for power in range(b)])

#Tests
print(maximum_digital_sum(10,10), "is 45")
print(maximum_digital_sum(100,100), "is 972")
print(maximum_digital_sum(100,200), "is 1872")
