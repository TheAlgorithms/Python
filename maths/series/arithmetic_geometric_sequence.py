#!/usr/bin/env python3
"""
This is a pure Python implementation of the Arithmetic–Geometric Sequence algorithm
https://en.wikipedia.org/wiki/Arithmetico%E2%80%93geometric_sequence
For doctests run following command:
python -m doctest -v arithmetic_geometric_sequence.py
or
python3 -m doctest -v arithmetic_geometric_sequence.py
For manual testing run:
python3 arithmetic_geometric_sequence.py
"""


class ArithmeticGeometricSequence:
    def __init__(
        self,
        arithmetic_value: float,
        arithmetic_difference: float,
        geometric_value: float,
        common_ratio: float,
        term_count: int,
    ) -> None:
        self.arithmetic_value = arithmetic_value
        self.arithmetic_difference = arithmetic_difference
        self.geometric_value = geometric_value
        self.common_ratio = common_ratio
        self.term_count = term_count

    """:params arithmetic_value: Initial Value For Arithmetic Progression
        arithmetic_difference: Difference For Arithmetic Progression
        geometric_value: Initial Value For Geometric Progression
        common_ratio: Common Ratio For Geometric Progression
        term_count: Number Of Terms
        k_in_kth_term: Value Of K In K-th Term
    """

    def full_series(self) -> list:
        """
        >>> ArithmeticGeometricSequence(2, 3, 5, 6, 3).full_series()
        ['2 x 5', '(2 + 3) x 5x6^1', '(2 + 6) x 5x6^2']
        >>> ArithmeticGeometricSequence(3, 2.1, 1.3, 0.4, 3).full_series()
        ['3 x 1.3', '(3 + 2.1) x 1.3x0.4^1', '(3 + 4.2) x 1.3x0.4^2']
        >>> ArithmeticGeometricSequence(9, 3, 2, -0.5, 1).full_series()
        ['9 x 2']
        """
        series = []
        for i in range(self.term_count):
            if i == 0:
                series.append(f"{self.arithmetic_value} x {self.geometric_value}")
            else:
                ap_part = f"{self.arithmetic_value} + {i * self.arithmetic_difference}"
                gp_part = f"{self.geometric_value}x{self.common_ratio}^{i}"
                series.append(f"({ap_part}) x {gp_part}")
        return series

    def last_term_value(self) -> float:
        """
        >>> ArithmeticGeometricSequence(2, 3, 5, 6, 3).last_term_value()
        1440
        >>> ArithmeticGeometricSequence(3, 2.1, 1.3, 0.4, 3).last_term_value()
        1.4976000000000003
        >>> ArithmeticGeometricSequence(9, 3, 2, -0.5, 1).last_term_value()
        18.0
        """
        return (
            self.arithmetic_value + (self.term_count - 1) * self.arithmetic_difference
        ) * (self.geometric_value * pow(self.common_ratio, self.term_count - 1))

    def sum(self) -> float:
        """
        >>> ArithmeticGeometricSequence(2, 3, 5, 6, 3).sum()
        1600.0
        >>> ArithmeticGeometricSequence(3, 2.1, 1.3, 0.4, 3).sum()
        8.049600000000002
        >>> ArithmeticGeometricSequence(9, 3, 2, -0.5, 1).sum()
        18.0
        """
        return (
            (self.arithmetic_value * self.geometric_value)
            - (
                (self.arithmetic_value + (self.term_count * self.arithmetic_difference))
                * (self.geometric_value * pow(self.common_ratio, self.term_count))
            )
        ) / (1 - self.common_ratio) + (
            self.arithmetic_difference
            * self.geometric_value
            * self.common_ratio
            * (1 - pow(self.common_ratio, self.term_count))
        ) / pow(
            (1 - self.common_ratio), 2
        )

    def inf_sum(self) -> float:
        """
        >>> ArithmeticGeometricSequence(2, 3, 5, 6, 3).inf_sum()
        1.6
        >>> ArithmeticGeometricSequence(3, 2.1, 1.3, 0.4, 3).inf_sum()
        9.533333333333335
        >>> ArithmeticGeometricSequence(9, 3, 2, -0.5, 1).inf_sum()
        10.666666666666666
        """
        return (self.arithmetic_value * self.geometric_value) / (
            1 - self.common_ratio
        ) + (
            self.arithmetic_difference * self.geometric_value * self.common_ratio
        ) / pow(
            (1 - self.common_ratio), 2
        )

    def kth_term_value(self, k_in_kth_term: int) -> float:
        """
        >>> ArithmeticGeometricSequence(2, 3, 5, 6, 3).kth_term_value(2)
        150
        >>> ArithmeticGeometricSequence(3, 2.1, 1.3, 0.4, 3).kth_term_value(1)
        3.9000000000000004
        >>> ArithmeticGeometricSequence(9, 3, 2, -0.5, 1).kth_term_value(1)
        18.0
        """
        return (
            self.arithmetic_value + (k_in_kth_term - 1) * self.arithmetic_difference
        ) * (self.geometric_value * pow(self.common_ratio, k_in_kth_term - 1))


def main():
    run = True
    while run:
        try:
            arithmetic_value = float(input("\nEnter Initial Value For A.P. : ").strip())
            run = False
        except ValueError:
            print("Please Give A Number For Corresponding Input!")
    run = True
    while run:
        try:
            arithmetic_difference = float(input("Enter Difference For A.P. : ").strip())
            run = False
        except ValueError:
            print("Please Give A Number For Corresponding Input!")
    run = True
    while run:
        try:
            geometric_value = float(input("Enter Initial Value For G.P. : ").strip())
            run = False
        except ValueError:
            print("Please Give A Number For Corresponding Input!")
    run = True
    while run:
        try:
            common_ratio = float(input("Enter Common Ratio For G.P. : ").strip())
            if common_ratio == 1:
                print("Common Ratio Must Not Be 1")
            else:
                run = False
        except ValueError:
            print("Please Give A Number For Corresponding Input!")
    not_get_number_of_term = True
    while not_get_number_of_term:
        try:
            term_count = int(input("Enter Number Of Terms : ").strip())
            if term_count <= 0:
                print("Give A Positive Integer.")
            else:
                not_get_number_of_term = False
        except ValueError:
            print("Please Give An Integer As The Number Of Terms!")

    arithmetic_geometric_sequence_object = ArithmeticGeometricSequence(
        arithmetic_value,
        arithmetic_difference,
        geometric_value,
        common_ratio,
        term_count,
    )

    print(f"\nFull Series : \n{arithmetic_geometric_sequence_object.full_series()}")
    print(
        f"\nValue Of Last Term : {arithmetic_geometric_sequence_object.last_term_value()}"
    )
    print(f"Sum Of Your A.G.S. : {arithmetic_geometric_sequence_object.sum()}")
    print(f"Infinite Series Sum : {arithmetic_geometric_sequence_object.inf_sum()}")

    not_get_k_in_kth_term = True
    while not_get_k_in_kth_term:
        try:
            k_in_kth_term = int(input("\nValue Of Which Term You Want : ").strip())
            if term_count >= k_in_kth_term >= 1:
                not_get_k_in_kth_term = False
            else:
                print(f"Give an Integer belongs to [1, {term_count}]")
        except ValueError:
            print("Please Give Integer For Corresponding Input!")

    print(
        f"Value Of {k_in_kth_term}th Term : {arithmetic_geometric_sequence_object.kth_term_value(k_in_kth_term)}"
    )


if __name__ == "__main__":
    import doctest

    doctest.testmod()
    main()
