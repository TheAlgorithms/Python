from collections import deque


class HitCounter:
    """
    A counter that records hits (events) and can return
    the number of hits in the past 5 minutes (300 seconds).

    >>> hc = HitCounter()
    >>> hc.hit(1)
    >>> hc.hit(2)
    >>> hc.hit(300)
    >>> hc.get_hits(300)
    3
    >>> hc.get_hits(301)
    2
    """

    def __init__(self) -> None:
        self.hits: deque[int] = deque()

    def hit(self, timestamp: int) -> None:
        """Record a hit at the given timestamp (in seconds)."""
        self.hits.append(timestamp)

    def get_hits(self, timestamp: int) -> int:
        """
        Return the number of hits in the past 5 minutes
        from the given timestamp.
        """
        while self.hits and self.hits[0] <= timestamp - 300:
            self.hits.popleft()
        return len(self.hits)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
