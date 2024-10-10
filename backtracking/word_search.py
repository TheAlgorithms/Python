"""
Yazar  : Alexander Pantyukhin
Tarih  : 24 Kasım 2022

Görev:
m x n karakter ızgarası ve bir kelime verildiğinde,
kelimenin ızgarada bulunup bulunmadığını döndürün.

Kelime, ardışık bitişik hücrelerin harflerinden oluşturulabilir,
bitişik hücreler yatay veya dikey olarak komşu olan hücrelerdir.
Aynı harf hücresi birden fazla kullanılamaz.

Organiser: K. Umut Araz

Örnek:

Matris:
---------
|A|B|C|E|
|S|F|C|S|
|A|D|E|E|
---------

Kelime:
"ABCCED"

Sonuç:
True

Uygulama notları: Geri izleme yaklaşımını kullanın.
Her noktada, kelimenin bir sonraki harfini bulmaya çalışmak için tüm komşuları kontrol edin.

leetcode: https://leetcode.com/problems/word-search/

"""


def nokta_anahtarını_al(len_board: int, len_board_column: int, row: int, column: int) -> int:
    """
    Matris indekslerinin hash anahtarını döndürür.

    >>> nokta_anahtarını_al(10, 20, 1, 0)
    200
    """

    return len_board * len_board_column * row + column


def kelime_var_mı(
    board: list[list[str]],
    word: str,
    row: int,
    column: int,
    word_index: int,
    ziyaret_edilen_noktalar: set[int],
) -> bool:
    """
    Kelimenin son ekini aramanın mümkün olup olmadığını döndürür
    word_index'ten başlayarak.

    >>> kelime_var_mı([["A"]], "B", 0, 0, 0, set())
    False
    """

    if board[row][column] != word[word_index]:
        return False

    if word_index == len(word) - 1:
        return True

    yönler = [(0, 1), (0, -1), (-1, 0), (1, 0)]
    len_board = len(board)
    len_board_column = len(board[0])
    for direction in yönler:
        next_i = row + direction[0]
        next_j = column + direction[1]
        if not (0 <= next_i < len_board and 0 <= next_j < len_board_column):
            continue

        key = nokta_anahtarını_al(len_board, len_board_column, next_i, next_j)
        if key in ziyaret_edilen_noktalar:
            continue

        ziyaret_edilen_noktalar.add(key)
        if kelime_var_mı(board, word, next_i, next_j, word_index + 1, ziyaret_edilen_noktalar):
            return True

        ziyaret_edilen_noktalar.remove(key)

    return False


def kelime_bulunur_mu(board: list[list[str]], word: str) -> bool:
    """
    >>> kelime_bulunur_mu([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "ABCCED")
    True
    >>> kelime_bulunur_mu([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "SEE")
    True
    >>> kelime_bulunur_mu([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "ABCB")
    False
    >>> kelime_bulunur_mu([["A"]], "A")
    True
    >>> kelime_bulunur_mu([["B", "A", "A"], ["A", "A", "A"], ["A", "B", "A"]], "ABB")
    False
    >>> kelime_bulunur_mu([["A"]], 123)
    Traceback (most recent call last):
        ...
    ValueError: Kelime parametresi uzunluğu 0'dan büyük bir dize olmalıdır.
    >>> kelime_bulunur_mu([["A"]], "")
    Traceback (most recent call last):
        ...
    ValueError: Kelime parametresi uzunluğu 0'dan büyük bir dize olmalıdır.
    >>> kelime_bulunur_mu([[]], "AB")
    Traceback (most recent call last):
        ...
    ValueError: Tahta tek karakterli dizelerden oluşan boş olmayan bir matris olmalıdır.
    >>> kelime_bulunur_mu([], "AB")
    Traceback (most recent call last):
        ...
    ValueError: Tahta tek karakterli dizelerden oluşan boş olmayan bir matris olmalıdır.
    >>> kelime_bulunur_mu([["A"], [21]], "AB")
    Traceback (most recent call last):
        ...
    ValueError: Tahta tek karakterli dizelerden oluşan boş olmayan bir matris olmalıdır.
    """

    # Tahtayı doğrula
    tahta_hata_mesajı = (
        "Tahta tek karakterli dizelerden oluşan boş olmayan bir matris olmalıdır."
    )

    len_board = len(board)
    if not isinstance(board, list) or len(board) == 0:
        raise ValueError(tahta_hata_mesajı)

    for row in board:
        if not isinstance(row, list) or len(row) == 0:
            raise ValueError(tahta_hata_mesajı)

        for item in row:
            if not isinstance(item, str) or len(item) != 1:
                raise ValueError(tahta_hata_mesajı)

    # Kelimeyi doğrula
    if not isinstance(word, str) or len(word) == 0:
        raise ValueError(
            "Kelime parametresi uzunluğu 0'dan büyük bir dize olmalıdır."
        )

    len_board_column = len(board[0])
    for i in range(len_board):
        for j in range(len_board_column):
            if kelime_var_mı(
                board, word, i, j, 0, {nokta_anahtarını_al(len_board, len_board_column, i, j)}
            ):
                return True

    return False


if __name__ == "__main__":
    import doctest

    doctest.testmod()
