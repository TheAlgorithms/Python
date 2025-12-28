"""
This is a pure Python implementation of a dynamic programming solution
to generate the Fibonacci sequence.
"""

from typing import List


class Fibonacci:
    def __init__(self) -> None:
        self.sequence: List[int] = [0, 1]

    def get(self, index: int) -> List[int]:
        """
        Return the Fibonacci sequence up to the given index (exclusive).

        Args:
            index: The number of Fibonacci values to generate.

        Returns:
            A list of Fibonacci numbers up to the given index.

        Raises:
            ValueError: If index is a negative integer.

        >>> Fibonacci().get(10)
        [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
        >>> Fibonacci().get(5)
        [0, 1, 1, 2, 3]
        """
        if index < 0:
            raise ValueError("index must be a non-negative integer")

        if (difference := index - (len(self.sequence) - 2)) >= 1:
            for _ in range(difference):
                self.sequence.append(self.sequence[-1] + self.sequence[-2])

        return self.sequence[:index]


def main() -> None:
    print(
        "Fibonacci Series Using Dynamic Programming\n"
        "Enter the number of Fibonacci values to generate.\n"
        "(Type 'exit' or press Ctrl-C to quit)\n"
    )

    fibonacci = Fibonacci()

    while True:
        prompt: str = input(">> ")

        if prompt.lower() in {"exit", "quit"}:
            break

        try:
            index = int(prompt)
            print(fibonacci.get(index))
        except ValueError as exc:
            print(f"Error: {exc}")


if __name__ == "__main__":
    main()
