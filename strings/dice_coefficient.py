"""
Dice's coefficient used to measure string similarity between two strings.

https://en.wikipedia.org/wiki/S%C3%B8rensen%E2%80%93Dice_coefficient
"""


def dice_coefficient(a: str, b: str) -> float:
    if not len(a) or not len(b):
        return 0.0
    if len(a) == 1:
        a = a + "."
    if len(b) == 1:
        b = b + "."

    a_bigram, b_bigram = [], []
    for i in range(len(a) - 1):
        a_bigram.append(a[i : i + 2])

    for i in range(len(b) - 1):
        b_bigram.append(b[i : i + 2])

    a_bigrams, b_bigrams = set(a_bigram), set(b_bigram)
    bigram_overlap = len(a_bigrams & b_bigrams)
    string_similarity = (2.0 * bigram_overlap) / (len(a_bigrams) + len(b_bigrams))
    return string_similarity


def test_dice_coeff():
    assert dice_coefficient("JP Morgan", "JP Morgan Chase and Co INC") > 0.5


if __name__ == "__main__":
    import doctest

    doctest.testmod()

    test_dice_coeff()
    print(dice_coefficient("JP Morgan", "JP Morgan Chase and Co INC"))
