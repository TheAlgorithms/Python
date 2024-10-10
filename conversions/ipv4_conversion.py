# https://www.geeksforgeeks.org/convert-ip-address-to-integer-and-vice-versa/

def ipv4_to_decimal(ipv4_address: str) -> int:
    """

    Organiser: K. Umut Araz

    Bir IPv4 adresini ondalık temsil biçimine dönüştürür.

    Args:
        ipv4_address: Bir IPv4 adresini temsil eden bir dize (örneğin, "192.168.0.1").

    Returns:
        int: IP adresinin ondalık temsil biçimi.

    >>> ipv4_to_decimal("192.168.0.1")
    3232235521
    >>> ipv4_to_decimal("10.0.0.255")
    167772415
    >>> ipv4_to_decimal("10.0.255")
    Traceback (most recent call last):
        ...
    ValueError: Geçersiz IPv4 adres formatı
    >>> ipv4_to_decimal("10.0.0.256")
    Traceback (most recent call last):
        ...s
    ValueError: Geçersiz IPv4 okteti 256
    """

    oktetler = [int(octet) for octet in ipv4_address.split(".")]
    if len(oktetler) != 4:
        raise ValueError("Geçersiz IPv4 adres formatı")

    decimal_ipv4 = 0
    for oktet in oktetler:
        if not 0 <= oktet <= 255:
            raise ValueError(f"Geçersiz IPv4 okteti {oktet}")  # noqa: EM102
        decimal_ipv4 = (decimal_ipv4 << 8) + int(oktet)

    return decimal_ipv4


def alt_ipv4_to_decimal(ipv4_address: str) -> int:
    """
    Alternatif bir yöntemle IPv4 adresini ondalık sayıya dönüştürür.

    >>> alt_ipv4_to_decimal("192.168.0.1")
    3232235521
    >>> alt_ipv4_to_decimal("10.0.0.255")
    167772415
    """
    return int("0x" + "".join(f"{int(i):02x}" for i in ipv4_address.split(".")), 16)


def decimal_to_ipv4(decimal_ipv4: int) -> str:
    """
    Bir IP adresinin ondalık temsilini IPv4 formatına dönüştürür.

    Args:
        decimal_ipv4: Ondalık IP adresini temsil eden bir tamsayı.

    Returns:
        Ondalık IP adresinin IPv4 temsil biçimi.

    >>> decimal_to_ipv4(3232235521)
    '192.168.0.1'
    >>> decimal_to_ipv4(167772415)
    '10.0.0.255'
    >>> decimal_to_ipv4(-1)
    Traceback (most recent call last):
        ...
    ValueError: Geçersiz ondalık IPv4 adresi
    """

    if not (0 <= decimal_ipv4 <= 4294967295):
        raise ValueError("Geçersiz ondalık IPv4 adresi")

    ip_bolumleri = []
    for _ in range(4):
        ip_bolumleri.append(str(decimal_ipv4 & 255))
        decimal_ipv4 >>= 8

    return ".".join(reversed(ip_bolumleri))


if __name__ == "__main__":
    import doctest

    doctest.testmod()
