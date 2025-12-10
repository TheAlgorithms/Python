class squares_natural_numbers:
    def __init__(self, n):
        self.n = n

    def get(self):
        a = (self.n * (self.n + 1) * (2 * self.n + 1)) / 6
        print("The sum of the squares of the first", self.n, "natural numbers is", a)

sol = squares_natural_numbers(2)
sol.get()

