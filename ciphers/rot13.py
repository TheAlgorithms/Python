def dencrypt(s: str, n: int = 13) -> str:
    """
    https://en.wikipedia.org/wiki/ROT13

    >>> msg = "My secret bank account number is 173-52946 so don't tell anyone!!"
    >>> s = dencrypt(msg)
    >>> s
    "Zl frperg onax nppbhag ahzore vf 173-52946 fb qba'g gryy nalbar!!"
    >>> dencrypt(s) == msg
    True
    """
    out = ""
    for c in s:
        if ord(c) in range(65, 91):
            out += chr(ord("A") + (ord(c) - ord("A") + n) % 26)
        elif ord(c) in range(97, 123):
            out += chr(ord("a") + (ord(c) - ord("a") + n) % 26)
        else:
            out += c
    return out


def main() -> None:
    s0 = input("Enter message: ")

    s1 = dencrypt(s0, 13)
    print("Encryption:", s1)

    s2 = dencrypt(s1, 13)
    print("Decryption: ", s2)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
    main()
