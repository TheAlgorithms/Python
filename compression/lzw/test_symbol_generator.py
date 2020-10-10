import unittest

from compression.lzw.symbol import Symbol
from compression.lzw.symbol_generator import SymbolGenerator


class TestSymbolGenerator(unittest.TestCase):
    def test_start_from_provided_number_of_bits_and_value(self):
        generator = SymbolGenerator(0, 4)
        self.assertEqual(Symbol("0000"), next(generator))
        self.assertEqual(4, generator.current_bit_length)

    def test_linear_progression(self):
        generator = SymbolGenerator(4, 3)
        next(generator)
        next(generator)
        next(generator)
        self.assertEqual(Symbol("111"), next(generator))

    def test_linear_progression_when_needs_1_bit_more(self):
        generator = SymbolGenerator(7, 3)
        self.assertEqual(3, generator.current_bit_length)
        next(generator)  # yields the initial value
        self.assertEqual(Symbol("1000"), next(generator))
        self.assertEqual(4, generator.current_bit_length)

    def test_next_bit_length_returns_the_bits_needed_to_encode_the_next_symbol(self):
        generator = SymbolGenerator(1, 1)
        self.assertEqual(
            1, generator.next_bit_length
        )  # the next symbol will be the initial value
        self.assertEqual(Symbol("1"), next(generator))
        self.assertEqual(2, generator.next_bit_length)
        self.assertEqual(Symbol("10"), next(generator))
        self.assertEqual(2, generator.next_bit_length)
        self.assertEqual(Symbol("11"), next(generator))
        self.assertEqual(3, generator.next_bit_length)
        self.assertEqual(Symbol("100"), next(generator))

    def test_start_with_invalid_number_of_bits_for_initial_value(self):
        self.assertRaises(OverflowError, SymbolGenerator, 8, 3)

    def test_start_very_far_from_the_required_number_of_bits_for_initial_value(self):
        self.assertRaises(OverflowError, SymbolGenerator, 32, 2)


if __name__ == "__main__":
    unittest.main()
