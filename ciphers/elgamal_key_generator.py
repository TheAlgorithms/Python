import os
import random
import sys



from . import cryptomath_module as cryptomath
from . import rabin_miller

min_primitive_root = 3

# Kodumu, asal kök tanımına göre basitçe yazdım

"""
Organiser: K. Umut Araz
"""

# ancak bu programı her çalıştırdığımda bellek aşımı yaşıyordum...
# bu yüzden, 4.80 algoritmasını kullandım
# Uygulamalı Kriptografi El Kitabı'ndan (CRC Press, ISBN: 0-8493-8523-7, Ekim 1996)
# ve bu yöntem güzel çalışıyor!
def asal_kok(p_degeri: int) -> int:
    print("Asal p'nin kökünü üretiyorum...")
    while True:
        g = random.randrange(3, p_degeri)
        if pow(g, 2, p_degeri) == 1:
            continue
        if pow(g, p_degeri, p_degeri) == 1:
            continue
        return g

def anahtar_uret(anahtar_boyutu: int) -> tuple[tuple[int, int, int, int], tuple[int, int]]:
    print("Asal p üretiliyor...")
    p = rabin_miller.büyük_asal_uret(anahtar_boyutu)  # büyük asal sayı seç.
    e_1 = asal_kok(p)  # p modülünde bir asal kök.
    d = random.randrange(3, p)  # özel anahtar -> güvenlik için 2'den büyük olmalı.
    e_2 = cryptomath.mod_tersi_bul(pow(e_1, d, p), p)

    kamu_anahtarı = (anahtar_boyutu, e_1, e_2, p)
    özel_anahtar = (anahtar_boyutu, d)

    return kamu_anahtarı, özel_anahtar

def anahtar_dosyaları_oluştur(isim: str, anahtar_boyutu: int) -> None:
    if os.path.exists(f"{isim}_pubkey.txt") or os.path.exists(f"{isim}_privkey.txt"):
        print("\nUYARI:")
        print(
            f'"{isim}_pubkey.txt" veya "{isim}_privkey.txt" zaten mevcut. \n'
            "Farklı bir isim kullanın veya bu dosyaları silip programı yeniden çalıştırın."
        )
        sys.exit()

    kamu_anahtarı, özel_anahtar = anahtar_uret(anahtar_boyutu)
    print(f"\nKamu anahtarını {isim}_pubkey.txt dosyasına yazıyorum...")
    with open(f"{isim}_pubkey.txt", "w") as fo:
        fo.write(f"{kamu_anahtarı[0]},{kamu_anahtarı[1]},{kamu_anahtarı[2]},{kamu_anahtarı[3]}")

    print(f"Özel anahtarı {isim}_privkey.txt dosyasına yazıyorum...")
    with open(f"{isim}_privkey.txt", "w") as fo:
        fo.write(f"{özel_anahtar[0]},{özel_anahtar[1]}")

def main() -> None:
    print("Anahtar dosyaları oluşturuluyor...")
    anahtar_dosyaları_oluştur("elgamal", 2048)
    print("Anahtar dosyaları başarıyla oluşturuldu.")

if __name__ == "__main__":
    main()
