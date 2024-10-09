"""
https://en.wikipedia.org/wiki/Best-first_search#Greedy_BFS
"""

from __future__ import annotations

#Produced by K. Umut Araz

Yol = list[tuple[int, int]]

# 0'lar serbest yol, 1'ler engellerdir
TEST_IZGARALARI = [
    [
        [0, 0, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 1, 0, 0, 0, 0],
        [1, 0, 1, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 0],
    ],
    [
        [0, 0, 0, 1, 1, 0, 0],
        [0, 0, 0, 0, 1, 0, 1],
        [0, 0, 0, 1, 1, 0, 0],
        [0, 1, 0, 0, 1, 0, 0],
        [1, 0, 0, 1, 1, 0, 1],
        [0, 0, 0, 0, 0, 0, 0],
    ],
    [
        [0, 0, 1, 0, 0],
        [0, 1, 0, 0, 0],
        [0, 0, 1, 0, 1],
        [1, 0, 0, 1, 1],
        [0, 0, 0, 0, 0],
    ],
]

delta = ([-1, 0], [0, -1], [1, 0], [0, 1])  # yukarı, sol, aşağı, sağ


class Düğüm:
    """
    >>> k = Düğüm(0, 0, 4, 5, 0, None)
    >>> k.heuristik_hesapla()
    9
    >>> n = Düğüm(1, 4, 3, 4, 2, None)
    >>> n.heuristik_hesapla()
    2
    >>> l = [k, n]
    >>> n == l[0]
    False
    >>> l.sort()
    >>> n == l[0]
    True
    """

    def __init__(
        self,
        pos_x: int,
        pos_y: int,
        hedef_x: int,
        hedef_y: int,
        g_maliyet: float,
        ebeveyn: Düğüm | None,
    ):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.pos = (pos_y, pos_x)
        self.hedef_x = hedef_x
        self.hedef_y = hedef_y
        self.g_maliyet = g_maliyet
        self.ebeveyn = ebeveyn
        self.f_maliyet = self.heuristik_hesapla()

    def heuristik_hesapla(self) -> float:
        """
        Buradaki heuristik Manhattan Mesafesidir
        Daha fazla seçenek sunmak için genişletilebilir
        """
        dx = abs(self.pos_x - self.hedef_x)
        dy = abs(self.pos_y - self.hedef_y)
        return dx + dy

    def __lt__(self, diğer) -> bool:
        return self.f_maliyet < diğer.f_maliyet

    def __eq__(self, diğer) -> bool:
        return self.pos == diğer.pos


class AçgözlüEnİyiİlk:
    """
    >>> ızgara = TEST_IZGARALARI[2]
    >>> ae = AçgözlüEnİyiİlk(ızgara, (0, 0), (len(ızgara) - 1, len(ızgara[0]) - 1))
    >>> [x.pos for x in ae.ardılları_al(ae.başlangıç)]
    [(1, 0), (0, 1)]
    >>> (ae.başlangıç.pos_y + delta[3][0], ae.başlangıç.pos_x + delta[3][1])
    (0, 1)
    >>> (ae.başlangıç.pos_y + delta[2][0], ae.başlangıç.pos_x + delta[2][1])
    (1, 0)
    >>> ae.yolu_izle(ae.başlangıç)
    [(0, 0)]
    >>> ae.ara()  # doctest: +NORMALIZE_WHITESPACE
    [(0, 0), (1, 0), (2, 0), (2, 1), (3, 1), (4, 1), (4, 2), (4, 3),
     (4, 4)]
    """

    def __init__(
        self, ızgara: list[list[int]], başlangıç: tuple[int, int], hedef: tuple[int, int]
    ):
        self.ızgara = ızgara
        self.başlangıç = Düğüm(başlangıç[1], başlangıç[0], hedef[1], hedef[0], 0, None)
        self.hedef = Düğüm(hedef[1], hedef[0], hedef[1], hedef[0], 99999, None)

        self.açık_düğümler = [self.başlangıç]
        self.kapalı_düğümler: list[Düğüm] = []

        self.ulaşıldı = False

    def ara(self) -> Yol | None:
        """
        Yolu ara,
        eğer bir yol bulunamazsa, sadece başlangıç pozisyonu döndürülür
        """
        while self.açık_düğümler:
            # Açık Düğümler __lt__ kullanılarak sıralanır
            self.açık_düğümler.sort()
            mevcut_düğüm = self.açık_düğümler.pop(0)

            if mevcut_düğüm.pos == self.hedef.pos:
                self.ulaşıldı = True
                return self.yolu_izle(mevcut_düğüm)

            self.kapalı_düğümler.append(mevcut_düğüm)
            ardıllar = self.ardılları_al(mevcut_düğüm)

            for çocuk_düğüm in ardıllar:
                if çocuk_düğüm in self.kapalı_düğümler:
                    continue

                if çocuk_düğüm not in self.açık_düğümler:
                    self.açık_düğümler.append(çocuk_düğüm)

        if not self.ulaşıldı:
            return [self.başlangıç.pos]
        return None

    def ardılları_al(self, ebeveyn: Düğüm) -> list[Düğüm]:
        """
        Ardılların listesini döndürür (hem ızgarada hem de serbest alanlarda)
        """
        return [
            Düğüm(
                pos_x,
                pos_y,
                self.hedef.pos_x,
                self.hedef.pos_y,
                ebeveyn.g_maliyet + 1,
                ebeveyn,
            )
            for eylem in delta
            if (
                0 <= (pos_x := ebeveyn.pos_x + eylem[1]) < len(self.ızgara[0])
                and 0 <= (pos_y := ebeveyn.pos_y + eylem[0]) < len(self.ızgara)
                and self.ızgara[pos_y][pos_x] == 0
            )
        ]

    def yolu_izle(self, düğüm: Düğüm | None) -> Yol:
        """
        Başlangıç düğümüne kadar ebeveynlerden ebeveynlere yolu izler
        """
        mevcut_düğüm = düğüm
        yol = []
        while mevcut_düğüm is not None:
            yol.append((mevcut_düğüm.pos_y, mevcut_düğüm.pos_x))
            mevcut_düğüm = mevcut_düğüm.ebeveyn
        yol.reverse()
        return yol


if __name__ == "__main__":
    for idx, ızgara in enumerate(TEST_IZGARALARI):
        print(f"==ızgara-{idx + 1}==")

        başlangıç = (0, 0)
        hedef = (len(ızgara) - 1, len(ızgara[0]) - 1)
        for eleman in ızgara:
            print(eleman)

        print("------")

        açgözlü_ei = AçgözlüEnİyiİlk(ızgara, başlangıç, hedef)
        yol = açgözlü_ei.ara()
        if yol:
            for pos_x, pos_y in yol:
                ızgara[pos_x][pos_y] = 2

            for eleman in ızgara:
                print(eleman)
