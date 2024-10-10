"""
Kesirli Morse Şifrelemesi için Python programı.

Kesirli Morse şifrelemesi, önce düz metni Morse koduna dönüştürür,
sonra Morse kodunun sabit boyutlu bloklarını harflere şifreler.
Bu işlem, düz metin harflerinin şifreli metin harfleriyle karışmasına neden olur,
bu da onu yer değiştirme şifrelerinden daha güvenli hale getirir.

http://practicalcryptography.com/ciphers/fractionated-morse-cipher/

Organiser: K. Umut Araz
"""

import string

MORSE_KODU_SÖZLÜĞÜ = {
    "A": ".-",
    "B": "-...",
    "C": "-.-.",
    "D": "-..",
    "E": ".",
    "F": "..-.",
    "G": "--.",
    "H": "....",
    "I": "..",
    "J": ".---",
    "K": "-.-",
    "L": ".-..",
    "M": "--",
    "N": "-.",
    "O": "---",
    "P": ".--.",
    "Q": "--.-",
    "R": ".-.",
    "S": "...",
    "T": "-",
    "U": "..-",
    "V": "...-",
    "W": ".--",
    "X": "-..-",
    "Y": "-.--",
    "Z": "--..",
    " ": "",
}

# Morse kodunun olası trigramlarını tanımla
MORSE_KOMBİNASYONLARI = [
    "...",
    "..-",
    "..x",
    ".-.",
    ".--",
    ".-x",
    ".x.",
    ".x-",
    ".xx",
    "-..",
    "-.-",
    "-.x",
    "--.",
    "---",
    "--x",
    "-x.",
    "-x-",
    "-xx",
    "x..",
    "x.-",
    "x.x",
    "x-.",
    "x--",
    "x-x",
    "xx.",
    "xx-",
    "xxx",
]

# Morse kodu için ters sözlük oluştur
TERS_SÖZLÜK = {değer: anahtar for anahtar, değer in MORSE_KODU_SÖZLÜĞÜ.items()}


def morse_koduna_çevir(düz_metin: str) -> str:
    """Düz metin mesajını Morse koduna çevir.

    Argümanlar:
        düz_metin: Çevrilecek düz metin mesajı.

    Döndürür:
        Düz metin mesajının Morse kodu temsili.

    Örnek:
        >>> morse_koduna_çevir("doğu savun")
        '-..x.x..-.x.x-.x-..xx-x....x.xx.x.-x...x-'
    """
    return "x".join([MORSE_KODU_SÖZLÜĞÜ.get(harf.upper(), "") for harf in düz_metin])


def kesirli_morse_şifrele(düz_metin: str, anahtar: str) -> str:
    """Düz metin mesajını Kesirli Morse Şifrelemesi ile şifrele.

    Argümanlar:
        düz_metin: Şifrelenecek düz metin mesajı.
        anahtar: Şifreleme anahtarı.

    Döndürür:
        Şifrelenmiş metin.

    Örnek:
        >>> kesirli_morse_şifrele("doğu savun","Yuvarlakmasa")
        'ESOAVVLJRSSTRX'
    """
    morse_kodu = morse_koduna_çevir(düz_metin)
    anahtar = anahtar.upper() + string.ascii_uppercase
    anahtar = "".join(sorted(set(anahtar), key=anahtar.find))

    # Morse kodu uzunluğunun 3'ün katı olmasını sağla
    doldurma_uzunluğu = 3 - (len(morse_kodu) % 3)
    morse_kodu += "x" * doldurma_uzunluğu

    kesirli_morse_sözlüğü = {değer: anahtar for anahtar, değer in zip(anahtar, MORSE_KOMBİNASYONLARI)}
    kesirli_morse_sözlüğü["xxx"] = ""
    şifrelenmiş_metin = "".join(
        [
            kesirli_morse_sözlüğü[morse_kodu[i : i + 3]]
            for i in range(0, len(morse_kodu), 3)
        ]
    )
    return şifrelenmiş_metin


def kesirli_morse_şifre_çöz(ciphertext: str, anahtar: str) -> str:
    """Kesirli Morse Şifrelemesi ile şifrelenmiş bir metni çöz.

    Argümanlar:
        ciphertext: Çözülecek şifreli metin.
        anahtar: Şifre çözme anahtarı.

    Döndürür:
        Çözülmüş düz metin mesajı.

    Örnek:
        >>> kesirli_morse_şifre_çöz("ESOAVVLJRSSTRX","Yuvarlakmasa")
        'DOĞU SAVUN'
    """
    anahtar = anahtar.upper() + string.ascii_uppercase
    anahtar = "".join(sorted(set(anahtar), key=anahtar.find))

    ters_kesirli_morse_sözlüğü = dict(zip(anahtar, MORSE_KOMBİNASYONLARI))
    morse_kodu = "".join(
        [ters_kesirli_morse_sözlüğü.get(harf, "") for harf in ciphertext]
    )
    çözülmüş_metin = "".join(
        [TERS_SÖZLÜK[kod] for kod in morse_kodu.split("x")]
    ).strip()
    return çözülmüş_metin


if __name__ == "__main__":
    """
    Kesirli Morse Şifrelemesi'nin örnek kullanımı.
    """
    düz_metin = "doğu savun"
    print("Düz Metin:", düz_metin)
    anahtar = "YUVARLAKMASA"

    şifreli_metin = kesirli_morse_şifrele(düz_metin, anahtar)
    print("Şifrelenmiş:", şifreli_metin)

    çözülmüş_metin = kesirli_morse_şifre_çöz(şifreli_metin, anahtar)
    print("Çözülmüş:", çözülmüş_metin)
