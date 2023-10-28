import matplotlib.pyplot as plt
import numpy as np


class FuzzySet:
    """
    A class for representing and manipulating triangular fuzzy sets.
    Attributes:
        name (str): The name or label of the fuzzy set.
        left_boundary (float): The left boundary of the fuzzy set.
        peak (float): The peak (central) value of the fuzzy set.
        right_boundary (float): The right boundary of the fuzzy set.
    Methods:
        membership(x): Calculate the membership value of an
        input 'x' in the fuzzy set.
        union(other): Calculate the union of
        this fuzzy set with another fuzzy set.
        intersection(other): Calculate the intersection of
        this fuzzy set with another fuzzy set.
        complement(): Calculate the complement (negation) of
        this fuzzy set.
        plot(): Plot the membership function of the fuzzy set.
    """

    def __init__(
        self, name: str, left_boundary: float, peak: float, right_boundary: float
    ) -> None:
        """
        Initializes a triangular fuzzy set with the given parameters.
        Args:
            name (str): The name or label of the fuzzy set.
            left_boundary (float): The left boundary of the fuzzy set.
            peak (float): The peak (central) value of the fuzzy set.
            right_boundary (float): The right boundary of the fuzzy set.
        """
        self.name = name  # Fuzzy set name
        self.left_boundary = left_boundary  # Left boundary
        self.peak = peak  # Peak value
        self.right_boundary = right_boundary  # Right boundary

    def membership(self, x: float) -> float:
        """
    Calculate the membership value of an input 'x' in the fuzzy set.
    Returns:
        float: The membership value of 'x' in the fuzzy set.
    """
        if x <= self.left_boundary or x >= self.right_boundary:
            return 0.0
        elif self.left_boundary < x <= self.peak:
            return (x - self.left_boundary) / (self.peak - self.left_boundary)
        elif self.peak < x < self.right_boundary:
            return (self.right_boundary - x) / (self.right_boundary - self.peak)


    def union(self, other) -> "FuzzySet":
        """
        Calculate the union of this fuzzy set with another fuzzy set.
        Args:
            other (FuzzySet): Another fuzzy set to union with.
        Returns:
            FuzzySet: A new fuzzy set representing the union.
        """
        union_name = f"{self.name} ∪ {other.name}"
        return FuzzySet(
            union_name,
            min(self.left_boundary, other.left_boundary),
            max(self.right_boundary, other.right_boundary),
            (self.peak + other.peak) / 2,
        )

    def intersection(self, other) -> "FuzzySet":
        """
        Calculate the intersection of this fuzzy set
        with another fuzzy set.
        Args:
            other (FuzzySet): Another fuzzy set to intersect with.
        Returns:
            FuzzySet: A new fuzzy set representing the intersection.
        """
        intersection_name = f"{self.name} ∩ {other.name}"
        return FuzzySet(
            intersection_name,
            max(self.left_boundary, other.left_boundary),
            min(self.right_boundary, other.right_boundary),
            (self.peak + other.peak) / 2,
        )

    def complement(self) -> "FuzzySet":
        """
        Calculate the complement (negation) of this fuzzy set.
        Returns:
            FuzzySet: A new fuzzy set representing the complement.
        """
        complement_name = f"¬{self.name}"
        return FuzzySet(
            complement_name,
            1 - self.right_boundary,
            1 - self.left_boundary,
            1 - self.peak,
        )

    def plot(self):
        """
        Plot the membership function of the fuzzy set.
        """
        x = np.linspace(0, 1, 1000)
        y = [self.membership(xi) for xi in x]

        plt.plot(x, y, label=self.name)

    def __str__(self):
        return (
            f"{self.name}: [{self.left_boundary}, {self.peak}, {self.right_boundary}]"
        )


if __name__ == "__main__":
    a = FuzzySet("A", 0, 0.5, 1)
    b = FuzzySet("B", 0.2, 0.7, 1)

    a.plot()
    b.plot()

    plt.xlabel("x")
    plt.ylabel("Membership")
    plt.legend()
    plt.show()

    union_ab = a.union(b)
    intersection_ab = a.intersection(b)
    complement_a = a.complement()

    union_ab.plot()
    intersection_ab.plot()
    complement_a.plot()

    plt.xlabel("x")
    plt.ylabel("Membership")
    plt.legend()
    plt.show()
