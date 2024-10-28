def dencrypt(s: str) -> str:
    """
    Applies the ROT13 cipher to the input string, `s`, shifting each alphabetic character 
    by 13 positions within the alphabet. This cipher is symmetrical, meaning applying it 
    twice returns the original text. Non-alphabet characters are left unchanged.

    https://en.wikipedia.org/wiki/ROT13

    Args:
        s (str): The input string to be encoded/decoded using ROT13.

    Returns:
        str: The encoded/decoded string after applying the ROT13 transformation.

    Raises:
        TypeError: If the input `s` is not a string.

    >>> msg = "My secret bank account number is 173-52946 so don't tell anyone!!"
    >>> s = dencrypt(msg)
    >>> s
    "Zl frperg onax nppbhag ahzore vf 173-52946 fb qba'g gryy nalbar!!"
    >>> dencrypt(s) == msg
    True
    
    """
    if not isinstance(s, str):
        raise TypeError("Input must be a string.")
    
    out = []
    for c in s:
        if "A" <= c <= "Z":
            out.append(chr(ord("A") + (ord(c) - ord("A") + 13) % 26))
        elif "a" <= c <= "z":
            out.append(chr(ord("a") + (ord(c) - ord("a") + 13) % 26))
        else:
            out.append(c)
    return ''.join(out)


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
