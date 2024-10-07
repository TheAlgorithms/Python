import random
import sys
from sympy import isprime, mod_inverse
from typing import List, Tuple


def generate_prime_candidate(length: int) -> int:
    """
    Generate a large prime number candidate.

    >>> p = generate_prime_candidate(16)
    >>> isprime(p)
    True
    """
    p = random.getrandbits(length)
    while not isprime(p):
        p = random.getrandbits(length)
    return p


def generate_keys(keysize: int) -> Tuple[Tuple[int, int], Tuple[int, int]]:
    """
    Generate RSA keys.

    >>> public, private = generate_keys(16)
    >>> len(bin(public)) - 2  # Check bit length of n
    32
    >>> len(bin(private)) - 2  # Check bit length of n
    32
    """
    try:
        e = d = n = 0

        p = generate_prime_candidate(keysize)
        q = generate_prime_candidate(keysize)

        n = p * q
        phi = (p - 1) * (q - 1)

        e = random.randrange(1, phi)
        g = gcd(e, phi)
        while g != 1:
            e = random.randrange(1, phi)
            g = gcd(e, phi)

        d = mod_inverse(e, phi)

        return ((e, n), (d, n))
    except ValueError as ex:
        print(f"Value error generating keys: {ex}", file=sys.stderr)
        sys.exit(1)
    except TypeError as ex:
        print(f"Type error generating keys: {ex}", file=sys.stderr)
        sys.exit(1)
    except ArithmeticError as ex:
        print(f"Arithmetic error generating keys: {ex}", file=sys.stderr)
        sys.exit(1)


def gcd(a: int, b: int) -> int:
    """
    Compute the greatest common divisor of a and b.

    >>> gcd(48, 18)
    6
    """
    while b != 0:
        a, b = b, a % b
    return a


def encrypt(pk: Tuple[int, int], plaintext: str) -> List[int]:
    """
    Encrypt a message with a public key.

    >>> public, private = generate_keys(16)
    >>> encrypted = encrypt(public, "test")
    >>> isinstance(encrypted, list)
    True
    """
    try:
        key, n = pk
        cipher = [(ord(char) ** key) % n for char in plaintext]
        return cipher
    except TypeError as ex:
        print(f"Type error during encryption: {ex}", file=sys.stderr)
        return None
    except ValueError as ex:
        print(f"Value error during encryption: {ex}", file=sys.stderr)
        return None
    except OverflowError as ex:
        print(f"Overflow error during encryption: {ex}", file=sys.stderr)
        return None


def decrypt(pk: Tuple[int, int], ciphertext: List[int]) -> str:
    """
    Decrypt a message with a private key.

    >>> public, private = generate_keys(16)
    >>> encrypted = encrypt(public, "test")
    >>> decrypted = decrypt(private, encrypted)
    >>> decrypted == "test"
    True
    """
    try:
        key, n = pk
        plain = [chr((char**key) % n) for char in ciphertext]
        return "".join(plain)
    except TypeError as ex:
        print(f"Type error during decryption: {ex}", file=sys.stderr)
        return None
    except ValueError as ex:
        print(f"Value error during decryption: {ex}", file=sys.stderr)
        return None
    except OverflowError as ex:
        print(f"Overflow error during decryption: {ex}", file=sys.stderr)
        return None


if __name__ == "__main__":
    import doctest

    doctest.testmod()

    try:
        keysize = 1024
        public, private = generate_keys(keysize)

        message = "Hello, RSA!"
        print("Original message:", message)

        encrypted_msg = encrypt(public, message)
        if encrypted_msg:
            print("Encrypted message:", encrypted_msg)

            decrypted_msg = decrypt(private, encrypted_msg)
            if decrypted_msg:
                print("Decrypted message:", decrypted_msg)
            else:
                print("Decryption failed.", file=sys.stderr)
        else:
            print("Encryption failed.", file=sys.stderr)
    except ValueError as ex:
        print(f"Value error: {ex}", file=sys.stderr)
        sys.exit(1)
    except TypeError as ex:
        print(f"Type error: {ex}", file=sys.stderr)
        sys.exit(1)
    except ArithmeticError as ex:
        print(f"Arithmetic error: {ex}", file=sys.stderr)
        sys.exit(1)
