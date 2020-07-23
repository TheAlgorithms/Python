
def enQueue(lst: list, data: str):
    # Adds element to the back of the queue
    lst.append(data)


def deQueue(lst: list):
    # Returns element at front of the queue
    return lst.pop(0)


def mirror(qString: str):
    '''
    Returns a mirrored form of the string using enqueue and dequeue methods
    >>> mirror("python")
    'pythonnohtyp'
    >>> mirror("github")
    'githubbuhtig'
    '''
    qString = qString.strip()
    qString = list(qString)
    Reverse = qString[::-1]
    for i in range(len(Reverse)):
        enQueue(qString, deQueue(Reverse))
    str1 = ''
    qString = str1.join(qString)
    return (qString)


if __name__ == "__main__":
    import doctest
    doctest.testmod()
