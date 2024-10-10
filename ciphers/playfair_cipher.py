"""
https://tr.wikipedia.org/wiki/Playfair_cipher#Tanım

Playfair şifrelemesi, 1854 yılında Charles Wheatstone tarafından geliştirilmiştir.
Kullanımı Lord Playfair tarafından yoğun bir şekilde teşvik edilmiştir, bu nedenle ismi buradan gelmektedir.

Playfair şifrelemesinin bazı özellikleri şunlardır:

Organiser: K. Umut Araz

1) İlk harf diagramı yerine geçen şifreleme yöntemidir.
2) Manuel simetrik şifreleme tekniğidir.
3) Çoklu harf şifreleme yöntemidir.

Aşağıdaki kod, yalnızca alfabeleri şifreler.
Boşlukları, özel karakterleri ve sayıları koddan çıkarır.

Playfair, bilinen güvenlik açıkları ve otomatik şifreleme cihazlarının ortaya çıkması nedeniyle artık askeri güçler tarafından kullanılmamaktadır.
Bu şifreleme yöntemi, Birinci Dünya Savaşı'ndan önce güvenli olmayan bir yöntem olarak kabul edilmektedir.
"""

import itertools
import string
from collections.abc import Generator, Iterable


def chunker(seq: Iterable[str], size: int) -> Generator[tuple[str, ...], None, None]:
    it = iter(seq)
    while True:
        chunk = tuple(itertools.islice(it, size))
        if not chunk:
            return
        yield chunk


def prepare_input(dirty: str) -> str:
    """
    Düz metni büyük harfe çevirir
    ve tekrar eden harfleri X ile ayırır.
    """

    dirty = "".join([c.upper() for c in dirty if c in string.ascii_letters])
    clean = ""

    if len(dirty) < 2:
        return dirty

    for i in range(len(dirty) - 1):
        clean += dirty[i]

        if dirty[i] == dirty[i + 1]:
            clean += "X"

    clean += dirty[-1]

    if len(clean) % 2 != 0:
        clean += "X"

    return clean


def generate_table(key: str) -> list[str]:
    # I ve J harfleri birbirinin yerine kullanılmaktadır
    # böylece 5x5'lik bir tablo (25 harf) kullanabiliyoruz.
    alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
    # Tabloyu kurmak ve gerçek şifreleme/şifre çözme işlemlerini yapmak için
    # '2d' dizi yerine bir liste kullanıyoruz, bu matematiği basitleştiriyor.
    table = []

    # Anahtar karakterlerini tabloya kopyala, eğer `alphabet` içinde ve tekrar etmiyorsa ekle
    for char in key.upper():
        if char not in table and char in alphabet:
            table.append(char)

    # Tabloyu kalan alfabe karakterleriyle doldur
    for char in alphabet:
        if char not in table:
            table.append(char)

    return table


def encode(plaintext: str, key: str) -> str:
    """
    Verilen düz metni Playfair şifrelemesi ile şifreler.
    Düz metni ve anahtarı girdi olarak alır ve şifrelenmiş dizeyi döner.

    >>> encode("Merhaba", "ANAHTAR")
    'CFSUPM'
    >>> encode("sola saldır", "ACİL")
    'DQZSBYFSDZFMFNLOHFDRSG'
    >>> encode("Üzgünüm!", "ÖZEL")
    'AVXETX'
    >>> encode("Sayı 1", "SAYI")
    'UMBENF'
    >>> encode("Fotosentez!", "GÜNEŞ")
    'OEMHQHVCHESUKE'
    """

    table = generate_table(key)
    plaintext = prepare_input(plaintext)
    ciphertext = ""

    for char1, char2 in chunker(plaintext, 2):
        row1, col1 = divmod(table.index(char1), 5)
        row2, col2 = divmod(table.index(char2), 5)

        if row1 == row2:
            ciphertext += table[row1 * 5 + (col1 + 1) % 5]
            ciphertext += table[row2 * 5 + (col2 + 1) % 5]
        elif col1 == col2:
            ciphertext += table[((row1 + 1) % 5) * 5 + col1]
            ciphertext += table[((row2 + 1) % 5) * 5 + col2]
        else:  # dikdörtgen
            ciphertext += table[row1 * 5 + col2]
            ciphertext += table[row2 * 5 + col1]

    return ciphertext


def decode(ciphertext: str, key: str) -> str:
    """
    Verilen şifreli dizeyi sağlanan anahtar ile çözer.

    >>> decode("BMZFAZRZDH", "HAZARD")
    'FIREHAZARD'
    >>> decode("HNBWBPQT", "AUTOMOBILE")
    'DRIVINGX'
    >>> decode("SLYSSAQS", "CASTLE")
    'ATXTACKX'
    """

    table = generate_table(key)
    plaintext = ""

    for char1, char2 in chunker(ciphertext, 2):
        row1, col1 = divmod(table.index(char1), 5)
        row2, col2 = divmod(table.index(char2), 5)

        if row1 == row2:
            plaintext += table[row1 * 5 + (col1 - 1) % 5]
            plaintext += table[row2 * 5 + (col2 - 1) % 5]
        elif col1 == col2:
            plaintext += table[((row1 - 1) % 5) * 5 + col1]
            plaintext += table[((row2 - 1) % 5) * 5 + col2]
        else:  # dikdörtgen
            plaintext += table[row1 * 5 + col2]
            plaintext += table[row2 * 5 + col1]

    return plaintext


if __name__ == "__main__":
    import doctest

    doctest.testmod()

    print("Şifrelenmiş:", encode("HOŞÇAKAL VE TEŞEKKÜRLER", "SELAM"))
    print("Şifre Çözülmüş:", decode("CXRBANRLBALQ", "SELAM"))
