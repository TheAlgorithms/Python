import os
import random
import sys
from typing import Tuple

from maths.greatest_common_divisor import gcd_by_iterative
from . import cryptomath_module, rabin_miller

#Organiser: K. Umut Araz

def rsa_anahtar_cifti_olustur(key_size: int) -> Tuple[Tuple[int, int], Tuple[int, int]]:
    p = rabin_miller.büyük_asal_üret(key_size)
    q = rabin_miller.büyük_asal_üret(key_size)
    n = p * q

    while True:
        e = random.randrange(2 ** (key_size - 1), 2 ** key_size)
        if gcd_by_iterative(e, (p - 1) * (q - 1)) == 1:
            break

    d = cryptomath_module.mod_tersini_bul(e, (p - 1) * (q - 1))

    açık_anahtar = (n, e)
    özel_anahtar = (n, d)
    return açık_anahtar, özel_anahtar

def anahtarı_dosyaya_kaydet(dosya_adı: str, anahtar: Tuple[int, int], anahtar_boyutu: int) -> None:
    with open(dosya_adı, "w") as dosya:
        dosya.write(f"{anahtar_boyutu},{anahtar[0]},{anahtar[1]}")

def ssh_anahtar_cifti_oluştur(name: str, key_size: int) -> None:
    if os.path.exists(f"{name}_rsa_pubkey.txt") or os.path.exists(f"{name}_rsa_privkey.txt"):
        print("\nUYARI:")
        print(
            f'"{name}_rsa_pubkey.txt" veya "{name}_rsa_privkey.txt" zaten mevcut. \n'
            "Farklı bir isim kullanın veya bu dosyaları silip programı yeniden çalıştırın."
        )
        sys.exit()

    açık_anahtar, özel_anahtar = rsa_anahtar_cifti_olustur(key_size)
    print(f"\nAçık anahtar {name}_rsa_pubkey.txt dosyasına yazılıyor...")
    anahtarı_dosyaya_kaydet(f"{name}_rsa_pubkey.txt", açık_anahtar, key_size)

    print(f"Özel anahtar {name}_rsa_privkey.txt dosyasına yazılıyor...")
    anahtarı_dosyaya_kaydet(f"{name}_rsa_privkey.txt", özel_anahtar, key_size)

if __name__ == "__main__":
    print("RSA SSH anahtar çifti oluşturuluyor...")
    ssh_anahtar_cifti_oluştur("ssh", 1024)
    print("Anahtar çifti oluşturma başarılı.")
