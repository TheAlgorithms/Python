"""
wiki: https://en.wikipedia.org/wiki/IPv4

Is IP v4 address valid?
A valid IP address must be four numbers in the form of A.B.C.D,
where A,B,C and D are numbers from 0-255

for example:
    192.168.23.1, 172.254.254.254 are valid IP address
    192.168.01.0, 256.192.3.121 are invalid IP address
"""


def is_ip_v4_address_valid(ip: str) -> bool:
    """
    print "Valid IP address" If IP is valid.
    or
    print "Invalid IP address" If IP is invalid.

    >>> is_ip_v4_address_valid("192.168.0.23")
    True

    >>> is_ip_v4_address_valid("192.255.15.8")
    True

    >>> is_ip_v4_address_valid("172.100.0.8")
    True

    >>> is_ip_v4_address_valid("0.0.0.0")
    True

    >>> is_ip_v4_address_valid("254.256.0.255")
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

    >>> is_ip_v4_address_valid("1.2.3.05")
    False
    """

    parts = ip.split('.')

    if len(parts) != 4:
        return False
    
    for part in parts:
        if not part:
            return False
        
        for i in range(len(part)):
            if not part[i].isdigit():
                return False

        if part[0] == '0' and len(part) > 1:
            return False
        
        if not (0 <= int(part) <= 255):  
            return False
    
    return True


if __name__ == "__main__":
    ip = input().strip()
    result = "valid" if is_ip_v4_address_valid(ip) else "invalid"
    print(f"{ip} is a {result} IPv4 address.")
