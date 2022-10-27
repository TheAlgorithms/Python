import re


def is_valid_ipv4_address(address: str) -> bool:
    """
    Determine whether a string is a valid ipv4 address or not
    >>> is_valid_ipv4_address('10.93.2.145')
    True
    >>> is_valid_ipv4_address('128.75.80.99')
    True
    >>> is_valid_ipv4_address('255.255.255.255')
    True
    >>> is_valid_ipv4_address('192.32.64.0')
    True
    >>> is_valid_ipv4_address('10.5.9.1')
    True
    >>> is_valid_ipv4_address('01.023.035.089')
    True
    >>> is_valid_ipv4_address('0192.065.032.012')
    True
    >>> is_valid_ipv4_address('0192.65.032.12')
    True
    >>> is_valid_ipv4_address('255.255.198.256')
    False
    >>> is_valid_ipv4_address('175.45.21.20.2')
    False
    >>> is_valid_ipv4_address('100.90.88.-1')
    False
    >>> is_valid_ipv4_address('70.102.2')
    False
    >>> is_valid_ipv4_address('191.70.32.1.3')
    False
    """
    pattern = re.compile(r"^(0?(25[0-5]|(2[0-4]|1\d|[1-9]|)\d)(\.(?!$)|$)){4}$")

    return bool(re.search(pattern, address))


if __name__ == "__main__":
    address = input("Enter an IPv4 address: ").strip()
    print(is_valid_ipv4_address(address))
