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
        membership(element): Calculate the membership value of
        an input 'element' in the fuzzy set.
        union(other): Calculate the union of a fuzzyset with other fuzzyset
        intersection(other): Calculate the intersection of this fuzzy set with other.
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

    >>> sheru.complement()
    FuzzySet(name='¬Sheru', left_boundary=0.4, peak=0.6, right_boundary=0)
    >>> siya.complement()  # doctest: +NORMALIZE_WHITESPACE
    FuzzySet(name='¬Siya', left_boundary=0.30000000000000004, peak=0.5,
    right_boundary=0)

    >>> siya.intersection(sheru)
    FuzzySet(name='Siya ∩ Sheru', left_boundary=0.5, peak=0.6, right_boundary=1.0)

    >>> sheru.membership(0.5)
    0.16666666666666663
    >>> sheru.membership(0.6)
    0.0

    >>> siya.union(sheru)
    FuzzySet(name='Siya ∪ Sheru', left_boundary=0.4, peak=0.7, right_boundary=1.0)
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

    def __contains__(self, element: float) -> bool:
        """
        Check if an element 'element' is a member of the fuzzy set.
        Returns:
            True if 'x' is a member; False otherwise.
        >>> a = FuzzySet("A", 0, 0.5, 1)
        >>> 0.0 in a
        False
        >>> 0.6 in a
        True
        """
        return self.membership(element) > 0

    def __and__(self, other: FuzzySet) -> FuzzySet:
        """
        Calculate the intersection of this fuzzy set with another fuzzy set.
        Args:
            other (FuzzySet): Another fuzzy set to intersect with.
        Returns:
            FuzzySet: A new fuzzy set representing the intersection.

        >>> FuzzySet("A", 0, 0.5, 1) & FuzzySet("B", 0.2, 0.7, 1)
        FuzzySet(name='A ∩ B', left_boundary=0.2, peak=1, right_boundary=0.6)
        """
        return FuzzySet(
            f"{self.name} ∩ {other.name}",
            max(self.left_boundary, other.left_boundary),
            min(self.right_boundary, other.right_boundary),
            (self.peak + other.peak) / 2,
        )

    def __or__(self, other: FuzzySet) -> FuzzySet:
        """
        Calculate the union of this fuzzy set with another fuzzy set.
        Args:
            other (FuzzySet): Another fuzzy set to union with.
        Returns:
            FuzzySet: A new fuzzy set representing the union.

        >>> FuzzySet("A", 0, 0.5, 1) | FuzzySet("B", 0.2, 0.7, 1)
        FuzzySet(name='A ∪ B', left_boundary=0, peak=1, right_boundary=0.6)
        """
        union_name = f"{self.name} ∪ {other.name}"
        return FuzzySet(
            union_name,
            min(self.left_boundary, other.left_boundary),
            max(self.right_boundary, other.right_boundary),
            (self.peak + other.peak) / 2,
        )

    def __invert__(self) -> FuzzySet:
        """
        Calculate the complement (negation) of this fuzzy set.
        Returns:
            FuzzySet: A new fuzzy set representing the complement.

        >>> ~FuzzySet("A", 0, 0.5, 1)
        FuzzySet(name='¬A', left_boundary=0, peak=1, right_boundary=0.5)
        """
        return FuzzySet(
            f"¬{self.name}",
            1 - self.right_boundary,
            1 - self.left_boundary,
            1 - self.peak,
        )

    def complement(self) -> FuzzySet:
        """
        Calculate the complement (negation) of this fuzzy set.
        Returns:
            A new fuzzy set representing the complement.

        >>> FuzzySet("fuzzy_set", 0.1, 0.2, 0.3).complement()
        FuzzySet(name='¬fuzzy_set', left_boundary=0.7, peak=0.9, right_boundary=0.8)
        """
        return FuzzySet(
            f"¬{self.name}",
            1 - self.right_boundary,
            1 - self.left_boundary,
            1 - self.peak,
        )

    def intersection(self, second_fuzzy_set) -> FuzzySet:
        """
        Calculate the intersection of two fuzzysets
        Args:
            other: Another fuzzy set to intersect with.
        Returns:
            A new fuzzy set representing the intersection.

        >>> FuzzySet("a", 0.1, 0.2, 0.3).intersection(FuzzySet("b", 0.4, 0.5, 0.6))
        FuzzySet(name='a ∩ b', left_boundary=0.4, peak=0.3, right_boundary=0.35)
        """
        return FuzzySet(
            f"{self.name} ∩ {second_fuzzy_set.name}",
            max(self.left_boundary, second_fuzzy_set.left_boundary),
            min(self.right_boundary, second_fuzzy_set.right_boundary),
            (self.peak + second_fuzzy_set.peak) / 2,
        )

    def membership(self, element: float) -> float:
        """
        Calculate the membership value of an input 'element' in the fuzzy set.
        Returns:
            The membership value of 'element' in the fuzzy set.

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
        if element <= self.left_boundary or element >= self.right_boundary:
            return 0.0
        elif self.left_boundary < element <= self.peak:
            return (element - self.left_boundary) / (self.peak - self.left_boundary)
        elif self.peak < element < self.right_boundary:
            return (self.right_boundary - element) / (self.right_boundary - self.peak)
        elif self.peak == element:
            return 1.0

        msg = f"Invalid value {element} for fuzzy set {self}"
        raise ValueError(msg)

    def union(self, second_fuzzy_set) -> FuzzySet:
        """
        Calculate the union of this fuzzy set with another fuzzy set.
        Args:
            other: Another fuzzy set to union with.
        Returns:
            A new fuzzy set representing the union.

        >>> FuzzySet("a", 0.1, 0.2, 0.3).union(FuzzySet("b", 0.4, 0.5, 0.6))
        FuzzySet(name='a ∪ b', left_boundary=0.1, peak=0.6, right_boundary=0.35)
        """
        return FuzzySet(
            f"{self.name} ∪ {second_fuzzy_set.name}",
            min(self.left_boundary, second_fuzzy_set.left_boundary),
            max(self.right_boundary, second_fuzzy_set.right_boundary),
            (self.peak + second_fuzzy_set.peak) / 2,
        )

    def plot(self) -> None:
        """
        Plot the membership function of the fuzzy set.
        """
        x_axis = np.linspace(0, 1, 1000)
        y_axis = [self.membership(xi) for xi in x_axis]

        plt.plot(x_axis, y_axis, label=self.name)


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
