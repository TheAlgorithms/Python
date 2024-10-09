"""
Her bir çubuğun genişliğinin 1 olduğu bir yükseklik haritasını temsil eden negatif olmayan
tamsayılar dizisi verildiğinde, bu program ne kadar yağmur suyunun tutulabileceğini hesaplar.

Örnek - yükseklik = (0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1)
Çıktı: 6
Bu problem "DİNAMİK PROGRAMLAMA" kavramı kullanılarak çözülebilir.

Dizideki her çubuğun solunda ve sağında bulunan çubukların maksimum yüksekliğini hesaplarız.
Sonra yapının genişliği boyunca iterasyon yaparız ve her indeksde,
tutulacak su miktarı, her iki taraftaki çubukların maksimum yüksekliğinin minimumu eksi
mevcut konumdaki çubuğun yüksekliğine eşittir.
"""


def tutulan_yagmur_suyu(yukseklikler: tuple[int, ...]) -> int:
    """
    Tutulan yağmur suyu fonksiyonu, çubuk yükseklikleri dizisi verildiğinde tutulabilecek
    toplam yağmur suyu miktarını hesaplar.
    Dinamik programlama yaklaşımını kullanarak, her çubuğun her iki tarafındaki çubukların
    maksimum yüksekliğini belirler ve ardından her çubuğun üzerindeki tutulan suyu hesaplar.
    Fonksiyon toplam tutulan suyu döndürür.

    >>> tutulan_yagmur_suyu((0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1))
    6
    >>> tutulan_yagmur_suyu((7, 1, 5, 3, 6, 4))
    9
    >>> tutulan_yagmur_suyu((7, 1, 5, 3, 6, -1))
    Traceback (most recent call last):
        ...
    ValueError: Hiçbir yükseklik negatif olamaz
    """
    if not yukseklikler:
        return 0
    if any(h < 0 for h in yukseklikler):
        raise ValueError("Hiçbir yükseklik negatif olamaz")
    uzunluk = len(yukseklikler)

    sol_max = [0] * uzunluk
    sol_max[0] = yukseklikler[0]
    for i, yukseklik in enumerate(yukseklikler[1:], start=1):
        sol_max[i] = max(yukseklik, sol_max[i - 1])

    sag_max = [0] * uzunluk
    sag_max[-1] = yukseklikler[-1]
    for i in range(uzunluk - 2, -1, -1):
        sag_max[i] = max(yukseklikler[i], sag_max[i + 1])

    return sum(
        min(sol, sag) - yukseklik
        for sol, sag, yukseklik in zip(sol_max, sag_max, yukseklikler)
    )


if __name__ == "__main__":
    import doctest

    doctest.testmod()
    print(f"{tutulan_yagmur_suyu((0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1)) = }")
    print(f"{tutulan_yagmur_suyu((7, 1, 5, 3, 6, 4)) = }")
