def hollow_diamond_alphabet(diamond_size: int) -> None:
    """
    Prints a hollow diamond pattern using alphabet characters.

    Parameters:
    diamond_size (int): The size of the diamond. Determines the number of rows.

    Example:
    >>> hollow_diamond_alphabet(5)
            A
           B C
          D   E
         F     G
        H       I
         F     G
          D   E
           B C
            A
    """
    alpha = 64
    for i in range(1, diamond_size + 1):
        left_spaces = " " * (diamond_size - i)
        hollow_spaces = " " * (((i - 1) * 2) - 1)
        if i == 1:
            print(left_spaces + chr(alpha + 1))
        else:
            print(left_spaces + chr(alpha) + hollow_spaces + chr(alpha + 1))
        alpha += 2

    alpha -= 2
    for i in range(diamond_size - 1, 0, -1):
        left_spaces = " " * (diamond_size - i)
        hollow_spaces = " " * (((i - 1) * 2) - 1)
        if i == 1:
            print(left_spaces + chr(alpha - 1))
        else:
            print(left_spaces + chr(alpha - 2) + hollow_spaces + chr(alpha - 1))
        alpha -= 2

# Example usage
diamond_size = int(input("Enter the diamond size: "))
hollow_diamond_alphabet(diamond_size)
