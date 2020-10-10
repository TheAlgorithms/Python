class Decoder:
    def __init__(self, alphabet, symbol):
        self._alphabet = alphabet
        self._symbol = symbol
        self._reconstructed_extended_dict = {
            int(symbol): letter for letter, symbol in self._alphabet.copy().items()
        }

    def decode(self, encoded_input):
        output = ""
        last_decoded_symbol = ""
        for current_decoded_symbol in self._decoded_symbols(encoded_input):
            if current_decoded_symbol is None:
                value_to_add = last_decoded_symbol + last_decoded_symbol[0]
                current_decoded_symbol = value_to_add
            else:
                value_to_add = last_decoded_symbol + current_decoded_symbol[0]

            output += current_decoded_symbol
            last_decoded_symbol = current_decoded_symbol

            self._update_dict(value_to_add)
        return output

    def _decoded_symbols(self, encoded_input):
        i = 0
        while i < len(encoded_input):
            symbol_length = self._symbol.next_bit_length
            current_symbol = encoded_input[i : i + symbol_length]
            current_int_symbol = int(current_symbol)
            current_decoded_symbol = self._reconstructed_extended_dict.get(
                current_int_symbol
            )
            i += symbol_length
            yield current_decoded_symbol

    def _update_dict(self, value_to_add):
        if value_to_add not in self._reconstructed_extended_dict.values():
            self._reconstructed_extended_dict[int(next(self._symbol))] = value_to_add
