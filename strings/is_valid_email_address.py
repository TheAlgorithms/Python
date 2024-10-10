"""
Geçerli bir e-posta adresi algoritması uygular

Organiser: K. Umut Araz

@ https://en.wikipedia.org/wiki/Email_address
"""

import string

email_tests: tuple[tuple[str, bool], ...] = (
    ("simple@example.com", True),
    ("very.common@example.com", True),
    ("disposable.style.email.with+symbol@example.com", True),
    ("other-email-with-hyphen@and.subdomains.example.com", True),
    ("fully-qualified-domain@example.com", True),
    ("user.name+tag+sorting@example.com", True),
    ("x@example.com", True),
    ("example-indeed@strange-example.com", True),
    ("test/test@test.com", True),
    (
        "123456789012345678901234567890123456789012345678901234567890123@example.com",
        True,
    ),
    ("admin@mailserver1", True),
    ("example@s.example", True),
    ("Abc.example.com", False),
    ("A@b@c@example.com", False),
    ("abc@example..com", False),
    ("a(c)d,e:f;g<h>i[j\\k]l@example.com", False),
    (
        "12345678901234567890123456789012345678901234567890123456789012345@example.com",
        False,
    ),
    ("i.like.underscores@but_its_not_allowed_in_this_part", False),
    ("", False),
)

# Yerel kısım ve alan adı kısmının alabileceği maksimum oktet sayısı
MAX_LOCAL_PART_OCTETS = 64
MAX_DOMAIN_OCTETS = 255


def is_valid_email_address(email: str) -> bool:
    """
    Geçerli bir e-posta adresi olup olmadığını kontrol eder.

    E-postanın yerel kısmı, tekil @ sembolünden önce gelir ve
    bir görüntü adı ile ilişkilidir. Örneğin, "john.smith"
    Alan adı, yerel kısımdan daha katıdır ve @ sembolünden sonra gelir.

    Genel e-posta kontrolleri:
     1. E-posta adresinde yalnızca bir @ sembolü olmalıdır. Teknik olarak, eğer
        @ sembolü yerel kısımda tırnak içinde ise geçerlidir, ancak bu
        uygulama şu anda ""'yi göz ardı etmektedir.
        (Bkz. https://en.wikipedia.org/wiki/Email_address#:~:text=If%20quoted,)
     2. Yerel kısım ve alan adı belirli bir oktet sayısı ile sınırlıdır. Unicode
        bir karakteri bir bayt olarak sakladığı için, her oktet bir
        karakterle eşdeğerdir. Bu nedenle, yalnızca dize uzunluğunu kontrol edebiliriz.
    Yerel kısım için kontroller:
     3. Yerel kısım şunları içerebilir: büyük ve küçük Latin harfleri, 0'dan 9'a kadar
        rakamlar ve yazdırılabilir karakterler (!#$%&'*+-/=?^_`{|}~)
     4. Yerel kısım, ilk veya son karakter olmayan herhangi bir yerde "." içerebilir
        ve ardışık olarak birden fazla "." bulunduramaz.

    Alan adı için kontroller:
     5. Alan adı şunları içerebilir: büyük ve küçük Latin harfleri ve 0'dan 9'a kadar
        rakamlar
     6. Tire "-", ilk veya son karakter olmamak kaydıyla
     7. Alan adı, ilk veya son karakter olmayan herhangi bir yerde "." içerebilir
        ve ardışık olarak birden fazla "." bulunduramaz.

    >>> for email, valid in email_tests:
    ...     assert is_valid_email_address(email) == valid
    """

    # (1.) E-posta adresinde yalnızca bir @ sembolü olduğundan emin olun
    if email.count("@") != 1:
        return False

    local_part, domain = email.split("@")
    # (2.) Yerel kısım ve alan adı için oktet uzunluğunu kontrol et
    if len(local_part) > MAX_LOCAL_PART_OCTETS or len(domain) > MAX_DOMAIN_OCTETS:
        return False

    # (3.) Yerel kısımda karakterleri doğrula
    if any(
        char not in string.ascii_letters + string.digits + ".(!#$%&'*+-/=?^_`{|}~)"
        for char in local_part
    ):
        return False

    # (4.) Yerel kısımda "." karakterlerinin yerleşimini doğrula
    if local_part.startswith(".") or local_part.endswith(".") or ".." in local_part:
        return False

    # (5.) Alan adındaki karakterleri doğrula
    if any(char not in string.ascii_letters + string.digits + ".-" for char in domain):
        return False

    # (6.) Alan adındaki "-" karakterlerinin yerleşimini doğrula
    if domain.startswith("-") or domain.endswith("."):
        return False

    # (7.) Alan adındaki "." karakterlerinin yerleşimini doğrula
    return not (domain.startswith(".") or domain.endswith(".") or ".." in domain)


if __name__ == "__main__":
    import doctest

    doctest.testmod()

    for email, valid in email_tests:
        is_valid = is_valid_email_address(email)
        assert is_valid == valid, f"{email} geçerli değil, durum: {is_valid}"
        print(f"E-posta adresi {email} {'geçersiz' if not is_valid else 'geçerli'}")
