"""
Bag distance used to measure string similarity between two strings.

http://www-db.disi.unibo.it/research/papers/SPIRE02.pdf
"""


def bag_distance(a: str, b: str) -> float:
    if a == b:
        return 0

    a_m, b_m = {}, {}
    a_len, b_len = len(a), len(b)

    if not a_len:
        return b_len
    if not b_len:
        return a_len

    longest_len: int = max(a_len, b_len)

    for i in range(longest_len):
        if i < a_len:
            val = a[i]

            if val not in a_m:
                a_m[val] = 0

            a_m[val] += 1

        if i < b_len:
            val = b[i]

            if val not in b_m:
                b_m[val] = 0

            b_m[val] += 1

    for elem in a_m:
        if elem in b_m:
            a_len -= min(a_m[elem], b_m[elem])

    for elem in b_m:
        if elem in a_m:
            b_len -= min(b_m[elem], a_m[elem])

    return max(a_len, b_len)


def test_bag_distance():
    assert bag_distance("aluminum", "Catalan") == 5
    assert bag_distance("cat", "cat") == 0


if __name__ == "__main__":
    import doctest

    doctest.testmod()
    test_bag_distance()
