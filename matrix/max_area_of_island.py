"""
İki boyutlu bir ikili matris verildiğinde, bir ada 1'lerin (karasal alanı temsil eden) 
dört yönlü (yatay veya dikey) bağlı olduğu bir grup olarak tanımlanır. Matrisin dört kenarının 
su ile çevrili olduğunu varsayabilirsiniz. Bir adanın alanı, adadaki 1 değerine sahip hücrelerin 
sayısıdır. Bir matris içindeki en büyük adanın alanını döndürün. Eğer ada yoksa, 0 döndürün.

Organiser: K. Umut Araz
"""

matris = [
    [0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
    [0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0],
    [0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0],
]


def güvenli_mi(satır: int, sütun: int, satır_sayısı: int, sütun_sayısı: int) -> bool:
    """
    (satır, sütun) koordinatının geçerli olup olmadığını kontrol eder.

    >>> güvenli_mi(0, 0, 5, 5)
    True
    >>> güvenli_mi(-1, -1, 5, 5)
    False
    """
    return 0 <= satır < satır_sayısı and 0 <= sütun < sütun_sayısı


def derinlikten_ilk_arama(satır: int, sütun: int, görülen: set, mat: list[list[int]]) -> int:
    """
    Adanın mevcut alanını döndürür.

    >>> derinlikten_ilk_arama(0, 0, set(), matris)
    0
    """
    satır_sayısı = len(mat)
    sütun_sayısı = len(mat[0])
    if güvenli_mi(satır, sütun, satır_sayısı, sütun_sayısı) and (satır, sütun) not in görülen and mat[satır][sütun] == 1:
        görülen.add((satır, sütun))
        return (
            1
            + derinlikten_ilk_arama(satır + 1, sütun, görülen, mat)
            + derinlikten_ilk_arama(satır - 1, sütun, görülen, mat)
            + derinlikten_ilk_arama(satır, sütun + 1, görülen, mat)
            + derinlikten_ilk_arama(satır, sütun - 1, görülen, mat)
        )
    else:
        return 0


def en_büyük_alani_bul(mat: list[list[int]]) -> int:
    """
    Tüm adaların alanını bulur ve en büyük alanı döndürür.

    >>> en_büyük_alani_bul(matris)
    6
    """
    görülen: set = set()

    en_büyük_alani = 0
    for satır, satır_dizisi in enumerate(mat):
        for sütun, eleman in enumerate(satır_dizisi):
            if eleman == 1 and (satır, sütun) not in görülen:
                # Alanı maksimize etme
                en_büyük_alani = max(en_büyük_alani, derinlikten_ilk_arama(satır, sütun, görülen, mat))
    return en_büyük_alani


if __name__ == "__main__":
    import doctest

    print(en_büyük_alani_bul(matris))  # Çıktı -> 6

    """
    Açıklama:
    Dört yönde (yatay veya dikey) hareket etmemize izin verildiği için, bir matris içinde 
    x ve y pozisyonunda isek, olası hareketler şunlardır:

    Yönler [(x, y+1), (x, y-1), (x+1, y), (x-1, y)] ancak sınır durumlarına da dikkat etmemiz 
    gerekiyor; x ve y sıfırdan küçük olamaz ve sırasıyla satır ve sütun sayısından büyük olamaz.

    Görselleştirme
    mat = [
        [0,0,A,0,0,0,0,B,0,0,0,0,0],
        [0,0,0,0,0,0,0,B,B,B,0,0,0],
        [0,C,C,0,D,0,0,0,0,0,0,0,0],
        [0,C,0,0,D,D,0,0,E,0,E,0,0],
        [0,C,0,0,D,D,0,0,E,E,E,0,0],
        [0,0,0,0,0,0,0,0,0,0,E,0,0],
        [0,0,0,0,0,0,0,F,F,F,0,0,0],
        [0,0,0,0,0,0,0,F,F,0,0,0,0]
    ]

    Görselleştirme için, bağlı adayı harflerle tanımladım. Gözlemlerimize göre,
        A adası 1 alanına sahiptir.
        B adası 4 alanına sahiptir.
        C adası 4 alanına sahiptir.
        D adası 5 alanına sahiptir.
        E adası 6 alanına sahiptir ve
        F adası 5 alanına sahiptir.

    Belirtilen alanlara sahip 6 benzersiz ada vardır ve bunların en büyüğü 6'dır, bu yüzden 6 döndürüyoruz.
    """

    doctest.testmod()
