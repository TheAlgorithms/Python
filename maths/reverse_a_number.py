from __future__ import print_function


def reverse_num(num):
    """
    >>> reverse_num("123")
    321

    >>> reverse_num("321")
    123
    """

    return num[::-1]


if __name__ == "__main__":
    number_input = input("Please input any number (integer): ")
    try:
        converted = int(number_input)
    except ValueError as e:
        print(f"{number_input} is not a number, please input a number ({e})")
    else:
        print(
            f"Reverse of input number {number_input} is : {reverse_num(number_input)}"
        )
