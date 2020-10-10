import compression.lzw.symbol_generator as symbol_generator


def generate_initial_dictionary():
    """
    Generate an initial dictionary to be used for encoder and decoder.

    The dictionary holds all the encoding of single "letters" in the vocabulary that
    the encoder and decoder can understand, and it must be the same for both the
    encoder and decoder.

    This implementation creates a dictionary with only the capital english letters.
    It's useful for testing, but not much more.

    :return: a dict mapping each possible input "letter" to its encoded Symbol
    """
    symbol = symbol_generator.SymbolGenerator(1, 5)
    alphabet = [
        "A",
        "B",
        "C",
        "D",
        "E",
        "F",
        "G",
        "H",
        "I",
        "J",
        "K",
        "L",
        "M",
        "N",
        "O",
        "P",
        "Q",
        "R",
        "S",
        "T",
        "U",
        "V",
        "W",
        "X",
        "Y",
        "Z",
    ]

    initial_dictionary = {letter: next(symbol) for letter in alphabet}

    return initial_dictionary, symbol
