import copy
import unittest

from compression.lzw.common import generate_initial_dictionary
from compression.lzw.decoder import Decoder
from compression.lzw.symbol import Symbol


class TestDecoder(unittest.TestCase):
    def setUp(self) -> None:
        self.alphabet, self._symbol = generate_initial_dictionary()
        self._test_symbol = copy.deepcopy(self._symbol)
        self.decoder = Decoder(self.alphabet, self._symbol)

    def test_decode_empty_input(self):
        encoded_input = Symbol()
        decoded = self.decoder.decode(encoded_input)
        self.assertEqual("", decoded)

    def test_decode_single_symbol(self):
        encoded_input = self.alphabet["A"]
        decoded = self.decoder.decode(encoded_input)
        self.assertEqual("A", decoded)

    def test_decode_two_different_symbols(self):
        encoded_input = self.alphabet["A"] + self.alphabet["B"]
        decoded = self.decoder.decode(encoded_input)
        self.assertEqual("AB", decoded)

    def test_decode_repetition(self):
        encoded_input = (
            self.alphabet["A"] + self.alphabet["B"] + next(self._test_symbol)
        )
        decoded = self.decoder.decode(encoded_input)
        self.assertEqual("ABAB", decoded)

    def test_decode_double_repetition(self):
        ab_symbol = next(self._test_symbol)
        # ba_symbol will not be used by the encoder to encode this input
        # but still we need to generate it
        _ = next(self._test_symbol)
        aba_symbol = next(self._test_symbol)
        encoded_input = self.alphabet["A"] + self.alphabet["B"] + ab_symbol + aba_symbol
        decoded = self.decoder.decode(encoded_input)
        self.assertEqual("ABABABA", decoded)

    # example taken from https://en.wikipedia.org/wiki/Lempel%E2%80%93Ziv%E2%80%93Welch
    def test_decode_wikipedia_example(self):
        encoded_raw = (
            "10100011110001000101011111001000111000111101010001101101110"
            "1011111100100011110100000100010"
        )
        encoded_input = Symbol(encoded_raw)
        decoded = self.decoder.decode(encoded_input)
        self.assertEqual("TOBEORNOTTOBEORTOBEORNOT", decoded)


if __name__ == "__main__":
    unittest.main()
