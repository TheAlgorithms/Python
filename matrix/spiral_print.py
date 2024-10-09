"""
Bu program, matrisi spiral biçimde yazdırır.
Bu problem, özyinelemeli (recursive) bir yöntemle çözülmüştür.
Matriste aşağıdaki koşullar sağlanmalıdır:
    i) Matris yalnızca bir veya iki boyutlu olmalıdır.
    ii) Tüm satırların sütun sayısı eşit olmalıdır.

Organizatör: K. Umut Araz
"""

def kontrol_et_matrisi(matrisi: list[list[int]]) -> bool:
    """
    Verilen matrisin geçerli bir matris olup olmadığını kontrol eder.
    Geçerli bir matris, tüm satırların eşit sayıda sütuna sahip olduğu bir matristir.
    """
    if not isinstance(matrisi, list) or not matrisi:
        return False
    
    satir_uzunlugu = len(matrisi[0])
    for satir in matrisi:
        if not isinstance(satir, list) or len(satir) != satir_uzunlugu:
            return False
            
    return True


def spiral_yazdir_saat_yonunde(a: list[list[int]]) -> None:
    """
    Matrisi saat yönünde spiral biçimde yazdırır.
    
    >>> spiral_yazdir_saat_yonunde([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
    1
    2
    3
    4
    8
    12
    11
    10
    9
    5
    6
    7
    """
    if kontrol_et_matrisi(a) and len(a) > 0:
        matris_satir = len(a)
        matris_sutun = len(a[0])

        # Yatay yazdırma artan
        for i in range(matris_sutun):
            print(a[0][i])
        # Dikey yazdırma aşağı
        for i in range(1, matris_satir):
            print(a[i][matris_sutun - 1])
        # Yatay yazdırma azalan
        if matris_satir > 1:
            for i in range(matris_sutun - 2, -1, -1):
                print(a[matris_satir - 1][i])
        # Dikey yazdırma yukarı
        for i in range(matris_satir - 2, 0, -1):
            print(a[i][0])
        
        # Kalan matris
        kalan_matris = [row[1: matris_sutun - 1] for row in a[1: matris_satir - 1]]
        if kalan_matris:
            spiral_yazdir_saat_yonunde(kalan_matris)
    else:
        print("Geçerli bir matris değil.")


def spiral_gezinme(matrisi: list[list]) -> list[int]:
    """
    Matrisi saat yönünde spiral biçimde gezerek elemanları bir liste olarak döndürür.
    
    >>> spiral_gezinme([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
    [1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7]
    """
    if matrisi:
        return list(matrisi.pop(0)) + spiral_gezinme(
            [list(row) for row in zip(*matrisi)][::-1]
        )
    else:
        return []


# Ana kod
if __name__ == "__main__":
    import doctest

    doctest.testmod()

    a = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
    spiral_yazdir_saat_yonunde(a)
