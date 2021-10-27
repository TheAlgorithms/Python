"""
Program to list all the ways a target string can be
constructed from the given list of substrings
"""


def all_construct(target, word_bank=[]):
    """
        returns the list containing all the possible
        combinations a string(target) can be constructed from
        the given list of substrings(word_bank)
    >>> all_construct("hello", ["he", "l", "o"])
    [['he', 'l', 'l', 'o']]
    >>> all_construct("purple",["purp","p","ur","le","purpl"])
    [['purp', 'le'], ['p', 'ur', 'p', 'le']]
    """
    # create a table
    table_size = len(target) + 1
    table = []
    for i in range(table_size):
        table.append([])

    # seed value
    table[0] = [[]]  # because empty string has empty combination

    # iterate through the indices
    for i in range(table_size):
        # condition
        if table[i] != []:
            for word in word_bank:
                # slice condition
                if target[i : i + len(word)] == word:
                    new_combinations = list(map(lambda way: [word] + way, table[i]))
                    # adds the word to every combination the current position holds
                    # now,push that combination to the table[i+len(word)]
                    table[i + len(word)] += new_combinations

    # combinations are in reverse order so reverse for better output
    for combination in table[len(target)]:
        combination.reverse()

    return table[len(target)]


def main():
    print(all_construct("jwajalapa", ["jwa", "j", "w", "a", "la", "lapa"]))
    print(all_construct("rajamati", ["s", "raj", "amat", "raja", "ma", "i", "t"]))
    print(
        all_construct(
            "hexagonosaurus",
            ["h", "ex", "hex", "ag", "ago", "ru", "auru", "rus", "go", "no", "o", "s"],
        )
    )


if __name__ == "__main__":
    main()
