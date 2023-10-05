'''
The Fletcher checksum is an algorithm for computing a position-dependent checksum devised by John G. Fletcher (1934–2012) at Lawrence Livermore Labs in the late 1970s.[1] The objective of the Fletcher checksum was to provide error-detection properties approaching those of a cyclic redundancy check but with the lower computational effort associated with summation techniques.

Source: https://en.wikipedia.org/wiki/Fletcher%27s_checksum
'''

def fletcher16(data):
    '''
    Loops through every character in the data and adds to two sums

    fletcher16('hello world') == 6752
    '''
    sum1 = 0
    sum2 = 0
    for character in data:
        sum1 = (sum1+character)%255
        sum2 = (sum1+sum2)%255
    return (sum2 << 8) | sum1


if __name__ == "__main__":
    text = input("Enter a text: ")
    stuffs = bytes(text, "ascii")
    print(fletcher16(stuffs))