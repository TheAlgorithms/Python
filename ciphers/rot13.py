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
    s0 = input("Enter message: ")

    s1 = dencrypt(s0, 13)
    print("Encryption: "+s1)  

    s2 = dencrypt(s1, 13)
    print("Decryption: "+s2)  


if __name__ == "__main__":
    main()
