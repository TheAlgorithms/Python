"""
Fletcher checksum, 1970'lerin sonlarında Lawrence Livermore Labs'da John G. Fletcher (1934-2012) tarafından geliştirilen,
konuma bağlı bir checksum hesaplama algoritmasıdır.[1] Fletcher checksum'un amacı, döngüsel artıklık kontrolüne yaklaşan
hata tespit özellikleri sağlamak, ancak toplama teknikleriyle ilişkili daha düşük hesaplama çabasıyla bunu başarmaktır.

Kaynak: https://en.wikipedia.org/wiki/Fletcher%27s_checksum
"""


def fletcher16(metin: str) -> int:
    """
    Verideki her karakteri döngüyle gez ve iki toplamaya ekle.

    >>> fletcher16('hello world')
    6752
    >>> fletcher16('onethousandfourhundredthirtyfour')
    28347
    >>> fletcher16('The quick brown fox jumps over the lazy dog.')
    5655
    """
    veri = bytes(metin, "ascii")
    toplam1 = 0
    toplam2 = 0
    for karakter in veri:
        toplam1 = (toplam1 + karakter) % 255
        toplam2 = (toplam1 + toplam2) % 255
    return (toplam2 << 8) | toplam1


if __name__ == "__main__":
    import doctest

    doctest.testmod()
