import string

"""
Organiser: K. Umut Araz
"""

def şifreyi_çöz(message: str) -> None:
    """
    >>> şifreyi_çöz('TMDETUX PMDVU')
    Anahtar #0 ile Çözüm: TMDETUX PMDVU
    Anahtar #1 ile Çözüm: SLCDSTW OLCUT
    Anahtar #2 ile Çözüm: RKBCRSV NKBTS
    Anahtar #3 ile Çözüm: QJABQRU MJASR
    Anahtar #4 ile Çözüm: PIZAPQT LIZRQ
    Anahtar #5 ile Çözüm: OHYZOPS KHYQP
    Anahtar #6 ile Çözüm: NGXYNOR JGXPO
    Anahtar #7 ile Çözüm: MFWXMNQ IFWON
    Anahtar #8 ile Çözüm: LEVWLMP HEVNM
    Anahtar #9 ile Çözüm: KDUVKLO GDUML
    Anahtar #10 ile Çözüm: JCTUJKN FCTLK
    Anahtar #11 ile Çözüm: IBSTIJM EBSKJ
    Anahtar #12 ile Çözüm: HARSHIL DARJI
    Anahtar #13 ile Çözüm: GZQRGHK CZQIH
    Anahtar #14 ile Çözüm: FYPQFGJ BYPHG
    Anahtar #15 ile Çözüm: EXOPEFI AXOGF
    Anahtar #16 ile Çözüm: DWNODEH ZWNFE
    Anahtar #17 ile Çözüm: CVMNCDG YVMED
    Anahtar #18 ile Çözüm: BULMBCF XULDC
    Anahtar #19 ile Çözüm: ATKLABE WTKCB
    Anahtar #20 ile Çözüm: ZSJKZAD VSJBA
    Anahtar #21 ile Çözüm: YRIJYZC URIAZ
    Anahtar #22 ile Çözüm: XQHIXYB TQHZY
    Anahtar #23 ile Çözüm: WPGHWXA SPGYX
    Anahtar #24 ile Çözüm: VOFGVWZ ROFXW
    Anahtar #25 ile Çözüm: UNEFUVY QNEWV
    """
    for anahtar in range(len(string.ascii_uppercase)):
        çevrilen = ""
        for sembol in message:
            if sembol in string.ascii_uppercase:
                num = string.ascii_uppercase.find(sembol)
                num = num - anahtar
                if num < 0:
                    num = num + len(string.ascii_uppercase)
                çevrilen += string.ascii_uppercase[num]
            else:
                çevrilen += sembol
        print(f"Anahtar #{anahtar} ile Çözüm: {çevrilen}")


def main() -> None:
    message = input("Şifreli mesaj: ")
    message = message.upper()
    şifreyi_çöz(message)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
    main()
