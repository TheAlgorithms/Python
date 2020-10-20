# Fibonacci Sequence Using Recursion and Memoization

# Memoization Concept: https://en.wikipedia.org/wiki/Memoization
# Fibonacci Concept : https://pt.wikipedia.org/wiki/Sequ%C3%AAncia_de_Fibonacci


def fibonacci(n: int, cache: dict = dict()) -> int:
    """
    Return number of index n in sequence fibonacci
    >>> [fibonacci(i) for i in range(12)]
    [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    >>> fibonacci(12)
    144
    """
    aux = n

    try:
        if aux in cache:
            return cache[aux]

        if n in {0, 1}:
            ans = n
        else:
            ans = fibonacci(n - 1, cache) + fibonacci(n - 2, cache)
        cache[aux] = ans

        return ans
    except TypeError:
        print("Error: An integer value is expected")
    except ValueError:
        print("Error: The value must be greater than or equal to zero")


def main() -> None:
    try:
        number = int(input("Enter an integer greater than or equal to 0: "))
        print(f"The first {number} Fibonacci sequence terms are:")
        print([fibonacci(n) for n in range(number)])
        print(f"The {number} index of the fibonacci sequence: ", end="")
        print(fibonacci(number))
    except ValueError:
        print("Error: Input value should be an integer greater than or equal to 0")


if __name__ == "__main__":
    import doctest
    doctest.testmod()
    
    main()
