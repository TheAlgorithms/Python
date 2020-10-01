# Fibonacci Sequence Using Recursion and Memoization

# Memoization Concept: https://en.wikipedia.org/wiki/Memoization
# Fibonacci Concept : https://pt.wikipedia.org/wiki/Sequ%C3%AAncia_de_Fibonacci

cache = dict()


def fibonacci(n):
    """
    >>> [fibonacci(i) for i in range(12)]
    [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    """
    aux = n

    if aux in cache:
        return cache[aux]

    if (n == 0) or (n == 1):
        ans = n
    else:
        ans = fibonacci(n - 1) + fibonacci(n - 2)
    cache[aux] = ans

    return ans


def main() -> None:
    lenght = int(input("Enter an integer greater than or equal to 0: "))
    print(f"The first {lenght} Fibbonaci sequence terms are:")
    print([fibonacci(n) for n in range(lenght)])


if __name__ == "__main__":
    main()
