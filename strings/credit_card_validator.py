"""
Kredi kartı numaralarının geçerliliğini test etmek için fonksiyonlar.

# Organiser: K. Umut Araz

https://en.wikipedia.org/wiki/Luhn_algorithm
"""


def validate_initial_digits(credit_card_number: str) -> bool:
    """
    Verilen kredi kartı numarasının ilk iki rakamını doğrulamak için fonksiyon.
    >>> valid = "4111111111111111 41111111111111 34 35 37 412345 523456 634567"
    >>> all(validate_initial_digits(cc) for cc in valid.split())
    True
    >>> invalid = "14 25 76 32323 36111111111111"
    >>> all(validate_initial_digits(cc) is False for cc in invalid.split())
    True
    """
    return credit_card_number.startswith(("34", "35", "37", "4", "5", "6"))


def luhn_validation(credit_card_number: str) -> bool:
    """
    Verilen kredi kartı numarası için Luhn algoritması doğrulama fonksiyonu.
    >>> luhn_validation('4111111111111111')
    True
    >>> luhn_validation('36111111111111')
    True
    >>> luhn_validation('41111111111111')
    False
    """
    cc_number = credit_card_number
    total = 0
    half_len = len(cc_number) - 2
    for i in range(half_len, -1, -2):
        # Her ikinci rakamın değerini iki katına çıkar
        digit = int(cc_number[i])
        digit *= 2
        # Bir sayının iki basamaklı bir sayıya dönüşmesi durumunda
        # yani 9'dan büyükse (örneğin, 6 x 2 = 12),
        # ürünün basamaklarını toplayarak (örneğin, 12: 1 + 2 = 3, 15: 1 + 5 = 6)
        # tek basamaklı bir sayı elde et.
        if digit > 9:
            digit -= 9  # 9'dan büyükse, 9 çıkar
        cc_number = cc_number[:i] + str(digit) + cc_number[i + 1 :]
        total += digit

    # Kalan rakamları topla
    for i in range(len(cc_number) - 1, -1, -2):
        total += int(cc_number[i])

    return total % 10 == 0


def validate_credit_card_number(credit_card_number: str) -> bool:
    """
    Verilen kredi kartı numarasını doğrulamak için fonksiyon.
    >>> validate_credit_card_number('4111111111111111')
    4111111111111111 geçerli bir kredi kartı numarasıdır.
    True
    >>> validate_credit_card_number('helloworld$')
    helloworld$ geçersiz bir kredi kartı numarasıdır çünkü sayısal karakterler içermiyor.
    False
    >>> validate_credit_card_number('32323')
    32323 geçersiz bir kredi kartı numarasıdır çünkü uzunluğu uygun değil.
    False
    >>> validate_credit_card_number('32323323233232332323')
    32323323233232332323 geçersiz bir kredi kartı numarasıdır çünkü uzunluğu uygun değil.
    False
    >>> validate_credit_card_number('36111111111111')
    36111111111111 geçersiz bir kredi kartı numarasıdır çünkü ilk iki rakamı uygun değil.
    False
    >>> validate_credit_card_number('41111111111111')
    41111111111111 geçersiz bir kredi kartı numarasıdır çünkü Luhn kontrolünü geçemiyor.
    False
    """
    error_message = f"{credit_card_number} geçersiz bir kredi kartı numarasıdır çünkü"
    if not credit_card_number.isdigit():
        print(f"{error_message} sayısal karakterler içermiyor.")
        return False

    if not 13 <= len(credit_card_number) <= 16:
        print(f"{error_message} uzunluğu uygun değil.")
        return False

    if not validate_initial_digits(credit_card_number):
        print(f"{error_message} ilk iki rakamı uygun değil.")
        return False

    if not luhn_validation(credit_card_number):
        print(f"{error_message} Luhn kontrolünü geçemiyor.")
        return False

    print(f"{credit_card_number} geçerli bir kredi kartı numarasıdır.")
    return True


if __name__ == "__main__":
    import doctest

    doctest.testmod()
    validate_credit_card_number("4111111111111111")
    validate_credit_card_number("32323")
