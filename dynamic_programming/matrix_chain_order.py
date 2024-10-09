import sys

"""
Dinamik Programlama
Matris Zinciri Çarpımının Uygulanması
Zaman Karmaşıklığı: O(n^3)
Alan Karmaşıklığı: O(n^2)
"""


def matris_zinciri_sirasi(dizi):
    n = len(dizi)
    matris = [[0 for x in range(n)] for x in range(n)]
    cozum = [[0 for x in range(n)] for x in range(n)]

    for zincir_uzunlugu in range(2, n):
        for a in range(1, n - zincir_uzunlugu + 1):
            b = a + zincir_uzunlugu - 1

            matris[a][b] = sys.maxsize
            for c in range(a, b):
                maliyet = (
                    matris[a][c] + matris[c + 1][b] + dizi[a - 1] * dizi[c] * dizi[b]
                )
                if maliyet < matris[a][b]:
                    matris[a][b] = maliyet
                    cozum[a][b] = c
    return matris, cozum


# Matrisin sırasını Ai olarak yazdır
def optimal_cozumu_yazdir(optimal_cozum, i, j):
    if i == j:
        print("A" + str(i), end=" ")
    else:
        print("(", end=" ")
        optimal_cozumu_yazdir(optimal_cozum, i, optimal_cozum[i][j])
        optimal_cozumu_yazdir(optimal_cozum, optimal_cozum[i][j] + 1, j)
        print(")", end=" ")


def main():
    dizi = [30, 35, 15, 5, 10, 20, 25]
    n = len(dizi)
    # Yukarıdaki diziden oluşturulan matrisin boyutu
    # 30*35 35*15 15*5 5*10 10*20 20*25
    matris, optimal_cozum = matris_zinciri_sirasi(dizi)

    print("Gerekli İşlem Sayısı: " + str(matris[1][n - 1]))
    optimal_cozumu_yazdir(optimal_cozum, 1, n - 1)


if __name__ == "__main__":
    main()
