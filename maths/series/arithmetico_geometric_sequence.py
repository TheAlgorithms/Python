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


class AGS:
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
        >>> AGS(2, 3, 5, 6, 3).full_series()
        ['2 x 5', '(2 + 3) x 5x6^1', '(2 + 6) x 5x6^2']
        >>> AGS(3, 2.1, 1.3, 0.4, 3).full_series()
        ['3 x 1.3', '(3 + 2.1) x 1.3x0.4^1', '(3 + 4.2) x 1.3x0.4^2']
        >>> AGS(9, 3, 2, -0.5, 0).full_series()
        []
        """
        series = []
        for i in range(self.term_count):
            if i == 0:
                series.append(
                    str(self.arithmetic_value) + " x " + str(self.geometric_value)
                )
            else:
                ap_part = (
                    str(self.arithmetic_value)
                    + " + "
                    + str(i * self.arithmetic_difference)
                )
                gp_part = (
                    str(self.geometric_value)
                    + "x"
                    + str(self.common_ratio)
                    + "^"
                    + str(i)
                )
                series.append(f"({ap_part}) x {gp_part}")
        return series

    def last_term_value(self) -> float:
        """
        >>> AGS(2, 3, 5, 6, 3).last_term_value()
        1440
        >>> AGS(3, 2.1, 1.3, 0.4, 3).last_term_value()
        1.4976000000000003
        >>> AGS(9, 3, 2, -0.5, 0).last_term_value()
        'None'
        """
        if self.term_count == 0:
            return "None"
        return (
            self.arithmetic_value + (self.term_count - 1) * self.arithmetic_difference
        ) * (self.geometric_value * pow(self.common_ratio, self.term_count - 1))

    def sum(self) -> float:
        """
        >>> AGS(2, 3, 5, 6, 3).sum()
        1600.0
        >>> AGS(3, 2.1, 1.3, 0.4, 3).sum()
        8.049600000000002
        >>> AGS(9, 3, 2, -0.5, 0).sum()
        'None'
        """
        if self.term_count == 0:
            return "None"
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
        >>> AGS(2, 3, 5, 6, 3).inf_sum()
        1.6
        >>> AGS(3, 2.1, 1.3, 0.4, 3).inf_sum()
        9.533333333333335
        >>> AGS(9, 3, 2, -0.5, 0).inf_sum()
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
        >>> AGS(2, 3, 5, 6, 3).kth_term_value(2)
        150
        >>> AGS(3, 2.1, 1.3, 0.4, 3).kth_term_value(1)
        3.9000000000000004
        >>> AGS(9, 3, 2, -0.5, 0).kth_term_value(0)
        'None'
        """
        if k_in_kth_term == 0:
            return "None"
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
            run = False
        except ValueError:
            print("Please Give A Number For Corresponding Input!")
    not_get_number_of_term = True
    while not_get_number_of_term:
        try:
            term_count = int(input("Enter Number Of Terms : ").strip())
            if term_count < 0:
                print("Give A Positive Integer Including Zero.")
            else:
                not_get_number_of_term = False
        except ValueError:
            print("Please Give An Integer As The Number Of Terms!")

    ags = AGS(
        arithmetic_value,
        arithmetic_difference,
        geometric_value,
        common_ratio,
        term_count,
    )

    print(f"\nFull Series : \n{ags.full_series()}")
    print(f"\nValue Of Last Term : {ags.last_term_value()}")
    print(f"Sum Of Your A.G.S. : {ags.sum()}")
    print(f"Infinite Series Sum : {ags.inf_sum()}")

    not_get_k_in_kth_term = True
    while not_get_k_in_kth_term:
        try:
            k_in_kth_term = int(input("\nValue Of Which Term You Want : ").strip())
            if term_count >= k_in_kth_term >= 0:
                not_get_k_in_kth_term = False
            else:
                print(f"Give an Integer belongs to [0, {term_count}]")
        except ValueError:
            print("Please Give Integer For Corresponding Input!")

    print(f"Value Of {k_in_kth_term}th Term : {ags.kth_term_value(k_in_kth_term)}")


if __name__ == "__main__":
    import doctest

    doctest.testmod()
    main()
