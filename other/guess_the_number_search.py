"""
get the random number guessed by the computer by passing the lower,higher
and the number to guess

this solution works on divide and getting the half of number of previous and
current, this depends on the number is low or high

if the number is more than last lower and less than to the number to guess then
the number is assigned to it, and same but opposite for higher number

suppose lower is 0, higher is 1000 and the number to guess is 355
then:
    num = int((lower+higher)/2)
    for above statement the function already declared as the get_avg(a,b)

        [1]
    get_avg(0,1000)  : 500
    answer(500) : high
        Now this value is passed to the answer function and that returns the
        passed number is lower than the guess number or higher than the guess
        number and also for equality

        [2]
    get_avg(0,500) : 250
    answer(250) : low

        [3]
    get_avg(250,500) : 375
    answer(375) : high

        [4]
    get_avg(375,250) : 312
    answer(312) : low

        [5]
    get_avg(312,375) : 343
    answer(343) : low

        [6]
    get_avg(343,375) : 359
    answer(359) : high

        [7]
    get_avg(343,359) : 351
    answer(351) : low

        [8]
    get_avg(351,359) : 355
    answer(355) : same

The number is found : 355

>>> guess_the_number(10, 1000, 17)
started...
guess the number : 17
details : [505, 257, 133, 71, 40, 25, 17]

"""


def temp_input_value(min_val: int = 10, max_val: int = 1000, option: int = True) -> int:
    """
    Temporary input values for tests

    >>> temp_input_value(option=True)
    10

    >>> temp_input_value(option=False)
    1000
    """
    if option is True:
        return min_val
    return max_val


def get_avg(a: int, b: int) -> int:
    """
    Return the mid-number(whole) of two integers a and b
    >>> get_avg(10,15)
    12
    >>> get_avg(20,300)
    160
    >>> get_avg("a",300)
    Traceback (most recent call last):
        ...
    TypeError: can only concatenate str (not "int") to str
    """
    return int((a + b) / 2)


def guess_the_number(lower: int, higher: int, to_guess: int) -> None:
    """
    The `guess_the_number` function that guess the number by some operations
    and using inner functions

    >>> guess_the_number(10, 1000, 17)
    started...
    guess the number : 17
    details : [505, 257, 133, 71, 40, 25, 17]

    >>> guess_the_number(10, 1000, "a")
    Traceback (most recent call last):
        ...
    TypeError: '>' not supported between instances of 'int' and 'str'
    """

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
