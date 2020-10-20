class py_int_roman:
    def int_to_Roman(self, num):
        """
          LeetCode No. 14 Integer to Roman
          Given an integer, convert it to a roman numeral.
          https://en.wikipedia.org/wiki/Roman_numerals
          >>> tests = {3: "III", 154: "CLIV", 1009: "MIX", 2500: "MMD"}
          >>> all(int_to_roman(key) == value for key, value in tests.items())
          True
          
        """
        val = [
            1000, 900, 500, 400,
            100, 90, 50, 40,
            10, 9, 5, 4,
            1
            ]
        syb = [
            "M", "CM", "D", "CD",
            "C", "XC", "L", "XL",
            "X", "IX", "V", "IV",
            "I"
            ]
        roman_num = ''
        i = 0
        while  num > 0:
            for _ in range(num // val[i]):
                roman_num += syb[i]
                num -= val[i]
            i += 1
        return roman_num


print(py_int_roman().int_to_Roman(1))
print(py_int_roman().int_to_Roman(4000))
