#!/usr/bin/python

"""Yazar: OMKAR PATHAK"""

from __future__ import annotations

from queue import Queue


class Grafik:
    def __init__(self) -> None:
        self.düğümler: dict[int, list[int]] = {}

    def grafik_yazdir(self) -> None:
        """
        komşuluk listesi gösterimini yazdırır
        >>> g = Grafik()
        >>> g.grafik_yazdir()
        >>> g.kenar_ekle(0, 1)
        >>> g.grafik_yazdir()
        0  :  1
        """
        for i in self.düğümler:
            print(i, " : ", " -> ".join([str(j) for j in self.düğümler[i]]))

    def kenar_ekle(self, başlangıç_düğüm: int, bitiş_düğüm: int) -> None:
        """
        iki düğüm arasına kenar ekler
        >>> g = Grafik()
        >>> g.grafik_yazdir()
        >>> g.kenar_ekle(0, 1)
        >>> g.grafik_yazdir()
        0  :  1
        """
        if başlangıç_düğüm in self.düğümler:
            self.düğümler[başlangıç_düğüm].append(bitiş_düğüm)
        else:
            self.düğümler[başlangıç_düğüm] = [bitiş_düğüm]

    def bfs(self, başlangıç_düğüm: int) -> set[int]:
        """
        >>> g = Grafik()
        >>> g.kenar_ekle(0, 1)
        >>> g.kenar_ekle(0, 1)
        >>> g.kenar_ekle(0, 2)
        >>> g.kenar_ekle(1, 2)
        >>> g.kenar_ekle(2, 0)
        >>> g.kenar_ekle(2, 3)
        >>> g.kenar_ekle(3, 3)
        >>> sorted(g.bfs(2))
        [0, 1, 2, 3]
        """
        # ziyaret edilen düğümleri saklamak için bir set oluştur
        ziyaret_edilen = set()

        # BFS için tüm düğümleri saklayacak bir FIFO kuyruğu oluştur
        kuyruk: Queue = Queue()

        # kaynak düğümü ziyaret edildi olarak işaretle ve kuyruğa ekle
        ziyaret_edilen.add(başlangıç_düğüm)
        kuyruk.put(başlangıç_düğüm)

        while not kuyruk.empty():
            düğüm = kuyruk.get()

            # tüm komşu düğümleri dolaş ve henüz ziyaret edilmediyse kuyruğa ekle
            for komşu_düğüm in self.düğümler[düğüm]:
                if komşu_düğüm not in ziyaret_edilen:
                    kuyruk.put(komşu_düğüm)
                    ziyaret_edilen.add(komşu_düğüm)
        return ziyaret_edilen


if __name__ == "__main__":
    from doctest import testmod

    testmod(verbose=True)

    g = Grafik()
    g.kenar_ekle(0, 1)
    g.kenar_ekle(0, 2)
    g.kenar_ekle(1, 2)
    g.kenar_ekle(2, 0)
    g.kenar_ekle(2, 3)
    g.kenar_ekle(3, 3)

    g.grafik_yazdir()
    # 0  :  1 -> 2
    # 1  :  2
    # 2  :  0 -> 3
    # 3  :  3

    assert sorted(g.bfs(2)) == [0, 1, 2, 3]
