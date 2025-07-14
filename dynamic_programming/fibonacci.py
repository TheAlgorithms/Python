"""
This is a pure Python implementation of Dynamic Programming solution to the Fibonacci
sequence problem.

The Fibonacci sequence is a series of numbers where each number is the sum of the
two preceding ones, usually starting with 0 and 1. The sequence begins:
0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, ...

Reference: https://en.wikipedia.org/wiki/Fibonacci_number

Time Complexity: O(n) for first calculation, O(1) for subsequent calls with memoization
Space Complexity: O(n) for storing the sequence
"""


class Fibonacci:
    """
    Dynamic Programming implementation of Fibonacci sequence generator.

    This class maintains a memoized sequence of Fibonacci numbers and can efficiently
    generate new numbers by building on previously calculated values.

    Attributes:
        sequence (list[int]): Memoized Fibonacci sequence starting with [0, 1]
    """

    def __init__(self) -> None:
        """Initialize the Fibonacci sequence with the first two numbers."""
        self.sequence = [0, 1]

    def get(self, index: int) -> list[int]:
        """
        Get the first `index` Fibonacci numbers. If numbers don't exist in the sequence,
        calculate all missing numbers leading up to the required index.

        Args:
            index (int): Number of Fibonacci numbers to return (must be non-negative)

        Returns:
            list[int]: List containing the first `index` Fibonacci numbers

        Raises:
            ValueError: If index is negative

        Examples:
            >>> fib = Fibonacci()
            >>> fib.get(0)
            []
            >>> fib.get(1)
            [0]
            >>> fib.get(2)
            [0, 1]
            >>> fib.get(5)
            [0, 1, 1, 2, 3]
            >>> fib.get(10)
            [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
            >>> fib.get(1)  # Test memoization - should not recalculate
            [0]
            >>> fib.get(15)  # Test extending existing sequence
            [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377]

            # Test edge cases
            >>> fib_new = Fibonacci()
            >>> fib_new.get(0)
            []
            >>> fib_new.get(1)
            [0]
            >>> fib_new.get(2)
            [0, 1]

            # Test error handling
            >>> fib_error = Fibonacci()
            >>> fib_error.get(-1)
            Traceback (most recent call last):
                ...
            ValueError: Index must be non-negative, got -1
            >>> fib_error.get(-5)
            Traceback (most recent call last):
                ...
            ValueError: Index must be non-negative, got -5

            # Test large numbers
            >>> fib_large = Fibonacci()
            >>> result = fib_large.get(20)
            >>> len(result)
            20
            >>> result[-1]  # 20th Fibonacci number (0-indexed, so 19th position)
            4181
            >>> result[0], result[1], result[2]
            (0, 1, 1)

            # Test sequence correctness
            >>> fib_test = Fibonacci()
            >>> seq = fib_test.get(8)
            >>> all(seq[i] == seq[i-1] + seq[i-2] for i in range(2, len(seq)))
            True
        """
        if index < 0:
            error_msg = f"Index must be non-negative, got {index}"
            raise ValueError(error_msg)

        if index == 0:
            return []

        # Calculate missing numbers if needed
        if (difference := index - len(self.sequence)) > 0:
            for _ in range(difference):
                self.sequence.append(self.sequence[-1] + self.sequence[-2])

        return self.sequence[:index]

    def get_nth(self, n: int) -> int:
        """
        Get the nth Fibonacci number (0-indexed).

        Args:
            n (int): The index of the Fibonacci number to retrieve

        Returns:
            int: The nth Fibonacci number

        Raises:
            ValueError: If n is negative

        Examples:
            >>> fib = Fibonacci()
            >>> fib.get_nth(0)
            0
            >>> fib.get_nth(1)
            1
            >>> fib.get_nth(2)
            1
            >>> fib.get_nth(5)
            5
            >>> fib.get_nth(10)
            55
            >>> fib.get_nth(-1)
            Traceback (most recent call last):
                ...
            ValueError: Index must be non-negative, got -1
        """
        if n < 0:
            error_msg = f"Index must be non-negative, got {n}"
            raise ValueError(error_msg)

        # Extend sequence if needed
        if n >= len(self.sequence):
            difference = n - len(self.sequence) + 1
            for _ in range(difference):
                self.sequence.append(self.sequence[-1] + self.sequence[-2])

        return self.sequence[n]

    def reset(self) -> None:
        """
        Reset the sequence to its initial state.

        Examples:
            >>> fib = Fibonacci()
            >>> fib.get(10)
            [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
            >>> len(fib.sequence)
            10
            >>> fib.reset()
            >>> fib.sequence
            [0, 1]
        """
        self.sequence = [0, 1]


def main() -> None:
    """
    Interactive CLI for generating Fibonacci numbers.

    Allows users to input indices and get the corresponding Fibonacci sequence.
    Supports commands: 'exit', 'quit', 'reset', 'help'
    """
    print(
        "Fibonacci Series Using Dynamic Programming\n"
        "Enter the index of the Fibonacci number you want to calculate\n"
        "Commands: 'exit'/'quit' to exit, 'reset' to clear cache, 'help' for help\n"
    )

    fibonacci = Fibonacci()

    while True:
        try:
            prompt: str = input(">> ").strip().lower()

            if prompt in {"exit", "quit"}:
                print("Goodbye!")
                break
            elif prompt == "reset":
                fibonacci.reset()
                print("Fibonacci sequence cache cleared.")
                continue
            elif prompt == "help":
                print(
                    "Commands:\n"
                    "  <number>  - Get first N Fibonacci numbers\n"
                    "  reset     - Clear the memoized sequence\n"
                    "  help      - Show this help message\n"
                    "  exit/quit - Exit the program\n"
                )
                continue
            elif prompt == "":
                continue

            try:
                index: int = int(prompt)
                if index < 0:
                    print("Please enter a non-negative number.")
                    continue

                result = fibonacci.get(index)
                if not result:
                    print("[]")
                else:
                    print(f"First {index} Fibonacci numbers: {result}")
                    if index > 0:
                        print(
                            f"The {index}th Fibonacci number is: {fibonacci.get_nth(index)}"
                        )

            except ValueError:
                print("Invalid input. Enter a number or use 'help' for commands.")

        except KeyboardInterrupt:
            print("\nGoodbye!")
            break
        except EOFError:
            print("\nGoodbye!")
            break


if __name__ == "__main__":
    main()
