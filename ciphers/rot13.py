def dencrypt(s: str) -> str:
    """
    Performs ROT13 encryption/decryption on the input string `s`.

    https://en.wikipedia.org/wiki/ROT13

    >>> msg = "My secret bank account number is 173-52946 so don't tell anyone!!"
    >>> s = dencrypt(msg)
    >>> s
    "Zl frperg onax nppbhag ahzore vf 173-52946 fb qba'g gryy nalbar!!"
    >>> dencrypt(s) == msg
    True
    """
    # Validate input
    assert isinstance(s, str), "Input must be a string"

    # Using list to accumulate characters for efficiency
    out = []
    for c in s:
        if "A" <= c <= "Z":
            out.append(chr(ord("A") + (ord(c) - ord("A") + 13) % 26))
        elif "a" <= c <= "z":
            out.append(chr(ord("a") + (ord(c) - ord("a") + 13) % 26))
        else:
            out.append(c)
    return "".join(out)


def main() -> None:
    s0 = input("Enter message: ")

    s1 = dencrypt(s0)
    print("Encryption:", s1)

    s2 = dencrypt(s1)
    print("Decryption:", s2)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
    main()
