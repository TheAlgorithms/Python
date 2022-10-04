# to get a simple introduction to tail recursion

"""
In a tail recursive function, the recursive call is the last statement which is executed by the compiler.
How are tail recursive functions useful?
Ususally the compiler can easily optimize tail recursive functions by completely removing the functions's stack frame during the recursive call itself.

"""


def example_of_tail_recursive_factorial(n: int, ans: int = 1) -> int:
    """
    this fuction simply prints numbers from 1 to n
    >>> example_of_tail_recursive_factorial(5)
    120
    >>> example_of_tail_recursive_factorial(4)
    24
    """

    if n <= 1:
        return ans

    # last statement of the function is recursive call this is tail recursive function
    return example_of_tail_recursive_factorial(n - 1, ans * n)


if __name__ == "__main__":
    print(example_of_tail_recursive_factorial(4))
