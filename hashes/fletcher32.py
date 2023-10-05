'''
The Fletcher checksum is an algorithm for computing a position-dependent
checksum devised by John G. Fletcher (1934–2012) at Lawrence Livermore Labs
in the late 1970s.[1] The objective of the Fletcher checksum was to
provide error-detection properties approaching those of a cyclic
redundancy check but with the lower computational effort associated
with summation techniques.

Source: https://en.wikipedia.org/wiki/Fletcher%27s_checksum
'''

def fletcher32(text: str) -> int:
    '''
    Turns the data into a list, and then loops them in pairs of two and adds to sums

    >>> fletcher32('Apple')
    705355030
    >>> fletcher32('ABCDEFGHI')
    3220837722
    >>> fletcher32("abcd")
    690407108
    '''
    data = bytes(text, "ascii")
    sum1 = 0
    sum2 = 0
    data_list = list(data)
    if len(data_list)%2 == 1:
        data_list.append(0)
    for idx in range(len(data_list)//2):
        v = (data_list[idx*2+1] << 8) + data_list[idx*2]
        sum1 = (sum1+v)%65535
        sum2 = (sum1+sum2)%65535
    return (sum2 << 16) | sum1

if __name__ == "__main__":
    import doctest
    doctest.testmod()