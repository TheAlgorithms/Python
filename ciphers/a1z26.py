"""

Converts a string of characters to a sequence of numbers corresponding to the character's position in the alphabet.

Information URLs:
https://www.dcode.fr/letter-number-cipher
http://bestcodes.weebly.com/a1z26.html
"""

def encode(plain : str) -> list:
    """
    >>> encode("myname")
    [13, 25, 14, 1, 13, 5]
    """
    return [ord(elem) - 96 for elem in plain]

def decode(encoded : list) -> str:
    """
    >>> decode([13, 25, 14, 1, 13, 5])
    'myname'
    """
    return "".join(map(lambda elem : chr(elem + 96), encoded))

def main():
    inp = input("->")
    lowered = inp.lower()
    encoded = encode(lowered)
    print("Encoded: ", encoded)
    decoded = decode(encoded)
    print("Decoded:", decoded)

if __name__ == "__main__":
    main()
