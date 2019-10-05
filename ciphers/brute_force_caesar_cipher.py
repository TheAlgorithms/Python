def decrypt(message):
    """
    >>> decrypt('TMDETUX PMDVU')
    Decryption using Key #0: TMDETUX PMDVU
    Decryption using Key #1: SLCDSTW OLCUT
    Decryption using Key #2: RKBCRSV NKBTS
    Decryption using Key #3: QJABQRU MJASR
    Decryption using Key #4: PIZAPQT LIZRQ
    Decryption using Key #5: OHYZOPS KHYQP
    Decryption using Key #6: NGXYNOR JGXPO
    Decryption using Key #7: MFWXMNQ IFWON
    Decryption using Key #8: LEVWLMP HEVNM
    Decryption using Key #9: KDUVKLO GDUML
    Decryption using Key #10: JCTUJKN FCTLK
    Decryption using Key #11: IBSTIJM EBSKJ
    Decryption using Key #12: HARSHIL DARJI
    Decryption using Key #13: GZQRGHK CZQIH
    Decryption using Key #14: FYPQFGJ BYPHG
    Decryption using Key #15: EXOPEFI AXOGF
    Decryption using Key #16: DWNODEH ZWNFE
    Decryption using Key #17: CVMNCDG YVMED
    Decryption using Key #18: BULMBCF XULDC
    Decryption using Key #19: ATKLABE WTKCB
    Decryption using Key #20: ZSJKZAD VSJBA
    Decryption using Key #21: YRIJYZC URIAZ
    Decryption using Key #22: XQHIXYB TQHZY
    Decryption using Key #23: WPGHWXA SPGYX
    Decryption using Key #24: VOFGVWZ ROFXW
    Decryption using Key #25: UNEFUVY QNEWV
    """
    LETTERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for key in range(len(LETTERS)):
        translated = ""
        for symbol in message:
            if symbol in LETTERS:
                num = LETTERS.find(symbol)
                num = num - key
                if num < 0:
                    num = num + len(LETTERS)
                translated = translated + LETTERS[num]
            else:
                translated = translated + symbol
        print("Decryption using Key #%s: %s" % (key, translated))


def main():
    message = input("Encrypted message: ")
    message = message.upper()
    decrypt(message)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
    main()
