import random, sys, os
import rabin_miller as rabinMiller, cryptomath_module as cryptoMath


def main():
    print("Making key files...")
    makeKeyFiles("rsa", 1024)
    print("Key files generation successful.")


    
from random import randrange, getrandbits
def is_prime(n, k=128):
    """ Test if a number is prime
        Args:
            n -- int -- the number to test
            k -- int -- the number of tests to do
        return True if n is prime
    """
    # Test if n is not even.
    # But care, 2 is prime !
    if n == 2 or n == 3:
        return True
    if n <= 1 or n % 2 == 0:
        return False
    # find r and s
    s = 0
    r = n - 1
    while r & 1 == 0:
        s += 1
        r //= 2
    # do k tests
    for _ in range(k):
        a = randrange(2, n - 1)
        x = pow(a, r, n)
        if x != 1 and x != n - 1:
            j = 1
            while j < s and x != n - 1:
                x = pow(x, 2, n)
                if x == 1:
                    return False
                j += 1
            if x != n - 1:
                return False
    return True
def generate_prime_candidate(length):
    """ Generate an odd integer randomly
        Args:
            length -- int -- the length of the number to generate, in bits
        return a integer
    """
    # generate random bits
    p = getrandbits(length)
    # apply a mask to set MSB and LSB to 1
    p |= (1 << length - 1) | 1
    return p
def generate_prime_number(length=1024):
    """ Generate a prime
        Args:
            length -- int -- length of the prime to generate, in          bits
        return a prime
    """
    p = 4
    # keep generating while the primality test fail
    while not is_prime(p, 128):
        p = generate_prime_candidate(length)
    return p

p = generate_prime_number()

q = generate_prime_number()

"""From Scratch implementation of Generating large prime_numbers"""
def makeKeyFiles(name, keySize):
    if os.path.exists("%s_pubkey.txt" % (name)) or os.path.exists(
        "%s_privkey.txt" % (name)
    ):
        print("\nWARNING:")
        print(
            '"%s_pubkey.txt" or "%s_privkey.txt" already exists. \nUse a different name or delete these files and re-run this program.'
            % (name, name)
        )
        sys.exit()

    publicKey, privateKey = generateKey(keySize)
    print("\nWriting public key to file %s_pubkey.txt..." % name)
    with open("%s_pubkey.txt" % name, "w") as fo:
        fo.write("%s,%s,%s" % (keySize, publicKey[0], publicKey[1]))

    print("Writing private key to file %s_privkey.txt..." % name)
    with open("%s_privkey.txt" % name, "w") as fo:
        fo.write("%s,%s,%s" % (keySize, privateKey[0], privateKey[1]))


if __name__ == "__main__":
    main()
