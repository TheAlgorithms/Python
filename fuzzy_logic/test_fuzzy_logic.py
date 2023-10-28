import unittest
from fuzzy_operations import FuzzySet


class TestFuzzySet(unittest.TestCase):
    def test_membership_within_boundaries(self):
        A = FuzzySet("A", 0, 0.5, 1)
<<<<<<< Updated upstream

        self.assertAlmostEqual(A.membership(0), 1.0)  # Left boundary
        self.assertAlmostEqual(A.membership(0.25), 0.5)  # Peak value
        self.assertAlmostEqual(A.membership(0.5), 0.0)  # Right boundary

    def test_membership_outside_boundaries(self):
        A = FuzzySet("A", 0, 0.5, 1)

        self.assertAlmostEqual(A.membership(0.75), 0.0)  # Outside boundaries
        self.assertAlmostEqual(A.membership(-0.1), 0.0)  # Outside boundaries

    def test_union(self):
        A = FuzzySet("A", 0, 0.5, 1)
        B = FuzzySet("B", 0.2, 0.7, 1)

        union_ab = A.union(B)

        self.assertAlmostEqual(union_ab.membership(0.1), 1.0)  # Member of A
        self.assertAlmostEqual(union_ab.membership(0.35), 0.5)  # Member of both A and B
        self.assertAlmostEqual(union_ab.membership(0.75), 0.0)  # Outside boundaries
=======
        
        self.assertEqual(A.membership(0), 1.0)  # Left boundary
        self.assertEqual(A.membership(0.25), 0.5)  # Peak value
        self.assertEqual(A.membership(0.5), 0.0)  # Right boundary

    def test_membership_outside_boundaries(self):
        a = FuzzySet("A", 0, 0.5, 1)
        
        self.assertEqual(a.membership(0.75), 0.0)  # Outside boundaries
        self.assertEqual(a.membership(-0.1), 0.0)  # Outside boundaries

    def test_union(self):
        a = FuzzySet("A", 0, 0.5, 1)
        b = FuzzySet("B", 0.2, 0.7, 1)
        
        union_ab = a.union(b)
        
        self.assertEqual(union_ab.membership(0.1), 1.0)  # Member of A
        self.assertEqual(union_ab.membership(0.35), 0.5)  # Member of both A and B
        self.assertEqual(union_ab.membership(0.75), 0.0)  # Outside boundaries
>>>>>>> Stashed changes

    def test_intersection(self):
        A = FuzzySet("A", 0, 0.5, 1)
        B = FuzzySet("B", 0.2, 0.7, 1)

        intersection_ab = A.intersection(B)
<<<<<<< Updated upstream

        self.assertAlmostEqual(
            intersection_ab.membership(0.1), 0.0
        )  # Not a member of B
        self.assertAlmostEqual(
            intersection_ab.membership(0.35), 0.5
        )  # Member of both A and B
        self.assertAlmostEqual(
            intersection_ab.membership(0.75), 0.0
        )  # Not a member of A

    def test_complement(self):
        A = FuzzySet("A", 0, 0.5, 1)

        complement_a = A.complement()

        self.assertAlmostEqual(complement_a.membership(0.1), 0.0)  # Member of A
        self.assertAlmostEqual(complement_a.membership(0.75), 1.0)  # Outside boundaries
=======
        
        self.assertEqual(intersection_ab.membership(0.1), 0.0)  # Not a member of B
        self.assertEqual(intersection_ab.membership(0.35), 0.5)  # Member of both A and B
        self.assertEqual(intersection_ab.membership(0.75), 0.0)  # Not a member of A

    def test_complement(self):
        a = FuzzySet("a", 0, 0.5, 1)
        
        complement_a = a.complement()
        
        self.assertEqual(complement_a.membership(0.1), 0.0)  # Member of A
        self.assertEqual(complement_a.membership(0.75), 1.0)  # Outside boundaries
>>>>>>> Stashed changes


if __name__ == "__main__":
    unittest.main()
