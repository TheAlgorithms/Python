import heapq
from collections import defaultdict
import sys


class HuffmanNode:
    def __init__(self, char=None, freq=0):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.freq < other.freq


def calculate_frequencies(file_path):
    """
    Reads the file and calculates the frequency of each character.
    """
    freq = defaultdict(int)
    with open(file_path, "r") as file:
        for line in file:
            for char in line:
                freq[char] += 1
    return freq


def build_huffman_tree(freq_dict):
    """
    Builds the Huffman tree using a priority queue.
    """
    priority_queue = [HuffmanNode(char, freq) for char, freq in freq_dict.items()]
    heapq.heapify(priority_queue)

    while len(priority_queue) > 1:
        left = heapq.heappop(priority_queue)
        right = heapq.heappop(priority_queue)

        merged = HuffmanNode(freq=left.freq + right.freq)
        merged.left = left
        merged.right = right

        heapq.heappush(priority_queue, merged)

    return priority_queue[0]


def generate_codes(node, current_code="", code_map=None):
    """
    Generates the Huffman codes by traversing the tree recursively.
    """
    if code_map is None:
        code_map = {}

    if node is not None:
        if node.char is not None:
            code_map[node.char] = current_code

        generate_codes(node.left, current_code + "0", code_map)
        generate_codes(node.right, current_code + "1", code_map)

    return code_map


def encode_file(file_path, code_map):
    """
    Encodes the file contents using the Huffman codes.
    """
    encoded_output = []
    with open(file_path, "r") as file:
        for line in file:
            for char in line:
                encoded_output.append(code_map[char])

    return "".join(encoded_output)


def huffman(file_path):
    """
    Main function to perform Huffman encoding on a given file.
    """
    freq_dict = calculate_frequencies(file_path)
    huffman_tree_root = build_huffman_tree(freq_dict)
    code_map = generate_codes(huffman_tree_root)

    print(f"Huffman Codes for characters in {file_path}:")
    for char, code in code_map.items():
        print(f"'{char}': {code}")

    encoded_data = encode_file(file_path, code_map)
    print("\nEncoded Data:")
    print(encoded_data)


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python huffman.py <file_path>")
    else:
        huffman(sys.argv[1])
