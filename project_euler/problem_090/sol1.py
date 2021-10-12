from itertools import permutations, combinations

def set_to_bit(s):
    """
        returns bit representation of a given iterable, preferably set
        @param s - set representing the 1 bits
    """
    res = 0
    for i in s:
        res |= 1<<i
    return res

def is_bit_set(n, c):
    """
        checks if a given bit is 1 in the given number (work around for 6 and 9)
        @param n - the number/set to search in
        @param c - the index to look for
    """
    if c == 6 or c == 9:
        return (1<<6 & n) or (1<<9 & n)
    return 1<<c & n

def validate_cubes(cubes, sq):
    """
        verifies whether or not the selected combination of cubes is valid, by iterating through
        all square values.
        @param cubes - array of cubes represented by numbers (having six 1 bits (0-9))
        @param sq - list of squares to validate
    """
    for s in sq:
        res = False
        for p in permutations(s):
            cur_res = True
            for i, c in enumerate(map(int, p)):
                cur_res = cur_res and is_bit_set(cubes[i], c)
            res = res or cur_res
        if not res:
            return False
    return True

def solution(n=9, m=2):
    """
        returns the solution of problem 90 using helper functions
        e.g 1217 for the default argument values

        @param n - the number of squares to validate.
        @param m - the number of dice to use.
    """
    sq = [str(i**2).zfill(m) for i in range(1, n+1)]
    all_dices = [set_to_bit(c) for c in combinations(range(10), 6)]
    dices = [p for p in combinations(all_dices, m)]

    res = 0
    for d in dices:
        if validate_cubes(d, sq):
            res += 1
    return res


if __name__ == "__main__":
    print(f"{solution()}")
