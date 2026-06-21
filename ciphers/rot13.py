def dencrypt(s: str) -> str:
    """
    Applies ROT13 encryption or decryption to the input string.

    Example usage:
    >>> msg = "My secret bank account number is 173-52946 so don't tell anyone!!"
    >>> encrypted = dencrypt(msg)
    >>> encrypted
    "Zl frperg onax nppbhag ahzore vf 173-52946 fb qba'g gryy nalbar!!"
    >>> dencrypt(encrypted) == msg
    True
    """
    result = []
    for c in s:
        if "A" <= c <= "Z":
            result.append(chr(ord("A") + (ord(c) - ord("A") + 13) % 26))
        elif "a" <= c <= "z":
            result.append(chr(ord("a") + (ord(c) - ord("a") + 13) % 26))
        else:
            result.append(c)
    return "".join(result)


def main() -> None:
    s0 = input("Enter message: ")

    s1 = dencrypt(s0)
    print("Encryption:", s1)

    s2 = dencrypt(s1)
    print("Decryption: ", s2)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
    main()
