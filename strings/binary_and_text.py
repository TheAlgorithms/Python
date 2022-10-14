def text_to_binary(text: str) -> str:
    """
    Converts any string to binary

    >>> text_to_binary('A')
    '1000001'

    >>> text_to_binary('Dexter')
    '1000100 1100101 1111000 1110100 1100101 1110010'

    >>> text_to_binary('❤️')
    '10011101100100 1111111000001111'
    """
    return " ".join(map(lambda char: bin(ord(char))[2:], text))


def binary_to_text(binary: str) -> str:
    """
    Converts any binary to string

    >>> binary_to_text('1000001')
    'A'

    >>> binary_to_text('1000100 1100101 1111000 1110100 1100101 1110010')
    'Dexter'

    >>> binary_to_text('10011101100100 1111111000001111')
    '❤️'
    """
    return "".join(map(lambda bin_text: chr(int(bin_text, base=2)), binary.split()))


if __name__ == "__main__":
    while True:
        string = input(
            """Choose from below options : [1,2]
    1. Convert text to binary
    2. Convert binary to text
    3. Cancel\n: """
        )
        if string == "1":
            print(
                "RESULT :\033[92m",
                text_to_binary(input("Enter the string to convert: ")),
                end="\033[0m\n\n",
            )
        elif string == "2":
            print(
                "RESULT :\033[92m",
                binary_to_text(input("Enter the binary string to convert: ")),
                end="\033[0m\n\n",
            )
        elif string == "3":
            exit()
        else:
            print("\033[91mPlease enter a valid input.", end="\033[0m\n\n")
