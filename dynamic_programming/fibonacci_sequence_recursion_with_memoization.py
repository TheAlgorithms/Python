# Fibonacci Sequence Using Recursion and Memoization

# Memoization Concept: https://en.wikipedia.org/wiki/Memoization
# Fibonacci Concept : https://pt.wikipedia.org/wiki/Sequ%C3%AAncia_de_Fibonacci

class Fibonacci:

    def __init__(self) -> None:
        self.cache: Dict[int, int] = dict()

    def __getitem__(self, key: int) -> int:
        """
        Return number of index n in sequence fibonacci
        >>> fibonacci = Fibonacci()
        >>> [fibonacci[i] for i in range(12)]
        [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
        >>> fibonacci[12]
        144
        """
        if type(key) != int:
            raise "An integer value is expected"

        elif key < 0:
            raise "The value must be greater than or equal to zero"

        if key in self.cache:
            return self.cache[key]

        if key in {0, 1}:
            ans = key
        else:
            ans = self.__getitem__(key - 1) + self.__getitem__(key - 2)
        self.cache[key] = ans
        return ans



def main(number: int) -> None:
    """
    >>> main(3)
    The first 3 Fibonacci sequence terms are: [0, 1, 1]
    The 3 index of the fibonacci sequence: 2
    """
    fibonacci = Fibonacci()
    print(f"The first {number} Fibonacci sequence terms are:", end=" ")
    print([fibonacci[n] for n in range(number)])
    print(f"The {number} index of the fibonacci sequence:", end=" ")
    print(fibonacci[number])

if __name__ == "__main__":
    import doctest

    doctest.testmod()
    main(int(input("Enter an integer greater than or equal to 0: ")))
