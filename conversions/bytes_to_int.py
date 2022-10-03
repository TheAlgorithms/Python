"""
This script first converts a byetarray to its corresponding sugned/unsigned binary number and the converts the binary number to an integer.
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

        if signed == True:
            temp = ""
            for j in binval:
                if (j == "0") is True:
                    temp = str(temp) + "1"
                else:
                    temp = str(temp) + "0"
            binval = temp
            binval = str(bin(int(binval, 2) + int("1", 2)))[2:]

        for k in binval:
            rslt = 2 * rslt + int(k)

        if (signed == True) is True:
            rslt *= -1

        return rslt

    except Exception as e:
        print(f"ERROR - {e}")
        return 0
 
