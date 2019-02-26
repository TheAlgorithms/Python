# @Author: S. Sharma <silentcat>
# @Date:   2019-02-25T12:08:53-06:00
# @Email:  silentcat@protonmail.com
# @Last modified by:   silentcat
# @Last modified time: 2019-02-26T07:07:38-06:00

import sys

# Finds 2 numbers a and b such that it satisfies
# the equation am + bn = gcd(m, n) (a.k.a Bezout's Identity)
def extended_euclidean_algorithm(m, n):
    a = 0; aprime = 1; b = 1; bprime = 0
    q = 0; r = 0
    if m > n:
        c = m; d = n
    else:
        c = n; d = m

    while True:
        q = int(c / d)
        r = c % d
        if r == 0:
            break
        c = d
        d = r

        t = aprime
        aprime = a
        a = t - q*a

        t = bprime
        bprime = b
        b = t - q*b

    pair = None
    if m > n:
        pair = (a,b)
    else:
        pair = (b,a)
    return pair

def main():
    if len(sys.argv) < 3:
        print('2 integer arguments required')
        exit(1)
    m = int(sys.argv[1])
    n = int(sys.argv[2])
    print(extended_euclidean_algorithm(m, n))

if __name__ == '__main__':
    main()
