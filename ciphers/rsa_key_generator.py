import os
import random
import sys

from . import cryptomath_module as cryptoMath  # noqa: N812
from . import rabin_miller as rabinMiller  # noqa: N812


def main() -> None:
    print("Making key files...")
    make_key_files("rsa", 1024)
    print("Key files generation successful.")


def generate_key(key_size: int) -> tuple[tuple[int, int], tuple[int, int]]:
    print("Generating prime p...")
    p = rabinMiller.generate_large_prime(key_size)
    print("Generating prime q...")
    q = rabinMiller.generate_large_prime(key_size)
    n = p * q

    print("Generating e that is relatively prime to (p - 1) * (q - 1)...")
    while True:
        e = random.randrange(2 ** (key_size - 1), 2 ** (key_size))
        if cryptoMath.gcd(e, (p - 1) * (q - 1)) == 1:
            break

    print("Calculating d that is mod inverse of e...")
    d = cryptoMath.find_mod_inverse(e, (p - 1) * (q - 1))

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
