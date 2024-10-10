import random
import sys

from maths.greatest_common_divisor import gcd_by_iterative

from . import cryptomath_module as cryptomath

SYMBOLS = (
    r""" !"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^_`"""
    r"""abcdefghijklmnopqrstuvwxyz{|}~
    
    Organiser: K. Umut Araz
    """
)


def anahtar_kontrol(key_a: int, key_b: int, mod: str) -> None:
    if mod == "şifrele":
        if key_a == 1:
            sys.exit(
                "Affine şifreleme, anahtar A 1 olarak ayarlandığında zayıf hale gelir. "
                "Farklı bir anahtar seçin."
            )
        if key_b == 0:
            sys.exit(
                "Affine şifreleme, anahtar B 0 olarak ayarlandığında zayıf hale gelir. "
                "Farklı bir anahtar seçin."
            )
    if key_a < 0 or key_b < 0 or key_b > len(SYMBOLS) - 1:
        sys.exit(
            "Anahtar A 0'dan büyük olmalı ve anahtar B 0 ile "
            f"{len(SYMBOLS) - 1} arasında olmalıdır."
        )
    if gcd_by_iterative(key_a, len(SYMBOLS)) != 1:
        sys.exit(
            f"Anahtar A {key_a} ve sembol seti boyutu {len(SYMBOLS)} "
            "birbirine asal değildir. Farklı bir anahtar seçin."
        )


def mesajı_şifrele(key: int, mesaj: str) -> str:
    """
    >>> mesajı_şifrele(4545, 'Affine şifreleme, monoalfabetik '
    ...                       'yerine geçme şifreleme türüdür.')
    'VL}p MM{I}p~{HL}Gp{vp pFsH}pxMpyxIx JHL O}F{~pvuOvF{FuF{xIp~{HL}Gi'
    """
    key_a, key_b = divmod(key, len(SYMBOLS))
    anahtar_kontrol(key_a, key_b, "şifrele")
    şifreli_metin = ""
    for sembol in mesaj:
        if sembol in SYMBOLS:
            sembol_indeksi = SYMBOLS.find(sembol)
            şifreli_metin += SYMBOLS[(sembol_indeksi * key_a + key_b) % len(SYMBOLS)]
        else:
            şifreli_metin += sembol
    return şifreli_metin


def mesajı_çöz(key: int, mesaj: str) -> str:
    """
    >>> mesajı_çöz(4545, 'VL}p MM{I}p~{HL}Gp{vp pFsH}pxMpyxIx JHL O}F{~pvuOvF{FuF'
    ...                       '{xIp~{HL}Gi')
    'Affine şifreleme, monoalfabetik yerine geçme şifreleme türüdür.'
    """
    key_a, key_b = divmod(key, len(SYMBOLS))
    anahtar_kontrol(key_a, key_b, "çöz")
    düz_metin = ""
    mod_tersi_key_a = cryptomath.find_mod_inverse(key_a, len(SYMBOLS))
    for sembol in mesaj:
        if sembol in SYMBOLS:
            sembol_indeksi = SYMBOLS.find(sembol)
            düz_metin += SYMBOLS[
                (sembol_indeksi - key_b) * mod_tersi_key_a % len(SYMBOLS)
            ]
        else:
            düz_metin += sembol
    return düz_metin


def rastgele_anahtar_al() -> int:
    while True:
        key_b = random.randint(2, len(SYMBOLS))
        if gcd_by_iterative(key_b, len(SYMBOLS)) == 1 and key_b % len(SYMBOLS) != 0:
            return key_b * len(SYMBOLS) + key_b


def ana_fonksiyon() -> None:
    """
    >>> key = rastgele_anahtar_al()
    >>> msg = "Bu bir testtir!"
    >>> mesajı_çöz(key, mesajı_şifrele(key, msg)) == msg
    True
    """
    mesaj = input("Mesajı girin: ").strip()
    key = int(input("Anahtarı girin [2000 - 9000]: ").strip())
    mod = input("Şifrele/Çöz [Ş/C]: ").strip().lower()

    if mod.startswith("ş"):
        mod = "şifrele"
        çevrilen = mesajı_şifrele(key, mesaj)
    elif mod.startswith("c"):
        mod = "çöz"
        çevrilen = mesajı_çöz(key, mesaj)
    print(f"\n{mod.title()}ilmiş metin: \n{çevrilen}")


if __name__ == "__main__":
    import doctest

    doctest.testmod()
    # ana_fonksiyon()
