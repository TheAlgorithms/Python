from __future__ import annotations

import sys
from collections import defaultdict

# Description for the ppm algorithm can be found at https://en.wikipedia.org/wiki/Prediction_by_partial_matching


class PPMNode:
    def __init__(self) -> None:
        # Initialize a PPMNode with a dictionary for child nodes
        # and a count of total occurrences
        self.counts: dict[str, PPMNode] = defaultdict(PPMNode)
        self.total: int = 0

    def __repr__(self) -> str:
        return f"PPMNode(total={self.total})"


class PPM:
    def __init__(self, order: int = 2) -> None:
        # Initialize the PPM model with a specified order and create a root node
        self.order: int = order
        self.root: PPMNode = PPMNode()
        self.current_context: PPMNode = self.root

    def update_model(self, context: str, symbol: str) -> None:
        # Update the model with the new symbol in the given context
        node = self.current_context
        for char in context:
            # Traverse through the context characters, updating the total counts
            node = node.counts[char]
            node.total += 1

        # Increment the count for the specific symbol in the current context
        node.counts[symbol].total += 1

    def compress(self, data: str) -> list[float]:
        # Compress the data using the PPM algorithm and return a list of probabilities
        compressed_output: list[float] = []
        context: str = ""

        for symbol in data:
            # Update the model with the current context and symbol
            self.update_model(context, symbol)
            # Encode the symbol based on the current context
            compressed_output.append(self.encode_symbol(context, symbol))
            # Update the context by appending the symbol,
            # keeping it within the specified order
            context = (context + symbol)[-self.order :]  # Keep the context within order

        return compressed_output

    def encode_symbol(self, context: str, symbol: str) -> float:
        # Encode a symbol based on the current context and return its probability
        node = self.root
        for char in context:
            # Traverse through the context to find the corresponding node
            if char in node.counts:
                node = node.counts[char]
            else:
                return 0.0  # Return 0.0 if the context is not found

        # Return the probability of the symbol given the context
        if symbol in node.counts:
            return node.counts[symbol].total / node.total  # Return probability
        return 0.0  # Return 0.0 if the symbol is not found

    def decompress(self, compressed_data: list[float]) -> str:
        # Decompress the compressed data back into the original string
        decompressed_output: list[str] = []
        context: str = ""

        for prob in compressed_data:
            # Decode each probability to retrieve the corresponding symbol
            symbol = self.decode_symbol(context, prob)
            if symbol:
                decompressed_output.append(symbol)
                # Update the context with the newly decoded symbol
                context = (context + symbol)[
                    -self.order :
                ]  # Keep the context within order
            else:
                break  # Stop if a symbol cannot be found

        return "".join(decompressed_output)  # Join the list into a single string

    def decode_symbol(self, context: str, prob: float) -> str | None:
        # Decode a symbol from the given context based on the probability
        node = self.root
        for char in context:
            # Traverse through the context to find the corresponding node
            if char in node.counts:
                node = node.counts[char]
            else:
                return None  # Return None if the context is not found

        # Iterate through the children of the node to
        # find the symbol matching the given probability
        for symbol, child in node.counts.items():
            if child.total / node.total == prob:
                return symbol  # Return the symbol if the probability matches
        return None  # Return None if the symbol is not found


def read_file(file_path: str) -> str:
    """Read the entire file and return its content as a string."""
    with open(file_path) as f:
        return f.read()


def ppm(file_path: str) -> None:
    """Compress and decompress the file using PPM algorithm."""
    data = read_file(file_path)  # Read the data from the specified file
    ppm_instance = PPM(order=2)  # Create an instance of the PPM model with order 2

    # Compress the data using the PPM model
    compressed = ppm_instance.compress(data)
    print("Compressed Data (Prob abilities):", compressed)

    # Decompress the data back to its original form
    decompressed = ppm_instance.decompress(compressed)
    print("Decompressed Data:", decompressed)


if __name__ == "__main__":
    # Check if the correct number of command line arguments is provided
    if len(sys.argv) != 2:
        print("Usage: python ppm.py <file_path>")
        sys.exit(1)

    # Call the ppm function with the provided file path
    ppm(sys.argv[1])
