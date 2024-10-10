"""
Lempel-Ziv-Welch sıkıştırma algoritmasının birkaç uygulamasından biri
https://en.wikipedia.org/wiki/Lempel%E2%80%93Ziv%E2%80%93Welch

Organiser: K. Umut Araz
"""

import math
import os
import sys


def dosyayı_ikili_okuma(dosya_yolu: str) -> str:
    """
    Verilen dosyayı bayt olarak okur ve uzun bir string olarak döner
    """
    sonuç = ""
    try:
        with open(dosya_yolu, "rb") as ikili_dosya:
            veri = ikili_dosya.read()
        for dat in veri:
            mevcut_bayt = f"{dat:08b}"
            sonuç += mevcut_bayt
        return sonuç
    except OSError:
        print("Dosyaya erişilemiyor")
        sys.exit()


def sözlüğe_anahtar_ekle(
    sözlük: dict[str, str], mevcut_string: str, indeks: int, son_eşleşme_id: str
) -> None:
    """
    Yeni stringler (mevcut_string + "0", mevcut_string + "1") sözlüğe ekler
    """
    sözlük.pop(mevcut_string)
    sözlük[mevcut_string + "0"] = son_eşleşme_id

    if math.log2(indeks).is_integer():
        for mevcut_anahtar in sözlük:
            sözlük[mevcut_anahtar] = "0" + sözlük[mevcut_anahtar]

    sözlük[mevcut_string + "1"] = bin(indeks)[2:]


def veriyi_sıkıştır(data_bits: str) -> str:
    """
    Verilen data_bits'i Lempel-Ziv-Welch sıkıştırma algoritması ile sıkıştırır
    ve sonucu bir string olarak döner
    """
    sözlük = {"0": "0", "1": "1"}
    sonuç, mevcut_string = "", ""
    indeks = len(sözlük)

    for i in range(len(data_bits)):
        mevcut_string += data_bits[i]
        if mevcut_string not in sözlük:
            continue

        son_eşleşme_id = sözlük[mevcut_string]
        sonuç += son_eşleşme_id
        sözlüğe_anahtar_ekle(sözlük, mevcut_string, indeks, son_eşleşme_id)
        indeks += 1
        mevcut_string = ""

    while mevcut_string != "" and mevcut_string not in sözlük:
        mevcut_string += "0"

    if mevcut_string != "":
        son_eşleşme_id = sözlük[mevcut_string]
        sonuç += son_eşleşme_id

    return sonuç


def dosya_uzunluğunu_ekle(kaynak_yolu: str, sıkıştırılmış: str) -> str:
    """
    Verilen dosyanın uzunluğunu (Elias gamma kodlaması kullanarak) sıkıştırılmış
    stringin önüne ekler
    """
    dosya_uzunluğu = os.path.getsize(kaynak_yolu)
    dosya_uzunluğu_ikili = bin(dosya_uzunluğu)[2:]
    uzunluk_uzunluğu = len(dosya_uzunluğu_ikili)

    return "0" * (uzunluk_uzunluğu - 1) + dosya_uzunluğu_ikili + sıkıştırılmış


def dosyayı_ikili_yazma(dosya_yolu: str, yazılacak: str) -> None:
    """
    Verilen yazılacak stringi (sadece 0'lar ve 1'lerden oluşmalıdır) dosyaya bayt
    olarak yazar
    """
    bayt_uzunluğu = 8
    try:
        with open(dosya_yolu, "wb") as açılan_dosya:
            sonuç_bayt_dizisi = [
                yazılacak[i : i + bayt_uzunluğu]
                for i in range(0, len(yazılacak), bayt_uzunluğu)
            ]

            if len(sonuç_bayt_dizisi[-1]) % bayt_uzunluğu == 0:
                sonuç_bayt_dizisi.append("10000000")
            else:
                sonuç_bayt_dizisi[-1] += "1" + "0" * (
                    bayt_uzunluğu - len(sonuç_bayt_dizisi[-1]) - 1
                )

            for elem in sonuç_bayt_dizisi:
                açılan_dosya.write(int(elem, 2).to_bytes(1, byteorder="big"))
    except OSError:
        print("Dosyaya erişilemiyor")
        sys.exit()


def sıkıştır(kaynak_yolu: str, hedef_yolu: str) -> None:
    """
    Kaynak dosyayı okur, sıkıştırır ve sıkıştırılmış sonucu hedef dosyaya yazar
    """
    veri_bitleri = dosyayı_ikili_okuma(kaynak_yolu)
    sıkıştırılmış = veriyi_sıkıştır(veri_bitleri)
    sıkıştırılmış = dosya_uzunluğunu_ekle(kaynak_yolu, sıkıştırılmış)
    dosyayı_ikili_yazma(hedef_yolu, sıkıştırılmış)


if __name__ == "__main__":
    sıkıştır(sys.argv[1], sys.argv[2])
