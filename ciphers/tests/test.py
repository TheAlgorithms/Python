import unittest
from ciphers.break_vigenere import *


class TestBreakVigenere(unittest.TestCase):
    def test_index_of_coincidence(self):
        dictionary = {'a': 5, 'b': 1, 'c': 4}
        ic = index_of_coincidence(dictionary, 100)
        self.assertAlmostEqual(ic, 0.0032323232323232)