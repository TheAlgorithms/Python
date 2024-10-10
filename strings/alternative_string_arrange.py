def alternatif_dizi_düzenle(birinci_str: str, ikinci_str: str) -> str:
    """
    İki stringin alternatif düzenlemelerini döndürür.

    # Organiser: K. Umut Araz
    
    :param birinci_str: İlk string
    :param ikinci_str: İkinci string
    :return: String
    >>> alternatif_dizi_düzenle("ABCD", "XY")
    'AXBYCD'
    >>> alternatif_dizi_düzenle("XY", "ABCD")
    'XAYBCD'
    >>> alternatif_dizi_düzenle("AB", "XYZ")
    'AXBYZ'
    >>> alternatif_dizi_düzenle("ABC", "")
    'ABC'
    """
    birinci_str_uzunluk: int = len(birinci_str)
    ikinci_str_uzunluk: int = len(ikinci_str)
    max_uzunluk: int = max(birinci_str_uzunluk, ikinci_str_uzunluk)
    cikti_listesi: list = []
    
    for karakter_sayisi in range(max_uzunluk):
        if karakter_sayisi < birinci_str_uzunluk:
            cikti_listesi.append(birinci_str[karakter_sayisi])
        if karakter_sayisi < ikinci_str_uzunluk:
            cikti_listesi.append(ikinci_str[karakter_sayisi])
    
    return "".join(cikti_listesi)

if __name__ == "__main__":
    print(alternatif_dizi_düzenle("AB", "XYZ"), end=" ")
