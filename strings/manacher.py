def palindromik_dizi(girdi_dizisi: str) -> str:
    """

    Organiser: K. Umut Araz

    >>> palindromik_dizi('abbbaba')
    'abbba'
    >>> palindromik_dizi('ababa')
    'ababa'

    Manacher algoritması, en uzun palindromik alt diziyi lineer zamanda bulur.

    1. İlk olarak girdi_dizisi("xyx") yeni_diziye("x|y|x") dönüştürülür; burada
       tek pozisyonlar gerçek girdi karakterleridir.
    2. Yeni dizideki her karakter için karşılık gelen uzunluğu bulur ve
       uzunluğu saklar, ayrıca daha önce hesaplanan bilgileri saklamak için
       sol ve sağ değerlerini günceller.
       (detaylar için açıklamaya bakınız)

    3. Tüm "|" karakterlerini kaldırarak karşılık gelen çıktı dizisini döndürür.
    """
    max_uzunluk = 0

    # Eğer girdi_dizisi "aba" ise yeni_dizi "a|b|a" olur
    yeni_dizi = ""
    cikti_dizisi = ""

    # yeni_diziye her karakteri + "|" ekle
    for i in girdi_dizisi[: len(girdi_dizisi) - 1]:
        yeni_dizi += i + "|"
    # son karakteri ekle
    yeni_dizi += girdi_dizisi[-1]

    # Önceki en uzak palindromik alt dizinin başlangıç ve bitişini saklayacağız
    sol, sag = 0, 0

    # length[i] i merkezli palindromik alt dizinin uzunluğunu gösterir
    uzunluk = [1 for i in range(len(yeni_dizi))]

    # yeni_dizideki her karakter için karşılık gelen palindromik diziyi bul
    baslangic = 0
    for j in range(len(yeni_dizi)):
        k = 1 if j > sag else min(uzunluk[sol + sag - j] // 2, sag - j + 1)
        while (
            j - k >= 0
            and j + k < len(yeni_dizi)
            and yeni_dizi[k + j] == yeni_dizi[j - k]
        ):
            k += 1

        uzunluk[j] = 2 * k - 1

        # Bu dizinin daha önce keşfedilen sonun (yani sag) sonrasında mı bitiyor?
        # Eğer evet ise, yeni sag'ı bu dizinin son indeksine güncelle
        if j + k - 1 > sag:
            sol = j - k + 1
            sag = j + k - 1

        # max_uzunluk ve başlangıç pozisyonunu güncelle
        if max_uzunluk < uzunluk[j]:
            max_uzunluk = uzunluk[j]
            baslangic = j

    # o diziyi oluştur
    s = yeni_dizi[baslangic - max_uzunluk // 2 : baslangic + max_uzunluk // 2 + 1]
    for i in s:
        if i != "|":
            cikti_dizisi += i

    return cikti_dizisi


if __name__ == "__main__":
    import doctest

    doctest.testmod()

"""
...a0...a1...a2.....a3......a4...a5...a6....

En uzun palindromik alt diziyi hesapladığımız dizi yukarıda gösterilmiştir; burada ... bazı karakterlerdir ve şu anda a5 merkezli palindromik alt dizinin uzunluğunu hesaplıyoruz. 
i) a3 merkezli palindromik alt dizinin uzunluğunu sakladık (sol'dan başlar, sağ'da biter) ve bu, şimdiye kadar en uzak bitiştir ve a6'dan sonra bitmektedir.
ii) a2 ve a4, a3'e eşit uzaklıktadır, bu nedenle char(a2) == char(a4)
iii) a0 ve a6, a3'e eşit uzaklıktadır, bu nedenle char(a0) == char(a6)
iv) a1, a3 merkezli palindromedeki a5'in karşılık gelen eşit karakteridir (a4==a6 türevinde hatırlayın)

Şimdi a5 için a5 merkezli palindromik alt dizinin uzunluğunu hesaplayacağız, ancak daha önce hesaplanan bilgileri bir şekilde kullanabilir miyiz?
Evet, yukarıdaki dizide a5'in a3 merkezli palindromun içinde olduğunu biliyoruz ve daha önce hesapladık ki
a0==a2 (a1 merkezli palindrom)
a2==a4 (a3 merkezli palindrom)
a0==a6 (a3 merkezli palindrom)
bu nedenle a4==a6

Bu durumda, a5 merkezli palindromun en az a1 merkezli palindrom kadar uzun olduğunu söyleyebiliriz, ancak bu yalnızca a0 ve a6'nın a3 merkezli palindromun sınırları içinde olması durumunda geçerlidir.
Sonuç olarak ..

len_of_palindrome__at(a5) = min(len_of_palindrome_at(a1), sag-a5)
burada a3 sol'dan sağ'a uzanır ve bunu sürekli güncellememiz gerekir.

Eğer a5 sol ve sağ sınırın dışındaysa, palindromun uzunluğunu brute force ile hesaplarız ve sol, sağ'ı güncelleriz.

Bu, z-fonksiyonu gibi lineer zaman karmaşıklığı sağlar.
"""
