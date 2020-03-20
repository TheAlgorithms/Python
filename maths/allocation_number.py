#-*- coding:utf-8 -*-


def allocation_num(num, x) -> int:
    """
    Divide the numbers into x parts.
    
    This algorithm can be used in multi thread Download.
    For byte splitting.
    For example:
        for i in allocation_list:
            requests.get(url,headers={'Range':f'bytes={i}'})

    parameter
    ------------
    : param num: the number
    : param x: number of copies

    return
    ------------
    : return: split completed list

    example
    ------------
    >>> allocation_num(16647, 4)
    ['0-4161', '4162-8322', '8323-12483', '12484-16647']

    >>> allocation_num(888, 888)
    Traceback (most recent call last):
        ...
    ValueError: param x can't past or be equal to the param num!

    >>> allocation_num(888, 999)
    Traceback (most recent call last):
        ...
    ValueError: param x can't past or be equal to the param num!
    """


    if x >= num:
        raise ValueError('param x can\'t past or be equal to the param num!')

    shares = num // x

    allocation_list = [f'0-{shares*1}']
    for i in range(1,x-1):
        length = f'{shares*i+1}-{shares*(i+1)}'
        allocation_list.append(length)
    allocation_list.append(f'{(shares*(x-1))+1}-{num}')

    return allocation_list


if __name__ == '__main__':
    import doctest
    doctest.testmod()


