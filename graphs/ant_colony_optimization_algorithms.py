"""
Karınca kolonisi optimizasyon algoritmasını kullanarak gezgin satıcı problemini (TSP) çözün
ve şu soruyu sorun:
"Bir şehir listesi ve her şehir çifti arasındaki mesafeler verildiğinde, her şehri tam olarak bir kez ziyaret eden ve başlangıç şehrine dönen en kısa rota nedir?"

https://en.wikipedia.org/wiki/Ant_colony_optimization_algorithms
https://en.wikipedia.org/wiki/Travelling_salesman_problem

Prouduced by: K. Umut Araz
"""

import copy
import random

şehirler = {
    0: [0, 0],
    1: [0, 5],
    2: [3, 8],
    3: [8, 10],
    4: [12, 8],
    5: [12, 4],
    6: [8, 0],
    7: [6, 2],
}


def ana(
    şehirler: dict[int, list[int]],
    karınca_sayısı: int,
    iterasyon_sayısı: int,
    feromon_buharlaşma: float,
    alfa: float,
    beta: float,
    q: float,  # Feromon sistemi parametreleri Q, sabit bir değerdir
) -> tuple[list[int], float]:
    """
    Karınca kolonisi algoritması ana fonksiyonu
    >>> ana(şehirler=şehirler, karınca_sayısı=10, iterasyon_sayısı=20,
    ...      feromon_buharlaşma=0.7, alfa=1.0, beta=5.0, q=10)
    ([0, 1, 2, 3, 4, 5, 6, 7, 0], 37.909778143828696)
    >>> ana(şehirler={0: [0, 0], 1: [2, 2]}, karınca_sayısı=5, iterasyon_sayısı=5,
    ...      feromon_buharlaşma=0.7, alfa=1.0, beta=5.0, q=10)
    ([0, 1, 0], 5.656854249492381)
    >>> ana(şehirler={0: [0, 0], 1: [2, 2], 4: [4, 4]}, karınca_sayısı=5, iterasyon_sayısı=5,
    ...      feromon_buharlaşma=0.7, alfa=1.0, beta=5.0, q=10)
    Traceback (most recent call last):
      ...
    IndexError: list index out of range
    >>> ana(şehirler={}, karınca_sayısı=5, iterasyon_sayısı=5,
    ...      feromon_buharlaşma=0.7, alfa=1.0, beta=5.0, q=10)
    Traceback (most recent call last):
      ...
    StopIteration
    >>> ana(şehirler={0: [0, 0], 1: [2, 2]}, karınca_sayısı=0, iterasyon_sayısı=5,
    ...      feromon_buharlaşma=0.7, alfa=1.0, beta=5.0, q=10)
    ([], inf)
    >>> ana(şehirler={0: [0, 0], 1: [2, 2]}, karınca_sayısı=5, iterasyon_sayısı=0,
    ...      feromon_buharlaşma=0.7, alfa=1.0, beta=5.0, q=10)
    ([], inf)
    >>> ana(şehirler={0: [0, 0], 1: [2, 2]}, karınca_sayısı=5, iterasyon_sayısı=5,
    ...      feromon_buharlaşma=1, alfa=1.0, beta=5.0, q=10)
    ([0, 1, 0], 5.656854249492381)
    >>> ana(şehirler={0: [0, 0], 1: [2, 2]}, karınca_sayısı=5, iterasyon_sayısı=5,
    ...      feromon_buharlaşma=0, alfa=1.0, beta=5.0, q=10)
    ([0, 1, 0], 5.656854249492381)
    """
    # Feromon matrisini başlat
    şehir_sayısı = len(şehirler)
    feromon = [[1.0] * şehir_sayısı] * şehir_sayısı

    en_iyi_yol: list[int] = []
    en_iyi_mesafe = float("inf")
    for _ in range(iterasyon_sayısı):
        karınca_yolları = []
        for _ in range(karınca_sayısı):
            ziyaret_edilmemiş_şehirler = copy.deepcopy(şehirler)
            mevcut_şehir = {next(iter(şehirler.keys())): next(iter(şehirler.values()))}
            del ziyaret_edilmemiş_şehirler[next(iter(mevcut_şehir.keys()))]
            karınca_yolu = [next(iter(mevcut_şehir.keys()))]
            while ziyaret_edilmemiş_şehirler:
                mevcut_şehir, ziyaret_edilmemiş_şehirler = şehir_seç(
                    feromon, mevcut_şehir, ziyaret_edilmemiş_şehirler, alfa, beta
                )
                karınca_yolu.append(next(iter(mevcut_şehir.keys())))
            karınca_yolu.append(0)
            karınca_yolları.append(karınca_yolu)

        feromon, en_iyi_yol, en_iyi_mesafe = feromon_güncelle(
            feromon,
            şehirler,
            feromon_buharlaşma,
            karınca_yolları,
            q,
            en_iyi_yol,
            en_iyi_mesafe,
        )
    return en_iyi_yol, en_iyi_mesafe


def mesafe(şehir1: list[int], şehir2: list[int]) -> float:
    """
    İki koordinat noktası arasındaki mesafeyi hesapla
    >>> mesafe([0, 0], [3, 4] )
    5.0
    >>> mesafe([0, 0], [-3, 4] )
    5.0
    >>> mesafe([0, 0], [-3, -4] )
    5.0
    """
    return (((şehir1[0] - şehir2[0]) ** 2) + ((şehir1[1] - şehir2[1]) ** 2)) ** 0.5


def feromon_güncelle(
    feromon: list[list[float]],
    şehirler: dict[int, list[int]],
    feromon_buharlaşma: float,
    karınca_yolları: list[list[int]],
    q: float,  # Feromon sistemi parametreleri Q, sabit bir değerdir
    en_iyi_yol: list[int],
    en_iyi_mesafe: float,
) -> tuple[list[list[float]], list[int], float]:
    """
    Rotalardaki feromonları güncelle ve en iyi rotayı güncelle
    >>>
    >>> feromon_güncelle(feromon=[[1.0, 1.0], [1.0, 1.0]],
    ...                  şehirler={0: [0,0], 1: [2,2]}, feromon_buharlaşma=0.7,
    ...                  karınca_yolları=[[0, 1, 0]], q=10, en_iyi_yol=[],
    ...                  en_iyi_mesafe=float("inf"))
    ([[0.7, 4.235533905932737], [4.235533905932737, 0.7]], [0, 1, 0], 5.656854249492381)
    >>> feromon_güncelle(feromon=[],
    ...                  şehirler={0: [0,0], 1: [2,2]}, feromon_buharlaşma=0.7,
    ...                  karınca_yolları=[[0, 1, 0]], q=10, en_iyi_yol=[],
    ...                  en_iyi_mesafe=float("inf"))
    Traceback (most recent call last):
      ...
    IndexError: list index out of range
    >>> feromon_güncelle(feromon=[[1.0, 1.0], [1.0, 1.0]],
    ...                  şehirler={}, feromon_buharlaşma=0.7,
    ...                  karınca_yolları=[[0, 1, 0]], q=10, en_iyi_yol=[],
    ...                  en_iyi_mesafe=float("inf"))
    Traceback (most recent call last):
      ...
    KeyError: 0
    """
    for a in range(len(şehirler)):  # Tüm rotalardaki feromon buharlaşmasını güncelle
        for b in range(len(şehirler)):
            feromon[a][b] *= feromon_buharlaşma
    for karınca_yolu in karınca_yolları:
        toplam_mesafe = 0.0
        for i in range(len(karınca_yolu) - 1):  # Toplam mesafeyi hesapla
            toplam_mesafe += mesafe(şehirler[karınca_yolu[i]], şehirler[karınca_yolu[i + 1]])
        delta_feromon = q / toplam_mesafe
        for i in range(len(karınca_yolu) - 1):  # Feromonları güncelle
            feromon[karınca_yolu[i]][karınca_yolu[i + 1]] += delta_feromon
            feromon[karınca_yolu[i + 1]][karınca_yolu[i]] = feromon[karınca_yolu[i]][
                karınca_yolu[i + 1]
            ]

        if toplam_mesafe < en_iyi_mesafe:
            en_iyi_yol = karınca_yolu
            en_iyi_mesafe = toplam_mesafe

    return feromon, en_iyi_yol, en_iyi_mesafe


def şehir_seç(
    feromon: list[list[float]],
    mevcut_şehir: dict[int, list[int]],
    ziyaret_edilmemiş_şehirler: dict[int, list[int]],
    alfa: float,
    beta: float,
) -> tuple[dict[int, list[int]], dict[int, list[int]]]:
    """
    Karıncalar için bir sonraki şehri seç
    >>> şehir_seç(feromon=[[1.0, 1.0], [1.0, 1.0]], mevcut_şehir={0: [0, 0]},
    ...             ziyaret_edilmemiş_şehirler={1: [2, 2]}, alfa=1.0, beta=5.0)
    ({1: [2, 2]}, {})
    >>> şehir_seç(feromon=[], mevcut_şehir={0: [0,0]},
    ...             ziyaret_edilmemiş_şehirler={1: [2, 2]}, alfa=1.0, beta=5.0)
    Traceback (most recent call last):
      ...
    IndexError: list index out of range
    >>> şehir_seç(feromon=[[1.0, 1.0], [1.0, 1.0]], mevcut_şehir={},
    ...             ziyaret_edilmemiş_şehirler={1: [2, 2]}, alfa=1.0, beta=5.0)
    Traceback (most recent call last):
      ...
    StopIteration
    >>> şehir_seç(feromon=[[1.0, 1.0], [1.0, 1.0]], mevcut_şehir={0: [0, 0]},
    ...             ziyaret_edilmemiş_şehirler={}, alfa=1.0, beta=5.0)
    Traceback (most recent call last):
      ...
    IndexError: list index out of range
    """
    olasılıklar = []
    for şehir in ziyaret_edilmemiş_şehirler:
        şehir_mesafesi = mesafe(
            ziyaret_edilmemiş_şehirler[şehir], next(iter(mevcut_şehir.values()))
        )
        olasılık = (feromon[şehir][next(iter(mevcut_şehir.keys()))] ** alfa) * (
            (1 / şehir_mesafesi) ** beta
        )
        olasılıklar.append(olasılık)

    seçilen_şehir_i = random.choices(
        list(ziyaret_edilmemiş_şehirler.keys()), weights=olasılıklar
    )[0]
    seçilen_şehir = {seçilen_şehir_i: ziyaret_edilmemiş_şehirler[seçilen_şehir_i]}
    del ziyaret_edilmemiş_şehirler[next(iter(seçilen_şehir.keys()))]
    return seçilen_şehir, ziyaret_edilmemiş_şehirler


if __name__ == "__main__":
    en_iyi_yol, en_iyi_mesafe = ana(
        şehirler=şehirler,
        karınca_sayısı=10,
        iterasyon_sayısı=20,
        feromon_buharlaşma=0.7,
        alfa=1.0,
        beta=5.0,
        q=10,
    )

    print(f"{en_iyi_yol = }")
    print(f"{en_iyi_mesafe = }")
