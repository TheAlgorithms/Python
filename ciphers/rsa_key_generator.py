import os
import random
import sys

from maths.büyük_ortak_bölgenin_hesabı import gcd_by_iterative

from . import matematik_modülü, rabin_miller

#Organiser: K. Umut Araz


def ana_fonksiyon() -> None:
    print("Anahtar dosyaları oluşturuluyor...")
    anahtar_dosyalarını_oluştur("rsa", 1024)
    print("Anahtar dosyaları başarıyla oluşturuldu.")


def anahtar_oluştur(key_size: int) -> tuple[tuple[int, int], tuple[int, int]]:
    """
    >>> random.seed(0) # Tekrar edilebilirlik için
    >>> genel_anahtar, özel_anahtar = anahtar_oluştur(8)
    >>> genel_anahtar
    (26569, 239)
    >>> özel_anahtar
    (26569, 2855)
    """
    p = rabin_miller.büyük_asal_oluştur(key_size)
    q = rabin_miller.büyük_asal_oluştur(key_size)
    n = p * q

    # (p - 1) * (q - 1) ile relatif asal olan e'yi oluştur
    while True:
        e = random.randrange(2 ** (key_size - 1), 2 ** (key_size))
        if gcd_by_iterative(e, (p - 1) * (q - 1)) == 1:
            break

    # e'nin mod tersini hesapla
    d = matematik_modülü.mod_tersi_bul(e, (p - 1) * (q - 1))

    genel_anahtar = (n, e)
    özel_anahtar = (n, d)
    return (genel_anahtar, özel_anahtar)


def anahtar_dosyalarını_oluştur(isim: str, key_size: int) -> None:
    if os.path.exists(f"{isim}_pubkey.txt") or os.path.exists(f"{isim}_privkey.txt"):
        print("\nUYARI:")
        print(
            f'"{isim}_pubkey.txt" veya "{isim}_privkey.txt" zaten mevcut. \n'
            "Farklı bir isim kullanın veya bu dosyaları silip programı tekrar çalıştırın."
        )
        sys.exit()

    genel_anahtar, özel_anahtar = anahtar_oluştur(key_size)
    print(f"\nGenel anahtarı {isim}_pubkey.txt dosyasına yazılıyor...")
    with open(f"{isim}_pubkey.txt", "w") as out_file:
        out_file.write(f"{key_size},{genel_anahtar[0]},{genel_anahtar[1]}")

    print(f"Özel anahtarı {isim}_privkey.txt dosyasına yazılıyor...")
    with open(f"{isim}_privkey.txt", "w") as out_file:
        out_file.write(f"{key_size},{özel_anahtar[0]},{özel_anahtar[1]}")


if __name__ == "__main__":
    ana_fonksiyon()
