from __future__ import annotations

import doctest
import sys
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from _typeshed import SupportsWrite


class Letter:
    def __init__(self, letter: str, freq: int):
        self.letter: str = letter
        self.freq: int = freq
        self.bitstring: dict[str, str] = {}

    def __repr__(self) -> str:
        return f"{self.letter}:{self.freq}"


class TreeNode:
    def __init__(self, freq: int, left: Letter | TreeNode, right: Letter | TreeNode):
        self.freq: int = freq
        self.left: Letter | TreeNode = left
        self.right: Letter | TreeNode = right


def parse_string(string: str) -> list[Letter]:
    """
    Return a list of Letter objects storing frequency
    >>> string_in1 = "goose"
    >>> out1 = parse_string(string_in1)
    >>> out1
    [g:1, s:1, e:1, o:2]
    >>> string_in2 = ""
    >>> out2 = parse_string(string_in2)
    >>> out2
    []
    >>> string_in3 = "abbcccd"
    >>> out3 = parse_string(string_in3)
    >>> out3
    [a:1, d:1, b:2, c:3]
    """
    chars: dict[str, Letter] = {}
    for char in string:
        if char not in chars:
            chars[char] = Letter(char, 1)
        else:
            chars[char].freq += 1
    return sorted(chars.values(), key=lambda letter: letter.freq)


def parse_file(file_path: str) -> list[Letter]:
    """
    Read file and return a list of Letter objects storing frequency
    """
    chars: dict[str, Letter] = {}
    with open(file_path) as input_file:
        while char := input_file.read(1):
            if char not in chars:
                chars[char] = Letter(char, 1)
            else:
                chars[char].freq += 1
    return sorted(chars.values(), key=lambda letter: letter.freq)


def build_tree(letters: list[Letter]) -> Letter | TreeNode:
    """
    Build the min heap for the Huffman Tree; return root node
    >>> letters_in1 = [Letter('g', 1), Letter('s', 1), Letter('e', 1), Letter('o', 2)]
    >>> out1 = build_tree(letters_in1)
    >>> out1.freq
    5
    >>> out1.left.freq
    2
    >>> out1.left.left
    g:1
    >>> out1.left.right
    s:1
    >>> out1.right.freq
    3
    >>> out1.right.left
    e:1
    >>> out1.right.right
    o:2
    >>> letters_in2 = [Letter('a', 1), Letter('b', 1)]
    >>> out2 = build_tree(letters_in2)
    >>> out2.freq
    2
    >>> out2.left
    a:1
    >>> out2.right
    b:1
    """
    response: list[Letter | TreeNode] = list(letters)
    while len(response) > 1:
        left = response.pop(0)
        right = response.pop(0)
        total_freq = left.freq + right.freq
        node = TreeNode(total_freq, left, right)
        response.append(node)
        response.sort(key=lambda x: x.freq)
    return response[0]


def traverse_tree(root: Letter | TreeNode, bitstring: str = "") -> list[Letter]:
    """
    Recursively traverse the Huffman Tree to set each
    Letter's bitstring dictionary, and return the list of Letters
    >>> root_in1 = build_tree(parse_string("goose"))
    >>> out1 = traverse_tree(root_in1, "")
    >>> out1
    [g:1, s:1, e:1, o:2]
    >>> out1[0].bitstring['g']
    '00'
    >>> out1[1].bitstring['s']
    '01'
    >>> out1[2].bitstring['e']
    '10'
    >>> out1[3].bitstring['o']
    '11'
    >>> root_in2 = build_tree(parse_string("This is a test..."))
    >>> out2 = traverse_tree(root_in2)
    >>> out2
    [.:3, i:2, t:2, T:1, h:1, a:1, e:1, s:3,  :3]
    >>> out2[0].bitstring['.']
    '00'
    >>> out2[4].bitstring['h']
    '1001'
    """
    if isinstance(root, Letter):
        root.bitstring[root.letter] = bitstring
        return [root]
    treenode: TreeNode = root
    letters = []
    letters += traverse_tree(treenode.left, bitstring + "0")
    letters += traverse_tree(treenode.right, bitstring + "1")
    return letters


def huffman_string(string: str, *, sep: str = " ") -> str:
    """
    Return huffman coded string, with
    each bitstring separated by sep parameter
    >>> huffman_string("goose")
    '00 11 11 01 10'
    >>> huffman_string("This is a test...", sep="")
    '1000100101011011101011011110101110111011110011000000'
    """
    letters_list = parse_string(string)
    root = build_tree(letters_list)
    letter_bitstrings = {
        k: v for letter in traverse_tree(root) for k, v in letter.bitstring.items()
    }
    return sep.join(letter_bitstrings[char] for char in string)


def huffman(
    file_path: str, *, sep: str = " ", output_file: SupportsWrite[str] | None = None
) -> None:
    """
    Parse the file, Huffman Code it and print the result
    to the given output_file, with each bitstring
    separated by sep parameter
    """
    letters_list = parse_file(file_path)
    root = build_tree(letters_list)
    letter_bitstrings = {
        k: v for letter in traverse_tree(root) for k, v in letter.bitstring.items()
    }
    print(f"Huffman Coding of {file_path}:", file=output_file)
    with open(file_path) as input_file:
        while char := input_file.read(1):
            print(letter_bitstrings[char], end=sep, file=output_file)
    print(file=output_file)


if __name__ == "__main__":
    if len(sys.argv) < 2:
        # if no file path given, test module
        doctest.testmod()
    else:
        # pass the file path to the huffman function
        huffman(sys.argv[1])
