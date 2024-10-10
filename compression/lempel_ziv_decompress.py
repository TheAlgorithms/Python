"""
Lempel-Ziv-Welch dekompresyon algoritmasının birkaç uygulamasından biri
https://tr.wikipedia.org/wiki/Lempel%E2%80%93Ziv%E2%80%93Welch

# Organiser: K. Umut Araz
"""

import math
import sys


def dosyayi_ikili_oku(dosya_yolu: str) -> str:
    """
    Verilen dosyayı bayt olarak okur ve uzun bir dize olarak döner
    """
    sonuc = ""
    try:
        with open(dosya_yolu, "rb") as ikili_dosya:
            veri = ikili_dosya.read()
        for dat in veri:
            mevcut_bayt = f"{dat:08b}"
            sonuc += mevcut_bayt
        return sonuc
    except OSError:
        print("Dosyaya erişilemiyor")
        sys.exit()


def verileri_dekompres(data_bits: str) -> str:
    """
    Verilen data_bits'i Lempel-Ziv-Welch sıkıştırma algoritması kullanarak dekompres eder
    ve sonucu bir dize olarak döner
    """
    sözlük = {"0": "0", "1": "1"}
    sonuc, mevcut_dize = "", ""
    indeks = len(sözlük)

    for i in range(len(data_bits)):
        mevcut_dize += data_bits[i]
        if mevcut_dize not in sözlük:
            continue

        son_eşleşme_id = sözlük[mevcut_dize]
        sonuc += son_eşleşme_id
        sözlük[mevcut_dize] = son_eşleşme_id + "0"

        if math.log2(indeks).is_integer():
            yeni_sözlük = {}
            for mevcut_anahtar in list(sözlük):
                yeni_sözlük["0" + mevcut_anahtar] = sözlük.pop(mevcut_anahtar)
            sözlük = yeni_sözlük

        sözlük[bin(indeks)[2:]] = son_eşleşme_id + "1"
        indeks += 1
        mevcut_dize = ""
    return sonuc


def dosyaya_ikili_yaz(dosya_yolu: str, yazilacak: str) -> None:
    """
    Verilen yazilacak dizesini (sadece 0'lar ve 1'lerden oluşmalıdır) bayt olarak dosyaya yazar
    """
    bayt_uzunlugu = 8
    try:
        with open(dosya_yolu, "wb") as acik_dosya:
            sonuc_bayt_dizisi = [
                yazilacak[i : i + bayt_uzunlugu]
                for i in range(0, len(yazilacak), bayt_uzunlugu)
            ]

            if len(sonuc_bayt_dizisi[-1]) % bayt_uzunlugu == 0:
                sonuc_bayt_dizisi.append("10000000")
            else:
                sonuc_bayt_dizisi[-1] += "1" + "0" * (
                    bayt_uzunlugu - len(sonuc_bayt_dizisi[-1]) - 1
                )

            for eleman in sonuc_bayt_dizisi[:-1]:
                acik_dosya.write(int(eleman, 2).to_bytes(1, byteorder="big"))
    except OSError:
        print("Dosyaya erişilemiyor")
        sys.exit()


def on_ek_kaldir(data_bits: str) -> str:
    """
    Sıkıştırılmış dosyanın sahip olması gereken boyut ön ekini kaldırır
    Sonucu döner
    """
    sayac = 0
    for harf in data_bits:
        if harf == "1":
            break
        sayac += 1

    data_bits = data_bits[sayac:]
    data_bits = data_bits[sayac + 1 :]
    return data_bits


def sikistir(dosya_yolu: str, hedef_dosya_yolu: str) -> None:
    """
    Kaynak dosyayı okur, dekompres eder ve sonucu hedef dosyaya yazar
    """
    data_bits = dosyayi_ikili_oku(dosya_yolu)
    data_bits = on_ek_kaldir(data_bits)
    dekompreslenmis = verileri_dekompres(data_bits)
    dosyaya_ikili_yaz(hedef_dosya_yolu, dekompreslenmis)


if __name__ == "__main__":
    sikistir(sys.argv[1], sys.argv[2])
