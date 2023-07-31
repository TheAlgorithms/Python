"""
This is a pure Python implementation of Dynamic Programming solution to the fibonacci
sequence problem.
"""


class Fibonacci:
    def __init__(self) -> None:
        self.sequence = [0, 1]

    def get(self, index: int) -> list:
        """
        Get the Fibonacci number of `index`. If the number does not exist,
        calculate all missing numbers leading up to the number of `index`.

        >>> Fibonacci().get(10)
        [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
        >>> Fibonacci().get(5)
        [0, 1, 1, 2, 3]
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
