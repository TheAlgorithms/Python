# fibonacci.py
"""
1. Calculates the iterative fibonacci sequence

2. Calculates the fibonacci sequence with a formula
    an = [ Phin - (phi)n ]/Sqrt[5]
    reference-->Su, Francis E., et al. "Fibonacci Number Formula." Math Fun Facts. <http://www.math.hmc.edu/funfacts>
"""
import math
import functools
import time
from decimal import getcontext, Decimal

getcontext().prec = 100


def timer_decorator(func):
    @functools.wraps(func)
    def timer_wrapper(*args, **kwargs):
        start = time.time()
        func(*args, **kwargs)
        end = time.time()
        if int(end - start) > 0:
            print(f"Run time for {func.__name__}: {(end - start):0.2f}s")
        else:
            print(f"Run time for {func.__name__}: {(end - start)*1000:0.2f}ms")
        return func(*args, **kwargs)

    return timer_wrapper


# define Python user-defined exceptions
class Error(Exception):
    """Base class for other exceptions"""


class ValueTooLargeError(Error):
    """Raised when the input value is too large"""


class ValueTooSmallError(Error):
    """Raised when the input value is not greater than one"""


class ValueLessThanZero(Error):
    """Raised when the input value is less than zero"""


def _check_number_input(n, min_thresh, max_thresh=None):
    """
    :param n: single integer
    :type n: int
    :param min_thresh: min threshold, single integer
    :type min_thresh: int
    :param max_thresh: max threshold, single integer
    :type max_thresh: int
    :return: boolean
    """
    try:
        if n >= min_thresh and max_thresh is None:
            return True
        elif min_thresh <= n <= max_thresh:
            return True
        elif n < 0:
            raise ValueLessThanZero
        elif n < min_thresh:
            raise ValueTooSmallError
        elif n > max_thresh:
            raise ValueTooLargeError
    except ValueLessThanZero:
        print("Incorrect Input: number must not be less than 0")
    except ValueTooSmallError:
        print(
            f"Incorrect Input: input number must be > {min_thresh} for the recursive calculation"
        )
    except ValueTooLargeError:
        print(
            f"Incorrect Input: input number must be < {max_thresh} for the recursive calculation"
        )
    return False


@timer_decorator
def fib_iterative(n):
    """
    :param n: calculate Fibonacci to the nth integer
    :type n:int
    :return: Fibonacci sequence as a list
    """
    n = int(n)
    if _check_number_input(n, 2):
        seq_out = [0, 1]
        a, b = 0, 1
        for _ in range(n - len(seq_out)):
            a, b = b, a + b
            seq_out.append(b)
        return seq_out


@timer_decorator
def fib_formula(n):
    """
    :param n: calculate Fibonacci to the nth integer
    :type n:int
    :return: Fibonacci sequence as a list
    """
    seq_out = [0, 1]
    n = int(n)
    if _check_number_input(n, 2, 1000000):
        sqrt = Decimal(math.sqrt(5))
        phi_1 = Decimal(1 + sqrt) / Decimal(2)
        phi_2 = Decimal(1 - sqrt) / Decimal(2)
        for i in range(2, n):
            temp_out = ((phi_1 ** Decimal(i)) - (phi_2 ** Decimal(i))) * (
                Decimal(sqrt) ** Decimal(-1)
            )
            seq_out.append(int(temp_out))
        return seq_out


if __name__ == "__main__":
    num = 20
    # print(f'{fib_recursive(num)}\n')
    # print(f'{fib_iterative(num)}\n')
    # print(f'{fib_formula(num)}\n')
    fib_iterative(num)
    fib_formula(num)
