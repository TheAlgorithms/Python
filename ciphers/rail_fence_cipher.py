""" https://en.wikipedia.org/wiki/Rail_fence_cipher """


def encrypt(input_string: str, key: int) -> str:
    """
    Shuffles the character of a string by placing each of them
    in a grid (the height is dependent on the key) in a zigzag
    formation and reading it left to right.

    >>> encrypt("Hello World", 4)
    'HWe olordll'

    >>> encrypt("This is a message", 0)
    Traceback (most recent call last):
        ...
    ValueError: Height of grid can't be 0 or negative

    >>> encrypt(b"This is a byte string", 5)
    Traceback (most recent call last):
        ...
    TypeError: sequence item 0: expected str instance, int found
    """
    temp_grid: list[list[str]] = [[] for _ in range(key)]
    lowest = key - 1

    if key <= 0:
        raise ValueError("Height of grid can't be 0 or negative")
    if key == 1 or len(input_string) <= key:
        return input_string

    for position, character in enumerate(input_string):
        num = position % (lowest * 2)  # puts it in bounds
        num = min(num, lowest * 2 - num)  # creates zigzag pattern
        temp_grid[num].append(character)
    grid = ["".join(row) for row in temp_grid]
    output_string = "".join(grid)

    return output_string


def decrypt(input_string: str, key: int) -> str:
    """
    Generates a template based on the key and fills it in with
    the characters of the input string and then reading it in
    a zigzag formation.

    >>> decrypt("HWe olordll", 4)
    'Hello World'

    >>> decrypt("This is a message", -10)
    Traceback (most recent call last):
        ...
    ValueError: Height of grid can't be 0 or negative

    >>> decrypt("My key is very big", 100)
    'My key is very big'
    """
    grid = []
    lowest = key - 1

    if key <= 0:
        raise ValueError("Height of grid can't be 0 or negative")
    if key == 1:
        return input_string

    temp_grid: list[list[str]] = [[] for _ in range(key)]  # generates template
    for position in range(len(input_string)):
        num = position % (lowest * 2)  # puts it in bounds
        num = min(num, lowest * 2 - num)  # creates zigzag pattern
        temp_grid[num].append("*")

    counter = 0
    for row in temp_grid:  # fills in the characters
        splice = input_string[counter : counter + len(row)]
        grid.append([character for character in splice])
        counter += len(row)

    output_string = ""  # reads as zigzag
    for position in range(len(input_string)):
        num = position % (lowest * 2)  # puts it in bounds
        num = min(num, lowest * 2 - num)  # creates zigzag pattern
        output_string += grid[num][0]
        grid[num].pop(0)
    return output_string


def bruteforce(input_string: str) -> dict[int, str]:
    """Uses decrypt function by guessing every key

    >>> bruteforce("HWe olordll")[4]
    'Hello World'
    """
    results = {}
    for key_guess in range(1, len(input_string)):  # tries every key
        results[key_guess] = decrypt(input_string, key_guess)
    return results


if __name__ == "__main__":
    import doctest

    doctest.testmod()
