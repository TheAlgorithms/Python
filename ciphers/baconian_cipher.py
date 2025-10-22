encode_dict = {
    "a": "AAAAA",
    "b": "AAAAB",
    "c": "AAABA",
    "d": "AAABB",
    "e": "AABAA",
    "f": "AABAB",
    "g": "AABBA",
    "h": "AABBB",
    "i": "ABAAA",
    "j": "BBBAA",
    "k": "ABAAB",
    "l": "ABABA",
    "m": "ABABB",
    "n": "ABBAA",
    "o": "ABBAB",
    "p": "ABBBA",
    "q": "ABBBB",
    "r": "BAAAA",
    "s": "BAAAB",
    "t": "BAABA",
    "u": "BAABB",
    "v": "BBBAB",
    "w": "BABAA",
    "x": "BABAB",
    "y": "BABBA",
    "z": "BABBB",
    " ": " ",
}

decode_dict = {value: key for key, value in encode_dict.items()}

def encode(word: str, symbols=("A","B")) -> str:
    a_sym, b_sym = symbols
    encoded = ""
    for letter in word.lower():
        if letter.isalpha() or letter == " ":
            # replace A with a_symbol, B with b_symbol
            bacon = encode_dict[letter]
            bacon_custom = bacon.replace("A", a_sym).replace("B", b_sym)
            encoded += bacon_custom
        else:
            raise Exception("encode() accepts only letters of the alphabet and spaces")
    return encoded

def decode(coded: str, symbols=("A","B")) -> str:
    sym1, sym2 = symbols
    #  check if we need to remap
    unique_symbols = set(coded.replace(" ", ""))
    if unique_symbols - {sym1, sym2} != set():
        raise Exception(f"decode() accepts only symbols {sym1} and {sym2} and spaces")
    
    # Try both mappings: symbol1 maps to A, symbol2 maps to B or symbol1 maps to B, symbol2 maps A
    candidates = []
    for mapping in [(sym1, sym2), (sym2, sym1)]:
        s1, s2 = mapping
        # convert coded symbols to standard A/B
        standard = coded.replace(s1, "A").replace(s2, "B")
        try:
            decoded = ""
            for word in standard.split():
                while len(word) != 0:
                    chunk = word[:5]
                    if chunk not in decode_dict:
                        raise ValueError
                    decoded += decode_dict[chunk]
                    word = word[5:]
                decoded += " "
            candidates.append(decoded.strip())
        except ValueError:
            candidates.append(None)
    
    # return the valid decoding
    for candidate in candidates:
        if candidate is not None:
            return candidate
    raise Exception("No valid decoding found with the given symbols")
def detect_unique_char (cipher):
    #CD CD DC returns C, D
    cipher = cipher.replace(" ","")
    unique_chars = set(cipher)
    unique_letters = [char for char in unique_chars if char.isalpha()]
    if len(unique_letters) != 2:
        raise Exception("Cipher must contain exactly two unique alphabetic characters for encoding.")
    else:
        list_unique = list(unique_letters)
        return list_unique[0], list_unique[1]

if __name__ == "__main__":
    # Example usage
    cipher_text = "FEEFE EEFFF EEFEE EFFFF FEEFF EFEEE EEEFE EFEEF EEEEF FEEEE EFFEF FEFEE EFFEE EEFEF EFFEF FEFEF"
    symbol_1, symbol_2 = detect_unique_char(cipher_text)
    decoded = decode(cipher_text, symbols=(symbol_1, symbol_2))
    print(decoded)  # prints the quick brown fox
