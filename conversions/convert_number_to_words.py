from enum import Enum
from typing import ClassVar, Literal


class NumberingSystem(Enum):
    SHORT = (
        (15, "quadrillion"),
        (12, "trillion"),
        (9, "billion"),
        (6, "million"),
        (3, "thousand"),
        (2, "hundred"),
    )

    LONG = (
        (15, "billiard"),
        (9, "milliard"),
        (6, "million"),
        (3, "thousand"),
        (2, "hundred"),
    )

    INDIAN = (
        (14, "crore crore"),
        (12, "lakh crore"),
        (7, "crore"),
        (5, "lakh"),
        (3, "thousand"),
        (2, "hundred"),
    )

    @classmethod
    def max_value(cls, system: str) -> int:
        """
        Gets the max value supported by the given number system.

        >>> NumberingSystem.max_value("short") == 10**18 - 1
        True
        >>> NumberingSystem.max_value("long") == 10**21 - 1
        True
        >>> NumberingSystem.max_value("indian") == 10**19 - 1
        True
        """
        match (system_enum := cls[system.upper()]):
            case cls.SHORT:
                max_exp = system_enum.value[0][0] + 3
            case cls.LONG:
                max_exp = system_enum.value[0][0] + 6
            case cls.INDIAN:
                max_exp = 19
            case _:
                raise ValueError("Invalid numbering system")
        return 10**max_exp - 1


class NumberWords(Enum):
    ONES: ClassVar[dict[int, str]] = {
        0: "",
        1: "one",
        2: "two",
        3: "three",
        4: "four",
        5: "five",
        6: "six",
        7: "seven",
        8: "eight",
        9: "nine",
    }

    TEENS: ClassVar[dict[int, str]] = {
        0: "ten",
        1: "eleven",
        2: "twelve",
        3: "thirteen",
        4: "fourteen",
        5: "fifteen",
        6: "sixteen",
        7: "seventeen",
        8: "eighteen",
        9: "nineteen",
    }

    TENS: ClassVar[dict[int, str]] = {
        2: "twenty",
        3: "thirty",
        4: "forty",
        5: "fifty",
        6: "sixty",
        7: "seventy",
        8: "eighty",
        9: "ninety",
    }


def convert_small_number(num: int) -> str:
    """
    Converts small, non-negative integers with irregular constructions in English (i.e.,
    numbers under 100) into words.

    >>> convert_small_number(0)
    'zero'
    >>> convert_small_number(5)
    'five'
    >>> convert_small_number(10)
    'ten'
    >>> convert_small_number(15)
    'fifteen'
    >>> convert_small_number(20)
    'twenty'
    >>> convert_small_number(25)
    'twenty-five'
    >>> convert_small_number(-1)
    Traceback (most recent call last):
    ...
    ValueError: This function only accepts non-negative integers
    >>> convert_small_number(123)
    Traceback (most recent call last):
    ...
    ValueError: This function only converts numbers less than 100
    """
    if num < 0:
        raise ValueError("This function only accepts non-negative integers")
    if num >= 100:
        raise ValueError("This function only converts numbers less than 100")
    tens, ones = divmod(num, 10)
    if tens == 0:
        return NumberWords.ONES.value[ones] or "zero"
    if tens == 1:
        return NumberWords.TEENS.value[ones]
    return (
        NumberWords.TENS.value[tens]
        + ("-" if NumberWords.ONES.value[ones] else "")
        + NumberWords.ONES.value[ones]
    )


def convert_number(
    num: int, system: Literal["short", "long", "indian"] = "short"
) -> str:
    """
    Converts an integer to English words.

    :param num: The integer to be converted
    :param system: The numbering system (short, long, or Indian)

    >>> convert_number(0)
    'zero'
    >>> convert_number(1)
    'one'
    >>> convert_number(100)
    'one hundred'
    >>> convert_number(-100)
    'negative one hundred'
    >>> convert_number(123_456_789_012_345) # doctest: +NORMALIZE_WHITESPACE
    'one hundred twenty-three trillion four hundred fifty-six billion
    seven hundred eighty-nine million twelve thousand three hundred forty-five'
    >>> convert_number(123_456_789_012_345, "long") # doctest: +NORMALIZE_WHITESPACE
    'one hundred twenty-three thousand four hundred fifty-six milliard
    seven hundred eighty-nine million twelve thousand three hundred forty-five'
    >>> convert_number(12_34_56_78_90_12_345, "indian") # doctest: +NORMALIZE_WHITESPACE
    'one crore crore twenty-three lakh crore
    forty-five thousand six hundred seventy-eight crore
    ninety lakh twelve thousand three hundred forty-five'
    >>> convert_number(10**18)
    Traceback (most recent call last):
    ...
    ValueError: Input number is too large
    >>> convert_number(10**21, "long")
    Traceback (most recent call last):
    ...
    ValueError: Input number is too large
    >>> convert_number(10**19, "indian")
    Traceback (most recent call last):
    ...
    ValueError: Input number is too large
    """
    word_groups = []

    if num < 0:
        word_groups.append("negative")
        num *= -1

    if num > NumberingSystem.max_value(system):
        raise ValueError("Input number is too large")

    for power, unit in NumberingSystem[system.upper()].value:
        digit_group, num = divmod(num, 10**power)
        if digit_group > 0:
            word_group = (
                convert_number(digit_group, system)
                if digit_group >= 100
                else convert_small_number(digit_group)
            )
            word_groups.append(f"{word_group} {unit}")
    if num > 0 or not word_groups:  # word_groups is only empty if input num was 0
        word_groups.append(convert_small_number(num))
    return " ".join(word_groups)


if __name__ == "__main__":
    import doctest

    doctest.testmod()

    print(f"{convert_number(123456789) = }")
