def truth_table_and():
    """
    Generate the truth table for the logical AND operator (a AND b).

    Output:
    a    b    a AND b
    -----------------
    0    0    0
    0    1    0
    1    0    0
    1    1    1
    """
    print("Truth table of AND:\n")
    print("a\tb\ta AND b")
    print("-----------------")
    for a in [0, 1]:
        for b in [0, 1]:
            c = a and b
            print(f"{a}\t{b}\t{c}")

def truth_table_or():
    """
    Generate the truth table for the logical OR operator (a OR b).

    Output:
    a    b    a OR b
    ----------------
    0    0    0
    0    1    1
    1    0    1
    1    1    1
    """
    print("\nTruth table of OR:\n")
    print("a\tb\ta OR b")
    print("----------------")
    for a in [0, 1]:
        for b in [0, 1]:
            c = a or b
            print(f"{a}\t{b}\t{c}")

def truth_table_not():
    """
    Generate the truth table for the logical NOT operator (NOT a).

    Output:
    a    NOT a
    ----------
    0    1
    1    0
    """
    print("\nTruth table of NOT:\n")
    print("a\tNOT a")
    print("----------")
    for a in [0, 1]:
        c = not a
        print(f"{a}\t{c}")

if __name__ == "__main__":
    truth_table_and()
    truth_table_or()
    truth_table_not()
