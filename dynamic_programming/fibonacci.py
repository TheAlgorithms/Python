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
        return self.sequence[:index]


def main():
    print(
        'Fibonacci Series Using Dynamic Programming\n',
        'Enter the index of the Fibonacci number you want to calculate ',
        'in the prompt below. (To exit enter exit or Ctrl-C)\n',
        sep="",
    )
    fibonacci = Fibonacci()

    while True:
        prompt = input('>> ')
        if prompt in ['exit', 'quit']:
            break

        try:
            index = int(prompt)
        except ValueError:
            print('Enter a number or "exit"')
            continue

        print(fibonacci.get(index))


if __name__ == "__main__":
    main()
