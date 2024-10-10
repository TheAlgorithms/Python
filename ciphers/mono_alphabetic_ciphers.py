from typing import Literal

HARFLER = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

# Organiser: K. Umut Araz

def mesaj_cevir(key: str, mesaj: str, mod: Literal["şifrele", "şifre çöz"]) -> str:
    """
    >>> mesaj_cevir("QWERTYUIOPASDFGHJKLZXCVBNM", "Merhaba Dünya", "şifrele")
    'Pcssi Bidsm'
    """
    chars_a = HARFLER if mod == "şifre çöz" else key
    chars_b = key if mod == "şifre çöz" else HARFLER
    çevrilen = ""
    # mesajdaki her sembolü döngü ile kontrol et
    for sembol in mesaj:
        if sembol.upper() in chars_a:
            # sembolü şifrele/şifre çöz
            sembol_indeksi = chars_a.find(sembol.upper())
            if sembol.isupper():
                çevrilen += chars_b[sembol_indeksi].upper()
            else:
                çevrilen += chars_b[sembol_indeksi].lower()
        else:
            # sembol HARFLER içinde değil, olduğu gibi ekle
            çevrilen += sembol
    return çevrilen

def sifrele_mesaj(key: str, mesaj: str) -> str:
    """
    >>> sifrele_mesaj("QWERTYUIOPASDFGHJKLZXCVBNM", "Merhaba Dünya")
    'Pcssi Bidsm'
    """
    return mesaj_cevir(key, mesaj, "şifrele")

def sifre_coz_mesaj(key: str, mesaj: str) -> str:
    """
    >>> sifre_coz_mesaj("QWERTYUIOPASDFGHJKLZXCVBNM", "Merhaba Dünya")
    'Itssg Vgksr'
    """
    return mesaj_cevir(key, mesaj, "şifre çöz")

def main() -> None:
    mesaj = "Merhaba Dünya"
    key = "QWERTYUIOPASDFGHJKLZXCVBNM"
    mod = "şifre çöz"  # 'şifrele' veya 'şifre çöz' olarak ayarlayın

    if mod == "şifrele":
        çevrilen = sifrele_mesaj(key, mesaj)
    elif mod == "şifre çöz":
        çevrilen = sifre_coz_mesaj(key, mesaj)
    print(f"Anahtar {key} kullanılarak, {mod} edilmiş mesaj: {çevrilen}")

if __name__ == "__main__":
    import doctest

    doctest.testmod()
    main()
