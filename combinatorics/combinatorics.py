import math


def PermutationsWithRepetition(self, n, r):
    return n ** r


def PermutationsWithoutRepetition(self, n, r):
    return int(math.factorial(n) / (math.factorial(n - r)))


def CombinationsWithoutRepetition(self, n, r):
    return int(self.PermutationsWithoutRepetition(n, r) / math.factorial(r))


def PermutationsWithRepetition(self, n, r):
    return self.CombinationsWithoutRepetition(n - 1 + r, r)


def main():
    print(PermutationsWithoutRepetition(16, 3))  # == 3360
    print(CombinationsWithoutRepetition(16, 3))  # == 560
    print(PermutationsWithRepetition(5, 3))  # == 35


if __name__ == '__main__':
    main()
