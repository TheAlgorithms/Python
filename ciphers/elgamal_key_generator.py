import os
import random
import sys

from . import cryptomath_module as cryptomath
from . import rabin_miller

min_primitive_root = 3


# I have written my code naively same as definition of primitive root
# however every time I run this program, memory exceeded...
# so I used 4.80 Algorithm in
# Handbook of Applied Cryptography(CRC Press, ISBN : 0-8493-8523-7, October 1996)
# and it seems to run nicely!
def primitive_root(p_val: int) -> int:
    print("Generating primitive root of p")
    while True:
        g = random.randrange(3, p_val)
        if pow(g, 2, p_val) == 1:
            continue
        if pow(g, p_val, p_val) == 1:
            continue
        return g


def generate_key(key_size: int) -> tuple[tuple[int, int, int, int], tuple[int, int]]:
    print("Generating prime p...")
    p = rabin_miller.generateLargePrime(key_size)  # select large prime number.
    e_1 = primitive_root(p)  # one primitive root on modulo p.
    d = random.randrange(3, p)  # private_key -> have to be greater than 2 for safety.
    e_2 = cryptomath.find_mod_inverse(pow(e_1, d, p), p)

    public_key = (key_size, e_1, e_2, p)
    private_key = (key_size, d)

    return public_key, private_key


def make_key_files(name: str, keySize: int) -> None:
    if os.path.exists(f"{name}_pubkey.txt") or os.path.exists(f"{name}_privkey.txt"):
        print("\nWARNING:")
        print(
            '"%s_pubkey.txt" or "%s_privkey.txt" already exists. \n'
            "Use a different name or delete these files and re-run this program."
            % (name, name)
        )
        sys.exit()

    publicKey, privateKey = generate_key(keySize)
    print(f"\nWriting public key to file {name}_pubkey.txt...")
    with open(f"{name}_pubkey.txt", "w") as fo:
        fo.write(
            "%d,%d,%d,%d" % (publicKey[0], publicKey[1], publicKey[2], publicKey[3])
        )

    print(f"Writing private key to file {name}_privkey.txt...")
    with open(f"{name}_privkey.txt", "w") as fo:
        fo.write("%d,%d" % (privateKey[0], privateKey[1]))


def main() -> None:
    print("Making key files...")
    make_key_files("elgamal", 2048)
    print("Key files generation successful")


if __name__ == "__main__":
    main()
