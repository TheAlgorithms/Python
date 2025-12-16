class MinStack:
    """
    A Stack data structure that supports retrieving the minimum element
    in O(1) time using an auxiliary stack .

    >>> st = MinStack()
    >>> st.push(18)
    >>> st.push(19)
    >>> st.push(29)
    >>> st.push(15)
    >>> st.push(16)
    >>> st.get_min()
    15
    >>> st.pop()
    16
    >>> st.get_min()
    15
    >>> st.pop()
    15
    >>> st.get_min()
    18
    >>> st.peek()
    29
    """

    def __init__(self) -> None:
        """Initialize the stack and auxiliary min stack."""
        self.st: list[int] = []
        self.min_st: list[int] = []

    def push(self, value: int) -> None:
        """Push a value onto the stack."""
        self.st.append(value)
        if not self.min_st or value <= self.min_st[-1]:
            self.min_st.append(value)

    def pop(self) -> int | None:
        """Pop the top element from the stack. Return None if empty."""
        if not self.st:
            return None
        value = self.st.pop()
        if value == self.min_st[-1]:
            self.min_st.pop()
        return value

    def peek(self) -> int | None:
        """Return the top element without removing it. Return None if empty."""
        if not self.st:
            return None
        return self.st[-1]

    def get_min(self) -> int | None:
        """Return the minimum element in the stack. Return None if empty."""
        if not self.min_st:
            return None
        return self.min_st[-1]


if __name__ == "__main__":
    st = MinStack()
    st.push(18)
    st.push(19)
    st.push(29)
    st.push(15)
    st.push(16)
    print(st.get_min())  # should print 15
