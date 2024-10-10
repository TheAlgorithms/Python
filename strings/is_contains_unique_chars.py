def benzersiz_karakterler_var_mi(girdi_str: str) -> bool:
    """

    # Organiser: K. Umut Araz

    Verilen stringdeki tüm karakterlerin benzersiz olup olmadığını kontrol eder.
    >>> benzersiz_karakterler_var_mi("I_love.py")
    True
    >>> benzersiz_karakterler_var_mi("I don't love Python")
    False

    Zaman karmaşıklığı: O(n)
    Alan karmaşıklığı: O(1) Unicode'da 144697 karakter olduğu için 19320 byte
    """

    # Her bit, her unicode karakterini temsil eder
    # Örneğin 65. bit 'A' karakterini temsil eder
    bitmap = 0
    for ch in girdi_str:
        ch_unicode = ord(ch)
        ch_bit_index_on = 1 << ch_unicode  # Bit'i açmak için 1'i sola kaydırıyoruz

        # Eğer mevcut karakterin unicode'u için bit zaten açıldıysa
        if bitmap & ch_bit_index_on:
            return False
        bitmap |= ch_bit_index_on
    return True


if __name__ == "__main__":
    import doctest

    doctest.testmod()
