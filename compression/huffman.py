from __future__ import annotations

import sys


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


def parse_file(file_path: str) -> list[Letter]:
    """
    Read the file and build a dict of all letters and their
    frequencies, then convert the dict into a list of Letters.

    >>> file_path = 'file_to_read.txt'
    >>> print(open(file_path, 'r').read()) # showing content of file
    This is the text contained in the file
    >>> parse_file(file_path)
    [T:1, x:1, c:1, o:1, a:1, d:1, f:1, l:1, s:2, h:3, n:3, i:5, t:5, e:5,  :7]

    """
    chars: dict[str, int] = {}
    with open(file_path) as f:
        while True:
            c = f.read(1)
            if not c:
                break
            chars[c] = chars[c] + 1 if c in chars else 1
    return sorted((Letter(c, f) for c, f in chars.items()), key=lambda x: x.freq)


def build_tree(letters: list[Letter]) -> Letter | TreeNode:
    """
    Run through the list of Letters and build the min heap
    for the Huffman Tree.

    # >>> result_from_parse_file_func = parse_file('file_to_read.txt')
    # >>> result_from_parse_file_func
    # [T:1, x:1, c:1, o:1, a:1, d:1, f:1, l:1, s:2, h:3, n:3, i:5, t:5, e:5,  :7]
    # >>> build_tree(result_from_parse_file_func)
    # <__main__.TreeNode object at 0x7fb08adff810>

    """
    response: list[Letter | TreeNode] = letters  # type: ignore
    while len(response) > 1:
        left = response.pop(0)
        right = response.pop(0)
        total_freq = left.freq + right.freq
        node = TreeNode(total_freq, left, right)
        response.append(node)
        response.sort(key=lambda x: x.freq)
    return response[0]


def traverse_tree(root: Letter | TreeNode, bitstring: str) -> list[Letter]:
    """
    Recursively traverse the Huffman Tree to set each
    Letter's bitstring dictionary, and return the list of Letters

    # >>> result_from_parse_file_func = parse_file('file_to_read.txt')
    # >>> result_from_build_tree_func = build_tree(result_from_parse_file_func)
    # >>> result_from_build_tree_func
    # <huffman.TreeNode object at 0x10c0cf8c0>
    # >>> traverse_tree(result_from_build_tree_func, "")
    # [n:3, s:2, T:1, x:1, c:1, o:1, a:1, d:1, i:5, t:5, e:5, f:1, l:1, h:3,  :7]

    """
    if isinstance(root, Letter):
        root.bitstring[root.letter] = bitstring
        return [root]
    treenode: TreeNode = root  # type: ignore
    letters = []
    letters += traverse_tree(treenode.left, bitstring + "0")
    letters += traverse_tree(treenode.right, bitstring + "1")
    return letters


def huffman(file_path: str) -> None:
    """
    Parse the file, build the tree, then run through the file
    again, using the letters dictionary to find and print out the
    bitstring for each letter.

    # >>> file_path = 'file_to_read.txt'
    # >>> print(open(file_path, 'r').read())
    # This is the text contained in the file

    ### huffman algorithm returns dynamic encoding depending on how
    ### the 0s and 1s are assigned

    # >>> huffman(file_path)
    # Huffman Coding  of file_to_read.txt:
    # 00110 1101 011 0010 111 011 0010 111 100 1101 101 111 100 101 00111 \
    # 100 111 01000 01001 000 100 01010 011 000 101 01011 111 011 000 111 \
    # 100 1101 101 111 11000 011 11001 101
    # None

    """
    letters_list = parse_file(file_path)
    root = build_tree(letters_list)
    letters = {
        k: v for letter in traverse_tree(root, "") for k, v in letter.bitstring.items()
    }
    print(f"Huffman Coding  of {file_path}: ")
    with open(file_path) as f:
        while True:
            c = f.read(1)
            if not c:
                break
            print(letters[c], end=" ")
    print()


if __name__ == "__main__":
    # pass the file path to the huffman function
    huffman(sys.argv[0])
