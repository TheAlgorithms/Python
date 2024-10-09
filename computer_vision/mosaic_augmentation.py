"""Kaynak: https://github.com/jason9075/opencv-mosaic-data-aug"""

import glob
import os
import random
from string import ascii_lowercase, digits

import cv2
import numpy as np

# Parametreler
CIKTI_BOYUTU = (720, 1280)  # Yükseklik, Genişlik
OLCEK_ARALIGI = (0.4, 0.6)  # Eğer yükseklik veya genişlik bu ölçekten düşükse, bırak.
FILTRE_KUCUK_OLCEK = 1 / 100
ETIKET_DIZINI = ""
GORUNTU_DIZINI = ""
CIKTI_DIZINI = ""
GORUNTU_SAYISI = 250


def ana() -> None:
    """
    Görüntü listesi ve açıklama listesini giriş dizininden alın.
    Yeni görüntüleri ve açıklamaları güncelleyin.
    Görüntüleri ve açıklamaları çıkış dizininde kaydedin.
    """
    goruntu_yollari, aciklamalar = veri_setini_al(ETIKET_DIZINI, GORUNTU_DIZINI)
    for indeks in range(GORUNTU_SAYISI):
        indeksler = random.sample(range(len(aciklamalar)), 4)
        yeni_goruntu, yeni_aciklamalar, yol = goruntu_ve_aciklamayi_guncelle(
            goruntu_yollari,
            aciklamalar,
            indeksler,
            CIKTI_BOYUTU,
            OLCEK_ARALIGI,
            filtre_olcegi=FILTRE_KUCUK_OLCEK,
        )

        # Rastgele karakter kodu al: '7b7ad245cdff75241935e4dd860f3bad'
        karakter_kodu = rastgele_karakterler(32)
        dosya_adi = yol.split(os.sep)[-1].rsplit(".", 1)[0]
        dosya_kok = f"{CIKTI_DIZINI}/{dosya_adi}_MOZAİK_{karakter_kodu}"
        cv2.imwrite(f"{dosya_kok}.jpg", yeni_goruntu, [cv2.IMWRITE_JPEG_QUALITY, 85])
        print(f"Başarılı {indeks+1}/{GORUNTU_SAYISI} ile {dosya_adi}")
        aciklama_listesi = []
        for aciklama in yeni_aciklamalar:
            genislik = aciklama[3] - aciklama[1]
            yukseklik = aciklama[4] - aciklama[2]
            x_merkezi = aciklama[1] + genislik / 2
            y_merkezi = aciklama[2] + yukseklik / 2
            nesne = f"{aciklama[0]} {x_merkezi} {y_merkezi} {genislik} {yukseklik}"
            aciklama_listesi.append(nesne)
        with open(f"{dosya_kok}.txt", "w") as cikti_dosyasi:
            cikti_dosyasi.write("\n".join(satir for satir in aciklama_listesi))


def veri_setini_al(etiket_dizini: str, goruntu_dizini: str) -> tuple[list, list]:
    """
    - etiket_dizini <type: str>: Görüntülerin açıklamalarını içeren etiketlerin yolu
    - goruntu_dizini <type: str>: Görüntüleri içeren klasörün yolu
    Dönüş <type: list>: Görüntü yolları ve etiketlerin listesi
    """
    goruntu_yollari = []
    etiketler = []
    for etiket_dosyasi in glob.glob(os.path.join(etiket_dizini, "*.txt")):
        etiket_adi = etiket_dosyasi.split(os.sep)[-1].rsplit(".", 1)[0]
        with open(etiket_dosyasi) as giris_dosyasi:
            nesne_listeleri = giris_dosyasi.readlines()
        goruntu_yolu = os.path.join(goruntu_dizini, f"{etiket_adi}.jpg")

        kutular = []
        for nesne_listesi in nesne_listeleri:
            nesne = nesne_listesi.rstrip("\n").split(" ")
            xmin = float(nesne[1]) - float(nesne[3]) / 2
            ymin = float(nesne[2]) - float(nesne[4]) / 2
            xmax = float(nesne[1]) + float(nesne[3]) / 2
            ymax = float(nesne[2]) + float(nesne[4]) / 2

            kutular.append([int(nesne[0]), xmin, ymin, xmax, ymax])
        if not kutular:
            continue
        goruntu_yollari.append(goruntu_yolu)
        etiketler.append(kutular)
    return goruntu_yollari, etiketler


def goruntu_ve_aciklamayi_guncelle(
    tum_goruntu_listesi: list,
    tum_aciklamalar: list,
    indeksler: list[int],
    cikti_boyutu: tuple[int, int],
    olcek_araligi: tuple[float, float],
    filtre_olcegi: float = 0.0,
) -> tuple[list, list, str]:
    """
    - tum_goruntu_listesi <type: list>: tüm görüntülerin listesi
    - tum_aciklamalar <type: list>: belirli bir görüntünün tüm açıklamalarının listesi
    - indeksler <type: list>: listedeki görüntünün indeksi
    - cikti_boyutu <type: tuple>: çıktı görüntüsünün boyutu (Yükseklik, Genişlik)
    - olcek_araligi <type: tuple>: görüntü ölçek aralığı
    - filtre_olcegi <type: float>: görüntü ve sınırlayıcı kutuyu küçültme koşulu
    Dönüş:
        - cikti_goruntu <type: narray>: yeniden boyutlandırıldıktan sonra görüntü
        - yeni_aciklama <type: list>: ölçeklendirmeden sonra yeni açıklamaların listesi
        - yol[0] <type: string>: görüntü dosyasının adını al
    """
    cikti_goruntu = np.zeros([cikti_boyutu[0], cikti_boyutu[1], 3], dtype=np.uint8)
    olcek_x = olcek_araligi[0] + random.random() * (olcek_araligi[1] - olcek_araligi[0])
    olcek_y = olcek_araligi[0] + random.random() * (olcek_araligi[1] - olcek_araligi[0])
    bolme_noktasi_x = int(olcek_x * cikti_boyutu[1])
    bolme_noktasi_y = int(olcek_y * cikti_boyutu[0])

    yeni_aciklama = []
    yol_listesi = []
    for i, indeks in enumerate(indeksler):
        yol = tum_goruntu_listesi[indeks]
        yol_listesi.append(yol)
        goruntu_aciklamalari = tum_aciklamalar[indeks]
        goruntu = cv2.imread(yol)
        if i == 0:  # sol üst
            goruntu = cv2.resize(goruntu, (bolme_noktasi_x, bolme_noktasi_y))
            cikti_goruntu[:bolme_noktasi_y, :bolme_noktasi_x, :] = goruntu
            for kutu in goruntu_aciklamalari:
                xmin = kutu[1] * olcek_x
                ymin = kutu[2] * olcek_y
                xmax = kutu[3] * olcek_x
                ymax = kutu[4] * olcek_y
                yeni_aciklama.append([kutu[0], xmin, ymin, xmax, ymax])
        elif i == 1:  # sağ üst
            goruntu = cv2.resize(goruntu, (cikti_boyutu[1] - bolme_noktasi_x, bolme_noktasi_y))
            cikti_goruntu[:bolme_noktasi_y, bolme_noktasi_x : cikti_boyutu[1], :] = goruntu
            for kutu in goruntu_aciklamalari:
                xmin = olcek_x + kutu[1] * (1 - olcek_x)
                ymin = kutu[2] * olcek_y
                xmax = olcek_x + kutu[3] * (1 - olcek_x)
                ymax = kutu[4] * olcek_y
                yeni_aciklama.append([kutu[0], xmin, ymin, xmax, ymax])
        elif i == 2:  # sol alt
            goruntu = cv2.resize(goruntu, (bolme_noktasi_x, cikti_boyutu[0] - bolme_noktasi_y))
            cikti_goruntu[bolme_noktasi_y : cikti_boyutu[0], :bolme_noktasi_x, :] = goruntu
            for kutu in goruntu_aciklamalari:
                xmin = kutu[1] * olcek_x
                ymin = olcek_y + kutu[2] * (1 - olcek_y)
                xmax = kutu[3] * olcek_x
                ymax = olcek_y + kutu[4] * (1 - olcek_y)
                yeni_aciklama.append([kutu[0], xmin, ymin, xmax, ymax])
        else:  # sağ alt
            goruntu = cv2.resize(
                goruntu, (cikti_boyutu[1] - bolme_noktasi_x, cikti_boyutu[0] - bolme_noktasi_y)
            )
            cikti_goruntu[
                bolme_noktasi_y : cikti_boyutu[0], bolme_noktasi_x : cikti_boyutu[1], :
            ] = goruntu
            for kutu in goruntu_aciklamalari:
                xmin = olcek_x + kutu[1] * (1 - olcek_x)
                ymin = olcek_y + kutu[2] * (1 - olcek_y)
                xmax = olcek_x + kutu[3] * (1 - olcek_x)
                ymax = olcek_y + kutu[4] * (1 - olcek_y)
                yeni_aciklama.append([kutu[0], xmin, ymin, xmax, ymax])

    # Filtre ölçeğinden küçük sınırlayıcı kutuyu kaldır
    if filtre_olcegi > 0:
        yeni_aciklama = [
            aciklama
            for aciklama in yeni_aciklama
            if filtre_olcegi < (aciklama[3] - aciklama[1]) and filtre_olcegi < (aciklama[4] - aciklama[2])
        ]

    return cikti_goruntu, yeni_aciklama, yol_listesi[0]


def rastgele_karakterler(karakter_sayisi: int) -> str:
    """
    Otomatik olarak rastgele 32 karakter oluşturun.
    Rastgele karakter kodu al: '7b7ad245cdff75241935e4dd860f3bad'
    >>> len(rastgele_karakterler(32))
    32
    """
    assert karakter_sayisi > 1, "Karakter sayısı 1'den büyük olmalıdır"
    karakter_kodu = ascii_lowercase + digits
    return "".join(random.choice(karakter_kodu) for _ in range(karakter_sayisi))


if __name__ == "__main__":
    ana()
    print("TAMAMLANDI ✅")
