def bytes_to_int(bytes_var: bytearray,byteorder: str,signed: bool,) -> (int):

    r"""
    This script first converts a bytearray,
    to its corresponding signed/unsigned binary number,
    and then converts the binary number to an integer.

    >>> tests = ((b"\x00\x10", "big", False), (b'\xfc\x00', "big", True),
    ...          (b'\x00\x01', "big", False), (b'\x00\x10', 'little', False))
    >>> all(bytes_to_int(bytes, byteorder, signed=signed) == int.from_bytes(bytes, byteorder, signed=signed)
    ...     for bytes, byteorder, signed in tests)
    True
    >>> bytes_to_int('abc',False,'big')
    AttributeError - 'bool' object has no attribute 'lower'
    0
    >>> bytes_to_int(7.1, 'little', signed=True)
    TypeError - 'float' object is not subscriptable
    0

    """

    try:
        byteorder = byteorder.lower()
        if byteorder == "little":
            bytes_var = bytes_var[::-1]
        binval = ""
        for i in bytes_var:
            binnum = str(bin(i))[2:]
            if len(binnum) < 8:
                for i in range(0, 8 - len(binnum)):
                    binnum = "0" + binnum
            binval = binval + binnum

        rslt = 0

        if signed is True:
            temp = ""
            for j in binval:
                flag = j == "0"
                temp += str(int(flag))
            binval = temp
            binval = str(bin(int(binval, 2) + int("1", 2)))[2:]

        for k in binval:
            rslt = 2 * rslt + int(k)

        if signed is True:
            rslt *= -1

        return rslt

    except Exception as e:
        print(f"{type(e).__name__} - {e}")
        return 0


if __name__ == "__main__":
    import doctest

    doctest.testmod()
