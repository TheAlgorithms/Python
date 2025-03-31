def apply_rot13(s: str) -> str:
    """
    Performs a special reversible case of the Caesar cipher.
    Rotates a text by 13 letters.
    Also see: https://en.wikipedia.org/wiki/ROT13

    Example usage:
    >>> msg = "My secret bank account number is 173-52946 so don't tell anyone!!"
    >>> s = apply_rot13(msg)
    >>> s
    "Zl frperg onax nppbhag ahzore vf 173-52946 fb qba'g gryy nalbar!!"
    >>> apply_rot13(s) == msg
    True
    """
    if not isinstance(s, str):
        return "The input must be a string. Please try again."
    n = 13
    out = ""
    for c in s:
        if "A" <= c <= "Z":
            out += chr(ord("A") + (ord(c) - ord("A") + n) % 26)
        elif "a" <= c <= "z":
            out += chr(ord("a") + (ord(c) - ord("a") + n) % 26)
        else:
            out += c
    return out


def main() -> None:
    s0 = input("Enter message: ").strip()

    s1 = apply_rot13(s0)
    print("Encryption:", s1)

    s2 = apply_rot13(s1)
    print("Decryption:", s2)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
    main()
