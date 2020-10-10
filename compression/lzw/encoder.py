import compression.lzw.symbol as symbol


class Encoder:
    def __init__(self, alphabet, symbol_generator):
        self._alphabet = alphabet
        self._symbol_generator = symbol_generator
        self._extended_dict = {}

    @property
    def extended_dict(self):
        return self._extended_dict

    def encode(self, uncompressed_input):
        output = symbol.Symbol()
        self._extended_dict = self._alphabet.copy()

        for next_output, next_entry in self._next_output_and_new_entry(
            uncompressed_input
        ):
            output += next_output
            self._update_dict(next_entry)

        return output

    def _find_longest_prefix_in_dict(self, uncompressed_input, dictionary):
        end = len(uncompressed_input)
        while end > 0 and uncompressed_input[:end] not in dictionary:
            end -= 1
        return uncompressed_input[:end]

    def _get_symbol_to_encode(self, prefix):
        return self._extended_dict[prefix].pad_to_len(
            self._symbol_generator.current_bit_length
        )

    def _update_dict(self, entry):
        if entry not in self._extended_dict:
            self._extended_dict[entry] = next(self._symbol_generator)

    def _next_output_and_new_entry(self, uncompressed_input):
        i = 0
        while i < len(uncompressed_input):
            longest_match = self._find_longest_prefix_in_dict(
                uncompressed_input[i:], self._extended_dict
            )
            next_output = self._get_symbol_to_encode(longest_match)
            if i + len(longest_match) < len(uncompressed_input):
                next_entry = longest_match + uncompressed_input[i + len(longest_match)]
            else:
                next_entry = longest_match
            i += len(longest_match)
            yield next_output, next_entry
