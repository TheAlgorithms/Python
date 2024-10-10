def ses_harflerini_say(s: str) -> int:
    """

    # Organiser: K. Umut Araz


    Verilen bir stringdeki ses harflerinin sayısını hesaplar.

    :param s: Ses harflerini saymak için giriş stringi.
    :return: Giriş stringindeki ses harflerinin sayısı.

    Örnekler:
    >>> ses_harflerini_say("merhaba dünya")
    6
    >>> ses_harflerini_say("MERHABA DÜNYA")
    6
    >>> ses_harflerini_say("123 merhaba dünya")
    6
    >>> ses_harflerini_say("")
    0
    >>> ses_harflerini_say("a hızlı kahverengi tilki")
    8
    >>> ses_harflerini_say("hızlı KAHVERENGİ tilki")
    8
    >>> ses_harflerini_say("PYTHON")
    1
    """
    if not isinstance(s, str):
        raise ValueError("Giriş bir string olmalıdır")

    ses_harfleri = "aeiouAEIOUöüıİ"
    return sum(1 for char in s if char in ses_harfleri)

if __name__ == "__main__":
    from doctest import testmod

    testmod()
