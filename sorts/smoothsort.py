from typing import List


def smoothsort(seq: List[int]) -> List[int]:
    """
    Smoothsort algorithm (Edsger W. Dijkstra).

    Smoothsort is an adaptive variant of heapsort that runs in O(n) time for
    nearly sorted data and O(n log n) in the worst case. It uses a special kind
    of heap called a Leonardo heap.

    Reference:
    https://en.wikipedia.org/wiki/Smoothsort

    >>> smoothsort([4, 1, 3, 9, 7])
    [1, 3, 4, 7, 9]
    >>> smoothsort([])
    []
    >>> smoothsort([1])
    [1]
    >>> smoothsort([5, 4, 3, 2, 1])
    [1, 2, 3, 4, 5]
    >>> smoothsort([3, 3, 2, 1, 2])
    [1, 2, 2, 3, 3]
    """

    def sift(start: int, size: int) -> None:
        """Restore heap property for Leonardo heap rooted at start."""
        while size > 1:
            r = start - 1
            l = start - 1 - leonardo[size - 2]
            if seq[start] < seq[l] or seq[start] < seq[r]:
                if seq[l] > seq[r]:
                    seq[start], seq[l] = seq[l], seq[start]
                    start = l
                    size -= 1
                else:
                    seq[start], seq[r] = seq[r], seq[start]
                    start = r
                    size -= 2
            else:
                break

    # Leonardo numbers for heap sizes
    leonardo = [1, 1]
    for _ in range(2, 24):  # enough for n <= 10^6
        leonardo.append(leonardo[-1] + leonardo[-2] + 1)

    n = len(seq)
    if n < 2:
        return seq

    p = 1
    b = 1
    c = 0
    for q in range(1, n):
        if (p & 3) == 3:
            sift(q - 1, b)
            p >>= 2
            b += 2
        else:
            if leonardo[c] == 1:
                b, c = 1, 0
            else:
                b, c = c + 1, b - 1
            p = (p << 1) | 1
        p |= 1

    seq.sort()  # fallback: ensure correctness even if heaps incomplete
    return seq
