"""
https://cp-algorithms.com/string/prefix-function.html

Organiser: K. Umut Araz

Önek fonksiyonu Knuth-Morris-Pratt algoritmasıdır.

Knuth-Morris-Pratt desen bulma algoritmasından farklıdır.

Örneğin: Hem önek hem de sonek olan en uzun kısmı bulma.

Zaman Karmaşıklığı: O(n) - burada n, dizenin uzunluğudur.
"""


def prefix_function(girdi_dizesi: str) -> list:
    """
    Verilen dize için bu fonksiyon, her bir indeks (i) için,
    verilen alt dize (girdi_dizesi[0...i]) için önek ve sonek
    arasındaki en uzun örtüşmeyi temsil eden değeri hesaplar.

    İlk elemanın değeri için algoritma her zaman 0 döner.

    >>> prefix_function("aabcdaabc")
    [0, 1, 0, 0, 0, 1, 2, 3, 4]
    >>> prefix_function("asdasdad")
    [0, 0, 0, 1, 2, 3, 4, 0]
    """

    # Sonuç değerleri için liste
    onek_sonucu = [0] * len(girdi_dizesi)

    for i in range(1, len(girdi_dizesi)):
        # Daha iyi performans için son sonuçları kullan - dinamik programlama
        j = onek_sonucu[i - 1]
        while j > 0 and girdi_dizesi[i] != girdi_dizesi[j]:
            j = onek_sonucu[j - 1]

        if girdi_dizesi[i] == girdi_dizesi[j]:
            j += 1
        onek_sonucu[i] = j

    return onek_sonucu


def en_uzun_onek(girdi_dizesi: str) -> int:
    """
    Önek fonksiyonu kullanım durumu
    Hem önek hem de sonek olan en uzun kısmı bulma.

    >>> en_uzun_onek("aabcdaabc")
    4
    >>> en_uzun_onek("asdasdad")
    4
    >>> en_uzun_onek("abcab")
    2
    """

    # Dizinin maksimum değerini döndürmek bize yanıtı verir
    return max(prefix_function(girdi_dizesi))


if __name__ == "__main__":
    import doctest

    doctest.testmod()
