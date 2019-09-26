import math


def rearrange(bitString32):
    """[summary]
    Regroups the given binary string.

    Arguments:
        bitString32 {[string]} -- [32 bit binary]

    Raises:
    ValueError -- [if the given string not are 32 bit binary string]

    Returns:
        [string] -- [32 bit binary string]
    >>> rearrange('1234567890abcdfghijklmnopqrstuvw')
    'pqrstuvwhijklmno90abcdfg12345678'
    """

    if len(bitString32) != 32:
        raise ValueError("Need length 32")
    newString = ""
    for i in [3, 2,1,0]:
        newString += bitString32[8*i:8*i+8]
    return newString


def reformatHex(i):
    """[summary]
    Converts the given integer into 8-digit hex number.

    Arguments:
            i {[int]} -- [integer]
    >>> reformatHex(666)
    '9a020000'
    """

    hexrep = format(i, '08x')
    thing = ""
    for i in [3, 2,1,0]:
        thing += hexrep[2*i:2*i+2]
    return thing


def pad(bitString):
    """[summary]
    Fills up the binary string to a 512 bit binary string

    Arguments:
            bitString {[string]} -- [binary string]

    Returns:
            [string] -- [binary string]
    """
    startLength = len(bitString)
    bitString += '1'
    while len(bitString) % 512 != 448:
        bitString += '0'
    lastPart = format(startLength, '064b')
    bitString += rearrange(lastPart[32:]) + rearrange(lastPart[:32])
    return bitString


def getBlock(bitString):
    """[summary]
    Iterator:
            Returns by each call a list of length 16 with the 32 bit
            integer blocks.

    Arguments:
            bitString {[string]} -- [binary string >= 512]
    """

    currPos = 0
    while currPos < len(bitString):
        currPart = bitString[currPos:currPos+512]
        mySplits = []
        for i in range(16):
            mySplits.append(int(rearrange(currPart[32*i:32*i+32]), 2))
        yield mySplits
        currPos += 512


def not32(i):
    '''
    >>> not32(34)
    4294967261
    '''
    i_str = format(i, '032b')
    new_str = ''
    for c in i_str:
        new_str += '1' if c == '0' else '0'
    return int(new_str, 2)

def sum32(a, b):
    '''

    '''
    return (a + b) % 2**32

def leftrot32(i, s):
    return (i << s) ^ (i >> (32-s))


def md5me(testString):
    """[summary]
    Returns a 32-bit hash code of the string 'testString'

    Arguments:
            testString {[string]} -- [message]
    """

    bs = ''
    for i in testString:
        bs += format(ord(i), '08b')
    bs = pad(bs)

    tvals = [int(2**32 * abs(math.sin(i+1))) for i in range(64)]

    a0 = 0x67452301
    b0 = 0xefcdab89
    c0 = 0x98badcfe
    d0 = 0x10325476

    s = [7, 12, 17, 22,  7, 12, 17, 22,  7, 12, 17, 22,  7, 12, 17, 22,
         5,  9, 14, 20,  5,  9, 14, 20,  5,  9, 14, 20,  5,  9, 14, 20, \
         4, 11, 16, 23,  4, 11, 16, 23,  4, 11, 16, 23,  4, 11, 16, 23, \
         6, 10, 15, 21,  6, 10, 15, 21,  6, 10, 15, 21,  6, 10, 15, 21 ]

    for m in getBlock(bs):
        A = a0
        B = b0
        C = c0
        D = d0
        for i in range(64):
            if i <= 15:
                #f = (B & C) | (not32(B) & D)
                f = D ^ (B & (C ^ D))
                g = i
            elif i <= 31:
                #f = (D & B) | (not32(D) & C)
                f = C ^ (D & (B ^ C))
                g = (5*i+1) % 16
            elif i <= 47:
                f = B ^ C ^ D
                g = (3*i+5) % 16
            else:
                f = C ^ (B | not32(D))
                g = (7*i) % 16
            dtemp = D
            D = C
            C = B
            B = sum32(B, leftrot32((A + f + tvals[i] + m[g]) % 2**32, s[i]))
            A = dtemp
        a0 = sum32(a0, A)
        b0 = sum32(b0, B)
        c0 = sum32(c0, C)
        d0 = sum32(d0, D)

    digest = reformatHex(a0) + reformatHex(b0) + \
                         reformatHex(c0) + reformatHex(d0)
    return digest


def test():
    assert md5me("") == "d41d8cd98f00b204e9800998ecf8427e"
    assert md5me(
        "The quick brown fox jumps over the lazy dog") == "9e107d9d372bb6826bd81d3542a419d6"
    print("Success.")


if __name__ == "__main__":
    test()
    import doctest
    doctest.testmod()
