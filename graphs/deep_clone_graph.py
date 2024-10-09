"""
LeetCode 133. Clone Graph
https://leetcode.com/problems/clone-graph/

Bağlantılı, yönsüz bir grafikte bir düğüm referansı verildiğinde,
grafın derin bir kopyasını (klonunu) döndürün.

Grafikteki her düğüm bir değer (int) ve komşularının bir listesini (List[Node]) içerir.
"""

from dataclasses import dataclass


@dataclass
class Düğüm:
    değer: int = 0
    komşular: list["Düğüm"] | None = None

    def __post_init__(self) -> None:
        """
        >>> Düğüm(3).komşular
        []
        """
        self.komşular = self.komşular or []

    def __hash__(self) -> int:
        """
        >>> hash(Düğüm(3)) != 0
        True
        """
        return id(self)


def graf_klonla(düğüm: Düğüm | None) -> Düğüm | None:
    """
    Bu fonksiyon bağlantılı, yönsüz bir grafın klonunu döndürür.
    >>> graf_klonla(Düğüm(1))
    Düğüm(değer=1, komşular=[])
    >>> graf_klonla(Düğüm(1, [Düğüm(2)]))
    Düğüm(değer=1, komşular=[Düğüm(değer=2, komşular=[])])
    >>> graf_klonla(None) is None
    True
    """
    if not düğüm:
        return None

    orijinallerden_klonlara = {}  # düğümleri klonlara eşle

    yığın = [düğüm]

    while yığın:
        orijinal = yığın.pop()

        if orijinal in orijinallerden_klonlara:
            continue

        orijinallerden_klonlara[orijinal] = Düğüm(orijinal.değer)

        yığın.extend(orijinal.komşular or [])

    for orijinal, klon in orijinallerden_klonlara.items():
        for komşu in orijinal.komşular or []:
            klonlanmış_komşu = orijinallerden_klonlara[komşu]

            if not klon.komşular:
                klon.komşular = []

            klon.komşular.append(klonlanmış_komşu)

    return orijinallerden_klonlara[düğüm]


if __name__ == "__main__":
    import doctest

    doctest.testmod()
