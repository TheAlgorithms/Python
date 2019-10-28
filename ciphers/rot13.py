def dencrypt(s, n):
    out = ""
    for c in s:
        if c >= "A" and c <= "Z":
            out += chr(ord("A") + (ord(c) - ord("A") + n) % 26)
        elif c >= "a" and c <= "z":
            out += chr(ord("a") + (ord(c) - ord("a") + n) % 26)
        else:
            out += c
    return out


def main():
    s0 = "HELLO"

    s1 = dencrypt(s0, 13)
    print(s1)  # URYYB

    s2 = dencrypt(s1, 13)
    print(s2)  # HELLO


if __name__ == "__main__":
    main()
