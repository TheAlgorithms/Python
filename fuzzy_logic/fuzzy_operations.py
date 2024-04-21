"""
By @Shreya123714

https://en.wikipedia.org/wiki/Fuzzy_set
"""

from __future__ import annotations

from dataclasses import dataclass

import matplotlib.pyplot as plt
import numpy as np


@dataclass
class FuzzySet:
    """
    A class for representing and manipulating triangular fuzzy sets.
    Attributes:
        name: The name or label of the fuzzy set.
        left_boundary: The left boundary of the fuzzy set.
        peak: The peak (central) value of the fuzzy set.
        right_boundary: The right boundary of the fuzzy set.
    Methods:
        membership(x): Calculate the membership value of an input 'x' in the fuzzy set.
        union(other): Calculate the union of this fuzzy set with another fuzzy set.
        intersection(other): Calculate the intersection of this fuzzy set with another.
        complement(): Calculate the complement (negation) of this fuzzy set.
        plot(): Plot the membership function of the fuzzy set.

    >>> sheru = FuzzySet("Sheru", 0.4, 1, 0.6)
    >>> sheru
    FuzzySet(name='Sheru', left_boundary=0.4, peak=1, right_boundary=0.6)
    >>> str(sheru)
    'Sheru: [0.4, 1, 0.6]'

    >>> siya = FuzzySet("Siya", 0.5, 1, 0.7)
    >>> siya
    FuzzySet(name='Siya', left_boundary=0.5, peak=1, right_boundary=0.7)

    # Complement Operation
    >>> sheru.complement()
    FuzzySet(name='¬Sheru', left_boundary=0.4, peak=0.6, right_boundary=0)
    >>> siya.complement()  # doctest: +NORMALIZE_WHITESPACE
    FuzzySet(name='¬Siya', left_boundary=0.30000000000000004, peak=0.5,
     right_boundary=0)

    # Intersection Operation
    >>> siya.intersection(sheru)
    FuzzySet(name='Siya ∩ Sheru', left_boundary=0.5, peak=0.6, right_boundary=1.0)

    # Membership Operation
    >>> sheru.membership(0.5)
    0.16666666666666663
    >>> sheru.membership(0.6)
    0.0

    # Union Operations
    >>> siya.union(sheru)
    FuzzySet(name='Siya U Sheru', left_boundary=0.4, peak=0.7, right_boundary=1.0)
    """

    name: str
    left_boundary: float
    peak: float
    right_boundary: float

    def __str__(self) -> str:
        """
        >>> FuzzySet("fuzzy_set", 0.1, 0.2, 0.3)
        FuzzySet(name='fuzzy_set', left_boundary=0.1, peak=0.2, right_boundary=0.3)
        """
        return (
            f"{self.name}: [{self.left_boundary}, {self.peak}, {self.right_boundary}]"
        )

    def complement(self) -> FuzzySet:
        """
        Calculate the complement (negation) of this fuzzy set.
        Returns:
            FuzzySet: A new fuzzy set representing the complement.

        >>> FuzzySet("fuzzy_set", 0.1, 0.2, 0.3).complement()
        FuzzySet(name='¬fuzzy_set', left_boundary=0.7, peak=0.9, right_boundary=0.8)
        """
        return FuzzySet(
            f"¬{self.name}",
            1 - self.right_boundary,
            1 - self.left_boundary,
            1 - self.peak,
        )

    def intersection(self, other) -> FuzzySet:
        """
        Calculate the intersection of this fuzzy set
        with another fuzzy set.
        Args:
            other: Another fuzzy set to intersect with.
        Returns:
            A new fuzzy set representing the intersection.

        >>> FuzzySet("a", 0.1, 0.2, 0.3).intersection(FuzzySet("b", 0.4, 0.5, 0.6))
        FuzzySet(name='a ∩ b', left_boundary=0.4, peak=0.3, right_boundary=0.35)
        """
        return FuzzySet(
            f"{self.name} ∩ {other.name}",
            max(self.left_boundary, other.left_boundary),
            min(self.right_boundary, other.right_boundary),
            (self.peak + other.peak) / 2,
        )

    def membership(self, x: float) -> float:
        """
        Calculate the membership value of an input 'x' in the fuzzy set.
        Returns:
            The membership value of 'x' in the fuzzy set.

        >>> a = FuzzySet("a", 0.1, 0.2, 0.3)
        >>> a.membership(0.09)
        0.0
        >>> a.membership(0.1)
        0.0
        >>> a.membership(0.11)
        0.09999999999999995
        >>> a.membership(0.4)
        0.0
        >>> FuzzySet("A", 0, 0.5, 1).membership(0.1)
        0.2
        >>> FuzzySet("B", 0.2, 0.7, 1).membership(0.6)
        0.8
        """
        if x <= self.left_boundary or x >= self.right_boundary:
            return 0.0
        elif self.left_boundary < x <= self.peak:
            return (x - self.left_boundary) / (self.peak - self.left_boundary)
        elif self.peak < x < self.right_boundary:
            return (self.right_boundary - x) / (self.right_boundary - self.peak)
        msg = f"Invalid value {x} for fuzzy set {self}"
        raise ValueError(msg)

    def union(self, other) -> FuzzySet:
        """
        Calculate the union of this fuzzy set with another fuzzy set.
        Args:
            other (FuzzySet): Another fuzzy set to union with.
        Returns:
            FuzzySet: A new fuzzy set representing the union.

        >>> FuzzySet("a", 0.1, 0.2, 0.3).union(FuzzySet("b", 0.4, 0.5, 0.6))
        FuzzySet(name='a U b', left_boundary=0.1, peak=0.6, right_boundary=0.35)
        """
        return FuzzySet(
            f"{self.name} U {other.name}",
            min(self.left_boundary, other.left_boundary),
            max(self.right_boundary, other.right_boundary),
            (self.peak + other.peak) / 2,
        )

    def plot(self):
        """
        Plot the membership function of the fuzzy set.
        """
        x = np.linspace(0, 1, 1000)
        y = [self.membership(xi) for xi in x]

        plt.plot(x, y, label=self.name)


if __name__ == "__main__":
    from doctest import testmod

    testmod()
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
