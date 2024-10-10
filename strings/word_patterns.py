def kelime_dizilimi(kelime: str) -> str:
    """
    # Düzenleyen: K. Umut Araz, 10/10/2024
    
    Verilen kelimedeki karakterlerin görünüm sırasını sayısal olarak döndürür.
    >>> kelime_dizilimi("")
    ''
    >>> kelime_dizilimi(" ")
    '0'
    >>> kelime_dizilimi("desen")
    '0.1.2.2.3'
    >>> kelime_dizilimi("kelime desen")
    '0.1.2.3.4.5.6.7.7.8.2.9'
    >>> kelime_dizilimi("get kelime desen")
    '0.1.2.3.4.5.6.7.3.8.9.2.2.1.6.10'
    >>> kelime_dizilimi()
    Traceback (most recent call last):
    ...
    TypeError: kelime_dizilimi() missing 1 required positional argument: 'kelime'
    >>> kelime_dizilimi(1)
    Traceback (most recent call last):
    ...
    AttributeError: 'int' object has no attribute 'upper'
    >>> kelime_dizilimi(1.1)
    Traceback (most recent call last):
    ...
    AttributeError: 'float' object has no attribute 'upper'
    >>> kelime_dizilimi([])
    Traceback (most recent call last):
    ...
    AttributeError: 'list' object has no attribute 'upper'
    """
    kelime = kelime.upper()
    sonraki_numara = 0
    harf_numaraları = {}
    kelime_dizisi = []

    for harf in kelime:
        if harf not in harf_numaraları:
            harf_numaraları[harf] = str(sonraki_numara)
            sonraki_numara += 1
        kelime_dizisi.append(harf_numaraları[harf])
    return ".".join(kelime_dizisi)


if __name__ == "__main__":
    import pprint
    import time

    baslangic_zamani = time.time()
    with open("dictionary.txt") as in_file:
        kelime_listesi = in_file.read().splitlines()

    tum_diziler: dict = {}
    for kelime in kelime_listesi:
        dizilim = kelime_dizilimi(kelime)
        if dizilim in tum_diziler:
            tum_diziler[dizilim].append(kelime)
        else:
            tum_diziler[dizilim] = [kelime]

    with open("kelime_dizilimleri.txt", "w") as out_file:
        out_file.write(pprint.pformat(tum_diziler))

    toplam_zaman = round(time.time() - baslangic_zamani, 2)
    print(f"Tamamlandı!  {len(tum_diziler):,} kelime dizilimi {toplam_zaman} saniyede bulundu.")
    # Tamamlandı!  9,581 kelime dizilimi 0.58 saniyede bulundu.
