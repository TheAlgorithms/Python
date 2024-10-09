"""
Bu, açgözlü birleştirme sıralama algoritmasının saf Python uygulamasıdır.
referans: https://www.geeksforgeeks.org/optimal-file-merge-patterns/

Doctest'leri çalıştırmak için şu komutu kullanın:
python3 -m doctest -v greedy_merge_sort.py

Amaç
Farklı uzunluklardaki sıralanmış dosyaları tek bir sıralanmış dosyada birleştirin.
Sonuç dosyasının minimum sürede oluşturulacağı optimal bir çözüm bulmamız gerekiyor.

Yaklaşım
Sıralanmış dosyaların sayısı verilirse, bunları tek bir sıralanmış dosyada birleştirmenin birçok yolu vardır.
Bu birleştirme çiftler halinde yapılabilir.
Bir m-kayıt dosyasını ve bir n-kayıt dosyasını birleştirmek muhtemelen m+n kayıt hareketi gerektirir.
Optimal seçim, her adımda en küçük iki dosyayı birleştirmektir (açgözlü yaklaşım).
"""


def optimal_birlestirme_deseni(dosyalar: list) -> float:
    """Tüm dosyaları optimum maliyetle birleştirme fonksiyonu

    Argümanlar:
        dosyalar [list]: Birleştirilecek farklı dosyaların boyutlarının listesi

    Dönüş:
        optimal_birlestirme_maliyeti [int]: Tüm bu dosyaları birleştirmek için optimal maliyet

    Örnekler:
    >>> optimal_birlestirme_deseni([2, 3, 4])
    14
    >>> optimal_birlestirme_deseni([5, 10, 20, 30, 30])
    205
    >>> optimal_birlestirme_deseni([8, 8, 8, 8, 8])
    96
    """
    optimal_birlestirme_maliyeti = 0
    while len(dosyalar) > 1:
        temp = 0
        # Birleştirilecek minimum maliyetli iki dosyayı düşünün
        for _ in range(2):
            min_index = dosyalar.index(min(dosyalar))
            temp += dosyalar[min_index]
            dosyalar.pop(min_index)
        dosyalar.append(temp)
        optimal_birlestirme_maliyeti += temp
    return optimal_birlestirme_maliyeti


if __name__ == "__main__":
    import doctest

    doctest.testmod()
