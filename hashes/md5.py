"""
MD5 algoritması, veri bozulmasını tespit etmek için yaygın olarak kullanılan bir hash fonksiyonudur. Algoritma, verilen mesajı 512 bitlik bloklar halinde işleyerek çalışır ve gerektiğinde mesajı doldurur. Blokları kullanarak 128 bitlik bir durumu işletir ve toplamda 64 işlem gerçekleştirir. Tüm değerlerin little-endian olduğunu unutmayın, bu nedenle girişler gerektiği gibi dönüştürülür.

MD5 geçmişte kriptografik bir hash fonksiyonu olarak kullanılmış olsa da, artık kırıldığı için güvenlik amaçlı kullanılmamalıdır.

Daha fazla bilgi için bkz. https://en.wikipedia.org/wiki/MD5
"""

from collections.abc import Generator
from math import sin


def little_endian_donustur(string_32: bytes) -> bytes:
    """
    Verilen stringi 8 karakterlik gruplar halinde little-endian'a dönüştürür.

    Argümanlar:
        string_32 {[string]} -- [32 karakterlik string]

    Hatalar:
        ValueError -- [giriş 32 karakter değilse]

    Döndürür:
        32 karakterlik little-endian string
    >>> little_endian_donustur(b'1234567890abcdfghijklmnopqrstuvw')
    b'pqrstuvwhijklmno90abcdfg12345678'
    >>> little_endian_donustur(b'1234567890')
    Traceback (most recent call last):
    ...
    ValueError: Giriş uzunluğu 32 olmalıdır
    """
    if len(string_32) != 32:
        raise ValueError("Giriş uzunluğu 32 olmalıdır")

    little_endian = b""
    for i in [3, 2, 1, 0]:
        little_endian += string_32[8 * i : 8 * i + 8]
    return little_endian


def hex_formatla(i: int) -> bytes:
    """
    Verilen negatif olmayan tam sayıyı hex stringine dönüştürür.

    Örnek: Girişin aşağıdaki gibi olduğunu varsayalım:
        i = 1234

        Giriş hex olarak 0x000004d2'dir, bu nedenle little-endian hex stringi
        "d2040000" olur.

    Argümanlar:
        i {[int]} -- [tam sayı]

    Hatalar:
        ValueError -- [giriş negatifse]

    Döndürür:
        8 karakterlik little-endian hex stringi

    >>> hex_formatla(1234)
    b'd2040000'
    >>> hex_formatla(666)
    b'9a020000'
    >>> hex_formatla(0)
    b'00000000'
    >>> hex_formatla(1234567890)
    b'd2029649'
    >>> hex_formatla(1234567890987654321)
    b'b11c6cb1'
    >>> hex_formatla(-1)
    Traceback (most recent call last):
    ...
    ValueError: Giriş negatif olmamalıdır
    """
    if i < 0:
        raise ValueError("Giriş negatif olmamalıdır")

    hex_rep = format(i, "08x")[-8:]
    little_endian_hex = b""
    for j in [3, 2, 1, 0]:
        little_endian_hex += hex_rep[2 * j : 2 * j + 2].encode("utf-8")
    return little_endian_hex


def on_isleme(message: bytes) -> bytes:
    """
    Mesaj stringini ön işler:
    - Mesajı bit stringine dönüştür
    - Bit stringini 512 karakterin katları olacak şekilde doldur:
        - Bir 1 ekle
        - Uzunluk = 448 (mod 512) olana kadar 0 ekle
        - Orijinal mesajın uzunluğunu ekle (64 karakter)

    Örnek: Girişin aşağıdaki gibi olduğunu varsayalım:
        message = "a"

        Mesaj bit stringi "01100001"dir, bu 8 bit uzunluğundadır. Bu nedenle,
        bit stringinin 439 bit dolguya ihtiyacı vardır, böylece
        (bit_string + "1" + dolgu) = 448 (mod 512) olur.
        Mesaj uzunluğu 64 bit little-endian ikili olarak "000010000...0"dır.
        Birleştirilmiş bit stringi daha sonra 512 bit uzunluğundadır.

    Argümanlar:
        message {[string]} -- [mesaj stringi]

    Döndürür:
        512 karakterin katları olacak şekilde doldurulmuş bit stringi

    >>> on_isleme(b"a") == (b"01100001" + b"1" +
    ...                     (b"0" * 439) + b"00001000" + (b"0" * 56))
    True
    >>> on_isleme(b"") == b"1" + (b"0" * 447) + (b"0" * 64)
    True
    """
    bit_string = b""
    for char in message:
        bit_string += format(char, "08b").encode("utf-8")
    start_len = format(len(bit_string), "064b").encode("utf-8")

    # Bit stringini 512 karakterin katları olacak şekilde doldur
    bit_string += b"1"
    while len(bit_string) % 512 != 448:
        bit_string += b"0"
    bit_string += little_endian_donustur(start_len[32:]) + little_endian_donustur(start_len[:32])

    return bit_string


def blok_kelime_al(bit_string: bytes) -> Generator[list[int], None, None]:
    """
    Bit stringini 512 karakterlik bloklara böler ve her bloğu 32 bitlik kelimeler
    listesi olarak döndürür.

    Örnek: Girişin aşağıdaki gibi olduğunu varsayalım:
        bit_string =
            "000000000...0" +  # 0x00 (32 bit, sağa doldurulmuş)
            "000000010...0" +  # 0x01 (32 bit, sağa doldurulmuş)
            "000000100...0" +  # 0x02 (32 bit, sağa doldurulmuş)
            "000000110...0" +  # 0x03 (32 bit, sağa doldurulmuş)
            ...
            "000011110...0"    # 0x0a (32 bit, sağa doldurulmuş)

        O zaman len(bit_string) == 512, bu nedenle 1 blok olacaktır. Blok,
        32 bitlik kelimelere bölünür ve her kelime little-endian olarak
        dönüştürülür. İlk kelime ondalık olarak 0, ikinci kelime ondalık olarak
        1 vb. olarak yorumlanır.

        Bu nedenle, blok_kelime == [[0, 1, 2, 3, ..., 15]] olur.

    Argümanlar:
        bit_string {[string]} -- [uzunluğu 512'nin katları olan bit stringi]

    Hatalar:
        ValueError -- [bit stringinin uzunluğu 512'nin katları değilse]

    Döndürür:
        16 adet 32 bitlik kelime listesi

    >>> test_string = ("".join(format(n << 24, "032b") for n in range(16))
    ...                  .encode("utf-8"))
    >>> list(blok_kelime_al(test_string))
    [[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]]
    >>> list(blok_kelime_al(test_string * 4)) == [list(range(16))] * 4
    True
    >>> list(blok_kelime_al(b"1" * 512)) == [[4294967295] * 16]
    True
    >>> list(blok_kelime_al(b""))
    []
    >>> list(blok_kelime_al(b"1111"))
    Traceback (most recent call last):
    ...
    ValueError: Giriş uzunluğu 512'nin katları olmalıdır
    """
    if len(bit_string) % 512 != 0:
        raise ValueError("Giriş uzunluğu 512'nin katları olmalıdır")

    for pos in range(0, len(bit_string), 512):
        block = bit_string[pos : pos + 512]
        block_words = []
        for i in range(0, 512, 32):
            block_words.append(int(little_endian_donustur(block[i : i + 32]), 2))
        yield block_words


def not_32(i: int) -> int:
    """
    Verilen tam sayıya bitwise NOT uygular.

    Argümanlar:
        i {[int]} -- [verilen tam sayı]

    Hatalar:
        ValueError -- [giriş negatifse]

    Döndürür:
        i'ye bitwise NOT uygulanmış hali

    >>> not_32(34)
    4294967261
    >>> not_32(1234)
    4294966061
    >>> not_32(4294966061)
    1234
    >>> not_32(0)
    4294967295
    >>> not_32(1)
    4294967294
    >>> not_32(-1)
    Traceback (most recent call last):
    ...
    ValueError: Giriş negatif olmamalıdır
    """
    if i < 0:
        raise ValueError("Giriş negatif olmamalıdır")

    i_str = format(i, "032b")
    new_str = ""
    for c in i_str:
        new_str += "1" if c == "0" else "0"
    return int(new_str, 2)


def toplam_32(a: int, b: int) -> int:
    """
    İki sayıyı 32 bitlik tam sayılar olarak toplar.

    Argümanlar:
        a {[int]} -- [ilk verilen tam sayı]
        b {[int]} -- [ikinci verilen tam sayı]

    Döndürür:
        (a + b) 32 bitlik işaretsiz tam sayı olarak

    >>> toplam_32(1, 1)
    2
    >>> toplam_32(2, 3)
    5
    >>> toplam_32(0, 0)
    0
    >>> toplam_32(-1, -1)
    4294967294
    >>> toplam_32(4294967295, 1)
    0
    """
    return (a + b) % 2**32


def sola_dondur_32(i: int, shift: int) -> int:
    """
    Verilen tam sayının bitlerini verilen miktarda sola döndürür.

    Argümanlar:
        i {[int]} -- [verilen tam sayı]
        shift {[int]} -- [döndürme miktarı]

    Hatalar:
        ValueError -- [verilen tam sayı veya döndürme miktarı negatifse]

    Döndürür:
        `i`'yi `shift` bit kadar sola döndürülmüş hali

    >>> sola_dondur_32(1234, 1)
    2468
    >>> sola_dondur_32(1111, 4)
    17776
    >>> sola_dondur_32(2147483648, 1)
    1
    >>> sola_dondur_32(2147483648, 3)
    4
    >>> sola_dondur_32(4294967295, 4)
    4294967295
    >>> sola_dondur_32(1234, 0)
    1234
    >>> sola_dondur_32(0, 0)
    0
    >>> sola_dondur_32(-1, 0)
    Traceback (most recent call last):
    ...
    ValueError: Giriş negatif olmamalıdır
    >>> sola_dondur_32(0, -1)
    Traceback (most recent call last):
    ...
    ValueError: Döndürme miktarı negatif olmamalıdır
    """
    if i < 0:
        raise ValueError("Giriş negatif olmamalıdır")
    if shift < 0:
        raise ValueError("Döndürme miktarı negatif olmamalıdır")
    return ((i << shift) ^ (i >> (32 - shift))) % 2**32


def md5_hesapla(message: bytes) -> bytes:
    """
    Verilen mesajın 32 karakterlik MD5 hash'ini döndürür.

    Referans: https://en.wikipedia.org/wiki/MD5#Algorithm

    Argümanlar:
        message {[string]} -- [mesaj]

    Döndürür:
        32 karakterlik MD5 hash stringi

    >>> md5_hesapla(b"")
    b'd41d8cd98f00b204e9800998ecf8427e'
    >>> md5_hesapla(b"The quick brown fox jumps over the lazy dog")
    b'9e107d9d372bb6826bd81d3542a419d6'
    >>> md5_hesapla(b"The quick brown fox jumps over the lazy dog.")
    b'e4d909c290d0fb1ca068ffaddf22cbd0'

    >>> import hashlib
    >>> from string import ascii_letters
    >>> msgs = [b"", ascii_letters.encode("utf-8"), "Üñîçø∂é".encode("utf-8"),
    ...         b"The quick brown fox jumps over the lazy dog."]
    >>> all(md5_hesapla(msg) == hashlib.md5(msg).hexdigest().encode("utf-8") for msg in msgs)
    True
    """

    # Bit stringine dönüştür, dolgu ekle ve mesaj uzunluğunu ekle
    bit_string = on_isleme(message)

    eklenen_sabitler = [int(2**32 * abs(sin(i + 1))) for i in range(64)]

    # Başlangıç durumları
    a0 = 0x67452301
    b0 = 0xEFCDAB89
    c0 = 0x98BADCFE
    d0 = 0x10325476

    donus_miktarlari = [
        7,
        12,
        17,
        22,
        7,
        12,
        17,
        22,
        7,
        12,
        17,
        22,
        7,
        12,
        17,
        22,
        5,
        9,
        14,
        20,
        5,
        9,
        14,
        20,
        5,
        9,
        14,
        20,
        5,
        9,
        14,
        20,
        4,
        11,
        16,
        23,
        4,
        11,
        16,
        23,
        4,
        11,
        16,
        23,
        4,
        11,
        16,
        23,
        6,
        10,
        15,
        21,
        6,
        10,
        15,
        21,
        6,
        10,
        15,
        21,
        6,
        10,
        15,
        21,
    ]

    # Bit stringini bloklar halinde işleyin, her biri 16 32 karakterlik kelime içerir
    for block_words in blok_kelime_al(bit_string):
        a = a0
        b = b0
        c = c0
        d = d0

        # Mevcut bloğu hashle
        for i in range(64):
            if i <= 15:
                # f = (b & c) | (not_32(b) & d)     # f için alternatif tanım
                f = d ^ (b & (c ^ d))
                g = i
            elif i <= 31:
                # f = (d & b) | (not_32(d) & c)     # f için alternatif tanım
                f = c ^ (d & (b ^ c))
                g = (5 * i + 1) % 16
            elif i <= 47:
                f = b ^ c ^ d
                g = (3 * i + 5) % 16
            else:
                f = c ^ (b | not_32(d))
                g = (7 * i) % 16
            f = (f + a + eklenen_sabitler[i] + block_words[g]) % 2**32
            a = d
            d = c
            c = b
            b = toplam_32(b, sola_dondur_32(f, donus_miktarlari[i]))

        # Hashlenmiş bloğu toplam değere ekle
        a0 = toplam_32(a0, a)
        b0 = toplam_32(b0, b)
        c0 = toplam_32(c0, c)
        d0 = toplam_32(d0, d)

    digest = hex_formatla(a0) + hex_formatla(b0) + hex_formatla(c0) + hex_formatla(d0)
    return digest


if __name__ == "__main__":
    import doctest

    doctest.testmod()
