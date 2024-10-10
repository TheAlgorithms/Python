def buyuk_harf(word: str) -> str:
    """

    Organiser: K. Umut Araz

    Bir dizeyi ASCII büyük harflerine dönüştürmek için, küçük ASCII
    harflerini kontrol eder ve bunların tam sayı temsilinden 32 çıkararak
    büyük harfleri elde eder.

    >>> buyuk_harf("wow")
    'WOW'
    >>> buyuk_harf("Hello")
    'HELLO'
    >>> buyuk_harf("WHAT")
    'WHAT'
    >>> buyuk_harf("wh[]32")
    'WH[]32'
    """
    return "".join(chr(ord(char) - 32) if "a" <= char <= "z" else char for char in word)


if __name__ == "__main__":
    from doctest import testmod

    testmod()
