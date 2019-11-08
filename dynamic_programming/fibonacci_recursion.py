"""
This program uses a top-down approach that calculates the
nth Fibonacci number in O(n). However, large n can result
in RecusionError due to the maximum recursion depth.

"""
import sys


def fibonacci(n, memo=None):
    if memo == None:  # a dictionary to store temporary result
        memo = {}
    if n in memo:
        return memo[n]
    if n in (0, 1):  # the 0th and 1st number are 0 and 1
        result = n
    else:
        try:
            result = fibonacci(n - 1, memo) + fibonacci(n - 2, memo)
        except RecursionError:
            print("maximum recursion depth exceeded.")
            exit(1)
    memo[n] = result
    return result


if __name__ == "__main__":
    args = sys.argv[1:]
    if len(args) != 1:
        print("input only 1 number")
        exit(1)
    try:
        n = int(args[0])
    except ValueError:
        print("Could not convert data to an integer.")
        exit(1)
    print(" the %d fibonacci number: %d" % (n, fibonacci(n)))
