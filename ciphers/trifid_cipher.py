"""
Trifid şifreleme, her bir düz metin harfini bir trigram'a ayırmak için bir tablo kullanır,
trigramların bileşenlerini karıştırır ve ardından bu karıştırılmış trigramları şifreli harflere
dönüştürmek için tabloyu tersine uygular.

#Organiser: K. Umut Araz

https://tr.wikipedia.org/wiki/Trifid_cipher
"""

from __future__ import annotations

# fmt: off
TEST_HARF_TO_NUMARA = {
    "A": "111", "B": "112", "C": "113", "D": "121", "E": "122", "F": "123", "G": "131",
    "H": "132", "I": "133", "J": "211", "K": "212", "L": "213", "M": "221", "N": "222",
    "O": "223", "P": "231", "Q": "232", "R": "233", "S": "311", "T": "312", "U": "313",
    "V": "321", "W": "322", "X": "323", "Y": "331", "Z": "332", "+": "333",
}
# fmt: off

TEST_NUMARA_TO_HARF = {val: key for key, val in TEST_HARF_TO_NUMARA.items()}


def __sifrele_bolumu(mesaj_bolumu: str, harf_to_numara: dict[str, str]) -> str:
    """
    'mesaj_bolumu' içindeki her harfin trigram değerini dikey olarak düzenler ve
    yatay olarak birleştirir.

    >>> __sifrele_bolumu('ASK', TEST_HARF_TO_NUMARA)
    '132111112'
    """
    bir, iki, uc = "", "", ""
    for her in (harf_to_numara[karakter] for karakter in mesaj_bolumu):
        bir += her[0]
        iki += her[1]
        uc += her[2]

    return bir + iki + uc


def __coz_bolumu(
    mesaj_bolumu: str, harf_to_numara: dict[str, str]
) -> tuple[str, str, str]:
    """
    Giriş dizesindeki her harfi ilgili trigram değerlerine dönüştürür, bunları birleştirir
    ve üç eşit grup dizeye ayırarak döndürür.

    >>> __coz_bolumu('ABCDE', TEST_HARF_TO_NUMARA)
    ('11111', '21131', '21122')
    """
    bu_bolum = "".join(harf_to_numara[karakter] for karakter in mesaj_bolumu)
    sonuc = []
    tmp = ""
    for rakam in bu_bolum:
        tmp += rakam
        if len(tmp) == len(mesaj_bolumu):
            sonuc.append(tmp)
            tmp = ""

    return sonuc[0], sonuc[1], sonuc[2]


def __hazirla(
    mesaj: str, alfabe: str
) -> tuple[str, str, dict[str, str], dict[str, str]]:
    """
    Trigramları oluşturan ve alfabenin her harfini karşılık gelen trigram ile eşleştirip
    bunu bir sözlükte saklayan yardımcı bir fonksiyon ("harf_to_numara" ve "numara_to_harf")
    alfabenin uzunluğunun 27 olup olmadığını kontrol ettikten sonra.

    >>> test = __hazirla('I aM a BOy','abCdeFghijkLmnopqrStuVwxYZ+')
    >>> expected = ('IAMABOY','ABCDEFGHIJKLMNOPQRSTUVWXYZ+',
    ... TEST_HARF_TO_NUMARA, TEST_NUMARA_TO_HARF)
    >>> test == expected
    True

    Eksik alfabe ile test
    >>> __hazirla('I aM a BOy','abCdeFghijkLmnopqrStuVw')
    Traceback (most recent call last):
        ...
    KeyError: 'Alfabenin uzunluğu 27 olmalıdır.'

    Fazla uzun alfabeler ile test
    >>> __hazirla('I aM a BOy','abCdeFghijkLmnopqrStuVwxyzzwwtyyujjgfd')
    Traceback (most recent call last):
        ...
    KeyError: 'Alfabenin uzunluğu 27 olmalıdır.'

    Verilen alfabenin dışında kalan noktalama işaretleri ile test
    >>> __hazirla('am i a boy?','abCdeFghijkLmnopqrStuVwxYZ+')
    Traceback (most recent call last):
        ...
    ValueError: Her mesaj karakteri alfabenin içinde olmalıdır!

    Sayılar ile test
    >>> __hazirla(500,'abCdeFghijkLmnopqrStuVwxYZ+')
    Traceback (most recent call last):
        ...
    AttributeError: 'int' nesnesinin 'replace' özelliği yok.
    """
    # Mesaj ve alfabenin doğrulanması, büyük harfe çevirme ve boşlukları kaldırma
    alfabe = alfabe.replace(" ", "").upper()
    mesaj = mesaj.replace(" ", "").upper()

    # Uzunluk ve karakter kontrolü
    if len(alfabe) != 27:
        raise KeyError("Alfabenin uzunluğu 27 olmalıdır.")
    if any(karakter not in alfabe for karakter in mesaj):
        raise ValueError("Her mesaj karakteri alfabenin içinde olmalıdır!")

    # Sözlükleri oluştur
    harf_to_numara = dict(zip(alfabe, TEST_HARF_TO_NUMARA.values()))
    numara_to_harf = {
        numara: harf for harf, numara in harf_to_numara.items()
    }

    return mesaj, alfabe, harf_to_numara, numara_to_harf


def mesaj_sifrele(
    mesaj: str, alfabe: str = "ABCDEFGHIJKLMNOPQRSTUVWXYZ.", periyot: int = 5
) -> str:
    """
    mesaj_sifrele
    ===============

    Trifid şifreleme kullanarak bir mesajı şifreler. Kullanılacak noktalama işaretleri
    alfabenin içine eklenmelidir.

    PARAMETRELER
    ----------

    *   mesaj: Şifrelemek istediğiniz mesaj.
    *   alfabe (isteğe bağlı): Şifreleme için kullanılacak karakterler.
    *   periyot (isteğe bağlı): Şifreleme sırasında grupta istediğiniz karakter sayısı.

    >>> mesaj_sifrele('I am a boy')
    'BCDGBQY'

    >>> mesaj_sifrele(' ')
    ''

    >>> mesaj_sifrele('   aide toi le c  iel      ta id  era    ',
    ... 'FELIXMARDSTBCGHJKNOPQUVWYZ+',5)
    'FMJFVOISSUFTFPUFEQQC'

    """
    mesaj, alfabe, harf_to_numara, numara_to_harf = __hazirla(
        mesaj, alfabe
    )

    sifreli_numerik = ""
    for i in range(0, len(mesaj) + 1, periyot):
        sifreli_numerik += __sifrele_bolumu(
            mesaj[i : i + periyot], harf_to_numara
        )

    sifreli = ""
    for i in range(0, len(sifreli_numerik), 3):
        sifreli += numara_to_harf[sifreli_numerik[i : i + 3]]
    return sifreli


def mesaj_coz(
    mesaj: str, alfabe: str = "ABCDEFGHIJKLMNOPQRSTUVWXYZ.", periyot: int = 5
) -> str:
    """
    mesaj_coz
    ===============

    Trifid şifreleme ile şifrelenmiş bir mesajı çözer.

    PARAMETRELER
    ----------

    *   mesaj: Çözmek istediğiniz mesaj.
    *   alfabe (isteğe bağlı): Şifreleme için kullanılan karakterler.
    *   periyot (isteğe bağlı): Şifrelenirken gruplama için kullanılan karakter sayısı.

    >>> mesaj_coz('BCDGBQY')
    'IAMABOY'

    Kendi alfabeniz ve periyodunuz ile çözme
    >>> mesaj_coz('FMJFVOISSUFTFPUFEQQC','FELIXMARDSTBCGHJKNOPQUVWYZ+',5)
    'AIDETOILECIELTAIDERA'
    """
    mesaj, alfabe, harf_to_numara, numara_to_harf = __hazirla(
        mesaj, alfabe
    )

    sifreli_numerik = []
    for i in range(0, len(mesaj), periyot):
        a, b, c = __coz_bolumu(mesaj[i : i + periyot], harf_to_numara)

        for j in range(len(a)):
            sifreli_numerik.append(a[j] + b[j] + c[j])

    return "".join(numara_to_harf[her] for her in sifreli_numerik)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
    msg = "KALENİN DOĞU DUVARINI SAVUN."
    sifreli = mesaj_sifrele(msg, "EPSDUCVWYM.ZLKXNBTFGORIJHAQ")
    cozulmus = mesaj_coz(sifreli, "EPSDUCVWYM.ZLKXNBTFGORIJHAQ")
    print(f"Şifreli: {sifreli}\nÇözülmüş: {cozulmus}")
