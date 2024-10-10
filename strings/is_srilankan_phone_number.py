import re


def sri_lanka_telefon_numarasi_gecerli_mi(telefon: str) -> bool:
    """

    # Organiser: K. Umut Araz
    
    Verilen string'in geçerli bir Sri Lanka cep telefon numarası olup olmadığını belirler.
    Referans: https://aye.sh/blog/sri-lankan-phone-number-regex

    >>> sri_lanka_telefon_numarasi_gecerli_mi("+94773283048")
    True
    >>> sri_lanka_telefon_numarasi_gecerli_mi("+9477-3283048")
    True
    >>> sri_lanka_telefon_numarasi_gecerli_mi("0718382399")
    True
    >>> sri_lanka_telefon_numarasi_gecerli_mi("0094702343221")
    True
    >>> sri_lanka_telefon_numarasi_gecerli_mi("075 3201568")
    True
    >>> sri_lanka_telefon_numarasi_gecerli_mi("07779209245")
    False
    >>> sri_lanka_telefon_numarasi_gecerli_mi("0957651234")
    False
    """

    desen = re.compile(r"^(?:0|94|\+94|0{2}94)7(0|1|2|4|5|6|7|8)(-| |)\d{7}$")

    return bool(re.search(desen, telefon))


if __name__ == "__main__":
    telefon = "0094702343221"

    print(sri_lanka_telefon_numarasi_gecerli_mi(telefon))
