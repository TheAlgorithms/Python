def hamming_distance(string1: str, string2: str) -> int:
    """Calculate the Hamming distance between two equal length strings
    In information theory, the Hamming distance between two strings of equal
    length is the number of positions at which the corresponding symbols are
    different. https://en.wikipedia.org/wiki/Hamming_distance

    Args:
        string1 (str): Sequence 1
        string2 (str): Sequence 2

    Returns:
        int: Hamming distance

    >>> hamming_distance("python", "python")
    0
    >>> hamming_distance("karolin", "kathrin")
    3
    >>> hamming_distance("00000", "11111")
    5
    """
    assert len(string1) == len(string2)

    count = 0

    for i in range(len(string1)):
        if string1[i] != string2[i]:
            count += 1

    return count


if __name__ == "__main__":

    def test_hamming_distance():
        assert hamming_distance("", "") == 0
        assert hamming_distance("python", "python") == 0
        assert hamming_distance("karolin", "kathrin") == 3
        assert hamming_distance("kathrin", "kerstin") == 4
        assert hamming_distance("00000", "11111") == 5

    test_hamming_distance()
