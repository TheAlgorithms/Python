def F(A: int, B: int) -> int:
    """
    Define the function F(A, B).

    >>> F(0, 0)
    0
    >>> F(1, 1)
    1
    """
    return (A & (not B)) | (A & B) | (A & B)

def simplify_kmap(kmap: list[list[int]]) -> str:
    """
    Simplify the K-Map.

    >>> kmap = [[0, 1], [1, 1]]
    >>> simplify_kmap(kmap)
    "A'B + AB' + AB"
    """
    simplified_F = []
    for A in range(2):
        for B in range(2):
            if kmap[A][B]:
                term = ("A" if A else "A'") + ("B" if B else "B'")
                simplified_F.append(term)
    return ' + '.join(simplified_F)

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
    print("\nSimplified Expression:")
    print(simplified_expression)

if __name__ == "__main__":
    main()
