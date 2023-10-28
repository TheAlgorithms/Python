# https://www.allaboutcircuits.com/technical-articles/karnaugh-map-boolean-algebraic-simplification-technique/


def simplify_kmap(kmap: list[list[int]]) -> str:
    """
    Simplify the K-Map.

    >>> kmap = [[0, 1], [1, 1]]
    >>> simplify_kmap(kmap)
    "A'B + AB' + AB"
    """
    simplified_f = []
    for a in range(2):
        for b in range(2):
            if kmap[a][b]:
                term = ("A" if a else "A'") + ("B" if b else "B'")
                simplified_f.append(term)
    return " + ".join(simplified_f)


def main() -> None:
    """
    Main function to create and simplify a K-Map.

    >>> main()
    [0, 1]
    [1, 1]
    Simplified Expression:
    A'B + AB' + AB
    """
    kmap = [[0, 1], [1, 1]]

    # Manually generate the product of [0, 1] and [0, 1]

    for row in kmap:
        print(row)

    simplified_expression = simplify_kmap(kmap)
    print("Simplified Expression:")
    print(simplified_expression)


if __name__ == "__main__":
    main()
