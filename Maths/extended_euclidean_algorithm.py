# @Author: S. Sharma <silentcat>
# @Date:   2019-02-25T12:08:53-06:00
# @Email:  silentcat@protonmail.com
# @Last modified by:   silentcat
# @Last modified time: 2019-02-25T12:36:52-06:00

import sys

# Finds 2 numbers a and b such that it satisfies
# the equation am + bn = gcd(m, n) (a.k.a Bezout's Identity)
def extended_euclidean_algorithm(m, n):
    a = 1; aprime = 0; b = 0; bprime = 1
    q = 0; r = 1
    c = m; d = n

    while r != 0:
        q = c / d
        r = c % d
        c = n
        d = r

        t = a
        a = aprime
        aprime = int(t - q*a)

        t = b
        b = bprime
        bprime = int(t - q*b)
    return (a, b)

def main():
    if len(sys.argv) < 3:
        print('2 integer arguments required')
        exit(1)
    m = int(sys.argv[1])
    n = int(sys.argv[2])
    print(extended_euclidean_algorithm(m, n))

if __name__ == '__main__':
    main()
