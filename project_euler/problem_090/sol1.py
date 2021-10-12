from itertools import permutations, combinations

def setToBit(s):
    """
        returns bit representation of a given iterable, preferably set
    """
    res = 0
    for i in s:
        res |= 1<<i
    return res

def isBitSet(n, c):
    """
        checks if a given bit is 1 in the given number (work around for 6 and 9)
    """
    if c == 6 or c == 9:
        return (1<<6 & n) or (1<<9 & n)
    return 1<<c & n

def validateCubes(cubes, sq):
    """
        verifies whether or not the selected combination of cubes is valid, by iterating through
        all square values
    """
    for s in sq:
        res = False
        for p in permutations(s):
            curRes = True
            for i, c in enumerate(map(int, p)):
                curRes = curRes and isBitSet(cubes[i], c)
            res = res or curRes
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
    allDices = [setToBit(c) for c in combinations(range(10), 6)]
    dices = [p for p in combinations(allDices, m)]

    res = 0
    for d in dices:
        if validateCubes(d, sq):
            res += 1
    return res


if __name__ == "__main__":
    print(f"{solution()}")
