import unittest

from compression.lzw.common import generate_initial_dictionary
from compression.lzw.encoder import Encoder
from compression.lzw.symbol import Symbol


class EncoderTest(unittest.TestCase):
    def setUp(self) -> None:
        self.alphabet, self._symbol = generate_initial_dictionary()
        self.encoder = Encoder(self.alphabet, self._symbol)

    def test_encode_empty_string(self):
        uncompressed_input = ""

        encoded = self.encoder.encode(uncompressed_input)

        self.assertEqual(Symbol(), encoded)

    def test_encode_single_character(self):
        uncompressed_input = "A"

        encoded = self.encoder.encode(uncompressed_input)

        self.assertEqual(self.alphabet["A"], encoded)

    def test_encode_two_different_characters(self):
        uncompressed_input = "AB"

        encoded = self.encoder.encode(uncompressed_input)

        self.assertEqual(self.alphabet["A"] + self.alphabet["B"], encoded)

    def test_encode_with_repetition(self):
        uncompressed_input = "ABAB"

        encoded = self.encoder.encode(uncompressed_input)

        expected_encoded = self.alphabet["A"]
        expected_encoded += self.alphabet["B"]
        expected_encoded += self.encoder.extended_dict["AB"]

        self.assertEqual(expected_encoded, encoded)

    # example taken from https://en.wikipedia.org/wiki/Lempel%E2%80%93Ziv%E2%80%93Welch
    def test_encode_wikipedia_example(self):
        uncompressed_input = "TOBEORNOTTOBEORTOBEORNOT"

        encoded = self.encoder.encode(uncompressed_input)

        expected_encoded_raw = (
            "10100011110001000101011111001000111000111101010001"
            "1011011101011111100100011110100000100010"
        )
        expected_encoded = Symbol(expected_encoded_raw)
        original_encoding = Symbol.from_dict(self.alphabet, uncompressed_input)

        self.assertLess(len(expected_encoded), len(original_encoding))
        self.assertEqual(expected_encoded, encoded)


if __name__ == "__main__":
    unittest.main()
