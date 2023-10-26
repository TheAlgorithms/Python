# https://www.geeksforgeeks.org/convert-ip-address-to-integer-and-vice-versa/


def ip_to_decimal(ip_address: str) -> int:
    """
    Convert an IPv4 address to its decimal representation.

    Args:
        ip_address (str): A string representing an IPv4 address (e.g., "192.168.0.1").

    Returns:
        int: The decimal representation of the IP address.

    >>> ip_to_decimal("192.168.0.1")
    3232235521
    >>> ip_to_decimal("10.0.0.255")
    167772415
    """

    octets = ip_address.split(".")
    if len(ip_parts) != 4:
        raise ValueError("Invalid IPv4 address format")

    decimal_ip = 0
    for part in ip_parts:
        decimal_ip = (decimal_ip << 8) + int(part)

    return decimal_ip


def decimal_to_ip(decimal_ip: int) -> str:
    """
    Convert a decimal representation of an IP address to its IPv4 format.

    Args:
        decimal_ip (int): An integer representing the decimal IP address.

    Returns:
        str: The IPv4 representation of the decimal IP address.

    >>> decimal_to_ip(3232235521)
    '192.168.0.1'
    >>> decimal_to_ip(167772415)
    '10.0.0.255'
    """

    if not (0 <= decimal_ip <= 4294967295):
        raise ValueError("Invalid decimal IP address")

    ip_parts = []
    for _ in range(4):
        ip_parts.append(str(decimal_ip & 255))
        decimal_ip >>= 8

    ip_parts.reverse()
    return ".".join(ip_parts)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
