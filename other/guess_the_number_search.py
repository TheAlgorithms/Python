"""
guess the number using lower,higher and the value to find or guess

solution works by dividing lower and higher of number guessed

suppose lower is 0, higher is 1000 and the number to guess is 355

>>> guess_the_number(10, 1000, 17)
started...
guess the number : 17
details : [505, 257, 133, 71, 40, 25, 17]

"""


def temp_input_value(
    min_val: int = 10, max_val: int = 1000, option: bool = True
) -> int:
    """
    Temporary input values for tests

    >>> temp_input_value(option=True)
    10

    >>> temp_input_value(option=False)
    1000

    >>> temp_input_value(min_val=100, option=True)
    100

    >>> temp_input_value(min_val=100, max_val=50)
    Traceback (most recent call last):
        ...
    ValueError: Invalid value for min_val or max_val (min_value < max_value)

    >>> temp_input_value("ten","fifty",1)
    Traceback (most recent call last):
        ...
    AssertionError: Invalid type of value(s) specified to function!

    >>> temp_input_value(min_val=-100, max_val=500)
    -100

    >>> temp_input_value(min_val=-5100, max_val=-100)
    -5100
    """
    assert (
        isinstance(min_val, int)
        and isinstance(max_val, int)
        and isinstance(option, bool)
    ), "Invalid type of value(s) specified to function!"

    if min_val > max_val:
        raise ValueError("Invalid value for min_val or max_val (min_value < max_value)")
    return min_val if option else max_val


def get_avg(number_1: int, number_2: int) -> int:
    """
    Return the mid-number(whole) of two integers a and b

    >>> get_avg(10, 15)
    12

    >>> get_avg(20, 300)
    160

    >>> get_avg("abcd", 300)
    Traceback (most recent call last):
        ...
    TypeError: can only concatenate str (not "int") to str

    >>> get_avg(10.5,50.25)
    30
    """
    return int((number_1 + number_2) / 2)


def guess_the_number(lower: int, higher: int, to_guess: int) -> None:
    """
    The `guess_the_number` function that guess the number by some operations
    and using inner functions

    >>> guess_the_number(10, 1000, 17)
    started...
    guess the number : 17
    details : [505, 257, 133, 71, 40, 25, 17]

    >>> guess_the_number(-10000, 10000, 7)
    started...
    guess the number : 7
    details : [0, 5000, 2500, 1250, 625, 312, 156, 78, 39, 19, 9, 4, 6, 7]

    >>> guess_the_number(10, 1000, "a")
    Traceback (most recent call last):
        ...
    AssertionError: argument values must be type of "int"

    >>> guess_the_number(10, 1000, 5)
    Traceback (most recent call last):
        ...
    ValueError: guess value must be within the range of lower and higher value

    >>> guess_the_number(10000, 100, 5)
    Traceback (most recent call last):
        ...
    ValueError: argument value for lower and higher must be(lower > higher)
    """
    assert (
        isinstance(lower, int) and isinstance(higher, int) and isinstance(to_guess, int)
    ), 'argument values must be type of "int"'

    if lower > higher:
        raise ValueError("argument value for lower and higher must be(lower > higher)")

    if not lower < to_guess < higher:
        raise ValueError(
            "guess value must be within the range of lower and higher value"
        )

    def answer(number: int) -> str:
        """
        Returns value by comparing with entered `to_guess` number
        """
        if number > to_guess:
            return "high"
        elif number < to_guess:
            return "low"
        else:
            return "same"

    print("started...")

    last_lowest = lower
    last_highest = higher

    last_numbers = []

    while True:
        number = get_avg(last_lowest, last_highest)
        last_numbers.append(number)

        if answer(number) == "low":
            last_lowest = number
        elif answer(number) == "high":
            last_highest = number
        else:
            break

    print(f"guess the number : {last_numbers[-1]}")
    print(f"details : {str(last_numbers)}")


def main() -> None:
    """
    starting point or function of script
    """
    lower = int(input("Enter lower value : ").strip())
    higher = int(input("Enter high value : ").strip())
    guess = int(input("Enter value to guess : ").strip())
    guess_the_number(lower, higher, guess)


if __name__ == "__main__":
    main()
