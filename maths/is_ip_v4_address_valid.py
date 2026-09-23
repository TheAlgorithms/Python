"""
wiki: https://en.wikipedia.org/wiki/IPv4

Is IP v4 address valid?
A valid IP address must be four octets in the form of A.B.C.D,
where A, B, C and D are numbers from 0-255
for example: 192.168.23.1, 172.255.255.255 are valid IP address
             192.168.256.0, 256.192.3.121 are invalid IP address
"""


def is_ip_v4_address_valid(ip: str) -> bool:
    """
    print "Valid IP address" If IP is valid.
    or
    print "Invalid IP address" If IP is invalid.

    >>> is_ip_v4_address_valid("192.168.0.23")
    True

    >>> is_ip_v4_address_valid("192.256.15.8")
    False

    >>> is_ip_v4_address_valid("172.100.0.8")
    True

    >>> is_ip_v4_address_valid("255.256.0.256")
    False

    >>> is_ip_v4_address_valid("1.2.33333333.4")
    False

    >>> is_ip_v4_address_valid("1.2.-3.4")
    False

    >>> is_ip_v4_address_valid("1.2.3")
    False

    >>> is_ip_v4_address_valid("1.2.3.4.5")
    False

    >>> is_ip_v4_address_valid("1.2.A.4")
    False

    >>> is_ip_v4_address_valid("0.0.0.0")
    True

    >>> is_ip_v4_address_valid("1.2.3.")
    False

    >>> is_ip_v4_address_valid("1.2.3.05")
    False
    """
    octets = ip.split(".")
    if len(octets) != 4:
        return False

    for octet in octets:
        if not octet.isdigit():
            return False

        number = int(octet)
        if len(str(number)) != len(octet):
            return False

        if not 0 <= number <= 255:
            return False

    return True


if __name__ == "__main__":
    ip = input().strip()
    valid_or_invalid = "valid" if is_ip_v4_address_valid(ip) else "invalid"
    print(f"{ip} is a {valid_or_invalid} IPv4 address.")
