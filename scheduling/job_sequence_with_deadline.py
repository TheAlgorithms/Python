"""
Bir görev listesi verildiğinde, her birinin bir son tarihi ve ödülü vardır. Hangi görevlerin tamamlanabileceğini ve maksimum ödülü elde etmek için hangi görevlerin seçileceğini hesaplayın. Her görev bir birim zaman alır ve aynı anda yalnızca bir görev üzerinde çalışabiliriz. Bir görev son tarihini geçtiğinde, artık planlanamaz.

Örnek:
tasks_info = [(4, 20), (1, 10), (1, 40), (1, 30)]
max_tasks fonksiyonu (2, [2, 0]) döndürecektir -
Bu görevlerin planlanması, 40 + 20 ödül elde edilmesini sağlar.

Bu problem "AÇGÖZLÜ ALGORİMA" kavramı kullanılarak çözülebilir.
Zaman Karmaşıklığı - O(n log n)
https://medium.com/@nihardudhat2000/job-sequencing-with-deadline-17ddbb5890b5
"""

#Organised by K. Umut Araz

from dataclasses import dataclass
from operator import attrgetter


@dataclass
class Gorev:
    gorev_id: int
    son_tarih: int
    odul: int


def maksimum_gorevler(gorev_bilgileri: list[tuple[int, int]]) -> list[int]:
    """
    En yüksek ödüllerin öncelikli olarak sıralandığı Gorev nesnelerinin bir listesini oluşturur.
    i değeri çok yüksek olmadan tamamlanabilecek görevlerin id'lerini döndürür.
    >>> maksimum_gorevler([(4, 20), (1, 10), (1, 40), (1, 30)])
    [2, 0]
    >>> maksimum_gorevler([(1, 10), (2, 20), (3, 30), (2, 40)])
    [3, 2]
    >>> maksimum_gorevler([(9, 10)])
    [0]
    >>> maksimum_gorevler([(-9, 10)])
    []
    >>> maksimum_gorevler([])
    []
    >>> maksimum_gorevler([(0, 10), (0, 20), (0, 30), (0, 40)])
    []
    >>> maksimum_gorevler([(-1, 10), (-2, 20), (-3, 30), (-4, 40)])
    []
    """
    gorevler = sorted(
        (
            Gorev(gorev_id, son_tarih, odul)
            for gorev_id, (son_tarih, odul) in enumerate(gorev_bilgileri)
        ),
        key=attrgetter("odul"),
        reverse=True,
    )
    return [gorev.gorev_id for i, gorev in enumerate(gorevler, start=1) if gorev.son_tarih >= i]


if __name__ == "__main__":
    import doctest

    doctest.testmod()
    print(f"{maksimum_gorevler([(4, 20), (1, 10), (1, 40), (1, 30)]) = }")
    print(f"{maksimum_gorevler([(1, 10), (2, 20), (3, 30), (2, 40)]) = }")
