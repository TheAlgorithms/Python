"""
Bu betik, ikili bir ızgara üzerinde Dijkstra algoritmasını uygular.
Izgara, 0 ve 1'lerden oluşur; burada 1, yürünebilir bir düğümü ve 0, bir engeli temsil eder.
Algoritma, başlangıç düğümünden hedef düğüme en kısa yolu bulur.
Çapraz hareketlere izin verilebilir veya verilmeyebilir.
"""

from heapq import heappop, heappush

import numpy as np


def dijkstra(
    grid: np.ndarray,
    kaynak: tuple[int, int],
    hedef: tuple[int, int],
    capraz_hareket: bool,
) -> tuple[float | int, list[tuple[int, int]]]:
    """
    İkili bir ızgara üzerinde Dijkstra algoritmasını uygular.

    Argümanlar:
        grid (np.ndarray): Izgarayı temsil eden 2D numpy dizisi.
        1, yürünebilir bir düğümü ve 0, bir engeli temsil eder.
        kaynak (Tuple[int, int]): Başlangıç düğümünü temsil eden bir demet.
        hedef (Tuple[int, int]): Hedef düğümü temsil eden bir demet.
        capraz_hareket (bool): Çapraz hareketlere izin verilip verilmediğini belirleyen bir boolean.

    Döndürür:
        Tuple[Union[float, int], List[Tuple[int, int]]]:
        Başlangıç düğümünden hedef düğüme en kısa mesafe ve düğümlerin listesi olarak en kısa yol.

    >>> dijkstra(np.array([[1, 1, 1], [0, 1, 0], [0, 1, 1]]), (0, 0), (2, 2), False)
    (4.0, [(0, 0), (0, 1), (1, 1), (2, 1), (2, 2)])

    >>> dijkstra(np.array([[1, 1, 1], [0, 1, 0], [0, 1, 1]]), (0, 0), (2, 2), True)
    (2.0, [(0, 0), (1, 1), (2, 2)])

    >>> dijkstra(np.array([[1, 1, 1], [0, 0, 1], [0, 1, 1]]), (0, 0), (2, 2), False)
    (4.0, [(0, 0), (0, 1), (0, 2), (1, 2), (2, 2)])
    """
    satirlar, sutunlar = grid.shape
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    if capraz_hareket:
        dx += [-1, -1, 1, 1]
        dy += [-1, 1, -1, 1]

    kuyruk, ziyaret_edilen = [(0, kaynak)], set()
    matris = np.full((satirlar, sutunlar), np.inf)
    matris[kaynak] = 0
    oncekiler = np.empty((satirlar, sutunlar), dtype=object)
    oncekiler[kaynak] = None

    while kuyruk:
        (mesafe, (x, y)) = heappop(kuyruk)
        if (x, y) in ziyaret_edilen:
            continue
        ziyaret_edilen.add((x, y))

        if (x, y) == hedef:
            yol = []
            while (x, y) != kaynak:
                yol.append((x, y))
                x, y = oncekiler[x, y]
            yol.append(kaynak)  # kaynağı manuel olarak ekle
            yol.reverse()
            return float(matris[hedef]), yol

        for i in range(len(dx)):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < satirlar and 0 <= ny < sutunlar:
                sonraki_dugum = grid[nx][ny]
                if sonraki_dugum == 1 or matris[nx, ny] > mesafe + 1:
                    heappush(kuyruk, (mesafe + 1, (nx, ny)))
                    matris[nx, ny] = mesafe + 1
                    oncekiler[nx, ny] = (x, y)

    return np.inf, []


if __name__ == "__main__":
    import doctest

    doctest.testmod()
