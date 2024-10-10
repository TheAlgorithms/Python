def metin_hizalama(kelime: str, max_genislik: int) -> list:
    """

    Organiser: K. Umut Araz

    Verilen metni, her satırın tam olarak (max_genislik) karaktere sahip olacak şekilde
    (sol ve sağ) hizalanmış olarak formatlar ve hizalanmış metin listesini döndürür.

    Örnek 1:
    metin = "Bu bir metin hizalama örneğidir."
    max_genislik = 16

    çıktı = ['Bu    bir    metin',
             'hizalama örneğidir.']

    >>> metin_hizalama("Bu bir metin hizalama örneğidir.", 16)
    ['Bu    bir    metin', 'hizalama örneğidir.']

    Örnek 2:
    metin = "İki yol sarı bir ormanda ayrıldı"
    max_genislik = 16
    çıktı = ['İki        yol',
             'sarı bir   ormanda',
             'ayrıldı       ']

    >>> metin_hizalama("İki yol sarı bir ormanda ayrıldı", 16)
    ['İki        yol', 'sarı bir   ormanda', 'ayrıldı       ']

    Zaman karmaşıklığı: O(m*n)
    Alan karmaşıklığı: O(m*n)
    """

    # Metni boşluklara göre bölerek kelimeler listesine çevirme
    kelimeler = kelime.split()

    def hizala(satir: list, genislik: int, max_genislik: int) -> str:
        toplam_bosluk_sayisi = max_genislik - genislik
        kelime_sayisi = len(satir)
        if len(satir) == 1:
            # Eğer satırda sadece bir kelime varsa
            # satırın geri kalanına toplam_bosluk_sayisi kadar boşluk ekle
            return satir[0] + " " * toplam_bosluk_sayisi
        else:
            bosluk_eklenecek_kelime_sayisi = kelime_sayisi - 1
            # bosluk_sayisi_listesi[i] : satir[i] kelimesinden sonra
            # bosluk_sayisi_listesi[i] kadar boşluk ekle
            bosluk_sayisi_listesi = bosluk_eklenecek_kelime_sayisi * [
                toplam_bosluk_sayisi // bosluk_eklenecek_kelime_sayisi
            ]
            bosluk_sayisi_yerleri = (
                toplam_bosluk_sayisi % bosluk_eklenecek_kelime_sayisi
            )
            # Boşlukları soldaki kelimelere dağıt
            for i in range(bosluk_sayisi_yerleri):
                bosluk_sayisi_listesi[i] += 1
            hizalanmis_kelime_listesi = []
            for i in range(bosluk_eklenecek_kelime_sayisi):
                # Kelimeyi ekle
                hizalanmis_kelime_listesi.append(satir[i])
                # Eklenmesi gereken boşlukları ekle
                hizalanmis_kelime_listesi.append(bosluk_sayisi_listesi[i] * " ")
            # Son kelimeyi cümleye ekle
            hizalanmis_kelime_listesi.append(satir[-1])
            # Hizalanmış kelime listesini birleştirerek hizalanmış bir satır oluştur
            return "".join(hizalanmis_kelime_listesi)

    cevap = []
    satir: list[str] = []
    genislik = 0
    for ic_kelime in kelimeler:
        if genislik + len(ic_kelime) + len(satir) <= max_genislik:
            # max_genislik'i doldurana kadar kelimeleri eklemeye devam et
            satir.append(ic_kelime)
            genislik += len(ic_kelime)
        else:
            # Satırı hizala ve sonucu ekle
            cevap.append(hizala(satir, genislik, max_genislik))
            # Yeni satır ve yeni genişliği sıfırla
            satir, genislik = [ic_kelime], len(ic_kelime)
    kalan_bosluklar = max_genislik - genislik - len(satir)
    cevap.append(" ".join(satir) + (kalan_bosluklar + 1) * " ")
    return cevap


if __name__ == "__main__":
    from doctest import testmod

    testmod()
