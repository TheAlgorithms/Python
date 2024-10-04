import os
import random
import sys
from typing import Tuple

from maths.greatest_common_divisor import gcd_by_iterative
from . import cryptomath_module, rabin_miller

def generate_rsa_keypair(key_size: int) -> Tuple[Tuple[int, int], Tuple[int, int]]:
    p = rabin_miller.generate_large_prime(key_size)
    q = rabin_miller.generate_large_prime(key_size)
    n = p * q

    while True:
        e = random.randrange(2 ** (key_size - 1), 2 ** key_size)
        if gcd_by_iterative(e, (p - 1) * (q - 1)) == 1:
            break

    d = cryptomath_module.find_mod_inverse(e, (p - 1) * (q - 1))

    public_key = (n, e)
    private_key = (n, d)
    return public_key, private_key

def save_key_to_file(filename: str, key: Tuple[int, int], key_size: int) -> None:
    with open(filename, "w") as file:
        file.write(f"{key_size},{key[0]},{key[1]}")

def create_ssh_keypair(name: str, key_size: int) -> None:
    if os.path.exists(f"{name}_rsa_pubkey.txt") or os.path.exists(f"{name}_rsa_privkey.txt"):
        print("\nUYARI:")
        print(
            f'"{name}_rsa_pubkey.txt" veya "{name}_rsa_privkey.txt" zaten mevcut. \n'
            "Farklı bir isim kullanın veya bu dosyaları silip programı yeniden çalıştırın."
        )
        sys.exit()

    public_key, private_key = generate_rsa_keypair(key_size)
    print(f"\nAçık anahtar {name}_rsa_pubkey.txt dosyasına yazılıyor...")
    save_key_to_file(f"{name}_rsa_pubkey.txt", public_key, key_size)

    print(f"Özel anahtar {name}_rsa_privkey.txt dosyasına yazılıyor...")
    save_key_to_file(f"{name}_rsa_privkey.txt", private_key, key_size)

if __name__ == "__main__":
    print("RSA SSH anahtar çifti oluşturuluyor...")
    create_ssh_keypair("ssh", 1024)
    print("Anahtar çifti oluşturma başarılı.")
