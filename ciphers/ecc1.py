'''
Author : Dhruv B Kakadiya

'''
# import libraries
from multiplicative_inverse import find_mul_inverse
from prime_number_generater import simple_testing, miller_rabin_test
import math

# find power mod prime
def power_nmod (a, n, prime):
    res = 1
    a %= prime
    if (a == 0):
        return (0)
    while (n > 0):
        if ((n & 1) == 1):
            res = (res * a) % prime
        n >>= 1
        a = (a ** 2) % prime
    return (res)

# checking for valid parameters
def is_valid_ab (a, b):
    if (4 * (a ** 3) + 3 * (b ** 2) == 0):
        print(f"\nNot valid a = {a} and b = {b}")
        return (False)
    else:
        print(f"\na = {a} and b = {b} is valid!")
        return (True)

# find all possible points
def find_points_elliptic_curve(a, b, prime):
    if (is_valid_ab(a, b)):
        x = 0
        all_points = []
        while (x < prime):
            w = ((x ** 3) + (a * x) + b) % prime
            if (power_nmod(w, ((prime - 1) // 2), prime) == 1):
                root = math.sqrt(w)
                while (math.ceil(root) != root):
                    w += prime
                    root = math.sqrt(w)
                all_points.append((x, int(root % prime)))
                all_points.append((x, int((-root) % prime)))
            if (power_nmod(w, ((prime - 1) // 2), prime) == -1):
                print(f"\nNo Solutions! for x = {x}")
            x += 1
        return (all_points)
    else:
        return ([])

# main if condition
if __name__ == "__main__":
    n = int(input("\nEnter the number of bits of prime number :- "))
    while (True):
        n_bit_prime = simple_testing(n)
        if (not miller_rabin_test(n_bit_prime)):
            continue
        else:
            prime = n_bit_prime
            break

    a, b = map(int, input("\nEnter two points a, b :- ").split())
    print(f"\nThe prime number is => '{prime}'")
    prime = 13
    all_points = find_points_elliptic_curve(a, b, prime)
    print(all_points, end = "\n")