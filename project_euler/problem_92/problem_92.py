def solution() -> int:
    """
    https://projecteuler.net/problem=92
    >>> solution()
    8581146
    """
    known_solutions = {}
    known_solutions[89] = 1
    known_solutions[1] = 0

    def helper(x: int) -> int:
        return sum([int(c) ** 2 for c in list(str(x))])

    def f(x: int) -> int:
        if x in known_solutions:
            return known_solutions[x]
        else:
            result = f(helper(x))
            known_solutions[x] = result
            return result

    count = 0

    for i in range(1, 10_000_000):
        if i in known_solutions:
            count += known_solutions[i]
        else:
            count += f(i)
        # if i%100_000==0: print(i)
    return count
