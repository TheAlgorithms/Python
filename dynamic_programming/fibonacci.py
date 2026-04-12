"""
This is a pure Python implementation of Dynamic Programming solution to the fibonacci
sequence problem.

Time Complexity: O(n) - We compute each Fibonacci number once and store it
Space Complexity: O(n) - We maintain a list of all computed Fibonacci numbers

Note: For computing a single large Fibonacci number efficiently, consider using
fast_fibonacci.py which implements the fast doubling method in O(log n) time.
"""


class Fibonacci:
    """
    A class to generate Fibonacci numbers using dynamic programming with memoization.
    
    The Fibonacci sequence is defined as:
    F(0) = 0, F(1) = 1, and F(n) = F(n-1) + F(n-2) for n > 1
    
    Attributes:
        sequence (list[int]): Internal storage for computed Fibonacci numbers.
    
    Example:
        >>> fib = Fibonacci()
        >>> fib.get(10)
        [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
    """
    
    def __init__(self) -> None:
        """Initialize the Fibonacci sequence with the first two values [0, 1]."""
        self.sequence = [0, 1]
    
    def get(self, index: int) -> list:
        """
        Get the first `index` Fibonacci numbers.
        
        If the requested index exceeds previously computed values, this method
        extends the sequence using the recurrence relation F(n) = F(n-1) + F(n-2).
        This memoization approach ensures each Fibonacci number is computed only once.
        
        Args:
            index (int): The number of Fibonacci numbers to return (must be non-negative).
        
        Returns:
            list[int]: A list containing the first `index` Fibonacci numbers.
        
        Raises:
            IndexError: If index is negative (though Python's slice handles this gracefully).
        
        Examples:
            >>> Fibonacci().get(10)
            [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
            >>> Fibonacci().get(5)
            [0, 1, 1, 2, 3]
            >>> Fibonacci().get(0)
            []
            >>> Fibonacci().get(1)
            [0]
        """
        if (difference := index - (len(self.sequence) - 2)) >= 1:
            for _ in range(difference):
                self.sequence.append(self.sequence[-1] + self.sequence[-2])
        return self.sequence[:index]


def main() -> None:
    print(
        "Fibonacci Series Using Dynamic Programming\n",
        "Enter the index of the Fibonacci number you want to calculate ",
        "in the prompt below. (To exit enter exit or Ctrl-C)\n",
        sep="",
    )
    fibonacci = Fibonacci()

    while True:
        prompt: str = input(">> ")
        if prompt in {"exit", "quit"}:
            break

        try:
            index: int = int(prompt)
        except ValueError:
            print("Enter a number or 'exit'")
            continue

        print(fibonacci.get(index))


if __name__ == "__main__":
    main()
