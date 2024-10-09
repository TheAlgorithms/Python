#!/usr/bin/python

"""Yazar: OMKAR PATHAK"""


class Graf:
    def __init__(self):
        self.düğüm = {}

    # Graf düğümlerini yazdırmak için
    def graf_yazdir(self) -> None:
        """
        Graf düğümlerini yazdır.

        Örnek:
        >>> g = Graf()
        >>> g.kenar_ekle(0, 1)
        >>> g.kenar_ekle(0, 2)
        >>> g.kenar_ekle(1, 2)
        >>> g.kenar_ekle(2, 0)
        >>> g.kenar_ekle(2, 3)
        >>> g.kenar_ekle(3, 3)
        >>> g.graf_yazdir()
        {0: [1, 2], 1: [2], 2: [0, 3], 3: [3]}
        0  ->  1 -> 2
        1  ->  2
        2  ->  0 -> 3
        3  ->  3
        """
        print(self.düğüm)
        for i in self.düğüm:
            print(i, " -> ", " -> ".join([str(j) for j in self.düğüm[i]]))

    # İki düğüm arasına kenar eklemek için
    def kenar_ekle(self, kaynak_düğüm: int, hedef_düğüm: int) -> None:
        """
        İki düğüm arasına kenar ekle.

        :param kaynak_düğüm: Kaynak düğüm.
        :param hedef_düğüm: Hedef düğüm.

        Örnek:
        >>> g = Graf()
        >>> g.kenar_ekle(0, 1)
        >>> g.kenar_ekle(0, 2)
        >>> g.graf_yazdir()
        {0: [1, 2]}
        0  ->  1 -> 2
        """
        # düğüm zaten mevcutsa kontrol et,
        if kaynak_düğüm in self.düğüm:
            self.düğüm[kaynak_düğüm].append(hedef_düğüm)
        else:
            # değilse yeni bir düğüm oluştur
            self.düğüm[kaynak_düğüm] = [hedef_düğüm]

    def dfs(self) -> None:
        """
        Graf üzerinde derinlik öncelikli arama (DFS) yap ve ziyaret edilen düğümleri yazdır.

        Örnek:
        >>> g = Graf()
        >>> g.kenar_ekle(0, 1)
        >>> g.kenar_ekle(0, 2)
        >>> g.kenar_ekle(1, 2)
        >>> g.kenar_ekle(2, 0)
        >>> g.kenar_ekle(2, 3)
        >>> g.kenar_ekle(3, 3)
        >>> g.dfs()
        0 1 2 3
        """
        # ziyaret edilen düğümleri saklamak için dizi
        ziyaret_edildi = [False] * len(self.düğüm)

        # özyinelemeli yardımcı fonksiyonu çağır
        for i in range(len(self.düğüm)):
            if not ziyaret_edildi[i]:
                self.dfs_özyinelemeli(i, ziyaret_edildi)

    def dfs_özyinelemeli(self, başlangıç_düğüm: int, ziyaret_edildi: list) -> None:
        """
        Graf üzerinde özyinelemeli derinlik öncelikli arama (DFS) yap.

        :param başlangıç_düğüm: Arama için başlangıç düğümü.
        :param ziyaret_edildi: Ziyaret edilen düğümleri izlemek için liste.

        Örnek:
        >>> g = Graf()
        >>> g.kenar_ekle(0, 1)
        >>> g.kenar_ekle(0, 2)
        >>> g.kenar_ekle(1, 2)
        >>> g.kenar_ekle(2, 0)
        >>> g.kenar_ekle(2, 3)
        >>> g.kenar_ekle(3, 3)
        >>> ziyaret_edildi = [False] * len(g.düğüm)
        >>> g.dfs_özyinelemeli(0, ziyaret_edildi)
        0 1 2 3
        """
        # başlangıç düğümünü ziyaret edildi olarak işaretle
        ziyaret_edildi[başlangıç_düğüm] = True

        print(başlangıç_düğüm, end="")

        # Bu düğüme bitişik olan tüm düğümler için yinele
        for i in self.düğüm[başlangıç_düğüm]:
            if not ziyaret_edildi[i]:
                print(" ", end="")
                self.dfs_özyinelemeli(i, ziyaret_edildi)


if __name__ == "__main__":
    import doctest

    doctest.testmod()

    g = Graf()
    g.kenar_ekle(0, 1)
    g.kenar_ekle(0, 2)
    g.kenar_ekle(1, 2)
    g.kenar_ekle(2, 0)
    g.kenar_ekle(2, 3)
    g.kenar_ekle(3, 3)

    g.graf_yazdir()
    print("DFS:")
    g.dfs()
