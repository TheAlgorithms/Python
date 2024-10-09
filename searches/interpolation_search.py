"""
Bu, interpolasyon arama algoritmasının saf Python uygulamasıdır.

Organiser: K. Umut Araz
"""


def interpolasyon_arama(sıralı_koleksiyon: list[int], öğe: int) -> int | None:
    """
    Sıralı bir koleksiyonda interpolasyon arama algoritması ile bir öğeyi arar.

    Args:
        sıralı_koleksiyon: sıralı tam sayılardan oluşan liste
        öğe: aranacak öğe değeri

    Returns:
        int: Bulunan öğenin indeksi, öğe bulunamazsa None.
    Örnekler:
    >>> interpolasyon_arama([1, 2, 3, 4, 5], 2)
    1
    >>> interpolasyon_arama([1, 2, 3, 4, 5], 4)
    3
    >>> interpolasyon_arama([1, 2, 3, 4, 5], 6) is None
    True
    >>> interpolasyon_arama([], 1) is None
    True
    >>> interpolasyon_arama([100], 100)
    0
    >>> interpolasyon_arama([1, 2, 3, 4, 5], 0) is None
    True
    >>> interpolasyon_arama([1, 2, 3, 4, 5], 7) is None
    True
    >>> interpolasyon_arama([1, 2, 3, 4, 5], 2)
    1
    >>> interpolasyon_arama([1, 2, 3, 4, 5], 0) is None
    True
    >>> interpolasyon_arama([1, 2, 3, 4, 5], 7) is None
    True
    >>> interpolasyon_arama([1, 2, 3, 4, 5], 2)
    1
    >>> interpolasyon_arama([5, 5, 5, 5, 5], 3) is None
    True
    """
    sol = 0
    sağ = len(sıralı_koleksiyon) - 1

    while sol <= sağ:
        # interpolasyon sırasında sıfıra bölmeyi önle
        if sıralı_koleksiyon[sol] == sıralı_koleksiyon[sağ]:
            if sıralı_koleksiyon[sol] == öğe:
                return sol
            return None

        nokta = sol + ((öğe - sıralı_koleksiyon[sol]) * (sağ - sol)) // (
            sıralı_koleksiyon[sağ] - sıralı_koleksiyon[sol]
        )

        # aralık dışı kontrolü
        if nokta < 0 or nokta >= len(sıralı_koleksiyon):
            return None

        mevcut_öğe = sıralı_koleksiyon[nokta]
        if mevcut_öğe == öğe:
            return nokta
        if nokta < sol:
            sağ = sol
            sol = nokta
        elif nokta > sağ:
            sol = sağ
            sağ = nokta
        elif öğe < mevcut_öğe:
            sağ = nokta - 1
        else:
            sol = nokta + 1
    return None


def rekursif_interpolasyon_arama(
    sıralı_koleksiyon: list[int], öğe: int, sol: int = 0, sağ: int | None = None
) -> int | None:
    """Python'da rekursyon ile interpolasyon arama algoritmasının saf uygulaması.
    Koleksiyonun artan sıralı olması gerektiğine dikkat edin, aksi takdirde sonuç
    öngörülemez olacaktır.
    İlk rekursiyon sol=0 ve sağ=(len(sıralı_koleksiyon)-1) ile başlatılmalıdır.

    Args:
        sıralı_koleksiyon: karşılaştırılabilir öğeler içeren sıralı bir koleksiyon
        öğe: aranacak öğe değeri
        sol: koleksiyondaki sol indeks
        sağ: koleksiyondaki sağ indeks

    Returns:
        koleksiyondaki öğenin indeksi veya öğe mevcut değilse None

    Örnekler:
    >>> rekursif_interpolasyon_arama([0, 5, 7, 10, 15], 0)
    0
    >>> rekursif_interpolasyon_arama([0, 5, 7, 10, 15], 15)
    4
    >>> rekursif_interpolasyon_arama([0, 5, 7, 10, 15], 5)
    1
    >>> rekursif_interpolasyon_arama([0, 5, 7, 10, 15], 100) is None
    True
    >>> rekursif_interpolasyon_arama([5, 5, 5, 5, 5], 3) is None
    True
    """
    if sağ is None:
        sağ = len(sıralı_koleksiyon) - 1
    # interpolasyon sırasında sıfıra bölmeyi önle
    if sıralı_koleksiyon[sol] == sıralı_koleksiyon[sağ]:
        if sıralı_koleksiyon[sol] == öğe:
            return sol
        return None

    nokta = sol + ((öğe - sıralı_koleksiyon[sol]) * (sağ - sol)) // (
        sıralı_koleksiyon[sağ] - sıralı_koleksiyon[sol]
    )

    # aralık dışı kontrolü
    if nokta < 0 or nokta >= len(sıralı_koleksiyon):
        return None

    if sıralı_koleksiyon[nokta] == öğe:
        return nokta
    if nokta < sol:
        return rekursif_interpolasyon_arama(sıralı_koleksiyon, öğe, nokta, sol)
    if nokta > sağ:
        return rekursif_interpolasyon_arama(sıralı_koleksiyon, öğe, sağ, sol)
    if sıralı_koleksiyon[nokta] > öğe:
        return rekursif_interpolasyon_arama(
            sıralı_koleksiyon, öğe, sol, nokta - 1
        )
    return rekursif_interpolasyon_arama(sıralı_koleksiyon, öğe, nokta + 1, sağ)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
