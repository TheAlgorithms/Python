import unittest

CAPITALS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


def lower_char(capital: str) -> str:
    """
    Convert a capital to a lowercase letter
    """
    # int value of lowercase char = int value of uppercase char + 32
    return chr(ord(capital) + 32)


def lower(string: str) -> str:
    """
    Convert string to lowercase
    """
    return "".join(lower_char(char) if char in CAPITALS else char for char in string)


class TestLower(unittest.TestCase):
    def test_lower(self):
        self.assertEqual(lower("wow"), "wow")
        self.assertEqual(lower("HellZo"), "hellzo")
        self.assertEqual(lower("WHAT"), "what")
        self.assertEqual(lower("wh[]32"), "wh[]32")
        self.assertEqual(lower("whAT"), "what")


if __name__ == "__main__":
    unittest.main()
