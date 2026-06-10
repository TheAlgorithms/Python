"""
https://en.wikipedia.org/wiki/Karnaugh_map
https://www.allaboutcircuits.com/technical-articles/karnaugh-map-boolean-algebraic-simplification-technique
"""

# Changes I can make - 
# 1. Make a function for three and four variable kmap
# 2. Make truly simplified expressions

# Approach - Either store every possible box and brute force or make general expression and then simplify



def simplify_kmap(kmap: list[list[int]]) -> str:
    """
    Simplify the Karnaugh map.
    >>> simplify_kmap(kmap=[[0, 1], [1, 1]])
    "A'B + AB' + AB"
    >>> simplify_kmap(kmap=[[0, 0], [0, 0]])
    ''
    >>> simplify_kmap(kmap=[[0, 1], [1, -1]])
    "A'B + AB' + AB"
    >>> simplify_kmap(kmap=[[0, 1], [1, 2]])
    "A'B + AB' + AB"
    >>> simplify_kmap(kmap=[[0, 1], [1, 1.1]])
    "A'B + AB' + AB"
    >>> simplify_kmap(kmap=[[0, 1], [1, 'a']])
    "A'B + AB' + AB"
    """
    simplified_f = []
    # 4 sized boxes - There is only 1
    if kmap[0][0] + kmap[0][1] + kmap[1][0] + kmap[1][1] == 4:
        return "1"

    # 2 sized boxes - There are 4 (2 vertical and 2 horizontal)
    # check horizontal
    for i in range(2):
        if kmap[i][0] + kmap[i][1] == 2:
            simplified_f.append(("A" if i else "A'"))
    # check vertical
    for i in range(2):
        if kmap[0][i] + kmap[1][i] == 2:
            simplified_f.append(("B" if i else "B'"))
    
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
