def check_degree_sequence(degree_sequence):
    '''
    Args:
        degree_sequence (list of ints): sequence of the number of edges each vertex has

    Return: 
        bool: True if if there is an even number of odd elements and only positive integers in the degree sequence

    '''
    odd_count = 0
    for num in degree_sequence:
        if num % 2 != 0:
            odd_count += 1
        if num < 0:
            return False
    if odd_count % 2 != 0:
        return False
    return True


def check_zeros(degree_sequence):  
    '''
    Args:
        degree_sequence (list of ints): sequence of the number of edges each vertex has
    
    Return: 
        bool: True if the degree sequence only contains 0, False if at least one element is not 0

    '''
    flag = False
    for num in degree_sequence:
        if num != 0:
            flag = True
    if flag:
        return False
    return True


def havel_hakimi(degree_sequence):
    '''
    The Havel-Hakimi algorithm determines if a graph exists given a degree sequence
    https://en.wikipedia.org/wiki/Havel%E2%80%93Hakimi_algorithm

    Args:
        degree_sequence (list of ints): sequence of the number of edges each vertex has

    Return: 
        bool: True if the degree sequence is graphical, false if the degree sequence is not graphical

    '''

    while not check_zeros(degree_sequence):
        degree_sequence.sort(reverse=True)
        removed = degree_sequence.pop(0)

        if removed > len(degree_sequence):
            return False

        for itr in range(0, removed):
            degree_sequence[itr] -= 1

            if degree_sequence[itr] <= -1:  # not graphical if there are any numbers less than 0 in the list
                return False 

    return True


if __name__ == "__main__":
    import doctest
    doctest.testmod()

