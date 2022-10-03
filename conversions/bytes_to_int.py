"""
This script first converts a bytearray,
to its corresponding signed/unsigned binary number,
and then converts the binary number to an integer.

>>> bytes_to_int(b'\\x00\\x10',False)
16
>>> bytes_to_int(b'\\xfc\\x00',True)
-1024
>>> bytes_to_int(b'\\x00\\x01',False)
1
>>> bytes_to_int('abc',False)
ERROR - 'str' object cannot be interpreted as an integer
"""
def bytes_to_int(bytes_var: bytearray, signed: bool) -> (int):
    try:
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
                flag = (j == "0")
                if flag is True:
                    temp = str(temp) + "1"
                else:
                    temp = str(temp) + "0"
            binval = temp
            binval = str(bin(int(binval, 2) + int("1", 2)))[2:]

        for k in binval:
            rslt = 2 * rslt + int(k)
            
            
        if signed is True:
            rslt *= -1

        return rslt

    except Exception as e:
        print(f"ERROR - {e}")
 
if __name__ == "__main__":
    import doctest
    doctest.testmod()
