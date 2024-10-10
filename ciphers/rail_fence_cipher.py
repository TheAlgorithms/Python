"""https://tr.wikipedia.org/wiki/Raylı_çit_şifreleme"""

#Organiser: K. Umut Araz



def sifrele(girdi: str, anahtar: int) -> str:
    """
    Bir dizi karakteri, her birini bir ızgaraya yerleştirerek
    (yükseklik anahtara bağlıdır) zigzag formasyonunda karıştırır
    ve soldan sağa okur.

    >>> sifrele("Merhaba Dünya", 4)
    'Mra uahbDny'

    >>> sifrele("Bu bir mesajdır", 0)
    Traceback (most recent call last):
        ...
    ValueError: Izgaranın yüksekliği 0 veya negatif olamaz

    >>> sifrele(b"Bu bir bayt dizisidir", 5)
    Traceback (most recent call last):
        ...
    TypeError: dizi öğesi 0: str örneği bekleniyordu, int bulundu
    """
    temp_izgara: list[list[str]] = [[] for _ in range(anahtar)]
    en_dusuk = anahtar - 1

    if anahtar <= 0:
        raise ValueError("Izgaranın yüksekliği 0 veya negatif olamaz")
    if anahtar == 1 or len(girdi) <= anahtar:
        return girdi

    for konum, karakter in enumerate(girdi):
        num = konum % (en_dusuk * 2)  # sınırları belirler
        num = min(num, en_dusuk * 2 - num)  # zigzag deseni oluşturur
        temp_izgara[num].append(karakter)
    izgara = ["".join(satir) for satir in temp_izgara]
    cikti = "".join(izgara)

    return cikti


def cozul(girdi: str, anahtar: int) -> str:
    """
    Anahtara dayalı bir şablon oluşturur ve bunu
    girdi dizisinin karakterleriyle doldurur ve ardından
    zigzag formasyonunda okur.

    >>> cozul("Mra uahbDny", 4)
    'Merhaba Dünya'

    >>> cozul("Bu bir mesajdır", -10)
    Traceback (most recent call last):
        ...
    ValueError: Izgaranın yüksekliği 0 veya negatif olamaz

    >>> cozul("Anahtarım çok büyük", 100)
    'Anahtarım çok büyük'
    """
    izgara = []
    en_dusuk = anahtar - 1

    if anahtar <= 0:
        raise ValueError("Izgaranın yüksekliği 0 veya negatif olamaz")
    if anahtar == 1:
        return girdi

    temp_izgara: list[list[str]] = [[] for _ in range(anahtar)]  # şablon oluşturur
    for konum in range(len(girdi)):
        num = konum % (en_dusuk * 2)  # sınırları belirler
        num = min(num, en_dusuk * 2 - num)  # zigzag deseni oluşturur
        temp_izgara[num].append("*")

    sayac = 0
    for satir in temp_izgara:  # karakterleri doldurur
        parca = girdi[sayac : sayac + len(satir)]
        izgara.append(list(parca))
        sayac += len(satir)

    cikti = ""  # zigzag olarak okur
    for konum in range(len(girdi)):
        num = konum % (en_dusuk * 2)  # sınırları belirler
        num = min(num, en_dusuk * 2 - num)  # zigzag deseni oluşturur
        cikti += izgara[num][0]
        izgara[num].pop(0)
    return cikti


def brute_force(girdi: str) -> dict[int, str]:
    """Her anahtarı tahmin ederek çözme fonksiyonunu kullanır

    >>> brute_force("Mra uahbDny")[4]
    'Merhaba Dünya'
    """
    sonuclar = {}
    for anahtar_tahmin in range(1, len(girdi)):  # her anahtarı dener
        sonuclar[anahtar_tahmin] = cozul(girdi, anahtar_tahmin)
    return sonuclar


if __name__ == "__main__":
    import doctest

    doctest.testmod()
