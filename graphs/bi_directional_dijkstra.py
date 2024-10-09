"""
Çift yönlü Dijkstra algoritması.

Çift yönlü bir yaklaşım, Dijkstra'nın arama algoritması için
verimli ve daha az zaman alan bir optimizasyondur.

Referans: shorturl.at/exHM7
"""

# Yazar: K. Umut Araz (https://github.com/arazumut)

from queue import PriorityQueue
from typing import Any

import numpy as np


def geçiş_ve_gevşetme(
    grafik: dict,
    v: str,
    ziyaret_edilen_ileri: set,
    ziyaret_edilen_geri: set,
    maliyet_ileri: dict,
    maliyet_geri: dict,
    kuyruk: PriorityQueue,
    ebeveyn: dict,
    en_kısa_mesafe: float,
) -> float:
    for sonraki, d in grafik[v]:
        if sonraki in ziyaret_edilen_ileri:
            continue
        eski_maliyet_ileri = maliyet_ileri.get(sonraki, np.inf)
        yeni_maliyet_ileri = maliyet_ileri[v] + d
        if yeni_maliyet_ileri < eski_maliyet_ileri:
            kuyruk.put((yeni_maliyet_ileri, sonraki))
            maliyet_ileri[sonraki] = yeni_maliyet_ileri
            ebeveyn[sonraki] = v
        if (
            sonraki in ziyaret_edilen_geri
            and maliyet_ileri[v] + d + maliyet_geri[sonraki] < en_kısa_mesafe
        ):
            en_kısa_mesafe = maliyet_ileri[v] + d + maliyet_geri[sonraki]
    return en_kısa_mesafe


def çift_yönlü_dijkstra(
    kaynak: str, hedef: str, grafik_ileri: dict, grafik_geri: dict
) -> int:
    """
    Çift yönlü Dijkstra algoritması.

    Dönüş:
        en_kısa_yol_uzunluğu (int): en kısa yolun uzunluğu.

    Uyarılar:
        Eğer hedefe ulaşılamazsa, fonksiyon -1 döner.

    >>> çift_yönlü_dijkstra("E", "F", grafik_ileri, grafik_geri)
    3
    """
    en_kısa_yol_uzunluğu = -1

    ziyaret_edilen_ileri = set()
    ziyaret_edilen_geri = set()
    maliyet_ileri = {kaynak: 0}
    maliyet_geri = {hedef: 0}
    ebeveyn_ileri = {kaynak: None}
    ebeveyn_geri = {hedef: None}
    kuyruk_ileri: PriorityQueue[Any] = PriorityQueue()
    kuyruk_geri: PriorityQueue[Any] = PriorityQueue()

    en_kısa_mesafe = np.inf

    kuyruk_ileri.put((0, kaynak))
    kuyruk_geri.put((0, hedef))

    if kaynak == hedef:
        return 0

    while not kuyruk_ileri.empty() and not kuyruk_geri.empty():
        _, v_ileri = kuyruk_ileri.get()
        ziyaret_edilen_ileri.add(v_ileri)

        _, v_geri = kuyruk_geri.get()
        ziyaret_edilen_geri.add(v_geri)

        en_kısa_mesafe = geçiş_ve_gevşetme(
            grafik_ileri,
            v_ileri,
            ziyaret_edilen_ileri,
            ziyaret_edilen_geri,
            maliyet_ileri,
            maliyet_geri,
            kuyruk_ileri,
            ebeveyn_ileri,
            en_kısa_mesafe,
        )

        en_kısa_mesafe = geçiş_ve_gevşetme(
            grafik_geri,
            v_geri,
            ziyaret_edilen_geri,
            ziyaret_edilen_ileri,
            maliyet_geri,
            maliyet_ileri,
            kuyruk_geri,
            ebeveyn_geri,
            en_kısa_mesafe,
        )

        if maliyet_ileri[v_ileri] + maliyet_geri[v_geri] >= en_kısa_mesafe:
            break

    if en_kısa_mesafe != np.inf:
        en_kısa_yol_uzunluğu = en_kısa_mesafe
    return en_kısa_yol_uzunluğu


grafik_ileri = {
    "B": [["C", 1]],
    "C": [["D", 1]],
    "D": [["F", 1]],
    "E": [["B", 1], ["G", 2]],
    "F": [],
    "G": [["F", 1]],
}
grafik_geri = {
    "B": [["E", 1]],
    "C": [["B", 1]],
    "D": [["C", 1]],
    "F": [["D", 1], ["G", 1]],
    "E": [[None, np.inf]],
    "G": [["E", 2]],
}

if __name__ == "__main__":
    import doctest

    doctest.testmod()
