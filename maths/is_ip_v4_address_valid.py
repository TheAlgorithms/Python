"""
Is IP v4 address valid?
A valid IP address must be four octets in the form of A.B.C.D,
where A,B,C and D are numbers from 0-254
for example: 192.168.23.1, 172.254.254.254 are valid IP address
             192.168.255.0, 255.192.3.121 are invalid IP address
"""


def is_ip_v4_address_valid(ip_v4_address: str) -> bool:
    """
    print "Valid IP address" If IP is valid.
    or
    print "Invalid IP address" If IP is invalid.

    >>> is_ip_v4_address_valid("192.168.0.23")
    True

    >>> is_ip_v4_address_valid("192.255.15.8")
    False

    >>> is_ip_v4_address_valid("172.100.0.8")
    True

    >>> is_ip_v4_address_valid("254.255.0.255")
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
    """
    octets = [int(i) for i in ip_v4_address.split(".") if i.isdigit()]
    return len(octets) == 4 and all(0 <= int(octet) <= 254 for octet in octets)


if __name__ == "__main__":
    ip = input().strip()
    valid_or_invalid = "valid" if is_ip_v4_address_valid(ip) else "invalid"
    print(f"{ip} is a {valid_or_invalid} IP v4 address.")
