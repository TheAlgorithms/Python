# Created by sarathkaul on 12/11/19


def check_palindrome(input_str: str) -> None:
    """
    >>> check_palindrome("PALINDROME")
    Entered String PALINDROME is not Palindrome
    >>> check_palindrome("SSASS")
    Entered String SSASS is Palindrome
    """

    reverse_str = "".join(
        reversed(input_str)
    )  # Use reversed to reverse the input string
    if reverse_str == input_str:
        print(f"Entered String {input_str} is Palindrome")
    else:
        print(f"Entered String {input_str} is not Palindrome")


if __name__ == "main":
    print(check_palindrome("INPUT STRING"))
