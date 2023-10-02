import unittest


def int_to_roman(num: int) -> str:
    """
    criação de dicionário para armazenar os valores
    dos numerais e respectivos correspondentes romanos
    """
    roman_values = {
        1: "I",
        4: "IV",
        5: "V",
        9: "IX",
        10: "X",
        40: "XL",
        50: "L",
        90: "XC",
        100: "C",
        400: "CD",
        500: "D",
        900: "CM",
        1000: "M",
    }

    roman_str = ""
    """
    cria uma lista com as keys para
    conseguir percorrer ela de baixo pra cima
    """
    lista_indices = list(roman_values.keys())
    for value in lista_indices[::-1]:
        while num >= value:
            roman_str += roman_values[value]
            num -= value
    return roman_str


class TestIntToRoman(unittest.TestCase):
    def test_int_to_roman(self):
        self.assertEqual(int_to_roman(1), "I")
        self.assertEqual(int_to_roman(4), "IV")
        self.assertEqual(int_to_roman(9), "IX")
        self.assertEqual(int_to_roman(10), "X")
        self.assertEqual(int_to_roman(40), "XL")
        self.assertEqual(int_to_roman(50), "L")
        self.assertEqual(int_to_roman(90), "XC")
        self.assertEqual(int_to_roman(100), "C")
        self.assertEqual(int_to_roman(400), "CD")
        self.assertEqual(int_to_roman(500), "D")
        self.assertEqual(int_to_roman(900), "CM")
        self.assertEqual(int_to_roman(1000), "M")
        self.assertEqual(int_to_roman(3999), "MMMCMXCIX")  # Teste com um número maior


if __name__ == "__main__":
    unittest.main()
