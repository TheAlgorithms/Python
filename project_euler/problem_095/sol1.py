"""
Problem 95
Url: https://projecteuler.net/problem=95
"""
def solution(n: int = 10**6) -> int:
    """
    Returns the smallest member when n = 1000000
    >> 14316
    """

    sum_of_div = [0] * (n + 1)
    for i in range(1, n // 2 + 1):
        for j in range(i * 2, n + 1, i):
            sum_of_div[j] += i

    checked = [False] * (n + 1)
    max_len_of_chain = 0
    result = 0
    for i in range(2, n + 1):
        possible_chain = []
        j = i
        while not checked[j]:
            checked[j] = True
            possible_chain.append(j)
            j = sum_of_div[j]
            if j > n:
                break
            if j in possible_chain:
                len_of_chain = len(possible_chain) - possible_chain.index(j)
                if len_of_chain > max_len_of_chain:
                    max_len_of_chain = len_of_chain
                    result = min(possible_chain[-len_of_chain:])
                break
    return result


if __name__ == "__main__":
    import doctest

    doctest.testmod()
    print(f"{solution() = }")
