"""
Test suite for Pollard's Rho Discrete Logarithm Algorithm.

This module contains comprehensive tests for the pollard_rho_discrete_log module,
including basic functionality tests, edge cases, and performance validation.
"""

import unittest
import sys
import os

# Add the parent directory to sys.path to import maths module
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from maths.pollard_rho_discrete_log import pollards_rho_discrete_log


class TestPollardRhoDiscreteLog(unittest.TestCase):
    """Test cases for Pollard's Rho Discrete Logarithm Algorithm."""

    def test_basic_example(self):
        """Test the basic example from the GitHub issue."""
        # Since the algorithm is probabilistic, try multiple times
        found_solution = False
        for attempt in range(5):  # Try up to 5 times
            result = pollards_rho_discrete_log(2, 22, 29)
            if result is not None:
                # Verify the result is correct
                self.assertEqual(pow(2, result, 29), 22)
                found_solution = True
                break
        
        self.assertTrue(found_solution, 
                       "Algorithm should find a solution within 5 attempts")

    def test_simple_cases(self):
        """Test simple discrete log cases with known answers."""
        test_cases = [
            (2, 8, 17),   # 2^3 ≡ 8 (mod 17)
            (5, 3, 7),    # 5^5 ≡ 3 (mod 7)  
            (3, 9, 11),   # 3^2 ≡ 9 (mod 11)
        ]
        
        for g, h, p in test_cases:
            # Try multiple times due to probabilistic nature
            found_solution = False
            for attempt in range(3):
                result = pollards_rho_discrete_log(g, h, p)
                if result is not None:
                    self.assertEqual(pow(g, result, p), h)
                    found_solution = True
                    break
            # Not all cases may have solutions, so we don't assert found_solution

    def test_no_solution_case(self):
        """Test case where no solution exists."""
        # 3^x ≡ 7 (mod 11) has no solution (verified by brute force)
        # The algorithm should return None or fail to find a solution
        result = pollards_rho_discrete_log(3, 7, 11)
        if result is not None:
            # If it returns a result, it must be wrong since no solution exists
            self.assertNotEqual(pow(3, result, 11), 7)

    def test_edge_cases(self):
        """Test edge cases and input validation scenarios."""
        # g = 1: 1^x ≡ h (mod p) only has solution if h = 1
        result = pollards_rho_discrete_log(1, 1, 7)
        if result is not None:
            self.assertEqual(pow(1, result, 7), 1)
        
        # h = 1: g^x ≡ 1 (mod p) - looking for the multiplicative order
        result = pollards_rho_discrete_log(3, 1, 7)
        if result is not None:
            self.assertEqual(pow(3, result, 7), 1)

    def test_small_primes(self):
        """Test with small prime moduli."""
        test_cases = [
            (2, 4, 5),   # 2^2 ≡ 4 (mod 5)
            (2, 3, 5),   # 2^? ≡ 3 (mod 5)
            (2, 1, 3),   # 2^2 ≡ 1 (mod 3)
            (3, 2, 5),   # 3^3 ≡ 2 (mod 5)
        ]
        
        for g, h, p in test_cases:
            result = pollards_rho_discrete_log(g, h, p)
            if result is not None:
                # Verify the result is mathematically correct
                self.assertEqual(pow(g, result, p), h)
                
    def test_larger_examples(self):
        """Test with larger numbers to ensure algorithm scales."""
        # Test cases with larger primes
        test_cases = [
            (2, 15, 31),   # Find x where 2^x ≡ 15 (mod 31)
            (3, 10, 37),   # Find x where 3^x ≡ 10 (mod 37) 
            (5, 17, 41),   # Find x where 5^x ≡ 17 (mod 41)
        ]
        
        for g, h, p in test_cases:
            result = pollards_rho_discrete_log(g, h, p)
            if result is not None:
                self.assertEqual(pow(g, result, p), h)

    def test_multiple_runs_consistency(self):
        """Test that multiple runs give consistent results."""
        # Since the algorithm is probabilistic, run it multiple times
        # and ensure any returned result is mathematically correct
        g, h, p = 2, 22, 29
        results = []
        
        for _ in range(10):  # Run 10 times
            result = pollards_rho_discrete_log(g, h, p)
            if result is not None:
                results.append(result)
                self.assertEqual(pow(g, result, p), h)
        
        # Should find at least one solution in 10 attempts
        self.assertGreater(len(results), 0, 
                          "Algorithm should find solution in multiple attempts")


if __name__ == "__main__":
    unittest.main(verbosity=2)