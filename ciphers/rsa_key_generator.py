import os
import secrets
import sys

from maths.greatest_common_divisor import gcd_by_iterative

from . import cryptomath_module, rabin_miller


def main() -> None:
    print("Making key files...")
    make_key_files("rsa", 1024)
    print("Key files generation successful.")


def generate_key(key_size: int) -> tuple[tuple[int, int], tuple[int, int]]:
    """
    Generate an RSA key pair of the given bit size.

    Uses secrets.randbits (CSPRNG) for all random values so that generated
    keys are not predictable from observed outputs.

    >>> public_key, private_key = generate_key(16)
    >>> public_key[0] == private_key[0]  # same modulus n
    True
    >>> 0 < public_key[1] < public_key[0]  # e < n
    True
    >>> 0 < private_key[1] < private_key[0]  # d < n
    True
    """
    p = rabin_miller.generate_large_prime(key_size)
    q = rabin_miller.generate_large_prime(key_size)
    n = p * q

    # Generate e that is relatively prime to (p - 1) * (q - 1)
    while True:
        # Set the high bit so e is always in [2^(key_size-1), 2^key_size - 1]
        e = secrets.randbits(key_size) | (1 << (key_size - 1))
        if gcd_by_iterative(e, (p - 1) * (q - 1)) == 1:
            break

    # Calculate d that is mod inverse of e
    d = cryptomath_module.find_mod_inverse(e, (p - 1) * (q - 1))

    public_key = (n, e)
    private_key = (n, d)
    return (public_key, private_key)


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
    with open(f"{name}_pubkey.txt", "w") as out_file:
        out_file.write(f"{key_size},{public_key[0]},{public_key[1]}")

    print(f"Writing private key to file {name}_privkey.txt...")
    with open(f"{name}_privkey.txt", "w") as out_file:
        out_file.write(f"{key_size},{private_key[0]},{private_key[1]}")


if __name__ == "__main__":
    main()
