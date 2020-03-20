#-*- coding:utf-8 -*-


def allocation_content_length(content_length, portioning):
    """
    >>> content_length = 16647
    >>> portioning = 4
    >>> shares = content_length // portioning

    >>> f'0-{shares*1}'
    '0-4161'
    >>> f'{shares*1+1}-{shares*2}'
    '4162-8322'
    >>> f'{shares*2+1}-{shares*3}'
    '8323-12483'
    >>> f'{shares*3+1}-{shares*4}'
    '12484-16647'
    """

    shares = content_length // portioning

    allocation_list = [f'0-{shares*1}']
    for i in range(1,portioning-1):
        length = f'{shares*i+1}-{shares*(i+1)}'
        allocation_list.append(length)
    allocation_list.append(f'{(shares*(portioning-1))+1}-{content_length}')

    return allocation_list


def main():
    the_list = allocation_content_length(16647,4)
    print(the_list)


if __name__ == '__main__':
    main()


