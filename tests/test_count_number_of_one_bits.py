import unittest

from bit_manipulation.count_number_of_one_bits import (
    get_set_bits_count_using_brian_kernighans_algorithm,
    get_set_bits_count_using_modulo_operator,
)


class TestCountSetBits(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(get_set_bits_count_using_brian_kernighans_algorithm(25), 3)
        self.assertEqual(get_set_bits_count_using_brian_kernighans_algorithm(58), 4)
        self.assertEqual(get_set_bits_count_using_modulo_operator(37), 3)
        self.assertEqual(get_set_bits_count_using_modulo_operator(0), 0)

    def test_negative_input_raises(self):
        with self.assertRaises(ValueError):
            get_set_bits_count_using_brian_kernighans_algorithm(-1)


if __name__ == "__main__":
    unittest.main()
