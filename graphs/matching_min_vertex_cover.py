"""
* Yazar: Manuel Di Lullo (https://github.com/manueldilullo)
* Açıklama: Minimum köşe örtüsü problemi için yaklaşık algoritma.
            Eşleme Yaklaşımı. Komşuluk listesi ile temsil edilen grafikleri kullanır.

URL: https://mathworld.wolfram.com/MinimumVertexCover.html
URL: https://www.princeton.edu/~aaa/Public/Teaching/ORF523/ORF523_Lec6.pdf
"""

#Produced By K. Umut Araz

def eşleme_min_köşe_örtüsü(grafik: dict) -> set:
    """
    Eşleme Yaklaşımı kullanarak minimum köşe örtüsü için yaklaşık algoritma
    @girdi: grafik (her düğümün bir tamsayı olarak temsil edildiği komşuluk listesinde saklanan grafik)
    @örnek:
    >>> grafik = {0: [1, 3], 1: [0, 3], 2: [0, 3, 4], 3: [0, 1, 2], 4: [2, 3]}
    >>> eşleme_min_köşe_örtüsü(grafik)
    {0, 1, 2, 4}
    """
    # seçilen_düğümler = seçilen düğümlerin kümesi
    seçilen_düğümler = set()
    # kenarlar = grafiğin kenarlarının listesi
    kenarlar = kenarları_al(grafik)

    # Kenarlar listesinde hala elemanlar olduğu sürece, rastgele bir kenar al
    # (başlangıç_düğümü, bitiş_düğümü) ve uç noktalarını seçilen_düğümler kümesine ekle
    # ve ardından başlangıç_düğümü ve bitiş_düğümüne bitişik tüm yayları kaldır
    while kenarlar:
        başlangıç_düğümü, bitiş_düğümü = kenarlar.pop()
        seçilen_düğümler.add(başlangıç_düğümü)
        seçilen_düğümler.add(bitiş_düğümü)
        for kenar in kenarlar.copy():
            if başlangıç_düğümü in kenar or bitiş_düğümü in kenar:
                kenarlar.discard(kenar)
    return seçilen_düğümler


def kenarları_al(grafik: dict) -> set:
    """
    Tüm kenarları temsil eden çiftleri içeren bir küme döndürür.
    @girdi: grafik (her düğümün bir tamsayı olarak temsil edildiği komşuluk listesinde saklanan grafik)
    @örnek:
    >>> grafik = {0: [1, 3], 1: [0, 3], 2: [0, 3], 3: [0, 1, 2]}
    >>> kenarları_al(grafik)
    {(0, 1), (3, 1), (0, 3), (2, 0), (3, 0), (2, 3), (1, 0), (3, 2), (1, 3)}
    """
    kenarlar = set()
    for başlangıç_düğümü, bitiş_düğümleri in grafik.items():
        for bitiş_düğümü in bitiş_düğümleri:
            kenarlar.add((başlangıç_düğümü, bitiş_düğümü))
    return kenarlar


if __name__ == "__main__":
    import doctest

    doctest.testmod()

    # grafik = {0: [1, 3], 1: [0, 3], 2: [0, 3, 4], 3: [0, 1, 2], 4: [2, 3]}
    # print(f"Eşleme köşe örtüsü:\n{eşleme_min_köşe_örtüsü(grafik)}")
