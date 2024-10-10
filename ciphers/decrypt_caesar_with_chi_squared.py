#!/usr/bin/env python3
from __future__ import annotations

"""
Organiser: K. Umut Araz
"""

def sezar_sifresini_coz(
    sifreli_metin: str,
    sifre_alfabesi: list[str] | None = None,
    frekans_sozlugu: dict[str, float] | None = None,
    durum_duyarliligi: bool = False,
) -> tuple[int, float, str]:
    """
    Temel Kullanım
    ==============
    Argümanlar:
    * sifreli_metin (str): çözülmesi gereken metin (sezar şifresi ile şifrelenmiş)

    Opsiyonel Argümanlar:
    * sifre_alfabesi (list): şifreleme için kullanılan alfabe (her harf bir
      string olarak virgülle ayrılmış)
    * frekans_sozlugu (dict): anahtarlar harfler ve değerler frekansın
      ondalık/float olarak yüzdelik temsilidir
    * durum_duyarliligi (bool): bir boolean değeri: eğer durum çözümleme sırasında
      önemliyse True, değilse False

    Döndürür:
    * Aşağıdaki biçimde bir tuple:
      (
        en_olasi_sifre,
        en_olasi_sifre_kare_degeri,
        cozulmus_en_olasi_sifre
      )

      burada...
      - en_olasi_sifre, en küçük kare istatistiğine sahip kaydırmayı temsil eden
        bir tam sayıdır (en olası anahtar)
      - en_olasi_sifre_kare_degeri, en olası kaydırmanın kare istatistiğini
        temsil eden bir float
      - cozulmus_en_olasi_sifre, en_olasi_sifre anahtarı ile çözülen
        şifrelenmiş metni içeren bir stringtir


    Kare İstatistiği Testi
    =======================

    Sezar Şifresi
    --------------
    Sezar şifresi, çok güvenli olmayan bir şifreleme algoritmasıdır, ancak
    Julius Caesar'dan beri kullanılmaktadır. Şifre, düz metindeki her karakterin
    belirli bir sayıda karakter kaydırılarak alfabenin bir karakteri ile
    değiştirildiği basit bir yer değiştirme şifresidir. Kaydırma veya anahtar
    olarak adlandırılan bu karakter sayısıdır. Örneğin:

    Düz metin: merhaba
    Anahtar: 1
    Şifreli metin: nfsbcib
    (merhaba'daki her harf, İngiliz alfabesinde bir sağa kaydırılmıştır)

    Bu durum, çok fazla güvenlik sağlamaz. Aslında, şifreli metni brute-force
    ile çözmek oldukça kolaydır. Ancak bunu yapmanın bir yolu kare istatistiği
    testidir.

    Kare İstatistiği Testi
    -----------------------
    İngiliz alfabesindeki her harfin bir frekansı vardır, yani diğer harflere
    kıyasla ne kadar sıklıkla göründüğüdür (genellikle yüzdelik olasılığı
    temsil eden bir ondalık olarak ifade edilir). İngilizce dilindeki en yaygın
    harf "e"dir ve frekansı 0.11162 veya %11.162'dir. Test şu şekilde
    gerçekleştirilir.

    1. Şifreli metin brute force yöntemiyle çözülür (26 olası kombinasyonun
       her biri)
    2. Her kombinasyon için, kombinasyondaki her harf için, harfin mesajda
       ortalama kaç kez görünmesi gerektiği, toplam karakter sayısı ile
       harfin frekansının çarpılmasıyla hesaplanır.

       Örneğin:
       100 karakterlik bir mesajda, "e" yaklaşık 11.162 kez görünmelidir.

    3. Daha sonra, hata payını (harfin GEREKİYOR olması gereken sayısı ile
       gerçekten görünen sayısı arasındaki farkı) hesaplamak için kare
       istatistiği testini kullanırız. Aşağıdaki formül kullanılır:

        n: harfin gerçekten kaç kez göründüğü
        p: harfin görünmesi gereken tahmin edilen değeri (bkz. #2)
        v: kare istatistiği test sonucu (burada kare istatistik değeri olarak
        adlandırılır)

        (n - p)^2
        --------- = v
           p

    4. Her harf için kare istatistik değeri toplanır. Toplam, o şifreleme anahtarı
       için kare istatistiğidir.
    5. En düşük kare istatistik değerine sahip şifreleme anahtarı, en olası
       çözüm olacaktır.

    Daha Fazla Okuma
    =================

    * http://practicalcryptography.com/cryptanalysis/text-characterisation/chi-squared-
        statistic/
    * https://en.wikipedia.org/wiki/Letter_frequency
    * https://en.wikipedia.org/wiki/Chi-squared_test
    * https://en.m.wikipedia.org/wiki/Caesar_cipher

    Doctestler
    ===========
    >>> sezar_sifresini_coz(
    ...    'dof pz aol jhlzhy jpwoly zv wvwbshy? pa pz avv lhzf av jyhjr!'
    ... )  # doctest: +NORMALIZE_WHITESPACE
    (7, 3129.228005747531,
     'neden sezar şifresi bu kadar popüler? çözmesi çok kolay!')

    >>> sezar_sifresini_coz('crybd cdbsxq')
    (10, 233.35343938980898, 'kısa dize')

    >>> sezar_sifresini_coz('Crybd Cdbsxq', durum_duyarliligi=True)
    (10, 233.35343938980898, 'Kısa Dize')

    >>> sezar_sifresini_coz(12)
    Traceback (most recent call last):
    AttributeError: 'int' nesnesinin 'lower' özelliği yok
    """
    alfabe_harfleri = sifre_alfabesi or [chr(i) for i in range(97, 123)]

    # Eğer argüman None ise veya kullanıcı boş bir sözlük sağladıysa
    if not frekans_sozlugu:
        # İngilizce dilindeki harflerin frekansları (ne kadar sıklıkla göründükleri)
        frekanslar = {
            "a": 0.08497,
            "b": 0.01492,
            "c": 0.02202,
            "d": 0.04253,
            "e": 0.11162,
            "f": 0.02228,
            "g": 0.02015,
            "h": 0.06094,
            "i": 0.07546,
            "j": 0.00153,
            "k": 0.01292,
            "l": 0.04025,
            "m": 0.02406,
            "n": 0.06749,
            "o": 0.07507,
            "p": 0.01929,
            "q": 0.00095,
            "r": 0.07587,
            "s": 0.06327,
            "t": 0.09356,
            "u": 0.02758,
            "v": 0.00978,
            "w": 0.02560,
            "x": 0.00150,
            "y": 0.01994,
            "z": 0.00077,
        }
    else:
        # Özel frekans sözlüğü
        frekanslar = frekans_sozlugu

    if not durum_duyarliligi:
        sifreli_metin = sifreli_metin.lower()

    # Kare istatistik değerleri
    kare_istatistik_degerleri: dict[int, tuple[float, str]] = {}

    # Tüm kaydırmalar arasında döngü
    for kaydirma in range(len(alfabe_harfleri)):
        cozulmus_metin = ""

        # Mesajı kaydırma ile çöz
        for harf in sifreli_metin:
            try:
                # Harfi alfabede indekslemeyi dene
                yeni_anahtar = (alfabe_harfleri.index(harf.lower()) - kaydirma) % len(
                    alfabe_harfleri
                )
                cozulmus_metin += (
                    alfabe_harfleri[yeni_anahtar].upper()
                    if durum_duyarliligi and harf.isupper()
                    else alfabe_harfleri[yeni_anahtar]
                )
            except ValueError:
                # Harf alfabede değilse karakteri ekle
                cozulmus_metin += harf

        kare_istatistik = 0.0

        # Çözülmüş mesajdaki her harf için döngü
        for harf in cozulmus_metin:
            if durum_duyarliligi:
                harf = harf.lower()
                if harf in frekanslar:
                    # Mesajda harfin kaç kez geçtiğini al
                    gecis_sayisi = cozulmus_metin.lower().count(harf)

                    # Harfin frekansına göre görünmesi gereken sayıyı al
                    beklenen = frekanslar[harf] * gecis_sayisi

                    # Kare istatistik formülünü tamamla
                    kare_harf_degeri = ((gecis_sayisi - beklenen) ** 2) / beklenen

                    # Toplam kare istatistiğine hata payını ekle
                    kare_istatistik += kare_harf_degeri
            elif harf.lower() in frekanslar:
                # Mesajda harfin kaç kez geçtiğini al
                gecis_sayisi = cozulmus_metin.count(harf)

                # Harfin frekansına göre görünmesi gereken sayıyı al
                beklenen = frekanslar[harf] * gecis_sayisi

                # Kare istatistik formülünü tamamla
                kare_harf_degeri = ((gecis_sayisi - beklenen) ** 2) / beklenen

                # Toplam kare istatistiğine hata payını ekle
                kare_istatistik += kare_harf_degeri

        # Verileri kare_istatistik_degerleri sözlüğüne ekle
        kare_istatistik_degerleri[kaydirma] = (
            kare_istatistik,
            cozulmus_metin,
        )

    # En olası şifreyi bulmak için en küçük kare istatistiğine sahip şifreyi bul
    def kare_istatistik_degerleri_siralama_anahtari(anahtar: int) -> tuple[float, str]:
        return kare_istatistik_degerleri[anahtar]

    en_olasi_sifre: int = min(
        kare_istatistik_degerleri,
        key=kare_istatistik_degerleri_siralama_anahtari,
    )

    # En olası şifreden (anahtar, çözülen mesaj) tüm verileri al
    (
        en_olasi_sifre_kare_degeri,
        cozulmus_en_olasi_sifre,
    ) = kare_istatistik_degerleri[en_olasi_sifre]

    # En olası kaydırma ile ilgili verileri döndür
    return (
        en_olasi_sifre,
        en_olasi_sifre_kare_degeri,
        cozulmus_en_olasi_sifre,
    )
