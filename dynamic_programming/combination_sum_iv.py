"""
Soru:
Size farklı tamsayılardan oluşan bir dizi veriliyor ve bu diziden elemanları
seçmenin kaç farklı yolu olduğunu söylemeniz gerekiyor, öyle ki seçilen
elemanların toplamı hedef sayı tar'a eşit olmalıdır.

Örnek

Girdi:
N = 3
hedef = 5
dizi = [1, 2, 5]

Çıktı:
9

Yaklaşım:
Temel fikir, seçilen elemanların toplamının “tar” olacak şekilde yolu
bulmak için özyinelemeli olarak gitmektir. Her eleman için iki seçeneğimiz var:
    1. Elemanı seçilen elemanlar kümesine dahil et.
    2. Elemanı seçilen elemanlar kümesine dahil etme.
"""


def kombinasyon_toplam_iv(dizi: list[int], hedef: int) -> int:
    """
    Fonksiyon tüm olası kombinasyonları kontrol eder ve üstel Zaman
    Karmaşıklığında olası kombinasyonların sayısını döndürür.

    >>> kombinasyon_toplam_iv([1,2,5], 5)
    9
    """

    def olasi_kombinasyonlarin_sayisi(hedef: int) -> int:
        if hedef < 0:
            return 0
        if hedef == 0:
            return 1
        return sum(olasi_kombinasyonlarin_sayisi(hedef - eleman) for eleman in dizi)

    return olasi_kombinasyonlarin_sayisi(hedef)


def kombinasyon_toplam_iv_dp_dizi(dizi: list[int], hedef: int) -> int:
    """
    Fonksiyon tüm olası kombinasyonları kontrol eder ve O(N^2) Zaman
    Karmaşıklığında olası kombinasyonların sayısını döndürür, çünkü burada
    Dinamik programlama dizisi kullanıyoruz.

    >>> kombinasyon_toplam_iv_dp_dizi([1,2,5], 5)
    9
    """

    def dp_dizi_ile_olasi_kombinasyonlarin_sayisi(
        hedef: int, dp_dizi: list[int]
    ) -> int:
        if hedef < 0:
            return 0
        if hedef == 0:
            return 1
        if dp_dizi[hedef] != -1:
            return dp_dizi[hedef]
        cevap = sum(
            dp_dizi_ile_olasi_kombinasyonlarin_sayisi(hedef - eleman, dp_dizi)
            for eleman in dizi
        )
        dp_dizi[hedef] = cevap
        return cevap

    dp_dizi = [-1] * (hedef + 1)
    return dp_dizi_ile_olasi_kombinasyonlarin_sayisi(hedef, dp_dizi)


def kombinasyon_toplam_iv_bottom_up(n: int, dizi: list[int], hedef: int) -> int:
    """
    Fonksiyon alt-üst yaklaşımı kullanarak tüm olası kombinasyonları kontrol eder
    ve Dinamik programlama dizisi kullandığımız için O(N^2) Zaman Karmaşıklığında
    olası kombinasyonların sayısını döndürür.

    >>> kombinasyon_toplam_iv_bottom_up(3, [1,2,5], 5)
    9
    """

    dp_dizi = [0] * (hedef + 1)
    dp_dizi[0] = 1

    for i in range(1, hedef + 1):
        for j in range(n):
            if i - dizi[j] >= 0:
                dp_dizi[i] += dp_dizi[i - dizi[j]]

    return dp_dizi[hedef]


if __name__ == "__main__":
    import doctest

    doctest.testmod()
    hedef = 5
    dizi = [1, 2, 5]
    print(kombinasyon_toplam_iv(dizi, hedef))
