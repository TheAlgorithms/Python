import math


class Graph:
    def __init__(self, n=0):  # 0,1,...,N-1 düğümleri olan bir grafik
        self.n = n
        self.w = [
            [math.inf for j in range(n)] for i in range(n)
        ]  # ağırlık için komşuluk matrisi
        self.dp = [
            [math.inf for j in range(n)] for i in range(n)
        ]  # dp[i][j], i'den j'ye minimum mesafeyi saklar

    def kenar_ekle(self, u, v, w):
        """
        u düğümünden v düğümüne ağırlık w ile yönlendirilmiş bir kenar ekler.

        >>> g = Graph(3)
        >>> g.kenar_ekle(0, 1, 5)
        >>> g.dp[0][1]
        5
        """
        self.dp[u][v] = w

    def floyd_warshall(self):
        """
        Floyd-Warshall algoritmasını kullanarak tüm düğüm çiftleri arasındaki
        en kısa yolları hesaplar.

        >>> g = Graph(3)
        >>> g.kenar_ekle(0, 1, 1)
        >>> g.kenar_ekle(1, 2, 2)
        >>> g.floyd_warshall()
        >>> g.min_goster(0, 2)
        3
        >>> g.min_goster(2, 0)
        inf
        """
        for k in range(self.n):
            for i in range(self.n):
                for j in range(self.n):
                    self.dp[i][j] = min(self.dp[i][j], self.dp[i][k] + self.dp[k][j])

    def min_goster(self, u, v):
        """
        u düğümünden v düğümüne minimum mesafeyi döndürür.

        >>> g = Graph(3)
        >>> g.kenar_ekle(0, 1, 3)
        >>> g.kenar_ekle(1, 2, 4)
        >>> g.floyd_warshall()
        >>> g.min_goster(0, 2)
        7
        >>> g.min_goster(1, 0)
        inf
        """
        return self.dp[u][v]


if __name__ == "__main__":
    import doctest

    doctest.testmod()

    # Örnek kullanım
    graph = Graph(5)
    graph.kenar_ekle(0, 2, 9)
    graph.kenar_ekle(0, 4, 10)
    graph.kenar_ekle(1, 3, 5)
    graph.kenar_ekle(2, 3, 7)
    graph.kenar_ekle(3, 0, 10)
    graph.kenar_ekle(3, 1, 2)
    graph.kenar_ekle(3, 2, 1)
    graph.kenar_ekle(3, 4, 6)
    graph.kenar_ekle(4, 1, 3)
    graph.kenar_ekle(4, 2, 4)
    graph.kenar_ekle(4, 3, 9)
    graph.floyd_warshall()
    print(
        graph.min_goster(1, 4)
    )  # Düğüm 1'den düğüm 4'e minimum mesafeyi çıktılar
    print(
        graph.min_goster(0, 3)
    )  # Düğüm 0'dan düğüm 3'e minimum mesafeyi çıktılar
