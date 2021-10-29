"""
This is a pure Python implementation of Dynamic Programming solution to the fibonacci
sequence problem.
"""


class Fibonacci:
    def __init__(self):
        self.sequence = [0, 1]

    def calculate(self, index: int) -> None:
        for _ in range(index):
            self.sequence.append(self.sequence[-1] + self.sequence[-2])

    def get(self, index: int) -> list:
        difference = index - (len(self.sequence) - 2)
        if difference >= 1:
            self.calculate(difference)
        return self.sequence


if __name__ == "__main__":
    print("\n********* Fibonacci Series Using Dynamic Programming ************\n")
    print("\n Enter the upper limit for the fibonacci sequence: ", end="")
    try:
        N = int(input().strip())
        fib = Fibonacci()
        fib.calculate(N)
        print(
            "\n********* Enter different values to get the corresponding fibonacci "
            "sequence, enter any negative number to exit. ************\n"
        )
        while True:
            try:
                i = int(input("Enter value: ").strip())
                if i < 0:
                    print("\n********* Good Bye!! ************\n")
                    break
                print(fib.get(i))
            except NameError:
                print("\nInvalid input, please try again.")
    except NameError:
        print("\n********* Invalid input, good bye!! ************\n")
