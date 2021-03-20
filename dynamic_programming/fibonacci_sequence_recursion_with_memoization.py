# Fibonacci Sequence Using Recursion and Memoization

# Memoization Concept: https://en.wikipedia.org/wiki/Memoization
# Fibonacci Concept : https://pt.wikipedia.org/wiki/Sequ%C3%AAncia_de_Fibonacci

class Fibonacci():
    def __init__(self):
        self.cache: Dict[int, int] = dict()

    def __getitem__(self, key: int) -> int:
        return self.__calculate_fibonacci(key)

    
    def __calculate_fibonacci(self, n: int) -> int:
        """
        Return number of index n in sequence fibonacci
        >>> fibonacci = Fibonacci()
        >>> [fibonacci[i] for i in range(12)]
        [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
        >>> fibonacci[12]
        144
        """

        if type(n) != int:
            raise "An integer value is expected"

        elif(n < 0):
            raise "The value must be greater than or equal to zero"

        if n in self.cache:
            return self.cache[n]

        if n in {0, 1}:
            ans = n
        else:
            ans = self.__calculate_fibonacci(n - 1) + self.__calculate_fibonacci(n - 2)
        self.cache[n] = ans
        return ans


def main() -> None:
    fibonacci = Fibonacci()
    number = int(input("Enter an integer greater than or equal to 0: "))
    print(f"The first {number} Fibonacci sequence terms are:")
    print([fibonacci[n] for n in range(number)])
    print(f"The {number} index of the fibonacci sequence: ", end="")
    print(fibonacci[number])

if __name__ == "__main__":
    import doctest
    doctest.testmod()
    main()
