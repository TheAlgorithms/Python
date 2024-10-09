"""
Başlık : Renk kodlarını kullanarak n bantlı bir direncin direncini hesaplama

Açıklama :
    Dirençler elektrik akışını engeller. Her birinin, akım akışını ne kadar güçlü
    engellediğini belirten bir değeri vardır. Bu değerin birimi ohm olup, genellikle
    Yunan harfi omega: Ω ile gösterilir.

    Bir direnç üzerindeki renkli bantlar, değerini ve toleransını anlamanız için
    gereken her şeyi size söyleyebilir, yeter ki onları nasıl okuyacağınızı anlayın.
    Renklerin sıralanma düzeni çok önemlidir ve her direnç değerinin kendine özgü
    bir kombinasyonu vardır.

    Dirençler için renk kodlaması, IEC 60062'de tanımlanan uluslararası bir standarttır.

    Bir dirençte bulunan bant sayısı üç ile altı arasında değişir. Bunlar önemli
    rakamları, çarpanı, toleransı, güvenilirliği ve sıcaklık katsayısını temsil eder.
    Bir tür bant için kullanılan her rengin bir değeri vardır. Soldan sağa doğru okunur.
    Tüm dirençlerde önemli rakamlar ve çarpan bantları bulunur. Üç bantlı bir dirençte,
    soldan ilk iki bant önemli rakamları, üçüncü bant ise çarpan bandını temsil eder.

    Önemli rakamlar - Bir dirençteki önemli rakamlar bandının sayısı iki ile üç arasında
    değişebilir.
    Önemli rakam bantlarıyla ilişkili renkler ve değerler -
    (Siyah = 0, Kahverengi = 1, Kırmızı = 2, Turuncu = 3, Sarı = 4, Yeşil = 5, Mavi = 6,
    Mor = 7, Gri = 8, Beyaz = 9)

    Çarpan - Bir dirençte bir çarpan bandı bulunur. Önceki bantlardan elde edilen önemli
    rakamlarla çarpılır.
    Çarpan bandıyla ilişkili renkler ve değerler -
    (Siyah = 100, Kahverengi = 10^1, Kırmızı = 10^2, Turuncu = 10^3, Sarı = 10^4, Yeşil = 10^5,
    Mavi = 10^6, Mor = 10^7, Gri = 10^8, Beyaz = 10^9, Altın = 10^-1, Gümüş = 10^-2)
    Çarpan bantlarının önemli rakam bantları için kullanılmayan Altın ve Gümüş
    kullandığını unutmayın.

    Tolerans - Tolerans bandı her zaman mevcut değildir. Dört bantlı dirençlerde ve
    üzerinde görülebilir. Bu, direnç değerinin değişebileceği yüzdeyi belirtir.
    Tolerans bandıyla ilişkili renkler ve değerler -
    (Kahverengi = %1, Kırmızı = %2, Turuncu = %0.05, Sarı = %0.02, Yeşil = %0.5, Mavi = %0.25,
    Mor = %0.1, Gri = %0.01, Altın = %5, Gümüş = %10)
    Hiçbir renk belirtilmemişse, varsayılan olarak tolerans %20'dir.
    Tolerans bandının Siyah ve Beyaz renkleri kullanmadığını unutmayın.

    Sıcaklık Katsayısı - Bileşenin ortam sıcaklığının bir fonksiyonu olarak direnç
    değişimini ppm/K cinsinden belirtir.
    Altı bantlı dirençlerde bulunur.
    Sıcaklık katsayısı bandıyla ilişkili renkler ve değerler -
    (Siyah = 250 ppm/K, Kahverengi = 100 ppm/K, Kırmızı = 50 ppm/K, Turuncu = 15 ppm/K,
    Sarı = 25 ppm/K, Yeşil = 20 ppm/K, Mavi = 10 ppm/K, Mor = 5 ppm/K,
    Gri = 1 ppm/K)
    Sıcaklık katsayısı bandının Beyaz, Altın, Gümüş renklerini kullanmadığını unutmayın.

Kaynaklar :
    https://www.calculator.net/resistor-calculator.html
    https://learn.parallax.com/support/reference/resistor-color-codes
    https://byjus.com/physics/resistor-colour-codes/
"""

geçerli_renkler: list = [
    "Siyah",
    "Kahverengi",
    "Kırmızı",
    "Turuncu",
    "Sarı",
    "Yeşil",
    "Mavi",
    "Mor",
    "Gri",
    "Beyaz",
    "Altın",
    "Gümüş",
]

önemli_rakam_renk_değerleri: dict[str, int] = {
    "Siyah": 0,
    "Kahverengi": 1,
    "Kırmızı": 2,
    "Turuncu": 3,
    "Sarı": 4,
    "Yeşil": 5,
    "Mavi": 6,
    "Mor": 7,
    "Gri": 8,
    "Beyaz": 9,
}

çarpan_renk_değerleri: dict[str, float] = {
    "Siyah": 10**0,
    "Kahverengi": 10**1,
    "Kırmızı": 10**2,
    "Turuncu": 10**3,
    "Sarı": 10**4,
    "Yeşil": 10**5,
    "Mavi": 10**6,
    "Mor": 10**7,
    "Gri": 10**8,
    "Beyaz": 10**9,
    "Altın": 10**-1,
    "Gümüş": 10**-2,
}

tolerans_renk_değerleri: dict[str, float] = {
    "Kahverengi": 1,
    "Kırmızı": 2,
    "Turuncu": 0.05,
    "Sarı": 0.02,
    "Yeşil": 0.5,
    "Mavi": 0.25,
    "Mor": 0.1,
    "Gri": 0.01,
    "Altın": 5,
    "Gümüş": 10,
}

sıcaklık_katsayısı_renk_değerleri: dict[str, int] = {
    "Siyah": 250,
    "Kahverengi": 100,
    "Kırmızı": 50,
    "Turuncu": 15,
    "Sarı": 25,
    "Yeşil": 20,
    "Mavi": 10,
    "Mor": 5,
    "Gri": 1,
}

bant_türleri: dict[int, dict[str, int]] = {
    3: {"önemli": 2, "çarpan": 1},
    4: {"önemli": 2, "çarpan": 1, "tolerans": 1},
    5: {"önemli": 3, "çarpan": 1, "tolerans": 1},
    6: {"önemli": 3, "çarpan": 1, "tolerans": 1, "sıcaklık_katsayısı": 1},
}


def önemli_rakamları_al(renkler: list) -> str:
    """
    Fonksiyon, renkle ilişkilendirilen rakamı döndürür. Fonksiyon, giriş olarak
    renkleri içeren bir liste alır ve rakamları string olarak döndürür.

    >>> önemli_rakamları_al(['Siyah','Mavi'])
    '06'

    >>> önemli_rakamları_al(['Aqua','Mavi'])
    Traceback (most recent call last):
      ...
    ValueError: Aqua önemli rakam bantları için geçerli bir renk değil

    """
    rakam = ""
    for renk in renkler:
        if renk not in önemli_rakam_renk_değerleri:
            msg = f"{renk} önemli rakam bantları için geçerli bir renk değil"
            raise ValueError(msg)
        rakam = rakam + str(önemli_rakam_renk_değerleri[renk])
    return str(rakam)


def çarpanı_al(renk: str) -> float:
    """
    Fonksiyon, renkle ilişkilendirilen çarpan değerini döndürür.
    Fonksiyon, giriş olarak rengi alır ve çarpan değerini döndürür.

    >>> çarpanı_al('Altın')
    0.1

    >>> çarpanı_al('Fildişi')
    Traceback (most recent call last):
      ...
    ValueError: Fildişi çarpan bandı için geçerli bir renk değil

    """
    if renk not in çarpan_renk_değerleri:
        msg = f"{renk} çarpan bandı için geçerli bir renk değil"
        raise ValueError(msg)
    return çarpan_renk_değerleri[renk]


def toleransı_al(renk: str) -> float:
    """
    Fonksiyon, renkle ilişkilendirilen tolerans değerini döndürür.
    Fonksiyon, giriş olarak rengi alır ve tolerans değerini döndürür.

    >>> toleransı_al('Yeşil')
    0.5

    >>> toleransı_al('Çivit')
    Traceback (most recent call last):
      ...
    ValueError: Çivit tolerans bandı için geçerli bir renk değil

    """
    if renk not in tolerans_renk_değerleri:
        msg = f"{renk} tolerans bandı için geçerli bir renk değil"
        raise ValueError(msg)
    return tolerans_renk_değerleri[renk]


def sıcaklık_katsayısını_al(renk: str) -> int:
    """
    Fonksiyon, renkle ilişkilendirilen sıcaklık katsayısı değerini döndürür.
    Fonksiyon, giriş olarak rengi alır ve sıcaklık katsayısı değerini döndürür.

    >>> sıcaklık_katsayısını_al('Sarı')
    25

    >>> sıcaklık_katsayısını_al('Camgöbeği')
    Traceback (most recent call last):
      ...
    ValueError: Camgöbeği sıcaklık katsayısı bandı için geçerli bir renk değil

    """
    if renk not in sıcaklık_katsayısı_renk_değerleri:
        msg = f"{renk} sıcaklık katsayısı bandı için geçerli bir renk değil"
        raise ValueError(msg)
    return sıcaklık_katsayısı_renk_değerleri[renk]


def bant_türü_sayısını_al(toplam_bant_sayısı: int, bant_türü: str) -> int:
    """
    Fonksiyon, n bantlı bir dirençte verilen türdeki bantların sayısını döndürür.
    Fonksiyon, toplam_bant_sayısı ve bant_türü'nü giriş olarak alır ve verilen
    dirençte o türe ait bantların sayısını döndürür.

    >>> bant_türü_sayısını_al(3,'önemli')
    2

    >>> bant_türü_sayısını_al(2,'önemli')
    Traceback (most recent call last):
      ...
    ValueError: 2 geçerli bir bant sayısı değil

    >>> bant_türü_sayısını_al(3,'ön')
    Traceback (most recent call last):
      ...
    ValueError: ön 3 bantlı bir direnç için geçerli değil

    >>> bant_türü_sayısını_al(3,'tolerans')
    Traceback (most recent call last):
      ...
    ValueError: tolerans 3 bantlı bir direnç için geçerli değil

    >>> bant_türü_sayısını_al(5,'sıcaklık_katsayısı')
    Traceback (most recent call last):
      ...
    ValueError: sıcaklık_katsayısı 5 bantlı bir direnç için geçerli değil

    """
    if toplam_bant_sayısı not in bant_türleri:
        msg = f"{toplam_bant_sayısı} geçerli bir bant sayısı değil"
        raise ValueError(msg)
    if bant_türü not in bant_türleri[toplam_bant_sayısı]:
        msg = f"{bant_türü} {toplam_bant_sayısı} bantlı bir direnç için geçerli değil"
        raise ValueError(msg)
    return bant_türleri[toplam_bant_sayısı][bant_türü]


def geçerliliği_kontrol_et(bant_sayısı: int, renkler: list) -> bool:
    """
    Fonksiyon, sağlanan girişin geçerli olup olmadığını kontrol eder.
    Fonksiyon, bant_sayısı ve renkleri giriş olarak alır ve geçerliyse
    True döner.

    >>> geçerliliği_kontrol_et(3, ["Siyah","Mavi","Turuncu"])
    True

    >>> geçerliliği_kontrol_et(4, ["Siyah","Mavi","Turuncu"])
    Traceback (most recent call last):
      ...
    ValueError: 4 renk bekleniyor, sağlanan 3 renk

    >>> geçerliliği_kontrol_et(3, ["Camgöbeği","Kırmızı","Sarı"])
    Traceback (most recent call last):
      ...
    ValueError: Camgöbeği geçerli bir renk değil

    """
    if bant_sayısı >= 3 or bant_sayısı <= 6:
        if bant_sayısı == len(renkler):
            for renk in renkler:
                if renk not in geçerli_renkler:
                    msg = f"{renk} geçerli bir renk değil"
                    raise ValueError(msg)
            return True
        else:
            msg = f"{bant_sayısı} renk bekleniyor, sağlanan {len(renkler)} renk"
            raise ValueError(msg)
    else:
        msg = "Geçersiz bant sayısı. Direnç bantları 3 ile 6 arasında olmalıdır"
        raise ValueError(msg)


def direnç_hesapla(bant_sayısı: int, renk_kodu_listesi: list) -> dict:
    """
    Fonksiyon, renk kodlarını kullanarak direncin toplam direncini hesaplar.
    Fonksiyon, bant_sayısı ve renk_kodu_listesi'ni giriş olarak alır ve
    direnci döner.

    >>> direnç_hesapla(3, ["Siyah","Mavi","Turuncu"])
    {'direnç': '6000Ω ±20% '}

    >>> direnç_hesapla(4, ["Turuncu","Yeşil","Mavi","Altın"])
    {'direnç': '35000000Ω ±5% '}

    >>> direnç_hesapla(5, ["Mor","Kahverengi","Gri","Gümüş","Yeşil"])
    {'direnç': '7.18Ω ±0.5% '}

    >>> direnç_hesapla(6, ["Kırmızı","Yeşil","Mavi","Sarı","Turuncu","Gri"])
    {'direnç': '2560000Ω ±0.05% 1 ppm/K'}

    >>> direnç_hesapla(0, ["Mor","Kahverengi","Gri","Gümüş","Yeşil"])
    Traceback (most recent call last):
      ...
    ValueError: Geçersiz bant sayısı. Direnç bantları 3 ile 6 arasında olmalıdır

    >>> direnç_hesapla(4, ["Mor","Kahverengi","Gri","Gümüş","Yeşil"])
    Traceback (most recent call last):
      ...
    ValueError: 4 renk bekleniyor, sağlanan 5 renk

    >>> direnç_hesapla(4, ["Mor","Gümüş","Kahverengi","Gri"])
    Traceback (most recent call last):
      ...
    ValueError: Gümüş önemli rakam bantları için geçerli bir renk değil

    >>> direnç_hesapla(4, ["Mor","Mavi","Lime","Gri"])
    Traceback (most recent call last):
      ...
    ValueError: Lime geçerli bir renk değil

    """
    geçerli_mi = geçerliliği_kontrol_et(bant_sayısı, renk_kodu_listesi)
    if geçerli_mi:
        önemli_bant_sayısı = bant_türü_sayısını_al(
            bant_sayısı, "önemli"
        )
        önemli_renkler = renk_kodu_listesi[:önemli_bant_sayısı]
        önemli_rakamlar = int(önemli_rakamları_al(önemli_renkler))
        çarpan_renk = renk_kodu_listesi[önemli_bant_sayısı]
        çarpan = çarpanı_al(çarpan_renk)
        if bant_sayısı == 3:
            tolerans_renk = None
        else:
            tolerans_renk = renk_kodu_listesi[önemli_bant_sayısı + 1]
        tolerans = (
            20 if tolerans_renk is None else toleransı_al(str(tolerans_renk))
        )
        if bant_sayısı != 6:
            sıcaklık_katsayısı_renk = None
        else:
            sıcaklık_katsayısı_renk = renk_kodu_listesi[
                önemli_bant_sayısı + 2
            ]
        sıcaklık_katsayısı = (
            0
            if sıcaklık_katsayısı_renk is None
            else sıcaklık_katsayısını_al(str(sıcaklık_katsayısı_renk))
        )
        direnç = önemli_rakamlar * çarpan
        if sıcaklık_katsayısı == 0:
            cevap = f"{direnç}Ω ±{tolerans}% "
        else:
            cevap = f"{direnç}Ω ±{tolerans}% {sıcaklık_katsayısı} ppm/K"
        return {"direnç": cevap}
    else:
        raise ValueError("Giriş geçersiz")


if __name__ == "__main__":
    import doctest

    doctest.testmod()
