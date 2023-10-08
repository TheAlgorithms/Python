import argparse


class TwinHexEncoder:
    cbase = [chr(x) + chr(y) for x in range(32, 128) for y in range(32, 128)]
    alphabet = "0123456789abcdefghijklmnopqrstuvwxyz"

    def base36encode(self, number):
        if not isinstance(number, (int)):
            raise TypeError("must be an integer")
        if number < 0:
            raise ValueError("must be positive")
        encoded_string = ""
        while number:
            number, i = divmod(number, 36)
            encoded_string = self.alphabet[i] + encoded_string
        return encoded_string or self.alphabet[0]

    def encrypt(self, char):
        flag_out = ""
        for i in range(0, len(char), 2):
            pair = char[i : i + 2]
            if len(pair) < 2:
                pair += " "
            flag_out += self.base36encode(self.cbase.index(pair)).ljust(3, " ")
        return flag_out


class TwinHexDecoder:
    cbase = [chr(x) + chr(y) for x in range(32, 128) for y in range(32, 128)]

    def decrypt(self, char):
        flag_out = ""
        try:
            triples = [char[i : i + 3] for i in range(0, len(char), 3)]
            flag_out += "".join(self.cbase[int(x, 36)] for x in triples if x.strip())
        except Exception as e:
            exit(f"Error: {str(e)}")
        return flag_out


def main():
    print(
        """
          Twin-Hex Cipher Encoder/Decoder
    """
    )
    parser = argparse.ArgumentParser(
        description="Script for Encoding/Decoding Twin-Hex Cipher"
    )
    parser.add_argument("-d", "--decode", action="store_true", help="Decode Twin-Hex")
    parser.add_argument(
        "-e", "--encode", action="store_true", help="Encode to Twin-Hex"
    )
    parser.add_argument("text", nargs="?")
    args = parser.parse_args()

    if args.text:
        if args.decode:
            print(f"Decoded Flag: {TwinHexDecoder().decrypt(args.text)}")
        elif args.encode:
            print(f"Encoded Flag: {TwinHexEncoder().encrypt(args.text)}")
        else:
            exit("[!] Provide either --encode or --decode argument")
    else:
        exit("usage: twin_cipher.py [-h] [-d] [-e] [text]")


if __name__ == "__main__":
    main()
