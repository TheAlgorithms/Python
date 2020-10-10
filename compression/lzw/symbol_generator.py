import compression.lzw.symbol as symbol


class SymbolGenerator:
    def __init__(self, initial_value: int, initial_bits: int):
        symbol.Symbol.from_int(
            initial_value, initial_bits
        )  # raises if initial_bits are not enough to encode the value
        self._next_value = initial_value
        self._bits = initial_bits

    @property
    def current_bit_length(self):
        return self._bits

    @property
    def next_bit_length(self):
        return self._next_value.bit_length()

    def __iter__(self):
        return self

    def __next__(self):
        while True:
            try:
                ret = symbol.Symbol.from_int(self._next_value, self._bits)
                self._next_value += 1
                return ret
            except OverflowError:
                self._bits += 1
