"""

# Organiser: K. Umut Araz

Bu script, Damerau-Levenshtein mesafe algoritmasının bir uygulamasıdır.

Bu algoritma, iki dize dizisi arasındaki düzenleme mesafesini ölçer.

Bu algoritma hakkında daha fazla bilgiye şu Wikipedia makalesinden ulaşabilirsiniz:
https://en.wikipedia.org/wiki/Damerau%E2%80%93Levenshtein_distance
"""


def damerau_levenshtein_distance(birinci_dize: str, ikinci_dize: str) -> int:
    """
    Damerau-Levenshtein mesafe algoritmasını uygular ve iki dize arasındaki
    düzenleme mesafesini ölçer.

    Parametreler:
        birinci_dize: Karşılaştırılacak ilk dize
        ikinci_dize: Karşılaştırılacak ikinci dize

    Dönüş:
        mesafe: İlk ve ikinci dizeler arasındaki düzenleme mesafesi

    >>> damerau_levenshtein_distance("kedi", "kutu")
    1
    >>> damerau_levenshtein_distance("yavru", "yürüyüş")
    3
    >>> damerau_levenshtein_distance("merhaba", "dünya")
    4
    >>> damerau_levenshtein_distance("kitap", "kalem")
    2
    >>> damerau_levenshtein_distance("konteyner", "içerik")
    3
    >>> damerau_levenshtein_distance("konteyner", "kapsam")
    3
    """
    # Mesafeleri saklamak için dinamik programlama matrisini oluştur
    dp_matrix = [[0] * (len(ikinci_dize) + 1) for _ in range(len(birinci_dize) + 1)]

    # Matrisi başlat
    for i in range(len(birinci_dize) + 1):
        dp_matrix[i][0] = i
    for j in range(len(ikinci_dize) + 1):
        dp_matrix[0][j] = j

    # Matrisi doldur
    for i, birinci_karakter in enumerate(birinci_dize, start=1):
        for j, ikinci_karakter in enumerate(ikinci_dize, start=1):
            maliyet = int(birinci_karakter != ikinci_karakter)

            dp_matrix[i][j] = min(
                dp_matrix[i - 1][j] + 1,  # Silme
                dp_matrix[i][j - 1] + 1,  # Ekleme
                dp_matrix[i - 1][j - 1] + maliyet,  # Yer değiştirme
            )

            if (
                i > 1
                and j > 1
                and birinci_dize[i - 1] == ikinci_dize[j - 2]
                and birinci_dize[i - 2] == ikinci_dize[j - 1]
            ):
                # Yer değiştirme
                dp_matrix[i][j] = min(dp_matrix[i][j], dp_matrix[i - 2][j - 2] + maliyet)

    return dp_matrix[-1][-1]


if __name__ == "__main__":
    import doctest

    doctest.testmod()
