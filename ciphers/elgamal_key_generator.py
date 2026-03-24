import os
import secrets
import sys

from . import cryptomath_module as cryptomath
from . import rabin_miller

min_primitive_root = 3


# Algorithm 4.80 from Handbook of Applied Cryptography
# (CRC Press, ISBN: 0-8493-8523-7, October 1996).
#
# For a large prime p, p-1 = 2 * ((p-1)/2).  A generator g of Z_p* must
# satisfy g^((p-1)/q) ≢ 1 (mod p) for every prime factor q of p-1.
# Because p is a safe-ish large prime here, checking q=2 (i.e. the Legendre
# symbol) is the dominant filter; we also skip g=2 as a degenerate case.
def primitive_root(p_val: int) -> int:
    """
    Return a primitive root modulo the prime p_val.

    >>> p = 23  # small prime for testing
    >>> g = primitive_root(p)
    >>> pow(g, (p - 1) // 2, p) != 1
    True
    >>> 3 <= g < p
    True
    """
    print("Generating primitive root of p")
    while True:
        g = secrets.randbelow(p_val - 3) + 3  # range [3, p_val-1]
        # g must not be a quadratic residue mod p (order would divide (p-1)/2)
        if pow(g, (p_val - 1) // 2, p_val) == 1:
            continue
        return g


def generate_key(key_size: int) -> tuple[tuple[int, int, int, int], tuple[int, int]]:
    print("Generating prime p...")
    p = rabin_miller.generate_large_prime(key_size)  # select large prime number.
    e_1 = primitive_root(p)  # one primitive root on modulo p.
    d = secrets.randbelow(p - 3) + 3  # private key in [3, p-1]
    e_2 = cryptomath.find_mod_inverse(pow(e_1, d, p), p)

    public_key = (key_size, e_1, e_2, p)
    private_key = (key_size, d)

    return public_key, private_key


def make_key_files(name: str, key_size: int) -> None:
    if os.path.exists(f"{name}_pubkey.txt") or os.path.exists(f"{name}_privkey.txt"):
        print("\nWARNING:")
        print(
            f'"{name}_pubkey.txt" or "{name}_privkey.txt" already exists. \n'
            "Use a different name or delete these files and re-run this program."
        )
        sys.exit()

    public_key, private_key = generate_key(key_size)
    print(f"\nWriting public key to file {name}_pubkey.txt...")
    with open(f"{name}_pubkey.txt", "w") as fo:
        fo.write(f"{public_key[0]},{public_key[1]},{public_key[2]},{public_key[3]}")

    print(f"Writing private key to file {name}_privkey.txt...")
    with open(f"{name}_privkey.txt", "w") as fo:
        fo.write(f"{private_key[0]},{private_key[1]}")


def main() -> None:
    print("Making key files...")
    make_key_files("elgamal", 2048)
    print("Key files generation successful")


if __name__ == "__main__":
    main()
