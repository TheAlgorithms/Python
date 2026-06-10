"""
https://en.wikipedia.org/wiki/Karnaugh_map
https://www.allaboutcircuits.com/technical-articles/karnaugh-map-boolean-algebraic-simplification-technique
"""


def simplify_kmap(kmap: list[list[int]]) -> str:
    """
    Simplify a 2 variable Karnaugh map.

    Args:
        kmap (List[List[]]): The kmap as a 2D array

    Returns:
        str: The most simplified expression of the kmap


    >>> simplify_kmap(kmap=[[0, 1], [1, 1]])
    "A + B"
    >>> simplify_kmap(kmap=[[0, 0], [0, 0]])
    '0'
    >>> simplify_kmap(kmap=[[0, 1], [1, -1]])
    'A + B'
    >>> simplify_kmap(kmap=[[0, 1], [1, 2]])
    "A + B"
    >>> simplify_kmap(kmap=[[0, 1], [1, 1.1]])
    "A + B"
    >>> simplify_kmap(kmap=[[0, 1], [1, 'a']])
    "A + B"
    """
    simplified_f = []
    # 4 sized boxes - There is only 1
    if kmap[0][0] and kmap[0][1] and kmap[1][0] and kmap[1][1]:
        return "1"

    # 2 sized boxes - There are 4 (2 vertical and 2 horizontal)
    # check horizontal
    for i in range(2):
        if kmap[i][0] and kmap[i][1]:
            simplified_f.append("A" if i else "A'")
    # check vertical
    for i in range(2):
        if kmap[0][i] and kmap[1][i]:
            simplified_f.append("B" if i else "B'")

    # 1 sized boxes - There are 4

    if not (simplified_f):
        simplified_f.append("0")

    return " + ".join(simplified_f)


def main() -> None:
    """
    Main function to create and simplify a K-Map.

    >>> main()
    [0, 1]
    [1, 1]
    Simplified Expression:
    A + B
    """
    kmap = [[0, 1], [1, 1]]

    # Manually generate the product of [0, 1] and [0, 1]

    for row in kmap:
        print(row)

    print("Simplified Expression:")
    print(simplify_kmap(kmap))


if __name__ == "__main__":
    main()
    print(f"{simplify_kmap(kmap=[[0, 1], [1, 1]]) = }")
