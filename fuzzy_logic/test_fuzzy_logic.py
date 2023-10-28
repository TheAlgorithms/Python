import unittest
from fuzzy_operations import FuzzySet


class TestFuzzySet(unittest.TestCase):
    def setUp(self):
        self.A = FuzzySet("A", 0, 0.5, 1)
        self.B = FuzzySet("B", 0.2, 0.7, 1)

    def test_membership_within_boundaries(self):
        self.assertEqual(self.A.membership(0.1), 0.2)  # Modify with the expected value
        self.assertEqual(self.B.membership(0.6), 0.8)  # Modify with the expected value

    def test_union(self):
        union_ab = self.A.union(self.B)
        self.assertEqual(
            union_ab.membership(0.1), 0.1
        )  # Modify with the expected value
        self.assertEqual(
            union_ab.membership(0.35), 0.35
        )  # Modify with the expected value

    def test_intersection(self):
        intersection_ab = self.A.intersection(self.B)
        self.assertEqual(
            intersection_ab.membership(0.1), 0.0
        )  # Modify with the expected value
        self.assertEqual(
            intersection_ab.membership(0.35), 0.18749999999999994
        )  # Modify with the expected value

    def test_complement(self):
        complement_a = self.A.complement()
        self.assertEqual(
            complement_a.membership(0.1), 0.1
        )  # Modify with the expected value
        self.assertEqual(
            complement_a.membership(0.75), 0.0
        )  # Modify with the expected value


if __name__ == "__main__":
    unittest.main()
