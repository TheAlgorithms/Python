"""
A Vampire number (or true Vampire number) is a composite natural number
with an even number of digits, that can be factored into two natural numbers
each with half as many digits as the original number and not both with
trailing zeroes, where the two factors contain precisely all the digits of
the original number, in any order, counting multiplicity.

For example, 1435 is an Vampire number because 35 * 41 = 1435.
The first vampire number is 1260 = 21 × 60.

Refs:
https://en.wikipedia.org/wiki/Vampire_number

"""
from itertools import permutations


def getFangs(num_str: str) -> list:
    """
    Returns the list of fangs of an Vampire number if found
    else returns empty list

    >>> getFangs('1260')
    ['21', '60']
    >>> getFangs('1890')
    []
    >>> getFangs('243770')
    []
    >>> getFangs('125500')
    ['251', '500']
    >>> getFangs('13078260')
    ['1863', '7020']
    """
    num_permutations = permutations(num_str, len(num_str))

    for num_list in num_permutations:
        vampire = "".join(num_list)
        xfang, yfang = vampire[: len(vampire) // 2], vampire[len(vampire) // 2 :]

        if xfang[-1] == "0" and yfang[-1] == "0":
            continue

        if int(xfang) * int(yfang) == int(num_str):
            return [xfang, yfang]
    return []


def isVampire(num: int) -> bool:
    """
    Return the boolean true/false based on the number is an Vampire
    number or not.

    >>> isVampire(1260)
    True
    >>> isVampire(-126)
    False
    >>> isVampire(688)
    False
    >>> isVampire(125500)
    True
    >>> isVampire(13078260)
    True
    """
    if num > 0:
        num_str = str(num)
        if len(num_str) % 2 == 0:
            return False if not getFangs(num_str) else True
    return False


def main():
    """
    Takes input from the user and checks if it is an Vampire number or not.
    """
    num = int(input("Enter a number to see if it is an Vampire number: ").strip())
    print(f"{num} is {'' if isVampire(num) else 'not '}an Vampire number.")


if __name__ == "__main__":
    import doctest

    doctest.testmod()
    main()
