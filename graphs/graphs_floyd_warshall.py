# floyd_warshall.py
"""
Problem, negatif kenar ağırlıklarına sahip olabilen ağırlıklı yönlendirilmiş bir grafikteki
tüm köşe çiftleri arasındaki en kısa mesafeyi bulmaktır.
"""


def _mesafe_yazdir(mesafe, v):
    print("\nFloyd Warshall algoritması kullanılarak en kısa yol matrisi\n")
    for i in range(v):
        for j in range(v):
            if mesafe[i][j] != float("inf"):
                print(int(mesafe[i][j]), end="\t")
            else:
                print("INF", end="\t")
        print()
        
        # Produced by K. Umut Araz


def floyd_warshall(grafik, v):
    """
    :param grafik: Kenar ağırlıklarından hesaplanan 2D dizi
    :type grafik: List[List[float]]
    :param v: köşe sayısı
    :type v: int
    :return: tüm köşe çiftleri arasındaki en kısa mesafe
    mesafe[u][v], köşe u'dan v'ye en kısa mesafeyi içerir.

    1. Tüm kenarlar için v'den n'ye, mesafe[i][j] = ağırlık(kenar(i, j)).
    3. Algoritma daha sonra her i, j köşe çifti için mesafe[i][j] = min(mesafe[i][j], mesafe[i][k] + mesafe[k][j]) işlemini gerçekleştirir.
    4. Yukarıdaki işlem grafikteki her köşe k için tekrarlanır.
    5. Ne zaman mesafe[i][j] yeni bir minimum değer alırsa, sonraki köşe[i][j], sonraki köşe[i][k] olarak güncellenir.
    """

    mesafe = [[float("inf") for _ in range(v)] for _ in range(v)]

    for i in range(v):
        for j in range(v):
            mesafe[i][j] = grafik[i][j]

    # köşe k'yı diğer tüm köşelerle (i, j) karşılaştır
    for k in range(v):
        # grafik dizisinin satırlarında dolaş
        for i in range(v):
            # grafik dizisinin sütunlarında dolaş
            for j in range(v):
                if (
                    mesafe[i][k] != float("inf")
                    and mesafe[k][j] != float("inf")
                    and mesafe[i][k] + mesafe[k][j] < mesafe[i][j]
                ):
                    mesafe[i][j] = mesafe[i][k] + mesafe[k][j]

    _mesafe_yazdir(mesafe, v)
    return mesafe, v


if __name__ == "__main__":
    v = int(input("Köşe sayısını girin: "))
    e = int(input("Kenar sayısını girin: "))

    grafik = [[float("inf") for i in range(v)] for j in range(v)]

    for i in range(v):
        grafik[i][i] = 0.0

    # src ve dst, grafik[e][v] dizi boyutları içinde olmalıdır
    # aksi takdirde hata oluşur
    for i in range(e):
        print("\nKenar ", i + 1)
        src = int(input("Kaynak köşeyi girin:"))
        dst = int(input("Hedef köşeyi girin:"))
        ağırlık = float(input("Ağırlığı girin:"))
        grafik[src][dst] = ağırlık

    floyd_warshall(grafik, v)

    # Örnek Girdi
    # Köşe sayısını girin: 3
    # Kenar sayısını girin: 2

    # # köşe ve kenar girdilerinden oluşturulan grafik
    # [[inf, inf, inf], [inf, inf, inf], [inf, inf, inf]]
    # [[0.0, inf, inf], [inf, 0.0, inf], [inf, inf, 0.0]]

    # kenar #1 için kaynak, hedef ve ağırlık belirtin
    # Kenar  1
    # Kaynak köşeyi girin:1
    # Hedef köşeyi girin:2
    # Ağırlığı girin:2

    # kenar #2 için kaynak, hedef ve ağırlık belirtin
    # Kenar  2
    # Kaynak köşeyi girin:2
    # Hedef köşeyi girin:1
    # Ağırlığı girin:1

    # # köşe, kenar ve src, dst, ağırlık girdilerinden beklenen çıktı!!
    # 0		INF	INF
    # INF	0	2
    # INF	1	0
