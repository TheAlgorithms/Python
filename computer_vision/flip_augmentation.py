import glob
import os
import random
from string import ascii_lowercase, digits

import cv2

"""
Görüntü ve sınırlayıcı kutuyu bilgisayarla görme görevi için çevir
https://paperswithcode.com/method/randomhorizontalflip
"""

# Parametreler
ETIKET_DIZINI = ""
GORUNTU_DIZINI = ""
CIKTI_DIZINI = ""
CEVIRME_TIPI = 1  # (0 dikey, 1 yatay)


def ana() -> None:
    """
    Girdi dizininden görüntü listesi ve açıklama listesi alın.
    Yeni görüntüleri ve açıklamaları güncelleyin.
    Görüntüleri ve açıklamaları çıktı dizininde kaydedin.
    """
    img_yollar, aciklamalar = veri_setini_al(ETIKET_DIZINI, GORUNTU_DIZINI)
    print("İşleniyor...")
    yeni_goruntuler, yeni_aciklamalar, yollar = goruntu_ve_aciklama_guncelle(img_yollar, aciklamalar, CEVIRME_TIPI)

    for index, goruntu in enumerate(yeni_goruntuler):
        # Rastgele karakter kodu al: '7b7ad245cdff75241935e4dd860f3bad'
        harf_kodu = rastgele_karakterler(32)
        dosya_adi = yollar[index].split(os.sep)[-1].rsplit(".", 1)[0]
        dosya_kok = f"{CIKTI_DIZINI}/{dosya_adi}_CEVIR_{harf_kodu}"
        cv2.imwrite(f"{dosya_kok}.jpg", goruntu, [cv2.IMWRITE_JPEG_QUALITY, 85])
        print(f"Başarılı {index+1}/{len(yeni_goruntuler)} ile {dosya_adi}")
        aciklamalar_listesi = []
        for aciklama in yeni_aciklamalar[index]:
            nesne = f"{aciklama[0]} {aciklama[1]} {aciklama[2]} {aciklama[3]} {aciklama[4]}"
            aciklamalar_listesi.append(nesne)
        with open(f"{dosya_kok}.txt", "w") as cikti_dosyasi:
            cikti_dosyasi.write("\n".join(satir for satir in aciklamalar_listesi))


def veri_setini_al(etiket_dizini: str, goruntu_dizini: str) -> tuple[list, list]:
    """
    - etiket_dizini <type: str>: Görüntülerin açıklamalarını içeren etiketlerin yolu
    - goruntu_dizini <type: str>: Görüntüleri içeren klasörün yolu
    Dönüş <type: list>: Görüntü yolları ve etiketlerin listesi
    """
    img_yollar = []
    etiketler = []
    for etiket_dosyasi in glob.glob(os.path.join(etiket_dizini, "*.txt")):
        etiket_adi = etiket_dosyasi.split(os.sep)[-1].rsplit(".", 1)[0]
        with open(etiket_dosyasi) as giris_dosyasi:
            nesne_listeleri = giris_dosyasi.readlines()
        img_yolu = os.path.join(goruntu_dizini, f"{etiket_adi}.jpg")

        kutular = []
        for nesne_listesi in nesne_listeleri:
            nesne = nesne_listesi.rstrip("\n").split(" ")
            kutular.append(
                [
                    int(nesne[0]),
                    float(nesne[1]),
                    float(nesne[2]),
                    float(nesne[3]),
                    float(nesne[4]),
                ]
            )
        if not kutular:
            continue
        img_yollar.append(img_yolu)
        etiketler.append(kutular)
    return img_yollar, etiketler


def goruntu_ve_aciklama_guncelle(
    img_listesi: list, aciklama_listesi: list, cevirme_tipi: int = 1
) -> tuple[list, list, list]:
    """
    - img_listesi <type: list>: tüm görüntülerin listesi
    - aciklama_listesi <type: list>: belirli bir görüntünün tüm açıklamalarının listesi
    - cevirme_tipi <type: int>: 0 dikey, 1 yatay
    Dönüş:
        - yeni_goruntu_listesi <type: narray>: yeniden boyutlandırıldıktan sonra görüntü
        - yeni_aciklama_listeleri <type: list>: yeniden ölçeklendirdikten sonra yeni açıklamaların listesi
        - yol_listesi <type: list>: görüntü dosyasının adının listesi
    """
    yeni_aciklama_listeleri = []
    yol_listesi = []
    yeni_goruntu_listesi = []
    for idx in range(len(img_listesi)):
        yeni_aciklamalar = []
        yol = img_listesi[idx]
        yol_listesi.append(yol)
        img_aciklamalar = aciklama_listesi[idx]
        img = cv2.imread(yol)
        if cevirme_tipi == 1:
            yeni_img = cv2.flip(img, cevirme_tipi)
            for bbox in img_aciklamalar:
                x_merkez_yeni = 1 - bbox[1]
                yeni_aciklamalar.append([bbox[0], x_merkez_yeni, bbox[2], bbox[3], bbox[4]])
        elif cevirme_tipi == 0:
            yeni_img = cv2.flip(img, cevirme_tipi)
            for bbox in img_aciklamalar:
                y_merkez_yeni = 1 - bbox[2]
                yeni_aciklamalar.append([bbox[0], bbox[1], y_merkez_yeni, bbox[3], bbox[4]])
        yeni_aciklama_listeleri.append(yeni_aciklamalar)
        yeni_goruntu_listesi.append(yeni_img)
    return yeni_goruntu_listesi, yeni_aciklama_listeleri, yol_listesi


def rastgele_karakterler(karakter_sayisi: int = 32) -> str:
    """
    Otomatik olarak rastgele 32 karakter oluşturun.
    Rastgele karakter kodu al: '7b7ad245cdff75241935e4dd860f3bad'
    >>> len(rastgele_karakterler(32))
    32
    """
    assert karakter_sayisi > 1, "Karakter sayısı 1'den büyük olmalıdır"
    harf_kodu = ascii_lowercase + digits
    return "".join(random.choice(harf_kodu) for _ in range(karakter_sayisi))


if __name__ == "__main__":
    ana()
    print("TAMAMLANDI ✅")
