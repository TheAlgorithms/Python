"""
By @Shreya123714
https://en.wikipedia.org/wiki/Fuzzy_set
https://en.wikipedia.org/wiki/Fuzzy_set_operations
https://en.wikipedia.org/wiki/Membership_function_(mathematics)
"""

from __future__ import annotations

from dataclasses import dataclass

import matplotlib.pyplot as plt
import numpy as np


@dataclass
class TrapezoidalFuzzySet:
    """
    Represents and manipulates trapezoidal fuzzy sets.

    Attributes:
        name: The name or label of the fuzzy set.
        left_base: The left base of the trapezoid.
        left_peak: The top left vertex of the trapezoid.
        right_peak: The top right vertex of the trapezoid.
        right_base: The right base of the trapezoid.
        is_complement: Indicates if this is the complement of the fuzzy set.

    Methods:
        membership(value): Calculates membership value for input 'value'.
        complement(): Creates left_base TrapezoidalFuzzySet instance representing
            the complement.
        plot(): Plots the membership function of the fuzzy set.
    """

    name: str
    left_base: float
    left_peak: float
    right_peak: float
    right_base: float
    is_complement: bool = False  # Flag for complement set

    def membership(self, value: float) -> float:
        """
        Calculates membership value for input 'value'. For complement sets,
        returns 1 - trapezoidal membership.

        >>> TrapezoidalFuzzySet("Medium", 0, 1, 2, 3).membership(1)
        1.0
        >>> TrapezoidalFuzzySet("Medium", 0, 1, 2, 3).membership(0.5)
        0.5
        """
        if value < self.left_base or value > self.right_base:
            membership_value = 0.0
        elif self.left_base <= value < self.left_peak:
            membership_value = (value - self.left_base) / (
                self.left_peak - self.left_base
            )
        elif self.left_peak <= value <= self.right_peak:
            membership_value = 1.0
        elif self.right_peak < value <= self.right_base:
            membership_value = (self.right_base - value) / (
                self.right_base - self.right_peak
            )

        # For complements, invert the membership value
        return membership_value if not self.is_complement else 1 - membership_value

    def complement(self) -> TrapezoidalFuzzySet:
        """
        Creates a new TrapezoidalFuzzySet instance representing the complement.

        >>> TrapezoidalFuzzySet("Medium", 0, 1, 2, 3).complement().membership(1)
        0.0
        """
        return TrapezoidalFuzzySet(
            f"¬{self.name}",
            self.left_base,
            self.left_peak,
            self.right_peak,
            self.right_base,
            is_complement=not self.is_complement,
        )

    def plot(self) -> None:
        """
        Plots the membership function of the trapezoidal fuzzy set.
    
        >>> fuzzy_set = TrapezoidalFuzzySet("Medium", left_base=0,left_peak=1, 
        ...                                 right_peak=2, right_base=3)
        >>> fuzzy_set.plot()
        """
        x = np.linspace(self.left_base - 1, self.right_base + 1, 1000)
        y = [self.membership(xi) for xi in x]
        plt.plot(x, y, label=self.name)
        plt.xlabel("Value")
        plt.ylabel("Membership")
        plt.title(f"Membership Function for {self.name}")
        plt.grid()
        plt.legend()


if __name__ == "__main__":
    from doctest import testmod

    testmod()

    # Create an instance of TrapezoidalFuzzySet
    fuzzy_set = TrapezoidalFuzzySet(
        "Medium Temperature", left_base=20, left_peak=25, right_peak=30, right_base=35
    )

    # Display some membership values
    print(f"Membership at 25: {fuzzy_set.membership(25)}")
    print(f"Membership at 22: {fuzzy_set.membership(22)}")
    print(f"Complement Membership at 25: {fuzzy_set.complement().membership(25)}")

    # Plot of Trapezoidal Fuzzy Set and its complement
    fuzzy_set.plot()
    fuzzy_set.complement().plot()
    plt.title("Trapezoidal Fuzzy Set and its Complement")
    plt.show()
