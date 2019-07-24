# Fibonacci Sequence Using Recursion

class FibonacciSequenceRecursive:

    def __init__(self):
        pass

    def generate_n_1_th_fibonacci_number(self, n):
        if n <= 1:
            return n
        return self.generate_n_1_th_fibonacci_number(n - 1) + self.generate_n_1_th_fibonacci_number(n - 2)

    def generate_fibonacci_series(self, limit):
        return [self.generate_n_1_th_fibonacci_number(n) for n in range(limit)]

    def is_positive_integer(self, limit):
        return limit > 0

    def fire_fibonacci_generation(self):
        limit = int(input("How many terms to include in fibonacci series: "))
        if self.is_positive_integer(limit):
            print("The first '{limit}' terms of the fibonacci series are as follows:".format(limit=limit))
            print(self.generate_fibonacci_series(limit))
        else:
            print("Enter a positive integer next time!")


if __name__ == '__main__':
    fibonacci = FibonacciSequenceRecursive()
    fibonacci.fire_fibonacci_generation()
