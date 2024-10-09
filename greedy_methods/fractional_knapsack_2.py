# https://en.wikipedia.org/wiki/Continuous_knapsack_problem
# https://www.guru99.com/fractional-knapsack-problem-greedy.html
# https://medium.com/walkinthecode/greedy-algorithm-fractional-knapsack-problem-9aba1daecc93

from __future__ import annotations

# Produced By K. Umut Araz


def kesirli_sırtçantası(
    değer: list[int], ağırlık: list[int], kapasite: int
) -> tuple[float, list[float]]:
    """
    >>> değer = [1, 3, 5, 7, 9]
    >>> ağırlık = [0.9, 0.7, 0.5, 0.3, 0.1]
    >>> kesirli_sırtçantası(değer, ağırlık, 5)
    (25, [1, 1, 1, 1, 1])
    >>> kesirli_sırtçantası(değer, ağırlık, 15)
    (25, [1, 1, 1, 1, 1])
    >>> kesirli_sırtçantası(değer, ağırlık, 25)
    (25, [1, 1, 1, 1, 1])
    >>> kesirli_sırtçantası(değer, ağırlık, 26)
    (25, [1, 1, 1, 1, 1])
    >>> kesirli_sırtçantası(değer, ağırlık, -1)
    (-90.0, [0, 0, 0, 0, -10.0])
    >>> kesirli_sırtçantası([1, 3, 5, 7], ağırlık, 30)
    (16, [1, 1, 1, 1])
    >>> kesirli_sırtçantası(değer, [0.9, 0.7, 0.5, 0.3, 0.1], 30)
    (25, [1, 1, 1, 1, 1])
    >>> kesirli_sırtçantası([], [], 30)
    (0, [])
    """
    indeks = list(range(len(değer)))
    oran = [v / w for v, w in zip(değer, ağırlık)]
    indeks.sort(key=lambda i: oran[i], reverse=True)

    max_değer: float = 0
    kesirler: list[float] = [0] * len(değer)
    for i in indeks:
        if ağırlık[i] <= kapasite:
            kesirler[i] = 1
            max_değer += değer[i]
            kapasite -= ağırlık[i]
        else:
            kesirler[i] = kapasite / ağırlık[i]
            max_değer += değer[i] * kapasite / ağırlık[i]
            break

    return max_değer, kesirler


if __name__ == "__main__":
    import doctest

    doctest.testmod()
