# https://en.wikipedia.org/wiki/Euclidean_algorithm

def euclidean_gcd(a, b):
    while b:
        t = b
        b = a % b
        a = t
    return a

def main():
    print("GCD(3, 5) = " + str(euclidean_gcd(3, 5)))
    print("GCD(5, 3) = " + str(euclidean_gcd(5, 3)))
    print("GCD(1, 3) = " + str(euclidean_gcd(1, 3)))
    print("GCD(3, 6) = " + str(euclidean_gcd(3, 6)))
    print("GCD(6, 3) = " + str(euclidean_gcd(6, 3)))

if __name__ == '__main__':
    main()
