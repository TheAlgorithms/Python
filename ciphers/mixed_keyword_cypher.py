from string import ascii_uppercase


def karışık_anahtar(
    anahtar: str, düz_metin: str, ayrıntılı: bool = False, alfabe: str = ascii_uppercase
) -> str:
    """
    Anahtar: merhaba

    H E L O
    A B C D
    F G I J
    K M N P
    Q R S T
    U V W X
    Y Z
    ve dikey olarak eşleştir

    Organiser: K. Umut Araz

    >>> karışık_anahtar("kolej", "ÜNİVERSİTE", True)  # doctest: +NORMALIZE_WHITESPACE
    {'A': 'K', 'B': 'O', 'C': 'L', 'D': 'E', 'E': 'J', 'F': 'D', 'G': 'G', 'H': 'I',
     'I': 'N', 'J': 'R', 'K': 'S', 'L': 'T', 'M': 'U', 'N': 'Y', 'O': 'Z', 'P': 'A',
     'Q': 'B', 'R': 'C', 'S': 'F', 'T': 'H', 'U': 'M', 'V': 'P', 'W': 'Q', 'X': 'V',
     'Y': 'W', 'Z': 'X'}
    'XKJGUFMJST'

    >>> karışık_anahtar("kolej", "ÜNİVERSİTE", False)  # doctest: +NORMALIZE_WHITESPACE
    'XKJGUFMJST'
    """
    anahtar = anahtar.upper()
    düz_metin = düz_metin.upper()
    alfabe_set = set(alfabe)

    # Anahtardaki benzersiz karakterlerin bir listesini oluştur - sıraları önemlidir
    # Bu, düz metin karakterlerini şifreli metin karakterlerine nasıl eşleştireceğimizi belirler
    benzersiz_karakterler = []
    for char in anahtar:
        if char in alfabe_set and char not in benzersiz_karakterler:
            benzersiz_karakterler.append(char)
    # Bu benzersiz karakterlerin sayısı, satır sayısını belirleyecektir
    benzersiz_karakter_sayısı = len(benzersiz_karakterler)

    # Alfabenin kaydırılmış bir versiyonunu oluştur
    kaydırılmış_alfabe = benzersiz_karakterler + [
        char for char in alfabe if char not in benzersiz_karakterler
    ]

    # Kaydırılmış alfabenin satırlara bölünmesiyle değiştirilmiş bir alfabe oluştur
    değiştirilmiş_alfabe = [
        kaydırılmış_alfabe[k : k + benzersiz_karakter_sayısı]
        for k in range(0, 26, benzersiz_karakter_sayısı)
    ]

    # Alfabe karakterlerini değiştirilmiş alfabe karakterlerine eşle
    # Değiştirilmiş alfabede 'dikey' olarak ilerleyerek - önce sütunları düşün
    eşleme = {}
    harf_indeksi = 0
    for sütun in range(benzersiz_karakter_sayısı):
        for satır in değiştirilmiş_alfabe:
            # Eğer mevcut satır (sonuncusu) çok kısa ise döngüden çık
            if len(satır) <= sütun:
                break

            # Mevcut harfi değiştirilmiş alfabedeki harfe eşle
            eşleme[alfabe[harf_indeksi]] = satır[sütun]
            harf_indeksi += 1

    if ayrıntılı:
        print(eşleme)
    # Düz metni değiştirilmiş alfabeye eşleyerek şifreli metni oluştur
    return "".join(eşleme.get(char, char) for char in düz_metin)


if __name__ == "__main__":
    # örnek kullanım
    print(karışık_anahtar("kolej", "ÜNİVERSİTE"))
