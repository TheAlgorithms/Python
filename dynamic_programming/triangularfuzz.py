class TriangularFuzzySet:
    def __init__(self, a, b, c):
        """
        Initializes a triangular fuzzy set with the given parameters.

        :param a: Left point of the fuzzy set.
        :param b: Peak point of the fuzzy set.
        :param c: Right point of the fuzzy set.
        """
        self.a = a
        self.b = b
        self.c = c

    def membership(self, x):
        """
        Calculate the membership degree of a value 'x' in the fuzzy set.

        :param x: The input value to calculate the membership for.
        :return: The membership degree of 'x' in the fuzzy set.
        """
        if x < self.a or x > self.c:
            return 0.0
        elif self.a <= x < self.b:
            return (x - self.a) / (self.b - self.a)
        elif self.b <= x <= self.c:
            return (self.c - x) / (self.c - self.b)
        else:
            return 1.0

# Example usage:
if __name__ == "__main__":
    # Create a triangular fuzzy set with parameters (a=2, b=4, c=6)
    fuzzy_set = TriangularFuzzySet(2, 4, 6)

    # Calculate the membership degree of values in the set
    values = [3, 4, 5, 6, 7]
    for value in values:
        membership_degree = fuzzy_set.membership(value)
        print(f"Membership of {value} in the fuzzy set: {membership_degree}")
