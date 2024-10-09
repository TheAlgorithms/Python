"""
Test durumları:
Kendi madeni paralarınızı girmek ister misiniz? (E/H) :H
Yapmak istediğiniz değişikliği Hint Para Biriminde girin: 987
987 için minimum değişiklikler:
500 100 100 100 100 50 20 10 5 2

Kendi madeni paralarınızı girmek ister misiniz? (E/H) :E
Madeni para sayısını girin:10
1
5
10
20
50
100
200
500
1000
2000
Yapmak istediğiniz değişikliği girin: 18745
18745 için minimum değişiklikler:
2000 2000 2000 2000 2000 2000 2000 2000 2000 500 200 20 20 5

Kendi madeni paralarınızı girmek ister misiniz? (E/H) :H
Yapmak istediğiniz değişikliği girin: 0
Toplam değer sıfır veya negatif olamaz.
Kendi madeni paralarınızı girmek ister misiniz? (E/H) :H
Yapmak istediğiniz değişikliği girin: -98
Toplam değer sıfır veya negatif olamaz.

Kendi madeni paralarınızı girmek ister misiniz? (E/H) :E
Madeni para sayısını girin:5
1
5
100
500
1000
Yapmak istediğiniz değişikliği girin: 456
456 için minimum değişiklikler:
100 100 100 100 5 5 5 5 5 5 5 5 5 5 5 1
"""


def minimum_degisiklik_bul(madeni_paralar: list[int], deger: str) -> list[int]:
    """
    Verilen madeni paralar ve değer ile minimum değişikliği bul
    >>> minimum_degisiklik_bul([1, 5, 10, 20, 50, 100, 200, 500, 1000,2000], 18745)
    [2000, 2000, 2000, 2000, 2000, 2000, 2000, 2000, 2000, 500, 200, 20, 20, 5]
    >>> minimum_degisiklik_bul([1, 2, 5, 10, 20, 50, 100, 500, 2000], 987)
    [500, 100, 100, 100, 100, 50, 20, 10, 5, 2]
    >>> minimum_degisiklik_bul([1, 2, 5, 10, 20, 50, 100, 500, 2000], 0)
    []
    >>> minimum_degisiklik_bul([1, 2, 5, 10, 20, 50, 100, 500, 2000], -98)
    []
    >>> minimum_degisiklik_bul([1, 5, 100, 500, 1000], 456)
    [100, 100, 100, 100, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 1]
    """
    toplam_deger = int(deger)

    # Sonucu başlat
    cevap = []

    # Tüm madeni paraları dolaş
    for madeni_para in reversed(madeni_paralar):
        # Madeni paraları bul
        while int(toplam_deger) >= int(madeni_para):
            toplam_deger -= int(madeni_para)
            cevap.append(madeni_para)  # "cevap" dizisine ekle

    return cevap


# Ana Kod
if __name__ == "__main__":
    madeni_paralar = []
    deger = "0"

    if (
        input("Kendi madeni paralarınızı girmek ister misiniz? (eE/hH): ").strip().lower()
        == "e"
    ):
        n = int(input("Eklemek istediğiniz madeni para sayısını girin: ").strip())

        for i in range(n):
            madeni_paralar.append(int(input(f"Madeni Para {i}: ").strip()))
        deger = input("Yapmak istediğiniz değişikliği Hint Para Biriminde girin: ").strip()
    else:
        # Kullanıcı girmediğinde tüm Hint Para Birimi madeni paraları
        madeni_paralar = [1, 2, 5, 10, 20, 50, 100, 500, 2000]
        deger = input("Yapmak istediğiniz değişikliği girin: ").strip()

    if int(deger) == 0 or int(deger) < 0:
        print("Toplam değer sıfır veya negatif olamaz.")

    else:
        print(f"{deger} için minimum değişiklikler: ")
        cevap = minimum_degisiklik_bul(madeni_paralar, deger)
        # Sonucu yazdır
        for i in range(len(cevap)):
            print(cevap[i], end=" ")
