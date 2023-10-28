import matplotlib.pyplot as plt
import numpy as np

""""
 FuzzySet class for triangular fuzzy sets
 Author: Shreya123714
 Source: https://en.wikipedia.org/wiki/Fuzzy_set
"""


class FuzzySet:
    """
    A class for representing and 
    manipulating triangular fuzzy sets.

    Attributes:
        name (str): The name or label of the fuzzy set.
        a (float): The left boundary of the fuzzy set.
        b (float): The peak (central) value of the fuzzy set.
        c (float): The right boundary of the fuzzy set.

    Methods:
        membership(x): Calculate the membership value 
        of an input 'x' in the fuzzy set.
        union(other): Calculate the union of this fuzzy set 
        with another fuzzy set.
        intersection(other): Calculate the intersection of this fuzzy set 
        with another fuzzy set.
        complement(): Calculate the complement (negation) 
        of this fuzzy set.
        plot(): Plot the membership function of the fuzzy set.
    """

    def __init__(self, name, a, b, c):
        """
        Initializes a triangular fuzzy set 
        with the given parameters.

        Args:
            name (str): The name or label of the fuzzy set.
            a (float): The left boundary of the fuzzy set.
            b (float): The peak (central) value of 
            the fuzzy set.
            c (float): The right boundary of the fuzzy set.
        """
        self.name = name  # Fuzzy set name
        self.a = a  # Left boundary
        self.b = b  # Peak value
        self.c = c  # Right boundary

    def membership(self, x):
        """
        Calculate the membership value of 
        an input 'x' in the fuzzy set.

        Args:
            x (float): The input value for 
            which the membership is calculated.

        Returns:
            float: The membership value of 'x' in 
            the fuzzy set.
        """

        if x <= self.a or x >= self.c:
            return 0
        elif self.a < x <= self.b:
            return (x - self.a) / (self.b - self.a)
        elif self.b < x < self.c:
            return (self.c - x) / (self.c - self.b)

    def union(self, other):
        """
        Calculate the union of this fuzzy set 
        with another fuzzy set.

        Args:
            other (FuzzySet): Another fuzzy set
            to union with.

        Returns:
            FuzzySet: A new fuzzy 
            set representing the union.
        """

        union_name = f"{self.name} ∪ {other.name}"
        return FuzzySet(
            union_name,
            min(self.a, other.a),
            max(self.c, other.c),
            (self.b + other.b) / 2,
        )

    def intersection(self, other):
        """
        Calculate the intersection of this 
        fuzzy set with another fuzzy set.

        Args:
            other (FuzzySet): Another fuzzy set to intersect with.

        Returns:
            FuzzySet: A new fuzzy set representing the intersection.
        """
        intersection_name = f"{self.name} ∩ {other.name}"
        return FuzzySet(
            intersection_name,
            max(self.a, other.a),
            min(self.c, other.c),
            (self.b + other.b) / 2,
        )

    def complement(self):
        """
        Calculate the complement (negation) of this fuzzy set.

        Returns:
            FuzzySet: A new fuzzy set representing the complement.
        """
        complement_name = f"¬{self.name}"
        return FuzzySet(complement_name, 1 - self.c, 1 - self.a, 1 - self.b)

    def plot(self):
        """
        Plot the membership function of the fuzzy set.
        """
        x = np.linspace(0, 1, 1000)
        y = [self.membership(xi) for xi in x]

        plt.plot(x, y, label=self.name)

    def __str__(self):
        return f"{self.name}: [{self.a}, {self.b}, {self.c}]"


# Example usage:
if __name__ == "__main__":
    A = FuzzySet("A", 0, 0.5, 1)
    B = FuzzySet("B", 0.2, 0.7, 1)

    A.plot()
    B.plot()

    plt.xlabel("x")
    plt.ylabel("Membership")
    plt.legend()
    plt.show()

    union_ab = A.union(B)
    intersection_ab = A.intersection(B)
    complement_a = A.complement()

    union_ab.plot()
    intersection_ab.plot()
    complement_a.plot()

    plt.xlabel("x")
    plt.ylabel("Membership")
    plt.legend()
    plt.show()
