"""
Minimax algoritması, bir oyunda maksimum skoru elde etmek için tüm olası hamleleri kontrol eder.
depth, oyun ağacındaki mevcut derinliği belirtir.

nodeIndex, scores[] içindeki mevcut düğümün indeksidir.
Eğer hamle maksimize edici oyuncuya aitse true, değilse false döner.
Oyun ağacının yaprakları scores[] içinde saklanır.
height, oyun ağacının maksimum yüksekliğidir.
"""

from __future__ import annotations

import math


def minimax(
    depth: int, node_index: int, is_max: bool, scores: list[int], height: float
) -> int:
    """
    Bu fonksiyon, iki oyunculu bir oyunda optimal skoru elde etmek için minimax algoritmasını uygular.
    Eğer oyuncu maksimize edici ise, skor maksimize edilir.
    Eğer oyuncu minimize edici ise, skor minimize edilir.

    Parametreler:
    - depth: Oyun ağacındaki mevcut derinlik.
    - node_index: Scores listesindeki mevcut düğümün indeksi.
    - is_max: Mevcut hamlenin maksimize edici oyuncuya (True) veya minimize edici oyuncuya (False) ait olduğunu belirten bir boolean.
    - scores: Oyun ağacının yapraklarının skorlarını içeren bir liste.
    - height: Oyun ağacının maksimum yüksekliği.

    Dönüş:
    - Mevcut oyuncu için optimal skoru temsil eden bir tamsayı.

    >>> import math
    >>> scores = [90, 23, 6, 33, 21, 65, 123, 34423]
    >>> height = math.log(len(scores), 2)
    >>> minimax(0, 0, True, scores, height)
    65
    >>> minimax(-1, 0, True, scores, height)
    Traceback (most recent call last):
        ...
    ValueError: Derinlik 0'dan küçük olamaz
    >>> minimax(0, 0, True, [], 2)
    Traceback (most recent call last):
        ...
    ValueError: Skorlar boş olamaz
    >>> scores = [3, 5, 2, 9, 12, 5, 23, 23]
    >>> height = math.log(len(scores), 2)
    >>> minimax(0, 0, True, scores, height)
    12
    """

    if depth < 0:
        raise ValueError("Derinlik 0'dan küçük olamaz")
    if len(scores) == 0:
        raise ValueError("Skorlar boş olamaz")

    # Temel durum: Mevcut derinlik, ağacın yüksekliğine eşitse,
    # mevcut düğümün skorunu döndür.
    if depth == height:
        return scores[node_index]

    # Eğer maksimize edici oyuncunun sırasıysa, iki olası hamle arasından maksimum skoru seç.
    if is_max:
        return max(
            minimax(depth + 1, node_index * 2, False, scores, height),
            minimax(depth + 1, node_index * 2 + 1, False, scores, height),
        )

    # Eğer minimize edici oyuncunun sırasıysa, iki olası hamle arasından minimum skoru seç.
    return min(
        minimax(depth + 1, node_index * 2, True, scores, height),
        minimax(depth + 1, node_index * 2 + 1, True, scores, height),
    )


def main() -> None:
    # Örnek skorlar ve yükseklik hesaplaması
    scores = [90, 23, 6, 33, 21, 65, 123, 34423]
    height = math.log(len(scores), 2)

    # Minimax algoritmasını kullanarak optimal değeri hesapla ve yazdır
    print("Optimal değer : ", end="")
    print(minimax(0, 0, True, scores, height))


if __name__ == "__main__":
    import doctest

    doctest.testmod()
    main()
