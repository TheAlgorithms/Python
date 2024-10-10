"""
Vikipedi: https://en.wikipedia.org/wiki/Enigma_machine
Video açıklaması: https://youtu.be/QwQVMqfoB2E
Bu konu hakkında Numberphile ve Computerphile'in videolarını da kontrol edin.

Bu modül, II. Dünya Savaşı'ndan ünlü Enigma makinesini taklit eden 'enigma' fonksiyonunu içerir.
Modül şunları içerir:
- enigma fonksiyonu
- fonksiyon kullanımına dair örnekler
- 9 rastgele üretilmiş rotor
- reflektör (statik rotor olarak da bilinir)
- orijinal alfabeyi

Yazar: TrapinchO

Organiser: K. Umut Araz
"""

from __future__ import annotations

RotorPositionT = tuple[int, int, int]
RotorSelectionT = tuple[str, str, str]

# Kullanılan alfabeyi tanımlama --------------------------
abc = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

# -------------------------- Varsayılan seçim --------------------------
# rotörler --------------------------
rotor1 = "EGZWVONAHDCLFQMSIPJBYUKXTR"
rotor2 = "FOBHMDKEXQNRAULPGSJVTYICZW"
rotor3 = "ZJXESIUQLHAVRMDOYGTNFWPBKC"
# reflektör --------------------------
reflector = {
    "A": "N",
    "N": "A",
    "B": "O",
    "O": "B",
    "C": "P",
    "P": "C",
    "D": "Q",
    "Q": "D",
    "E": "R",
    "R": "E",
    "F": "S",
    "S": "F",
    "G": "T",
    "T": "G",
    "H": "U",
    "U": "H",
    "I": "V",
    "V": "I",
    "J": "W",
    "W": "J",
    "K": "X",
    "X": "K",
    "L": "Y",
    "Y": "L",
    "M": "Z",
    "Z": "M",
}

# -------------------------- Ek rotörler --------------------------
rotor4 = "RMDJXFUWGISLHVTCQNKYPBEZOA"
rotor5 = "SGLCPQWZHKXAREONTFBVIYJUDM"
rotor6 = "HVSICLTYKQUBXDWAJZOMFGPREN"
rotor7 = "RZWQHFMVDBKICJLNTUXAGYPSOE"
rotor8 = "LFKIJODBEGAMQPXVUHYSTCZRWN"
rotor9 = "KOAEGVDHXPQZMLFTYWJNBRCIUS"

def _validator(
    rotpos: RotorPositionT, rotsel: RotorSelectionT, pb: str
) -> tuple[RotorPositionT, RotorSelectionT, dict[str, str]]:
    """
    'enigma' fonksiyonu için değerlerin kullanılabilirliğini kontrol eder.

    >>> _validator((1,1,1), (rotor1, rotor2, rotor3), 'POLAND')
    ((1, 1, 1), ('EGZWVONAHDCLFQMSIPJBYUKXTR', 'FOBHMDKEXQNRAULPGSJVTYICZW', \
'ZJXESIUQLHAVRMDOYGTNFWPBKC'), \
{'P': 'O', 'O': 'P', 'L': 'A', 'A': 'L', 'N': 'D', 'D': 'N'})

    :param rotpos: rotor pozisyonu
    :param rotsel: rotor seçimi
    :param pb: plugboard -> doğrulanmış ve dönüştürülmüş
    :return: (rotpos, rotsel, pb)
    """
    # 3 benzersiz rotor olup olmadığını kontrol etme

    if (unique_rotsel := len(set(rotsel))) < 3:
        msg = f"Lütfen 3 benzersiz rotor kullanın (şu anda {unique_rotsel})"
        raise Exception(msg)

    # Rotor pozisyonlarının geçerliliğini kontrol etme
    rotorpos1, rotorpos2, rotorpos3 = rotpos
    if not 0 < rotorpos1 <= len(abc):
        msg = f"Birinci rotor pozisyonu 1..26 aralığında değil ({rotorpos1})"
        raise ValueError(msg)
    if not 0 < rotorpos2 <= len(abc):
        msg = f"İkinci rotor pozisyonu 1..26 aralığında değil ({rotorpos2})"
        raise ValueError(msg)
    if not 0 < rotorpos3 <= len(abc):
        msg = f"Üçüncü rotor pozisyonu 1..26 aralığında değil ({rotorpos3})"
        raise ValueError(msg)

    # Dizeyi doğrular ve sözlük döndürür
    pbdict = _plugboard(pb)

    return rotpos, rotsel, pbdict

def _plugboard(pbstring: str) -> dict[str, str]:
    """
    https://en.wikipedia.org/wiki/Enigma_machine#Plugboard

    >>> _plugboard('PICTURES')
    {'P': 'I', 'I': 'P', 'C': 'T', 'T': 'C', 'U': 'R', 'R': 'U', 'E': 'S', 'S': 'E'}
    >>> _plugboard('POLAND')
    {'P': 'O', 'O': 'P', 'L': 'A', 'A': 'L', 'N': 'D', 'D': 'N'}

    Kodda 'pb', 'plugboard' anlamına gelir.

    Çiftler boşluklarla ayrılabilir.
    :param pbstring: Enigma makinesi için plugboard ayarlarını içeren dize
    :return: dönüştürülmüş çiftleri içeren sözlük
    """

    # Giriş dizesinin
    # a) dize türünde olup olmadığını
    # b) çiftler oluşturulabilmesi için çift uzunlukta olup olmadığını kontrol etme
    if not isinstance(pbstring, str):
        msg = f"Plugboard ayarı dize türünde değil ({type(pbstring)})"
        raise TypeError(msg)
    elif len(pbstring) % 2 != 0:
        msg = f"Tek sayıda sembol var ({len(pbstring)})"
        raise Exception(msg)
    elif pbstring == "":
        return {}

    pbstring = pbstring.replace(" ", "")

    # Tüm karakterlerin benzersiz olup olmadığını kontrol etme
    tmppbl = set()
    for i in pbstring:
        if i not in abc:
            msg = f"'{i}' semboller listesinde yok"
            raise Exception(msg)
        elif i in tmppbl:
            msg = f"Tekrar eden sembol ({i})"
            raise Exception(msg)
        else:
            tmppbl.add(i)

    # Sözlüğü oluşturma
    pb = {}
    for j in range(0, len(pbstring) - 1, 2):
        pb[pbstring[j]] = pbstring[j + 1]
        pb[pbstring[j + 1]] = pbstring[j]

    return pb

def enigma(
    text: str,
    rotor_position: RotorPositionT,
    rotor_selection: RotorSelectionT = (rotor1, rotor2, rotor3),
    plugb: str = "",
) -> str:
    """
    Gerçek dünyadaki enigma ile tek farkım, dize girişi kabul etmemdir.
    Tüm karakterler büyük harfe dönüştürülür. (harf olmayan semboller göz ardı edilir)
    Nasıl çalışır:
    (mesajdaki her harf için)

    - Giriş harfi plugboard'a gider.
    Eğer başka bir harfle bağlantılıysa, değiştirir.

    - Harf 3 rotordan geçer.
    Her rotor, birinin karıştırıldığı 2 sembol seti olarak temsil edilebilir.
    İlk setten her sembolün, ikinci setle karşılık gelen bir sembolü vardır ve tersine.

    örnek:
    | ABCDEFGHIJKLMNOPQRSTUVWXYZ | örn. F=D ve D=F
    | VKLEPDBGRNWTFCJOHQAMUZYIXS |

    - Sembol daha sonra reflektörden (statik rotor) geçer.
    Orada, eşleşen sembolle değiştirilir.
    Reflektör, alfanet'in yarısını içeren 2 set olarak temsil edilebilir.
    Genellikle 10 harf çifti vardır.

    Örnek:
    | ABCDEFGHIJKLM | örn. E, X ile eşleşir
    | ZYXWVUTSRQPON | böylece E girdiğinde X çıkar ve tersine

    - Harf daha sonra rotorlardan tekrar geçer.

    - Eğer harf plugboard'a bağlıysa, değiştirilir.

    - Harfi döndür.

    >>> enigma('Hello World!', (1, 2, 1), plugb='pictures')
    'KORYH JUHHI!'
    >>> enigma('KORYH, juhhi!', (1, 2, 1), plugb='pictures')
    'HELLO, WORLD!'
    >>> enigma('hello world!', (1, 1, 1), plugb='pictures')
    'FPNCZ QWOBU!'
    >>> enigma('FPNCZ QWOBU', (1, 1, 1), plugb='pictures')
    'HELLO WORLD'

    :param text: giriş mesajı
    :param rotor_position: 1..26 aralığında 3 değer içeren demet
    :param rotor_selection: 3 rotordan oluşan demet
    :param plugb: plugboard yapılandırmasını içeren dize (varsayılan '')
    :return: şifrelenmiş/şifresi çözülmüş dize
    """

    text = text.upper()
    rotor_position, rotor_selection, plugboard = _validator(
        rotor_position, rotor_selection, plugb.upper()
    )

    rotorpos1, rotorpos2, rotorpos3 = rotor_position
    rotor1, rotor2, rotor3 = rotor_selection
    rotorpos1 -= 1
    rotorpos2 -= 1
    rotorpos3 -= 1

    result = []

    # şifreleme/şifre çözme süreci --------------------------
    for symbol in text:
        if symbol in abc:
            # 1. plugboard --------------------------
            if symbol in plugboard:
                symbol = plugboard[symbol]

            # rotor ra --------------------------
            index = abc.index(symbol) + rotorpos1
            symbol = rotor1[index % len(abc)]

            # rotor rb --------------------------
            index = abc.index(symbol) + rotorpos2
            symbol = rotor2[index % len(abc)]

            # rotor rc --------------------------
            index = abc.index(symbol) + rotorpos3
            symbol = rotor3[index % len(abc)]

            # reflektör --------------------------
            symbol = reflector[symbol]

            # 2. rotörler
            symbol = abc[rotor3.index(symbol) - rotorpos3]
            symbol = abc[rotor2.index(symbol) - rotorpos2]
            symbol = abc[rotor1.index(symbol) - rotorpos1]

            # 2. plugboard
            if symbol in plugboard:
                symbol = plugboard[symbol]

            # rotor pozisyonlarını hareket ettirir/sıfırlar
            rotorpos1 += 1
            if rotorpos1 >= len(abc):
                rotorpos1 = 0
                rotorpos2 += 1
            if rotorpos2 >= len(abc):
                rotorpos2 = 0
                rotorpos3 += 1
            if rotorpos3 >= len(abc):
                rotorpos3 = 0

        result.append(symbol)

    return "".join(result)

if __name__ == "__main__":
    message = "Bu, II. Dünya Savaşı'ndan Enigma makinesini taklit eden Python betiğim."
    rotor_pos = (1, 1, 1)
    pb = "pictures"
    rotor_sel = (rotor2, rotor4, rotor8)
    en = enigma(message, rotor_pos, rotor_sel, pb)

    print("Şifrelenmiş mesaj:", en)
    print("Şifresi çözülmüş mesaj:", enigma(en, rotor_pos, rotor_sel, pb))
