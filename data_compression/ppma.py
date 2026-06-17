"""
PPMA (Prediction by Partial Matching) is a statistical data compression technique
    - it is using context to predict the next symbol
    - output of this class should be handled to arithmetic coder for final compression
    - it has more version like PPMB or PPMC (this is PPMA)
    - version only difference is in how they handle escape symbol
    - it was first introduced by Clearly and Witten in 1984 in article
        'Data Compression Using Adaptive Coding and PartialString Matching'
    - unfortunately article is not available online for free
    - https://en.wikipedia.org/wiki/Prediction_by_partial_matching
    - https://www.mbit.edu.in/wp-content/uploads/2020/05/data_compression.pdf
        (chapter 6.3)

Output is divided into 2 parts:
    - readable_output: list of dictionaries with information about the symbol, context,
        order and probability, this is for better understanding of the process
    - ranges: list of tuples with low, high and total count for arithmetic coder

Doctest note:
    - the output is very long even for short input strings, so it is not possible
        to test the whole output
    - the output were tested and are correct (it was part of my course on university)
"""

from collections import defaultdict


class PPMA:
    """
    Core class for PPM compression algorithm containing compression and decompression.
    """

    def __init__(self, max_order: int = 2, alphabet_size: int = 256) -> None:
        self.max_order = max_order
        self.alphabet_size = alphabet_size
        self.history = ""

        # context is list of dictionary inside a dictionary
        #   - outer dictionary stores all context of given order
        #   - inner dictionary stores following symbol and their counts
        self.contexts = [
            defaultdict(lambda: defaultdict(int)) for _ in range(max_order + 1)
        ]

    def encode_text(self, text: str) -> dict:
        """
        Process whole input text and return list of actions and ranges for arithmetic
        coder.
        """

        self.__reset_memory()
        output = []
        output_ranges = []
        for char in text:
            char_output, char_range = self.process_char(char)
            output.extend(char_output)
            output_ranges.extend(char_range)

        return {"readable_output": output, "ranges": output_ranges}

    def decode_text(self, ranges: list) -> str:
        """
        Process the output ranges and decode it to the original text.
        """

        self.__reset_memory()
        decoded_text = ""
        current_order = self.max_order

        for low, high, total in ranges:
            context = self.history[-current_order:] if current_order > 0 else ""

            # 01 - range is -1 which means new symbol
            if total == self.alphabet_size and current_order == -1:
                char = chr(low)
                decoded_text += char
                self._update_models(char)
                # reset to max order after new symbol
                current_order = self.max_order
                continue

            # to ensure the context exists in the model
            counts_dict, total_count = self._get_context_probs(current_order, context)

            # 02 - escape symbol, always [N, N+1, N+1]
            if low == (total_count - 1) and high == total_count:
                # move to lower order context
                current_order -= 1
                continue

            # 03 - known symbol, need to find which char is it
            found_char = None
            current_low = 0
            sorted_symbols = sorted(counts_dict.keys())

            # iterating through symbols (sorted for conssistency) to find the one
            # fitting the range
            for sym in sorted_symbols:
                count = counts_dict[sym]
                if current_low == low and (current_low + count) == high:
                    found_char = sym
                    break
                current_low += count

            if found_char:
                decoded_text += found_char
                # update model with the found character
                self._update_models(found_char)
                # reset to max order after finding symbol
                current_order = self.max_order
            else:
                error_message = f"""This range (low={low}, high={high}, total={total})
                does not fit any symbol."""
                raise ValueError(error_message)

        return decoded_text

    def _get_context_probs(self, order: int, context: str) -> tuple[dict, int]:
        """
        Returns the symbol count and total count for given context and order, including
        the escape symbol.
        """

        # takes right order and select given context
        counts = self.contexts[order][context]
        # +1 for escape symbol
        total_count = sum(counts.values()) + 1

        return dict(counts), total_count

    def process_char(self, char: str) -> tuple:
        """
        Process a single character, update the context, and generate an interval for
        the arithmetic coder.
        """

        output = []
        output_ranges = []
        found = False

        # going from highest order to the lowest and ending on -1 because of
        # possibility of the new symbol
        for order in range(self.max_order, -1, -1):
            context = self.history[-order:] if order > 0 else ""
            symbol_counts, total_count = self._get_context_probs(order, context)

            # 01 - symbol is known in this context
            if char in symbol_counts:
                found = True
                low = 0
                sorted_symbols = sorted(symbol_counts.keys())
                for sym in sorted_symbols:
                    if sym == char:
                        break
                    low += symbol_counts[sym]
                high = low + symbol_counts[char]

                output.append(
                    {
                        "type": "SYMBOL",
                        "order": order,
                        "context": context,
                        "symbol": char,
                        "prob": f"{symbol_counts[char]}/{total_count}",
                    }
                )
                output_ranges.append((low, high, total_count))
                break

            # 02 - symbol is not in context, we need ESCAPE char
            else:
                low = total_count - 1
                high = total_count

                output.append(
                    {
                        "type": "ESCAPE",
                        "order": order,
                        "context": context,
                        "prob": f"1/{total_count}",
                    }
                )
                output_ranges.append((low, high, total_count))

        # symbol is completely new
        if not found:
            output.append(
                {
                    "type": "NEW_SYMBOL",
                    "symbol": char,
                    "prob": f"1/{self.alphabet_size}",
                }
            )
            # the ord() function return the ASCII value of the character
            output_ranges.append((ord(char), ord(char) + 1, self.alphabet_size))

        self._update_models(char)

        return output, output_ranges

    def _update_models(self, char: str) -> None:
        """
        Update the model for all context orders with the new character.
        """

        for order in range(self.max_order + 1):
            context = self.history[-order:] if order > 0 else ""
            self.contexts[order][context][char] += 1

        # sliding window of history
        self.history = (
            (self.history + char)[-self.max_order :] if self.max_order > 0 else ""
        )

    def __reset_memory(self) -> None:
        """
        Clear the history and model so that methods don't leave fragments.
        """

        self.history = ""
        self.contexts = [
            defaultdict(lambda: defaultdict(int)) for _ in range(self.max_order + 1)
        ]

    def __str__(self) -> str:
        """
        Return a string representation of the model for look inside the model.
        """

        return "\n".join(
            f"ORDER {order} ['symbols': context=time_of_occurrence]:\n"
            + "\n".join(
                f"    Context '{ctx}': "
                + ", ".join(f"{sym}={cnt}" for sym, cnt in symbols.items())
                for ctx, symbols in self.contexts[order].items()
            )
            for order in range(self.max_order + 1)
        )


if __name__ == "__main__":
    # Example usage
    ppma = PPMA(max_order=2)
    text = "ABABAB"
    encoded = ppma.encode_text(text)

    print("Encoded output:")
    for item in encoded["readable_output"]:
        print(item)

    print("\nRanges for arithmetic coder:")
    for one_range in encoded["ranges"]:
        print(one_range)

    decoded = ppma.decode_text(encoded["ranges"])
    print("\nDecoded text:", decoded)
