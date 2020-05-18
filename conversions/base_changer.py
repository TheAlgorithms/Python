def base_changer(num: str, from_base: int, to_base: int) -> str:
    # set decimal value for each hexadecimal digit and vice versa
    hex_codes = {
        "A": 10,
        "B": 11,
        "C": 12,
        "D": 13,
        "E": 14,
        "F": 15,
        "G": 16,
        "H": 17,
        10: "A",
        11: "B",
        12: "C",
        13: "D",
        14: "E",
        15: "F",
        16: "G",
        17: "H",
    }

    # split the number with decimal into before and after decimal point if any.
    splitter = num.split(".")
    before_dec = 0
    power = 0
    num_int = splitter[0][::-1]
    for i in num_int:
        # to change to numbers only if base
        # >10  for before decimal part
        if i in hex_codes:
            before_dec = before_dec + hex_codes[i] * (from_base ** power)
        else:
            i = int(i)
            before_dec = before_dec + i * (from_base ** power)
        power += 1

    intermediate_result = before_dec

    # to tackle after decimal part
    if len(splitter) != 1:
        point = 0
        power = -1
        num_before_dec = splitter[1]
        for i in num_before_dec:
            if i in hex_codes:
                point = point + hex_codes[i] * (from_base ** power)
            else:
                i = int(i)
                point = point + i * (from_base ** power)
            power = power - 1
        intermediate_result = intermediate_result + point
    before_dec = []
    after_dec = []

    # as we already converted to base 10
    if to_base == 10:
        ans = intermediate_result
        return ans
    else:
        intermediate_result = str(intermediate_result)
        # to tackle decimals in intermediate_result if any
        split_intermediate = intermediate_result.split(".")
        intermediate_result = int(split_intermediate[0])
        while intermediate_result >= to_base:
            rem = intermediate_result % to_base
            intermediate_result = intermediate_result // to_base
            if rem in hex_codes:
                before_dec.append(hex_codes[rem])
            else:
                before_dec.append(rem)
        if intermediate_result in hex_codes:
            before_dec.append(hex_codes[intermediate_result])
        else:
            before_dec.append(intermediate_result)
        before_dec = before_dec[::-1]
        ans = "".join([str(i) for i in before_dec])
        # for part after decimal in intermediate_result

        if len(splitter) != 1:
            len_dec = len(split_intermediate[1])
            intermediate_dec = int(split_intermediate[1])
            for i in range(5):
                multiply_intermediate_dec = str(intermediate_dec * to_base)
                len_inter_dec = len(multiply_intermediate_dec)
                if len_inter_dec > len_dec:
                    appender = (
                            multiply_intermediate_dec[: len_inter_dec - len_dec]
                            + "."
                            + multiply_intermediate_dec[len_inter_dec - len_dec:]
                    )
                else:
                    appender = "0." + multiply_intermediate_dec
                append_splitter = appender.split(".")
                hex_check = int(append_splitter[0])
                if hex_check in hex_codes:
                    after_dec.append(hex_codes[hex_check])
                else:
                    after_dec.append(append_splitter[0])
                intermediate_dec = int(append_splitter[1])
            after_dec = "".join([str(i) for i in after_dec])
            ans = ans + "." + after_dec
        return ans


if __name__ == "__main__":
    num = input("Enter the number ").strip()
    from_base = int(input("Enter the base(2-18) ").strip())
    to_base = int(input("Enter the new base(2-18) ").strip())
    if 18 >= from_base >= 2 and 18 >= to_base >= 2:
        result = base_changer(num, from_base, to_base)
        print(result)
    else:
        print("Invalid Inputs.")
