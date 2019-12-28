def encode_base64(text):
    r"""
    >>> encode_base64('WELCOME to base64 encoding 😁')
    'V0VMQ09NRSB0byBiYXNlNjQgZW5jb2Rpbmcg8J+YgQ=='
    >>> encode_base64('AÅᐃ𐀏🤓')
    'QcOF4ZCD8JCAj/CfpJM='
    >>> encode_base64('A'*60)
    'QUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFB\r\nQUFB'
    """
    base64_chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"

    byte_text = bytes(text, "utf-8")  # put text in bytes for unicode support
    r = ""  # the result
    c = -len(byte_text) % 3  # the length of padding
    p = "=" * c  # the padding
    s = byte_text + b"\x00" * c  # the text to encode

    i = 0
    while i < len(s):
        if i > 0 and ((i / 3 * 4) % 76) == 0:
            r = r + "\r\n"  # for unix newline, put "\n"

        n = (s[i] << 16) + (s[i + 1] << 8) + s[i + 2]

        n1 = (n >> 18) & 63
        n2 = (n >> 12) & 63
        n3 = (n >> 6) & 63
        n4 = n & 63

        r += base64_chars[n1] + base64_chars[n2] + base64_chars[n3] + base64_chars[n4]
        i += 3

    return r[0 : len(r) - len(p)] + p


def decode_base64(text):
    r"""
    >>> decode_base64('V0VMQ09NRSB0byBiYXNlNjQgZW5jb2Rpbmcg8J+YgQ==')
    'WELCOME to base64 encoding 😁'
    >>> decode_base64('QcOF4ZCD8JCAj/CfpJM=')
    'AÅᐃ𐀏🤓'
    >>> decode_base64("QUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFB\r\nQUFB")
    'AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA'
    """
    base64_chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"
    s = ""

    for i in text:
        if i in base64_chars:
            s += i
            c = ""
        else:
            if i == "=":
                c += "="

    p = ""
    if c == "=":
        p = "A"
    else:
        if c == "==":
            p = "AA"

    r = b""
    s = s + p

    i = 0
    while i < len(s):
        n = (
            (base64_chars.index(s[i]) << 18)
            + (base64_chars.index(s[i + 1]) << 12)
            + (base64_chars.index(s[i + 2]) << 6)
            + base64_chars.index(s[i + 3])
        )

        r += bytes([(n >> 16) & 255]) + bytes([(n >> 8) & 255]) + bytes([n & 255])

        i += 4

    return str(r[0 : len(r) - len(p)], "utf-8")


def main():
    print(encode_base64("WELCOME to base64 encoding 😁"))
    print(decode_base64(encode_base64("WELCOME to base64 encoding 😁")))


if __name__ == "__main__":
    main()
