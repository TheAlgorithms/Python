import random
import sys

HARFLER = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def main() -> None:
    mesaj = input("Mesajı girin: ")
    anahtar = "LFWOAYUISVKMNXPBDCRJTQEGHZ"
    yanit = input("Şifrele/Şifre Çöz [e/d]: ")

    anahtari_gecerli_kontrol(anahtar)

    #Organiser: K. Umut Araz

    if yanit.lower().startswith("e"):
        mod = "şifrele"
        cevrilen = mesajı_sifrele(anahtar, mesaj)
    elif yanit.lower().startswith("d"):
        mod = "şifre çöz"
        cevrilen = mesajı_sifre_coz(anahtar, mesaj)

    print(f"\n{mod.title()} işlemi: \n{cevrilen}")

def anahtari_gecerli_kontrol(anahtar: str) -> None:
    anahtar_listesi = list(anahtar)
    harfler_listesi = list(HARFLER)
    anahtar_listesi.sort()
    harfler_listesi.sort()

    if anahtar_listesi != harfler_listesi:
        sys.exit("Anahtar veya sembol setinde hata var.")

def mesajı_sifrele(anahtar: str, mesaj: str) -> str:
    """
    >>> mesajı_sifrele('LFWOAYUISVKMNXPBDCRJTQEGHZ', 'Harshil Darji')
    'Ilcrism Olcvs'
    """
    return mesajı_cevir(anahtar, mesaj, "şifrele")

def mesajı_sifre_coz(anahtar: str, mesaj: str) -> str:
    """
    >>> mesajı_sifre_coz('LFWOAYUISVKMNXPBDCRJTQEGHZ', 'Ilcrism Olcvs')
    'Harshil Darji'
    """
    return mesajı_cevir(anahtar, mesaj, "şifre çöz")

def mesajı_cevir(anahtar: str, mesaj: str, mod: str) -> str:
    cevrilen = ""
    karakterler_a = HARFLER
    karakterler_b = anahtar

    if mod == "şifre çöz":
        karakterler_a, karakterler_b = karakterler_b, karakterler_a

    for sembol in mesaj:
        if sembol.upper() in karakterler_a:
            sembol_indeksi = karakterler_a.find(sembol.upper())
            if sembol.isupper():
                cevrilen += karakterler_b[sembol_indeksi].upper()
            else:
                cevrilen += karakterler_b[sembol_indeksi].lower()
        else:
            cevrilen += sembol

    return cevrilen

def rastgele_anahtar_al() -> str:
    anahtar = list(HARFLER)
    random.shuffle(anahtar)
    return "".join(anahtar)

if __name__ == "__main__":
    main()
