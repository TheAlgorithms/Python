from __future__ import annotations

YÖNLER = [
    [-1, 0],  # sol
    [0, -1],  # aşağı
    [1, 0],  # sağ
    [0, 1],  # yukarı
]

# Produced by K. Umut Araz

# yolu arama fonksiyonu
def ara(
    ızgara: list[list[int]],
    başlangıç: list[int],
    hedef: list[int],
    maliyet: int,
    heuristik: list[list[int]],
) -> tuple[list[list[int]], list[list[int]]]:
    """
    Engellerden kaçınarak bir ızgarada yol arayın.
    >>> ızgara = [[0, 1, 0, 0, 0, 0],
    ...           [0, 1, 0, 0, 0, 0],
    ...           [0, 1, 0, 0, 0, 0],
    ...           [0, 1, 0, 0, 1, 0],
    ...           [0, 0, 0, 0, 1, 0]]
    >>> başlangıç = [0, 0]
    >>> hedef = [len(ızgara) - 1, len(ızgara[0]) - 1]
    >>> maliyet = 1
    >>> heuristik = [[0 for row in range(len(ızgara[0]))] for col in range(len(ızgara))]
    >>> for i in range(len(ızgara)):
    ...     for j in range(len(ızgara[0])):
    ...         heuristik[i][j] = abs(i - hedef[0]) + abs(j - hedef[1])
    ...         if ızgara[i][j] == 1:
    ...             heuristik[i][j] = 99
    >>> yol, eylem = ara(ızgara, başlangıç, hedef, maliyet, heuristik)
    >>> yol  # doctest: +NORMALIZE_WHITESPACE
    [[0, 0], [1, 0], [2, 0], [3, 0], [4, 0], [4, 1], [4, 2], [4, 3], [3, 3],
    [2, 3], [2, 4], [2, 5], [3, 5], [4, 5]]
    >>> eylem  # doctest: +NORMALIZE_WHITESPACE
    [[0, 0, 0, 0, 0, 0], [2, 0, 0, 0, 0, 0], [2, 0, 0, 0, 3, 3],
    [2, 0, 0, 0, 0, 2], [2, 3, 3, 3, 0, 2]]
    """
    kapalı = [
        [0 for col in range(len(ızgara[0]))] for row in range(len(ızgara))
    ]  # referans ızgara
    kapalı[başlangıç[0]][başlangıç[1]] = 1
    eylem = [
        [0 for col in range(len(ızgara[0]))] for row in range(len(ızgara))
    ]  # eylem ızgarası

    x = başlangıç[0]
    y = başlangıç[1]
    g = 0
    f = g + heuristik[x][y]  # başlangıç hücresinden hedef hücresine maliyet
    hücre = [[f, g, x, y]]

    bulundu = False  # arama tamamlandığında ayarlanan bayrak
    vazgeç = False  # genişletemezsek ayarlanan bayrak

    while not bulundu and not vazgeç:
        if len(hücre) == 0:
            raise ValueError("Algoritma çözüm bulamıyor")
        else:  # hedefe daha yakın hareket etmek için en az maliyetli eylemi seçmek
            hücre.sort()
            hücre.reverse()
            sonraki_hücre = hücre.pop()
            x = sonraki_hücre[2]
            y = sonraki_hücre[3]
            g = sonraki_hücre[1]

            if x == hedef[0] and y == hedef[1]:
                bulundu = True
            else:
                for i in range(len(YÖNLER)):  # farklı geçerli eylemleri denemek için
                    x2 = x + YÖNLER[i][0]
                    y2 = y + YÖNLER[i][1]
                    if (
                        x2 >= 0
                        and x2 < len(ızgara)
                        and y2 >= 0
                        and y2 < len(ızgara[0])
                        and kapalı[x2][y2] == 0
                        and ızgara[x2][y2] == 0
                    ):
                        g2 = g + maliyet
                        f2 = g2 + heuristik[x2][y2]
                        hücre.append([f2, g2, x2, y2])
                        kapalı[x2][y2] = 1
                        eylem[x2][y2] = i
    ters_yol = []
    x = hedef[0]
    y = hedef[1]
    ters_yol.append([x, y])  # buradan ters yolu alıyoruz
    while x != başlangıç[0] or y != başlangıç[1]:
        x2 = x - YÖNLER[eylem[x][y]][0]
        y2 = y - YÖNLER[eylem[x][y]][1]
        x = x2
        y = y2
        ters_yol.append([x, y])

    yol = []
    for i in range(len(ters_yol)):
        yol.append(ters_yol[len(ters_yol) - 1 - i])
    return yol, eylem


if __name__ == "__main__":
    ızgara = [
        [0, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],  # 0 serbest yol, 1 ise engellerdir
        [0, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, 1, 0],
        [0, 0, 0, 0, 1, 0],
    ]

    başlangıç = [0, 0]
    # tüm koordinatlar [y,x] formatında verilir
    hedef = [len(ızgara) - 1, len(ızgara[0]) - 1]
    maliyet = 1

    # yolu hedefe yaklaştıran maliyet haritası
    heuristik = [[0 for row in range(len(ızgara[0]))] for col in range(len(ızgara))]
    for i in range(len(ızgara)):
        for j in range(len(ızgara[0])):
            heuristik[i][j] = abs(i - hedef[0]) + abs(j - hedef[1])
            if ızgara[i][j] == 1:
                # heuristik haritasına ekstra ceza eklendi
                heuristik[i][j] = 99

    yol, eylem = ara(ızgara, başlangıç, hedef, maliyet, heuristik)

    print("EYLEM HARİTASI")
    for i in range(len(eylem)):
        print(eylem[i])

    for i in range(len(yol)):
        print(yol[i])
