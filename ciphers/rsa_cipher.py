import os
import sys

from . import rsa_key_generator as rkg

DEFAULT_BLOCK_SIZE = 128
BYTE_SIZE = 256

#Organiser: K. Umut Araz

def metni_bloklara_ayir(
    mesaj: str, blok_boyutu: int = DEFAULT_BLOCK_SIZE
) -> list[int]:
    mesaj_byteleri = mesaj.encode("ascii")

    blok_tamsayilari = []
    for blok_baslangici in range(0, len(mesaj_byteleri), blok_boyutu):
        blok_tamsayisi = 0
        for i in range(blok_baslangici, min(blok_baslangici + blok_boyutu, len(mesaj_byteleri))):
            blok_tamsayisi += mesaj_byteleri[i] * (BYTE_SIZE ** (i % blok_boyutu))
        blok_tamsayilari.append(blok_tamsayisi)
    return blok_tamsayilari


def bloklardan_metni_al(
    blok_tamsayilari: list[int], mesaj_uzunlugu: int, blok_boyutu: int = DEFAULT_BLOCK_SIZE
) -> str:
    mesaj: list[str] = []
    for blok_tamsayisi in blok_tamsayilari:
        blok_mesaji: list[str] = []
        for i in range(blok_boyutu - 1, -1, -1):
            if len(mesaj) + i < mesaj_uzunlugu:
                ascii_numarasi = blok_tamsayisi // (BYTE_SIZE**i)
                blok_tamsayisi = blok_tamsayisi % (BYTE_SIZE**i)
                blok_mesaji.insert(0, chr(ascii_numarasi))
        mesaj.extend(blok_mesaji)
    return "".join(mesaj)


def mesajı_şifrele(
    mesaj: str, anahtar: tuple[int, int], blok_boyutu: int = DEFAULT_BLOCK_SIZE
) -> list[int]:
    şifreli_bloklar = []
    n, e = anahtar

    for blok in metni_bloklara_ayir(mesaj, blok_boyutu):
        şifreli_bloklar.append(pow(blok, e, n))
    return şifreli_bloklar


def mesajı_şifrele_çöz(
    şifreli_bloklar: list[int],
    mesaj_uzunluğu: int,
    anahtar: tuple[int, int],
    blok_boyutu: int = DEFAULT_BLOCK_SIZE,
) -> str:
    çözülmüş_bloklar = []
    n, d = anahtar
    for blok in şifreli_bloklar:
        çözülmüş_bloklar.append(pow(blok, d, n))
    return bloklardan_metni_al(çözülmüş_bloklar, mesaj_uzunluğu, blok_boyutu)


def anahtar_dosyasını_oku(anahtar_dosya_adı: str) -> tuple[int, int, int]:
    with open(anahtar_dosya_adı) as fo:
        içerik = fo.read()
    anahtar_boyutu, n, e_veya_d = içerik.split(",")
    return (int(anahtar_boyutu), int(n), int(e_veya_d))


def mesajı_şifrele_ve_dosyaya_yaz(
    mesaj_dosya_adı: str,
    anahtar_dosya_adı: str,
    mesaj: str,
    blok_boyutu: int = DEFAULT_BLOCK_SIZE,
) -> str:
    anahtar_boyutu, n, e = anahtar_dosyasını_oku(anahtar_dosya_adı)
    if anahtar_boyutu < blok_boyutu * 8:
        sys.exit(
            f"HATA: Blok boyutu {blok_boyutu * 8} bit ve anahtar boyutu {anahtar_boyutu} "
            "bit. RSA şifrelemesi, blok boyutunun anahtar boyutuna eşit veya daha büyük olmasını gerektirir. "
            "Ya blok boyutunu azaltın ya da farklı anahtarlar kullanın."
        )

    şifreli_bloklar = [str(i) for i in mesajı_şifrele(mesaj, (n, e), blok_boyutu)]

    şifreli_içerik = ",".join(şifreli_bloklar)
    şifreli_içerik = f"{len(mesaj)}_{blok_boyutu}_{şifreli_içerik}"
    with open(mesaj_dosya_adı, "w") as fo:
        fo.write(şifreli_içerik)
    return şifreli_içerik


def dosyadan_oku_ve_şifreyi_çöz(mesaj_dosya_adı: str, anahtar_dosya_adı: str) -> str:
    anahtar_boyutu, n, d = anahtar_dosyasını_oku(anahtar_dosya_adı)
    with open(mesaj_dosya_adı) as fo:
        içerik = fo.read()
    mesaj_uzunluğu_str, blok_boyutu_str, şifreli_masaj = içerik.split("_")
    mesaj_uzunluğu = int(mesaj_uzunluğu_str)
    blok_boyutu = int(blok_boyutu_str)

    if anahtar_boyutu < blok_boyutu * 8:
        sys.exit(
            f"HATA: Blok boyutu {blok_boyutu * 8} bit ve anahtar boyutu {anahtar_boyutu} "
            "bit. RSA şifrelemesi, blok boyutunun anahtar boyutuna eşit veya daha büyük olmasını gerektirir. "
            "Doğru anahtar dosyası ve şifreli dosya belirtildi mi?"
        )

    şifreli_bloklar = [int(blok) for blok in şifreli_masaj.split(",")]
    return mesajı_şifrele_çöz(şifreli_bloklar, mesaj_uzunluğu, (n, d), blok_boyutu)

def ana_fonksiyon() -> None:
    dosya_adı = "şifreli_dosya.txt"
    yanıt = input(r"Şifrele\Çöz [e\d]: ")

    if yanıt.lower().startswith("e"):
        mod = "şifrele"
    elif yanıt.lower().startswith("d"):
        mod = "çöz"

    if mod == "şifrele":
        if not os.path.exists("rsa_pubkey.txt"):
            rkg.make_key_files("rsa", 1024)

        mesaj = input("\nMesajı girin: ")
        pubkey_dosya_adı = "rsa_pubkey.txt"
        print(f"{dosya_adı} dosyasına şifreleme ve yazma işlemi yapılıyor...")
        şifreli_metin = mesajı_şifrele_ve_dosyaya_yaz(dosya_adı, pubkey_dosya_adı, mesaj)

        print("\nŞifreli metin:")
        print(şifreli_metin)

    elif mod == "çöz":
        privkey_dosya_adı = "rsa_privkey.txt"
        print(f"{dosya_adı} dosyasından okuma ve şifre çözme işlemi yapılıyor...")
        çözülmüş_metin = dosyadan_oku_ve_şifreyi_çöz(dosya_adı, privkey_dosya_adı)
        print("Şifre çözümlemesini rsa_decryption.txt dosyasına yazma işlemi yapılıyor...")
        with open("rsa_decryption.txt", "w") as dec:
            dec.write(çözülmüş_metin)

        print("\nŞifre çözümü:")
        print(çözülmüş_metin)


if __name__ == "__main__":
    ana_fonksiyon()
