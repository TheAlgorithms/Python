#https://www.allaboutcircuits.com/technical-articles/karnaugh-map-boolean-algebraic-simplification-technique/

def F(A: int, B: int) -> int:
    """
    Define the function F(A, B).

    >>> F(0, 0)
    0
    >>> F(1, 1)
    1
    """
    return A and (not B) or (A and B) or (A and B)

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
    
kmap = [[0 for _ in range(2)] for _ in range(2)]

# Manually generate the product of [0, 1] and [0, 1]
for A in [0, 1]:
    for B in [0, 1]:
        kmap[A][B] = F(A, B)

for row in kmap:
    print(row)

simplified_expression = simplify_kmap(kmap)
print("\nSimplified Expression:")
print(simplified_expression)

if __name__ == "__main__":
    main()
