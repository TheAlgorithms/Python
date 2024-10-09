"""
Adler-32, Mark Adler tarafından 1995 yılında icat edilen bir sağlama algoritmasıdır.
Aynı uzunluktaki döngüsel artıklık kontrolüne kıyasla, güvenilirlikten ziyade hızı tercih eder.
Adler-32, Fletcher-16'dan daha güvenilirdir ve Fletcher-32'den biraz daha az güvenilirdir.[2]

kaynak: https://en.wikipedia.org/wiki/Adler-32
"""

MOD_ADLER = 65521


def adler32(metin: str) -> int:
    """
    Adler-32 hash fonksiyonunu uygular.
    Her karakter için yeni bir değer hesaplar ve iterasyon yapar

    >>> adler32('Algoritmalar')
    363791387

    >>> adler32('hepsini adlerle')
    708642122
    """
    a = 1
    b = 0
    for karakter in metin:
        a = (a + ord(karakter)) % MOD_ADLER
        b = (b + a) % MOD_ADLER
    return (b << 16) | a
